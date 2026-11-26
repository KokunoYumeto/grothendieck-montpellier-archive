#!/usr/bin/env python3
"""Original vector figure for the paper. Requires matplotlib.

python draw_wire_networks.py --output ../papers/wire_geometry/wire_networks.pdf
"""
import argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ap=argparse.ArgumentParser()
ap.add_argument('--output',required=True)
args=ap.parse_args()
plt.rcParams.update({'font.family':'serif','font.size':11,'pdf.fonttype':42})
fig,axes=plt.subplots(1,2,figsize=(6.9,2.6))
corners=[(-1,1),(1,1),(1,-1),(-1,-1)]
for ax in axes:
    ax.set_aspect('equal');ax.set_xlim(-1.45,1.45);ax.set_ylim(-1.4,1.55);ax.axis('off')
    for i,(x,y) in enumerate(corners):
        ax.plot(x,y,'o',color='#101010',markersize=5,zorder=4)
        ax.text(x*1.18,y*1.18,str(i+1),ha='center',va='center')
    ax.plot([-1,1,1,-1,-1],[1,1,-1,-1,1],color='#aaaaaa',lw=.7,ls=(0,(2,3)),zorder=0)
for a,b in [(0,2),(1,3)]:
    axes[0].plot([corners[a][0],corners[b][0]],[corners[a][1],corners[b][1]],color='#153c5b',lw=1.7)
axes[0].text(-.77,.05,'$m$',ha='center')
axes[0].text(.77,.05,'$m$',ha='center')
axes[0].text(0,1.53,'Crossing wires',ha='center',va='top',fontsize=12)
for ids,hub in [([0,1],(0,.42)),([2,3],(0,-.42))]:
    for i in ids:
        axes[1].plot([corners[i][0],hub[0]],[corners[i][1],hub[1]],color='#153c5b',lw=1.7)
    axes[1].plot(*hub,'o',markerfacecolor='white',markeredgecolor='#101010',markersize=6,zorder=4)
axes[1].plot([0,0],[-.42,.42],color='#8c3d2b',lw=2)
axes[1].text(.14,0,'$h$',va='center')
for x,y in [(-.58,.86),(.58,.86),(-.58,-.94),(.58,-.94)]:
    axes[1].text(x,y,'$m$',ha='center')
axes[1].text(0,1.53,'A two-hub alternative',ha='center',va='top',fontsize=12)
fig.subplots_adjust(left=.03,right=.97,bottom=.02,top=.98,wspace=.24)
out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,bbox_inches='tight',pad_inches=.03,metadata={'Title':'Crossing wires and a two-hub alternative','Author':''})
plt.close(fig)
