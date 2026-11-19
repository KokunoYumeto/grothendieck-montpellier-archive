# Checks for the reading of 156-8 (reader C: Claude Opus 5.5 at effort max, sub-agent of a6d42bf6fe2b0d8a8), horizontal sweep 3, 19 Nov 2026.
# run: python -I -B 156-8_checks.py
import itertools
def closure(rel, els):  # reflexive-transitive closure of a set of pairs
    R = set(rel) | {(x, x) for x in els}
    ch = True
    while ch:
        ch = False
        for (a, b) in list(R):
            for (c, d) in list(R):
                if b == c and (a, d) not in R: R.add((a, d)); ch = True
    return R
def magasin_from_circ(M, le, oo, circ):
    """M list; le, oo: sets of pairs (orders, reflexive); circ: symmetric set of pairs. Returns dict of checks."""
    below = {X: [Y for Y in M if (Y, X) in le] for X in M}
    ll = {(X, Y) for X in M for Y in M if any((X, Yp) in oo and (Yp, Y) in le for Yp in M)}  # (*) X << Y iff X <<o Y' <= Y
    out = {}
    out['Mag3a'] = all((Y, X) in circ and X != Y for (X, Y) in circ)
    out['Mag3b'] = all((Xp, Yp) in circ for (X, Y) in circ for Xp in M for Yp in M if (Xp, X) in oo and (Yp, Y) in oo)
    out['Mag4_two_strata'] = all((Y, Z) in circ for X in M for Y in below[X] for Z in below[X] if Y != Z)
    out['Mag4_comparable'] = all((Y, X) in circ for X in M for Y in below[X] if Y != X)
    return out
# 1. Proposition-Scholie of 156-8/16-17: (<=, <<) with Mag 1, Mag 2, Mog L1 and || on lieux with div 3, div 4 need not give Mag 3 b.
M = ['x', 'y', 'Z', 'Xp', 'X']
le = closure({('Z', 'X')}, M)
ll = closure({('x', 'Z'), ('x', 'Xp'), ('Xp', 'X'), ('y', 'Xp'), ('Z', 'X')}, M)
def lst(X, Y):  # least element of Y~^X
    S = [Z for Z in M if (Z, Y) in le and (X, Z) in ll]
    m = [Z for Z in S if all((Z, W) in le for W in S)]
    return m[0] if m else None
mag2 = all(lst(X, Y) is not None for X in M for Y in M if (X, Y) in ll)
oo = {(X, Y) for X in M for Y in M if (X, Y) in ll and lst(X, Y) == Y}
lieux = [X for X in M if all(not ((Y, X) in ll and Y != X) for Y in M)]
ombo = {X: [x for x in lieux if (x, X) in oo] for X in M}
par = {('x', 'y'), ('y', 'x')}
div4 = all((y, z) in par for X in M for Y in M for Z in M if (Y, X) in le and (Z, X) in le and Y != Z for y in ombo[Y] for z in ombo[Z])
circ = {(X, Y) for X in M for Y in M if all((a, b) in par for a in ombo[X] for b in ombo[Y])}
r = magasin_from_circ(M, le, oo, circ)
print('1. Prop-Scholie 156-8/16-17 countermodel: Mag2', mag2, '| lieux', lieux, '| MogL1', all(ombo[X] for X in M), '| div4', div4,
      '| <<o transitive', all((a, c) in oo for (a, b) in oo for (b2, c) in oo if b == b2), '| derived |o|:', r)
# 2. Mag 4' in the comparable form (156-8/31) does not give Mag 4: maquette y, z < X, |o| = {y-X, z-X}
M = ['y', 'z', 'X']; le = closure({('y', 'X'), ('z', 'X')}, M); oo = closure(set(), M)
circ = {('y', 'X'), ('X', 'y'), ('z', 'X'), ('X', 'z')}
print('2. Mag 4 comparable-form countermodel:', magasin_from_circ(M, le, oo, circ))
# 3. Faithful magasins (|o| = no common <<o-lower bound): supports form the regular-open algebra of (M, <<o), hence Boolean; Axiome supp 1 holds.
def supports_check(M, le, oo):
    circ = {(X, Y) for X in M for Y in M if not any((Z, X) in oo and (Z, Y) in oo for Z in M)}
    cos = lambda A: frozenset(Y for Y in M if all((X, Y) in circ for X in A))
    sup = lambda A: cos(cos(A))
    Sig = {sup(frozenset(A)) for k in range(len(M) + 1) for A in itertools.combinations(M, k)}
    join = lambda a, b: sup(a | b)
    distrib = all(a & join(b, c) == join(a & b, a & c) for a in Sig for b in Sig for c in Sig)
    below = {X: [Y for Y in M if (Y, X) in le] for X in M}
    figs = [F for k in range(len(M) + 1) for F in itertools.combinations(M, k)
            if all(Y in F for X in F for Y in below[X]) and all((X, Y) in circ for X in F for Y in F if X != Y)]
    ax = all(sup(frozenset(F)) & cos(frozenset(P)) == sup(frozenset(F) - frozenset(P))
             for F in figs for k in range(len(F) + 1) for P in itertools.combinations(F, k))
    return len(Sig), distrib, ax, magasin_from_circ(M, le, oo, circ)
