# Game Design Suite Chat Edition — Itemization / Equipment

> Purpose: project knowledge for ordinary Chat mode. This file is NOT a Skill and does not depend on Skill/Plugin runtime.
> Use it for equipment, itemization, affixes, rolls, rarity, enhancement, sets, loot, replacement, salvage, and build ecology.

## Usage
- Use this file when the decision object is equipment/itemization.
- Consult balance, economy/progression, or audit knowledge only when the task truly requires them.
- Do not claim a Skill was invoked.
- Treat unsupported concrete values as candidate until grounded in combat/economy evidence.


---

# Source Module: gds-itemization-design

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# Itemization / 装备与物品化设计

## 强制用户可见输出协议（MUST）

每一个独立装备结构结论、属性预算结论、词条池判断、强化方案、套装/唯一特效判断、掉落/替换结论或Build生态结论前，都必须先显示：

```text
【本次专业视角】
主责：装备 / Itemization 策划（itemization-design）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `balance-design`：属性价值、Power Budget、DPS/EHP/TTK、特殊效果强度；
- `progression-design`：强化、品质、装备等级、突破、长期替换与毕业节奏；
- `economy-design`：掉落、强化成本、分解、回收、商店、重复物价值；
- `simulation-design`：词条分布、毕业时间、掉落概率、Build覆盖和极端组合模拟；
- `meta-balance`：Best-in-Slot集中、角色×装备矩阵、Build垄断、Power Creep；
- `config-audit` / `code-verification`：真实表字段、随机规则、权重、强化/套装实现；
- `skill-design`：装备特效与角色技能循环、触发和Team Hook的关系。

Direct Specialist Entry 仍执行共享 First-Visible-Line / Section Gate / Pre-Send Header Lint。

---

## 1. 先定义 Itemization Job

设计任何装备系统前，先回答它在项目里负责什么：

- **Progression**：提供长期成长与替换；
- **Build Expression**：让玩家形成不同构筑；
- **Loot Excitement**：提供掉落期待和惊喜；
- **Role Support**：强化角色定位；
- **Encounter Adaptation**：针对不同敌人/模式调整；
- **Collection**：收集与完成度；
- **Economy Loop**：制造、强化、分解、交易或资源循环；
- **Seasonal/Live Content**：版本追求和Meta变化。

如果装备只是在已有成长外再叠一层“更多攻击/生命”，但没有新的决策或体验价值，先标记为 `Progression Redundancy` 风险。

---

## 2. Slot Architecture / 槽位架构

每个槽位必须有明确职责，不默认所有槽位都是同一张属性表。

可按项目划分：

- Weapon / Main-hand：输出、技能行为、攻击资源；
- Armor / Body：生存、减伤、抗性；
- Shoes / Boots：速度、移动、行动经济；
- Accessory：功能、暴击、资源、条件强化；
- Relic / Rune / Chip：Build特化、规则修改、套装；
- Class/Character-specific Slot：身份强化，但警惕专属绑定。

至少检查：

- Slot 是否承担不同决策；
- Slot Power Budget 是否合理；
- 是否存在某槽位对总强度贡献过大；
- 某槽位是否只有唯一正确答案；
- 是否出现“所有输出都找同一属性、所有坦克都找同一属性”的伪选择。

---

## 3. Item Power Budget

装备总预算建议拆为：

`Total Item Budget = Base Stat Budget + Affix Budget + Special Effect Budget + Set/Collection Budget - Constraint/Condition Cost`

该式是分析框架，不是跨项目固定公式。

必须明确：

- 每个属性的预算单位；
- 属性价值来自哪个 Benchmark；
- 固定值与百分比是否同价；
- 是否存在边际收益递减/递增；
- 是否跨过攻速、暴击、能量、命中等 Breakpoint；
- 特效是否有 Uptime / Reliability / Applicability 折扣；
- 装备是否同时吃多个乘区形成 Double/Triple Scaling。

**禁止把固定的 `ATK:DEF:HP` 比例直接当装备预算真理。** 属性交换率应来自当前项目公式、Benchmark和模拟。

---

## 4. Base Stat / Main Stat / Substat

先区分三类价值：

### Base Stat
装备天然提供，建立槽位和品质身份。

### Main Stat
玩家最主要的装备选择轴，数量应有限、可读、可比较。

### Substat / Affix
提供Build差异、随机性和追求空间。

检查：

- 主词条是否足以产生真实选择；
- 副词条是否只是“继续堆主词条”；
- 同属性是否允许同时出现在主/副词条；
- 固定值属性是否会在后期完全失效；
- 百分比属性是否在后期无限放大；
- 稀有属性是否真正稀有，还是只是低权重但必选；
- 是否存在明显 Dead Affix。

---

## 5. Affix Pool / 词条池

每个词条池至少定义：

- Eligible Slots；
- Tier；
- Min/Max Roll；
- Weight；
- Mutual Exclusion / Group；
- Required/Forbidden Tags；
- Duplicate Rule；
- Rarity Gate；
- Level/Item Power Gate；
- Roll Count；
- Upgrade Roll Rule。

词条设计需要同时检查：

- **Power**：值不值；
- **Frequency**：出现多频繁；
- **Compatibility**：哪些角色/Build能用；
- **Readability**：玩家能否理解；
- **Search Space**：毕业组合有多难；
- **Dead Roll Rate**：掉落中有多少天然废词条；
- **False Choice**：看似很多词条，实际只有暴击/攻速等少数有效。

词条池越大不自动等于Build越丰富。

---

## 6. Roll Range / 随机Roll

随机词条必须明确：

- 是离散档位还是连续区间；
- 初始Roll数；
- 强化时新增词条还是提升旧词条；
- 是否等概率；
- 是否按词条Tier加权；
- 是否有保底/纠偏/定向；
- 是否允许锁词条/重铸；
- 重铸是否保留品质/强化；
- 玩家能否判断“好Roll”和“坏Roll”。

随机系统不能只看期望值，还要看：

- P50 / P90 / P95毕业时间；
- 极端坏运气；
- Best-in-Slot概率；
- 可用装备概率；
- 目标Build的有效掉落率；
- 重复刷取疲劳。

复杂随机模型交给 `simulation-design`。

---

## 7. Quality / Rarity Ladder

品质差异可以来自：

- Base Budget；
- Affix Count；
- Affix Tier；
- Roll Range；
- Enhancement Cap；
- Unique Effect；
- Set Access；
- Rule Modification。

不要默认每升一个品质就全部维度同时变强，否则容易指数膨胀。

品质梯度至少检查：

- 低品质是否有过渡价值；
- 高品质是否只是纯数值碾压；
- 新品质是否直接让旧品质全部报废；
- 品质与获取难度是否匹配；
- 高品质装备是否因为随机副词条反而经常不如低品质。

---

## 8. Enhancement / 强化曲线

强化系统要同时设计：

- 强化上限；
- 每级增长；
- 关键节点；
- 消耗曲线；
- 成功/失败规则（若存在）；
- 返还/继承；
- 换装损失；
- 强化是否改变词条；
- 强化是否形成 Sunk Cost Trap。

验证：

`Upgrade Power Delta <-> Upgrade Cost Delta <-> Replacement Probability`

常见问题：

- 强化太强 -> 玩家不愿换新装备；
- 强化太弱 -> 强化系统没有意义；
- 继承损失太大 -> 形成换装惩罚；
- 成本随等级暴涨但收益线性 -> 后段成为纯税。

成长节奏交给 `progression-design` 协同。

---

## 9. Set Bonus / 套装

套装价值拆为：

`Set Value = Stat Value + Behavior Change + Synergy Value - Slot Lock Cost - Flexibility Loss`

检查：

- 2件/4件/6件是否形成合理阶梯；
- 套装是否强到压死散件；
- 套装是否只服务单一角色；
- 为凑套装牺牲的高质量单件是否有真实机会成本；
- 套装效果是否与角色循环真正交互；
- 是否产生永久Buff、无限资源、近无限循环；
- 是否因为环境变化导致整套装备失效。

强套装可以存在，但不能自动成为所有角色的唯一答案。

---

## 10. Unique / Legendary Effect

唯一特效、专武、神器等应先定义它改变什么：

- 数值倍率；
- Target；
- Trigger；
- Resource；
- Rotation；
- State；
- Team Hook；
- Encounter Response。

优先奖励“新的决策/循环”，而不是单纯更大的乘区。

### 专属装备 Guard

专武/专属遗物需要检查：

- 没有专武时角色是否完整可玩；
- 专武是否只修复人为缺陷；
- 专武提升是纵向强度还是机制解锁；
- 是否形成 `Mandatory Signature / Equipment Tax`；
- 通用装备是否仍有意义。

---

## 11. Loot Quality / 可用掉落率

掉落设计不能只给“橙装5%”。

至少区分：

- Item Drop Rate；
- Target Slot Rate；
- Target Set Rate；
- Target Main Stat Rate；
- Usable Affix Rate；
- Good Roll Rate；
- Upgrade-compatible Rate；
- Actual Build Upgrade Rate。

概念上：

`Actual Upgrade Chance ≈ Drop × Slot × Set × MainStat × UsableAffix × RollQuality`

各项未必独立，正式计算需按真实规则建模。

如果单层概率都“看起来不低”，乘起来后仍可能导致极端低的实际升级概率。

---

## 12. Replacement Curve / 替换曲线

装备成长必须回答：

- 新装备多久出现一次；
- 多久产生一次真实Upgrade；
- 旧装备平均服役多久；
- 强化投入多久被替换；
- 前期/中期/后期替换速度如何变化；
- 毕业后还有什么追求；
- 版本更新如何避免一键报废整个库存。

可跟踪：

- Time-to-First-Usable；
- Time-to-Upgrade；
- Time-to-Best-in-Slot；
- Replacement Frequency；
- Inventory Obsolescence Rate；
- P50/P90/P95 Graduation Time。

---

## 13. Salvage / Duplicate / Crafting Economy

废装备必须有合理去向，但不要为了制造 Sink 强迫分解。

可设计：

- Sell；
- Salvage；
- Feed / EXP；
- Crafting Material；
- Reforge Currency；
- Set Conversion；
- Target Craft；
- Collection/Archive。

检查：

- 废装是否仍有价值；
- 分解是否产生闭环通胀；
- 重铸成本是否远高于重新刷取；
- 重复高稀有装备是否令人沮丧；
- 定向制作是否摧毁Loot期待；
- 装备库存是否无限堆积。

资源生命周期由 `economy-design` 主责。

---

## 14. Build Ecology / 装备生态

单件装备正常不代表生态健康。

至少根据项目建立：

- Character × Item Matrix；
- Build × Item Matrix；
- Item × Encounter Matrix；
- Slot Competition Matrix；
- Set / Unique Synergy Matrix。

检查：

- Best-in-Slot集中度；
- Top-N装备使用集中；
- 角色是否共享同一套装备答案；
- 专武依赖；
- Build多样性；
- 装备是否制造不可替代Pair Lock；
- 新装备是否产生Power Creep；
- 某词条是否因为底层公式成为无条件第一属性。

生态问题交给 `meta-balance` 协同验证。

---

## 15. Deterministic vs Random Itemization

不同项目不应被迫使用随机词条。

### Deterministic
适合强调规划、明确成长、低重复刷取成本的项目。

### Randomized
适合强调Loot、长线刷取、Build探索的项目，但必须控制坏运气和Dead Roll。

### Hybrid
固定主结构 + 随机副词条 / 可定向重铸，常用于兼顾确定性与追求。

先服务目标体验，再决定随机程度。

---

## 16. Itemization Benchmark

正式比较装备时至少固定：

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
- 随机模型/Seed（若相关）。

不同装备不能在不同Benchmark下直接横比。

---

## 17. Evidence Boundary

根据证据标记：

- 设计规则明确 -> `confirmed`；
- 表直接确认 -> `verified-config`；
- 代码确认 -> `verified-code`；
- Runtime确认 -> `verified-runtime`；
- Telemetry确认 -> `verified-data`；
- 新装备数值方案 -> `candidate`；
- 模拟 -> Simulation evidence，不自动等于Playtest。

外部游戏的词条数量、掉率、强化曲线、套装倍率只能作为参考，不可直接复制为通用标准。

---

## 18. Done Criteria

一次完整Itemization任务至少按需交付：

- Itemization Job；
- Slot Architecture；
- Quality/Rarity Ladder；
- Base/Main/Substat结构；
- Attribute/Power Budget；
- Affix Pool与Roll规则；
- Enhancement曲线；
- Set/Unique预算；
- Drop/Targeting模型；
- Replacement/Graduation目标；
- Salvage/Duplicate处理；
- Build/Meta风险；
- Simulation/Telemetry/Playtest验证计划；
- Evidence状态。

---

## 19. 反模式

- **Stat Soup**：所有装备都堆同一批属性；
- **Fake Choice**：词条很多，但有效词条只有少数；
- **Dead Affix Pool**：大量掉落天然不可用；
- **Best-in-Slot Lock**：每个角色只有唯一装备答案；
- **Signature Tax**：角色必须专武才能完整；
- **Set Prison**：套装收益压死所有散件；
- **Power Creep Ladder**：新版本只能靠更高Item Power吸引玩家；
- **Upgrade Hostage**：强化沉没成本阻止换装；
- **Loot Lottery Without Floor**：多层随机相乘却没有纠偏；
- **Overrandomized Progression**：成长结果主要由运气而非决策决定；
- **Guaranteed Loot Without Choice**：完全确定性但没有Build选择；
- **Salvage Inflation Loop**：分解与重铸形成自我增殖；
- **Universal Stat Ratio**：跨项目硬套固定属性交换率；
- **Average-only Loot Model**：只看期望掉落，不看P90/P95坏运气。

---

## 20. 跨 Skill 交接

当前结果核心是：

- 装备结构、槽位、词条池、套装、唯一特效、掉落可用率 -> `itemization-design` 主责；
- 某属性/特效到底强多少 -> `balance-design` 主责；
- 强化/品质/装备等级的长期节点 -> `progression-design` 主责；
- 掉落资源、强化材料、分解、商店与通胀 -> `economy-design` 主责；
- 大规模掉落/毕业时间/极端Roll模拟 -> `simulation-design` 主责；
- 多角色装备使用集中、BiS、版本生态 -> `meta-balance` 主责；
- 表字段/权重/随机池是否配置正确 -> `config-audit` 主责；
- 程序如何Roll、继承、重铸、触发 -> `code-verification` 主责。

不要用一个“装备策划”Header覆盖这些不同Decision Object。


---

# Source Module: gds-itemization-benchmark

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# Itemization Benchmark / 装备对标与参考验证

目标不是“抄某款游戏的装备数值”，而是把成熟项目的公开 Itemization 结构拆成**可验证事实、可迁移模式和不可直接迁移的项目特定参数**，再用这些参考帮助新的项目做设计与验证。

本 Skill 与 `itemization-design` 明确分工：

- `itemization-benchmark`：外部项目参考、数据抽取、曲线归一化、跨游戏对标、参考模式验证；
- `itemization-design`：当前项目的装备系统职责、槽位、预算、词条、强化、套装、Loot、替换和 Build 生态的最终设计；
- `balance-design`：具体属性/特效强度；
- `simulation-design`：毕业概率、词条分布、极端组合和长期刷取分布；
- `config-audit + code-verification`：当前项目真实配置与实现。

优先读取：

- [Reference Extraction & Normalization](reference-extraction-and-normalization.md)
- [HSR Relic Patterns](hsr-relic-patterns.md)
- [Genshin Weapon & Artifact Patterns](genshin-weapon-artifact-patterns.md)
- [Wuthering Waves Weapon & Echo Patterns](wuwa-weapon-echo-patterns.md)
- [Cross-Game Itemization Benchmark](cross-game-itemization-benchmark.md)
- [Source Map](source-map.md)
- [Benchmark Audit Template](../templates/benchmark-audit.md)

## 强制用户可见输出协议（MUST）

每一个独立外部装备参考事实、跨游戏对标结论、参考曲线判断、可迁移模式或项目差异结论前，都必须先显示：

```text
【本次专业视角】
主责：装备对标 / Benchmark（itemization-benchmark）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `itemization-design`：把参考模式转成当前项目结构候选；
- `balance-design`：比较属性预算、主副词条价值、武器基础/副属性权衡；
- `progression-design`：等级、突破、强化和稀有度成长；
- `simulation-design`：随机词条、有效掉落率、P50/P90毕业时间；
- `meta-balance`：套装、专武、BiS 集中和版本膨胀；
- `economy-design`：强化、回收、刷取成本和资源循环。

