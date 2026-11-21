#!/usr/bin/env python3
"""Direct E0-valued K(0,5) tests, with exact marked pair transport.

The source presentation is Lochak--Schneps (1997), printed p.578.
This is an exploratory necessary test, not a claim of a GT lift.
"""
from pathlib import Path
import json, sys, time
import numpy as np

WORK=Path(__file__).resolve().parents[1]
CHAR=WORK/'agents/characters'; PENT=WORK/'agents/pentagon'
sys.path.insert(0,str(WORK/'agents/five_level_six'))
from hurwitz_last_coordinate import same, inv as winv, comm

def main():
    start=time.monotonic()
    # Verify the transcription against the exact standard B4 marking.
    words=[(1,1),(2,2),(3,3),(1,2,1)*2,(2,3,2)*2]
    for i in range(5): assert same(comm(words[i],words[(i+2)%5]),(),4)
    rel=[5,-2,1,-3,2,-4,3,-5,4,-1]
    rword=sum((words[i-1] if i>0 else winv(words[-i-1]) for i in rel),())
    assert same(rword,(),4)
    data=np.load(CHAR/'records/affine216_marked_pair_kernels.npz')
    meta=json.loads((CHAR/'records/affine216_marked_pair_kernels.json').read_text())
    mt,iv,pk,els=[data[k]for k in ('multiplication','inverse','pair_kernel','elements')]
    index={tuple(map(int,e)):i for i,e in enumerate(els)};one=index[(0,0,1,0,0,1)]
    cubic=tuple(map(int,data['cubic_pair']))
    def mul(seq):
        q=one
        for z in seq:q=int(mt[q,z])
        return q
    cache={}
    def trans(a,b):
        if (a,b)not in cache:
            k=int(pk[a,b]);todo=[one];seen={one}
            for g in todo:
                for h in(a,b):
                    u=int(mt[g,h])
                    if u not in seen:seen.add(u);todo.append(u)
            can=data[f'kernel_{k}_members'];assert len(can)==len(todo)
            fwd=np.full(216,-1,dtype=int);fwd[can]=todo
            cache[a,b]=(k,fwd)
        return cache[a,b]
    def evaluate(a,b,table):
        k,fwd=trans(a,b)
        if k not in table:return None
        v=int(fwd[table[k]]);assert v>=0
        return v
    tables=json.loads((PENT/'hurwitz_colored_last_commonword.json').read_text())['cases']
    kids=list(map(int,np.load(PENT/'hurwitz_colored_last_commonword.npz')['kernel_ids']))
    assignments=[dict(zip(kids,t['values']))for t in tables]
    for d in assignments:
        assert evaluate(*cubic,d)==index[(1,1,1,0,0,1)]
    a,b=cubic
    ca=np.flatnonzero(mt[a,:]==mt[:,a]);cb=np.flatnonzero(mt[b,:]==mt[:,b])
    dab=np.intersect1d(ca,cb);assert list(dab)==[one]
    ap,bp=[one],[one]
    for j in range(1,6):ap.append(int(mt[ap[-1],a]));bp.append(int(mt[bp[-1],b]))
    assert len(set(ap))==len(set(bp))==6 and mt[ap[-1],a]==mt[bp[-1],b]==one
    assert set(map(int,ca))==set(ap) and set(map(int,cb))==set(bp)
    cross_commuting=[[i,j]for i in range(6)for j in range(6)if mt[ap[i],bp[j]]==mt[bp[j],ap[i]]]
    assert cross_commuting==[[i,j]for i in range(6)for j in range(6)if i==0 or j==0]
    rows=[]
    for c in ca:
        for e in cb:
            c,e=int(c),int(e);d=one
            if mt[c,e]!=mt[e,c]:continue
            xs=[a,b,c,d,e]
            if mul([xs[i-1]if i>0 else int(iv[xs[-i-1]])for i in rel])!=one:continue
            # LS1997 definition (III): f34,45 f51,12 f23,34 f45,51 f12,23.
            pairs=[(c,d),(e,a),(b,c),(d,e),(a,b)]
            kernels=[int(pk[x,y])for x,y in pairs]
            outcomes=[]
            for table in assignments:
                vals=[one if mt[x,y]==mt[y,x]else evaluate(x,y,table)for x,y in pairs]
                outcomes.append(None if None in vals else mul(vals)==one)
            rows.append({'tuple':xs,'kernels':kernels,'outcomes':outcomes})
    assert sorted(r['tuple']for r in rows)==sorted([[a,b,one,one,b],[a,b,a,one,one]])
    out={'source':'Lochak--Schneps1997 printed p.578 K(0,5) presentation; p.572 definition III',
         'exact_B4_presentation_replay':'PASS','first_pair':list(cubic),
         'centralizer_orders':[len(ca),len(cb)],'homomorphisms':len(rows),
         'commuting_power_exponents':cross_commuting,
         'case_labels':[t['assembly']for t in tables],'cases':rows,
         'elapsed_seconds':time.monotonic()-start,
         'scope':'All E0-valued pure pentagon homomorphisms with prescribed cubic first pair; unassigned evaluations remain open.'}
    (WORK/'records/affine216_pure_pentagon_probe.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
