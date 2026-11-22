#!/usr/bin/env python3
"""Finite diagnostic for a canonical pairing, not a uniform theorem.

Use the source toral kernel basis s_0,s_1, its dual modulo the Cartier
image, and the actual etale trace to remove arbitrary row/column bases.
No earlier program's output is overwritten or top-level run executed.
"""
from pathlib import Path
from time import perf_counter
import ast, itertools, json, random

started = perf_counter()
source = Path(__file__).with_name('post_CP16_etale_double_variation_probe.py')
nodes = []
for node in ast.parse(source.read_text()).body:
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'out' for t in node.targets):
        break
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'started' for t in node.targets):
        continue
    nodes.append(node)
ns = {'__file__': str(source.resolve())}
exec(compile(ast.Module(body=nodes, type_ignores=[]), str(source), 'exec'), ns)
for key in ['basis', 'cartier', 'multiply', 'rank', 'apply', 'stable_rank',
            'padd', 'pmul', 'ppow', 'nullspace', 'transpose',
            'coordinate_solver', 'toral', 'matrix']:
    globals()[key] = ns[key]
pairs, indices, b = ns['pairs'], ns['indices'], ns['b']
u, v = ns['u'], ns['v']
spairs = list(itertools.product(basis(6), basis(3)))
sindices = {x: i for i, x in enumerate(spairs)}
pull = []
for (i, j), z in spairs:
    a = pmul({(3, 0)}, pmul(ppow(u, i), ppow(v, j)))
    pull.append(sum(1 << indices[(x, z)] for x in a))
solvepull = coordinate_solver(pull)
tx = {(-1, 0)}
ty = {(-2, 1), (0, 0), (-1, 0), (-2, 0)}
tau = []
for (i, j), z in pairs:
    a = pmul({(6, 0)}, pmul(ppow(tx, i), ppow(ty, j)))
    tau.append(sum(1 << indices[(x, z)] for x in a))
assert all(apply(tau, apply(tau, 1 << j)) == 1 << j for j in range(b))
trace = [solvepull((1 << j) ^ tau[j]) for j in range(b)]
assert rank(trace) == 18

def independent_columns(cols):
    basiscols, source_indices = [], []
    for i, col in enumerate(cols):
        if rank(basiscols + [col]) > len(basiscols):
            basiscols.append(col)
            source_indices.append(i)
    return basiscols, source_indices

def right_inverse_on_image(cols):
    selected, ix = independent_columns(cols)
    coord = coordinate_solver(selected)
    def lift(x):
        c = coord(x)
        return sum(1 << ix[j] for j in range(len(ix)) if c >> j & 1)
    return lift

lifttrace = right_inverse_on_image(trace)

def smalltoral(s):
    ans = 0
    for j, ((i, h), z) in enumerate(spairs):
        if not (s >> j & 1):
            continue
        if (i + h) % 2:
            ans ^= 1 << j
        if h:
            ans ^= 1 << sindices[((i + 2, 0), z)]
    return ans

smallcoeff = []
for c, d in spairs:
    collist = []
    for a, z in spairs:
        col = 0
        for aa in cartier(multiply(a, c, True), True):
            for zz in cartier(multiply(z, d, False), False):
                col ^= 1 << sindices[(aa, zz)]
        collist.append(col)
    smallcoeff.append(collist)

def smallmatrix(s):
    cols = [0] * 18
    for j in range(18):
        if s >> j & 1:
            cols = [a ^ c for a, c in zip(cols, smallcoeff[j])]
    return cols

def determinant(cols):
    return ((cols[0] & 1) * ((cols[1] >> 1) & 1)) ^ (((cols[0] >> 1) & 1) * (cols[1] & 1))

records = []
rng = random.Random(202611191501)
for trial in range(300):
    s = rng.getrandbits(18)
    Cs = smallmatrix(s)
    sr, sequence = stable_rank(Cs)
    if sr != 16:
        continue
    r1 = smalltoral(s)
    R = [s ^ r1, r1]
    imageCs, _ = independent_columns(Cs)
    assert len(imageCs) == 16
    direct = coordinate_solver(R + imageCs)
    projection = lambda x: direct(x) & 3
    K = [sum(((projection(1 << j) >> i) & 1) << j for j in range(18)) for i in range(2)]
    assert all((ki & rj).bit_count() % 2 == (i == j) for i, ki in enumerate(K) for j, rj in enumerate(R))
    assert all(not ((ki & y).bit_count() % 2) for ki in K for y in Cs)
    pullK = [sum(((ki & tr).bit_count() % 2) << j for j, tr in enumerate(trace)) for ki in K]
    S = apply(pull, s)
    CA = matrix(S)
    q = [lifttrace(r) for r in R]
    vi = [solvepull(apply(CA, x)) for x in q]
    cup_alpha = [projection(x) for x in vi]
    lifts = right_inverse_on_image(Cs)
    corrected = []
    for x, y, ry in zip(q, vi, cup_alpha):
        stablepart = y ^ apply(R, ry)
        w = lifts(stablepart)
        corrected.append(x ^ apply(pull, w))
    assert all(apply(trace, x) == r for x, r in zip(corrected, R))
    assert all(apply(CA, x) == apply(pull, apply(R, ry)) for x, ry in zip(corrected, cup_alpha))
    variations = []
    for Ct in ns['coefficients']:
        cols = []
        for qj in corrected:
            y = apply(Ct, qj)
            cols.append(sum(((ki & y).bit_count() % 2) << i for i, ki in enumerate(pullK)))
        variations.append(cols)
    flat = [a | (c << 2) for a, c in variations]
    annihilators = [h for h in range(1, 16) if all((h & x).bit_count() % 2 == 0 for x in flat)]
    records.append({'trial': trial, 'source_bits': s,
                    'source_toral_kernel_basis': R,
                    'source_kernel_dual_basis': K,
                    'alpha_cup_columns_in_beta_basis': cup_alpha,
                    'alpha_cup_rank': rank(cup_alpha),
                    'alpha_cup_trace': (cup_alpha[0] & 1) ^ ((cup_alpha[1] >> 1) & 1),
                    'alpha_cup_determinant': determinant(cup_alpha),
                    'full_pulled_Cartier_rank': rank(CA),
                    'rank_formula_check': rank(CA) == 32 + rank(cup_alpha),
                    'variation_dimension': rank(flat),
                    'variation_annihilators': annihilators,
                    'all_variations': variations,
                    'all_symmetric': all(((d[0] >> 1) & 1) == (d[1] & 1) for d in variations),
                    'all_trace_zero': all((d[0] & 1) == ((d[1] >> 1) & 1) for d in variations)})
    if len(records) == 20:
        break

out = {'status': 'COMPLETED_FINITE_DIAGNOSTIC',
       'scope': 'Canonical beta-cup and etale-trace bases at twenty old F2 sources only. No uniform matrix symmetry asserted.',
       'records': records, 'elapsed_seconds': perf_counter() - started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({'samples': len(records),
                  'alpha_cup_traces': [r['alpha_cup_trace'] for r in records],
                  'alpha_cup_ranks': [r['alpha_cup_rank'] for r in records],
                  'rank_formula_checks': [r['rank_formula_check'] for r in records],
                  'all_symmetric': [r['all_symmetric'] for r in records],
                  'all_trace_zero': [r['all_trace_zero'] for r in records],
                  'annihilators': [r['variation_annihilators'] for r in records],
                  'elapsed_seconds': out['elapsed_seconds']}, indent=2))
