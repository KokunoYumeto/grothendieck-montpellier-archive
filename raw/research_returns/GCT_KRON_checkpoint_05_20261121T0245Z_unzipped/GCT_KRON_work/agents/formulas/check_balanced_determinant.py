#!/usr/bin/env python3
"""Exact small-instance certificates for root's M-006 balanced two-trie determinant.
This is additional verification of the cycle-cover proof, not a proof for all m,r.
"""
from itertools import product
from math import comb
from pathlib import Path
import json,time
import sympy as s

def exponents(k,degree):
    if k==0:return [()]
    return [a for a in product(range(degree+1),repeat=k) if sum(a)<=degree]

def monomial(xx,alpha):
    return s.prod(v**a for v,a in zip(xx,alpha))

def construct(m,r,symbolic_coefficients=False):
    k=r-1;p=k//2;q=k-p
    vv=s.symbols('x1:'+str(r));L=s.Symbol('L')
    px=exponents(p,m);qy=exponents(q,m)
    zpx=(0,)*p;zqy=(0,)*q
    # The two root vertices are the same central vertex0.
    prefix={zpx:0};suffix={zqy:0};idx=1
    for alpha in px:
        if alpha!=zpx:prefix[alpha]=idx;idx+=1
    for beta in qy:
        if beta!=zqy:suffix[beta]=idx;idx+=1
    S=comb(m+p,p)+comb(m+q,q)-1
    assert idx==S
    A=s.zeros(S,S)
    for i in range(1,S):A[i,i]=L
    # Unique sorted prefix path: remove greatest-index variable for parent.
    for alpha,aidx in prefix.items():
        if aidx==0:continue
        j=max(i for i,v in enumerate(alpha) if v)
        par=list(alpha);par[j]-=1
        A[prefix[tuple(par)],aidx]-=vv[j]
    # Reversed tree: each beta has a unique path to its zero root.
    for beta,bidx in suffix.items():
        if bidx==0:continue
        j=max(i for i,v in enumerate(beta) if v)
        par=list(beta);par[j]-=1
        A[bidx,suffix[tuple(par)]]-=vv[p+j]
    f=0;cn=0
    for alpha in px:
      for beta in qy:
        deg=sum(alpha)+sum(beta)
        if deg>m:continue
        cn+=1
        coeff=s.Symbol('c'+str(cn)) if symbolic_coefficients else ((cn*cn+7*cn+3)%17-8)
        A[prefix[alpha],suffix[beta]]+=coeff*L
        f+=coeff*monomial(vv[:p],alpha)*monomial(vv[p:],beta)*L**(m-deg)
    assert cn==comb(m+r-1,r-1)
    return A,s.expand(f),L,S,vv

def main():
    t=time.time();rows=[]
    for m,r,sc in [(1,2,True),(2,2,True),(2,3,True),(3,3,False),(2,4,False)]:
        A,f,L,S,vv=construct(m,r,sc)
        residual=s.Poly(s.expand(A.det(method='domain-ge')-L**(S-m)*f),L,*vv,*sorted(f.free_symbols-set(vv)-{L},key=str))
        assert residual.is_zero,(m,r,S,residual)
        rows.append({'m':m,'r':r,'matrix_size':S,'coefficients':'independent symbols' if sc else 'fixed signed integers','symbolic_residual':'0'})
    # Larger exact integer determinant evaluations, including L=0.
    nchecks=0
    for m,r in [(3,4),(2,5),(4,3),(4,4),(3,5)]:
        A,f,L,S,vv=construct(m,r,False)
        for trial in range(4):
            subs={L:trial-1}
            subs.update({v:((j+2)*(trial+3))%7-3 for j,v in enumerate(vv)})
            det=A.subs(subs).det(method='domain-ge')
            target=(L**(S-m)*f).subs(subs)
            assert det==target,(m,r,trial,det,target)
            nchecks+=1
        rows.append({'m':m,'r':r,'matrix_size':S,'coefficients':'fixed signed integers','exact_integer_evaluations':4})
    out={'construction':'balanced two-trie, signed variable edges, coefficient edges c_alpha_beta L','symbolic_cases':5,'integer_evaluations':nchecks,'results':rows,'elapsed_seconds':round(time.time()-t,3)}
    print(json.dumps(out,indent=2))
    Path(__file__).with_name('balanced_determinant_certificate.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
