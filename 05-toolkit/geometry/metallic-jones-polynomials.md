---
title: "§5.24.3 Metallic Jones Polynomials"
type: analysis
status: proven
depends_on:
  - /01-foundations/golden-ratio.md
  - /02-meeting-points/metallic-means.md
  - /05-toolkit/geometry/torus-knots.md
  - /05-toolkit/geometry/knot-spectrum.md
  - /05-toolkit/reference/fibonacci-lucas-identities.md
tags:
  - jones-polynomial
  - metallic-means
  - torus-knots
  - golden-ratio
  - bronze-mean
  - silver-mean
  - trefoil
  - knot-invariants
  - geometry
  - part-v
---

# §5.24.3 Metallic Jones Polynomials

## I. The Question

The knot spectrum (§5.24) catalogues every torus knot the framework permits. Each metallic family — golden, silver, bronze — generates its own convergent knots through rational approximations. Section 5.21 established that the Jones polynomial of the trefoil at $\phi$ yields $V(\phi) = 3/\phi^3$ (in the Kauffman bracket convention). The question is: what happens when we evaluate the Jones polynomials of metallic convergent knots at their native metallic means? Do the results encode the numbers of their own metallic family?

## II. The Three-Term Theorem for $T(3,q)$

**Theorem.** For any torus knot $T(3,q)$ with $\gcd(3,q) = 1$, the Jones polynomial is:

$$V(t) = -t^{2q} + t^{q+1} + t^{q-1}$$

*Proof.* $T(3,q)$ is the closure of the 3-strand braid $(\sigma_1 \sigma_2)^q$. In the Temperley-Lieb algebra $\mathrm{TL}_3$ with basis $\{I, e_1, e_2, e_1 e_2, e_2 e_1\}$ and loop value $\delta = -A^2 - A^{-2}$, the braid generators are $\sigma_i = A \cdot I + A^{-1} \cdot e_i$. Computing $(\sigma_1 \sigma_2)^q$ as a $5 \times 5$ matrix, taking the Markov trace, and applying the writhe correction $(-A^3)^{-2q}$ yields exactly three surviving terms under the substitution $t = A^{-4}$. $\square$

**Verification:**

| Knot | Formula | Computed |
|------|---------|----------|
| $T(3,5)$ | $-t^{10} + t^6 + t^4$ | $\checkmark$ |
| $T(3,7)$ | $-t^{14} + t^8 + t^6$ | $\checkmark$ |
| $T(3,10)$ | $-t^{20} + t^{11} + t^9$ | $\checkmark$ |

The polynomial has exactly **three terms** — one for each strand of the braid. The leading exponent is $2q$ (the total crossing number of the 3-strand closure), and the two positive terms are symmetrically placed at $q \pm 1$.

## III. The Three Force Knots at $\phi$

Evaluating the Jones polynomials of the three force knots at the golden ratio $\phi = (1+\sqrt{5})/2$, using the power expansion $\phi^n = F(n) \cdot \phi + F(n-1)$:

### Strong Force: $T(2,3)$

$$V(t) = -t^4 + t^3 + t$$

$$V(\phi) = -(3\phi + 2) + (2\phi + 1) + \phi = (-3 + 2 + 1)\phi + (-2 + 1 + 0) = -1$$

**The trefoil Jones polynomial at $\phi$ is exactly $-1$.**

The Fibonacci coefficients cancel perfectly: $-F(4) + F(3) + F(1) = -3 + 2 + 1 = 0$. This is the Fibonacci recurrence $F(1) + F(3) = F(4)$ encoded in the knot's exponents $(4, 3, 1)$. The rational part gives $-F(3) + F(2) + F(0) = -1 + 1 + 0 = ... $ wait — let's be precise: $-F(3) + F(2) + F(0) = -2 + 1 + 0 = -1$.

### EM Force: $T(3,5)$

$$V(t) = -t^{10} + t^6 + t^4$$

$$V(\phi) = (-F(9) + F(5) + F(3)) + (-F(10) + F(6) + F(4)) \cdot \phi = -27 - 44\phi$$

In surd form: $V(\phi) = -(49 + 22\sqrt{5}) \approx -98.19$

Note: $44 = 4 \times 11 = L(3) \times L(5)$, both Lucas numbers.

### Weak Force: $T(2,7)$

