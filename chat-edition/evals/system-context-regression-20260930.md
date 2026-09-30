# System Context / Boundary Regression — 2026-09-30

## Reproduced failure

Observed behavior:

A request to redesign a challenge after changing total wave count was treated mainly as a wave-level problem. The answer focused on local monsters/choices before reconstructing the full Roguelite Session.

The missing reasoning step was not “cross-system impact after design”. It was **system understanding before choosing the design boundary**.

## Root cause in Chat Edition

Pre-fix flow:

`Classify -> Decision Object -> ... -> Candidate -> Cross-system Ripple`

This allowed the model to define the Decision Object too early.

Existing `01-core-systems.md` already had:
- system templates;
- Gameplay Structure;
- cross-system checks;
- Roguelite build rules.

But these appeared as design guidance after the object had effectively been scoped.

Therefore a wrongly narrow object could still receive a sophisticated but incomplete answer.

## Fix

Canonical flow is now:

`Classify -> System Context -> Decision Boundary -> Success Bar -> Evidence -> Workflow -> Domain Gates -> Adversarial -> Verification`

New mandatory distinction:

- **System Context** answers what the owning system does in the whole game/session.
- **Decision Boundary** determines whether the current request is Local/System/Cross-system.
- **Decision Object** is chosen only inside that validated boundary.

## System Context Map

For non-trivial design/rework:

`System Job -> Loop Layer -> Entry -> Inputs -> Internal Phases -> Outputs -> Upstream -> Downstream -> Feedback -> Session/Meta Consequence -> Fixed Rules`

## Target case

Prompt:

> 挑战副本原来39波，现在改成30波。帮我重新设计30波的波次表，先把每波怪物和三选一安排好。

### Required behavior

Before authoring per-wave rows, identify the design object as the whole Run/Session if the count change affects:

- total duration;
- Fight / Decision / Reward / Recovery / Special slot budget;
- skill/attribute/special-system opportunity count;
- build Seed / Engine / Scaler / Stabilizer / Capstone timing;
- boss cadence;
- power spikes;
- RNG guarantees;
- reward budget;
- cognitive load;
- failure/recovery.

Then project the session contract down to individual waves.

### Fail behavior

Immediately producing 30 wave rows and only adding a generic “also consider rewards/Boss/build” note afterwards.

That is still local-first reasoning.

## Counter-test — do not become globally obsessive

Prompt:

> 30波结构、Boss、奖励、Build节奏都已经定稿并验证。只修第8波显示名称的一个错别字。

Required behavior:
- Local;
- no full session redesign;
- only verify the affected content/text surface.

## Acceptance

This fix passes only if both are true:

1. broad structural changes trigger whole-system understanding **before** design;
2. genuinely isolated changes remain local.

The goal is correct boundary selection, not maximum scope.
