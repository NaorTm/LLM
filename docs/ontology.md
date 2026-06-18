# Ontology

## Status

No ontology is implemented. This document records the design contract for the first ontology proposal.

## Purpose

The ontology will represent scientific literature in enough detail to answer approved competency questions while retaining the evidence and context required to audit every assertion.

## Design Rules

- Begin with competency questions from a narrow research domain.
- Add only concepts and relations required by validated questions.
- Separate documents and document versions, methods and implementations, datasets and versions, metrics and measured values, and citations and semantic support.
- Represent claims, evidence spans, experiments, conditions, results, limitations, provenance, uncertainty, and disagreement explicitly.
- Never interpret missing extraction as scientific absence.
- Preserve conflicting claims rather than collapsing them into a single truth value.
- Give each entity an identity policy and each relation defined direction, cardinality, and constraints.
- Version ontology changes and evaluate their migration and reprocessing impact.

## Candidate Concepts

Initial investigation may consider papers, authors, methods, algorithms, datasets, metrics, experiments, claims, evidence, limitations, baselines, and results. These are candidates, not an accepted schema.

## Required Outputs Before Implementation

1. Approved competency questions and representative source examples.
2. Definitions with valid and invalid examples.
3. Machine-checkable constraints and identity rules.
4. Provenance and evidence-location requirements.
5. Evaluation fixtures for ambiguity, conflict, missing data, and versioning.
6. A decision record for consequential semantic choices.