Direct Specialist Entry 仍执行共享 First-Visible-Line / Section Gate / Pre-Send Header Lint。

---

## 1. External Reference Boundary / 外部参考边界

外部游戏只能提供：

- 已公开的数据事实；
- 可观察的结构模式；
- 已验证过“可以存在”的设计空间；
- 用于提出问题和构建 Benchmark 的参照物。

外部游戏**不能自动提供**：

- 当前项目的正确属性比例；
- 当前项目的正确装备等级上限；
- 当前项目的正确掉率；
- 当前项目的正确主副词条数量；
- 当前项目的正确套装倍率；
- 当前项目的正确毕业周期；
- 当前项目的正确专武强度。

固定原则：

```text
Reference Fact != Transfer Rule
Reference Pattern != Project Standard
Reference Popularity != Design Correctness
```

任何迁移到当前项目的参数都必须重新经过 `itemization-design + balance-design`，必要时再经过 `simulation-design / economy-design / meta-balance`。

---

## 2. Reference Fact / Pattern / Candidate 三层分离

所有结论必须先分类。

### Reference Fact

公开页面直接支持的事实，例如：

- 某系统的最高强化等级；
- 某槽位允许哪些主属性；
- 某品质初始副词条数量；
- 某武器 90 级基础攻击和副属性；
- 某套装 2件/4件/5件效果；
- 某副词条有几个离散 Roll 档。

