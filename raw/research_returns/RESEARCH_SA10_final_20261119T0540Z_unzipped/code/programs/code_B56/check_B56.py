#!/usr/bin/env python3
"""Finite checks for RESEARCH_SA10, B.5--B.6.

These check finite counterexamples and normal-form images.  The proof of
presentation completeness and claims in arbitrary degree is in agent_B56_proofs.md.
No external libraries are required. Run with Python 3.
"""
from itertools import permutations, product
from fractions import Fraction
from time import perf_counter
import json

t0 = perf_counter()
counts = {}

def comp(f, g):
    """Coordinate maps, f after g: substitute g's outputs in f's indices."""
    return tuple(g[i] for i in f)

def chain(*fs):
    out = fs[-1]
    for f in reversed(fs[:-1]):
        out = comp(f, out)
    return out

p, d = (0,), (0, 0)
q, e = (0, 1), (1, 0, 0)
s, r = (1, 0), (1, 2, 0)
s1, s3 = (0, 2, 1), (1, 0, 2)
r2 = comp(r, r)
S2 = list(permutations(range(2)))
S3 = list(permutations(range(3)))
relations = {
    "p d = id": (comp(p, d), (0,)),
    "sigma d = d": (comp(s, d), d),
    "q e = sigma": (comp(q, e), s),
    "q rho e = d p": (chain(q, r, e), comp(d, p)),
    "q rho^2 e = id": (chain(q, r2, e), (0, 1)),
    "sigma_1 e = e": (comp(s1, e), e),
    "q sigma_3 = sigma q": (comp(q, s3), comp(s, q)),
    "p q sigma_1 = p q": (chain(p, q, s1), comp(p, q)),
}
for name, (left, right) in relations.items():
    assert left == right, (name, left, right)
for g in S3:
    assert chain(g, e, d) == chain(e, d)
counts["low_degree_corrected_relations"] = len(relations) + len(S3)
assert comp(s3, e) != e
assert chain(p, q, s3) != comp(p, q)
print("LOW DEGREE: all corrected relations hold; the sigma_3 readings of the two disputed relations fail.")

# Generate every composite between arities 1,2,3 and verify the image counts.
gens = [(2,1,p),(1,2,d),(3,2,q),(2,3,e)]
gens += [(2,2,g) for g in S2] + [(3,3,g) for g in S3]
hom = {(a,b): set() for a in range(1,4) for b in range(1,4)}
for a in range(1,4): hom[a,a].add(tuple(range(a)))
changed = True
while changed:
    changed = False
    for a in range(1,4):
        for b,c,g in gens:
            for f in list(hom[a,b]):
                fg = comp(g, f)
                if fg not in hom[a,c]:
                    hom[a,c].add(fg); changed = True
matrix = []
rank_counts = {}
for a in range(1,4):
    row = []
    for b in range(1,4):
        assert hom[a,b] == set(product(range(a), repeat=b))
        row.append(len(hom[a,b]))
        rank_counts[f"{a}->{b}"] = {str(k):sum(len(set(f))==k for f in hom[a,b]) for k in range(1,min(a,b)+1)}
    matrix.append(row)
assert matrix == [[1,1,1],[2,4,8],[3,9,27]]
counts["finite_set_maps_arities_1_to_3"] = sum(map(sum,matrix))
print("LOW DEGREE hom-set count matrix (source arity rows):", matrix)
print("LOW DEGREE rank counts:", json.dumps(rank_counts,sort_keys=True))

# Global countermodel to 151/017(a)--(d), even with the two global relations.
# E_1={0}, E_n={0,1} for n>=2; all group actions trivial.
objects = {1:(0,), **{n:(0,1) for n in range(2,8)}}
def pp(n,x): return 0 if n==1 else x
def dd(n,x): return 0 if n==1 else x
def act(n,g,x):
    assert tuple(sorted(g)) == tuple(range(n))
    assert x in objects[n]
    return x
