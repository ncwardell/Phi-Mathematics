import numpy as np
from scipy import integrate
# Units: q^2/(4 pi eps0)=1, c=1, R=1. Rest electric energy of shell U0 = 1/(2R) = 0.5
def energies(b):
    g=1/np.sqrt(1-b*b)
    # field of uniformly moving charge; region outside contracted shell (ellipsoid: z'=gz, r'>=1)
    # use rest-frame coords: x=x'/1, z=z'/g ; dV = dV'/g
    def fE(rp,th):  # integrand in rest-frame spherical coords (rp,th)
        s,c=np.sin(th),np.cos(th)
        x=rp*s; z=rp*c/g; r2=x*x+z*z; sin2=x*x/r2
        E=(1-b*b)/(r2*(1-b*b*sin2)**1.5)
        Bm=b*E*np.sqrt(sin2)
        w=2*np.pi*rp*rp*s/g
        return E*E/(8*np.pi)*w, Bm*Bm/(8*np.pi)*w, (E*Bm*np.sqrt(sin2))/(4*np.pi)*w
    out=[]
    for k in range(3):
        v,_=integrate.dblquad(lambda th,rp: fE(rp,th)[k],1,400,0,np.pi,epsabs=1e-10)
        out.append(v)
    return g,*out
U0=0.5
print(f"{'v/c':>6} {'gamma':>7} {'U_elec':>8} {'U_mag':>8} {'mag %':>6} {'(Ue-Um)*g/U0':>13} {'P/(g*U0*v)':>11}")
for b in [0.0,0.3,0.6,0.9,0.99,0.999]:
    g,Ue,Um,P=energies(b)
    Pn = P/(g*U0*b) if b>0 else float('nan')
    print(f"{b:6.3f} {g:7.2f} {Ue/U0:8.3f} {Um/U0:8.3f} {100*Um/(Ue+Um):6.1f} {(Ue-Um)*g/U0:13.3f} {Pn:11.3f}")
