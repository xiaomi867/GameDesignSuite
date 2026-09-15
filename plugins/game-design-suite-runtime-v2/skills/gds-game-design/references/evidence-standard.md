# Evidence Standard

## 目的

统一 Game Design Suite 中事实、候选方案、代码验证、运行时验证和 Playtest 的证据等级，避免不同 Skill 对 `verified` 使用不一致。

## 推荐状态

### confirmed
用户、正式策划文档或项目负责人已经明确确认的规则/约束。它是项目事实，但不等于实现已验证。

### verified-config
已经从当前真实配置文件确认字段、Key、ID、引用或数值存在。

### verified-code
已经从实际客户端/服务器代码确认字段解析、枚举、条件或执行链语义。

### verified-runtime
已经从实际运行、日志、调试、构建或可复现运行路径确认结果。

### verified-data
已经从当前真实 Telemetry / 运营数据 / 实验数据确认。

### candidate
设计、数值或配置候选方案，尚未得到足够项目证据支持。

### supported-inference
已有若干直接证据支持，但仍缺关键链路或反例验证。

### unverified
理论上可检查，但当前缺少对应项目材料。

### not-yet-playtested
机制、数值或实现可以成立，但尚未得到代表性玩家体验证据。

### externally-blocked
必须依赖当前不可访问的外部环境、构建、账号、服务器或测试条件。

## 证据优先级

针对“实际怎么生效”类问题，通常优先级为：

`runtime evidence > current code > current config > current design document > historical note > inference`

但不同问题证据类型不同：

- 体验/好玩：Playtest/玩家数据优先；
- 实现语义：代码/运行时优先；
- 当前配置：真实配置文件优先；
- 产品约束：用户/负责人确认优先。

## 禁止升级

以下情况不得直接升级为更高证据：

- Spreadsheet/Simulation -> Playtest；
- 配置存在 -> 代码一定读取；
- 代码读取 -> 路径一定触发；
- 历史方案 -> 当前版本事实；
- 用户症状描述 -> 根因确认；
- 相似游戏经验 -> 当前项目实现事实。

## 冲突处理

新证据与旧结论冲突时：

1. 保留新旧结论来源；
2. 按证据层级判断；
3. 明确撤销或降级旧结论；
4. 不为了保持一致而护住历史答案。
