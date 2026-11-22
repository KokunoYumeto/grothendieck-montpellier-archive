"""Exact finite certificates for Part E, 2026-11-19.

Independent deterministic enumerations by GPT-6 Astra. No numerical tolerance,
third-party algebra package, random sampling, or external data is used.
Permutation composition p*q means first q, then p.
"""
from itertools import combinations, permutations, product
from collections import Counter
from math import lcm, factorial
import time

start=time.perf_counter()
def comp(p,q): return tuple(p[x] for x in q)
def inv(p): return tuple(p.index(x) for x in range(len(p)))
def cycles(p):
    todo=set(range(len(p))); out=[]
    while todo:
        a=min(todo); c=[]; b=a
        while b in todo: todo.remove(b); c.append(b); b=p[b]
        out.append(tuple(c))
    return out
def typ(p): return tuple(sorted(map(len,cycles(p)),reverse=True))
def sign(p): return (-1)**(len(p)-len(cycles(p)))
def order(p): return lcm(*map(len,cycles(p)))
def act(p,A): return tuple(sorted(p[x] for x in A))
def aset(p,A): return tuple(sorted(act(p,B) for B in A))
def group(gens,n):
    G={tuple(range(n))}; frontier=list(G)
    while frontier:
        h=frontier.pop()
        for g in gens:
            z=comp(g,h)
            if z not in G: G.add(z); frontier.append(z)
    return G
def matchings(S):
    S=tuple(sorted(S))
    if not S: yield (); return
    for b in S[1:]:
        for rest in matchings(x for x in S if x not in (S[0],b)):
            yield tuple(sorted(((S[0],b),)+rest))
def conjugate(p,G):
    pi=inv(p); return frozenset(comp(comp(p,g),pi) for g in G)
def orbits(G,S):
    rem=set(S); out=[]
    while rem:
        a=min(rem); O=tuple(sorted({g[a] for g in G})); out.append(O); rem-=set(O)
    return tuple(sorted(out,key=lambda z:(len(z),z)))

S=tuple(range(6)); S6=tuple(permutations(S)); e6=S
duads=tuple(combinations(S,2)); sy=tuple(sorted(matchings(S)))
totals=tuple(sorted(tuple(sorted(T)) for T in combinations(sy,5)
                    if len({d for s in T for d in s})==15))
assert len(sy)==15 and len(totals)==6
tidx={T:i for i,T in enumerate(totals)}
def total_action(p): return tuple(tidx[tuple(sorted(aset(p,s) for s in T))] for T in totals)
outer={p:total_action(p) for p in S6}; outerinv={v:k for k,v in outer.items()}
assert len(outerinv)==720
# Equivariance is structural; also check all 720^2 multiplication pairs.
assert all(outer[comp(p,q)]==comp(outer[p],outer[q]) for p in S6 for q in S6)
assert typ(outer[(1,0,2,3,4,5)])==(2,2,2)
assert all(len(set(T)&set(U))==1 for T,U in combinations(totals,2))
disjoint_pairs=[(a,b) for a,b in combinations(sy,2) if not(set(a)&set(b))]
assert len(disjoint_pairs)==60
assert all(sum(a in T and b in T for T in totals)==1 for a,b in disjoint_pairs)
# The 60 ordinary hexagons split into six ten-hexagon classes.
hexagons=tuple(tuple(sorted(a+b)) for a,b in disjoint_pairs)
assert len(set(hexagons))==60
bihexagons=[(i,j) for i,j in combinations(range(60),2) if not(set(hexagons[i])&set(hexagons[j]))]
assert len(bihexagons)==90
adj={i:{j for a,b in bihexagons for j in ([b] if a==i else [a] if b==i else [])} for i in range(60)}
assert all(len(N)==3 for N in adj.values())
components=[];todo=set(range(60))
while todo:
    reached={min(todo)};frontier=list(reached)
    while frontier:
        a=frontier.pop()
        for b in adj[a]-reached:reached.add(b);frontier.append(b)
    todo-=reached;components.append(reached)
assert len(components)==6 and all(len(C)==10 for C in components)
assert all(len({next(i for i,T in enumerate(totals) if a in T and b in T) for j in C for a,b in [disjoint_pairs[j]]})==1 for C in components)
print('E.003: duads=15 synthemes=15 totals=6; homomorphism pairs=518400; hexagons=60, unique completions=60')
print('E.003: 90 bihexagons; disjoint-hexagon graph has six connected components of order 10 and degree 3 (Petersen graphs)')
for i,T in enumerate(totals): print('  total',i,T)

