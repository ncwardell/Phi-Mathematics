---
title: "Theorem 43 — Stationary Action as Conservation"
type: theorem
status: proven
depends_on:
  - 03-physical-structure/lagrangian
  - 01-foundations/axioms-and-postulates
tags:
  - theorem
  - stationary-action
  - variational
  - conservation
  - sigma-zero
  - physical-structure
---

# 3.4 The Principle of Stationary Action as Conservation

> **Theorem 43 (Stationary Action = $\Sigma = 0$):**
> *The principle of stationary action ($\delta S = 0$) is the variational manifestation of the Conservation axiom ($\Sigma = 0$).*

## Statement

The principle of stationary action ($\delta S = 0$) is the variational manifestation of the Conservation axiom ($\Sigma = 0$).

## Proof

The action $S = \int L \, d\eta = -m \int d\tau \sqrt{\dot{t}^2 - \dot{x}^2}$ measures the accumulated deviation from the fundamental constraint $H = 0$.

When the constraint is satisfied ($H = 0$), the system resides on its mass-shell hyperbola, and the action is stationary with respect to variations that maintain the constraint.

The logic is:

| Framework Element | Variational Expression |
|-------------------|----------------------|
| $\Sigma = 0$ (Conservation axiom) | $\delta S = 0$ (stationary action) |
| $H = pf - m^2 = 0$ (hyperbolic constraint) | Euler-Lagrange equations |
| Physical trajectory | Geodesic on the mass-shell hyperbola |

Physical paths are those that *conserve* the self-referential balance. Any path "off" the hyperbola would violate the zero-sum totality -- it would require a net surplus or deficit of past/future intensity, contradicting $\Sigma = 0$.

The principle of stationary action is therefore not an independent postulate -- it is the Conservation axiom expressed in the language of calculus of variations. $\blacksquare$

## Dependencies

- [Lagrangian (Theorem 42)](lagrangian.md) -- provides the action $S$ whose variation is set to zero
- [Axiom (Conservation)](../01-foundations/axioms-and-postulates.md) -- $\Sigma = 0$ is the fundamental constraint of which $\delta S = 0$ is the variational form
- [Hamiltonian Constraint (Theorem 40)](hamiltonian-constraint.md) -- $H = 0$ is the constraint that makes $S$ stationary

## Dependents

- [Variational Summary](variational-summary.md) -- $\delta S = 0$ appears in the variational structure table

## Related Concepts

- [Axioms and Postulates](../01-foundations/axioms-and-postulates.md) -- $\Sigma = 0$ as the root axiom
- [Lagrangian](lagrangian.md) -- the action whose variation vanishes
- [Hamiltonian Constraint](hamiltonian-constraint.md) -- the constraint surface on which $S$ is stationary

## Tags

`#theorem` `#stationary-action` `#variational` `#conservation` `#sigma-zero` `#euler-lagrange` `#physical-structure`
