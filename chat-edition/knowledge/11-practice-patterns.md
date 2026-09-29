# Game Design Suite Chat Edition — Practice Patterns from High-Adoption Agent Skills

> Purpose: strengthen reasoning quality for game design and game development without copying any external Skill verbatim.
> Use this as a method layer. Domain facts still come from the project's own evidence and GDS domain references.

## Source families studied

Patterns were abstracted from:
- `obra/superpowers`: brainstorming, systematic debugging, verification-before-completion, writing-skills.
- `Donchitos/Claude-Code-Game-Studios`: design-system, design-review, balance-check, playtest-report, project-stage workflows.
- `Unity-Technologies/skills`: official Unity task skills with narrow scopes and executable workflows.
- `gamedev-skills/awesome-gamedev-agent-skills`: router + engine/task/genre composition, version-aware references.
- `fagemx/gstack-game`: game review, balance review, player experience, playtest, QA and shipping loops.
- OpenAI / Anthropic public Skill authoring guidance: concise routing, load detail on demand, deterministic scripts for fragile operations.

These are process references, not authority over the user's project.

## 1. Situation First, Topic Second

Do not route only by nouns such as “装备 / 英雄 / 数值”.

First identify what the user is doing:
- Create
- Review
- Debug
- Verify
- Tune
- Compare / Benchmark
- Implement
- Validate / Playtest

Then apply the relevant domain.

Example:
- “设计装备” = Create + Itemization.
- “为什么掉率让人刷不动” = Diagnose + Itemization + Economy + Simulation.
- “这个技能倍率对象是不是错的” = Verify + Config/Code, not Balance first.
- “把这个数值调到能上线” = Tune + Balance + Validation.

This reduces shallow template answers.

## 2. Shared Understanding Before Heavy Design

For material system work, establish:
- intended player experience;
- system job;
- current constraints;
- success criteria;
- what is fixed vs negotiable.

When the prompt already supplies these, do not ask them again. Restate the working brief internally and proceed.

Do not start with a feature list before knowing what problem the system is supposed to solve.

## 3. Evidence Gate Before Verdict

Before judging “healthy / broken / balanced / fixed”:
- list what evidence actually exists;
- identify target/baseline;
- identify missing evidence;
- distinguish NOT ASSESSED from PASS.

If there is no target range, do not call a value “normal”.
If there is no runtime evidence, do not call a code path “working”.
If there is no playtest, do not call a design “fun”.

“NOT ASSESSED — NO DATA” is a valid result.

## 4. Target Before Outlier

A number is not an outlier merely because it looks large.

For balance/economy/progression:
1. define intended range or experience target;
2. identify the observable metric;
3. compare current value to target;
4. inspect interactions and tails;
5. only then classify issue severity.

Useful targets:
- TTK / HPS / EHP;
- actions per cycle;
- resource stock days;
- upgrade cadence;
- actual upgrade chance;
- graduation time P50/P90/P95;
- decision frequency;
- failure/retry rate;
- encounter completion time.

## 5. Working Analogue Before Fix

For bugs, configs, implementation mismatches, and even some system-design problems:
- find the nearest working example in the same project;
- compare all meaningful differences;
- trace the data/decision chain backwards;
- form one hypothesis;
- test the smallest possible variable.

Do not stack three candidate fixes and then guess which one mattered.

## 6. Dependency Graph and Change Propagation

Any structural design change should identify:
- upstream inputs;
- downstream consumers;
- shared constants/formulas;
- content that assumes the old rule;
- UI/text/tutorial dependencies;
- economy/progression consequences;
- configuration/code migration impact.

A local-looking change can be Cross-system.

Before approving a change, ask:
> If this rule changes, what else becomes wrong even if this local screen now looks correct?

## 7. Compare Credible Alternatives

For important design decisions, do not stop at the first plausible answer.

Generate 2–3 materially different candidates when real alternatives exist.
Compare:
- player behavior;
- clarity;
- agency;
- pacing;
- balance stability;
- economy impact;
- content burden;
- implementation cost;
- exploit/degenerate risk;
- long-term scalability.

Reject fake alternatives that are only parameter variants.

## 8. Adversarial Player / Degenerate Strategy Pass

Pressure-test the preferred design against:
- min-max behavior;
- hoarding;
- skipping;
- farming the easiest source;
- one-build dominance;
- one-stat dominance;
- infinite/near-infinite loops;
- sunk-cost lock-in;
- reward invalidation;
- onboarding confusion;
- endgame accumulation.

Ask:
- What is the strongest exploit?
- What is the cheapest dominant strategy?
- What happens at the 90th percentile player, not only average?
- What happens after months of inventory/resource accumulation?

## 9. Player Experience Is an Observable Chain

Avoid vague claims such as “更有趣 / 更沉浸 / 更策略”.

Translate them into:
`Situation -> Player notices -> Interprets -> Decides -> Acts -> Feedback -> Updates plan`

For a design claim, name:
- what the player sees;
- what choice exists;
- what tradeoff makes it meaningful;
- what feedback teaches the result;
- what next decision changes.

## 10. Playtest Protocol Instead of “Need Playtest”

If a design depends on player behavior, define the cheapest useful test:
- hypothesis;
- participant/player segment;
- task;
- build/content slice;
- observable behavior;
- quantitative metric;
- failure threshold;
- interpretation rule.

Examples:
- 5/8 first-time players identify the intended target priority without text tutorial;
- P90 wave clear time remains under the target while failure cause stays readable;
- <10% of runs are forced into off-build picks by wave 10;
- at least 3 viable item builds remain within the accepted DPS/EHP envelope.

## 11. Fresh Verification Before Completion

Before claiming “完成 / 修复 / 可上线 / 通过”:
1. identify what evidence proves it;
2. obtain fresh evidence;
3. read the result;
4. verify the actual acceptance criteria;
5. only then use completion language.

Confidence is not evidence.

## 12. Deterministic Where Fragile, Judgment Where Contextual

Use low freedom for:
- file transforms;
- schema validation;
- formula recomputation;
- migration steps;
- build/test commands;
- exact code patches.

Use higher freedom for:
- creative ideation;
- game feel;
- player fantasy;
- alternative system concepts;
- qualitative tradeoffs.

Do not bury judgment under rigid templates, and do not use vague prose for fragile implementation.

## 13. Reasoning Quality Gate

Before finalizing a non-trivial answer, check:
- Did I solve the actual decision, or a nearby easier question?
- Did I distinguish facts, assumptions, and candidates?
- Did I test the strongest alternative explanation?
- Did I consider second-order/cross-system effects?
- Did I use numbers where adjectives would be misleading?
- Did I define what evidence would reverse my conclusion?
- Did I give a validation path?
