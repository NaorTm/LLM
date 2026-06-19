# Initial Research Domain

## Scope

The first domain is particle filtering for state-space inference, with emphasis on differentiable particle filters (DPFs): particle-filter-based methods whose model, proposal, weighting, resampling, or related components are learned through gradient-based training.

The initial corpus must support comparison of algorithm design, probabilistic correctness, empirical behavior, and evidence. It is not intended to cover every sequential Monte Carlo method or every application that uses a particle filter.

## Why This Domain

Particle filters provide a bounded but technically meaningful test case for the research agent:

- papers contain identifiable algorithms, assumptions, proposals, weights, resampling choices, datasets, metrics, and baselines;
- DPF work connects classical probabilistic inference with learned components and differentiable optimization;
- claims often depend on whether learned proposals receive valid importance correction and whether comparisons control for particle count, model capacity, and evaluation protocol;
- known failure modes such as weight degeneracy, particle impoverishment, and reported mode collapse require precise evidence rather than keyword matching;
- the literature contains extension, comparison, and application relationships suitable for graph queries.

## In Scope For The First MVP

- Classical particle filtering concepts needed to interpret DPF work, including sequential importance sampling/resampling, bootstrap filters, and auxiliary particle filters (APFs).
- Learned proposal distributions, learned dynamics or observation models, learned weighting components, and differentiable or surrogate resampling methods.
- Whether reported weighting includes the importance correction required by the stated proposal and target distribution.
- Algorithmic contributions, application-only uses, and papers combining both.
- Experimental setups: datasets, simulated systems, benchmarks, baselines, metrics, particle counts, ablations, and reported results.
- Explicit claims, assumptions, limitations, and evidence about degeneracy, impoverishment, mode collapse, bias, variance, stability, or training behavior.
- Paper-to-paper relations supported by text or bibliography context, such as extends, compares with, applies, reproduces, or critiques.
- Contradictory findings and missing evidence, represented without forcing a single conclusion.

## Out Of Scope For The First MVP

- Exhaustive coverage of sequential Monte Carlo, particle MCMC, SMC samplers, smoothing, or population Monte Carlo outside direct DPF context.
- General Bayesian filtering, Kalman filtering, or variational inference except when used as background or an explicit baseline.
- Exhaustive modeling of application domains such as robotics, tracking, finance, or navigation.
- Reproducing experiments, executing paper code, or independently validating mathematical proofs.
- Inferring probabilistic correctness from terminology alone; validity must be supported by equations, algorithm text, or explicit derivation in the source.
- Treating a missing mention as proof that a method, correction, limitation, or experiment is absent.
- Corpus-scale ingestion, automated gap claims, or broad field-level conclusions.

## Initial Corpus Boundary

Start with a human-curated seed set of approximately 15 to 25 papers: foundational particle-filter references needed for interpretation, representative DPF methods, direct comparison papers, and a small number of application-focused papers. Record selection criteria and paper versions. Expand only after the competency questions, evidence contract, and gold examples work reliably on this set.
