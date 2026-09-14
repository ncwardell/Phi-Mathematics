---
title: "§5.24.4 Magnetic Order and the Golden Threshold"
type: analysis
status: mixed
depends_on:
  - /01-foundations/golden-ratio.md
  - /01-foundations/triangle-structure.md
  - /01-foundations/breathing-torus-and-spin.md
  - /05-toolkit/geometry/electromagnetic-field.md
  - /05-toolkit/geometry/platonic-solids.md
  - /05-toolkit/reference/golden-ratio-properties.md
tags:
  - magnetism
  - exchange-interaction
  - ferromagnetism
  - antiferromagnetism
  - frustration
  - e8
  - ising-chain
  - quantum-criticality
  - fibonacci-anyons
  - kam
  - incommensurate
  - null-result
  - geometry
  - part-v
---

# §5.24.4 Magnetic Order and the Golden Threshold

## Governing Result

> **$\phi$ does not appear in how many electrons a shell holds. It appears at the boundary where magnetic order becomes marginal — at criticality, at frustration, and at aperiodicity.**

§5.24.2 identified the breathing torus with the electromagnetic field: the $\phi$-strand as $\vec{B}$, the $\psi$-strand as $\vec{E}$. That identification concerns the *field*. This section asks a different question: when many such tori are bound into matter, does $\phi$ govern how their moments **order**?

The answer is sharply split, and the split is itself the result. Every test is reported below, including the ones that fail.

---

## I. Method: The Anti-Numerology Control

Before any pattern match, the null hypothesis must be quantified. Powers of $\phi$ are spaced $\ln\phi = 0.4812$ apart in log space. A ratio drawn at random from a broad distribution therefore has a substantial chance of landing near *some* power of $\phi$ purely by luck:

| Tolerance | $P(\text{random ratio within tolerance of some } \phi^n)$ |
|-----------|--------------------------------------------------------|
| $\pm 0.5\%$ | 2.1% |
| $\pm 1\%$ | 4.1% |
| $\pm 2\%$ | **8.2%** |
| $\pm 3\%$ | 12.3% |
| $\pm 5\%$ | 20.3% |

(Analytic value $2\ln(1+t)/\ln\phi$; confirmed by Monte Carlo over $10^5$ samples.)

**Consequence:** a single isolated agreement at the 2% level is worth nothing — it happens by chance roughly one time in twelve. A claim in this section is admitted as **STRONG** only if it is either

1. **exact** — an algebraic identity with zero free parameters and zero tolerance, or
2. **multiple** — several independent quantities hitting simultaneously.

This standard is applied uniformly below. It disqualifies several patterns that look attractive.

---

## II. STRONG: The E8 Spectrum and the Four Golden Pairs

### The mathematics

Zamolodchikov (1989) showed that the two-dimensional Ising model at its critical point, perturbed by a small magnetic field, is an integrable field theory whose particle spectrum is governed by the exceptional Lie algebra $E_8$. The eight masses are fixed with no free parameters:

$$m_1 = 1, \quad m_2 = 2\cos\tfrac{\pi}{5}, \quad m_3 = 2\cos\tfrac{\pi}{30}, \quad m_4 = 2m_2\cos\tfrac{7\pi}{30}$$
$$m_5 = 2m_2\cos\tfrac{2\pi}{15}, \quad m_6 = 2m_2\cos\tfrac{\pi}{30}, \quad m_7 = 4m_2\cos\tfrac{\pi}{5}\cos\tfrac{7\pi}{30}, \quad m_8 = 4m_2\cos\tfrac{\pi}{5}\cos\tfrac{2\pi}{15}$$

Numerically: $1$, $1.618034$, $1.989044$, $2.404867$, $2.956295$, $3.218340$, $3.891157$, $4.783386$.

Since $2\cos(\pi/5) = \phi$ exactly, the second mass *is* the golden ratio. But this is not an isolated occurrence. The spectrum contains **four exact golden pairs**:

$$\boxed{\frac{m_2}{m_1} = \frac{m_6}{m_3} = \frac{m_7}{m_4} = \frac{m_8}{m_5} = \phi}$$

Each verified to machine precision ($<10^{-13}$% deviation). Half the $E_8$ spectrum is the other half scaled by $\phi$. The eight masses are four golden-ratio doublets.

### The experiment

