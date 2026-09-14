# Game Design Suite Core Regression Evals

这些用例用于防止后续 Skill 修改把已经修复的问题重新引入。

## E1 Missing Evidence Must Not Stall

**Prompt**

> 我有一个已经开发中的坦克英雄，技能机制不能改。检查倍率、Buff、Target、升星、配置引用和代码行为。如果缺少代码或配置，不要猜。

**Expected**

- 自动路由 `skill-design + balance-design + config-audit + code-verification + design-review`；
- 缺文件时只检查一次可用性；
- 标记 `unverified / externally-blocked`；
- 列出最小缺失材料；
- 继续完成不依赖缺失证据的分析；
- 不反复搜索不存在文件；
- 不整项停住。

## E2 No Sink For Sink's Sake

**Prompt**

> 游戏里食物、水、电、硅晶后期很多，英雄升级目前不消耗这些资源。怎么解决？

**Expected**

- 不直接把四资源加入 HeroLvUp；
- 先定义 Resource Role；
- 检查 Source、Stock、现有 Sink、生命周期、转换与基地中后期内容；
- 通过 Sink Legitimacy Gate 后才允许新增 Sink；
- 指出“健康盈余”可能是合理状态；
- 优先考虑经营系统自身的扩张、制造、科技、运行、转换等自然用途；
- 若跨系统联动，优先能力/效率/解锁，而不是强制收费。

**Fail**

- “Lv1~20 吃食物，Lv21~30 加纯水……”这类没有系统语义证据的分段消耗方案。

## E3 Symptom Is Not Solution

**Prompt**

> 三选一里治疗和防御没人选，所以我准备把它们都加 30%，你帮我定最终数值。

**Expected**

- 将“没人选”识别为症状；
- 检查 Dominant Strategy、TTK、机会成本、隐性伤害收益、场景适用面；
- 不直接接受 +30% 作为目标；
- 给 candidate 区间和验证方案。

## E4 New Evidence Must Override Old Candidate

**Prompt sequence**

1. 无代码时根据配置推断 DamageCfg 枚举；
2. 后续上传真实代码，枚举含义与旧推断冲突。

**Expected**

- 旧结论保持 `candidate/unverified`；
- 新代码证据出现后明确撤销旧建议；
- 升级为 `verified-code`；
- 不为了维护历史回答而忽略新证据。

## E5 Math Cannot Legitimize Bad Design

**Prompt**

> 给英雄升级增加 500 水+300 电后，帮我算一个不会卡成长的日获取量。

**Expected**

- 先验证该成本是否符合 Resource Role 与 Progression Cost Semantics；
- 如果成本本身不合理，不进入“把它调平”的流程；
- 明确区分 design legitimacy 与 numerical feasibility。

## E6 Cross-System Coupling Is Not Cross-Charging

**Prompt**

> 我想让基地经营和英雄养成联动，最简单是不是英雄升级直接扣基地资源？

**Expected**

- 不把“最简单实现”当“最佳设计”；
- 比较解锁、效率、制造、可选加速、资源转换、强制成本等 Coupling Ladder；
- 说明强制成本是高耦合方案，需要更强语义和玩家价值证据。

## E7 Spreadsheet Is Not Playtest

**Prompt**

> 模拟 10000 场后胜率 50%，是不是证明已经平衡而且好玩？

**Expected**

- 只允许支持理论/模拟层结论；
- 不把胜率 50% 等价成体验公平/好玩；
- 标记 `not-yet-playtested`；
- 给 Runtime / Telemetry / Playtest 下一步。

## E8 Fixed Rule Protection

**Prompt**

> 技能机制不能改，只能调数值。

**Expected**

- Target、Trigger、状态关系、技能结构视为 Fixed Rules；
- 不通过改 Target/Trigger 绕过约束；
- 只调整允许的 Tunables，除非发现实现 bug 并明确区分“修错”和“改机制”。
