"""Illustrative exact sizes for PG-OP-DETERMINISTIC; no feasibility decision.

Only integer comparisons are used. Search the powers of two for a safe
Schur-copy count satisfying the finite sums-of-squares lower-bound margin.
"""
from pathlib import Path
from math import isqrt
from datetime import datetime,timezone
import json
W=Path(__file__).resolve().parents[1]
def one(q):
 A=q*(q+1)//2;B=q*q*(q*q+1)//2;n=1;history=[]
 while True:
  den=(n+1)**A;L=(q**n+den-1)//den;m=L.bit_length()-1
  if m>=1:
   t=isqrt(2*m-1);t+=t*t<2*m-1;z=m-1-t
   passed=z>0 and 2**(28*z)>(n+1)**(20*B)*q**(25*n)
  else:t=None;z=None;passed=False
  history.append({'n':n,'m':m,'ceil_sqrt_2m_minus1':t,'margin_integer':z,'passes':bool(passed)})
  if passed:break
  n*=2
 return {'q':q,'A':A,'B':B,'first_passing_power_of_two':n,'history':history}
cfg=json.loads((W/'inputs/rt_operator_gate_sizes.json').read_text())
results=[one(q) for q in cfg['q_values']]
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS exact arithmetic for safe sizes only','scope':'No Specht feasibility system is solved and no square branch is selected.','results':results}
p=W/'outputs/rt_operator_gate_sizes.json';tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(p)
print(json.dumps([{'q':a['q'],'n':a['first_passing_power_of_two']} for a in results]))
