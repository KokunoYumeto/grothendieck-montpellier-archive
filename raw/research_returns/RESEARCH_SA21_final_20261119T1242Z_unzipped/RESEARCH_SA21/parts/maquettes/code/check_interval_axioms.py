"""Check every strong primed axiom for interval magasins on orders n<=4.

Only the naturally-labelled order generator is imported; all interval
relations and assertions are defined here. GPT-6 Astra (OpenAI), 2026-11-19.
"""
from itertools import product, combinations
from pathlib import Path
from time import perf_counter
import sys, json
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'code'))
from supports_core import natural_posets


def check(n, lt):
    base_le = lambda x, y: x == y or (x, y) in lt
    symbols = [('P', x) for x in range(n)] + [('I', a, b) for a, b in sorted(lt)]
    endpoints = lambda u: (u[1],) if u[0] == 'P' else u[1:]
    incidence = {(u, v) for u, v in product(symbols, repeat=2)
                 if u == v or (u[0] == 'P' and v[0] == 'I' and u[1] in v[1:])}
    rho = {(u, v) for u, v in product(symbols, repeat=2)
           if u == v or (v[0] == 'I' and
               ((u[0] == 'P' and (v[1], u[1]) in lt and (u[1], v[2]) in lt)
                or (u[0] == 'I' and base_le(v[1], u[1]) and base_le(u[2], v[2]))))}
    pos = {(u, v) for u, v in product(symbols, repeat=2)
           if u != v and all(base_le(a, b) for a, b in product(endpoints(u), endpoints(v)))}
    orth = pos | {(v, u) for u, v in pos}
    for relation in (incidence, rho):
        assert all((u, u) in relation for u in symbols)
        assert all(u == v or (v, u) not in relation for u, v in relation)
        assert all((u, w) in relation for u, v in relation for vv, w in relation if v == vv)
    assert all((u, w) in pos for u, v in pos for vv, w in pos if v == vv)
    assert all((u, u) not in orth for u in symbols)
    lower = {v: {u for u in symbols if (u, v) in incidence} for v in symbols}
    for u, v in product(symbols, repeat=2):
        assert sum((u, z) in rho for z in lower[v]) <= 1
        if (u, v) in rho:
            assert all(any((up, vp) in rho for vp in lower[v]) for up in lower[u])
        if (u, v) in orth:
            assert all((up, vp) in orth for up, vp in product(symbols, repeat=2)
                       if (up, u) in rho and (vp, v) in rho)
    assert all(u == v or (u, v) in orth for x in symbols for u, v in product(lower[x], repeat=2))
    faithful = all(((u, v) in orth) == (not any((w, u) in rho and (w, v) in rho for w in symbols))
                   for u, v in product(symbols, repeat=2))
    assert faithful == (len(lt) == n*(n-1)//2)
    # Lieux are minimal for FULL refinement, not merely for rho.
    full_refinement = {(u, v) for u, v in product(symbols, repeat=2)
                       if any((u, z) in rho for z in lower[v])}
    lieux = {v for v in symbols if all(u == v for u in symbols if (u, v) in full_refinement)}
    assert lieux == {('P', x) for x in range(n)}
    rho_minima = {v for v in symbols if all(u == v for u in symbols if (u, v) in rho)}
    for u in rho_minima-lieux:
        assert u[0] == 'I' and not any((u[1], x) in lt and (x, u[2]) in lt for x in range(n))
        assert (('P', u[1]), u) in full_refinement
    universe = frozenset(symbols)
    polar = lambda a: frozenset(u for u in symbols if all((u, v) in orth for v in a))
    closed_sets = {universe}
    for u in symbols:
        neighbourhood = polar({u})
        closed_sets |= {c & neighbourhood for c in tuple(closed_sets)}
    all_lieu_supports_atomic = True
    isolated = {x for x in range(n) if not any((x, y) in lt or (y, x) in lt for y in range(n))}
    for u in lieux:
        support = polar(polar({u}))
        atomic = not any(c and c < support for c in closed_sets)
        all_lieu_supports_atomic &= atomic
        assert support == (universe if u[1] in isolated else frozenset({u}))
    assert all_lieu_supports_atomic == (not lt or not isolated)
    prefigures = figures = 0
    for mask in range(1 << len(symbols)):
        f = {u for i, u in enumerate(symbols) if mask >> i & 1}
        if not all((u, v) in orth for u, v in combinations(f, 2)):
            continue
        prefigures += 1
        closed = set().union(*(lower[u] for u in f))
        assert all((u, v) in orth for u, v in combinations(closed, 2))
        if closed == f:
            figures += 1
    return len(symbols), prefigures, figures, faithful, all_lieu_supports_atomic, len(rho_minima-lieux)


if __name__ == '__main__':
    started = perf_counter()
    records = []
    for n in range(5):
        count = symbols = prefigures = figures = faithful = atoms = excluded = 0
        for lt in natural_posets(n):
            m, p, f, t, a, e = check(n, lt)
            count += 1; symbols += m; prefigures += p; figures += f; faithful += t
            atoms += a; excluded += e
        records.append({'base_points': n, 'naturally_labelled_orders': count,
                        'symbols_checked': symbols, 'prefigures_checked': prefigures,
                        'figures_checked': figures, 'faithful_orders': faithful,
                        'all_lieu_supports_atomic_orders': atoms,
                        'rho_only_minima_correctly_excluded_from_lieux': excluded})
    print(json.dumps({'records': records, 'all_assertions_passed': True,
                      'runtime_seconds': perf_counter()-started}, indent=2))
