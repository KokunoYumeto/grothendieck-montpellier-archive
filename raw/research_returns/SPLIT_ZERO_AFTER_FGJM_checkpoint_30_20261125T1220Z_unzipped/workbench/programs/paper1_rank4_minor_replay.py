"""Independent replay from the supplied words/rows; no author program imported.

Uses left Hecke multiplication with words processed backwards, expands the two
summands of each P-generator separately, then uses modular Bareiss elimination.
"""
from pathlib import Path
from itertools import permutations
import hashlib,json,math,time
BASE=Path(__file__).resolve().parents[1]
INPUT=BASE/'checks/paper3_rank4_word_minor.json'
t0=time.time();j=json.loads(INPUT.read_text());prime=j['prime']
if any(prime%d==0 for d in range(2,math.isqrt(prime)+1)):raise ValueError('not prime')
perms=list(permutations(range(1,5)));index={p:i for i,p in enumerate(perms)}
rows=j['selected_rows_zero_based'];words=j['words']
for row,ps in zip(rows,j['selected_rows_as_permutations']):
 if list(perms[row//24])!=ps[0]or list(perms[row%24])!=ps[1]:raise ValueError('row convention')
def left_terms(i,s,c,h):
 w=perms[i];wi=w.index(s);wj=w.index(s+1);z=list(w);z[wi],z[wj]=z[wj],z[wi]
 return ((index[tuple(z)],1),(i,(c+(h if wi>wj else 0))%prime))
def step(vec,s,v):
 vi=pow(v,-1,prime);h=(v-vi)%prime;out={}
 for c in [vi,(-v)%prime]:
  factors=[left_terms(i,s,c,h)for i in range(24)]
  for (a,b),coef in vec.items():
   for x,cx in factors[a]:
    for y,cy in factors[b]:
     out[x,y]=(out.get((x,y),0)+coef*cx*cy)%prime
 return {key:v for key,v in out.items()if v}
def vector(word,v):
 out={(0,0):1}
 for s in reversed(word):out=step(out,s,v)
 return out
def det_bareiss(A):
 a=[r[:]for r in A];n=len(a);sgn=1;previous=1
 for k in range(n-1):
  pivot=next((i for i in range(k,n)if a[i][k]),None)
  if pivot is None:return 0
  if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sgn=-sgn
  p=a[k][k];inv=pow(previous,-1,prime)
  for i in range(k+1,n):
   q=a[i][k]
   for z in range(k+1,n):a[i][z]=(p*a[i][z]-q*a[k][z])*inv%prime
   a[i][k]=0
  previous=p
 return sgn*a[-1][-1]%prime
v0=j['parameter_v'];values=[v0,(-v0)%prime,pow(v0,-1,prime),(-pow(v0,-1,prime))%prime];dets=[]
for v in values:
 columns=[vector(word,v)for word in words]
 matrix=[[col.get((r//24,r%24),0)for col in columns]for r in rows]
 dets.append(det_bareiss(matrix))
norm=math.prod(dets)%prime
if dets!=j['minor_determinants_mod_prime']or norm!=j['norm_determinant_mod_prime']:raise ValueError((dets,norm))
out={'status':'independent exact modular replay passed','input_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'prime':prime,'prime_independently_checked':True,'word_count':len(words),'selected_rows':len(rows),'method':'left multiplication, reverse word order, two summands expanded separately, modular Bareiss determinant','conjugate_v_values':values,'determinants':dets,'norm':norm,'generic_dimension_upper_bound':'external primary background; not proved by this finite calculation','seconds':round(time.time()-t0,3)}
(BASE/'checks/paper1_rank4_minor_replay.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
