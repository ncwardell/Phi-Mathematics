---
title: "Quark Correction Coefficients — The Primitive Decomposition"
type: theorem
status: observed
depends_on:
  - /02-particles/quarks.md
  - /02-particles/leptons.md
  - /05-toolkit/theorems/primitive-set-theorem.md
  - /03-forces/weak-mixing.md
tags:
  - quark-coefficients
  - primitive-decomposition
  - pentagon-channel
  - weak-channel
  - electroweak-unification
  - generation-structure
  - part-v
---

# §5.18 Quark Correction Coefficients — The Primitive Decomposition

## The Observation

Complete particles (leptons, bosons) have single Fibonacci or Lucas correction coefficients:

| Particle | C | Identity |
|----------|---|----------|
| Muon | 5 | F(5) |
| Tau | 4 | L(3) |
| W/Z | 8 | F(6) |
| Higgs | 13 | F(7) |

Quarks have compound coefficients that decompose into the framework's four primitives.

## The Four Primitives

The framework's irreducible structural numbers are:

| Number | Symbol | Meaning |
|--------|--------|---------|
| 2 | F(3) | Duality — two strands (φ and ψ) |
| 3 | F(4) | Triangle — witnessing circuit, 3 color charges |
| 5 | F(5) | Pentagon — algebraic completion (F(5) = 5) |
| 7 | L(4) | Weak mixing — from sin²θ_W = φ/7 + α² |

Every quark C value decomposes uniquely into a meaningful combination of these four numbers.

## The Decomposition

**Up-type quarks (charge +2/3):**

| Quark | C | Decomposition | Meaning |
|-------|---|---------------|---------|
| u | 5 | 5 | Pentagon |
| c | 15 | 3 × 5 | Triangle × pentagon |
| t | 29 | 2×7 + 3×5 | Duality×weak + triangle×pentagon |

**Down-type quarks (charge −1/3):**

| Quark | C | Decomposition | Meaning |
|-------|---|---------------|---------|
| d | 13 | 2×3 + 7 | Duality×triangle + weak |
| s | 10 | 3 + 7 | Triangle + weak |
| b | 18 | 2×3 + 5 + 7 | Duality×triangle + pentagon + weak |

## The Two Channels

The decomposition reveals two distinct self-witnessing channels:

**Pentagon channel (5):** Pure EM self-witnessing through algebraic completion. This is the up-type quarks' primary coupling mechanism.

**Weak channel (7):** Self-witnessing through the weak mixing structure L(4) = 7. This appears in *every* down-type quark and *only* in down-type quarks — until Gen 3.

In Gen 1 and Gen 2, the two channels are completely separate: up-type quarks contain 5 but not 7, down-type quarks contain 7 but not 5. In Gen 3, the channels **cross**: the top quark (up-type) acquires 2×7, and the bottom quark (down-type) acquires 5.

## The Generation Progression

**Gen 1 — Basic building blocks:**
- u = 5 (pentagon alone)
- d = 2×3 + 7 (duality × triangle + weak)

The up quark at depth 3 uses *everything available*: 3 (triangle) + 2 (duality) = 5. Its C equals its depth plus the strand duality — it has nothing else to work with.

**Gen 2 — Triangle multiplies both channels:**
- c = 3 × 5 (triangle enters the pentagon channel)
- s = 3 + 7 (triangle enters the weak channel)

The charm quark gains color structure (×3) applied to algebraic completion. The strange quark gains color structure (+3) alongside weak mixing.

**Gen 3 — Channels cross (electroweak mixing):**
- t = 2×7 + 3×5 (weak enters the pentagon channel)
- b = 2×3 + 5 + 7 (pentagon enters the weak channel)

The top quark is the only up-type quark whose C contains 7 (weak mixing). This corresponds to known physics: the top Yukawa coupling ≈ 1, and its mass (~173 GeV) is at the electroweak v.e.v. scale. The bottom quark is the only down-type whose C contains 5 (pentagon), gaining access to the algebraic completion channel.

**The channel crossing at Gen 3 is electroweak unification written in the coupling coefficients.**

### Structural Properties

**7 as weak charge marker:** The number 7 = L(4) appears in every down-type quark C and in no up-type quark C except the top. Down-type quarks have weak isospin −1/2; the weak mixing number literally marks their coupling. The top quark, uniquely among up-type quarks, couples strongly enough to the weak sector to acquire this marker.

**The role of each primitive:**
- 5 (pentagon) appears in: u, c, t (all up-type) and b — the "EM identity" of quarks
- 7 (weak) appears in: d, s, b (all down-type) and t — the "weak identity" of quarks
- 3 (triangle) appears in: c, t, d, s, b (all except u) — color structure beyond the ground state
- 2 (duality) appears in: t, d, b (heaviest of each type per generation) — full two-strand coupling

**The up quark is special:** C(u) = 5 = 3 + 2 is the *only* quark C that decomposes as depth + duality rather than using the primitives as independent factors. The up quark is so elementary that its C equals "everything at depth 3" — it has no structural surplus.

## Cross-Generation Sums

| Generation | C(up) + C(down) | Value | Identity |
|------------|-----------------|-------|----------|
| 1 | 5 + 13 | 18 | L(6) = C(b) |
| 2 | 15 + 10 | 25 | F(5)² = d(W/Z) |
| 3 | 29 + 18 | 47 | L(8) |

The Gen 1 quark C sum equals the Gen 3 bottom quark C — the bottom quark "inherits" the full Gen 1 coupling structure. The Gen 2 sum equals the weak boson depth, linking the quark sector to the force sector. The Gen 3 sum is L(8), the next Lucas number.

## What Remains

This decomposition is observed, not yet derived from first principles. To complete the derivation:

1. Show that the witnessing triangle topology requires exactly the primitive set {2, 3, 5, 7}
2. Prove that up-type node assignment selects the pentagon channel and down-type selects the weak channel
3. Derive the channel-crossing rule at Gen 3 from the bifurcation structure

---

**Cross-links:**

- For the proof that {2, 3, 5, 7} is the primitive set: see [§5.19 — Primitive Set Theorem](primitive-set-theorem.md)
- For the weak mixing angle (L(4) = 7): see [§3 — Weak Mixing](/03-forces/weak-mixing.md)
- For the depth derivation using F(5) and L(4): see [§5.15 — Depth Derivation Theorem](depth-derivation-theorem.md)
- For quark mass formulas: see [§2 — Quarks](/02-particles/quarks.md)
- For lepton correction coefficients: see [§2 — Leptons](/02-particles/leptons.md)
