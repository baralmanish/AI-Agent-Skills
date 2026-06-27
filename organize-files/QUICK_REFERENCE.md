# Organize Files — Quick Reference

## Trigger Phrases

```
"Organize these files"
"Rename these files consistently"
"Clean up my folder structure"
"Sort and reorganize these into a zip"
"Create a naming scheme for these files"
```

## Process Order (Always This Sequence)

1. Understand the goal → what does the user need to _retrieve_ most often?
2. Design the naming scheme → rules first, then apply
3. Design the folder hierarchy → shallow for small sets, deep for large
4. Execute renaming + reorganization
5. Package as downloadable `.zip`
6. Explain decisions briefly

## Naming Pattern Cheat Sheet

| File Type         | Pattern                                         |
| ----------------- | ----------------------------------------------- |
| Reports / Docs    | `[topic]_[YYYY-MM-DD]_[descriptor].[ext]`       |
| Meeting notes     | `[YYYY-MM-DD]_[meeting-type]_[topic].[ext]`     |
| Design / Creative | `[project]_[component]_[variant].[ext]`         |
| Images / Photos   | `[YYYY-MM-DD]_[subject]_[sequence].[ext]`       |
| Data / Exports    | `[source]_[dataset]_[YYYY-MM-DD].[ext]`         |
| Presentations     | `[topic]_[audience]_[YYYY-MM-DD].[ext]`         |
| Invoices          | `[YYYY-MM-DD]_[vendor]_[amount-or-ref].[ext]`   |
| Code files        | Follow language conventions — no dates, use git |

## Version Label Standards

Use: `draft` · `v2` · `review` · `approved` · `final`  
Never: `_FINAL_FINAL` · `_USE_THIS` · `(1)` · `_new_copy`

## Folder Pattern Guide

| Pattern    | Use When                                             |
| ---------- | ---------------------------------------------------- |
| By project | Distinct named projects or clients                   |
| By date    | Time-series, logs, archival (invoices, reports)      |
| By type    | Mixed files needing fast lookup by file format       |
| By topic   | Research, notes, learning materials                  |
| Hybrid     | Large collection with both project + type dimensions |

## Depth Rules

- <50 files → 1–2 levels
- 50–500 files → 2–3 levels
- > 500 files → 3–4 levels max

## Zip Output Format

`[project-or-topic]_organized_[YYYY-MM-DD].zip`

## Reference Files

- `references/NAMING_CONVENTIONS.json` — full naming rules by file type, date format, depth rules, zip output spec
