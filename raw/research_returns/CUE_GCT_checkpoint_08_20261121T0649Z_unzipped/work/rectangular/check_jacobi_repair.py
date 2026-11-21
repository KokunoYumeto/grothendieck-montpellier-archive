"""Exact first-order endpoint repair test, using path/continuant formulas.

No untested-size maximal-rank claim is made by this script.
"""
import json
import sys
from pathlib import Path
import numpy as np
from check_border_first_order_rank import kernel, rref

UNITS=[(1,0,0),(0,1,0),(0,0,1)]

def multiply(a,b,p):
    out={}
    for ma,ca in a.items():
        for mb,cb in b.items():
            mon=tuple(ma[i]+mb[i] for i in range(3));out[mon]=(out.get(mon,0)+ca*cb)%p
    return {m:c for m,c in out.items() if c}

def build(m,alpha,delta,forms,p):
    L=m-1;D=m+1
    P={}
    for a in range(m+1):
        P[a,a-1]=[1]
        if a<m:P[a,a]=[alpha[a]]
        for b in range(a+1,m):
            v=[0]*((b-a+1)//2+1)
            for k,c in enumerate(P[a,b-1]):v[k]=(v[k]+alpha[b]*c)%p
            for k,c in enumerate(P[a,b-2]):v[k+1]=(v[k+1]+delta[b-1]*c)%p
            P[a,b]=v
    monos=[(a,b,D-a-b) for a in range(D,-1,-1) for b in range(D-a,-1,-1)]
    lookup={v:i for i,v in enumerate(monos)}
    C=np.zeros((len(monos),8*m+3),dtype=np.int64)
    u0,uL,v0,vL=[{UNITS[k]:int(c)%p for k,c in enumerate(row) if c%p} for row in forms]
    def term(col,a,b,shift,polynomial,scale=1):
        length=b-a+1
        for k,c in enumerate(P[a,b]):
            for mon,v in polynomial.items():
                out=(length-2*k+shift[0]+mon[0],k+shift[1]+mon[1],k+shift[2]+mon[2])
                C[lookup[out],col]=(C[lookup[out],col]+scale*c*v)%p
    def product(start,end):
        t=1
        for i in range(start,end):t=t*delta[i]%p
        return t
    for k,e in enumerate(UNITS):term(k,0,L,e,{(0,0,0):1})
    vv=multiply(v0,vL,p);uu=multiply(u0,uL,p)
    tv0=multiply(vv,u0,p);tvL=multiply(vv,uL,p)
    tu0=multiply(uu,v0,p);tuL=multiply(uu,vL,p)
    for i in range(m):
        pre=product(0,i);suf=product(i,L)
        for k,e in enumerate(UNITS):
            term(3+3*i+k,i+1,L,(e[0],e[1]+i,e[2]),v0)
            term(3+3*i+k,0,i-1,(e[0],e[1],e[2]+L-i),vL,suf)
            term(3+3*m+3*i+k,i+1,L,(e[0],e[1],e[2]+i),u0,pre)
            term(3+3*m+3*i+k,0,i-1,(e[0],e[1]+L-i,e[2]),uL)
        if i>0:
            term(6*m+3+i,1,i-1,(0,0,L-i),tv0,2*suf)
            term(7*m+3+i,1,i-1,(0,L-i,0),tu0,2)
        if i<L:
            term(6*m+3+i,i+1,L-1,(0,i,0),tvL,2)
            term(7*m+3+i,i+1,L-1,(0,0,i),tuL,2*pre)
    return C,monos

def next_random(s):return (1664525*s+1013904223)%(1<<32)

def main():
    m=int(sys.argv[1]);directory=Path(sys.argv[2]);p=101;s=20261121+4099*m
    alpha=[];delta=[]
    for arr,size in [(alpha,m),(delta,m-1)]:
        for i in range(size):s=next_random(s);arr.append(((s>>8)%p) or 1)
    base=np.array([[1,0,0],[0,1,0],[1,0,0],[0,0,1]],dtype=np.int64)
    C0,monos=build(m,alpha,delta,base,p);K,rank0=kernel(C0,p);left,_=kernel(C0.T,p)
    assert not np.any(left.T@C0%p)
    chars=np.array([(b-c)%m for a,b,c in monos])
    colchars=[]
    for j in range(C0.shape[1]):
        found=set(chars[np.flatnonzero(C0[:,j])]);assert len(found)==1;colchars.append(next(iter(found)))
    kerchars=[]
    for j in range(K.shape[1]):
        found={colchars[i] for i in np.flatnonzero(K[:,j])};assert len(found)==1;kerchars.append(next(iter(found)))
    leftchars=[]
    for j in range(left.shape[1]):
        found=set(chars[np.flatnonzero(left[:,j])]);assert len(found)==1;leftchars.append(next(iter(found)))
    weights=[-11*pow(6,-1,p)%p,3,-3*pow(2,-1,p)%p,pow(3,-1,p)]
    trials=[];derivatives=[]
    for e in range(4):
        for k in range(3):
            if base[e,k]:continue
            change=np.zeros((4,3),dtype=np.int64);change[e,k]=1;C1=np.zeros_like(C0)
            for t,w in enumerate(weights):C1=(C1+w*build(m,alpha,delta,(base+t*change)%p,p)[0])%p
            N=left.T@C1@K%p;rk=len(rref(N,p)[1]);derivatives.append((change,C1))
            blocks=[]
            for char in sorted(set(leftchars)):
                rows=[i for i,c in enumerate(leftchars) if c==char];v=len(rref(N[rows,:],p)[1])
                if v:blocks.append([int(char),v])
            trials.append({'endpoint':e,'added_variable':k,'normal_rank':rk,'output_character_ranks':blocks})
    change=np.zeros((4,3),dtype=np.int64);C1=np.zeros_like(C0)
    for i,(ch,der) in enumerate(derivatives):change=(change+(i+1)*ch)%p;C1=(C1+(i+1)*der)%p
    N=left.T@C1@K%p
    second_weights=[1,-5*pow(2,-1,p)%p,2,-pow(2,-1,p)%p]
    C2=np.zeros_like(C0)
    for t,w in enumerate(second_weights):C2=(C2+w*build(m,alpha,delta,(base+t*change)%p,p)[0])%p
    residual,first_rank=kernel(N,p);k0=K@residual%p;rhs=-C1@k0%p
    augmented,pivots=rref(np.concatenate((C0,rhs),axis=1),p)
    assert len(pivots)==rank0 and max(pivots)<C0.shape[1]
    k1=np.zeros((C0.shape[1],residual.shape[1]),dtype=np.int64)
    k1[pivots,:]=augmented[:rank0,C0.shape[1]:]
    assert not np.any((C0@k1+C1@k0)%p)
    N2=left.T@(C2@k0+C1@k1)%p
    total_normal=len(rref(np.concatenate((N,N2),axis=1),p)[1])
    actual_rank=len(rref(build(m,alpha,delta,(base+change)%p,p)[0],p)[1])
    out={'m':m,'prime':p,'alpha':alpha,'delta':delta,'rank_at_zero':rank0,'kernel_dimension':K.shape[1],
         'kernel_characters':kerchars,'single_direction_trials':trials,
         'combined_change':change.tolist(),'combined_normal_rank':first_rank,'corrected_second_order_gain':total_normal-first_rank,'total_normal_rank':total_normal,'rank_at_epsilon_one':actual_rank}
    directory.mkdir(parents=True,exist_ok=True);stem=directory/f'jacobi_repair_m{m}'
    stem.with_suffix('.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
    np.savez(str(stem)+'.npz',C0=C0,C1=C1,C2=C2,kernel=K,left_kernel=left,normal=N,second_normal=N2,second_kernel=k0,first_lift=k1,monomials=np.array(monos),alpha=np.array(alpha),delta=np.array(delta),change=change)
    print(json.dumps(out,indent=2,default=int))

if __name__=='__main__':main()