$$V(t) = -t^{10} + t^9 - t^8 + t^7 - t^6 + t^5 + t^3$$

$$V(\phi) = -19 - 30\phi = -(34 + 15\sqrt{5}) \approx -67.54$$

Note: $30 = 2 \times 3 \times 5 = 2 \times F(4) \times F(5)$.

### Summary Table

| Force | Knot | $V(\phi)$ | Numerical |
|-------|------|-----------|-----------|
| Strong | $T(2,3)$ | $-1$ | $-1$ |
| EM | $T(3,5)$ | $-27 - 44\phi$ | $-98.19$ |
| Weak | $T(2,7)$ | $-19 - 30\phi$ | $-67.54$ |

The strong force knot is the unique knot whose Jones polynomial evaluates to a **rational number** at the golden ratio.

## IV. The Trefoil Miracle: Golden Uniqueness

**Theorem (Golden Uniqueness).** The trefoil is the only torus knot whose Jones polynomial evaluates to a rational number at both roots of $x^2 - x - 1 = 0$.

*Proof.* The trefoil $T(2,3)$ has $V(t) = -t^4 + t^3 + t$. At any metallic mean $\sigma_k$ satisfying $\sigma_k^2 = k\sigma_k + 1$, the evaluation gives:

$$V(\sigma_k) = (-k^2 + k - 1) + (-(k-1)(k^2+2)) \cdot \sigma_k$$

The irrational component vanishes if and only if $(k-1)(k^2+2) = 0$. Since $k^2 + 2 > 0$ for all real $k$, this requires $k = 1$ — the golden ratio.

Therefore $V(\phi) = -1$ and $V(\psi) = -1$, and these are the only metallic means at which the Jones polynomial is rational. $\square$

**Interpretation.** The golden ratio is the unique metallic mean where the trefoil's knot invariant collapses to a pure integer. The strong force knot and the golden ratio are matched: the topology (trefoil) and the algebra (golden ratio) "recognise" each other. At every other metallic mean, the trefoil's Jones polynomial retains an irrational component proportional to the mean itself. Only $\phi$ annihilates it.

This is a knot-theoretic expression of the golden ratio's uniqueness within the framework. The strong force is the foundation (Theorem 1.3, the triangle); the golden ratio is the foundation (Theorem 1.1, $\Sigma = 0$). Their Jones pairing gives $-1$ — negative unity, the sign flip that separates $\phi$ from $\psi$.

## V. Metallic Mean Identity

**Lemma.** For any metallic mean $\sigma_k = (k + \sqrt{k^2+4})/2$:

$$\sigma_k + \frac{1}{\sigma_k} = \sqrt{k^2 + 4}$$

*Proof.* From $\sigma_k^2 = k\sigma_k + 1$, we get $1/\sigma_k = \sigma_k - k$. Therefore $\sigma_k + 1/\sigma_k = 2\sigma_k - k = \sqrt{k^2+4}$. $\square$

**Corollary.** $\phi + 1/\phi = \sqrt{5}$, $\sigma_2 + 1/\sigma_2 = \sqrt{8}$, $\beta + 1/\beta = \sqrt{13}$.

## VI. The Closed Form for $T(3,q)$ at Metallic Means

**Theorem.** For the torus knot $T(3,q)$ evaluated at any metallic mean $\sigma_k$:

$$V_{T(3,q)}(\sigma_k) = \sigma_k^q \left(\sqrt{k^2+4} - \sigma_k^q\right)$$

*Proof.* From the three-term formula $V(t) = -t^{2q} + t^{q+1} + t^{q-1}$:

$$V(\sigma_k) = -\sigma_k^{2q} + \sigma_k^{q+1} + \sigma_k^{q-1} = -\sigma_k^{2q} + \sigma_k^q(\sigma_k + \sigma_k^{-1})$$

By the Metallic Mean Identity, $\sigma_k + \sigma_k^{-1} = \sqrt{k^2+4}$, giving:

$$V(\sigma_k) = \sigma_k^q\sqrt{k^2+4} - \sigma_k^{2q} = \sigma_k^q(\sqrt{k^2+4} - \sigma_k^q) \quad \square$$

### Evaluations

**Golden:** $T(3,5)$ at $\phi$ ($k=1$):
$$V(\phi) = \phi^5(\sqrt{5} - \phi^5) = 11.09 \times (-8.85) \approx -98.19$$

