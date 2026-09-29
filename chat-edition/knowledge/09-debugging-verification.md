# Game Design Suite Chat Edition — Debugging & Verification

> Use for bugs, build failures, implementation mismatches, config/code disagreement, and completion claims.

## Iron Rules

- No final fix before root-cause investigation.
- No “fixed / passed / complete” claim without fresh evidence.
- One hypothesis, one smallest test.
- Fix at the source when possible, not at the visible symptom.

## Phase 1 — Reproduce and Bound

Record:
- exact symptom/error;
- reproduction steps;
- frequency;
- affected scope;
- recent changes;
- environment/version;
- what is known to still work.

If it cannot be reproduced, gather evidence instead of guessing.

## Phase 2 — Trace the Failure Chain

For multi-layer game systems, trace boundaries explicitly.

Typical chain:
`Config → Generated Data → Loader → Parser → Condition → Runtime Consumer → Target/Object → UI/Result`

At every boundary ask:
- what entered;
- what exited;
- whether defaults changed the value;
- whether the branch actually executed.

For config issues, lock field identity before interpreting values.

## Phase 3 — Compare Working vs Broken

Find the nearest working analogue in the same project.

List meaningful differences:
- config row/field;
- level/star mapping;
- Target/Selector;
- Buff/Attach object;
- enum/parser;
- state/condition;
- client/server authority;
- initialization/order;
- null/default behavior.

Do not discard small differences without evidence.

## Phase 4 — Single Hypothesis

Write a concise testable statement:

> X is the likely root cause because Y evidence shows the failure starts at Z boundary.

Then design the smallest test that can falsify it.

Do not apply several candidate fixes simultaneously.

## Phase 5 — Minimal Fix

Once the root cause is supported:
- change the smallest necessary code/config;
- preserve unrelated formatting and behavior;
- keep user Fixed Rules;
- add guard/assert/log/test only where it protects the diagnosed path.

For code responses, follow Code Output Integrity: original one-line code stays one physical line unless the original or syntax requires otherwise.

## Phase 6 — Verification Before Completion

Before saying the issue is fixed:

1. Re-run the original reproduction.
2. Verify the intended path/value.
3. Check the nearest regression risk.
4. Read actual result/output, not expectation.
5. Only then use completion language.

Examples:

- Build success requires actual build exit success.
- Bug fixed requires original symptom no longer reproduces.
- Config corrected requires the exact current field/value to be re-read.
- Code semantics verified does not equal runtime verified.
- A test existing does not prove it fails before the fix and passes after it.

## Completion Claim Matrix

| Claim | Required evidence |
|---|---|
| Config fixed | Current table tuple shows corrected value |
| Code fixed | Correct source path + successful targeted validation |
| Runtime fixed | Reproduction/log/runtime behavior confirms |
| Regression protected | Targeted test reproduces old failure and now passes |
| Build passes | Fresh build output/exit state |
| Requirement complete | Acceptance checklist reviewed against output |

If evidence is unavailable, say what is changed and what remains unverified.
