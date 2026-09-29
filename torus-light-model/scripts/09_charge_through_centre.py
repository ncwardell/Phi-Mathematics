"""Charge path that passes through the centre (waist) of the horn torus.
Path: (p,q) torus knot on a horn torus (R = r): p turns around the axis, q turns through the waist.
Charge moves at c, path length = Compton wavelength, period T (shared with the energy loop, spin 1/2).
Axial magnetic moment mu = (e / 2T) * loop integral of (x dy - y dx)."""
import numpy as np
h=6.62607015e-34; hb=h/(2*np.pi); c=299792458; e=1.602176634e-19; m=9.1093837015e-31
lam=h/(m*c); T=lam/c; muB=e*hb/(2*m)
t=np.linspace(0,1,400001)[:-1]
def knot(p,q,R=1.0,r=1.0):
    u=2*np.pi*p*t; v=2*np.pi*q*t
    return np.stack([(R+r*np.cos(v))*np.cos(u),(R+r*np.cos(v))*np.sin(u),r*np.sin(v)])
def length(X): d=np.roll(X,-1,1)-X; return np.sum(np.linalg.norm(d,axis=0))
def area(X): d=np.roll(X,-1,1)-X; return 0.5*np.sum(X[0]*d[1]-X[1]*d[0])
print(f"{'path':32s} {'torus radius R':>15s} {'centre passes':>13s} {'g (spin 1/2)':>12s}")
for p,q in [(1,0),(1,1),(1,2),(1,3),(2,1),(2,3)]:
    X=knot(p,q); s=lam/length(X); X=X*s
    mu=e/T*area(X)                     # area already counts windings
    g=(mu/muB)/0.5
    print(f"({p},{q}) {p} around axis, {q} through centre   {s:15.4e} {q:13d} {g:12.4f}")
