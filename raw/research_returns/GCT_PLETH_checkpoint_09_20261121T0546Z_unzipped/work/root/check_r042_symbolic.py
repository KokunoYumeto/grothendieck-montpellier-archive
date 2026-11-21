from pathlib import Path
import runpy
import sympy as s
r=runpy.run_path('work/root/check_r041_symbolic.py')
a,m,C=r['a'],r['m'],r['C'];beta=C[:,1]
leadA=(a-1)/a;leadB=1-2/a+(m+1)/a**2;leadCp=-m/a+m*(m+1)/(2*a**2)
leadP1=leadA/a;leadP2=(leadB-leadP1)/a;leadP3=(leadCp+leadP1)/a
assert s.simplify(s.Matrix([leadP1,leadP2,leadP3])-beta)==s.zeros(3,1)
Q2=(beta[0]*C[1,:]-beta[1]*C[0,:]).subs(m,2)
Q3=(beta[0]*C[2,:]-beta[2]*C[0,:]).subs(m,2)
assert s.simplify(Q2-s.Matrix([[-(a-3)**2/a**3,0,-2*(a-3)/a**4]]))==s.zeros(1,3)
assert s.simplify(Q3-s.Matrix([[(a-3)/a**3,0,(a-3)*(a-2)/a**4]]))==s.zeros(1,3)
mom=s.Matrix([-s.Rational(1,216),0,-s.Rational(1,54)])
factor=a*(a-1)*(a-2)
assert s.factor((Q2*mom)[0]*factor-(a-3)*(a-2)*(a-1)*(a*a-3*a+8)/(216*a**3))==0
assert s.factor((Q3*mom)[0]*factor+(a-3)*(a-2)*(a-1)*(5*a-8)/(216*a**3))==0
assert s.simplify((beta[1]+beta[2]-beta[0]/2).subs(a,m+2))==0
Path('work/root/R042_SYMBOLIC_CUBIC_CHECK.txt').write_text('All three row-leading coefficients equal the second matrix column symbolically in a,m. Both cubic combination rows, their zero fourth-moment column, both normalized scalars and the finite-row Q3=-Q2 relation were verified as exact rational identities. PASS.\n')
print('R042 row-leading, extension relations and cubic scalars PASS')
