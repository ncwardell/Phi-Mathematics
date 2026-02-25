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

## Theorem (Generating Function at $\phi$-Powers)

The Fibonacci generating function $F_{\text{gen}}(z) = z/(1-z-z^2)$ evaluated at $z = \phi^{-k}$ gives:

**For odd $k \geq 3$:**
**$F_{\text{gen}}(\phi^{-k}) = 1/(L(k) - 1)$**

**For even $k \geq 2$:**
**$F_{\text{gen}}(\phi^{-k}) = 1/(F(k)\sqrt{5} - 1)$**

**Proof (odd k):**

$F_{\text{gen}}(\phi^{-k}) = \phi^{-k} / (1 - \phi^{-k} - \phi^{-2k})$

Multiply numerator and denominator by $\phi^{2k}$:

$= \phi^k / (\phi^{2k} - \phi^k - 1) = 1 / (\phi^k - 1 - \phi^{-k})$

For odd k: $\psi^k = (-1/\phi)^k = -\phi^{-k}$ (since k is odd)

Therefore: $\phi^k - \phi^{-k} = \phi^k + \psi^k = L(k)$

And: $\phi^k - 1 - \phi^{-k} = L(k) - 1$

So: **$F_{\text{gen}}(\phi^{-k}) = 1/(L(k) - 1)$** $\blacksquare$

**Proof (even k):**

For even k: $\psi^k = (-1/\phi)^k = +\phi^{-k}$

Therefore: $\phi^k - \phi^{-k} = \phi^k - \psi^k = F(k)\sqrt{5}$

And: $\phi^k - 1 - \phi^{-k} = F(k)\sqrt{5} - 1$

So: **$F_{\text{gen}}(\phi^{-k}) = 1/(F(k)\sqrt{5} - 1)$** $\blacksquare$

## Values at Framework Depths

| k | Type | $F_{\text{gen}}(\phi^{-k})$ | Physical Significance |
|---|------|---------------|----------------------|
| 3 | Odd | $1/(L(3)-1) = $ **1/3** | 3 = number of colors (SU(3)) |
| 5 | Odd | $1/(L(5)-1) = $ **1/10** | 10 = 2F(5) = EM depth |
| 7 | Odd | $1/(L(7)-1) = $ **1/28** | 28 = $\mu+\tau = u+W$ (depth sum) |
| 9 | Odd | $1/(L(9)-1) = $ **1/75** | |
| 10 | Even | $1/(F(10)\sqrt{5}-1) = 1/121.98 \approx $ **$\alpha$** | EM coupling! |
| 11 | Odd | $1/(L(11)-1) = $ **1/198** | $198 = L(11)-1$ |
| 17 | Odd | $1/(L(17)-1) = $ **1/3570** | $L(17)-1 \approx \phi^{17} \approx$ tau mass ratio |

**The even-k result at k=10 is remarkable:** $F_{\text{gen}}(\phi^{-10}) = 1/(F(10)\sqrt{5} - 1) = 1/(55\sqrt{5} - 1) = 1/121.98 \approx 0.00820 \approx $ **$\alpha$** (error ~12%). The Fibonacci generating function at the EM depth approximately recovers the fine structure constant.

## The Odd/Even Duality

Odd depths produce **rational** results through Lucas numbers. Even depths produce **irrational** results through Fibonacci$\times\sqrt{5}$. This is the Fibonacci/Lucas duality of the framework — odd depths "close" through the integer structure (Lucas), while even depths retain the $\sqrt{5}$ discriminant (Fibonacci).

---

**Cross-links:**

- For the EM depth and fine structure constant: see [§3 — EM Coupling](/03-forces/em-coupling.md)
- For Fibonacci and Lucas number identities: see [§1 — Fibonacci/Lucas Sequences](/01-foundations/fibonacci-lucas-sequences.md)
- For the depth derivation using 2F(5) = 10: see [§5.15 — Depth Derivation Theorem](depth-derivation-theorem.md)
- For the depth arithmetic symmetries involving these values: see [§5.13 — Depth Arithmetic](depth-arithmetic.md)
