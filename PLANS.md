# Execution Plans

Use an execution plan for work that spans multiple components, changes a data contract, introduces a dependency, affects scientific interpretation, or is expected to take more than one focused session. Small, low-risk changes may use a short checklist.

## Required Plan Content

1. **Goal**: State the user-visible or research outcome and explicit non-goals.
2. **Context**: Identify relevant files, existing behavior, constraints, and prior decisions.
3. **Scientific contract**: Define evidence, provenance, uncertainty, and correctness requirements.
4. **Security and privacy**: Identify untrusted inputs, secret handling, licensing, and data-retention risks.
5. **Approach**: Describe interfaces, data flow, migrations, and alternatives considered.
6. **Milestones**: Break work into independently verifiable increments with one active step at a time.
7. **Validation**: Name unit, integration, regression, and evaluation coverage plus acceptance thresholds.
8. **Cost**: Estimate major one-time and recurring costs and define a budget guardrail.
9. **Rollout and recovery**: Explain compatibility, observability, rollback, and reprocessing needs.

## Planning Rules

- Inspect the repository before proposing changes; do not invent nonexistent components.
- Resolve uncertainty with a bounded spike or test before committing to a costly design.
- Prefer reversible decisions and narrow interfaces.
- Include negative and adversarial cases, not only the happy path.
- Keep plan status current. Record discoveries, deviations, and decisions as they occur.
- Stop and revise the plan if evidence invalidates a core assumption or a budget threshold would be exceeded.

## Completion Record

At completion, record what changed, validation performed, measured evaluation results, actual cost when available, remaining limitations, and any follow-up work. Move durable architectural rationale to `DECISIONS.md`; do not use plans as a decision log.
