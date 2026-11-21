import sys, mpmath as mp
sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 50
xi = lambda s: s*(s-1)/2 * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)
def lam(n):  # Li coefficient: (1/(n-1)!) d^n/ds^n [s^(n-1) log xi(s)] at s = 1
    return mp.diff(lambda s: s**(n-1) * mp.log(xi(s)), 1, n, singular=True) / mp.factorial(n-1)
N = 10
L = [mp.mpf(0)] + [lam(n) for n in range(1, N + 1)]
print("lambda_1..4:", [mp.nstr(x, 12) for x in L[1:5]])
for M in range(1, N + 1):
    T = mp.matrix(M + 1, M + 1)
    for j in range(M + 1):
        for k in range(M + 1):
            T[j, k] = L[abs(j - k)]
    ev = mp.eigsy(T)[0]
    pos = sum(1 for x in ev if x > 0); neg = sum(1 for x in ev if x < 0)
    print(f"Toeplitz section size {M+1}: positive {pos}, negative {neg}, smallest |ev| {mp.nstr(min(abs(x) for x in ev), 4)}")
