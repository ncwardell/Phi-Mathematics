---
title: "§5.24.6 Permanent Magnets: Where the Lens Points"
type: applied-analysis
status: speculative-direction
depends_on:
  - /05-toolkit/geometry/magnetic-order.md
  - /05-toolkit/geometry/crystalline-lattices.md
  - /05-toolkit/geometry/platonic-solids.md
  - /05-toolkit/assumptions-audit.md
tags:
  - permanent-magnets
  - rare-earth-free
  - anisotropy
  - metastability
  - exchange-spring
  - tetrataenite
  - applied
  - part-v
---

# §5.24.6 Permanent Magnets: Where the Lens Points

## Statement of Limits (read first)

> **The framework cannot compute a magnet. §5.24.4 tested $\phi$ against ordering temperature, saturation magnetization, and exchange threshold — and rejected all three. Those are precisely the quantities that determine permanent magnet performance.**

Nothing in this section derives a material from $\Sigma = 0$. Any future claim that it does should be checked against audit entry A-M1, which already records the failures.

What follows is the framework used as a **search heuristic** — a lens that says *where to look*, not *what you will find*. A lens is judged by whether it redirects attention productively, not by whether it is a correct theory. This one does redirect, in three specific and non-obvious ways, and each redirection is checked below against real materials data.

---

## I. The Problem, In Numbers

A permanent magnet needs three things simultaneously:

1. **High saturation magnetization $M_s$** — sets the absolute ceiling $(BH)_{\max} \le B_s^2/4\mu_0$.
2. **High magnetocrystalline anisotropy $K_1$** — resists demagnetization. Quantified by the hardness parameter $\kappa = \sqrt{K_1/(\mu_0 M_s^2)}$; a usable magnet needs $\kappa > 1$.
3. **High Curie temperature $T_C$** — with working margin above room temperature.

| Material | $B_s$ (T) | $K_1$ (MJ/m³) | $T_C$ (K) | $(BH)_{\max}$ ceiling | $\kappa$ | Class |
|----------|-----------|---------------|-----------|----------------------|----------|-------|
| Fe$_{65}$Co$_{35}$ | 2.45 | 0.02 | 1210 | 150 MGOe | **0.06** | free |
| bcc Fe | 2.15 | 0.048 | 1043 | 116 MGOe | **0.11** | free |
| Fe$_{16}$N$_2$ | 2.40 | 1.00 | 810 | 144 MGOe | 0.47 | free |
| L1$_0$-FeNi | 1.60 | 1.20 | 823 | 64 MGOe | 0.77 | free |
| Nd$_2$Fe$_{14}$B | 1.61 | 4.90 | 585 | 65 MGOe | **1.54** | Nd |
| $\tau$-MnAl | 0.78 | 1.70 | 650 | 15 MGOe | **1.87** | free |
| MnBi (LTP) | 0.78 | 1.20 | 628 | 15 MGOe | **1.57** | free |
| SrFe$_{12}$O$_{19}$ | 0.47 | 0.35 | 750 | 5.5 MGOe | **1.41** | free |
| SmCo$_5$ | 1.07 | 17.2 | 1020 | 29 MGOe | **4.34** | Sm |

**The entire problem is in the first two rows against the last two.** Fe–Co has the highest magnetization any material will ever have — and essentially zero anisotropy, because it is cubic. SmCo$_5$ is rock-hard and magnetically weak. Nobody has both.

The division is not accidental:

- $M_s$ comes from **electron counting** — the Slater–Pauling curve, $m \approx |N_v - 2N_\downarrow|$. Integer, well understood, and **already at its physical maximum** at Fe$_{65}$Co$_{35}$. There is no headroom left and no theory will create any.
- $K_1$ comes from **spin–orbit coupling acting through a low-symmetry crystal field**. It is a symmetry quantity. Rare earths supply it because 4f electrons have large unquenched orbital moment; the crystal field then locks that orbital moment, and hence the spin, to a crystallographic axis.

---

## II. Lens Redirection 1 — The Moment Side Is Closed; Work the Symmetry Side

§5.24.4 Section VIII.2 showed saturation moments follow integer electron counting with no $\phi$. §5.24.5 Section IV showed shell capacities are $\mathrm{SO}(3)/\mathrm{SO}(4)$ integers with no $\phi$. The framework is *structurally silent* on magnitude.

Read as a lens, that silence is informative rather than embarrassing: **it says the moment side of the problem is not where the framework — or anyone — will find anything, because it is closed integer combinatorics that is already saturated.**

