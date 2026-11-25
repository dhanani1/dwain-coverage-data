"""Stage a pinned release and publish the score and forecast together."""

import argparse
import csv
import json
import math
from pathlib import Path


SCORE_ID = 777013
FORECAST_ID = 777012
SCORE_NUMERIC = {0, 6, 7, 9, 10, 11, 12, 13}


def read_table(path, width):
    with path.open(newline="", encoding="utf-8") as source:
        rows = list(csv.reader(source))
    if rows == [[]]:
        return []
    if any(len(row) != width for row in rows):
        raise ValueError(f"{path.name} must have {width} columns on every row")
    return rows


def build_tables(source):
    meta = json.loads((source / "meta.json").read_text())
    score = read_table(source / "t2_fp.csv", 17)
    forecast = read_table(source / "t2_matchup.csv", 43)
    opponent_header = f"Wk{meta['opp_week']} Opp"
    if len(score) < 2 or score[0][:5] != ["player_id", "Player", "Pos", "Team", opponent_header]:
        raise ValueError("Matchup Score is empty or has the wrong opponent week")
    if forecast and forecast[0][:3] != ["Offense", "Defense", "QB"]:
        raise ValueError("Unexpected Matchup Forecast header")
    if meta["forecast"]["active"]:
        if meta["forecast"]["week"] != meta["opp_week"] or len(forecast) < 2:
            raise ValueError("Active Matchup Forecast is empty or has the wrong week")
        matchups = {team: (opponent, qb) for team, opponent, qb, *_ in forecast[1:]}
        if len(matchups) != len(forecast) - 1:
            raise ValueError("Matchup Forecast repeats an offense")
        for _, player, position, team, opponent, *_ in score[1:]:
            matchup = matchups.get(team)
            if not matchup or matchup[0] != opponent:
                raise ValueError(f"Score and forecast disagree on {team}'s opponent")
            if position == "QB" and matchup[1] != player:
                raise ValueError(f"Score and forecast disagree on {team}'s quarterback")
    elif len(forecast) > 1:
        raise ValueError("Inactive Matchup Forecast still has data rows")
    return score, forecast


def cell(value, numeric):
    if not value or not numeric:
        return value
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"Invalid numeric cell: {value!r}")
    return number


def table_requests(sheet_id, width, grid_rows, row_count, stage_id, stage_column):
    if grid_rows < 8:
        raise ValueError(f"Unexpected row count for sheet {sheet_id}")
    if row_count > grid_rows:
        start = grid_rows - 1
        yield {"insertDimension": {
            "range": {"sheetId": sheet_id, "dimension": "ROWS", "startIndex": start,
                      "endIndex": start + row_count - grid_rows},
            "inheritFromBefore": True,
        }}
    if row_count:
        yield {"copyPaste": {
            "source": {"sheetId": stage_id, "startRowIndex": 0, "endRowIndex": row_count,
                       "startColumnIndex": stage_column, "endColumnIndex": stage_column + width},
            "destination": {"sheetId": sheet_id, "startRowIndex": 0, "endRowIndex": row_count,
                            "startColumnIndex": 0, "endColumnIndex": width},
            "pasteType": "PASTE_VALUES",
        }}
    first_unused = max(row_count, 1)
    if first_unused < grid_rows:
        yield {"repeatCell": {
            "range": {"sheetId": sheet_id, "startRowIndex": first_unused,
                      "endRowIndex": grid_rows, "startColumnIndex": 0, "endColumnIndex": width},
            "cell": {}, "fields": "userEnteredValue",
        }}


def build_batch(score, forecast, score_grid_rows, forecast_grid_rows, stage_id):
    if stage_id in {SCORE_ID, FORECAST_ID}:
        raise ValueError("A staging tab must be distinct from both destination tabs")
    return [
        *table_requests(SCORE_ID, 17, score_grid_rows, len(score), stage_id, 0),
        *table_requests(FORECAST_ID, 43, forecast_grid_rows, len(forecast), stage_id, 17),
        {"deleteSheet": {"sheetId": stage_id}},
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check", help="Validate the source and print the two table row counts")
    stage = commands.add_parser("stage", help="Return typed values for a bounded staging write")
    stage.add_argument("table", choices=["score", "forecast"])
    stage.add_argument("first_row", type=int)
    stage.add_argument("last_row", type=int)
    publish = commands.add_parser("publish", help="Build an atomic values-only publish request")
    publish.add_argument("stage_id", type=int)
    publish.add_argument("score_grid_rows", type=int)
    publish.add_argument("forecast_grid_rows", type=int)
    args = parser.parse_args()
    try:
        score, forecast = build_tables(args.source)
        if args.command == "check":
            result = {"score_rows": len(score), "forecast_rows": len(forecast)}
        elif args.command == "stage":
            table, numeric = (score, SCORE_NUMERIC) if args.table == "score" else (forecast, range(3, 43))
            if not 1 <= args.first_row <= args.last_row <= len(table):
                raise ValueError("Staging rows must be within the selected table")
            result = [[cell(value, i > 0 and col in numeric) for col, value in enumerate(table[i])]
                      for i in range(args.first_row - 1, args.last_row)]
        else:
            result = build_batch(score, forecast, args.score_grid_rows, args.forecast_grid_rows, args.stage_id)
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Matchup sheet update held: {error}\n")
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()
