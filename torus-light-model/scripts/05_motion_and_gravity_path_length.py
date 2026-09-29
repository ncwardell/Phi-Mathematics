import numpy as np
c=299792458.0
print("TEST 1: a loop of light (speed c) carried along at speed v must spiral. Path per cycle vs rest:")
L0=1.0; N=200000
for b in [0.1,0.5,0.9,0.99]:
    v=b*c; w=np.sqrt(c*c-v*v)          # loop-wise speed left over
    T=L0/w                              # time to close one loop
    t=np.linspace(0,T,N); th=2*np.pi*w*t/L0; rr=L0/(2*np.pi)
    P=np.stack([rr*np.cos(th),rr*np.sin(th),v*t])
    Lpath=np.sum(np.linalg.norm(np.diff(P,axis=1),axis=0))
    print(f"  v={b:4.2f}c  path/rest = {Lpath/L0:.5f}   gamma = {1/np.sqrt(1-b*b):.5f}   clock slows by {T*c/L0:.5f}")
print()
print("TEST 2: gravity from a gradient in path length. If the surrounding field lengthens every loop")
print("by factor n(r)=1+GM/(r c^2), a torus drifts toward longer paths with a = -c^2 d(ln n)/dr:")
G=6.674e-11
for name,M,R in [("Earth surface",5.972e24,6.371e6),("Sun surface",1.989e30,6.957e8),("GPS orbit",5.972e24,2.656e7)]:
    lnn=lambda r:np.log1p(G*M/(r*c*c)); h=R*1e-3
    a=-c*c*(lnn(R+h)-lnn(R-h))/(2*h)
    print(f"  {name:14s} path lengthening = {G*M/(R*c*c):.3e}   a = {a:9.4f} m/s^2   Newton GM/r^2 = {G*M/R**2:9.4f}")
