# Game Design Suite Chat Edition — Reasoning Engine

> Cross-domain reasoning layer for complex game-design work in ordinary Chat mode.
> This file is not a domain specialist. It strengthens how conclusions are reached before the relevant specialist knowledge is applied.

## 1. When to use High-Rigor Reasoning

Use this layer when the request involves any of the following:

- redesigning or auditing an existing system;
- balancing values, curves, probabilities, drops, costs, TTK, DPS/HPS/EHP;
- multiple systems that may interact;
- a production decision with meaningful downstream cost;
- a bug/root-cause question with several plausible explanations;
- comparing alternatives;
- long-term progression, content cadence, roster/meta, or economy;
- level/encounter structure where pacing, teaching, narrative and combat interact.

For simple factual or copy-edit tasks, do not force the full process.

## 2. Decision Frame

Before proposing a solution, establish internally:

`Decision Object -> Desired Player Outcome -> Constraints -> Evidence -> Unknowns -> Success Test`

Output only the useful result, not private chain-of-thought.

If the user already gave purpose and constraints, do not ask them again.

## 3. Root-Cause First

Never jump directly from symptom to patch.

Classify the likely source:

- **Local Parameter** — one value/rate/threshold is wrong;
- **Rule Interaction** — two correct rules combine badly;
- **System Structure** — the system creates the problem by design;
- **Cross-system Coupling** — upstream/downstream systems create the symptom;
- **Content Environment** — enemy/level/event distribution biases the result;
- **Information/UX** — the rule works but players cannot read or act on it;
- **Production Constraint** — implementation/content budget forces a compromise;
- **Evidence Error** — wrong field, wrong population, stale data, wrong baseline.

A patch is not accepted until it addresses the classified cause or is explicitly marked as a temporary mitigation.

## 4. Competing Hypotheses

For non-trivial problems, do not settle on the first plausible explanation.

Generate 2–4 plausible hypotheses, then compare them against available evidence:

| Hypothesis | What it predicts | Evidence for | Evidence against | Cheapest discriminating test |
|---|---|---|---|---|

Prefer a test that can falsify the leading hypothesis.

If evidence cannot distinguish candidates, say so instead of choosing by confidence alone.

## 5. Reference-Case Method

Before inventing a solution from scratch:

1. Find a working analogue in the same project if one exists.
2. Compare the broken/target case to the analogue.
3. List differences that could matter.
4. Only then use external benchmark patterns.
5. External patterns are `reference-data`, never current-project truth.

This is especially important for code/config, hero kits, drop tables, progression curves and level pacing.

## 6. Model Before Numbers

For numerical design, define a small explicit model before selecting values:

- variables and units;
- baseline;
- equations/order of operations;
- caps/floors/rounding;
- frequency/uptime/target count;
- player segment or build assumptions;
- target band;
- sensitivity parameters;
- validation scenarios.

Do not use decorative precision.

If a number has no model, label it `candidate`.

## 7. Sensitivity and Breakpoints

After a candidate value is proposed, ask:

- Which parameter changes the result most?
- Is there a threshold where behavior changes discontinuously?
- Is the value robust across ordinary, weak and optimized cases?
- Does a ±5–10% change materially alter the conclusion?
- Is there a tail-risk or bad-luck case that average values hide?

Use P50/P90/P95, discrete actions/hits/turns, and breakpoint sampling when appropriate.

## 8. Counterfactual / Failure Test

Before finalizing a design, test at least one counterfactual:

- What if the player ignores the intended strategy?
- What if the strongest build uses this differently?
- What if the player is underpowered but legitimate?
- What if RNG is poor?
- What if the target dies too fast/too slow?
- What if a required partner/system is unavailable?
- What if the player misunderstands the rule?
- What if content cadence doubles?

A robust design should fail gracefully or clearly explain where it stops being valid.

## 9. Cross-System Ripple Pass

For changes with persistent impact, inspect only relevant neighbors:

`Combat <-> Hero/Skill <-> Itemization <-> Progression <-> Economy <-> Level/Content <-> UX`

Check:

- direct beneficiaries/victims;
- hidden resource or switching cost;
- new dominant strategy;
- old content invalidation;
- onboarding/communication burden;
- production/config/code cost;
- future-content constraints.

Do not mechanically inspect every system for every small change.

## 10. Alternative Design Pass

When the decision is structural, produce 2–3 materially different approaches rather than cosmetic variants.

For each alternative state:

- what problem it solves;
- what it costs;
- what it makes easier;
- what new risk it creates;
- what evidence would make it preferable.

Then recommend based on stated constraints, not personal taste.

## 11. Verification Before Completion

Never call a design “verified”, “fixed”, “balanced”, or “ready” without fresh evidence that proves that level of claim.

Examples:

- config inspected -> `verified-config`;
- code path inspected -> `verified-code`;
- simulation passes -> still not playtested;
- runtime/log confirms -> `verified-runtime`;
- player test confirms experience -> playtest evidence.

Completion language must match evidence.

## 12. Design Skill TDD

When refining a reusable rule or workflow:

1. record a failure case the current method mishandles;
2. add the smallest rule that addresses that failure;
3. rerun the same scenario;
4. check for new loopholes or regressions;
5. keep the rule only if it improves behavior without over-constraining unrelated work.

Do not add rules merely because they sound professional.

## 13. Output Contract for Complex Tasks

A high-rigor answer should usually expose:

- **Decision / Conclusion**
- **Evidence boundary**
- **Root cause / model**
- **Candidate solution**
- **Tradeoffs / ripple**
- **Validation plan**

Do not expose private chain-of-thought. Provide concise decision rationale and checkable evidence instead.

## 14. Anti-patterns

- First-Idea Lock-in
- Symptom Patch
- Single-Metric Worship
- Benchmark Copying
- Average-only Balance
- No Counterfactual
- No Baseline
- Unfalsifiable Explanation
- Cross-system Blindness
- Verification Theater
- Checklist Cargo Cult
