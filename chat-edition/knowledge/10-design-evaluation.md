# Game Design Suite Chat Edition — Design Decision & Review Engine

> Use when creating, revising, or reviewing a game system where trade-offs matter.

## Phase 1 — Design Intent

Define:
- player fantasy / desired behavior;
- system job;
- target player decision;
- scope;
- Fixed Rules;
- success criteria.

A feature without a clear job is a candidate for removal, not automatic expansion.

## Phase 2 — Current Constraint Map

For existing projects, collect only constraints that can change the decision:
- combat formula;
- content cadence;
- economy;
- progression;
- UI/UX;
- implementation;
- live-ops/production scope.

Separate:
- hard constraints;
- soft preferences;
- assumptions.

## Phase 3 — Candidate Approaches

For significant decisions, generate 2–3 credible approaches.

Each candidate should specify:
- rule/mechanic;
- player-facing consequence;
- quantitative or structural cost;
- implementation cost;
- main risk.

Avoid cosmetic variants that are effectively the same solution.

## Phase 4 — Comparative Evaluation

Compare candidates against:
- clarity;
- depth;
- agency;
- pacing;
- balance stability;
- content burden;
- economy impact;
- exploit/degenerate risk;
- scalability;
- maintainability.

When numbers matter, use a model rather than adjectives.

## Phase 5 — Failure Modes

Actively search for:
- dominant strategy;
- mandatory tax;
- progression hostage;
- dead choice;
- fake choice;
- power cliff;
- infinite/near-infinite loop;
- sunk-cost trap;
- reward invalidation;
- player confusion;
- content obsolescence;
- cross-system contradiction.

A design that works only under average conditions is not finished.

## Phase 6 — Lifecycle Check

Test the recommendation at:
- onboarding/early game;
- mid game;
- late game;
- endgame or long-term repeat play.

Ask whether the same rule remains healthy as:
- stats scale;
- roster grows;
- item pool expands;
- resource inventory accumulates;
- content difficulty rises.

## Phase 7 — Decision

Choose a candidate only after comparison.

State:
- chosen approach;
- rejected alternatives and key reason;
- evidence level;
- risks retained;
- what would make you reverse the decision.

## Phase 8 — Validation Plan

Specify how to validate:
- spreadsheet model;
- simulation;
- config audit;
- code verification;
- playtest;
- telemetry;
- A/B experiment;
- cohort/retention data.

Do not call a design “validated” when only a theoretical model exists.
