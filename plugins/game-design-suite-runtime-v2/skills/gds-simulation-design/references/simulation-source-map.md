# Simulation Source Map

Public references used to shape the generic simulation workflow. These sources are methodology references, not project truth.

| Source | Type | Useful pattern | Boundary |
|---|---|---|---|
| GDC 2019, David Morris, "Beyond Spreadsheets: Building a Metagame Simulator for Balance and Prototyping" — https://www.gdcvault.com/play/1026489/Beyond-Spreadsheets-Building-a-Metagame | Industry talk | Full-system metagame simulation, designer-accessible pre-analytics, embracing interaction complexity | Does not make simulator output equivalent to player evidence |
| GameDeveloper, "Breaking down the metagame design in a mobile RPG" — https://www.gamedeveloper.com/design/breaking-down-the-metagame-design-in-a-mobile-rpg | Production case | Separate simulation engine from UI; simulate long-term state progression; automated agents at scale | Project-specific implementation details are examples only |
| Beau & Bakkes, "Automated Game Balancing of Asymmetric Video Games" (IEEE CIG 2016) — https://doi.org/10.1109/CIG.2016.7860432 | Academic | Monte Carlo can identify major imbalance contributors and support iterative parameter adjustment | Fairness definition and agent behavior depend on game domain |
| Isaksen & Nealen, "Comparing Player Skill, Game Variants, and Learning Rates Using Survival Analysis" (AIIDE 2015) — https://doi.org/10.1609/aiide.v11i5.12846 | Academic | Model multiple player skill/learning assumptions; analyze distributions and survival/hazard, not only means | Simplified player models remain assumptions |
| Uriarte & Ontañón, "Combat Models for RTS Games" — https://arxiv.org/abs/1605.05305 | Academic | Forward models can approximate combat and can be compared against replay outcomes | RTS combat abstraction is not directly portable to other genres |
| Ubisoft, data science overview — https://news.ubisoft.com/en-us/article/5eZ3g9FHSlIkSIkp12lyVL/shaping-the-future-of-games-how-machine-learning-and-data-science-will-help-transform-the-industry | Industry | Player-like bots and automated testing can anticipate balance/performance issues | Automation complements, not replaces, human validation |
| IEEE SCCC 2025, "Evaluating the Play Quality of a Game-balancing Simulation using Monte Carlo algorithm" — https://doi.org/10.1109/SCCC67219.2025.11420422 | Academic | Simulation count interacts with randomness and agent decision quality; more runs alone do not guarantee useful decisions | One study/domain; do not adopt a fixed universal run count |

## Source policy

- Prefer production runtime and project tests as Ground Truth for current-game rules.
- Use academic/industry references for methodology and failure modes.
- Do not copy another game's formulas, sample counts, or player models as defaults.
- Every external model imported into a project remains `candidate` until validated against that project.
