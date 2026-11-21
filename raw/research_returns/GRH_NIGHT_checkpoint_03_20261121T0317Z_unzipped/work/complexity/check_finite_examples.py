import itertools,json,math
from pathlib import Path

def dot(a,b):return (a&b).bit_count()%2
def mv(rows,v):return sum(dot(row,v)<<i for i,row in enumerate(rows))
def cov_times(c,rows):
 out=0
 for i in range(3):
  if c>>i&1:out^=rows[i]
 return out
G=[r for r in itertools.product(range(8),repeat=3) if len({mv(r,v) for v in range(8)})==8]
assert len(G)==168
counts={}
for g in G:
 a=sum(mv(g,v)==v for v in range(1,8))
 b=sum(cov_times(c,g)==c for c in range(1,8))
 assert a==b
 counts[a]=counts.get(a,0)+1
H=[g for g in G if mv(g,1)==1]
fixed_covectors=[c for c in range(1,8) if all(cov_times(c,g)==c for g in H)]
assert len(H)==24 and not fixed_covectors
val=pow(2,17,35)
gcds=[math.gcd(x,35) for x in [2,val-1,val+1]]
assert val==32 and gcds==[1,1,1]
out={'GL3_F2_order':len(G),'point_stabilizer_order':len(H),'fixed_point_count_distribution':counts,'stabilizer_common_nonzero_fixed_covectors':fixed_covectors,'Miller_example':{'N':35,'base':2,'odd_exponent':17,'power':val,'gcds':gcds},'status':'all exact integer/finite-field assertions passed','not_a_Lean_certificate':True}
Path('work/complexity/finite_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
