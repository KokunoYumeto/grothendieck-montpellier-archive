#!/usr/bin/env python3
"""Exact modular exploration of determinant ten-plane Borel ideals.

All matrix entries are reconstructed from the integral tensor.  Weight blocks
retain original row/column indices and exact modular nonzero pivot minors.
This is discovery data; a separate checker is required for final use.
"""
from pathlib import Path
from itertools import combinations
from collections import defaultdict,Counter
import argparse,json,math,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'work/root'))
from coordinate_koszul import slices,RECTS,modular_rank

def weighted_blocks(S,orientation,p):
    support,mats=slices(S,-1);m,j=len(support),len(S)
    vw=[32**(v//4)+32**(4+v%4) for v in support]
    aw=[sum(32**i for i in RECTS[q][0])+sum(32**(4+i) for i in RECTS[q][1]) for q in S]
    d=j if orientation=='A' else m
    src=list(combinations(range(d),p));dst=list(combinations(range(d),p+1));di={I:i for i,I in enumerate(dst)}
    sparse=[(h,int(u),int(v),int(M[u,v])) for h,M in enumerate(mats) for u,v in zip(*np.nonzero(M))]
    result=defaultdict(list)
    for ci,I in enumerate(src):
        if orientation=='A':
            isum=-sum(aw[h] for h in I)
            for h,u,v,z in sparse:
                if h in I:continue
                J=tuple(sorted(I+(h,)));w=isum-vw[v]
                assert w==-sum(aw[h] for h in J)+vw[u]
                result[w].append((di[J]*m+u,ci*m+v,z*(-1)**sum(i<h for i in I)))
        else:
            isum=sum(vw[u] for u in I)
            for h,u,v,z in sparse:
                if u in I:continue
                J=tuple(sorted(I+(u,)));w=isum-vw[v]
                assert w==sum(vw[u] for u in J)-aw[h]
                result[w].append((di[J]*j+h,ci*m+v,z*(-1)**sum(i<u for i in I)))
    for w,triples in sorted(result.items()):
        rows=sorted({r for r,c,v in triples});cols=sorted({c for r,c,v in triples})
        ri={r:i for i,r in enumerate(rows)};ci={c:i for i,c in enumerate(cols)}
        mat=np.zeros((len(rows),len(cols)),dtype=np.int64)
        for r,c,v in triples:mat[ri[r],ci[c]]=v
        yield w,rows,cols,mat

def certificate(S,o,p):
    support,_=slices(S,-1);d=len(S) if o=='A' else len(support)
    total=0;certs=[];largest=[0,0]
    for w,rows,cols,M in weighted_blocks(S,o,p):
        c=modular_rank(M);total+=c['rank_mod_p']
        if M.shape[0]*M.shape[1]>largest[0]*largest[1]:largest=list(M.shape)
        if c['rank_mod_p']:
            c.update(weight=w,rows=[rows[i] for i in c['rows']],cols=[cols[i] for i in c['cols']]);certs.append(c)
    cost=math.comb(d-1,p)
    return {'orientation':o,'p':p,'rank':total,'cost':cost,'bound':(total+cost-1)//cost,'largest':largest,'blocks':certs}

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--mode',choices=['A','B','A9'],default='A');pa.add_argument('--out',type=Path,required=True);args=pa.parse_args()
    source=json.loads((ROOT/'work/root/borel_7_12.json').read_text())['results'];recs=next(x['records'] for x in source if x['j']==10)
    out=[];t=time.time();cache={}
    for rec in recs:
        S=rec['subset'];m=len(rec['support']);trans=tuple(sorted(q%6*6+q//6 for q in S));key=min(tuple(S),trans)
        if key in cache:
            out.append({'subset':S,'transpose_of':list(key),'bound':cache[key]});continue
        if rec['lower_bound']>=18:
            out.append({'subset':S,'previous_bound':rec['lower_bound'],'bound':rec['lower_bound']});cache[key]=rec['lower_bound'];continue
        certs=[];best=17
        if args.mode=='A':jobs=[(S,'A',p) for p in [4,3,2,1]]
        elif args.mode=='B':jobs=[(S,'B',p) for p in sorted({max(1,int(9*m/(m+10))),min(m-2,math.ceil(9*m/(m+10)))},key=lambda p:abs(p-9*m/(m+10)))]
        else:jobs=[([q for q in S if q!=excluded],'A',4) for excluded in S]
        for subset,o,p in jobs:
            c=certificate(subset,o,p);c['restriction']=subset;certs.append(c);best=max(best,c['bound'])
            print(S,'m',m,'restriction',len(subset),o,p,'rank',c['rank'],'cost',c['cost'],'bound',c['bound'],'time',round(time.time()-t,2),flush=True)
            if best>=18:break
        cache[key]=best;out.append({'subset':S,'support':m,'bound':best,'certificates':certs})
        args.out.write_text(json.dumps({'mode':args.mode,'seconds':time.time()-t,'records':out},indent=2)+'\n')
    args.out.write_text(json.dumps({'mode':args.mode,'seconds':time.time()-t,'records':out},indent=2)+'\n')
    print('DONE',Counter(r['bound'] for r in out),time.time()-t,flush=True)

if __name__=='__main__':main()
