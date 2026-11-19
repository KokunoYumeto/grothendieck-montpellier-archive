"""Exhaust the four integral graded-unit possibilities in weights one and two."""
from itertools import product
from pathlib import Path
import json,time
start=time.monotonic()
checks=[]
for u1,u2 in product((-1,1),repeat=2):
    checks.append({'weight_one_unit':u1,'weight_two_unit':u2,
                   'commuting_square':u2==2*u1})
assert not any(c['commuting_square'] for c in checks)
out={'checks':checks,'candidates':4,'survivors':0,'seconds':time.monotonic()-start}
path=Path(__file__).resolve().parents[1]/'logs/A_model_comparison.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
