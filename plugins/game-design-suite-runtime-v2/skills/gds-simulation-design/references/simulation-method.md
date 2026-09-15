# Simulation Method

## Why simulate

Use simulation when direct algebra is insufficient because the result depends on time, state, randomness, interaction, policy, or long-horizon accumulation.

Common questions:

- How often does this build fail, not just what is its average DPS?
- How many turns until an ultimate across different speed/energy setups?
- What is the P90 time to reach a progression milestone?
- Which parameter actually causes the imbalance?
- Do two individually safe multipliers create an unsafe interaction?

## Model Fidelity Ladder

Choose the lowest-cost model that can answer the decision:

1. Closed-form formula
2. Spreadsheet / deterministic calculation
3. Timeline / rotation model
4. Discrete-event simulation
5. Monte Carlo simulation
6. Agent simulation
7. Production-runtime replay / bot farm
8. Telemetry / human playtest

Do not use a higher-fidelity model merely to look sophisticated. Do not use a lower-fidelity model for claims it cannot support.

## Randomness

Track every stochastic source separately:

- crit
- hit/resist
- target selection
- proc chance
- drop tables
- event routes
- card/skill offerings
- AI decisions

Prefer one central seedable RNG interface. Record seed and stream identity when multiple independent RNG streams exist.

## Sampling

For every key metric ask:

- What variance do we expect?
- What minimum effect size matters to the design decision?
- How wide may the confidence interval be?
- Are tail events important?

If the metric is rare-event dominated, brute-force Monte Carlo may be inefficient. Prefer analytic probability, targeted scenario generation, or importance sampling where appropriate.

## Sensitivity

A good simulator is not just a calculator. It should help answer "what lever matters?"

For parameter x and output y, useful diagnostics include:

- absolute delta: Δy
- relative delta: Δy / y
- local slope: Δy / Δx
- elasticity: (%Δy) / (%Δx)
- breakpoint location
- pairwise interaction: effect(x,y) beyond the sum of individual effects

## Validation Pyramid

1. Unit-test individual formulas.
2. Golden-test known complete scenarios.
3. Compare simulation against production runtime with same inputs/seeds where possible.
4. Compare aggregate distributions against telemetry once available.
5. Use human playtest for experience claims.

## Agent Personas

When player choice matters, run more than one policy if the design should support different playstyles.

Examples:

- greedy damage
- survival-first
- resource-conserving
- combo-completion
- novelty-seeking
- beginner heuristic
- expert heuristic

A design that is balanced only under one handcrafted policy may be brittle.

## Performance

For large sweeps:

- separate pure model from presentation;
- avoid rendering;
- batch runs;
- cache immutable config parsing;
- profile before optimizing;
- use parallelism only when RNG and shared state remain deterministic/reproducible;
- save compact run summaries and representative traces instead of every full trace.

## Result Discipline

Always separate:

- model fact
- simulation observation
- design interpretation
- runtime evidence
- player evidence

Simulation is pre-analytics, not replacement analytics.
