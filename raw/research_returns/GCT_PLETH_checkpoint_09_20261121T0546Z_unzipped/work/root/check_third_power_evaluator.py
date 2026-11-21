from pathlib import Path
from math import comb
import json
from third_power_fixed_twist_positive import coefficient,polytopes,witnesses,LABELS
from fixed_twist_arrangement import coefficients
cases=0;matrix_checks=0;exhaustive=0
for c in range(3):
 for b in list(range(9))+[68,130]:
  shift=max(0,15-3*c-2*b)
  for offset in (0,1,59,60,125):
   x=shift+offset
   values=coefficients(x,b,3,c)
   for d in (0,1):
    actual=values[::-1] if (d+b+x+c)%2 else values
    for label,expected in zip(LABELS,actual):
     got=coefficient(x,b,c,d,label)
     assert got==expected,(x,b,c,d,label,got,expected)
     cases+=1
     if offset not in (0,60) or b not in (0,8):continue
     poly=polytopes(x,b,c,d,label)
     index={(tuple(p['residues']),tuple(p['order'])):p for p in poly}
     limit=got+1 if got<=200 else 17
     points=list(witnesses(x,b,c,d,label,limit))
     assert len(points)==min(got,limit)
     assert len({(tuple(p['residues']),tuple(p['order']),tuple(p['coordinates'])) for p in points})==len(points)
     if got<=200:exhaustive+=1
     for point in points:
      p=index[(tuple(point['residues']),tuple(point['order']))];v=point['coordinates']
      assert len(v)==len(p['variables'])
      assert all(sum(a*b for a,b in zip(row,v))==rhs for row,rhs in p['equalities'])
      assert all(sum(a*b for a,b in zip(row,v))<=rhs for row,rhs in p['inequalities'])
      matrix_checks+=1
r={'statement':'G-032','coefficient_comparisons':cases,'witness_matrix_checks':matrix_checks,'exhaustive_small_witness_cases':exhaustive,'outcome':'PASS'}
Path(__file__).with_name('THIRD_POWER_EVALUATOR_CHECK.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
