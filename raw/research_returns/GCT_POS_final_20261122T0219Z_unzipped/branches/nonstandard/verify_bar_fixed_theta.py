"""Certificate-only verification of N018, without module construction.

For each actual intersection: selected rows are replayed as polynomial
combinations of prior actual rows; prior rows divide exactly by the full
triangular certificate; discarded leading pivots force the intersection.
Membership of discarded output rows is not needed for this argument.

Finite degree comparisons are independently replayed using Flint matrix
ranks, not the custom incremental equation class used by the search.
The all-degree completeness of these finite spaces is N016 together
with the quotient/cutoff data and the direct N018 fifth-stage proof.
"""
from pathlib import Path
from collections import Counter
import gzip,json,time
from flint import fmpq,fmpq_poly,fmpq_mat

HERE=Path(__file__).resolve().parent
ZERO=fmpq_poly([]);ONE=fmpq_poly([1]);D=fmpq_poly([0,1])


def parse(p):return fmpq_poly([fmpq(p.get(str(i),'0')) for i in range(max(map(int,p),default=-1)+1)])
def vector(v):return {int(j):parse(p) for j,p in v.items()}
def length(w):return sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))


def add(x,y,c):
    for j,p in y.items():
        v=x.get(j,ZERO)+c*p
        if v:x[j]=v
        else:x.pop(j,None)


def linear(polynomials,rows):
    out={}
    for p,row in zip(polynomials,rows):add(out,row,p)
    return out


def intersection(sourceGT,sourceAmbient,cert):
    columns=cert['column_order'];selected=cert['selected_columns'];n=len(columns)
    assert selected==columns[-len(selected):]
    inv={j:i for i,j in enumerate(columns)}
    gt=[{inv[j]:p for j,p in row.items()} for row in sourceGT]
    H=[vector(row) for row in cert['full_Hermite_rows']]
    assert len(H)==n
    for j,row in enumerate(H):assert min(row)==j and row[j].leading_coefficient()==1
    for source in gt:
        row=dict(source)
        while row:
            j=min(row);q,r=divmod(row[j],H[j][j]);assert not r
            add(row,H[j],-q)
    leaves=[]
    for x,y in zip(gt,sourceAmbient):
        z=dict(x);z.update({j+n:p for j,p in y.items()});leaves.append(z)
    nodes=cert['straight_line_program'];finals=cert['final_nodes'];uses=Counter(finals)
    for node in nodes:
        if 'input_row' not in node:
            uses[node['a']]+=1
            if node['b'] is not None:uses[node['b']]+=1
    cache={}
    for i,node in enumerate(nodes):
        if 'input_row' in node:cache[i]=leaves[node['input_row']]
        else:
            a,b=node['a'],node['b'];assert a<i and (b is None or b<i)
            out=linear([parse(node['p'])],[cache[a]])
            if b is not None:add(out,cache[b],parse(node['q']))
            cache[i]=out
            for j in [a,b]:
                if j is not None:
                    uses[j]-=1
                    if not uses[j]:del cache[j]
    outGT=[vector(row) for row in cert['output_GT']]
    outAmbient=[vector(row) for row in cert['output_ambient']]
    for j,idx,x,y in zip(selected,finals,outGT,outAmbient):
        row=cache[idx]
        assert {k:p for k,p in row.items() if k<n}==H[inv[j]]
        assert {columns[k]:p for k,p in row.items() if k<n}==x
        assert {k-n:p for k,p in row.items() if k>=n}==y
        assert not set(x)-set(selected)
    return outGT,outAmbient


