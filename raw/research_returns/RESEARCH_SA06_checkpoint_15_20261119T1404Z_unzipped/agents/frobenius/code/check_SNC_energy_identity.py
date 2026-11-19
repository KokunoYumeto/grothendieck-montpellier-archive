"""Exact local expansion and product-cycle degree-map check; no geometric extrapolation."""
import datetime,json,time
from pathlib import Path
import sympy as s
start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.perf_counter()
a,b,c,x,y,z,A,B=s.symbols('a b c x y z A B')
local=s.expand(-a*b*c*(x*x+y*y+z*z)-2*a*b*c*(x*y+y*z+z*x)+a*b*c*(x+y+z)**2)
edge=s.expand(a*b*b*x*x*A+b*a*a*x*x*B-a*b*x*x*(b*A+a*B))
old=s.Matrix([[1,0,-1],[-1,1,0],[0,-1,1]])
new=old.col_join(s.Matrix([[1,0,0]]))
assert local==0 and edge==0 and old.rank()==2 and new.rank()==3
out={'started_utc':start,'seconds':time.perf_counter()-t,'local_triple_expansion':str(local),'weighted_edge_expansion':str(edge),'cycle_product_degree_matrix':[[int(v) for v in row] for row in old.tolist()],'old_rank':old.rank(),'one_boundary_blowup_matrix':[[int(v) for v in row] for row in new.tolist()],'new_rank':new.rank(),'passed':True,'scope':'Exact weighted polynomial identity and elementary degree-map illustration only. The all-dimensional statement uses the written intersection proof; no Chow or K-theory descent is numerically inferred.'}
p=Path(__file__).resolve().parents[1]/'output/check_SNC_energy_identity.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