只有来源实际支持时才能写成事实。

### Reference Pattern

从多个事实归纳的结构，例如：

- Slot-gated Main Stat；
- Base Stat vs Secondary Stat Tradeoff；
- Fixed Growth + Random Affix Growth；
- Set Threshold Pressure；
- Refinement/Resonance Duplicate Scaling；
- Cost-constrained Loadout；
- Upgrade Milestone Roll。

这是 `supported-inference`，不是官方设计意图。

### Transfer Candidate

准备迁移到当前项目的设计候选，例如：

- “鞋子承担速度主属性”；
- “每4级强化一次副词条”；
- “武器使用高基础/低副属性与低基础/高副属性两个预算家族”。

这只能标 `candidate`，必须重新验证。

---

## 3. Interactive Detail Page / 等级进度条抽取

当参考网站存在等级滑杆、强化等级切换、精炼/谐振切换时，不能只记录满级截图。

至少建立 Level Curve Snapshot：

```text
Entity
Rarity
Level / Enhancement Level
Ascension / Breakthrough State
Refinement / Resonance Rank
Primary Stat
Secondary Stat
Passive / Set Effect Parameters
Source URL
Source Date
Version (if known)
```

优先采样：

- Lv1 / 起始值；
- 每个突破前后；
- 中位等级；
- 满级；
- 每个强化触发副词条/特效的关键节点；
- 精炼/谐振 1~5（若存在）。

