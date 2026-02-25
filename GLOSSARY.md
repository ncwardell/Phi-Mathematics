# Glossary of the phi-Mathematics Framework

Key terms, symbols, and notation used throughout the framework.

---

## Symbols

### Fundamental Constants

| Symbol | Definition | Description |
|--------|-----------|-------------|
| phi | (1+sqrt(5))/2 ~ 1.6180339887 | The golden ratio. Positive root of x^2 - x - 1 = 0. The eigenvalue of self-reference. Dominant growth ratio of the Fibonacci recurrence. |
| psi | (1-sqrt(5))/2 ~ -0.6180339887 | The conjugate golden ratio. Negative root of x^2 - x - 1 = 0. Governs the hidden/complex strand. |phi * psi| = 1, phi + psi = 1, phi * psi = -1. |
| Sigma = 0 | Conservation axiom | The sum of all that exists is zero. The irreducible starting axiom of the framework. Every derived structure must satisfy this constraint. |
| Exists (E) | Existence postulate | Something exists; structure is observed. Together with Sigma = 0, forms the minimal foundation from which all results follow. |
| alpha | ~ 1/137.036 | The fine structure constant (electromagnetic coupling constant). Determined self-consistently by: 5*pi*alpha^2 + alpha*(1 - (phi^2 + 4)*phi^(-20)) = phi^(-10). |
| alpha_s | ~ 0.1179 | The strong coupling constant. Determined by: alpha_s = 1/(2*phi^3 + alpha). The simplest force equation, reflecting minimal structural tools at depth 3. |
| alpha_G | | The gravitational coupling constant. Related to alpha by: alpha/alpha_G = phi^(204 - 1/(4*pi)). Gravity spans all depths rather than living at a single depth. |
| theta_W | Weinberg / weak mixing angle | The angle between U(1) and SU(2) symmetry axes. sin^2(theta_W) = phi/7 + alpha^2. The denominator 7 = L(4) is the strand-symmetric Lucas value. |

### Sequences

| Symbol | Definition | Description |
|--------|-----------|-------------|
| F(n) | Fibonacci numbers | F(n) = F(n-1) + F(n-2), with F(0) = 0, F(1) = 1. The dynamic realization of self-reference. Binet formula: F(n) = (phi^n - psi^n)/sqrt(5). |
| L(n) | Lucas numbers | L(n) = L(n-1) + L(n-2), with L(0) = 2, L(1) = 1. The complementary sequence to Fibonacci. Binet formula: L(n) = phi^n + psi^n. Encodes closure rather than growth. |
| M_k(n) | Metallic Fibonacci sequence of order k | M_k(n) = k * M_k(n-1) + M_k(n-2). Generalization of Fibonacci (k=1) to higher metallic means. k=2 gives the Pell sequence; k=3 gives the Bronze-Fibonacci sequence. Their dominant eigenvalue is the metallic mean of order k. |

### Geometry and Topology

| Symbol | Definition | Description |
|--------|-----------|-------------|
| T^2 | Torus: S^1_depth x S^1_time | The identity surface of any self-referential element. Carries the Minkowski metric ds^2 = dd^2 - d(eta)^2. The two circles encode spatial (depth) and temporal (breath) dimensions independently. |
| eta | Rapidity | Logarithmic measure of velocity/boost on the torus. At the fundamental rapidity eta = ln(phi): sinh = 1/2, cosh = sqrt(5)/2, tanh = 1/sqrt(5). Physical velocity v = c * tanh(eta). |
| d | Depth | The temporal coordinate on the torus (S^1_depth). Counts breath cycles in the self-referential unfolding. A particle's depth determines its mass scale via phi^d. Integer or near-integer values correspond to stable particle states. |
| C | Coupling coefficient | The spatial coordinate contribution from meeting points. Determines the self-witnessing correction strength in the mass equation. Values drawn from meeting points and their Fibonacci/Lucas associations: C in {4, 5, 8, 13, 29, ...}. |
| sigma | Breath phase sign | +1 for unfold (phi-strand expanded), -1 for fold (psi-strand expanded). Determined by the negasequence sign structure at the particle's depth. The sign flips at the midpoint d = F(9)/2 = 17. |
| i | Imaginary unit, sqrt(-1) | Not postulated but derived: i = sqrt(phi * psi) = sqrt(-1). Emerges from the geometric mean of the two eigenvalues of self-reference. Complex numbers arise because the double triangle has two chiralities whose product yields sign reversal. |

