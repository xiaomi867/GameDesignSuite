# GameDesignSuite

一套面向生产项目的通用游戏策划 Skill Suite，覆盖：玩法/系统、英雄设定、Hero Kit、英雄等级属性、技能数值、战斗/数值/公式、装备/Itemization、外部Benchmark、Simulation、Telemetry/A-B实验、Meta/版本平衡、经济/成长、关卡、UI/UX、配置审计、代码验证、设计评审和 GDD。

## 多 Agent 架构

Game Design Suite 采用 **单一专业真源 + 多宿主适配层**：

```text
GameDesignSuite/
├── .agents/plugins/marketplace.json
├── .deepcode/skills/                  # DeepSeek Deep Code adapters
├── plugins/game-design-suite/
│   ├── .codex-plugin/plugin.json
│   ├── skills/                        # Canonical Skills
│   └── evals/
├── scripts/sync_agent_skills.py
├── AGENTS.md
├── skills-index.json
└── validate_skills.py
```

唯一专业真源：

```text
plugins/game-design-suite/skills/<skill-name>/SKILL.md
```

`.deepcode/skills/` 只负责发现，执行时继续读取 canonical Skill。

## 安装

ChatGPT / Codex Marketplace：

```text
来源：https://github.com/xiaomi867/GameDesignSuite.git
Git 引用：main
稀疏路径：留空
```

当前插件版本：**1.7.0**。

当前 canonical Skills：**24 个**。

DeepSeek Deep Code：

```bash
git clone https://github.com/xiaomi867/GameDesignSuite.git
cd GameDesignSuite
deepcode
```

## Skill 清单

| Skill | 主要职责 |
|---|---|
| `game-design` | 总入口、结果级路由、多 Skill 协调 |
| `game-production` | 玩法、系统、产品、跨系统与制作约束 |
| `design-frameworks` | MDA、Core Loop、Flow、Pattern |
| `hero-concept-design` | 角色设定、Core Fantasy、身份标签、Combat Promise、角色池差异化 |
| `hero-kit-design` | Hero Loop、技能槽位、状态机、资源图、Trigger、Target、Team Hook |
| `hero-stat-progression` | Lv1~上限基础属性、突破Delta、Bonus Stat、成长曲线与Roster Envelope |
| `skill-value-design` | 技能Lv1~上限倍率、治疗/护盾、Buff/Debuff、概率、持续、资源、CD与等级收益 |
| `skill-design` | 已有项目综合技能设计/改造、Target/Buff/被动/升星与机制保护 |
| `combat-design` | 战斗规则、行动/资源经济、状态、Gauge、AI、遭遇 |
| `balance-design` | Power Budget、DPS/HPS/EHP、横向强度、参数平衡 |
| `formula-verification` | 公式还原、乘区、单位、Clamp/Round、概率、边界、代码交叉验证 |
| `simulation-design` | Monte Carlo、离散事件、Rotation、参数扫描、分布与敏感性 |
| `telemetry-experiment-design` | 埋点、指标、分群、A/B、SRM、显著性、因果边界 |
| `meta-balance` | Roster/Composition/Matchup/Synergy/Counter、Mastery、Power Creep、版本生态 |
| `itemization-design` | 槽位、品质、主副词条、Roll、强化、套装、Unique、Loot、替换、BiS/Build生态 |
| `itemization-benchmark` | 公开商业游戏装备数据、等级曲线、结构归一化、跨游戏对标与迁移边界 |
| `economy-design` | Resource Role、Sources/Sinks、流速、库存、价值与产销 |
| `progression-design` | 账号/系统级等级、星级、突破、技能树、解锁、成长节奏与成本 |
| `level-design` | 关卡、地图、波次、Encounter、节奏、Boss |
| `game-interface-design` | HUD、菜单、引导、反馈、Accessibility |
| `config-audit` | Excel/配置字段、ID、引用、漏配、一致性 |
| `code-verification` | 客户端/服务器读取与实际生效链 |
| `design-review` | 根因、反模式、矛盾、主导策略、验证实验 |
| `game-design-doc` | GDD、System Spec、正式设计文档 |

## Hero Specialist Suite

