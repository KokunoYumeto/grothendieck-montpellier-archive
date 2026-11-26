"""Draw the six central sheets after length-three paths have been contracted."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle


colors = ("#14688a", "#b3471e")
fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.2))
for ax in axes:
    ax.set_aspect("equal")
    ax.set_xlim(-0.6, 5)
    ax.set_ylim(-0.65, 2.05)
    ax.axis("off")


def labels(ax, pts):
    for i, (x, y) in enumerate(pts):
        ax.add_patch(Circle((x, y), .14, facecolor="white", edgecolor="#20252c", lw=1.3, zorder=3))
        ax.text(x, y, str(i), ha="center", va="center", fontsize=10, zorder=4)


def loop(ax, x, y, color, direction):
    ax.add_patch(Arc((x+.22*direction, y+.13), .49,.36, angle=direction*20,
                     theta1=0, theta2=360, color=colors[color], lw=2))


def edge(ax, pts, i, j, color, offset=0):
    ax.plot([pts[i][0]+offset, pts[j][0]+offset],
            [pts[i][1], pts[j][1]], lw=2.7, color=colors[color], solid_capstyle="round")


ax = axes[0]
ax.set_title("X   Regular orbit and two fixed sheets", fontsize=12, loc="left")
pts = [(0, .05), (1.45,.05), (0,1.45), (1.45,1.45), (3.15,.05), (3.15,1.45)]
for i, j in ((0,1),(2,3)): edge(ax,pts,i,j,0)
for i, j in ((0,2),(1,3)): edge(ax,pts,i,j,1)
for i in (4,5):
    for color, direction in ((0,-1),(1,1)): loop(ax,*pts[i],color,direction)
labels(ax,pts)

ax = axes[1]
ax.set_title("Y   Three two-sheet orbits", fontsize=12, loc="left")
pts = [(x,y) for x in (0.2,2,3.8) for y in (.05,1.45)]
edge(ax,pts,0,1,1)
edge(ax,pts,2,3,0)
edge(ax,pts,4,5,0,-.055)
edge(ax,pts,4,5,1,.055)
for i,color in ((0,0),(1,0),(2,1),(3,1)): loop(ax,*pts[i],color,-1 if color==0 else 1)
labels(ax,pts)
fig.text(.1,.13,"a",color=colors[0],fontweight="bold",fontsize=13)
fig.text(.13,.13,"and",fontsize=11)
fig.text(.18,.13,"b",color=colors[1],fontweight="bold",fontsize=13)
fig.text(.205,.13,"are the two triangle transports.",fontsize=11)
fig.text(.1,.04,"A link represents two lifted paths. A loop represents one. Each path has three edges.",fontsize=11)
fig.subplots_adjust(left=.055,right=.99,top=.86,bottom=.21,wspace=.08)
fig.savefig(Path(__file__).with_name("six_sheets.png"), dpi=165, bbox_inches="tight")
