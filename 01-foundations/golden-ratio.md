---
title: "The Golden Ratio"
type: theorem
status: proven
depends_on:
  - 01-foundations/self-reference-equation
tags:
  - golden-ratio
  - phi
  - psi
  - eigenvalues
  - vieta
  - quadratic
---

# 1.9 The Golden Ratio

> **Theorem 5 (φ Emerges):**
> *The unique positive solution to x² − x − 1 = 0 is φ = (1 + √5)/2 ≈ 1.6180339887. The negative solution is ψ = (1 − √5)/2 ≈ −0.6180339887. These are the eigenvalues of self-reference.*

## Statement

The self-reference equation x² − x − 1 = 0 (Theorem 4) has exactly two solutions: φ = (1 + √5)/2 and ψ = (1 − √5)/2. These are the eigenvalues of self-reference, and they satisfy Vieta's formulas: φ + ψ = 1 and φ × ψ = −1.

## Proof

From [Theorem 4](self-reference-equation.md), x² − x − 1 = 0 has discriminant Δ = 1 + 4 = 5, giving:

x₁ = (1 + √5)/2 = φ ≈ 1.6180339887...
x₂ = (1 − √5)/2 = ψ ≈ −0.6180339887...

By Vieta's formulas:
- φ + ψ = 1 (the sum of eigenvalues equals the unit of distinction)
- φ × ψ = −1 (the product of eigenvalues equals negative unity) ∎

## Corollaries

*(None stated explicitly; key properties are carried forward into [Theorem 5.1](four-structure.md) and [Theorem 5.2](two-kepler-triangles.md).)*

## Dependencies

- [Theorem 4 — The Self-Reference Equation](self-reference-equation.md): Provides the quadratic x² − x − 1 = 0 whose roots are φ and ψ.

## Dependents

- [Theorem 5.1 — The Four-Structure](four-structure.md): Organizes {φ, ψ, 1, −1} into complementary pairs.
- [Theorem 5.2 — Two Kepler Triangles](two-kepler-triangles.md): Uses φ and ψ as the squared hypotenuse ratios of the two Kepler triangles.

## Tags

`golden-ratio` · `phi` · `psi` · `eigenvalues` · `vieta` · `quadratic`
