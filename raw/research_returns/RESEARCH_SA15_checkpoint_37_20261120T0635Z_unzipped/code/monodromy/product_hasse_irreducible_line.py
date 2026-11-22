#!/usr/bin/env python3
"""Bounded irreducible-line test for a whole Hasse polynomial.
If successful, a full-degree irreducible restriction proves base-field
irreducibility; a rational smooth Hasse point then proves geometric
irreducibility. Failure of this bounded search proves nothing.
"""
import json,random,time,sys
from pathlib import Path
started=time.perf_counter();root=Path(__file__).resolve().parents[1]
src=Path(__file__).with_name('product_higher_degree_certificates.py')
ctx={'__file__':str(src)}
exec(compile(src.read_text().split("print('degree',d")[0],str(src),'exec'),ctx)
d,n=ctx['d'],ctx['n'];rank,apply,matrix=ctx['rank'],ctx['apply'],ctx['matrix']
charpoly,irreducible=ctx['charpoly'],ctx['irreducible']
inverse_cols=ctx['ns']['inverse_cols']
rng=random.Random(202611190740+d)
out={'degree':d,'W_dimension':n,'seed':202611190740+d,'maximum_pairs':5000,
 'scope':'Exact certificate only if success=True; bounded failure is inconclusive'}
dest=root/'outputs'/('product_degree'+str(d)+'_hasse_irreducible_line.json')
for attempt in range(1,10001):
 s=rng.getrandbits(n);C=matrix(s)
 if rank(C)==n-1 and rank([apply(C,v) for v in C])==n-1:
  out['rational_smooth_hasse_point']={'section_bits':s,'columns':C,
     'rank_M':n-1,'rank_M_squared':n-1,'attempt':attempt}
  print('rational smooth Hasse point',attempt,flush=True);break
else:raise AssertionError('No smooth point in bounded search')
tested=0
for attempt in range(1,5001):
 a=rng.getrandbits(n);b=rng.getrandbits(n);A=matrix(a);B=matrix(b)
 if rank(B)!=n:continue
 tested+=1;Bi=inverse_cols(B);BA=[apply(Bi,c) for c in A]
 h=charpoly(BA)
 if irreducible(h):
  assert h.bit_length()-1==n
  out['success']=True
  out['line']={'section_a_bits':a,'section_b_bits':b,'A_columns':A,'B_columns':B,
      'determinant_bits':h,'attempt':attempt,'invertible_B_pairs_tested':tested,
      'full_degree':n,'irreducible_over_F2':True}
  print('irreducible full-degree line found',attempt,'tested',tested,flush=True);break
 if tested%100==0:print('tested',tested,'pairs',attempt,flush=True)
else:out['success']=False;out['pairs_tried']=5000;out['invertible_B_pairs_tested']=tested
out['runtime_seconds']=time.perf_counter()-started
dest.write_text(json.dumps(out,indent=2)+'\n')
print('saved',dest,'success',out['success'],flush=True)
