# Hero Specialist Cross-Validation Regressions

这些回归测试用于防止新增 Hero 专业 Skill 再次退化成“一个技能包办全部角色问题”。

## Case 1 — 角色设定 vs 技能机制
Prompt：
> 这个角色设定是高速猎手，但技能循环是30秒一次的大招炮台。哪里有问题？

Expected：
- `hero-concept-design` 主责设定/玩法承诺冲突；
- `hero-kit-design` 协同解释循环；
- 不直接用倍率补救。

FAIL：只建议把大招倍率提高。

## Case 2 — Kit结构
Prompt：
> 这个英雄四个技能互相没有资源、状态或触发关系，但每个技能倍率都正常。

Expected：`hero-kit-design` 主责，指出 Kit Cohesion / Button Collection 风险。

FAIL：仅做DPS比较。

## Case 3 — Lv1~80属性曲线
Prompt：
> 给我设计Lv1~80 HP/ATK/DEF成长，突破20/30/40/50/60/70。

Expected：`hero-stat-progression` 主责；先定义Growth Contract、关键节点、曲线族、突破Delta，再给候选数值。

FAIL：只用Lv1和Lv80做线性插值且不检查突破。

## Case 4 — 技能Lv1~10倍率
Prompt：
> 技能Lv1是100%，Lv10应该多少？

Expected：`skill-value-design` 主责；要求/声明Skill Job、使用频率、角色等级成长、Rotation等必要Benchmark；可给candidate但不能说存在通用2倍规则。

FAIL：直接回答200%是行业标准。

## Case 5 — 外部商业游戏参考
Prompt：
> 原神技能Lv10大约是Lv1的1.8倍，那我们的技能都按1.8倍成长。

Expected：引用只作为reference pattern，拒绝跨项目直接复制；`skill-value-design`重新验证。

FAIL：直接采用1.8。

## Case 6 — HSR基础攻击曲线
Prompt：
> 崩铁很多普攻是50%到100%，我们所有普攻也这么做。

Expected：外部事实 != Transfer Rule；结合本项目行动经济、普攻频率、资源职责验证。

FAIL：照抄。

## Case 7 — Utility不应套伤害曲线
Prompt：
> 伤害倍率Lv1到Lv10翻倍，所以减伤、控制概率、资源回复也全部翻倍。

Expected：`skill-value-design` 主责，触发 Utility Scaling Guard。

FAIL：接受统一倍率表。

## Case 8 — 属性×技能双重成长
Prompt：
> 角色ATK从Lv1到满级变3倍，技能倍率从Lv1到满级变2倍，两条曲线分别都很平滑，所以没问题。

Expected：`hero-stat-progression + skill-value-design` 拆块；指出组合后至少需要检查约6倍基础输出放大与其他乘区。

FAIL：分别看平滑就通过。

## Case 9 — Tank Scaling Source
Prompt：
> 坦克的伤害和护盾都吃DEF，而且DEF成长也是全角色最高。

Expected：`hero-stat-progression`确认成长，`hero-kit-design`确认Scaling Source职责，`balance-design`检查Double Scaling。

FAIL：因为符合坦克身份就自动通过。

## Case 10 — 设定与角色标签
Prompt：
> 页面标签写“治疗”，但角色只有一次很低概率的自疗。

Expected：`hero-concept-design`主责 Role Tag Mismatch；具体数值再交 `skill-value-design`。

FAIL：只讨论治疗倍率。

## Case 11 — 相同主责也重复Header
长回答连续两个独立技能数值结论都由 `skill-value-design` 主责。

Expected：两个Result Block都显示Header。

FAIL：第二个省略。

## Case 12 — Decision Object切换
Prompt：
> 先判断角色设定，再看技能循环，再做1~80属性，再定技能1~10倍率。

Expected顺序：
1. `hero-concept-design`
2. `hero-kit-design`
3. `hero-stat-progression`
4. `skill-value-design`

每个块独立Header。

FAIL：整篇只显示“技能/英雄策划”。

## Case 13 — 旧 skill-design 不应吞掉新专业
Prompt：
> 我只要检查这个英雄的Lv1~100属性成长。

Expected：`hero-stat-progression`主责；`skill-design`不应因为“英雄”关键词自动主责。

## Case 14 — 角色技能配置事实
Prompt：
> 表里这个技能Lv5倍率字段到底填了多少？

Expected：`config-audit`主责，不因为新增 `skill-value-design` 就抢配置事实责任。

## Case 15 — 公式语义
Prompt：
> {2#6000} 中2到底是攻击还是防御？

Expected：`code-verification/formula-verification`按证据主责，不由 `skill-value-design` 猜。

## Case 16 — Playtest边界
Prompt：
> 数值模拟显示角色强度很平衡，所以技能设计已经验证好玩。

Expected：拒绝把Simulation升级为Playtest。
