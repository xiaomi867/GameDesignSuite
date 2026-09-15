# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# Meta / 版本级平衡

目标是从“一个对象是否合理”上升到“整个选择生态是否健康”。

优先读取：

- [Meta Balance Framework](meta-balance-framework.md)
- [Meta Balance Source Map](meta-balance-source-map.md)
- [Meta Balance Audit Template](../templates/meta-balance-audit.md)

## 强制用户可见输出协议（MUST）

每一个独立Meta结论、Roster异常、组合风险、版本趋势或系统性平衡建议前，都先显示：

```text
【本次专业视角】
主责：Meta / 版本平衡（meta-balance）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `balance-design`：单体Power Budget与候选改动；
- `simulation-design`：预上线组合矩阵和代理仿真；
- `telemetry-experiment-design`：线上Pick/Win/Usage/Segment证据；
- `skill-design` / `combat-design`：解释角色工具、Counter与战斗阶段；
- `level-design`：检查内容环境是否系统性偏袒某类Build。

## 1. 平衡对象不是只有角色

根据项目建立实际生态单位：

- Hero / Character；
- Skill / Card；
- Item / Equipment；
- Build / Archetype；
- Team / Composition；
- Enemy / Encounter；
- Map / Mode；
- Difficulty tier；
- Player skill/mastery cohort。

Meta问题往往来自对象之间的关系，不是某个对象单独数值错误。

## 2. 建立 Balance Matrix

至少按任务建立一个或多个矩阵：

### Roster Matrix
角色 × 关键指标。

### Matchup Matrix
对象A × 对象B 的相对结果。

### Synergy Matrix
组合后收益是否显著超过个体预期。

### Counter Matrix
是否存在有效反制，以及反制成本。

### Content Coverage Matrix
角色/Build × 关卡/敌人/模式。

### Cohort Matrix
角色/Build × 玩家技能/熟练度。

矩阵的作用是发现“局部合理、整体挤压”。

## 3. 不用一个总胜率统治所有判断

根据游戏类型组合：

- Pick / Usage Rate；
- Win / Clear Rate；
- Ban / Presence（适用时）；
- Matchup；
- Team/Composition win rate；
- Role/Position performance；
- Skill/Move usage；
- Build diversity；
- Experienced-player performance；
- First-use vs mastered performance；
- Sample size / uncertainty；
- Frustration / qualitative feedback。

低Pick高Win可能是小样本、高手专属、反制位或隐藏强势；必须继续分解。

## 4. Player Segment / Skill Band

不同玩家层可以存在不同平衡问题。

至少在需要时分：

- 新手；
- 主流熟练度；
- 高熟练；
- 顶尖/竞技；
- 角色新手 vs 角色专精者。

不要因为高端环境健康，就默认新手环境健康；反之亦然。

## 5. Mastery Curve

角色强度必须区分：

- Entry Power；
- Learning Slope；
- Mastered Power；
- Execution Reliability。

新角色上线早期低胜率可能来自学习曲线。高熟练度角色在总体50%时也可能在专精群体过强。

## 6. Accessibility of Power

同样的理论强度，如果一个角色的强工具更容易、更稳定地兑现，其实战生态压力可能更大。

记录：

- Setup Cost；
- Execution Difficulty；
- Counterplay visibility；
- Reliability；
- Error Punishment；
- Recovery。

平衡不能只看最终上限。

## 7. Synergy / Pair Lock

检查组合：

`Observed Pair Value` vs `Expected Independent Value`

重点识别：

- multiplicative synergy；
- infinite/near-infinite loops；
- resource engine；
- permanent uptime；
- unique state detonator；
- mandatory partner；
- one-composition dominance。

强联动本身不是问题；如果没有合理机会成本或替代组合，才会造成Pair Lock。

## 8. Counter Health

一个健康Counter通常满足：

- 玩家能理解；
- 可在合理时机选择；
- 成本可接受；
- 不要求完全放弃自己的Build；
- 不只是“免疫/封死”；
- 被Counter方仍有恢复或二次决策。

如果只能靠Boss/敌人全面免疫某体系来平衡，优先判为系统性设计风险。

## 9. Diversity Metrics

多样性不是“每个对象Pick完全相等”。

可观察：

- Viable Pool Size；
- Top-N usage concentration；
- Herfindahl-Hirschman Index (HHI) 或其他集中度；
- Archetype share；
- Composition diversity；
- Matchup polarization；
- Number of meaningful alternatives。

角色天然人气不同，不能把Popularity直接当Power。

## 10. Power Creep

每个版本记录：

- Baseline power distribution；
- 新内容相对旧内容的Power Delta；
- Top percentile变化；
- 内容TTK/TTD变化；
- 老内容Clear Rate；
- 新机制覆盖旧机制的比例；
- 是否需要全局抬敌人来追赶玩家。

### Power Creep 信号

- 新角色必须明显更强才能被选；
- 新装备普遍替代旧装备；
- Boss只能靠更高HP/免疫应对；
- 老角色需要连续数值Buff才能生存；
- Build选择越来越集中。

## 11. Systemic vs Local Fix

发现Meta问题后先分类：

### Local
一个角色/技能/物品过强，可局部调参。

### Interaction
两个或多个对象组合失控，需要改交互、资源或条件。

### Environment
当前关卡/敌人/模式系统性偏袒一种策略。

### Systemic
底层公式、装备系统、资源经济、Counter结构或奖励机制导致全局偏斜。

不要用十几个局部Nerf掩盖一个系统性根因。

## 12. Patch Risk / 版本风险

任何改动都检查：

- direct targets；
- indirect beneficiaries；
- indirect victims；
- existing counters；
- item/build ripple；
- low/high skill cohorts；
- old content；
- new player experience；
- future content assumptions。

物品、共享资源、通用机制的改动通常比单角色改动波及更广。

## 13. Pre-Analytics + Live Analytics

上线前：

`formula/balance -> simulation -> predicted matrix`

上线后：

`telemetry -> observed matrix`

比较：

- 预测强度与真实胜率；
- 代理策略与真实Pick；
- 预期Counter与真实Counter；
- 预期Build多样性与真实集中度。

差异本身就是重要设计信息。

## 14. Done Criteria

一次Meta评审至少交付：

- Scope与版本；
- Player cohorts；
- Matrix；
- Sample size / uncertainty；
- Outliers；
- Diversity / concentration；
- Synergy/Counter；
- Power creep；
- Root-cause classification；
- Candidate changes；
- Ripple risk；
- Simulation/Telemetry验证计划。

## 15. 反模式

- **50% Win Rate Worship**：总体50%就宣称平衡；
- **Pick Rate = Power**：把人气等同强度；
- **No Skill Buckets**：忽视玩家水平；
- **No Mastery Curve**：忽视角色学习成本；
- **Pair Lock Blindness**：单体正常但组合必选；
- **Counter by Immunity**：靠完全免疫解决体系过强；
- **Patch Whack-a-Mole**：不断局部修补系统性问题；
- **Power Creep Normalization**：通过全体敌人加血适配新角色膨胀；
- **Small Sample Ranking**：低样本对象硬排名；
- **Environment Blindness**：内容环境偏斜被误判为角色数值问题。
