# Independent checks of RESEARCH_SA09's B.1, B.2 and B.4 statements (intake of 19 Nov 2026).
# a34c04448e8299803 (Claude Opus 5.5 at effort max). Uses itertools and sympy only; runs no program of the return.
import itertools, sys
from collections import Counter
import sympy as sp
sys.stdout.reconfigure(encoding='utf-8')
n = 6


def compose(p, q):            # (p*q)(x) = p(q(x)), permutations as tuples
    return tuple(p[q[x]] for x in range(len(q)))


def inverse(p):
    r = [0] * len(p)
    for i, x in enumerate(p):
        r[x] = i
    return tuple(r)


def ctype(p):
    seen, t = set(), []
    for i in range(len(p)):
        if i not in seen:
            j, l = i, 0
            while j not in seen:
                seen.add(j); j = p[j]; l += 1
            t.append(l)
    return tuple(sorted(t, reverse=True))


def from_cycles(cycles, m=n):
    p = list(range(m))
    for c in cycles:
        for a, b in zip(c, c[1:] + c[:1]):
            p[a] = b
    return tuple(p)


S6 = list(itertools.permutations(range(n)))


def dessins(t0, t1, tinf):
    """classes of (s0, s1) with s0 s1 sinf = 1, types t0, t1, tinf; sinf fixed as a 6-cycle (transitive automatically)"""
    sinf = from_cycles([[0, 1, 2, 3, 4, 5]])
    C = [g for g in S6 if compose(g, sinf) == compose(sinf, g)]           # centralizer of sinf
    sols = []
    for s0 in S6:
        if ctype(s0) != t0:
            continue
        s1 = compose(inverse(s0), inverse(sinf))                          # s0 s1 sinf = 1
        if ctype(s1) == t1:
            sols.append(s0)
    orbits, seen = [], set()
    for s0 in sols:
        if s0 in seen:
            continue
        orb = {compose(compose(g, s0), inverse(g)) for g in C}
        seen |= orb
        orbits.append((s0, len(C) // len(orb)))                            # representative, |Aut|
    return len(sols), orbits


print('B2.3 / B0.1: dessins of passport [3,2,1; 2,2,1,1; 6] (sigma_inf fixed as (012345)):')
ns, orb = dessins((3, 2, 1), (2, 2, 1, 1), (6,))
print('   solutions', ns, '; classes', len(orb), '; automorphism group orders', [a for _, a in orb])
ns2, orb2 = dessins((3, 2, 1), (3, 1, 1, 1), (6,))
print('B2.5: dessins of passport [3,2,1; 3,1,1,1; 6]: classes', len(orb2), '; automorphism orders', [a for _, a in orb2])

print('B2.3: the run\'s triples rho = (123)(45), alpha = (14)(36), (14)(56), (14)(26) on {1..6}:')
rho = from_cycles([[0, 1, 2], [3, 4]])
alphas = [from_cycles([[0, 3], [2, 5]]), from_cycles([[0, 3], [4, 5]]), from_cycles([[0, 3], [1, 5]])]
Crho = [g for g in S6 if compose(g, rho) == compose(rho, g)]
for a in alphas:
    print('   type(rho*alpha) =', ctype(compose(rho, a)), ' type(alpha*rho) =', ctype(compose(a, rho)))
same = [[any(compose(compose(g, a), inverse(g)) == b for g in Crho) for b in alphas] for a in alphas]
print('   pairwise simultaneously conjugate (fixing rho):', same)
allalpha = [a for a in S6 if ctype(a) == (2, 2, 1, 1) and ctype(compose(rho, a)) == (6,)]
print('   all alpha of type [2,2,1,1] with rho*alpha a 6-cycle:', len(allalpha), '; |C(rho)| =', len(Crho))

z, c = sp.symbols('z c')
h = z**3 * (z - 1)**2 * (z - c)
G = z**2 - (5 * c + 4) * z / 6 + c / 2
print('B2.1: h\'(z) = z^2 (z-1) * 6 G_c(z):', sp.expand(sp.diff(h, z) - z**2 * (z - 1) * 6 * G) == 0)
rem = sp.rem(sp.expand(h), G, z)
P = sp.factor(sp.expand(rem).coeff(z, 1)); Q = sp.factor(sp.expand(rem).coeff(z, 0))
delta = 25 * c**2 - 32 * c + 16
p = 25 * c**3 - 12 * c**2 - 24 * c - 16
print('   remainder P z + Q with P =', P)
print('   P == -delta*p/7776:', sp.simplify(P + delta * p / 7776) == 0)
print('   Q =', Q, '; Q == c(5c-8)(25c^3-6c^2+8)/2592:', sp.simplify(Q - c * (5 * c - 8) * (25 * c**3 - 6 * c**2 + 8) / 2592) == 0)
print('   disc_z(G_c) * 36 == delta:', sp.simplify(sp.discriminant(G, z) * 36 - delta) == 0)
Qred = sp.rem(sp.numer(sp.together(Q)), p, c) / sp.denom(sp.together(Q))
print('   Q mod p(c) =', sp.factor(Qred), '; == (32-52c-c^2)/1500 mod p:',
      sp.rem(sp.numer(sp.together(Qred - (32 - 52 * c - c**2) / 1500)), p, c) == 0)
r = sp.cbrt(2)
cj = (4 + 18 * r + 6 * r**2) / 25
mp = sp.minimal_polynomial(cj, c)
print('B2.4: minimal polynomial of (4+18r+6r^2)/25, r^3 = 2:', mp, '; proportional to p:', sp.simplify(mp * 25 - p) == 0 or sp.simplify(mp - p) == 0)
print('   r back from c: r is in Q(c) since deg Q(c) = 3 = deg Q(r) and c in Q(r)')
print('   disc(p) =', sp.factor(sp.discriminant(p, c)), '; real roots of p:', [sp.N(x, 12) for x in sp.real_roots(p)])
for root in sp.Poly(p, c).nroots(n=30):
    Gn = sp.Poly(G.subs(c, root), z)
    r1, r2 = Gn.nroots(n=30)
    hv = [sp.N(h.subs({c: root, z: rr}), 25) for rr in (r1, r2)]
    print('   c = %s: |h(r1)-h(r2)| = %.1e, h(r1) = %s, r1,r2 = %s, %s' % (sp.N(root, 8), abs(complex(hv[0] - hv[1])),
          sp.N(hv[0], 8), sp.N(r1, 6), sp.N(r2, 6)))
print('   roots of delta:', sp.solve(delta, c))

x = sp.symbols('x')
print('B4.1: x^8 - 2 over Q(zeta_8) = Q(i, sqrt 2):', sp.factor_list(x**8 - 2, extension=[sp.I, sp.sqrt(2)]))
print('      x^4 - 2 over Q(zeta_4) = Q(i):', sp.factor_list(x**4 - 2, extension=[sp.I]))
print('      so [Q(zeta_8, 2^(1/8)):Q] = 4*4 = 16 = 8*phi(8)/2 (index 2) and [Q(zeta_4, 2^(1/4)):Q] = 2*4 = 8 = 4*phi(4) (index 1)')
