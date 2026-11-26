"""Finite W0 certificate: a discrete bifibration need not be W0-Serre.

E is the chaotic groupoid on {0,1}. B is the one-object groupoid C2.
p(i->j)=j-i modulo2. q:*->B is a W0-map, its pullback is not.
"""
import json
from itertools import product

objects=[0,1]
arrows=list(product(objects,repeat=2))
def p(a):return (a[1]-a[0])%2
def compose(b,a):
    assert a[1]==b[0]
    return a[0],b[1]

for i,j,k in product(objects,repeat=3):
    assert p(compose((j,k),(i,j)))==(p((j,k))+p((i,j)))%2
for a in objects:
    for g in [0,1]:
        assert len([b for b in arrows if b[0]==a and p(b)==g])==1
        assert len([b for b in arrows if b[1]==a and p(b)==g])==1

def components(obs,ars):
    parent={o:o for o in obs}
    def root(o):
        if parent[o]!=o:parent[o]=root(parent[o])
        return parent[o]
    for a,b in ars:parent[root(a)]=root(b)
    return len({root(o) for o in obs})

fibre=[a for a in arrows if p(a)==0]
out={
 'statement_id':'SA27-C456',
 'base':'B=C2 one-object groupoid',
 'total_objects':objects,'total_arrows':arrows,
 'functor_values':[[list(a),p(a)] for a in arrows],
 'composition_preserved':True,
 'unique_source_and_target_lifts_for_each_base_arrow':True,
 'p_is_discrete_bifibration':True,
 'q':'point -> BC2',
 'pi0_point':1,'pi0_base':1,'q_in_W0':True,
 'pullback_objects':objects,'pullback_arrows':fibre,
 'pi0_pullback':components(objects,fibre),
 'pi0_total':components(objects,arrows),
 'pullback_of_q_in_W0':components(objects,fibre)==components(objects,arrows),
 'conclusion':'p is not W0-Serre despite being a discrete bifibration. Proper/smooth implication to Serre cannot be asserted for all fundamental localizers.'}
assert out['pi0_pullback']==2 and out['pi0_total']==1
assert not out['pullback_of_q_in_W0']
print(json.dumps(out,indent=2))
