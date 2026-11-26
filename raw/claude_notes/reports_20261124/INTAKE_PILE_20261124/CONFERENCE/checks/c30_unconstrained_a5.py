# Check of the remark after LM4_SUCCESSOR C.30: for lambda = 1, f = [x,y]^2 the substitution
# x -> x, y -> f^-1 y f is not surjective in the quotient A5, x = (123), y = (345).
# Permutations of {1..5} as tuples p with p[i-1] = image of i; products are right-to-left: (p*q)(i) = p(q(i)).
# Also printed: relation (I), f(x,y) f(y,x) = 1. It holds, and it holds identically in the free group, because
# [y,x] = [x,y]^-1. So relation (I) alone does not force surjectivity; the hexagon (II) is what C.30 uses.
from itertools import product

def mul(p, q):            # p after q
    return tuple(p[q[i] - 1] for i in range(5))

def inv(p):
    r = [0] * 5
    for i, v in enumerate(p):
        r[v - 1] = i + 1
    return tuple(r)

def cyc(*c):
    p = list(range(1, 6))
    for i, a in enumerate(c):
        p[a - 1] = c[(i + 1) % len(c)]
    return tuple(p)

def comm(a, b):           # [a,b] = a b a^-1 b^-1
    return mul(mul(a, b), mul(inv(a), inv(b)))

def gen(gens):
    e = tuple(range(1, 6))
    seen = {e}
    frontier = [e]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                k = mul(h, g)
                if k not in seen:
                    seen.add(k)
                    nxt.append(k)
        frontier = nxt
    return seen

x, y = cyc(1, 2, 3), cyc(3, 4, 5)
def f(a, b):
    c = comm(a, b)
    return mul(c, c)

F = f(x, y)
ynew = mul(mul(inv(F), y), F)
G = gen([x, y])
H = gen([x, ynew])
print("order of <x,y>:", len(G))
print("f(x,y) =", F, " f^-1 y f =", ynew)
print("order of <x, f^-1 y f>:", len(H), " fixes the point 4:", all(h[3] == 4 for h in H))
print("relation (I) f(x,y) f(y,x) = 1 holds in A5:", mul(f(x, y), f(y, x)) == tuple(range(1, 6)))
