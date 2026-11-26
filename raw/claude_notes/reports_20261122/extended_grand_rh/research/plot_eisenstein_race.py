"""Render the exact finite Eisenstein lattice sample used in the workshop."""
from importlib.util import module_from_spec, spec_from_file_location
from math import isqrt, sqrt
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle


base = Path(__file__).resolve().parent
spec = spec_from_file_location("slopes", base / "machine69/check_eisenstein_slopes.py")
slopes = module_from_spec(spec)
spec.loader.exec_module(slopes)
norm_limit = 67

def good_split_prime(n):
    return n > 1 and n % 3 == 1 and all(n % j for j in range(2, isqrt(n) + 1))

points = []
for a in range(-10, 11):
    for b in range(-10, 11):
        n = slopes.norm(a, b)
        if 0 < n <= norm_limit:
            is_cube = slopes.power((a, b), (269**2 - 1) // 3) == (1, 0)
            points.append((a - b/2, b*sqrt(3)/2, is_cube, good_split_prime(n)))

fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.8), layout="constrained")
colors = {True: "#005c77", False: "#ad452b"}
for index, (ax, title) in enumerate(zip(axes, ["All nonzero Eisenstein integers", "Only split prime norms"])):
    ax.add_patch(Circle((0, 0), sqrt(norm_limit), facecolor="none", edgecolor="#89939b", lw=.8))
    for cube in [False, True]:
        subset = [(x,y) for x,y,c,prime in points if c == cube and (index == 0 or prime)]
        xs, ys = zip(*subset)
        ax.scatter(xs, ys, color=colors[cube], marker="o" if cube else "x",
                   s=16 if cube else 18, linewidths=.9, zorder=3)
    if index:
        excluded = [(x,y) for x,y,_,prime in points if not prime]
        ax.scatter(*zip(*excluded), s=5, color="#c7cacc", zorder=1)
    ax.set_title(title, fontsize=12)
    ax.set(xlim=(-9,9), ylim=(-9,9), aspect="equal", xlabel="Real part")
    ax.spines[["top","right"]].set_visible(False)
    ax.spines[["left","bottom"]].set_color("#adb4ba")
    ax.set_xticks([-8,-4,0,4,8])
    ax.set_yticks([-8,-4,0,4,8])
axes[0].set_ylabel("Imaginary part")
for n,xy,text in [(13,(3.5,sqrt(3)/2),(6.25,-2.6)), (37,(5.5,3*sqrt(3)/2),(5.25,7.6))]:
    axes[1].annotate(f"norm {n}",xy=xy,xytext=text,ha="center",fontsize=9,zorder=4,
                     bbox=dict(boxstyle="round,pad=.2",facecolor="white",edgecolor="none"),
                     arrowprops=dict(arrowstyle="->",color="#272e32",lw=.9,shrinkB=3))
legend = [Line2D([0],[0],marker=mark,ls="",color=color,label=label)
          for mark,color,label in [("o",colors[True],"Cubic weight +2"),("x",colors[False],"Cubic weight −1"),
                                   (".","#aeb5b9","Excluded norm")]]
fig.legend(handles=legend,loc="outside lower center",ncols=3,frameon=False)
fig.savefig(base/"eisenstein_norms.png",dpi=160,facecolor="white")
