#!/usr/bin/env python3
"""Exact checks of the supersingular point/noncube equivalence.

Run from the workbench root: python3 programs/verify_supersingular_point.py
No external dependencies. Pair coordinates use delta^2=-3.
"""
import json


class Field:
    def __init__(self, p):
        self.p = p
        self.zero, self.one = (0, 0), (1, 0)
    def s(self, a): return (a % self.p, 0)
    def add(self, a, b): return ((a[0]+b[0]) % self.p, (a[1]+b[1]) % self.p)
    def neg(self, a): return ((-a[0]) % self.p, (-a[1]) % self.p)
    def sub(self, a, b): return self.add(a, self.neg(b))
    def mul(self, a, b):
        return ((a[0]*b[0]-3*a[1]*b[1]) % self.p,
                (a[0]*b[1]+a[1]*b[0]) % self.p)
    def pow(self, a, n):
        if n < 0: return self.pow(self.inv(a), -n)
        z = self.one
        while n:
            if n & 1: z = self.mul(z, a)
            a = self.mul(a, a)
            n >>= 1
        return z
    def inv(self, a):
        n = (a[0]*a[0]+3*a[1]*a[1]) % self.p
        assert n
        c = pow(n, -1, self.p)
        return (a[0]*c % self.p, -a[1]*c % self.p)
    def div(self, a, b): return self.mul(a, self.inv(b))


def add(F, P, Q):
    if P is None: return Q
    if Q is None: return P
    x, y = P
    xx, yy = Q
    if x == xx and F.add(y, yy) == F.zero: return None
    if P == Q:
        slope = F.div(F.mul(F.s(3), F.pow(x, 2)), F.mul(F.s(2), y))
    else:
        slope = F.div(F.sub(yy, y), F.sub(xx, x))
    u = F.sub(F.sub(F.pow(slope, 2), x), xx)
    v = F.sub(F.mul(slope, F.sub(x, u)), y)
    return (u, v)


def mul(F, n, P):
    R = None
    while n:
        if n & 1: R = add(F, R, P)
        P = add(F, P, P)
        n >>= 1
    return R


def on_curve(F, P, b):
    return P is None or F.pow(P[1], 2) == F.add(F.pow(P[0], 3), F.s(b))


def phi(F, P, b):
    if P is None or P[0] == F.zero: return None
    x, y = P
    x3 = F.pow(x, 3)
    return (F.div(F.add(x3, F.s(4*b)), F.pow(x, 2)),
            F.div(F.mul(y, F.sub(x3, F.s(8*b))), x3))


def dual(F, P):
    Q = phi(F, P, 81)
    if Q is None: return None
    return (F.div(Q[0], F.s(9)), F.div(Q[1], F.s(27)))


def line_value(F, P, Q, R):
    assert P is not None and Q is not None and R is not None
    if P[0] == Q[0] and F.add(P[1], Q[1]) == F.zero:
        return F.sub(R[0], P[0])
    if P == Q:
        slope = F.div(F.mul(F.s(3), F.pow(P[0], 2)), F.mul(F.s(2), P[1]))
    else:
        slope = F.div(F.sub(Q[1], P[1]), F.sub(Q[0], P[0]))
    PQ = add(F, P, Q)
    numerator = F.sub(F.sub(R[1], P[1]), F.mul(slope, F.sub(R[0], P[0])))
    return F.div(numerator, F.sub(R[0], PQ[0]))


def miller(F, n, P, R):
    T, f = P, F.one
    for bit in bin(n)[3:]:
        h = line_value(F, T, T, R)
        assert h != F.zero
        f = F.mul(F.pow(f, 2), h)
        T = add(F, T, T)
        if bit == '1':
            h = line_value(F, T, P, R)
            assert h != F.zero
            f = F.mul(f, h)
            T = add(F, T, P)
    assert T is None
    return f


