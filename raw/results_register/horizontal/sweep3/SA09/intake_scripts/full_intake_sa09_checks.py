# Computations for the full intake of RESEARCH_SA09 (21-22 Nov 2026).
# Claude Opus 5.5 at effort max, agent a34c04448e8299803. Standard library only; runs no program of the return.
import math, sys
sys.stdout.reconfigure(encoding='utf-8')


def vp(n, p):
    if n == 0:
        return 10**9
    v = 0
    while n % p == 0:
        n //= p; v += 1
    return v


def formula(n, m, l):
    s, h = min(n, m), abs(n - m)
    if l > 2:
        return min(s, 1 + vp(h, l)) if h % (l - 1) == 0 else 0
    return min(s, 1) if h % 2 else min(s, 2 + vp(h, 2))


print('A1.9: v_l(D_{n,m}) against gcd_{0<=lam<=400} |lam^n - lam^m|, 1 <= m < n <= 14, primes l <= 31')
bad = 0; tested = 0
for n in range(2, 15):
    for m in range(1, n):
        g = 0
        for lam in range(0, 401):
            g = math.gcd(g, abs(lam**n - lam**m))
        for l in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
            tested += 1
            if vp(g, l) != formula(n, m, l):
                bad += 1; print('   mismatch', n, m, l, vp(g, l), formula(n, m, l))
print('   tested', tested, 'mismatches', bad)

print('A2.5: G = {(x,y) in Z/16 + Z/4 : x = 2y mod 4}')
G = [(x, y) for x in range(16) for y in range(4) if x % 4 == (2 * y) % 4]


def order(e):
    k, (x, y) = 1, e
    while ((k * x) % 16, (k * y) % 4) != (0, 0):
        k += 1
    return k


print('   order', len(G), '; exponent', max(order(e) for e in G), '; order of (2,1):', order((2, 1)),
      '; kernel of projection to y:', [e for e in G if e[1] == 0])

print('A4.4: rank L_n = 1 + 2 sum_{i=1}^n C(n,i) = 2^{n+1} - 1 for n <= 20:',
      all(1 + 2 * sum(math.comb(n, i) for i in range(1, n + 1)) == 2**(n + 1) - 1 for n in range(21)))
print('A3.1: C(m+n+1,n+1) = sum_i C(m,i) C(n+1,i) for m,n <= 15:',
      all(math.comb(m + n + 1, n + 1) == sum(math.comb(m, i) * math.comb(n + 1, i) for i in range(n + 2))
          for m in range(16) for n in range(16)))
