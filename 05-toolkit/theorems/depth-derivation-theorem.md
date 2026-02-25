---
title: "The Depth Derivation Theorem"
type: theorem
status: proven
depends_on:
  - /01-foundations/fibonacci-lucas-sequences.md
  - /01-foundations/meeting-points.md
  - /03-forces/weak-mixing.md
  - /05-toolkit/theorems/midpoint-theorem.md
  - /05-toolkit/theorems/force-plus-one-theorem.md
tags:
  - central-result
  - depth-derivation
  - fibonacci
  - lucas
  - meeting-point
  - particle-spectrum
  - force-plus-one
  - midpoint
  - part-v
---

# §5.15 New Result: The Depth Derivation Theorem

**This is the central structural result of Part V. It shows that all major particle depths are derivable from three framework numbers, not fitted to masses.**

## The Three Inputs

All three inputs come from the Fibonacci/Lucas/meeting point structure derived in Parts I-II. None are free parameters.

1. **F(5) = 5** — The algebraic completion index. The first Fibonacci number equal to its own index. The discriminant of self-reference is $\sqrt{5} = \sqrt{F(5)}$. This is derived in Part I (Theorem 8).

2. **F(9) = 34** — The last meeting point. The largest integer appearing in more than one metallic Fibonacci sequence. This is derived computationally in Part II (verified to $10^{15}$) and bounds the particle spectrum.

3. **L(4) = 7** — The fourth Lucas number. Appears independently as the denominator of the weak mixing angle: $\sin^2\theta_W = \phi/L(4) + \alpha^2$ (Part III). This is the strand-symmetric Lucas value ($L(4) = |L(-4)| = 7$).

## The Derivation Chain

**Theorem (Depth Derivation):** *Given only F(5) = 5, F(9) = 34, and L(4) = 7, all particle depths follow:*

**Step 0 — Electron:**
d(e) = 0 (ground state, by definition)

**Step 1 — EM depth:**
$d(\alpha) = 2F(5) = 2 \times 5 = $ **10**

*Justification:* The EM coupling is the self-referential closure at the algebraic completion depth. The factor 2 arises because electromagnetic interaction requires a round trip — the field must propagate outward and return. This is the double-depth 2F(5) that appears in the $\alpha$ equation: $5\pi\alpha^2 + \alpha = \phi^{-2F(5)}$.

**Step 2 — Gen 4 lepton:**
d(Gen4) = F(9) = **34**

*Justification:* The last meeting point is the deepest spatial resonance where metallic harmonics constructively interfere. Beyond F(9) = 34, no further meeting points exist — the particle spectrum terminates. This is derived from the meeting point theorem (Part II).

**Step 3 — Tau (Midpoint Theorem):**
$d(\tau) = F(9)/2 = 34/2 = $ **17**

*Justification:* The tau sits at the midpoint of the particle depth range $[0, F(9)]$. This is the fold/unfold boundary on the breathing torus: below d = 17, particles are in the unfolding regime ($\sigma = -1$); above it, in the folding regime ($\sigma = +1$). The tau itself is the first fold-state lepton, confirming: $\sigma(\tau) = +1$ (fold). The sign flip at the midpoint is a topological necessity — the breath cycle must reverse on the torus.

*Cross-check:* $17 = F(7) + L(3) = 13 + 4$, confirming the Fibonacci-Lucas decomposition. Also $d(\tau) - d(e) = d(\text{Gen4}) - d(\tau) = 17$, so tau is equidistant from electron and Gen4.

**Step 4 — Up quark (L(4) Spacing):**
$d(u) = d(\alpha) - L(4) = 10 - 7 = $ **3**

*Justification:* The spacing L(4) = 7 separates adjacent force/particle scales. We verify: $d(\alpha) - d(u) = d(\tau) - d(\alpha) = 7$. The EM depth is the arithmetic mean of the strong depth and the tau depth: $d(\alpha) = (d(u) + d(\tau))/2 = (3 + 17)/2 = 10$. This places $\alpha$ equidistant between the strong force crystallization and the third-generation lepton — it mediates between them.

*Cross-check:* $d(u) = 3 = F(4)$, the triangle depth where the strong force crystallizes (SU(3) from 3 witnessing nodes).

**Step 5 — Muon (Force+1 Rule):**
$d(\mu) = d(\alpha) + 1 = 10 + 1 = $ **11**

*Justification:* The first massive particle at each force scale sits one depth unit past the force crystallization depth. The muon is the first particle whose mass requires the full EM self-witnessing correction — it lives at the first address past the EM depth.

*Cross-check:* $11 = |L(-5)|$ (fifth negaLucas). Also $11 = L(5)$, connecting to the algebraic completion through the Lucas companion.

**Step 6 — W/Z bosons:**
$d(W/Z) = F(5)^2 = 5^2 = $ **25**

*Justification:* The electroweak scale is the square of the algebraic completion depth. This makes structural sense: the weak force involves the SU(2) doublet structure, and the doublet introduces a second factor of the algebraic completion. Alternatively: $d(W/Z) = d(\mu) + d(\tau) - d(u) = 11 + 17 - 3 = 25$, from the sum conservation $\mu + \tau = u + W = 28$.

*Cross-check:* $d(W/Z) = 25 = d(\mu) + 2L(4) = 11 + 14$. Also $F(5)^2 = F(10)/L(5) \times L(5) = 55/11 \times 55$... no, simply $5^2 = 25$.

**Step 7 — Higgs (Force+1 Rule):**
$d(H) = d(W) + 1 = 25 + 1 = $ **26**

