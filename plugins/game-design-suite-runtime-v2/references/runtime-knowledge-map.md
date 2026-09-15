# Game Design Suite Runtime Knowledge Map

This file maps the eight ChatGPT runtime entry skills to the 24 preserved professional knowledge modules.

The preserved modules under `../skills/` are knowledge sources, not first-level runtime selectors in the consolidated package. Runtime skills may read them directly. Do not claim a preserved module was separately invoked; say it was used as supporting guidance when relevant.

## 1. Core / Systems

- `gds-game-design`
- `gds-game-production`
- `gds-design-frameworks`
- `gds-design-review`
- `gds-game-design-doc`

## 2. Hero & Skill

- `gds-hero-concept-design`
- `gds-hero-kit-design`
- `gds-hero-stat-progression`
- `gds-skill-design`
- `gds-skill-value-design`

## 3. Balance & Simulation

- `gds-balance-design`
- `gds-formula-verification`
- `gds-simulation-design`
- `gds-telemetry-experiment-design`
- `gds-meta-balance`

## 4. Itemization

- `gds-itemization-design`
- `gds-itemization-benchmark`

## 5. Combat

- `gds-combat-design`

## 6. Economy & Progression

- `gds-economy-design`
- `gds-progression-design`

## 7. Level & UX

- `gds-level-design`
- `gds-game-interface-design`

## 8. Audit & Verification

- `gds-config-audit`
- `gds-code-verification`

## Loading Rule

For any selected runtime entry:

1. Read the smallest relevant set of `../skills/<module>/references/canonical-guidance.md` files.
2. Follow links to that module's additional references/templates only when needed.
3. For cross-system work, load supporting knowledge modules directly rather than attempting runtime skill-to-skill invocation.
4. Preserve evidence states and do not upgrade spreadsheet/simulation output into playtest evidence.
5. If required project evidence is missing, state the boundary and continue only with independent candidate work.
