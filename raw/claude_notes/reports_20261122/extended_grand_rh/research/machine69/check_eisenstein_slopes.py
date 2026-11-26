"""Exact finite-field, lattice and logarithmic derivative checks for radicand 269."""
from collections import Counter, defaultdict
from math import isqrt

Q = 269
N = 3600


def mul(u, v):
    a, b = u
    c, d = v
    return ((a*c - b*d) % Q, (a*d + b*c - b*d) % Q)


def power(u, n):
    result = (1, 0)
    while n:
        if n % 2:
            result = mul(result, u)
        u = mul(u, u)
        n //= 2
    return result


def norm(a, b):
    return a*a - a*b + b*b


def factors(n):
    pf = {}
    d = 2
    while d*d <= n:
        while not n % d:
            pf[d] = pf.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        pf[n] = 1
    return pf


def main():
    # b=0 is the last projective point. Powers name the three complex phases by 0,1,2.
    names = {(1, 0): 0, (0, 1): 1, (Q-1, Q-1): 2}
    dirs = [names[power((d,1), (Q*Q-1)//3)] for d in range(Q)]
    dirs.append(names[power((1,0), (Q*Q-1)//3)])
    assert Counter(dirs) == {0:90, 1:90, 2:90}

    def phase(a, b):
        a, b = a % Q, b % Q
        if a == b == 0:
            return None
        return dirs[Q] if b == 0 else dirs[a * pow(b,-1,Q) % Q]

    def signed(a, b):
        j = phase(a, b)
        return 0 if j is None else 2 if j == 0 else -1

    fibers = defaultdict(Counter)
    units = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1)]
    for a in range(Q):
        for b in range(Q):
            j = phase(a, b)
            if j is None:
                continue
            assert all(phase(*mul((a,b),u)) == j for u in units)
            assert phase(a-b,-b) == (-j) % 3
            fibers[norm(a,b) % Q][j] += 1
    assert len(fibers) == Q-1
    assert all(count == {0:90, 1:90, 2:90} for count in fibers.values())

    w_sum = [0] * (N+1)
    rad = isqrt(4*N//3) + 1
    split_checks = 0
    for a in range(-rad, rad+1):
        for b in range(-rad, rad+1):
            n = norm(a,b)
            if 0 < n <= N:
                w_sum[n] += signed(a,b)
    assert all(value % 12 == 0 for value in w_sum)
    # a(n) = 1/12 times the full, oriented, signed lattice-shell sum.
    coeff = [v//12 for v in w_sum]
    assert coeff[1] == 1
    for p in range(5, N+1):
        if p == Q or p % 3 != 1 or factors(p) != {p:1}:
            continue
        t = 3*int(pow(Q,(p-1)//3,p)==1)-1
        assert coeff[p] == t
        split_checks += 1

    inverse = [0] * (N+1)
    inverse[1] = 1
    for i in range(1,N+1):
        for j in range(2,N//i+1):
            inverse[i*j] -= inverse[i] * coeff[j]

    # For all n, compare the coefficient of log(p) in ((a log)*a^{-1})(n)
    # with the prime-power trace in the Artin Euler factors.
    terms = [Counter() for _ in range(N+1)]
    for i in range(1, N+1):
        for p, exponent in factors(i).items():
            for j in range(1,N//i+1):
                terms[i*j][p] += coeff[i]*exponent*inverse[j]
    for n in range(2,N+1):
        pf = factors(n)
        expected = {}
        if len(pf) == 1:
            (p,k), = pf.items()
            if p == Q:
                trace = 0
            elif p == 3:
                trace = 1
            elif p % 3 == 2:
                trace = 2*int(k%2 == 0)
            else:
                t = 3*int(pow(Q,(p-1)//3,p)==1)-1
                prev, trace = 2,t
                for _ in range(1,k):
                    prev, trace = trace,t*trace-prev
            if trace:
                expected[p] = trace
        assert {p:v for p,v in terms[n].items() if v} == expected, n
    print(f"PASS: {Q+1} projective slopes; all {Q*Q-1} nonzero residues and six units;")
    print(f"{Q-1} norm fibres; {split_checks} split primes and {N-1} log-derivative coefficients.")


if __name__ == "__main__":
    main()
