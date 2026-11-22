import sympy as s,itertools,json
x0,x1,x2,x3=s.symbols('x0 x1 x2 x3');u=s.symbols('u',nonzero=True);v=s.symbols('v',nonzero=True)
f=x0*x0*x1*x1-x0*x0*x3*x3-x0*x1*x2*x2-x1**3*x3+x1*x3**3
roots=[s.Integer(1),s.Integer(-1),s.I,-s.I]
V=s.Matrix([[1,-1],[1,1]])
for a,b in itertools.product(roots,repeat=2):
 if a*a != -b*b:continue
 W=s.Matrix([[a*a/a,b*b*s.I/b],[1/a,s.I/b]])
 L=s.simplify(W*V.inv())
 xx=[x0,L[0,0]*x1+L[0,1]*x3,u*x2,L[1,0]*x1+L[1,1]*x3]
 ff=s.expand(f.subs(dict(zip([x0,x1,x2,x3],xx)),simultaneous=True))
 pp=s.Poly(ff-v*f,x0,x1,x2,x3)
 eq=list({s.factor(c) for c in pp.coeffs()})
 gg=s.groebner(eq,v,u)
 print('a,b',a,b,'L',L.tolist(),'constraints',list(gg),flush=True)
