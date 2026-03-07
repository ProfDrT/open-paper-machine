# Simulated Peer Review

**Paper:** The Open Academic Paper Machine: An Autonomous LLM Plugin for End-to-End Academic Paper Production
**Source reviewed:** paper/paper.tex (v6.0.0)
**Date:** 2026-03-07
**Simulated venue level:** ICIS / ECIS (top IS conference)
**Word count:** ~9,000 words (17 pages)
**References:** ~45 unique references
**Sections:** 7 (Introduction, Related Work, Research Methodology, System Design, Demonstration, Discussion, Conclusion)
**Figures:** 3 | **Tables:** 3

> **Note:** These reviews are AI-generated simulations designed to identify potential weaknesses before formal submission. They follow the structure and tone of real peer reviews at top IS/CS venues. Use `/respond-reviewers simulated_reviews.md` to process this feedback systematically.

---

## Reviewer 1

### Summary

This paper presents the Open Academic Paper Machine, an open-source Claude Code plugin that automates the academic paper production pipeline through fourteen modular skill engines, two MCP servers, and an eight-phase workflow with human checkpoints. The authors follow a Design Science Research methodology, articulate five design principles, and evaluate the system through a self-referential case study in which a companion position paper was produced using the tool. The system covers the full pipeline from multi-database literature search through LaTeX compilation and automated revision. The paper is well-structured and provides extensive technical detail about the artifact's architecture.

### Strengths

- **S1:** The system architecture is thoroughly documented with reproducible detail. Listing 1 (directory structure), Listing 4 (plugin manifest), and Tables 1-2 provide sufficient information for independent replication. The fact that the system is open-source under MIT License on GitHub strengthens this considerably (Section 4.2).

- **S2:** The eight-phase pipeline design (Section 4.4) mirrors established academic writing workflows and provides meaningful human-in-the-loop checkpoints. The orchestration log mechanism (since v5.2.0) that records every phase transition, quality gate decision, and human override is a thoughtful design choice for accountability and is well-aligned with DSR transparency requirements.

- **S3:** The multi-source literature search through four academic databases (Section 4.5) is methodologically sound. The acknowledgment that no single database has comprehensive coverage and the implementation of cross-database deduplication directly addresses known limitations in automated literature retrieval (cf. Bolanos et al., 2024).

- **S4:** The scope note in the introduction (line 79-81) is commendably transparent about the paper's focus on technical feasibility rather than ethical permissibility. This honest scoping prevents the paper from overreaching.

### Weaknesses

- **W1: Single-case evaluation with author-as-evaluator.** The evaluation rests entirely on a single case study (Section 5) in which the system's developer is also its sole evaluator. All five assessment criteria (structural completeness, citation accuracy, argumentative coherence, formatting quality, scholarly contribution) are assessed qualitatively by the author, with no external raters, no blind evaluation protocol, and no inter-rater reliability measures. This creates a significant threat to construct validity and evaluator bias. **Suggestion:** Recruit 2-3 independent IS researchers to assess the companion position paper against the same five criteria using a structured rubric. Even a small external evaluation (n=3 raters) would substantially strengthen the evaluation. Alternatively, consider using automated metrics where feasible (e.g., citation accuracy can be partially automated, structural completeness can be operationalized as a checklist).

- **W2: Self-referential circularity in the case study.** The system is used to produce a companion paper, and that companion paper is used to evaluate the system. This creates a circularity problem: the evaluation cannot reveal fundamental architectural limitations because the evaluation artifact was shaped by the same architectural choices being evaluated. Moreover, the companion paper (Blask & Funk, 2026) was produced with an earlier version (v5.3.0/v5.4.0), yet the paper describes and evaluates the current v6.0.0 architecture. **Suggestion:** Add at least one additional case study where the system produces a paper in a different domain (e.g., a methodological review, a theory paper) using the current v6.0.0 version. Alternatively, clearly delineate which capabilities were tested by the companion paper and which remain unevaluated.

