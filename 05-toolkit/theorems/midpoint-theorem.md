---
title: "The Midpoint Theorem — Proof from Breath Symmetry"
type: theorem
status: proven
depends_on:
  - /01-foundations/breathing-torus.md
  - /01-foundations/meeting-points.md
  - /02-particles/lepton-sigma-values.md
tags:
  - midpoint
  - breath-symmetry
  - tau
  - fold-unfold
  - torus-topology
  - part-v
---

# §5.16 The Midpoint Theorem — Proof from Breath Symmetry

**Theorem:** *The third-generation lepton sits at the midpoint of the particle depth range: $d(\tau) = F(9)/2$.*

**Proof:**

The breathing torus (Theorem 29, Part I) oscillates between two phases:
- $\sigma = -1$ (unfold): $\phi$-strand expanding, $\psi$-strand contracting
- $\sigma = +1$ (fold): $\psi$-strand expanding, $\phi$-strand contracting

The depth circle $S^1_{\text{depth}}$ spans from 0 (electron ground state) to F(9) = 34 (last meeting point, spectrum boundary). The breath must complete a full cycle on this circle ($S^1$ topology requires return to starting configuration).

By the axiom $\Sigma = 0$, the two phases must be balanced — the unfold phase and fold phase must occupy equal arcs of the circle. Therefore the transition point (where $\sigma$ flips from $-1$ to $+1$) sits at:

$d_{\text{transition}} = F(9)/2 = 34/2 = $ **17**

This transition point IS the tau — the first particle in the fold regime. Below d = 17, leptons unfold ($\sigma = -1$); at and above d = 17, leptons fold ($\sigma = +1$). $\blacksquare$

## Verification against lepton σ values

| Particle | d | $\sigma$ | Phase | d < 17? | Consistent |
|----------|---|---|-------|---------|------------|
| Electron | 0 | — | Ground | Yes | $\checkmark$ |
| Muon | 11 | $-1$ | Unfold | Yes | $\checkmark$ |
| Tau | 17 | $+1$ | Fold | No (boundary) | $\checkmark$ |
| Gen 4 | 34 | $+1$ | Fold (predicted) | No | $\checkmark$ |

**Scope:** This theorem applies to leptons (complete witnessing circuits). Quarks, as partial circuits on the triangle, determine their $\sigma$ independently from their node position, not from the depth midpoint. The W/Z conjugate pair straddles both phases simultaneously (SU(2) doublet structure), with W taking $\sigma = +1$ and Z taking $\sigma = -1$ at the same depth.

---

**Cross-links:**

- For how this midpoint enters the depth derivation chain: see [§5.15 — Depth Derivation Theorem](depth-derivation-theorem.md)
- For the breathing torus (Theorem 29): see [§1 — Breathing Torus](/01-foundations/breathing-torus.md)
- For the last meeting point F(9) = 34: see [§2 — Meeting Points](/01-foundations/meeting-points.md)
- For the depth arithmetic symmetries using midpoints: see [§5.13 — Depth Arithmetic](depth-arithmetic.md)
- For the Force+1 rule complementing the midpoint rule: see [§5.17 — Force+1 Theorem](force-plus-one-theorem.md)