英雄设计不再默认由一个 `skill-design` 包办，而是按 Decision Object 拆成四个可相互验证的专业层：

```text
Design Intent
-> hero-concept-design
-> hero-kit-design
-> hero-stat-progression
-> skill-value-design
-> balance-design
-> formula-verification
-> config-audit / code-verification
-> simulation-design
-> Runtime
-> telemetry-experiment-design
-> meta-balance
-> Playtest
```

### `hero-concept-design`

负责“这个角色是谁、玩家应该感受到什么”：

- Core Fantasy / Narrative Identity；
- 阵营、属性、武器、职业与Role Tags；
- Combat Promise；
- Signature Verb；
- Power Source / Risk / Cost；
- Team Relationship；
- Growth Fantasy；
- 设定 -> 玩法约束；
- 角色池差异化与Role Tag Mismatch。

### `hero-kit-design`

负责“技能机制如何兑现角色设定”：

- Hero Loop；
- Skill Slot Responsibility；
- State Machine；
- Resource Graph；
- Trigger Graph；
- Target Architecture；
- Action / Field-Time Budget；
- Team Hook；
- Upgrade Topology；
- Infinite Trigger / Permanent Burst / Mechanic Soup等风险。

### `hero-stat-progression`

负责“英雄等级对应的基础数值如何变化”：

- Lv1~Cap HP/ATK/DEF；
- 固定SPD/Energy/Crit等身份参数；
- 突破/晋阶跳变；
- Bonus Stat；
- Linear / Piecewise / Multiplier / Hybrid曲线；
- Normalized Growth；
- Roster Stat Envelope；
- Scaling Source Alignment；
- Character Level × Skill Level联合放大检查。

### `skill-value-design`

负责“技能等级对应的参数如何变化”：

- Damage / Heal / Shield；
- Buff / Debuff；
- 概率、持续、层数；
- CD、Resource Cost/Gain；
- Fixed vs Scaled Fields；
- 不同Parameter Type的Scaling Family；
- Normal Max / Extended Max；
- Rotation Contribution；
- Utility Breakpoint；
- Upgrade Power Delta / Cost。

## 四向相互验证

```text
hero-concept-design
  ↓ 设定承诺
hero-kit-design
  ↓ 机制兑现
hero-stat-progression
  ↓ 体质/成长支持
skill-value-design
  ↓ 数值表达
  ↘ 回看是否仍强化原始角色身份
```

典型冲突：

- 设定是“高速猎手”，Kit却是超低频炮台；
- Kit主伤害吃DEF，基础成长又把DEF推到极高，形成输出+生存Double Scaling；
- 角色等级ATK涨3倍、技能倍率再涨2倍，两条曲线单看平滑但组合后约6倍放大；
- Skill Value把辅助技能抬成主要输出，导致Role Drift；
- 页面标签写“治疗”，实际Kit只存在偶发自疗，形成Role Tag Mismatch。

## 外部英雄参考语料

首批共享公开角色总页：

```text
崩坏：星穹铁道  https://sr.appfeng.com/character
原神            https://ys.appfeng.com/character
鸣潮            https://mc.appfeng.com/avatar
```

共享规范：

```text
plugins/game-design-suite/skills/hero-concept-design/references/hero-reference-corpus.md
```

当任务要求研究“所有英雄”时，必须：

1. 先从总页建立当时版本完整 Index；
2. 按角色/形态/Detail URL建立唯一键；
3. 逐个读取二级详情页；
4. 等级滑杆不能只读默认等级；
5. 技能等级表不能只读Lv1或满级；
6. 记录Source Date / Version；
7. 报告 `success / total / blocked / duplicate-variant` Coverage；
8. 失败详情页标 `externally-blocked`，不从记忆补精确值。

外部资料只允许三层：

```text
reference-data      # 页面直接支持
supported-inference # 跨角色/跨游戏归纳
candidate           # 准备迁移到当前项目的候选
```

核心边界：

```text
Reference Fact != Transfer Rule
Reference Pattern != Project Standard
```

所以崩铁/原神/鸣潮的等级上限、基础属性、技能倍率、命座/星魂/共鸣链、技能槽位都不能自动成为当前项目标准。

## Itemization Suite

