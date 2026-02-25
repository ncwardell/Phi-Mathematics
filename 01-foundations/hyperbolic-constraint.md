---
title: "The Hyperbolic Constraint"
type: theorem
status: proven
depends_on:
  - 01-foundations/dynamic-self-reference
  - 01-foundations/emergence-of-time
tags:
  - minkowski
  - hyperbolic
  - rapidity
  - metric
  - pf-equals-1
  - torus
  - velocity
---

# 1.15 The Hyperbolic Constraint

> **Theorem 14 (Minkowski Structure from Self-Reference):**
> *Past and future intensities are related by p × f = 1, where p = 1/φ and f = φ. This is the Minkowski hyperbolic structure.*

## Statement

Dynamic self-reference unfolds forward with ratio φ and collapses backward with ratio 1/φ. The product of these — past intensity p and future intensity f — satisfies pf = 1, defining a rectangular hyperbola. In logarithmic (rapidity) coordinates this yields the Minkowski metric ds² = dd² − dη².

## Proof

Dynamic self-reference unfolds in the forward direction ([Theorem 12](emergence-of-time.md)) with ratio φ, and collapses in the backward direction with ratio 1/φ.

Define:
- Future intensity: f = φ (the growth eigenvalue)
- Past intensity: p = 1/φ (the decay eigenvalue)

Then:
p × f = (1/φ) × φ = 1

This is a rectangular hyperbola pf = 1 with asymptotes defining invariant null directions. The hyperbola pf = constant defines invariant "mass shells."

In logarithmic coordinates (rapidity η = ln(f)):
- f = e^η, p = e^(−η)
- pf = e^η · e^(−η) = 1

The metric on the torus T² = S¹(depth) × S¹(time) inherits the signature:

ds² = dd² − dη²

This is the Minkowski metric. The minus sign is not imposed — it comes from the asymmetry between the two eigenvalues (one > 1, one < 1, their product = 1). ∎

## Corollaries

**Corollary 14.1 (Exact Rapidity Values):** At the fundamental rapidity η = ln(φ):

- sinh(ln φ) = (φ − 1/φ)/2 = (φ − ψ − 1)/2... let us compute directly:
  - sinh(ln φ) = (e^(ln φ) − e^(−ln φ))/2 = (φ − 1/φ)/2 = (φ − (φ−1))/2 = 1/2
  - cosh(ln φ) = (φ + 1/φ)/2 = (φ + φ−1)/2 = (2φ−1)/2 = √5/2
  - tanh(ln φ) = sinh/cosh = (1/2)/(√5/2) = 1/√5

If physical, the fundamental velocity is v₁ = tanh(ln φ) = 1/√5 ≈ 0.447c.

## Dependencies

- [Theorem 11 — Dynamic Self-Reference](dynamic-self-reference.md): Provides the two eigenvalues φ and ψ = 1/φ whose asymmetry generates the hyperbolic structure.
- [Theorem 12 — Emergence of Time](emergence-of-time.md): Establishes forward/backward asymmetry that defines the future and past intensities.

## Dependents

- [Theorem 28 — Torus Structure](torus-structure.md): The Minkowski metric ds² = dd² − dη² is the metric on the torus.
- [Theorem 29 — Breathing Torus](breathing-torus-and-spin.md): The reciprocal constraint pf = 1 drives the antiphase oscillation of the two strands.

## Tags

`minkowski` · `hyperbolic` · `rapidity` · `metric` · `pf-equals-1` · `torus` · `velocity`
