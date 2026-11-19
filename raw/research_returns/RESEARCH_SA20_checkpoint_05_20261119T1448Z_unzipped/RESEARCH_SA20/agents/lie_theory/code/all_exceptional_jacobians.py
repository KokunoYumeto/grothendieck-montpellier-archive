#!/usr/bin/env python3
from pathlib import Path
import re,json
from datetime import datetime,timezone
from time import perf_counter
import sympy as sp
from exceptional_jacobian import RootLie,FoldLie,Minuscule,OUT
START=perf_counter()
rows={}
for rec in json.loads((Path(__file__).resolve().parent/'exceptional_orbits.json').read_text()):
 rows.setdefault(rec['type'],[]).append((rec['orbit'],rec['diagram'],rec['orbit_dimension']))
print('Started UTC',datetime.now(timezone.utc).isoformat(),flush=True)
allreports=[]
for kind in ['G2','F4','E6','E7','E8']:
 L=FoldLie(kind) if kind in ['G2','F4'] else RootLie(kind)
 rep=Minuscule(L) if kind=='E6' else None
 print(kind,'dimension',L.n,'root count',L.nr,'Jacobi triples',L.jacobi(),flush=True)
 exps={'G2':[1,5],'F4':[1,5,7,11],'E6':[1,4,5,7,8,11],'E8':[1,7,11,13,17,19,23,29],'E7':[1,5,7,9,11,13,17]}[kind]
 for name,diagram,dim in rows[kind]:
  if not any(diagram):
   report={'type':kind,'orbit':name,'diagram':diagram,'orbit_dimension':0,'nonzero_exponents':[]}
  else:
   e,h,f,deg,attempt=L.triple(diagram)
   # For an exact sl2 triple, dim centralizer = dim g(0)+dim g(1).
   centralizer=deg.count(0)+deg.count(1)
   assert L.n-centralizer==dim,(kind,name,L.n-centralizer,dim)
   vals=rep.derivatives(L,e,deg,exps) if rep else L.powers_and_traces(e,deg,exps)
   report={'type':kind,'orbit':name,'diagram':diagram,'orbit_dimension':dim,'e':L.record_element(e),'h':L.record_element(h),'f':L.record_element(f),
      'max_h_weight':max(deg),'triple_search_attempt':attempt,
      'nonzero_exponents':[m for m in exps if vals[m]],
      'derivatives':{m:[{'root':L.roots[i],'value':str(v)} for i,v in values] for m,values in vals.items()}}
  allreports.append(report)
  print(kind,name,''.join(map(str,diagram)),dim,report['nonzero_exponents'],flush=True)
  (OUT/'all_exceptional_jacobians.json').write_text(json.dumps({'results':allreports,'elapsed_seconds':perf_counter()-START},indent=2))
 print('Completed',kind,len(rows[kind]),'orbits',flush=True)
print('Elapsed seconds',perf_counter()-START,flush=True)
