import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
R=r=1.0
ELEC="#dc2626"; MAG="#2563eb"; WAIST="#16a34a"; SURF="#94a3b8"
fig=plt.figure(figsize=(15,6.6),facecolor="white")
ax=fig.add_subplot(1,2,1,projection="3d")
u,v=np.meshgrid(np.linspace(0,2*np.pi,90),np.linspace(0,2*np.pi,60))
ax.plot_surface((R+r*np.cos(v))*np.cos(u),(R+r*np.cos(v))*np.sin(u),r*np.sin(v),color=SURF,alpha=0.10,linewidth=0,shade=False)
t=np.linspace(0,2*np.pi,400)
# electric: toroidal circles (around the main axis), at several positions on the surface
for i,vv in enumerate([0,np.pi/3,-np.pi/3,2*np.pi/3,-2*np.pi/3]):
    rad=R+r*np.cos(vv); z=r*np.sin(vv)
    ax.plot(rad*np.cos(t),rad*np.sin(t),z+0*t,color=ELEC,lw=2.2 if vv==0 else 1.4,alpha=1 if vv==0 else 0.75,
            label="Electric: circulates around the axis (toroidal)" if i==0 else None)
    a=0.35+i*0.9; ax.quiver(rad*np.cos(a),rad*np.sin(a),z,-np.sin(a)*0.45,np.cos(a)*0.45,0,color=ELEC,lw=2,arrow_length_ratio=0.5)
# magnetic: poloidal loops (around the tube, all threading the waist)
for i,uu in enumerate(np.linspace(0,2*np.pi,8,endpoint=False)):
    X=(R+r*np.cos(t))*np.cos(uu);Y=(R+r*np.cos(t))*np.sin(uu);Z=r*np.sin(t)
    ax.plot(X,Y,Z,color=MAG,lw=1.6,alpha=0.85,label="Magnetic: loops through the waist (poloidal) = hourglass" if i==0 else None)
    k=np.pi/2   # arrow at top of tube, pointing inward (field goes down through waist? -> up through waist, out & down outside)
    p=np.array([(R+r*np.cos(k))*np.cos(uu),(R+r*np.cos(k))*np.sin(uu),r*np.sin(k)])
    d=np.array([r*np.sin(k)*np.cos(uu),r*np.sin(k)*np.sin(uu),-r*np.cos(k)])
    ax.quiver(*p,*(d*0.45),color=MAG,lw=2,arrow_length_ratio=0.5)
ax.plot([0,0],[0,0],[-1.6,1.6],color=MAG,lw=2.5)
ax.quiver(0,0,1.1,0,0,0.5,color=MAG,lw=2.5,arrow_length_ratio=0.4)
ax.scatter([0],[0],[0],color=WAIST,s=90,depthshade=False,label="Waist: every magnetic loop passes through here")
ax.set_box_aspect((1,1,0.62)); ax.view_init(elev=24,azim=-60); ax.set_axis_off()
ax.set_title("External torus: electric at 90° to magnetic",fontsize=14,weight="bold")
ax.legend(loc="lower center",bbox_to_anchor=(0.5,-0.1),frameon=False,fontsize=10)

b=fig.add_subplot(1,2,2); b.set_aspect("equal")
s=np.linspace(0,2*np.pi,300)
for sx in (-1,1):
    b.fill(sx*R+r*np.cos(s),r*np.sin(s),color=SURF,alpha=0.12)
    b.plot(sx*R+r*np.cos(s),r*np.sin(s),color=MAG,lw=2.5)
    # magnetic arrows: up through waist, out over the top, down the outside, back in underneath
    for a in (np.pi/2,0.0,3*np.pi/2,np.pi*0.75,np.pi*1.25):
        x=sx*(R+r*np.cos(a)); y=r*np.sin(a)
        dx,dy=sx*np.sin(a),-np.cos(a)
        b.annotate("",xy=(x+0.06*dx,y+0.06*dy),xytext=(x-0.2*dx,y-0.2*dy),
                   arrowprops=dict(arrowstyle="-|>",color=MAG,lw=2,mutation_scale=18))
    # electric: toroidal flow crosses the page, out on right, in on left
    sym="⊙" if sx>0 else "⊗"
    for vv in np.linspace(0,2*np.pi,8,endpoint=False):
        b.text(sx*R+r*np.cos(vv),r*np.sin(vv),sym,color=ELEC,ha="center",va="center",fontsize=15,weight="bold")
b.plot([0,0],[-1.5,1.5],color=MAG,lw=2.5); b.annotate("",xy=(0,1.7),xytext=(0,1.3),arrowprops=dict(arrowstyle="-|>",color=MAG,lw=2.5,mutation_scale=20))
b.scatter([0],[0],s=220,color=WAIST,zorder=6)
b.annotate("Waist: all magnetic flux\npasses through one point",xy=(0,0),xytext=(-2.1,1.75),fontsize=10,color=WAIST,ha="center",
           arrowprops=dict(arrowstyle="->",color=WAIST))
b.text(2.45,1.2,"Magnetic (blue)\nloops around each lobe:\nthe hourglass",color=MAG,fontsize=10,ha="center")
b.text(2.45,-1.35,"Electric (red)\n⊙ out of page, ⊗ into page:\ncirculates around the axis",color=ELEC,fontsize=10,ha="center")
b.set_xlim(-3.1,3.5); b.set_ylim(-2.1,2.2); b.axis("off")
b.set_title("Cross-section: magnetic hourglass, electric through the page",fontsize=14,weight="bold")
fig.text(0.5,0.015,"Electric and magnetic cross at 90° at every point on the surface, as in a light wave. "
         "Same field shape as a current loop: the circulating charge makes magnetic loops that thread the centre.",
         ha="center",fontsize=10.5,color="#334155")
plt.tight_layout(rect=(0,0.04,1,1)); plt.savefig("../figures/horn_torus_EM.png",dpi=150)
