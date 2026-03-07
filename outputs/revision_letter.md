# Response to Reviewers

Dear Editor,

Thank you for the constructive reviews of our manuscript "The Open Academic Paper Machine: An Autonomous LLM Plugin for End-to-End Academic Paper Production." We have carefully addressed all reviewer comments as detailed below. Changes are marked with [R1-XX] in the manuscript for traceability.

---

## Reviewer 1 (The Methodologist)

### Comment 1.1 (W1): Single-case evaluation with author-as-evaluator
> The evaluation rests entirely on a single case study in which the system's developer is also its sole evaluator.

**Response:** We acknowledge this as a fundamental limitation of the current evaluation. We have added a structured validity discussion (Section 6.5) that explicitly addresses construct validity threats from author-as-evaluator bias and external validity threats from the single-case design. We outline specific mitigations and identify external evaluation with independent raters as a priority for future work.
**Change:** Section 6.5 — restructured as four-part validity discussion (internal, construct, external, conclusion validity).

### Comment 1.2 (W2): Self-referential circularity and version mismatch
> The companion paper was produced with v5.3.0/v5.4.0, but the paper describes v6.0.0.

**Response:** We have added a "Version scope" paragraph in Section 5.2 that explicitly delineates which capabilities were tested (core pipeline v5.3/5.4) and which remain unevaluated (v6.0.0 extended engines). We also note that the simulated peer-review engine was applied to the companion paper post-hoc, partially addressing this gap.
**Change:** Section 5.2 — new "Version scope" paragraph.

### Comment 1.3 (W3): Lack of comparison
> The paper does not compare the system's output quality against any baseline.

**Response:** We acknowledge this limitation in the new conclusion validity discussion (Section 6.5) and have added controlled comparison as an explicit future research direction.
**Change:** Section 6.5 (conclusion validity paragraph) and future research directions.

### Comment 1.4 (W4): No validity discussion
> There is no structured discussion of internal, external, construct, and conclusion validity threats.

**Response:** We have replaced the single limitations paragraph with a comprehensive validity discussion addressing all four threat types with specific mitigations.
**Change:** Section 6.5 — complete rewrite with structured validity framework.

### Minor Comments

**M1 (10-15% time window):** Added "across STEM and social science disciplines in 2023–2024" (Section 1).
**M4 (45-min breakdown):** Added per-phase timings: Reconnaissance ~8 min, Framing ~5 min, Structure ~4 min, Production ~20 min, Assembly ~3 min, LaTeX/PDF ~5 min (Section 5.2).
**M5 ("+" notation):** Added explanatory footnote to Table 1 caption clarifying that "N+" means "from Phase N onwards."

---

## Reviewer 2 (The Theorist)

### Comment 2.1 (W1): Design principles lack theoretical grounding
> The five DPs are derived inductively from development experience rather than deductively from established theory.

**Response:** We have added theoretical grounding for all five design principles: DP1 is now connected to Parnas (1972) on modular decomposition and Flower & Hayes (1981) on cognitive process theory; DP2 extends Parnas's information hiding principle; DP3 is grounded in Swales (1990) genre analysis and Hyland (2005) metadiscourse theory; DP4 draws on Vygotsky (1978) scaffolding theory; DP5 operationalizes Denzin (1978) triangulation methodology.
**Change:** Section 6.2 — substantial expansion with theoretical anchoring for each DP. Six new references added.

### Comment 2.2 (W2): Ambiguous contribution positioning
> The paper oscillates between presenting primarily an artifact and primarily design knowledge.

**Response:** We have clarified that the primary contribution is the artifact itself, accompanied by nascent design knowledge (Level 2) in the form of five theoretically grounded design principles. We have also added a transferability paragraph demonstrating how the DPs could apply to analogous systems (grant writing, thesis supervision, regulatory compliance).
**Change:** Section 3.1 — reframed contribution positioning and added transferability examples.

### Comment 2.3 (W3): Missing writing process literature
> The paper does not engage with Flower & Hayes, Swales, Hyland.

**Response:** We have added a substantial new paragraph in Section 2.2 that connects our system design to the academic writing process literature, and cross-references this connection to Section 4.3 (skill engines). The writing templates are now explicitly linked to Swales's genre conventions and Flower & Hayes's cognitive scaffolding.
**Change:** Section 2.2 — new paragraph on cognitive process models of writing. Section 6.2 (DP3) — connected to Swales and Hyland.

### Comment 2.4 (W4): Quality criteria underspecified
> The paper never defines "established scholarly quality standards" beyond five ad hoc criteria.

**Response:** We have anchored the evaluation criteria in published frameworks: Hevner (2004) DSR evaluation guidelines, Webster & Watson (2002) review quality criteria, and Swales (1990) genre conventions.
**Change:** Section 3.4 — evaluation criteria now reference established quality frameworks.

### Minor Comments

**M1 (60-80 hours):** Added hedging: "estimates vary by discipline and paper type" (Section 1).
**M2 (gap framing):** Refined to "end-to-end automation target with structured human oversight" (Section 1).
**M5 ("competent but not deep"):** Added three-part specification of intellectual depth deficit: inability to challenge frameworks, failure to synthesize unexpected connections, absence of judgment about significance (Section 6.1).
**M6 (publisher implications):** Expanded to full paragraph covering detection challenges, disclosure norms, standardized contribution statements, and the orchestration log as a transparency model (Section 6.4).

---

We believe these revisions substantially strengthen the manuscript's theoretical grounding, evaluation framework, and scholarly positioning. The paper has grown from 17 to 19 pages and now includes 51 references (6 new). We look forward to your assessment.

Sincerely,
Tobias-Benedikt Blask
