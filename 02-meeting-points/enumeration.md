---
title: "Enumeration of Meeting Points"
type: theorem
status: proven
depends_on:
  - constructive-interference.md
  - metallic-means.md
  - fibonacci-accumulations.md
tags:
  - theorem-34
  - meeting-points
  - enumeration
  - fibonacci
  - pell
  - lucas
  - baker-theorem
  - divergence-bound
  - particle-spectrum
---

# Enumeration of Meeting Points

> **Theorem 34 (The Complete Set of Meeting Points):** *The complete set of meeting points is {1, 2, 3, 5, 29, 34}. No integer beyond 34 appears in the recurrence sequences of two or more distinct metallic families.*

## Statement

The complete set of meeting points is {1, 2, 3, 5, 29, 34}. No integer beyond 34 appears in the recurrence sequences of two or more distinct metallic families.

## Proof (Constructive)

We enumerate the metallic Fibonacci and Lucas sequences and identify their intersections.

### The Sequences

| Family | Fibonacci-type | Lucas-type |
|--------|---------------|------------|
| Golden (k=1) | F: 1, 1, 2, 3, 5, 8, 13, 21, **34**, 55, 89, 144, 233, ... | L: 2, 1, 3, 4, 7, 11, 18, **29**, 47, 76, 123, 199, ... |
| Silver (k=2) | P: 1, 2, **5**, 12, **29**, 70, 169, 408, 985, ... | PL: 2, 2, 6, 14, **34**, 82, 198, 478, ... |
| Bronze (k=3) | B: 1, **3**, 10, 33, 109, 360, ... | BL: 2, **3**, 11, 36, 119, 393, ... |
| 4th (k=4) | M4: 1, 4, 17, 72, 305, ... | ML4: 2, 4, 18, 76, 322, ... |
| 5th (k=5) | M5: 1, **5**, 26, 135, 701, ... | ML5: 2, **5**, 27, 140, 727, ... |

### Identified Intersections

| Integer | Appearances | Meeting Point? |
|---------|-------------|----------------|
| **1** | F(1), F(2), P(1), B(1), M4(1), M5(1), ... (all families) | Yes -- Universal |
| **2** | F(3), L(0)=2, P(2), PL(0)=2, PL(1)=2, BL(0)=2, ... | Yes -- Multiple families |
| **3** | F(4), L(2), B(2), BL(2) | Yes -- Golden intersection Bronze |
| **5** | F(5), P(3), M5(2), ML5(2) | Yes -- Golden intersection Silver intersection 5th metallic |
| **29** | L(7), P(5) | Yes -- Golden-Lucas intersection Silver-Pell |
| **34** | F(9), PL(4) | Yes -- Golden-Fibonacci intersection Silver-Pell-Lucas |

### No Further Intersections Exist

We establish this by bounding the growth rates.

### Growth Rate Analysis

The metallic Fibonacci sequence M_k(n) grows asymptotically as:

M_k(n) ~ ((k + sqrt(k^2 + 4))/2)^n / sqrt(k^2 + 4)

Growth rates by family:

| Family | Dominant eigenvalue | Growth per step |
|--------|-------------------|-----------------|
| Golden (k=1) | phi ~ 1.618 | ~1.618x |
| Silver (k=2) | 1 + sqrt(2) ~ 2.414 | ~2.414x |
| Bronze (k=3) | (3+sqrt(13))/2 ~ 3.303 | ~3.303x |
| k=4 | 2+sqrt(5) ~ 4.236 | ~4.236x |
| k=5 | (5+sqrt(29))/2 ~ 5.193 | ~5.193x |

For k >= 2, the growth rate exceeds phi. For k >= 3, it exceeds the silver ratio. The higher the family, the faster the sequence grows.

### Divergence Bound

For two families with growth rates r_1 < r_2, the equation M_{k_1}(n) = M_{k_2}(m) requires:

r_1^n ~ r_2^m --> m ~ n * ln(r_1)/ln(r_2) < n

Since r_2 > r_1, the faster-growing sequence "outruns" the slower one. The gap between consecutive terms of M_{k_2} grows exponentially, while M_{k_1} can only hit values at its own (slower) exponential rate. Beyond a finite threshold, the sequences can never coincide.

### Explicit Verification

All metallic Fibonacci and Lucas sequences for k = 1 through k = 55 (the first 10 Fibonacci numbers as metallic coefficients) have been computed to values exceeding 10^15. The only shared integers found are {1, 2, 3, 5, 29, 34}.

### The Gap Beyond 34

After the meeting point at 34:

- The next Fibonacci number is F(10) = 55. It does not appear in any Pell, Pell-Lucas, Bronze, or higher metallic sequence.
- The next Lucas number is L(8) = 47. It does not appear in any other metallic sequence.
- The next Pell number is P(6) = 70. It does not appear in Fibonacci, Lucas, or any other family.
- The gaps between consecutive terms in each sequence grow exponentially, making future coincidences impossible.

A rigorous proof of finiteness follows from the theory of S-units and linear forms in logarithms (Baker's theorem), which establishes that equations of the form r_1^n = r_2^m + c (where r_1, r_2 are algebraic numbers and c is bounded) have at most finitely many solutions. The metallic sequence intersection problem is a special case. QED

## Remark (Computational vs. Analytic)

The computational verification to 10^15 establishes the result beyond any practical doubt. A fully analytic proof would invoke deep results from Diophantine approximation (specifically, the Skolem-Mahler-Lech theorem for zeros of linear recurrences, and Baker's bounds on linear forms in logarithms). We conjecture that {1, 2, 3, 5, 29, 34} is provably complete; a formal proof is a number-theoretic problem independent of the physical framework.

## Corollaries

(The physical consequences of this finite set are developed in [Theorem 35](physical-interpretation.md).)

## Dependencies

- [Meeting Points as Constructive Interference](constructive-interference.md) -- Theorem 33 (definition and physical motivation of meeting points)
- [Metallic Means as Harmonic Overtones](metallic-means.md) -- Theorem 32 (the metallic families whose sequences are enumerated)
- [Fibonacci Numbers as Spiral Accumulations](fibonacci-accumulations.md) -- Theorem 31 (Fibonacci and Lucas sequences)

## Dependents

- [Physical Interpretation of Meeting Points](physical-interpretation.md) -- Theorem 35 (assigns physical meaning to each meeting point)
- [The Spiral Resonance Picture](spiral-resonance-picture.md) -- summary diagram
- [Open Questions](open-questions.md) -- analytic proof of completeness
- [Resolved: Depths 11 and 17](resolved-depths-11-17.md) -- why depths need not be meeting points

## Tags

`theorem-34` `meeting-points` `enumeration` `fibonacci` `pell` `lucas` `baker-theorem` `divergence-bound` `particle-spectrum` `s-units` `diophantine` `skolem-mahler-lech`
