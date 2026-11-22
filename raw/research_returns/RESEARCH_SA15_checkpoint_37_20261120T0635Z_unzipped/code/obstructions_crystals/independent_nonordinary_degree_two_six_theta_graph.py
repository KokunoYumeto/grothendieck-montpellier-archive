"""Exact F2 graph supplement; no inference of geometric monodromy."""
from pathlib import Path
from itertools import combinations
import json,time,datetime
start=time.perf_counter()
V=tuple(range(1,7))
E=tuple((i,j,a) for i,j in combinations(V,2) for a in (0,1))
idx={e:i for i,e in enumerate(E)}
def basis(vectors):
    piv={}
    for v in vectors:
        while v:
            j=v.bit_length()-1
            if j in piv:v^=piv[j]
            else:piv[j]=v;break
    return piv
def rank(v):return len(basis(v))
def bit(e):return 1<<idx[e]
stars=[sum(bit(e) for e in E if i in e[:2]) for i in V]
assert len(E)==30 and rank(stars)==5
assert len(E)-rank(stars)==25
parts=[({1,2,3},{4,5,6}),({1,2,4},{3,5,6})]
rows=[]
for I,J in parts:
    cross=[e for e in E if (e[0] in I)!=(e[1] in I)]
    assert len(cross)==18
    cv=[bit(e) for e in cross]
    heart=[cv[0]^v for v in cv[1:]]
    qrank=rank(stars+cv)-rank(stars)
    hrank=rank(stars+heart)-rank(stars)
    assert (qrank,hrank)==(17,16)
    rows.append({'first':sorted(I),'second':sorted(J),'cross_edges':18,'graph_rank':qrank,'heart_rank':hrank})
vC=bit((1,3,0))^bit((2,3,0))
vD=bit((4,5,0))^bit((4,6,0))
altcross={e for e in E if (e[0] in parts[1][0])!=(e[1] in parts[1][0])}
for v in (vC,vD):
    assert v.bit_count()%2==0
    assert all(not (v>>idx[e]&1) or e in altcross for e in E)
    assert rank(stars+[v])==6
proj=[]
for I in parts[0]:
    internal=[e for e in E if e[0] in I and e[1] in I]
    ii={e:i for i,e in enumerate(internal)}
    st=[sum(1<<ii[e] for e in internal if i in e[:2]) for i in sorted(I)]
    assert len(internal)==6 and rank(st)==2
    def restrict(v):return sum((1<<ii[e]) for e in internal if v>>idx[e]&1)
    values=[int(rank(st+[restrict(v)])>rank(st)) for v in (vC,vD)]
    proj.append(values)
assert proj==[[1,0],[0,1]]
assert ((vC>>idx[(1,3,0)])^(vC>>idx[(1,3,1)]))&1
assert ((vD>>idx[(4,5,0)])^(vD>>idx[(4,5,1)]))&1
for f in (0,1):
    assert 2*(8+f)+17-f==33+f
    assert 25+6*f-f==25+5*f
    assert (33+f)-(1+f)==32
result={'verdict':'PASS','time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'edges':30,'vertex_coboundary_rank':5,'total_graph_rank':25,'partitions':rows,'old_component_projection_nonzero':proj,'stable_rank_at_six_theta':{'f0':25,'f1':30},'generic_relative_rank':{'f0':33,'f1':34},'common_covector_kernel_rank':32,'scope':'Finite doubled-K6 graph calculation and stated rank arithmetic only; no geometric inference.'}
out=Path(__file__).resolve().parent.parent/'outputs/nonordinary_degree_two_six_theta_graph.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
