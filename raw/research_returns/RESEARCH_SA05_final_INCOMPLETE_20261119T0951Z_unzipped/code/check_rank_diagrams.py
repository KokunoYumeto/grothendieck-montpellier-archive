"""Exact finite-dimensional checks for the proposed C6 diagram argument.

This checks two linear-algebra identities over Q. It neither tests a
geometric realization nor proves independence of ell or a motivic conjecture.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import random
import time
import sympy as sp

start = time.perf_counter()
rng = random.Random(202611190729)

def matrix(r, c):
    return sp.Matrix(r, c, lambda i, j: rng.randrange(-3, 4))

def unitriangular(n):
    return sp.eye(n) + sp.Matrix(n, n, lambda i, j: rng.randrange(-2, 3) if i < j else 0)

cohomology_checks = []
for case in range(48):
    bc, hc, pc, bd, hd, pd = [rng.randrange(0, 3) for _ in range(6)]
    nc, nd = bc + hc + pc, bd + hd + pd
    f = matrix(nd, nc)
    for i in range(bd, bd + hd):
        for j in range(bc):
            f[i, j] = 0
    for i in range(bd + hd, nd):
        for j in range(bc + hc):
            f[i, j] = 0
    expected = f[bd:bd + hd, bc:bc + hc].rank()
    dc = sp.zeros(pc, nc)
    for i in range(pc):
        dc[i, bc + hc + i] = 1
    dd = sp.zeros(nd, bd)
    for i in range(bd):
        dd[i, i] = 1
    sc, sd = unitriangular(nc), unitriangular(nd)
    f = sd * f * sc.inv()
    dc = dc * sc.inv()
    dd = sd * dd
    block = dc.row_join(sp.zeros(pc, bd)).col_join(f.row_join(dd))
    actual = block.rank() - dc.rank() - dd.rank()
    assert actual == expected
    cohomology_checks.append(dict(case=case, dimensions=[bc,hc,pc,bd,hd,pd], rank=int(actual)))

graph_checks = []
for case in range(48):
    nu, nz, nv = [rng.randrange(0, 5) for _ in range(3)]
    f, h, k, g = matrix(nz, nu), matrix(nv, nz), matrix(nv, nu), unitriangular(nz)
    r = (-f).row_join(g).row_join(sp.zeros(nz, nv)).col_join(
        (-k).row_join(-h).row_join(sp.eye(nv)))
    pi = sp.zeros(nv, nu + nz).row_join(sp.eye(nv))
    actual = r.col_join(pi).rank() - r.rank()
    expected = (h * g.inv() * f + k).rank()
    assert actual == expected
    # Add genuinely nonunique internal variables, absent from the constraints.
    extra = case % 3
    r_free = r.row_join(sp.zeros(r.rows, extra))
    pi_free = pi.row_join(sp.zeros(nv, extra))
    assert r_free.col_join(pi_free).rank() - r_free.rank() == expected
    graph_checks.append(dict(case=case, dimensions=[nu,nz,nv], free_internal_variables=extra, rank=int(actual)))

result = dict(
    utc=datetime.now(timezone.utc).isoformat(),
    scope='Exact rational linear algebra only; no geometric or motivic conjecture is tested.',
    seed=202611190729,
    cohomology_rank_cases=cohomology_checks,
    graph_constraint_cases=graph_checks,
    status='passed',
    seconds=round(time.perf_counter()-start,6),
    sympy_version=sp.__version__,
)
path=Path(__file__).with_name('check_rank_diagrams_output.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if not isinstance(v,list)},indent=2))
print('Passed 48 cohomology-rank cases and 48 graph cases, including nonunique internal variables.')
