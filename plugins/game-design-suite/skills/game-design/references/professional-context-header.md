# Professional Context Header

> **NON-OPTIONAL USER-VISIBLE OUTPUT CONTRACT**
>
> 只要 Game Design Suite 正在回答游戏设计/策划相关任务，**无论用户有没有提醒、有没有指定 Skill，每一个独立正式结果前都必须显示 `【本次专业视角】`。**
>
> 这不是测试专用格式，也不需要用户重复写在 Prompt 里。

Header 用来暴露**当前结果实际采用的专业路由**，不是角色扮演。

## 0. Strict Header Gate / 硬门禁

这是输出前必须执行的结构检查，不是“建议格式”。

### First-Visible-Line Rule

除非当前回复只是提出必要澄清问题，**Game Design Suite 的第一段用户可见实质内容必须从 `【本次专业视角】` 开始。**

禁止在第一个 Header 之前输出：

- “先给结论”；
- “下一个处理……”；
- 英雄/系统/装备名称介绍；
- 摘要；
- 风险判断；
- “我重新检查了……”；
- 任何配置、代码、数值、装备、技能或设计结论。

也就是说，不能出现：

```text
先给结论：这个英雄有三个问题……

【本次专业视角】
...
```

必须改成：

```text
【本次专业视角】
主责：...
协同：...

结论：这个英雄有三个问题……
```

### Section Gate

长回答中，只要一个 Markdown `# / ## / ###` 标题开始了新的正式判断、Finding、修改项、验证结论、候选数值或设计方案，**该标题前必须紧邻一个 Header**。

尤其下列标题默认视为新 Result Block，除非它显然只是同一结果中的纯证据小节：

- “一、二、三……”或数字编号章节；
- “结论 / 最终判断 / 必须修改 / 建议 / 风险 / Verified / Candidate”；
- 新的配置错误；
- 新的代码语义；
- 新的数值判断；
- 新的装备/词条/掉落/强化判断；
- 新的经济/成长/技能/关卡方案。

如果不确定是否算新的独立结果，**宁可重复 Header，也不要省略。**

### Result-Transition Gate

当内容从一种 Decision Object 切换到另一种时，必须先停止当前块，再输出新的 Header。例如：

`配置事实 -> 代码语义 -> 数值影响`

必须是三个 Result Blocks，不能用一个 Header 覆盖。

装备任务常见：

`装备结构 -> 属性强度 -> 随机分布 -> 经济生命周期 -> Meta生态`

也必须按 Decision Object 拆块。

### Pre-Send Header Lint

在发送答案前，对草稿做一次结构自检：

1. 第一段实质内容是否以 `【本次专业视角】` 开始；
2. 每个独立编号结果/正式结论标题前是否有 Header；
3. 每个“必须修改 / 建议 / 保持 / Bug / 风险 / Verified / Candidate”结论是否属于某个明确 Header 块；
4. Decision Object 改变时主责/协同是否同步改变；
5. 是否出现了 Header 之后跨越多个不同专业结果的情况；
6. 是否用了非标准、模糊职业名替代真实 Skill，例如只写“战斗程序”“技能数值”“装备数值”而不对应 Skill。

任一项不通过，先修正格式再输出。

## 每个结果都必须重新路由

正式输出顺序固定：

`Header -> Result -> Evidence/Reasoning -> Recommendation/Validation`

只要开始新的核心 Decision Object，就先重新判断：

- Primary Discipline / 主责；
- Supporting Disciplines / 协同；
- Critical Constraint / 关键约束（会改变结果时）；
- Evidence Boundary / 证据边界（依赖证据时）。

相邻两个结果即使专业组合完全相同，也重复显示 Header。

## 推荐格式

复杂生产结果：

```text
【本次专业视角】
主责：数值模拟 / 仿真（simulation-design）
协同：公式 / 数值验证（formula-verification） / 数值策划（balance-design）
证据边界：当前为 Simulation 证据，不等于 verified-runtime 或 Playtest
```

简单结果：

```text
【本次专业视角】主责：装备 / Itemization 策划（itemization-design）｜协同：数值策划（balance-design）
```

不存在协同时可以只显示主责。

## Skill -> 用户可见专业称谓

| Skill | 用户可见专业称谓 |
|---|---|
| `game-production` | 玩法 / 系统策划 |
| `design-frameworks` | 游戏设计方法 / 框架 |
| `combat-design` | 战斗策划 |
| `skill-design` | 技能 / 英雄策划 |
| `balance-design` | 数值策划 |
| `formula-verification` | 公式 / 数值验证 |
| `simulation-design` | 数值模拟 / 仿真 |
| `telemetry-experiment-design` | 数据分析 / 实验设计 |
| `meta-balance` | Meta / 版本平衡 |
| `itemization-design` | 装备 / Itemization 策划 |
| `economy-design` | 经济策划 |
| `progression-design` | 成长策划 |
| `level-design` | 关卡策划 |
| `game-interface-design` | 游戏 UI / UX 策划 |
| `config-audit` | 配置审计 |
| `code-verification` | 代码 / 实现验证 |
| `design-review` | 设计评审 |
| `game-design-doc` | 策划文档 / System Spec |

`game-design` 是路由器，通常不作为主责职业显示；只有当前任务本身是在检查路由/Skill 架构时，才可显示“游戏设计总控 / 路由（game-design）”。

用户可见称谓优先使用上表，不临时发明“技能数值”“战斗程序”“品质基准设计”“装备数值”等无法直接映射到 Skill 的称谓。需要表达更细职责时，放到正文，不替换 Header 中的标准专业名。

## 按 Decision Object 选主责

