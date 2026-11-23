# Frozen receiving-under rule (MSH): forward report

Written 2026-11-23 14:21 ET. Rule frozen 2026-11-13. Prices are the last pre-kickoff DraftKings snapshot. Uncertainty is clustered by game.

- Week 10: all games and stats verified (28 of 28 teams); stats last ingested 2026-11-17 08:58 ET
- Week 11: waiting on CIN, WAS, 2026_11_CIN_WAS final (24 of 26 teams); stats last ingested 2026-11-23 10:21 ET
- Week 12: waiting on ARI, ATL, BAL, BUF, CAR, CHI, CIN, CLE, DAL, DEN, DET, GB, HOU, IND, JAX, KC, LA, LAC, LV, MIA, MIN, NE, NO, NYG, NYJ, PHI, PIT, SEA, SF, TB, TEN, WAS, 2026_12_ATL_MIN final, 2026_12_BAL_HOU final, 2026_12_CAR_TB final, 2026_12_CHI_DET final, 2026_12_DEN_PIT final, 2026_12_GB_LA final, 2026_12_KC_BUF final, 2026_12_LV_CLE final, 2026_12_NE_LAC final, 2026_12_NO_CIN final, 2026_12_NYG_IND final, 2026_12_NYJ_MIA final, 2026_12_PHI_DAL final, 2026_12_SEA_SF final, 2026_12_TEN_JAX final, 2026_12_WAS_ARI final (0 of 32 teams)

```
MSH excluded 1 mixed-game snapshot(s) from grading: [(11, '2026-11-16 09:33')]
MSH excluded 6 snapshot(s) awaiting approved model and training cutoff evidence
FORWARD (weeks [np.int64(10), np.int64(11), np.int64(12)]) | fired player-markets logged 154 | never had a DraftKings line 66 | settled bets 50 over 16 games
   pending prices by outcome: 18 without verified finals, 14 without a matched official result
   by week: {10: {'bets': 24, 'roi': -0.157}, 11: {'bets': 26, 'roi': -0.031}} | quote age at kickoff, hours: median 3.6, max 16.2 | model cutoffs used: ['2026 wk 9']
   net ROI -9.1% | hit 48.0% | game-clustered 90% -35.0% to +20.0%, 95% -39.6% to +26.4% | P(ROI >= 10%) 14% | control (all other logged DK receiving unders): n 448, ROI +3.0%
   health comparison: 480/498 lines with all fields
   health beyond price only: coef +0.107 (se 0.117, p 0.359), n 480, games 25
   health beyond price + role (his share of the team's posted lines): coef +0.109 (se 0.117, p 0.351), n 480, games 25
```