不要只比较满级绝对值。必须同时观察：

- `V(level) / V(max)`；
- 每一级增量；
- 突破跳变；
- 是否线性；
- 是否分段线性；
- 是否存在成长前置/后置；
- 主属性和副属性是否同曲线。

具体抽取方法见 Reference Extraction & Normalization。

---

## 4. Normalized Comparison / 归一化比较

跨游戏绝对数字不可直接比较。

例如：

- 43.2% ATK；
- 46.6% ATK；
- 18% ATK；

不能因为数字大小不同就说一个系统更强。

至少转成以下一种或多种归一化指标：

### Max-Normalized Growth

`NormalizedLevelValue = ValueAtLevel / ValueAtMaxLevel`

用于比较成长曲线形状。

### Base-Stat Share

`BaseShare = BaseStatBudget / TotalItemPowerBudget`

用于比较武器“白值”与副属性/特效的预算结构。

### Random Power Share

`RandomShare = ExpectedRandomAffixValue / ExpectedTotalItemValue`

用于比较装备的随机性占总强度多少。

### Set Lock Share

`SetLockShare = SetConditionalValue / TotalExpectedItemValue`

用于估计套装对散件自由度的压迫。

### Upgrade Event Density

`UpgradeEventDensity = MeaningfulUpgradeEvents / MaxEnhancementLevel`

