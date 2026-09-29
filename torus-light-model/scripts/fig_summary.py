import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ELEC="#dc2626"; MAG="#2563eb"; WAIST="#16a34a"; SURF="#94a3b8"; INK="#1e293b"; MUTED="#64748b"; MASS="#f59e0b"
fig=plt.figure(figsize=(17,12.5),facecolor="white")
fig.suptitle("The torus model so far: one light loop, seen at rest, in motion, and among other tori",fontsize=17,weight="bold",color=INK,y=0.985)
s=np.linspace(0,2*np.pi,300)

# ---- Panel 1: at rest ----
a=fig.add_axes([0.03,0.52,0.30,0.42]); a.set_aspect("equal"); a.axis("off")
a.set_title("1 · At rest: a self-referencing light loop",fontsize=13,weight="bold",color=INK)
for sx in (-1,1):
    a.fill(sx+np.cos(s),np.sin(s),color=SURF,alpha=0.12); a.plot(sx+np.cos(s),np.sin(s),color=MAG,lw=2.5)
    for ang in (np.pi/2,0.0,3*np.pi/2):
        x=sx*(1+np.cos(ang)); y=np.sin(ang); dx,dy=sx*np.sin(ang),-np.cos(ang)
        a.annotate("",xy=(x+0.06*dx,y+0.06*dy),xytext=(x-0.22*dx,y-0.22*dy),arrowprops=dict(arrowstyle="-|>",color=MAG,lw=2,mutation_scale=16))
    for vv in np.linspace(np.pi/4,2*np.pi+np.pi/4,4,endpoint=False):
        a.text(sx*(1+0.55*np.cos(vv)),0.55*np.sin(vv),"⊙" if sx>0 else "⊗",color=ELEC,ha="center",va="center",fontsize=13,weight="bold")
a.plot([0,0],[-1.35,1.35],color=MAG,lw=2); a.scatter([0],[0],s=160,color=WAIST,zorder=5)
a.text(0,-1.75,"Electric (red) circulates around the axis\nMagnetic (blue) loops through the waist: the hourglass\nThey cross at 90°, like a light wave",ha="center",fontsize=10,color=INK)
a.text(0,1.55,"waist",color=WAIST,ha="center",fontsize=10)
a.set_xlim(-2.3,2.3); a.set_ylim(-2.25,1.8)

# ---- Panel 2: moving ----
b=fig.add_axes([0.37,0.55,0.30,0.38],projection="3d")
b.set_title("2 · Moving: the loop must take a longer path",fontsize=13,weight="bold",color=INK)
t=np.linspace(0,2*np.pi,300)
b.plot(np.cos(t),np.sin(t),0*t,color=MAG,lw=2.5,label="At rest: closed circle")
beta=0.8; g=1/np.sqrt(1-beta**2); tt=np.linspace(0,2*np.pi*2,600)
b.plot(np.cos(tt),np.sin(tt),tt*beta/np.sqrt(1-beta**2)/(2*np.pi)*1.1,color=ELEC,lw=2.2,label=f"Moving at 0.8c: spiral, path × {g:.2f}")
b.quiver(1.6,0,0,0,0,2.2,color=INK,lw=2,arrow_length_ratio=0.12); b.text(1.75,0,2.4,"motion",color=INK,fontsize=10)
b.set_axis_off(); b.view_init(elev=14,azim=-55); b.set_box_aspect((1,1,1.3))
b.legend(loc="lower center",bbox_to_anchor=(0.5,-0.06),frameon=False,fontsize=10)
fig.text(0.52,0.525,"Extra path = γ exactly  →  time dilation, γmc², inertia",ha="center",fontsize=11,color=INK,weight="bold")

# ---- Panel 3: among other tori ----
c=fig.add_axes([0.70,0.52,0.28,0.42]); c.set_aspect("equal"); c.axis("off")
c.set_title("3 · Among other tori: gravity",fontsize=13,weight="bold",color=INK)
c.add_patch(plt.Circle((0,0),0.9,color=MASS,alpha=0.85)); c.text(0,0,"accumulated\ntori\n(mass M)",ha="center",va="center",fontsize=9,color=INK,weight="bold")
for rr in (1.3,1.9,2.6,3.4):
    c.plot(rr*np.cos(s),rr*np.sin(s),color=MUTED,lw=0.8,ls=":")
