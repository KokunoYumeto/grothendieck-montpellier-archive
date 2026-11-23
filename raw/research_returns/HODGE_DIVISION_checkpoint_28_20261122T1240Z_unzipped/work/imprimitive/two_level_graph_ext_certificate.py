"""HD-N25 exact graded-index and dimension supplements.
GPT-6 Astra Pro /root/imprimitive; 21 November2026; inherited effort.
This checks bookkeeping only. Cross-Koszul concentration, triangle
exactness and coherent point invariance are universal proofs in the TeX.
No formality or degeneration of an endomorphism spectral sequence is used.
"""
from math import comb
from pathlib import Path
import json

# Exact exterior Kunneth coefficients for one abelian-threefold support.
left=[comb(3,k) for k in range(4)]
right=left[:]
self_ext=[sum(left[a]*right[k-a] for a in range(4)
              if 0<=k-a<4) for k in range(7)]
assert self_ext==[1,6,15,20,15,6,1]

# Cross Ext is concentrated in ordinary degree3. Record all actual
# neighboring cross degrees in the canonical short exact sequence.
neighbor_degrees={
 'restriction_Hom(E,Q4)_left':4,
 'restriction_Hom(E,Q4)_right':5,
 'Hom(E,P1)_left':-2,
 'Hom(E,P1)_right':-1,
 'Hom(E,P2)_left':-1,
 'Hom(E,P2)_right':0,
 'left_boundary_middle_composite':4,
 'right_boundary_middle_composite':5}
assert all(k!=3 for k in neighbor_degrees.values())
# For every negative k, k-2 is negative and k+2<=1, hence neither is3.
# The following finite range is explicitly only an index cross-check.
for k in range(-20,0):
    assert k-2<0 and k+2<=1 and k+2!=3

components=9408
stabilizer_bound=144
trace_target=sum(comb(6,p)*comb(6,p+2) for p in range(5))
assert trace_target==495
ordinary_ext2=15*components
ordinary_kernel=ordinary_ext2-trace_target
rows=[]
for order in range(1,stabilizer_bound+1):
    orbits=(components+order-1)//order
    ext=15*orbits
    kernel=ext-trace_target
    assert orbits>=66 and ext>=990 and kernel>=495
    rows.append([order,orbits,ext,kernel])
assert ordinary_ext2==141120 and ordinary_kernel==140625
assert min(r[1] for r in rows)==66
assert min(r[2] for r in rows)==990
assert min(r[3] for r in rows)==495
out={
 'statement':'HD-N25','status':'PASS',
 'one_support_self_Ext_dimensions':self_ext,
 'actual_triangle_neighbor_cross_degrees':neighbor_degrees,
 'ordinary_Ext2':ordinary_ext2,
 'ordinary_trace_kernel_lower':ordinary_kernel,
 'trace_target_dimension':trace_target,
 'minimum_component_orbits':66,
 'invariant_Ext2_lower':990,
 'invariant_trace_kernel_lower':495,
 'all_point_group_order_bounds':rows,
 'scope':'Exact graded indices, exterior convolution and integer bounds only. Actual cones, all-delta exactness, complement-isogeny actions, arbitrary coherent linearizations and isogeny-label orbit maps are proved universally in the text.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='all_point_group_order_bounds'},indent=2))
