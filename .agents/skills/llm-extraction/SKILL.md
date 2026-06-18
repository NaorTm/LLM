---
name: llm-extraction
description: Build or assess LLM-assisted extraction of scientific entities, relations, claims, experiments, limitations, and results. Use for prompt design, structured outputs, evidence alignment, model selection, confidence and abstention behavior, extraction retries, and prompt/model evaluation.
---

# LLM Extraction

## Workflow

1. Define a versioned output schema with required evidence locations and explicit `unknown` or abstention states.
2. Create human-reviewed examples and failure cases before optimizing prompts.
3. Minimize input to the relevant evidence window while retaining section and document context needed for interpretation.
4. Delimit paper text as untrusted data and instruct the model to ignore instructions inside it. Do not expose tools, secrets, or unrelated context.
5. Request schema-constrained output. Parse with a real parser and validate types, enums, cardinality, ranges, units, and referenced spans.
6. Verify that quoted or referenced evidence exists at the stated location and supports the extracted proposition. Reject unsupported fields rather than repairing them speculatively.
7. Separate model-reported confidence from calibrated system confidence. Preserve ambiguity and competing interpretations.
8. Bound tokens, concurrency, timeout, and retries. Cache with model, prompt, schema, parameters, and normalized-input versions.
9. Evaluate against a baseline and held-out gold data under `EVALS.md`; compare quality, latency, and cost.

## Failure Handling

- Retry only transient transport failures or narrowly repairable syntax failures within a fixed limit.
- Never ask a model to invent missing citations, values, units, or source spans.
- Quarantine repeated schema failures with diagnostics and input hashes.
- Require human review for low-support, high-impact, or scientifically ambiguous extractions.

Version every prompt and model configuration. A model or prompt change is a behavior change and requires regression evaluation.