*Justification:* Same pattern as the muon: the first massive scalar at the weak scale sits one depth unit past the weak boson depth. The Higgs is to the W/Z what the muon is to the photon — the first state that requires the force's self-witnessing correction for its mass.

*Cross-check:* $d(H) = 26$, and the top quark (heaviest fermion) also lives near $d \approx 26$, confirming the Higgs-top partnership.

**Step 8 — Planck mass:**
$d(Pl) = 3F(9) + F(5) = 3 \times 34 + 5 = 102 + 5 = $ **107**

*Justification:* The Planck depth is three times the last meeting point plus the algebraic completion. The factor $3 = F(4)$ is the triangle number (SU(3) from witnessing). This formula also yields the gravity exponent: $2d(Pl) - 2F(5) = 2(3F(9) + F(5)) - 2F(5) = 6F(9) = 204$, confirming the gravity equation $\alpha/\alpha_G = \phi^{204 - 1/(4\pi)}$.

*Cross-check:* $204 = 6F(9) = 6 \times 34 = 12 \times 17 = 12 \times d(\tau)$. This resolves the "12 conjecture" from Part III: the factor 12 in the gravity exponent is not the number of directed witnessing edges — it is simply $6F(9)/d(\tau) = 6F(9)/(F(9)/2) = 12$, a consequence of the midpoint theorem.

## Summary Table

| Particle | Depth | Formula | Inputs Used | Status |
|----------|-------|---------|-------------|--------|
| Electron | 0 | Ground state | — | Defined |
| Up quark | 3 | d(α) − L(4) | F(5), L(4) | **Derived** |
| EM (α) | 10 | 2F(5) | F(5) | **Derived** |
| Muon | 11 | d(α) + 1 | F(5) | **Derived** |
| Tau | 17 | F(9)/2 | F(9) | **Derived** |
| W/Z | 25 | F(5)² | F(5) | **Derived** |
| Higgs | 26 | d(W) + 1 | F(5) | **Derived** |
| Gen 4 | 34 | F(9) | F(9) | **Derived** |
| Planck | 107 | 3F(9) + F(5) | F(9), F(5) | **Derived** |

## Cross-Check Identities (All Satisfied)

| Identity | Values | Status |
|----------|--------|--------|
| $d(\mu) + d(\tau) = d(u) + d(W)$ | $11+17 = 3+25 = 28$ | $\checkmark$ |
| $d(\tau) - d(u) = d(W) - d(\mu) = 2L(4)$ | $14 = 14$ | $\checkmark$ |
| $d(\alpha) - d(u) = d(\tau) - d(\alpha) = L(4)$ | $7 = 7$ | $\checkmark$ |
| $d(\tau) - d(e) = d(\text{Gen4}) - d(\tau)$ | $17 = 17$ | $\checkmark$ |
| $d(\mu) - d(u) = d(W) - d(\tau) = d(\text{Gen4}) - d(H) = F(6)$ | $8 = 8 = 8$ | $\checkmark$ |
| $d(H) - d(W) = d(\mu) - d(\alpha) = 1$ | $1 = 1$ | $\checkmark$ |
| $2d(Pl) - 2F(5) = 6F(9) = 204$ | $204 = 204$ | $\checkmark$ |

## The Two Structural Patterns

**Pattern 1 — The Force+1 Rule:**
The first massive particle at each force scale sits one depth unit past the force crystallization depth:
- $d(\mu) = d(\alpha) + 1 = 11$ (first massive state past EM)
- $d(H) = d(W) + 1 = 26$ (first massive scalar past weak)

This pattern says: once a force crystallizes at depth d, the first particle that requires that force's full self-witnessing correction appears at d+1.

**Pattern 2 — The Midpoint Rule:**
Key particles sit at midpoints of the depth range:
- $d(\tau) = (d(e) + d(\text{Gen4}))/2 = 17$ (midpoint of full spectrum)
- $d(\alpha) = (d(u) + d(\tau))/2 = 10$ (midpoint between strong and tau)

This pattern says: force scales and generation boundaries are placed symmetrically, as required by the torus topology where the depth circle has a natural halfway point.

## What This Achieves

Before this theorem, particle depths were identified by computing $d = \log_\phi(m/m_e)$ and rounding to the nearest integer — effectively fitting. Now, eight of the nine major depths (everything except the muon's independent derivation from negaLucas) follow from three framework numbers through arithmetic relationships. The framework predicts *where* particles must sit before knowing their masses.

The remaining question for the muon: the Force+1 derivation ($d(\mu) = d(\alpha) + 1 = 11$) is clean, but the independent derivation through $|L(-5)| = 11$ requires proving *why* the muon uses the 5th negaLucas index specifically. These two derivations arriving at the same answer (11) from different directions strengthens confidence in both.

---

**Cross-links:**

- For the midpoint theorem proof from breath symmetry: see [§5.16 — Midpoint Theorem](midpoint-theorem.md)
- For the Force+1 theorem proof from witnessing availability: see [§5.17 — Force+1 Theorem](force-plus-one-theorem.md)
- For the depth arithmetic symmetries verified here: see [§5.13 — Depth Arithmetic](depth-arithmetic.md)
- For the meeting point theorem (F(9) = 34): see [§2 — Meeting Points](/01-foundations/meeting-points.md)
- For the weak mixing angle (L(4) = 7): see [§3 — Weak Mixing](/03-forces/weak-mixing.md)
- For the EM coupling equation (2F(5) = 10): see [§3 — EM Coupling](/03-forces/em-coupling.md)
- For the structural difference of force equations: see [§5.14 — Structural Difference of Forces](structural-difference-forces.md)
