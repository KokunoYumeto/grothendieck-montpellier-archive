"""Certificate separating C1--C8_0 from least carriers.
Every quantified clause of C5, C6(a,b,c), C7_0, C8_0 is enumerated.
GPT-6 Astra (OpenAI), /root/axioms, 2026-11-19.
"""
from itertools import product
from time import perf_counter

def run():
    t=perf_counter();names=['d','a','y','z'];M=range(4)
    F=[frozenset(),frozenset({0}),frozenset({0,1}),frozenset({0,2}),frozenset({0,3}),frozenset({0,2,3})]
    inds=range(len(F));le={(i,j) for i,j in product(inds,repeat=2) if F[i]<=F[j]}
    sub={(i,i) for i in inds}|{(2,3),(2,4),(2,5)}
    assert all((j,i) not in sub or i==j for i,j in sub)
    assert all((i,k) in sub for i,j in sub for jj,k in sub if j==jj)
    ref={(i,j) for i,j in product(inds,repeat=2) if any((i,h) in le and (h,j) in sub for h in inds)}
    assert all((i,k) in ref for i,j in ref for jj,k in ref if j==jj)
    assert all((j,i) not in ref or i==j for i,j in ref)
    def comp(i,j):return F[i]|F[j] in F
    def disj(i,j):return comp(i,j) and not F[i]&F[j]
    # C1 and the repaired prime C2 follow from this explicit downset family;
    # verify its closed-subfamily and bounded-union closure.
    md=[frozenset({0}),frozenset({0,1}),frozenset({0,2}),frozenset({0,3})]
    obj=[1,2,3,4]
    assert all(q in F for p in F for q in (frozenset(i for i in M if mask>>i&1) for mask in range(16)) if q<=p and all(md[i]<=q for i in q))
    assert all(comp(i,j)==all(comp(obj[x],obj[y]) for x in F[i] for y in F[j]) for i,j in product(inds,repeat=2))
    # C4 is vacuous: the incidence comparability graph is the connected star.
    assert all(0 in p for p in F if p)
    assert all(all(disj(k,i)==disj(k,j) for k in inds) for i,j in sub)
    pulls={}
    for fp,f in sub:
        for g in inds:
            if (g,f) not in le:continue
            solutions=[h for h in inds if (h,fp) in le and (h,g) in sub]
            assert len(solutions)==1,(fp,f,g,solutions)
            h=solutions[0];pulls[fp,f,g]=h
            assert F[h]=={x for x in F[fp] if (obj[x],g) in ref}
        subs=[g for g in inds if (g,f) in le]
        for mask in range(1<<len(subs)):
            gs=[subs[k] for k in range(len(subs)) if mask>>k&1]
            u=F.index(frozenset().union(*(F[g] for g in gs)))
            lhs=F[pulls[fp,f,u]];rhs=frozenset().union(*(F[pulls[fp,f,g]] for g in gs))
            assert lhs==rhs
    for g,f in le:
        for gp,gg in sub:
            if gg==g:assert any((fp,f) in sub and pulls[fp,f,g]==gp for fp in inds)
    for x in obj:
        assert all(not((x,h) in le and (h,x) in sub) or h==x for h in inds)
        assert all(not((x,h) in sub and (h,x) in le) or h==x for h in inds)
    carriers=[y for y in F[5] if (2,obj[y]) in ref]
    assert carriers==[2,3]
    assert not any(md[y]<=md[z] for y,z in [(2,3),(3,2)])
    # Mixed subdivisions of y,z agree on d but do not glue.
    assert pulls[2,3,1]==pulls[4,4,1]==1
    assert not comp(2,4)
    # Literal 156-7 At6, whose hypothesis is X incident with F, is much
    # weaker than the intended external-carrier axiom. The same model
    # satisfies all the other intended core clauses.
    assert all(((i,j) in ref)==all(any((obj[x],obj[y]) in ref for y in F[j]) for x in F[i]) for i,j in product(inds,repeat=2))
    assert all(not(comp(obj[x],obj[y]) and (obj[x],obj[y]) in ref) or md[x]<=md[y] for x,y in product(M,repeat=2))
    internal={(x,y) for x,y in product(M,repeat=2) if (obj[x],obj[y]) in ref and not any(z!=y and z in md[y] and (obj[x],obj[z]) in ref for z in M)}
    assert all((x,z) in internal for x,y in internal for yy,z in internal if y==yy)
    for f in F:
        for x in f:
            choices=[y for y in f if (obj[x],obj[y]) in ref]
            assert x in choices and all(md[x]<=md[y] for y in choices)
    print('C1-C4, prime generation, C5, literal C6(a,b,c), C7_0, C8_0 PASS')
    print('At5 least-carrier axiom FAIL: a refines y and z in figure {d,y,z}, neither carrier least')
    print('Final C8 full subdivision gluing FAIL: a subdivides y; z subdivides z; agree on d but incompatible')
    print('Literal incident-source 156-7 At6, At4, compatible-refinement incidence and At7 PASS; intended external-carrier axiom FAIL')
    print('figures=',[sorted(names[x] for x in f) for f in F])
    print('seconds',perf_counter()-t)

def identity_subdivision_chain():
    # Two strata a<x, three figures, primitive subdivision equality.
    F=[frozenset(),frozenset({0}),frozenset({0,1})]
    le=lambda f,g:f<=g
    sub=lambda f,g:f==g
    comp=lambda f,g:True
    disj=lambda f,g:not f&g
    assert all(sub(f,g)==sub(g,f) for f in F for g in F)
    restrictions={}
    for fp,f,g in product(F,repeat=3):
        if sub(fp,f) and le(g,f):
            sols=[h for h in F if le(h,fp) and sub(h,g)]
            assert sols==[g]
            restrictions[fp,f,g]=g
            # Each stratum refines g exactly when it belongs to g.
            assert frozenset(x for x in fp if frozenset(range(x+1))<=g)==g
    for f,g,gp in product(F,repeat=3):
        if le(g,f) and sub(gp,g):
            assert any(sub(fp,f) and restrictions[fp,f,g]==gp for fp in F)
    glue_diagrams=0
    for f in F:
        lower=[g for g in F if le(g,f)]
        for mask in range(1<<len(lower)):
            cover=[lower[i] for i in range(len(lower)) if mask>>i&1]
            if frozenset().union(*cover)==f:
                pieces=cover  # these are all primitive subdivisions
                sols=[p for p in F if sub(p,f) and all(restrictions[p,f,g]==gp for g,gp in zip(cover,pieces))]
                assert sols==[f];glue_diagrams+=1
    assert all(disj(h,F[1])==disj(h,F[2]) for h in F)
    assert le(F[1],F[2]) and not sub(F[1],F[2])
    print('two-stratum equality-subdivision chain: C1-C8 (including C4,C4bis,C6abc,C7_0,C8_0,gluing) PASS')
    print('primitive subdivision != refinement plus equal cosupport: a refines x, equal cosupport, a does not subdivide x; gluing diagrams',glue_diagrams)

if __name__=='__main__':run();identity_subdivision_chain()
