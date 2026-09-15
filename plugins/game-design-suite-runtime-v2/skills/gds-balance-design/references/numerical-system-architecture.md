# Numerical System Architecture

## Purpose

Use this reference when designing or auditing the **numerical backbone of a whole game**, not just one skill coefficient or one economy reward.

The goal is to translate intended player experience into measurable behavior, models, parameters, and validation loops without importing another game's values as universal truth.

Core chain:

`Experience Target -> Observable Behavior -> Metric -> Numerical Model -> Parameters -> Validation`

Do not reverse this into `Parameter -> justification after the fact`.

---

## 1. Numerical Architecture Layers

A useful cross-genre decomposition is:

1. **Macro Pacing / Timeline** — the long-term time structure: sessions, chapters, days, seasons, account progression, expected time to goals.
2. **Economy** — resource sources, sinks, stock, conversion, prices, scarcity, reward cadence.
3. **Progression** — level, rank, equipment, stars, unlocks, breakthroughs, skill growth, capability growth.
4. **Combat / Moment-to-Moment** — damage, healing, defense, timing, speed, resource cycles, hit/resist, control, gauges, encounter strength.

This is a modeling lens, not a mandatory feature list.

Do **not** force every project to contain a "social module" or any fixed MMORPG-era structure. A roguelite, action game, puzzle game, idle game, card battler, tactics game, or simulation game may use different concrete systems while still needing some combination of macro pacing, economy, progression, and moment-to-moment numerical rules.

Commercialization, live operations, collection, social, crafting, housing, or PvP may be additional layers or constraints where relevant.

---

## 2. Experience Anchor First

Before choosing numbers, define the intended player-visible outcome.

Examples:

- Boss should usually survive 20-30 seconds against the target build.
- A defensive upgrade should let the player survive roughly one additional enemy action in the benchmark encounter.
- A level-up should be perceptible but should not invalidate the next content tier.
- A weekly resource should create one meaningful purchase decision, not a forced tax.
- A speed increase should matter only if it changes realized actions/casts inside actual combat windows.

Then convert the target into measurable quantities:

| Experience target | Observable behavior | Metric examples |
|---|---|---|
| Fast combat | enemies die before combat stalls | TTK, actions-to-kill |
| Defensive value | player survives more meaningful events | TTD, EHP, enemy actions survived |
| Frequent growth | upgrades arrive and feel distinct | time-to-upgrade, power delta |
| Healthy scarcity | player chooses between competing uses | stock coverage, purchase interval |
| Build diversity | multiple strategies remain viable | usage, clear rate, opportunity cost |

The metric must represent the experience closely enough that optimizing the metric does not destroy the experience.

---

## 3. Long-Term vs Moment-to-Moment Numbers

Separate at least two scales:

### Long-term / progression-scale

- Level and breakthrough curves
- Account progression
- Equipment/stat budgets
- Reward and resource flow
- Collection and unlock cadence
- Content difficulty curve

### Moment-to-moment / combat-scale

- Damage and mitigation
- Action timing / cooldown / attack interval
- Crit, hit, resist, control
- Energy/resource generation and spending
- Healing/shielding
- Secondary gauges

They must connect, but should not be collapsed into one spreadsheet column called "power".

A healthy project checks:

`Power Curve <-> Cost Curve <-> Content Curve <-> Time Curve`

---

## 4. Benchmark Contract

Any value comparison requires a reproducible benchmark.

At minimum specify relevant items:

- progression state;
- equipment/build assumptions;
- skill levels;
- teammates or solo state;
- target/enemy stats;
- encounter length;
- target count;
- enemy behavior/attack frequency;
- resource starting state;
- random seed or random model when relevant.

A ratio or value derived under one benchmark is not automatically portable to another.

---

## 5. Attribute Value Anchor / Exchange Rate

It is useful to build a shared value language for attributes, but **fixed universal ratios are prohibited**.

Do not treat statements such as:

`ATK : DEF : HP = 1 : 1 : 10`

as universal truths.

Instead derive value under a benchmark.

### Recommended method

1. Choose a benchmark character/build/enemy/window.
2. Perturb one attribute by a small controlled amount.
3. Recompute the relevant outcome.
4. Measure marginal value.
5. Repeat across low/mid/high progression and different encounter classes.
6. Build an exchange-rate range, not a sacred constant.

Examples:

`Marginal DPS = ΔDPS / ΔATK`

`Marginal EHP = ΔEHP / ΔDEF`

`Marginal Survival = ΔExpectedEnemyActionsSurvived / ΔHP`

The correct comparison target may be DPS, EHP, TTK, TTD, realized actions, clear rate, or another metric depending on the design goal.

### Value-anchor warning

`Stat Budget != Effective Combat Value`

A budget is a production convenience. Realized value still depends on formula buckets, caps, thresholds, uptime, encounter context, team composition, and current build saturation.

---

## 6. Heuristic vs Universal Rule Guard

External design heuristics must be labeled before use.

Use one of:

- `example-heuristic`
- `project-candidate`
- `community-pattern`
- `validated-project-rule`
- `universal-math-identity`

Examples that are **not** universal rules by default:

- fixed ATK/DEF/HP ratios;
- fixed "readable number" ranges;
- fixed ideal crit rates;
- fixed pity counts;
- fixed acceptable win-rate bands;
- fixed speed breakpoints;
- fixed progression multipliers.

