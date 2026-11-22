"""Exact four-case coefficient optimization for NN-G028.
The proof supplies the global mass bound H(4)<=5,including arbitrary degrees.
No source search implementation is imported; every remaining inequality is explicit.
"""
from pathlib import Path
from fractions import Fraction
import json
rows=[]
for j0 in (2,4,6):
 for j1 in (3,5):
  j2=5
  if 8*j0+16*j1+12*j2<144:continue
  n=j0+2*j1+2*j2
  cchoices=[]
  for y in (3,5):
   cap=min((65-j1*y)//5,(89-(j0+5)*y)//j1,(94-2*j1*y)//j0)
   x=cap-cap%2
   if x>=2:cchoices.append({'x':x,'y':y,'C_mass':x+2*y})
  vchoices=[]
  for y in range(3,(j1+15)//2+1,2):
   cap=min(3*j0+4*j1-2*y,2*j0+(7*j1+13)//2-2*y,j0//2+2*j1+12-y)
   x=cap-cap%2
   if x>=6:vchoices.append({'x':x,'y':y,'z':2,'V2_mass':x+2*y+4})
  assert cchoices and vchoices
  cm=max(v['C_mass'] for v in cchoices);vm=max(v['V2_mass'] for v in vchoices)
  A1=480-n*cm;A2=16*n-10*vm
  bottom=40*n+20*(120+4*n)+2400+20*(16+3*cm+vm)
  cell=520+14*(A1+A2);total=bottom+cell
  rows.append({'J_q':[j0,j1,5],'J_mass':n,'C1_endpoint_choices':cchoices,'V2_endpoint_choices':vchoices,
               'max_C1_mass':cm,'max_V2_mass':vm,'A1_mass':A1,'A2_mass':A2,
               'bottom_mass':bottom,'cell_mass':cell,'total_mass':total,
               'score':(total-4424)//2,'bottom_score':(bottom-4096)//2})
assert {tuple(r['J_q']):r['score'] for r in rows}=={(2,5,5):3720,(4,5,5):3452,(6,3,5):3352,(6,5,5):3728}
assert min(r['score'] for r in rows)==3352
# Exact evaluation of the analytic bound at its proved global minimum for m>=6.
m,n=6,16
lower=8*m*n+584*m+80*n+3056+Fraction(5760*m-480,n)+Fraction(160*n-160,m)
assert lower==11138 and lower>11128
result={'rows':rows,'global_mass_lower_at_m6_n16':int(lower),'minimum_score':3352,
        'scope':'W=3D,U1=3D,U2=D;paper proves arbitrary-degree reduction to these four cases'}
Path('work/gct/fixed_bottom_optimum_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
for r in rows:print(r['J_q'],'score',r['score'],'bottom',r['bottom_score'],'C1_mass',r['max_C1_mass'],'V2_mass',r['max_V2_mass'])
print('GLOBAL_MASS_LOWER_m_ge_6',lower)
