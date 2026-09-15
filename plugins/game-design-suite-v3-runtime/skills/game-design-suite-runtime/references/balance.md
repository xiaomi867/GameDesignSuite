# V3 Module — Balance

Derived from the canonical `balance-design` knowledge source. This is a runtime reference module, not a separate Skill.

## 1. Numerical Design Order

Always start with:

`Experience Target -> Observable Behavior -> Metric -> Numerical Model -> Parameters -> Validation`

Never start by inventing parameters and then explaining them afterward.

Examples of useful experience anchors:

- target Boss TTK;
- number of enemy actions the player should survive;
- perceptible breakthrough Power Delta;
- target resource coverage days;
- expected number of actions/casts in a window;
- target Build diversity.

## 2. Benchmark Contract

Any comparison needs a reproducible Benchmark. Depending on task, lock:

- level / breakthrough / rarity / star;
- skill level;
- equipment quality and stat budget;
- party assumptions;
- enemy level / DEF / resistance;
- enemy behavior / attack frequency;
- battle duration;
- target count / Boss vs Elite;
- initial resources;
- RNG model / seed where relevant.

Different Benchmarks cannot be compared as if they were the same test.

## 3. Numerical Architecture

Check the relationship:

`Power Curve <-> Cost Curve <-> Content Curve <-> Time Curve`

Separate at least:

- macro pacing / timeline;
- economy;
- progression;
- combat moment-to-moment.

A local coefficient fix must not silently break another layer.

## 4. Model Construction

Use only the model needed for the current Decision Object. Common models:

- single-hit damage;
- expected DPS / HPS;
- EHP;
- Burst Window;
- Crit EV;
- Buff Uptime;
- CC Coverage;
- resource per rotation/minute;
- break-even;
- growth per level/star;
- enemy-to-player power ratio.

Complex damage should identify multiplicative/additive layers, for example:

`Final = Base × Crit × DamageBonus × Defense × Resistance × Vulnerability × Mitigation × State`

This is a framework; a real project may have fewer or more layers.

For each variable state:

- unit;
- source;
- tunability;
- domain/range;
- evidence status.

## 5. Power Budget

Do not compare different effects using only panel percentages.

Separate:

- Raw Power;
- Effective Power;
- Situational Power;
- Synergy Power;
- Cost / opportunity cost.

Conceptual framework:

`Effective Value = Raw Value × Uptime × Applicability × Reliability × Context Factor - Cost`

Conditional effects need Context Discount.

## 6. Attribute Value Anchor

A cross-project constant such as `ATK:DEF:HP = 1:1:10` is not a truth. Derive exchange rates from the current project:

1. lock Benchmark;
2. perturb one stat;
3. measure target metric change;
4. repeat at multiple stages/enemy types;
5. derive an exchange-rate interval;
6. reuse only as a local budget language.

## 7. Sensitivity and Extremes

For candidate values, test:

- one-variable sensitivity;
- breakpoint behavior;
- worst/best combinations;
- low/high uptime;
- short/long encounters;
- target count changes;
- stacking limits;
- multiplicative interaction chains.

If a small parameter change creates a large output swing, mark the system as high-sensitivity and avoid pretending the single chosen number is robust.

## 8. Candidate vs Verified

- Mathematical consistency -> candidate unless tied to verified project rules.
- Spreadsheet / simulation -> not Playtest.
- Config truth -> `verified-config` only after field identity is locked.
- Code semantics -> `verified-code` only after runtime consumer is checked.
- Runtime behavior -> `verified-runtime` only with actual execution evidence.

## 9. Balance Fingerprint

A proper V3 Balance answer must visibly follow:

`Experience Target -> Benchmark -> Model -> Parameters -> Validation`

If any step is impossible due to missing evidence, say which one and continue only with independent steps.
