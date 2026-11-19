"""Intake check (Claude Opus 5.5 at effort max, 19 Nov 2026) of RESEARCH_SA17 Prop. A4:all-primes.
Independent of the run's code. In the run's example the boundary classes live in
H = (+)_j W t^j eps, and after evaluating coefficients at (0,0) the two boundary maps are
  additive:     c = sum s_j t^j  ->  c'(t)   in k[t]/(t^p)   (coefficient of t^j -> e_j)
  logarithmic:  u (unit)         ->  u'/u    in k[t]/(t^p)
because t_x^j - t_y^j = j t^(j-1) (t_x - t_y) and t_x - t_y = eps/(xy), eps^2 = 0.
We enumerate both images over F_p for p = 2,3,5,7 and compare with the run's claims:
  additive image = {c_(p-1) = 0},  log image = {c_(p-1) = c_0}."""
import itertools, sys

def mul(a, b, p):
    n = len(a); r = [0]*n
    for i, ai in enumerate(a):
        if ai:
            for j in range(n - i):
                r[i+j] = (r[i+j] + ai*b[j]) % p
    return r

def inv(u, p):
    # inverse of a unit in F_p[t]/(t^p) by Newton/series
    n = len(u); c0 = pow(u[0], p-2, p)
    r = [0]*n; r[0] = c0
    for k in range(1, n):
        s = sum(u[i]*r[k-i] for i in range(1, k+1)) % p
        r[k] = (-s*c0) % p
    return r

def deriv(u, p):
    n = len(u)
    return [((i+1)*u[i+1]) % p for i in range(n-1)] + [0]

out = []
for p in (2, 3, 5, 7):
    n = p
    add_img = set(); log_img = set()
    for coeffs in itertools.product(range(p), repeat=n):
        c = list(coeffs)
        add_img.add(tuple(deriv(c, p)))
        if c[0] != 0:
            u = c
            log_img.add(tuple(mul(deriv(u, p), inv(u, p), p)))
    hyper_add = {v for v in itertools.product(range(p), repeat=n) if v[n-1] == 0}
    hyper_log = {v for v in itertools.product(range(p), repeat=n) if v[n-1] == v[0]}
    w = [1, 1] + [0]*(n-2)                       # u = 1 + t
    wl = tuple(mul(deriv(w, p), inv(w, p), p))
    res = dict(p=p, additive_image_size=len(add_img), log_image_size=len(log_img),
               additive_equals_claim=(add_img == hyper_add), log_equals_claim=(log_img == hyper_log),
               images_equal=(add_img == log_img), dlog_1_plus_t=wl, dlog_1_plus_t_in_additive=(wl in add_img))
    out.append(res); print(res)
ok = all(r['additive_equals_claim'] and r['log_equals_claim'] and not r['images_equal'] for r in out)
print('ALL CLAIMS CONFIRMED' if ok else 'MISMATCH')
