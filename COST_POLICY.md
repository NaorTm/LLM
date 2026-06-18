# Cost Policy

Cost is a correctness constraint. The system must remain observable, bounded, and reproducible across model calls, embeddings, document processing, storage, and external services.

## Principles

- Use deterministic parsing, filtering, caching, and validation before invoking an LLM.
- Select the least expensive model that meets a measured quality threshold; justify stronger models with evaluation results.
- Estimate cost before corpus-wide jobs. Require an explicit budget and a representative sample run.
- Cache by normalized input, model/provider, prompt version, schema version, and relevant parameters.
- Make retries bounded and idempotent. Never retry permanent failures or invalid outputs indefinitely.
- Batch only when it reduces cost without harming evidence boundaries, isolation, or debuggability.
- Store usage metadata without storing secrets or unnecessary sensitive text.

## Required Controls

Every metered workflow must expose:

- per-request and per-job hard limits;
- timeout, concurrency, and retry limits;
- token or unit estimates before execution;
- actual input/output units, model, price basis, latency, and cache status after execution;
- cancellation and resumability for batch work;
- alerts or fail-closed behavior at configured budget thresholds.

Pricing must be configuration or dated metadata, never an unexplained constant. Estimates must state currency, pricing date, and excluded costs.

## Approval Gates

- Unbudgeted local work: make no paid calls; use mocks, fixtures, or an approved cache.
- Representative evaluation or ingestion sample: record the sample size, estimated maximum spend, and hard-stop value before running.
- Corpus-scale processing, paid reprocessing, or a new provider: require explicit human approval of scope and maximum spend.
- If actual or projected cost reaches the approved maximum, stop before new paid work and preserve resumable state.

## Reporting

Report cost per paper, page or chunk, accepted extraction, and answered query where applicable. Compare quality against cost in evaluations; cheaper is not better when it violates scientific acceptance criteria.
