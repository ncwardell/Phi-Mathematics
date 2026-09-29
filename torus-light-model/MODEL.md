# Torus Light Model: The Math

Inputs: particle mass m, and the constants c, ħ (h = 2πħ), e, α.
Everything else follows from the steps below. Numbers are for the electron.

---

## 0. Current picture: one loop, outside and inside

One loop of light carries the charge. It goes once around the outside (the rim, radius ρ_out) and passes through the centre of the horn torus (the waist, radius ρ_in → 0). Total length is L = h/mc at speed c. Along the loop, angular momentum is conserved, so energy concentrates inward (∝ 1/radius, like a skater pulling in).

With ρ_out + ρ_in = ħ/mc and x = ρ_out/(ħ/mc):

$$S = \frac{\hbar}{2} \ \text{(for any split)}, \qquad g = 2\big(x^2 + (1 - x)^2\big)$$

When the inside passage goes through the exact centre (x → 1): **S = ħ/2, g = 2**, with ρ_out = ħ/mc. The outside lap supplies all the magnetism; spin is shared by both halves. See `scripts/10_one_loop_inside_outside.py`.

The two-circle description in Section 2 (energy at ħ/2mc, charge at ħ/mc) gives the same numbers. It is the bookkeeping version of this one loop, not two objects.

## 1. Closure (one loop of light)

Light moving at c closes on itself after one wavelength.

$$L = \frac{h}{mc}, \qquad T = \frac{L}{c} = \frac{h}{mc^2}, \qquad E\,T = h \;\Rightarrow\; E = mc^2$$

L = 2.4263 × 10⁻¹² m, T = 8.0933 × 10⁻²¹ s, clock 1/T = 1.2356 × 10²⁰ Hz.

## 2. Geometry (horn torus)

Both flows move at c, have length L, and share the period T.

| Flow | Windings | Condition | Radius |
|---|---|---|---|
| Energy (core) | 2 (4π) | 2 · 2π r_E = L | r_E = ħ/2mc = 1.9308 × 10⁻¹³ m |
| Charge (rim) | 1 (2π) | 2π r_q = L | r_q = ħ/mc = 3.8616 × 10⁻¹³ m |

$$r_q = 2r_E \;\Rightarrow\; \text{ring radius } R = \text{tube radius } r = r_E \quad\text{(horn torus)}$$

Torus surface, with the axis along z:

$$\mathbf{x}(u,v) = \big((R + r\cos v)\cos u,\; (R + r\cos v)\sin u,\; r\sin v\big)$$

- Electric flow: along u (toroidal), sign +
- Magnetic flow: along v (poloidal, through the waist), sign −
- The two are orthogonal: $\partial_u \mathbf{x} \cdot \partial_v \mathbf{x} = 0$, so E·B = 0

## 3. Spin

$$S = p\,r_E = \frac{E}{c}\cdot\frac{\hbar}{2mc} = \frac{\hbar}{2}$$

## 4. Magnetic moment and g

$$\mu = I\,A = \frac{e}{T}\,\pi r_q^2 = \frac{e\hbar}{2m} = \mu_B, \qquad g = \frac{\mu/\mu_B}{S/\hbar} = 2$$

With a general charge-ring ratio k = r_q/r_E: charge speed = (k/2)c and g = k²/2. Only k = 2 gives both a charge speed of c and g = 2.

## 5. Mass as polarity (electric + / magnetic −)

$$mc^2 \propto \int \big(\varepsilon_0 E^2 - B^2/\mu_0\big)\,dV \qquad\text{(Lorentz-invariant)}$$

For a moving loop: $(U_E - U_B)\,\gamma = mc^2$. Light (U_E = U_B) has no mass.

## 6. Waist flip

Each pass through the waist multiplies the state by −1:

$$\psi \to (-1)^n \psi, \qquad 2\pi: -1, \qquad 4\pi: +1 \quad\text{(spin ½)}$$

