# Frozen receiving-under rule (MSH): forward report

Written 2026-11-15 18:17 ET by the scheduled build. Rule frozen 2026-11-13; prices = last pre-kickoff DraftKings snapshot; uncertainty clustered by game.

- Week 10: waiting on ARI, BAL, CIN, DAL, LA, LAC, LV, PIT, SEA, SF (18 of 28 teams); stats last ingested 2026-11-15 18:17 ET

```
FORWARD (weeks [np.int64(10)]) | fired player-markets logged 60 | never had a DraftKings line 26 | settled bets 18 over 6 games
   by week: {10: {'bets': 18, 'roi': -0.265}} | quote age at kickoff, hours: median 2.1, max 16.2 | model cutoffs used: ['2026 wk 9']
   net ROI -26.5% | hit 38.9% | game-clustered 90% -69.7% to +21.5%, 95% -77.2% to +33.1% | P(ROI >= 10%) 10% | control (all other logged DK receiving unders): n 130, ROI +7.7%
   health beyond market props and role: needs 300+ settled lines over 20+ games on forward weeks; have 148 lines, 8 games
```
