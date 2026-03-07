# Revision Log — Round 1 (Simulated Peer Review)

**Date:** 2026-03-07
**Reviewer:** Simulated (R1: The Methodologist + R2: The Theorist)
**Source:** simulated_reviews.md
**Review points:** 26 total (14 implemented, 3 deferred, 6 questions addressed in-text, 3 positive/no action)

## Changes Implemented

### Change 1: Ground design principles in theory (CRITICAL)
- **Type:** EXPAND
- **Reviewer said:** R2-W1: "DPs lack theoretical grounding — derived inductively from development experience rather than deductively from established theory"
- **Action:** Added theoretical anchoring for all five DPs: DP1→Parnas (1972) module decomposition + Flower & Hayes (1981) cognitive process model; DP2→Parnas information hiding; DP3→Swales (1990) genre analysis + Hyland (2005) metadiscourse; DP4→Vygotsky (1978) cognitive scaffolding; DP5→Denzin (1978) triangulation methodology
- **Files affected:** paper.tex (Section 6.2), references.bib (+6 new references)

### Change 2: Add structured validity discussion (CRITICAL)
- **Type:** EXPAND
- **Reviewer said:** R1-W4: "Threats to validity not systematically discussed — no structured discussion of internal, external, construct, and conclusion validity"
- **Action:** Replaced single-paragraph limitations with structured four-part validity discussion (internal, construct, external, conclusion validity) with specific threats and mitigations for each
- **Files affected:** paper.tex (Section 6.5)

### Change 3: Add academic writing process literature (MAJOR)
- **Type:** EXPAND
- **Reviewer said:** R2-W3: "Missing engagement with the academic writing process literature — Flower & Hayes, Swales, Hyland"
- **Action:** Added new paragraph in Section 2.2 connecting system design to Flower & Hayes (1981) cognitive process model, Swales (1990) CARS model, and Hyland (2005) metadiscourse analysis. Cross-references to Section 4.3 skill engines.
- **Files affected:** paper.tex (Section 2.2), references.bib

### Change 4: Anchor evaluation criteria in published frameworks (MAJOR)
- **Type:** EXPAND
- **Reviewer said:** R2-W4: "Quality criteria underspecified — using self-defined criteria rather than established ones"
- **Action:** Added grounding in Hevner (2004) DSR evaluation guidelines, Webster & Watson (2002) quality criteria, and Swales (1990) genre conventions to the five evaluation criteria
- **Files affected:** paper.tex (Section 3.4)

### Change 5: Address version mismatch (MAJOR)
- **Type:** EXPAND
- **Reviewer said:** R1-W2/Q1: "Evaluation conducted on v5.3.0/v5.4.0 while paper describes v6.0.0"
- **Action:** Added "Version scope" paragraph explicitly delineating which capabilities were tested by the case study (core pipeline v5.3/5.4) and which remain unevaluated (v6.0.0 extended engines). Notes that simulated peer review was applied post-hoc.
- **Files affected:** paper.tex (Section 5.2)

### Change 6: Clarify contribution framing + transferability (MAJOR)
- **Type:** RESTRUCTURE
- **Reviewer said:** R2-W2: "Contribution positioning ambiguous between artifact and theory"; R2-M3: "Level 2 not fully justified"
- **Action:** Reframed as "primary contribution is the artifact, accompanied by nascent design knowledge (Level 2)." Added transferability examples (grant writing, thesis supervision, regulatory compliance).
- **Files affected:** paper.tex (Section 3.1)

### Change 7: Expand publisher/reviewer implications (MAJOR)
- **Type:** EXPAND
- **Reviewer said:** R2-M6: "Publisher implications underdeveloped"
- **Action:** Expanded from 2 sentences to a full paragraph covering detection challenges, disclosure norms, standardized contribution statements, evaluation criteria for AI vs human depth, and orchestration log as transparency model.
- **Files affected:** paper.tex (Section 6.4)

### Change 8: Fix "+" notation in Table 1 (MINOR)
- **Type:** FIX
- **Reviewer said:** R1-M5: "'1+', '2+' notation unclear"
- **Action:** Added explanatory footnote to Table 1 caption: "N+" means "from Phase N onwards"
- **Files affected:** paper.tex (Table 1 caption)

### Change 9: Specify 10-15% time window (MINOR)
- **Type:** EXPAND
- **Reviewer said:** R1-M1: "Should specify the exact time window and disciplines"
- **Action:** Added "across STEM and social science disciplines in 2023--2024" after the 10-15% claim
- **Files affected:** paper.tex (Section 1, para 2)

### Change 10: Break down 45-min execution by phase (MINOR)
- **Type:** EXPAND
- **Reviewer said:** R1-M4: "Break this down by phase to help readers understand where time is spent"
- **Action:** Added approximate per-phase timings: Reconnaissance ~8 min, Framing ~5 min, Structure ~4 min, Production ~20 min, Assembly ~3 min, LaTeX/PDF ~5 min
- **Files affected:** paper.tex (Section 5.2)

### Change 11: Elaborate "competent but not intellectually deep" (MINOR)
- **Type:** EXPAND
- **Reviewer said:** R2-M5: "What specific aspects of intellectual depth are missing?"
- **Action:** Added three-part specification: (1) inability to challenge frameworks, (2) failure to synthesize unexpected connections, (3) absence of judgment about significance
- **Files affected:** paper.tex (Section 6.1)

### Change 12: Refine gap framing (MINOR)
- **Type:** REPLACE
- **Reviewer said:** R2-M2: "Gap framing needs nuance — some tools are converging toward integration"
- **Action:** Changed "integrated automation target" to "end-to-end automation target with structured human oversight"
- **Files affected:** paper.tex (Section 1, para 3)

### Change 13: Add transferability paragraph (MINOR)
- **Type:** EXPAND
- **Reviewer said:** R2-M3: "Level 2 requires showing how DPs transfer beyond specific instantiation"
- **Action:** Added transferability examples: grant writing, thesis supervision, regulatory compliance documentation
- **Files affected:** paper.tex (Section 3.1) — combined with Change 6

### Change 14: Hedge 60-80 hours estimate (MINOR)
- **Type:** EXPAND
- **Reviewer said:** R2-M1: "60-80 hours relies on single source"
- **Action:** Added "estimates vary by discipline and paper type, but" before the 60-80 hours claim
- **Files affected:** paper.tex (Section 1, para 1)

## Deferred to Future Work

### Deferred 1: External evaluation component
- **Reviewer said:** R1-W1: "Recruit 2-3 independent IS researchers to assess the companion paper"
- **Reason:** Requires human action — recruiting external raters, designing rubric, collecting assessments. Acknowledged in validity discussion (Change 2).

### Deferred 2: Comparison/ablation study
- **Reviewer said:** R1-W3: "Include a controlled comparison against baseline"; R2-Q2: "Template ablation evidence"
- **Reason:** Requires experimental design and execution. Acknowledged in conclusion validity discussion (Change 2) and future research directions.

### Deferred 3: Second template example
- **Reviewer said:** R2-M4: "Add a second template example from a different engine"
- **Reason:** Would add length; deferred to keep paper within page constraints (already grew from 17 to 19 pages).

## Verification

- **Compilation:** Clean (0 errors, 0 undefined references)
- **Page count:** 19 pages (was 17 before revision; +2 pages from expanded content)
- **New references added:** 6 (Flower & Hayes 1981, Swales 1990, Hyland 2005, Parnas 1972, Vygotsky 1978, Denzin 1978)
- **Total references:** ~51 (was ~45)