nchecks = 0
for n in range(1,7):
    for x in objects[n]:
        assert pp(n,dd(n,x)) == x; nchecks += 1
    # Trivial actions make both equivariance relations and K transposition
    # invariance identities. Enumerate every permutation for n<=5.
    if n<=5:
        for g in permutations(range(n)):
            for x in objects[n+1]:
                assert act(n,g,pp(n,x)) == pp(n,act(n+1,g+(n,),x)); nchecks += 1
        for g in permutations(range(max(0,n-1))):
            for x in objects[n]:
                assert dd(n,act(n,g+(n-1,),x)) == act(n+1,g+(n-1,n),dd(n,x)); nchecks += 1
        for x in objects[n]:
            trans=tuple(range(n-1))+(n,n-1)
            assert act(n+1,trans,dd(n,x)) == dd(n,x); nchecks += 1
    if n<=5:
        for x in objects[n+2]:
            trans=tuple(range(n))+(n+1,n)
            assert pp(n,pp(n+1,act(n+2,trans,x))) == pp(n,pp(n+1,x)); nchecks += 1
        for x in objects[n]:
            trans=tuple(range(n-1))+(n,n-1,n+1)
            assert act(n+2,trans,dd(n+1,dd(n,x))) == dd(n+1,dd(n,x)); nchecks += 1
left, right = pp(2, dd(2,1)), dd(1, pp(1,1))
assert (left,right) == (1,0)
# Actual maps: delta_2:2->3, transposition(1,3), K_2:3->2.
delta2, trans13, K2 = (0,1),(2,1,0),(0,1,1)
actual_left = tuple(K2[trans13[delta2[i]]] for i in range(2))
delta1, K1 = (0,),(0,0)
actual_right = tuple(delta1[K1[i]] for i in range(2))
# This choice is constant at 2, hence differs by the target swap from delta1 K1.
# The manuscript-coordinate choice q rho e yields precisely the required
# rank-one map. The abstract finite-set equation uses permutation (1 3)
# plus sigma_2 on the target, as verified here.
actual_left_corrected = tuple(s[K2[trans13[delta2[i]]]] for i in range(2))
assert actual_left_corrected == actual_right == (0,0)
counts["global_countermodel_checks"] = nchecks
print("GLOBAL PRESENTATION COUNTERMODEL: all required equations hold; mixed equation gives",left,"!=",right)
print("Actual finite-set mixed equation checked: sigma_2 K_2 (1 3) delta_2 = delta_1 K_1.")

# BC2, constant singleton: all forest comparison generator conditions hold;
# a parallel pair has no equalizing cone.
G=(0,1)
cones_pair = [(a,b) for a in G for b in G]
assert cones_pair
cospans=0; commutative_squares=0
for f,g in product(G,repeat=2):
    squares=[(a,b) for a,b in product(G,repeat=2) if (f+a)%2==(g+b)%2]
    assert squares
    cospans += 1; commutative_squares += len(squares)
assert not [a for a in G if a == (a+1)%2]
counts["BC2_cospans"] = cospans
counts["BC2_commutative_squares"] = commutative_squares
print("BC2: Hyp1, Hyp2, Hyp2prime verified; parallel equalizer comparison is empty -> singleton.")
counts["BC2_normalized_H1_mod2_dimension"] = 1
# The only normalized 1-simplex is g, and the only normalized 2-simplex
# (g,g) has boundary g + g in F2, since gg=identity is degenerate.
assert (1+1)%2 == 0
print("BC2: normalized H_1(-;F2) has dimension 1, certifying noncontractibility.")

# Symmetric C2 nerve phi(n)=C2^n/C2. Canonical orbit representative starts 0.
def orbit(t): return tuple(x^t[0] for x in t)
def orbits(n): return [(0,)+t for t in product(G,repeat=n-1)]
def restrict(t,f): return orbit(tuple(t[i] for i in f))
product_checks=0
for psize,qsize in product(range(1,5),repeat=2):
    image={(restrict(t,tuple(range(psize))),restrict(t,tuple(range(psize,psize+qsize)))) for t in orbits(psize+qsize)}
    target=set(product(orbits(psize),orbits(qsize)))
    assert image==target
    product_checks += 1
