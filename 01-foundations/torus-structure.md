---
title: "The Torus"
type: theorem
status: proven
depends_on:
  - 01-foundations/emergence-of-time
  - 01-foundations/hyperbolic-constraint
tags:
  - torus
  - minkowski-metric
  - depth
  - time
  - topology
  - identity
---

# 1.17 The Torus

> **Theorem 28 (Torus Structure):**
> *The identity of any self-referential element is a position (d, η) on the torus T² = S¹_depth × S¹_time, with Minkowski metric.*

## Statement

The directed 3-cycle of time defines a circle S¹_time. The depth structure of self-reference defines a circle S¹_depth. Their product T² = S¹_depth × S¹_time is a torus, and the metric inherited from the hyperbolic constraint is ds² = dd² − dη² (Minkowski signature).

## Proof

From [Theorem 12](emergence-of-time.md): time is the index of dynamic self-reference — a periodic process on the directed 3-cycle. The cycle repeats: A → B → C → A → ... This defines a circle S¹_time.

From the depth structure: self-reference unfolds to various depths d. The meeting point structure (see Part II) constrains d to discrete values, but the underlying topology is a circle S¹_depth.

The product T² = S¹_depth × S¹_time is a torus. A position on this torus is a pair (d, η) specifying depth and temporal phase.

The metric, from [Theorem 14](hyperbolic-constraint.md):

ds² = dd² − dη²

The Minkowski signature distinguishes spacelike (depth) from timelike (rapidity) directions. ∎

## Corollaries

*(None stated explicitly.)*

## Dependencies

- [Theorem 12 — Emergence of Time](emergence-of-time.md): Provides S¹_time as the periodic cycle of dynamic self-reference.
- [Theorem 14 — Hyperbolic Constraint](hyperbolic-constraint.md): Provides the Minkowski metric ds² = dd² − dη² on the torus.

## Dependents

- [Theorem 29 — Breathing Torus](breathing-torus-and-spin.md): The torus is the arena for the antiphase oscillation of the two strands.
- [Theorem 29.3 — Dual Dimensions](breathing-torus-and-spin.md): The two circles of the torus carry distinct physical roles (spatial resonance vs. temporal depth).

## Tags

`torus` · `minkowski-metric` · `depth` · `time` · `topology` · `identity`
