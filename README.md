# dwain-coverage-data
Weekly PFF tier2 coverage splits (2026) feeding the "PFF Man Zone RB Eff 2026 + Single-High Two-High" Google Sheet.
Built Mon/Tue 09:15 CT by `nfl-sim/scripts/dwain_weekly_refresh.py`; a claude.ai routine writes the sheet at 10:00 CT.
- `t2_data.csv` — one row per player_id, 83 columns (→ tab `T2 Data` A:CF)
- `t2_def.csv` — one row per defense in Dwain's team codes, 23 rate columns + next-week opponent (→ tab `T2 Def` A:X, DEF Cov Averages!B)
- `meta.json` — weeks included, opponent week, build time
