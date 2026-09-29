import numpy as np
hbar=1.054571817e-34;c=299792458;e=1.602176634e-19;m=9.1093837015e-31
muB=e*hbar/(2*m); lamC=2*np.pi*hbar/(m*c); T=lamC/c
N=200000; t=np.linspace(0,1,N,endpoint=False)
def path(p,q,R,r):   # (p toroidal, q poloidal) torus knot
    th=2*np.pi*p*t; ph=2*np.pi*q*t
    return np.stack([(R+r*np.cos(ph))*np.cos(th),(R+r*np.cos(ph))*np.sin(th),r*np.sin(ph)])
def loop_integral(X):   # closed-loop integral of (x dy - y dx)
    d=np.roll(X,-1,axis=1)-X
    return np.sum(X[0]*d[1]-X[1]*d[0])
def scale_to_length(X,L):
    d=np.roll(X,-1,axis=1)-X; return X*L/np.sum(np.linalg.norm(d,axis=0))
print("A) charge rides WITH the energy, various torus knots (path length = Compton wavelength):")
for (p,q,ratio) in [(2,1,0.3),(2,1,0.99),(2,3,0.5),(1,2,0.5),(2,1,1.0)]:
    X=scale_to_length(path(p,q,1.0,ratio),lamC)
    A=loop_integral(X)
    Lz=(m*c*c/c**2)*A/T         # (E/c^2) * (1/T) * loop integral
    mu=e*A/(2*T)
    print(f"   (p,q)=({p},{q}) r/R={ratio}: spin={Lz/hbar:.3f} hbar, g={2*mu/muB/(2*Lz/hbar):.4f}")
print("B) energy: 2 loops at radius hbar/2mc; charge: 1 loop on outer rim (radius hbar/mc), same period:")
rE=hbar/(2*m*c); rq=hbar/(m*c)
XE=np.stack([rE*np.cos(4*np.pi*t),rE*np.sin(4*np.pi*t),0*t])
Xq=np.stack([rq*np.cos(2*np.pi*t),rq*np.sin(2*np.pi*t),0*t])
Lz=m*loop_integral(XE)/T; mu=e*loop_integral(Xq)/(2*T)
vE=np.sum(np.linalg.norm(np.roll(XE,-1,1)-XE,axis=0))/T; vq=np.sum(np.linalg.norm(np.roll(Xq,-1,1)-Xq,axis=0))/T
print(f"   energy speed={vE/c:.4f}c, charge speed={vq/c:.4f}c, spin={Lz/hbar:.4f} hbar, mu={mu/muB:.4f} muB, g={2*mu/muB/(2*Lz/hbar):.4f}")
