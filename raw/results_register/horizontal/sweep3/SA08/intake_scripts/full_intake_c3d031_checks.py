# Computations for the full intake of RESEARCH_SA08_C3_D031 (checkpoint 08, 20261119T2043Z), 22 Nov 2026.
# Claude Opus 5.5 at effort max, agent a34c04448e8299803. Standard library only; runs no program of the return.
import itertools, math, sys
from fractions import Fraction
sys.stdout.reconfigure(encoding='utf-8')
C = math.comb


def vp(n, p):
    n = abs(n); k = 0
    while n and n % p == 0:
        n //= p; k += 1
    return k


# AT10-lattice: over Z_(p), N = p^e, 0 <= s < N: (lN+s)!/(l!(N!)^l s!) is a p-unit.
ok = True; cnt = 0
for p in (2, 3, 5, 7):
    for e in range(0, 4):
        N = p ** e
        for l in range(0, 11):
            for s in range(N):
                num = math.factorial(l * N + s)
                den = math.factorial(l) * math.factorial(N) ** l * math.factorial(s)
                assert num % den == 0
                ok &= vp(num // den, p) == 0; cnt += 1
print('AT10-lattice: (lN+s)!/(l!(N!)^l s!) is a p-unit for p in 2,3,5,7, N = p^e (e<=3), l<=10, s<N:', ok, '(', cnt, 'cases )')

# AT11: C(p^r, a) = 0 mod p for 0 < a < p^r, and C(p^(r+1), p^r) = 0 mod p.
ok1 = all(C(p ** r, a) % p == 0 for p in (2, 3, 5, 7) for r in range(1, 5) for a in range(1, p ** r))
ok2 = all(C(p ** (r + 1), p ** r) % p == 0 for p in (2, 3, 5, 7) for r in range(0, 5))
print('AT11: C(p^r,a) = 0 mod p (0<a<p^r):', ok1, '; C(p^(r+1),p^r) = 0 mod p:', ok2)


# AT12 (AT.39): C_n = Z^{triples 0<=i<=j<=k<=n}; normalized N_n = cap_{i>=1} ker d_i, differential d_0.
def triples(n):
    return [t for t in itertools.product(range(n + 1), repeat=3) if t[0] <= t[1] <= t[2]]


def face(i, n):  # delta_i: [n-1] -> [n] skipping i
    return lambda a: a if a < i else a + 1


def rank(M):
    M = [[Fraction(x) for x in row] for row in M]
    r = 0; cols = len(M[0]) if M else 0
    for c in range(cols):
        piv = next((k for k in range(r, len(M)) if M[k][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for k in range(len(M)):
            if k != r and M[k][c] != 0:
                f = M[k][c] / M[r][c]
                M[k] = [a - f * b for a, b in zip(M[k], M[r])]
        r += 1
    return r


def normalized_basis(n):
    # an indicator e_t lies in ker d_i iff t avoids nothing... d_i(e_t) = e_t o delta_i, zero iff no triple of [n-1] maps to t,
    # i.e. iff t contains i. The intersection over i = 1..n of the kernels is spanned by the e_t with t containing 1..n
    # (each d_i is a coordinate restriction, so the kernels are spanned by indicators).
    return [t for t in triples(n) if all(v in t for v in range(1, n + 1))]


bases = {n: normalized_basis(n) for n in range(0, 6)}
print('AT12 (AT.39): normalized bases:', {n: [''.join(map(str, t)) for t in b] for n, b in bases.items()})
d0 = {}
for n in range(1, 6):
    src, tgt = bases[n], bases[n - 1]
    f = face(0, n)
    M = []
    for t in tgt:  # (d_0 e_s)(t) = e_s(delta_0 t)
        M.append([1 if tuple(f(a) for a in t) == s else 0 for s in src])
    d0[n] = M
ranks = {n: (rank(d0[n]) if bases[n] and bases[n - 1] else 0) for n in range(1, 6)}
homology = {n: len(bases[n]) - (ranks.get(n, 0)) - ranks.get(n + 1, 0) for n in range(0, 5)}
print('AT12: ranks of d_0:', ranks, '; dimensions of normalized homology (rational), degrees 0-4:', homology)
# e_012 is closed for every face
print('AT12: e_012 killed by d_0, d_1, d_2:',
      all(not any(tuple(face(i, 2)(a) for a in t) == (0, 1, 2) for t in triples(1)) for i in range(3)))
# integral contraction: each d_0 matrix is a 0/1 partial permutation, so the complex splits over Z.
print('AT12: every d_0 is a 0/1 partial permutation matrix (integral splitting):',
      all(all(sum(row) <= 1 for row in d0[n]) and all(sum(d0[n][r][c] for r in range(len(d0[n]))) <= 1
          for c in range(len(d0[n][0]) if d0[n] else 0)) for n in range(1, 6) if d0[n]))


# A-S09-22 and AT18: the resolved generators (S09.98)-(S09.100) in the rational free algebra over Q[t],
# T = t, U = T^[2] = t^2/2, with K = H + tC/2 (from TC = 2(K-H)) and J = tH/2 (from TH = 2J).
DEG = {'C': 0, 'H': 0, 'x': 1, 'y': 1, 'g': 1, 'l': 1, 'a': 2, 'b': 2, 'r': 2, 's': 2, 'E': 3, 'F': 3, 'eta': 3, 'z': 4}
ORDER = list(DEG)


def mono_mul(m1, m2):
    (p1, g1), (p2, g2) = m1, m2
    gens = list(g1) + list(g2); sign = 1
    for i in range(len(gens)):  # bubble sort with Koszul signs
        for j in range(len(gens) - 1 - i):
            if ORDER.index(gens[j]) > ORDER.index(gens[j + 1]):
                if DEG[gens[j]] % 2 and DEG[gens[j + 1]] % 2:
                    sign = -sign
                gens[j], gens[j + 1] = gens[j + 1], gens[j]
    for j in range(len(gens) - 1):
        if gens[j] == gens[j + 1] and DEG[gens[j]] % 2:
            return None, 0
    return (p1 + p2, tuple(gens)), sign


def mul(P, Q):
    out = {}
    for m1, c1 in P.items():
        for m2, c2 in Q.items():
            m, s = mono_mul(m1, m2)
            if m is not None:
                out[m] = out.get(m, 0) + s * c1 * c2
    return {m: c for m, c in out.items() if c != 0}


def add(*Ps):
    out = {}
    for P in Ps:
        for m, c in P.items():
            out[m] = out.get(m, 0) + c
    return {m: c for m, c in out.items() if c != 0}


def sc(c, P, tp=0):
    return {(m[0] + tp, m[1]): Fraction(c) * v for m, v in P.items()} if c else {}


def gen(n):
    return {(0, (n,)): Fraction(1)}


G = {n: gen(n) for n in DEG}
T1 = lambda P: sc(1, P, 1)            # multiplication by T = t
U1 = lambda P: sc(Fraction(1, 2), P, 2)  # multiplication by U = t^2/2
Kp = add(G['H'], sc(Fraction(1, 2), G['C'], 1))
Jp = sc(Fraction(1, 2), G['H'], 1)


def make_d(twisted):
    dg = {
        'C': add(sc(2, G['g']), T1(G['x']), sc(-2, G['y'])),
        'H': add(sc(-1, T1(G['g'])), sc(2, G['l'])),
        'x': add(sc(2, G['r']), T1(G['a']), sc(-2, G['b'])),
        'y': add(sc(2, G['s']), U1(G['a']), sc(-1, T1(G['b']))),
        'g': add(sc(-1, T1(G['r'])), sc(2, G['s'])),
        'l': add(sc(-1, U1(G['r'])), T1(G['s'])),
        'a': sc(2, G['E']), 'b': sc(2, G['F']),
        'r': add(sc(-1, T1(G['E'])), sc(2, G['F'])),
        's': add(sc(-1, U1(G['E'])), T1(G['F'])),
        'E': {}, 'F': {}, 'eta': sc(2, G['z']), 'z': {}}
    if twisted:
        dg['a'] = add(dg['a'], sc(-1, T1(G['eta'])))
        dg['b'] = add(dg['b'], sc(-1, U1(G['eta'])))
        dg['E'] = T1(G['z']); dg['F'] = U1(G['z'])

    def d(P):
        out = {}
        for (p, gens), c in P.items():
            sgn = 1
            for i, n in enumerate(gens):
                left = {(p, gens[:i]): Fraction(1)}; right = {(0, gens[i + 1:]): Fraction(1)}
                term = mul(mul(left, dg[n]), right)
                out = add(out, sc(sgn * c, term))
                if DEG[n] % 2:
                    sgn = -sgn
        return out
    return d


for tw in (False, True):
    d = make_d(tw)
    d2 = all(d(d(G[n])) == {} for n in DEG)
    dK = d(Kp); dKclaim = add(sc(2, G['l']), U1(G['x']), sc(-1, T1(G['y'])))
    B = add(mul(G['a'], G['H']), sc(-1, mul(G['C'], G['r'])), sc(-1, mul(G['g'], G['x'])))
    zeta = add(mul(G['E'], Kp), sc(-1, mul(G['F'], G['C'])), mul(G['r'], G['y']), sc(-1, mul(G['s'], G['x'])),
               sc(-1, mul(G['g'], G['b'])), mul(G['l'], G['a']))
    if tw:
        zeta = add(zeta, sc(-1, mul(Jp, G['eta'])))
    dJ_ok = d(Jp) == add(sc(-1, U1(G['g'])), T1(G['l']))
    print('A-S09-22 (%s): d^2 = 0 on all generators:' % ('twisted' if tw else 'untwisted'), d2,
          '; dK = 2l + Ux - Ty:', d(Kp) == dKclaim, '; dJ = -Ug + Tl:', dJ_ok,
          '; dB = 2 zeta%s:' % ('_tw' if tw else ''), d(B) == sc(2, zeta), '; d zeta = 0:', d(zeta) == {})
d = make_d(False)
basis = [mul(G['C'], G['r']), mul(G['g'], G['x']), mul(G['a'], G['H']), mul(G['a'], Kp), mul(G['b'], G['C']), mul(G['x'], G['y'])]


def ek_coeff(P):  # coefficient of EK in the integral basis EH, EK, FC: EK = EH + tEC/2, so it is 2 x coeff of t*E*C
    return 2 * P.get((1, ('C', 'E')), 0)


zeta0 = add(mul(G['E'], Kp), sc(-1, mul(G['F'], G['C'])), mul(G['r'], G['y']), sc(-1, mul(G['s'], G['x'])),
            sc(-1, mul(G['g'], G['b'])), mul(G['l'], G['a']))
print('A-S09-22 (S09.104): EK-coefficients of d(Cr, gx, aH, aK, bC, xy):', [ek_coeff(d(P)) for P in basis],
      '; of zeta:', ek_coeff(zeta0))
# AT18 (AT.99): mod-2 expansion check with symbols in a commutative algebra over F_2 is done by hand in the intake note.


# A-L20 (p = 3): rational free algebra over Q[t], t = T, u = T^[3] = t^3/6, with
# K = H/2 + t^2 C/6 (from t^2 C = 3(2K - H)) and J = (tK - uC)/3 = tH/6.
DEG = {'C': 0, 'H': 0, 'x': 1, 'y': 1, 'g': 1, 'l': 1, 'r': 2, 'a': 2, 'b': 2, 's': 2, 'E': 3, 'F': 3, 'z': 3, 'w': 3}
ORDER = list(DEG)
G = {n: gen(n) for n in DEG}
tt = lambda P, k=1: sc(1, P, k)                       # multiplication by t^k
uu = lambda P: sc(Fraction(1, 6), P, 3)               # multiplication by u = t^3/6
K3 = add(sc(Fraction(1, 2), G['H']), sc(Fraction(1, 6), G['C'], 2))
J3 = sc(Fraction(1, 6), G['H'], 1)
dg3 = {
    'C': add(sc(3, G['g']), tt(G['x']), sc(-6, G['y'])),
    'H': add(sc(-1, tt(G['g'], 2)), sc(6, G['l'])),
    'x': add(sc(3, G['r']), tt(G['a'], 2), sc(-6, G['b'])),
    'y': add(sc(3, G['s']), uu(G['a']), sc(-1, tt(G['b']))),
    'g': add(sc(-1, tt(G['r'])), sc(6, G['s'])),
    # (AL.110) prints dl = -ur + t sigma; the weights (l: 9, u r: 3+6, t sigma: 1+7) and the column (u, -t^2) of N
    # force dl = -(u r - t^2 sigma) = -ur + t^2 sigma.  The printed form is tested separately below.
    'l': add(sc(-1, uu(G['r'])), tt(G['s'], 2)),
    'a': add(sc(3, G['E']), tt(G['z']), sc(-6, G['w'])),
    'b': add(sc(3, G['F']), uu(G['z']), sc(-1, tt(G['w'], 2))),
    'r': add(sc(-1, tt(G['E'], 2)), sc(6, G['F'])),
    's': add(sc(-1, uu(G['E'])), tt(G['F'])),
    'E': None, 'F': None, 'z': None, 'w': None}


def d3(P):
    out = {}
    for (p, gens), c in P.items():
        sgn = 1
        for i, n in enumerate(gens):
            if dg3[n] is None:
                raise ValueError('d of ' + n + ' not specified')
            left = {(p, gens[:i]): Fraction(1)}; right = {(0, gens[i + 1:]): Fraction(1)}
            out = add(out, sc(sgn * c, mul(mul(left, dg3[n]), right)))
            if DEG[n] % 2:
                sgn = -sgn
    return out


ok_d2 = all(d3(d3(G[n])) == {} for n in ['C', 'H', 'x', 'y', 'g', 'l'])
dK_ok = d3(K3) == add(sc(3, G['l']), uu(G['x']), sc(-1, tt(G['y'], 2)))
dJ_ok = d3(J3) == add(sc(-1, uu(G['g'])), tt(G['l']))
B3 = sc(Fraction(1, 2), add(mul(G['a'], G['H']), sc(-1, mul(G['C'], G['r'])), sc(-1, mul(G['g'], G['x']))))
Z3 = add(mul(K3, G['E']), sc(-1, mul(G['C'], G['F'])), mul(G['l'], G['a']), mul(G['y'], G['r']),
         sc(-1, mul(G['s'], G['x'])), sc(-1, mul(G['g'], G['b'])), sc(-1, mul(G['H'], G['w'])), mul(J3, G['z']))
print('A-L20 (p=3): d^2 = 0 on C,H,x,y,g,l:', ok_d2, '; dK = 3l + ux - t^2 y:', dK_ok, '; dJ = -ug + tl:', dJ_ok,
      '; dB = 3 zeta:', d3(B3) == sc(3, Z3))
basis3 = [mul(G['C'], G['r']), mul(G['g'], G['x']), mul(G['a'], G['H']), mul(G['a'], K3), mul(G['C'], G['b']), mul(G['x'], G['y'])]
gb = lambda P: P.get((0, ('g', 'b')), 0)
print('A-L20 (AL.113): gb_1-coefficients of d(Cr, gx, aH, aK, Cb_1, xy):', [gb(d3(P)) for P in basis3], '; of zeta:', gb(Z3))

dg3['l'] = add(sc(-1, uu(G['r'])), tt(G['s']))
print('A-L20: with the printed dl = -ur + t sigma, d^2 l = 0:', d3(d3(G['l'])) == {})
