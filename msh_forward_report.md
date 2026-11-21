# Frozen receiving-under rule (MSH): forward report

Written 2026-11-21 13:12 ET by the scheduled build. Rule frozen 2026-11-13; prices = last pre-kickoff DraftKings snapshot; uncertainty clustered by game.

- Week 10: ALL stats landed (28 of 28 teams); stats last ingested 2026-11-17 08:58 ET
- Week 11: waiting on ARI, BAL, BUF, CAR, CHI, CIN, DAL, DEN, DET, JAX, KC, LAC, LV, MIA, MIN, NO, NYG, NYJ, PHI, PIT, SF, TB, TEN, WAS (2 of 26 teams); stats last ingested 2026-11-20 10:19 ET

```
MSH excluded 1 mixed-game snapshot(s) from grading: [(11, '2026-11-16 09:33')]
MSH excluded 6 snapshot(s) awaiting approved model and training cutoff evidence
FORWARD (weeks [np.int64(10), np.int64(11)]) | fired player-markets logged 130 | never had a DraftKings line 46 | settled bets 26 over 9 games
   by week: {10: {'bets': 24, 'roi': -0.157}, 11: {'bets': 2, 'roi': -1.0}} | quote age at kickoff, hours: median 2.1, max 16.2 | model cutoffs used: ['2026 wk 9']
   net ROI -22.1% | hit 42.3% | game-clustered 90% -57.8% to +14.7%, 95% -64.9% to +21.0% | P(ROI >= 10%) 8% | control (all other logged DK receiving unders): n 240, ROI +8.7%
   health beyond market props and role: needs 300+ settled lines over 20+ games on forward weeks; have 266 lines, 14 games
```
