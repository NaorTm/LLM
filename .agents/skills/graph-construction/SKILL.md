---
name: graph-construction
description: Construct or evolve a provenance-rich scientific knowledge graph from validated records. Use for graph mapping, stable IDs, entity resolution, deduplication, constraints, incremental updates, conflict representation, graph migrations, and graph quality checks.
---

# Graph Construction

## Workflow

1. Accept only schema-valid source records with stable document/version and evidence identifiers.
2. Map records to versioned node and edge types without dropping provenance, extraction method, timestamps, or uncertainty.
3. Generate stable deterministic identifiers where identity is established. Keep uncertain matches separate and record candidate links.
4. Resolve entities using conservative, explainable rules. Require stronger evidence for merges than for candidate relationships.
5. Represent claims and measurements in their experimental context; retain contradictions and source-specific values.
6. Enforce ontology constraints before committing. Quarantine invalid records with actionable diagnostics.
7. Make writes idempotent and transactional at a documented boundary. Support safe resume after partial failure.
8. Version transformations and preserve lineage from graph element to input record and exact source span.
9. Test clean rebuilds, incremental updates, deletions/corrections, ontology migrations, and deterministic parity.

## Quality Gates

Measure constraint violations, provenance coverage, duplicate and false-merge rates, dangling references, unresolved candidates, conflict preservation, and rebuild parity. Sample merged identities and high-degree nodes for human review.

Do not mutate historical scientific assertions in place when a paper, extraction, or ontology changes. Create versioned state or an auditable supersession path. Never infer semantic support from citation alone.
