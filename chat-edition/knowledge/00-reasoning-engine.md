# Game Design Suite Chat Edition — Reasoning Engine

> Universal process layer for non-trivial game-design, balancing, review, debugging, and implementation tasks.
> This file is process guidance, not a domain encyclopedia.

## 1. Task Mode

Classify the request before solving it:

- **Create** — design something new.
- **Review** — assess an existing design/artifact.
- **Debug** — explain unexpected behavior or a defect.
- **Verify** — prove whether a claim/config/code path is correct.
- **Tune** — adjust values without changing the fixed mechanic.
- **Explain** — clarify a concept without changing the system.

Then classify scope:

- **Local** — one field, one rule, one UI state, one code path.
- **System** — one complete system with upstream/downstream dependencies.
- **Cross-system** — multiple systems whose interaction creates the real outcome.

Do not use a Cross-system process for a one-line fix, and do not use a Local process for economy loops or progression architecture.

## 2. Decision Object

State internally what is actually being decided.

Examples:
- “Is DamageCfgSec scaling from the correct source stat?”
- “What should this equipment slot contribute to the total item budget?”
- “Should this resource be a mandatory hero-upgrade sink?”
- “Which progression curve reaches the target TTK without a power cliff?”

If the prompt contains several independent decisions, split them and solve one at a time.

## 3. Success Bar

A strong answer has a falsifiable completion condition.

Examples:
- config audit: exact field chain is verified;
- code fix: original reproduction no longer occurs and no regression appears;
- balance: target range is met across representative levels;
- economy: sources/sinks remain healthy over the intended horizon;
- design: player decision quality improves without violating Fixed Rules.

If success cannot be measured numerically, define observable acceptance criteria.

## 4. Evidence Gate

Before design or diagnosis, separate:

- what the user explicitly confirmed;
- what current project evidence proves;
- what is inferred;
- what is missing.

For existing projects, current evidence outranks old docs, previous answers, names, and analogies.

If required evidence is absent, do not “complete the template” with invented facts. Use:
- NOT ASSESSED — NO DATA
- unverified
- externally-blocked

Absence of evidence is not evidence of absence.

## 5. Alternatives and Hypotheses

### Design
For material system decisions, compare at least two credible approaches unless only one is technically possible.

For each option, check:
- player experience;
- systemic cost;
- implementation complexity;
- balance risk;
- long-term scalability;
- failure mode.

Do not manufacture fake alternatives just to fill a table.

### Debug / Audit
Use one explicit hypothesis at a time:
- hypothesis;
- supporting evidence;
- falsifying evidence;
- smallest test.

If the test fails, discard or revise the hypothesis instead of stacking unrelated fixes.

## 6. Evaluation

Evaluate only dimensions that can change the decision.

Useful lenses:
- power budget;
- DPS/HPS/EHP/TTK;
- source/sink flow;
- probability distribution;
- action economy;
- replacement cadence;
- progression curve;
- usability/error state;
- implementation dependency chain.

For randomness, check distribution/tails, not only the average.

For systems, check second-order effects:
- What does this make easier/harder elsewhere?
- Which resource, build, hero, encounter, or UI state becomes dominant?
- Does the fix merely move the problem downstream?

## 7. Adversarial Check

Before finalizing, challenge the preferred conclusion:

- What is the strongest alternative explanation?
- What edge case breaks this?
- What hidden assumption matters most?
- What could make the recommendation harmful?
- What evidence would reverse the recommendation?

Only surface concise results, not private chain-of-thought.

## 8. Smallest Defensible Decision

Prefer:
- root-cause fix over symptom patch;
- smallest change that solves the actual problem;
- reversible change when uncertainty is high;
- parameter tuning before mechanism rewrite when mechanics are Fixed Rules;
- explicit trade-offs over fake certainty.

## 9. Verification

Every important recommendation should include how to prove it.

Examples:
- run 100 / 1000 combat simulations;
- compare Lv1/Lv20/Lv40/Lv60/Lv80 samples;
- reproduce before/after;
- inspect exact config tuple;
- trace Config → Parser → Runtime Consumer;
- measure P50/P90/P95;
- validate UI state transitions;
- compare source/sink balance over D1–D7.

A recommendation without a verification path remains candidate.
