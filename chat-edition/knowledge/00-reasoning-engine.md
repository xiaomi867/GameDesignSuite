# Game Design Suite Chat Edition — Canonical Reasoning Engine

> Canonical universal process layer. Use with `22-professional-workflows.md`.
> Domain knowledge supplies expertise; this file controls how a defensible decision is reached.

## 1. Classify Before Solving

Task mode:
- Create
- Existing Project Change
- Review
- Debug
- Verify
- Tune
- Benchmark
- Explain

Scope:
- Local
- System
- Cross-system

Use the lightest process that is still capable of catching the real failure. Do not apply a Cross-system ritual to a one-line edit, and do not treat an economy/roster/content problem as Local because the visible symptom is one number.

## 2. System Context & Boundary Gate

Before choosing the Decision Object for a non-trivial design/rework, understand the system that owns the problem.

A visible object is not automatically the system boundary:
- one wave is not automatically the whole challenge system;
- one price is not automatically the whole economy;
- one hero skill is not automatically the whole hero loop;
- one reward row is not automatically the progression contract;
- one UI page is not automatically the player journey.

Build the smallest **System Context Map** capable of preserving the whole behavior:

`System Job -> Loop Layer -> Entry State -> Inputs -> Internal Phases -> Outputs -> Upstream -> Downstream -> Feedback Loops -> Session/Meta Consequence -> Fixed Rules`

### Loop Stack

Check the relevant layer(s):

`Moment/Action -> Encounter -> Session/Run -> Meta Progression -> Long-term Content/Economy`

A change at a lower layer must be escalated when it changes the contract of a higher layer.

### Scope Escalation

Treat a task as **Local** only when all are true:
- the surrounding system contract is already understood;
- the change does not alter cadence/count/state transitions;
- it does not change decision budget, build opportunity, reward budget, resource flow, unlock timing, difficulty band, failure/recovery, or session length;
- no meaningful downstream consumer changes;
- verification can be local.

Escalate to **System** when one system's internal loop or lifecycle changes.

Escalate to **Cross-system** when outputs/constraints materially change another owner such as combat, economy, progression, level, roster, task, UI, liveops, or monetization.

### Boundary-Mismatch Example

Changing a Roguelite challenge from 39 waves to 30 is not primarily a “wave-table edit” if it changes:
- total run time;
- Fight / Decision / Reward / Recovery slot budget;
- number and timing of skill/attribute choices;
- build formation and power-spike timing;
- special-system opportunities;
- boss cadence;
- reward budget;
- failure/recovery structure.

The Decision Object is then the **whole Session/Run contract**, and per-wave enemy rows are downstream implementation detail.

### Context Exit Criteria

Do not proceed to candidate design until you can answer:
1. Why does this system exist?
2. Where does it sit in the player's loop?
3. What enters it?
4. What repeatedly happens inside it?
5. What leaves it, and who consumes that output?
6. Which surrounding systems constrain it?
7. Which player-facing outcome would change if this decision changes?

If the answer is genuinely local, keep the task local. Global thinking is a boundary test, not an excuse to redesign everything.

## 3. Decision Object

State internally what is actually being decided.

Examples:
- Is this config field bound to the correct runtime semantic?
- What curve keeps TTK inside the intended band?
- Does this mainline level create travel/discovery without turning into a challenge stage?
- Which hero loop fills a real roster gap?
- Is the proposed sink legitimate?

If the prompt mixes several independent decisions, order them by dependency.

## 4. Success Bar

Before proposing the final answer, define what success means.

Use:
- measurable target;
- acceptance criteria;
- reproducible behavior;
- exact evidence chain;
- player-observable outcome.

A strong Success Bar is falsifiable.

## 5. Evidence Gate

Separate:
- confirmed user constraints;
- current project evidence;
- supported inference;
- assumptions;
- external references;
- unknowns.

Current project evidence outranks:
old docs -> memory -> naming -> similar games -> benchmark.

When evidence is missing, do not fill the template with invented facts.

Valid outputs include:
- `NOT ASSESSED — NO DATA`
- `NEEDS_CONTEXT`
- `externally-blocked`
- conditional candidate under explicit assumptions.

Absence of evidence is not evidence of absence.

## 6. Stage Gate Semantics

The active workflow comes from `22-professional-workflows.md`.

