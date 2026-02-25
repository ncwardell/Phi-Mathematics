---
title: "Weak Mixing Angle -- sin^2(theta_W)"
type: theorem
status: proven
depends_on:
  - 03-physical-structure/force-equations/README
  - 03-physical-structure/gauge-structure
  - 03-physical-structure/force-equations/electromagnetic-coupling
tags:
  - theorem
  - weak-mixing-angle
  - weinberg-angle
  - electroweak
  - lucas
  - strand-symmetric
  - physical-structure
---

# 3.9.3 Weak Mixing Angle: sin^2(theta_W) (Geometric -- The Angle Between Symmetries)

> **sin^2(theta_W) = phi/7 + alpha^2**

## Statement

The weak mixing angle theta_W is determined by a geometric relationship between the U(1) and SU(2) symmetry axes. It is not a coupling constant but a ratio between couplings: sin^2(theta_W) = g'^2/(g^2 + g'^2), where g is the SU(2) weak coupling and g' is the U(1) hypercharge coupling. It describes the geometric angle between the bridge (U(1)) and the strand exchange (SU(2)).

## Structural Derivation

**What this quantity IS:** The weak mixing angle is fundamentally different from the other force equations. It is not a coupling constant -- it is a *ratio* between couplings. sin^2(theta_W) = g'^2/(g^2 + g'^2), where g is the SU(2) weak coupling and g' is the U(1) hypercharge coupling. It describes the geometric angle between the bridge (U(1)) and the strand exchange (SU(2)) -- how the two symmetry axes are oriented relative to each other.

**Why 7 = L(4):** The denominator must come from a number that is symmetric between the two strands, because the mixing angle describes the *relationship* between them. L(4) = 7, and crucially, L(-4) = 7 as well. It is one of the rare Lucas values that is identical in both the positive and negative extensions -- a strand-symmetric number. This makes it the natural scale for a quantity that measures the relative orientation of the two symmetry groups, one living on each strand.

**Why phi/7:** This asks: what fraction of the total structure is "bridge" (electromagnetic) versus "strand exchange" (weak)? The fundamental ratio phi divided by the strand-symmetric Lucas value 7 gives the bridge fraction. phi/7 ~ 0.231, meaning ~23% of the electroweak structure is bridge and ~77% is strand exchange. The bridge is the smaller component because U(1) is a simpler symmetry than SU(2) -- one circle versus a three-dimensional rotation group.

**Why alpha^2 and not alpha:** The correction is quadratic, not linear. This is the EM self-loop -- the same 5pi*alpha^2 structure that appears in the EM equation, but here *only the alpha^2 part survives* because the mixing angle doesn't live at a specific depth (no phi^(-n) terms). There is no linear correction and no depth terms because the mixing angle is not measuring the coupling at a depth -- it's measuring a geometric relationship between symmetry axes. The self-loop enters minimally, as the smallest correction the bridge can contribute to its own orientation.

**Physical meaning:** "I'm not a force -- I'm the angle between the bridge and the strand exchange. I'm set by the strand-symmetric Lucas value because I measure a symmetric relationship. My only self-correction is the minimal EM self-loop."

## Result

**sin^2(theta_W) = 0.23120 vs. measured 0.23121. Error: 0.004% (within MS-bar scheme uncertainty)**

## Dependencies

- [Force Equations (Theorem 47)](README.md) -- the overarching force equation framework
- [Gauge Structure (Theorem 46)](../gauge-structure.md) -- the U(1) and SU(2) symmetry groups whose angle is being measured
- [Electromagnetic Coupling](electromagnetic-coupling.md) -- alpha^2 enters as the EM self-loop correction
- [Golden Ratio (Theorem 5)](../../01-foundations/golden-ratio.md) -- phi as the fundamental ratio in the numerator
- Theorem 12 / Lucas numbers -- L(4) = 7 = L(-4) as the strand-symmetric denominator

## Dependents

- The weak mixing angle completes the force equation hierarchy for the non-gravitational forces.

## Related Concepts

- [Gauge Structure](../gauge-structure.md) -- U(1) and SU(2) whose relative orientation theta_W measures
- [Electromagnetic Coupling](electromagnetic-coupling.md) -- alpha whose self-loop provides the correction
- [Strong Coupling](strong-coupling.md) -- the first force in the hierarchy

## Tags

`#theorem` `#weak-mixing-angle` `#weinberg-angle` `#electroweak` `#lucas` `#strand-symmetric` `#geometric` `#physical-structure`
