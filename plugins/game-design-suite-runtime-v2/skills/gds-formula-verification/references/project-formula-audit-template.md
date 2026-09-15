# Project Formula Audit Template

用于把本项目的每一条关键公式整理成可持续维护的审计记录。

## Formula Card

```markdown
# Formula: <Formula ID>

## Purpose
- 设计目的：
- 使用场景：
- 不适用场景：

## Evidence
- Design Doc：
- Config：
- Code：
- Runtime/Test：
- 当前最高证据等级：

## Variables
| Symbol | Project Field | Meaning | Unit | Min | Max | Source |
|---|---|---|---|---:|---:|---|

## Current Formula
```text
...
```

## Block Decomposition
- Base：
- Additive Bucket：
- Multiplicative Bucket：
- Defense：
- Resistance：
- Vulnerability：
- Reduction：
- State：
- Special：

## Clamp / Round
- Clamp：
- Rounding：
- Integer/Float：
- Overflow Risk：

## Timing
- 读取时机：
- Snapshot / Dynamic：
- 每 Hit / 每 Skill / 每 Tick / 每回合：

## Test Vectors
| Case | Inputs | Hand Calc | Code/Runtime | Delta | Result |
|---|---|---:|---:|---:|---|

## Boundary Tests
- Zero：
- Min：
- Max：
- Breakpoint：
- Extreme Stack：
- Invalid Input：

## Sensitivity
- +1% ATK：
- +1% DMG：
- +1% PEN/DEF Shred：
- +1% Speed/Interval：
- 其他：

## Reference Comparison
- HSR pattern：
- ZZZ pattern：
- 只借鉴什么：
- 明确不照抄什么：

## Findings
1. ...

## Candidate Changes
1. ...

## Validation Plan
1. ...
```

## 推荐 Formula IDs

```text
Combat.Player.DirectDamage
Combat.Player.DotDamage
Combat.Enemy.DirectDamage
Combat.Heal
Combat.Shield
Combat.DefenseMultiplier
Combat.ResistanceMultiplier
Combat.CritExpectedValue
Combat.EffectHit
Combat.AttackInterval
Combat.ActionGauge
Combat.EnergyGain
Combat.Aggro
Combat.SecondaryGauge
Progression.HeroLevelStat
Progression.StarPowerDelta
Economy.ResourceDailyNet
```

Formula ID 应表达职责，不绑定某个具体英雄，英雄专属公式再追加命名空间，例如：

`Hero.BigBear.CounterDamage`
