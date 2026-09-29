import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
R=r=1.0   # horn torus: tube radius = ring radius (units of hbar/2mc)
CORE="#2563eb"; RIM="#dc2626"; WAIST="#16a34a"; SURF="#94a3b8"
fig=plt.figure(figsize=(15,6.4),facecolor="white")

# --- Panel 1: 3D horn torus ---
ax=fig.add_subplot(1,2,1,projection="3d")
u,v=np.meshgrid(np.linspace(0,2*np.pi,90),np.linspace(0,2*np.pi,60))
X=(R+r*np.cos(v))*np.cos(u);Y=(R+r*np.cos(v))*np.sin(u);Z=r*np.sin(v)
ax.plot_surface(X,Y,Z,color=SURF,alpha=0.13,linewidth=0,shade=False)
ax.plot_wireframe(X,Y,Z,rstride=6,cstride=6,color=SURF,alpha=0.25,linewidth=0.4)
t=np.linspace(0,1,800)
# core: energy, two loops (4pi) on the tube-centre circle; slight spiral so both loops are visible
rc=R*(1+0.06*np.sin(2*np.pi*t)); tc=4*np.pi*t
ax.plot(rc*np.cos(tc),rc*np.sin(tc),0.05*np.cos(2*np.pi*t),color=CORE,lw=3,label="Core: energy, 2 loops (4π) → spin ½, mass")
# rim: charge, one loop (2pi) on outer equator
ax.plot(2*R*np.cos(2*np.pi*t),2*R*np.sin(2*np.pi*t),0*t,color=RIM,lw=3,label="Rim: charge, 1 loop (2π) → magnetism, g = 2")
ax.scatter([0],[0],[0],color=WAIST,s=90,depthshade=False,label="Waist: self-interaction, α/2π")
for k,col,rad in [(0.13,CORE,R),(0.38,RIM,2*R)]:
    a=2*np.pi*k; ax.quiver(rad*np.cos(a),rad*np.sin(a),0,-np.sin(a)*0.5,np.cos(a)*0.5,0,color=col,lw=2.5,arrow_length_ratio=0.5)
ax.set_box_aspect((1,1,0.5)); ax.view_init(elev=28,azim=-60); ax.set_axis_off()
ax.set_title("Horn torus electron (3D)",fontsize=14,weight="bold")
ax.legend(loc="lower center",bbox_to_anchor=(0.5,-0.08),frameon=False,fontsize=10)

# --- Panel 2: cross-section (the hourglass) ---
b=fig.add_subplot(1,2,2); b.set_aspect("equal")
s=np.linspace(0,2*np.pi,300)
for sx in (-1,1):
    b.fill(sx*R+r*np.cos(s),r*np.sin(s),color=SURF,alpha=0.18)
    b.plot(sx*R+r*np.cos(s),r*np.sin(s),color=SURF,lw=1.5)
    b.scatter([sx*R],[0],s=160,color=CORE,zorder=5)
    b.scatter([sx*2*R],[0],s=160,color=RIM,zorder=5)
b.text(1,0.22,"⊙",color=CORE,ha="center",fontsize=16); b.text(-1,0.22,"⊗",color=CORE,ha="center",fontsize=16)
b.scatter([0],[0],s=200,color=WAIST,zorder=6)
b.axvline(0,color="#64748b",ls=":",lw=1)
b.annotate("",xy=(1,-1.25),xytext=(0,-1.25),arrowprops=dict(arrowstyle="<->",color=CORE))
b.text(0.5,-1.42,"ħ/2mc",color=CORE,ha="center",fontsize=11)
b.annotate("",xy=(2,-1.65),xytext=(0,-1.65),arrowprops=dict(arrowstyle="<->",color=RIM))
b.text(1,-1.84,"ħ/mc",color=RIM,ha="center",fontsize=11)
b.annotate("Waist (pinch point)\nself-reference link\nstores α/2π · mc²",xy=(0,0),xytext=(-0.95,1.45),
           fontsize=10,color=WAIST,ha="center",arrowprops=dict(arrowstyle="->",color=WAIST))
b.annotate("Core circle\nenergy · 4π · spin ½",xy=(1,0),xytext=(1.25,1.45),fontsize=10,color=CORE,ha="center",
           arrowprops=dict(arrowstyle="->",color=CORE))
b.annotate("Outer rim\ncharge · 2π · g = 2",xy=(2,0),xytext=(2.55,-0.95),fontsize=10,color=RIM,ha="center",
           arrowprops=dict(arrowstyle="->",color=RIM))
b.text(0,-2.25,"Axis of rotation",ha="center",fontsize=9,color="#64748b")
b.set_xlim(-2.6,3.3); b.set_ylim(-2.4,2.0); b.axis("off")
b.set_title("Cross-section through the axis: the hourglass",fontsize=14,weight="bold")

fig.text(0.5,0.015,"Both loops move at c, have length = one Compton wavelength, and share one period.   "
         "Results: spin = ½ħ (exact) · g = 2 (exact) · g−2 ≈ α/2π (0.27% off; 2nd-order sign wrong)",
         ha="center",fontsize=10.5,color="#334155")
plt.tight_layout(rect=(0,0.04,1,1))
plt.savefig("../figures/early-internal-version.png",dpi=150)
