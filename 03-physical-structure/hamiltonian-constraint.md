---
title: "Theorem 40 — Hamiltonian Constraint from the Hyperbolic Structure"
type: theorem
status: proven
depends_on:
  - 01-foundations/axioms-and-postulates
  - 02-meeting-points/hyperbolic-structure
tags:
  - theorem
  - hamiltonian
  - constraint
  - hyperbolic
  - mass-shell
  - dynamics
  - physical-structure
---

# 3.1 The Hamiltonian Constraint

> **Theorem 40 (Hamiltonian Constraint from the Hyperbolic Structure):**
> *The dynamical constraint governing any self-referential structure on the torus is $H = pf - m^2 = 0$, where $p$ is the past (contracting) intensity, $f$ is the future (expanding) intensity, and $m$ is the rest mass. This constraint defines existence as residence on a specific hyperbola.*

## Statement

The dynamical constraint governing any self-referential structure on the torus is $H = pf - m^2 = 0$, where $p$ is the past (contracting) intensity, $f$ is the future (expanding) intensity, and $m$ is the rest mass. This constraint defines existence as residence on a specific hyperbola.

## Proof

From Theorem 14, the hyperbolic constraint is $p \times f = 1$ for the ground state (electron, $m = 1$ in natural units). For a general self-referential structure with mass $m$, the constraint generalizes to:

$p \times f = m^2$

This follows because mass scales the depth on the torus (Theorem 29.3). A structure with mass $m$ has accumulated $m^2$ units of winding (the square arising from the product of the two strand contributions -- $\phi$-strand $\times$ $\psi$-strand, consistent with the double helix).

Define the Hamiltonian constraint:

$H = pf - m^2 = 0$

This constraint is formally identical to the Hamiltonian constraint in general relativity, which encodes the reparametrization invariance of worldlines. Here it arises not from diffeomorphism invariance but from the self-referential structure of the torus: the product of past and future intensities must equal the mass shell, which is determined by the depth and coupling (Part II).

**Interpretation:** A physical system must "live" on its specific hyperbola. The constraint $H = 0$ is the variational expression of $\Sigma = 0$ -- the conservation axiom applied to the dynamical evolution. A trajectory satisfying $H = 0$ is one that maintains the internal balance between expanding (future) and contracting (past) components at every moment. $\blacksquare$

## Dependencies

- [Axiom (Conservation)](../01-foundations/axioms-and-postulates.md) -- $\Sigma = 0$ is the conservation axiom whose dynamical expression is $H = 0$
- Theorem 14 (Hyperbolic Structure) -- provides the ground-state constraint $p \times f = 1$
- Theorem 29.3 (Breathing Torus / Depth) -- mass scales the depth, giving $p \times f = m^2$
- [Double Triangle (Theorem 1.4)](../01-foundations/double-triangle.md) -- the double helix whose two strands produce the $m^2$ factor

## Dependents

- [Flow Equations (Theorem 41)](flow-equations.md) -- derives the natural evolution on the hyperbola from $H = 0$
- [Lagrangian (Theorem 42)](lagrangian.md) -- the Lagrangian is constructed from the Hamiltonian constraint
- [Stationary Action (Theorem 43)](stationary-action.md) -- $\delta S = 0$ is the variational form of $H = 0$
- [Lorentz Algebra (Theorem 44)](lorentz-algebra.md) -- $\mathfrak{sl}(2,\mathbb{R})$ is the symmetry group of the hyperbolic constraint
- [Variational Summary](variational-summary.md) -- $H = pf - m^2 = 0$ is the first entry in the variational table

## Related Concepts

- [Axioms and Postulates](../01-foundations/axioms-and-postulates.md) -- $\Sigma = 0$ as the root constraint
- [Flow Equations](flow-equations.md) -- the dynamical evolution that preserves $H = 0$
- [Lagrangian](lagrangian.md) -- Legendre transform of $H$

## Tags

`#theorem` `#hamiltonian` `#constraint` `#hyperbolic` `#mass-shell` `#dynamics` `#sigma-zero` `#physical-structure`