Conversely, everything the framework *is* natively about — symmetry, topology, closure, broken degeneracy — lives on the $K_1$ side. And $K_1$ is where every real research program is in fact working.

A quantitative statement of the whole field's problem:

$$\text{cubic symmetry} \implies K_1 \text{ small} \qquad \text{(Fe: 0.048, Fe-Co: 0.02 MJ/m}^3\text{)}$$
$$\text{uniaxial symmetry} \implies K_1 \text{ large} \qquad \text{(L1}_0\text{, hexagonal, tetragonal: 1-17 MJ/m}^3\text{)}$$

Every good permanent magnet in existence is uniaxial. None is cubic. **Anisotropy is purchased with broken symmetry**, and the lens correctly identifies symmetry-breaking — not moment — as the design resource.

---

## III. Lens Redirection 2 — Every Cheap Candidate Is Metastable, and That Is Structural

The framework's central claim about $\phi$ is that it is the eigenvalue of **marginal self-reference** — the value at which a structure is exactly able to sustain itself and no more. §5.24.4 confirmed $\phi$ appears at marginal boundaries (criticality, frustration, aperiodicity) and nowhere else.

Point that lens at the candidate list and a pattern appears immediately:

| Candidate | Thermodynamic status | Failure mode |
|-----------|---------------------|--------------|
| Fe$_{16}$N$_2$ ($\alpha''$) | **metastable** | decomposes to Fe$_4$N + Fe above ~200 °C |
| $\tau$-MnAl | **metastable** | decomposes to $\beta$-Mn + $\gamma_2$ |
| L1$_0$-FeNi | ordered phase, **kinetically unreachable** | ~1 atomic jump per 2,600 years below 320 °C |
| MnBi (LTP) | **low-temperature phase only** | structural transition at 628 K |
| Nd$_2$Fe$_{14}$B | stable | — (but needs Nd) |
| SmCo$_5$ | stable | — (but needs Co) |

**Every rare-earth-free candidate worth pursuing is metastable or kinetically trapped. Every thermodynamically comfortable magnet needs a critical element.**

This is not coincidence, and the reason is the same as Redirection 1. Cheap, abundant elements (Fe, Ni, Mn, Al, N) have cubic ground states — close-packed or bcc, high symmetry, low anisotropy. To get uniaxial symmetry out of cheap elements you must hold the system in a structure that is *not* its ground state. The anisotropy and the metastability have a common cause.

So the lens yields a usable design rule, stated in the framework's own vocabulary:

> **A cheap permanent magnet is a marginally stable structure. The design problem is not finding the phase — it is holding it.**

This reframing is the section's main content, and it is where the framework's instinct genuinely earns its place: a framework built around marginal stability points straight at the class of materials that the field has, independently, converged on.

---

## IV. Lens Redirection 3 — It Is a Path Problem, Not a Materials Problem

L1$_0$-FeNi (tetrataenite) is the sharpest case, and the most promising cheap candidate:

- **Composition:** roughly equiatomic Fe and Ni. No rare earth, no cobalt. Raw material ~\$9/kg.
- **Properties:** $K_1 \approx 1.2$ MJ/m³, $B_s = 1.6$ T, $T_C = 823$ K, theoretical $(BH)_{\max} \approx 42$ MGOe (335 kJ/m³) — competitive with commercial Nd-Fe-B.
- **Occurrence:** forms naturally in iron meteorites, which cooled at roughly 1 K per million years.
- **Obstacle:** below the 320 °C order–disorder temperature, atomic mobility is approximately **one atomic jump per 2,600 years**. The phase is thermodynamically fine. It is kinetically inaccessible.

Nobody is searching for this material. It is known, characterized, and cheap. **The entire difficulty is the route.**

And the routes that work are topological rather than compositional. The NITE method (nitrogen insertion and topotactic extraction) achieves single-phase L1$_0$-FeNi with order parameter 0.71 by:

1. nitriding disordered A1-FeNi with ammonia to form **FeNiN**, which orders readily;
2. removing the nitrogen **topotactically** — the lattice framework is preserved while the scaffold species leaves;
3. leaving behind the ordered L1$_0$ arrangement that could never have been reached directly.

A third element is used as a **temporary ordering scaffold**, then withdrawn without disturbing the structure it imposed. The order is inherited from a path, not from equilibrium.

This is a statement about *connectivity in configuration space* — which structures can be continuously deformed into which others, and through what intermediates. That is the framework's native language, and it is the one place where its habits of thought (topology, closure, admissible paths) map onto the actual open problem rather than onto a quantity the framework has already been shown not to predict.

