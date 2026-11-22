#!/usr/bin/env python3
"""Exact finite PL graph-code certificate for B=point, 0<=q<=2.

All arithmetic uses fractions.Fraction.  A q-code consists of full-dimensional
graph simplices for homeomorphisms I x Delta^q -> I x Delta^q.  This executable
checks a useful triangulated rational subclass of the general algebraic graph
syntax in A131; it does NOT claim to implement arbitrary RCF QE or prove the
infinite homotopy theorem.  No numeric tolerances or isotopy oracle are used.

Coordinates are (x,t_1,...,t_q,x',t'_1,...,t'_q), with t_0=1-sum(t_i).
The projections must be nondegenerate triangulations of the entire prism.
Their exact volumes, disjoint interiors, and overlap agreement certify both
bijections.  Composition constructs the actual common polyhedral refinement.
Faces and degeneracies compute affine preimages of cells and triangulate them.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import factorial
from time import perf_counter
import json


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def rank(rows):
    a = [list(r) for r in rows]
    if not a:
        return 0
    r = 0
    for j in range(len(a[0])):
        k = next((i for i in range(r, len(a)) if a[i][j]), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        p = a[r][j]
        a[r] = [v/p for v in a[r]]
        for i in range(len(a)):
            if i != r and a[i][j]:
                c = a[i][j]
                a[i] = [u-c*v for u, v in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def solve(a, b):
    n = len(a)
    a = [list(r)+[v] for r, v in zip(a, b)]
    for j in range(n):
        k = next((i for i in range(j, n) if a[i][j]), None)
        if k is None:
            return None
        a[j], a[k] = a[k], a[j]
        p = a[j][j]
        a[j] = [v/p for v in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                c = a[i][j]
                a[i] = [u-c*v for u, v in zip(a[i], a[j])]
    return tuple(a[i][-1] for i in range(n))


def det(a):
    a = [list(r) for r in a]
    d = Q(1)
    for j in range(len(a)):
        k = next((i for i in range(j, len(a)) if a[i][j]), None)
        if k is None:
            return Q(0)
        if k != j:
            a[j], a[k] = a[k], a[j]
            d = -d
        p = a[j][j]
        d *= p
        for i in range(j+1, len(a)):
            c = a[i][j]/p
            a[i] = [u-c*v for u, v in zip(a[i], a[j])]
    return d


def dim(vertices):
    if not vertices:
        return -1
    v = vertices[0]
    return rank([tuple(x-y for x, y in zip(w, v)) for w in vertices[1:]])


def domain_ineq(q):
    d = q+1
    out = []
    for j in range(d):
        a = tuple(Q(-1 if i == j else 0) for i in range(d))
        out.append((a, Q(0)))
    out.append((tuple(Q(i == 0) for i in range(d)), Q(1)))
    if q:
        out.append((tuple(Q(i > 0) for i in range(d)), Q(1)))
    return tuple(out)


def inside(v, inequalities):
    return all(dot(a, v) <= b for a, b in inequalities)


def vertices_of(inequalities, d):
    """All vertices of a bounded rational polyhedron, any affine dimension."""
    out = set()
    for rows in combinations(inequalities, d):
        v = solve([a for a, b in rows], [b for a, b in rows])
        if v is not None and inside(v, inequalities):
            out.add(v)
    return tuple(sorted(out))


def simplex_ineq(vertices):
    """H representation by nonnegative affine barycentric coordinates."""
    d = len(vertices[0])
    a = [tuple(v)+(Q(1),) for v in vertices]
    out = []
    for j in range(d+1):
        c = solve(a, [Q(i == j) for i in range(d+1)])
        if c is None:
            raise ValueError('degenerate simplex')
        out.append((tuple(-x for x in c[:-1]), c[-1]))
    return tuple(out)


def triangulate(inequalities, d, vertices=None):
    """Exact pulling triangulation, using the complete finite face poset."""
    vv = vertices if vertices is not None else vertices_of(inequalities, d)
    if dim(vv) < d:
        return []
    full = frozenset(range(len(vv)))
    faces = {full}
    for a, b in inequalities:
        f = frozenset(i for i, v in enumerate(vv) if dot(a, v) == b)
        if f:
            faces.add(f)
    changed = True
    while changed:
        changed = False
        for f, g in combinations(tuple(faces), 2):
            h = f & g
            if h and h not in faces:
                faces.add(h)
                changed = True
    dims = {f: dim(tuple(vv[i] for i in sorted(f))) for f in faces}

    def pull(f):
        k = dims[f]
        v = min(f)
        if k == 0:
            return [(vv[v],)]
        out = []
        for h in sorted(faces, key=lambda h: tuple(sorted(h))):
            if h < f and dims[h] == k-1 and v not in h:
                out.extend((vv[v],)+s for s in pull(h))
        return out

    return pull(full)


def affine(source, target):
    a = [tuple(v)+(Q(1),) for v in source]
    cc = [solve(a, [v[j] for v in target]) for j in range(len(target[0]))]
    if any(c is None for c in cc):
        raise ValueError('degenerate affine source')
    return tuple(cc)


def evaluate(coeff, v):
    return tuple(dot(c[:-1], v)+c[-1] for c in coeff)


def volume(vv):
    d = len(vv[0])
    return abs(det([tuple(x-y for x, y in zip(v, vv[0])) for v in vv[1:]]))/factorial(d)


def project(simplex, d, target=False):
    return tuple(v[d:] if target else v[:d] for v in simplex)


def bbox_disjoint(vv, ww):
    return any(max(v[j] for v in vv) < min(w[j] for w in ww)
               or max(w[j] for w in ww) < min(v[j] for v in vv)
               for j in range(len(vv[0])))


def deduplicate(code):
    return tuple(sorted(set(tuple(sorted(s)) for s in code)))


def validate(code, q):
    """Returns a mathematical rejection reason, or exact projection counts."""
    d = q+1
    code = deduplicate(code)
    if not code:
        return {'valid': False, 'reason': 'empty graph'}
    for s in code:
        if len(s) != d+1 or any(len(v) != 2*d for v in s):
            return {'valid': False, 'reason': 'wrong finite simplex format'}
        for v in s:
            if v[1:d] != v[d+1:]:
                return {'valid': False, 'reason': 'parameter not preserved'}
            if not inside(v[:d], domain_ineq(q)) or not inside(v[d:], domain_ineq(q)):
                return {'valid': False, 'reason': 'vertex outside domain'}
            if (v[0] == 0) != (v[d] == 0) or (v[0] == 1) != (v[d] == 1):
                return {'valid': False, 'reason': 'bottom/top condition fails'}
    counts = []
    for target in (False, True):
        cells = [project(s, d, target) for s in code]
        if any(dim(vv) != d for vv in cells):
            return {'valid': False, 'reason': 'degenerate projection'}
        ineq = [simplex_ineq(vv) for vv in cells]
        maps = [affine(project(s, d, target), project(s, d, not target)) for s in code]
        expected = Q(1, factorial(q))
        total = sum((volume(vv) for vv in cells), Q(0))
        if total != expected:
            return {'valid': False, 'reason': 'projection volume mismatch', 'volume': str(total)}
        count = 0
        for i, j in combinations(range(len(cells)), 2):
            if bbox_disjoint(cells[i], cells[j]):
                continue
            vv = vertices_of(ineq[i]+ineq[j], d)
            if dim(vv) == d:
                return {'valid': False, 'reason': 'projection interiors overlap'}
            if any(evaluate(maps[i], v) != evaluate(maps[j], v) for v in vv):
                return {'valid': False, 'reason': 'graph disagrees on overlap'}
            count += bool(vv)
        counts.append(count)
    return {'valid': True, 'simplices': len(code), 'dimension': d,
            'domain_volume': str(Q(1, factorial(q))), 'intersections': counts}


def inverse(code, q):
    d = q+1
    return deduplicate(tuple(tuple(v[d:]+v[:d] for v in s) for s in code))


def equal(code_a, code_b, q):
    """Graph equality of valid codes by their exact common subdivision."""
    d = q+1
    for s, t in product(code_a, code_b):
        a, b = project(s, d), project(t, d)
        if bbox_disjoint(a, b):
            continue
        vv = vertices_of(simplex_ineq(a)+simplex_ineq(b), d)
        ma, mb = affine(a, project(s, d, True)), affine(b, project(t, d, True))
        if any(evaluate(ma, v) != evaluate(mb, v) for v in vv):
            return False
    return True


def compose(g, h, q):
    """The graph of g after h, with an actual rational common refinement."""
    d = q+1
    out = []
    for sh, sg in product(h, g):
        middle_h, middle_g = project(sh, d, True), project(sg, d)
        if bbox_disjoint(middle_h, middle_g):
            continue
        inequalities = simplex_ineq(middle_h)+simplex_ineq(middle_g)
        vv = vertices_of(inequalities, d)
        if dim(vv) < d:
            continue
        back = affine(middle_h, project(sh, d))
        forward = affine(middle_g, project(sg, d, True))
        for cell in triangulate(inequalities, d, vv):
            out.append(tuple(evaluate(back, v)+evaluate(forward, v) for v in cell))
    return deduplicate(out)


def pullback(code, q, alpha):
    """All simplicial operators: alpha:[m]->[q] is nondecreasing."""
    if list(alpha) != sorted(alpha) or min(alpha) < 0 or max(alpha) > q:
        raise ValueError('not an order-preserving simplex map')
    m = len(alpha)-1
    d, e = q+1, m+1
    # Old coordinates as affine functions of new (x,s_1,...,s_m).
    phi = [(Q(1),)+(Q(0),)*m+(Q(0),)]
    for j in range(1, q+1):
        phi.append((Q(0),)+tuple(Q(alpha[k] == j)-Q(alpha[0] == j)
                                  for k in range(1, m+1))+(Q(alpha[0] == j),))
    out = []
    for s in code:
        src, dst = project(s, d), project(s, d, True)
        mp = affine(src, dst)
        inequalities = list(domain_ineq(m))
        for a, b in simplex_ineq(src):
            coeff = tuple(sum((a[j]*phi[j][k] for j in range(d)), Q(0)) for k in range(e))
            constant = sum((a[j]*phi[j][-1] for j in range(d)), Q(0))
            inequalities.append((coeff, b-constant))
        vv = vertices_of(inequalities, e)
        if dim(vv) < e:
            continue
        for cell in triangulate(tuple(inequalities), e, vv):
            out.append(tuple(v+(evaluate(mp, evaluate(phi, v))[0],)+v[1:] for v in cell))
    return deduplicate(out)


def identity(q):
    return tuple(tuple(v+v for v in s) for s in triangulate(domain_ineq(q), q+1))


def min_family(q, epsilon=Q(1, 2)):
    """h(x,t)=x+epsilon*min(x,1-x,t_0,...,t_q), q>=1."""
    d = q+1
    forms = [(Q(1),)+(Q(0),)*q+(Q(0),),
             (Q(-1),)+(Q(0),)*q+(Q(1),)]
    forms.append((Q(0),)+(Q(-1),)*q+(Q(1),))
    for j in range(1, q+1):
        forms.append(tuple(Q(i == j) for i in range(d))+(Q(0),))
    out = []
    for f in forms:
        inequalities = list(domain_ineq(q))
        for g in forms:
            inequalities.append((tuple(a-b for a, b in zip(f[:-1], g[:-1])), g[-1]-f[-1]))
        for s in triangulate(tuple(inequalities), d):
            out.append(tuple(v+(v[0]+epsilon*(dot(f[:-1], v)+f[-1]),)+v[1:] for v in s))
    return deduplicate(out)


def subdivide(code):
    """Stellar subdivision at the exact barycenter of each source simplex."""
    out = []
    for s in code:
        c = tuple(sum((v[j] for v in s), Q(0))/len(s) for j in range(len(s[0])))
        out.extend((c,)+s[:i]+s[i+1:] for i in range(len(s)))
    return deduplicate(out)


def run():
    start = perf_counter()
    tests = []

    def check(name, condition, details=None):
        assert condition, (name, details)
        tests.append({'name': name, 'pass': True, 'details': details})

    id0, id1, id2 = (identity(q) for q in range(3))
    for q, code in enumerate((id0, id1, id2)):
        result = validate(code, q)
        check('identity_q'+str(q), result['valid'], result)
    h = min_family(1)
    result = validate(h, 1)
    check('joint_PL_min_family_q1', result['valid'], result)
    check('family_nonidentity', not equal(h, id1, 1))
    hinv = inverse(h, 1)
    check('inverse_valid', validate(hinv, 1)['valid'])
    left = compose(hinv, h, 1)
    right = compose(h, hinv, 1)
    check('inverse_after_family', validate(left, 1)['valid'] and equal(left, id1, 1), len(left))
    check('family_after_inverse', validate(right, 1)['valid'] and equal(right, id1, 1), len(right))
    hh = compose(h, h, 1)
    check('composition_refinement_valid', validate(hh, 1)['valid'], len(hh))
    check('composition_nonidentity', not equal(hh, id1, 1))
    hs = subdivide(h)
    check('subdivision_valid', validate(hs, 1)['valid'], len(hs))
    check('equality_after_subdivision', equal(h, hs, 1))
    for i, alpha in enumerate(((0,), (1,))):
        face = pullback(h, 1, alpha)
        check('q1_endpoint_face_'+str(i), validate(face, 0)['valid'] and equal(face, id0, 0))

    # A nontrivial 0-simplex and its actual degeneracy, not an identity-only test.
    f = (((Q(0), Q(0)), (Q(1, 2), Q(3, 4))),
         ((Q(1, 2), Q(3, 4)), (Q(1), Q(1))))
    check('nontrivial_interval_code', validate(f, 0)['valid'])
    sf = pullback(f, 0, (0, 0))
    check('degeneracy_s0_valid', validate(sf, 1)['valid'], len(sf))
    for i in (0, 1):
        back = pullback(sf, 1, (i,))
        check('d'+str(i)+'s0_equals_identity_operator', equal(back, f, 0))

    h2 = min_family(2)
    result = validate(h2, 2)
    check('joint_PL_min_family_q2', result['valid'], result)
    check('q2_family_nonidentity', not equal(h2, id2, 2))
    for i in range(3):
        face = pullback(h2, 2, tuple(j for j in range(3) if j != i))
        check('q2_all_faces_identity_'+str(i), validate(face, 1)['valid'] and equal(face, id1, 1), len(face))
    ss0 = pullback(sf, 1, (0, 0, 1))
    ss1 = pullback(sf, 1, (0, 1, 1))
    check('double_degeneracy_valid', validate(ss0, 2)['valid'] and validate(ss1, 2)['valid'])
    check('s0s0_equals_s1s0', equal(ss0, ss1, 2))

    # Five independently defective finite codes, each caught by a distinct gate.
    hole = h[:-1]
    result = validate(hole, 1)
    check('reject_hole', not result['valid'], result)
    wrong_parameter = []
    for s in h:
        wrong_parameter.append(tuple(v[:3]+(Q(2, 3),) if v[:2] == (Q(1, 2), Q(1, 2)) else v for v in s))
    result = validate(wrong_parameter, 1)
    check('reject_wrong_parameter', not result['valid'], result)
    folding = tuple(tuple(v[:2]+(Q(5, 4),)+v[3:] if v[:2] == (Q(1, 2), Q(1, 2)) else v for v in s) for s in h)
    result = validate(folding, 1)
    check('reject_outside_fold', not result['valid'], result)
    discontinuous = list(h)
    discontinuous[0] = tuple(v[:2]+(Q(2, 3),)+v[3:] if v[:2] == (Q(1, 2), Q(1, 2)) else v for v in discontinuous[0])
    result = validate(discontinuous, 1)
    check('reject_overlap_disagreement', not result['valid'], result)
    bad_bottom = tuple(tuple((v[0], v[1], Q(1, 8), v[3]) if v[0] == 0 else v for v in s) for s in h)
    result = validate(bad_bottom, 1)
    check('reject_bottom_motion', not result['valid'], result)

    return {'status': 'PASS', 'arithmetic': 'exact fractions.Fraction only',
            'scope': 'B=point; rational triangulated graph codes; q=0,1,2',
            'claims_not_tested': ['general real-algebraic QE', 'arbitrary finite K',
                                  'infinite Moore theorem', 'word-problem decision'],
            'tests': tests, 'test_count': len(tests),
            'elapsed_seconds': round(perf_counter()-start, 6)}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