用于比较 +15、+20、+25 等体系下副词条/节点出现频率。

### Effective Acquisition Funnel

`EffectiveUpgradeRate = Drop × Slot × Set × MainStat × UsableAffixes × RollQuality × UpgradeOutcome`

用于比较“掉很多”与“真正升级很多”的差异。

这些都是分析框架，不是跨项目统一精确公式。

---

## 5. Reference Families / 参考家族

首批维护三个参考家族。

### Honkai: Star Rail / 遗器

重点用于研究：

- 槽位限定主属性；
- +15 终局强化；
- 5★主属性固定成长；
- 3档副词条 Roll；
- 每3级副词条新增/强化；
- 2/4件与位面饰品结构；
- 速度、命中、抵抗、击破等功能属性如何进入装备系统。

### Genshin Impact / 武器 + 圣遗物

重点用于研究：

- 武器基础攻击 + 副属性 + 被动；
- Lv1~90 与突破节点；
- 精炼 1~5 的特效成长；
- 圣遗物 +20；
- 固定主属性槽位与随机主属性槽位共存；
- 初始3/4副词条与每4级升级；
- 2/4件套装如何制造 Build 约束。

### Wuthering Waves / 武器 + 声骸

重点用于研究：

- 武器 Lv1~90、基础攻击 + 副属性 + 谐振1~5；
- 不同基础攻击/副属性档位家族；
- Echo Cost 1/3/4 与总 Cost 上限；
- 双主属性；
- +25 与每5级调谐副词条；
- Sonata / 合鸣套装；
- Echo Skill 把装备槽位与主动战斗行为结合。