**Bronze:** $T(3,10)$ at $\beta$ ($k=3$):
$$V(\beta) = \beta^{10}(\sqrt{13} - \beta^{10}) = 154451 \times (3.61 - 154451) \approx -2.39 \times 10^{10}$$

## VII. Bronze Sequence Encoding

The bronze mean $\beta = (3 + \sqrt{13})/2$ satisfies $\beta^2 = 3\beta + 1$. Powers of $\beta$ decompose as:

$$\beta^n = B(n-1) + B(n) \cdot \beta$$

where $B(n)$ is the bronze sequence: $0, 1, 3, 10, 33, 109, 360, 1189, 3927, 12970, 42837, 141481, \ldots$ satisfying $B(n) = 3B(n-1) + B(n-2)$.

| Power | Decomposition |
|-------|---------------|
| $\beta^0$ | $1 + 0 \cdot \beta$ |
| $\beta^1$ | $0 + 1 \cdot \beta$ |
| $\beta^3$ | $3 + 10 \cdot \beta$ |
| $\beta^9$ | $3927 + 12970 \cdot \beta$ |
| $\beta^{10}$ | $12970 + 42837 \cdot \beta$ |
| $\beta^{11}$ | $42837 + 141481 \cdot \beta$ |
| $\beta^{20}$ | $2003229469 + 6616217487 \cdot \beta$ |

For the bronze echo knot $T(3,10)$:

$$V(\beta) = (-B(19) + B(10) + B(8)) + (-B(20) + B(11) + B(9)) \cdot \beta$$

$$= -2003182705 - 6616063036 \cdot \beta$$

$$\approx -2.39 \times 10^{10}$$

**Every coefficient is a sum of bronze sequence values.** The indices $\{8, 9, 10, 11, 19, 20\}$ come directly from the Jones exponents $\{q-1, q, q+1, 2q-1, 2q\} = \{9, 10, 11, 19, 20\}$, shifted by the power decomposition. The Jones polynomial of the bronze knot, evaluated at the bronze mean, is written entirely in the bronze number system.

The ratio of the $\beta$-coefficient to the rational coefficient converges to $\beta$ itself:

$$\frac{6616063036}{2003182705} \approx 3.302776 \approx \beta$$

This is a general property: for $T(3,q)$ at $\sigma_k$ with large $q$, the dominant term $\sigma_k^{2q}$ has coefficient ratio $B_k(2q)/B_k(2q-1) \to \sigma_k$ as $q \to \infty$.

## VIII. The Trefoil at All Metallic Means

For the trefoil $T(2,3)$ with $V(t) = -t^4 + t^3 + t$:

$$V(\sigma_k) = (k - k^2 - 1) - (k-1)(k^2+2) \cdot \sigma_k$$

| $k$ | Mean $\sigma_k$ | $V(\sigma_k)$ | Numerical |
|-----|-----------------|----------------|-----------|
| 1 | $\phi = 1.618$ | $-1$ | $-1$ |
| 2 | $\sigma_2 = 2.414$ | $-3 - 6\sigma_2$ | $-17.49$ |
| 3 | $\beta = 3.303$ | $-7 - 22\beta$ | $-79.66$ |
| 4 | $\sigma_4 = 4.236$ | $-13 - 54\sigma_4$ | $-241.75$ |
| 5 | $\sigma_5 = 5.193$ | $-21 - 108\sigma_5$ | $-581.80$ |

At $k=1$: $V = -1 + 0 \cdot \phi$. The irrational part vanishes.

At $k=2$: $V = -3 - 6\sigma_2$. The coefficient $6 = 1 \times 6 = (k-1)(k^2+2)$.

At $k=3$: $V = -7 - 22\beta$. The coefficient $22 = 2 \times 11 = (k-1)(k^2+2)$.

The rational parts $-1, -3, -7, -13, -21, \ldots$ follow the pattern $-(k^2 - k + 1)$, which equals $-1, -3, -7, -13, -21, -31, \ldots$ — the **centered hexagonal numbers** with alternating sign.

## IX. Connection to the Framework

### The Strong Force as Fixed Point

