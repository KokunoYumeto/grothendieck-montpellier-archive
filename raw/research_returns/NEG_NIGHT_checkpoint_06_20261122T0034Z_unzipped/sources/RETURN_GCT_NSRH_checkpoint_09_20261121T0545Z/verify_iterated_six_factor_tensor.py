"""F67: exact source-normalized Delta^(3,3) whole-tensor certificate."""
import sympy as s

v = s.symbols('v', nonzero=True)
m, a = s.symbols('m a')
I2 = s.eye(2)
N1 = s.Matrix([[m,a],[0,0]])
N2 = s.Matrix([[0,0],[a,m]])
R = [s.kronecker_product(N,N)+s.kronecker_product(m*I2-N,m*I2-N) for N in (N1,N2)]
expected = [
    s.Matrix([[m*m,m*a,m*a,2*a*a],[0,0,0,-m*a],[0,0,0,-m*a],[0,0,0,m*m]]),
    s.Matrix([[m*m,0,0,0],[-m*a,0,0,0],[-m*a,0,0,0],[2*a*a,m*a,m*a,m*m]]),
]
for actual,wanted in zip(R,expected):
    assert actual==wanted
    assert actual*actual==m*m*actual
product = R[0]*R[1]
diagonal = [s.expand(product[i,i]) for i in range(4)]
assert diagonal==[m**4-2*m*m*a*a+4*a**4,-m*m*a*a,-m*m*a*a,m**4]
assert s.expand(s.trace(product)-(m**4+(2*a*a-m*m)**2))==0

delta=v+1/v
D=s.expand(delta*delta)
m3=s.expand(delta**3)
a3=s.expand(3*D-4)
assert all(t.as_coeff_Mul()[0]>0 for t in s.Add.make_args(m3))
assert all(t.as_coeff_Mul()[0]>0 for t in s.Add.make_args(a3))
assert s.expand(m3*m3-a3*a3-(D-1)*(D-4)**2)==0
A6=s.expand(2*a3*a3-m3*m3)
assert s.expand(A6-(-D**3+18*D**2-48*D+32))==0
trace=s.expand((m**4+(2*a*a-m*m)**2).subs({m:m3,a:a3}))
coeff={-12:2,-10:-12,-8:192,-6:388,-4:1134,-2:1416,0:1952,
       2:1416,4:1134,6:388,8:192,10:-12,12:2}
assert s.expand(trace-sum(c*v**e for e,c in coeff.items()))==0
assert trace.subs(v,1)==8192
assert sum(c for c in coeff.values() if c>0)==8216
assert -sum(c for c in coeff.values() if c<0)==24

# The chosen regular two-state lattice is NOT an ambient S3 lattice at v=1.
G1=s.Matrix([[1,2],[0,-1]])
G2=s.Matrix([[-1,0],[2,1]])
assert G1**2==I2 and G2**2==I2
assert (G1*G2)**3==s.Matrix([[7,6],[-6,-5]])
assert (G1*G2)**3!=I2

print('PASS: both source coproduct matrices and quadratics; full four-entry product diagonal')
print('diagonal =',diagonal)
print('PASS: effective k=3 input characters and exact generic irreducibility factor')
print('A6 =',A6)
print('whole P1 P2 trace =',trace)
print('PASS: negative coefficients -12 at v^10 and v^-10; value8192 at v=1')
print('PASS: explicit mixed Tate multiplicities8216 positive,24 negative')
print('PASS: chosen input lattice fails ambient S3 product-cube relation at v=1')