# Dual incidences, double dual, and (point,total) complement bijections.
dual_duad={s:tuple(i for i,T in enumerate(totals) if s in T) for s in sy}
assert all(len(d)==2 for d in dual_duad.values())
dual_syntheme={d:tuple(sorted(dual_duad[s] for s in sy if d in s)) for d in duads}
assert set(dual_syntheme.values())==set(sy)
double_points={a:tuple(sorted(dual_syntheme[d] for d in duads if a in d)) for a in S}
assert set(double_points.values())==set(totals)
dits=tuple(tuple(sorted((A,tuple(x for x in S if x not in A))))
           for A in combinations(S,3) if 0 in A)
for D in dits:
    H=[p for p in S6 if aset(p,D)==D]
    fixed=[D2 for D2 in dits if all(aset(outer[p],D2)==D2 for p in H)]
    assert len(H)==72 and len(fixed)==1
for a in S:
    for j in range(6):
        H=[p for p in S6 if p[a]==a and outer[p][j]==j]
        A=tuple(x for x in S if x!=a); B=tuple(x for x in S if x!=j)
        maps=[]
        for values in permutations(B):
            f=dict(zip(A,values))
            if all(f[p[x]]==outer[p][f[x]] for p in H for x in A): maps.append(f)
        assert len(H)==20 and len(maps)==1
print('E.003: all 10 ditriads have unique duals; all 36 point-total pairs have one equivariant complement bijection')

# Hemiicosahedra from a rooted pentagon. Faces not containing root are
# complements of root triangles whose opposite edge is a diagonal.
def icofaces(root,C):
    n=len(C); assert n==5
    faces={tuple(sorted((root,C[i],C[(i+1)%5]))) for i in range(5)}
    for i in range(5):
        diagonal={C[i],C[(i+2)%5]}
        faces.add(tuple(x for x in C if x not in diagonal))
    return tuple(sorted(tuple(sorted(f)) for f in faces))
Ic=tuple(sorted({icofaces(0,C) for C in permutations(range(1,6))}))
alltri=set(combinations(S,3))
opp=lambda F:tuple(sorted(alltri-set(F)))
Bic=tuple(sorted({tuple(sorted((F,opp(F)))) for F in Ic}))
assert len(Ic)==12 and len(Bic)==6
assert all(opp(F) in Ic for F in Ic)
def link(F,a): return tuple(sorted(tuple(x for x in f if x!=a) for f in F if a in f))
def cycle_orders(edges,vertices):
    return [C for C in permutations(vertices) if all(tuple(sorted((C[i],C[(i+1)%len(C)]))) in edges for i in range(len(C)))]
ori={}
for F in Ic:
    orientations=set()
    for a in S:
        C=cycle_orders(link(F,a),tuple(x for x in S if x!=a))
        assert len(C)==10
        assert all(icofaces(a,c)==F for c in C)
        orientations|={sign((a,)+c) for c in C}
    assert len(orientations)==1
    ori[F]=orientations.pop()
    assert all(sum(set(d)<=set(f) for f in F)==2 for d in duads)
    assert all(sum(set(f)<=set(Q) for f in F)==2 for Q in combinations(S,4))
    assert all(tuple(x for x in S if x not in f) not in F for f in F)
assert all(ori[opp(F)]==-ori[F] for F in Ic)
assert all(ori[aset(p,F)]==sign(p)*ori[F] for p in S6 for F in Ic)
# Canonical map Biicos -> total, independent of root and choice of opposite.
def bic_total(B,a):
    black=set(link(B[0],a)); white=set(combinations(tuple(x for x in S if x!=a),2))-black
    T=[]
    for d in black:
        matches=[c for c in white if not(set(c)&set(d))]; assert len(matches)==1
        c=matches[0]; last=tuple(x for x in S if x not in d+c)
        T.append(tuple(sorted((d,c,last))))
    return tuple(sorted(T))
bt={}
for B in Bic:
    ts={bic_total(B,a) for a in S}; assert len(ts)==1
    T=ts.pop(); assert T in totals; bt[B]=tidx[T]
assert len(set(bt.values()))==6
for F in Ic:
    H=[p for p in S6 if aset(p,F)==F]
    assert len(H)==60 and all(sign(p)==1 for p in H)
for B in Bic:
    H=[p for p in S6 if tuple(sorted(aset(p,F) for F in B))==B]
    assert len(H)==120 and all(outer[p][bt[B]]==bt[B] for p in H)
print('E.004: 12 hemiicosahedra, 6 biicosahedra; all 72 root perspectives; orientations checked on 8640 actions; stabilizers 60/120')

