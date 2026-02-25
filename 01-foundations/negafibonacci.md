---
title: "The NegaFibonacci Extension and Two Strands"
type: theorem
status: proven
depends_on:
  - 01-foundations/dynamic-self-reference
tags:
  - negafibonacci
  - negalucas
  - psi-strand
  - binet-formula
  - sign-alternation
  - negative-index
  - lepton-masses
---

# 1.14 The NegaFibonacci Extension and Two Strands

> **Theorem 13 (NegaFibonacci and NegaLucas — The ψ-Strand):**
> *The Fibonacci and Lucas recurrences extend to negative indices, producing the ψ-strand. The sign alternation in the negative extension corresponds to the complex branch (second Kepler triangle).*

## Statement

The recurrence F(n) = F(n−1) + F(n−2) can be rearranged to compute backward: F(n−2) = F(n) − F(n−1). The resulting sequences for negative n exhibit sign alternation governed by the relations F(−n) = (−1)^(n+1) × F(n) and L(−n) = (−1)^n × L(n). This sign alternation is the algebraic manifestation of the ψ-strand (the second Kepler triangle).

## Proof

The recurrence F(n) = F(n−1) + F(n−2) can be rearranged: F(n−2) = F(n) − F(n−1). This allows backward computation:

| n | F(n) | L(n) |
|---|------|------|
| −7 | 13 | −29 |
| −5 | 5 | −11 |
| −4 | −3 | 7 |
| −3 | 2 | −4 |
| −2 | −1 | 3 |
| −1 | 1 | −1 |
| 0 | 0 | 2 |
| 1 | 1 | 1 |
| 2 | 1 | 3 |
| 3 | 2 | 4 |
| 4 | 3 | 7 |
| 5 | 5 | 11 |

The general relations are:

F(−n) = (−1)^(n+1) × F(n)
L(−n) = (−1)^n × L(n)

The alternating signs in the negative extension are not a convention — they are the algebraic consequence of ψ < 0. The Binet formulas are:

F(n) = (φⁿ − ψⁿ) / √5
L(n) = φⁿ + ψⁿ

For negative indices, ψⁿ with n < 0 produces the sign alternation. This is the ψ-strand manifesting through the recurrence — the second Kepler triangle's contribution oscillates in sign, reflecting the imaginary component i = √(φψ). ∎

## Corollaries

**Corollary 13.1:** Specific negaLucas values that appear in the physical structure:
- |L(−3)| = 4 — the coefficient C for the tau lepton, and the factor in the 4α correction
- L(−4) = 7 — the denominator in the weak mixing angle: sin²θ_W = φ/7 + α²
- |L(−5)| = 11 — the depth d for the muon
- |L(−7)| = 29 — the coefficient C for the 4th generation

## Dependencies

- [Theorem 11 — Dynamic Self-Reference](dynamic-self-reference.md): Provides the Fibonacci and Lucas recurrences that are extended to negative indices.

## Dependents

- [Theorem 29.3 — Dual Dimensions](breathing-torus-and-spin.md): NegaLucas values serve as temporal addresses (breath counts) for particle crystallization.

## Tags

`negafibonacci` · `negalucas` · `psi-strand` · `binet-formula` · `sign-alternation` · `negative-index` · `lepton-masses`
