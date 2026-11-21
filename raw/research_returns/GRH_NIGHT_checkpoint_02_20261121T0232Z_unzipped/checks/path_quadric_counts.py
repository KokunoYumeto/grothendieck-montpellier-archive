"""Finite exact checks for MT-Q01; the symbolic proof is in GRH_NIGHT.tex."""
from itertools import product
import json

rows=[]
for q in (2,3,5):
    for k in range(2,7):
        count=sum(sum(x[i]*x[i+1] for i in range(k-1))%q==0
                  for x in product(range(q),repeat=k))
        d=(k+1)//2
        expected=q**(k-1)+(q-1)*q**(d-1)
        assert count==expected,(q,k,count,expected)
        rows.append(dict(q=q,k=k,count=count,expected=expected))
print(json.dumps({'statement':'MT-Q01','scope':'Exact finite checks only; no formal proof assistant claim.',
                  'cases':rows},indent=2))
