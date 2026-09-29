import numpy as np
alpha=1/137.035999177; a_meas=0.00115965218059
hbar=1.054571817e-34;c=299792458;m=9.1093837015e-31
lamC=2*np.pi*hbar/(m*c)
rE=hbar/(2*m*c); rq=hbar/(m*c)
# Horn torus model. Total energy mc^2. Fraction f is self-interaction energy held at the waist
# (radius 0, carries no angular momentum). Remaining (1-f) circulates at rE (2 loops, 4pi).
# Spin fixed at hbar/2  ->  rE scales by 1/(1-f); charge radius rq=2rE (shared period).
# => g = 2/(1-f),  anomaly a = g/2-1 = f/(1-f)
def anomaly(f): return f/(1-f)
print("Self-interaction energy U = alpha*hbar*c/d for the charge meeting its own field at distance d:")
cands={"inner radius hbar/2mc":rE,"charge radius hbar/mc":rq,"diameter 2hbar/mc":2*rq,
       "one full loop (Compton wavelength)":lamC,"two loops (4pi path)":2*lamC}
for name,d in cands.items():
    f=alpha*hbar*c/d/(m*c*c)
    a=anomaly(f)
    print(f"  d = {name:36s} f = {f:.6e}  a = {a:.6e}  ({a/a_meas:7.4f} x measured)")
print()
f=alpha/(2*np.pi)
a_model=anomaly(f)
schw=alpha/(2*np.pi); qed2=schw+(-0.328478965579)*(alpha/np.pi)**2
print(f"measured a_e              = {a_meas:.11f}")
print(f"Schwinger alpha/2pi       = {schw:.11f}  (off by {schw-a_meas:+.2e})")
print(f"QED to 2nd order          = {qed2:.11f}  (off by {qed2-a_meas:+.2e})")
print(f"horn-torus model f/(1-f)  = {a_model:.11f}  (off by {a_model-a_meas:+.2e})")
print(f"model 2nd-order coefficient: {(a_model-schw)/(alpha/np.pi)**2:+.4f} x (alpha/pi)^2   vs QED -0.3285")
