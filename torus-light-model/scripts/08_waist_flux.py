"""Magnetic flux through the waist. Does the rim current supply the half flux quantum h/2e
that would make the waist sign flip an Aharonov-Bohm phase?
Thin ring, radius R = hbar/mc, wire (rim) thickness a, current I = e/T:
   self-inductance  L = mu0 R (ln(8R/a) - 2),   flux  Phi = L I"""
import math
h=6.62607015e-34; hb=h/(2*math.pi); c=299792458; e=1.602176634e-19; m=9.1093837015e-31
alpha=1/137.035999177; mu0=2*h*alpha/(e*e*c); lP=1.616255e-35
R=hb/(m*c); T=h/(m*c*c); I=e/T; target=h/(2*e)
print(f"rim radius R = {R:.4e} m, current I = e/T = {I:.4e} A, target flux h/2e = {target:.4e} Wb")
print("\n1) Flux from the rim current alone, for candidate rim thicknesses a:")
for name,a in [("classical electron radius (alpha*R)",alpha*R),("breath amplitude (0.0964*R/2)",0.0964*R/2),
               ("Planck length",lP),("1e-3 Planck length",1e-3*lP)]:
    Phi=mu0*R*(math.log(8*R/a)-2)*I
    print(f"   a = {name:36s} {a:.3e} m -> Phi/(h/2e) = {Phi/target:.4f}")
need=2+math.pi/(2*alpha)
print(f"   exact h/2e needs ln(8R/a) = 2 + pi/(2 alpha) = {need:.2f}  ->  a = {8*R*math.exp(-need):.1e} m (impossible)")
print("\n   General result: Phi/(h/2e) = (2 alpha/pi) * (ln(8R/a) - 2)  -> the charge current supplies only ~alpha of it.")
print("\n2) If the waist carries h/2e as its OWN magnetic loop, its field energy is U_B = Phi^2/(2L):")
for name,a in [("classical electron radius",alpha*R),("Planck length",lP)]:
    L=mu0*R*(math.log(8*R/a)-2); UB=target**2/(2*L)
    print(f"   a = {name:26s}: U_B / mc^2 = {UB/(m*c*c):.3f}")
lnB=2+math.pi/(8*alpha); aB=8*R*math.exp(-lnB)
print(f"   U_B = mc^2 exactly needs ln(8R/a) = 2 + pi/(8 alpha) = {lnB:.2f} -> a = {aB:.2e} m = {aB/lP:.3f} Planck lengths")
