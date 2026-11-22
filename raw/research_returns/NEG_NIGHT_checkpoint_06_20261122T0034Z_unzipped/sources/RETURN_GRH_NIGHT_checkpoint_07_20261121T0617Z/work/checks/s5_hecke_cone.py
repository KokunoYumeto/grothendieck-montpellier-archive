"""Exact finite-character enumeration; numerical optimization is exploratory."""
from itertools import permutations, product, combinations
from pathlib import Path
import json
import math
import numpy as np
import sympy as sp
from scipy.optimize import milp, Bounds, LinearConstraint, linprog

out = Path(__file__).resolve().parent
perms = list(permutations(range(5)))
index = {p: i for i, p in enumerate(perms)}
size = len(perms)
identity = index[tuple(range(5))]
mul = [[index[tuple(p[q[k]] for k in range(5))] for q in perms] for p in perms]
inv = [next(j for j in range(size) if mul[i][j] == identity) for i in range(size)]

def generated(gs):
    seen = {identity}
    queue = [identity]
    for x in queue:
        for g in gs:
            y = mul[x][g]
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return frozenset(seen)

groups = [(frozenset({identity}), ())]
known = {groups[0][0]}
for subgroup, gs in groups:
    for g in range(size):
        if g in subgroup:
            continue
        enlarged = generated(gs + (g,))
        if enlarged not in known:
            known.add(enlarged)
            groups.append((enlarged, gs + (g,)))
assert len(groups) == 156

reps = []
conjugates_seen = set()
for subgroup, gs in sorted(groups, key=lambda x: (len(x[0]), sorted(x[0]))):
    if subgroup in conjugates_seen:
        continue
    reps.append((subgroup, gs))
    for g in range(size):
        conjugates_seen.add(frozenset(mul[mul[g][h]][inv[g]] for h in subgroup))
assert len(conjugates_seen) == 156

def element_order(g):
    x = identity
    for i in range(1, 61):
        x = mul[x][g]
        if x == identity:
            return i
    raise AssertionError('order')

orders = [element_order(g) for g in range(size)]
chars = []
cycle_types = []
for i, p in enumerate(perms):
    fixed = sum(j == p[j] for j in range(5))
    v = fixed - 1
    p2 = perms[mul[i][i]]
    v2 = sum(j == p2[j] for j in range(5)) - 1
    inversions = sum(p[j] > p[k] for j in range(5) for k in range(j + 1, 5))
    sign = (-1) ** inversions
    w = (v * v + v2) // 2 - 1 - v
    chars.append([1, sign, v, sign * v, w, sign * w, (v * v - v2) // 2])
    seen = set()
    cycles = []
    for j in range(5):
        if j not in seen:
            x = j
            n = 0
            while x not in seen:
                seen.add(x)
                n += 1
                x = p[x]
            cycles.append(n)
    cycle_types.append(tuple(sorted(cycles, reverse=True)))
X = np.array(chars, dtype=int)
assert np.array_equal(X.T @ X, 120 * np.eye(7, dtype=int))

z = sp.Symbol('z')
phi = sp.Poly(sp.cyclotomic_poly(60, z), z, domain=sp.ZZ)
reductions = []
for k in range(60):
    rem = sp.rem(sp.Poly(z**k, z), phi)
    reductions.append([int(rem.nth(j)) for j in range(phi.degree())])
reductions = np.array(reductions, dtype=int)

rows = {}
subgroup_data = []
for subgroup, initial_gs in reps:
    gs = initial_gs
    if len(subgroup) == 1:
        gs = ()
    else:
        found = False
        for r in (1, 2):
            for trial in combinations(sorted(subgroup - {identity}), r):
                if generated(trial) == subgroup:
                    gs = trial
                    found = True
                    break
            if found:
                break
    commutators = [mul[mul[mul[a][b]][inv[a]]][inv[b]] for a in subgroup for b in subgroup]
    derived = generated(commutators)
    phase_choices = [range(0, 60, 60 // orders[g]) for g in gs]
    characters_found = 0
    for generator_phases in product(*phase_choices):
        phases = {identity: 0}
        queue = [identity]
        consistent = True
        for x in queue:
            for g, a in zip(gs, generator_phases):
                y = mul[x][g]
                value = (phases[x] + a) % 60
                if y in phases:
                    if phases[y] != value:
                        consistent = False
                        break
                else:
                    phases[y] = value
                    queue.append(y)
            if not consistent:
                break
        if not consistent:
            continue
        assert set(phases) == set(subgroup)
        assert all(phases[mul[a][b]] == (phases[a] + phases[b]) % 60 for a in subgroup for b in subgroup)
        characters_found += 1
        coeffs = []
        for j in range(7):
            reduced = sum((chars[g][j] * reductions[-phases[g] % 60] for g in subgroup), start=np.zeros(phi.degree(), dtype=int))
            assert not np.any(reduced[1:])
            assert reduced[0] % len(subgroup) == 0
            coeffs.append(int(reduced[0] // len(subgroup)))
        assert all(c >= 0 for c in coeffs)
        assert sum(c * d for c, d in zip(coeffs, [1, 1, 4, 4, 5, 5, 6])) == 120 // len(subgroup)
        rows.setdefault(tuple(coeffs), []).append(dict(order=len(subgroup), generators=[list(perms[g]) for g in gs], phases=list(generator_phases)))
    assert characters_found == len(subgroup) // len(derived)
    subgroup_data.append(dict(order=len(subgroup), generators=[list(perms[g]) for g in gs], linear_characters=characters_found))

patterns = sorted(rows)
matrix = np.array(patterns, dtype=float)
bounds = Bounds([0, 0, 0, 0, -np.inf, -np.inf, 0], [np.inf] * 7)
q = np.array([0, 0, 4, 4, 5, 5, 6], dtype=float)
constraint = LinearConstraint(matrix, np.zeros(len(patterns)), np.full(len(patterns), np.inf))
exploration = []
for negative in (4, 5):
    upper = np.full(7, np.inf)
    upper[negative] = -1
    r = milp(q, integrality=np.ones(7), bounds=Bounds(bounds.lb, upper), constraints=constraint, options={'time_limit': 30})
    exploration.append(dict(negative_coordinate=negative, success=bool(r.success), minimum=float(r.fun) if r.fun is not None else None, witness=r.x.tolist() if r.x is not None else None, message=r.message))
certificate = dict(character_names=['1', 'sign', '4', '4sign', '5', '5sign', '6'], group_order=120, subgroup_count=len(groups), conjugacy_representatives=len(reps), subgroup_data=subgroup_data, character_table={str(c): chars[cycle_types.index(c)] for c in sorted(set(cycle_types))}, induced_linear_patterns=[dict(coefficients=list(p), realizations=rows[p]) for p in patterns], exploratory_integer_optimization=exploration)
(out / 's5_hecke_cone.json').write_text(json.dumps(certificate, indent=2) + '\n')
print(json.dumps(dict(subgroups=len(groups), classes=len(reps), patterns=len(patterns), optimization=exploration), indent=2))
print('PATTERNS')
for p in patterns:
    print(p)
