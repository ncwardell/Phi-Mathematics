---
title: "The Weak Bosons -- Conjugate Pairs at Depth 25"
type: prediction
status: high-confidence
depends_on:
  - 04-extensions/universal-mass-equation.md
  - 03-physical-structure/force-equations/electromagnetic-coupling.md
  - 03-physical-structure/gauge-structure.md
tags:
  - weak-bosons
  - z-boson
  - w-boson
  - conjugate-pairs
  - electroweak
  - depth-25
  - part-iv
---

# 4.3 The Weak Bosons -- Conjugate Pairs at Depth 25

**Status: HIGH CONFIDENCE** (independently confirmed by computational search)

## Z Boson

**(d, n) = (25, 8), C = 8 = F(6), $\sigma$ = $-1$ (unfold)**

$m_Z/m_e = \phi^{25} / (1 - 8\alpha) = 167,761 / 0.9416 \approx 178,100$

| Quantity | Predicted | Measured | Error |
|----------|-----------|----------|-------|
| $m_Z/m_e$ | 178,100 | 178,450 | **0.2%** |

## W Boson

**(d, n) = (25, 8), C = 8 = F(6), $\sigma$ = $+1$ (fold)**

$m_W/m_e = \phi^{25} / (1 + 8\alpha) = 167,761 / 1.0584 \approx 158,500$

| Quantity | Predicted | Measured | Error |
|----------|-----------|----------|-------|
| $m_W/m_e$ | 158,500 | 157,340 | **0.7%** |

## Structural Interpretation

W and Z are **conjugate pairs** -- the same structure at the same address (d=25, n=8) with opposite breath phase $\sigma$. This is the SU(2) doublet (Theorem 46) manifested directly: strand exchange in one direction (W, fold) versus the other (Z, unfold).

**Why d = 25:** $25 = F(5)^2 = 5^2$. The depth is the square of the algebraic completion number. The electroweak scale lives at the depth where the discriminant ($\sqrt{5}$) meets itself.

**Why C = 8 = F(6):** The sixth Fibonacci number. The correction coefficient advances one step beyond F(5) = 5 (the muon's coefficient), which is structurally appropriate: the weak bosons mediate the interaction that the muon participates in, so their coupling involves the next Fibonacci step.

**Why n = 8 = F(6):** The temporal index matches the correction coefficient -- both are F(6). This is a resonance condition: the spatial and temporal coordinates coincide at the same Fibonacci value.

---

## Dependencies

- [Universal Mass Equation (§4.1)](universal-mass-equation.md) -- $m/m_e = \phi^d / (1 + \sigma \cdot C \cdot \alpha)$
- [Electromagnetic Coupling](../03-physical-structure/force-equations/electromagnetic-coupling.md) -- $\alpha$ entering the correction
- [Gauge Structure (Theorem 46)](../03-physical-structure/gauge-structure.md) -- SU(2) doublet structure

## Cross-References

- [Higgs Boson (§4.4)](higgs-boson.md) -- one depth deeper at d=26
- [Mass Equation (Theorem 48)](../03-physical-structure/mass-equation.md) -- the lepton equation this extends
- [Complete Prediction Table](../03-physical-structure/prediction-table.md) -- Part III predictions for comparison
- [Open Questions (§3.12)](../03-physical-structure/open-questions.md) -- W-Z mass splitting derivation (Question 4)

## Tags

`#weak-bosons` `#z-boson` `#w-boson` `#conjugate-pairs` `#electroweak` `#depth-25` `#part-iv`
