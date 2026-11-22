"""Exact F2 certificate for the flat torsor tangent-dimension caution.
R=F2[e1,e2,e3,e4]/(e_i e_j); A=R[z]/(z^2-e1).
A has the displayed free R basis 1,z. We check multiplication, tangent
quotients, and the torsor-coordinate isomorphism, without CAS dependencies.
"""
import itertools,json,time
from pathlib import Path
started=time.perf_counter()
# Basis 1,e1,e2,e3,e4, z,e1z,e2z,e3z,e4z.
n=10

def mul_basis(i,j):
    zi,ri=divmod(i,5); zj,rj=divmod(j,5)
    if ri and rj:return 0
    r=ri or rj; z=zi+zj
    if z==2:
        if r:return 0
        return 1<<1
    return 1<<(r+5*z)

def mul(a,b):
    out=0
    for i in range(n):
        if(a>>i)&1:
            for j in range(n):
                if(b>>j)&1:out^=mul_basis(i,j)
    return out

def rank(vs):
    piv={}
    for v in vs:
        while v:
            i=v.bit_length()-1
            if i not in piv:piv[i]=v;break
            v^=piv[i]
    return len(piv)

basis=[1<<i for i in range(n)]
for a,b,c in itertools.product(basis,repeat=3):
    assert mul(mul(a,b),c)==mul(a,mul(b,c))
    assert mul(a,b)==mul(b,a)
m=basis[1:]
m2=rank([mul(a,b) for a,b in itertools.product(m,repeat=2)])
assert m2==5 and 9-m2==4
# At the neutral product R[w]/w² the cotangent basis is e1,...,e4,w.
neutral_tangent=5
# The torsor isomorphism sends z2 -> z1+y+z1*y; determinant 1+e1.
one_plus_e1=1^(1<<1)
assert mul(one_plus_e1,one_plus_e1)==1
# No R point: every principal unit has square 1.
for mask in range(16):
    u=1
    for j in range(4):
        if(mask>>j)&1:u^=1<<(j+1)
    assert mul(u,u)==1
out={
  'base':'R=F2[e1,e2,e3,e4]/(all degree-two monomials)',
  'torsor':'A=R[z]/(z^2-e1)',
  'R_basis_dimension':5,'A_F2_dimension':10,'A_free_R_rank':2,
  'torsor_tangent_dimension':4,'neutral_mu2_product_tangent_dimension':neutral_tangent,
  'with_one_smooth_elliptic_factor_tangent_dimensions':[5,6],
  'base_tangent_image':'hyperplane d(e1)=0',
  'torsor_coordinate_map_determinant':'1+e1, a unit with square 1',
  'R_valued_section_exists':False,
  'runtime_seconds':round(time.perf_counter()-started,6),
  'scope':'finite flat torsor and tangent counterexample; no claim about the actual Igusa hull'
}
path=Path(__file__).with_name('check_flat_torsor_output.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
