---
name: agent-evaluation
description: Design and run reproducible evaluations for the Semantic Research Agent. Use for benchmarks, gold datasets, regression suites, retrieval and answer quality, extraction metrics, security tests, LLM-as-judge calibration, experiment comparison, and release gates.
---

# Agent Evaluation

## Workflow

1. State a falsifiable hypothesis and the decision the evaluation will inform.
2. Freeze task definitions, dataset and ontology versions, baseline, candidate, metrics, slices, and thresholds before running.
3. Build representative examples with exact evidence and adjudication guidance. Keep a held-out set and track leakage risk.
4. Include negatives, ambiguity, disagreement, missing evidence, malformed inputs, prompt injection, and rare but costly failures.
5. Pin code, model, prompt, parameters, random seeds where supported, and external data snapshots.
6. Run baseline and candidate under comparable conditions. Preserve raw outputs, traces, errors, latency, usage, and cache status.
7. Compute aggregate and slice metrics with uncertainty or repeated runs where nondeterminism matters.
8. Perform blinded human scientific review for semantic correctness. Calibrate any LLM judge against those labels and monitor judge bias.
9. Analyze failure categories, not only averages. Report regressions and threshold failures without selective omission.
10. Store a concise evaluation report and convert stable failures into regression fixtures.

## Release Rule

Promote only when predefined scientific, security, reliability, latency, and cost gates pass. Treat unsupported claims and incorrect citations as critical even when answers appear plausible. If results are noisy or underpowered, report inconclusive rather than choosing the preferred candidate.
