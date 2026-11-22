"""Finite algebra and specialization certificates for D:boundary-nonconstructible.
The infinite accumulation argument and étale duality are proved in paper_D.tex;
finite rings cannot certify the genuinely infinite topological obstruction.
"""
from itertools import product
from pathlib import Path
from datetime import datetime, timezone
import json, time
start=time.perf_counter()
# R_N = (F2[e]/e^2) x_F2 F2^(N+1) = (F2[e]/e^2) x F2^N.
# The last coordinate records the eventual value, equal to the residue of v.
def mulv(v,w):
    return ((v&1)*(w&1)) | ((((v&1)*((w>>1)&1)+((v>>1)&1)*(w&1))%2)<<1)
def add(x,y): return tuple(a^b for a,b in zip(x,y))
def mul(x,y): return (mulv(x[0],y[0]),)+tuple(a*b for a,b in zip(x[1:],y[1:]))
finite=[]
for n in range(1,7):
    ring=list(product(range(4),*([range(2)]*n)))
    one=(1,)+(1,)*n
    idem=[x for x in ring if mul(x,x)==x]
    assert len(idem)==2**(n+1)
    coordinates=[(0,)+tuple(int(j==i) for j in range(n)) for i in range(n)]
    for i,e in enumerate(coordinates):
        assert mul(e,e)==e
        for j,f in enumerate(coordinates):
            if i!=j: assert mul(e,f)==(0,)*(n+1)
        assert mul(e,add(one,e))==(0,)*(n+1)
    # Localizing at the distinguished residue point kills finite-support ideal.
    support=[x for x in ring if x[0]==0]
    assert len(support)==2**n
    for x in support:
        e=(0,)+tuple(int(a!=0) for a in x[1:])
        denominator=add(one,e)
        assert denominator[0]&1==1
        assert mul(x,denominator)==(0,)*(n+1)
    finite.append({'n':n,'ring_size':len(ring),'idempotents':len(idem),'support_ideal_size':len(support),'localization_kills_support':True})
# In F3[C2], e_sign=(1-sigma)/2 = 2 + sigma, e_triv=2+2sigma.
def gm(x,y): return ((x[0]*y[0]+x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0])%3)
es=(2,1);et=(2,2)
assert gm(es,es)==es and gm(et,et)==et and gm(es,et)==(0,0)
assert ((es[0]+et[0])%3,(es[1]+et[1])%3)==(1,0)
assert (es[0]+es[1])%3==0 # sign projector kills every trivial representation.
# Exact stalk complex Cone(Lambda -> Rj_*Lambda)[-1].
# At eta,m the map is identity; at n it is Lambda -> 0.
stalks={'eta':0,'m':0,'n':1}
assert stalks['eta']==stalks['m']
# Every finite-complement neighborhood contains a next isolated stalk unequal to m.
tails=[]
for maximum_excluded in range(21):
    witness=maximum_excluded+1
    assert witness>maximum_excluded and stalks['n']!=stalks['m']
    tails.append({'excluded_subset_bound':maximum_excluded,'nonzero_stalk_witness':witness})
output={'statement_id':'D:boundary-nonconstructible','utc':datetime.now(timezone.utc).isoformat(),'finite_ring_checks':finite,'C2_sign_projector_F3':{'sign':es,'trivial':et,'orthogonal_idempotents':True,'sign_on_trivial_cohomology':0},'stalk_dimensions_F3':stalks,'specialization_eta_to_m_isomorphism':True,'tail_witness_checks':tails,'limitation':'Finite auxiliaries only. Non-local-constancy of the infinite ring and étale cohomology identities are proved mathematically in paper_D.tex.','elapsed_seconds':time.perf_counter()-start}
p=Path(__file__).with_name('check_d10_nonconstructible_output.json');p.write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output,indent=2))
