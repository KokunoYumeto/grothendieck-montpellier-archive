"""G031 independent all-face seeds, generators, graph and ray transitions."""
from pathlib import Path
from itertools import product,combinations
from collections import deque
from fractions import Fraction
from functools import lru_cache
import json,hashlib
HERE=Path(__file__).resolve().parent
scope={'__file__':str(HERE/'check_gap2_seeds_independent.py')}
raw=(HERE/'check_gap2_seeds_independent.py').read_text()
exec(compile(raw.split('target=json.loads')[0],scope['__file__'],'exec'),scope)
scope['PRIME']=257
trace=scope['trace'];character=scope['character'];z=scope['z']
classes=scope['CLASSES'];labels=scope['LABELS'];compositions=scope['compositions_at_most']
path=HERE.parent/'root/ALL_WALL_SUPPORT_GRAPH.json';target=json.loads(path.read_text())
weight=lambda g:sum((i+1)*v for i,v in enumerate(g))
def embed(u,support):
    out=[0]*4
    for i,v in zip(support,u):out[i]=v
    return tuple(out)
def axis_threshold(g,axis):
    a,b,c,d=g
    return max(1,3*b+2*c+d) if axis==0 else max(1,a+2*b+3*c)
def stable(g,support):
    return tuple(i for i in (0,3) if i in support and g[i]>=axis_threshold(g,i))
def normal(g,support):
    axes=stable(g,support)
    if not axes:return tuple(g)
    axis=axes[0];threshold=axis_threshold(g,axis);out=list(g)
    out[axis]=threshold+(g[axis]-threshold)%10
    return tuple(out)

computed={};max_reduced_inner=0;complemented=0
@lru_cache(None)
def values(g):
    global max_reduced_inner,complemented
    assert weight(g)%5==0
    n=weight(g)//5;H=sum(g);reverse=n>H-n
    reduced=tuple(reversed(g)) if reverse else g
    nr=H-n if reverse else n
    lam=tuple(sum(reduced[i:]) for i in range(4))
    assert sum(lam)==5*nr
    tr=tuple(trace(lam,nr,cyc)*((-1)**((5-len(cyc))*H) if reverse else 1)
             for cyc in classes)
    mult=tuple(sum(Fraction(character(mu,cyc)*q,z(cyc)) for cyc,q in zip(classes,tr))
               for mu in labels)
    assert all(q.denominator==1 and q>=0 for q in mult)
    mult=tuple(map(int,mult))
    computed[g]=dict(inner=n,reduced_inner=nr,traces=tr,multiplicities=mult)
    max_reduced_inner=max(max_reduced_inner,nr);complemented+=reverse
    return mult

faces={tuple(f['support']):f for f in target['faces']}
assert set(faces)=={s for length in range(1,4) for s in combinations(range(4),length)}
totals={'faces':14,'seeds':0,'generators':0,'nodes':0,'point_edges':0,'ray_checks':0,
        'raw_normalized_class_equalities':0,'largest_ray_cutoff':0}