This is not only theory. Coldea et al. (*Science* **327**, 177, 2010) tuned the quasi-one-dimensional Ising ferromagnet **CoNb$_2$O$_6$** (cobalt niobate) through its quantum critical point with a transverse magnetic field and measured the excitation spectrum by neutron scattering. The two lowest modes appeared in the ratio

$$\frac{m_2}{m_1} = 1.64 \pm 0.03 \qquad \text{vs.} \qquad \phi = 1.6180$$

$\phi$ lies comfortably inside the experimental error bar. This is a **measured golden ratio in a real magnet** — the first observation of $E_8$ symmetry in any material.

### Why this matters to the framework

§5.20 already derives $E_8$ **from the icosahedron**: the binary icosahedral group (order 120) corresponds to the $E_8$ Dynkin diagram under the McKay correspondence, and the icosahedron is the $\{3,5\}$ solid whose coordinates $(0, \pm 1, \pm\phi)$ are golden by construction.

So the framework and experimental magnetism reach $E_8$ by two entirely independent routes:

```
framework:   triangle -> {3,5} icosahedron -> binary icosahedral group -> E8
magnetism:   Ising chain -> quantum critical point -> Zamolodchikov -> E8
                                    |
                              both land on phi
```

The framework did not predict the CoNb$_2$O$_6$ result. But the result is exactly what the framework's chain — $\phi \to$ icosahedron $\to E_8$ — says should be found at a critical point. This is the single strongest magnetic contact the framework has, because nothing is fitted on either side.

**Status: STRONG.** The mathematics is exact; the experiment is published and independent.

---

## III. STRONG: The Triangle Is the Minimal Frustrated Unit

The framework's central claim in Part I is that the **triangle is the minimal stable witnessing structure** — three nodes are the fewest that can close a chiral circuit (Corollary 1.3.1).

Magnetism makes an exactly parallel statement, provable in one line.

Place antiferromagnetically coupled Ising spins on the vertices of a graph. A bond is *satisfied* when its two spins are antiparallel. All bonds can be satisfied simultaneously **iff the graph is bipartite** — that is, iff it contains **no odd cycle**.

- **Square** (4-cycle, bipartite): all bonds satisfiable. Néel order. No frustration.
- **Triangle** (3-cycle, the minimal odd cycle): at most 2 of 3 bonds satisfiable. Ground state is 6-fold degenerate out of $2^3 = 8$ states.

The triangle is therefore the **smallest structure in which antiferromagnetic order cannot be satisfied** — the minimal frustrated unit. Wannier (1950) showed the triangular Ising antiferromagnet retains extensive residual entropy $S/k_B = 0.3231$ at zero temperature: it never orders at all.

Extended to lattices, this is the origin of the modern quantum spin liquid. The **kagome** lattice — corner-sharing triangles — is the canonical frustrated host; herbertsmithite is its best material realization.

The framework's triangle and magnetism's triangle are the same object seen from two sides:

| Framework | Frustrated magnetism |
|-----------|---------------------|
| Triangle = minimal chiral circuit that can close | Triangle = minimal odd cycle |
| Fewest nodes that can self-witness | Fewest sites that cannot all agree |
| Stability requires 3 | Frustration requires 3 |

The framework says three is the minimum for a structure to *hold itself up*. Magnetism says three is the minimum for a structure to be *unable to settle*. These are complementary, not contradictory: the triangle is precisely the point where a system becomes rich enough to sustain itself and too constrained to relax — which is the framework's definition of marginal stability.

**Status: STRONG** (graph-theoretic theorem, no fitting).

---

## IV. STRONG: $\phi$ as the Most Irrational Winding

§5.24.2 asserts that the golden strand is the **maximally ergodic** field line on the breathing torus — the winding hardest to approximate by rationals. This is a genuine theorem, and it has a direct magnetic consequence.

**Hurwitz's theorem:** for any irrational $x$, infinitely many rationals satisfy
$$\left| x - \frac{p}{q} \right| < \frac{1}{\sqrt{5}\, q^2}$$
and the constant $\sqrt{5}$ is **optimal** — it cannot be improved, and it is saturated only by numbers equivalent to $\phi$.

Note that the optimal constant is $\sqrt 5$, whose appearance the framework attributes to the discriminant $F(5) = 5$ crystallizing at depth 5 (§5.13). The "most irrational number" theorem and the framework's discriminant are the same $\sqrt 5$.

