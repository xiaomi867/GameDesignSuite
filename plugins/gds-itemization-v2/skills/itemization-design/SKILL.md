---
name: itemization-design
description: 装备与物品化系统 Specialist。用户提出装备槽位、品质、基础属性、主/副词条、Affix、随机Roll、强化、套装、唯一特效、掉落、替换、毕业、分解、回收、BiS、装备Build或装备生态时使用。用于武器、防具、饰品、遗物、符文、芯片、神器等可装备或可构筑物品。
---

# GDS Itemization / V2 Preview

这是 Game Design Suite V2 的独立装备 Specialist Runtime。

优先读取：

- [Itemization Architecture](references/itemization-architecture.md)
- [Affix Budget & Roll Model](references/affix-budget-and-roll-model.md)
- [Loot, Replacement & Salvage Economy](references/loot-replacement-and-salvage.md)
- [Itemization Audit Template](templates/itemization-audit.md)

## 强制用户可见协议

除纯澄清问题外，第一段实质内容必须先显示：

```text
【本次专业视角】
执行入口：GDS Itemization
主责：装备 / Itemization 策划
验证深度：Specialist
```

只有本插件真正完成的装备结论才能标为 Specialist 已执行。

如果结论需要数值、经济、模拟、代码或配置等其他专业深度验证，明确写：

```text
后续专家验证：Balance / Economy / Simulation / Config / Code / Meta
```

不得假装另一个 Specialist 已经动态执行。

## 1. Itemization Job

设计任何装备系统前，先定义装备系统究竟承担什么：

- Progression；
- Build Expression；
- Loot Excitement；
- Role Support；
- Encounter Adaptation；
- Collection；
- Economy Loop；
- Seasonal / Live Refresh。

如果装备只是在已有成长外再叠一层“更多攻击/生命”，但没有新的决策或体验价值，先标记 `Progression Redundancy` 风险。

## 2. Slot Architecture

每个槽位必须有明确职责。

至少检查：

- Slot 的决策类型；
- Power Budget；
- Replacement Cadence；
- Randomness；
- Role dependency；
- 是否存在唯一正确答案。

槽位数量多不自动等于装备系统深。

## 3. Item Power Budget

分析框架：

`Total Item Budget = Base Stat Budget + Affix Budget + Special Effect Budget + Set/Collection Budget - Constraint/Condition Cost`

该式不是跨项目固定公式。

必须明确：

- 属性预算来自哪个 Benchmark；
- 固定值与百分比是否跨阶段同价；
- Breakpoint / Cap；
- Uptime / Reliability / Applicability；
- Double / Triple Scaling；
- 条件成本和机会成本。

禁止把固定 `ATK:DEF:HP` 比例直接当装备预算真理。

## 4. Base / Main / Substat

区分：

- **Base Stat**：装备天然价值与槽位身份；
- **Main Stat**：主要选择轴；
- **Substat / Affix**：Build差异、随机性和追求空间。

检查：

- 主属性是否形成真实选择；
- 副属性是否只是继续堆主属性；
- Flat 与 Percent 是否在不同阶段失效或失控；
- 是否存在 Dead Affix；
- 主/副词条是否允许重复及其风险。

## 5. Affix Pool

每个词条至少定义：

- Eligible Slots；
- Tier；
- Min/Max Roll；
- Weight；
- Mutual Exclusion / Group；
- Required/Forbidden Tags；
- Duplicate Rule；
- Rarity Gate；
- Item Power / Level Gate；
- Roll Count；
- Upgrade Roll Rule。

同时检查 Power、Frequency、Compatibility、Readability、Search Space、Dead Roll Rate、False Choice。

词条数量不等于Build多样性。

## 6. Roll Model

随机词条必须说明：

- 离散档位还是连续区间；
- 初始Roll数；
- 强化时新增还是强化旧词条；
- 权重；
- Tier；
- 互斥；
- 保底/纠偏/定向；
- 锁词条/重铸；
- 玩家如何判断好Roll与坏Roll。

随机系统不能只看均值，至少关注：

- usable-item probability；
- good-item probability；
- near-BiS probability；
- exact-BiS probability；
- P50 / P90 / P95 graduation；
- bad-luck tail。

## 7. Quality / Rarity Ladder

品质差异可来自：

- Base Budget；
- Affix Count；
- Affix Tier；
- Roll Range；
- Enhancement Cap；
- Unique Effect；
- Set Access；
- Rule Modification。

不要默认品质每提升一级就在所有维度同步大幅变强。

检查低品质过渡价值、高品质碾压、品质与获取成本、低品质极品与高品质垃圾装之间的关系。

## 8. Enhancement

强化系统要同时定义：

- 上限；
- 每级增长；
- 关键节点；
- 消耗；
- 成功/失败；
- 返还/继承；
- 换装损失；
- 词条变化；
- Sunk Cost Trap。

必须验证：

`Upgrade Power Delta <-> Upgrade Cost Delta <-> Replacement Probability`

典型风险：

- 强化太强 -> 不愿换装；
- 强化太弱 -> 系统无意义；
- 继承损失太大 -> 换装惩罚；
- 成本暴涨收益线性 -> 后段纯税。

## 9. Set Bonus

