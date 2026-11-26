#!/usr/bin/env python3
"""Exact checks of the restricted-volcano identities; Python standard library.

Run from the workbench root:
  python3 programs/verify_restricted_volcano.py

Every assertion uses exact arithmetic in F_p[z]/(z^2+z+1).
The finite checks are not a proof of an asymptotic construction.
"""
import json


class Quadratic:
    def __init__(self, p):
        self.p = p
        self.zero = (0, 0)
        self.one = (1, 0)
        self.zeta = (0, 1)

    def scalar(self, n):
        return (n % self.p, 0)

    def add(self, x, y):
        return ((x[0] + y[0]) % self.p, (x[1] + y[1]) % self.p)

    def neg(self, x):
        return ((-x[0]) % self.p, (-x[1]) % self.p)

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        a, b = x
        c, d = y
        return ((a*c-b*d) % self.p, (a*d+b*c-b*d) % self.p)

    def pow(self, x, n):
        if n < 0:
            return self.pow(self.inv(x), -n)
        result = self.one
        while n:
            if n & 1:
                result = self.mul(result, x)
            x = self.mul(x, x)
            n >>= 1
        return result

    def inv(self, x):
        a, b = x
        norm = (a*a-a*b+b*b) % self.p
        assert norm
        u = pow(norm, -1, self.p)
        return ((a-b)*u % self.p, -b*u % self.p)

    def div(self, x, y):
        return self.mul(x, self.inv(y))

    def scale(self, n, x):
        return (n*x[0] % self.p, n*x[1] % self.p)


