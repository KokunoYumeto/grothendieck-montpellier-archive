from pathlib import Path
from itertools import combinations_with_replacement
import sympy as s
import json
x=s.symbols('x1:5');U=s.symbols('A B C D E')
f=(x[0]*x[2]-x[0]*x[1],x[0]*x[3]-x[0]*x[1],x[1]*x[2]-x[0]*x[1],x[1]*x[3]-x[0]*x[1],x[2]*x[3]-x[0]*x[1])
def mons(d):
 return [tuple(v.count(i) for i in range(4)) for v in combinations_with_replacement(range(4),d)]
def mon(e):return s.prod(xi**ei for xi,ei in zip(x,e))
q4=mons(4);q3=mons(3);qq=list(combinations_with_replacement(range(5),2))
ix={e:i for i,e in enumerate(q4)}
M=s.zeros(4*len(q4),4*len(qq)+len(q3));B=s.zeros(M.rows,5)
for i in range(4):
 for j,(a,b) in enumerate(qq):
  for e,v in s.Poly(f[a]*f[b],*x).terms():M[i*len(q4)+ix[e],i*len(qq)+j]=v
 for j,e3 in enumerate(q3):
  e=list(e3);e[i]+=1;M[i*len(q4)+ix[tuple(e)],4*len(qq)+j]=1
 for j,ff in enumerate(f):
  for e,v in s.Poly(ff*x[i]**2,*x).terms():B[i*len(q4)+ix[e],j]=v
sol,par=M.gauss_jordan_solve(B)
assert par.rows==0 and M*sol==B
Phi=s.Matrix(4,5,lambda i,j:s.expand(sum(sol[i*len(qq)+z,j]*U[a]*U[b] for z,(a,b) in enumerate(qq))))
h=[s.expand(sum(sol[4*len(qq)+z,j]*mon(e) for z,e in enumerate(q3))) for j in range(5)]
Mat=Phi.col_join(s.Matrix([[-v for v in U]]))
F=U[0]*U[3]*(U[4]-U[1]-U[2])-U[1]*U[2]*(U[4]-U[0]-U[3])
det=s.factor(Mat.det(method='domain-ge'))
adj=Mat.adjugate(method='domain-ge')
N=adj.applyfunc(lambda v:s.cancel(v/F**2))
assert all(s.denom(v)==1 for v in N)
assert all(s.expand(v)==0 for v in Mat*N-81*F*s.eye(5))
print('Phi=',Phi)
print('h=',h)
print('det=',det)
print('ratio=',s.cancel(det/F**3))
assert all(s.expand(f[j]*x[i]**2-Phi[i,j].subs(dict(zip(U,f)),simultaneous=True)-x[i]*h[j])==0 for i in range(4) for j in range(5))
Path('work/root/FIVE_POINT_Q_RELATIONS.json').write_text(json.dumps({'variables':[str(v) for v in U],'phi':[[str(v) for v in Phi.row(i)] for i in range(4)],'line_corrections':[str(v) for v in h],'relation_matrix':[[str(v) for v in Mat.row(i)] for i in range(5)],'cubic':str(F),'determinant':str(det),'determinant_ratio_to_cubic_cube':str(s.cancel(det/F**3)),'matrix_factorization_second_matrix':[[str(v) for v in N.row(i)] for i in range(5)],'matrix_factorization_identity':'P*N=81F*I PASS','all_twenty_polynomial_identities':'PASS','linear_system_shape':[M.rows,M.cols],'unique_solution':True},indent=2))
