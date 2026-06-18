---
name: cost-control
description: Estimate, instrument, and reduce metered costs for the Semantic Research Agent without compromising scientific quality. Use for LLM and embedding budgets, batch jobs, caching, provider or model selection, token optimization, retry policy, corpus-scale projections, and cost regressions.
---

# Cost Control

## Workflow

1. Identify all metered units: model input/output, embeddings, OCR, network APIs, compute, storage, and reprocessing.
2. Record the pricing source and date. Separate known charges from uncertain or excluded costs.
3. Estimate per-item and total cost using representative size distributions, cache assumptions, failure rate, and bounded retries. Show the formula.
4. Set per-request, per-job, and corpus budgets plus warning and hard-stop thresholds.
5. Run a small representative sample. Compare actual units, quality, latency, and failures with the estimate before scaling.
6. Instrument model/provider, versions, input/output units, price basis, cache status, latency, retries, and job identifiers without logging secrets.
7. Optimize in order: eliminate unnecessary calls, narrow inputs, reuse validated results, batch safely, then consider cheaper models.
8. Re-run relevant evaluations after any optimization. Reject savings that cross scientific or reliability thresholds.
9. Make batch work cancellable, resumable, idempotent, and safe when a budget stop occurs.

## Cost Review

Report fixed and variable costs, cost per paper/page/extraction/query, projected corpus total, worst-case retry exposure, and sensitivity to document size and cache hit rate. Require explicit approval before corpus-scale paid work or provider changes. Never allow an unbounded model loop, retry loop, retrieval fan-out, or recursive agent delegation.
