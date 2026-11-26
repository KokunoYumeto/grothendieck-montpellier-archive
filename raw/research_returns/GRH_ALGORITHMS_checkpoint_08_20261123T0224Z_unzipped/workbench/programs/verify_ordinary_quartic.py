#!/usr/bin/env python3
"""Exact, dependency-free checks of the two-trial ordinary construction.

Run from the workbench root: python3 programs/verify_ordinary_quartic.py
Only Python's standard library is used. Pair coordinates use delta^2=-3.
"""
import json


def sqrt_fp(a, p):
    a %= p
    if a == 0:
        return 0
    assert pow(a, (p-1)//2, p) == 1
    odd = p-1
    e = 0
    while odd % 2 == 0:
        odd //= 2
        e += 1
    c = pow(-3 % p, odd, p)  # known nonsquare, since p=2 mod3
    x = pow(a, (odd+1)//2, p)
    t = pow(a, odd, p)
    while t != 1:
        u = t
        j = 0
        while u != 1:
            u = u*u % p
            j += 1
        assert j < e
        b = pow(c, 1 << (e-j-1), p)
        x = x*b % p
        c = b*b % p
        t = t*c % p
        e = j
    assert x*x % p == a
    return min(x, p-x)


class K:
    def __init__(self, p):
        assert p > 3 and p % 3 == 2
        self.p, self.q = p, p*p
        self.zero, self.one = (0, 0), (1, 0)
    def scalar(self, a): return (a % self.p, 0)
    def add(self, a, b): return ((a[0]+b[0]) % self.p, (a[1]+b[1]) % self.p)
    def neg(self, a): return ((-a[0]) % self.p, (-a[1]) % self.p)
    def sub(self, a, b): return self.add(a, self.neg(b))
    def scale(self, c, a): return (c*a[0] % self.p, c*a[1] % self.p)
    def mul(self, a, b):
        return ((a[0]*b[0]-3*a[1]*b[1]) % self.p,
                (a[0]*b[1]+a[1]*b[0]) % self.p)
    def pow(self, a, n):
        result = self.one
        while n:
            if n & 1: result = self.mul(result, a)
            a = self.mul(a, a)
            n >>= 1
        return result
    def inv(self, a):
        n = (a[0]*a[0]+3*a[1]*a[1]) % self.p
        assert n
        return self.scale(pow(n, -1, self.p), (a[0], -a[1]))
    def div(self, a, b): return self.mul(a, self.inv(b))
    def sqrt(self, z):
        p = self.p
        if z == self.zero: return z
        assert self.pow(z, (self.q-1)//2) == self.one
        A, B = z
        if not B:
            if pow(A, (p-1)//2, p) == 1:
                root = (sqrt_fp(A, p), 0)
            else:
                root = (0, sqrt_fp(A*pow(-3 % p, -1, p), p))
        else:
            h = sqrt_fp(A*A+3*B*B, p)
            u = (A+h)*pow(2, -1, p) % p
            if pow(u, (p-1)//2, p) != 1:
                u = (A-h)*pow(2, -1, p) % p
            x = sqrt_fp(u, p)
            root = (x, B*pow(2*x, -1, p) % p)
        assert self.mul(root, root) == z
        return root


class L:
    def __init__(self, k, eta):
        self.k, self.eta = k, eta
        self.zero = (k.zero, k.zero)
        self.one = (k.one, k.zero)
        self.U = (k.zero, k.one)
    def scalar(self, n): return (self.k.scalar(n), self.k.zero)
    def add(self, a, b): return (self.k.add(a[0], b[0]), self.k.add(a[1], b[1]))
    def neg(self, a): return (self.k.neg(a[0]), self.k.neg(a[1]))
    def sub(self, a, b): return self.add(a, self.neg(b))
    def mul(self, a, b):
        k = self.k
        return (k.add(k.mul(a[0], b[0]), k.mul(self.eta, k.mul(a[1], b[1]))),
                k.add(k.mul(a[0], b[1]), k.mul(a[1], b[0])))
    def pow(self, a, n):
        result = self.one
        while n:
            if n & 1: result = self.mul(result, a)
            a = self.mul(a, a)
            n >>= 1
        return result
    def inv(self, a):
        k = self.k
        n = k.sub(k.mul(a[0], a[0]), k.mul(self.eta, k.mul(a[1], a[1])))
        return (k.div(a[0], n), k.div(k.neg(a[1]), n))
    def div(self, a, b): return self.mul(a, self.inv(b))


def polynomial(k, x):
    return k.sub(k.sub(k.mul(x, x), k.scale(216, x)), k.scalar(373248))


def trials(k, eta):
    field = L(k, eta)
    assert field.pow(field.U, k.q) == field.neg(field.U)
    result = []
    for t in (1, 2):
        A = field.mul(field.scalar(t), field.U)
        a3 = field.pow(A, 3)
        R = field.sub(a3, field.scalar(27))
        j = field.div(field.mul(a3, field.pow(field.sub(a3, field.scalar(24)), 3)), R)
        conjugate = field.pow(j, k.q)
        outside = j != conjugate
        assert outside == (j[1] != k.zero)
        criterion = polynomial(k, k.scale(t**6, k.pow(eta, 3)))
        assert outside == (criterion != k.zero)
        norm_R = field.pow(R, k.q+1)
        expected_norm = k.sub(k.scalar(729), k.scale(t**6, k.pow(eta, 3)))
        assert norm_R == (expected_norm, k.zero)
        is_cube = field.pow(R, (k.q*k.q-1)//3) == field.one
        assert is_cube == (k.pow(expected_norm, (k.q-1)//3) == k.one)
        result.append({"t": t, "j_outside_quadratic_field": outside,
                       "radicand_is_cube": is_cube,
                       "norm_radicand_delta_coordinates": expected_norm,
                       "ordinary_test_delta_coordinates": criterion})
    assert any(item["j_outside_quadratic_field"] for item in result)
    return result


def run_prime(p):
    k = K(p)
    square_count = nonsquare_count = 0
    for a in range(p):
        for b in range(p):
            z = (a, b)
            if z == k.zero: continue
            if k.pow(z, (k.q-1)//2) == k.one:
                root = k.sqrt(z)
                assert k.pow(root, 2) == z
                square_count += 1
            else:
                x = k.pow(z, 3)
                assert x[1] != 0
                assert polynomial(k, x) != k.zero or polynomial(k, k.scale(64, x)) != k.zero
                nonsquare_count += 1
    assert square_count == nonsquare_count == (k.q-1)//2
    eta = k.scalar(-1)
    steps = 0
    while k.pow(eta, (k.q-1)//2) == k.one:
        eta = k.sqrt(eta)
        steps += 1
    assert k.pow(eta, 1 << (steps+1)) == k.one
    assert k.pow(eta, 1 << steps) != k.one
    return {"p": p, "square_roots_checked": square_count,
            "nonsquare_parameters_checked": nonsquare_count,
            "root_chain_steps": steps, "eta_delta_coordinates": eta,
            "trials": trials(k, eta), "status": "PASS"}


def main():
    checked = [run_prime(p) for p in (5, 11, 17, 23, 29, 41, 47, 53, 59, 71, 83, 89, 101, 107)]
    k = K(53)
    eta = (19, 35)  # 1+17*zeta, where zeta=(-1+delta)/2.
    assert k.pow(eta, (k.q-1)//2) == k.scalar(-1)
    certificate = trials(k, eta)
    assert all(t["j_outside_quadratic_field"] and t["radicand_is_cube"] for t in certificate)
    print(json.dumps({"basis": "delta^2=-3", "checks": checked,
                      "ordinary_but_both_radicands_cubic": {"p": 53, "eta": eta,
                                                            "trials": certificate},
                      "all_checks_passed": True}, indent=2))


if __name__ == "__main__":
    main()
