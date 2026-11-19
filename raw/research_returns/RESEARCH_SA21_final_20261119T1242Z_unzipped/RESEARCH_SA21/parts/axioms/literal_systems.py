"""Literal axiom-list counterexamples. Standard-library Python only.
GPT-6 Astra (OpenAI), /root/axioms, 2026-11-19.
"""
from itertools import product
from time import perf_counter
from core_models import closure,Magasin
from finite_axioms import SetFigures

def m3():
    E=range(5);bottom=0;top=4;atoms=[1,2,3]
    le=closure(5,[(0,i) for i in E]+[(i,4) for i in E])
    def sup(A):
        upper=[x for x in E if all((a,x) in le for a in A)]
        return next(x for x in upper if all((x,y) in le for y in upper))
    subsets=[frozenset(i for i in E if mask>>i&1) for mask in range(32)]
    irr=[x for x in E if all(sup(A)!=x or x in A for A in subsets)]
    assert irr==atoms
    dep={x:frozenset(a for a in atoms if (a,x) in le) for x in E}
    assert all(sup(dep[x])==x for x in E)
    assert all(((x,y) in le)==(dep[x]<=dep[y]) for x,y in product(E,repeat=2))
    # All pairs have a bound, so At3 and compatibility half of At5 hold.
    # At4, with refinement=incidence, reduces to inclusion of deployments.
    assert all(((x,y) in le)==all(any(a==b for b in dep[y]) for a in dep[x]) for x,y in product(E,repeat=2))
    comp=lambda x,y:any((x,z) in le and (y,z) in le for z in E)
    assert all(comp(x,y)==all(comp(a,b) for a in dep[x] for b in dep[y]) for x,y in product(E,repeat=2))
    # Later At5: enumerate every elementary source and figure target.
    for x,f in product(atoms,E):
        candidates=[y for y in dep[f] if (x,y) in le]
        if candidates:assert sum(all((y,z) in le for z in candidates) for y in candidates)==1
    # At6 is compatible refinement => incidence; the two relations agree.
    assert all(not(comp(x,y) and (x,y) in le) or (x,y) in le for x,y in product(atoms,repeat=2))
    internal={(x,y) for x,y in product(atoms,repeat=2) if (x,y) in le and not any(z!=y and (z,y) in le and (x,z) in le for z in atoms)}
    assert internal=={(x,x) for x in atoms}
    assert all((x,z) in internal for x,y in internal for yy,z in internal if y==yy)
    mag=Magasin(['a','b','c'],[],[],[(0,1),(0,2),(1,2)])
    mag.magaxioms()
    assert all((i,j) in mag.compat for i,j in product(mag.M,repeat=2))
    # Atlas At5a,b, on the original figure poset and its irreducibles.
    delta={(x,y) for x,y in product(atoms,repeat=2) if x!=y}
    assert all(x in atoms and y in atoms for x,y in delta)
    assert all(comp(x,y)==all((a,b) in delta for a in dep[x]-dep[y] for b in dep[y]-dep[x]) for x,y in product(atoms,repeat=2))
    assert dep[sup({1,2})]!={1,2}
    print('M3: literal C1-C3, At1-At7, and atlas At1-At5+Mag1-4 PASS; bounded-join primeness FAIL')
    print('M3: deployment(a join b)=',sorted(dep[sup({1,2})]),'but union=',[1,2])

