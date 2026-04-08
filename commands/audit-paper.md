---
description: Audit a paper's empirical claims against the linked code repository — catches MISMATCH, MISSING, and PARTIAL claims before submission
---

# Audit Paper vs. Code: **$ARGUMENTS**

Activate the **audit-engine** skill. Read `skills/audit-engine/SKILL.md` in full.

Execute the complete 5-step audit workflow:
1. Extract testable claims from `paper.tex` (or `draft.md`)
2. Locate the code repository (from `$ARGUMENTS`, or scan paper for a code URL, or ask once)
3. Map the repo (entry points, configs, data loaders, results)
4. Search for evidence per claim using `Grep` + `Read` with file:line citations
5. Classify each claim as CONFIRMED / PARTIAL / MISSING / MISMATCH / NOT_AUDITABLE
6. Generate `outputs/audit_report.md`

`$ARGUMENTS` may contain:
- A repo path or GitHub URL to audit against
- A scope hint (e.g., "only Section 4", "only the training claims", "tier 1 only")
- Both

If no code repository can be located, stop and ask the user for a path or URL before proceeding.

This is a **static audit**: no code is executed. For full reproducibility, re-run training and evaluation manually after the audit surfaces any MISMATCH or MISSING claims.