分析：

`Set Value = Stat Value + Behavior Change + Synergy Value - Slot Lock Cost - Flexibility Loss`

检查：

- 2/4/6件门槛；
- Set Prison；
- 是否压死散件；
- 是否只服务单一角色；
- 是否与角色循环真实交互；
- 是否制造无限资源/永久Buff；
- 环境变化是否让整套装备失效。

## 10. Unique / Legendary / Signature

先定义唯一特效改变的是：

- Multiplier；
- Target；
- Trigger；
- Resource；
- Rotation；
- State；
- Team Hook；
- Encounter Response。

专属装备必须检查：

- 没有它角色是否完整可玩；
- 是否修复人为缺陷；
- 是否形成 Signature Tax；
- 通用装备是否仍然有意义。

## 11. Loot Quality / Actual Upgrade Rate

掉落不能只给“橙装5%”。

至少拆：

`Drop -> Slot -> Set/Family -> Main Stat -> Usable Affixes -> Roll Quality -> Actual Upgrade`

概念近似：

`Actual Upgrade Chance ≈ Drop × Slot × Set × MainStat × UsableAffix × RollQuality`

若各层不独立，必须用真实条件概率或模拟。

单层概率看起来都不低，组合后仍可能是极低升级率。

## 12. Replacement / Graduation

回答：

- 多久出现一件新装备；
- 多久出现真实Upgrade；
- 旧装备平均服役多久；
- 强化投入多久被替换；
- 前中后期替换速度；
- 毕业后还有什么追求。

跟踪：

- Time-to-First-Usable；
- Time-to-Upgrade；
- median item lifetime；
- P50/P90/P95 Graduation；
- exact-BiS（仅在产品确实需要时）。

## 13. Salvage / Duplicate / Crafting

废装备必须有合理去向，但不能为了制造 Sink 强迫分解。

可设计：Sell、Salvage、Feed、Crafting、Reforge Currency、Set Conversion、Target Craft、Collection。

检查：

- 废装是否仍有价值；
- 分解/重铸是否通胀；
- 重复高品质装备是否令人沮丧；
- 定向制作是否摧毁Loot期待；
- 库存压力是否失控。

## 14. Build Ecology

单件装备正常不代表生态健康。

至少检查：

- Character × Item；
- Build × Item；
- Item × Encounter；
- Slot Competition；
- Set / Unique Synergy；
- Best-in-Slot集中；
- Top-N item concentration；
- Signature dependency；
- Pair Lock；
- Build Diversity；
- Power Creep。

## 15. Deterministic vs Random

不强迫所有项目都使用随机词条。

- Deterministic：强调规划与明确成长；
- Randomized：强调Loot和长线刷取，但必须有坏运气保护；
- Hybrid：固定主结构 + 随机副结构/定向纠偏。

先服务目标体验，再决定随机程度。

## 16. Benchmark Contract

比较装备时固定：

- 角色/职业/Build；
- 等级/技能/其他成长；
- 槽位；
- 装备等级/品质；
- 强化等级；
- 主/副词条；
- 敌人/关卡；
- 战斗时间窗；
- 资源/触发状态；
- 是否考虑队友和套装；
- 随机模型/Seed。

不同装备不能在不同Benchmark下直接横比。

## 17. Evidence Boundary

- 规则明确 -> `confirmed`；
- 配置确认 -> `verified-config`；
- 代码确认 -> `verified-code`；
- Runtime确认 -> `verified-runtime`；
- Telemetry确认 -> `verified-data`；
- 新设计 -> `candidate`；
- 模拟 -> Simulation evidence，不等于Playtest。

外部游戏的词条数、掉率、强化曲线、套装倍率只能作为 Reference，不直接复制。

## 18. 反模式

重点识别：

- Stat Soup；
- Fake Choice；
- Dead Affix Pool；
- Best-in-Slot Lock；
- Signature Tax；
- Set Prison；
- Power Creep Ladder；
- Upgrade Hostage；
- Loot Lottery Without Floor；
- Overrandomized Progression；
- Salvage Inflation Loop；
- Universal Stat Ratio；
- Average-only Loot Model。

## 19. 跨专业验证边界

本 Specialist 可以直接完成装备结构和Itemization判断，但以下深度结论应明确标记为“后续专家验证”，而不是假装已经执行：

- 某属性/特效到底强多少 -> Balance；
- 强化/品质/装备等级长期节奏 -> Progression；
- 掉落资源、强化材料、分解和通胀 -> Economy；
- 大规模掉落、毕业时间、极端Roll -> Simulation；
- 多角色BiS集中和版本生态 -> Meta；
- 表字段/权重/随机池 -> Config Audit；
- 程序Roll/继承/重铸/触发 -> Code Verification。

## 20. Done Criteria

一次完整Itemization任务按需交付：

- Itemization Job；
- Slot Architecture；
- Quality/Rarity Ladder；
- Base/Main/Substat；
- Attribute/Power Budget；
- Affix Pool与Roll；
- Enhancement；
- Set/Unique；
- Drop/Targeting；
- Replacement/Graduation；
- Salvage/Duplicate；
- Build/Meta风险；
- Validation Plan；
- Evidence State。
