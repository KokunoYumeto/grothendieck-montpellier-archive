#!/usr/bin/env python3
"""Explore the stronger seven-plane lower bounds inside the P20 ten-plane."""
from pathlib import Path
from itertools import combinations
import sys,json,time,math

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'work/pencil'))
import det10_koszul_probe as k

def main():
    original=k.slices;k.slices=lambda S,sign:original(S,1)
    full=[0,1,2,3,4,6,7,8,9,10];start=time.time();out=[]
    for z,S in enumerate(combinations(full,7)):
        m=len(k.slices(S,1)[0]);certs=[];bound=max(14,m)
        for o,p in [('A',3),('B',round(6*m/(m+7)))]:
            if bound>=15:break
            c=k.certificate(S,o,p);certs.append(c);bound=max(bound,c['bound'])
        out.append({'subset':list(S),'support':m,'bound':bound,'certificates':certs})
        if z%10==9:print('done',z+1,'weak',sum(r['bound']<15 for r in out),'seconds',round(time.time()-start,3),flush=True)
    path=Path(__file__).with_name('per10_hereditary_probe.json')
    path.write_text(json.dumps({'full_subset':full,'records':out,'scope':'Exploration; exact modular pivot data have not been independently replayed.'},indent=2)+'\n')
    print('unresolved',[r['subset'] for r in out if r['bound']<15],flush=True)

if __name__=='__main__':main()
