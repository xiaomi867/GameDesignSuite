---
name: hero-kit-design
description: 负责英雄技能组（Hero Kit）的机制架构与相互关系，包括普攻/主动/被动/大招等槽位、状态机、资源图、触发链、循环、目标结构、场上时间、团队Hook与失败恢复。用于新英雄技能设定、机制审计和角色循环验证；不负责具体倍率曲线，具体数值协同 skill-value-design / balance-design。
---

# Hero Kit Design / 英雄技能设定

目标不是“给英雄填四个技能”，而是让整个 Kit 形成一个可读、可循环、可验证、与角色设定一致的战斗系统。

优先读取：

- [Cross-Game Hero Kit Patterns](references/cross-game-hero-kit-patterns.md)
- [Hero Kit Audit Template](templates/hero-kit-audit.md)

## 强制用户可见输出协议（MUST）

每一个独立 Kit 结构、技能槽位职责、状态机、资源循环、触发链、Team Hook 或机制一致性结论前，都先显示：

```text
【本次专业视角】
主责：英雄技能架构（hero-kit-design）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `hero-concept-design`：确认机制是否兑现角色设定；
- `skill-value-design`：为每个机制节点配置数值成长；
- `hero-stat-progression`：确认 Scaling Source 与基础成长匹配；
- `skill-design`：已有项目综合技能改造、Target/Buff配置语义；
- `combat-design`：战斗规则、行动/资源/Target底层约束；
- `balance-design`：判断完整循环的 Power Budget；
- `simulation-design`：验证Rotation、Uptime、触发频率与极端循环；
- `config-audit` / `code-verification`：确认真实实现。

Direct Specialist Entry 仍执行共享 First-Visible-Line / Section Gate / Pre-Send Header Lint。

---

## 1. 先定义 Hero Loop

新角色先写一句：

> 角色通过【Source/Setup】获得【状态/资源】，用【核心动作】完成【Payoff】，随后进入【Recovery/Reset】，并通过【Team Hook】与队伍发生关系。

至少明确：

- Entry State；
- Generator；
- Setup；
- Converter；
- Consumer；
- Payoff；
- Recovery；
- Loop Time；
- Team Hook；
- Failure Case。

如果技能可以各自独立删除而不影响循环，优先判断 Kit Cohesion 不足。

---

## 2. Slot Responsibility

技能槽位要有职责，不要求每个槽位同等强度。

常见职责：

- Basic / Normal：资源底座、低成本动作、补循环；
- Skill / Active：核心转换、主循环驱动；
- Ultimate / Liberation / Burst：高价值窗口、循环收束或状态转换；
- Talent / Passive / Forte：角色规则核心；
- Technique / Intro / Outro：战斗入口、换人、队伍衔接；
- Ascension Passive / Major Node：补充规则、修复体验或扩展Build；
- Eidolon/Constellation/Sequence：扩展、变体、上限或便利性。

禁止为了“槽位都有东西”而重复同一功能。

---

## 3. State Machine

复杂英雄必须显式状态化：

`Neutral -> Setup -> Primed -> Empowered -> Payoff -> Recovery`

每个状态明确：

- Enter Trigger；
- Exit Trigger；
- Duration / Turn / Action Semantics；
- 可否刷新；
- 可否叠加；
- 技能替换；
- 资源变化；
- Target变化；
- Buff/Debuff变化；
- 死亡、换人、控制、波次切换时的处理。

如果强化状态没有明确退出/恢复，警惕永久Burst。

---

## 4. Resource Graph

角色资源必须画成：

`Source -> Storage -> Threshold -> Spend/Convert -> Payoff -> Reset`

资源包括：

- 能量/怒气；
- 技能点/共享资源；
- 弹药；
- 层数；
- 标记；
- 特殊Gauge；
- 生命/护盾；
- 敌方状态；
- 队友行动；
- 受击次数；
- 击破/异常；
- 换人/协奏资源。

必须检查：

- Source是否足够；
- Storage是否会大量溢出；
- Threshold是否有意义；
- Spend是否有决策；
- 是否存在Source无Sink；
- 是否出现无限正反馈循环；
- 队友是否可以不合理地倍增资源生成。

---

## 5. Trigger Topology

不要只读技能描述，画 Trigger Graph：

`Action A -> State B -> Trigger C -> Attack D -> Gain Resource -> Trigger E`

标记：

- 主动触发；
- 自动触发；
- 每行动/每秒/每回合限制；
- ICD / Interval；
- 触发次数上限；
- 是否能被自身触发链递归；
- 是否能触发队友；
- 是否会重复计数；
- Trigger Reliability。

所有“额外行动/追击/反击/协同攻击/连携”必须检查自触发和循环闭合风险。

---

## 6. Target Architecture

每个动作明确：

- Single / Blast / AoE / Bounce / Random / Front / Back / Lowest/Highest HP；
- Ally / Self / Enemy / Team；
- Target Lock Timing；
- 目标死亡后的重定向；
- 多段攻击目标是否可变化；
- 随机目标是否均匀；
- Boss/单体环境是否改变技能价值。

Target不是纯描述字段，它直接影响Power Budget与体验。

---

## 7. Action / Field-Time Budget

根据游戏类型记录：

- Action Count；
- Field Time；
- Animation Time；
- Swap Time；
- Setup Time；
- Burst Window；
- Recovery Window；
- 共享资源占用；
- 输入复杂度。

纸面倍率必须通过真实行动次数与窗口兑现。

---

## 8. Team Hook

角色至少明确：

- 需要队友提供什么；
- 自己给队友什么；
- 是否依赖特定职业/元素/状态；
- 是否有通用Hook和专属Hook；
- 是否形成Mandatory Partner；
- 是否抢占公共资源；
- 是否改变队友行动节奏。

强协同允许存在，但需要 Opportunity Cost 与替代方案。

---

## 9. Mechanic Density / 机制密度

复杂不等于深度。

统计：

- 独立资源数；
- 独立状态数；
- 条件分支数；
- 需要记忆的阈值；
- 技能替换层数；
- 触发链长度；
- 例外规则数。

如果玩家为了使用一个角色必须同时维护过多互不关联规则，标 `Mechanic Soup`。

优先让多个效果围绕同一资源/状态形成组合，而不是每个技能发明一个新名词。

---

## 10. Upgrade Topology

技能等级、被动、星级/命座/共鸣链的升级先分类型：

- Numerical Upgrade；
- Reliability Upgrade；
- Rotation Upgrade；
- QoL Upgrade；
- Rule Expansion；
- New Team Hook；
- Capstone；
- Mechanic Replacement。

不能让所有成长节点都只是“+X%伤害”。

具体数值交给 `skill-value-design`；长期解锁节奏交给 `progression-design`。

---

## 11. Cross-Validation Matrix

### 与 hero-concept-design
- Core Fantasy 是否有高频动作表达；
- Signature Verb 是否出现在主循环；
- 风险/代价是否真实存在。

### 与 hero-stat-progression
- Scaling Source 与高成长属性是否匹配；
- Tank/Healer是否被迫堆完全无关属性；
- 速度/能量等固定属性是否支持循环。

### 与 skill-value-design
- 核心技能的数值成长是否匹配使用频率；
- Utility参数是否被过度随等级放大；
- 低频终结技是否获得合理Payoff。

### 与 balance-design
- 完整Rotation而非单技能是否在角色预算内；
- Team Hook是否形成隐性Power。

---

## 12. External Reference Boundary

崩铁、原神、鸣潮可用于观察不同 Skill Grammar：

- 回合制：Basic / Skill / Ultimate / Talent / Technique / Trace；
- 实时换人制：Normal / Skill / Burst / Passive / Constellation；
- 动作换人制：Normal / Resonance Skill / Forte / Liberation / Intro/Outro/Sequence等。

这只能证明“存在这些架构选择”，不能规定当前项目必须照搬槽位数量或升级结构。

---

## 13. Done Criteria

一次 Hero Kit 任务至少交付：

- Hero Loop；
- Slot Responsibility；
- State Machine；
- Resource Graph；
- Trigger Graph；
- Target Architecture；
- Action/Field-Time Budget；
- Team Hook；
- Failure/Recovery；
- Upgrade Topology；
- 与 Concept / Stat / Skill Value 的交叉验证；
- 需模拟/代码验证的风险。

## 14. 反模式

- **Button Collection**：技能只是几个独立按钮；
- **Mechanic Soup**：资源/状态很多但互不形成决策；
- **Infinite Trigger Loop**：触发链可自循环；
- **Permanent Burst**：强化状态无可靠结束；
- **Mandatory Partner**：角色只能绑定唯一队友；
- **Slot Redundancy**：多个技能做同一件事；
- **Passive Does Everything**：核心玩法几乎全自动，玩家决策被掏空；
- **Kit/Concept Split**：角色设定与实战循环没有对应关系。
