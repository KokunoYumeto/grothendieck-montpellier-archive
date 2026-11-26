"""Independent exact convolution of the integral sign-normalized border identity."""
from pathlib import Path
from itertools import product
from collections import defaultdict,Counter
import json,hashlib
root=Path(__file__).resolve().parents[1]
p=root/'inputs/pg_singh_border_sign_normalized.json';data=json.loads(p.read_text());D=data['tables']
coeff=defaultdict(int)
for first,second,realigned in [('U','V',False),('G','H',True)]:
 for da,ra,ja,va in D[first]:
  for db,rb,jb,vb in D[second]:
   if ja!=jb:continue
   a,b=divmod(ra,4);c,d=divmod(rb,4)
   ind=(a,c,b,d) if realigned else (a,b,c,d)
   coeff[(da+db,)+ind]+=va*vb
for degree in range(4):
 for x,y,u,v in product(range(4),repeat=4):
  assert coeff[(degree,x,y,u,v)]==int(degree==3 and x==v and y==u)
assert all(abs(v)<=1 for v in coeff.values())
assert not any(v for k,v in coeff.items() if k[0]==6)
error4={(2,1,3,0):-1,(1,2,0,3):-1,(2,2,0,0):1,(1,1,3,3):1}
error5={(3,3,0,0):-1,(1,1,2,2):-1,(3,1,2,0):-1,(1,3,0,2):-1}
for degree,error in [(4,error4),(5,error5)]:
 assert {k[1:]:v for k,v in coeff.items() if k[0]==degree and v}==error
# The full resulting tensor polynomial is a torus degeneration of its t=1 value.
weights=[[0,1,0,1],[0,2,1,1],[2,0,1,1],[1,0,1,0]]
for (degree,*ind),v in coeff.items():
 if v:assert degree==sum(w[i] for w,i in zip(weights,ind))
out={'status':'PASS exact integral identity, valid over every field','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'q':4,'cut_ranks':[3,3],'leading_degree':3,'leading_scalar':1,'checked_low_degree_coordinates':1024,'all_coefficients':[[*k,v] for k,v in sorted(coeff.items()) if v],'nonzero_counts_by_degree':[sum(k[0]==d and bool(v) for k,v in coeff.items()) for d in range(7)],'local_torus_weights':weights,'scope':'Polynomial border splitting; no exact rank3+3 identity or asymptotic amplification claimed.'}
f=root/'outputs/pg_singh_border_sign_verification.json';f.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='all_coefficients'},indent=2))