三套系统用于形成不同“装备设计解”的参考，不建立优劣排名。

---

## 6. Cross-Game Benchmark Questions

做对标时至少问：

### Power Distribution

- 强度主要在基础属性、主属性、副属性、套装还是特效？
- 随机部分占比多大？
- 满级强度有多少来自强化而非初始掉落？

### Choice Architecture

- 槽位是否限制主属性？
- 有没有固定槽位降低随机复杂度？
- 是否存在 Cost / Slot Budget？
- 玩家是在“选数值”还是“选玩法行为”？

### RNG Architecture

- 随机层数有几层？
- 主属性、词条类型、Roll档、强化命中是否分别随机？
- Dead Roll Rate 多高？
- 有没有定向、重铸、保底、回收？

### Progression

- 强化上限；
- 关键升级节点；
- 突破；
- 重复品/精炼/谐振；
- 资源回收率；
- 换装损失。

### Build / Meta

- 套装是否形成唯一答案？
- 专武是否成为角色完成度税？
- 高稀有度是否只是更高数值；
- 新套装是否造成旧套装失效；
- 功能属性是否存在 Breakpoint。

---

## 7. Design Use / 如何用于新项目设计

外部参考进入当前项目时使用：

`Reference Observation -> Design Intent -> Project Constraint -> Candidate Pattern -> Project Formula/Budget -> Simulation -> Playtest`

