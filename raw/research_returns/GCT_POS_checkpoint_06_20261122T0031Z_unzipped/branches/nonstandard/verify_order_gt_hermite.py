"""Verify the actual GT coordinate map and its polynomial Hermite certificate.

This does not trust the word-to-GT evaluation used by the construction.
Instead it verifies that the supplied map sends 1 to the block identities
and intertwines every right P_i action on all 114 actual order basis rows.
The ambient P_i action is reconstructed in the standard T convention by
the already reviewed N015 verifier.  Polynomial triangular division gives
the actual basis coefficients.  These 343 identities uniquely determine
the map on all words, hence on the whole actual order.

The Hermite straight-line program is replayed jointly in GT and ambient
coordinates, and every original basis row is divided by the output rows.
Both module containments, and thus unsaturated equality, are verified.
"""
from pathlib import Path
from collections import Counter
import gzip,json,time
import sympy as s
from flint import fmpq,fmpq_poly
import verify_polynomial_order_rank4 as source

HERE=Path(__file__).resolve().parent
ZERO=fmpq_poly([]);ONE=fmpq_poly([1]);D=s.Symbol('D')
parse=source.polynomial;vector=source.vector;axpy=source.axpy


def exact(p,q):
    a,r=divmod(p,q);assert not r
    return a


def fp(expr):
    p=s.Poly(expr,D)
    return fmpq_poly([fmpq(str(p.nth(i))) for i in range(p.degree()+1)]) if p else ZERO


def lcm(a,b):
    p=exact(a*b,a.gcd(b))
    return p/p.leading_coefficient()


def main():
    started=time.time()
    with gzip.open(HERE/'polynomial_order_rank4_rows.json.gz','rt') as f:actual=json.load(f)
    with gzip.open(HERE/'polynomial_order_gt_coordinates.json.gz','rt') as f:gt=json.load(f)
    with gzip.open(HERE/'polynomial_order_gt_hermite.json.gz','rt') as f:cert=json.load(f)
    models=json.loads((HERE/'rational_gt_rank4_verified.json').read_text())['GT_data']
    keys=[(tuple(a),tuple(b)) for a,b in actual['coordinates']]
    rows=[vector(row['vector']) for row in actual['rows']]
    pivot_row={min(row):i for i,row in enumerate(rows)}
    assert len(rows)==len(pivot_row)==114
    ops=source.make_operators(keys)

    def coordinates(x):
        x=dict(x);out={}
        while x:
            j=min(x);i=pivot_row[j]
            q=exact(x[j],rows[i][j]);out[i]=q
            axpy(x,rows[i],-q)
        return out

    den=[parse(p) for p in gt['coordinate_denominators']]
    Delta=ONE
    for p in den:Delta=lcm(Delta,p)
    numerators=[{j:p*exact(Delta,den[j]) for j,p in vector(v).items()}
                for v in gt['basis_numerators']]
    labels=gt['coordinate_labels'];index={}
    for j,label in enumerate(labels):index[label['module'],label['matrix_row'],label['matrix_column']]=j
    generator_fractions={};gamma=ONE
    for name,model in models.items():
        for si,M in enumerate(model['generator_matrices']):
            for i,row in enumerate(M):
                for j,text in enumerate(row):
                    p,q=s.fraction(s.cancel(s.sympify(text,locals={'D':D})))
                    p,q=fp(p),fp(q);generator_fractions[name,si,i,j]=(p,q)
                    gamma=lcm(gamma,q)
    right=[[] for _ in range(3)]
    for si in range(3):
        for label in labels:
            name,a,b=label['module'],label['matrix_row'],label['matrix_column']
            n=len(models[name]['path_labels']);out={}
            for j in range(n):
                p,q=generator_fractions[name,si,b,j]
                if p:out[index[name,a,j]]=p*exact(gamma,q)
            right[si].append(out)

    def mapped(coefficients):
        out={}
        for j,c in coefficients.items():axpy(out,numerators[j],c)
        return out

    one={keys.index((source.h.e,source.h.e)):ONE}
    image=mapped(coordinates(one))
    expected={j:Delta for j,label in enumerate(labels) if label['matrix_row']==label['matrix_column']}
    assert image==expected
    for i,row in enumerate(rows):
        for si in range(3):
            lhs={j:p*gamma for j,p in mapped(coordinates(source.step(row,ops[si]))).items()}
            rhs=source.step(numerators[i],right[si])
            assert lhs==rhs,(i,si)
    print(json.dumps({'GT_map':'PASS','identity_checks':1,'basis_action_checks':342,
                      'global_coordinate_denominator_degree':Delta.degree(),
                      'global_generator_denominator_degree':gamma.degree(),
                      'seconds':time.time()-started}),flush=True)

    order=list(reversed(gt['variant_order']['ascending_coordinate_indices']))
    inverse={j:i for i,j in enumerate(order)}
    source_GT=[{inverse[j]:p for j,p in vector(v).items()} for v in gt['basis_numerators']]
    assert [labels[j] for j in order]==cert['coordinate_labels']
    assert [gt['coordinate_denominators'][j] for j in order]==cert['coordinate_denominators']
    leaves=[]
    for x,y in zip(source_GT,rows):
        z=dict(x);z.update({j+114:p for j,p in y.items()});leaves.append(z)
    nodes=cert['straight_line_program'];finals=[r['slp_node'] for r in cert['rows']]
    uses=Counter(finals)
    for node in nodes:
        if 'basis_row' not in node:
            uses[node['a']]+=1
            if node['b'] is not None:uses[node['b']]+=1
    cache={}
    for i,node in enumerate(nodes):
        if 'basis_row' in node:cache[i]=leaves[node['basis_row']]
        else:
            a,b=node['a'],node['b'];assert a<i and (b is None or b<i)
            cache[i]=source.combination(cache[a],parse(node['p']),{} if b is None else cache[b],parse(node['q']))
            for k in [a,b]:
                if k is not None:
                    uses[k]-=1
                    if not uses[k]:del cache[k]
    hermite=[]
    for j,row in enumerate(cert['rows']):
        v=cache[row['slp_node']]
        x={k:p for k,p in v.items() if k<114}
        y={k-114:p for k,p in v.items() if k>=114}
        assert x==vector(row['gt_numerators']) and y==vector(row['ambient_coordinates'])
        assert min(x)==j and x[j].leading_coefficient()==1
        hermite.append(x)
    for row in source_GT:
        x=dict(row)
        while x:
            j=min(x);q=exact(x[j],hermite[j][j]);axpy(x,hermite[j],-q)
    result={'status':'PASS','scope':'Exact map-action verification and unsaturated Hermite equality; same author, separate algorithm.',
            'basis_rows':114,'GT_identity_checks':1,'GT_basis_action_checks':342,
            'Hermite_straight_line_nodes':len(nodes),'original_rows_contained':114,
            'seconds':time.time()-started}
    (HERE/'order_gt_hermite_verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
