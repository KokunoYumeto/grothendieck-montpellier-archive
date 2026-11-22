"""Extend the explicit product-path repair to the other minimal outer block.

The thetaSprime31 order is isolated by polynomial Hermite operations
inside the actual 29-dimensional sum with Sprime22.  Each product-path
down-set is then computed as an actual polynomial intersection, using
excluded GT pivots first.  This is exploratory until its complete proof
and certificate receive independent review; no full E(4) claim is made.
"""
from pathlib import Path
from collections import Counter
import gzip,json,time
from flint import fmpq_poly
from polynomial_order_rank4_flint import Module,combination,sp,sv
from bar_fixed_first_stages import parse,vector
from bar_fixed_block_rank4 import solve_stage

HERE=Path(__file__).resolve().parent
ZERO=fmpq_poly([])


def adapt(GT,ambient,columns,selected_columns=None):
    """Unimodular module reduction, with exact original-row containment."""
    inv={j:i for i,j in enumerate(columns)};n=len(columns)
    source=[{inv[j]:p for j,p in row.items()} for row in GT]
    M=Module()
    for i,row in enumerate(source):M.add(row,M.slp.word(i))
    assert sorted(M.rows)==list(range(n))
    assert all(M.contains(row) for row in source)
    if selected_columns is None:selected_columns=columns
    positions=[inv[j] for j in selected_columns]
    nodes,finals=M.slp.compact([M.expressions[j] for j in positions])
    uses=Counter(finals)
    for node in nodes:
        if node[0]=='combine':
            uses[node[1]]+=1
            if node[3] is not None:uses[node[3]]+=1
    leaves=[]
    for x,y in zip(source,ambient):
        z=dict(x);z.update({j+n:p for j,p in y.items()});leaves.append(z)
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
    resultGT=[];resultAmbient=[]
    for pivot,idx in zip(positions,finals):
        v=cache[idx]
        assert {j:p for j,p in v.items() if j<n}==M.rows[pivot]
        resultGT.append({columns[j]:p for j,p in v.items() if j<n})
        resultAmbient.append({j-n:p for j,p in v.items() if j>=n})
    serial=[]
    for node in nodes:
        if node[0]=='word':serial.append({'input_row':node[1]})
        else:
            _,a,p,b,q=node;serial.append({'a':a,'p':sp(p),'b':b,'q':sp(q)})
    certificate={'column_order':columns,'selected_columns':selected_columns,
                 'full_Hermite_rows':[sv(M.rows[j]) for j in range(n)],
                 'output_GT':[sv(v) for v in resultGT],'output_ambient':[sv(v) for v in resultAmbient],
                 'straight_line_program':serial,'final_nodes':finals,
                 'input_rows_contained':len(source)}
    return resultGT,resultAmbient,certificate


def main():
    started=time.time()
    with gzip.open(HERE/'polynomial_order_gt_hermite.json.gz','rt') as f:data=json.load(f)
    keys=[(tuple(a),tuple(b)) for a,b in data['ambient_coordinates']]
    GT=[vector(r['gt_numerators']) for r in data['rows'][85:]]
    ambient=[vector(r['ambient_coordinates']) for r in data['rows'][85:]]
    block_columns=list(range(85,110))
    blockGT,blockAmbient,isolation=adapt(GT,ambient,list(range(110,114))+block_columns,block_columns)
    assert all(not set(row)-set(block_columns) for row in blockGT)
    with gzip.open(HERE/'bar_fixed_theta_order.json.gz','wt') as f:json.dump(isolation,f)
    print(json.dumps({'isolated_actual_block':25,'nodes':len(isolation['straight_line_program']),
                      'seconds':time.time()-started}),flush=True)
    paths=[4,3,0,2,1]
    coordinate={(label['matrix_row'],label['matrix_column']):j
                for j,label in enumerate(data['coordinate_labels']) if label['module']=='thetaSprime31'}
    scalings={};stages=[]
    for r in range(5):
        for c in range(5):
            current=coordinate[paths[r],paths[c]]
            allowed=sorted(coordinate[paths[i],paths[j]] for i in range(r+1) for j in range(c+1))
            excluded=[j for j in block_columns if j not in allowed]
            adaptedGT,adaptedAmbient,certificate=adapt(blockGT,blockAmbient,excluded+allowed,allowed)
            inv={j:i for i,j in enumerate(allowed)}
            assert current==allowed[0]
            assert all(not set(row)-set(allowed) for row in adaptedGT)
            H=[{inv[j]:p for j,p in row.items()} for row in adaptedGT]
            den=[parse(data['coordinate_denominators'][j]) for j in allowed]
            answer=solve_stage(H,adaptedAmbient,den,[scalings[j] for j in allowed[1:]],keys)
            broad=solve_stage(H,adaptedAmbient,den,[scalings[j] for j in allowed[1:]],keys,'length_strata')
            assert broad['global_minimum_exists']==answer['global_minimum_exists']
            assert broad['lexicographic_candidate']==answer['lexicographic_candidate']
            if answer['global_minimum_exists']:
                assert broad['unique_in_full_bar_fixed_domain']==answer['unique_in_full_bar_fixed_domain']
            else:
                answer['length_stratum_failure_witness']=broad['partial_order_failure_witness']
                assert broad['partial_order_failure_witness']['coordinate']==263
            answer.update({'stage':len(stages)+1,'path_rectangle':[r+1,c+1],
                           'current_GT_coordinate':current,'allowed_GT_coordinates':allowed,
                           'label':data['coordinate_labels'][current],
                           'also_verified_for_length_stratum_order':True})
            stages.append(answer)
            with gzip.open(HERE/f'bar_fixed_theta_stage_{len(stages):02d}_order.json.gz','wt') as f:json.dump(certificate,f)
            result={'status':'COMPUTED_PENDING_PROOF_REVIEW','scope':'Explicit product-path bar-fixed repair, thetaSprime31 block only.',
                    'stages':stages,'seconds':time.time()-started}
            (HERE/'bar_fixed_theta_stages.json').write_text(json.dumps(result,indent=2)+'\n')
            print(json.dumps({'stage':len(stages),'rectangle':[r+1,c+1],
                              'current':current,'global_minimum':answer['global_minimum_exists'],
                              'unique':answer.get('unique_in_full_bar_fixed_domain'),
                              'exponent':answer['lexicographic_candidate']['scaling'],
                              'quotient_dimension':answer['finite_quotient_dimension'],
                              'cutoff':answer['cutoff_B'],
                              'space_dimension':answer['finite_space_dimension'],
                              'seconds':time.time()-started}),flush=True)
            if not answer['global_minimum_exists'] or not answer.get('unique_in_full_bar_fixed_domain'):return
            scalings[current]=answer['lexicographic_candidate']['scaling']


if __name__=='__main__':main()