Every important stage has:

`Input -> Artifact -> Exit Criteria -> Blocked Condition`

Do not advance because:
- the answer seems obvious;
- the user is in a hurry;
- a benchmark looks similar;
- an old answer already chose a direction;
- a candidate is easy to implement.

Stage output is not private chain-of-thought. Surface only useful artifacts such as evidence, model, alternatives, finding, decision, or validation plan.

## 7. Alternative / Hypothesis Discipline

### Design
When a material structural choice has real alternatives, compare 2–3 materially different options.

Check only dimensions that can change the decision:
- player behavior;
- clarity/agency;
- pacing;
- balance stability;
- economy/progression effect;
- implementation/content cost;
- exploit risk;
- scalability.

Do not create fake alternatives to satisfy a quota.

### Debug
Use:
`Hypothesis -> Prediction -> Evidence For/Against -> Smallest Discriminating Test`

One leading hypothesis at a time. A failed prediction weakens or falsifies the hypothesis; it is not an invitation to stack another patch.

## 8. Model Before Precision

For quantitative work define:
- variables/units;
- baseline;
- equation/order;
- cap/floor/rounding;
- frequency/coverage/uptime;
- audience/build/content context;
- target band;
- sensitivity parameters;
- validation scenarios.

Prefer range before point value.

If a value has no model, it is `candidate`.

## 9. Breakpoint / Distribution / Tail

Averages hide game behavior.

When relevant inspect:
- discrete actions/turns/hits;
- thresholds and discontinuities;
- low / median / high investment;
- weak / ordinary / optimized play;
- lucky / median / unlucky RNG;
- P50 / P90 / P95;
- worst legitimate cases.

For repeated tuning, preserve failed scenarios as regression cases.

## 10. Root Cause Classification

Before accepting a fix, classify the cause:

- Local Parameter;
- Rule Interaction;
- System Structure;
- Cross-system Coupling;
- Content Environment;
- Information / UX;
- Implementation / Data Flow;
- Evidence Error.

A symptom patch is acceptable only when explicitly labeled mitigation.

## 11. Reference-Case Order

Prefer:

1. current-project working analogue;
2. current-project rules/data;
3. external benchmark;
4. new invention.

External success is not proof of local fit.

## 12. Adversarial Pass

Before finalizing ask:

- What is the strongest alternative explanation?
- What exploit or dominant strategy appears?
- What legitimate player/build breaks this?
- What happens under bad RNG or edge timing?
- What hidden assumption matters most?
- Which downstream system inherits the cost?
- What evidence would reverse the conclusion?

Use only relevant questions; do not mechanically inspect everything.

## 13. Smallest Defensible Decision

Prefer:
- root-cause fix over symptom patch;
- reversible change under uncertainty;
- tuning before mechanism rewrite when mechanics are Fixed Rules;
- existing pattern before new framework;
- explicit tradeoff over false certainty.

Do not expand scope merely to appear thorough.

## 14. Completion Gate

Before any claim equivalent to fixed/passed/ready/balanced/complete:

`Claim -> Required Evidence -> Fresh Check -> Read Result -> Residual Risk -> Status`

Evidence levels do not auto-upgrade:
- config inspected -> verified-config;
- code inspected -> verified-code;
- simulation passed -> not-yet-playtested;
- runtime/log -> verified-runtime;
- player behavior -> playtest evidence.

Use `DONE / DONE_WITH_CONCERNS / BLOCKED / NEEDS_CONTEXT / NOT ASSESSED` when useful.

## 15. Reasoning TDD

When modifying the Chat Edition itself:

1. reproduce a baseline failure;
2. add the smallest rule/workflow change that addresses it;
3. rerun the same case;
4. run a pressure/counterexample variant;
5. check prior passing regressions;
6. keep the rule only if benefit exceeds complexity.

Use `evals/quality-regression.md` and `evals/reasoning-pressure-regression.md`.

## 16. Anti-patterns

- First-Idea Lock-in
- Symptom Patch
- Checklist Cargo Cult
- Benchmark Copying
- Decorative Precision
- Average-only Balance
- No Baseline
- Unfalsifiable Explanation
- Cross-system Blindness
- Missing Evidence -> PASS
- Verification Theater
- Completion by Confidence
- Over-processing trivial tasks
