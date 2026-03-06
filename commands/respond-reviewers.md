---
description: >
  Process reviewer or co-author feedback and implement revisions.
  Accepts annotated PDF, pasted comments, or reviewer report.
  Extracts review points, classifies actions, presents change plan for approval,
  implements changes, recompiles LaTeX, generates latexdiff, and documents everything.
---

# Respond to Reviewers: **$ARGUMENTS**

Read the review-engine skill at `skills/review-engine/SKILL.md` and execute the full
7-step workflow:

1. **EXTRACT** review points from the provided input
2. **MAP** each point to its location in `paper.tex`
3. **CLASSIFY** action type and priority for each point
4. **PLAN** and present the change plan for user approval (quality gate)
5. **IMPLEMENT** approved changes in dependency order
6. **VERIFY** by recompiling LaTeX and generating latexdiff
7. **DOCUMENT** with change log, revision letter, and orchestration log entry

## Input

`$ARGUMENTS` can be:
- **File path** to an annotated PDF (e.g., `@review_r1.pdf`)
- **Pasted reviewer comments** from a journal decision letter
- **"round N"** to continue a numbered revision series
- **Self-review output** from Phase 6

## Output

- Updated `paper.tex` with all approved changes implemented
- Recompiled `paper.pdf` (0 errors)
- `paper_diff.pdf` with visual change tracking (latexdiff)
- `outputs/revision_log_rN.md` with detailed change log
- Optional: `outputs/revision_letter.md` for journal R&R responses