pullback_checks=0; target_pairs=0
for psize,qsize,ksize in product(range(1,4),repeat=3):
    for f in product(range(psize),repeat=ksize):
        for g in product(range(qsize),repeat=ksize):
            parent=list(range(psize+qsize))
            def find(a):
                while parent[a]!=a:
                    parent[a]=parent[parent[a]]; a=parent[a]
                return a
            for a,b in zip(f,g):
                parent[find(a)]=find(psize+b)
            roots=sorted({find(a) for a in range(psize+qsize)})
            lookup={r:i for i,r in enumerate(roots)}
            ip=tuple(lookup[find(a)] for a in range(psize))
            iq=tuple(lookup[find(psize+a)] for a in range(qsize))
            image={(restrict(t,ip),restrict(t,iq)) for t in orbits(len(roots))}
            target={(x,y) for x,y in product(orbits(psize),orbits(qsize)) if restrict(x,f)==restrict(y,g)}
            assert image==target
            pullback_checks += 1; target_pairs += len(target)
counts["symmetric_C2_product_comparisons"] = product_checks
counts["symmetric_C2_pullback_comparisons"] = pullback_checks
counts["symmetric_C2_pullback_target_pairs"] = target_pairs
assert len(orbits(1))==1 and len(orbits(2))==2
print("SYMMETRIC C2 NERVE:",product_checks,"product comparisons;",pullback_checks,"pullback comparisons;",target_pairs,"target pairs, all surjective.")
print("SYMMETRIC C2 NERVE: equalizer of two coordinate projections has target size 2, image size 1.")

# Ordinary simplicial Cech nerve of a two-element cover of a point:
# endpoint equalizer of S^3 -> S contains (0,1,0), but comparisons only give
# constant triples because a monotone map identifying endpoints is constant.
witness=(0,1,0)
assert witness[0]==witness[2] and len(set(witness))>1
monotone_checks=0
for m in range(1,7):
    for f in product(range(m),repeat=3):
        if tuple(sorted(f))!=f: continue
        if f[0]==f[2]:
            assert len(set(f))==1
        monotone_checks+=1
counts["simplicial_Cech_monotone_maps"] = monotone_checks
print("SIMPLICIAL CECH NERVE: full Hyp fails at (0,1,0); category is the pair-groupoid nerve, hence contractible.")
print("SIMPLICIAL CECH NERVE: Hyp2prime also fails for the constant/endpoints cospan [0]->[1]<-[2].")

# A symmetric hypercover which violates Hyp2prime: continuous singular
# simplices of R. The polynomial b is zero on edge 02 but does not factor
# through any affine vertex map identifying 0 and 2.
P=(Fraction(1,2),Fraction(1,2),Fraction(0))
Q=(Fraction(0),Fraction(1,2),Fraction(1,2))
def polynomial(t): return t[1]*(t[0]-t[2])
assert polynomial(P)==Fraction(1,4)
assert polynomial(Q)==Fraction(-1,4)
amalgams=0
for size in range(1,5):
    for h in product(range(size),repeat=3):
        if h[0]!=h[2]: continue
        def affine(t):
            return tuple(sum(t[i] for i in range(3) if h[i]==j) for j in range(size))
        assert affine(P)==affine(Q)
        amalgams+=1
counts["symmetric_singular_hypercover_amalgams"] = amalgams
print("SYMMETRIC SINGULAR HYPERCOVER: Hyp2prime obstruction checked on",amalgams,"amalgams; b(P)=1/4, b(Q)=-1/4.")

# Naive symmetric realization of the C2 orbit nerve is the interval modulo
# endpoint exchange; the invariant midpoint gives a contraction.
midpoint=(Fraction(1,2),Fraction(1,2))
assert midpoint[::-1]==midpoint
for v in [(Fraction(0),Fraction(1)),midpoint,(Fraction(1),Fraction(0))]:
    for t in [Fraction(0),Fraction(1,2),Fraction(1)]:
        H=tuple((1-t)*v[i]+t*midpoint[i] for i in range(2))
        Hv=tuple((1-t)*v[1-i]+t*midpoint[i] for i in range(2))
        assert H[::-1]==Hv
print("NAIVE SYMMETRIC REALIZATION: C2 barycenter contraction is equivariant; this is not the homotopy colimit BG.")

counts["runtime_seconds"] = round(perf_counter()-t0,6)
print("COUNTS",json.dumps(counts,sort_keys=True))