The continued fractions make the mechanism visible:

| Number | Continued fraction |
|--------|-------------------|
| $\phi$ | $[1; 1, 1, 1, 1, 1, 1, \ldots]$ |
| $\sqrt 2$ (silver) | $[1; 2, 2, 2, 2, \ldots]$ |
| $\pi$ | $[3; 7, 15, 1, 292, \ldots]$ |
| $e$ | $[2; 1, 2, 1, 1, 4, \ldots]$ |

All partial quotients of $\phi$ equal 1 — the slowest possible convergence. Every other number has at least one large quotient, which is a rational approximation that is "too good."

### The magnetic consequence

In **incommensurate magnets** — helimagnets and spin-density-wave systems whose spiral turn angle need not match the lattice — the turn angle tends to **lock in** to rational fractions of the lattice period as temperature or field is varied. Plotted against the control parameter, the locked plateaus form a **devil's staircase**. Rational winding numbers lock easily; irrational ones resist; and the golden winding resists the longest.

This is the same phenomenon as the KAM theorem in dynamics: as a perturbation grows, invariant tori break in order of how well their winding number is approximated by rationals. In the Chirikov standard map, the **golden-mean torus is the last to break**, at $K_c = 0.971635\ldots$

So the framework's claim that the golden strand is the most robust winding on the torus is not decorative. It is the statement that the golden KAM torus survives the largest perturbation — and in magnetism, that a golden spiral is the configuration most resistant to lattice lock-in.

**Status: STRONG** (Hurwitz and KAM are theorems; the magnetic application is standard incommensurate-magnetism physics).

---

## V. STRONG: Fibonacci Anyons Satisfy the Framework's Own Equation

The framework's founding algebraic step is the self-reference equation
$$\phi^2 = \phi + 1$$

In topological quantum matter, the **Fibonacci anyon** $\tau$ is defined by the fusion rule

$$\tau \times \tau = 1 + \tau$$

"Two of these, fused, give either nothing or one of these." The quantum dimension $d_\tau$ — the asymptotic growth rate of the fusion Hilbert space — obeys

$$d_\tau^2 = 1 + d_\tau \implies \boxed{d_\tau = \phi}$$

This is not an analogy or a numerical fit. It is *literally the framework's self-reference equation*, arising in a magnetic/topological-order context from the requirement that fusion be consistent. The framework derives $\phi$ from "a structure that witnesses itself"; anyon theory derives $\phi$ from "a particle that can fuse with itself to give itself or the vacuum." Both are the statement $x^2 = x + 1$.

The **golden chain** (Feiguin et al., 2007) — a spin chain of coupled Fibonacci anyons — is critical, with central charge $c = 7/10$ (tricritical Ising). Fibonacci anyons are conjectured to occur in the $\nu = 12/5$ fractional quantum Hall state.

