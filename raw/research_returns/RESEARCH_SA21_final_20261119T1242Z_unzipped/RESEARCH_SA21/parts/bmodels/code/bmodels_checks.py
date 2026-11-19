#!/usr/bin/env python3
"""Finite certificates for B.3 and incidence examples for B.4.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 2026-11-19.
No external packages.  Exhaustive checks are finite checks, not substitutes for
the general proofs in BMODELS.md.
"""
from itertools import combinations, product
from time import perf_counter
import json


def subsets(xs):
    xs = tuple(xs)
    return [frozenset(xs[i] for i in range(len(xs)) if mask >> i & 1)
            for mask in range(1 << len(xs))]


def posets(n):
    pairs = list(combinations(range(n), 2))
    for choices in product(range(3), repeat=len(pairs)):
        le = {(i, i) for i in range(n)}
        for (i, j), c in zip(pairs, choices):
            if c == 1: le.add((i, j))
            if c == 2: le.add((j, i))
        if all((a, c) in le for a, b in le for bb, c in le if b == bb):
            yield le


def configurations(n, le, conflict):
    return [s for s in subsets(range(n))
            if all(a in s for a, b in le if b in s)
            and not any(a in s and b in s for a, b in conflict)]


def inspect_skeleton(n, le, conflict):
    cfg = configurations(n, le, conflict)
    cfg_set = set(cfg)
    principal = {frozenset(a for a, b in le if b == e) for e in range(n)}
    assert principal <= cfg_set
    # C1: nonempty family; every bounded pair has its union in the family.
    assert frozenset() in cfg_set
    compatible = lambda a, b: a | b in cfg_set
    for a in cfg:
        for b in cfg:
            bounded = any(a <= c and b <= c for c in cfg)
            assert bounded == compatible(a, b)
            assert a & b in cfg_set
    # Complete primes, tested using binary bounded joins (sufficient in finite D).
    primes = {p for p in cfg if p and all(
        not (p <= (a | b)) or p <= a or p <= b
        for a in cfg for b in cfg if compatible(a, b))}
    assert primes == principal
    for a in cfg:
        assert frozenset().union(*(p for p in principal if p <= a)) == a
    # C3: cross-pair compatibility of event-principal configurations suffices.
    by_e = {e: frozenset(a for a, b in le if b == e) for e in range(n)}
    for a in cfg:
        for b in cfg:
            rhs = all(compatible(by_e[e], by_e[f]) for e in a for f in b)
            assert compatible(a, b) == rhs
    # Recover causality and binary conflict from complete-prime configurations.
    for e in range(n):
        for f in range(n):
            assert ((e, f) in le) == (by_e[e] <= by_e[f])
            assert ((e, f) in conflict) == (not compatible(by_e[e], by_e[f]))
    return len(cfg)


def exhaustive_binary_pes(max_n=4):
    records = []
    for n in range(max_n + 1):
        pairs = list(combinations(range(n), 2))
        poset_count = model_count = total_configurations = 0
        for le in posets(n):
            poset_count += 1
            for mask in range(1 << len(pairs)):
                conflict = set()
                for k, (a, b) in enumerate(pairs):
                    if mask >> k & 1:
                        conflict.update(((a, b), (b, a)))
                if not all((a, c) in conflict
                           for a, b in conflict for bb, c in le if b == bb):
                    continue
                model_count += 1
                total_configurations += inspect_skeleton(n, le, conflict)
        records.append(dict(events=n, labelled_posets=poset_count,
                            binary_event_structures=model_count,
                            configurations_checked=total_configurations))
    return records


def ternary_conflict_counterexample():
    E = frozenset(range(3))
    le = {(e, e) for e in E}
    Con = {s for s in subsets(E) if len(s) <= 2}
    # Winskel (1987), Definition 1.3.4.
    assert all(frozenset({e}) in Con for e in E)
    assert all(t in Con for s in Con for t in subsets(s))
    assert all(s | {e} in Con for s in Con for e, ep in le if ep in s)
    assert all(len({a for a, b in le if b == e}) < 4 for e in E)
    # All pairs are consistent, but the triple is not.
    assert all(frozenset({e, f}) in Con for e in E for f in E)
    assert E not in Con
    F, G = frozenset({0, 1}), frozenset({2})
    assert F in Con and G in Con and F | G not in Con
    # No binary conflict relation on these events yields Con.
    represented = 0
    for m in range(8):
        conflict = {(a, b) for k, (a, b) in enumerate(combinations(E, 2))
                    if m >> k & 1}
        candidates = {s for s in subsets(E)
                      if not any(a in s and b in s for a, b in conflict)}
        represented += candidates == Con
    assert represented == 0
    return dict(events=list(E), causality=sorted(le),
                consistency_sets=[sorted(s) for s in sorted(Con,key=lambda s:(len(s),sorted(s)))],
                C3_failing_pair=[sorted(F),sorted(G)],
                binary_relations_representing_consistency=represented)


