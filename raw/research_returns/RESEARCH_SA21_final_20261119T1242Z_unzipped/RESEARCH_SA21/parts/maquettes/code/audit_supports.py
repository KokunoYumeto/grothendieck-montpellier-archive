"""Independent set-based audit of selected Part A claims.

No imports from the main certificates: this uses frozensets and explicit
relation tests. Finite checks supplement the proofs, not infinite claims.
GPT-6 Astra (OpenAI), ChatGPT Pro mode, /root/maquettes, 2026-11-19.
"""
from itertools import combinations, product
from time import perf_counter
import json


def subsets(items):
    items = tuple(items)
    return [frozenset(items[i] for i in range(len(items)) if mask >> i & 1)
            for mask in range(1 << len(items))]


def polarity(universe, orth):
    universe = frozenset(universe)
    def polar(a):
        return frozenset(x for x in universe if all((x, y) in orth for y in a))
    def close(a):
        return polar(polar(a))
    # Every closed set is an intersection of singleton neighbourhoods.
    closed = {universe}
    for x in universe:
        neighbourhood = polar({x})
        closed |= {a & neighbourhood for a in tuple(closed)}
    assert all(close(a) == a for a in closed)
    return polar, close, closed


def ten_element():
    universe = frozenset(range(4))
    old = {a for a in subsets(universe) if (0 in a) == (1 in a)}
    ap, aa = frozenset({0}), frozenset({0, 1})
    big_ap = universe - ap
    lattice = old | {ap, big_ap}
    def meet(a, b):
        lows = {x for x in lattice if x <= a and x <= b}
        ans = frozenset().union(*lows)
        assert ans in lattice
        return ans
    def join(a, b):
        uppers = {x for x in lattice if a <= x and b <= x}
        ans = universe.intersection(*uppers)
        assert ans in lattice
        return ans
    for x, y in product(lattice, repeat=2):
        assert meet(x, y) in lattice and join(x, y) in lattice
        assert universe - x in lattice
        assert meet(x, universe - x) == frozenset()
        assert join(x, universe - x) == universe
    for x in old:
        assert meet(ap, x) == (ap if aa <= x else frozenset())
        assert join(ap, x) == (ap if not x else aa | x)
    assert meet(aa, big_ap) == frozenset()
    assert join(ap, meet(aa, big_ap)) != aa
    return {"elements": len(lattice), "pairs": len(lattice)**2,
            "orthomodular_witness": [sorted(ap), sorted(aa)]}


def regular_opens():
    counts = []
    for n in range(5):
        universe = frozenset(range(n))
        choices = list(product(range(n), repeat=2))
        choices = [(x, y) for x, y in choices if x != y]
        count = 0
        for arrows in subsets(choices):
            relation = arrows | {(x, x) for x in universe}
            if any((x, z) not in relation for x, y in relation
                   for yy, z in relation if y == yy):
                continue
            count += 1
            lower = {x: frozenset(z for z in universe if (z, x) in relation)
                     for x in universe}
            orth = {(x, y) for x, y in product(universe, repeat=2)
                    if not lower[x] & lower[y]}
            polar, close, closed = polarity(universe, orth)
            interior = lambda a: frozenset(x for x in universe if lower[x] <= a)
            closure = lambda a: universe - interior(universe - a)
            regular = {a for a in subsets(universe) if interior(closure(a)) == a}
            assert closed == regular
            for a in subsets(universe):
                opened = frozenset().union(*(lower[x] for x in a))
                assert polar(a) == interior(universe - opened)
                assert close(a) == interior(closure(opened))
            assert all((not a & b) <= (a <= polar(b)) for a, b in product(closed, repeat=2))
        counts.append({"n": n, "all_labelled_preorders": count})
    return counts


def lieu_reduction():
    counts = []
    for n in range(5):
        lieux = frozenset(range(n))
        choices = list(combinations(lieux, 2))
        count = 0
        for edges in subsets(choices):
            orth = set(edges) | {(y, x) for x, y in edges}
            pl, cl, closed_l = polarity(lieux, orth)
            multistrates = frozenset(a for a in subsets(lieux) if a)
            orth_m = {(a, b) for a, b in product(multistrates, repeat=2)
                      if all((x, y) in orth for x, y in product(a, b))}
            pm, cm, closed_m = polarity(multistrates, orth_m)
            hat = lambda t: frozenset(a for a in multistrates if a <= t)
            trace = lambda s: frozenset(x for x in lieux if frozenset({x}) in s)
            assert {hat(t) for t in closed_l} == closed_m
            for s in closed_m:
                assert hat(trace(s)) == s
                assert trace(pm(s)) == pl(trace(s))
            for t in closed_l:
                assert trace(hat(t)) == t
            count += 1
        counts.append({"lieux": n, "all_labelled_graphs": count})
    return counts


