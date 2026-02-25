---
title: "Wave-Particle Duality from Helical Projection"
type: theorem
status: proven
depends_on:
  - /05-toolkit/holographic/scale-network.md
  - /01-foundations/golden-ratio.md
  - /02-meeting-points/golden-spiral.md
tags:
  - wave-particle-duality
  - heisenberg
  - holographic
  - torus
  - helix
  - de-broglie
  - quantum-classical
  - part-v
---

# 5.28.7 Wave-Particle Duality from Helical Projection

The golden spiral on the torus (Corollary 30.1) traces a **helix** in 3D embedding space. A helix has two natural projections, and these projections ARE wave-particle duality.

**THEOREM (Wave-Particle Duality from Helical Projection):**

*Let $\gamma$ be the golden helix on the breathing torus $T^2$ with $R_1/R_2 = \phi$. Then:*

*(i) The axial projection of $\gamma$ (looking along the propagation axis, end-on) is a circle of radius $R_1$ -- the PARTICLE aspect (localized, periodic).*

*(ii) The transverse projection of $\gamma$ (looking from the side) is a sinusoid of amplitude $R_2$ and wavelength $2\pi R_2$ -- the WAVE aspect (extended, oscillating).*

*(iii) The two projections are Fourier conjugates: $\Delta(\text{circle position}) \times \Delta(\text{wave frequency}) \geq 1/2$, which IS the Heisenberg uncertainty relation $\Delta x \cdot \Delta p \geq \hbar/2$.*

*(iv) The ratio of particle-scale to wave-scale = $\phi^d$ at depth d, so heavier particles appear more classical.*

*(v) These projections correspond to the $\phi$-strand (depth circle) and $\psi$-strand (breath circle), which are conjugate by $\phi \psi = -1$.* $\blacksquare$

**Proof sketch.** The torus path parameterized in $\mathbb{R}^3$:

$x(t) = (R_1 + R_2 \cos \omega_b t) \cos \omega_d t$,   $y(t) = (R_1 + R_2 \cos \omega_b t) \sin \omega_d t$,   $z(t) = R_2 \sin \omega_b t$

Project onto (x,y) plane (suppress z): you see a particle orbiting in a thick circle (annulus), radius $R_1 \pm R_2$. This is the **particle** -- localized, with definite angular position.

Project onto (x,z) plane (suppress y): you see a sinusoidal wave propagating along x with amplitude $R_2$ and frequency $\omega_b$. This is the **wave** -- extended, with definite frequency/momentum.

The two projections are related by Fourier transform (angular position $\leftrightarrow$ angular frequency), so they obey the Fourier uncertainty theorem: $\Delta\theta \cdot \Delta\omega \geq 1/2$. With $\hbar$ restoring units, this is Heisenberg. $\blacksquare$

**The de Broglie relation from the helix.** The circle view gives $E = \hbar \omega$ (energy from angular frequency). The wave view gives $p = h/\lambda$ (momentum from wavelength). On the golden torus:

$E/p = (\omega_d/R_1) / (\omega_b/R_2) = (\omega_d/\omega_b) \times (R_2/R_1) = (\omega_d/\omega_b) / \phi$

At rest (equal winding rates): $E/p = 1/\phi$. The de Broglie wavelength $\lambda = h/p$ is the helix pitch.

**Measurement = choosing a projection.** In the double slit experiment: if you measure "which slit" you are asking a PARTICLE question (circle projection, angular position). This collapses the wave projection (destroys phase coherence). If you don't measure which slit, the WAVE projection is intact and produces interference fringes. The "collapse" is not mysterious -- it is a change of projection axis. The helix doesn't change; the observer's viewpoint does.

**The quantum-classical boundary.** At depth d, the circle circumference exceeds the wave amplitude by $\phi^d$. At d = 0 (electron), the ratio is 1 -- equally wave and particle. At d = 11 (muon), the ratio is $\phi^{11} \sim 199$ -- mostly particle. At d = 26 (top quark), the ratio is $\phi^{26} \sim 271,443$ -- overwhelmingly particle. Heavier particles appear more classical because the circle projection dominates at higher depths. Quantum effects are most visible for light particles (electrons, photons) because their wave and particle scales are comparable.

**Connection to the two strands.** The $\phi$-strand governs the depth circle (position, particle aspect). The $\psi$-strand governs the breath circle (momentum, wave aspect). Since $\phi \psi = -1$, the strands are maximally conjugate -- perfect knowledge of one gives zero information about the other. Wave-particle duality is the observational consequence of the algebraic identity $\phi \psi = -1$.

---

**Cross-links:**

- For the golden spiral on the torus: see [Section 2 -- Golden Spiral](/02-meeting-points/golden-spiral.md)
- For the golden ratio and $\phi \psi = -1$: see [Section 1 -- Golden Ratio](/01-foundations/golden-ratio.md)
- For the holographic scale network: see [Section 5.27 -- Scale Network](scale-network.md)
- For anti-particles and CPT from torus symmetry: see [Section 5.28.4 -- Anti-Particles and CPT](antiparticles-cpt.md)
- For traditional dynamics (E = mc^2, velocity on the torus): see [Section 5.28.8 -- Traditional Dynamics](traditional-dynamics.md)
- For particle depth assignments and the quantum-classical boundary: see [Section 4 -- Phase Space Map](/04-extensions/phase-space-map.md)

## Tags

`#wave-particle-duality` `#heisenberg` `#holographic` `#torus` `#helix` `#de-broglie` `#quantum-classical` `#part-v`
