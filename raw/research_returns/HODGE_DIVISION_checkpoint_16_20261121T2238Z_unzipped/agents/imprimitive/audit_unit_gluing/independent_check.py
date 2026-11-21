#!/usr/bin/env python3
"""Independent exact arithmetic for UG and SF-E824, no author code imported.

Sparse integer multivariate polynomials check the generic chain identities.
An independent pair model of Q(sqrt2) checks the actual complete character.
Filtration, gluing and first-overlap arguments are proved in the report,
not inferred from these finite calculations.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib
import json
import time

start = time.perf_counter()
NVAR = 7  # x,y,b1,b2,c1,c2,P
ZERO = (0,)*NVAR


def con(a):
    return {} if a == 0 else {ZERO: a}


def var(i):
    e = [0]*NVAR
    e[i] = 1
    return {tuple(e): 1}


def add(*polys):
    out = {}
    for poly in polys:
        for mon, c in poly.items():
            out[mon] = out.get(mon, 0)+c
    return {m: c for m, c in out.items() if c}


def neg(p):
    return {m: -c for m, c in p.items()}


def mul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(x+y for x, y in zip(ma, mb))
            out[m] = out.get(m, 0)+ca*cb
    return {m: c for m, c in out.items() if c}


def mm(a, b):
    return [[add(*(mul(a[i][k], b[k][j]) for k in range(len(b))))
             for j in range(len(b[0]))] for i in range(len(a))]


def madd(a, b):
    return [[add(x, y) for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def smul(c, a):
    return [[mul(c, x) for x in row] for row in a]


def matzero(a):
    return all(not x for row in a for x in row)


I2 = [[con(1), {}], [{}, con(1)]]
x, y, b1, b2, c1, c2, P = [var(i) for i in range(NVAR)]
v = [[neg(y)], [x]]
w = [[x, y]]
b = [[b1, b2]]
c = [[c1, c2]]
tb = mm(b, v)[0][0]
tc = mm(c, v)[0][0]
d1, d2 = mm(v, w), v
Db = [mm(v, b), smul(tb, I2), [[tb]]]
Dc = [mm(v, c), smul(tc, I2), [[tc]]]
assert matzero(mm(d1, d2))
assert mm(Db[0], d1) == mm(d1, Db[1])
assert mm(Db[1], d2) == mm(d2, Db[2])
jb = [[b2], [neg(b1)]]
h0, hm1 = mm(jb, c), smul(tc, b)
assert mm(d1, h0) == mm(Db[0], Dc[0])
assert madd(mm(d2, hm1), mm(h0, d1)) == mm(Db[1], Dc[1])
assert mm(hm1, d2) == mm(Db[2], Dc[2])

# Actual nonminimal unit resolution and arbitrary Poisson correction P.
old_d1 = [[neg(y), {}, {}], [x, {}, {}], [con(-1), x, y]]
old_d2 = [[{}], [neg(y)], [x]]
correct2 = [[neg(P)], [{}], [{}]]
correct1 = [[{}, P, {}], [{}, {}, P], [{}, {}, {}]]
assert madd(mm(old_d1, correct2), mm(correct1, old_d2)) == [[{}], [{}], [P]]
assert matzero(mm(old_d1, old_d2))

# qfield element (a,b)=a+b sqrt2; no symbolic-algebra package is used.
def qa(x, y):
    return (x[0]+y[0], x[1]+y[1])


def qm(x, y):
    return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])


def qs(c, x):
    return (c*x[0], c*x[1])


zero, one = (F(0), F(0)), (F(1), F(0))


def eigenvalues(row):
    a, b, c, d = map(F, row)
    return [(a+c, b+d), (a-c, b-d), (a+c, -b-d), (a-c, -b+d)]


def exp_divisor(row):
    lam = eigenvalues(row)
    out = []
    for subset in range(16):
        val = one
        for j in range(4):
            if subset & (1 << j):
                val = qm(val, lam[j])
        out.append(val)
    return out


def ringmul(a, b):
    out = [zero]*16
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if not (i & j):
                out[i | j] = qa(out[i | j], qm(ai, bj))
    return out


rows = [
((-16,0,0,0),23104075775),((-8,-6,-8,6),38474612484),
((-8,-6,8,-6),38474612484),((0,-11,0,0),30281171392),
((-8,6,-8,-6),38474612484),((0,0,-16,0),33081896705),
((0,0,0,-11),30550999744),((8,-6,-8,-6),28751863668),
((-8,6,8,6),38474612484),((0,0,0,11),30550999744),
((0,0,16,0),33081896705),((8,-6,8,6),28751863668),
((0,11,0,0),30281171392),((8,6,-8,6),28751863668),
((8,6,8,-6),28751863668),((16,0,0,0),42549573407)]
rank = sum(n for _, n in rows)
assert rank == 522387689472 and all(n > 0 for _, n in rows)
chH = [zero]*16
for beta, n in rows:
    chH = [qa(a, qs(n, b)) for a, b in zip(chH, exp_divisor(beta))]
chH = [qs(F(1, rank), a) for a in chH]
expected_H = [F(x) for x in [1,0,0,'-1/2',0,0,0,324,0,0,0,324,'-1/2',324,324,'-31103/4']]
assert chH == [(a,F(0)) for a in expected_H]
chF = [zero]*16
for beta, coeff in [((-3,0,0,0),2),((-9,0,0,0),-2),((-12,0,0,0),1)]:
    chF = [qa(a, qs(coeff,b)) for a,b in zip(chF,exp_divisor(beta))]
expected_F = [one if i == 0 else (F(-324),F(0)) if i.bit_count()==3
              else (F(7776),F(0)) if i==15 else zero for i in range(16)]
assert chF == expected_F
balanced = [zero]*16
balanced[0], balanced[3], balanced[12], balanced[15] = one, (F(-1,2),F(0)), (F(-1,2),F(0)), (F(1,4),F(0))
assert ringmul(chH,chF) == balanced

delta = (8,-6,-8,6)
lam = eigenvalues(delta)
assert lam == [(F(0),F(0)),(F(16),F(-12)),(F(0),F(0)),(F(16),F(12))]
dims = []
for a in (1,2,3):
    shifted = [(x-3*a,y) for x,y in lam]
    determinant = one
    for x in shifted:
        determinant = qm(determinant,x)
    assert determinant[1] == 0
    assert 0 < 16-3*a and (16-3*a)**2 < 288
    dims.append(int(-determinant[0]))
assert dims == [1071,6768,19359]
assert dims[2]-2*dims[1] == 5823
chiS = lambda a: a**4-2*(a-1)**4+(a-2)**4
assert 2*chiS(-1)-4*chiS(1)+2*chiS(3) == 192

parent = Path(__file__).resolve().parents[2]/'sixfolds'
proof_files = ['rm_unit_gluing_obstruction_draft.md','rm_unit_gluing_analysis_draft.md']
out = {'status':'PASS', 'implementation':'Own sparse polynomial matrix arithmetic and pair-model Q(sqrt2), no author code or symbolic-algebra package imported',
       'generic_chain_lifts':True, 'generic_product_nullhomotopy':True,
       'arbitrary_local_poisson_correction':True,
       'complete_compensating_character':True, 'rank':rank,
       'index_three_dimensions':dims,'nontensor_parameter_lower_bound':5823,
       'positive_Ext_Euler_coefficient':192,
       'proof_hashes':{f:hashlib.sha256((parent/f).read_bytes()).hexdigest() for f in proof_files},
       'limitations':'No spectral-sequence degeneration, full derived trace, classification of Ext, finite action or semiregularity is computationally asserted. These are addressed in the separate whole-proof audit.',
       'seconds':round(time.perf_counter()-start,6)}
Path(__file__).with_name('independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
