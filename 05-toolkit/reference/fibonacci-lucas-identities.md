---
title: "Fibonacci and Lucas Identities"
type: reference
status: proven
depends_on:
  - 05-toolkit/reference/golden-ratio-properties
tags:
  - fibonacci
  - lucas
  - binet
  - cassini
  - negafibonacci
  - reference
  - toolkit
---

# 5.2 Fibonacci and Lucas Identities

**Recurrences:**
$F(n) = F(n-1) + F(n-2)$, $F(0) = 0$, $F(1) = 1$
$L(n) = L(n-1) + L(n-2)$, $L(0) = 2$, $L(1) = 1$

**Binet formulas:**
$F(n) = (\phi^n - \psi^n)/\sqrt{5}$
$L(n) = \phi^n + \psi^n$

**Key relationships:**
- $L(n) = F(n-1) + F(n+1)$
- $F(n)^2 + F(n+1)^2 = F(2n+1)$
- $F(n) \times F(n+2) = F(n+1)^2 + (-1)^{n+1}$ (Cassini identity)
- $F(2n) = F(n) \times L(n)$
- $L(n)^2 - 5F(n)^2 = 4(-1)^n$

**NegaFibonacci/NegaLucas:**
$F(-n) = (-1)^{n+1} \times F(n)$
$L(-n) = (-1)^n \times L(n)$

**Key negative values used in the framework:**

| n | F(−n) | L(−n) | |L(−n)| | Role |
|---|-------|-------|--------|------|
| 3 | 2 | −4 | 4 | Tau C, witnessing correction |
| 4 | −3 | 7 | 7 | Weak mixing denominator |
| 5 | 5 | −11 | 11 | Muon depth |
| 7 | 13 | −29 | 29 | Gen 4 coefficient |

## Cross-References

- [Golden Ratio Properties](golden-ratio-properties.md) -- powers of $\phi$ expressed through Fibonacci and Lucas numbers
- [Meeting Points Reference](meeting-points-reference.md) -- meeting points as Fibonacci/Lucas values
- [Patterns and Observations](../../04-extensions/patterns-and-observations.md) -- Fibonacci progression of boson coefficients
- [Correction Factor Anatomy](correction-factor-anatomy.md) -- L(3) = 4 as the witnessing quantum coefficient

## Tags

`#fibonacci` `#lucas` `#binet` `#cassini` `#negafibonacci` `#reference` `#toolkit`
