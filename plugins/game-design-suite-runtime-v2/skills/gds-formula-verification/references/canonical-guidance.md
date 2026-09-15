# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 游戏公式验证

本 Skill 的职责不是“拍一个看起来合理的公式”，而是把公式变成**可追溯、可复算、可与代码/配置交叉验证、可做边界测试**的生产资产。

涉及公式审计时，优先读取：

- [Formula Audit Method](formula-audit-method.md)
- [HSR Formula Reference](hsr-formula-reference.md)
- [ZZZ Formula Reference](zzz-formula-reference.md)
- [Formula Source Map](formula-source-map.md)

## 强制用户可见输出协议（MUST）

无论用户是否提醒，每一个独立公式结论、公式差异、推导、反例、边界问题或修改建议之前，都先显示：

```text
【本次专业视角】
主责：公式 / 数值验证（formula-verification）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `code-verification`：确认公式在代码里实际怎么写、执行顺序、Clamp、Round、类型转换；
- `config-audit`：确认公式输入字段、配置值、单位和默认值；
- `balance-design`：判断公式产生的强度曲线、收益率和数值区间是否合理；
- `combat-design`：确认公式是否符合战斗规则、窗口、Target、状态机；
- `skill-design`：确认技能公式的 Source/Target/Trigger 与设计意图一致；
- `progression-design`：确认等级、突破、星级等成长公式；
- `economy-design`：确认价格、资源流速、兑换等经济公式。

如果当前结果只是“代码实际上怎么执行”，应切换 `code-verification` 主责；如果只是“这个倍率是否平衡”，切换 `balance-design` 主责；如果只是“字段填错”，切换 `config-audit` 主责。

## 1. 先建立 Formula Identity

任何公式在验证前先锁定身份：

| 字段 | 必填内容 |
|---|---|
| Formula ID | 稳定名称，例如 `PlayerDamage.Physical` |
| Purpose | 这个公式解决什么问题 |
| Scope | PVE/PVP、普通攻击/技能/DoT、客户端/服务器等 |
| Source of Truth | 设计文档、代码、配置、运行时日志 |
| Inputs | 输入变量 |
| Units | 百分比/整数/秒/帧/点数等 |
| Output | 输出意义与单位 |
| Order | 运算顺序 |
| Bounds | Clamp/Min/Max |
| Rounding | floor/ceil/round/truncate |
| Timing | 结算时机 |
| Snapshot | 快照还是动态读取 |
| Owner | 谁维护公式 |

如果连 Formula Identity 都没有锁定，不进入“这个公式合理不合理”的阶段。

## 2. 先还原真实公式，再讨论设计

证据优先级：

`verified-runtime > verified-code > verified-config > confirmed design > supported-inference > candidate`

若用户给了代码：

1. 找输入字段；
2. 找解析；
3. 找中间变量；
4. 找运算顺序；
5. 找 Clamp/Round；
6. 找最终 Consumer；
7. 写成数学表达式；
8. 用测试向量复算。

不得仅根据字段名或历史文档猜公式。

## 3. 公式审计的七层检查

### A. Algebra / 代数正确性

- 括号是否正确；
- 加算/乘算是否放错层；
- 分母是否可能为 0；
- 负数是否允许；
- 百分数是否重复除以 100；
- 是否存在整数除法、溢出、精度损失。

### B. Dimension / 单位一致性

检查：

- 秒 vs 毫秒 vs 帧；
- 百分比 `20` vs `0.2`；
- 伤害点数 vs 倍率；
- 攻速 vs 攻击间隔；
- 角度/距离/格子；
- 等级系数与实际等级。

单位不一致时，先修单位，不进入平衡判断。

### C. Domain / 定义域

对每个输入给出：

- 最小值；
- 最大值；
- 合法范围；
- 空值/0/负值；
- 极端 Buff/叠层后范围。

### D. Monotonicity / 单调性

确认设计上应该“越高越强”的变量是否真的单调。

例如：

- 攻击力增加不应在某区间降低伤害；
- 减伤增加不应产生负承伤；
- 速度增加不应因为取整导致长期反向收益，除非有明确 Breakpoint；
- 防御穿透超过目标防御后如何处理必须明确。

### E. Marginal Value / 边际收益

检查一阶变化：

`ΔOutput / ΔInput`

关注：

- 线性；
- 递增收益；
- 递减收益；
- 阈值跳变；
- 软上限/硬上限；
- 乘区稀释；
- 多乘区是否形成爆炸增长。

### F. Boundary / 极端边界

至少测试相关项：

- 0 攻击 / 0 防御；
- 100% 暴击；
- 暴击率 >100%；
- 抗性 <0 / >100%；
- 减伤 =100% / >100%；
- 攻速极高 / 攻击间隔趋近 0；
- 大量叠层；
- 多 Buff 同层叠加；
- 目标死亡/无敌/复活；
- Gauge 已满/已空；
- 资源溢出；
- 同帧多次触发。

### G. Inversion / 反解

必要时反解公式，例如：

- 想让 TTK=20s，需要多少 DPS？
- 想保证 95% 命中，需要多少 Effect Hit？
- 想在 60s 内多行动 1 次，需要多少速度？
- 想把承伤降到 70%，需要多少防御/减伤？

反解有助于发现公式是否支持策划目标。

## 4. 乘区与顺序必须显式化

任何复杂伤害公式都优先写成乘区链，而不是一句“攻击×倍率”。

推荐抽象：

`Final = Base × Crit × DamageBonus × Defense × Resistance × Vulnerability × Mitigation × State × Special`

项目可以有不同乘区，但必须明确：

- 同乘区内是加算还是乘算；
- 不同乘区之间是否相乘；
- Clamp 在乘区前还是后；
- 取整发生在哪一层；
- 是否对 DoT/Break/反击/追击区别处理；
- Buff 读取快照还是动态属性。

## 5. 概率公式不能只看期望值

有随机时至少同时检查：

- 单次概率；
- EV；
- 方差；
- 连续 N 次失败/成功概率；
- P50/P90/P95；
- 保底/伪随机；
- 多段独立判定 vs 一次总判定；
- 暴击/命中是否每段单独 Roll。

例如多段命中：

`P(at least one success) = 1 - Π(1 - p_i)`

不要用“平均命中率”替代真实分布。

## 6. 行动与时间公式必须同时看离散结果

对于速度、攻击间隔、CD、行动条：

- 连续数学值只是中间结果；
- 最终价值往往由“是否多一次行动/多一次技能/多一次 Boss 窗口”决定。

因此必须报告：

- Continuous Value；
- Discrete Breakpoint；
- Realized Actions / Casts；
- Overcap/Waste。

## 7. Snapshot / Dynamic 是公式的一部分

对于 DoT、异常、Buff、护盾、治疗持续效果，必须确认：

- 施加时快照哪些属性；
- Tick 时重新读取哪些属性；
- 目标侧抗性/易伤何时读取；
- 多个角色共同贡献时如何加权；
- Buff 到期后已生成实例是否变化。

如果代码/资料没有证据，不猜。

## 8. 参考游戏公式只做 Pattern Comparator

崩铁、绝区零等外部公式只能用于：

- 识别常见乘区拆法；
- 学习防御/抗性/命中/行动等建模方式；
- 对照边际收益和 Breakpoint；
- 寻找反例和压力测试场景。

禁止：

- 因为参考游戏这么算，就直接要求本项目照抄；
- 把社区理论计算当官方源码事实；
- 忽略本项目节奏、等级、属性规模和目标体验；
- 用参考游戏当前版本数值反推本项目必然合理区间。

## 9. 与代码交叉验证

当代码可用时，推荐最短链：

`Config/Input -> Data Model -> Parser -> Formula Function -> Clamp/Round -> Runtime Consumer -> Final Result`

输出至少说明：

- 文件/类/方法；
- 公式原文；
- 还原后的数学表达式；
- 示例输入；
- 代码输出；
- 手算输出；
- 是否一致；
- 误差来源。

## 10. Test Vector / 测试向量

每个关键公式至少准备：

1. Normal Case；
2. Zero/Empty Case；
3. Lower Bound；
4. Upper Bound；
5. Breakpoint Case；
6. Extreme Stack Case；
7. Regression Case。

若是概率/随机公式，增加 Monte Carlo 或枚举验证。

## 11. 输出规范

每个公式结论建议使用：

| Formula | 当前公式 | 问题 | 证据 | 影响 | 候选公式 | 状态 | 验证 |
|---|---|---|---|---|---|---|---|

复杂公式附：

- Variable Table；
- Formula Blocks；
- Unit Table；
- Test Vectors；
- Boundary Results；
- Sensitivity / Breakpoint；
- Code Cross-check。

## 12. 证据状态

优先使用：

- `verified-formula-design`：正式设计公式明确；
- `verified-config`：输入/参数由真实配置确认；
- `verified-code`：代码公式和执行顺序已确认；
- `verified-runtime`：实际运行/日志复现；
- `supported-inference`：多项证据支持但未直接验证；
- `candidate`：候选公式；
- `unverified`：缺必要证据；
- `externally-blocked`：当前环境无法继续。

不要因为手算结果“看起来对”就标 `verified-runtime`。

## 13. 典型反模式

- **Formula-by-Intuition**：公式靠经验拍，没有目标和边界；
- **Math Washing**：用复杂公式掩盖错误设计；
- **Hidden Bucket**：文档写加算，代码实际乘算或反之；
- **Percent Unit Bug**：20 与 0.2 混用；
- **Integer Division Bug**：整数除法把比例截断；
- **Order-of-Operations Drift**：文档与代码括号不同；
- **Unbounded Multiplier**：乘区无上限导致极端组合爆炸；
- **Negative Defense Leak**：穿透后负防御未定义；
- **Over-100 Probability**：概率未 Clamp；
- **Snapshot Ambiguity**：持续效果快照规则不明确；
- **Reference Copying**：把参考游戏公式直接复制成本项目；
- **Average-only Validation**：只看均值不看分布和极端值；
- **Spreadsheet = Runtime**：表格算对就声称实现正确。