- **W3: Lack of comparison with alternative approaches.** The paper does not compare the system's output quality against any baseline: human-written papers, outputs from competing tools (ChatGPT, Gemini, The AI Scientist), or simpler prompt-based approaches. Without comparison, the reader cannot assess whether the fourteen-engine architecture actually produces better outputs than a skilled researcher using a general-purpose LLM with well-crafted prompts. **Suggestion:** Include a controlled comparison, even if small-scale. For example, give the same research topic to (a) the Open Academic Paper Machine, (b) a researcher using ChatGPT with manual orchestration, and (c) a researcher writing from scratch. Compare outputs using the five evaluation criteria.

- **W4: Threats to validity not systematically discussed.** While Section 6.5 acknowledges limitations, there is no structured discussion of internal, external, construct, and conclusion validity threats as expected in DSR evaluation. The single-case design limits external validity; the author-as-evaluator design threatens construct validity; the self-referential case creates internal validity concerns. **Suggestion:** Add a dedicated paragraph on threats to validity, explicitly mapping each threat to mitigation strategies (or acknowledging where mitigation is absent).

### Minor Comments

- [Section 1, para 2]: The claim that LLM usage markers are present in "10-15% of recent publications" (citing Liang et al.) is striking but should specify the exact time window and disciplines covered.

- [Section 3.3, line 148]: The development timeline ("October 2024 to March 2026") suggests 18 months of iteration, but the evaluation covers only one case. Given this development investment, a multi-case evaluation seems proportionate.

- [Section 4.3, line 260]: The statement that skill engines total "5,300 lines of Markdown" is presented as a quality indicator, but line count is a poor proxy for knowledge quality. Consider adding a qualitative assessment of knowledge coverage (e.g., how many method templates were validated against published methodology papers?).

- [Section 5.2]: The pipeline execution trace mentions "approximately 45 minutes of wall-clock time" for the core phases. It would be useful to break this down by phase (search: X min, framing: Y min, etc.) to help readers understand where the time is spent.

- [Table 1]: The "Phase" column for extended-capability engines uses "1+", "2+", "5+", "6+" notation. Clarify what the "+" means — is it "after Phase X" or "from Phase X onwards"?

### Questions for Authors

1. The companion position paper was produced with versions 5.3.0 and 5.4.0, but the paper describes v6.0.0 with six additional engines. How do the authors ensure that the evaluation conclusions generalize to the current architecture, given that the evaluation artifact was produced with a substantially earlier version?

2. The five evaluation criteria (Section 3.4) are assessed qualitatively. Were any quantitative metrics considered (e.g., citation precision/recall against a gold standard, automated readability scores, structural similarity to published papers in the same domain)?

3. The paper notes that the system "cannot collect or analyze empirical data" (Section 6.5). Given that v6.0.0 added capabilities for SLR screening, simulated peer review, and positioning analysis, have the authors considered extending the system to support empirical data analysis as a future capability?

### Overall Assessment

**Recommendation:** Major Revision
**Confidence:** High — I have extensive experience reviewing DSR papers and evaluating research tools in the IS domain.

The paper presents a technically impressive and well-documented artifact, but the evaluation is its critical weakness. A single self-referential case study evaluated solely by the artifact's developer does not meet the evaluation rigor expected at top IS venues. The contribution claim of a "Level 2 nascent design theory" requires stronger evidence than currently presented. With an external evaluation component, a validity discussion, and ideally a comparison baseline, this paper could make a solid contribution. In its current form, the artifact is convincing but the evaluation is not.

---

## Reviewer 2

### Summary

This paper contributes an open-source plugin for autonomous academic paper production, positioned as a Design Science Research contribution at Level 2 (nascent design theory) in the Gregor & Hevner (2013) taxonomy. The authors claim three contributions: the artifact itself, five generalizable design principles, and a self-referential case study. The paper engages with the emerging literature on AI-based scientific agents and tool-augmented LLMs, positioning the system as the first to target the scholarly *writing* pipeline specifically — as opposed to experimental research pipelines targeted by The AI Scientist and similar systems. The scope note clarifying that this is a technical contribution (what is possible, not what is permissible) is helpful framing.

