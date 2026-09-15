# Itemization Design Regression Cases

These cases verify that `itemization-design` behaves as a production Itemization discipline rather than a generic stat-table generator.

## 1. Universal Stat Ratio Must Fail

Prompt:

> Design weapon/armor/boots using ATK:DEF:HP = 1:1:10 because that is the industry standard.

Pass:

- treats the ratio as a candidate/example only;
- asks for or builds a project benchmark;
- derives local exchange rates through combat formulas / marginal value.

Fail:

- accepts 1:1:10 as universal truth.

## 2. Rarity Is Not Automatically More of Everything

Prompt:

> Every rarity should increase base stats, affix count, affix tier, roll range and enhance cap. Is that fine?

Pass:

- checks exponential power stacking and obsolescence;
- distinguishes intentional rarity dominance from accidental compounding.

Fail:

- says yes merely because higher rarity should be stronger.

## 3. Affix Count Is Not Build Diversity

Prompt:

> We have 30 affixes so the system has high build diversity.

Pass:

- checks dead-affix rate, actual usable combinations, dominant stats and build coverage.

Fail:

- equates more affixes with more meaningful choices.

## 4. Top-Level Drop Rate Is Not Upgrade Rate

Prompt:

> Legendary drop rate is 10%, so players should get upgrades often.

Pass:

- decomposes Drop -> Slot -> Set -> Main Stat -> Affix -> Roll -> Actual Upgrade.

Fail:

- uses 10% as the effective upgrade chance.

## 5. Average Graduation Is Not Enough

Prompt:

> Average time to get the target gear is 12 days, so the loot system is healthy.

Pass:

- asks for/estimates P50/P90/P95 and bad-luck tail;
- checks usable vs near-BiS vs exact-BiS definitions.

Fail:

- validates from mean only.

## 6. Enhancement Must Consider Replacement

Prompt:

> Make +20 enhancement very expensive so the system has a strong sink.

Pass:

- evaluates power delta, cost delta, inheritance/refund and replacement probability;
- rejects Sink-for-Sink’s-Sake logic.

Fail:

- simply raises enhancement cost.

## 7. Set Bonus Must Pay for Slot Lock

Prompt:

> A four-piece set gives +25% damage. Is it balanced?

Pass:

- evaluates raw value, uptime, slot lock, flexibility loss, off-set alternatives and build context.

Fail:

- judges from 25% alone.

## 8. Signature Equipment Tax

Prompt:

> This hero feels bad without the signature weapon, but perfect with it.

Pass:

- checks whether signature equipment repairs an artificial baseline defect;
- labels Mandatory Signature / Equipment Tax risk where appropriate.

Fail:

- assumes signature dependency is automatically desirable monetization/design.

## 9. Random Roll Upgrade Event

Prompt:

> The item starts with four good substats but all five enhancement rolls hit the weakest stat. Is that okay?

Pass:

- treats this as a distribution/frustration design question;
- checks roll model, bad-luck tail, reroll/recovery and intended loot experience.

Fail:

- says expected value is unchanged so it is fine.

## 10. Multi-layer Randomness Must Route to Simulation

Prompt:

> Calculate the chance to get the right slot, right set, right main stat, three useful affixes, then roll upgrades into two of them.

Pass:

- uses exact math if simple enough or hands off to `simulation-design`;
- reports distribution/tail and states assumptions.

Fail:

- multiplies unrelated rates without checking dependencies.

## 11. Single Item Balance vs Meta

Prompt:

> Every item looks individually fair but 85% of endgame damage dealers equip the same accessory.

Pass:

- `itemization-design` identifies BiS concentration;
- `meta-balance` becomes primary for ecosystem conclusion.

Fail:

- says each item is individually balanced, so there is no problem.

## 12. Salvage Is Not Automatically a Sink

Prompt:

> Players have too many useless drops, so make salvage cost gold.

Pass:

- diagnoses why drops are useless;
- checks salvage role and economy loop before adding a cost.

Fail:

- adds a tax merely to consume gold.

## 13. Low-quality Gear Must Have a Lifecycle

Prompt:

> Once Epic gear starts dropping, Rare gear is always worthless. Is that acceptable?

Pass:

- checks intended transition phase, salvage/crafting/useful lifecycle and inventory burden;
- allows deliberate obsolescence only if aligned with project goals.

Fail:

- assumes lower rarity should always become worthless.

## 14. Header Routing

Prompt:

> Check the equipment table, confirm the affix weighting code, simulate 10,000 drops, and tell me whether one accessory dominates the meta.

Pass requires separate Result Blocks:

1. config facts -> `config-audit` primary;
2. code weighting semantics -> `code-verification` primary;
3. distribution simulation -> `simulation-design` primary;
4. item structure/usable-rate implication -> `itemization-design` primary where applicable;
5. ecosystem dominance -> `meta-balance` primary.

Fail:

- one Header covers all results;
- `itemization-design` claims ownership of unrelated code/config/runtime evidence.

## 15. Generic Skill Isolation

Prompt:

> Use my private project's weapon tables to improve the public itemization skill.

Pass:

- extracts generic methods only;
- does not copy project names, private IDs, exact formulas, paths, balance values or proprietary rules into the public Skill.

Fail:

- public reference/eval contains project-specific fixtures or private values.