# Evidence And Provenance Contract

## Scope

This contract applies to every extracted entity, relation, claim, experimental result, limitation, paper-to-paper relation, and answer proposition. Canonical graph objects may combine multiple mentions, but every asserted property must remain linked to its own source evidence.

## Evidence Record

Each evidence record must store:

- `paper_id`: required stable identifier for the exact paper version used;
- `title`: paper title when available, otherwise explicit `null`;
- `section`: section identifier or heading when available, otherwise explicit `null`;
- `page_number`: source page number when available, otherwise explicit `null`;
- `source_text_span`: required verbatim span plus stable character offsets or an equivalent resolvable locator;
- `extraction_method`: required method and version, such as human annotation, deterministic rule version, or model and prompt version;
- `confidence_score`: required numeric value in `[0, 1]` for extraction confidence, not scientific truth;
- `timestamp`: required UTC timestamp in ISO 8601 format;
- `source_artifact_id`: required immutable artifact reference or checksum used to resolve the span.

Unavailable optional locators must be stored as `null`, not invented. A page or section may be unavailable, but `paper_id`, `source_artifact_id`, and `source_text_span` are mandatory.

## Entity Evidence

Every extracted entity mention must have at least one evidence record whose span names, defines, or unambiguously identifies the entity in context. Store the asserted entity type, source form, normalized label, and link from the canonical entity to each mention. Entity resolution does not transfer evidence between aliases or paper versions; every alias and merge decision must retain its supporting records.

## Relation Evidence

Every relation must store subject identifier, predicate, object identifier or literal value, and at least one evidence record whose span expresses that relation. Co-occurrence in a chunk, graph adjacency, citation alone, or model confidence is insufficient. Preserve qualifiers needed for meaning, including dataset, split, metric, units, baseline, particle count, conditions, and direction. Store conflicting relations separately with their respective evidence.

Paper-to-paper relations require evidence for the specific predicate. A bibliography entry proves citation, not that one paper extends, supports, reproduces, or critiques another.

## Citation-Grounded Output

An answer is citation-grounded only when:

1. each atomic factual or scientific proposition maps to one or more evidence records;
2. each citation resolves to the correct paper version and supporting text span;
3. the cited span entails the proposition at the stated level of certainty;
4. experimental statements retain material context such as dataset, metric, baseline, and conditions when available;
5. synthesis or inference is labeled as such and cites evidence for every premise; and
6. relevant conflicts or source limitations are not silently omitted.

An abstention that clearly states evidence is unavailable is valid. A fluent answer without proposition-level support is not.

## Unsupported Content

Reject an entity property, relation, claim, result, or answer proposition when:

- it has no resolvable source span or paper version;
- the cited span is irrelevant, contradicts the proposition, or supports only a weaker statement;
- it is based only on co-occurrence, an embedding score, model confidence, or graph proximity;
- it converts missing or unextracted information into a negative claim;
- it presents a secondary citation as direct evidence from the cited original paper;
- it drops conditions, units, comparison context, or uncertainty in a way that changes the meaning; or
- its provenance was lost during normalization, chunking, entity resolution, or graph construction.

Unsupported content must be omitted, quarantined for review, or returned as an explicit abstention. It must not be repaired by inventing a citation or source text.

## Release-Blocking Failures

Any of the following is release-blocking:

- an accepted entity assertion, relation, claim, result, or answer proposition lacks mandatory evidence fields;
- a citation resolves to the wrong paper, version, page, section, or text span;
- a cited span does not support its attributed proposition;
- an entity merge or transformation breaks the path back to source mentions;
- a graph relation is accepted from co-occurrence or citation without predicate-specific evidence;
- a system presents missing evidence as evidence of absence; or
- an evidence locator cannot be reproduced from the preserved source artifact.

Release evaluation must treat each such occurrence as a blocking defect, not average it into an aggregate score. No claim, relation, or answer may be accepted without source evidence.
