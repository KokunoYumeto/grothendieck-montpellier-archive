"""Independent contraction-by-source-assignment audit of EX37's binary point."""
from pathlib import Path
from itertools import product
from functools import reduce
import hashlib, json
import numpy as np

W = Path(__file__).resolve().parents[1]
inp = json.loads((W/'inputs/ex_balanced_tangent_parameters.json').read_text())
saved = json.loads((W/'outputs/ex_balanced_tangent_results.json').read_text())
maps = [np.asarray(a, dtype=np.int64) for a in inp['local_maps']]
incidence = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8)]
out_coordinates = list(product(range(4), repeat=6))
rows = [[np.array([i for i,a in enumerate(out_coordinates) if a[v]==b])
         for b in range(4)] for v in range(6)]
J = np.zeros((4096,192), dtype=np.int64)
for assignment in product(range(2), repeat=9):
    inputs = [tuple(assignment[k] for k in edges) for edges in incidence]
    vectors = [maps[v][(slice(None),)+inputs[v]] for v in range(6)]
    for v in range(6):
        values = reduce(np.multiply.outer, [vectors[j] for j in range(6) if j!=v]).ravel()
        virtual = sum(bit*2**(2-j) for j,bit in enumerate(inputs[v]))
        for b in range(4):
            J[rows[v][b],32*v+8*b+virtual] += values
sha = hashlib.sha256(J.astype('<i8').tobytes()).hexdigest()
assert sha == saved['jacobian_sha256_little_endian_int64']
minor = J[np.ix_(saved['minor_rows'], saved['minor_columns'])]
assert minor.tolist() == saved['minor_integer_entries']

def rank_det(matrix,p):
    M=matrix.copy()%p; rank=0; det=1
    for j in range(M.shape[1]):
        choices=np.nonzero(M[rank:,j])[0]
        if not choices.size: continue
        k=rank+int(choices[0])
        if k!=rank: M[[k,rank]]=M[[rank,k]]; det=-det
        pivot=int(M[rank,j]); det=det*pivot%p
        row=M[rank]*pow(pivot,-1,p)%p
        M[rank]=row
        M[rank+1:] = (M[rank+1:]-M[rank+1:,j,None]*row[None,:])%p
        rank+=1
        if rank==M.shape[0]: break
    return rank,det%p

result={'status':'PASS','reconstruction':'512 source assignments; outer products of five local vectors',
        'jacobian_sha256_little_endian_int64':sha,'checks':{}}
for p in (2,101):
    full=rank_det(J,p)[0]
    md=rank_det(minor,p)
    singles=[rank_det(J[:,32*v:32*(v+1)],p)[0] for v in range(6)]
    omitted=[rank_det(np.delete(J,range(32*v,32*(v+1)),axis=1),p)[0] for v in range(6)]
    assert full==160 and md==(155,saved['minor_checks'][str(p)]['determinant'])
    assert singles==[32]*6 and omitted==[138]*6
    result['checks'][str(p)]={'full_rank':full,'minor_rank_det':md,
                            'single_site_ranks':singles,'five_site_ranks':omitted}
    print(json.dumps({'prime':p,**result['checks'][str(p)]}),flush=True)
assert 15*2**4-24*2**2+10==154
for N in range(2,101):
    q=2**N
    assert 132*32**(N-1)>15*q**4-24*q**2+10
result['binary_power_numeric_diagnostic']='N=2..100; general proof is in paper'
(W/'outputs/rt_balanced_tangent_verification.json').write_text(json.dumps(result,indent=2)+'\n')