**Flip as an Aharonov–Bohm phase.** The flip is a phase of π, which requires the flux through the waist to be Φ = h/2e. The rim current (I = e/T, thickness a) supplies only

$$\frac{\Phi_{\text{rim}}}{h/2e} = \frac{2\alpha}{\pi}\big(\ln(8R/a) - 2\big) \approx 0.01\text{–}0.27$$

for any thickness from r_e down to below the Planck length. So the half flux quantum must be the magnetic loop's own flux, not something the charge induces. Its field energy, Φ²/2L, equals mc² when the rim thickness is 1.8 × 10⁻³⁶ m (0.11 Planck lengths). See `scripts/08_waist_flux.py`.

## 7. Self-witnessing and g − 2

The charge meets its own light after one loop (distance L):

$$U_1 = \frac{\alpha\hbar c}{L} = \frac{\alpha}{2\pi}\,mc^2 \equiv f\,mc^2$$

Each further pass through the waist flips the sign:

$$a = \frac{g-2}{2} = f - f^2 + f^3 - \dots = \frac{f}{1+f}$$

| | Value |
|---|---|
| f = α/2π | 0.00116140973 |
| Model a | 0.00116006242 |
| Measured a (electron) | 0.00115965218 |
| Difference | +4.1 × 10⁻⁷ |

The signs match QED at all five known orders. The second-order coefficient is −0.25; QED's is −0.3285.

## 8. Breath

$$r(t) = r_E\,\big(1 + \varepsilon \sin \omega_b t\big), \qquad \omega_b = \frac{2mc^2}{\hbar}$$

Breath frequency 2mc²/h = 2.4712 × 10²⁰ Hz, with amplitude scale ħ/2mc (the Zitterbewegung values).

**The charge rides the breathing rim.** The rim radius is R + r(t), so the ring ratio is k(t) = 2 + ε sin ω_b t. Over one breath, with the period fixed:

$$\langle g\rangle = \frac{\langle k^2\rangle}{2} = 2 + \frac{\varepsilon^2}{4}, \qquad a_{\text{breath}} = \frac{\varepsilon^2}{8}$$

Setting a_breath = α/2π requires ε = √(4α/π) = 0.0964. At that depth the charge's peak speed is (1 + ε/2)c = 1.048c, so either the period stretches during expansion or the flow is a phase velocity. Open.

## 9. Motion

Moving at v along the axis, the light still travels at c, so the speed left for going around is c/γ:

$$\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}, \qquad T' = \gamma T, \qquad \text{path per loop} = \gamma L, \qquad E' = \gamma mc^2$$

As v → c, T' → ∞: the loop never closes and time stops. For v > c there is no real solution.

## 10. Witnessing and gravity

Path stretching at x from all other loops:

$$\delta(\mathbf{x}) = \sum_j \frac{G\,m_j}{c^2\,|\mathbf{x} - \mathbf{x}_j|}, \qquad \text{clock rate} = 1 - \delta, \qquad \mathbf{a} = -c^2\,\nabla\delta$$

The constant G is fixed by the whole universe, whose total stretching is:

$$\frac{G M_U}{R_U c^2} = \frac{1}{2}$$

For a single mass M this reduces to Newton's law, a = GM/r². At Earth's surface δ = 6.96 × 10⁻¹⁰.

## 11. Nested shells

Every ring satisfies E·T = h, so energy ∝ 1/size. The electron's length ladder steps by 1/α:

$$r_e = \alpha\,\frac{\hbar}{mc} \;\;\rightarrow\;\; \frac{\hbar}{mc} \;\;\rightarrow\;\; a_0 = \frac{\hbar}{mc\,\alpha}$$

2.82 × 10⁻¹⁵ m → 3.86 × 10⁻¹³ m → 5.29 × 10⁻¹¹ m.

---

## Assumed, not yet derived

1. The 4π energy / 2π charge split (step 2)
2. The self-witnessing distance being L (step 7), and the weights beyond f (the target second-order term is −0.3285)
3. The 1/r witnessing law (step 10)
4. The breath amplitude ε (step 8)