**Concrete research question in that language:** given a target uniaxial phase that is kinetically unreachable, which scaffold species admit a topotactic exit — i.e. which insertions order the lattice *and* can be removed without a reconstructive transition? Nitrogen works for FeNi. The question of what else works, and whether it can be predicted from structure rather than found by trial, is open and is not obviously hard for the wrong reasons.

---

## V. Honest Negative: No $\phi$ in the Exchange-Spring Optimum

The exchange-spring (nanocomposite) magnet is the standard route past the $M_s$/$K_1$ tradeoff: couple a hard phase supplying anisotropy to a soft phase supplying magnetization, at a length scale below the hard phase's domain wall width.

This is a genuine marginal-stability optimization — too little soft phase wastes magnetization, too much decouples and coercivity collapses — so by the lens's own logic it is a place $\phi$ might appear. It was tested directly.

Optimizing realizable $(BH)_{\max}$ subject to the coercivity constraint $H_c \ge M_r/2$, with soft phase Fe$_{65}$Co$_{35}$:

| Hard phase | Optimal soft fraction | Mixed $B_s$ | Realizable $(BH)_{\max}$ | Feature size needed |
|-----------|----------------------|-------------|-------------------------|--------------------|
| Nd$_2$Fe$_{14}$B | 0.597 | 2.11 T | 111 MGOe | ~9 nm |
| $\tau$-MnAl | 0.505 | 1.62 T | 63 MGOe | ~15 nm |
| MnBi | 0.451 | 1.53 T | 56 MGOe | ~18 nm |
| SrFe$_{12}$O$_{19}$ | 0.329 | 1.12 T | 28 MGOe | ~34 nm |
| L1$_0$-FeNi | 0.307 | 1.86 T | 85 MGOe | ~18 nm |
| Fe$_{16}$N$_2$ | 0.001 | 2.40 T | 142 MGOe | ~20 nm |

The optimal fractions span 0.001–0.597 and track $K_1$ continuously. They are **not** a universal constant, and $1/\phi = 0.618$ and $1/\phi^2 = 0.382$ have no privileged position among them. Per the control in §5.24.4 Section I, even a single close hit would carry no weight at an 8.2% chance rate.

**Result: REJECTED.** The exchange-spring optimum is ordinary micromagnetics. Recorded so it is not revisited.

The physically important number in that table is not a ratio but a **length**: every entry requires nanostructuring at 9–34 nm with clean phase boundaries, in bulk, at scale. That — not the ratio — is why exchange-spring magnets have never been commercialized despite thirty years of theoretical promise.

---

## VI. Reframing "Cheap"

Raw material cost per kilogram, and per unit of delivered energy product:

| Material | Raw \$/kg | $(BH)_{\max}$ | \$/kJ | Critical element |
|----------|-----------|---------------|-------|-----------------|
| Fe$_{16}$N$_2$ | 0.5 | 350 kJ/m³ | 0.011 | none |
| SrFe$_{12}$O$_{19}$ | 0.6 | 35 | 0.082 | none |
| $\tau$-MnAl | 2.1 | 100 | 0.109 | none |
| L1$_0$-FeNi | 9.4 | 300 | 0.258 | none |
| Nd$_2$Fe$_{14}$B | 19.3 | 400 | 0.367 | **Nd, Dy** |
| MnBi | 8.3 | 80 | 0.926 | none |
| SmCo$_5$ | 24.1 | 200 | 1.036 | **Co** |

Two corrections to the usual framing:

1. **Samarium is one of the cheapest rare earths** (~\$6/kg; it is a byproduct in oversupply relative to demand). SmCo$_5$ is expensive because of **cobalt** (~\$33/kg, supply concentrated in the DRC), not samarium. "Rare-earth-free" is the wrong target. The real target is **Nd/Dy-free and Co-lean**.
2. **Raw material cost is not the binding constraint for the cheap candidates.** Fe$_{16}$N$_2$ is made of iron and air and is thirty times cheaper per unit energy than Nd-Fe-B. It is not commercial because it decomposes. The cost that matters is **process cost of holding a metastable phase**, which none of these numbers capture.

Combined with Section III, this is the sharpest practical conclusion available here:

> **The cheap magnet problem is not an elemental scarcity problem. It is a phase-stabilization and process problem. The materials are already known, already cheap, and already have adequate intrinsic properties.**

---

## VII. What Would Actually Be Worth Testing

