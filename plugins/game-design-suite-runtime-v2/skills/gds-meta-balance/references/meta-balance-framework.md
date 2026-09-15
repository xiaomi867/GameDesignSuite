# Meta Balance Framework

## Core idea

Balance is an ecosystem property. A single object can be numerically reasonable while the overall metagame is unhealthy because of interaction, accessibility, environment, or player-segment effects.

## Minimum data model

For each selectable object track where relevant:

```text
Object ID
Role / Archetype
Pick/Usage
Outcome
Sample Size
Skill Band
Mastery Band
Build/Team
Opponent/Content
Patch/Version
```

## Useful matrices

### Object × Content
Finds whether content systematically excludes or favors archetypes.

### Object × Object
Finds matchups and counters.

### Object × Partner
Finds synergy and pair-lock risk.

### Object × Skill Band
Finds accessibility/high-skill skew.

### Object × Mastery
Finds learning curves.

## Concentration

A solved meta often appears as concentration before extreme win rate.

Useful views:

- top-1 / top-3 / top-5 share;
- viable-pool size;
- HHI: `Σ share_i^2`;
- composition entropy;
- archetype share over time.

No metric has a universal healthy threshold. Compare against the game's intended diversity and historical baseline.

## Matchup polarization

A 50% aggregate object can still be unhealthy if it is extremely favorable into some opponents and extremely unfavorable into others.

Track:

- mean matchup result;
- standard deviation across matchups;
- worst/best matchup;
- frequency of encountering those matchups;
- availability and cost of counterplay.

## Mastery-aware balance

Compare at least:

- novice users of object;
- experienced users of object;
- player global skill buckets.

This prevents confusing "hard to learn" with "weak" and "easy to execute" with "fair at mastery".

## Change classification

Before patching, classify root cause:

1. Raw power
2. Reliability/accessibility
3. Interaction/synergy
4. Resource economy
5. Environment/content
6. Counter structure
7. Information/UX
8. Learning/mastery
9. Sample/data artifact

Different causes require different levers.

## Patch evaluation

For every candidate change predict:

- intended target metric;
- directly affected objects;
- second-order beneficiaries;
- second-order losers;
- expected composition changes;
- possible new dominant strategies;
- metrics that should remain stable.

Then compare predictions with telemetry after release.

## Power creep audit

Maintain a historical reference frame, not only current-relative balance.

Useful longitudinal metrics:

- normalized effective power by release cohort;
- median and top-decile TTK/TTD;
- number of obsolete items/characters;
- old-content completion speed;
- average number of mechanics/conditions required to remain competitive;
- systemic enemy inflation introduced to compensate.
