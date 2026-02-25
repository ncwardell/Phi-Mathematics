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
> *Past and future intensities are related by p $\times$ f = 1, where p = 1/$\varphi$ and f = $\varphi$. This is the Minkowski hyperbolic structure.*

## Statement

Dynamic self-reference unfolds forward with ratio $\varphi$ and collapses backward with ratio 1/$\varphi$. The product of these — past intensity p and future intensity f — satisfies pf = 1, defining a rectangular hyperbola. In logarithmic (rapidity) coordinates this yields the Minkowski metric ds² = dd² − dη².

## Proof

Dynamic self-reference unfolds in the forward direction ([Theorem 12](emergence-of-time.md)) with ratio $\varphi$, and collapses in the backward direction with ratio 1/$\varphi$.

Define:
- Future intensity: f = $\varphi$ (the growth eigenvalue)
- Past intensity: p = 1/$\varphi$ (the decay eigenvalue)

Then:
p $\times$ f = (1/$\varphi$) $\times$ $\varphi$ = 1

This is a rectangular hyperbola pf = 1 with asymptotes defining invariant null directions. The hyperbola pf = constant defines invariant "mass shells."

In logarithmic coordinates (rapidity $\eta$ = ln(f)):
- f = e^$\eta$, p = e^(−$\eta$)
- pf = e^$\eta$ · e^(−$\eta$) = 1

The metric on the torus $T^2$ = $S^1$(depth) $\times$ $S^1$(time) inherits the signature:

ds² = dd² − dη²

This is the Minkowski metric. The minus sign is not imposed — it comes from the asymmetry between the two eigenvalues (one > 1, one < 1, their product = 1). $\blacksquare$

## Corollaries

**Corollary 14.1 (Exact Rapidity Values):** At the fundamental rapidity $\eta$ = ln($\varphi$):

- sinh(ln $\varphi$) = ($\varphi$ − 1/$\varphi$)/2 = ($\varphi$ − $\psi$ − 1)/2... let us compute directly:
  - sinh(ln $\varphi$) = (e^(ln $\varphi$) − e^(−ln $\varphi$))/2 = ($\varphi$ − 1/$\varphi$)/2 = ($\varphi$ − ($\varphi$−1))/2 = 1/2
  - cosh(ln $\varphi$) = ($\varphi$ + 1/$\varphi$)/2 = ($\varphi$ + $\varphi$−1)/2 = (2$\varphi$−1)/2 = $\sqrt{5}$/2
  - tanh(ln $\varphi$) = sinh/cosh = (1/2)/($\sqrt{5}$/2) = 1/$\sqrt{5}$

If physical, the fundamental velocity is v₁ = tanh(ln $\varphi$) = 1/$\sqrt{5}$ $\approx$ 0.447c.

## Dependencies

- [Theorem 11 — Dynamic Self-Reference](dynamic-self-reference.md): Provides the two eigenvalues $\varphi$ and $\psi$ = 1/$\varphi$ whose asymmetry generates the hyperbolic structure.
- [Theorem 12 — Emergence of Time](emergence-of-time.md): Establishes forward/backward asymmetry that defines the future and past intensities.

## Dependents

- [Theorem 28 — Torus Structure](torus-structure.md): The Minkowski metric ds² = dd² − dη² is the metric on the torus.
- [Theorem 29 — Breathing Torus](breathing-torus-and-spin.md): The reciprocal constraint pf = 1 drives the antiphase oscillation of the two strands.

## Tags

`minkowski` · `hyperbolic` · `rapidity` · `metric` · `pf-equals-1` · `torus` · `velocity`