Ordered by tractability, not by how well they flatter the framework.

1. **Topotactic scaffold survey.** Nitrogen orders FeNi and exits cleanly. Systematically ask which other light interstitials (B, C, H, O) impose uniaxial order on a cheap cubic host *and* admit a non-reconstructive exit. This is the L1$_0$-FeNi route generalized, and it is a structural/topological question.

2. **Interstitial ordering in Fe-Co.** Fe$_{65}$Co$_{35}$ has the highest magnetization available and near-zero anisotropy purely because it is cubic. Tetragonal distortion is predicted to raise $K_1$ by orders of magnitude. Stabilizing that distortion in bulk — by interstitials, epitaxial strain, or a third element — is the single highest-ceiling target in the field (150 MGOe). Nobody has held it in bulk.

3. **Quasicrystal approximants as anisotropy hosts** — flagged with a strong caveat. Approximants have large unit cells with many inequivalent, low-symmetry sites, which is in principle favourable for crystal-field anisotropy, and they are the framework's own $\{3,5\}$ territory (§5.24.5). **But the honest evidence is discouraging:** real icosahedral quasicrystals order magnetically only at 16–23 K (§5.24.4 Section VI), and aperiodic averaging tends to cancel net anisotropy rather than build it. This is listed because the lens points here, not because the data supports it. It should be tested and most likely abandoned.

4. **Process routes for $\tau$-MnAl.** Of the cheap uniaxial phases it has the best $\kappa$ (1.87) and genuinely cheap elements (\$2.1/kg). Its ceiling is modest (15 MGOe intrinsic, ~63 MGOe in an ideal exchange spring) but its problem is decomposition kinetics — again a stabilization problem, and a less extreme one than Fe$_{16}$N$_2$.

**Falsification condition for this entire section:** if a rare-earth-free magnet exceeding 40 MGOe in bulk is commercialized by a route that is neither metastable-phase stabilization nor topotactic/scaffolded synthesis, then Redirections 2 and 3 were wrong and this section should be withdrawn.

---

## VIII. Summary

| Claim | Status |
|-------|--------|
| Framework computes magnet properties | **NO** — A-M1 rejects $T_C$, $M_s$, exchange |
| $\phi$ in exchange-spring optimum | **REJECTED** — tested, spans 0.001-0.597 |
| $\phi$ in quasicrystal magnet anisotropy | **UNSUPPORTED** — real QCs order at 16-23 K |
| Moment side is closed integer combinatorics | supported (Slater-Pauling; §5.24.4 VIII.2) |
| Anisotropy requires broken symmetry | established physics |
| Cheap candidates are all metastable | **observed pattern, 4/4** |
| The bottleneck is path, not composition | **supported** (L1$_0$-FeNi; NITE route) |
| "Rare-earth-free" is the wrong target | supported (Sm is cheap; Co and Nd/Dy are not) |

The framework did not produce a magnet and cannot. Used as a lens, it correctly identifies that the moment side is exhausted, that the useful candidates live at marginal stability, and that the open problem is one of admissible paths through configuration space rather than of composition. Those three redirections agree with where the field has independently arrived, which is the most that should be claimed for a heuristic.

---

## Dependencies

- [Magnetic Order (§5.24.4)](magnetic-order.md) -- the rejections of $T_C$, moment and exchange that bound this section; the 8.2% control
- [Crystalline Lattices (§5.24.5)](crystalline-lattices.md) -- symmetry, aperiodicity, and the quasicrystal caveat
- [Platonic Solids (§5.20)](platonic-solids.md) -- the $\{3,5\}$ structures of Section VII.3
- [Assumptions Audit (§5.30)](/05-toolkit/assumptions-audit.md) -- entry A-M1 bounds every claim here

## References

- Skomski, R. & Coey, J. M. D. (1993), *Phys. Rev. B* **48**, 15812 -- exchange-spring giant energy product
- Coey, J. M. D. (2020), *Engineering* **6**, 119 -- perspective on permanent magnets and critical elements
- Goto, S. et al. (2017), *Sci. Rep.* **7**, 13216 -- [single-phase L1$_0$-FeNi by nitrogen insertion and topotactic extraction](https://pmc.ncbi.nlm.nih.gov/articles/PMC5643398/)
- Lewis, L. H. et al. -- tetrataenite for permanent magnet applications; ordering kinetics below 320 °C

## Tags

`#permanent-magnets` `#rare-earth-free` `#anisotropy` `#metastability` `#exchange-spring` `#tetrataenite` `#applied` `#part-v`
