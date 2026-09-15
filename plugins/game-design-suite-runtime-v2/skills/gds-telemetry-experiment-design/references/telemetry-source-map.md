# Telemetry Source Map

Public methodology references. They define reusable patterns, not project-specific requirements.

| Source | Type | Useful pattern | Boundary |
|---|---|---|---|
| Microsoft PlayFab Experiments overview — https://learn.microsoft.com/en-us/gaming/playfab/live-service-management/game-configuration/experiments/ | Official platform docs | Controlled random assignment, variants, concurrent experiments, scorecards, statistical trustworthiness | Platform implementation is optional; methodology is portable |
| Microsoft PlayFab experiment best practices — https://learn.microsoft.com/en-us/xbox/playfab/live-service-management/game-configuration/experiments/experimentation-keys | Official platform docs | Start from a hypothesis, account for duration/seasonality, use statistical significance and operational planning | p-value threshold is not a universal design decision rule |
| Microsoft PlayFab experiment analysis — https://learn.microsoft.com/en-us/gaming/playfab/live-service-management/game-configuration/experiments/analyze-experiments | Official platform docs | Inspect player count, average, delta, standard deviation, significance and Sample Ratio Mismatch (SRM) | Specific scorecard fields depend on platform |
| Microsoft PlayFab Telemetry overview — https://learn.microsoft.com/en-us/xbox/playfab/data-analytics/ingest-data/telemetry-overview | Official platform docs | Separate telemetry pipeline for behavior/performance events and downstream analysis | Product API details are not part of the generic skill |
| Riot Games, "Get Data Informed" — https://www.riotgames.com/en/work-with-us/disciplines/insights/get-data-informed-on-the-insights-blog | Industry case | Win rate needs context such as mastery/learning curves; analytics can prevent premature over-correction | Historical game-specific numbers are not universal thresholds |
| Riot 2XKO Live Balance Philosophy — https://2xko.riotgames.com/en-us/news/dev/2xko-live-balance-philosophy/ | Industry case | Segment by skill, combine pick/win rate, matchups, team composition, move usage and qualitative feedback | Fighting-game thresholds are examples only |
| Chung, "Guidelines for the Design and Implementation of Game Telemetry for Serious Games Analytics" (2015) — DOI: 10.1007/978-3-319-05834-4_3 | Academic | Record behavior rather than inference, preserve context, use fine-enough event grain | Serious-game assessment context differs from entertainment games |
| Unity Game Overrides / Analytics docs — https://docs.unity.com/en-us/services/solutions/use-cases-project | Official platform docs | A/B tests can tune progression/balance variables through targeted audiences | Unity service architecture is optional |

## Source policy

- Project telemetry schema is determined by actual decisions, code authority, cost, privacy and analysis needs.
- Public examples inform method, not mandatory event names or KPI thresholds.
- Observational data supports diagnosis; causal claims require stronger design or controlled evidence.
