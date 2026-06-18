---
name: project-planning
description: Plan substantial repository work for the Semantic Research Agent. Use for multi-component features, data-contract or schema changes, scientific workflows, migrations, new dependencies, costly jobs, or work that needs milestones and explicit validation.
---

# Project Planning

## Workflow

1. Read `AGENTS.md`, `PLANS.md`, `ROADMAP.md`, `DECISIONS.md`, `EVALS.md`, and `COST_POLICY.md`.
2. Inspect the repository and current tests. Distinguish observed facts from assumptions.
3. Define the outcome, non-goals, affected users, and the smallest coherent scope.
4. Write the scientific contract: required evidence, provenance granularity, uncertainty behavior, and unacceptable failure modes.
5. Map inputs, outputs, trust boundaries, persistent data, external calls, and compatibility constraints.
6. Compare viable approaches across correctness, simplicity, reversibility, security, operational burden, and cost.
7. Split delivery into independently testable milestones. Put risky assumptions behind early spikes or fixtures.
8. Define acceptance criteria and named tests/evaluations before implementation.
9. Estimate metered costs and set stop conditions under `COST_POLICY.md`.
10. Record consequential choices in `DECISIONS.md` and keep plan status current during execution.

## Planning Standard

- Cite repository evidence with file paths; do not describe imagined architecture as fact.
- Prefer narrow vertical increments over broad layers that cannot be validated independently.
- Include malformed documents, missing metadata, conflicting claims, duplicate identities, prompt injection, partial failure, and reruns.
- Specify rollback, migration, observability, and reprocessing when state changes.
- Avoid scheduling unrelated cleanup. Create separate work for unrelated defects.

## Output

Produce a plan containing goal, context, non-goals, approach, alternatives, milestones, validation, security, cost, rollout/recovery, open questions, and definition of done. Mark unresolved scientific assumptions explicitly.
