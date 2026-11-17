PART 2 OF 5: T2 Extra and T2 ManZone

Tabs you own: 'T2 Extra' and 'T2 ManZone'. After writing each, read it back and compare the whole tab with its CSV in Python; rewrite any row that differs.

Step 1 and step 2 below apply to every part, but in step 2 check and extend ONLY the tabs this part writes.

STEPS
1. Read meta.json, build_status.json and all the CSVs with Bash/Read. Let N = opp_week, P = number of player rows in t2_data.csv (t2_fav, t2_extra and t2_align must have the same P and the same player_id order; if not, STOP and report).
2. Grid check: get_spreadsheet with fields ["sheets.properties"]; note each tab's current title and gridProperties.rowCount. Writes past rowCount FAIL, and step 12 of earlier runs trims every tab to its data, so EVERY tab you write usually needs rows added when it grows: whenever (rows to write incl. header) > rowCount, call insert_dimension (ROWS, startIndex = rowCount-1, endIndex = startIndex + (needed - rowCount), inheritFromBefore true) on that tab first (rowCount is always >= 8, so this never touches rows 1-8).
6. T2 Extra: update_values from 'T2 Extra'!A1 with header + all rows (35 values each, chunks of 100 rows at correct starting rows). Then clear 'T2 Extra'!A{P+2}:AI2000.
6e. T2 ManZone: update_values from 'T2 ManZone'!A1 with header + all rows of t2_manzone.csv (80 values each, chunks of 40 rows at correct starting rows; numbers as numbers, blank CSV cells as empty strings, player / position / team_name as text). Check each row has exactly 80 values before writing. Then clear 'T2 ManZone'!A{M+2}:CB2000.
(In every 'then clear' above and below, a clear range that starts past the tab's rowCount is simply skipped.)

FINAL MESSAGE: first line 'PART 2 COMPLETE' or 'PART 2 NOT COMPLETE'. Then one line per tab in this part: written (rows) / already current / NOT DONE with the reason. Then weeks included, opp week, any rows inserted or repaired, and anything odd. If the part is not complete, send a push notification saying which tabs are not done.
