---
name: game-interface-design
description: 负责游戏 HUD、菜单、界面流程、信息层级、反馈、Onboarding、输入提示、对话选择和 Accessibility。用于判断玩家是否能感知、理解并操作系统，不负责最终视觉资产制作。
---

# 游戏 UI / UX 策划

机制如果玩家无法感知、理解或操作，就等于没有可靠生效。

## Result-Level Professional Context

每一个独立 UI/UX 结论、界面流程问题或 Onboarding 建议前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。若当前结果核心已切换到关卡教学、战斗反馈、数值可读性等其他 Decision Object，则对应专业成为主责，本 Skill 只作为协同。相邻结果即使专业组合相同也重复显示。

## 先分问题类型

### Usability
玩家不知道能做、看不懂、点错、找不到。

### Engageability
玩家理解系统但觉得无聊、负担高、反馈弱。

两类问题不要混用修复方案。

## 信息设计

对每个界面明确：

- 玩家此刻目标；
- 必须看到的信息；
- 次要信息；
- 可延后信息；
- 操作优先级；
- 错误与恢复；
- 状态变化反馈。

## HUD

避免所有信息常驻。检查：

- 高频决策信息是否及时；
- 警告是否可见；
- Buff/Debuff 是否可辨识；
- 资源是否与行动绑定；
- 信息是否只依赖颜色或声音。

## 菜单流程

检查：

- 进入成本；
- 返回路径；
- 层级深度；
- 高频操作点击数；
- 重要动作确认；
- 错误恢复；
- 批量操作；
- Loading/Transition。

## Onboarding

优先通过真实操作教学，减少说明书式弹窗。检查：

- 什么时候教；
- 教什么；
- 玩家是否练过；
- 是否在压力下再次使用；
- Hint 是否会阻碍探索。

## Input Prompts

提示应：

- 跟随当前输入设备；
- 支持重绑定；
- 区分 Tap/Hold；
- 不与实际操作冲突。

## Accessibility

关注：

- 字号/对比；
- 色觉；
- 字幕；
- 音频替代；
- 输入需求；
- 动作强度；
- Assist 选项；
- 认知负荷。

无障碍是可用性底线，不是纯附加功能。
