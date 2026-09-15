# Itemization Architecture

Use this reference when designing or auditing an equipment/item system at the system level.

## Core chain

`Itemization Job -> Slot Architecture -> Budget -> Affix Structure -> Acquisition -> Replacement -> Salvage -> Build Ecology -> Validation`

Do not start from a rarity table or random affix count before deciding what the item system is supposed to do for the player.

## 1. Itemization jobs

An item system may serve one or more jobs:

- progression;
- build expression;
- encounter adaptation;
- loot excitement;
- collection;
- economy loop;
- live-content refresh;
- role specialization.

If two jobs conflict, state the trade-off. Example: highly deterministic progression improves planning but can reduce loot surprise.

## 2. Slot roles

Each slot should have a reason to exist. Compare slots by:

- power contribution;
- decision type;
- replacement cadence;
- randomness;
- role/character dependency;
- unique mechanics.

A slot that has no independent decision axis may be redundant.

## 3. Power budget decomposition

A practical analysis frame:

`Item Power = Base + Main Stat + Substat/Affix + Unique/Set Effect - Condition/Constraint Cost`

Never assume the components are directly additive in runtime power. Convert them to a shared benchmark metric with balance validation.

Possible benchmark outputs:

- DPS delta;
- burst delta;
- EHP delta;
- action/cast delta;
- resource delta;
- encounter coverage;
- build enabling value.

## 4. Vertical vs horizontal value

Separate:

### Vertical power
Directly makes the character stronger.

### Horizontal power
Changes targeting, resource use, rotation, control, range, utility or encounter response.

A healthy system does not require every new item to be vertically stronger than old items. Horizontal sidegrades are a major defense against power creep.

## 5. Quality ladder

Rarity/quality can alter one or more dimensions:

- base stat budget;
- affix count;
- affix tier;
- roll range;
- enhancement cap;
- unique effects;
- set eligibility;
- deterministic targeting options.

Avoid increasing all dimensions at once unless the project deliberately wants steep rarity dominance.

## 6. Main-stat architecture

Main stats should be few enough to read and broad enough to create distinct build directions.

Check:

- does each main stat serve a real build;
- does one stat dominate because of the underlying formula;
- are flat and percentage versions both meaningful across progression;
- do slot restrictions create meaningful planning or arbitrary frustration;
- are utility main stats real choices rather than traps.

## 7. Affix architecture

Each affix should have:

- intended users/builds;
- eligible slots;
- budget tier;
- weight;
- min/max roll;
- exclusion group;
- rarity/item-level gate;
- expected frequency;
- failure/dead-roll risk.

Affix count is not diversity. Diversity requires multiple competitive build paths.

## 8. Build-enabling items

Some items should be evaluated by whether they unlock a build, not just raw DPS.

Useful categories:

- engine item;
- payoff item;
- stabilizer;
- utility/counter item;
- capstone;
- flexible filler.

A build-enabling item can have lower standalone power if its synergy is deliberate and has opportunity cost.

## 9. Set architecture

Set bonuses consume flexibility. Evaluate:

`Set Effective Value = Raw Set Value - Flexibility Loss - Slot Lock Cost`

A strong set is acceptable if the player can rationally choose a high-quality off-set piece or another set under relevant conditions.

## 10. Signature/unique equipment

Check whether the item:

- completes a character or merely amplifies them;
- repairs an artificial weakness;
- has generic users;
- creates mandatory ownership pressure;
- invalidates alternative builds;
- changes gameplay in a visible way.

Prefer meaningful play-pattern differentiation over pure multiplier stacking when the product goal supports it.

## 11. Replacement architecture

Define expected replacement cadence by phase:

- onboarding;
- early progression;
- midgame;
- endgame;
- post-endgame/live season.

Too-fast replacement destroys attachment and makes enhancement feel wasteful. Too-slow replacement removes loot excitement.

## 12. Inventory state model

An item can be:

- immediate upgrade;
- sidegrade;
- niche/counter piece;
- future-build piece;
- crafting input;
- salvage/sell candidate;
- collection item.

If almost every non-BiS drop is instantly trash, the system has poor inventory state diversity.

## 13. Build ecology checks

At scale, inspect:

- Character x Item;
- Build x Item;
- Item x Encounter;
- Slot competition;
- Set overlap;
- unique-effect overlap;
- top-item concentration;
- BiS lock rate;
- obsolete-item rate;
- power-creep trend.

## 14. Cross-genre guard

Do not assume every project needs:

- random affixes;
- six rarity tiers;
- item levels;
- sets;
- reforging;
- salvage;
- dedicated weapons.

Itemization should match the game's core loop, session length, content cadence, player agency and business model.

## 15. Done criteria

A mature itemization architecture has explicit answers for:

- why items exist;
- why each slot exists;
- how item power is budgeted;
- how randomness works;
- how players target desired items;
- how items are replaced;
- what happens to bad/old items;
- how builds remain diverse;
- how future content avoids mandatory power creep.