# Three perspectives: vertices, edges, faces (all labelled structures).
edge_records=set(); face_records=set()
for B in Bic:
    F=B[0]
    for edge in duads:
        a,b=edge; Q=tuple(x for x in S if x not in edge)
        D=tuple(x for x in Q if tuple(sorted((a,b,x))) in F)
        Dc=tuple(x for x in Q if x not in D); diagonals=tuple(sorted((D,Dc)))
        assert len(D)==len(Dc)==2
        # Rotation character equals the action on the distinguished edge.
        H=[p for p in S6 if act(p,edge)==edge and tuple(sorted(aset(p,K) for K in B))==B]
        assert len(H)==8
        assert len({tuple(p[x] for x in Q) for p in H})==8
        diagchar=lambda p: 1 if act(p,D)==D else -1
        sideparts=tuple(sorted(tuple(sorted(P)) for P in matchings(Q) if tuple(sorted(P))!=diagonals))
        codchar=lambda p:1 if aset(p,sideparts[0])==sideparts[0] else -1
        assert all((1 if p[a]==a else -1)==diagchar(p)*codchar(p) for p in H)
        edge_records.add((edge,diagonals,bt[B]))
    for f in F:
        fc=tuple(x for x in S if x not in f)
        pairing=[]
        for x in f:
            candidates=[y for y in fc if tuple(sorted(tuple(z for z in f if z!=x)+(y,))) in F]
            assert len(candidates)==1; pairing.append((x,candidates[0]))
        assert len({y for x,y in pairing})==3
        face_records.add((f,tuple(pairing),F))
assert len(edge_records)==90 and len(face_records)==60
# All ordered face/prism data (20 faces times six bijections) reconstruct one Ic.
records={}
for F in Ic:
    for f in F:
        fc=tuple(x for x in S if x not in f)
        m=tuple(next(y for y in fc if tuple(sorted(tuple(z for z in f if z!=x)+(y,))) in F) for x in f)
        records[(f,m)]=F
assert len(records)==120
print('E.005: all 90 biicosahedron-edge perspectives; all 120 oriented face/prism perspectives are bijective')

# Square duality and the central twist of the side-dual square.
Q=(0,1,2,3); eps=(4,5); diag=((0,2),(1,3)); sides=((0,1),(1,2),(2,3),(0,3))
cod=(((0,1),(2,3)),((0,3),(1,2)))
H=[p for p in S6 if aset(p,diag)==diag]
assert len(H)==16
O=orbits([outer[p] for p in H],S); assert tuple(map(len,O))==(2,4)
epstar,qstar=O
dstar=[P for P in matchings(qstar) if all(aset(outer[p],P)==P for p in H)]
assert len(dstar)==1; dstar=dstar[0]
codstar=tuple(P for P in matchings(qstar) if P!=dstar)
def char(p,two,level=1): return 1 if (act(p,two[0]) if level==1 else aset(p,two[0]))==two[0] else -1
for p in H:
    pe=1 if p[4]==4 else -1; pes=1 if outer[p][epstar[0]]==epstar[0] else -1
    d=char(p,diag); c=char(p,cod,2)
    ds=char(outer[p],dstar); cs=char(outer[p],codstar,2)
    assert (ds,cs)==(c,d) and pe*pes*d*c==1
    assert sign(tuple(Q.index(p[x]) for x in Q))==c
def side_index(edge): return next(i for i,s in enumerate(sides) if set(s)==set(edge))
# Represent [4,side_i]; flipping eps acts by opposite side i+2.
twist={p:tuple((side_index(act(p,s))+(2 if p[4]==5 else 0))%4 for s in sides) for p in H}
maps=[]
for values in permutations(qstar):
    if all(values[twist[p][i]]==outer[p][values[i]] for p in H for i in range(4)): maps.append(values)
assert len(maps)==2
bad=[]
for values in permutations(qstar):
    if all(values[(p[i]+(2 if p[4]==5 else 0))%4]==outer[p][values[i]] for p in H for i in Q):bad.append(values)
assert len(bad)==0
print('E.006: square character table on all 16 elements; side-dual central twist maps=',maps,'; untwisted-vertex version has 0 maps')

# AGL(2,3) on its twelve affine lines, deterministic ordering by direction.
F3=range(3); points=tuple(product(F3,repeat=2)); dirs=((1,0),(0,1),(1,1),(1,2))
lines=[]
for d in dirs:
    lines.extend(sorted({tuple(sorted(((x+t*d[0])%3,(y+t*d[1])%3) for t in F3)) for x,y in points}))
