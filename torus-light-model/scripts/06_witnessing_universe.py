import numpy as np
rng=np.random.default_rng(1)
c=1.0
print("="*78)
print("A. A universe of tori. Each torus witnesses every other one; the witnessed")
print("   signal (a radiation field) falls off as 1/r. Path lengthening at x:")
print("   delta(x) = k * sum_j E_j / |x - x_j|,  with k fixed so the whole universe gives 1/2.")
N=400000; RU=1.0
u=rng.random(N)**(1/3); v=rng.normal(size=(N,3)); v/=np.linalg.norm(v,axis=1)[:,None]
X=v*u[:,None]*RU; E=np.full(N,1.0/N)          # total energy 1, spread uniformly
def S(x,P,W): return np.sum(W/np.linalg.norm(P-x,axis=1))
S0=S(np.zeros(3),X,E); k=0.5/S0
print(f"   k = {k:.4f}  (sets G:  G_eff = k c^2)")
for d in [0.0,0.02,0.05,0.1]:
    x=np.array([d,0,0]); h=1e-3
    grad=(k*S(x+[h,0,0],X,E)-k*S(x-[h,0,0],X,E))/(2*h)
    print(f"   at {d:4.2f} R from centre: baseline delta = {k*S(x,X,E):.4f}   (smooth-universe drift = {-k*d/RU**3:+.4f}, grows with distance: cosmic expansion scale)")
print("   -> baseline stays ~1/2 everywhere; distant matter adds no local pull, only a cosmic-scale term.")
print("="*78)
print("B. Add a small local clump (a 'planet') of tori at the centre.")
Mp=1e-6; Np=20000
Pp=rng.normal(size=(Np,3)); Pp/=np.linalg.norm(Pp,axis=1)[:,None]; Pp*=(rng.random(Np)**(1/3))[:,None]*0.004
Ep=np.full(Np,Mp/Np)
Geff=k*c*c
print(f"   clump energy M = {Mp:g}, radius 0.004;  G_eff = k c^2 = {Geff:.4f}")
print(f"   {'r':>6} {'extra delta (clump)':>20} {'drift toward clump':>20} {'G_eff M / r^2':>15} {'ratio':>7}")
for r in [0.006,0.01,0.02,0.04]:
    x=np.array([r,0,0]); h=r*1e-3
    dl=k*S(x,Pp,Ep)
    a=-(c*c)*(k*S(x+[h,0,0],Pp,Ep)-k*S(x-[h,0,0],Pp,Ep))/(2*h)
    print(f"   {r:6.3f} {dl:20.3e} {a:20.4e} {Geff*Mp/r**2:15.4e} {a/(Geff*Mp/r**2):7.4f}")
print("   -> the clump's witnessed share is G_eff M/(r c^2) and its gradient is Newton's 1/r^2 pull.")
print("="*78)
print("C. Light-speed delay. A torus witnesses a moving source where it WAS (retarded).")
print("   Does the pull point to where the source was, or where it is now?")
def retarded(xobs,t,x0,vel):
    lo,hi=-1e3,t
    for _ in range(200):
        m=(lo+hi)/2; d=np.linalg.norm(xobs-(x0+vel*m))-c*(t-m)
        lo,hi=(lo,m) if d>0 else (m,hi)
    return (lo+hi)/2
xobs=np.zeros(3)
for beta in [0.01,0.1,0.5]:
    vel=np.array([beta,0,0]); x0=np.array([0,-1.0,0])      # source passes 1 unit away, now directly below
    tr=retarded(xobs,0.0,x0,vel); xr=x0+vel*tr
    n=(xobs-xr)/np.linalg.norm(xobs-xr); kap=1-n@vel
    Epl=(n-vel)/(kap**3*np.linalg.norm(xobs-xr)**2)          # full witnessed field incl. velocity (magnetic-type) term
    ang=lambda a,b:np.degrees(np.arccos(np.clip(a@b/np.linalg.norm(a)/np.linalg.norm(b),-1,1)))
    now=xobs-x0
    print(f"   v={beta:4.2f}c: retarded-only pull off by {ang(n,now):6.3f} deg;  with velocity term off by {ang(Epl,now):.1e} deg")
print("   -> using only the delayed position gives the wrong direction; the velocity-dependent")
print("      (magnetic-type) part of the witnessed field corrects it exactly to the present position.")
