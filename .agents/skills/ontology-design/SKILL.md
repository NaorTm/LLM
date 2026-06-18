---
name: ontology-design
description: Design or evolve the scientific literature ontology and its constraints. Use for competency questions, entity and relation modeling, claim and experiment representation, provenance semantics, controlled vocabularies, identity rules, schema evolution, and ontology review.
---

# Ontology Design

## Workflow

1. Collect concrete competency questions from target research workflows.
2. Extract only the concepts and relations needed to answer them. Start with the smallest useful ontology.
3. Define each class, relation, attribute, direction, cardinality, identifier policy, and allowed unknown state in plain language.
4. Model observations separately from interpretations. Represent claims, evidence, experimental context, limitations, provenance, confidence, and disagreement explicitly.
5. Distinguish paper versions, methods from implementations, datasets from dataset versions, metrics from measured values, and citations from semantic support.
6. Reuse established vocabularies only when their semantics match; document mappings and avoid superficial equivalence.
7. Define machine-checkable constraints and valid/invalid examples.
8. Test competency questions against representative papers and difficult counterexamples.
9. Version the ontology and plan backward-compatible migration or explicit reprocessing.
10. Record consequential semantic decisions in `DECISIONS.md`.

## Guardrails

- Do not encode absence of extraction as evidence of absence.
- Do not collapse contradictory claims into one truth value.
- Do not use confidence as a substitute for provenance.
- Avoid classes that merely mirror phrasing from one paper.
- Make n-ary scientific relations explicit when results depend on dataset, split, metric, baseline, conditions, or units.
- Require stable identifiers and documented entity-resolution boundaries.

## Deliverables

Provide definitions, competency-question coverage, constraints, examples, provenance requirements, versioning impact, unresolved ambiguities, and evaluation fixtures. Prefer reviewable schema diffs over broad redesigns.
