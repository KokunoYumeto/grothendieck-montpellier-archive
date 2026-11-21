"""Explore iterated coordinate substitutions for tight coordinate tensors.

The original minor-index factor has weight minus the sum of the row and
column weights; the two variable factors have their ordinary weights.
All three are multiplicity-free. Thus any coordinate restriction retains
a diagonal stabilizer and the torus reduction applies at each node.
"""
from functools import lru_cache
from collections import Counter
from pathlib import Path
import sys,time,json,argparse,math
import numpy as np
from coordinate_koszul import slices,koszul,modular_rank

def main():
    pa=argparse.ArgumentParser()
    pa.add_argument('--j',type=int,choices=[5,6],required=True)
    pa.add_argument('--family',choices=['det','per'],default='per')
    pa.add_argument('--target',type=int,required=True)
    pa.add_argument('--koszul',action='store_true')
    pa.add_argument('--out',type=Path,required=True)
    args=pa.parse_args()
    s=[0,1,3,6,7]+([9] if args.j==6 else [])
    sup,mats=slices(s,-1 if args.family=='det' else 1)
    tensor=np.array(mats)
    entries=[tuple(map(int,x))+(int(tensor[tuple(x)]),) for x in np.argwhere(tensor)]
    counts=Counter();start=time.time();witness={}
    def norm(state):
        a,b,c=state
        es=[e for e in entries if a>>e[0]&1 and b>>e[1]&1 and c>>e[2]&1]
        masks=tuple(sum(1<<i for i in {e[k] for e in es}) for k in range(3))
        if masks[1]>masks[2]:masks=(masks[0],masks[2],masks[1])
        return masks
    @lru_cache(None)
    def decide(state,target):
        counts['states']+=1
        dims=[x.bit_count() for x in state]
        if max(dims)>=target:
            counts['flattening_pass']+=1;return True
        if min(dims)<=2:
            counts['pencil_stop']+=1;return False
        es=[e for e in entries if all(state[k]>>e[k]&1 for k in range(3))]
        verts=[[i for i in range(tensor.shape[k]) if state[k]>>i&1] for k in range(3)]
        if args.koszul:
            restricted=tensor[np.ix_(*verts)]
            for factor in sorted(range(3),key=lambda f:dims[f]):
                a=dims[factor]
                order=[factor]+[k for k in range(3) if k!=factor]
                mm=restricted.transpose(order)
                for p in range(1,a):
                    if p>3 and a-p-1>3:continue
                    cost=math.comb(a-1,p)
                    cap=min(math.comb(a,p)*mm.shape[2],math.comb(a,p+1)*mm.shape[1])
                    if cap<cost*(target-1)+1:continue
                    mat=koszul(mm,p)
                    cert=modular_rank(mat)
                    if cert['rank_mod_p']>cost*(target-1):
                        counts['koszul_pass']+=1
                        witness[str((state,target))]={'type':'koszul','factor':factor,'p':p,'cost':cost,'certificate':cert}
                        return True
        for factor in sorted(range(3),key=lambda f:-dims[f]):
            degrees=Counter(e[factor] for e in es)
            candidates=sorted(verts[factor],key=lambda v:(degrees[v],v))
            ok=True;children=[]
            for v in candidates:
                new=list(state);new[factor]&=~(1<<v);new=norm(tuple(new))
                if not decide(new,target-1):
                    ok=False;break
                children.append([list(new),target-1])
            if ok:
                counts['substitution_pass']+=1
                witness[str((state,target))]={'type':'substitution','factor':factor,'children':children}
                return True
        counts['failed']+=1
        return False
    full=tuple((1<<d)-1 for d in tensor.shape)
    result=decide(full,args.target)
    out={'family':args.family,'j':args.j,'subset':s,'target':args.target,'success':result,'koszul_enabled':args.koszul,'counts':dict(counts),'seconds':time.time()-start,'witnesses':witness}
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='witnesses'},indent=2),flush=True)

if __name__=='__main__':main()
