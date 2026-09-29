"""ONE loop of light: one lap around the outside (radius r_out) and one lap around the inside (radius r_in).
Moves at c, total length = Compton wavelength. The charge rides the loop the whole way.
Energy along the loop follows angular-momentum conservation (like a skater pulling arms in):
energy on a lap ~ 1/radius, so the inside lap carries its share more tightly."""
import numpy as np
h=6.62607015e-34; hb=h/(2*np.pi); c=299792458; e=1.602176634e-19; m=9.1093837015e-31
lam=h/(m*c); T=lam/c; E=m*c*c; muB=e*hb/(2*m)
S=lam/(2*np.pi)                       # r_out + r_in = hbar/mc
print(f"{'inside radius / (hbar/mc)':>26s} {'spin/hbar':>10s} {'g':>8s}")
for x_in in [0.5,0.3,0.1,0.03,0.01,0.001,0.0001]:
    r_in=x_in*S; r_out=S-r_in; radii=np.array([r_out,r_in])
    t_lap=2*np.pi*radii/c                       # time on each lap
    w=t_lap/np.maximum(radii,1e-300)            # energy share ~ time x (1/radius)
    Ew=E*w/w.sum()                              # energy on each lap
    L=np.sum(Ew/c*radii)                        # angular momentum
    mu=np.sum(e/T*np.pi*radii**2)               # charge goes round each lap once per period
    g=(mu/muB)/(L/hb)
    print(f"{x_in:26.2f} {L/hb:10.4f} {g:8.4f}")
print("limit (inside lap through the exact centre): spin = 1/2, g = 2(x_out^2 + x_in^2) -> 2")
