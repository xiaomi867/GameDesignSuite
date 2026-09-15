# Loot, Replacement & Salvage Economy

Use this reference for acquisition cadence, target farming, replacement speed, graduation time, duplicate value, enhancement-material loops and old-item disposal.

## 1. Acquisition funnel

Separate the probability funnel:

`Drop -> Slot -> Family/Set -> Main Stat -> Affix Quality -> Roll Quality -> Actual Upgrade`

Do not report only top-level rarity drop rate when the real question is upgrade probability.

If layers are dependent, model the true conditional probabilities rather than multiplying independent approximations.

## 2. Targeting systems

Common targeting tools:

- stage-specific drops;
- slot selection;
- set/family selection;
- pity/guarantee;
- crafting;
- exchange shop;
- conversion;
- reroll;
- lock/focus system;
- seasonal selector.

Targeting reduces variance. It should be valued as part of the acquisition system, not treated as a separate convenience feature.

## 3. Replacement curve

Define desired replacement cadence per progression phase.

Track:

- Time-to-First-Usable;
- Time-to-Meaningful-Upgrade;
- median item lifetime;
- enhancement sunk cost at replacement;
- inventory obsolescence;
- endgame upgrade frequency.

A healthy curve often shifts from frequent obvious upgrades early to rarer optimization upgrades later, but this is a pattern, not a universal law.

## 4. Graduation model

Define what “graduated” means before calculating time:

- correct slot only;
- correct set + main stat;
- minimum usable affixes;
- target score threshold;
- near-BiS;
- exact-BiS.

Report P50/P90/P95 where random acquisition matters. Exact-BiS may be intentionally very rare; do not use it as the only progression completion metric unless the product expects that behavior.

## 5. Duplicate value

Duplicates can become:

- upgrade copies;
- limit-break material;
- salvage currency;
- craft ingredients;
- reroll fuel;
- collection progress;
- trade value.

Check whether duplicate value preserves excitement without making duplicate ownership mandatory for baseline viability.

## 6. Salvage value

Salvage should answer:

- how much value does a bad drop retain;
- does salvage meaningfully contribute to future targeting;
- does salvage create inflation;
- does it encourage players to hoard everything;
- is the salvage UI burden reasonable.

Use dedicated economy validation for source/sink and inflation analysis.

## 7. Enhancement inheritance

When replacing items, define how prior investment transfers:

- no inheritance;
- partial refund;
- material refund;
- direct level transfer;
- slot-level enhancement;
- account-level enhancement.

Check the trade-off:

`Attachment to old item` vs `Willingness to equip new item`.

Too little inheritance can make new drops feel like punishment. Full inheritance can make item-specific investment meaningless.

## 8. Crafting and deterministic recovery

Crafting can function as:

- bad-luck protection;
- target completion;
- resource sink;
- build experimentation;
- duplicate conversion.

Do not make deterministic crafting strictly dominate natural drops unless loot excitement is intentionally secondary.

## 9. Inventory pressure

Track:

- items earned per session/day;
- inspection time;
- keep rate;
- salvage rate;
- lock rate;
- inventory cap pressure;
- sorting/filtering burden.

An item system can be numerically balanced and still fail because the player must inspect too many low-value drops.

## 10. Economy loop

A common loop:

`Play -> Drop -> Keep/Salvage -> Upgrade/Craft/Reforge -> Stronger Build -> Harder Content -> Better Drop`

Check for:

- self-amplifying inflation;
- dead-end resources;
- forced sinks;
- resource hostage behavior;
- conversion exploits;
- negative-value drops.

## 11. Seasonal/live refresh

When a new season or tier arrives, decide what happens to existing items:

- remain competitive;
- become sidegrades;
- become upgrade material;
- can be raised to new cap;
- partially reset;
- become legacy collection.

Avoid accidental full-inventory invalidation unless reset is an explicit core promise.

## 12. Telemetry metrics

Useful live metrics include:

- item drop rate by content;
- usable drop rate;
- equip rate;
- replacement rate;
- salvage rate;
- reroll attempts;
- enhancement spend;
- time-to-target-item;
- BiS concentration;
- inventory-cap hit rate;
- abandonment after loot sessions.

Observed player behavior should be segmented by progression, build and spend/engagement only where appropriate and lawful.

## 13. Anti-patterns

- rare item with near-zero actual upgrade chance;
- full random stack with no recovery path;
- salvage that returns almost nothing;
- enhancement loss that blocks replacement;
- target crafting so efficient that drops are irrelevant;
- unlimited reroll inflation;
- inventory spam as fake reward volume;
- endgame where every drop is trash except exact BiS.

## 14. Validation handoff

Require dedicated validation when needed for:

- acquisition and graduation distributions;
- resource loops and inflation;
- replacement/upgrade cadence;
- live acquisition and frustration signals;
- item-use concentration and power creep.
