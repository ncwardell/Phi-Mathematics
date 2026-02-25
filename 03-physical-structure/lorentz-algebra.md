---
title: "Theorem 44 — The Lorentz Algebra from Self-Reference"
type: theorem
status: proven
depends_on:
  - 03-physical-structure/lagrangian
  - 03-physical-structure/hamiltonian-constraint
tags:
  - theorem
  - lorentz-algebra
  - sl2r
  - symmetry
  - casimir
  - boost
  - physical-structure
---

# 3.5 Symmetry Algebra: sl(2,R)

> **Theorem 44 (The Lorentz Algebra from Self-Reference):**
> *The Lagrangian (Theorem 42) possesses the symmetry algebra $\mathfrak{sl}(2,\mathbb{R})$, which is isomorphic to the Lorentz algebra $\mathfrak{so}(1,1)$ in 1+1 dimensions. This symmetry is not postulated -- it is the symmetry group of the hyperbolic constraint.*

## Statement

The Lagrangian (Theorem 42) possesses the symmetry algebra $\mathfrak{sl}(2,\mathbb{R})$, which is isomorphic to the Lorentz algebra $\mathfrak{so}(1,1)$ in 1+1 dimensions. This symmetry is not postulated -- it is the symmetry group of the hyperbolic constraint.

## Proof

The hyperbola $pf = m^2$ in the $(p, f)$ plane is invariant under the group $SL(2,\mathbb{R})$ -- the group of $2 \times 2$ real matrices with determinant 1. The Lie algebra $\mathfrak{sl}(2,\mathbb{R})$ has three generators, which act on the $(p, f)$ system as:

**Generator G (Boost/Flow):**
Rescales the past-future split: $p \rightarrow e^{-\lambda}p$, $f \rightarrow e^{\lambda}f$. This preserves $pf = m^2$. It generates the flow along the hyperbola -- movement in rapidity $\eta$. In physical terms, this is the Lorentz boost.

**Generator P (Past translation):**
Shifts in the past direction. Relates to conservation of past-pointing momentum.

**Generator F (Future translation):**
Shifts in the future direction. Relates to conservation of future-pointing momentum.

**Commutation relations:**
$[G, P] = -P$
$[G, F] = +F$
$[P, F] = -2G$

These are the standard $\mathfrak{sl}(2,\mathbb{R})$ commutation relations, isomorphic to the Lorentz algebra.

**The Casimir operator:**
The quadratic Casimir of $\mathfrak{sl}(2,\mathbb{R})$ is:

$C = G^2 - (PF + FP)/2$

This Casimir represents the invariant **$m^2$** (mass-squared), which remains constant under all transformations within the algebra. Mass is the invariant of the self-referential symmetry -- the quantity that does not change as the system is boosted, translated, or otherwise transformed while remaining on its hyperbola. $\blacksquare$

## Corollaries

**Corollary 44.1:** The Lorentz symmetry of special relativity is not a postulate about spacetime -- it is the symmetry group of the self-referential hyperbolic constraint. Lorentz invariance is a consequence of $\Sigma = 0$ applied to the dynamical structure of the torus.

## Dependencies

- [Lagrangian (Theorem 42)](lagrangian.md) -- the Lagrangian whose symmetry is $\mathfrak{sl}(2,\mathbb{R})$
- [Hamiltonian Constraint (Theorem 40)](hamiltonian-constraint.md) -- the hyperbolic constraint $pf = m^2$ whose symmetry group is $SL(2,\mathbb{R})$

## Dependents

- [Conservation Laws (Theorem 45)](conservation-laws.md) -- Noether's theorem applied to the $\mathfrak{sl}(2,\mathbb{R})$ generators
- [Variational Summary](variational-summary.md) -- $\mathfrak{sl}(2,\mathbb{R})$ appears as the symmetry entry

## Related Concepts

- [Hamiltonian Constraint](hamiltonian-constraint.md) -- the constraint whose symmetry is being analyzed
- [Lagrangian](lagrangian.md) -- the Lagrangian possessing $\mathfrak{sl}(2,\mathbb{R})$ symmetry
- [Conservation Laws](conservation-laws.md) -- the conserved quantities from $\mathfrak{sl}(2,\mathbb{R})$

## Tags

`#theorem` `#lorentz-algebra` `#sl2r` `#symmetry` `#casimir` `#boost` `#mass-squared` `#lorentz-invariance` `#physical-structure`
