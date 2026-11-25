"""Select a committed, coherent source for a Matchup Score sheet refresh."""

import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import subprocess


def select_snapshot(repo, ref, now):
    def git(*args):
        return subprocess.check_output(
            ["git", "-C", str(repo), *args], text=True, timeout=30
        ).strip()

    def read_json(commit, name):
        return json.loads(git("show", f"{commit}:{name}"))

    def timestamp(value):
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None:
            raise ValueError("Build timestamp is missing its time zone")
        return result

    revision = git("rev-parse", "--verify", f"{ref}^{{commit}}")
    latest = read_json(revision, "build_status.json")
    using_fallback = latest["ok"] is False
    history = git(
        "log", "--first-parent", "--format=%H", revision, "--", "build_status.json"
    ).splitlines()
    for data_revision in history if using_fallback else history[:1]:
        success = read_json(data_revision, "build_status.json")
        if success["ok"] is True:
            break
    else:
        raise ValueError("No successful build found in this revision's history")

    changes = git("diff", "--name-only", data_revision, revision, "--").splitlines()
    data_changes = [
        name for name in changes
        if name not in {"build_status.json", "README.md"} and not name.startswith("routine/")
    ]
    if data_changes:
        raise ValueError("Data changed after the last successful build: " + ", ".join(data_changes))

    meta = read_json(data_revision, "meta.json")
    built = timestamp(meta["built_at_utc"])
    success_time = timestamp(success["at_utc"])
    week = int(meta["opp_week"])
    if not (built <= success_time <= now) or now - built > timedelta(hours=30):
        raise ValueError("Last successful build is too old or has inconsistent timestamps")
    if success.get("week", week) != week:
        raise ValueError("Success status and data have different matchup weeks")
    if using_fallback and not (success_time < timestamp(latest["at_utc"]) <= now):
        raise ValueError("Failure was not recorded after the selected successful release")

    return {
        "mode": "last_good" if using_fallback else "current",
        "source_revision": data_revision,
        "checked_revision": revision,
        "week": week,
        "built_at_utc": meta["built_at_utc"],
        "failure_at_utc": latest["at_utc"] if using_fallback else None,
        "error": latest.get("error") if using_fallback else None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ref", nargs="?", default="HEAD")
    args = parser.parse_args()
    try:
        result = select_snapshot(Path(__file__).resolve().parents[1], args.ref, datetime.now(timezone.utc))
    except (KeyError, TypeError, ValueError, subprocess.SubprocessError) as error:
        parser.exit(1, f"Sheet refresh held: {error}\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
