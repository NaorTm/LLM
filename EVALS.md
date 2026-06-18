# Evaluation Policy

Evaluations are versioned tests of scientific and system behavior. No model, prompt, extraction schema, ontology, retrieval strategy, or graph rule should be promoted on anecdotal examples alone.

## Evaluation Sets

- Maintain small smoke fixtures for fast local checks.
- Maintain a representative, human-reviewed gold set with source spans and adjudication notes.
- Keep a held-out set that prompt and implementation authors do not tune against.
- Include difficult negatives, conflicting papers, missing evidence, malformed documents, retractions or corrections, and prompt-injection content.
- Version datasets and record licenses, domain coverage, sampling method, and known limitations.
- Prevent project-side train/test leakage and document possible model-training contamination when it cannot be ruled out.

## Core Measures

- Ingestion: document completeness, section/order fidelity, metadata accuracy, and source-location stability.
- Extraction: entity/relation/claim precision, recall, F1, schema-valid rate, evidence-span accuracy, abstention quality, and calibration.
- Ontology and graph: constraint violations, duplicate rate, identity precision, dangling references, provenance coverage, and deterministic rebuild parity.
- Retrieval and answers: claim-level evidence recall, citation precision and recall, entailment/faithfulness, answer completeness, unsupported-claim rate, and appropriate uncertainty.
- Operations: latency percentiles, failure/retry rates, throughput, and cost per useful unit.
- Security: resistance to document-borne prompt injection, data exfiltration attempts, parser abuse, and unsafe tool invocation.

## Procedure

1. State the hypothesis, baseline, dataset version, metrics, slices, and acceptance thresholds before running.
2. Run the baseline and candidate under pinned configurations and comparable conditions.
3. Preserve raw outputs, traces, failures, usage, and code/configuration identifiers needed for reproduction.
4. Review aggregate metrics and meaningful slices; inspect false positives, false negatives, and unsupported answers.
5. Require human scientific review for semantic correctness claims. LLM-as-judge may assist but must be calibrated against human labels and cannot be the sole authority.
6. Record regressions explicitly. Do not hide a failed slice behind a better overall average.

Promotion requires meeting predefined thresholds with no unacceptable scientific, security, latency, or cost regression. Any unsupported scientific assertion or citation that does not support its attributed claim is release-blocking until corrected or explicitly abstained. If evidence is inconclusive, retain the existing baseline.
