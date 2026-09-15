# Formula Source Map

用于记录外部公式来源、证据等级和适用边界。目标不是“收藏链接”，而是防止把社区推导、旧版本资料和本项目事实混为一谈。

## Evidence Tags

| Tag | Meaning |
|---|---|
| `official-doc` | 官方明确文档/说明 |
| `official-data` | 官方可见数据，但公式仍可能是推导 |
| `community-theorycraft` | 社区理论计算/反推 |
| `community-wiki` | 社区 Wiki 汇总 |
| `tool-derived` | 计算器/工具项目推导 |
| `version-sensitive` | 明显依赖版本 |
| `pattern-only` | 只借结构，不借常数 |

外部公式默认不能直接升级成本项目 `verified-code` 或 `verified-runtime`。

## Honkai: Star Rail / 崩坏：星穹铁道

| Topic | Source | Tag | Use |
|---|---|---|---|
| General DMG blocks / stats | https://www.hoyolab.com/article/36700608 | community-theorycraft, version-sensitive | 乘区结构、基础属性组成、DEF/RES/易伤 |
| Damage multiplier blocks | https://www.hoyolab.com/article/18126946 | community-theorycraft | 乘区拆分、Break、早期资料对照 |
| Speed / Action Value | https://hsr.keqingmains.com/misc/speed-guide/ | community-theorycraft | AV、SPD、Advance/Delay、Breakpoint |
| Effect Hit / Effect RES | https://www.hoyolab.com/article/19460061 | community-theorycraft | BaseChance、EHR、RES、Specific RES |
| Toughness / Break | https://www.hoyolab.com/article/18981104 | community-theorycraft | 第二 Gauge、Break 状态与减伤 |
| Incoming DMG example | https://hsr.keqingmains.com/fu-xuan/ | community-theorycraft | DEF/RES/DR/Vulnerability、伤害转移 |
| Character mechanics | https://wiki.biligame.com/sr/%E8%A7%92%E8%89%B2%E5%9B%BE%E9%89%B4 | community-wiki, version-sensitive | 技能倍率/等级/机制样本 |
| Character database | https://sr.appfeng.com/character | community-wiki, version-sensitive | 角色与技能数据交叉参考 |

## Zenless Zone Zero / 绝区零

| Topic | Source | Tag | Use |
|---|---|---|---|
| Combat mechanics | https://www.hoyolab.com/article/28987778 | community-theorycraft | 基础伤害、异常、战斗属性 |
| Damage / Energy overview | https://www.hoyolab.com/article/37522351 | community-theorycraft | 直伤乘区、防御、抗性、暴击 |
| Anomaly / Disorder | https://www.hoyolab.com/article/35508795 | community-theorycraft | 异常伤害、AP、等级、多人贡献 |
| DEF Shred vs PEN Ratio | https://www.hoyolab.com/article/41060247 | community-theorycraft | 减防、无视、防穿顺序 |
| Anomalies and Disorders | https://www.prydwen.gg/zenless/guides/anomalies-and-disorders | community-theorycraft | 异常积蓄、触发、ICD、Disorder |
| Agent stats | https://www.prydwen.gg/zenless/guides/agents-attributes | community-theorycraft | PEN、AP、AM、Energy 等属性职责 |
| General formulas | https://github-wiki-see.page/m/Night-Sky-Studio/interknot-calculator/wiki/ZZZ-Formulas | tool-derived | 公式块交叉对照 |

## 用户此前提供的米游社资料

用户此前提供了多篇崩铁/绝区零的米游社文章，包含数值理论、角色技能、局内玩法、英雄设计等内容。部分页面是动态加载，无法稳定抓取正文时：

- 保留 URL 作为线索；
- 不声称已完整阅读；
- 不把无法读取正文的文章当公式证据；
- 优先用可稳定读取的同主题来源交叉验证。

## 使用规则

1. 外部来源只用于 Reference / Pattern Comparison。
2. 本项目真实配置、真实代码、Runtime 日志优先级更高。
3. 同一公式若多个社区来源冲突：
   - 记录版本；
   - 记录差异；
   - 不强行选一个当真；
   - 必要时用实测或源码验证。
4. 任何常数、Clamp、分段点都视为 `version-sensitive`，除非有更强证据。
5. 公式结构可以借鉴，参数规模必须按本项目重建。