lidx={L:i for i,L in enumerate(lines)}; direction=tuple(i//3 for i in range(12))
GL=tuple((a,b,c,d) for a,b,c,d in product(F3,repeat=4) if (a*d-b*c)%3)
def affine(M,v,p):a,b,c,d=M;x,y=p;return ((a*x+b*y+v[0])%3,(c*x+d*y+v[1])%3)
AGL={tuple(lidx[tuple(sorted(affine(M,v,p) for p in L))] for L in lines):(M,v) for M in GL for v in points}
assert len(AGL)==432
dp=lambda p:tuple(direction[p[3*i]] for i in range(4))
V=frozenset(p for p,(M,v) in AGL.items() if M==(1,0,0,1)); assert len(V)==9
kernel=[p for p in AGL if dp(p)==(0,1,2,3)]
assert len(kernel)==18
assert all(sign(tuple(p[i] for i in range(3)))==sign(tuple(p[i]-3 for i in range(3,6))) for p in kernel)
lifts=[p for p in AGL if typ(dp(p))==(2,2)]
assert len(lifts)==54 and all(order(p)==4 for p in lifts)
alphas=tuple(sorted(matchings(range(4))))
Glist=[]; stablist=[]
gen6=((1,0,2,3,4,5),(1,2,3,4,5,0))
for alpha in alphas:
    A=tuple(i for i in range(12) if direction[i] in alpha[0]); B=tuple(i for i in range(12) if direction[i] in alpha[1])
    stab=[p for p in AGL if aset(dp(p),alpha)==alpha]; stablist.append(stab)
    assert len(stab)==144
    keeps=[p for p in stab if p[A[0]] in A]
    ra=lambda p:tuple(A.index(p[x]) for x in A);rb=lambda p:tuple(B.index(p[x]) for x in B)
    found=[];before_normalization=Counter()
    for kind in (0,1):
        for f in S6:
            fi=inv(f)
            def theta(p):
                v=comp(comp(f,p),fi);return outerinv[v] if kind else v
            if not all(theta(ra(t))==rb(t) for t in V):continue
            before_normalization[kind]+=1
            if not all(theta(comp(comp(ra(h),x),inv(ra(h))))==comp(comp(rb(h),theta(x)),inv(rb(h))) for h in keeps for x in gen6):continue
            found.append((kind,f))
    assert len(found)==1 and found[0][0]==1
    assert before_normalization==Counter({1:9})
    f=found[0][1];fi=inv(f); G=set()
    for x in S6:
        y=outerinv[comp(comp(f,x),fi)];p=list(range(12))
        for i,a in enumerate(A):p[a]=A[x[i]]
        for i,b in enumerate(B):p[b]=B[y[i]]
        G.add(tuple(p))
    G=frozenset(G); assert len(G)==720 and V<=G;Glist.append(G)
    assert all(conjugate(h,G)==G for h in stab)
    assert len(set(stab)&G)==72
    assert sum(all(comp(h,g)==comp(g,h) for g in G) for h in stab)==1
    N=[g for g in G if conjugate(g,V)==V];assert len(N)==72
    cosets={frozenset(comp(g,t) for t in V):g for g in N}
    def quotient_order(g):
        h=g;n=1
        while h not in V:h=comp(g,h);n+=1
        return n
    assert Counter(quotient_order(g) for g in cosets.values())==Counter({1:1,2:5,4:2})
    print('E.008: alpha=',alpha,'translation-compatible graphs=',dict(before_normalization),'unique normalized outer graph conjugator=',f,'|G|=720 |stabilizer|=144 |intersection|=72 |centralizer|=1 |N_G(V)|=72')
assert len(set(Glist))==3
assert all(conjugate(h,G) in Glist for h in AGL for G in Glist)
print('E.008: all 1296 AGL conjugations checked; 54 lifts of double transpositions all have order 4')

# Incidence counterexample to c alone: all E_i plus one point of a later E_j.
classes=tuple(tuple(range(3*i,3*i+3)) for i in range(4))
badblocks=tuple(tuple(sorted(classes[i]+(b,))) for i in range(4) for j in range(i+1,4) for b in classes[j])
assert len(set(badblocks))==18
assert all(sum(a in B and b in B for B in badblocks)==1 for i in range(4) for j in range(i+1,4) for a in classes[i] for b in classes[j])
print('E.007: c-alone counterexample has 18 four-element blocks; all 54 cross-class pairs occur once')

# Projective linear groups, including an explicit faithful five-object action of PGL2(5).
def pgl(q):
    elems=range(q); PP=tuple(range(q+1)); infinity=q
    if q==4:
        add=lambda x,y:x^y
        def mul(x,y):
            if not x or not y:return 0
            lg={1:0,2:1,3:2};return (1,2,3)[(lg[x]+lg[y])%3]
        neg=lambda x:x
    else:add=lambda x,y:(x+y)%q;mul=lambda x,y:x*y%q;neg=lambda x:-x%q
    inverse=lambda x:next(y for y in elems if mul(x,y)==1)
    G=set()
    for a,b,c,d in product(elems,repeat=4):
        if add(mul(a,d),neg(mul(b,c)))==0:continue
        vals=[]
        for x in PP:
            num,den=(a,c) if x==infinity else (add(mul(a,x),b),add(mul(c,x),d))
            vals.append(infinity if den==0 else mul(num,inverse(den)))
        G.add(tuple(vals))
    return G
for q,n in ((2,6),(3,24),(4,60),(5,120)):
    PG=pgl(q);assert len(PG)==n
    if q==4:assert all(sign(g)==1 for g in PG)
    if q==5:
        A5={g for g in PG if sign(g)==1};assert len(A5)==60
        invol=[g for g in A5 if order(g)==2];assert len(invol)==15
        V4s=set()
        for g,h in combinations(invol,2):
            if comp(g,h)==comp(h,g):V4s.add(frozenset((e6,g,h,comp(g,h))))
        V4s=tuple(sorted(V4s,key=lambda G:tuple(sorted(G))));assert len(V4s)==5
        pg5action={tuple(V4s.index(conjugate(g,H)) for H in V4s) for g in PG}
        assert len(pg5action)==120
print('E.002: PGL orders 6,24,60,120; PGL2(4) even; PGL2(5) acts faithfully on its five Sylow-2 subgroups of PSL2(5)')

# Plane trees: exhaustive fixed-point-free pairings through 14 boundary sides.
def noncrossing(P):
    return not any(a<c<b<d or c<a<d<b for (a,b),(c,d) in combinations(P,2))
def repaired(P,active):
    if not P:return True
    pos={a:i for i,a in enumerate(active)}
    for a,b in P:
        if abs(pos[a]-pos[b])==1:
            return repaired(tuple(x for x in P if x!=(a,b)),tuple(x for x in active if x not in (a,b)))
    return False
def literal(P,active,fixed=()):
    if not P:return True
    pos={a:i for i,a in enumerate(active)}
    for a,b in P:
        if abs(pos[a]-pos[b])==1:
            for remove,keep in ((a,b),(b,a)):
                if literal(tuple(x for x in P if x!=(a,b)),tuple(x for x in active if x!=remove),fixed+(keep,)):return True
    return False
for n in range(1,8):
    hist=Counter(); count=0
    for P in matchings(range(2*n)):
        alpha=list(range(2*n))
        for a,b in P:alpha[a]=b;alpha[b]=a
        sigma=tuple((alpha[i]+1)%(2*n) for i in range(2*n))
        genus=(n+1-len(cycles(sigma)))//2
        assert 2*genus==n+1-len(cycles(sigma)) and genus>=0
        nc=noncrossing(P);assert nc==(genus==0)==repaired(P,tuple(range(2*n)))
        hist[genus]+=1;count+=1
    catalan=factorial(2*n)//(factorial(n)*factorial(n+1));assert hist[0]==catalan
    print('E.011: n=',n,'pairings=',count,'genus histogram=',dict(sorted(hist.items())))
P=((0,3),(1,2));assert noncrossing(P) and not literal(P,(0,1,2,3))
print('E.011: literal one-edge contraction rejects nested pairing ((0,3),(1,2)); repaired criterion accepts it')
def involutions(active):
    active=tuple(active)
    if not active:yield ();return
    yield from involutions(active[1:])
    a=active[0]
    for b in active[1:]:
        for P in involutions(x for x in active if x not in (a,b)):yield ((a,b),)+P
for n in range(11):
    total=accepted=0
    for P in involutions(range(n)):
        paired={x for ab in P for x in ab};fixed=set(range(n))-paired
        admissible=noncrossing(P) and not any(a<f<b for a,b in P for f in fixed)
        assert repaired(P,tuple(range(n)))==admissible
        total+=1;accepted+=admissible
    print('E.010/E.011: partial involutions n=',n,'total=',total,'admissible=',accepted)
print('ALL ASSERTIONS PASSED; elapsed seconds',round(time.perf_counter()-start,3))
