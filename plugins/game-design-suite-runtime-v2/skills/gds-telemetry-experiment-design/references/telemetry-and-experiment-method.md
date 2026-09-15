# Telemetry & Experiment Method

## Evidence chain

Use this chain for every data question:

`Design Decision -> Hypothesis -> Observable Behavior -> Event -> Metric -> Segment -> Analysis -> Decision Rule`

If a link is missing, the metric may be descriptive but not decision-ready.

## Event schema principles

Prefer durable IDs and raw facts. Typical envelope:

```text
event_name
schema_version
timestamp
player_id/session_id/run_id
build_version/config_version
mode/stage/wave
entity_id/source_id/target_id
before_state/after_state
reason/source
experiment_id/variant_id
```

Do not use localized display strings as entity identifiers.

## Metric definition contract

Every KPI should specify:

- numerator;
- denominator;
- eligibility population;
- time window;
- deduplication rule;
- version filters;
- segment dimensions;
- missing-data rule;
- whether higher/lower is better;
- decision threshold.

## Balance diagnostics

For a selectable object (hero/card/item/build), combine multiple views:

- usage share;
- outcome rate;
- conditional outcome by skill/mastery;
- contribution metrics;
- matchup/composition matrix;
- abandonment/switch rate;
- usage of sub-actions;
- qualitative frustration/fun signals.

Use confidence intervals for small samples. Do not rank tiny cohorts as if they were stable.

## Experiment hierarchy

1. Offline calculation / simulation
2. Internal controlled runtime test
3. Limited external playtest
4. A/B or multivariate experiment
5. Full rollout observation

Not every question needs an online experiment. Avoid experimenting on changes with obvious safety or fairness violations.

## A/B analysis minimum

Before interpreting effect:

1. validate assignment;
2. check SRM;
3. check event completeness;
4. verify eligibility;
5. inspect sample size and exposure duration;
6. compare primary metric;
7. inspect guardrails;
8. inspect pre-declared segments;
9. report effect size + uncertainty;
10. decide ship / iterate / rollback / inconclusive.

## Causal caution

Observational telemetry is excellent for locating where to investigate. It is weaker for proving why the behavior occurred. Prefer controlled intervention for causal claims when practical.

## Balance across skill

A healthy aggregate can hide unhealthy subgroups. For competitive or mastery-heavy games, define stable skill buckets and monitor both power and accessibility. Different cohorts may need different thresholds.

## Versioning

Telemetry without version context is dangerous. Preserve:

- client/server build;
- data/config revision;
- experiment variant;
- balance patch;
- relevant content version.

When definitions change, bump metric/schema version rather than silently changing historical meaning.