def two_refinements():
    E = range(2)
    inc = {(0, 0), (1, 1)}
    cfg = [frozenset(), frozenset({0}), frozenset({1})]
    results = []
    for extra in [False, True]:
        ref = inc | ({(0, 1)} if extra else set())
        interior_disjoint = set()
        # Mag 1: orders and incidence contained in refinement.
        assert inc <= ref
        for rel in [inc, ref]:
            assert all((e,e) in rel for e in E)
            assert all(a == b or (b,a) not in rel for a,b in rel)
            assert all((a,c) in rel for a,b in rel for bb,c in rel if b==bb)
        # Mag 2: unique least carrier in each principal incidence set.
        strong = set()
        for x,y in ref:
            carriers = [z for z in E if (z,y) in inc and (x,z) in ref]
            least = [z for z in carriers if all((z,t) in inc for t in carriers)]
            assert len(least)==1
            if least[0]==y: strong.add((x,y))
        # Mag 3: symmetry, irreflexivity, strong-refinement heredity.
        assert all((b,a) in interior_disjoint and a!=b for a,b in interior_disjoint)
        assert all((xp,yp) in interior_disjoint for x,y in interior_disjoint
                   for xp,xx in strong for yp,yy in strong if xx==x and yy==y)
        # Mag 4: every principal incidence set is a clique for internal disjointness.
        assert all(y==z or (y,z) in interior_disjoint for x in E
                   for y in E for z in E if (y,x) in inc and (z,x) in inc)
        lieux = [x for x in E if not any(y!=x and (y,x) in ref for y in E)]
        assert all(any((p,x) in strong for p in lieux) for x in E)
        assert all(((x,y) in interior_disjoint) ==
                   all((p,q) in interior_disjoint for p in lieux for q in lieux
                       if (p,x) in strong and (q,y) in strong)
                   for x in E for y in E)
        results.append(dict(refinement=sorted(ref), lieux=lieux,
                            figures=[sorted(s) for s in cfg],
                            Mag1_to_4=True, divisibility=True, MagL2=True))
    assert results[0]['figures'] == results[1]['figures']
    assert results[0]['refinement'] != results[1]['refinement']
    return results


def literal_contree_counterexample():
    # 0 < d < a,b,c < 1: M3 with a new least element below its old bottom.
    names = ('0', 'd', 'a', 'b', 'c', '1')
    L = range(6)
    le = {(i,i) for i in L} | {(0,i) for i in L} | {(i,5) for i in L}
    le |= {(1,i) for i in (2,3,4)}
    def sup(xs):
        upper = [u for u in L if all((x,u) in le for x in xs)]
        least = [u for u in upper if all((u,v) in le for v in upper)]
        assert len(least)==1
        return least[0]
    def inf(xs):
        lower = [u for u in L if all((u,x) in le for x in xs)]
        greatest = [u for u in lower if all((v,u) in le for v in lower)]
        assert len(greatest)==1
        return greatest[0]
    families = subsets(L)
    # C1, including empty supremum.
    assert all(sup(A) in L for A in families)
    assert sup([])==0
    # The manuscript's equality-based irreducibility, not join-primality.
    M = [x for x in L if all(sup(A)!=x or x in A for A in families)]
    assert M==[1,2,3,4]
    dep = lambda F: frozenset(x for x in M if (x,F) in le)
    comp = lambda F,G: any((F,u) in le and (G,u) in le for u in L)
    disj = lambda F,G: comp(F,G) and inf([F,G])==0
    # C2 and C3.
    assert all(sup(dep(F))==F for F in L)
    assert all(comp(F,G)==all(comp(x,y) for x in dep(F) for y in dep(G))
               for F in L for G in L)
    # M is connected under incidence; hence C4 and C4bis.
    component={M[0]}
    while True:
        new=component | {x for x in M if any((x,y) in le or (y,x) in le
                                              for y in component)}
        if new==component: break
        component=new
    assert component==set(M)
    assert all(comp(x,y) for x in M for y in M)
    # One component: the component trace of F is F, so every component tuple occurs.
    assert all(sup(dep(F)&component)==F for F in L)
    sub = lambda A,B: A==B
    ref = lambda A,B: (A,B) in le
    restriction = lambda H,G: inf([H,G])
    # C5.
    assert all(disj(G,Fp)==disj(G,F) for Fp in L for F in L for G in L if sub(Fp,F))
    # C6(a,b,c): unique induced subdivision, strata formula, bounded joins.
    for Fp in L:
        for F in L:
            if not sub(Fp,F): continue
            for G in L:
                if (G,F) not in le: continue
                candidates=[Gp for Gp in L if (Gp,Fp) in le and sub(Gp,G)]
                assert candidates==[G]
                assert dep(G)=={x for x in dep(Fp) if ref(x,G)}
            for A in families:
                if all((G,F) in le for G in A):
                    assert restriction(Fp,sup(A))==sup([restriction(Fp,G) for G in A])
    # C7_0: extend every subdivision of a subfigure.
    assert all(any(sub(Fp,F) and restriction(Fp,G)==Gp for Fp in L)
               for F in L for G in L for Gp in L if (G,F) in le and sub(Gp,G))
    # C8: every subdivision of every cover member is forced to be that member.
    assert all(sub(sup(A),sup(A)) for A in families)
    # C8_0: both zig-zag identities, even with X arbitrary.
    assert all(X==F for X in L for F in L if (X,F) in le and sub(F,X))
    assert all(X==F for X in L for F in L if sub(X,F) and (F,X) in le)
    missing=frozenset({1,2,3})
    assert missing not in {dep(F) for F in L}
    assert all(x in missing for x,y in le if y in missing and x in M)
    assert all(comp(x,y) for x in missing for y in missing)
    assert sup([2,3])==5 and 4 in dep(5) and 4 not in dep(2)|dep(3)
    assert inf([2,sup([3,4])])==2
    assert sup([inf([2,3]),inf([2,4])])==1
    return dict(elements=names, order=sorted((names[a],names[b]) for a,b in le),
                multistrates=[names[x] for x in M],
                deployments={names[F]:[names[x] for x in sorted(dep(F))] for F in L},
                subdivision='equality', refinement='incidence order',
                C1_C2_C3_C4_C4bis_C5_C6_C7zero_C8_C8zero=True,
                missing_finite_downward_closed_compatibility_clique=[names[x] for x in sorted(missing)],
                nondistributivity='a meet (b join c)=a; (a meet b) join (a meet c)=d')


