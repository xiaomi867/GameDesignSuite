# Professional Context Header

用于让用户在正式答案开始前看见本次 Game Design Suite 的实际专业路由，而不是只看到一个泛化的“资深策划”身份声明。

## 目的

Header 是可观察的路由结果，不是角色扮演。

它回答四件事：

1. **Primary Discipline / 主责专业**：谁对本次核心决策负责；
2. **Supporting Disciplines / 协同专业**：哪些专业只负责必要子问题；
3. **Critical Constraint / 关键约束**：哪些 Fixed Rules 不能被突破；
4. **Evidence Boundary / 证据边界**：当前结论最多能验证到哪一层。

Header 不能替代真正的 Skill 执行，也不能因为写了一个职业名称就声称对应 Skill 已被使用。

## 强制时机

Professional Context Header 必须是**正式答案最先出现的用户可见内容之一**，不得在长篇分析之后才补。

有两种入口：

### Router Entry

如果本轮先进入 `game-design`，由 Router 完成主责/协同选择后输出 Header。

### Direct Specialist Entry

宿主可能根据 Skill description 直接加载 `config-audit`、`balance-design`、`skill-design` 等专业 Skill，而没有先执行 `game-design`。

这种情况下：

- 当前专业 Skill 必须自行补出 Header；
- 只列当前轮**已经真实读取/使用**的 Skill；
- 不得为了还原“理想路由”而虚构尚未加载的协同 Skill；
- 如果之后又加载其他 Skill，可以在必要时更新一次 Header，但不要反复刷屏；
- 同一轮已有 Header 时不要重复。

因此，**Header 不依赖 Router 必须先被调用**。

## 输出规则

### 简单任务

只输出一行：

```text
专业视角：技能策划（skill-design）｜协同：数值策划（balance-design）
```

### 复杂生产任务

最多 4 行：

```text
【本次专业视角】
主责：技能策划（skill-design）
协同：数值策划（balance-design） / 配置审计（config-audit） / 代码验证（code-verification）
关键约束：技能机制不可修改；当前无运行时 Playtest 证据
```

存在关键证据边界时，也可以将最后一行写为：

```text
证据边界：配置可验证到 verified-config；缺源码时不得声称 verified-code
```

## Skill -> 专业称谓

| Skill | 用户可见专业称谓 |
|---|---|
| `game-production` | 玩法 / 系统策划 |
| `design-frameworks` | 游戏设计方法 / 框架 |
| `combat-design` | 战斗策划 |
| `skill-design` | 技能 / 英雄策划 |
| `balance-design` | 数值策划 |
| `economy-design` | 经济策划 |
| `progression-design` | 成长策划 |
| `level-design` | 关卡策划 |
| `game-interface-design` | 游戏 UI / UX 策划 |
| `config-audit` | 配置审计 |
| `code-verification` | 代码 / 实现验证 |
| `design-review` | 设计评审 |
| `game-design-doc` | 策划文档 / System Spec |

`game-design` 是总入口与路由器，通常不作为主责职业显示；只有用户明确询问路由机制时才可显示“游戏设计总控 / 路由”。

## 决定主责的方法

主责不是由用户口中的职业称呼直接决定，而由**当前最核心的决策对象**决定。

例：

- “资源后期很多怎么办” -> `economy-design` 主责，而不是看到“数值”就让 `balance-design` 主责；
- “英雄升级成本怎么设计” -> `progression-design` 主责，`economy-design + balance-design` 协同；
- “技能倍率、Buff、Target、升星和代码引用” -> `skill-design` 主责，`balance-design + config-audit + code-verification` 协同；
- “Boss 怎么设计” -> 具体空间/Encounter 为主时 `level-design` 主责；底层战斗机制为主时 `combat-design` 主责；
- “玩家总在地图里迷路” -> `level-design` 主责，必要时 `game-interface-design` 协同。

若两个专业都对核心决策不可缺少，选择对**最终设计决策承担责任**的一方为主责，另一方列入协同；不要写“双主责”来逃避判断。

Direct Specialist Entry 时，如果无法确认更高层主责，只显示当前 Skill 的专业身份，不凭空推断其他专业已经参与。

## 关键约束

只显示会改变本次结论的硬约束，例如：

- 技能机制不可修改；
- 服务器功能不可改；
- 只能使用现有 TaskType；
- 必须基于已有配置；
- 目标平台性能预算固定。

不要把普通背景信息全部塞进 Header。

## 证据边界

只有任务依赖证据时才显示。优先使用具体状态：

- `verified-config`
- `verified-code`
- `verified-runtime`
- `verified-data`
- `candidate`
- `unverified`
- `not-yet-playtested`
- `externally-blocked`

例如：

```text
证据边界：当前只有真实 Excel，可验证到 verified-config；字段运行时语义仍为 unverified-code
```

## 禁止事项

- 不得为了显得专业而列出没有实际读取/使用的 Skill；
- 不得把 14 个 Skill 全列出来；
- 不得只写“我是资深数值策划”而不暴露实际路由；
- 不得让 Header 超过正文的重要信息；
- 不得因为 Header 已经输出就停止任务；
- 不得把 `candidate` 写成 `verified`；
- 不得为了迎合用户指定身份而跳过真正应主责的专业；
- 不得因为直接进入专业 Skill 就省略 Header。

## 质量标准

一个好的 Header 应让用户在读正文前就能判断：

- AI 有没有找对主责专业；
- 有没有遗漏关键协同专业；
- 有没有违反“不改机制”等硬约束；
- 当前结论到底是设计候选、配置事实、代码事实还是运行时证据。
