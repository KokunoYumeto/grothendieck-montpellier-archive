"""Direct determinant/permanent minor certificates for F-022 odd jets."""
from datetime import datetime, timezone
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import json
import sympy as sp


def indices(R, degree):
    return sorted((a for a in product(range(degree+1), repeat=R)
                   if sum(a) <= degree), key=lambda a: (sum(a), a))


def split(gamma, ell):
    R = len(gamma)
    k = sum(gamma)
    assert ell < k <= 2*ell
    occupied = [i for i, a in enumerate(gamma) if a]
    lo, hi = occupied[0], occupied[-1]
    alpha, beta = [0]*R, [0]*R
    if hi-lo >= 2:
        alpha[lo], beta[hi] = 1, 1
        remaining = list(gamma)
        remaining[lo] -= 1
        remaining[hi] -= 1
        quota = ell-1
        for i, count in enumerate(remaining):
            take = min(count, quota)
            alpha[i] += take
            beta[i] += count-take
            quota -= take
        assert quota == 0
    elif lo == hi:
        alpha[lo], beta[lo] = ell, k-ell
    elif gamma[lo] > ell:
        beta[lo] = ell
        alpha = [g-b for g, b in zip(gamma, beta)]
    elif gamma[hi] > ell:
        alpha[hi] = ell
        beta = [g-a for g, a in zip(gamma, alpha)]
    else:
        alpha[hi], beta[lo] = gamma[hi], gamma[lo]
    alpha, beta = tuple(alpha), tuple(beta)
    assert tuple(a+b for a,b in zip(alpha,beta)) == gamma
    assert 1 <= sum(alpha) <= ell and 1 <= sum(beta) <= ell
    i = min(j for j, a in enumerate(alpha) if a)
    j = max(i for i, b in enumerate(beta) if b)
    assert j != (i+1) % R
    return alpha, beta


def build(R, ell):
    z = sp.symbols(f'z0:{R}')
    vertices = [('center',)] + [('core', i) for i in range(R)]
    monomials = indices(R, ell)
    vertices += [(side, a) for side in ('in', 'out')
                 for a in monomials if sum(a) >= 2]
    ids = {v: i for i, v in enumerate(vertices)}

    def node(side, a):
        if sum(a) == 1:
            j = a.index(1)
            return ids[('core', j if side == 'in' else (j-1) % R)]
        return ids[(side, a)]

    B = sp.zeros(len(vertices))
    for i in range(R):
        B[ids[('core', i)], 0] = z[i]
        B[0, ids[('core', i)]] = z[(i+1) % R]
    for a in monomials:
        if sum(a) < 2:
            continue
        for side in ('in', 'out'):
            occupied = [i for i, g in enumerate(a) if g]
            j = occupied[-1] if side == 'in' else occupied[0]
            parent = list(a)
            parent[j] -= 1
            parent = tuple(parent)
            source, target = node(side, a), node(side, parent)
            if side == 'out':
                source, target = target, source
            B[source, target] = z[j]
    assert B.rows == 2*comb(R+ell, ell)-(R+1)
    return B, z, node, ids[('core', 0)]


def minor_engine(A, signed):
    n = A.rows
    full = (1 << n)-1

    @lru_cache(None)
    def value(rows, cols):
        if not rows:
            return sp.Integer(1)
        active_rows = [i for i in range(n) if rows & (1 << i)]
        active_cols = [j for j in range(n) if cols & (1 << j)]
        i = min(active_rows,
                key=lambda a: sum(A[a, j] != 0 for j in active_cols))
        choices = [(position, j) for position, j in enumerate(active_cols)
                   if A[i, j] != 0]
        row_position = active_rows.index(i)
        result = 0
        for col_position, j in choices:
            sign = (-1)**(row_position+col_position) if signed else 1
            result += sign*A[i, j]*value(rows ^ (1 << i), cols ^ (1 << j))
        return sp.expand(result)

    return value, full


records = []
for R, ell in [(3, 1), (4, 1), (3, 2), (4, 2), (3, 3)]:
    B, z, node, fixed = build(R, ell)
    det, bits = minor_engine(sp.eye(B.rows)-B, True)
    per, _ = minor_engine(sp.eye(B.rows)+B, False)
    cycle_sum = sum(z[i]*z[(i+1) % R] for i in range(R))
    assert det(bits,bits) == 1-cycle_sum
    assert per(bits,bits) == 1+cycle_sum
    target = indices(R, 2*ell+1)
    used = {}
    distinct_cofactors = set()
    for gamma in target:
        reduced = list(gamma)
        multiplier = None
        if sum(gamma) == 2*ell+1:
            multiplier = next(i for i, g in enumerate(gamma) if g)
            reduced[multiplier] -= 1
        reduced = tuple(reduced)
        degree = sum(reduced)
        if degree == 0:
            i,j = 0,0
        elif degree <= ell:
            i,j = node('out', reduced),0
        else:
            alpha,beta = split(reduced,ell)
            i,j = node('out',beta),node('in',alpha)
        assert (i,j) != (fixed,fixed)
        cofactor_det = (-1)**(i+j)*det(bits ^ (1 << i), bits ^ (1 << j))
        cofactor_per = per(bits ^ (1 << i), bits ^ (1 << j))
        expected = sp.prod(z[a]**reduced[a] for a in range(R))
        assert sp.expand(cofactor_det-expected) == 0
        assert sp.expand(cofactor_per-expected) == 0
        key = (i,j,multiplier)
        assert key not in used or used[key] == gamma
        used[key] = gamma
        distinct_cofactors.add((i,j))
    assert len(used) == len(target) == comb(R+2*ell+1,2*ell+1)
    records.append({'R':R,'ell':ell,'matrix_size':B.rows,
                    'jet_order':2*ell+1,'identity_Jacobian_rank':len(target),
                    'direct_determinant_and_permanent_cofactors':len(distinct_cofactors),
                    'fixed_core_diagonal_avoided':True})

coverage = []
for R in range(3,9):
    for ell in range(1,5):
        count = 0
        for gamma in indices(R,2*ell):
            if sum(gamma) > ell:
                split(gamma,ell)
                count += 1
        coverage.append({'R':R,'ell':ell,'multisets':count})

result = {'finding':'F-022 shared-core odd jets',
          'date_utc':datetime.now(timezone.utc).isoformat(),
          'reviewer':'GPT-6 Astra Pro; effort not exposed; /root/positive_formulas',
          'run':'GCT_KRON_20261120','status':'PASS','matrix_checks':records,
          'finite_split_coverage':coverage,
          'scope':'Exact direct minors and finite multiset coverage supplement the complete arbitrary-parameter proof.'}
destination = Path(__file__).with_name('shared_core_jet_certificate.json')
destination.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','matrix_cases':len(records),
                  'ranks':[r['identity_Jacobian_rank'] for r in records],
                  'coverage_cases':len(coverage),
                  'multisets':sum(r['multisets'] for r in coverage),
                  'certificate':str(destination)}))
