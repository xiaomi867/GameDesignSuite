# Game Design Suite Chat Edition — Professional Workflows

> Purpose: stage-gated execution layer. Domain knowledge tells the model what to know; this file tells it how to reach a defensible decision.
> Use one primary workflow per Decision Object. Domain overlays may add gates but do not replace the primary workflow.

## 1. Stage Gate Contract

A stage is complete only when it has:

- **Input** — evidence/constraints needed to begin;
- **Artifact** — the concrete intermediate result produced;
- **Exit Criteria** — what must be true before moving on;
- **Blocked Condition** — what missing evidence makes the stage `NOT ASSESSED` or conditional.

Do not jump over a stage because the likely answer seems obvious.

Do not expose private chain-of-thought. Expose the artifact needed for review: evidence, model, alternatives, tradeoffs, findings, or validation.

## 2. Create / New Design

Use for new systems, features, heroes, levels, economies, itemization, or major redesigns.

`Intent -> Player Outcome -> Constraints -> Existing Pattern -> Problem Model -> Alternatives -> Tradeoff -> Candidate -> Cross-system Ripple -> Failure Modes -> Validation -> Acceptance`

### Gates

1. **Intent Gate**
   - Artifact: one-sentence system job + desired player behavior.
   - Exit: purpose is distinguishable from a feature list.

2. **Constraint Gate**
   - Artifact: Fixed Rules / negotiables / production constraints / unknowns.
   - Exit: no candidate violates a known hard constraint.

3. **Model Gate**
   - Artifact: rules/state/resource/flow model appropriate to domain.
   - Exit: design can be reasoned about without vague words.

4. **Alternative Gate**
   - Artifact: 2–3 materially different approaches when real alternatives exist.
   - Exit: tradeoff is explicit; no fake variants.

5. **Candidate Gate**
   - Artifact: selected candidate + why alternatives lose under current constraints.
   - Exit: candidate is implementable enough to inspect failure modes.

6. **Adversarial Gate**
   - Artifact: strongest exploit, counterexample, misunderstood use, tail case, lifecycle risk.
   - Exit: blocking failure is resolved or accepted as explicit risk.

7. **Validation Gate**
   - Artifact: test/simulation/playtest/telemetry plan + failure threshold.
   - Exit: evidence capable of proving or falsifying the intended outcome is defined.

## 3. Existing Project Change

Use when the user asks to modify an existing system, configuration, code path, document, hero, level, or economy.

`Evidence -> Current State -> Symptom -> Root Cause -> Constraint -> Candidates -> Minimal Change -> Ripple -> Verification`

### Gates

- **Evidence Gate**: inspect current artifact first. Historical memory is context, not proof.
- **Current-State Gate**: describe what actually happens now.
- **Root-Cause Gate**: classify Local Parameter / Rule Interaction / System Structure / Cross-system / Content / UX / Implementation / Evidence Error.
- **Change Gate**: choose smallest change that addresses the cause; temporary mitigation must be labeled.
- **Ripple Gate**: inspect only affected upstream/downstream systems.
- **Verification Gate**: original symptom + nearest regression risk.

Do not redesign fixed mechanics to solve a tunable problem.

## 4. Debug / Root Cause

`Reproduce -> Bound -> Trace Boundary -> Working Analogue -> Hypotheses -> Prediction -> Smallest Discriminating Test -> Root Cause -> Minimal Fix -> Regression -> Completion Evidence`

Rules:

- no final fix before root-cause investigation;
- one leading hypothesis at a time;
- a hypothesis must predict what evidence should exist if true;
- run the cheapest test that can falsify it;
- if falsified, discard/revise it rather than stacking patches;
- config/code/runtime are separate evidence layers.

Preferred trace:

`Config -> Generated Data -> Loader -> Parser -> Condition -> Runtime Consumer -> Target/Object -> UI/Result`

## 5. Numerical Design / Tune

`Experience Goal -> Metric -> Formula -> Baseline -> Budget -> Candidate Range -> Curve -> Breakpoints -> Sensitivity -> Distribution -> Simulation -> Cross-system Cost -> Validation`

### Required artifacts

- variables + units;
- formula/order/caps/rounding;
- baseline scenario;
- target band;
- candidate range before point value;
- representative samples;
- breakpoint table;
- sensitivity ranking;
- ordinary / weak / optimized cases;
- distribution/tails for randomness;
- evidence state.

When a model will be tuned repeatedly, treat the simulator/spreadsheet as an executable specification and regression asset.

A precise number with no model remains `candidate`.

## 6. Review / Audit

`Scope -> Evidence Baseline -> Expected Standard -> Findings -> Root Cause -> Impact -> Alternative -> Acceptance -> Re-review`

Each material finding contains:

`Problem + Evidence + Why it matters + Root cause + Proposed change + Retained tradeoff + Verification`

Use `NOT ASSESSED — NO DATA` when a required dimension cannot be checked.

Do not give clean PASS based on absence of evidence.

## 7. Benchmark / External Reference

`Question -> Source -> Observed Fact -> Version/State -> System Job -> Dependency -> Player Consequence -> Pattern -> Transfer Risk -> Project Fit -> Candidate -> Local Validation`

External values never become current-project verified facts.

When a page is interactive, record selected level/rank/skill state.

Prefer current project analogue before external benchmark.

## 8. Verify / Completion

`Claim -> Required Evidence -> Fresh Check -> Actual Result -> Regression/Residual Risk -> Status`

Status vocabulary:

- `DONE` — acceptance evidence obtained;
- `DONE_WITH_CONCERNS` — core acceptance passes, explicit residual risks remain;
- `BLOCKED` — known blocker prevents completion;
- `NEEDS_CONTEXT` — required evidence is unavailable;
- `NOT ASSESSED` — dimension was not actually tested.