def run_prime(p):
    assert p > 3 and p % 9 == 8
    f = Quadratic(p)
    z = f.zeta
    delta = f.sub(z, f.pow(z, 2))
    assert f.pow(delta, 2) == f.scalar(-3)
    exponent = pow(3, -1, p-1)
    fp_cube_root = lambda a: pow(a % p, exponent, p)
    cube_roots = {}
    for a in range(p):
        for b in range(p):
            x = (a, b)
            if x != f.zero:
                cube_roots.setdefault(f.pow(x, 3), x)
    assert len(cube_roots) == (p*p-1)//3

    curve_checks = 0
    quotient_cube_cases = 0
    ordinary_intermediate = 0
    supersingular = 0
    traces = {}
    for K in range(p):
        if K == 3:
            continue
        kk = f.scalar(K)
        c = fp_cube_root(K**3-27)
        assert c
        d = f.scale(c, z)
        denominator = f.sub(kk, d)
        x = f.div(f.scalar(-3), denominator)
        y = f.div(f.scalar(K-c), denominator)
        assert x[1] != 0
        lhs = f.add(f.add(f.pow(y, 2), f.scale(K, f.mul(x, y))), y)
        assert lhs == f.pow(x, 3)
        tangent_denominator = f.add(f.add(f.scale(2, y), f.scale(K, x)), f.one)
        slope = f.div(f.sub(f.scale(3, f.pow(x, 2)), f.scale(K, y)),
                      tangent_denominator)
        assert f.sub(f.sub(f.scale(3, x), f.pow(slope, 2)),
                     f.scale(K, slope)) == f.zero
        # Vanishing quadratic term after translation proves that Q is a flex.
        a0 = f.div(f.add(kk, f.scale(2, d)), delta)
        b0 = f.div(f.mul(delta, d), denominator)
        assert a0 == f.add(kk, f.scale(2, slope))
        assert b0 == tangent_denominator
        r0 = f.sub(f.pow(a0, 3), f.scale(27, b0))
        assert r0 == f.pow(f.div(denominator, delta), 3)
        t = K*pow(c, -1, p) % p
        assert t != 1
        assert b0 == f.div(f.mul(delta, z), f.sub(f.scalar(t), z))
        assert fp_cube_root(27*pow((t**3-1) % p, -1, p)) == c
        j1 = K**3 * (K**3-24)**3 * pow((K**3-27) % p, -1, p) % p
        j2 = 27*t**3*(t**3+8)**3*pow(pow((t**3-1) % p, 3, p), -1, p) % p
        assert j1 == j2
        trace = 0
        for xx in range(p):
            disc = ((K*xx+1)**2 + 4*xx**3) % p
            char = pow(disc, (p-1)//2, p)
            trace -= -1 if char == p-1 else char
        traces[K] = trace
        assert trace % 3 == 0
        if trace == 0:
            supersingular += 1
        if b0 in cube_roots:
            quotient_cube_cases += 1
            if trace:
                ordinary_intermediate += 1
                assert trace % 9 == 0
            zz = cube_roots[b0]
            images = set()
            for j in range(3):
                zzj = f.mul(zz, f.pow(z, j))
                X = f.add(f.mul(a0, zzj), f.scale(3, f.pow(zzj, 2)))
                images.add(X)
                cubic = f.sub(f.sub(f.pow(X, 3), f.scale(9, f.mul(f.mul(a0, b0), X))),
                              f.mul(b0, f.add(f.pow(a0, 3), f.scale(27, b0))))
                assert cubic == f.zero
                zz_back = f.div(f.add(f.mul(a0, X), f.scale(9, b0)),
                                f.add(f.pow(a0, 2), f.scale(3, X)))
                assert zz_back == zzj
            assert len(images) == 3
        elif trace:
            assert trace % 9 != 0
        curve_checks += 1

    scalar_cases = 0
    transformed_cases = 0
    excluded_classes = 0
    ordinary_inputs = 0
    supersingular_inputs = 0
    known_root = f.sub(f.one, z)
    known_cube = f.pow(known_root, 3)
    assert known_cube == f.scale(-3, delta)
    for gamma in cube_roots:
        A, B = gamma
        if B == 0:
            scalar_cases += 1
            assert f.pow(f.scalar(fp_cube_root(A)), 3) == gamma
            continue
        adjusted = gamma
        correction = f.one
        if (A-2*B) % p == 0 or (A-B) % p == 0:
            excluded_classes += 1
            adjusted = f.mul(gamma, known_cube)
            correction = known_root
        A, B = adjusted
        assert (A-2*B) % p and (A-B) % p
        denominator_inv = pow((A-2*B) % p, -1, p)
        t = (B-2*A)*denominator_inv % p
        s = (A*A-A*B+B*B)*denominator_inv % p
        assert t != 1 and s
        b0 = f.div(f.mul(delta, z), f.sub(f.scalar(t), z))
        assert adjusted == f.scale(s, b0)
        assert b0 in cube_roots
        root = f.div(f.scale(fp_cube_root(s), cube_roots[b0]), correction)
        assert f.pow(root, 3) == gamma
        c = fp_cube_root(27*pow((t**3-1) % p, -1, p))
        K = t*c % p
        if traces[K]:
            ordinary_inputs += 1
            assert traces[K] % 9 == 0
        else:
            supersingular_inputs += 1
        transformed_cases += 1
    assert scalar_cases + transformed_cases == len(cube_roots)
    return {
        "p": p,
        "admissible_curves": curve_checks,
        "cube_first_continuations": quotient_cube_cases,
        "ordinary_intermediate_curves": ordinary_intermediate,
        "supersingular_curves": supersingular,
        "nonzero_cubes": len(cube_roots),
        "scalar_inputs": scalar_cases,
        "transformed_inputs": transformed_cases,
        "excluded_class_adjustments": excluded_classes,
        "ordinary_transformed_inputs": ordinary_inputs,
        "supersingular_transformed_inputs": supersingular_inputs,
        "status": "PASS",
    }


def main():
    results = [run_prime(p) for p in (17, 53, 71, 107)]
    print(json.dumps({"checks": results, "all_checks_passed": True}, indent=2))


if __name__ == "__main__":
    main()