def profile_check(record,keys):
    vectors=[vector(v) for v in record['basis_vectors']]
    top=[parse(p) for p in record['top_numerators']];den=parse(record['top_denominator'])
    n=len(vectors);H=[max((v.get(z,ZERO).degree() for v in vectors),default=-1) for z in range(len(keys))]
    top_functions=[[p[i] for p in top] for i in range(max(p.degree() for p in top)+1)]
    coefs={(z,i):[v.get(z,ZERO)[i] for v in vectors] for z,h in enumerate(H) for i in range(h+1)}
    def rank(rows):return fmpq_mat(rows).rank() if rows else 0
    def viable(rows):return rank(rows+top_functions)>rank(rows)
    def bounded(z,b):return [coefs[z,i] for i in range(max(0,b+1),H[z]+1)]
    least=vector(record['lexicographic_candidate']['ambient_coordinates'])
    profile=[least.get(z,ZERO).degree() for z in range(len(keys))]
    assert profile==record['lexicographic_profile']
    coefficients=[fmpq_poly([fmpq(x)]) for x in record['lexicographic_candidate']['coefficient_vector']]
    assert linear(coefficients,vectors)==least
    current=sum((a*p for a,p in zip(coefficients,top)),ZERO)
    assert current.leading_coefficient()==den.leading_coefficient()
    assert den.degree()-current.degree()==record['lexicographic_candidate']['scaling']
    lengths=[tuple(sorted((length(a),length(b)),reverse=True)) for a,b in keys]
    extension=sorted(range(len(keys)),key=lambda z:(-sum(lengths[z]),-lengths[z][0],z))
    equations=[]
    for z in extension:
        if profile[z]>=0:assert not viable(equations+bounded(z,profile[z]-1))
        equations+=bounded(z,profile[z]);assert viable(equations)
    assert n-rank(equations)==record['lexicographic_minimizing_dimension']==1
    failures={}
    for convention in ['factor_product','length_strata']:
        def le(a,b):return a==b or length(a)>length(b)
        def less(x,z):
            if convention=='length_strata':
                return lengths[x][0]>=lengths[z][0] and lengths[x][1]>=lengths[z][1] and lengths[x]!=lengths[z]
            a,b=keys[x];c,d=keys[z]
            return x!=z and ((le(a,c) and le(b,d)) or (le(b,c) and le(a,d)))
        bad=[]
        for z,cap in enumerate(profile):
            if cap<0:continue
            eq=bounded(z,cap-1)
            for x in range(len(keys)):
                if less(x,z):eq+=bounded(x,profile[x])
            if viable(eq):bad.append(z)
        assert (not bad)==record['global_minimum_exists']
        failures[convention]=bad
    if not record['global_minimum_exists']:
        witness=record['length_stratum_failure_witness'];z=witness['coordinate'];assert z==263
        y=vector(witness['ambient_coordinates'])
        c=[fmpq_poly([fmpq(x)]) for x in witness['coefficient_vector']]
        assert y==linear(c,vectors)
        assert y.get(z,ZERO).degree()<profile[z]
        assert z in failures['length_strata'] and z in failures['factor_product']
        for x in range(len(keys)):
            if lengths[x][0]>=lengths[z][0] and lengths[x][1]>=lengths[z][1] and lengths[x]!=lengths[z]:
                assert y.get(x,ZERO).degree()<=profile[x]
    return {k:len(v) for k,v in failures.items()}


def main():
    started=time.time()
    with gzip.open(HERE/'polynomial_order_gt_hermite.json.gz','rt') as f:source=json.load(f)
    keys=[(tuple(a),tuple(b)) for a,b in source['ambient_coordinates']]
    sourceGT=[vector(row['gt_numerators']) for row in source['rows'][85:]]
    sourceAmbient=[vector(row['ambient_coordinates']) for row in source['rows'][85:]]
    with gzip.open(HERE/'bar_fixed_theta_order.json.gz','rt') as f:isolation=json.load(f)
    blockGT,blockAmbient=intersection(sourceGT,sourceAmbient,isolation)
    records=json.loads((HERE/'bar_fixed_theta_stages.json').read_text())['stages']
    results=[]
    for i,record in enumerate(records,1):
        with gzip.open(HERE/f'bar_fixed_theta_stage_{i:02d}_order.json.gz','rt') as f:cert=json.load(f)
        GT,ambient=intersection(blockGT,blockAmbient,cert)
        assert cert['selected_columns']==record['allowed_GT_coordinates']
        # Reconstruct the finite-space vectors from their actual rows.
        kernel=[parse(p) for p in record['kernel_row_coefficients']]
        complement=[[parse(p) for p in row] for row in record['finite_complement_row_coefficients']]
        t=linear(kernel,ambient);B=record['cutoff_B']
        space=[linear(c,ambient) for c in complement]+[linear([D**j],[t]) for j in range(B+1)]
        assert space==[vector(v) for v in record['basis_vectors']]
        assert B==max([0]+[p.degree()-t[z].degree() for y in space[:len(complement)] for z,p in y.items() if z in t])
        failures=profile_check(record,keys)
        results.append({'stage':i,'actual_module_rank':len(GT),
                        'global_minimum_exists':record['global_minimum_exists'],
                        'independent_failure_counts':failures})
        print(json.dumps(results[-1]),flush=True)
    result={'status':'PASS','scope':'Certificate-only actual intersections and separate matrix-rank degree comparisons; same author.',
            'stages':results,'seconds':time.time()-started}
    (HERE/'bar_fixed_theta_independent_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','seconds':time.time()-started}),flush=True)


if __name__=='__main__':main()
