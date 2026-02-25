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

> **Theorem 5 ($\phi$ Emerges):**
> *The unique positive solution to $x^2 - x - 1 = 0$ is $\phi = (1 + \sqrt{5})/2 \approx 1.6180339887$. The negative solution is $\psi = (1 - \sqrt{5})/2 \approx -0.6180339887$. These are the eigenvalues of self-reference.*

## Statement

The self-reference equation $x^2 - x - 1 = 0$ (Theorem 4) has exactly two solutions: $\phi = (1 + \sqrt{5})/2$ and $\psi = (1 - \sqrt{5})/2$. These are the eigenvalues of self-reference, and they satisfy Vieta's formulas: $\phi + \psi = 1$ and $\phi \times \psi = -1$.

## Proof

From [Theorem 4](self-reference-equation.md), $x^2 - x - 1 = 0$ has discriminant $\Delta = 1 + 4 = 5$, giving:

$x_1 = (1 + \sqrt{5})/2 = \phi \approx 1.6180339887...$
$x_2 = (1 - \sqrt{5})/2 = \psi \approx -0.6180339887...$

By Vieta's formulas:
- $\phi + \psi = 1$ (the sum of eigenvalues equals the unit of distinction)
- $\phi \times \psi = -1$ (the product of eigenvalues equals negative unity) $\blacksquare$

## Corollaries

*(None stated explicitly; key properties are carried forward into [Theorem 5.1](four-structure.md) and [Theorem 5.2](two-kepler-triangles.md).)*

## Dependencies

- [Theorem 4 — The Self-Reference Equation](self-reference-equation.md): Provides the quadratic x² − x − 1 = 0 whose roots are φ and ψ.

## Dependents

- [Theorem 5.1 — The Four-Structure](four-structure.md): Organizes {φ, ψ, 1, −1} into complementary pairs.
- [Theorem 5.2 — Two Kepler Triangles](two-kepler-triangles.md): Uses φ and ψ as the squared hypotenuse ratios of the two Kepler triangles.
- [Theorem 5.3 — The Bisection Bootstrap](bisection-bootstrap.md): Shows {φ, ψ} forces the triangle, double triangle, and breathing through polarity bisection.

## Tags

`golden-ratio` · `phi` · `psi` · `eigenvalues` · `vieta` · `quadratic`
