"""HD-N24 exact chain contraction and integer bounds.
GPT-6 Astra Pro /root/imprimitive, 21 November2026; inherited effort.
The certificate verifies actual polynomial chain maps, not the Ext-sheaf
identifications or their global gluing; those are proved in the TeX.
No previous certificate or stored output is imported.
"""
from pathlib import Path
from math import comb
import json
import sympy as sp

x=sp.symbols('x1:4')
y=sp.symbols('y1:4')

def koszul(z):
    a,b,c=z
    return (sp.Matrix([[a,b,c]]),
            sp.Matrix([[-b,-c,0],[a,0,-c],[0,a,b]]),
            sp.Matrix([[c],[-b],[a]]))

x1,x2,x3=koszul(x)
y1,y2,y3=koszul(y)
assert x1*x2==sp.zeros(1,3) and x2*x3==sp.zeros(3,1)
assert y1*y2==sp.zeros(1,3) and y2*y3==sp.zeros(3,1)

# Larger cone F: ranks 2,6,7,2 in degrees -2,-1,0,1.
Fdim={-2:2,-1:6,0:7,1:2}
Fd={
 -2:-sp.diag(x3,y3),
 -1:sp.zeros(1,6).col_join(-sp.diag(x2,y2)),
 0:sp.Matrix([[1]+[-v for v in x]+[0]*3,
              [1]+[0]*3+[-v for v in y]])}
# Smaller actual contraction M: ranks 2,6,6,1.
Mdim={-2:2,-1:6,0:6,1:1}
Md={-2:-sp.diag(x3,y3),-1:-sp.diag(x2,y2),
    0:x1.row_join(-y1)}
for d in (-2,-1):
    assert Fd[d+1]*Fd[d]==sp.zeros(Fdim[d+2],Fdim[d])
    assert Md[d+1]*Md[d]==sp.zeros(Mdim[d+2],Mdim[d])

P={-2:sp.eye(2),-1:sp.eye(6),
   0:sp.zeros(6,1).row_join(sp.eye(6)),1:sp.Matrix([[-1,1]])}
I={-2:sp.eye(2),-1:sp.eye(6),
   0:x1.row_join(sp.zeros(1,3)).col_join(sp.eye(6)),
   1:sp.Matrix([[0],[1]])}
H={1:sp.Matrix([[1,0]]+[[0,0]]*6)}
for d in (-2,-1,0,1):
    assert P[d]*I[d]==sp.eye(Mdim[d])
    if d<1:
        assert P[d+1]*Fd[d]==Md[d]*P[d]
        assert Fd[d]*I[d]==I[d+1]*Md[d]
    dh=sp.zeros(Fdim[d],Fdim[d])
    if d in H:
        dh+=Fd[d-1]*H[d]
    if d+1 in H:
        dh+=H[d+1]*Fd[d]
    assert sp.eye(Fdim[d])-I[d]*P[d]==dh

N=9408
Gbound=144
quotient_components=(N+Gbound-1)//Gbound
trace_target=sum(comb(6,p)*comb(6,p+2) for p in range(5))
assert quotient_components==66 and trace_target==495
ordinary_ext_lower=9*N-20
ordinary_kernel_lower=ordinary_ext_lower-trace_target
invariant_ext_lower=9*quotient_components-20
invariant_kernel_lower=invariant_ext_lower-trace_target
assert ordinary_ext_lower==84652 and ordinary_kernel_lower==84157
assert invariant_ext_lower==574 and invariant_kernel_lower==79
# Every possible actual subgroup order gives at least the uniform bound.
rows=[]
for order in range(1,Gbound+1):
    comps=(N+order-1)//order
    lower=9*comps-20-trace_target
    assert lower>=79
    rows.append([order,comps,lower])

out={'statement':'HD-N24','status':'PASS',
 'ring':'Z[x1,x2,x3,y1,y2,y3]',
 'cone_free_ranks':[Fdim[d] for d in (-2,-1,0,1)],
 'contracted_free_ranks':[Mdim[d] for d in (-2,-1,0,1)],
 'degrees':[-2,-1,0,1],
 'Koszul_compositions':True,'projection_and_inclusion_chain_maps':True,
 'projection_inclusion_identity':True,'explicit_contraction_homotopy':True,
 'component_count':N,'uniform_stabilizer_bound':Gbound,
 'minimum_quotient_components':quotient_components,
 'trace_target_dimension':trace_target,
 'ordinary_Ext2_lower':ordinary_ext_lower,
 'ordinary_trace_kernel_lower':ordinary_kernel_lower,
 'uniform_invariant_Ext2_lower':invariant_ext_lower,
 'uniform_invariant_trace_kernel_lower':invariant_kernel_lower,
 'all_order_integer_bounds':rows,
 'scope':'Exact polynomial chain maps and integer inequalities. Ext identifications, canonical Hartogs gluing, spectral-sequence survival, and every coherent-action statement are proved in the accompanying complete text.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='all_order_integer_bounds'},indent=2))
