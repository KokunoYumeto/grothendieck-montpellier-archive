#!/usr/bin/env python3
"""Exact exhaustive Coxeter normalizers, exceptional crystallographic types.

No group database: roots are generated from the Cartan reflections.  A root r
whose Coxeter orbit spans Q^rank determines every intertwiner w c = c^a w
by w(r).  We try every root image and every unit a, check integrality,
the Gram matrix, and Weyl membership by reducing the image of rho to the
fundamental chamber.  Complements are found or excluded by exhaustive lifts
of the displayed generators of (Z/h)^*.  Matrices and words are certificates.
"""
from pathlib import Path
from itertools import product
from math import gcd
import json, time
import numpy as np
import sympy as sp

OUT = Path(__file__).resolve().parents[1] / 'logs'
OUT.mkdir(exist_ok=True)

def cartan(kind):
    n = int(kind[1:]); A = np.eye(n, dtype=np.int64)*2
    if kind[0] == 'E':
        edges=[(0,2),(2,3),(1,3)]+[(i,i+1) for i in range(3,n-1)]
    else:
        edges=[(i,i+1) for i in range(n-1)]
    for i,j in edges: A[i,j]=A[j,i]=-1
    if kind=='F4': A[2,1]=-2
    if kind=='G2': A[1,0]=-3
    return A

def key(m): return tuple(map(int,m.flat))
def power(m,k):
    z=np.eye(len(m),dtype=np.int64)
    while k:
        if k&1: z=z@m
        m=m@m; k//=2
    return z

def run(kind):
    start=time.perf_counter(); A=cartan(kind); n=len(A)
    ident=np.eye(n,dtype=np.int64)
    S=[]
    for i in range(n):
        s=ident.copy();s[i]-=A[i];S.append(s)
    roots={tuple(ident[:,i]) for i in range(n)}
    todo=list(roots)
    for r in todo:
        for s in S:
            q=tuple(map(int,s@r))
            if q not in roots: roots.add(q);todo.append(q)
    rootlist=sorted(roots)
    c=ident.copy()
    for s in S: c=c@s
    powers=[ident]
    while key(powers[-1]@c)!=key(ident): powers.append(powers[-1]@c)
    h=len(powers)
    cyclic=None
    for r in rootlist:
        orb=np.array([p@r for p in powers]).T
        _,piv=sp.Matrix(orb).rref()
        if len(piv)==n:
            cyclic=(r,piv,orb[:,piv]);break
    assert cyclic, (kind,'no cyclic root')
    r,piv,B=cyclic
    det=int(sp.Matrix(B).det())
    adj=np.array(sp.Matrix(B).adjugate(),dtype=np.int64)
    d=[sp.Rational(1)]*n
    for _ in range(n):
        for i,j in product(range(n),repeat=2):
            if A[i,j]:
                if i!=j and i<j: d[j]=d[i]*sp.Rational(int(A[i,j]),int(A[j,i]))
    den=sp.ilcm(*[x.q for x in d]); d=[int(x*den) for x in d]
    # For branched E this is all ones; for F4/G2 the loop is along a chain.
    G=np.diag(d)@A
    assert np.array_equal(G,G.T)
    rho0=sp.Matrix(A).inv()*sp.ones(n,1)
    rho_den=sp.ilcm(*[x.q for x in rho0])
    rho=np.array([int(x*rho_den) for x in rho0],dtype=np.int64)
    assert min(A@rho)>0
    def weyl_word(w):
        v=w@rho; u=w.copy();word=[]
        while True:
            vals=A@v
            neg=[i for i,x in enumerate(vals) if x<0]
            if not neg: break
            i=neg[0];v=S[i]@v;u=S[i]@u;word.append(i+1)
            assert len(word)<=len(roots)//2
        return word if np.array_equal(u,ident) else None
    units=[a for a in range(h) if gcd(a,h)==1]
    normalizers={};discarded_outer=0
    for a in units:
        for s in rootlist:
            target=np.array([powers[(a*k)%h]@s for k in piv]).T
            numerator=target@adj
            if np.any(numerator%det):continue
            w=numerator//det
            if not np.array_equal(w.T@G@w,G): continue
            if not np.array_equal(w@c,powers[a]@w):continue
            if any(tuple(map(int,w@v)) not in roots for v in rootlist):continue
            word=weyl_word(w)
            if word is None: discarded_outer+=1;continue
            normalizers[key(w)]=(a,w,word)
    cosets={a:[v[1] for v in normalizers.values() if v[0]==a] for a in units}
    assert all(len(cosets[a])==h for a in units)
    assert {key(x) for x in cosets[1]}=={key(x) for x in powers}
    # Explicit independent generators and their orders for each unit group.
    gens={'G2':[(5,2)],'F4':[(5,2),(11,2)],'E6':[(5,2),(11,2)],
          'E7':[(5,6)],'E8':[(7,4),(29,2)]}[kind]
    genunit={1}
    for a,o in gens:
        assert pow(a,o,h)==1 and all(pow(a,j,h)!=1 for j in range(1,o))
        genunit={u*pow(a,j,h)%h for u in genunit for j in range(o)}
    assert genunit==set(units)
    assert np.prod([o for a,o in gens])==len(units)
    eligible=[]
    for a,o in gens:
        eligible.append([w for w in cosets[a] if np.array_equal(power(w,o),ident)])
    complement=None; tested=0
    for choice in product(*eligible):
        tested+=1
        if any(not np.array_equal(u@v,v@u) for u,v in product(choice,repeat=2)):continue
        subgroup={key(ident):ident}
        for w,(_,o) in zip(choice,gens):
            subgroup={key(v@power(w,j)):v@power(w,j) for v in subgroup.values() for j in range(o)}
        assert len(subgroup)==len(units)
        assert len(set(subgroup)&{key(v) for v in powers})==1
        complement=[normalizers[key(w)] for w in choice];break
    result={'type':kind,'cartan':A.tolist(),'gram':G.tolist(),'coxeter':c.tolist(),
            'root_count':len(roots),'h':h,'cyclic_root':list(map(int,r)),
            'basis_powers':list(map(int,piv)),'basis_determinant':det,
            'normalizer_order':len(normalizers),'outer_automorphisms_discarded':discarded_outer,
            'unit_generators':gens,'eligible_lift_counts':[len(x) for x in eligible],
            'lift_tuples_tested':tested,'splits':complement is not None,
            'complement':[{'unit':a,'matrix':w.tolist(),'inverse_reduction_word':word}
                          for a,w,word in complement] if complement else None,
            'all_normalizer_elements':[{'unit':a,'matrix':w.tolist(),'inverse_reduction_word':word}
                                       for a,w,word in normalizers.values()],
            'seconds':time.perf_counter()-start}
    print(f"{kind}: roots={len(roots)}, h={h}, |N|={len(normalizers)}, "
          f"generators={gens}, eligible={result['eligible_lift_counts']}, "
          f"split={result['splits']}, tested={tested}, seconds={result['seconds']:.4f}",flush=True)
    (OUT/f'normalizer_{kind}.json').write_text(json.dumps(result,indent=2))
    return result

if __name__=='__main__':
    all_results=[run(t) for t in ['G2','F4','E6','E7','E8']]
    (OUT/'coxeter_normalizers_summary.json').write_text(json.dumps([
        {k:v for k,v in x.items() if k!='all_normalizer_elements'} for x in all_results],indent=2))
