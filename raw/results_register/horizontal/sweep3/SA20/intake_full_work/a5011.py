"""RESEARCH_SA20 A5.011: check (A5.11.2)-(A5.11.4) in Z[C_23] and Z[omega]. Claude Opus 5.5 at effort max, acf08879a01b97ed4, 22 Nov 2026."""
p = 23
Q = sorted({(a * a) % p for a in range(1, p)})
print("quadratic residues mod 23:", Q, "matches run:", Q == [1,2,3,4,6,8,9,12,13,16,18])
def mul(x, y):
    z = [0] * p
    for i in range(p):
        if x[i]:
            for j in range(p):
                z[(i + j) % p] += x[i] * y[j]
    return z
r = [0] * p; r[0] = 1
for a in Q: r[a] += 1
N = [1] * p
r2 = mul(r, r)
lhs = [r2[i] - r[i] + (6 if i == 0 else 0) for i in range(p)]
print("r^2 - r + 6 == 6N:", lhs == [6] * p)
rbar = [r[(-i) % p] for i in range(p)]
print("rbar == N + 1 - r:", rbar == [N[i] + (1 if i == 0 else 0) - r[i] for i in range(p)])
# E^2 = E with E = [[1-r, 3(1-N)], [2, r]]
one = [1] + [0] * (p - 1)
def add(*xs): return [sum(t) for t in zip(*xs)]
def sc(c, x): return [c * t for t in x]
E = [[add(one, sc(-1, r)), sc(3, add(one, sc(-1, N)))], [sc(2, one), r]]
E2 = [[add(mul(E[i][0], E[0][k]), mul(E[i][1], E[1][k])) for k in range(2)] for i in range(2)]
print("E^2 == E:", E2 == E)
# norms in Z[omega], omega^2 = omega - 6: a^2+ab+6b^2 = 2 has no solution; p^3 = (2 - omega) has norm 8
print("norm 2 solvable:", any(a*a + a*b + 6*b*b == 2 for a in range(-10, 11) for b in range(-10, 11)))
print("N(2 - omega) =", 2*2 + 2*(-1) + 6*1)
# class group of Q(sqrt(-23)): reduced forms of discriminant -23
forms = [(a, b, c) for a in range(1, 10) for b in range(-a + 1, a + 1) for c in range(a, 30)
         if b*b - 4*a*c == -23 and (abs(b) <= a <= c) and not (b < 0 and (abs(b) == a or a == c))]
print("reduced forms of disc -23:", forms, "class number", len(forms))