def old_countermodel():
    names = ('a', 'b', 'X', 'p', 'e', 'w', 'h', 'g')
    universe = frozenset(names)
    lower = {x: frozenset({'a', 'b', 'X'}) if x == 'X' else frozenset({x})
             for x in names}
    le = {(x, y) for y in names for x in lower[y]}
    refine = le | {('p', 'X')}
    internal = {(x, x) for x in names} | {('p', 'X')}
    edge_strings = ('ab', 'ap', 'bp', 'ae', 'bw', 'pw', 'eh', 'hg', 'gw', 'Xa', 'Xb', 'Xw')
    orth = {(s[0], s[1]) for s in edge_strings}
    orth |= {(y, x) for x, y in tuple(orth)}
    assert all((xx, yy) in orth for x, y in orth for xx, yy in product(names, repeat=2)
               if (xx, x) in internal and (yy, y) in internal)
    assert all(x == y or (x, y) in orth for a in names for x, y in product(lower[a], repeat=2))
    for x, y in refine:
        carriers = [z for z in lower[y] if (x, z) in refine]
        least = [z for z in carriers if all((z, w) in le for w in carriers)]
        assert len(least) == 1
    compatible = {(x, y) for x, y in product(names, repeat=2)
                  if all((a, b) in orth for a, b in product(lower[x]-lower[y], lower[y]-lower[x]))}
    figures = [f for f in subsets(names) if all(lower[x] <= f for x in f)
               and all((x, y) in compatible for x, y in product(f, repeat=2))]
    figures_set = set(figures)
    fr = lambda f, g: all(any((x, y) in refine for y in g) for x in f)
    fc = lambda f, g: f | g in figures_set
    fd = lambda f, g: fc(f, g) and not f & g
    restriction = lambda f, g: frozenset(x for x in f if fr(lower[x], g))
    lieux = universe - {'X'}
    shadow = lambda f: frozenset(p for p in lieux if fr({p}, f))
    for x, y in product(names, repeat=2):
        assert fd(lower[x], lower[y]) == all(fd({p}, {q}) for p, q in product(shadow(lower[x]), shadow(lower[y])))
        assert any((p, x) in internal for p in lieux)
        if x != y and (x, y) in compatible:
            assert all(fd({p}, {q}) for p, q in product(lieux, repeat=2)
                       if (p, x) in internal and (q, y) in internal)
        common = lower[x] & lower[y]
        if all(fd({p}, {q}) for p, q in product(shadow(lower[x])-shadow(common), shadow(lower[y])-shadow(common))):
            assert (x, y) in compatible
    relative_instances = support_instances = 0
    for f, g in product(figures, repeat=2):
        if fc(f, g):
            common = f & g
            for p in figures:
                if not fr(p, f): continue
                for q in figures:
                    if not fr(q, g): continue
                    rp, rq = restriction(p, common), restriction(q, common)
                    assert not fc(rp, rq) or fc(p, q)
                    assert not fd(rp, rq) or fd(p, q)
                    relative_instances += 1
        if fr(g, f):
            witnesses = [w for w in figures if fd(w, g) and not fd(w, f)]
            if witnesses:
                assert any(fr(w, f) for w in witnesses)
            support_instances += 1
    old_orth = {(x, y) for x, y in product(names, repeat=2) if fd(lower[x], lower[y])}
    po, co, closed = polarity(universe, old_orth)
    assert not any(x == 'X' or y == 'X' for x, y in old_orth)
    opened = {x: co(lower[x]) & po(lower[x]-{x}) for x in names}
    assert opened['X'] == {'p'}
    assert all((y, x) in refine for x in names for y in opened[x])
    supp = lambda f: co(frozenset().union(*(opened[x] for x in f)))
    complement = (supp({'a', 'b', 'X'}) & po(supp({'a'})), supp({'b', 'X'}))
    intersection = (supp({'a', 'X'}) & supp({'a', 'b'}), supp({'a'}))
    assert complement == (frozenset({'b', 'p', 'e'}), frozenset({'b', 'p'}))
    assert intersection == (frozenset({'a', 'w'}), frozenset({'a'}))
    return {"figures": len(figures), "closed_supports": len(closed),
            "relative_C_and_D_instances": relative_instances,
            "support_separation_refinement_instances": support_instances,
            "complement_failure": [sorted(a) for a in complement],
            "meet_failure": [sorted(a) for a in intersection]}


def noncograph():
    represented = (frozenset({1}), frozenset({2}), frozenset({3}),
                   frozenset({1, 2}), frozenset({2, 3}))
    universe = frozenset(range(5))
    orth = {(i, j) for i, j in product(universe, repeat=2) if not represented[i] & represented[j]}
    polar, close, closed = polarity(universe, orth)
    expected = {frozenset(i for i in universe if represented[i] <= a) for a in subsets({1, 2, 3})}
    assert closed == expected and len(closed) == 8
    path = (3, 2, 0, 4)
    assert all(((path[i], path[j]) in orth) == (j == i+1)
               for i, j in combinations(range(4), 2))
    order = {(0, 1), (1, 2), (0, 2), (3, 2), (0, 4)}
    assert all((x, z) in order for x, y in order for yy, z in order if y == yy)
    assert orth == order | {(y, x) for x, y in order}
    return {"vertices": 5, "closed_supports": len(closed), "induced_path": list(path)}


if __name__ == '__main__':
    started = perf_counter()
    result = {'A11': ten_element(), 'A12': regular_opens(), 'A13': lieu_reduction(),
              'A24': old_countermodel(), 'A25': noncograph()}
    result['seconds'] = perf_counter() - started
    print(json.dumps(result, indent=2, sort_keys=True))
