# Formula Verification Regressions

用于防止公式 Skill 退化成“套公式/拍公式/拿参考游戏硬套本项目”。

## Case 1 — 先还原再评价

Prompt：

> 这段伤害代码公式合理吗？

Expected：

- 先还原真实数学表达式；
- 记录 Clamp/Round/单位/顺序；
- 再谈合理性；
- 代码事实标 `verified-code`，平衡结论保持 `candidate`，除非有更强证据。

Fail：

- 没看代码就直接给候选公式；
- 把注释当真实执行逻辑。

## Case 2 — 百分比单位错误

Data：

```text
DamageBonus = 20
公式写成 Final = Base * (1 + DamageBonus)
设计文档说 20 代表 20%
```

Expected：指出 `20` 与 `0.2` 单位约定冲突，并优先确认 Parser 是否做 `/100`。

Fail：直接计算成 21 倍且不报警。

## Case 3 — 整数除法

Data：

```csharp
int ratio = current / max;
```

Expected：检查类型和截断，不能只按数学实数除法解释。

## Case 4 — 乘区顺序

Prompt：

> 减防 40%、穿透率 24%、穿透值 9 是直接加起来吗？

Expected：

- 不默认同层；
- 先确认本项目公式；
- 可引用 ZZZ 等外部结构作为 Pattern Comparator；
- 不把参考游戏公式当本项目事实。

## Case 5 — 暴击期望

Prompt：

> 暴击率 60%，暴伤 100%，平均暴击乘区多少？

Expected：若该伤害允许暴击且无特殊规则，`1 + 0.6*1.0 = 1.6`；同时说明这是 EV，不代表每次都 1.6。

## Case 6 — 多段概率

Prompt：

> 5 段攻击，每段独立 30% 概率触发一次控制，至少触发一次的概率？

Expected：`1-(1-0.3)^5`，不能写成 `30%*5=150%`。

## Case 7 — 速度离散化

Prompt：

> 速度从 100 提到 105，强度就是 +5% 吗？

Expected：

- 先区分连续行动频率和真实窗口内离散行动次数；
- 检查 Breakpoint；
- 不直接等价成最终强度 +5%。

## Case 8 — 参考游戏不可硬套

Prompt：

> 崩铁是 10000/SPD，所以我们游戏也改成这个吧。

Expected：拒绝直接照抄；先确认本项目行动条、动画、攻击间隔和目标战斗时长。

## Case 9 — Snapshot vs Dynamic

Prompt：

> DoT 施加后攻击力 Buff 消失，后续 Tick 是否下降？

Expected：如果当前项目代码未提供，标 `unverified`；要求确认 Snapshot / Dynamic 读取时机，不从参考游戏猜。

## Case 10 — Negative Defense

Prompt：

> 防御穿透后 EffectiveDEF=-100，直接放进分母可以吗？

Expected：必须检查 Clamp/定义域/分母安全性和设计意图；不能默认负防合法。

## Case 11 — Formula vs Balance

Prompt：

> 这个公式数学上没 bug，所以角色应该平衡吧？

Expected：明确区分公式正确性和数值平衡。数学正确不能证明 Power Budget 合理。

## Case 12 — Formula vs Runtime

Prompt：

> Excel 算出来和策划文档一致，所以游戏运行肯定没问题。

Expected：Fail 该推论；需要 `code-verification` / `verified-runtime` 才能证明实现一致。

## Case 13 — Per-result Header

Prompt：

> 先验证伤害公式，再确认代码实现，最后判断强度。

Expected：至少拆成：

1. 公式数学结构 -> `formula-verification` 主责；
2. 代码执行事实 -> `code-verification` 主责；
3. 强度判断 -> `balance-design` 主责。

每个独立结果前都有 `【本次专业视角】`。
