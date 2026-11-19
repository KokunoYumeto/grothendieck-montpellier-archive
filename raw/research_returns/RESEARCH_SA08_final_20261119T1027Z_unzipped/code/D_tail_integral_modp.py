#!/usr/bin/env python3
"""Mod-p homology of the actual integral form-one image lattice.

This differs from taking the image over F_p: HNF is computed over Z first.
The source of the integral lattice functions is retained in the companion
program; only its definitions are executed here, not its long Smith run.
"""
from pathlib import Path
source=Path('SA08_work/code/D_tail_integral_horizontal.py').read_text()
exec(compile(source.split('\nrows=[]\n')[0], 'D_tail_integral_horizontal.py','exec'))
import numpy as np

def rank_mod(A,p):
    a=np.array(A.tolist(),dtype=np.int64)%p
    m,n=a.shape;r=0
    for j in range(n):
        piv=np.flatnonzero(a[r:,j])
        if len(piv)==0:continue
        s=int(piv[0])+r
        if s!=r:a[[r,s]]=a[[s,r]]
        a[r]=(a[r]*pow(int(a[r,j]),-1,p))%p
        for i in range(r+1,m):
            if a[i,j]:a[i]=(a[i]-a[i,j]*a[r])%p
        r+=1
        if r==m:break
    return r

rows=[]
for N,w in [(2,4),(2,5),(2,6),(2,7),(2,8),(3,6),(3,7),(3,8)]:
    ds={n:differential(w,n,N) for n in range(1,w+1)}
    for n in range(2,w+1):
        assert ds[n-1]*ds[n]==sp.zeros(ds[n-1].rows,ds[n].cols)
    for p in [2,3,5,7]:
        ranks={n:rank_mod(ds[n],p) if ds[n].rows and ds[n].cols else 0 for n in ds}
        hom={n:ds[n].cols-ranks[n]-ranks.get(n+1,0) for n in ds}
        row={'N':N,'weight':w,'p':p,'ranks':ranks,'homology':hom}
        rows.append(row);print(json.dumps(row),flush=True)
        out={'description':__doc__,'cases':rows,'elapsed_seconds':time.perf_counter()-started}
        Path('SA08_work/logs/D_tail_integral_modp.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'cases':len(rows),'elapsed_seconds':out['elapsed_seconds']}))