装备任务使用：

```text
External Benchmark(optional)
-> itemization-design
-> balance / progression / economy
-> simulation
-> meta-balance
```

`itemization-benchmark` 与 `itemization-design` 分离：前者研究外部成熟产品，后者对当前项目做最终设计。

## Numerical Production Chain

复杂数值任务按需要组合：

```text
Design Intent
-> Formula
-> Config/Code
-> Simulation
-> Runtime
-> Telemetry
-> Meta
-> Playtest
```

低层证据不能冒充高层证据：

- Spreadsheet/公式正确 != Runtime正确；
- Simulation稳定 != 玩家体验已验证；
- Telemetry相关 != 因果已验证；
- 总体50%胜率 != Meta健康。

## Professional Context Header

每一个独立正式结果前都必须显示实际专业路由，用户不需要额外提醒。

英雄完整任务会依次切换：

```text
角色设定策划（hero-concept-design）
-> 英雄技能架构（hero-kit-design）
-> 英雄成长数值（hero-stat-progression）
-> 技能数值策划（skill-value-design）
-> 数值策划（balance-design）
-> 配置审计 / 代码验证
```

不能用一个“技能/英雄策划”Header覆盖全部Decision Objects。

详细规则：

```text
plugins/game-design-suite/skills/game-design/references/professional-context-header.md
```

## 外部参考使用原则

崩铁、原神、鸣潮、绝区零、Riot、Ubisoft、GDC、Wiki与其他公开资料只用于：

- 公开事实；
- 结构与公式参考；
- 成长/技能/Itemization Benchmark；
- 专业方法论；
- 反模式与验证方法。

禁止把外部游戏的：

- 等级上限；
- HP/ATK/DEF成长表；
- 技能Lv1~Max倍率；
- 速度/能量阈值；
- 命座/星魂/共鸣链强度；
- 装备词条/掉率/套装倍率；

直接复制为当前项目标准。

## 私有项目隔离

真实项目配置、源码和日志可以用来**验证通用 Skill 是否覆盖生产问题**，但不会写入公开通用 Skill。

允许抽象：Hero Contract、Hero Loop、State/Resource Graph、Stat Curve Guard、Skill Scaling Family、deterministic seed、Golden Test、Formula/Runtime parity、Schema/version guard、Tail distribution、Loot funnel、Dead-affix guard。

禁止公开：私有项目名、角色/技能/装备/表名、ID、代码路径、真实公式、英雄基础属性、技能倍率、装备数值、掉率、经济数据、业务规则。

## 推荐测试 Prompt

### Hero Cross Validation

```text
设计/审计这个英雄，但不要把所有问题混成一个技能策划结论。分别检查角色设定、Hero Kit、Lv1~满级基础属性、技能Lv1~Max数值，再做总体Power Budget，并给每个Result Block显示实际主责。
```

### Stat Progression

```text
设计这个英雄Lv1~80的HP/ATK/DEF曲线，包含突破节点。先定义Growth Contract和曲线族，再检查Scaling Source、Roster Envelope和Character Level × Skill Level联合放大。
```

### Skill Value

```text
给这个技能设计Lv1~10完整数值表。区分Throughput、Utility、Reliability、Economy字段，不要把所有数字套同一倍率曲线，并检查每级Delta、Extended Level和Rotation Contribution。
```

### External Hero Corpus

```text
以崩铁/原神/鸣潮角色总页为Index，逐个读取详情，分别统计角色设定、技能架构、等级属性曲线与技能等级曲线。必须报告Coverage和blocked页面，不允许用记忆补精确值。
```

## 证据原则

常用状态：

- `verified-formula-design`
- `verified-config`
- `verified-code`
- `verified-runtime`
- `verified-data`
- `reference-data`
- `confirmed`
- `supported-inference`
- `candidate`
- `unverified`
- `not-yet-playtested`
- `externally-blocked`

## 维护与同步

新增/删除 Skill，或修改 canonical Skill 的 `name` / `description` 后运行：

```bash
python scripts/sync_agent_skills.py
python scripts/sync_agent_skills.py --check
```

专业正文只改 `plugins/game-design-suite/skills/`，不要人工维护多份。