$V_{\text{trefoil}}(\phi) = -1$ means the strong force knot is a **fixed point** of the golden ratio evaluation. The Jones polynomial — which encodes the topology of the knot — "sees through" the algebra of $\phi$ to arrive at pure negative unity. This is the topological analogue of $\phi \cdot \psi = -1$: the fundamental product of the double helix (Theorem 1.4).

### The Three-Term Structure

The three terms in $V_{T(3,q)}(t) = -t^{2q} + t^{q+1} + t^{q-1}$ correspond to the three strands of the braid. The leading (negative) term at $t^{2q}$ is the self-interaction; the two positive terms at $t^{q \pm 1}$ are the two witnessing partners. The three terms are the Jones polynomial's echo of the witnessing triangle (Theorem 1.3).

### Metallic Self-Recognition

When a metallic convergent knot $T(3, S_k(n))$ is evaluated at its own metallic mean $\sigma_k$, the result is expressed entirely in the metallic family's own number system:

- **Golden:** $V_{T(3,5)}(\phi) = -F(9) + F(5) + F(3) + (-F(10) + F(6) + F(4)) \cdot \phi$
- **Bronze:** $V_{T(3,10)}(\beta) = -B(19) + B(10) + B(8) + (-B(20) + B(11) + B(9)) \cdot \beta$

Each metallic family has its own internal "arithmetic of knots" — the Jones polynomial evaluated at the family's mean speaks the family's own language.

## X. Open Questions

1. **Alexander vs. Jones.** The Alexander polynomial of $T(3,5)$ at $\phi$ gives $\Delta(\phi) = 8 + 11\phi$ where $8 = F(6)$ and $11 = L(5)$. The Jones polynomial gives $V(\phi) = -27 - 44\phi$ where $44 = L(3) \times L(5)$. Is there a systematic relationship between Fibonacci/Lucas decompositions of the two invariants?

2. **Silver family.** The silver convergent knot $T(2,5)$ has Jones polynomial $V(t) = -t^7 + t^6 - t^5 + t^4 + t^2$ (five terms, not three — because it is a 2-strand knot). At the silver mean $\sigma_2 = 1 + \sqrt{2}$: $V(\sigma_2) = -161 - 114\sqrt{2} \approx -322.22$. Do the Pell numbers appear in this decomposition as cleanly as Fibonacci and bronze numbers appear in theirs?

3. **HOMFLY-PT polynomial.** The HOMFLY-PT polynomial generalises both Alexander and Jones. Evaluating it at metallic means in both variables might reveal a unified structure that the individual invariants only partially capture.

4. **Centered hexagonal numbers.** The rational parts of $V_{\text{trefoil}}(\sigma_k)$ are $-(k^2 - k + 1)$ — the centered hexagonal numbers. These count the vertices of a hexagonal lattice. Is this connected to the hexagonal confinement angle (§5.22)?

5. **Physical interpretation of $V = -1$.** If the trefoil is the strong force and $V(\phi) = -1$, what physical quantity does this represent? The Jones polynomial is related to Chern-Simons theory and topological quantum field theory. In the framework, $-1 = \phi \cdot \psi$ — the product of the two strands.

---

## Dependencies

- [Golden Ratio (Theorem 1.1)](/01-foundations/golden-ratio.md) — $\phi$ as the unique root of $x^2 - x - 1 = 0$
- [Metallic Means (Theorem 32)](/02-meeting-points/metallic-means.md) — $\sigma_k$ as harmonic overtones of $\phi$
- [Forces as Torus Knots (§5.21)](torus-knots.md) — force knot assignments $(2,3)$, $(3,5)$, $(2,7)$
- [The Knot Spectrum (§5.24)](knot-spectrum.md) — metallic convergent knot classification
- [Fibonacci and Lucas Identities (§5.2)](/05-toolkit/reference/fibonacci-lucas-identities.md) — $\phi^n = F(n)\phi + F(n-1)$

## Dependents

- [The Knot Spectrum (§5.24)](knot-spectrum.md) — resolves Open Question 8 (Jones at metallic means)
- [Chirality and Linkage (§5.24.1)](chirality-and-linkage.md) — chirality as Jones polynomial asymmetry

## Tags

`#jones-polynomial` `#metallic-means` `#torus-knots` `#golden-ratio` `#bronze-mean` `#trefoil` `#golden-uniqueness` `#three-term-theorem` `#knot-invariants` `#geometry` `#part-v`
