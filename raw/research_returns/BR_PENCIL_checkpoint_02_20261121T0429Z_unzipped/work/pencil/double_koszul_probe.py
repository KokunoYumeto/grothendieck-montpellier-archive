#!/usr/bin/env python3
"""Two exterior factors, one contracted factor, with torus block ranks."""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import argparse,math,json,time
import numpy as np
from det7_prolongation import data,quad_weight,var_weight,rank

def probe(S,p,q):
    variables,T,_,_=data(S,-1);a,b,_=T.shape
    aw=[-sum((32**i)*e for i,e in enumerate(quad_weight(z))) for z in S]
    bw=[sum((32**i)*e for i,e in enumerate(var_weight(z))) for z in variables]
    ai=list(combinations(range(a),p));aj=list(combinations(range(a),p+1));aix={I:i for i,I in enumerate(aj)}
    bi=list(combinations(range(b),q));bj=list(combinations(range(b),q+1));bix={I:i for i,I in enumerate(bj)}
    sparse=[(int(i),int(j),int(k),int(T[i,j,k])) for i,j,k in zip(*np.nonzero(T))]
    groups=defaultdict(list)
    for ii,I in enumerate(ai):
        for jj,J in enumerate(bi):
            base=sum(aw[i] for i in I)+sum(bw[j] for j in J)
            for i,j,k,c in sparse:
                if i in I or j in J:continue
                A=tuple(sorted(I+(i,)));B=tuple(sorted(J+(j,)))
                w=base-bw[k]
                assert w==sum(aw[i] for i in A)+sum(bw[j] for j in B)
                groups[w].append((aix[A]*len(bj)+bix[B],(ii*len(bi)+jj)*b+k,c*(-1)**(sum(x<i for x in I)+sum(x<j for x in J))))
    total=0;largest=0
    for w,triples in groups.items():
        rows=sorted({x for x,y,c in triples});cols=sorted({y for x,y,c in triples});ri={r:i for i,r in enumerate(rows)};ci={c:i for i,c in enumerate(cols)}
        M=np.zeros((len(rows),len(cols)),dtype=np.int64)
        for x,y,c in triples:M[ri[x],ci[y]]=c
        total+=rank(M)[0];largest=max(largest,len(rows)*len(cols))
    cost=math.comb(a-1,p)*math.comb(b-1,q)
    return {'subset':S,'support':b,'p':p,'q':q,'rank_mod_p':total,'cost':cost,'bound':(total+cost-1)//cost,'blocks':len(groups),'largest_size':largest}

if __name__=='__main__':
    pa=argparse.ArgumentParser();pa.add_argument('--subset',type=int,nargs='+',required=True);pa.add_argument('--p',type=int,required=True);pa.add_argument('--q',type=int,required=True);args=pa.parse_args()
    t=time.time();print(json.dumps(probe(args.subset,args.p,args.q)));print('seconds',time.time()-t)
