---
name: evaluate-idea
description: >
  Evaluate whether a research idea is worth pursuing before investing months of effort.
  Stress-tests ideas along 7 dimensions (novelty, impact, timing, feasibility,
  competition, nugget clarity, narrative potential) using 3 specialist agents.
  Delivers a PURSUE / PARK / KILL verdict with actionable next steps.
  Based on Carlini's research philosophy and the RS1-RS8 principles.
allowed_tools:
  - Agent
  - Read
  - Write
  - Glob
  - Grep
  - Bash
  - WebSearch
  - WebFetch
  - mcp__academic-search__academic_search_all
  - mcp__academic-search__academic_search_semantic_scholar
  - mcp__academic-search__academic_search_arxiv
  - mcp__academic-search__academic_snowball
user_invocable: true
---

# /evaluate-idea — Research Idea Stress-Test

Read `skills/idea-engine/SKILL.md` and execute the full 6-phase idea evaluation pipeline.

The user provides a research idea, topic, or question. Run the complete evaluation:
Phase 1 (SEED) → Phase 2 (DIVERGE) → Phase 3 (EVALUATE) → Phase 4 (DEEPEN) →
Phase 5 (FRAME) → Phase 6 (DECIDE).

Save the evaluation to `research-evaluations/YYYY-MM-DD-<topic-slug>.md`.

If the verdict is PURSUE and the user wants to proceed, hand off to the paper machine
pipeline (Phase 1: Reconnaissance).
