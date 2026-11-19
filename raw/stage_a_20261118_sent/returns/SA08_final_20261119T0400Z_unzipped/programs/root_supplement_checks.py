"""Supplemental exact checks: low stable Bockstein groups, elementary examples.

The stable models and their integral prime-torsion property are the hypotheses
from Cartan1955XI §6. The finite computation is not an independent proof of that
theorem; it redoes the manuscript's low-degree consequences within its range.
"""
import json,math
from itertools import product
out={}
for p,dx,dy in [(2,2,3),(3,4,5)]:
 # Through degree6 only x,y occur; for p3 y is exterior.
 basis={n:[] for n in range(7)}
 for a in range(4):
  for b in range(4 if p==2 else 2):
   n=a*dx+b*dy
   if n<=6:basis[n].append((a,b))
 images={n:set() for n in range(6)}
 for n in range(1,7):
  for a,b in basis[n]:
   if b and b%p:images[n-1].add((a+1,b-1))
 out[f'stable_p{p}']={'basis_through_degree6':basis,'Bockstein_images_by_degree':{n:sorted(v) for n,v in images.items()},'positive_integral_torsion_degrees_le5':[n for n,v in images.items() if n>0 and v]}
assert out['stable_p2']['positive_integral_torsion_degrees_le5']==[2,4]
assert out['stable_p3']['positive_integral_torsion_degrees_le5']==[4]
# UCT from integral groups Z/2 in degree2 and Z/2+Z/3 in degree4.
rows=[]
for m in [0,2,3,4,6,8,9,12]:
 # m=0 denotes the infinite cyclic group.
 q=lambda p:p if m==0 else math.gcd(m,p)
 tor=lambda p:1 if m==0 else math.gcd(m,p)
 rows.append({'G':'Z' if m==0 else f'Z/{m}','offset2_cyclic_orders':[q(2)],'offset3_cyclic_orders':[tor(2)],'offset4_cyclic_orders':[q(2),q(3)],'offset5_cyclic_orders':[tor(2),tor(3)]})
out['371_low_stable_UCT']={'rows':rows,'order1_means_zero_group':True,'range':'each offset i must satisfy i<n; all four simultaneously require n>=6','result':'matches quotient/torsion formulas; arbitrary-group result follows from the exact UCT sequences, not only these cyclic tests'}
out['345_circle']={'C1':'Z','C0':'Z','boundary_coefficient':1-1,'H0':'Z','H1':'Z','result':'one vertex, one nondegenerate edge'}
out['348_partial_product']={'boundary_times_cycle':'(da)z=d(az) with dz=0','result':'well-defined cohomology product under the stated half-dga axioms'}
out['371_unqualified_prime_torsion']={'G':'Z','space':'K(Z,2)=CP^infinity','homology':'H_(2r)=Z for every r>=0','result':'false outside the stable positive range; H_n=G is another immediate exception'}
out['371_arbitrary_group_cohomology']={'groups':['Z/2','Z/4'],'same_Hom_to_F2':True,'Hstar_BZ2':'F2[u1]','Hstar_BZ4':'Lambda_F2(u1) tensor F2[v2]','result':'different square of u1; only refutes an arbitrary-G interpretation, not a finite elementary-Fp-vector-space hypothesis'}
out['373_connectivity_bound_literal_smash']={'G':'Z','n':4,'p':4,'written_r':min(4+2*4-1,2*4+4-1),'tested_degree':10,'source_reduced_H10':'Z/2 direct_sum Z/2','target_H10':'Z/2','Kunneth_pairs':[[4,6],[6,4]],'source_order':4,'target_order':2,'result':'not isomorphic in degree10<11; refutes ordinary space-smash/homology interpretation only; simplicial-linear typing remains undecided'}
print(json.dumps(out,ensure_ascii=False,indent=2))
