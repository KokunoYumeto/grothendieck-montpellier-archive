"""Rationalize numerical discoveries and certify all 26 complete minimum sets."""
from pathlib import Path
from fractions import Fraction as F
from math import lcm
import json,sympy as sp
src=Path('work/k12_survivor_certificate.py').read_text().split('INTEGER_GRAM =')[0];ns={};exec(src,ns)
inputs=json.loads(Path('work/k12_ternary_glue_lp_complete.json').read_text());out=[]
tri=[(i,j)for i in range(10)for j in range(i,10)]
for rec in inputs:
 assert rec['status']=='complete_float_candidate'
 V=rec['V'];E=sp.Matrix([[v[i]*v[j]*(1 if i==j else 2)for i,j in tri]for v in V])
 piv=E.rref()[1];free=[j for j in range(55)if j not in piv];inverse=E[:,piv].inv()
 x=[None]*55
 for j in free:
  a,b=tri[j];x[j]=sp.Rational(round(rec['gram'][a][b]*3600),3600)
 sol=inverse*(sp.ones(13,1)-E[:,free]*sp.Matrix([x[j]for j in free]))
 for j,t in zip(piv,sol):x[j]=t
 Q=sp.zeros(10)
 for (i,j),t in zip(tri,x):Q[i,j]=Q[j,i]=t
 A=sp.Matrix(rec['ambient_basis_numerator'])/3
 assert abs(A.det())==sp.Rational(1,3)
 W=A.inv()*sp.Matrix(V).T;assert all(z.q==1 for z in W)
 W=[list(map(int,W[:,j]))for j in range(13)]
 P=A.T*Q*A;d=lcm(*(int(t.q)for t in P));H=[[int(P[i,j]*d)for j in range(10)]for i in range(10)]
 q=[[F(t,d)for t in row]for row in H]
 sv,nodes,diag=ns['exact_short_vectors'](q,F(1));target={tuple(v)for v in W}|{tuple(-z for z in v)for v in W}
 assert set(sv)==target and all(ns['gram_value'](q,v)==1 for v in W)
 assert ns['matrix_rank']([[v[i]*v[j]for i in range(10)for j in range(i,10)]for v in W])==13
 item={'record':rec['record'],'orbit':rec['orbit'],'state':rec['state'],'gale_columns':rec['B'],'Lmin_vectors':V,'colors':rec['colors'],'ambient_basis_numerator':rec['ambient_basis_numerator'],'gram_denominator':d,'integer_gram':H,'minimum_vectors':W,'enumeration_nodes':nodes,'ldl_diagonal':[str(t)for t in diag]}
 out.append(item);print(rec['record'],rec['orbit'],d,nodes,flush=True)
Path('work/k12_ternary_glue_exact_forms.json').write_text(json.dumps(out,indent=2)+'\n')
