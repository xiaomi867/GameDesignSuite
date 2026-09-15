# Professional Context Header

> **NON-OPTIONAL USER-VISIBLE OUTPUT CONTRACT**
>
> 只要 Game Design Suite 正在回答游戏设计/策划相关任务，**无论用户有没有提醒、有没有指定 Skill，每一个独立正式结果前都必须显示 `【本次专业视角】`。**
>
> 这不是测试专用格式，也不需要用户重复写在 Prompt 里。

Header 用来暴露**当前结果实际采用的专业路由**，不是角色扮演。

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
【本次专业视角】主责：关卡策划（level-design）｜协同：战斗策划（combat-design）
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
| `economy-design` | 经济策划 |
| `progression-design` | 成长策划 |
| `level-design` | 关卡策划 |
| `game-interface-design` | 游戏 UI / UX 策划 |
| `config-audit` | 配置审计 |
| `code-verification` | 代码 / 实现验证 |
| `design-review` | 设计评审 |
| `game-design-doc` | 策划文档 / System Spec |

`game-design` 是路由器，通常不作为主责职业显示。

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

不要用一个 Header 覆盖四种责任。

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
- Meta小样本结论应显示样本/不确定性边界。

## Direct Specialist Entry

宿主若直接命中专业 Skill 而未先执行 Router：

- 当前专业 Skill 仍必须在第一条结果前显示 Header；
- 不得虚构尚未读取的协同 Skill；
- 后续加载其他 Skill 后，按结果重新路由。

## 禁止事项

- 不得要求用户每次提醒 Header；
- 不得只在整篇答案开头显示一次；
- 不得为了减少重复而省略独立结果 Header；
- 不得列出未实际使用的 Skill；
- 不得把全部 Skill 都列出来；
- 不得只说“我是资深XX策划”；
- 不得因为出现数字就默认 `balance-design` 主责；
- 不得因为跑了模拟就默认 `simulation-design` 能证明体验；
- 不得因为有线上数据就默认 `telemetry-experiment-design` 能证明因果；
- 不得因为总体50%胜率就跳过 `meta-balance` 的分群与矩阵检查。

## 质量标准

一个好的 Header 应让用户在读结果前知道：

- 谁对这个结果负责；
- 谁只提供协同证据；
- 当前结论属于配置、代码、公式、模拟、线上数据、Meta、设计候选还是玩家体验证据；
- 哪些硬约束或证据边界限制了结论。
