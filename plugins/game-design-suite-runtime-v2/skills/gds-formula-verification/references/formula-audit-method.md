# Formula Audit Method

用于把“公式看起来没问题”升级为可复算、可回归、可和代码/配置逐层验证的公式审计流程。

## 1. Formula Ledger

每条正式公式建立记录：

| Field | Meaning |
|---|---|
| Formula ID | 稳定唯一名 |
| Owner | 负责专业/模块 |
| Version | 公式版本 |
| Purpose | 设计目的 |
| Input | 输入变量 |
| Unit | 单位 |
| Domain | 合法范围 |
| Formula | 数学表达式 |
| Bucket | 所属乘区/加算区 |
| Clamp | 上下限 |
| Rounding | 取整方式 |
| Timing | 结算时机 |
| Snapshot | 快照/动态 |
| Source | 文档/配置/代码/运行时 |
| Evidence | 证据状态 |

## 2. Formula Reconstruction

如果真实公式来自代码，不要从注释直接抄成公式。

按以下顺序：

1. 找输入变量来源；
2. 找默认值；
3. 找类型转换；
4. 展开中间变量；
5. 保留真实括号；
6. 记录 Clamp；
7. 记录 Round/Floor/Ceil；
8. 记录调用顺序；
9. 记录最终 Consumer；
10. 再整理成数学表达式。

## 3. Symbolic Check

把数值替换成符号，检查：

- 重复乘同一 Buff；
- 忘乘某个乘区；
- 同一变量既在 Base 又在 Bonus 重复计入；
- 分母/分子放反；
- 加法括号位置错误；
- 先 Clamp 还是后 Clamp 导致结果不同。

## 4. Unit Check

推荐给变量标单位：

```text
ATK         [point]
SkillRate   [ratio]
CritRate    [ratio]
Duration    [second]
Interval    [second/action]
Speed       [action-scale]
Damage      [point]
```

如果一个等式左右单位无法解释，应先停下。

## 5. Property Tests

不要只测几个手填数字，至少定义公式应该满足的性质。

例：

- `ATK2 > ATK1` 时，在其他变量不变的直接伤害公式中 `DMG2 >= DMG1`；
- `DamageReduction` 增加时承伤不应增加；
- `CritRate=0` 时 Crit EV 应等于 1；
- `CritRate=1` 时 Crit EV 应等于 `1+CritDMG`；
- `PEN=0` 时结果应退化到基础防御公式；
- `Buff=0` 时公式应退化到无 Buff 版本。

## 6. Sensitivity

用局部变化观察边际收益：

```text
Marginal ~= (F(x + dx) - F(x)) / dx
```

对离散系统还要检查是否跨 Breakpoint。

常见需要 sensitivity 的变量：

- ATK/DEF/HP；
- Crit Rate/Crit DMG；
- DMG Bonus；
- DEF Shred/PEN；
- RES/PEN；
- Speed/Attack Interval；
- Energy Regen；
- Effect Hit；
- Cooldown；
- Stack Count。

## 7. Edge Matrix

推荐至少覆盖：

| Case | Purpose |
|---|---|
| 0 | 退化行为 |
| 1 | 单位输入 |
| Min Legal | 最小合法值 |
| Max Legal | 最大合法值 |
| Just Below Breakpoint | 阈值前 |
| Breakpoint | 阈值点 |
| Just Above Breakpoint | 阈值后 |
| Extreme Stack | 极端组合 |
| Invalid Input | 非法输入处理 |

## 8. Probability Verification

单次独立概率：

`E(successes) = Σp_i`

至少一次成功：

`P(any) = 1 - Π(1-p_i)`

连续 N 次失败（同概率 p）：

`P(all fail) = (1-p)^N`

若存在保底、状态相关概率、伪随机，不能套独立同分布公式。

## 9. Time & Action Verification

对攻击间隔/CD/速度公式同时记录：

- 理论连续值；
- 实际离散行动次数；
- 动画锁/前后摇；
- 队列/插队；
- 资源是否足够；
- 目标是否仍存活；
- 窗口是否仍开放。

`Paper DPS != Realized DPS`，除非这些约束已处理。

## 10. Code Cross-check Template

```text
Formula ID:
Config/Input:
Data Model:
Parser:
Formula Function:
Clamp/Round:
Runtime Consumer:
Manual Test Input:
Manual Expected:
Runtime/Code Output:
Delta:
Evidence:
```

## 11. Reference Comparison

对外部游戏公式只比较结构：

- 有哪些乘区；
- 哪些变量同层加算；
- 哪些变量形成独立乘区；
- 是否有等级压制；
- 是否存在二级 Gauge；
- 概率如何处理抗性；
- 行动频率如何离散化。

不要比较完就说“我们也应该这样”。必须回到本项目目标、属性规模和战斗时长重新推导。