for ang in np.linspace(0,2*np.pi,7,endpoint=False)+0.3:
    for rr in (1.55,2.3,3.1):
        k=0.9/rr   # exaggerated path lengthening near mass
        cx,cy=rr*np.cos(ang),rr*np.sin(ang); rad=0.16*(1+1.2*k)
        c.plot(cx+rad*np.cos(s),cy+rad*np.sin(s),color=MAG,lw=1+1.5*k,alpha=0.9)
cx,cy=3.1*np.cos(0.3+2*np.pi*4/7),3.1*np.sin(0.3+2*np.pi*4/7)
c.annotate("",xy=(cx*0.72,cy*0.72),xytext=(cx*0.93,cy*0.93),arrowprops=dict(arrowstyle="-|>",color=ELEC,lw=2.5,mutation_scale=18))
c.text(0,-4.15,"Near mass, every loop's path is longer, so its clock runs slower.\nEach torus drifts toward longer paths: always attractive.",ha="center",fontsize=10,color=INK)
c.set_xlim(-3.8,3.8); c.set_ylim(-4.6,3.8)

# ---- Panel 4: gravity check chart ----
d=fig.add_axes([0.06,0.08,0.36,0.34])
d.set_title("Gravity from path lengthening vs Newton",fontsize=13,weight="bold",color=INK,loc="left")
G=6.674e-11; M=5.972e24; C=299792458.0
r=np.linspace(6.371e6,4.2e7,300)
newton=G*M/r**2; model=C*C*(G*M/(r**2*C*C))/(1+G*M/(r*C*C))
d.plot(r/1e6,newton,color=MUTED,lw=6,alpha=0.35,label="Newton  GM/r²")
d.plot(r/1e6,model,color=MAG,lw=2,label="Torus drift toward longer paths")
for name,rr in [("Earth surface",6.371e6),("GPS orbit",2.656e7)]:
    d.scatter([rr/1e6],[G*M/rr**2],color=ELEC,zorder=5); d.annotate(f"{name}\n{G*M/rr**2:.4f} m/s²",(rr/1e6,G*M/rr**2),xytext=(14,-22) if name.startswith("Earth") else (12,8),textcoords="offset points",fontsize=9,color=INK)
d.set_xlabel("Distance from Earth's centre (thousand km)",color=INK); d.set_ylabel("Pull (m/s²)",color=INK)
d.spines[["top","right"]].set_visible(False); d.legend(frameon=False,fontsize=10); d.grid(alpha=0.25)
d.text(0.99,0.55,"Requires paths lengthened by GM/rc²\n(7 parts per 10 billion at Earth's surface,\nmeasured by GPS and optical clocks)",transform=d.transAxes,ha="right",fontsize=9,color=MUTED)

# ---- Panel 5: scorecard ----
e=fig.add_axes([0.48,0.05,0.50,0.40]); e.axis("off"); e.set_xlim(0,1); e.set_ylim(0,1)
e.set_title("Scorecard",fontsize=13,weight="bold",color=INK,loc="left")
rows=[("✓","Mass = electric energy − magnetic energy","exact (Lorentz invariant)"),
      ("✓","Spin ½ from 4π double loop","exact"),
      ("✓","Internal clock = Compton frequency","exact"),
      ("✓","Magnetic moment g = 2 (charge on outer rim)","exact, rim placement assumed"),
      ("~","g − 2 = α/2π from one self-reference loop","within 0.27%"),
      ("✗","Second-order g − 2 term","wrong sign (+0.25 vs −0.33)"),
      ("✓","Motion lengthens loop by γ","exact: time dilation, inertia"),
      ("✓","Path-length gradient gives Newton's gravity","exact, if lengthening = GM/rc²"),
      ("?","Derive GM/rc² from neighbouring tori","next test"),
      ("?","Fix 2nd-order term with electric − magnetic at waist","next test")]
col={"✓":WAIST,"~":MASS,"✗":ELEC,"?":MUTED}
for i,(m,txt,res) in enumerate(rows):
    y=0.87-i*0.09
    e.text(0.0,y,m,fontsize=15,color=col[m],weight="bold",va="center",fontfamily="DejaVu Sans")
    e.text(0.05,y,txt,fontsize=11,color=INK,va="center")
    e.text(0.99,y,res,fontsize=10.5,color=col[m],va="center",ha="right")
    e.plot([0,1],[y-0.047,y-0.047],color="#e2e8f0",lw=0.8)
plt.savefig("../figures/torus_model_summary.png",dpi=140)
