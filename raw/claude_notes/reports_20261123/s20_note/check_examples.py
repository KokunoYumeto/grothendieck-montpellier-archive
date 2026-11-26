# Exact check of the two hand examples: values of h1, h2 at random x in R lie in R.
# Series over F2 / F4 truncated mod t^N. F4 = {0,1,w,w^2} encoded 0..3 with w=2, w^2=3=w+1.
import random
N = 60
def f4mul(a, b):
    if a == 0 or b == 0: return 0
    lg = {1: 0, 2: 1, 3: 2}; ex = [1, 2, 3]
    return ex[(lg[a] + lg[b]) % 3]
def mul(a, b):  # truncated product, coefficients in F4 (F2 is a subfield)
    c = [0] * N
    for i, ai in enumerate(a):
        if ai:
            for j in range(N - i):
                if b[j]: c[i + j] ^= f4mul(ai, b[j])
    return c
def add(a, b): return [x ^ y for x, y in zip(a, b)]
def shift(a, k):  # multiply by t^k (k may be negative: exact division required)
    if k >= 0: return [0] * k + a[:N - k]
    assert all(v == 0 for v in a[:-k]), "division not exact"
    return a[-k:] + [0] * (-k)   # top coefficients unknown -> padded; we lose precision -k
def scal(c, a): return [f4mul(c, x) for x in a]
def pw(a, e):
    r = [1] + [0] * (N - 1)
    for _ in range(e): r = mul(r, a)
    return r
def check(name, gen_x, in_R, build, prec):
    for trial in range(400):
        x = gen_x()
        h1, h2 = build(x)
        assert in_R(h1[:prec]) and in_R(h2[:prec]), (name, trial)
    print(name, "ok: 400 random x, h1(x), h2(x) in R to precision t^%d" % prec)
# Example 1: R = F2[[t^2,t^3]] (no t^1 term), V = F2[[t]]
def gen1():
    x = [random.randint(0, 1) for _ in range(N)]; x[1] = 0; return x
def inR1(y): return all(v in (0, 1) for v in y) and y[1] == 0
def build1(x):
    q = shift(add(mul(x, x), x), -2)          # (x^2+x)/t^2
    h2 = pw(shift(add(q, mul(q, q)), -1), 4)  # ((q+q^2)/t)^4
    h1 = add(q, shift(h2, 1))                 # q + t h2  (char 2)
    return h1, h2
check("F2[[t^2,t^3]]", gen1, inR1, build1, N - 8)
# Example 2: R = F2 + t F4[[t]], V = F4[[t]]
def gen2():
    x = [random.randint(0, 3) for _ in range(N)]; x[0] = random.randint(0, 1); return x
def inR2(y): return y[0] in (0, 1)
def build2(x):
    q = shift(add(mul(x, x), x), -1)          # (x^2+x)/t
    h2 = add(q, mul(q, q))                    # q + q^2
    h1 = add(q, scal(2, h2))                  # q + w h2
    return h1, h2
check("F2+tF4[[t]]", gen2, inR2, build2, N - 4)
# Sanity: q itself is not R-valued in example 1
x = [0, 0, 0, 1] + [0] * (N - 4)  # x = t^3
q = shift(add(mul(x, x), x), -2)
print("example 1: q(t^3) =", q[:4], "(t-coefficient 1, so q is not in Int(R))")