**Status: STRONG** (exact, and structurally identical to the framework's own axiom-level equation).

---

## VI. SUPPORTING: Ferromagnetic Order on a Golden Lattice

Quasicrystals have golden-ratio aperiodic order (§5.24.5). For nearly four decades after their 1984 discovery, no quasicrystal was found to exhibit long-range magnetic order — only spin-glass freezing, widely attributed to frustration from the aperiodic structure.

Tamura et al. (*J. Am. Chem. Soc.* **143**, 19938, 2021) reported the first genuine long-range magnetic order in real icosahedral quasicrystals:

| Material | Order | $T_C$ |
|----------|-------|-------|
| Au$_{65}$Ga$_{20}$Gd$_{15}$ | ferromagnetic | 23 K |
| Au$_{65}$Ga$_{20}$Tb$_{15}$ | ferromagnetic | 16 K |

confirmed by magnetic Bragg peaks in neutron diffraction. Antiferromagnetic order in a quasicrystal has since also been reported (*Nature Physics*, 2025).

This establishes that a golden-ratio aperiodic lattice can host cooperative magnetic order — the moments need no periodic lattice to agree. The framework's picture of matter as a network of breathing tori with $\phi$ winding does not require periodicity either, so this is consistent; but it is a consistency check, not a prediction the framework made.

**Status: SUPPORTING** (real, relevant, but no quantitative $\phi$-agreement is being claimed).

---

## VII. WEAK: The Bethe–Slater Threshold

The **Bethe–Slater curve** plots the exchange integral $J$ against the ratio $r_{ab}/r_{3d}$ of interatomic distance to 3d shell radius. $J > 0$ gives ferromagnetism; $J < 0$ gives antiferromagnetism. Textbook tabulations give:

| Element | $r_{ab}/r_{3d}$ | Order |
|---------|-----------------|-------|
| Cr | 1.30 | antiferromagnetic |
| Mn | 1.47 | antiferromagnetic |
| **—— sign change of $J$ ——** | **[1.47, 1.63]** | |
| Fe | 1.63 | ferromagnetic |
| Co | 1.82 | ferromagnetic |
| Ni | 1.98 | ferromagnetic |
| Gd | 3.10 | ferromagnetic |

The ferromagnetic threshold is bracketed between Mn and Fe, and $\phi = 1.618$ falls inside that bracket. Tempting: *ferromagnetism begins at $\phi$.*

**This should not be accepted.** Three objections:

1. **The conventional threshold is 1.5, not $\phi$.** The literature value was *assumed empirically* to separate positive from negative exchange. It is a fitted round number, not a measurement.
2. **The bracket is 0.16 wide** and contains 1.5 and $\phi$ equally comfortably. It cannot distinguish them.
3. **The mechanism is refuted.** Cardias et al. (*Sci. Rep.* **7**, 4058, 2017) revisited the Bethe–Slater curve with modern electronic-structure theory and found the sign of the nearest-neighbour coupling is governed by a competitive interplay of several orbital contributions, not by a single distance ratio. The one-parameter picture the $\phi$ claim would rest on is not the real physics.

**Status: WEAK / not admitted.** The bracket is real, but a threshold known only to $\pm 0.08$ against a mechanism known to be oversimplified cannot support a claim about $\phi$. Recorded here so that it is not "rediscovered" later and mistaken for evidence.

---

## VIII. REJECTED: Null Results

These tests were run and **failed**. They are reported in full because a framework that only publishes its hits cannot be evaluated.

### VIII.1 Curie and Néel temperatures are not $\phi$-powers

Every pairwise ratio among Fe (1043 K), Co (1394 K), Ni (628 K), Gd (292 K), Cr (311 K), Mn (95 K), tested against the nearest power of $\phi$:

| Ratio | Value | Depth $\ln r/\ln\phi$ | Nearest $\phi^n$ | Error |
|-------|-------|----------------------|-----------------|-------|
| Fe/Mn | 10.979 | 4.979 | $\phi^5$ | 1.00% |
| Fe/Ni | 1.661 | 1.054 | $\phi^1$ | 2.64% |
| Ni/Mn | 6.611 | 3.925 | $\phi^4$ | 3.55% |
| Co/Cr | 4.482 | 3.117 | $\phi^3$ | 5.81% |
| Co/Ni | 2.220 | 1.657 | $\phi^2$ | 15.21% |
| Fe/Co | 1.337 | 0.603 | $\phi^1$ | 17.40% |
| Cr/Mn | 3.274 | 2.464 | $\phi^2$ | 25.04% |

(Full 15-pair table computed; worst cases shown.) The depths do not cluster near integers — they scatter across the interval. Two hits under 3% out of 15 pairs is **below** the 8.2% chance rate. **No $\phi$-power structure exists in magnetic ordering temperatures.**

This is expected on the framework's own terms: $T_C$ is a many-body thermodynamic scale set by exchange energies, lattice structure and coordination — not a depth on the torus.

### VIII.2 Saturation moments are not $\phi$-powers

| Element | $m$ ($\mu_B$/atom) | Depth | Nearest $\phi^n$ | Error |
|---------|-------------------|-------|-----------------|-------|
| Fe | 2.22 | +1.657 | $\phi^2$ | 15.20% |
| Co | 1.72 | +1.127 | $\phi^1$ | 6.30% |
| Ni | 0.606 | −1.041 | $\phi^{-1}$ | **1.95%** |
| Gd | 7.55 | +4.201 | $\phi^4$ | 10.15% |

Ni's moment sits 1.95% from $\phi^{-1} = 0.618$. By the Section I control, a single 2% hit occurs by chance 8.2% of the time; with four elements tested, seeing one such hit is entirely unremarkable. Fe, Co and Gd miss badly. **Rejected.**

The real structure here is the **Slater–Pauling curve**, in which the moment tracks $|N_{\text{valence}} - 2N_\downarrow|$ — an integer electron-counting rule, with no $\phi$.

### VIII.3 The periodic table's scaffolding contains no $\phi$

This is the most important negative result, and it is unambiguous.

| Structure | Values | Generating rule |
|-----------|--------|----------------|
| Orbital capacities | 2, 6, 10, 14 | $2(2\ell+1)$ — arithmetic, step 4 |
| Shell capacities | 2, 8, 18, 32 | $2n^2$ |
| Period lengths | 2, 8, 8, 18, 18, 32, 32 | Madelung $(n+\ell)$ ordering |
| Fibonacci | 1, 1, 2, 3, 5, 8, 13, 21 | $F(n) = F(n-1)+F(n-2)$ |

The capacities $2, 6, 10, 14$ form an arithmetic progression with common difference 4 — not a Fibonacci sequence. The shell capacities are $2n^2$. The only overlaps with Fibonacci (2 and 8) are coincidences of small integers.

The same holds for crystallography and magnetic symmetry:

| Count | Value | Fibonacci/Lucas? |
|-------|-------|-----------------|
| Crystal systems | 7 | $L(4) = 7$ — but see below |
| Bravais lattices | 14 | no |
| Crystallographic point groups | 32 | no |
| Space groups | 230 | no |
| Magnetic point groups | 122 | no |
| Magnetic space groups (Shubnikov) | 1651 | no |

Only the 7 crystal systems coincides with a Lucas number, and with 6 other counts tested that is an expected coincidence, not a signal.

**Conclusion: the periodic table and crystallographic classification are integer group theory** — $\mathrm{SO}(3)$/$\mathrm{SO}(4)$ representation dimensions, Pauli exclusion, Madelung ordering, and the enumeration of discrete symmetry groups. There is no golden ratio in the counting, and the framework should not claim one.

---

## IX. What the Split Means

The results partition cleanly, and the partition line is meaningful:

| $\phi$ **absent** | $\phi$ **present and exact** |
|------------------|----------------------------|
| Shell capacities $2(2\ell+1)$ | $E_8$ critical spectrum (4 golden pairs) |
| Shell capacities $2n^2$ | Fibonacci anyon quantum dimension |
| Space-group / point-group counts | Crystallographic restriction (§5.24.5) |
| Curie and Néel temperatures | Golden KAM torus, Hurwitz $\sqrt 5$ |
| Saturation moments | Minimal frustrated unit (triangle) |

Everything in the left column is **counting under a closed symmetry** — how many states fit, how many groups exist. Everything in the right column is **behaviour at a marginal boundary** — a critical point, a frustrated ground state, an aperiodic tiling, a torus about to break.

This is precisely what the framework's own logic predicts. $\phi$ is introduced (Part I) as the eigenvalue of *marginal self-reference* — the fixed point of $x \mapsto 1 + 1/x$, the ratio at which a structure is exactly able to sustain itself and no more. A quantity of that kind has no business governing how many electrons fit in a $d$ shell. It has every business governing where order gives way.

So the framework makes a **falsifiable commitment** here:

> **$\phi$-signatures should be sought at critical points, frustrated ground states, and aperiodic orders — and should be expected to be absent from state-counting.**

The null results in Section VIII are not embarrassments to be explained away. They are the other half of the prediction, and they came out the right way.

---

## X. Open Questions

1. **Does the framework predict the $E_8$ perturbation, or only accommodate it?** §5.20 reaches $E_8$ through the icosahedron and McKay. Zamolodchikov reaches it through integrability of the perturbed Ising CFT. Is there a derivation connecting the two — i.e. does the framework's $\{3,5\}$ structure *imply* that a critical Ising system perturbed by a field must have $E_8$ symmetry? If so this would be a genuine prediction rather than a convergence.

2. **Why four golden pairs and not eight?** The $E_8$ spectrum splits as $\{m_1,m_2\}, \{m_3,m_6\}, \{m_4,m_7\}, \{m_5,m_8\}$. Four doublets. Does the framework's polarity structure ($\sigma = \pm 1$, §5.13) account for the doubling, and the number 4 for $L(3) = 4$, the witnessing quantum?

3. **Is the exchange interaction expressible on the torus?** §5.24.2 derives Maxwell's equations from torus geometry, but exchange is not an electromagnetic interaction — it is Coulomb repulsion plus Fermi statistics. The framework has no account of the Pauli principle. Until it does, it cannot say anything mechanistic about ferromagnetism, only about critical behaviour.

4. **Spin ice and emergent monopoles.** §5.24.2 proves no magnetic monopoles exist on a single $T^2$ (closure), while flagging the scale network as an open case. In spin ice (Dy$_2$Ti$_2$O$_7$, Ho$_2$Ti$_2$O$_7$) magnetic monopoles emerge as deconfined excitations of a pyrochlore lattice — monopoles that exist in the network but not in any constituent. Is this the framework's own caveat realized? Pyrochlore is corner-sharing tetrahedra, and the Pauling residual entropy is $\tfrac12\ln\tfrac32$.

5. **Skyrmion lattices.** Magnetic skyrmions in MnSi form a *hexagonal* lattice. §5.22 identifies the hexagon as the saturation boundary. Is the hexagonal skyrmion lattice the same saturation, or an unrelated close-packing?

6. **Does $\phi$ appear in the devil's staircase of a real helimagnet?** Section IV predicts golden turn angles resist lock-in longest. Holmium and erbium have well-measured incommensurate spiral wavevectors with temperature-dependent lock-in transitions. A direct test: does any measured helimagnet exhibit a lock-in-resistant plateau at golden winding?

---

## Dependencies

- [Golden Ratio (§1)](/01-foundations/golden-ratio.md) -- $\phi^2 = \phi + 1$, the equation Fibonacci anyons also satisfy
- [Triangle Structure (§1)](/01-foundations/triangle-structure.md) -- the triangle as minimal witnessing circuit; here also minimal frustrated unit
- [Breathing Torus (Theorem 29)](/01-foundations/breathing-torus-and-spin.md) -- the winding whose irrationality Section IV quantifies
- [EM Field from Torus (§5.24.2)](electromagnetic-field.md) -- the field identification this section extends from field to matter
- [Platonic Solids (§5.20)](platonic-solids.md) -- the icosahedron $\to$ McKay $\to E_8$ chain met by CoNb$_2$O$_6$
- [Golden Ratio Properties (§5.1)](/05-toolkit/reference/golden-ratio-properties.md) -- powers and identities used throughout

## Dependents

- [Crystalline Lattices (§5.24.5)](crystalline-lattices.md) -- the lattice side of the same question; the crystallographic restriction
- [Permanent Magnets (§5.24.6)](permanent-magnets.md) -- applies the rejections recorded here as hard limits on magnet design
- [Assumptions Audit (§5.30)](/05-toolkit/assumptions-audit.md) -- entries A-M1 through A-M4 record the status claims made here

## Related Concepts

- [Hexagon and Confinement (§5.22)](hexagon-confinement.md) -- the hexagonal saturation boundary, relevant to skyrmion lattices
- [Depth Crystallization (§5.13)](/05-toolkit/reference/depth-crystallization.md) -- $\sqrt 5$ at depth 5, the Hurwitz constant of Section IV

## References

- Zamolodchikov, A. B. (1989), *Int. J. Mod. Phys. A* **4**, 4235 -- $E_8$ structure of the perturbed Ising model
- Coldea, R. et al. (2010), *Science* **327**, 177 -- [Quantum criticality in an Ising chain: experimental evidence for emergent $E_8$ symmetry](https://www.science.org/doi/10.1126/science.1180085); arXiv:1103.3694
- Wannier, G. H. (1950), *Phys. Rev.* **79**, 357 -- residual entropy of the triangular Ising antiferromagnet
- Feiguin, A. et al. (2007), *Phys. Rev. Lett.* **98**, 160409 -- the golden chain
- Tamura, R. et al. (2021), *J. Am. Chem. Soc.* **143**, 19938 -- [Experimental observation of long-range magnetic order in icosahedral quasicrystals](https://pubs.acs.org/doi/10.1021/jacs.1c09954)
- Cardias, R. et al. (2017), *Sci. Rep.* **7**, 4058 -- [The Bethe-Slater curve revisited](https://www.nature.com/articles/s41598-017-04427-9)

## Tags

`#magnetism` `#exchange-interaction` `#ferromagnetism` `#antiferromagnetism` `#frustration` `#e8` `#ising-chain` `#quantum-criticality` `#fibonacci-anyons` `#kam` `#incommensurate` `#null-result` `#geometry` `#part-v`