The Skill may learn the method behind them, but must re-derive project values.

---

## 7. Numerical Readability and Player Perception

Player-facing number presentation is part of numerical design, but do not hard-code one global magnitude range.

Check:

- whether changes are perceptible;
- whether the displayed precision is meaningful;
- whether number growth preserves comparison ability;
- whether K/M/B or localized large-number notation is needed;
- whether percentage presentation is clearer than raw numbers;
- whether very large numbers create meaningful fantasy or only visual inflation;
- whether UI can communicate important deltas and thresholds.

When using psychophysical ideas such as relative-change sensitivity, treat them as hypotheses to validate in the specific UI and game context rather than as a universal percentage threshold.

---

## 8. Probability, Random Rewards, and Pity

Never judge a random system only by the displayed single-pull probability.

Model where relevant:

- base probability;
- effective long-run probability;
- expected attempts;
- variance;
- P50/P90/P95 attempts/cost;
- no-success tail probability;
- hard pity;
- soft pity;
- guarantee/reset rules;
- pool depletion;
- duplicate conversion/value;
- free-currency flow and purchase interval.

A pity system changes the distribution and often changes the long-run effective acquisition rate.

Do not import a rule such as "all paid gacha should pity within 100-200 pulls". Derive the candidate from product price, free flow, target expected cost, worst-case commitment, duplicate value, pool cadence, legal/platform constraints, and desired player experience.

---

## 9. Business Constraints Are Constraints, Not the Sole Objective

Commercial targets can be legitimate production constraints, but they do not automatically override experience quality, fairness, economy semantics, retention health, or long-term content sustainability.

Use a multi-objective frame:

`Experience Target + Business Constraint + Economy Sustainability + Fairness Boundary + Production Reality`

Reject patterns such as:

- designing a mandatory progression tax only to hit spend targets;
- creating resource scarcity with no systemic meaning;
- destroying build viability to force replacement purchases;
- using short-term revenue to justify long-term economy collapse.

If monetization is not part of the user's confirmed project scope, do not invent it.

---

## 10. Template Transfer Guard

Successful external game templates can transfer **structure**, not automatically values.

Safe to transfer as patterns:

- modeling sequence;
- benchmark methodology;
- curve families;
- simulation workflow;
- reward architecture patterns;
- validation methods;
- metric definitions.

Unsafe to copy without re-derivation:

- exact growth rates;
- exact defense constants;
- exact stat conversion ratios;
- exact pity counts;
- exact shop prices;
- exact power gaps;
- exact monetization pacing;
- exact acceptable win-rate ranges.

Rule:

`Template Structure can transfer. Template Values require project re-validation.`

---

## 11. External Numerical Simulator Architecture

For production projects, prefer an external or isolated numerical model that can expose intermediate calculations rather than only final results.

Recommended layers:

`Project Inputs / Config`
`-> Normalized Variables`
`-> Formula Buckets`
`-> Timeline / Rotation / Event Model`
`-> Random Model`
`-> Output Metrics`
`-> Sensitivity / Boundary / Regression Tests`

A useful combat trace should be able to show, where relevant:

- base value;
- skill coefficient;
- crit block;
- damage bonus block;
- defense block;
- resistance block;
- vulnerability/reduction blocks;
- state/special modifiers;
- rounding/clamp;
- final result.

The simulator must not silently replace runtime truth. When code/runtime exists, perform parity checks with `formula-verification + code-verification`.

---

## 12. Whole-Project Numerical Deliverables

For a complete numerical architecture task, produce only the relevant subset of:

- Experience Targets;
- Numerical Architecture Map;
- Benchmark Contracts;
- Attribute/Stat Budget Model;
- Combat Formula Map;
- Progression Curves;
- Economy Flow Model;
- Content Difficulty Curve;
- Probability/Reward Distribution Model;
- External Simulator Plan;
- Sensitivity and Breakpoint Map;
- Validation Matrix;
- Evidence Status and Open Questions.

Do not generate every artifact by default when the user only asks for one subsystem.

---

## 13. Common Failure Modes

- **Parameter-first Design** — picks numbers before defining the experience target.
- **Universal Ratio Fallacy** — treats one project's attribute ratio as universal.
- **Successful Template Copying** — imports values because another product succeeded.
- **Revenue-first Override** — lets monetization targets erase experience/economy constraints.
- **Perception Hardcode** — turns a heuristic number range into a universal UX law.
- **Pity-by-Rule-of-Thumb** — selects pity counts from industry folklore rather than distribution and economy modeling.
- **Single Power Number** — collapses all combat/progression value into one opaque combat-power score.
- **Spreadsheet Truth** — assumes a spreadsheet model proves runtime behavior or player experience.
- **Cross-scale Leakage** — fixes a long-term progression problem with a local combat coefficient or vice versa.

---

## 14. Reference Use Policy

Community articles, public talks, competitor data, and theorycrafting are useful for discovering modeling patterns and counterexamples. They are not project source-of-truth.

For external references, preserve:

- source type;
- publication/update context when known;
- whether the claim is mathematical identity, observed product behavior, author heuristic, or opinion;
- which part is being transferred: method, structure, or candidate value.

If the source is inaccessible or its exact wording cannot be verified, do not present the claim as a direct verified quotation. Use it only as a lead or user-provided hypothesis until independently supported.
