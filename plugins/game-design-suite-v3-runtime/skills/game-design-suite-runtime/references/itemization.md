# V3 Module — Itemization

Derived from the canonical `itemization-design` knowledge source. This is a runtime reference module, not a separate Skill.

## 1. Itemization Job

Before designing values, define which jobs the equipment system serves:

- Progression;
- Build Expression;
- Loot Excitement;
- Role Support;
- Encounter Adaptation;
- Collection;
- Economy Loop;
- Seasonal / Live Refresh.

If equipment only adds more HP/ATK with no new decision value, flag `Progression Redundancy`.

## 2. Slot Architecture

Every slot needs a distinct decision role. Check:

- slot identity;
- power budget;
- replacement cadence;
- randomness;
- role dependency;
- whether one answer dominates the slot.

More slots do not automatically create more depth.

## 3. Item Power Budget

Use as an analysis framework:

`Total Item Budget = Base Stat Budget + Affix Budget + Special Effect Budget + Set/Collection Budget - Constraint/Condition Cost`

Do not treat this as a universal game formula.

Budget must be tied to a current-project Benchmark. Check fixed vs percentage scaling, diminishing/increasing returns, breakpoints, uptime, reliability, applicability and double/triple scaling.

Never assume a universal `ATK:DEF:HP` exchange ratio.

## 4. Base / Main / Substat

Separate:

- Base Stat: native slot/rarity identity;
- Main Stat: primary equipment choice axis;
- Substat/Affix: build differentiation and pursuit.

Check:

- whether main stats create real choices;
- whether substats merely repeat the main stat;
- whether flat stats become dead late-game;
- whether percentage stats scale without bound;
- whether rare stats are secretly mandatory;
- Dead Affix rate.

## 5. Affix Pool

For every affix define:

- eligible slots;
- tier;
- min/max roll;
- weight;
- mutual-exclusion group;
- required/forbidden tags;
- duplicate rule;
- rarity gate;
- item-level gate;
- roll count;
- upgrade-roll rule.

Evaluate Power, Frequency, Compatibility, Readability, Search Space, Dead Roll Rate and False Choice.

## 6. Roll Model

Define whether rolls are discrete tiers or continuous ranges, initial roll count, upgrade roll behavior, weighting, pity/correction, lock/reforge rules and whether players can read good vs bad rolls.

Do not evaluate only EV. Also evaluate P50/P90/P95 graduation time, bad-luck tails, usable item rate and best-in-slot probability.

## 7. Quality / Rarity

Rarity may change:

- base budget;
- affix count;
- affix tier;
- roll range;
- enhancement cap;
- unique effect;
- set access;
- rule modification.

Avoid increasing every dimension at once unless deliberate. Check whether lower rarity has transition value and whether new rarity invalidates the old inventory instantly.

## 8. Enhancement

Design:

- cap;
- per-level growth;
- milestone levels;
- cost curve;
- success/failure rules if any;
- refund/inheritance;
- replacement loss;
- affix growth;
- sunk-cost risk.

Mandatory relationship check:

`Upgrade Power Delta <-> Upgrade Cost Delta <-> Replacement Probability`

If enhancement power is too high, replacement becomes painful. If too low, enhancement is meaningless.

## 9. Set / Unique Effects

Set analysis:

`Set Value = Stat Value + Behavior Change + Synergy Value - Slot Lock Cost - Flexibility Loss`

Check whether sets kill off off-set items, become one-character-only taxes, or create infinite loops/permanent buffs.

Unique/signature equipment should change decisions, rotation, resource, target, trigger, state or team interaction—not only add another multiplier.

## 10. Loot Quality / Actual Upgrade Rate

Never stop at top-level drop rate.

Separate at least:

- item drop rate;
- target slot rate;
- target set rate;
- target main-stat rate;
- usable-affix rate;
- good-roll rate;
- upgrade-compatible rate;
- actual build upgrade rate.

Conceptual fingerprint:

`Actual Upgrade Chance ≈ Drop × Slot × Set × MainStat × UsableAffix × RollQuality`

These factors may not be independent; formal calculation must model actual rules.

A healthy answer to an equipment task must either estimate Actual Upgrade Rate or explicitly state why current evidence is insufficient.

## 11. Replacement / Graduation

Track:

- Time-to-First-Usable;
- Time-to-Upgrade;
- Time-to-Best-in-Slot;
- Replacement Frequency;
- Inventory Obsolescence Rate;
- P50/P90/P95 Graduation Time.

The goal is not maximum drop volume; it is a believable cadence of meaningful upgrades.

## 12. Salvage / Duplicate Economy

Old equipment needs a rational lifecycle: sell, salvage, feed, crafting material, reforge currency, duplicate conversion, collection value.

Do not manufacture a sink merely because inventory accumulates. Verify what role the resource serves.

## 13. Build Ecology / BiS Risk

Check:

- Best-in-Slot concentration;
- Signature Tax;
- Set Prison;
- one-stat dominance;
- role compression;
- universal-best pieces;
- version-driven inventory invalidation.

Healthy itemization creates multiple defensible equipment choices, not only a longer path to one obvious answer.
