"""Independent boundary-coordinate audit of the integral 18-term identity.

The discovery/checker code enumerates internal wire assignments. This audit
instead evaluates each boundary coefficient directly as a product of six
epsilon entries. It also checks the division-free symmetric-quotient minor.
"""
from pathlib import Path
from itertools import product, permutations
import json, hashlib

W=Path(__file__).resolve().parents[1]
P=W/'inputs/pg_cauchy_r3_integral_cover.json'
data=json.loads(P.read_text())

def pos(v,u):
    assert v!=u and 0<=v<3 and 0<=u<3
    return int(u>min(x for x in range(3) if x!=v))

def eps(a,b):
    return b-a

def coeff(boundary,edges,mask=0):
    value=1
    for v,p,u,q in edges:
        a=(boundary[v]>>(p^((mask>>v)&1)))&1
        b=(boundary[u]>>(q^((mask>>u)&1)))&1
        value*=eps(a,b)
    return value

target_edges=[(s+i,pos(i,j),s+j,pos(j,i))
              for s in (0,3) for i in range(3) for j in range(i+1,3)]
perms=list(permutations(range(3)))
source_edges={sigma:[(i,pos(i,l),3+sigma[l],pos(sigma[l],sigma[i]))
                     for i in range(3) for l in range(3) if i!=l]
              for sigma in perms}
assert len(data['terms'])==18
for term in data['terms']:
    assert tuple(term['sigma']) in source_edges
    assert term['coefficient'] in(-1,1) and 0<=term['swap_mask']<64

quotients=[[0]*7 for _ in range(3**6)]
target_nonzero=[]
for boundary in product(range(4),repeat=6):
    expected=coeff(boundary,target_edges)
    actual=sum(t['coefficient']*coeff(boundary,source_edges[tuple(t['sigma'])],t['swap_mask'])
               for t in data['terms'])
    assert actual==expected,(boundary,expected,actual)
    idx=0;qi=0
    for x in boundary:idx=4*idx+x;qi=3*qi+x.bit_count()
    if expected:target_nonzero.append([idx,expected])
    for j,sigma in enumerate(perms):quotients[qi][j]+=coeff(boundary,source_edges[sigma])
    quotients[qi][6]+=expected

rows=[140,142,146,154,150,156]
minor=[quotients[r][:6] for r in rows]
assert minor==[[-int(i==j) for j in range(6)]for i in range(6)]
target_values=[quotients[r][6]for r in rows]
assert target_values==[1,-1,-1,1,1,-1]
class_totals=[sum(t['coefficient']for t in data['terms']if tuple(t['sigma'])==s)for s in perms]
assert class_totals==[-x for x in target_values]
out={'status':'PASS','input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
     'coordinate_count':4**6,'method':'Direct products of boundary epsilon entries; no generator imports',
     'integral_identity':True,'all_fields':True,'term_count':18,
     'target_nonzero_coordinates':target_nonzero,
     'matching_permutations':[list(s)for s in perms],
     'signed_class_totals':class_totals,
     'symmetric_quotient_rows':rows,'unit_minor':minor,'quotient_target':target_values,
     'class_omission_scope':'No matching class can be omitted if all local maps are port permutations and scalars; arbitrary local maps are not covered'}
DP=W/'inputs/pg_cauchy_r3_dense_cover.json'
if DP.exists():
    dense=json.loads(DP.read_text());assert len(dense['terms'])==13
    expanded={}
    for term in dense['terms']:
        sig=tuple(term['sigma']);assert sig in source_edges
        pol={0:term['coefficient']}
        assert len(term['local_I_swap_coefficients'])==6
        for party,pair in enumerate(term['local_I_swap_coefficients']):
            assert len(pair)==2 and all(isinstance(a,int)for a in pair)
            pol={mask|(choice<<party):value*pair[choice]
                 for mask,value in pol.items()for choice in(0,1)if value*pair[choice]}
        for mask,value in pol.items():expanded[sig,mask]=expanded.get((sig,mask),0)+value
    canonical={}
    for term in data['terms']:
        key=tuple(term['sigma']),term['swap_mask']
        canonical[key]=canonical.get(key,0)+term['coefficient']
    assert {k:v for k,v in expanded.items()if v}=={k:v for k,v in canonical.items()if v}
    out['dense13']={'status':'PASS','input_sha256':hashlib.sha256(DP.read_bytes()).hexdigest(),
                    'method':'Independent sparse polynomial multiplication of party-local I/SWAP factors'}
(W/'outputs/rt_crown_integral_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='target_nonzero_coordinates'},indent=2))
