---
title: "The Fibonacci Generating Function Theorem"
type: theorem
status: proven
depends_on:
  - /01-foundations/fibonacci-lucas-sequences.md
  - /01-foundations/golden-ratio.md
  - /03-forces/em-coupling.md
tags:
  - fibonacci
  - lucas
  - generating-function
  - phi-powers
  - fine-structure-constant
  - odd-even-duality
  - part-v
---

# §5.12 New Results: The Fibonacci Generating Function Theorem

## Theorem (Generating Function at φ-Powers)

The Fibonacci generating function F_gen(z) = z/(1-z-z²) evaluated at z = φ^(−k) gives:

**For odd k ≥ 3:**
**F_gen(φ^(−k)) = 1/(L(k) − 1)**

**For even k ≥ 2:**
**F_gen(φ^(−k)) = 1/(F(k)√5 − 1)**

**Proof (odd k):**

F_gen(φ^(−k)) = φ^(−k) / (1 − φ^(−k) − φ^(−2k))

Multiply numerator and denominator by φ^(2k):

= φ^k / (φ^(2k) − φ^k − 1) = 1 / (φ^k − 1 − φ^(−k))

For odd k: ψ^k = (−1/φ)^k = −φ^(−k) (since k is odd)

Therefore: φ^k − φ^(−k) = φ^k + ψ^k = L(k)

And: φ^k − 1 − φ^(−k) = L(k) − 1

So: **F_gen(φ^(−k)) = 1/(L(k) − 1)** ∎

**Proof (even k):**

For even k: ψ^k = (−1/φ)^k = +φ^(−k)

Therefore: φ^k − φ^(−k) = φ^k − ψ^k = F(k)√5

And: φ^k − 1 − φ^(−k) = F(k)√5 − 1

So: **F_gen(φ^(−k)) = 1/(F(k)√5 − 1)** ∎

## Values at Framework Depths

| k | Type | F_gen(φ^(−k)) | Physical Significance |
|---|------|---------------|----------------------|
| 3 | Odd | 1/(L(3)−1) = **1/3** | 3 = number of colors (SU(3)) |
| 5 | Odd | 1/(L(5)−1) = **1/10** | 10 = 2F(5) = EM depth |
| 7 | Odd | 1/(L(7)−1) = **1/28** | 28 = μ+τ = u+W (depth sum) |
| 9 | Odd | 1/(L(9)−1) = **1/75** | |
| 10 | Even | 1/(F(10)√5−1) = 1/121.98 ≈ **α** | EM coupling! |
| 11 | Odd | 1/(L(11)−1) = **1/198** | 198 = L(11)−1 |
| 17 | Odd | 1/(L(17)−1) = **1/3570** | L(17)−1 ≈ φ¹⁷ ≈ tau mass ratio |

**The even-k result at k=10 is remarkable:** F_gen(φ^(−10)) = 1/(F(10)√5 − 1) = 1/(55√5 − 1) = 1/121.98 ≈ 0.00820 ≈ **α** (error ~12%). The Fibonacci generating function at the EM depth approximately recovers the fine structure constant.

## The Odd/Even Duality

Odd depths produce **rational** results through Lucas numbers. Even depths produce **irrational** results through Fibonacci×√5. This is the Fibonacci/Lucas duality of the framework — odd depths "close" through the integer structure (Lucas), while even depths retain the √5 discriminant (Fibonacci).

---

**Cross-links:**

- For the EM depth and fine structure constant: see [§3 — EM Coupling](/03-forces/em-coupling.md)
- For Fibonacci and Lucas number identities: see [§1 — Fibonacci/Lucas Sequences](/01-foundations/fibonacci-lucas-sequences.md)
- For the depth derivation using 2F(5) = 10: see [§5.15 — Depth Derivation Theorem](depth-derivation-theorem.md)
- For the depth arithmetic symmetries involving these values: see [§5.13 — Depth Arithmetic](depth-arithmetic.md)