### Strengths

- **S1:** The positioning against The AI Scientist and its successors (Section 2.1) is precise and well-executed. The distinction between automating *experimental* research workflows (where outputs can be programmatically validated) versus *writing* workflows (where quality is judged by argumentative coherence and theoretical grounding) is a genuinely useful contribution to the discourse (Section 2.1, final paragraph). This frames the gap clearly.

- **S2:** The five design principles (Section 6.2) are clearly articulated and grounded in the development experience. DP3 (Template-Driven Generation) and DP4 (Human-in-the-Loop Checkpoints) are particularly well-motivated: the observation that "without such templates, LLM-generated academic text tends toward superficial, blog-like prose" (Section 4.3) is an important empirical insight from the development process.

- **S3:** The integration of the Massenkoff & Weidmann (2026) labor market findings (Section 6.3) adds a fresh empirical dimension to the practical implications. The argument that "the bottleneck is integration rather than capability" connects nicely to the system's raison d'etre and elevates the discussion beyond mere tool description.

- **S4:** The honest self-assessment in the evaluation (Section 5.3) — acknowledging that "the depth of theoretical engagement is notably shallower than what an experienced human researcher would produce" and that argumentative coherence is only "partially met" — builds credibility. The paper does not overclaim.

### Weaknesses

- **W1: The design principles lack theoretical grounding.** The five DPs are derived inductively from development experience rather than deductively from established theory. DP1 (Phase Decomposition) resembles well-known process decomposition in software engineering (e.g., Parnas' module decomposition) but is not connected to it. DP2 (Skill Modularity) echoes the concept of cognitive task decomposition in AI but is not theoretically anchored. DP3 (Template-Driven Generation) could be grounded in cognitive scaffolding theory or genre theory from writing studies. Without theoretical backing, the DPs remain descriptive observations rather than prescriptive design knowledge — which is what a Level 2 contribution requires. **Suggestion:** For each DP, identify the underlying theoretical mechanism. Why does phase decomposition work for LLMs specifically? What theory of LLM behavior predicts that templates improve output quality? Grounding DPs in theory transforms them from "this is what we did" into "this is what others should do and why."

- **W2: The contribution positioning is ambiguous between artifact and theory.** The paper oscillates between presenting primarily an artifact (Contribution 1) and primarily design knowledge (Contribution 2). At ICIS/ECIS, the reviewers will ask: Is this a systems demonstration paper or a design theory paper? The current framing tries to be both but succeeds fully at neither. As a demonstration paper, the evaluation is too thin; as a design theory paper, the theoretical grounding of the DPs is insufficient. **Suggestion:** Commit to one primary framing. If the artifact is the main contribution, strengthen the evaluation substantially (external raters, comparison). If the design principles are the main contribution, strengthen their theoretical grounding and show how they transfer to other domains (e.g., would the same DPs work for an AI-assisted grant writing system?).

- **W3: Missing engagement with the academic writing process literature.** The paper draws on tool-augmented LLM literature and AI scientist literature but does not engage with the substantial body of work on academic writing *as a cognitive and social process*. Scholarship on academic writing (e.g., Flower & Hayes' cognitive process model, Swales' genre analysis, Hyland's work on metadiscourse) would enrich the theoretical foundation and help explain *why* certain system design choices work. For instance, the six-paragraph introduction template (Listing 5) implicitly implements genre conventions studied by Swales (1990), but this connection is never made explicit. **Suggestion:** Add a brief subsection in Related Work (or integrate into Section 4.3) that connects the system's writing templates to established academic writing theory. This would strengthen DP3 substantially and demonstrate that the templates are not arbitrary but grounded in decades of genre analysis.

- **W4: The "scholarly quality" criterion remains underspecified.** RQ3 asks "to what extent can such a system produce academic papers that meet established scholarly quality standards" — but what are those standards? The paper never defines "established scholarly quality standards" beyond the five ad hoc criteria in Section 3.4. IS has well-established review criteria (e.g., Lee's editorial criteria for MISQ, the AIS Quality Criteria for IS Research). Using established criteria rather than self-defined ones would strengthen the evaluation framework. **Suggestion:** Anchor the evaluation criteria in published review guidelines (e.g., Webster & Watson's literature review quality criteria, Hevner's DSR evaluation criteria, MISQ reviewer guidelines). This would also make RQ3 answerable in a way that the current framework does not fully achieve.

### Minor Comments

- [Section 1, para 1]: The opening statistic ("60-80 hours per manuscript") is a useful hook but relies on a single source (Korinek, 2023). Consider adding corroborating evidence or noting that estimates vary by field and paper type.

- [Section 1, para 3]: The framing of the gap as "the scholarly writing pipeline has not been addressed as an integrated automation target" is strong but could be nuanced. Some would argue that tools like Elicit, SciSpace, and Semantic Scholar Writer are converging toward integration. The gap is more accurately about *end-to-end* integration with human oversight, not about *any* integration.

- [Section 3.1]: The claim of a "Level 2 contribution — a nascent design theory" per Gregor & Hevner (2013) is asserted but not fully justified. Level 2 requires that the design knowledge be generalizable beyond the specific instantiation. The paper would benefit from a paragraph demonstrating how the DPs could transfer to a different system.

- [Section 4.3, Listing 5]: The writing template excerpt (six-paragraph introduction formula) is the most compelling illustration in the paper. Consider adding a second example from a different engine (e.g., the gap formulation heuristics from the theory engine) to show the breadth of template-driven knowledge encoding.

- [Section 6.1]: The phrase "competent but not intellectually deep" aptly characterizes the LLM quality ceiling. This deserves further exploration — what specific aspects of intellectual depth are missing? Is it the inability to challenge existing frameworks, to synthesize unexpected connections, or to exercise judgment about what matters?

- [Section 6.3]: The practical implications for "academic publishers and reviewers" are underdeveloped compared to those for researchers and institutions. Given the system's capabilities, this stakeholder group faces the most direct impact and deserves more attention.

### Questions for Authors

1. The paper claims the system is "the first to focus specifically on the scholarly writing pipeline as an integrated automation target" (Section 1). How do the authors distinguish this from ScholarCopilot (Wang et al., 2025), which also integrates literature retrieval with writing generation? What specifically makes the Open Academic Paper Machine's integration qualitatively different?

2. Design Principle 3 (Template-Driven Generation) is presented as essential for quality, but no ablation is provided. Have the authors tested what happens when the templates are removed — i.e., does the same LLM produce meaningfully worse output without the writing templates? This would provide direct evidence for the principle's value.

3. The paper positions itself within DSR but does not engage with the ongoing debate about what constitutes adequate evaluation in DSR (e.g., Venable et al., 2016; Prat et al., 2015). Given that evaluation is acknowledged as the paper's weakest point, how do the authors respond to the argument that a single case without external validation falls below the evaluation threshold for DSR contributions?

### Overall Assessment

**Recommendation:** Major Revision
**Confidence:** High — I have published on DSR methodology and contribution theory in IS and regularly review for ICIS and EJIS.

The paper addresses a timely and practically relevant problem, and the artifact itself appears to be a genuine contribution to the IS community's toolkit. However, the paper's theoretical scaffolding does not match its ambition. Claiming a Level 2 design theory contribution requires theoretically grounded design principles, not just inductively derived observations from a development process. The disconnect between the strong technical artifact and the weak theoretical framing creates an asymmetry that reviewers will notice. I recommend that the authors either (a) strengthen the theoretical grounding of the design principles by connecting them to established theory (cognitive process models of writing, software engineering decomposition principles, genre theory), or (b) reframe the paper as a primarily artifact-focused contribution and invest the freed space in a stronger multi-case evaluation.

---

## Meta-Reviewer Summary

### Consensus Strengths

1. **Well-documented, reproducible artifact.** Both reviewers agree that the system is thoroughly described with sufficient detail for replication. The open-source release under MIT License strengthens the contribution substantially.

2. **Honest self-assessment.** Both reviewers credit the authors for not overclaiming — the acknowledgment that LLM output is "competent but not intellectually deep" and the scope note on ethics build credibility.

3. **Clear positioning against prior work.** The distinction between experimental research automation (AI Scientist) and writing pipeline automation is recognized as a useful contribution to the discourse.

### Consensus Weaknesses

1. **Insufficient evaluation.** Both reviewers identify the single self-referential case study with author-as-evaluator as the paper's critical weakness. R1 focuses on methodological rigor (no external raters, no validity discussion); R2 focuses on the evaluation framework (ad hoc criteria rather than established standards). Both agree this must be addressed.

2. **Theoretical thinness.** R1 notes the lack of a structured validity discussion; R2 identifies the deeper issue that the design principles lack theoretical grounding. The paper describes *what* was built in impressive detail but insufficiently explains *why* the design choices work, which is required for the claimed Level 2 contribution.

### Divergent Views

- **R1 prioritizes methodological rigor** (external evaluation, baselines, validity framework) while **R2 prioritizes theoretical depth** (grounding DPs in theory, engaging with writing process literature, committing to a clear contribution type). This divergence reveals the paper's fundamental tension: it is an impressive engineering achievement that needs stronger academic framing — but whether that framing should come through better evaluation (R1) or better theory (R2) is a strategic choice for the authors.

- **Version mismatch concern:** R1 raises a specific concern about the evaluation being conducted on v5.3.0/v5.4.0 while the paper describes v6.0.0. R2 does not flag this directly. This is a legitimate concern that should be addressed explicitly.

### Priority Revision Checklist

1. [ ] **Add external evaluation component** — Recruit 2-3 independent IS researchers to assess the companion paper against structured criteria. Even a small-scale external evaluation would address the most critical weakness identified by both reviewers. (Addresses R1-W1, R2-W4)

2. [ ] **Ground the design principles in theory** — For each DP, identify the underlying theoretical mechanism from established literature (cognitive process models, genre theory, software decomposition, scaffolding theory). Transform DPs from descriptive observations to prescriptive, theoretically anchored design knowledge. (Addresses R2-W1, R2-W3)

3. [ ] **Add structured validity discussion** — Include a dedicated paragraph addressing internal validity (self-referential case), construct validity (author-as-evaluator), external validity (single case), and conclusion validity. Map threats to mitigations. (Addresses R1-W4)

4. [ ] **Clarify contribution framing** — Decide whether this is primarily an artifact paper (strengthen evaluation) or a design theory paper (strengthen theoretical grounding). Adjust emphasis accordingly. (Addresses R2-W2)

5. [ ] **Address version mismatch** — Explicitly discuss which v6.0.0 capabilities are evaluated by the case study and which remain unevaluated. Consider adding a brief evaluation of at least one v6.0.0 feature (e.g., run the simulated peer review engine on the companion paper and report results). (Addresses R1-W2, R1-Q1)

6. [ ] **Engage with academic writing process literature** — Add references to Flower & Hayes, Swales, Hyland, or other writing process scholars. Connect the writing templates to established genre analysis. (Addresses R2-W3)

7. [ ] **Anchor evaluation criteria in published guidelines** — Replace or supplement the five ad hoc criteria with established review criteria from IS (e.g., Lee's MISQ criteria, Hevner's DSR evaluation framework, Webster & Watson quality criteria). (Addresses R2-W4, R1-W1)

8. [ ] **Add comparison or ablation** — If feasible, include a comparison against baseline (e.g., skilled prompt engineering without the plugin) or an ablation study (e.g., pipeline with vs. without writing templates). (Addresses R1-W3, R2-Q2)

### Recommended Next Steps

- Run `/respond-reviewers` with `simulated_reviews.md` to systematically address feedback
- Focus on items classified as MAJOR by both reviewers: evaluation and theoretical grounding
- Address consensus weaknesses first (both reviewers flagged them)
- The version mismatch issue (item 5) can be partially addressed by running the peer-review engine on the companion paper and including results as a brief v6.0.0 evaluation vignette
