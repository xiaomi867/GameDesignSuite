# Hero Reference Corpus

本文件定义四个Hero专业Skill共同使用的外部公开参考语料边界。目标是让后续研究面对“完整角色池”，而不是只挑几个喜欢的角色做例子。

## Corpus Index

### 崩坏：星穹铁道
- Index: `https://sr.appfeng.com/character`
- Detail pattern: `https://sr.appfeng.com/character/<id>`
- Index dimensions: 属性、命途、稀有度。
- Detail schema: 阵营/命途/属性/介绍、基础属性、技能树、星魂、推荐、故事、语音。
- 注意：开拓者等多形态/重复入口应以Detail URL + 形态做唯一键，不按列表文字直接去重。

### 原神
- Index: `https://ys.appfeng.com/character`
- Detail pattern: `https://ys.appfeng.com/character/<id>`
- Index dimensions: 元素、武器、体型、稀有度。
- Index页面当前可见总量字段；数量会随版本变化，采集时记录Source Date。
- Detail schema: 所属/元素/武器/体型/生日/命座/称号、介绍、基础属性、天赋、命之座、故事、语音。

### 鸣潮
- Index: `https://mc.appfeng.com/avatar`
- Detail pattern: `https://mc.appfeng.com/avatar/<id>`
- Index dimensions: 属性、武器、性别、稀有度、战斗标签。
- Detail schema: 身份标签、共鸣能力、战斗技巧、基础属性、技能/共鸣链、检验鉴定、故事、语音。
- 漂泊者等多形态/重复入口以形态+URL做唯一键。

## Full-Corpus Rule

当任务要求“参考这些游戏所有英雄”时：

1. 先读取总页，锁定当次版本的完整Index；
2. 保存每个Detail URL、角色名、形态、稀有度、系统分类；
3. 对每个Detail页按统一Schema抽取；
4. 等级滑杆/技能等级切换不能只读默认值；
5. 记录Source Date与页面版本/游戏版本（若可得）；
6. 失败页面记录 `externally-blocked`，不能静默跳过；
7. 最终报告Coverage：`success / total / blocked / duplicate-variant`。

只有Coverage明确时，才可以声称“全量角色池分析”。

## Detail Extraction Schema

每个角色至少抽：

### Concept
- Name / Variant
- Rarity
- Faction/Region
- Element/Attribute
- Weapon/Path/Class
- Role Tags
- Title/Identity
- Short Introduction

### Level Stats
- Level Cap
- Ascension/Breakthrough milestones
- Lv1 snapshot
- key pre/post-break snapshots
- mid-level snapshot
- max-level snapshot
- HP/ATK/DEF
- SPD/Energy/Crit/other fixed stats
- Ascension/Bonus Stat

### Kit
- Skill slots
- Skill names/types
- resource/state names
- triggers
- target structure
- team hooks
- ascension passives
- eidolon/constellation/sequence effects

### Skill Values
- Skill level range
- each scalable field Lv1~normal max
- extended max if applicable
- fixed fields
- damage/heal/shield coefficients
- Buff/Debuff values
- probability/duration/resource/CD

### Narrative
- story/identity summary
- voice/personality signals only when relevant to design

## Slider / Interactive Guard

AppFeng详情页常通过滑杆或标签切换等级/技能等级。默认页面显示的往往只是当前选中值。

禁止：
- 只读默认满级就声称掌握成长曲线；
- 只看技能Lv1或Lv10就反推所有中间值；
- 页面抓取失败时用旧记忆补精确值。

推荐采样：
- 所有突破前后；
- 25% / 50% / 75%等级区间；
- LvMax；
- 技能Lv1、所有关键节点、Normal Max、Extended Max；
- 如果页面能完整展开1~10/1~12表，优先使用完整表。

## Evidence Labels

- `reference-data`：外部页面直接支持的字段/数值；
- `supported-inference`：跨角色/跨游戏归纳模式；
- `candidate`：准备迁移到当前项目的设计方案；
- `externally-blocked`：页面/滑杆/版本不可读取；
- `stale-risk`：来源可能落后于当前游戏版本。

## Cross-Skill Ownership

- 角色身份/设定语义 -> `hero-concept-design`
- Skill slots / 状态机 / 资源循环 -> `hero-kit-design`
- Lv1~Cap基础属性 -> `hero-stat-progression`
- 技能Lv1~Cap参数 -> `skill-value-design`

四个Skill可以读取同一Corpus，但不得互相替代最终责任。
