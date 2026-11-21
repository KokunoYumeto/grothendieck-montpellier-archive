"""Exact finite checks for P-F52; source: GCT VII Figure 1, printed p.30.

This verifies the transcribed projection and its product Gram form. It does
not use the inconsistent two-by-two matrices printed on p.20.
"""
import sympy as s

q = s.symbols("q", positive=True)
f = (q**4+1)*(q**4-q**2+1)*(q**2+1)/q**5
a = q**6-1
b = (q**2-1)**2*(q**4+q**2+1)
c = (q**2+1)**2*(q**2-1)
h = (q**2+1)*(q**8-q**6+q**4-q**2+1)/q**5
e = (q**2+1)/q
k = (q**4+1)/q**2
j = -(q**8-q**6-2*q**4-q**2+1)/q**4
rows = [
    {1:f},
    {2:q*(q**4+1),5:k},
    {3:h,6:a/q**4,9:e},
    {4:(q**8-q**6+q**4+1)/q**3,7:b/q**6,10:a/q**5,13:k},
    {2:k,5:(q**4+1)/q**5},
    {3:c/q**2,6:2*e,9:-c/q**2},
    {4:b/q**2,7:(2*q**8+q**6-2*q**2+1)/q**5,10:j,13:-a/q},
    {8:h,11:c/q**4,14:e},
    {3:e,6:-a/q**4,9:h},
    {4:a/q,7:j,10:(q**8-2*q**6+q**2+2)/q**3,13:b/q**2},
    {8:a/q**2,11:2*e,14:-a/q**2},
    {12:q*(q**4+1),15:k},
    {4:k,7:-a/q**5,10:b/q**6,13:(q**8+q**4-q**2+1)/q**5},
    {8:e,11:-c/q**4,14:h},
    {12:k,15:(q**4+1)/q**5},
    {16:f},
]
P = s.zeros(16)
for i, entries in enumerate(rows):
    for col, val in entries.items():
        P[i,col-1] = val

two = q+q**-1
three = q**2+1+q**-2
d = [s.Integer(1),q**-1*three,three*two**2,q**3*three**2*two**2]
gram = s.diag(*(d[i]*d[j] for i in range(4) for j in range(4)))

def zero_matrix(M):
    return all(s.cancel(v) == 0 for v in M)

assert zero_matrix(gram*P-P.T*gram)
assert zero_matrix(P*P-f*P)
Q = f*s.eye(16)-P
assert zero_matrix(gram*Q-Q.T*gram)
assert zero_matrix(Q*Q-f*Q)

S = (q**10+q**-10+3*(q**8+q**-8)+(q**6+q**-6)
     +5*(q**4+q**-4)-2*(q**2+q**-2)+16)
v = q**2+q**-2-2
R = 3*v**4+23*v**3+57*v**2+48*v+16
assert s.cancel(S-f**2-R) == 0

# Basis-normalization identity for the descended two-dimensional space.
x, pp = s.symbols("x pp")
change = s.Matrix([[1,x],[1,-x]])
diag = s.diag((pp+x)/(2*q**20),(pp-x)/(2*q**20))
M = change.inv()*diag*change
assert zero_matrix(M-s.Matrix([[pp,x**2],[1,pp]])/(2*q**20))

print("PASS: 16x16 source projection, product Gram self-adjointness, complement,")
print("positive scalar identity, and exact descended 2x2 normalization.")

# All coefficients, not only the leading terms, of VII Figures 2 and 7.
# The lists below transcribe the actual source polynomials in ascending
# even powers; the factorizations are checked independently afterward.
def evenpoly(vals, start=0):
    return sum(s.Integer(val)*q**(start+2*i) for i,val in enumerate(vals))

R = -3*q**28-4*q**24+2*q**22-10*q**20+2*q**18-4*q**16-3*q**12
D = (q**8+1)**2*q**24*(5*q**16+8*q**12-4*q**10+18*q**8
                        -4*q**6+8*q**4+5)
g1 = (-R-x)/(2*q**20)
g2 = (-R+x)/(2*q**20)
g3 = q**4+2+q**-4
g4 = q**6+2+q**-6
g5 = q**10+2+q**-10
E1 = g3+g4+g5
E2 = g3*g4+g3*g5+g4*g5
E3 = g3*g4*g5
L = -R/q**20
NN = (q**4-q**2+1)**2*(q**12+q**10+2*q**8+2*q**4+q**2+1)**2/q**16
assert s.cancel((R**2-D)/(4*q**40)-NN) == 0
assert s.cancel(L+E1-S) == 0

source_a = [
    -(q**12+q**10+2*q**8+2*q**4+q**2+1)**2
      *(q**8-q**6+q**4-q**2+1)**2*(q**2+1)**4
      *(q**4-q**2+1)**4*(q**4+1)**2/q**36,
    evenpoly([1,1,7,5,18,21,20,73,-14,187,-107,328,-197,402,
              -197,328,-107,187,-14,73,20,21,18,5,7,1,1])
      *(q**2+1)**2*(q**4-q**2+1)**2/q**32,
    -evenpoly([1,3,8,4,33,12,76,27,115,113,80,253,-9,360,
               -9,253,80,113,115,27,76,12,33,4,8,3,1])/q**26,
    evenpoly([3,2,8,5,17,30,11,61,-15,108,-15,61,11,30,17,5,8,2,3])/q**18,
    -S,
    s.Integer(1),
]
factored_a = [-NN*E3,NN*E2+L*E3,-NN*E1-L*E2-E3,
              NN+L*E1+E2,-L-E1,s.Integer(1)]
