from pathlib import Path
import sympy as s
v=s.symbols("a b c d e f g h i j")
a,b,c,d,e,f,g,h,i,j=v
Y=s.Matrix([[a,b,e,f],[c,d,f,g],[h,i,-a,-c],[i,j,-b,-d]])
N=s.Matrix([[0,0,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])
pt={x:0 for x in v};pt.update({e:1,g:1})
co=Y.charpoly().all_coeffs()
J=s.Matrix([co[2],co[4]]).jacobian(v).subs(pt)
C=s.Matrix(list(Y*N-N*Y)).jacobian(v)
print("N squared",N*N)
print("centralizer dimension",10-C.rank())
print("quotient Jacobian",J,"rank",J.rank())
