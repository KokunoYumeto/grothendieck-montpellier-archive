import sympy as sp
t = sp.symbols('t')
A = -sp.Rational(3, 4)*t**3*(t-1); B = sp.Rational(1, 4)*t**4*(t-1)**2      # S6-001 E_t
Delta = sp.factor(-16*(4*A**3 + 27*B**2)); print("Delta(E_t) =", Delta)
j = sp.factor(1728*4*A**3/(4*A**3 + 27*B**2)); print("j(E_t) =", j)
J = 1728*t; a = -3*J/(J-1728); b = -2*J/(J-1728)                            # AG-027 E(J)
d = -t*(t-1)/2
print("A == d^2 a:", sp.simplify(A - d**2*a) == 0, "  B == d^3 b:", sp.simplify(B - d**3*b) == 0)
# AG-003: P' = (Z,Y) = (-a4/3, -a6/2) on Y^2 = Z^3 + D/108, D = 4a4^3+27a6^2 ; normalized Z0 = Z*(108/D)^(1/3): -Z0^3 = 4a4^3/D = j/1728
D = 4*A**3 + 27*B**2
print("-Z0^3 =", sp.factor(-(-A/3)**3*108/D), "  j/1728 =", sp.factor(j/1728))
# S6-012 m=3 norm law at P_t = (0, t^2(t-1)/2): psi_3(0) = -a4^2 ; |Delta|^{2/3}/|psi_3|
psi3 = -A**2
print("Delta^(2/3)/psi3^... : Delta =", Delta, " psi3(0) =", sp.factor(psi3))
print("ratio^3 = Delta^2/psi3^3 =", sp.factor(Delta**2/psi3**3))
# S6-030: j/1728 = 4t(1-t) -> (2t-1)^2 = -(j-1728)/1728
s = sp.symbols('s')
print("S6-030:", sp.factor(1728*4*s*(1-s) - 1728), " = -1728(2s-1)^2 ?", sp.expand(1728*4*s*(1-s) - 1728 + 1728*(2*s-1)**2) == 0)
# S6-033 vs S6-029: j = -110592 s(s+1)^3/(8s+9), x = -24 s - 27 -> (x+27)(x+3)^3/x
x = -24*s - 27
print("S6-033 j - S6-029 j(x):", sp.simplify(-110592*s*(s+1)**3/(8*s+9) - (x+27)*(x+3)**3/x))
# K = t^4/(t-1)^3 = t * u^-3 with u = 1 - 1/t (AG-004's u = 1 - 1728/j at j = 1728 t)
u = 1 - 1/t
print("K == t*u^-3:", sp.simplify(t**4/(t-1)**3 - t*u**-3) == 0)
# Theta_J - Theta_Leech
aa, bb = sp.symbols('a b')
TJ = aa**12 - 72*aa**9*bb + 24786*aa**6*bb**2 + 866052*aa**3*bb**3 + 2480058*bb**4
TL = aa**12 - 72*aa**9*bb + 198288*aa**6*bb**2 + 8503056*aa**3*bb**3 + 14171760*bb**4
TM = aa**12 + 192456*aa**6*bb**2 + 8660520*aa**3*bb**3 + 12754584*bb**4
print("Theta_J - Theta_Leech =", sp.factor(TJ - TL))
print("Theta_M - Theta_Leech =", sp.factor(TM - TL), "  (should be 72 Delta = 72 b (a^3-27b)^3):", sp.expand(TM - TL - 72*bb*(aa**3 - 27*bb)**3) == 0)
print("Theta_J - Theta_M =", sp.factor(TJ - TM))
