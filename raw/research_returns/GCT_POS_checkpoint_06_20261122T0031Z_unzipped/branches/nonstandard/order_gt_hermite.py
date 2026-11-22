"""Actual polynomial Hermite basis adapted to a recorded total GT order.

No polynomial saturation: both original-basis containment and polynomial
straight-line preimages are checked.  This is an explicit additional
label-order choice for the repaired bar-fixed variant.
"""
from pathlib import Path
from collections import Counter
import json,gzip,time
from flint import fmpq,fmpq_poly
from polynomial_order_rank4_flint import Module,combination,sv

HERE=Path(__file__).resolve().parent
ZERO=fmpq_poly([])


def parse(p):
    return fmpq_poly([fmpq(p.get(str(i),'0'))
                      for i in range(max(map(int,p),default=-1)+1)])


def vector(v):return {int(j):parse(p) for j,p in v.items()}


def main():
    started=time.time()
    with gzip.open(HERE/'polynomial_order_gt_coordinates.json.gz','rt') as f:data=json.load(f)
    with gzip.open(HERE/'polynomial_order_rank4_rows.json.gz','rt') as f:ambient=json.load(f)
    order=list(reversed(data['variant_order']['ascending_coordinate_indices']))
    inv={j:i for i,j in enumerate(order)}
    source=[{inv[j]:p for j,p in vector(v).items()} for v in data['basis_numerators']]
    M=Module()
    for i,v in enumerate(source):
        assert M.add(v,M.slp.word(i))
        if (i+1)%10==0:
            print(json.dumps({'input_rows':i+1,'rank':len(M.rows),'updates':M.updates,
                              'maximum_row_degree':max(p.degree() for v in M.rows.values() for p in v.values()),
                              'seconds':time.time()-started}),flush=True)
    assert sorted(M.rows)==list(range(114))
    assert all(M.contains(v) for v in source)
    nodes,finals=M.slp.compact([M.expressions[j] for j in range(114)])
    uses=Counter(finals)
    for node in nodes:
        if node[0]=='combine':
            uses[node[1]]+=1
            if node[3] is not None:uses[node[3]]+=1
    leaves=[]
    for a,b in zip(source,ambient['rows']):
        v=dict(a)
        v.update({j+114:p for j,p in vector(b['vector']).items()})
        leaves.append(v)
    cache={}
    for i,node in enumerate(nodes):
        if node[0]=='word':cache[i]=leaves[node[1]]
        else:
            _,a,p,b,q=node
            cache[i]=combination(cache[a],p,{} if b is None else cache[b],q)
            for k in [a,b]:
                if k is not None:
                    uses[k]-=1
                    if not uses[k]:del cache[k]
    rows=[]
    for j,idx in enumerate(finals):
        v=cache[idx]
        assert {k:p for k,p in v.items() if k<114}==M.rows[j]
        rows.append({'pivot':j,'gt_numerators':sv(M.rows[j]),
                     'ambient_coordinates':sv({k-114:p for k,p in v.items() if k>=114}),
                     'slp_node':idx})
    slp=[]
    for node in nodes:
        if node[0]=='word':slp.append({'basis_row':node[1]})
        else:
            _,a,p,b,q=node
            from polynomial_order_rank4_flint import sp
            slp.append({'a':a,'p':sp(p),'b':b,'q':sp(q)})
    result={'status':'PASS','scope':'Actual unsaturated polynomial order; recorded total GT order variant',
            'coordinate_labels':[data['coordinate_labels'][j] for j in order],
            'coordinate_denominators':[data['coordinate_denominators'][j] for j in order],
            'variant_order':data['variant_order'],'ambient_coordinates':ambient['coordinates'],
            'rows':rows,'straight_line_program':slp,
            'first_stage_label':data['coordinate_labels'][order[-1]],
            'first_stage_scaling':parse(data['coordinate_denominators'][order[-1]]).degree()-M.rows[113][113].degree(),
            'seconds':time.time()-started}
    with gzip.open(HERE/'polynomial_order_gt_hermite.json.gz','wt') as f:json.dump(result,f)
    print(json.dumps({'status':'PASS','rank':114,'straight_line_nodes':len(nodes),
                      'first_stage_label':result['first_stage_label'],
                      'first_stage_scaling':result['first_stage_scaling'],
                      'first_stage_ambient_support':len(rows[-1]['ambient_coordinates']),
                      'maximum_ambient_polynomial_degree':max(parse(p).degree() for row in rows for p in row['ambient_coordinates'].values()),
                      'seconds':time.time()-started}),flush=True)


if __name__=='__main__':main()
