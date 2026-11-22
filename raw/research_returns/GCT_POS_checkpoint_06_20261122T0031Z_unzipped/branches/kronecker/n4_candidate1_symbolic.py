import sympy as s
x0,x1,x2,x3=s.symbols('x0 x1 x2 x3');x=(x0,x1,x2,x3)
q=[x0*x0+x2*x2,2*x0*x3,2*x1*x2+x3*x3,2*x0*x2+x1*x1]
t0,t1,t2,t3,a1,a2=s.symbols('t0 t1 t2 t3 a1 a2',nonzero=True)
# Preserving special rank-two point q1 gives x0'=t0*x0,x3'=t3*x3.
# preserving modulo x0 rank-one locus gives x1',x2' scalar coordinate permutation +x0.
for swap in (False,True):
 xx=[t0*x0,t1*(x2 if swap else x1)+a1*x0,t2*(x1 if swap else x2)+a2*x0,t3*x3]
 eq=[]
 for z in q:
  f=s.Poly(s.expand(z.subs(dict(zip(x,xx)),simultaneous=True)),x)
  # Q coefficient constraints: x0^2=x2^2, x0*x3 free; x1*x2=2*x3^2; x0*x2=2*x1^2
  c=lambda ex:f.coeff_monomial(ex)
  eq += [c(x0*x0)-c(x2*x2),c(x1*x2)-2*c(x3*x3),c(x0*x2)-2*c(x1*x1),c(x0*x1),c(x1*x3),c(x2*x3)]
 eq=list({s.factor(z) for z in eq if z!=0})
 print('SWAP',swap,eq)
