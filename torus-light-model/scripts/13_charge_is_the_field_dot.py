"""Charge and field dot as ONE point: the charge itself winds the (1,N) path on the donut
(once around the axis, N times around the tube: outer edge = hbar/mc, inner edge = hbar/2mc).
Energy loop unchanged (spin 1/2 at hbar/2mc, period T = h/mc^2). Two ways to time the charge."""
import numpy as np
h=6.62607015e-34; hb=h/(2*np.pi); c=299792458; e=1.602176634e-19; m=9.1093837015e-31
T=h/(m*c*c); muB=e*hb/(2*m); rin=hb/(2*m*c); rout=hb/(m*c); Rt=(rin+rout)/2; rt=(rout-rin)/2
t=np.linspace(0,1,400001)[:-1]
for N in [0,1,2,4,8]:
    u=2*np.pi*t; w=2*np.pi*N*t
    X=np.stack([(Rt+rt*np.cos(w))*np.cos(u),(Rt+rt*np.cos(w))*np.sin(u),rt*np.sin(w)])
    if N==0: X=np.stack([rout*np.cos(u),rout*np.sin(u),0*u])
    d=np.roll(X,-1,1)-X; L=np.linalg.norm(d,axis=0).sum(); A=0.5*np.sum(X[0]*d[1]-X[1]*d[0])
    g_sameT=(e/T*A/muB)/0.5                     # one lap per energy period T (speed = L/T)
    Tc=L/c; g_atc=(e/Tc*A/muB)/0.5              # charge held at speed c (lap takes L/c)
    print(f"N={N}: path/lap = {L/rout:6.3f} x (hbar/mc)   same period: speed {L/T/c:5.2f}c, g = {g_sameT:5.3f}   |   at speed c: g = {g_atc:5.3f}")
