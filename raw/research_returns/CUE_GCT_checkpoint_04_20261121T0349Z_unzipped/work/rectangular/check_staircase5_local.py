"""Exact symbolic check of the local five-row motif's second-order identities."""
from itertools import permutations
from pathlib import Path
import json
import sympy as sp
from staircase5_certificate import top_forms,x,y,z,w,q

e=sp.symbols('epsilon')
L=lambda c:x-c*y
V=lambda c:z-c*w
ell=lambda i:x-q**i*y
v=lambda i:z-q**i*w
B=sp.Matrix([
 [ell(0),v(0),e*L(2),e*L(3),e*V(3),0],
 [0,ell(1),v(1),e*L(4),e*L(3),e*V(2)],
 [0,0,ell(2),v(2),e*V(6),0],
 [0,e*V(5),0,ell(3),v(3),e*V(4)],
 [0,e*L(2),e*V(7),e*L(5),ell(4),v(4)],
])
R,S=top_forms([2,3,4,5,2,3,4,5,6,7])
checks=[]
for side,A,forms in [('row',B[1:5,1:6],R),('column',B[0:5,1:5].T,S)]:
    T=A.copy()
    for i in range(4):
      for j in range(5):
        if j>i+1:T[i,j]*=(-1)**(j-i-1)
        elif j<i:T[i,j]*=(-1)**(i-j)
    P=[];D=[];E=[]
    for missing in range(5):
        cols=[j for j in range(5) if j!=missing]
        pp=0;dd=0
        for perm in permutations(range(4)):
            inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
            pp+=sp.prod(A[i,cols[perm[i]]] for i in range(4))
            dd+=(-1)**inv*sp.prod(T[i,cols[perm[i]]] for i in range(4))
        diff=sp.Poly(sp.expand(pp-dd),e)
        assert diff.nth(0)==0 and diff.nth(1)==0
        P.append(sp.expand(pp));D.append(sp.expand(dd));E.append(diff.nth(2))
    assert E[0]==E[4]==0
    for i in range(4):
        relation=sp.expand(sum((-1)**(i+j)*T[i,j]*P[j] for j in range(5)))
        determinant_relation=sp.expand(sum((-1)**(i+j)*T[i,j]*D[j] for j in range(5)))
        assert determinant_relation==0
        ep=sp.Poly(relation,e)
        assert ep.nth(0)==ep.nth(1)==0
        leading=ep.nth(2)
        assert sp.expand(leading-(A[i,i]*E[i]-A[i,i+1]*E[i+1]))==0
        poly=sp.Poly(leading,x,y,z,w)
        grade=max(zz+ww for (xx,yy,zz,ww),c in poly.terms())
        top=sum(c*x**xx*y**yy*z**zz*w**ww for (xx,yy,zz,ww),c in poly.terms() if zz+ww==grade)
        assert sp.expand(top-2*forms[i])==0,(side,i)
        checks.append({'side':side,'relation':i,'highest_zw_degree':grade,
                       'epsilon0_and1_zero':True,'top_equals_twice_displayed_form':True})
result={'all_passed':True,'minor_differences_checked':10,'signed_determinant_relations_checked':8,
        'second_order_and_highest_bidegree_relations':checks,
        'method':'explicit24-permutation expansion; no growing-size Jacobian extrapolation'}
Path(__file__).with_name('staircase5_local_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_passed':True,'minor_differences':10,'cofactor_relations':8}))
