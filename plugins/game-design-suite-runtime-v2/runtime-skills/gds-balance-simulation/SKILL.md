---
name: gds-balance-simulation
description: "Use when the task centers on game balance, formulas, simulations, telemetry experiments, benchmarks, probability distributions, or meta/roster balance."
---

# Balance & Simulation

Own numerical targets, formula verification, simulation plans/results, experiment design, and meta/roster balance.

## First visible block

```text
【本次专业视角】
主责：数值 / 模拟策划（gds-balance-simulation）
协同：仅列当前结果真实使用的专业
证据边界：<candidate / verified-config / verified-code / verified-data / verified-runtime>
```

## Preserved knowledge

Read only what the task needs:

- [Balance Design](../../skills/gds-balance-design/references/canonical-guidance.md)
- [Formula Verification](../../skills/gds-formula-verification/references/canonical-guidance.md)
- [Simulation Design](../../skills/gds-simulation-design/references/canonical-guidance.md)
- [Telemetry Experiment Design](../../skills/gds-telemetry-experiment-design/references/canonical-guidance.md)
- [Meta Balance](../../skills/gds-meta-balance/references/canonical-guidance.md)
- [Runtime knowledge map](../../references/runtime-knowledge-map.md) for adjacent domain support.

## Workflow

1. Define target metric and benchmark before tuning values.
2. Lock formula semantics and units before calculating outputs.
3. Separate deterministic calculation, stochastic simulation, telemetry evidence, and playtest evidence.
4. Report central tendency plus tails where randomness matters (for example P50/P90/P95 and extreme failure cases).
5. Check sensitivity, breakpoints, saturation, runaway scaling, dominant strategies, and power creep.
6. Mark every unvalidated recommendation as candidate; never label spreadsheet/simulation output as playtest proof.

For existing systems, use actual config/code/data when available. Do not infer unknown field semantics from names alone.