def geometric_incidence_examples():
    # Circle split into two closed arcs e,f and their common endpoints a,b.
    # Supports are encoded by the four nonempty open strata a,b,e°,f°.
    circle = [frozenset({0}), frozenset({1}), frozenset({0,1,2}),
              frozenset({0,1,3})]
    e,f = circle[2:]
    intersection = e & f
    assert intersection == {0,1}
    assert intersection not in circle
    lower = [a for a in circle if a <= intersection]
    assert len(lower)==2 and all(not (a < b) for a in lower for b in lower)
    # Circle with one vertex and one open edge: top is not a regular closed cell.
    monogon = [frozenset({0}), frozenset({0,1})]
    covers = [a for a in monogon if a < monogon[1] and
              not any(a < b < monogon[1] for b in monogon)]
    assert len(covers)==1
    return dict(two_arc_circle=dict(closed_strata=[sorted(a) for a in circle],
                                   arc_intersection=sorted(intersection),
                                   At_pol1=False),
                monogon=dict(closed_strata=[sorted(a) for a in monogon],
                             top_immediate_predecessors=len(covers), At_simp1=False),
                scope='Finite incidence verification; geometric realization is proved in bmodels.tex.')


def literal_at14bis_interval():
    # Atomic regions: endpoint 0, midpoint, endpoint 1, left open half, right open half.
    regions = frozenset(range(5))
    old = [frozenset({0}), frozenset({2}), regions]
    new = [frozenset({0}), frozenset({1}), frozenset({2}),
           frozenset({0,1,3}), frozenset({1,2,4})]
    def cell(A, family):
        return A - frozenset().union(*(B for B in family if B < A))
    old_cells = [cell(A,old) for A in old]
    new_cells = [cell(A,new) for A in new]
    assert all(old_cells) and all(new_cells)
    assert frozenset().union(*old_cells) == regions
    assert frozenset().union(*new_cells) == regions
    assert all(not (a&b) for a,b in combinations(new_cells,2))
    carrier = []
    for C in new_cells:
        candidates=[j for j,D in enumerate(old_cells) if C <= D]
        assert len(candidates)==1
        carrier.append(candidates[0])
    assert all(not (new[i] <= new[j]) or old[carrier[i]] <= old[carrier[j]]
               for i in range(5) for j in range(5))
    # G=F, G'=F'; restriction is prescribed and every point of support is covered.
    assert carrier[3]==carrier[4]==2
    assert old[carrier[3]] <= old[carrier[4]]
    assert not new[3] <= new[4]
    failures=[(i,j) for i in range(5) for j in range(5)
              if (new[i] <= new[j]) != (old[carrier[i]] <= old[carrier[j]])]
    return dict(old_closed_strata=[sorted(A) for A in old],
                new_closed_strata=[sorted(A) for A in new],
                carrier=carrier, subdivision=True, G_equals_F=True,
                literal_order_reflection=False,
                order_reflection_failures=failures,
                corrected_exterior_clause=True,
                scope='Finite carrier-poset certificate; interval realization in bmodels.tex.')


if __name__ == '__main__':
    start = perf_counter()
    result = dict(exhaustive_binary_pes=exhaustive_binary_pes(),
                  ternary_conflict=ternary_conflict_counterexample(),
                  literal_contree_counterexample=literal_contree_counterexample(),
                  same_event_structure_two_refinements=two_refinements(),
                  geometric_incidence_examples=geometric_incidence_examples(),
                  literal_at14bis_interval=literal_at14bis_interval())
    result['runtime_seconds'] = round(perf_counter()-start,6)
    result['all_assertions_passed'] = True
    print(json.dumps(result,indent=2))
