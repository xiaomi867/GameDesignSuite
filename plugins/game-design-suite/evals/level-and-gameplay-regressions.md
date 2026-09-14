# Level & Gameplay Design Regression Evals

这些用例用于防止关卡/玩法 Skill 退化成“排波次 + 加难度 + 塞内容”。

## L1 Mechanic Must Have a Lifecycle

**Prompt**

> 我有一个新机关，想在一关里用三次。帮我排一下。

**Expected**

- 不只给 3 个位置；
- 明确 Introduce / Practice / Test / Twist/Closure；
- 首次出现有 Safety Net；
- 后续至少一次改变关系而非只涨数值；
- 给验证方式。

**Fail**

- 第一次简单、第二次中等、第三次困难，仅通过数值升级。

## L2 Intensity Is Not Difficulty

**Prompt**

> 我想让第 8 波更紧张，是不是敌人血量翻倍最好？

**Expected**

- 区分 gameplay intensity 与 difficulty；
- 检查重规划、目标变化、空间压缩、刷新位置、资源压力等旋钮；
- 不默认用 HP/ATK 解决节奏问题。

## L3 Rest Is Not Empty Content

**Prompt**

> 高强度关卡里不要休息波，会不会更爽？

**Expected**

- 指出连续高强度会适应/麻木；
- 说明 Recovery / Reward / Planning Beat 的功能；
- 不机械规定固定比例；
- 给 Playtest 验证指标。

## L4 Boss Need Not Be the Mechanical Peak

**Prompt**

> 最终 Boss 必须是全关最难吗？

**Expected**

- 不给绝对答案；
- 区分 Mechanical Peak / Emotional Peak / Narrative Payoff；
- 根据产品目标决定是否重合；
- 说明技能考试可以前置，但极限挑战型产品可让最终 Boss 最难。

## L5 Random Does Not Mean Unplanned

**Prompt**

> 我们是随机事件肉鸽，所以关卡没法做节奏设计吧？

**Expected**

- 转为分布设计；
- 定义槽位角色、概率、连续上限、恢复下限、保底、峰值区间；
- 优先固定宏观结构、随机槽内内容；
- 关注 P50/P90 时长。

## L6 Decision Budget

**Prompt**

> 我想每波都给一次三选一，这样构筑感更强。

**Expected**

- 不直接认同；
- 检查 Decision Pressure、阅读/选择时间、菜单疲劳；
- 区分高压与低压决策；
- 比较“更多选择”与“更高质量选择”。

## L7 Config Duration Is Not Player Duration

**Prompt**

> 配置里这个事件 Duration=1 秒，所以放 20 个也只要 20 秒。

**Expected**

- 拆解 UI/动画/等待/选择/结算/过渡；
- 若运行时未知，标 `unverified` 并要求代码/实测；
- 不把配置字段直接当体感时长。

## L8 Spatial Teaching Before Tutorial Popup

**Prompt**

> 玩家总是不知道门可以打开，我加个弹窗“点击门”可以吗？

**Expected**

- 先检查 Signifier、构图、视线、交互反馈、第一次教学环境；
- 弹窗可以是补救但不是默认第一方案；
- 给低风险测试场景。

## L9 Mental Map vs Maze by Sameness

**Prompt**

> 玩家容易迷路，我是不是多加几个箭头就行？

**Expected**

- 检查 Landmark、Junction、房间独特性、Loop、Shortcut、视线；
- 箭头只是其中一种 Signifier；
- 不能用更多 HUD 引导掩盖空间同质化。

## L10 Negative Beat Needs a Landing

**Prompt**

> 我想在第 10 波随机扣玩家 10% 属性，让节奏有变化。

**Expected**

- 检查是否可预期/可选择/有收益交换/恢复窗口；
- 不把纯惩罚等同于 Twist；
- 若采用负反馈，应明确后续 Payoff 或策略变化。

## L11 System-to-Level Contract

**Prompt**

> 系统已经做完了，关卡策划自己找地方教玩家就行。

**Expected**

- 反对把教学完全甩给关卡；
- 系统策划应提供首次教学条件、安全网、可调参数、失败恢复、Twist 和禁止组合；
- `game-production + level-design` 联合处理。

## L12 Paper Pacing Is Not Evidence

**Prompt**

> 我把强度曲线画得很漂亮，是不是说明关卡节奏已经好了？

**Expected**

- 明确只能作为 candidate hypothesis；
- 要用实际 Beat 时长、失败率、重规划频率、停顿、玩家自评等验证；
- 未 Playtest 不得标记节奏已验证。
