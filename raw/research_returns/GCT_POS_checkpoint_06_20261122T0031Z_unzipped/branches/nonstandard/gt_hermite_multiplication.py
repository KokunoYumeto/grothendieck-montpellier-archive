"""Full multiplication table of the actual rank-four GT-Hermite order basis.

This is a new, explicit maximal-scaling selection rule, not VIII's
ambient least-degree rule.  The 114-element basis already has a complete
actual-order certificate.  Products are computed in its faithful nine
GT matrix blocks, then divided by the polynomial Hermite pivots.  Every
division is exact.  Associativity is inherited from the faithful matrix
algebra; it is not inferred from numerical samples.
"""
from pathlib import Path
from math import comb
from collections import Counter
import gzip,json,time
from flint import fmpq,fmpq_poly

HERE=Path(__file__).resolve().parent
ZERO=fmpq_poly([]);ONE=fmpq_poly([1]);D=fmpq_poly([0,1])


def parse(p):return fmpq_poly([fmpq(p.get(str(i),'0')) for i in range(max(map(int,p),default=-1)+1)])
def vector(v):return {int(j):parse(p) for j,p in v.items()}
def sp(p):return {str(i):str(c) for i,c in enumerate(p.coeffs()) if c}
def sv(v):return {str(j):sp(p) for j,p in v.items() if p}


def exact(p,q):
    a,r=divmod(p,q);assert not r
    return a


def axpy(x,y,c):
    for j,p in y.items():
        v=x.get(j,ZERO)+c*p
        if v:x[j]=v
        else:x.pop(j,None)


def signed_test(p,epsilon=0):
    power=0
    while not p(4):p=exact(p,D-4);power+=1
    sign=1 if p.leading_coefficient()>0 else -1;p*=sign
    m=p.degree();coefs=[fmpq(0) for _ in range(2*m+epsilon+1)]
    for k,c in enumerate(p.coeffs()):
        if not c:continue
        for j in range(2*k+epsilon+1):coefs[m-k+j]+=c*comb(2*k+epsilon,j)
    assert coefs==list(reversed(coefs))
    return {'sign':sign,'v_minus_inverse_power':2*power,
            'remaining_delta_power':epsilon,'remaining_D_polynomial':sp(p),
            'nonnegative':all(c>=0 for c in coefs),
            'unimodal_on_q_lattice':all(coefs[j]<=coefs[j+1] for j in range(len(coefs)//2)),
            'q_lattice_coefficients':[str(c) for c in coefs]}


def main():
    started=time.time()
    with gzip.open(HERE/'polynomial_order_gt_hermite.json.gz','rt') as f:data=json.load(f)
    labels=data['coordinate_labels'];den=[parse(p) for p in data['coordinate_denominators']]
    Delta=ONE
    for d in den:
        Delta=exact(Delta*d,Delta.gcd(d));Delta/=Delta.leading_coefficient()
    rows=[{j:p*exact(Delta,den[j]) for j,p in vector(row['gt_numerators']).items()}
          for row in data['rows']]
    assert len(rows)==114
    for i,row in enumerate(rows):
        assert min(row)==i
        # Intrinsic Hermite remainder condition in the rational GT coordinates.
        for j,p in row.items():
            if j>i:assert p.degree()<rows[j][j].degree()
    assert vector(data['rows'][0]['ambient_coordinates'])=={0:ONE}
    index={(label['module'],label['matrix_row'],label['matrix_column']):j for j,label in enumerate(labels)}
    products={}
    for i,a in enumerate(labels):
        for j,b in enumerate(labels):
            if a['module']==b['module'] and a['matrix_column']==b['matrix_row']:
                products[i,j]=index[a['module'],a['matrix_row'],b['matrix_column']]

    def multiply(A,B):
        z={}
        for i,p in A.items():
            for j,q in B.items():
                k=products.get((i,j))
                if k is not None:
                    r=z.get(k,ZERO)+p*q
                    if r:z[k]=r
                    else:z.pop(k,None)
        # Both input vectors use denominator Delta.  The order's closure
        # forces the product into that same denominator, verified here.
        return {j:exact(p,Delta) for j,p in z.items()}

    def coordinates(z):
        z=dict(z);out={}
        while z:
            i=min(z);q=exact(z[i],rows[i][i]);out[i]=q
            axpy(z,rows[i],-q)
        return out

    table=[];degree_counts=Counter();nonzero=0;zero_products=0
    distinct={};bad_positive=[];bad_unimodal=[]
    for i,A in enumerate(rows):
        block=[]
        for j,B in enumerate(rows):
            result=coordinates(multiply(A,B))
            if i==0:assert result=={j:ONE}
            if j==0:assert result=={i:ONE}
            if not result:zero_products+=1
            block.append(sv(result));nonzero+=len(result)
            for k,p in result.items():
                degree_counts[p.degree()]+=1
                key=tuple(str(c) for c in p.coeffs())
                if key not in distinct:
                    test=signed_test(p);distinct[key]=test
                    if not test['nonnegative'] and len(bad_positive)<20:
                        bad_positive.append({'left':i,'right':j,'output':k,'polynomial':sp(p),'test':test})
                    if not test['unimodal_on_q_lattice'] and len(bad_unimodal)<20:
                        bad_unimodal.append({'left':i,'right':j,'output':k,'polynomial':sp(p),'test':test})
        table.append(block)
        if (i+1)%10==0:
            print(json.dumps({'left_basis_rows':i+1,'nonzero_constants':nonzero,
                              'distinct_polynomials':len(distinct),'seconds':time.time()-started}),flush=True)
    ambient_bad=[];ambient_support=0
    def length(w):return sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))
    for i,row in enumerate(data['rows']):
        for z,p in vector(row['ambient_coordinates']).items():
            ambient_support+=1
            epsilon=sum(length(w) for w in data['ambient_coordinates'][z])%2
            test=signed_test(p,epsilon)
            if (not test['nonnegative'] or not test['unimodal_on_q_lattice']) and len(ambient_bad)<20:
                ambient_bad.append({'basis_row':i,'coordinate':z,'polynomial':sp(p),'test':test})
    metadata={'status':'PASS','scope':'Actual Q[D]-basis chosen by maximal current scaling / GT-Hermite reduction; not VIII E(4).',
              'basis_size':114,'products':114**2,'structure_constant_slots':114**3,
              'nonzero_structure_constants':nonzero,'zero_products':zero_products,
              'distinct_nonzero_polynomials':len(distinct),'degree_counts':dict(degree_counts),
              'nonnegative_distinct_after_forced_factor':sum(t['nonnegative'] for t in distinct.values()),
              'unimodal_distinct_after_forced_factor':sum(t['unimodal_on_q_lattice'] for t in distinct.values()),
              'first_signed_positivity_failures':bad_positive,'first_unimodality_failures':bad_unimodal,
              'ambient_nonzero_coefficients':ambient_support,'first_ambient_failures':ambient_bad,
              'identity_basis_index':0,
              'scaling_exponents':[den[i].degree()-parse(data['rows'][i]['gt_numerators'][str(i)]).degree() for i in range(114)],
              'seconds':time.time()-started}
    with gzip.open(HERE/'gt_hermite_multiplication_table.json.gz','wt') as f:
        json.dump({'basis_labels':labels,'multiplication':table},f)
    (HERE/'gt_hermite_multiplication_verified.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps({k:v for k,v in metadata.items() if k not in ['first_signed_positivity_failures','first_unimodality_failures','first_ambient_failures','scaling_exponents']},indent=2),flush=True)


if __name__=='__main__':main()