def cube_root(F, gamma, eta, a):
    R = 3**a
    m = (F.p*F.p-1)//R
    u = pow(3, -1, m) if m > 1 else 0
    x0 = F.pow(gamma, u)
    error = F.div(gamma, F.pow(x0, 3))
    zeta = F.pow(eta, R//3)
    digit_values = [F.one, zeta, F.pow(zeta, 2)]
    exponent = 0
    for i in range(a):
        value = F.pow(F.mul(error, F.pow(eta, -exponent)), 3**(a-1-i))
        digit = digit_values.index(value)
        exponent += digit*3**i
    assert exponent % 3 == 0
    root = F.mul(x0, F.pow(eta, exponent//3))
    assert F.pow(root, 3) == gamma
    return root


def trim(f):
    while f and not f[-1]: f.pop()
    return f


def remainder(f, g, p):
    f = trim(f[:])
    while len(f) >= len(g):
        c = f[-1]*pow(g[-1], -1, p) % p
        off = len(f)-len(g)
        for i, x in enumerate(g): f[off+i] = (f[off+i]-c*x) % p
        trim(f)
    return f


def multiply_mod(f, g, modulus, p):
    out = [0]*(len(f)+len(g)-1)
    for i, a in enumerate(f):
        for j, b in enumerate(g): out[i+j] = (out[i+j]+a*b) % p
    return remainder(out, modulus, p)


def unique_fp_root(modulus, p):
    f, x, n = [1], [0, 1], p
    while n:
        if n & 1: f = multiply_mod(f, x, modulus, p)
        x = multiply_mod(x, x, modulus, p)
        n >>= 1
    while len(f) < 2: f.append(0)
    f[1] = (f[1]-1) % p
    A, B = modulus, trim(f)
    while B: A, B = B, remainder(A, B, p)
    assert len(A) == 2
    return -A[0]*pow(A[1], -1, p) % p


def run_prime(p):
    F = Field(p)
    e = pow(3, -1, p-1)
    points = [None]+[(F.s(pow((y*y+3) % p, e, p)), F.s(y)) for y in range(p)]
    assert all(on_curve(F, P, -3) for P in points)
    image3 = {mul(F, 3, P) for P in points}
    nondivisible = []
    for P in points[1:]:
        gamma = F.add(P[1], (0, 1))
        is_cube = F.pow(gamma, (p*p-1)//3) == F.one
        assert is_cube == (P in image3)
        if not is_cube: nondivisible.append(P)
        Q = phi(F, P, -3)
        assert on_curve(F, Q, 81)
        assert dual(F, Q) == mul(F, 3, P)
    assert len(nondivisible) == 2*(p+1)//3
    a, cofactor = 0, p+1
    while cofactor % 3 == 0: a += 1; cofactor //= 3
    n = 3**a
    P = mul(F, cofactor, nondivisible[0])
    assert mul(F, n, P) is None and mul(F, n//3, P) is not None
    zeta = (-(pow(2, -1, p)) % p, pow(2, -1, p))
    Q = (F.mul(zeta, P[0]), P[1])
    S = (F.s(pow(3, e, p)), F.zero)
    assert mul(F, 2, S) is None
    eta = F.div(F.mul(miller(F, n, P, add(F, Q, S)), miller(F, n, Q, S)),
                F.mul(miller(F, n, P, S), miller(F, n, Q, add(F, P, S))))
    assert F.pow(eta, n) == F.one and F.pow(eta, n//3) != F.one
    current = (F.s(pow(12, e, p)), F.s(3))
    assert mul(F, 3, current) is None
    for i in range(1, a):
        X, Y = current
        c = cube_root(F, F.add(Y, (0, 1)), eta, a)
        w = F.add(c, F.div(X, c))
        z = F.mul(F.s(3), F.sub(F.pow(w, 2), X))
        assert w[1] == z[1] == 0
        z3 = F.pow(z, 3)
        yy = F.div(F.mul(F.mul(F.s(27), Y), z3), F.sub(z3, F.s(648)))
        preimage = (z, yy)
        assert on_curve(F, preimage, 81) and dual(F, preimage) == current
        r = unique_fp_root([(-12) % p, 0, (-z[0]) % p, 1], p)
        r3 = F.s(pow(r, 3, p))
        y = F.div(F.mul(yy, r3), F.add(r3, F.s(24)))
        lifted = (F.s(r), y)
        assert y[1] == 0 and on_curve(F, lifted, -3)
        assert phi(F, lifted, -3) == preimage
        assert mul(F, 3, lifted) == current
        current = lifted
    assert mul(F, n, current) is None and mul(F, n//3, current) is not None
    return {"p": p, "a": a, "affine_points_checked": p,
            "nondivisible_points": len(nondivisible),
            "pairing_generator_delta_coordinates": eta,
            "constructed_maximal_point": current,
            "reverse_lifts": a-1, "status": "PASS"}


def main():
    data = [run_prime(p) for p in (5, 11, 17, 23, 53, 71, 107, 1619)]
    print(json.dumps({"checks": data, "all_checks_passed": True}, indent=2))


if __name__ == '__main__': main()
