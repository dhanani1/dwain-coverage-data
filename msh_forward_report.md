# Frozen receiving-under rule (MSH): forward report

Written 2026-11-17 08:58 ET by the scheduled build. Rule frozen 2026-11-13; prices = last pre-kickoff DraftKings snapshot; uncertainty clustered by game.

- Week 10: ALL stats landed (28 of 28 teams); stats last ingested 2026-11-17 08:58 ET
- Week 11: waiting on ARI, BAL, BUF, CAR, CHI, CIN, DAL, DEN, DET, HOU, IND, JAX, KC, LAC, LV, MIA, MIN, NO, NYG, NYJ, PHI, PIT, SF, TB, TEN, WAS (0 of 26 teams)

```
MSH excluded 1 mixed-game snapshot(s) from grading: [(11, '2026-11-16 09:33')]
FORWARD (weeks [np.int64(10), np.int64(11)]) | fired player-markets logged 76 | never had a DraftKings line 42 | settled bets 24 over 8 games
   by week: {10: {'bets': 24, 'roi': -0.157}} | quote age at kickoff, hours: median 2.1, max 16.2 | model cutoffs used: ['2026 wk 9']
   net ROI -15.7% | hit 45.8% | game-clustered 90% -51.8% to +23.0%, 95% -58.1% to +30.0% | P(ROI >= 10%) 13% | control (all other logged DK receiving unders): n 224, ROI +5.4%
   health beyond market props and role: needs 300+ settled lines over 20+ games on forward weeks; have 248 lines, 13 games
```
