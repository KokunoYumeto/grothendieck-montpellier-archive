#!/usr/bin/env python3
"""Exact finite range analysis of the fixed62556 sparse template.

The reusable arithmetic definitions are compiled without executing the
discovery driver's top level, preserving all discovery output bytes.
"""
from pathlib import Path
import ast,itertools,json,time
import sympy as sp
started=time.perf_counter();w=Path(__file__).resolve().parents[1]
source=w/'code/ss_rectangular_sparse_templates.py'
tree=ast.parse(source.read_text());defs=ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[])
namespace={'itertools':itertools};exec(compile(defs,str(source),'exec'),namespace)
elementary=namespace['elementary'];rank=namespace['rank'];apply=namespace['apply']
pattern=62556;rows=[];polynomials=[]
for m in range(3,97):
 system=elementary(m);C=[0]*(6*m)
 for j in range(18):
  if pattern>>j&1:C=[a^b for a,b in zip(C,system['matrices'][j])]
 C2=[apply(C,v) for v in C]
 rec={'m':m,'degrees':[2*m,3],'rank_C':rank(C),'rank_C2':rank(C2),'target':6*m-2}
 rec['sharp']=rec['rank_C']==rec['rank_C2']==rec['target'];rows.append(rec)
 if m in (3,6,12):
  t=sp.Symbol('T');matrix=sp.Matrix(6*m,6*m,lambda i,j:(C[j]>>i)&1)
  tick=time.perf_counter();cp=sp.Poly(matrix.charpoly(t).as_expr(),t,modulus=2)
  factors=sp.factor_list(cp.as_expr(),modulus=2)
  polynomials.append({'m':m,'characteristic_polynomial':str(cp.as_expr()),
   'factors':[(str(f),int(e)) for f,e in factors[1]],'seconds':time.perf_counter()-tick})
result={'status':'FINITE_RANGE_COMPLETED','scope':'No uniform theorem inferred',
 'pattern':pattern,'nonzero_template_positions':[divmod(j,3) for j in range(18) if pattern>>j&1],
 'range_half_first_degree':[3,96],'rows':rows,'nonsharp':[r for r in rows if not r['sharp']],
 'small_characteristic_polynomials':polynomials,'elapsed_seconds':time.perf_counter()-started}
(w/'outputs/ss_sparse_template_range.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('rows',)},indent=2))
