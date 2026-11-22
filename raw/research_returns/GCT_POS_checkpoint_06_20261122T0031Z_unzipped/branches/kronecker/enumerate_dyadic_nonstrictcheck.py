from itertools import combinations_with_replacement, combinations, product
from collections import Counter,defaultdict
import json, pathlib, time, sys
import numpy as np
from scipy.optimize import linprog
import sympy as sp

n=int(sys.argv[1]) if len(sys.argv)>1 else 4
M=2**(n-1)
base=pathlib.Path(__file__).resolve().parent

def canon(A,B,C):
    det=(sum(A)+sum(B)+sum(C))%M
    inv=pow(det,-1,M)
    A=tuple((a*inv)%M for a in A); B=tuple((a*inv)%M for a in B); C=tuple((a*inv)%M for a in C)
    keys=[]
    for a,b,c in product(set(A),set(B),set(C)):
        if (a+b+c)%M==0:
            aa=tuple(sorted((v-a)%M for v in A));bb=tuple(sorted((v-b)%M for v in B));cc=tuple(sorted((v-c)%M for v in C))
            keys.append(tuple(sorted([aa,bb,cc])))
    return min(keys)

spectra=[x for x in combinations_with_replacement(range(M),n) if x[0]==0]
seen=set(); records=[]; counts=Counter();start=time.time()
for ia,A in enumerate(spectra):
    for ib in range(ia,len(spectra)):
        B=spectra[ib]
        for ic in range(ib,len(spectra)):
            C=spectra[ic]
            if (sum(A)+sum(B)+sum(C))%2==0: continue
            # Every vertex must be covered; prefilter on aggregate support.
            sets=[tuple(sorted(set(X))) for X in [A,B,C]]
            S=[(a,b,c) for a,b,c in product(*sets) if (a+b+c)%M==0]
            if any(set(e[j] for e in S)!=set(sets[j]) for j in range(3)):continue
            key=canon(A,B,C)
            if key in seen:continue
            seen.add(key); counts['covered_orbits']+=1
            AA=[tuple(sorted(set(X))) for X in key]
            S=[e for e in product(*AA) if sum(e)%M==0]
            mult=[Counter(X) for X in key]
            rows=[(i,v) for i in range(3) for v in AA[i]]
            mat=sp.Matrix([[int(e[i]==v) for e in S] for i,v in rows])
            rhs=sp.Matrix([mult[i][v] for i,v in rows])
            aeq=np.array(mat).astype(float);beq=np.array(rhs).astype(float).ravel()
            # maximize minimum aggregate support mass; necessary for exact full support
            cvec=np.zeros(len(S)+1);cvec[-1]=-1
            aeq2=np.c_[aeq,np.zeros(len(rows))]
            aub=np.c_[-np.eye(len(S)),np.ones(len(S))]
            res=linprog(cvec,A_ub=aub,b_ub=np.zeros(len(S)),A_eq=aeq2,b_eq=beq,bounds=[(0,None)]*(len(S)+1),method='highs')
            if not res.success:continue
            counts['feasible_orbits']+=1
            if res.x[-1]<1e-8:
                print('NONSTRICT',key,flush=True)
                counts['nonstrict_orbits']+=1
                continue
            counts['strict_balance_orbits']+=1
            distinct=all(len(set(X))==n for X in key)
            if distinct: counts['distinct_orbits']+=1
            # Reconstruct an exact positive feasible point from basic floating solution.
            pt=[sp.Rational(float(v)).limit_denominator(10**8) for v in res.x[:-1]]
            exact=(mat*sp.Matrix(pt)==rhs and all(v>0 for v in pt))
            if not exact:
                sol,pars=mat.gauss_jordan_solve(rhs)
                sub={p:sp.Rational(float(res.x[j])).limit_denominator(10**8) for p,j in []}
            full_edges=sum(mult[0][a]*mult[1][b]*mult[2][c] for a,b,c in S)
            centralizer=sum(sum(v*v for v in mm.values())-1 for mm in mult)
            rec={'spectra':key,'aggregate_support':S,'aggregate_positive_masses':[str(x) for x in pt], 'certificate_exact':bool(exact),'distinct':distinct,'fixed_W_dim':full_edges,'fixed_lie_dim':centralizer,'expected_fixed_quotient_dim':full_edges-centralizer,'aggregate_incidence_rank':mat.rank()}
            records.append(rec)
    if ia%20==0:print('progress',ia,len(spectra),dict(counts), 'seconds',round(time.time()-start,2),flush=True)
obj={'n':n,'M':M,'scope':'semisimple lifts whose eigenvalues are M-th roots, normalized determinant character primitive; necessary strict aggregate balance, sufficient critical tensor when distinct spectra','counts':dict(counts),'records':records,'seconds':time.time()-start}
fn=base/f'dyadic_n{n}_classification_nonstrictcheck.json';fn.write_text(json.dumps(obj,indent=2));print(fn,dict(counts),time.time()-start,flush=True)
