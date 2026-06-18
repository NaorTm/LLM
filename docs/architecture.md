# Architecture

## Status

This document defines initial package boundaries only. It does not select providers, storage engines, model frameworks, or orchestration technology.

## Quality Attributes

- Scientific assertions remain traceable to an immutable source and exact location.
- Uncertainty, disagreement, missing data, and abstention remain explicit.
- Untrusted documents and model output never become executable instructions.
- Deterministic processing and validation are preferred over model calls.
- Workflows remain testable, reproducible, observable, and cost-bounded.

## Package Boundaries

- `ingestion`: acquire and normalize literature while preserving source identity and locations.
- `extraction`: produce schema-valid scientific records tied to supporting evidence.
- `graph`: map validated records into versioned semantic structures with provenance.
- `retrieval`: locate relevant records and evidence for structured or semantic questions.
- `agents`: coordinate future workflows without owning domain rules.
- `evaluation`: measure scientific correctness, grounding, security, reliability, latency, and cost.

Domain packages should expose narrow typed interfaces. Provider-specific adapters should remain outside domain rules and depend inward on those interfaces. Cross-package data contracts must be versioned and tested before implementation.

## Data Flow

The intended direction is ingestion to extraction to graph, with retrieval reading validated graph and evidence records. Evaluation observes every stage. Future agents may coordinate these capabilities but must not bypass validation, provenance, or cost controls.

## Deferred Decisions

The corpus domain, document formats, extraction models, ontology representation, graph technology, retrieval strategy, persistence, APIs, and deployment model remain undecided. Resolve them through plans, evaluations, and decision records before implementation.
