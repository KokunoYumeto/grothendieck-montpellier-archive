# For each of the 23 Niemeier root systems: Coxeter frame shape pi^X, check a_{h/d} = -a_d, sum a_d = 0,
# Fricke constant prod d^{a_d/2} vs sqrt(det R) = glue order, constant term of T^X = 1/eta_pi = -#components.
import sys; sys.path.insert(0, '.')
from fractions import Fraction as Fr
from math import isqrt, prod
from collections import Counter
from qs import etaq
def frame(t, n):
    c = Counter()
    if t == 'A':   # (x^{n+1}-1)/(x-1)
        c[n+1] += 1; c[1] -= 1
    elif t == 'D': # (x^{n-1}+1)(x+1) = (x^{2n-2}-1)/(x^{n-1}-1) * (x^2-1)/(x-1)
        c[2*n-2] += 1; c[n-1] -= 1; c[2] += 1; c[1] -= 1
    elif t == 'E' and n == 6:  # Phi12 Phi3
        for d, e in [(12, 1), (6, -1), (4, -1), (2, 1), (3, 1), (1, -1)]: c[d] += e
    elif t == 'E' and n == 7:  # Phi18 Phi2
        for d, e in [(18, 1), (9, -1), (6, -1), (3, 1), (2, 1), (1, -1)]: c[d] += e
    elif t == 'E' and n == 8:  # Phi30
        for d, e in [(30, 1), (15, -1), (10, -1), (6, -1), (5, 1), (3, 1), (2, 1), (1, -1)]: c[d] += e
    return c
def det(t, n): return {'A': n+1, 'D': 4}.get(t, {6: 3, 7: 2, 8: 1}.get(n))
def cox(t, n): return {'A': n+1, 'D': 2*n-2}.get(t, {6: 12, 7: 18, 8: 30}.get(n))
X = {
 'A1^24': [('A',1)]*24, 'A2^12': [('A',2)]*12, 'A3^8': [('A',3)]*8, 'A4^6': [('A',4)]*6,
 'A5^4D4': [('A',5)]*4+[('D',4)], 'D4^6': [('D',4)]*6, 'A6^4': [('A',6)]*4, 'A7^2D5^2': [('A',7)]*2+[('D',5)]*2,
 'A8^3': [('A',8)]*3, 'A9^2D6': [('A',9)]*2+[('D',6)], 'D6^4': [('D',6)]*4, 'E6^4': [('E',6)]*4,
 'A11D7E6': [('A',11),('D',7),('E',6)], 'A12^2': [('A',12)]*2, 'D8^3': [('D',8)]*3, 'A15D9': [('A',15),('D',9)],
 'A17E7': [('A',17),('E',7)], 'D10E7^2': [('D',10),('E',7),('E',7)], 'D12^2': [('D',12)]*2, 'A24': [('A',24)],
 'D16E8': [('D',16),('E',8)], 'E8^3': [('E',8)]*3, 'D24': [('D',24)]}
for name, comps in X.items():
    pi = Counter()
    for t, n in comps: pi.update(frame(t, n))
    pi = {d: a for d, a in pi.items() if a != 0}
    h = cox(*comps[0])
    anti = all(pi.get(h//d, 0) == -a for d, a in pi.items())
    fr = prod(Fr(d)**a for d, a in pi.items())  # = prod d^{a_d} ; Fricke constant = sqrt
    D = prod(det(t, n) for t, n in comps)
    glue = isqrt(D)
    fc2 = fr  # prod d^{a_d}
    # T^X = 1/eta_pi = prod eta(d tau)^{-a_d}; leading q^{-sum d a_d/24}
    lead = -sum(d*a for d, a in pi.items())
    T = etaq({d: -a for d, a in pi.items()}, 4)
    print(f"{name:10s} h={h:2d} pi={dict(sorted(pi.items()))} sum a={sum(pi.values())} lead q^{Fr(lead,24)} "
          f"W_h-anti={anti} prod d^a_d={fc2} det R={D} glue={glue} Fricke^2==det:{fc2==D} "
          f"T^X const={T[1]} comps={len(comps)} q-coef={T[2]}")
