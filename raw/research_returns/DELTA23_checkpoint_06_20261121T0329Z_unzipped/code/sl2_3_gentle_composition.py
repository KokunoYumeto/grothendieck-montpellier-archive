#!/usr/bin/env python3
"""GT composition and actual inversion on the four normalized SL2 residues."""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
WORK=Path(__file__).resolve().parents[1];R=WORK/'agents/characters/records'

def main():
    start=time.monotonic();data=np.load(R/'affine216_marked_pair_kernels.npz');meta=json.loads((R/'affine216_marked_pair_kernels.json').read_text())
    mt,iv,pk,els=[data[k]for k in ('multiplication','inverse','pair_kernel','elements')]
    one=6;core=np.load(WORK/'records/sl2_3_gentle_core.npz');kids=list(map(int,core['kernel_ids']));vals=core['survivors'];loc={k:j for j,k in enumerate(kids)}
    lookup={v.tobytes():j for j,v in enumerate(vals)};cache={}
    def mapping(a,b):
        key=int(a),int(b)
        if key not in cache:
            k=int(pk[a,b]);todo=[one];seen={one}
            for g in todo:
                for h in(a,b):
                    q=int(mt[g,h])
                    if q not in seen:seen.add(q);todo.append(q)
            fwd=np.full(216,-1,dtype=int);fwd[data[f'kernel_{k}_members']]=todo
            cache[key]=(loc[k],fwd)
        return cache[key]
    def ev(row,a,b):
        k,fwd=mapping(a,b);q=int(fwd[row[k]]);assert q>=0;return q
    table=[];inversion=[]
    for i,f in enumerate(vals):
        line=[]
        for g in vals:
            value=[]
            for j,k in enumerate(kids):
                a,b=meta['kernels'][k]['pair'];bf=int(mt[mt[iv[f[j]],b],f[j]])
                value.append(int(mt[f[j],ev(g,a,bf)]))
            v=np.array(value,dtype=np.int16);assert v.tobytes()in lookup;line.append(lookup[v.tobytes()])
        table.append(line)
        v=np.array([ev(f,int(iv[meta['kernels'][k]['pair'][0]]),int(iv[meta['kernels'][k]['pair'][1]]))for k in kids],dtype=np.int16)
        assert v.tobytes()in lookup;inversion.append(lookup[v.tobytes()])
    out={'composition':table,'complex_conjugation':inversion,'cube':[table[table[j][j]][j]for j in range(4)],
         'elapsed_seconds':time.monotonic()-start,'scope':'Exact finite GT multiplication on the four necessary normalized SL2 value tables. No actual lift asserted.'}
    (WORK/'records/sl2_3_gentle_composition.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
