# Roadmap

This roadmap sequences discovery and delivery; it does not preselect an implementation stack. Each phase requires an approved plan, evaluation criteria, and cost boundary before product work begins.

## Phase 0: Foundations

- Establish agent instructions, planning, decision, evaluation, and cost policies.
- Define repository quality, security, provenance, and minimal-diff expectations.
- Exit when the infrastructure documents and skills are validated.

## Phase 1: Research Contract And Baselines

- Select a narrow scientific domain and representative corpus under clear licensing terms.
- Define target research questions, user workflows, terminology, and evidence requirements.
- Build human-reviewed gold examples and baseline retrieval/extraction evaluations.
- Exit when scope, datasets, metrics, thresholds, and budgets are approved.

## Phase 2: Evidence-Preserving Ingestion

- Design and validate document identity, parsing, normalization, chunking, and provenance contracts.
- Handle malformed inputs, versions, corrections, deduplication, and prompt-injection content.
- Exit when ingestion quality and source-location stability meet evaluation thresholds.

## Phase 3: Ontology And Structured Extraction

- Design a minimal ontology from validated competency questions.
- Implement schema-constrained extraction with evidence spans, uncertainty, and abstention.
- Exit when extraction and ontology consistency meet held-out quality and cost gates.

## Phase 4: Knowledge Graph

- Construct an idempotent, versioned graph with entity resolution and complete provenance.
- Validate constraints, rebuild parity, conflict representation, and migration behavior.
- Exit when graph quality gates pass on the representative corpus.

## Phase 5: Research Queries And Grounded Answers

- Support semantic retrieval, structured queries, and citation-grounded synthesis.
- Evaluate faithfulness, evidence recall, citation correctness, uncertainty, security, latency, and cost.
- Exit when answers meet predefined human-reviewed acceptance thresholds.

## Phase 6: Gap Analysis And Hardening

- Add cautious research-gap analysis that distinguishes missing evidence from genuine gaps.
- Improve observability, reproducibility, access control, failure recovery, and corpus-scale economics.
- Exit only after adversarial evaluation and documented limitations.

## Current Scope

Only Phase 0 is authorized. Do not implement product components until a subsequent phase is explicitly approved.
