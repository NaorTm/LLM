# Competency Questions

These questions define the minimum useful query surface for the first ontology and evaluation set. A system must answer with the evidence required by `evidence_contract.md`; absence claims require explicit source evidence or a bounded-corpus qualification.

| ID | Query type | Competency question |
| --- | --- | --- |
| CQ-01 | entity lookup | Which papers introduce or use a learned proposal distribution in a particle filter, and what is the proposal conditioned on? |
| CQ-02 | relation query | Which learned proposal is used by each method, and how is that proposal related to the transition model, observation model, and importance weight? |
| CQ-03 | evidence-grounded QA | For a method with a learned proposal, does the paper derive or state an importance correction consistent with its stated proposal and target distribution? Cite the equation or algorithm text; do not infer validity from a method name. |
| CQ-04 | relation query | Which papers compare against an auxiliary particle filter (APF), under which datasets, particle counts, metrics, and model assumptions? |
| CQ-05 | entity lookup | Which datasets, simulated systems, benchmarks, metrics, and evaluation protocols are used by each paper? |
| CQ-06 | evidence-grounded QA | What evidence does a paper report for weight degeneracy, particle impoverishment, mode collapse, or improved particle diversity, and how is the failure mode measured? |
| CQ-07 | relation query | Is a paper's contribution algorithmic, application-only, or mixed, and which extracted contribution statements support that classification? |
| CQ-08 | evidence-grounded QA | What limitations, assumptions, and failure conditions do the authors explicitly report for the proposed particle-filter method? |
| CQ-09 | evidence-grounded QA | Which experiments and ablations directly test the paper's main algorithmic contribution, and what results are reported? |
| CQ-10 | evidence-grounded QA | Which major claims are supported by reported quantitative or qualitative results, and which claims lack direct experimental support in the paper? |
| CQ-11 | relation query | Which papers extend, compare with, apply, reproduce, or critique earlier particle-filter or DPF work, and what source text supports each relation? |
| CQ-12 | entity lookup | For each method, what proposal, weighting rule, resampling strategy, differentiable component, particle count, and training objective are explicitly specified? |
| CQ-13 | research-gap query | Within the bounded corpus, which combinations of learned proposal, explicit importance correction, APF comparison, and degeneracy evaluation have not been jointly evaluated? |
| CQ-14 | research-gap query | Which author-reported limitations recur across multiple DPF papers without a cited experiment or later paper in the corpus that addresses them? |

## Interpretation Rules

- `APF` means auxiliary particle filter; preserve any more specific variant named by a paper.
- Separate an explicit negative result from missing or unextracted information.
- Record results with their dataset, split, metric, units, particle count, baseline, and experimental conditions when available.
- Treat algorithmic-versus-application classification as an evidence-backed paper attribute, not a judgment based only on title or venue.
- Phrase research gaps as observations about the versioned corpus, never as universal claims about the field.