for j,(left,right) in enumerate(zip(source_a,factored_a)):
    assert s.cancel(left-right) == 0, ("relation coefficient",j)

Pscalar = q**20*(22-2*(q**2+q**-2)+6*(q**4+q**-4)
                         +2*(q**6+q**-6)+3*(q**8+q**-8)+2*(q**10+q**-10))
b1constant = evenpoly([3,-3,9,2,-1,47,-84,210,-295,462,-516,604,
                       -516,462,-295,210,-84,47,-1,2,9,-3,3],12)
b1x = evenpoly([1,-1,1,4,-9,19,-24,30,-24,19,-9,4,1,-1,1])
b2constant = evenpoly([3,2,9,1,24,18,22,45,-2,92,-2,45,22,18,24,1,9,2,3],12)
b2x = 1+q**4+q**6+6*q**10+q**14+q**16+q**20
source_b = [
    (q**4-q**2+1)**2*(q**8-q**6+q**4-q**2+1)**2*(q**4+1)**2
       *(q**2+1)**4*(-R+x)/(2*q**40),
    -(q**2+1)**2*(b1constant+x*b1x)/(2*q**36),
    (b2constant+x*b2x)/(2*q**30),
    -(Pscalar+x)/(2*q**20),
    s.Integer(1),
]
factored_b = [g2*E3,-E3-g2*E2,E2+g2*E1,-E1-g2,s.Integer(1)]
for j,(left,right) in enumerate(zip(source_b,factored_b)):
    assert s.cancel(left-right) == 0, ("cell coefficient",j)

def quadratic_zero(expr):
    num,den = s.fraction(s.cancel(expr))
    rem = s.rem(num,x*x-D,x)
    return s.cancel(rem) == 0

# (t-g1)*p1(t)=r(t), compared in all six coefficients modulo x²=D.
for j in range(6):
    coeff = (source_b[j-1] if j else 0) - (g1*source_b[j] if j<5 else 0)
    assert quadratic_zero(coeff-source_a[j]), ("full eigenidentity",j)
print("PASS: all six relation coefficients and all five cell coefficients;")
print("complete (t-g1)*p1(t)=r(t) identity modulo x^2=D, independently of blocks.")

# Alternative normalization: actual positive action and both positive
# Lefschetz coefficient lists do not characterize the source factor F.
H = (q+1+q**-1)**4
T = Pscalar/q**20
N = s.cancel((Pscalar**2-D)/(4*q**40))
alphaH = [390,336,242,160,139,132,128,112,103,88,70,44,23,8,2]
betaH = [169556,164696,152852,139200,127656,118312,109695,
         100480,90558,79776,68121,55832,44025,33832,25905,20000,
         15558,12016,9093,6632,4587,2936,1699,864,377,136,39,8,1]
def symmetric_polynomial(vals):
    return vals[0]+sum(v*(q**j+q**-j) for j,v in enumerate(vals[1:],1))
assert s.cancel(H*T-symmetric_polynomial(alphaH)) == 0
assert s.cancel(H**2*N-symmetric_polynomial(betaH)) == 0
for vals in [alphaH,betaH]:
    assert min(vals)>0
    assert all(a>=b for a,b in zip(vals,vals[1:]))
assert alphaH[0]+2*sum(alphaH[1:]) == 3564
assert betaH[0]+2*sum(betaH[1:]) == 2939328
print("PASS: alternative H normalization, full positive nonincreasing trace/norm")
print("coefficient certificates and both values at one.")

# Actual source interpolation denominator and the prescribed normalization.
r = s.symbols("r", positive=True)
eigen = [r**9,-r**-3,r**-11,-r**-15]  # q=r² clears half powers
fp_product = s.prod(eigen[i]-eigen[j] for i in [0,2] for j in range(4) if j!=i)
fp_formula = -q**-33*(q**10-1)**2*(q**6+1)*(q**12+1)*(q**4+1)*(q**2+1)
assert s.cancel(fp_product-fp_formula.subs(q,r**2)) == 0
Ffactor = q**-16*sum(q**j for j in range(10))**2*(1+q**2)*(1+q**12)
assert s.cancel(q**11*(-q*fp_formula/((q-1)**2*f))-Ffactor) == 0
sourceF = [16,16,16,16,17,18,18,18,16,14,12,10,8,6,4,2,1]
assert s.cancel(Ffactor-symmetric_polynomial(sourceF)) == 0
assert Ffactor.subs(q,1) == 400
print("PASS: actual four-eigenvalue interpolation product, all normalization")
print("cancellations, and the full33-term source F coefficient list.")
