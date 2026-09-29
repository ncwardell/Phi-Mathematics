import numpy as np
phi=(1+5**.5)/2; pi=np.pi; a=1/137.035999177
Cs=[1,2,3,4,5,8,11,13,18,21,29,34]          # Fibonacci/Lucas/meeting-point style coefficients
vals=[]
for d in range(0,40):
    for C in Cs:
        k=C*a*(1+4*a)
        vals += [phi**d/(1-k), phi**d/(1+k), phi**d/(1+k/(1+5*pi*a)), phi**d/(1-k/(1+5*pi*a))]
vals=np.sort(np.array(vals)); print("formulas in family:",len(vals))
rng=np.random.default_rng(0)
T=np.exp(rng.uniform(np.log(100),np.log(5000),200000))
idx=np.clip(np.searchsorted(vals,T),1,len(vals)-1)
err=np.minimum(abs(vals[idx]-T),abs(vals[idx-1]-T))/T
for tol in [1.5e-5,6e-6]:
    print(f"random number in 100-5000 matched within {tol*100:.4f}%: {np.mean(err<tol)*100:.2f}% of the time")
