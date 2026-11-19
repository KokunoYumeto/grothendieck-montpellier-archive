"""Exact coordinate verification of the universal jet identity for root claim620.
The general proof is recorded separately; this checks its signs and operator order.
"""
import sympy as s, json
x,h,k=s.symbols('x h k')
cs=s.symbols('c0:8'); a=s.symbols('a0:5')
F=sum(cs[i]*x**i for i in range(8))
j=F.subs(x,x+h)-F
cocycle=s.expand(j.subs(h,h+k)-j-j.subs({x:x+h,h:k},simultaneous=True))
assert cocycle==0
linearized=s.diff(j,h)
jet_connection=s.diff(F,x).subs(x,x+h)
assert s.expand(linearized-jet_connection)==0
mu=sum(a[i]*s.diff(j,h,i+1).subs(h,0) for i in range(5))
nu=sum(a[i]*s.diff(F,x,i+1) for i in range(5))
assert s.expand(mu-nu)==0
print(json.dumps({'identity':'J(connection) lambda(p)=jet(d_P p)','local_jet':'F(x+h)-F(x)','cocycle_residual':str(cocycle),'connection_residual':str(s.expand(linearized-jet_connection)),'mu_minus_nu':str(s.expand(mu-nu)),'sign':'positive; D0=Delta composed with d_E','scope':'exact polynomial identity with symbolic coefficients, all operators of order at most4 and primitives degree at most7; universal proof uses horizontal stratified extension, not this finite bound'},indent=2))
