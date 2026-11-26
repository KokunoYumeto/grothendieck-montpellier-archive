# Independent recomputation of Paper II (BEYOND_DIRICHLET cp10) certificate for disc 8249 and 60061
import sys
from mpmath import mp, mpf, quad, euler, pi, log, exp, cosh, sqrt
from sympy import Poly, symbols, factor_list, GF, primerange, discriminant, factorint
x = symbols('x')
mp.dps = 40
def cycle_type(f, p):
    fl = Poly(f, x, modulus=p).factor_list()[1]
    degs=[]
    for g,e in fl:
        if e!=1: return None
        degs.append(g.degree())
    return sorted(degs)
def chiR(degs, k):
    # permutation u^k where u has cycle type degs
    # cycles of length d under k-th power split into gcd(d,k) cycles of length d/gcd
    from math import gcd
    cyc=[]
    for d in degs:
        g=gcd(d,k); cyc += [d//g]*g
    a=cyc.count(1); b=cyc.count(2)
    sgn=1
    for c in cyc: sgn *= (-1)**(c-1)
    return sgn + a*(a-3)//2 + b
def run(fexpr, ram, Qexp, A=8):
    f = fexpr
    D = discriminant(Poly(f,x))
    print("disc", D, factorint(D))
    eA = exp(A)
    P = mpf(0)
    for p in primerange(2, int(eA)+1):
        k=1
        while p**k <= eA:
            if p in ram:
                t = ram[p](k)
            else:
                ct = cycle_type(f,p)
                if ct is None: raise Exception("ramified %d"%p)
                t = chiR(ct,k)
            P += 4*t*log(p)/(p**k+1)*(1-k*log(p)/A)
            k+=1
    Q = mpf(abs(D))**Qexp
    C = log(Q) - 6*euler - pi - 18*log(2) - 6*log(pi)
    g = lambda t: (1-t/A)/cosh(t/2) if t<A else mpf(0)
    K = lambda t: (4*exp(-t/2)+2*exp(-3*t/2))/(1-exp(-2*t))
    J = lambda t: mpf(3)/A if t==0 else K(t)*(1-g(t))
    I = quad(J, [0, 1, A]) + quad(K,[A, mp.inf])
    H0 = 2*quad(g,[0,A])
    S = C + 2*I - P
    print("C",C); print("I",I); print("P",P); print("S",S); print("2H(0)",2*H0, "margin", 2*H0-S)
f1 = x**5-2*x**4-x**3+4*x+1
run(f1, {73: lambda k: 3 if k%3==0 else 0, 113: lambda k: 2+(-1)**k}, 3)
f2 = x**5+2*x**3+2*x**2-2*x+1
run(f2, {17: lambda k: 2+(-1)**k, 3533: lambda k: 3}, 3)
