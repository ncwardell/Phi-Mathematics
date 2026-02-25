---
title: "Theorem 45 — Conservation Laws from Self-Referential Symmetry"
type: theorem
status: proven
depends_on:
  - 03-physical-structure/lorentz-algebra
  - 03-physical-structure/lagrangian
tags:
  - theorem
  - noether
  - conservation-laws
  - momentum
  - boost
  - mass-shell
  - physical-structure
---

# 3.6 Noether's Theorem and Conservation Laws

> **Theorem 45 (Conservation Laws from Self-Referential Symmetry):**
> *By Noether's theorem, the $\mathfrak{sl}(2,\mathbb{R})$ symmetry of the Lagrangian (Theorem 44) generates conservation laws that correspond to the fundamental conservation laws of physics.*

## Statement

By Noether's theorem, the $\mathfrak{sl}(2,\mathbb{R})$ symmetry of the Lagrangian (Theorem 44) generates conservation laws that correspond to the fundamental conservation laws of physics.

## Proof

Noether's theorem states that each continuous symmetry of the Lagrangian yields a conserved quantity. Applied to the three generators of $\mathfrak{sl}(2,\mathbb{R})$:

| Symmetry Generator | Transformation | Conserved Quantity |
|-------------------|---------------|-------------------|
| G (Boost) | Rapidity translation | Boost charge / center-of-mass motion |
| P (Past translation) | Past-direction shift | Past-pointing momentum |
| F (Future translation) | Future-direction shift | Future-pointing momentum |
| Casimir C | Invariant under all | $m^2$ (mass-squared) |

In standard spacetime coordinates, these map to:

- **G $\rightarrow$ Lorentz boost invariance:** The physics is the same in all inertial frames.
- **P, F $\rightarrow$ Momentum conservation:** The total momentum (past + future components) is conserved.
- **C $\rightarrow$ Mass-shell condition:** $p^2 - E^2 = -m^2$ (the relativistic energy-momentum relation).

All of these emerge from the structure, not from assumptions about spacetime. $\blacksquare$

## Dependencies

- [Lorentz Algebra (Theorem 44)](lorentz-algebra.md) -- provides the $\mathfrak{sl}(2,\mathbb{R})$ symmetry generators
- [Lagrangian (Theorem 42)](lagrangian.md) -- the Lagrangian to which Noether's theorem is applied

## Dependents

- [Variational Summary](variational-summary.md) -- conservation laws complete the variational picture

## Related Concepts

- [Lorentz Algebra](lorentz-algebra.md) -- the symmetry algebra whose generators produce the conservation laws
- [Stationary Action](stationary-action.md) -- the variational principle underlying Noether's theorem
- [Axioms and Postulates](../01-foundations/axioms-and-postulates.md) -- $\Sigma = 0$ as the root conservation principle

## Tags

`#theorem` `#noether` `#conservation-laws` `#momentum` `#boost` `#mass-shell` `#energy-momentum` `#physical-structure`