例如观察到多个项目都使用“固定槽位 + 随机槽位”，不能直接照搬槽位数；应先问：

- 当前项目需要多少 Build 自由度；
- 玩家每次换装要处理多少认知负担；
- 当前装备掉落量和刷取时长；
- 角色是否已经有大量局内构筑；
- 装备随机性是否会与其他随机层叠加。

只有这些成立后才提出候选结构。

---

## 8. Validation Use / 如何用于项目验证

对现有装备系统可做差异审计：

```text
Project
vs
HSR Pattern
vs
Genshin Pattern
vs
Wuthering Waves Pattern
```

比较：

- Level Curve；
- Rarity Ladder；
- Main/Substat Budget；
- Affix Roll Spread；
- Upgrade Cadence；
- Set Threshold；
- Random Layer Count；
- Effective Upgrade Rate；
- Replacement Friction；
- Signature/BiS Pressure。

输出不是“哪款游戏最像我们”，而是：

- 项目在哪些维度明显更激进；
- 哪些维度更保守；
- 哪些差异是有意的；
- 哪些差异可能是风险；
- 需要怎样的项目内验证。

---

## 9. Freshness / Version Guard

商业游戏会持续更新装备、套装和属性。

任何精确参考数据都必须记录：

- 来源 URL；
- 抓取/查看日期；
- 游戏版本（若页面提供）；
- 页面是否为官方/社区/数据库；
- 是否经过第二来源交叉验证；
- 是否可能版本敏感。

如果当前无法访问详情页：

- 不从记忆补具体值；
- 标 `externally-blocked`；
- 可以继续做不依赖该值的结构分析。

---

## 10. Source Quality

外部 Itemization 数据优先级：

1. 官方数据/官方Wiki或游戏内可验证数据；
2. 稳定数据库与结构化图鉴；
3. 高质量社区Wiki / Theorycraft 数据；
4. 攻略文章；
5. 二手转述。

AppFeng 等结构化图鉴非常适合查看：

- 实体列表；
- 等级滑杆；
- 满级/中间等级属性；
- 武器精炼/谐振；
- 套装效果；
- 材料曲线。

但如果页面数据与更高优先级来源冲突，应标冲突，不自行挑一个“看起来合理”的值。

---

## 11. Done Criteria

一次正式对标至少交付：

- Reference Scope；
- Source Snapshot；
- Reference Facts；
- Normalization；
- Cross-game Pattern；
- Project Difference；
- Transfer Candidates；
- Non-transferable Values；
- Risk / Anti-pattern；
- 下一步项目内公式/模拟/Playtest验证。

---

## 12. 反模式

- **Copy-the-Number**：直接复制外部游戏倍率；
- **One-Game Truth**：把一个游戏当行业标准；
- **Max-Level Tunnel Vision**：只看满级值，不看成长曲线；
- **Screenshot Absolutism**：一张截图当完整系统；
- **Version Blindness**：忽略版本变化；
- **Absolute-Number Comparison**：跨游戏直接比 43.2% 和 46.6%；
- **Rarity Equivalence**：假设两个游戏的5星强度意义相同；
- **Slot Equivalence**：假设“鞋/头/手”等槽位跨游戏职责相同；
- **Passive Value Blindness**：只比基础属性不比被动/套装；
- **RNG Layer Blindness**：只比掉率不比主词条/副词条/升级随机层；
- **Reference-to-Verified Leap**：外部参考直接宣称当前项目已验证。

外部 Benchmark 是设计显微镜，不是数值答案库。
