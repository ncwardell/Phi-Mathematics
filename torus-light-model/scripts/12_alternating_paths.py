"""The charge alternates, switching at the centre:
   magnetic part = vertical loop through the centre (radius R), charge part = horizontal loop around the axis
   starting and ending at the centre (radius R). Charge moves at c; each part takes half the cycle.
   f_B = share of the energy carried during the magnetic part."""
import numpy as np
h=6.62607015e-34; hb=h/(2*np.pi); c=299792458; e=1.602176634e-19; m=9.1093837015e-31
E=m*c*c; muB=e*hb/(2*m)
def outputs(fB,R):
    T=2*(2*np.pi*R)/c                         # both loops at speed c
    mu=e/T*np.pi*R**2                          # only the horizontal loop has area facing the axis
    L=(1-fB)*E/c*R                             # only the horizontal loop carries angular momentum about the axis
    return (mu/muB)/(L/hb), L/hb, T
for fB in [0.5,0.6,0.75]:
    R=hb/(2*(1-fB)*m*c)                        # size chosen so spin = 1/2
    g,S,T=outputs(fB,R)
    print(f"magnetic part carries {fB:.2f} of the energy: g = {g:.4f}, spin = {S:.3f}, loop size R = {R/(hb/(m*c)):.3f} hbar/mc, E*T/h = {E*T/h:.3f}")
