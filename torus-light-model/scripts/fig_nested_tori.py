import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
MAG="#2563eb"; ELEC="#dc2626"; WAIST="#16a34a"; INK="#1e293b"; MUTED="#64748b"
fig,(a,b)=plt.subplots(1,2,figsize=(16,7.5),gridspec_kw=dict(width_ratios=[1.15,1]),facecolor="white")
s=np.linspace(0,2*np.pi,400)
shells=[(1.0,"#1d4ed8",3.0),(1.9,"#3b82f6",2.4),(3.0,"#60a5fa",1.9),(4.4,"#93c5fd",1.5)]
for k,(R,col,lw) in enumerate(shells):
    for sx in (-1,1):
        a.plot(sx*R+R*np.cos(s),R*np.sin(s),color=col,lw=lw)
        for ang in (np.pi/2,0.0,3*np.pi/2):
            x=sx*(R+R*np.cos(ang)); y=R*np.sin(ang); dx,dy=sx*np.sin(ang),-np.cos(ang)
            a.annotate("",xy=(x+0.05*dx,y+0.05*dy),xytext=(x-0.25*dx,y-0.25*dy),arrowprops=dict(arrowstyle="-|>",color=col,lw=1.6,mutation_scale=14))
    a.text(2*R,-0.35 if k%2==0 else 0.35,"⊙",color=ELEC,ha="center",va="center",fontsize=13,weight="bold")
    a.text(-2*R,-0.35 if k%2==0 else 0.35,"⊗",color=ELEC,ha="center",va="center",fontsize=13,weight="bold")
a.plot([0,0],[-5,5],color=MAG,lw=2.5); a.annotate("",xy=(0,5.4),xytext=(0,4.8),arrowprops=dict(arrowstyle="-|>",color=MAG,lw=2.5,mutation_scale=20))
a.scatter([0],[0],s=240,color=WAIST,zorder=6)
a.annotate("Shared waist:\nevery shell's magnetic\nflux passes through here",xy=(0,0),xytext=(-6.3,4.3),color=WAIST,fontsize=10.5,
           arrowprops=dict(arrowstyle="->",color=WAIST))
a.text(6.3,4.6,"Inner torus\n(inside every shell)",color=shells[0][1],fontsize=10.5,ha="center")
a.annotate("",xy=(1.2,1.0),xytext=(5.4,4.2),arrowprops=dict(arrowstyle="->",color=shells[0][1]))
a.text(6.6,-4.9,"Outer shells",color=shells[3][1],fontsize=10.5,ha="center")
a.set_aspect("equal"); a.axis("off"); a.set_xlim(-9.3,9.3); a.set_ylim(-5.6,5.8)
a.set_title("Nested tori sharing one hourglass",fontsize=14,weight="bold",color=INK)
a.text(0,-5.55,"Cross-section: each shell is a bigger hourglass through the same waist.\nThis is exactly the shape of a magnetic dipole's field lines.",ha="center",fontsize=10,color=INK)

b.axis("off"); b.set_xlim(0,1); b.set_ylim(0,1)
b.set_title("Real nested scales in the electron / atom",fontsize=14,weight="bold",color=INK,loc="left")
rows=[("Classical electron radius","α · ħ/mc","2.82 × 10⁻¹⁵ m"),
      ("Electron torus (our model)","ħ/mc","3.86 × 10⁻¹³ m"),
      ("Hydrogen atom (Bohr radius)","ħ/mc ÷ α","5.29 × 10⁻¹¹ m")]
y=0.84
for i,(n,f,v) in enumerate(rows):
    b.add_patch(plt.Rectangle((0.02,y-0.06),0.96,0.12,color=["#dbeafe","#bfdbfe","#93c5fd"][i],alpha=0.6,lw=0))
    b.text(0.05,y+0.015,n,fontsize=12,weight="bold",color=INK); b.text(0.05,y-0.035,f,fontsize=11,color=MUTED)
    b.text(0.95,y,v,fontsize=12,ha="right",va="center",color=INK)
    if i<2:
        b.annotate("",xy=(0.5,y-0.155),xytext=(0.5,y-0.065),arrowprops=dict(arrowstyle="-|>",color=ELEC,lw=2))
        b.text(0.54,y-0.11,"× 137  (= 1/α)",color=ELEC,fontsize=12,weight="bold",va="center")
    y-=0.22
b.text(0.03,0.13,"Each shell is 137 times the one inside it.\n"
       "α is the same self-reference coupling that gave g − 2 = α/2π,\n"
       "so the coupling that corrects one loop also sets the spacing between shells.",fontsize=11,color=INK,va="center")
plt.tight_layout(); plt.savefig("../figures/nested_tori.png",dpi=140)
