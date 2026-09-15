# Affix Budget & Roll Model

Use this reference when designing substats, affix pools, roll tiers, random stat distribution, reforge rules or item power normalization.

## 1. Affix identity

Each affix should define:

- `AffixId` / stable identity;
- semantic category;
- allowed slots;
- power family;
- tier;
- roll range;
- weight;
- exclusion group;
- rarity/item-level gates;
- build tags;
- stack/cap rules.

Do not infer power from the display name alone.

## 2. Shared budget language

Choose one benchmark-normalized budget unit for design work.

Example process:

1. choose a representative build and encounter;
2. perturb one stat at a time;
3. measure target metric delta;
4. convert to a local budget unit;
5. repeat across early/mid/endgame and multiple archetypes;
6. store a range, not a universal constant.

Possible target metrics:

- DPS;
- burst damage;
- EHP;
- actions per window;
- resource cycle;
- control coverage;
- healing throughput;
- break/gauge throughput.

## 3. Flat vs percent stats

Flat and percentage stats often cross in value over progression.

Check:

- low-level dominance;
- high-level obsolescence;
- scaling with base stats;
- interaction with additive percentage buckets;
- interaction with external buffs;
- breakpoints and caps.

If one representation becomes dead after a narrow level band, consider phase-specific pools or scaling rules.

## 4. Affix tiering

An affix tier can change:

- roll floor;
- roll ceiling;
- weight;
- item-level requirement;
- rarity requirement.

Avoid making higher tiers simultaneously much stronger and much more common on higher rarity items unless steep progression is intentional.

## 5. Roll model

Common models:

### Discrete roll
One of several exact values.

Pros: readable, easy to audit.
Cons: visible tier chasing can dominate loot evaluation.

### Continuous roll
Uniform or shaped interval.

Pros: granular loot.
Cons: harder to communicate and more optimization noise.

### Hybrid
Discrete tier + continuous value inside tier.

Use the simplest model that supports the target loot experience.

## 6. Weight model

Weights can be:

- equal;
- global weighted;
- slot-specific;
- build/tag-aware;
- rarity-aware;
- stateful/pity-aware.

Always distinguish:

`Probability of affix category` from `Probability of a usable item`.

Large pools can make actual upgrade probability extremely low even when each individual weight looks reasonable.

## 7. Exclusion groups

Use exclusion rules for:

- mutually exclusive damage types;
- flat + percent duplicates if undesirable;
- incompatible class stats;
- conflicting unique mechanics;
- duplicate affix families.

But do not overconstrain until every item looks identical.

## 8. Dead-affix rate

Define a usable threshold by build and estimate:

- no-use affix rate;
- one-use affix rate;
- two-use affix rate;
- fully synergistic affix rate;
- item-level usable rate;
- real upgrade rate.

A broad pool with 60% dead affixes can create less practical diversity than a smaller pool with several competitive choices.

## 9. Expected item quality

For random affixes, inspect distribution, not just average budget.

Useful outputs:

- mean total budget;
- median;
- P10/P90/P95;
- usable-item probability;
- good-item probability;
- near-BiS probability;
- exact-BiS probability;
- build-specific probability;
- variance by slot.

## 10. Upgrade rolls

If enhancement adds or upgrades affixes, define:

- trigger levels;
- new-affix vs upgrade-affix probability;
- target selection rule;
- roll increment range;
- duplicate handling;
- max tier/count;
- deterministic guarantees.

A common risk is that a good base item becomes bad only because later upgrades repeatedly hit a low-value affix. Decide whether that frustration is intentional.

## 11. Reforge / reroll

For each reroll system define:

- what is locked;
- what is rerolled;
- cost growth;
- whether old/new result can be chosen;
- pity/guarantee;
- target selection;
- reset behavior;
- account/season caps.

Reroll systems should reduce unacceptable randomness without making natural loot irrelevant.

## 12. Normalization guard

Do not use a single theoretical budget to declare all affixes equal.

Check effective value under:

- multiple roles;
- multiple encounters;
- multiple progression states;
- different existing stat saturation;
- different skill/trigger patterns.

An affix can be budget-equal but strategically unequal.

## 13. Breakpoint stats

Special handling for stats whose value is discontinuous:

- speed / action interval;
- crit cap;
- hit/resist thresholds;
- cooldown reduction;
- resource thresholds;
- set activation;
- proc frequency caps.

Use breakpoint search and local sensitivity rather than smooth linear valuation.

## 14. Randomness fairness guard

Do not label a system fair only because expected value is correct.

Check:

- worst-case tails;
- repeated failure probability;
- visible progress during bad luck;
- target-farming options;
- protection against impossible combinations;
- recovery via craft/reroll/salvage.

## 15. Simulation handoff

When more than two random layers multiply, use `simulation-design` unless an exact analytic solution is simpler.

Minimum simulation outputs:

- N and seed policy;
- usable item rate;
- upgrade rate;
- P50/P90/P95 target time;
- resource cost distribution;
- bad-luck tail;
- sensitivity to each random layer.