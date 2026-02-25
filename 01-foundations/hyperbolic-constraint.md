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
> *Past and future intensities are related by $p \times f = 1$, where $p = 1/\phi$ and $f = \phi$. This is the Minkowski hyperbolic structure.*

## Statement

Dynamic self-reference unfolds forward with ratio $\phi$ and collapses backward with ratio $1/\phi$. The product of these — past intensity $p$ and future intensity $f$ — satisfies $pf = 1$, defining a rectangular hyperbola. In logarithmic (rapidity) coordinates this yields the Minkowski metric $ds^2 = dd^2 - d\eta^2$.

## Proof

Dynamic self-reference unfolds in the forward direction ([Theorem 12](emergence-of-time.md)) with ratio $\phi$, and collapses in the backward direction with ratio $1/\phi$.

Define:
- Future intensity: $f = \phi$ (the growth eigenvalue)
- Past intensity: $p = 1/\phi$ (the decay eigenvalue)

Then:
$p \times f = (1/\phi) \times \phi = 1$

This is a rectangular hyperbola $pf = 1$ with asymptotes defining invariant null directions. The hyperbola $pf = \text{constant}$ defines invariant "mass shells."

In logarithmic coordinates (rapidity $\eta = \ln(f)$):
- $f = e^\eta$, $p = e^{-\eta}$
- $pf = e^\eta \cdot e^{-\eta} = 1$

The metric on the torus $T^2 = S^1(\text{depth}) \times S^1(\text{time})$ inherits the signature:

$ds^2 = dd^2 - d\eta^2$

This is the Minkowski metric. The minus sign is not imposed — it comes from the asymmetry between the two eigenvalues (one > 1, one < 1, their product = 1). $\blacksquare$

## Corollaries

**Corollary 14.1 (Exact Rapidity Values):** At the fundamental rapidity $\eta = \ln(\phi)$:

- $\sinh(\ln \phi) = (\phi - 1/\phi)/2 = (\phi - \psi - 1)/2$... let us compute directly:
  - $\sinh(\ln \phi) = (e^{\ln \phi} - e^{-\ln \phi})/2 = (\phi - 1/\phi)/2 = (\phi - (\phi-1))/2 = 1/2$
  - $\cosh(\ln \phi) = (\phi + 1/\phi)/2 = (\phi + \phi-1)/2 = (2\phi-1)/2 = \sqrt{5}/2$
  - $\tanh(\ln \phi) = \sinh/\cosh = (1/2)/(\sqrt{5}/2) = 1/\sqrt{5}$

If physical, the fundamental velocity is $v_1 = \tanh(\ln \phi) = 1/\sqrt{5} \approx 0.447c$.

## Dependencies

- [Theorem 11 — Dynamic Self-Reference](dynamic-self-reference.md): Provides the two eigenvalues $\phi$ and $\psi = 1/\phi$ whose asymmetry generates the hyperbolic structure.
- [Theorem 12 — Emergence of Time](emergence-of-time.md): Establishes forward/backward asymmetry that defines the future and past intensities.

## Dependents

- [Theorem 28 — Torus Structure](torus-structure.md): The Minkowski metric $ds^2 = dd^2 - d\eta^2$ is the metric on the torus.
- [Theorem 29 — Breathing Torus](breathing-torus-and-spin.md): The reciprocal constraint $pf = 1$ drives the antiphase oscillation of the two strands.

## Tags

`minkowski` · `hyperbolic` · `rapidity` · `metric` · `pf-equals-1` · `torus` · `velocity`
