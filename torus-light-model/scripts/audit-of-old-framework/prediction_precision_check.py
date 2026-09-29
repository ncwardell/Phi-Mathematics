import numpy as np
phi=(1+5**.5)/2; pi=np.pi
# CODATA 2022-ish values and 1-sigma relative uncertainties
a_inv=137.035999177; a_inv_u=0.000000021
mu=206.7682827; mu_u=0.0000046
tau=3477.23; tau_u=0.23
MP=2.176434e-8/9.1093837e-31; MP_u=MP*1.1e-5     # Planck mass / m_e  (G-limited)
G=6.67430e-11; hbar=1.054571817e-34; c=299792458; me=9.1093837e-31
aG=G*me**2/(hbar*c); aG_u=aG*2.2e-5
# repo alpha: 5 pi a^2 + a(1-(phi^2+4)phi^-20) - phi^-10 = 0
A=5*pi; B=1-(phi**2+4)*phi**-20; C=-phi**-10
alpha=(-B+np.sqrt(B*B-4*A*C))/(2*A)
a=1/a_inv
rows=[("1/alpha",1/alpha,a_inv,a_inv_u),
      ("muon/e",phi**11/(1-5*a*(1+4*a)),mu,mu_u),
      ("tau/e",phi**17/(1+4*a*(1+4*a)/(1+5*pi*a)),tau,tau_u),
      ("Planck/e",phi**(107+1/(4*pi)),MP,MP_u),
      ("alpha/alpha_G",phi**(204-1/(4*pi)),a/aG,(a/aG)*2.2e-5)]
print(f"{'quantity':14s} {'repo formula':>16s} {'measured':>16s} {'rel. error':>11s} {'meas. unc.':>11s} {'sigmas off':>11s}")
for n,p,m,u in rows:
    print(f"{n:14s} {p:16.8g} {m:16.8g} {abs(p-m)/m:11.1e} {u/m:11.1e} {abs(p-m)/u:11.1f}")
