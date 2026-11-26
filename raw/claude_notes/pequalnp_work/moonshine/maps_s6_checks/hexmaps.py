import sympy as sp
g, x, y, z = sp.symbols('g x y z')
def a1(v): x, y, z = v; return (6*g + y, -6*g - x - y, z - 2*g + x)
def a2(v): x, y, z = v; return (-y, x - 6*g, z + 3*g + y)
def ainf(v): x, y, z = v; return (x, y + x, z - g)
v = (x, y, z)
def it(f, n, v):
    for _ in range(n): v = f(v)
    return tuple(sp.expand(c) for c in v)
print("a1^3 :", it(a1, 3, v))
print("a2^4 :", it(a2, 4, v))
# composition order: a1 a2 ainf means apply ainf first? test both orders
print("a1(a2(ainf(v))):", tuple(sp.expand(c) for c in a1(a2(ainf(v)))))
print("ainf(a2(a1(v))):", tuple(sp.expand(c) for c in ainf(a2(a1(v)))))
# hexagonal coordinates X = t2 - t1, Y = t0 - t1, W = -(t0+t1+t2); Q = X^2 - XY + Y^2 ; 2Q + W^2 = 3(t0^2+t1^2+t2^2)
t0, t1, t2 = sp.symbols('t0 t1 t2')
X, Y, W = t2 - t1, t0 - t1, -(t0 + t1 + t2)
print("2Q+W^2 - 3 sum t^2 =", sp.expand(2*(X**2 - X*Y + Y**2) + W**2 - 3*(t0**2 + t1**2 + t2**2)))
# r(t) = (-t1,-t2,-t0): order 6 and action on (X,Y,W)
def r(t): return (-t[1], -t[2], -t[0])
tt = (t0, t1, t2)
rt = r(tt)
Xr, Yr, Wr = rt[2] - rt[1], rt[0] - rt[1], -(rt[0] + rt[1] + rt[2])
print("r on (X,Y,W):", sp.expand(Xr), sp.expand(Yr), sp.expand(Wr), " expected (X-Y, X, -W) =", sp.expand(X - Y), sp.expand(X), sp.expand(-W))
# S6-063 alpha: SL2(Z)->Z/12, alpha(S)=9, alpha(T)=1. Linear parts: a=[[0,1],[-1,-1]], S=[[0,-1],[1,0]], L=[[1,0],[1,1]]
A = sp.Matrix([[0, 1], [-1, -1]]); S = sp.Matrix([[0, -1], [1, 0]]); L = sp.Matrix([[1, 0], [1, 1]]); T = sp.Matrix([[1, 1], [0, 1]])
print("A*S*L =", A*S*L, " A^3 =", A**3, " S^2 =", S**2)
# express A, L as words in S, T to read alpha: L = S^-1 T^-1 S ? check
print("S^-1 T^-1 S =", S.inv()*T.inv()*S, " S T^-1 S^-1 =", S*T.inv()*S.inv())
# A in terms of S,T: try T S, S T, -S T etc.
for name, M in [("ST", S*T), ("TS", T*S), ("-ST", -S*T), ("(ST)^-1", (S*T).inv()), ("(TS)^-1", (T*S).inv()), ("-TS", -T*S), ("S^-1T^-1", S.inv()*T.inv()), ("T^-1S^-1", T.inv()*S.inv()), ("-T^-1 S^-1", -T.inv()*S.inv()), ("-S^-1T^-1", -S.inv()*T.inv())]:
    if M == A: print("A =", name)
