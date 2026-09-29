"""One loop that is both paths at once: (1,1) curve, once around the axis and once through the tube.
Charge rides the loop; energy either uniform (light at constant energy) or skater-weighted (~1/radius).
Path length = Compton wavelength. Reports g and spin for several tube/ring ratios."""
import numpy as np
N=2000000; t=np.arange(N)/N
def calc(rr,skater):
    u=2*np.pi*t; v=2*np.pi*t
    X=np.stack([(1+rr*np.cos(v))*np.cos(u),(1+rr*np.cos(v))*np.sin(u),rr*np.sin(v)])
    d=np.roll(X,-1,1)-X; ds=np.linalg.norm(d,axis=0); L=ds.sum()
    rho=np.hypot(X[0],X[1]); cr=X[0]*d[1]-X[1]*d[0]
    mu=0.5*cr.sum()/L; w=ds/rho if skater else ds.copy(); w/=w.sum(); Lz=np.sum(w*cr/ds)
    return 2*mu/Lz, 2*np.pi*Lz/L
for rr in [0.6,0.8,0.8498,0.9,0.95]:
    gu,su=calc(rr,False); gs,ss=calc(rr,True)
    print(f"tube/ring {rr:.4f}: uniform g={gu:.4f} spin={su:.4f} | skater g={gs:.4f} spin={ss:.4f}")