def missing_membership():
    E=frozenset({0,1});a=frozenset({0});b=E
    U=frozenset({a,b});fam={frozenset(),U}
    def canonical(A):return frozenset(B for B in U if B<=A)
    figures=list(fam)
    for mask in range(1<<len(figures)):
        subfam=[figures[i] for i in range(len(figures)) if mask>>i&1]
        if any(all(q<=p for q in subfam) for p in fam):
            assert frozenset().union(*subfam) in fam
    assert all(SetFigures.admissible(P) for P in fam)
    assert all(frozenset(B for B in P if B<=A)==frozenset(B for B in Q if B<=A) for P,Q in product(fam,repeat=2) for A in P&Q)
    assert canonical(a) not in fam
    # At*3, interpreted in ambient Fig(E), for every occurring pair.
    assert all(not A<=B or SetFigures.refine(canonical(A),canonical(B)) for A,B in product(U,repeat=2))
    # At*4: when P=Q=U its antecedent already fails for A=B=a;
    # when either is empty the conclusion is one of the two admitted figures.
    for P,Q in product(fam,repeat=2):
        if all(canonical(A)|canonical(B) in fam for A in P for B in Q):assert P|Q in fam
    # U is an admissible separating cover with residuals {0},{1}.
    assert SetFigures.admissible(U) and frozenset().union(*U)==E
    assert all(x==y or any((x in A)!=(y in A) for A in U) for x,y in product(E,repeat=2))
    assert canonical(b)==U
    print('two-point final At*1-At*5 literal list PASS; canonical subfigure membership FAIL')

def nontransitive_internal():
    # x,y,Z,Xp,X, exactly the model of SA21-R8-09, independently checked.
    m=Magasin(['x','y','Z','Xp','X'],[(2,4)],[(0,2),(0,3),(1,3),(3,4)],[])
    U={i:{p for p in m.lieux if (p,i) in m.intern} for i in m.M}
    assert m.lieux==[0,1] and all(U.values())
    for i,j in m.ref:
        c=[k for k in m.down[j] if (i,k) in m.ref]
        assert sum(all((k,l) in m.le for l in c) for k in c)==1
    orth={(i,j) for i,j in product(m.M,repeat=2) if U[i].isdisjoint(U[j])}
    assert all(i!=j and (j,i) in orth for i,j in orth)
    assert all(i==j or (i,j) in orth for k in m.M for i,j in product(m.down[k],repeat=2))
    assert (0,3) in m.intern and (3,4) in m.intern and (0,4) not in m.intern
    assert (0,4) in orth and (3,4) in m.intern and (0,3) not in orth
    print('156-8/16-17 literal data Mag1,Mag2,MogL1,div3,div4 PASS; internal transitivity and Mag3 hereditary FAIL')
    print('open lieu sets=',{m.names[i]:[m.names[p] for p in sorted(U[i])] for i in m.M})
    # The same two orders give a literal final Cont1--5 system, even with
    # the lieu-disjointness extras, but fail later At7. This compatibility
    # is specified independently; it is not the failed reconstructed δ.
    pairs={(0,1),(1,2),(2,4)}
    m.compat={(i,i) for i in m.M}|pairs|{(j,i) for i,j in pairs}
    m.F=[frozenset(i for i in m.M if mask>>i&1) for mask in range(1<<m.n)]
    m.F=[f for f in m.F if all(m.down[i]<=f for i in f) and all((i,j) in m.compat for i,j in product(f,repeat=2))]
    m.Fset=set(m.F)
    assert all(m.down[i] in m.Fset for i in m.M)
    assert all(not((i,j) in m.compat and (i,j) in m.ref) or (i,j) in m.le for i,j in product(m.M,repeat=2))
    assert all((ii,jj) in m.compat for i,j in m.compat for ii in m.down[i] for jj in m.down[j])
    for i,f in product(m.M,m.F):
        choices=[j for j in f if (i,j) in m.ref]
        if choices:assert sum(all((j,k) in m.le for k in choices) for j in choices)==1
    assert all(not(m.fr(f,g) and m.fr(g,f)) or f==g for f,g in product(m.F,repeat=2))
    flags=m.flags();assert flags['L1'] and flags['L2'] and flags['L3']
    assert all(not(m.fd(f,g) and m.fr(p,f) and m.fr(q,g)) or m.fd(p,q) for f,g,p,q in product(m.F,repeat=4))
    print('final Cont1--5, Fig1--4, Cont6, Cond7, prime At1--6 PASS; At7 FAIL; figures',len(m.F))

if __name__=='__main__':
    t=perf_counter();m3();missing_membership();nontransitive_internal();print('seconds',perf_counter()-t)