No completion language without fresh evidence.

---

# Domain Overlays

## 9. Level Design Router

First classify the level job. Do not run one generic workflow for every level.

### A. Mainline / Exploration / Travel

`Purpose -> Journey -> Orientation -> Travel Beats -> Events -> Discovery -> Light Encounter Support -> Reward/Unlock -> Reorientation -> Exit State -> Playtest`

Primary metrics:
- travel/combat/event/reward time ratio;
- event density by time/distance;
- wrong-turn/backtrack;
- discovery uptake;
- objective comprehension;
- room/feature unlock friction;
- quit point.

Combat is support unless challenge is explicitly the level's primary job.

### B. Challenge / Roguelite / Wave

`Run State -> Build State -> Wave Role -> Pressure Axis -> Encounter Composition -> Resource Attrition -> Choice/Reward -> Recovery -> Difficulty Ramp -> Boss Test -> Run Outcome`

Primary metrics:
- TTK by wave and speed setting;
- damage taken/resource loss;
- build completion probability;
- forced off-build picks;
- P50/P90/P95 clear/fail time;
- composition coverage;
- boss pass rate by legitimate build archetype.

Randomness must preserve pacing guarantees.

### C. Boss

`Contract -> Teach Signal -> Phase 1 Read -> Practice -> Escalation -> Mastery Test -> Recovery Window -> Final Check -> Reward/Closure`

Stress a player capability; do not nullify it.

### D. Tutorial / FTUE

`Need-to-Know -> Safe Introduction -> Guided Action -> Independent Repeat -> Pressure Test -> Recall Later`

Measure intervention rate, wrong action rate, time-to-first-success and delayed recall.

### E. Resource / Farming Stage

`Economic Job -> Expected Investment -> Encounter Cost -> Reward Variance -> Repeat Time -> Dominant-Farm Risk -> Exit`

Check level economy and whether one easiest stage invalidates other content.

### Level mandatory pass

Always check when relevant:
Level Purpose, Player Journey, Beat/Rhythm, Traversal, Encounter, Exploration/Event, Reward, Difficulty/TTK, Spatial Pressure, Enemy Composition, Learning->Test->Mastery, Boss Teaching, Pacing, Checkpoint, Failure Recovery, Level Economy, Replayability, Procedural Constraints, Mainline-vs-Challenge fit, Playtest metrics.

## 10. Hero Design Workflow

Do not design a hero as "element + weapon + six skills".

`World/Faction Slot -> Character Fantasy -> Combat Fantasy -> Roster Gap -> Core Loop -> Kit Architecture -> Team Hook -> Counterplay -> Stat Envelope -> Growth -> Skill Values -> Content Fit -> Description -> Validation`

### Hero Concept Gate

Required:
- world rule / identity / faction / social role;
- want / need / fear / contradiction;
- narrative function;
- player recognition;
- visual keywords/silhouette/animation verbs;
- character fantasy;
- combat fantasy;
- roster differentiation.

Exit only when the character has a reason to exist beyond throughput.

### Hero Kit Gate

Required:
Role, Combat Loop, Basic/Skill/Ultimate/Passive, Resource, Trigger, State, Target, Team Hook, Counterplay, Skill Expression, Synergy, Anti-synergy, Failure/Recovery.

Exit only when every slot serves the loop or a deliberate exception.

### Hero Stat Gate

Required:
Lv1->cap HP/ATK/DEF, fixed stats, speed/action identity, crit/break/relevant secondaries, ascension deltas, power budget, EHP/DPS/HPS, breakpoints, representative level samples.

## 11. Skill Design — Mechanism Before Numbers

A skill uses two separate Decision Objects.

### Gate A — Mechanism

`Purpose -> Trigger -> State -> Target -> Effect -> Resource -> Timing -> Buff/Debuff -> Stack/Group/Exclusive -> Proc -> Crit Rule -> Snapshot/Dynamic -> Refresh -> Interaction -> Counterplay -> Boundary -> Runtime Semantics`

Do not tune multipliers while the mechanic contract is ambiguous.

### Gate B — Numerical Value

`Scaling Object -> Base Value -> Multiplier -> Hit Count -> Frequency -> Target/Coverage Factor -> Duration -> Uptime -> Cooldown -> Energy -> Reliability -> Rotation Contribution -> Lv1..N Curve -> Star/Ascension Delta -> Breakpoint -> Sensitivity -> Simulation -> Runtime Verification`

For every material skill parameter capture:
- source stat/scaling object;
- unit;
- level context;
- star/ascension context;
- formula;
- cap/floor;
- target count/coverage;
- refresh/stack semantics;
- evidence state.

### Skill Description Gate

Player text order:

`Trigger/Action -> Target -> Effect -> Value -> Duration -> Stack/Limit -> Exception`

The tooltip must let a player predict behavior. Config/code/runtime semantics outrank old prose.

## 12. Narrative / Worldbuilding Workflow

Use `21-narrative-worldbuilding.md`.

Primary path:

`Theme/Experience -> World Rule -> Consequence -> Faction -> Character -> Conflict -> Story Hook -> Player Agency -> Delivery -> Level/System Expression -> Continuity -> Validation`

Worldbuilding is not complete until at least one rule changes something the player can observe, decide, or do.

## 13. Playtest Workflow

`Decision -> Hypothesis -> Player Segment -> Build/Content Slice -> Task -> Observation -> Metrics -> Failure Threshold -> Interpretation -> Next Action`

Choose Blind / Facilitated / A-B / Stress / Focus according to the question.

Observed behavior outranks post-hoc preference when they conflict; both are evidence.

A playtest with no hypothesis is exploratory evidence, not validation of a specific design claim.
