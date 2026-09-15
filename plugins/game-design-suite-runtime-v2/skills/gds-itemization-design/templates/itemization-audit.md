# Itemization Audit Template

Use this template for an existing or proposed equipment/itemization system.

## 1. Scope

- Game / mode:
- Item system:
- Slots:
- Rarity/quality:
- Item level / enhancement:
- Randomness model:
- Set/unique effects:
- Acquisition sources:
- Salvage/crafting:
- Current player phase:
- Evidence available:

## 2. Itemization Job

What should the system accomplish?

- Progression:
- Build expression:
- Loot excitement:
- Encounter adaptation:
- Collection:
- Economy:
- Live/seasonal refresh:

## 3. Slot Matrix

| Slot | Intended job | Base budget | Main-stat options | Affix budget | Unique/set access | Replacement cadence | Risk |
|---|---|---:|---|---:|---|---|---|

## 4. Quality Ladder

| Quality | Base budget | Affix count | Affix tier | Roll range | Enhance cap | Unique access | Acquisition rate |
|---|---:|---:|---|---|---:|---|---|

## 5. Attribute Budget

Benchmark:

- character/build:
- progression state:
- enemy/content:
- time window:
- target count:
- team assumptions:

| Stat | Test delta | Metric delta | Marginal value | Budget unit | Breakpoint/cap | Evidence |
|---|---:|---:|---:|---:|---|---|

## 6. Affix Pool

| Affix | Eligible slots | Tier | Min-Max | Weight | Exclusion group | Intended builds | Dead-roll risk |
|---|---|---|---|---:|---|---|---|

## 7. Random Roll Model

- initial affix count:
- roll model:
- weight model:
- duplicate rule:
- enhancement roll rule:
- reroll/reforge:
- target/lock options:
- pity/floor:

Required outputs when random:

- usable rate:
- good-item rate:
- near-BiS rate:
- exact-BiS rate:
- P50/P90/P95 target time:
- bad-luck tail:

## 8. Enhancement

| Level/Node | Power delta | Cost delta | Affix event | Cumulative power | Replacement friction |
|---|---:|---:|---|---:|---|

Inheritance/refund rule:

## 9. Set / Unique Effects

| Item/Set | Raw effect | Trigger/Uptime | Effective value | Slot lock cost | Build users | BiS risk |
|---|---|---|---:|---:|---|---|

## 10. Acquisition Funnel

`Drop -> Slot -> Set/Family -> Main Stat -> Usable Affixes -> Roll Quality -> Actual Upgrade`

| Layer | Probability / rule | Evidence | Notes |
|---|---:|---|---|

## 11. Replacement / Graduation

- Time-to-first-usable:
- Time-to-upgrade:
- median item lifetime:
- P50 graduation:
- P90 graduation:
- P95 graduation:
- exact-BiS target (if relevant):

## 12. Salvage / Duplicate / Crafting

- sell:
- salvage:
- feed:
- crafting:
- reroll fuel:
- selector/target craft:
- duplicate value:
- inflation risk:

## 13. Build Ecology

Matrices to inspect:

- Character × Item
- Build × Item
- Item × Encounter
- Slot Competition
- Set / Unique Synergy

Metrics:

- Top-N item concentration:
- BiS lock rate:
- viable alternatives:
- signature dependency:
- build diversity:
- power-creep trend:

## 14. Findings

For every independent finding:

- Header / responsible Skill:
- Result:
- Evidence:
- Severity:
- Current value/rule:
- Proposed value/rule:
- Reason:
- Validation:
- Evidence state:

## 15. Final Decision

Classify each issue:

- keep;
- tune value;
- restructure itemization;
- change affix pool;
- change acquisition;
- change enhancement;
- change salvage/crafting;
- investigate code/config;
- simulate;
- telemetry/playtest required.