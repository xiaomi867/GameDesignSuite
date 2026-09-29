# Game Design Suite Chat Edition — Game Design Review & Playtest Practice

> Purpose: strengthen game-design judgment, review depth, playtest design, and balance diagnosis using patterns abstracted from widely adopted game-development agent workflows.
> This is a method reference, not a template that must be filled mechanically.

## 1. Review Entry Gate

Before reviewing a design, determine what evidence exists:
- design document / current rules;
- current config/data;
- formulas/targets;
- implementation constraints;
- playtest/telemetry;
- known Fixed Rules.

If the artifact or target is absent, mark the affected judgment `NOT ASSESSED — NO DATA` instead of issuing a clean verdict.

## 2. Design Review Dimensions

Review only dimensions that can change the decision:

### Completeness
- system job and player fantasy;
- detailed rules;
- edge cases;
- dependencies;
- formulas/targets where numeric;
- tuning knobs;
- acceptance criteria;
- failure/recovery behavior.

### Internal Consistency
- rules do not contradict each other;
- terms have one meaning;
- unlocks/costs/targets match across sections;
- the same resource/stat is not assigned incompatible roles.

### Cross-system Consistency
- combat ↔ hero kit;
- hero ↔ equipment;
- equipment ↔ economy;
- progression ↔ content difficulty;
- level ↔ tutorial/UX;
- reward ↔ effort/risk;
- UI text ↔ actual config/code.

### Implementability
- states and transitions are explicit;
- ownership/authority is clear;
- data/config needs are defined;
- edge cases have a rule;
- runtime dependencies are known.

## 3. Target Before Balance Verdict

For balance review, do not ask “这个数值大不大”.
Ask:
- intended target?
- measured metric?
- allowed range?
- representative scenarios?
- failure threshold?

Then check:
- Combat: DPS / TTK / EHP / HPS / uptime / action economy;
- Economy: faucet/sink flow, accumulation horizon, conversion loops;
- Progression: power curve, dead zones, spikes, content gates;
- Loot: acquisition time, pity, usable-drop rate, inventory pressure.

A value with no stated target is “not judged”, not “healthy”.

## 4. Degenerate Strategy Pass

Explicitly search for:
- one option strictly dominates;
- one build solves all content;
- skip/grind route invalidates intended pacing;
- easiest farm source dominates all sources;
- infinite or near-infinite resource loop;
- defense creates practical invulnerability;
- reward makes risk irrelevant;
- a stat breakpoint invalidates alternative stats;
- pair-lock or hard gate collapses roster diversity.

## 5. Player Experience Chain

Avoid vague words unless operationalized.

Instead of:
- “更有趣”
- “更策略”
- “更沉浸”
- “更爽”

Write:
`Trigger → Player notices → Choice → Tradeoff → Action → Feedback → Updated plan`

A good design claim names:
- what the player perceives;
- what decision changes;
- why two options are meaningfully different;
- what feedback confirms the rule;
- how the next decision changes.

## 6. Playtest Plan

For any behavior-dependent design, define:

| Field | Requirement |
|---|---|
| Hypothesis | What should happen |
| Segment | New/returning/advanced, target profile |
| Build | Exact version/content slice |
| Task | What player is asked to do |
| Observation | What behavior to watch |
| Metrics | Quantitative measures |
| Failure threshold | What counts as a problem |
| Interpretation | What result implies |
| Next action | What changes if hypothesis fails |

Useful observations:
- first 5 minutes: goal/control comprehension;
- confusion point;
- decision hesitation time;
- death/failure location;
- retry behavior;
- unused features;
- dominant choice;
- resource hoarding;
- moments of delight / clear payoff.

## 7. Balance Test Matrix

Do not validate only one “average” build.

When relevant test:
- low / median / high investment;
- early / mid / late/endgame;
- single target / multi-target;
- weak / neutral / resistant enemy;
- short / medium / long encounter;
- lucky / median / unlucky RNG;
- baseline / intended build / exploit build.

Report distribution and worst-case behavior, not only the mean.

## 8. Re-review Discipline

A changed design should be re-reviewed against:
- previous blocking issues;
- new downstream effects;
- dependencies;
- new evidence.

Do not assume “the changed section is fixed” means the whole design is still coherent.

## 9. Recommendation Quality

Every material recommendation should include:
- problem;
- evidence;
- root cause;
- proposed change;
- retained tradeoff;
- validation method.

If evidence is weak, recommend the cheapest test that reduces uncertainty instead of inventing certainty.

## 10. Shipping Gate

Before calling a system “ready”:
- critical rules are unambiguous;
- dependencies exist;
- known blockers are resolved or explicitly accepted;
- numeric targets have validation evidence;
- implementation-sensitive claims are code/runtime verified where required;
- playtest-dependent claims have playtest evidence;
- acceptance criteria are checkable.

A theoretically coherent design is not automatically production-validated.
