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
