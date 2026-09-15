# Cross-Game Character Stat Growth Patterns

本参考用于比较崩坏：星穹铁道、原神、鸣潮的角色等级/突破/基础属性结构。只提炼曲线与投放模式，不把具体外部数值当作当前项目标准。

## Source Boundary

首批公开来源：

- `https://sr.appfeng.com/character`
- `https://ys.appfeng.com/character`
- `https://mc.appfeng.com/avatar`
- 公开Wiki的 Character/Level Scaling、Ascension、Trace/Talent 等页面用于交叉验证。

详情页通常有等级滑杆；精确快照必须记录页面时间与版本。

## HSR Pattern

常见角色基础面板：

- HP；
- ATK；
- DEF；
- SPD；
- Energy Max；
- Taunt；
- Crit Rate / Crit DMG基础值。

角色通常以 Lv80 为传统满级基准，突破节点分布于20/30/40/50/60/70等阶段；Trace系统还独立提供 Stat Bonus 与 Bonus Ability。公开角色页显示速度、能量、嘲讽等往往作为固定身份参数存在，而HP/ATK/DEF随等级成长。

设计启发：

- 把“体质成长”和“循环参数”分离；
- 通过Trace/Bonus Ability提供离散成长节点；
- 行动速度若固定，更容易形成稳定角色节奏与配速Breakpoint。

## Genshin Pattern

公开角色等级体系长期采用多阶段Ascension，基础 HP/ATK/DEF 随等级成长，并有 Character Bonus Attribute 在部分突破阶段增加。公开 Level Scaling 数据显示，角色基础属性常使用基于稀有度与等级的Multiplier表，而不是每个角色单独手工画完全不同曲线。

设计启发：

- 可用“角色基础模板 × 等级Multiplier”统一曲线形状；
- 用Bonus Stat让角色在突破阶段强化配装/定位；
- Talent Level Cap 与Ascension阶段联动，使等级成长和技能成长有明确门槛。

Version Guard：公开资料可能随版本开放更高等级上限；引用时必须写明Source Date，不能固定认为“原神永远90级”。

## Wuthering Waves Pattern

公开角色页常见：

- HP；
- ATK；
- DEF；
- Crit Rate；
- Crit DMG；
- Resonance Efficiency；
- Resonance Energy Max；
- 部分角色/版本还会有其他节点属性。

角色常以 Lv90 页面快照展示，突破材料按阶段投放。技能节点与角色属性节点在同一成长树中，并存在多个个人/公共资源。

设计启发：

- 等级基础属性、资源上限、技能节点应分开建模；
- 动作游戏中固定暴击/共鸣效率基线与装备/声骸成长之间需要明确分工；
- 不同角色的Energy Max可以作为循环身份参数，而不是单纯Power属性。

## Cross-Game Shared Patterns

可观察到：

1. HP/ATK/DEF通常是主要等级成长属性；
2. 速度、能量、暴击基线等更常被当成角色身份/循环参数，而不是全部随等级同步增长；
3. 突破不仅提升上限，还承担技能等级上限、被动节点或Bonus Stat；
4. 角色满级数值不能单独评估，必须结合技能Scaling Source和装备系统；
5. 稀有度/职业可以共享成长曲线形状，但最终基准仍应以项目自身Benchmark验证。

以上为 `supported-inference`。

## Normalization Checklist

跨项目比较时至少记录：

- Level Cap；
- Ascension Levels；
- Lv1 values；
- pre/post-ascension values；
- LvMax values；
- fixed stats；
- bonus stat schedule；
- skill-cap unlock schedule；
- passive unlock schedule。

再计算：

- `V(L)/Vmax`；
- `V(L)/V1`；
- phase delta；
- growth density；
- roster percentile。

绝对值不可直接跨游戏比较。
