"""Map the certified actual Q[D] order basis into the exact rank-four GT models.

Each GT matrix coordinate has one common polynomial denominator across
all words.  Straight-line evaluation therefore uses polynomials only.
This is preparatory exact data for a separately chosen bar-fixed variant.
"""
from pathlib import Path
from collections import Counter
import json,gzip,time
import sympy as s
from flint import fmpq,fmpq_poly

HERE=Path(__file__).resolve().parent
D=s.Symbol('D');ZERO=fmpq_poly([]);ONE=fmpq_poly([1])


def fp(expr):
    p=s.Poly(expr,D)
    return fmpq_poly([fmpq(str(p.nth(i))) for i in range(p.degree()+1)]) if p else ZERO


def parse(poly):
    return fmpq_poly([fmpq(poly.get(str(i),'0'))
                      for i in range(max(map(int,poly),default=-1)+1)])


def serial(p):return {str(i):str(c) for i,c in enumerate(p.coeffs()) if c}


def quotient(p,q):
    a,r=divmod(p,q);assert not r
    return a


def matmul(A,B):
    n=len(A);out=[[ZERO for j in range(n)] for i in range(n)]
    for i in range(n):
        for k in range(n):
            if not A[i][k]:continue
            for j in range(n):
                if B[k][j]:out[i][j]+=A[i][k]*B[k][j]
    return out


def main():
    started=time.time()
    gt=json.loads((HERE/'rational_gt_rank4_verified.json').read_text())['GT_data']
    meta=json.loads((HERE/'polynomial_order_rank4_verified.json').read_text())
    with gzip.open(HERE/'polynomial_order_rank4_rows.json.gz','rt') as f:cert=json.load(f)
    words=[tuple(w) for w in meta['accepted_words']];L=max(map(len,words))
    word_vectors=[{} for _ in words];denominators=[];labels=[];offset=0
    for name,block in gt.items():
        mats=block['generator_matrices'];n=len(mats[0]);gamma=ONE;fractions=[]
        for M in mats:
            a=[]
            for row in M:
                b=[]
                for text in row:
                    p,q=s.fraction(s.cancel(s.sympify(text,locals={'D':D})))
                    p,q=fp(p),fp(q);b.append((p,q))
                    gamma=quotient(gamma*q,gamma.gcd(q))
                    gamma/=gamma.leading_coefficient()
                a.append(b)
            fractions.append(a)
        numerators=[[[p*quotient(gamma,q) for p,q in row] for row in M]
                    for M in fractions]
        unit=[[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
        wm={():unit};arrays=[]
        for w in words:
            if w:wm[w]=matmul(wm[w[:-1]],numerators[w[-1]-1])
            scale=gamma**(L-len(w))
            arrays.append([x*scale for row in wm[w] for x in row])
        for j in range(n*n):
            g=gamma**L
            for v in arrays:
                if v[j]:g=g.gcd(v[j])
                if g.degree()==0:break
            den=quotient(gamma**L,g)
            denominators.append(den)
            for i,v in enumerate(arrays):
                if v[j]:word_vectors[i][offset+j]=quotient(v[j],g)
            labels.append({'module':name,'row_path':block['path_labels'][j//n],
                           'column_path':block['path_labels'][j%n],
                           'matrix_row':j//n,'matrix_column':j%n})
        offset+=n*n
        print(json.dumps({'module':name,'dimension':n,'generator_denominator_degree':gamma.degree(),
                          'seconds':time.time()-started}),flush=True)
    assert offset==114
    nodes=cert['straight_line_program'];finals=[r['slp_node'] for r in cert['rows']]
    uses=Counter(finals)
    for node in nodes:
        if 'word' not in node:
            uses[node['a']]+=1
            if node['b'] is not None:uses[node['b']]+=1
    cache={}
    for i,node in enumerate(nodes):
        if 'word' in node:cache[i]=word_vectors[node['word']]
        else:
            a,b=node['a'],node['b'];p,q=parse(node['p']),parse(node['q'])
            v={j:c*p for j,c in cache[a].items() if c*p}
            if b is not None:
                for j,c in cache[b].items():
                    c=v.get(j,ZERO)+q*c
                    if c:v[j]=c
                    else:v.pop(j,None)
            cache[i]=v
            for k in [a,b]:
                if k is not None:
                    uses[k]-=1
                    if not uses[k]:del cache[k]
    # The chosen total label order is an explicit variant.  The outer
    # order refines inclusion of dominance lower sets of maximal-weight
    # antichains in faithful dimensions; the tied downset sizes of eps-
    # and tensor31_22 are resolved by their dimensions, 1 before 6.
    outer=['Sprime22','thetaSprime31','eps-','tensor31_22','Sprime31',
           'wedge31','triv22','triv31','eps+']
    rank3=['N2','eps-','N1','eps+']

    def pathkey(path):return (rank3.index(path[0]),0 if path[1]=='-' else 1)
    ascending=sorted(range(114),key=lambda j:(outer.index(labels[j]['module']),
                      pathkey(labels[j]['row_path']),pathkey(labels[j]['column_path'])))
    record={'status':'PASS','scope':'actual polynomial-order basis in N010 GT matrix coordinates',
            'basis_ambient_pivots':[r['pivot'] for r in cert['rows']],
            'coordinate_labels':labels,'coordinate_denominators':[serial(p) for p in denominators],
            'basis_numerators':[{str(j):serial(p) for j,p in cache[idx].items()} for idx in finals],
            'variant_order':{'outer_modules':outer,'rank3_modules':rank3,'rank2_signs':['-','+'],
                             'within_block':'row path first, then column path',
                             'ascending_coordinate_indices':ascending,
                             'source_status':'Explicit additional choice; not attributed to VIII.'},
            'seconds':time.time()-started}
    with gzip.open(HERE/'polynomial_order_gt_coordinates.json.gz','wt') as f:json.dump(record,f)
    print(json.dumps({'status':'PASS','coordinates':114,'basis_rows':len(finals),
                      'maximum_common_denominator_degree':max(p.degree() for p in denominators),
                      'maximum_numerator_degree':max(p.degree() for idx in finals for p in cache[idx].values()),
                      'seconds':time.time()-started}),flush=True)


if __name__=='__main__':main()
