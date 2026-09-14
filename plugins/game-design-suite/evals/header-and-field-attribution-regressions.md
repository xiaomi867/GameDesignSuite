# Header & Field Attribution Regression Cases

These cases protect two production-critical behaviors:

1. Professional Context Header must remain visible even when a host enters a specialist Skill directly.
2. Spreadsheet/config values must never be attributed to the wrong field.

## 1. Direct Specialist Entry Still Shows Header

### Prompt

```text
检查 P10BattleBuff.xlsx 里 BUF_bear_taunt 的 CoverCheckType 是否正确。
```

### Pass

The first visible answer section includes a Professional Context Header such as:

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

## 2. Do Not Duplicate Header

### Setup

`game-design` already emitted the Header, then delegates to `config-audit`.

### Pass

`config-audit` continues the answer without emitting a second full Header.

### Fail

The response repeats multiple identical routing banners.

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
