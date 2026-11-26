#!/usr/bin/env python3
"""Exact checks of selected attached border-rank seeds, not a shortening search.

Input: ../inputs/rt_border_seeds.json.
Output: JSON certificate summary on stdout. All arithmetic is over Z or
Z[z,h]/(z^4-z^2+1,h^2-5). No floating-point arithmetic is used.
"""
import json
from collections import defaultdict
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
cfg = json.loads((ROOT / 'inputs/rt_border_seeds.json').read_text())


def z_reduce(n):
    p = {n: 1}
    for d in range(n, 3, -1):
        c = p.pop(d, 0)
        if c:
            p[d-2] = p.get(d-2, 0) + c
            p[d-4] = p.get(d-4, 0) - c
    return p


def ring_monomial(c=1, z=0, h=0):
    a = [0]*8
    for j, b in z_reduce(z).items():
        a[4*(h % 2)+j] += c*b*5**(h//2)
    return tuple(a)


ZERO = (0,)*8
ONE = ring_monomial()


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def mul(a, b):
    out = ZERO
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x and y:
                out = add(out, ring_monomial(x*y, i % 4+j % 4, i//4+j//4))
    return out


def sign_perm(p):
    return (-1)**sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))


def check_det_seed():
    vecs = []
    for row in cfg['det17']:
        v = [ZERO]*9
        for index, coefficient, zpow, hpow in row['entries']:
            v[index] = add(v[index], ring_monomial(coefficient, zpow, hpow))
        c = ZERO
        for coefficient, zpow, hpow in row['multiplier']:
            c = add(c, ring_monomial(coefficient, zpow, hpow))
        vecs.append((v, c))
    weights = cfg['weights']
    checked = nonzero = negative = 0
    for indices in product(range(9), repeat=3):
        exponent = sum(weights[i] for i in indices)
        if exponent > 0:
            continue
        checked += 1
        negative += exponent < 0
        value = ZERO
        for v, c in vecs:
            value = add(value, mul(c, mul(v[indices[0]], mul(v[indices[1]], v[indices[2]]))))
        rows = [i//3 for i in indices]
        cols = [i % 3 for i in indices]
        target = ZERO
        if exponent == 0 and len(set(rows)) == len(set(cols)) == 3:
            target = ring_monomial(40*sign_perm(rows)*sign_perm(cols))
            nonzero += 1
        assert value == target, (indices, exponent, value, target)
    return {'nonpositive_coordinates_checked': checked,
            'negative_coordinates_checked': negative,
            'nonzero_constant_coordinates': nonzero,
            'ring': 'Z[z,h]/(z^4-z^2+1,h^2-5)',
            'constant_tensor': '40*Det_3',
            'usable_characteristics_for_division': 'all except 2 and 5',
            'status': 'PASS'}


def check_squarefree18():
    labels = cfg['squarefree18']['labels']
    masks = [frozenset(s) for s in cfg['squarefree18']['cell_monomials']]
    targets = [frozenset(s) for s in cfg['squarefree18']['slice_monomials']]
    downset = {frozenset(labels[i] for i in range(4) if n & (1 << i)) for n in range(16)}
    downset |= {frozenset('z'), frozenset('xz')}
    checked = nonzero = negative = 0
    for i, j, k in product(range(10), range(11), range(11)):
        M, u, v = targets[i], masks[j], masks[k]
        coeff = sum((-1)**(len(M)-len(p)) for p in downset if u <= p and v <= p and p <= M)
        degree = len(u)+len(v)-len(M)
        expected = int(u | v == M)
        assert coeff == expected
        if coeff:
            assert degree == len(u & v) >= 0
        if degree < 0:
            negative += 1
            assert coeff == 0
        if degree == 0 and coeff:
            nonzero += 1
        checked += 1
    assert len(downset) == 18 and nonzero == 40
    return {'summands': len(downset), 'coordinates_checked': checked,
            'negative_exponent_coordinates_cancelled': negative,
            'nonzero_constant_coordinates': nonzero, 'status': 'PASS'}


def check_full19():
    """Multiply the actual nineteen Laurent pure tensors, not only the seed.

    First-factor labels 0..8 stand for cofactor minor kappa(c),kappa(r)
    for index 3*r+c. Label 9 is the added minor (01,03).
    Second-factor labels are the 16 row-major cells of a 4 by 4 matrix.
    """
    def shift(v, power, sign=1):
        return {(i,d+power): mul(ring_monomial(sign),c) for (i,d),c in v.items()}

    def plus(v, i, d, sign):
        out=dict(v)
        out[i,d]=add(out.get((i,d),ZERO),ring_monomial(sign))
        return {k:c for k,c in out.items() if c != ZERO}

    av=[]; bv=[]; cs=[]
    for row in cfg['det17']:
        a={}; b={}; c=ZERO
        for index, coefficient, zp, hp in row['entries']:
            r,j=divmod(index,3); d=cfg['weights'][index]
            va=ring_monomial(coefficient*(-1)**(r+j),zp,hp)
            vb=ring_monomial(coefficient,zp,hp)
            a[index,d]=add(a.get((index,d),ZERO),va)
            b[4*j+r,d]=add(b.get((4*j+r,d),ZERO),vb)
        for coefficient,zp,hp in row['multiplier']:
            c=add(c,ring_monomial(coefficient,zp,hp))
        av.append(a);bv.append(b);cs.append(c)
    terms=[(cs[l],av[l],bv[l],bv[l]) for l in range(17) if l not in (0,9)]
    X=shift(bv[0],5,-1);Y=shift(bv[9],4,-1)
    terms.extend([
        (ring_monomial(40),plus(shift(av[0],-10),9,-1,-1),X,X),
        (ring_monomial(40),plus(shift(av[9],-8),9,-1,1),Y,Y),
        (ring_monomial(40),{(9,-1):ONE},plus(X,7,1,1),plus(X,7,1,1)),
        (ring_monomial(-40),{(9,-1):ONE},plus(Y,3,1,1),plus(Y,3,1,1))])
    table={}
    for c,a,b,v in terms:
        for ((i,di),ai),((j,dj),bj),((k,dk),vk) in product(a.items(),b.items(),v.items()):
            key=(i,j,k,di+dj+dk)
            table[key]=add(table.get(key,ZERO),mul(c,mul(ai,mul(bj,vk))))
    negative=sum(d<0 for i,j,k,d in table)
    assert all(value==ZERO for (i,j,k,d),value in table.items() if d<0)
    constants={(i,j,k):v for (i,j,k,d),v in table.items() if d==0 and v!=ZERO}
    target={}
    for index in range(9):
        r,c=divmod(index,3)
        rows=[u for u in range(3) if u!=c]
        cols=[u for u in range(3) if u!=r]
        diagonal=(4*rows[0]+cols[0],4*rows[1]+cols[1])
        offdiag=(4*rows[0]+cols[1],4*rows[1]+cols[0])
        for j,k in (diagonal,diagonal[::-1]):target[index,j,k]=ring_monomial(40)
        for j,k in (offdiag,offdiag[::-1]):target[index,j,k]=ring_monomial(-40)
    for j,k in ((0,7),(7,0)):target[9,j,k]=ring_monomial(40)
    for j,k in ((4,3),(3,4)):target[9,j,k]=ring_monomial(-40)
    assert constants==target,(constants,target)
    assert len(terms)==19 and len(constants)==40
    return {'pure_summands':len(terms),'expanded_laurent_coordinates':len(table),
            'negative_coordinates_cancelled':negative,'constant_coordinates':len(constants),
            'constant_tensor':'40 times the ten specified 2-by-2-minor slices',
            'usable_characteristics_for_division':'all except 2 and 5','status':'PASS'}


def graph_curve(edges):
    # A point is represented by the set of nonzero t coefficients, with base e0.
    coefficients = defaultdict(lambda: defaultdict(int))
    for s, (i, j) in enumerate(edges):
        if i == 0:
            coefficients[(j,)][(s, -1)] += 1
            coefficients[()][(s, -1)] -= 1
        else:
            coefficients[(i, j)][(s, -2)] += 1
            coefficients[(i,)][(s, -2)] -= 1
            coefficients[(j,)][(s, -2)] -= 1
            coefficients[()][(s, -2)] += 1
    return {p: {term: c for term, c in co.items() if c}
            for p, co in coefficients.items()}


def check_graph_curve(edges):
    curve = graph_curve(edges)
    table = defaultdict(int)
    for p, coeff in curve.items():
        v = [(0, 0)] + [(i, 1) for i in p]
        for (s, degree), a in coeff.items():
            for (i, di), (j, dj) in product(v, repeat=2):
                table[s, i, j, degree+di+dj] += a
    table = {key: value for key, value in table.items() if value}
    for (s, i, j, degree), value in table.items():
        assert degree >= 0
        if degree == 0:
            assert (i, j) in (tuple(edges[s]), tuple(reversed(edges[s]))) and value == 1
    for s, (i, j) in enumerate(edges):
        assert table.get((s, i, j, 0)) == table.get((s, j, i, 0)) == 1
    return len(curve)


def check_product_curves():
    out = []
    for case in cfg['product_curves']:
        r = check_graph_curve(case['row_edges'])
        c = check_graph_curve(case['column_edges'])
        out.append({'slices': len(case['row_edges'])*len(case['column_edges']),
                    'pure_summands': r*c, 'status': 'PASS'})
    return out


result = {'determinant17_seed_for19_curve': check_det_seed(),
          'full19_minor_curve': check_full19(),
          'squarefree18_curve': check_squarefree18(),
          'product_curves': check_product_curves(),
          'scope': 'Verifies the specified finite seed coefficients. Does not certify a strict shortening or a price obstruction.'}
print(json.dumps(result, indent=2, sort_keys=True))
