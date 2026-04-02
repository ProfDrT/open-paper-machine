# Research Strategy Principles (RS1-RS8)

Derived from Nicholas Carlini's "How to Win a Best Paper Award" (2026) and
the research-companion framework by Andre Huang.

These principles guide idea evaluation and strategic research decisions throughout
the Open Academic Paper Machine.

---

## A. Problem Selection

### RS1: The Novelty Test
**"If you don't do this, how many months until someone else does?"**

The magnitude of your contribution correlates with the gap between your publication
and when someone else would independently achieve similar results. Favor problems
where your unique combination of skills creates a gap of months or years, not weeks.

*Application:* When evaluating ideas in the Idea Critic, estimate the specific
timeline and name the groups most likely to do similar work.

### RS2: The Conclusion-First Test
**"Can you write a compelling conclusion right now, without doing the work?"**

Before investing, write the best-case conclusion. If you cannot articulate why the
work matters beyond "our method improved numbers by X%," the project may lack
sufficient impact. If the conclusion writes itself and feels important, proceed.

*Application:* Phase 5 of the idea-engine pipeline. The most important single test.
If the conclusion is hollow, the idea dies here — regardless of how strong other
dimensions look.

### RS3: The Nugget Test
**"Can you state the key insight in one sentence?"**

Every strong paper advances exactly one idea expressible in a few words. Multiple
ideas dilute the message. Write the nugget down and keep it visible throughout the
project. Every experiment and figure should connect to it.

*Application:* The nugget from Phase 0 becomes the guiding star for the entire paper.
If the nugget is fuzzy, the paper will be unfocused.

---

## B. Execution Strategy

### RS4: Fail Fast
**"Start with the sub-problem most likely to kill the project."**

Most ideas die upon contact with reality. Order work by risk, not by logical sequence
or ease. If the hardest part doesn't work, nothing else matters. Don't build the
polished version when a small prototype will tell you whether the core idea works.

*Application:* The "One Question" from the Idea Critic output should target the
highest-risk assumption. The first step after PURSUE should de-risk the project.

### RS5: Kill Early
**"A working project with low impact is worse than a killed project."**

If the paper lacks potential impact, terminate it. Sunk cost is not a reason to
continue. Convert to a workshop paper or blog post if it has some value. This is
Stephen King's "kill your darlings" applied to research.

*Application:* The Idea Critic gives KILL verdicts when warranted. The Research
Strategist's Project Triage mode catches projects that should have been killed earlier.

### RS6: Unreasonable Effort
**"Strengthen 'sometimes' to 'usually' through additional work."**

Great papers result from effort exceeding reasonable expectations. Run additional
trials, control confounders, anticipate skeptical reader questions. This is the
"magic" of great research: spending more time than anyone would reasonably expect.

**Critical:** This principle applies AFTER RS4 and RS5. Unreasonable effort on the
wrong project is still wasted effort. First confirm the idea is worth pursuing,
then go to unreasonable lengths to execute it.

*Application:* Phases 4-6 of the paper machine pipeline (Production, Assembly, Export).
Once the idea has passed Phase 0, execute with maximum quality.

---

## C. Strategic Positioning

### RS7: Comparative Advantage
**"Research space is high-dimensional; find your unique corner."**

You are almost certainly world-best at some specific combination of skills, knowledge,
and perspective. Because the space is high-dimensional, even researchers who aren't
the best at any single thing can be uniquely positioned at a specific intersection.

Being first in a young field carries outsized impact. Bridging distant fields creates
contributions researchers in either field alone would not produce.

*Application:* The Research Strategist's Comparative Advantage Mapping mode.
The Brainstormer's cross-field connections dimension.

### RS8: Timing Awareness
**"Impact = skill in domain x importance of domain at this moment."**

You control your skill but not when the world needs it. Being too early means
reviewers reject your premises. Being too late means the contribution is incremental.
Monitor which problems are *becoming* more important, not just which are currently popular.

*Application:* The "Timing" dimension in the Idea Critic. The Research Strategist's
Impact Forecasting mode.

---

## The Three Kill Conditions (Carlini)

Research projects should be killed under three distinct conditions:

1. **Technical failure.** The core idea doesn't work. De-risk early (RS4).
2. **Low impact.** It works, but the conclusion-first test fails (RS2 + RS5).
3. **Opportunity cost.** Something better came along. Paper impact is distributed
   exponentially — a paper 100x more important justifies abandoning a 90% complete
   mediocre paper. But beware excitement bias: new ideas always sound better.

---

## Sources

- Carlini, N. (2026). "How to Win a Best Paper Award."
  https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html
- Huang, A. (2025). research-companion: Strategic research thinking agents.
  https://github.com/andrehuang/research-companion
