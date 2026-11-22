"""Complete integer verification of K-017, independent of search and LP."""
from itertools import product
from pathlib import Path
import json,math

root=Path(__file__).resolve().parent
r=json.loads((root/'n8_cyclic256_fixedspace.json').read_text())
W=r['W'];M=r['M'];n=8
full=[e for e in product(range(n),repeat=3)if sum(W[j][e[j]]for j in range(3))%M==0]
expected=[tuple(e)for e in r['full_support']]
assert full==expected and len(full)==22
assert sum(map(sum,W))==2933 and math.gcd(2933,256)==1
assert all(len(set(w))==8 for w in W)
assert all(len(set((e[i],e[j])for e in full))==22 for i,j in [(0,1),(0,2),(1,2)])
y=[[14,-6,1,33,9,12,8,1],[-1,6,-6,-12,13,-9,-30,0],[-7,-8,-3,18,-27,-14,-7,0]]
assert sum(map(sum,y))==-15
for e in full:assert sum(y[j][e[j]]for j in range(3))==(64 if e==(3,4,3)else 0)
z=[[8*a-sum(v)for a in v]for v in y]
assert all(sum(v)==0 for v in z)
assert all(sum(z[j][e[j]]for j in range(3))==(527 if e==(3,4,3)else 15)for e in full)
print('PASS K-017: complete512-triple test, primitive character117, free support, explicit SL8^3 instability')
