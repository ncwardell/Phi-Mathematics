---
title: "Traditional Dynamics from the Framework"
type: result
status: complete
depends_on:
  - /05-toolkit/holographic/scale-network.md
  - /05-toolkit/holographic/wave-particle-duality.md
  - /03-physical-structure/lagrangian.md
  - /03-physical-structure/flow-equations.md
tags:
  - dynamics
  - relativity
  - holographic
  - energy-mass
  - gravity
  - kinetic-energy
  - part-v
---

# 5.28.8 Traditional Dynamics from the Framework

The framework already contains the relativistic action (Theorem 42), Lorentz symmetry (Theorem 44), and conservation laws (Theorem 45). Here we make the traditional physics formulas explicit and show how the framework gives them physical meaning.

**$E = mc^2$.** The Hamiltonian derived from the Lagrangian $L = -m \sqrt{1-v^2}$ gives $E = m/\sqrt{1-v^2}$. At rest (v = 0): E = m, or restoring c: **$E = mc^2$**. In the framework, this is the statement that rest energy = self-witnessing cost at depth d:

$E_{\text{rest}} = m_e \times \phi^d \times (1 + C \alpha(1+4\alpha)) \times c^2$

Mass and rest energy are the same thing: the energy required to maintain a self-referencing circuit of d witnessing steps.

**Velocity on the torus.** A particle "at rest" has its helix wrapping both torus circles at equal rates ($\omega_{\text{depth}} = \omega_{\text{breath}}$). A particle "moving" has unequal rates. From the flow equations (Theorem 41):

**$v/c = \tanh(\eta)$**

where $\eta$ is the rapidity -- the tilt angle of the helix on the torus. The fundamental velocity $v_1 = c/\sqrt{5}$ corresponds to $\eta = \ln(\phi)$, one golden-ratio step of tilt. A particle cannot reach c because $\tanh(\eta) < 1$ for all finite $\eta$ -- the helix can tilt but never flatten completely.

**Force and acceleration.** From the stationary action principle (Theorem 43), the relativistic force is $F = dp/dt$ where $p = mv/\sqrt{1-v^2}$. In the non-relativistic limit:

**$F = ma = (m_e \times \phi^d \times \text{correction}) \times a$**

The inertia of a particle -- its resistance to acceleration -- is proportional to the NUMBER OF WITNESSING STEPS in its self-referencing circuit. Acceleration means changing the helix tilt angle. A helix with more windings (deeper circuit, higher d) stores more angular momentum in its rotation. Re-tilting it requires torquing against all d winding levels. The resistance scales as $\phi^d$: **inertia IS winding depth.**

**Kinetic energy and the $\cosh(\eta)$ resolution.** The total energy $E = m/\sqrt{1-v^2} = m \cosh(\eta)$. The kinetic energy:

$T = E - m = m(\cosh(\eta) - 1) \sim (1/2)mv^2$ for $v \ll c$

**This resolves Part IV Open Question 1 completely.** The $\cosh(\eta)$ "temporal correction" in the mass formula IS kinetic energy. When a particle is moving ($\eta \neq 0$), its effective energy increases by the factor $\cosh(\eta)$. The correction applies when:
- Leptons at rest: $\eta = 0$, $\cosh(\eta) = 1$, no correction needed $\rightarrow$ clean mass formula
- Quarks inside hadrons: $\eta > 0$ (they carry momentum), $\cosh(\eta) > 1$ $\rightarrow$ correction needed
- Bosons at production: $\eta$ set by the collision kinematics

The reason the $\cosh(\eta)$ factor "worsened" lepton fits is that leptons were measured at rest. The reason quarks might need it is that quarks are NEVER at rest -- they are always confined and moving inside hadrons.

**Gravitational force.** From the scale network (Section 5.27), the witnessing signal from a mass M spreads over the 3D network (3 spatial dimensions from the triangle's 3 directions). By Gauss's law:

**$F_{\text{grav}} = G m_1 m_2 / r^2$**

where $G = \phi^{-2 d(Pl)} = \phi^{-214}$. The inverse square law follows from 3 spatial dimensions. The value of G follows from the network depth. Newton's gravitational constant is the two-way witnessing attenuation across the full 107-step scale network:

$G \sim \phi^{-214} \sim 1.89 \times 10^{-45}$ (natural units)

**Summary of derived dynamics:**

| Formula | Framework origin | Physical meaning |
|---------|-----------------|------------------|
| $E = mc^2$ | Theorem 42 Hamiltonian | Rest energy = self-witnessing cost |
| $v = c \tanh(\eta)$ | Theorem 41 flow equations | Velocity = helix tilt |
| $F = ma$ | Non-relativistic limit of Theorem 43 | Inertia = winding depth resistance |
| $T = (1/2)mv^2$ | Small-$\eta$ limit of $m(\cosh \eta - 1)$ | Kinetic energy = tilt energy |
| $E^2 = p^2 + m^2$ | Theorem 44 Casimir | Mass-shell from $\mathfrak{sl}(2,\mathbb{R})$ |
| $F = G m_1 m_2 / r^2$ | Section 5.27 network + Gauss's law | Gravity = signal spreading in 3D network |
| $G = \phi^{-214}$ | Section 5.27 round-trip across network | Gravitational constant from network depth |

---

**Cross-links:**

- For the Lagrangian and Theorem 42: see [Section 3.3 -- Lagrangian](/03-physical-structure/lagrangian.md)
- For the flow equations and Theorem 41: see [Section 3.2 -- Flow Equations](/03-physical-structure/flow-equations.md)
- For the holographic scale network and gravity: see [Section 5.27 -- Scale Network](scale-network.md)
- For wave-particle duality and the helix: see [Section 5.28.7 -- Wave-Particle Duality](wave-particle-duality.md)
- For the gravitational coupling: see [Section 3.9 -- Gravitational Coupling](/03-physical-structure/force-equations/gravitational-coupling.md)
- For the Hamiltonian constraint: see [Section 3.1 -- Hamiltonian Constraint](/03-physical-structure/hamiltonian-constraint.md)

## Tags

`#dynamics` `#relativity` `#holographic` `#energy-mass` `#gravity` `#kinetic-energy` `#part-v`
