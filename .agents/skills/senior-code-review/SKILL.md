---
name: senior-code-review
description: Review changes to the Semantic Research Agent for correctness, security, scientific validity, evidence preservation, tests, cost, and maintainability. Use for pull requests, diffs, patches, refactors, schema changes, and pre-merge quality assessment.
---

# Senior Code Review

## Review Order

1. Read applicable policies and the change intent. Inspect the actual diff and surrounding code.
2. Check behavior against requirements, public contracts, migrations, and backward compatibility.
3. Trace scientific data from source to output. Verify evidence spans, provenance, uncertainty, conflicts, and abstention are not discarded or overstated.
4. Analyze trust boundaries: document-borne prompt injection, parser attacks, unsafe deserialization, injection, path traversal, SSRF, secret leakage, authorization, and dependency risk.
5. Check determinism, idempotency, concurrency, retries, partial failure, cache keys, and reproducibility.
6. Check LLM boundaries: schema validation, bounded context, model/prompt versioning, output distrust, fallback behavior, and token limits.
7. Check cost controls, batching, cache behavior, unbounded fan-out, and accidental corpus-wide work.
8. Evaluate tests for positive, negative, adversarial, regression, and scientific edge cases. Run focused checks when possible.
9. Reject unrelated refactors or generated churn that obscure the behavioral change.

## Finding Standard

Report only actionable findings. For each finding include:

- severity and concise title;
- exact file and tight line range;
- concrete failure scenario and impact;
- why existing validation does not prevent it;
- a direction for correction when non-obvious.

Order findings by severity. Distinguish blocking correctness/security issues from maintainability suggestions. Do not assert a defect without tracing the relevant path. If no findings remain, state that clearly and list residual test or evaluation gaps.
