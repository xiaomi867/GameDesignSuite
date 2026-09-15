# Shared Evidence Contract

This reference defines the evidence discipline shared by all V3 modules.

## Evidence States

Use only when supported:

- `confirmed`
- `supported-inference`
- `candidate`
- `assumed`
- `unknown`
- `verified-config`
- `verified-code`
- `verified-runtime`
- `verified-data`
- `not-yet-playtested`
- `externally-blocked`
- `unverified`

## Core Rules

1. Spreadsheet calculation, formula derivation and simulation are not Playtest evidence.
2. Existing-project claims must be grounded in actual rules, files, config, code or runtime evidence when the user asks for verification.
3. User-fixed mechanics are treated as Fixed Rules unless the user explicitly reopens them.
4. Newer verified evidence overrides older candidates.
5. Missing evidence must stay missing; do not fill it with a similar game, old schema or guessed parser behavior.

## Decision Object Discipline

Before each formal conclusion, identify what is being decided:

- configuration fact;
- runtime/code meaning;
- numerical strength;
- economy lifecycle;
- progression structure;
- itemization structure;
- hero stat growth;
- design review/root cause.

Do not mix different Decision Objects into one unsupported conclusion.

## Missing Evidence Guard

When critical evidence is unavailable:

1. perform at most one necessary availability check;
2. mark dependent conclusions `unverified` or `externally-blocked`;
3. list the minimum missing evidence;
4. continue independent work;
5. stop at the boundary if the user says not to guess.

## Root-Cause Levels

Check at least:

- Local: field, coefficient, one object;
- System: rules, loop, curve, resources;
- Cross-system: lifecycle, content environment, roster, economy, progression, meta.

Do not patch a local number before confirming the problem is local.