### 配置事实

字段值、漏配、错引、`_lv`不一致 -> `config-audit`。

### 代码语义

枚举、Parser、Runtime Consumer、执行顺序 -> `code-verification`。

### 公式结构

乘区、单位、Clamp/Round、定义域、Snapshot、公式还原 -> `formula-verification`。

### 单体数值强度

倍率、DPS/EHP/TTK、Power Budget、候选值 -> `balance-design`。

### 模拟分布

100/1000/10000次、Monte Carlo、离散事件、参数扫描、P90/P95、敏感性 -> `simulation-design`。

### Telemetry / 实验

埋点、KPI、玩家分群、A/B、SRM、显著性、因果边界 -> `telemetry-experiment-design`。

### Meta / 版本生态

Roster、Composition、Matchup、Synergy、Counter、Pick/Win、Mastery、Power Creep -> `meta-balance`。

### 装备 / Itemization

槽位、品质、主/副词条、词条池、Roll、套装、唯一装备、Loot可用率、替换曲线、BiS结构 -> `itemization-design`。

如果核心问题变成“某个词条/特效到底强多少”，切换 `balance-design`；如果变成“掉落/毕业概率分布”，切换 `simulation-design`；如果变成“强化材料/分解/通胀”，切换 `economy-design`；如果变成“版本装备使用集中和生态”，切换 `meta-balance`。

### 经济与成长

资源生命周期、Source/Sink -> `economy-design`。

等级、星级、突破、成长成本/节点 -> `progression-design`。

### 英雄 / 战斗 / 关卡

技能机制、状态机、Target -> `skill-design`。

底层战斗规则、AI、战斗窗口 -> `combat-design`。

空间、波次、路线、Encounter -> `level-design`。

## 常见跨层切换示例

用户要求“从表和代码确认伤害公式，模拟10000次，再判断全角色Meta影响”时，必须拆块：

```text
【本次专业视角】
主责：配置审计（config-audit）
协同：代码 / 实现验证（code-verification）
```

先确认输入字段。

```text
【本次专业视角】
主责：公式 / 数值验证（formula-verification）
协同：代码 / 实现验证（code-verification）
```

再还原公式。

```text
【本次专业视角】
主责：数值模拟 / 仿真（simulation-design）
协同：公式 / 数值验证（formula-verification） / 数值策划（balance-design）
```

再跑分布与敏感性。

```text
【本次专业视角】
主责：Meta / 版本平衡（meta-balance）
协同：数据分析 / 实验设计（telemetry-experiment-design） / 数值策划（balance-design）
```

最后才评估生态影响。

装备任务例如“设计词条池、算单词条强度、模拟毕业时间、判断BiS集中”时，至少拆为：

```text
【本次专业视角】
主责：装备 / Itemization 策划（itemization-design）
协同：数值策划（balance-design）
```

```text
【本次专业视角】
主责：数值策划（balance-design）
协同：装备 / Itemization 策划（itemization-design）
```

```text
【本次专业视角】
主责：数值模拟 / 仿真（simulation-design）
协同：装备 / Itemization 策划（itemization-design）
```

```text
【本次专业视角】
主责：Meta / 版本平衡（meta-balance）
协同：装备 / Itemization 策划（itemization-design）
```

不要用一个 Header 覆盖多种责任。

## 证据边界

根据当前结果显示必要状态：

- `verified-config`
- `verified-code`
- `verified-runtime`
- `verified-data`
- `candidate`
- `supported-inference`
- `unverified`
- `not-yet-playtested`
- `externally-blocked`

特别规则：

- Simulation 不能自动写 `verified-runtime`；
- Telemetry 观察相关性不能自动写“因果已验证”；
- 外部游戏公开案例不能写成本项目 `verified`；
- Meta小样本结论应显示样本/不确定性边界；
- Itemization预算或外部装备模板不能自动写成本项目标准，除非经过本项目Benchmark/公式/验证。

## Direct Specialist Entry

宿主若直接命中专业 Skill 而未先执行 Router：

- 当前专业 Skill 仍必须让第一段实质内容以 Header 开始；
- 当前专业 Skill 仍执行 Section Gate 与 Pre-Send Header Lint；
- 不得虚构尚未读取的协同 Skill；
- 后续加载其他 Skill 后，按结果重新路由。

## 禁止事项

- 不得要求用户每次提醒 Header；
- 不得在第一个 Header 前输出结论、摘要或对象介绍；
- 不得只在整篇答案开头显示一次；
- 不得为了减少重复而省略独立结果 Header；
- 不得把多个编号结果默认视为同一个 Result Block；
- 不得列出未实际使用的 Skill；
- 不得把全部 Skill 都列出来；
- 不得只说“我是资深XX策划”；
- 不得使用无法映射到 Skill 的临时职业名称替代标准主责/协同；
- 不得因为出现数字就默认 `balance-design` 主责；
- 不得因为出现装备就让 `itemization-design` 包办公式、代码、经济、模拟和Meta结论；
- 不得因为跑了模拟就默认 `simulation-design` 能证明体验；
- 不得因为有线上数据就默认 `telemetry-experiment-design` 能证明因果；
- 不得因为总体50%胜率就跳过 `meta-balance` 的分群与矩阵检查。

## 质量标准

一个好的 Header 应让用户在读结果前知道：

- 谁对这个结果负责；
- 谁只提供协同证据；
- 当前结论属于配置、代码、公式、装备结构、模拟、线上数据、Meta、设计候选还是玩家体验证据；
- 哪些硬约束或证据边界限制了结论。

最终发送前必须通过 Pre-Send Header Lint；未通过时视为格式回归失败。
