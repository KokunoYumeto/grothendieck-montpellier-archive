"""Exact cyclotomic finite diagnostic for LIFT23; not a theta quotient proof."""
from itertools import product, permutations
from pathlib import Path
from math import gcd
import json
import sympy as sp

def determinant(A,q):
    n=len(A); z=0
    for p in permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=sign
        for i,j in enumerate(p):term*=A[i][j]
        z+=term
    return z%q

def cofactors(A,q):
    k=len(A[0]);r=k+1
    return tuple(determinant([A[i]+[int(i==j)] for i in range(r)],q) for j in range(r))

def root_reduce(L):
    z=sp.Symbol("z")
    poly=sp.Poly(sp.cyclotomic_poly(L,z),z)
    degree=poly.degree()
    coeff=[int(poly.nth(i)) for i in range(degree+1)]
    def reduce(arr):
        a=list(arr)+[0]*max(0,degree-len(arr))
        for j in range(len(a)-1,degree-1,-1):
            c=a[j]
            if c:
                for i in range(degree):
                    a[j-degree+i]-=c*coeff[i]
        return tuple(a[:degree])
    return reduce

def primitive(q):
    return next(g for g in range(1,q) if len({pow(g,i,q) for i in range(q-1)})==q-1)

def check_case(q,k,t,M,char_power,A_all):
    r=k+1;b=r+t;d=t+1
    mod=q**M;order=q-1
    root=primitive(q);logs={pow(root,i,q):i for i in range(order)}
    L=mod*order;red=root_reduce(L)
    add_step=order
    char_step=mod
    # chi(root)=exp(2pi i char_power/(q-1)).
    trivial=char_power%order==0
    ys=list(product(range(mod),repeat=r))
    lowers=list(product(range(0,mod,q),repeat=t))
    ys=[z+w for z in ys for w in lowers]
    etas=list(product(range(mod),repeat=b))
    checks=0;fullrank=0;nonzero_checks=0;deep_zero=0
    for A in A_all:
        ell=cofactors(A,q)
        entries=[]
        for y in ys:
            det=sum(ell[i]*y[i] for i in range(r))%q
            if det:
                entries.append((y,char_power*logs[det]*char_step%L))
        if any(ell):
            fullrank+=1
            expected_n=(q-1)*q**(M*b-d)
            assert len(entries)==expected_n
        else:
            assert not entries
        support=0
        for h in etas:
            literal=[0]*L
            for y,ch in entries:
                exponent=(ch-add_step*sum(h[i]*y[i] for i in range(b)))%L
                literal[exponent]+=1
            left=red(literal)
            predicted=[0]*L
            if any(ell) and all(x%(q**(M-1))==0 for x in h):
                a=tuple((h[i]//q**(M-1))%q for i in range(r))
                cs=[c for c in range(q) if a==tuple(c*x%q for x in ell)]
                assert len(cs)<=1
                if cs:
                    c=cs[0]
                    multiplier=q**((M-1)*b+k)
                    if c==0:
                        if trivial:predicted[0]=multiplier*(q-1)
                    elif trivial:
                        predicted[0]=-multiplier
                    else:
                        factor=(-char_power*logs[(-c)%q]*char_step)%L
                        # Gauss psi_0(s) has exponent (q^(M-1))*s*add_step.
                        for u in range(1,q):
                            exponent=(factor+char_power*logs[u]*char_step+
                                      q**(M-1)*u*add_step)%L
                            predicted[exponent]+=multiplier
            right=red(predicted)
            assert left==right,(q,k,t,M,char_power,A,h,left,right)
            checks+=1
            if any(left):support+=1;nonzero_checks+=1
            if M>1 and any(x%q for x in h):
                assert not any(left);deep_zero+=1
        if any(ell):
            expected=(q if trivial else q-1)*q**t
            assert support==expected
            # Counting in the full eta quotient has q^(Mb) integral translates.
            full_eta_support=support*q**(M*b)
            if not trivial:
                # Parseval after dividing the raw sum by q^(Mb).
                assert full_eta_support*q == len(entries)*q**(2*d)
            else:
                # c=0 amplitude(q-1) and c!=0 amplitude1.
                weighted=(q-1)**2+(q-1)
                assert q**(t+M*b)*weighted==len(entries)*q**(2*d)
    return dict(q=q,k=k,t=t,M=M,char_power=char_power,
                matrices=len(A_all),full_rank_matrices=fullrank,
                exact_transform_checks=checks,nonzero_transforms=nonzero_checks,
                higher_depth_zero_checks=deep_zero)

def all_A(q,k):
    r=k+1
    return [[list(vals[i*k:(i+1)*k]) for i in range(r)]
            for vals in product(range(q),repeat=r*k)]

out=[]
out.append(check_case(3,1,1,1,1,all_A(3,1)))
out.append(check_case(3,1,1,2,1,all_A(3,1)))
out.append(check_case(5,1,1,1,1,all_A(5,1))) # genuinely quartic character
out.append(check_case(3,1,1,1,0,all_A(3,1)))
# Higher-k oriented cofactors, including a singular matrix.
As=[
[[1,0],[0,1],[0,0]],
[[1,1],[0,1],[1,0]],
[[0,1],[1,0],[1,1]],
[[1,0],[0,0],[0,0]],
]
out.append(check_case(3,2,1,1,1,As))
result={"status":"PASS","scope":"literal finite Q contraction; no automorphic quotient claim",
        "cases":out,"total_exact_transform_checks":sum(x["exact_transform_checks"] for x in out),
        "total_higher_depth_zero_checks":sum(x["higher_depth_zero_checks"] for x in out)}
target=Path(__file__).with_suffix(".json")
target.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))

