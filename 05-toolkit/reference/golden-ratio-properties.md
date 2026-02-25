---
title: "The Golden Ratio and Its Properties"
type: reference
status: proven
depends_on:
  - 01-foundations/golden-ratio
tags:
  - golden-ratio
  - phi
  - powers
  - fundamental-identity
  - reference
  - toolkit
---

# 5.1 The Golden Ratio and Its Properties

**Fundamental identity:**
$\phi^2 = \phi + 1$ (equivalently: $\phi = 1 + 1/\phi$)

**Powers of $\phi$:**
$\phi^n = F(n) \cdot \phi + F(n-1)$ for all integers n (where F is Fibonacci)
$\phi^n + \psi^n = L(n)$ (Lucas numbers)
$\phi^n - \psi^n = F(n) \cdot \sqrt{5}$

**Reciprocal:**
$1/\phi = \phi - 1 = 0.6180339887...$

**Key powers:**

| n | $\phi^n$ | $\approx$ | F(n) | L(n) |
|---|-----|---|------|------|
| 0 | 1 | 1 | 0 | 2 |
| 1 | $\phi$ | 1.618 | 1 | 1 |
| 2 | $\phi+1$ | 2.618 | 1 | 3 |
| 3 | $2\phi+1$ | 4.236 | 2 | 4 |
| 4 | $3\phi+2$ | 6.854 | 3 | 7 |
| 5 | $5\phi+3$ | 11.09 | 5 | 11 |
| 10 | $55\phi+34$ | 122.99 | 55 | 123 |
| 11 | $89\phi+55$ | 199.01 | 89 | 199 |
| 17 | $1597\phi+987$ | 3571.00 | 1597 | 3571 |
| 25 | — | 167,761 | — | — |
| 26 | — | 271,443 | — | — |
| 34 | — | 12,752,043 | — | — |

## Cross-References

- [The Golden Ratio (Theorem 5)](../../01-foundations/golden-ratio.md) -- foundational derivation of $\phi$ from self-reference
- [Fibonacci and Lucas Identities](fibonacci-lucas-identities.md) -- recurrences and Binet formulas for F(n) and L(n)
- [The Four-Structure](four-structure.md) -- the algebraic structure $\{\phi, \psi, 1, -1\}$
- [The Complete Phase Space Map](../../04-extensions/phase-space-map.md) -- particle depths as powers of $\phi$

## Tags

`#golden-ratio` `#phi` `#powers` `#fundamental-identity` `#reference` `#toolkit`
