"""Reduce root's complete coefficient table in the surviving affine-line chart.

The full determinant is NOT rebuilt.  Only its squarefree-x coefficient is
independently reconstructed by the exact transversal condition.  The remaining
input is the retained root table, whose source hash is checked.
"""
from pathlib import Path
from itertools import product, permutations
from collections import Counter
from functools import lru_cache
from datetime import datetime, timezone
import hashlib, json, sys, time
sys.path.insert(0, '/tmp/research_sa15_flint')
from flint import fmpz_mod_mpoly_ctx

start=time.perf_counter()
root=Path(__file__).resolve().parents[3]
data=root/'outputs/root_Moore_Fermat_fulltorus_normalized_coefficients.json'
metadata=json.loads((root/'code/root_Moore_Fermat_fulltorus_coefficients.output.json').read_text())
assert hashlib.sha256(data.read_bytes()).hexdigest()==metadata['normalized_table_sha256']
table=json.loads(data.read_text())
assert len(table)==67
G=list(product(range(3),repeat=2));ind={g:i for i,g in enumerate(G)}
plus=[[ind[((a[0]+b[0])%3,(a[1]+b[1])%3)] for b in G] for a in G]
minus=[[ind[((a[0]-b[0])%3,(a[1]-b[1])%3)] for b in G] for a in G]

coefficient=set();transversals=0
for p in permutations(range(9)):
    if len({plus[i][p[i]] for i in range(9)})!=9:
        continue
    transversals+=1
    e=[0]*9
    for i,j in enumerate(p):e[minus[i][j]]+=1
    e=tuple(e)
    if e in coefficient:coefficient.remove(e)
    else:coefficient.add(e)
expected=set()
for i,j in product(range(9),repeat=2):
    e=[0]*9;e[i]+=6;e[j]+=3;expected.add(tuple(e))
assert coefficient==expected and len(coefficient)==81

# Set c00=1 and use a character to make c22=c11.  Write
# (c00,...,c22)=(1,a,u,b,d,v,w,t,d).
# The four line equations reduce u^3=1+a^3, v^3=a^3+b^3,
# w^3=1+b^3, t^3=1+a^3+b^3.
names=['a','b','d','u','v','w','t']
ctx=fmpz_mod_mpoly_ctx.get(names,2)
decode=lambda m:tuple((m>>(4*i))&15 for i in range(7))
encode=lambda e:sum(v<<(4*i) for i,v in enumerate(e))
def multiply(a,b):
    result=set()
    for x in a:
        for y in b:
            m=x+y
            if m in result:result.remove(m)
            else:result.add(m)
    return result
rhs=[{0,3},{3,3<<4},{0,3<<4},{0,3,3<<4}]
powers=[]
for base in rhs:
    seq=[{0}]
    for j in range(3):seq.append(multiply(seq[-1],base))
    powers.append(seq)
@lru_cache(None)
def reduce_monomial(m):
    e=list(decode(m));result={0}
    for j in range(4):
        q,r=divmod(e[j+3],3)
        e[j+3]=r
        result=multiply(result,powers[j][q])
    base=encode(e)
    return {base+x for x in result}
def normalized(poly):
    if not poly:return (),()
    exps=[decode(m) for m in poly]
    common=tuple(min(e[i] for e in exps) for i in range(7))
    sub=encode(common)
    return tuple(sorted(m-sub for m in poly)),common
records=[];distinct={}
for number,item in enumerate(table):
    poly=set()
    for old in item['terms']:
        new=(old[1],old[3],old[4]+old[8],old[2],old[5],old[6],old[7])
        poly.symmetric_difference_update(reduce_monomial(encode(new)))
    norm,monomial=normalized(poly)
    if norm not in distinct:
        p=ctx.from_dict({decode(m):1 for m in norm})
        unit,factors=p.factor() if p else (0,[])
        distinct[norm]={'polynomial':str(p),'term_count':len(norm),
                        'terms':[decode(m) for m in norm],
                        'factorization':{'unit':str(unit),'factors':[{'factor':str(f),'power':int(n),'terms':[[[int(x) for x in e],int(v)] for e,v in f.to_dict().items()]} for f,n in factors]},
                        'original_polynomial_indices':[]}
    distinct[norm]['original_polynomial_indices'].append(number)
    records.append({'original_index':number,'removed_normal_form_monomial':monomial,
                    'normalized_reduction':str(ctx.from_dict({decode(m):1 for m in norm}))})
out={'status':'EXACT_REDUCTION_COMPLETE','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-start,
     'input_table':str(data.relative_to(root)),'input_sha256':metadata['normalized_table_sha256'],
     'independent_squarefree_coefficient':{'transversal_permutations':transversals,'terms':len(coefficient),
        'identity':'[product x_g] D_c = (sum c_g^3)^3','all_terms':[list(m) for m in sorted(coefficient)]},
     'variables':names,'c_normal_form':['1','a','u','b','d','v','w','t','d'],
     'relations':['u^3=1+a^3','v^3=a^3+b^3','w^3=1+b^3','t^3=1+a^3+b^3'],
     'distinct_reduced_polynomials':list(distinct.values()),'all_reductions':records,
     'counts':{'input_polynomials':len(table),'distinct_reductions':len(distinct),
               'zero_reductions':sum(not v['term_count'] for v in distinct.values())},
     'scope':'Exploratory exact quotient-ring coefficient reduction on the full torus. No solution, exclusion, geometric theta implication or wall nonemptiness inferred.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','actual_utc','runtime_seconds','counts')},indent=2))
for v in distinct.values():print(json.dumps({'indices':v['original_polynomial_indices'],'terms':v['term_count'],'factors':[(f['factor'],f['power']) for f in v['factorization']['factors']]}))
