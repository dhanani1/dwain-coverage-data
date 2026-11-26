# Frozen receiving-under rule (MSH): forward report

Written 2026-11-26 10:18 ET. Rule frozen 2026-11-13. Prices are the last pre-kickoff DraftKings snapshot. Uncertainty is clustered by game.

- Week 10: all games and stats verified (28 of 28 teams); stats last ingested 2026-11-17 08:58 ET
- Week 11: all games and stats verified (26 of 26 teams); stats last ingested 2026-11-25 14:25 ET
- Week 12: waiting on ARI, ATL, BAL, BUF, CAR, CHI, CIN, CLE, DAL, DEN, DET, HOU, IND, JAX, KC, LAC, LV, MIA, MIN, NE, NO, NYG, NYJ, PHI, PIT, SEA, SF, TB, TEN, WAS, 2026_12_ATL_MIN final, 2026_12_BAL_HOU final, 2026_12_CAR_TB final, 2026_12_CHI_DET final, 2026_12_DEN_PIT final, 2026_12_KC_BUF final, 2026_12_LV_CLE final, 2026_12_NE_LAC final, 2026_12_NO_CIN final, 2026_12_NYG_IND final, 2026_12_NYJ_MIA final, 2026_12_PHI_DAL final, 2026_12_SEA_SF final, 2026_12_TEN_JAX final, 2026_12_WAS_ARI final (2 of 32 teams); stats last ingested 2026-11-26 10:18 ET

```
MSH excluded 1 mixed-game snapshot(s) from grading: [(11, '2026-11-16 09:33')]
MSH excluded 6 snapshot(s) awaiting approved model and training cutoff evidence
FORWARD (weeks [np.int64(10), np.int64(11), np.int64(12)]) | fired player-markets logged 182 | never had a DraftKings line 76 | settled bets 50 over 16 games
   pending prices by outcome: 0 without verified finals, 14 without a matched official result
   by week: {10: {'bets': 24, 'roi': -0.157}, 11: {'bets': 26, 'roi': -0.031}} | quote age at kickoff, hours: median 3.6, max 16.2 | model cutoffs used: ['2026 wk 9']
   net ROI -9.1% | hit 48.0% | game-clustered 90% -35.0% to +20.0%, 95% -39.6% to +26.4% | P(ROI >= 10%) 14% | control (all other logged DK receiving unders): n 466, ROI +2.5%
   health comparison: 498/516 lines with all fields
   health beyond price only: coef +0.103 (se 0.114, p 0.370), n 498, games 26
   health beyond price + role (his share of the team's posted lines): coef +0.105 (se 0.115, p 0.360), n 498, games 26
```
