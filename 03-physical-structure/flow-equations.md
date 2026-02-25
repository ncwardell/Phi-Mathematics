---
title: "Theorem 41 — Aetheric Flow"
type: theorem
status: proven
depends_on:
  - 03-physical-structure/hamiltonian-constraint
  - 02-meeting-points/hyperbolic-structure
tags:
  - theorem
  - flow-equations
  - rapidity
  - hyperbolic
  - breathing-torus
  - dynamics
  - physical-structure
---

# 3.2 The Flow Equations

> **Theorem 41 (Aetheric Flow):**
> *The natural evolution on the hyperbola pf = m^2 is given by the flow equations dp/deta = -p and df/deta = f, where the dot denotes differentiation with respect to rapidity eta.*

## Statement

The natural evolution on the hyperbola pf = m^2 is given by the flow equations dp/deta = -p and df/deta = f, where the dot denotes differentiation with respect to rapidity eta.

## Proof

From Theorem 14, past = e^(-eta) and future = e^(eta) (in units where m = 1). Differentiating with respect to rapidity:

dp/deta = -e^(-eta) = -p
df/deta = e^(eta) = f

These flow equations encode the breathing torus (Theorem 29): the past intensity decays exponentially (collapse pressure pulling backward) while the future intensity grows exponentially (dynamic self-reference unfolding forward). The particle survives by riding the constraint surface where these two flows balance.

Verification: d(pf)/deta = (dp/deta)f + p(df/deta) = (-p)f + p(f) = 0. The constraint pf = m^2 is preserved by the flow, as required. ∎

## Dependencies

- [Hamiltonian Constraint (Theorem 40)](hamiltonian-constraint.md) -- the constraint H = pf - m^2 = 0 on which the flow operates
- Theorem 14 (Hyperbolic Structure) -- provides p = e^(-eta), f = e^(eta)
- Theorem 29 (Breathing Torus) -- physical interpretation as the breathing cycle

## Dependents

- [Lagrangian (Theorem 42)](lagrangian.md) -- the Lagrangian is constructed to reproduce these flow equations
- [Variational Summary](variational-summary.md) -- flow equations appear as the second entry in the variational table

## Related Concepts

- [Hamiltonian Constraint](hamiltonian-constraint.md) -- the constraint surface on which the flow lives
- [Lagrangian](lagrangian.md) -- the variational principle that reproduces the flow

## Tags

`#theorem` `#flow-equations` `#rapidity` `#hyperbolic` `#breathing-torus` `#dynamics` `#physical-structure`
