"""Finite projected boundary-jet certificate at a central Jacobi cut.

The proposed uniform insertion proof is separate from this finite check.
"""
import json
import sys
from pathlib import Path
import numpy as np
from check_jacobi_repair import build
from check_border_first_order_rank import kernel,rref

def profile(C0,C1,C2,p):
    K,r0=kernel(C0,p);left,_=kernel(C0.T,p);N=left.T@C1@K%p
    residual,r1=kernel(N,p);k0=K@residual%p;rhs=-C1@k0%p
    augmented,pivots=rref(np.concatenate((C0,rhs),axis=1),p)
    assert len(pivots)==r0 and max(pivots)<C0.shape[1]
    k1=np.zeros((C0.shape[1],residual.shape[1]),dtype=np.int64);k1[pivots]=augmented[:r0,C0.shape[1]:]
    assert not np.any((C0@k1+C1@k0)%p)
    N2=left.T@(C2@k0+C1@k1)%p
    total=len(rref(np.concatenate((N,N2),axis=1),p)[1])
    return {'rank0':r0,'kernel0':K.shape[1],'gain1':r1,'gain2':total-r1,'final_rank_lower_bound':r0+total},(K,left,N,k0,k1,N2)

def main():
    m=int(sys.argv[1]);directory=Path(sys.argv[2]);data=json.loads((directory/f'jacobi_repair_m{m}.json').read_text());p=data['prime'];alpha=data['alpha'];delta=data['delta'];cut=m//2;window=5
    base=np.array([[1,0,0],[0,1,0],[1,0,0],[0,0,1]],dtype=np.int64);change=np.array(data['combined_change'],dtype=np.int64)
    ordinary,monos=build(m,alpha,delta,base,p);weights=np.array([b-c for a,b,c in monos]);chars=weights%m
    allowed=set(range(window+1))|set(range(m-window,m))
    rows=[i for i,c in enumerate(chars) if c in allowed];columns=[]
    for c in range(ordinary.shape[1]):
        cs=set(chars[np.flatnonzero(ordinary[:,c])]);assert len(cs)==1
        if next(iter(cs)) in allowed:columns.append(c)
    d0=delta.copy();d0[cut]=0;d1=delta.copy();d1[cut]=1
    product=1
    for d in d1:product=product*d%p
    inverse=pow(product,-1,p)
    negative=[i for i,w in enumerate(weights) if -m-window<=w<=-m+window]
    def boundary(forms):
        C,_=build(m,alpha,d0,forms,p);Cnonzero,_=build(m,alpha,d1,forms,p)
        C[negative,:]=Cnonzero[negative,:]*inverse%p
        return C[np.ix_(rows,columns)]
    values=[boundary((base+t*change)%p) for t in range(4)]
    w1=[-11*pow(6,-1,p)%p,3,-3*pow(2,-1,p)%p,pow(3,-1,p)]
    w2=[1,-5*pow(2,-1,p)%p,2,-pow(2,-1,p)%p]
    C0=values[0];C1=sum(w*C for w,C in zip(w1,values))%p;C2=sum(w*C for w,C in zip(w2,values))%p
    result,arrays=profile(C0,C1,C2,p)
    result.update({'m':m,'prime':p,'cut_edge':cut,'window':window,'rows':rows,'columns':columns,'alpha':alpha,'delta_with_zero_cut':d0,'change':change.tolist(),'rank_at_one':len(rref(values[1],p)[1])})
    stem=directory/f'jacobi_boundary_repair_m{m}';stem.with_suffix('.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
    np.savez(str(stem)+'.npz',C0=C0,C1=C1,C2=C2,kernel=arrays[0],left=arrays[1],normal1=arrays[2],kernel2=arrays[3],lift1=arrays[4],normal2=arrays[5],rows=np.array(rows),columns=np.array(columns),monomials=np.array(monos)[rows])
    print({k:v for k,v in result.items() if k not in ['rows','columns','alpha','delta_with_zero_cut']})

if __name__=='__main__':main()