summaries=[]
for support,face in sorted(faces.items(),key=lambda p:(len(p[0]),p[0])):
    expected_seeds={(tuple(r['parity']),tuple(r['increment'])):r for r in face['initial_seeds']}
    seeds=[]
    for parity in product((0,1),repeat=len(support)):
        base=embed(tuple(1+p for p in parity),support)
        for u in compositions(4,len(support)):
            full=embed(u,support);g=tuple(a+2*b for a,b in zip(base,full))
            if weight(g)%5:continue
            if any(weight(tuple(a+2*b for a,b in zip(base,embed(v,support))))%5==0
                   for v in product(*(range(q+1) for q in u)) if v!=u):continue
            row=expected_seeds[parity,full]
            assert tuple(row['gaps'])==g
            assert tuple(row['partition'])==tuple(sum(g[i:]) for i in range(5))
            assert row['inner']==weight(g)//5
            assert tuple(row['multiplicities'])==values(g)
            assert tuple(row['traces'])==computed[g]['traces']
            seeds.append(g)
    assert len(seeds)==len(expected_seeds)
    generators=[]
    for u in compositions(5,len(support)):
        full=embed(u,support)
        if not any(u) or weight(full)%5:continue
        if any(any(v) and v!=u and weight(embed(v,support))%5==0
               for v in product(*(range(q+1) for q in u))):continue
        generators.append(full)
    assert set(generators)==set(map(tuple,face['generators']))
    expected_edges={(tuple(r['source']),tuple(r['generator'])):r for r in face['edges']}
    expected_rays={(tuple(r['source']),tuple(r['generator']),r['axis'],r['q']):r for r in face['ray_edges']}
    queue=deque(normal(g,support) for g in seeds if min(values(g))==0)
    seen={};npoints=nrays=0;visited_points=set();visited_rays=set()
    while queue:
        g=queue.popleft()
        if g in seen:continue
        seen[g]=values(g);assert min(seen[g])==0
        for h in generators:
            raw=tuple(a+2*b for a,b in zip(g,h))
            tests=[(None,0,0,raw)]
            for axis in stable(g,support):
                needed=max(0,axis_threshold(raw,axis)-raw[axis]);cutoff=(needed+9)//10
                totals['largest_ray_cutoff']=max(totals['largest_ray_cutoff'],cutoff)
                for q in range(cutoff+1):
                    vector=list(raw);vector[axis]+=10*q
                    tests.append((axis,q,cutoff,tuple(vector)))
            for axis,q,cutoff,rawtarget in tests:
                norm=normal(rawtarget,support)
                val=values(rawtarget);assert val==values(norm)
                assert computed[rawtarget]['traces']==computed[norm]['traces']
                totals['raw_normalized_class_equalities']+=7
                if axis is None:
                    key=(g,h);row=expected_edges[key];visited_points.add(key);npoints+=1
                else:
                    key=(g,h,axis,q);row=expected_rays[key];visited_rays.add(key);nrays+=1
                    assert row['cutoff']==cutoff
                    if q==cutoff:
                        later=list(rawtarget);later[axis]+=10
                        assert axis in stable(rawtarget,support)
                        assert normal(tuple(later),support)==norm
                assert tuple(row['raw_target'])==rawtarget and tuple(row['target'])==norm
                assert tuple(row['multiplicities'])==val and tuple(row['traces'])==computed[norm]['traces']
                assert row['all_positive']==(min(val)>0)
                if min(val)==0:queue.append(norm)
    assert visited_points==set(expected_edges) and visited_rays==set(expected_rays)
    expected_nodes={tuple(r['gaps']):r for r in face['nodes']}
    assert set(seen)==set(expected_nodes)
    for g,row in expected_nodes.items():
        assert tuple(row['multiplicities'])==seen[g]
        assert tuple(row['traces'])==computed[g]['traces']
        assert tuple(row['stable_axes'])==stable(g,support)
    for name,count in [('seeds',len(seeds)),('generators',len(generators)),('nodes',len(seen)),
                       ('point_edges',npoints),('ray_checks',nrays)]:totals[name]+=count
    summary=dict(support=support,seeds=len(seeds),generators=len(generators),nodes=len(seen),
                 point_edges=npoints,ray_checks=nrays)
    summaries.append(summary);print('PASS',summary,flush=True)
assert totals['nodes']==344 and totals['point_edges']==1896 and totals['ray_checks']==2084
assert totals['largest_ray_cutoff']==3 and max_reduced_inner==22
receipt=dict(statement='G031 all proper faces, complete independent graph reconstruction',status='PASS',
 totals=totals,by_face=summaries,distinct_gap_vectors=len(computed),distinct_class_traces=7*len(computed),
 maximum_original_inner_degree=max(r['inner'] for r in computed.values()),
 maximum_inner_after_exact_complement=max_reduced_inner,complemented_vectors=complemented,
 finite_field=257,finite_field_exactness='After the explicit determinant-complement map, n<=22. Two-cycle interpolation degree<=44<257; centered signed bounds22<=23 and32<=10 uniquely recover each integer.',
 base_computations=scope['counts'],
 input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
 values_sha256=hashlib.sha256(json.dumps(sorted(computed.items()),separators=(',',':')).encode()).hexdigest(),
 method='Independent parity-minimal and zero-sum generation; BFS with every bounded ray transition; direct raw/normalized comparisons; integer single-cycle JT determinants and F257 two-cycle JT interpolation, with exact determinant-complement transport',
 scope='All graph fields and closure data checked. Infinite exhaustion and actual stability maps receive a separate whole-proof audit.')
(HERE/'ALL_WALL_SUPPORT_INDEPENDENT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ('by_face',)},indent=2))
