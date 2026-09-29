"""Every closed ring carries energy x period = h, whatever its size."""
h=6.62607015e-34; hbar=h/(2*3.141592653589793); c=299792458; eV=1.602176634e-19
me=9.1093837015e-31; mp=1.67262192369e-27; a=1/137.035999177
a0=hbar/(me*c*a); vB=a*c
rows=[("proton torus",hbar/(mp*c),mp*c*c,h/(mp*c*c)),
      ("electron torus",hbar/(me*c),me*c*c,h/(me*c*c)),
      ("hydrogen shell (Bohr)",a0,a*a*me*c*c,2*3.141592653589793*a0/vB)]
for n,r,E,T in rows:
    print(f"{n:22s} size {r:.2e} m  energy {E/eV:.4g} eV  period {T:.3e} s  E*T/h = {E*T/h:.6f}")