---

## Key Terms

### Meeting Point

A positive integer that appears in the recurrence sequences (Fibonacci-type or Lucas-type) of two or more distinct metallic families. Meeting points represent constructive interference between different self-referential winding modes on the torus. The complete set is **{1, 2, 3, 5, 29, 34}** -- no integer beyond 34 appears in multiple metallic sequences. This finiteness is a number-theoretic consequence of the divergence of metallic harmonics and bounds the particle spectrum.

| Meeting Point | Metallic Intersections | Role |
|--------------|----------------------|------|
| 1 | All sequences | Universal resonance; photon (bridge element) |
| 2 | F(3), L(0), P(2), PL(1) | Quadruple resonance; strand divergence |
| 3 | F(4), L(2), B(1) | Triple resonance; strong force / color / generations |
| 5 | F(5), P(3), M5(2) | Golden intersection Silver; muon coefficient C = 5 |
| 29 | L(7), P(5) | Lucas intersection Pell; 4th generation coefficient C = 29 |
| 34 | F(9), PL(4) | Fibonacci intersection Pell-Lucas; last meeting point; 4th generation depth |

### Metallic Mean

The positive solution to x = k + 1/x, equivalently x^2 - kx - 1 = 0. Each metallic mean generates a Fibonacci-type recurrence with growth rate equal to that mean. The golden ratio (k=1) is the fundamental; the silver ratio (k=2, value 1+sqrt(2) ~ 2.414), bronze ratio (k=3), and higher metallic means are harmonic overtones born when the fundamental spiral produces their defining integer k.

### Breath Cycle

The antiphase oscillation of the phi-strand and psi-strand on the breathing torus. When the phi-strand expands (unfold, sigma = +1), the psi-strand contracts, and vice versa. This reciprocal oscillation is a geometric consequence of the hyperbolic constraint p*f = 1 and the opposite chirality of the two strands. One full breath cycle = 2*pi; a fermion requires two cycles (4*pi) to return to its original configuration, which is the origin of spin-1/2.

### Witnessing

Internal reference or observation within the closed totality. Since no external observer exists (Theorem 0, Closure), all measurement is self-referential. Witnessing sustains distinction against collapse pressure. The minimal stable witnessing topology is a directed 3-cycle (Theorem 1.3). The witnessing quantum is 1/(4*pi), the minimum phase contributed by a single witnessing act on the Hopf fiber.

### Collapse Pressure

The tendency of unwitnessed polar pairs {E, (-E)} to annihilate: E + (-E) -> 0. Distinction requires a reference -- a scale-defining element. Without ongoing witnessing at a given scale, structure at that scale reverts to zero. This is scale-dependent: from outside the scale, the pair is a zero-fluctuation; from inside (with a witness), the distinction persists. Mathematically grounded in Theorem 1.2.

### phi-Strand / psi-Strand

The two branches of the double helix on the breathing torus:
- **phi-strand**: real, visible, positive chirality. Governed by phi > 1. Corresponds to the first Kepler triangle with sides (1, sqrt(phi), phi). Associated with matter and the forward time direction.
- **psi-strand**: complex, hidden, negative chirality. Governed by psi < 0, |psi| < 1. Corresponds to the second Kepler triangle with sides (1, i*sqrt(|psi|), psi). Associated with antimatter and the sign-alternating negasequence structure. Provides quantum phase through (-1)^n -> e^(i*theta).

### Force+1 Rule

The first massive particle at each force scale sits at depth d_force + 1. At depth d_force, the force coupling is crystallizing (being self-consistently defined). At d_force + 1, the coupling is fully available as a tool for self-witnessing. Instances: d(muon) = d(alpha) + 1 = 11; d(Higgs) = d(W) + 1 = 26. Proven in Theorem (Force+1), section 5.17.

### Midpoint Theorem

