# Header & Field Attribution Regression Cases

These cases protect three production-critical behaviors:

1. Professional Context Header must remain visible even when a host enters a specialist Skill directly.
2. Every independent result must expose its own actual professional routing.
3. Spreadsheet/config values must never be attributed to the wrong field.

## 1. Direct Specialist Entry Still Shows Header

### Prompt

```text
检查 P10BattleBuff.xlsx 里 BUF_bear_taunt 的 CoverCheckType 是否正确。
```

### Pass

The result begins with a Professional Context Header such as:

```text
【本次专业视角】
主责：配置审计（config-audit）
```

If `code-verification` has not actually been loaded, it must not be listed as an active supporting discipline.

### Fail

- no header at all;
- header appears only after the conclusion;
- claims unrelated Skills were used.

---

## 2. Repeat Header for Every Independent Result

### Setup

The answer finds two independent configuration findings one after another.

### Pass

Each finding receives its own Header, even if both use exactly the same routing:

```text
【本次专业视角】
主责：配置审计（config-audit）
```

...result 1...

```text
【本次专业视角】
主责：配置审计（config-audit）
```

...result 2...

### Fail

- only the first result has a Header;
- the second Header is omitted because “the profession has not changed”.

---

## 3. CoverCheckType Must Not Become UniqueId

### Data

For one row:

```text
Key = BUF_bear_taunt
UniqueId = <blank>
CoverCheckType = 2
```

### Pass

The answer records:

```text
P10BattleBuff.xlsx | BUF_bear_taunt | CoverCheckType | 2
P10BattleBuff.xlsx | BUF_bear_taunt | UniqueId | <blank>
```

and does not infer any `UniqueId = 2` behavior.

### Fail

Any statement equivalent to:

```text
BUF_bear_taunt 的 UniqueId = 2
```

when the 2 actually belongs to `CoverCheckType`.

---

## 4. Distribution Must Stay Bound to Its Field

### Data

`UniqueId` is blank for most rows. `CoverCheckType` commonly contains 1/2/3.

### Pass

A distribution report explicitly names which field is being counted and derives values only from that column.

### Fail

- reports `UniqueId` distribution using `CoverCheckType` values;
- states “大量 UniqueId=2” because another field commonly equals 2.

---

## 5. User Correction Triggers Full Re-read

### Prompt Sequence

1. Assistant attributes value 2 to the wrong field.
2. User says: `你看错字段了，2 是 CoverCheckType，不是 UniqueId。`

### Pass

Assistant:

- explicitly retracts conclusions dependent on `UniqueId = 2`;
- restarts from Header Row -> FieldName -> RowKey -> RawValue;
- preserves only conclusions independent of the mistaken field attribution.

### Fail

- tries to preserve the old conclusion with a new explanation;
- says “虽然字段看错，但结果应该差不多”。

---

## 6. Code Verification Waits for Field Identity

### Data

Code contains several enums where value `2` has different meanings.

### Pass

Before interpreting value 2, `code-verification` requires the config tuple:

```text
Table/Sheet + RowKey/ID + FieldName + RawValue
```

Then follows that exact field through Data Model -> Parser -> Runtime Consumer.

### Fail

Searches code for “2” or a familiar enum first and retrofits that meaning onto the spreadsheet value.

---

## 7. Critical Field Two-Pass Check

### Prompt

```text
给出需要修改的 GroupKey、UniqueId、CoverCheckType、Target 和 BuffCfg。
```

### Pass

Before final modification output, all listed critical fields are rechecked against their exact row/key and field names.

### Fail

Uses a first-pass visual/read assumption without rechecking fields that directly drive edits.

---

## 8. Screenshot Proximity Is Not Schema

### Setup

A screenshot visually places `UniqueId` near a cell showing `2`, but the actual table header mapping puts that cell under `CoverCheckType`.

### Pass

The assistant treats screenshot proximity as insufficient evidence and relies on actual schema/header mapping.

### Fail

Uses visual adjacency to assign the numeric value to `UniqueId`.

---

## 9. Bear CoverCheckType Mismatch Is Config-Audit Primary

### Data

```text
BUF_bear_def_pct       CoverCheckType = 3
BUF_bear_def_pct_lv2   CoverCheckType = 2
BUF_bear_def_pct_lv3   CoverCheckType = 2
BUF_bear_def_pct_lv4   CoverCheckType = 2
BUF_bear_def_pct_lv5   CoverCheckType = 2
```

### Pass

The finding that the base row differs from lv2~lv5 begins with:

```text
【本次专业视角】
主责：配置审计（config-audit）
```

If the implementation is also consulted, `code-verification` may be supporting.

### Fail

Uses:

```text
主责：数值策划（balance-design）
```

merely because the values are numeric or because the mismatch may ultimately affect strength.

---

## 10. Code Meaning Gets Its Own Result Block

### Continuation of Case 9

The answer then explains what `CoverCheckType = 2/3` means in the parser/runtime.

### Pass

A new result block starts with:

```text
【本次专业视角】
主责：代码 / 实现验证（code-verification）
协同：配置审计（config-audit）
```

### Fail

Keeps the previous config-audit Header while presenting a distinct code-semantics conclusion without rerouting.

---

## 11. Strength Impact Gets Its Own Result Block

### Continuation of Case 9/10

The answer evaluates how the behavior difference affects Buff uptime, EHP, DPS, or hero strength.

### Pass

Only now can a result use:

```text
【本次专业视角】
主责：数值策划（balance-design）
```

with only actually used supporting Skills.

### Fail

Labels the original field mismatch itself as a balance finding.
