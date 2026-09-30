"""Fractal step: the charge is a small copy of the loop; moving around the big ring, its own
light loop spirals at 45 deg (4 turns per lap). Light moves at c along every spiral, so each
forward speed is c/sqrt2. Put the WHOLE particle (energy loop and charge) on that one clock and
ask what size s (radii x s) keeps spin 1/2 and g = 2."""
import numpy as np
h=6.62607015e-34; hb=h/(2*np.pi); c=299792458; e=1.602176634e-19; m=9.1093837015e-31
E=m*c*c; muB=e*hb/(2*m); T0=h/(m*c*c)
vf=c/np.sqrt(2)                                   # forward speed on a 45-degree spiral
for s in [1.0, np.sqrt(2), 2.0]:
    rE=s*hb/(2*m*c); rq=s*hb/(m*c)
    S=(E/c)*(vf/c)*rE                              # only the forward part of the light's momentum turns around the axis
    TE=2*2*np.pi*rE/vf; Tq=2*np.pi*rq/vf           # energy loop: 2 turns; charge: 1 turn
    mu=e/Tq*np.pi*rq**2
    g=(mu/muB)/(S/hb)
    print(f"radii x {s:5.3f}: spin = {S/hb:.4f}  g = {g:.4f}  energy period = {TE/T0:.3f} T0  charge period = {Tq/T0:.3f} T0  E*T/h = {E*Tq/h:.3f}")
