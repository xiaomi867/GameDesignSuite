# Professional Header Hard-Gate Regressions

These cases validate that `【本次专业视角】` is a non-optional structural output contract rather than a formatting suggestion.

## Case 1 — First visible substantive line must be Header

Prompt:

```text
下一个英雄，继续检查技能、配置、代码和数值。
```

FAIL if the answer starts with any substantive text such as:

```text
下一个处理某英雄。
先给结论：存在三个问题……
```

before `【本次专业视角】`.

PASS only when the first substantive visible block starts with:

```text
【本次专业视角】
主责：...
协同：...
```

## Case 2 — Numbered result section cannot inherit an old Header silently

Given a long answer with:

```text
【本次专业视角】
主责：代码 / 实现验证（code-verification）

## 二、发现运行问题
...

## 三、这个配置必须改
...
```

FAIL because section 三 contains a new formal modification result but has no Header immediately before it.

PASS form:

```text
【本次专业视角】
主责：配置审计（config-audit）
协同：代码 / 实现验证（code-verification）

## 三、这个配置必须改
```

## Case 3 — Same profession still repeats Header

Two independent config findings both owned by `config-audit` must each receive a Header. Do not omit the second Header because the profession did not change.

## Case 4 — Decision Object transition requires reroute

A response that moves through:

1. config fact;
2. code semantics;
3. numeric strength impact;

must show three separate Headers with the corresponding primary disciplines:

- `config-audit`;
- `code-verification`;
- `balance-design`.

One shared Header for all three is FAIL.

## Case 5 — Preamble is not exempt

The following before the first Header is FAIL:

- hero/system name introduction;
- `先给结论`;
- summary paragraph;
- `我重新核了一遍`;
- key risk statement;
- any Verified/Candidate statement.

Only a necessary clarification question may precede normal result generation.

## Case 6 — Standard profession names only

FAIL examples in Header:

- `主责：技能数值`
- `协同：战斗程序`
- `主责：品质基准设计`

when these are being used as substitutes for actual Skills.

PASS by mapping to canonical professions, e.g.:

- `数值策划（balance-design）`
- `代码 / 实现验证（code-verification）`
- `技能 / 英雄策划（skill-design）`

Fine-grained responsibilities may appear in body text, not as invented Skill identities.

## Case 7 — Long answer drift

Generate an answer with at least 10 numbered result sections. Every independent section must still pass the Header gate; omission in later sections is FAIL.

## Case 8 — User does not mention Header

Prompt A:

```text
检查这个英雄的配置、代码和数值问题。
```

Prompt B:

```text
检查这个英雄的配置、代码和数值问题。每个结果前显示【本次专业视角】。
```

A and B must have the same Header behavior. If only B shows Headers, FAIL.

## Pre-Send Lint Acceptance

Before emitting, verify:

- first substantive block begins with Header;
- each independent numbered result has Header;
- each modification/bug/verified/candidate conclusion belongs to a Header block;
- Decision Object transitions reroute;
- profession names map to real Skills.
