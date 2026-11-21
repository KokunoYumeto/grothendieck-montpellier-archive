import sympy as sp, itertools
v,Q=sp.symbols('v Q')
D=(v+1/v)**2
Delta=sp.simplify((D-1)/D-4*(D-1)/D**2)
print('Delta =',sp.factor(Delta))
num=sp.factor(sp.numer(sp.together(Delta)))
print('numerator roots:',[ (r, sp.Abs(r).evalf()) for r in sp.Poly(sp.expand(num),v).nroots()])
# trace form on C=R[x]/(x(x-Delta)), basis 1,x ; eigenvalues of x: 0, Delta
d=sp.symbols('d')
G=sp.Matrix([[2,d],[d,d**2]])
print('Gram det:',sp.factor(G.det()),' kernel at d=0:',G.subs(d,0).nullspace())
# Moebius on Boolean cube: sum_{I subset [a]} (-1)^|I| v^(a-2|I|) = (v-1/v)^a
for a in range(1,6):
    s=sum((-1)**len(I)*v**(a-2*len(I)) for k in range(a+1) for I in itertools.combinations(range(a),k))
    assert sp.expand(s-(v-1/v)**a)==0
print('Boolean Moebius identity checked a=1..5')
# based count of F_Q is Q+1; D at v=sqrt(Q) equals (Q+1)^2/Q
print('D(sqrt Q) - (Q+1)^2/Q =',sp.simplify(D.subs(v,sp.sqrt(Q))-(Q+1)**2/Q))
