#!/usr/bin/env python3
"""Exact projective dual-arrangement count for the stated rational n=6 example."""
from pathlib import Path
from itertools import combinations
from functools import reduce
from math import gcd
import json,time
ROOT=Path(__file__).resolve().parents[1]
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def canonical(v):
 d=reduce(gcd,v);v=tuple(x//abs(d) for x in v);s=next(x for x in v if x);return tuple(x if s>0 else -x for x in v)
def main():
 tic=time.perf_counter();data=json.loads((ROOT/'audit/counts_n6_three_pair_input.json').read_text());a=data['base_vectors'];p=(0,0,1);pairs=list(combinations(range(6),2));walls=[cross(a[i],a[j]) for i,j in pairs]
 vertices={}
 for i,j in combinations(range(15),2):
  v=canonical(cross(walls[i],walls[j]));vertices.setdefault(v,set()).update([i,j])
 original=set(map(canonical,a));distribution={m:sum(len(ii)==m for ii in vertices.values()) for m in sorted({len(ii) for ii in vertices.values()})}
 E=sum(map(len,vertices.values()));V=len(vertices);F=1-V+E
 qp=[sum(w[j]*p[j] for j in range(3)) for w in walls];qp=[(x>0)-(x<0) for x in qp]
 determinants=[{'triple':t,'determinant':sum(a[t[0]][j]*cross(a[t[1]],a[t[2]])[j] for j in range(3))} for t in combinations(range(6),3)]
 assert all(d['determinant'] for d in determinants)
 result={'base_vectors':a,'base_triple_determinants':determinants,'p':p,'pair_order':pairs,'target_extension_signs':qp,'target_chirotope_signs_quotient':qp,'dual_vertices':V,'dual_edges':E,'dual_faces':F,'dual_vertex_multiplicities':distribution,'nonoriginal_multiple_vertices':[{'point':v,'walls':[pairs[k] for k in sorted(ii)]} for v,ii in vertices.items() if v not in original and len(ii)>2],'straight_position_count_s2':V-6+E+F,'straight_corner_count_s0':2*E,'straight_euler':1-6,'elapsed_seconds':time.perf_counter()-tic}
 (ROOT/'audit/counts_straight_dual.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