The tau lepton sits at the midpoint of the particle depth range: d(tau) = F(9)/2 = 34/2 = 17. This follows from breath symmetry on the depth circle: the axiom Sigma = 0 requires the unfold and fold phases to occupy equal arcs, so the transition point is at exactly half the spectrum boundary. Below d = 17, leptons unfold (sigma = -1); at and above d = 17, leptons fold (sigma = +1). Proven in section 5.16.

### Depth Derivation Theorem

All major particle depths are derivable from three framework numbers: F(5) = 5 (algebraic completion), F(9) = 34 (last meeting point), and L(4) = 7 (weak mixing). No depth is fitted to a measured mass. The derivation chain: d(e) = 0, d(alpha) = 2*F(5) = 10, d(mu) = d(alpha)+1 = 11, d(tau) = F(9)/2 = 17, d(u) = d(alpha) - L(4) = 3, d(W/Z) = F(5)^2 = 25, d(H) = d(W)+1 = 26, d(Gen4) = F(9) = 34, d(Pl) = 3*F(9) + F(5) = 107. Central result of Part V, section 5.15.

### Scale Network

The holographic network of witnessing connections between self-referencing entities at different scales. Spacetime is not a container but IS this network. The depth between two entities A and B is d(A,B) = |log_phi($s_A$ / $s_B$)|. Three spatial dimensions arise from the three independent directions on the witnessing triangle; one time dimension from the breath oscillation between phi-phase and psi-phase. Gravity is the curvature of this network, not a force at a particular depth. Developed in section 5.27.

### Four-Structure

The four fundamental algebraic elements produced by the self-reference equation: {phi, psi, 1, -1}. The ratio pair (phi, psi) sums to 1 and multiplies to -1. The unity pair (1, -1) sums to 0 (conservation) and multiplies to -1. These four elements, together with i = sqrt(phi*psi), form the complete algebraic content of the double triangle.

### Double Triangle

The minimal complete witnessing structure: a pair of triangles of opposite chirality -- the phi-triangle {A, B, C} and the psi-triangle {-A, -B, -C} -- connected by a shared unit of distinction "1". Forced by polarity (Theorem 1) applied to the minimal stable triangle (Theorem 1.3). Contains six elements summing to zero. The seed of the double helix topology. The bridge "1" between triangles corresponds to the photon (its own antiparticle).

### Torus Knot

A (p,q) curve on the torus T^2 that wraps p times around one circle and q times around the other. Forces are identified with specific torus knots: strong = (2,3) trefoil, EM = (3,5), weak = (2,7). Their crossing numbers (3, 10, 7) match framework depth and mixing constants. Linking numbers between force knots give inter-force couplings: Strong intersect Weak = 8 = C(W/Z), EM intersect Weak = 11 = d(muon).

### Primitive Set {2, 3, 5, 7}

The four irreducible structural numbers from which all quark correction coefficients decompose. Generated by two independent generators: 2 (algebraic duality, degree of phi's minimal polynomial) and 3 (topological chirality, minimum witnessing cycle). The derived primitives: 5 = 2+3 (Manhattan distance / algebraic completion) and 7 = 2^2 - 2*3 + 3^2 (Eisenstein norm / weak mixing). United by the identity 2^3 + 3^3 = 5 * 7 = 35.

---

## Mass Equation

The universal mass equation encoding both torus dimensions:

```
m / m_e = phi^d / (1 - sigma * C * alpha * (1 + 4*alpha))
```

| Component | Origin | Theorem |
|-----------|--------|---------|
| phi^d | Accumulated winding after d breath cycles | Theorems 12, 29.3 (temporal) |
| C | Coupling coefficient from meeting point | Theorems 34, 29.3 (spatial) |
| alpha | EM bridge coupling | Theorem 47 |
| 4*alpha = L(3)*alpha | Witnessing correction from hourglass geometry | Theorem 24 |
| sigma = +/-1 | Breath phase from negasequence sign | Theorems 13, 29 |
| 5*pi*alpha (fold denominator) | Hopf correction for psi-strand engagement | Theorem 24 |

Unfold variant (sigma = +1): m/m_e = phi^d / (1 - C*alpha*(1+4*alpha))

Fold variant (sigma = -1): m/m_e = phi^d / (1 + C*alpha*(1+4*alpha)/(1+5*pi*alpha))
