# V3 Module — Hero Stat Progression

Derived from the canonical `hero-stat-progression` knowledge source. This is a runtime reference module, not a separate Skill.

## 1. Stat Taxonomy

Before building a level curve, separate:

- Level-Scaled Base Stats: commonly HP / ATK / DEF;
- Fixed or Mostly-Fixed Combat Stats: speed, energy cap, base crit, taunt weight, etc.;
- Ascension / Breakthrough Bonus Stats;
- Node-Based Stats from talent/trace trees;
- Derived Stats such as EHP, DPS and real action frequency.

Do not place every stat into the same level interpolation formula.

## 2. Growth Contract

Before choosing a curve, explicitly define:

- Level Cap;
- breakthrough / ascension levels;
- Lv1 Base;
- LvMax target or target multiplier;
- whether breakthrough directly adds stats;
- whether slope changes by phase;
- bonus-stat timing;
- rarity / role templates;
- fixed stats;
- target content curve;
- intended Power Delta by phase.

Mandatory relationship:

`Power Curve <-> Content Curve <-> Cost Curve <-> Time Curve`

## 3. Curve Families

Choose deliberately among:

### Linear
`V(L) = V1 + k*(L-1)`

### Piecewise Linear
Different slopes between breakthrough phases.

### Multiplier Table
`V(L) = BaseTemplate * LevelMultiplier(L) + AscensionDelta(Phase)`

Useful when many heroes share the same curve shape with different bases.

### Exponential / Power Curve
Use only when long-term numerical space is intentional; validate late-game inflation.

### Hybrid
Base stat multiplier + discrete breakthrough delta + separate bonus-stat nodes.

Do not copy another game's multiplier table without validating the current project.

## 4. Normalized Growth

For cross-hero or cross-phase analysis use:

`Normalized(L) = V(L) / V(Lmax)`

`GrowthFromBase(L) = V(L) / V(1)`

`MarginalGrowth(L) = V(L) - V(L-1)`

`PhaseDelta = V(after ascension) - V(before ascension)`

`PhaseShare = PhaseDelta / V(Lmax)`

These reveal early/late loading, dead levels and power cliffs.

## 5. Roster Stat Envelope

Track at least:

- Min / P25 / Median / P75 / Max;
- within-role distributions;
- within-rarity distributions;
- scaling-source distributions;
- distributions by level phase.

Check whether role identity is explainable without creating hidden power creep.

## 6. Scaling-Source Alignment

Cross-check hero stats against the kit's scaling source:

- ATK damage vs ATK growth;
- DEF scaling that also increases survival;
- HP scaling that affects both survival and healing/damage;
- fixed speed vs intended fast-character identity;
- energy cap vs rotation;
- crit/hit bonus stats vs forced equipment answers.

If one stat improves multiple primary outcomes, ask Balance to evaluate double scaling.

## 7. Breakthrough / Ascension

A breakthrough may contain:

- level-cap increase;
- base-stat jump;
- bonus stat;
- major passive;
- skill-level cap;
- mechanism unlock.

Check for:

- perceptible reward;
- excessive one-point power spike;
- hard usability gates;
- content hard-locks;
- multiple systems exploding at the same node.

Conceptual review:

`TotalPowerDelta = BaseStatDelta + BonusStatDelta + UnlockValue + SkillCapValue`

Do not mechanically add incomparable dimensions without a model.

## 8. Growth Density

Across Lv1~LvMax, inspect each phase for:

- per-level or per-10-level growth;
- breakthrough jumps;
- skill-cap changes;
- passive unlocks;
- equipment/system unlock timing.

Flag:

- Dead Levels;
- Power Cliffs;
- multiple systems spiking on one node;
- early overgrowth that invalidates content;
- late undergrowth that makes leveling feel meaningless.

## 9. Hero Growth Fingerprint

A proper V3 hero-level-growth answer must:

1. establish the Growth Contract;
2. select and justify a curve family;
3. show normalized/marginal or phase growth checks;
4. inspect Growth Density and breakthrough Power Delta;
5. mark proposed values as `candidate` until project formulas/content validate them.
