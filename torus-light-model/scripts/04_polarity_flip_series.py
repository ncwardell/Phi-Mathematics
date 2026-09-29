"""g-2 with a sign flip at every pass through the waist: a = f - f^2 + f^3 - ... = f/(1+f), f = alpha/2pi."""
import math
a=1/137.035999177; f=a/(2*math.pi); x=a/math.pi; meas=0.00115965218059
qed=[0.5,-0.328478965579,1.181241456,-1.9122457,6.737]
print("QED coefficients of (alpha/pi)^n:      ",qed)
print("flip-at-waist series coefficients:     ",[(-1)**n*0.5**(n+1) for n in range(5)])
for name,v in [("alpha/2pi only",f),("no flip f/(1-f)",f/(1-f)),("flip at waist f/(1+f)",f/(1+f)),("QED to 2nd order",f+qed[1]*x**2)]:
    print(f"{name:24s} {v:.11f}  off by {v-meas:+.2e}")