# 3a. all posets (M, <<o) on 4 points with <= discrete (every such datum is a faithful magasin)
M = [0, 1, 2, 3]; pairs = [(a, b) for a in M for b in M if a < b]; seen = set(); bad = 0; n = 0
for k in range(len(pairs) + 1):
    for rel in itertools.combinations(pairs, k):
        oo = closure(rel, M)
        if frozenset(oo) in seen: continue
        seen.add(frozenset(oo)); n += 1
        s, d, a, _ = supports_check(M, closure(set(), M), oo)
        if not (d and a): bad += 1
print('3a. faithful magasins with discrete <=, (M,<<o) a poset on 4 labelled points:', n, 'orders checked, failures of distributivity or Axiome supp 1:', bad)
# 3b. the magasin of a finite total order {0<1<2<3} (156-8/90-92): P_x, S_ab
L = [0, 1, 2, 3]; M = [('P', x) for x in L] + [('S', a, b) for a in L for b in L if a < b]
le = closure({(('P', a), ('S', a, b)) for a in L for b in L if a < b} | {(('P', b), ('S', a, b)) for a in L for b in L if a < b}, M)
oo = closure({(('P', x), ('S', a, b)) for x in L for a in L for b in L if a < x < b} |
             {(('S', a, b), ('S', c, d)) for a in L for b in L for c in L for d in L if a < b and c < d and c <= a and b <= d}, M)
def circ_pos(X, Y):
    if X[0] == 'P' and Y[0] == 'P': return X[1] != Y[1]
    if X[0] == 'P': return X[1] <= Y[1] or X[1] >= Y[2]
    if Y[0] == 'P': return circ_pos(Y, X)
    return X[2] <= Y[1] or Y[2] <= X[1]
circ = {(X, Y) for X in M for Y in M if circ_pos(X, Y)}
faithful = all(((X, Y) in circ) == (not any((Z, X) in oo and (Z, Y) in oo for Z in M)) for X in M for Y in M)
print('3b. magasin of {0<1<2<3}: Mag 3-4', magasin_from_circ(M, le, oo, circ), '| faithful', faithful, '| supports (count, distributive, Axiome supp 1):', supports_check(M, le, oo)[:3])
# 4. magasin of a non-total order: the "ficelle a deux brins" type, L = {a<b, c<d} product-free: two incomparable chains a<b, c<d
L = ['a', 'b', 'c', 'd']; lt = {('a', 'b'), ('c', 'd')}
M = [('P', x) for x in L] + [('S', x, y) for (x, y) in lt]
le = closure({(('P', x), ('S', x, y)) for (x, y) in lt} | {(('P', y), ('S', x, y)) for (x, y) in lt}, M)
oo = closure(set(), M)  # no a<x<b, no nested segments
comp = lambda x, y: (x, y) in lt or (y, x) in lt
def cp(X, Y):
    if X[0] == 'P' and Y[0] == 'P': return comp(X[1], Y[1])
    if X[0] == 'P': return X[1] == Y[1] or X[1] == Y[2] or ((X[1], Y[1]) in lt) or ((Y[2], X[1]) in lt)
    if Y[0] == 'P': return cp(Y, X)
    return (X[2], Y[1]) in lt or X[2] == Y[1] or (Y[2], X[1]) in lt or Y[2] == X[1]
circ = {(X, Y) for X in M for Y in M if X != Y and cp(X, Y)}
print('4. magasin of two incomparable chains a<b, c<d: Mag 3-4', magasin_from_circ(M, le, oo, circ))
