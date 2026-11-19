#!/usr/bin/env python3
"""Finite exact support checks for the independently proved nodal-image lemmas.
The universal geometric arguments do not depend on extrapolating this check.
"""
from itertools import combinations,product
from pathlib import Path
import json,time
started=time.perf_counter()
def rank(cols):
 piv={}
 for c in cols:
  while c:
   k=c.bit_length()-1
   if k in piv:c^=piv[k]
   else:piv[k]=c;break
 return len(piv)
def tensor(a,b):
 return sum(((a>>i)&1)*((b>>j)&1)<<(3*i+j) for i in range(3) for j in range(3))
pts=[(a,b,tensor(a,b)) for a,b in product(range(1,8),repeat=2)]
checked=collinear=0
for tri in combinations(pts,3):
 r=rank([t[2] for t in tri]);samea=len({t[0] for t in tri})==1;sameb=len({t[1] for t in tri})==1
 expected=(samea and rank([t[1] for t in tri])==2) or(sameb and rank([t[0] for t in tri])==2)
 assert (r==2)==expected
 assert r in (2,3)
 checked+=1;collinear+=r==2
# Relation alpha*a+beta*c=0 on the two parallel derivatives; transverse b,d free.
relations=[]
for al,be in [(1,0),(0,1),(1,1)]:
 allowed=[];nonzero=[]
 for a,b,c,d in product(range(2),repeat=4):
  if (al*a+be*c)%2:continue
  allowed.append((a,b,c,d))
  if (a*d+b*c)%2:nonzero.append((a,b,c,d))
 assert len(allowed)==8 and len(nonzero)==2
 relations.append({'alpha':al,'beta':be,'allowed':len(allowed),'transverse':len(nonzero),'witness':nonzero[0]})
assert 31>18 and all(31%d for d in range(2,6)) and (2**5-1)==31
out={'status':'PASS','scope':'Supporting finite checks; universal proof retained in TeX',
 'distinct_rank_one_F2_3x3_matrices':len(pts),'triples_checked':checked,
 'collinear_triples':collinear,'all_triples_match_common_factor_criterion':True,
 'parallel_gradient_relations':relations,'GL8_prime31_exceeds_node_cover_degree18':True,
 'runtime_seconds':time.perf_counter()-started}
p=Path(__file__).resolve().parents[1]/'outputs'/'ordinary_product_isogeny_incidence_checks.json'
p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
