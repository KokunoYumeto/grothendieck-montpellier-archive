"""Exact multiplication and signed Laurent tests for the N017 four-element block.

The basis is obtained from the actual Hermite rows and independently
compared with a short symbolic 2-by-2 formula.  All 64 structure constants
are computed exactly.  Positivity/unimodality is tested after removing
the maximal (D-4) power; because D=(v+v^-1)^2, that removes an even power
of v-v^-1.  The remaining coefficients are stated in q=v^2, including
every integer q exponent between the endpoints.
"""
from pathlib import Path
import gzip,json,time
import sympy as s

HERE=Path(__file__).resolve().parent
D,q=s.symbols('D q')


def poly(d):return sum(s.Rational(c)*D**int(i) for i,c in d.items())


def main():
    started=time.time()
    with gzip.open(HERE/'polynomial_order_gt_hermite.json.gz','rt') as f:data=json.load(f)
    matrices=[]
    for i in [113,112,111,110]:
        M=s.zeros(2)
        for j,text in data['rows'][i]['gt_numerators'].items():
            j=int(j);label=data['coordinate_labels'][j]
            assert label['module']=='Sprime22'
            M[label['matrix_row'],label['matrix_column']]=s.cancel(poly(text)/poly(data['coordinate_denominators'][j]))
        matrices.append(M)
    A,B,C,E=matrices
    basis=[A,D*B-2*A,D*C-A/2,E+C+B/4]
    e=D*(D-4)**2*(D-2)*(D-1)**2
    a=D**2*e;b=D**3*(D-4)**2*(D-2)**2*(D-1);c=D**3*(D-4)**2*(D-1)**2;k=(D-2)/D**2
    expected=[s.Matrix([[0,0],[0,a]]),s.Matrix([[0,0],[b,0]]),
              s.Matrix([[0,c],[0,0]]),s.Matrix([[e,k*c],[k*b/4,-e]])]
    assert all(all(s.cancel(x-y)==0 for x,y in zip(M,N)) for M,N in zip(basis,expected))
    change=s.Matrix.hstack(*[s.Matrix(list(M)) for M in basis]);inverse=change.inv()
    labels=['X','Y','Z','W'];table=[];unique={};nonzero=0
    for i,M in enumerate(basis):
        for j,N in enumerate(basis):
            coefficients=[s.factor(x) for x in inverse*s.Matrix(list(M*N))]
            assert all(s.cancel(x-y)==0 for x,y in zip(M*N,sum((t*B for t,B in zip(coefficients,basis)),s.zeros(2))))
            table.append({'left':labels[i],'right':labels[j],
                          'coefficients':{label:str(x) for label,x in zip(labels,coefficients) if x}})
            for value in coefficients:
                if not value:continue
                nonzero+=1
                if str(value) in unique:continue
                num,den=s.fraction(value);assert not den.has(D)
                rational,factors=s.factor_list(value,D)
                exponents={str(s.expand(f)):int(n) for f,n in factors}
                assert set(exponents)<=set(['D','D - 4','D - 2','D - 1'])
                assert exponents.get('D',0)>=1 and exponents.get('D - 4',0)==2
                assert 1<=exponents.get('D - 2',0)<=3 and exponents.get('D - 1',0)>=1
                p=s.Poly(num/den,D);power=0
                while p.eval(4)==0:
                    p=p.exquo(s.Poly(D-4,D));power+=1
                sign=s.sign(p.LC());p=p*sign
                degree=p.degree();laurent=s.expand(p.as_expr().subs(D,q+2+1/q))
                shifted=s.Poly(s.expand(laurent*q**degree),q)
                sequence=[shifted.nth(i) for i in range(2*degree+1)]
                symmetric=sequence==list(reversed(sequence))
                positive=all(x>=0 for x in sequence)
                unimodal=all(sequence[i]<=sequence[i+1] for i in range(degree)) and symmetric
                unique[str(value)]={'sign':int(sign),'v_minus_inverse_power':2*power,
                                    'positive_rational_factor':str(abs(rational)),
                                    'D_factor_exponents':exponents,
                                    'remaining_D_polynomial':str(s.factor(p.as_expr())),
                                    'q_exponents':[-degree,degree],
                                    'q_coefficients':[str(x) for x in sequence],
                                    'symmetric':symmetric,'nonnegative':positive,'unimodal_in_q':unimodal}
    # The same signed test on the ambient KL coefficients is more
    # restrictive: it detects explicit nonunimodal residual polynomials.
    minima=json.loads((HERE/'bar_fixed_block_rank4_verified.json').read_text())['variants']['product_paths']
    def length(w):return sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))
    ambient_tests=[]
    for label,minimum in zip(labels,minima):
        failures=[];support=minimum['lexicographic_candidate']['ambient_coordinates']
        for z,terms in support.items():
            z=int(z);pair=data['ambient_coordinates'][z]
            epsilon=sum(length(w) for w in pair)%2
            p=s.Poly(poly(terms),D);power=0
            while p.eval(4)==0:p=p.exquo(s.Poly(D-4,D));power+=1
            sign=s.sign(p.LC());p*=sign;degree=p.degree()
            shifted=s.Poly(s.expand(q**degree*(1+q)**epsilon*p.as_expr().subs(D,q+2+1/q)),q)
            sequence=[shifted.nth(i) for i in range(2*degree+epsilon+1)]
            positive=all(x>=0 for x in sequence)
            symmetric=sequence==list(reversed(sequence))
            unimodal=symmetric and all(sequence[i]<=sequence[i+1] for i in range(len(sequence)//2))
            assert positive and symmetric
            if not unimodal:
                failures.append({'coordinate':z,'permutations_one_based':[[x+1 for x in w] for w in pair],
                                 'sign':int(sign),'v_minus_inverse_power':2*power,
                                 'remaining_delta_power':epsilon,
                                 'remaining_D_polynomial':str(s.factor(p.as_expr())),
                                 'q_coefficients':[str(x) for x in sequence]})
        ambient_tests.append({'basis_element':label,'nonzero_coefficients':len(support),
                              'all_signed_positive':True,'unimodality_failures':failures})
    assert any(f['coordinate']==272 and f['remaining_D_polynomial']=='(D - 2)/2'
               for f in ambient_tests[-1]['unimodality_failures'])
    record={'status':'PASS','scope':'Four-element repaired Sprime22 block only; not full E(4).',
            'basis_labels':labels,'basis_matrices':[[[str(s.factor(x)) for x in row] for row in M.tolist()] for M in basis],
            'multiplication':table,'structure_constants_total':64,'nonzero_structure_constants':nonzero,
            'distinct_nonzero_structure_constants':len(unique),'signed_Laurent_tests':unique,
            'all_nonnegative_after_sign_and_vanishing_factor':all(r['nonnegative'] for r in unique.values()),
            'all_unimodal_in_q_after_sign_and_vanishing_factor':all(r['unimodal_in_q'] for r in unique.values()),
            'ambient_coefficient_tests':ambient_tests,
            'seconds':time.time()-started}
    (HERE/'bar_fixed_block_constants_verified.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k not in ['basis_matrices','multiplication','signed_Laurent_tests','ambient_coefficient_tests']},indent=2),flush=True)
    for row in table:print(row['left']+row['right'],row['coefficients'])
    for value,tests in unique.items():
        if not tests['nonnegative'] or not tests['unimodal_in_q']:print('FAILED_SIGNED_TEST',value,tests)
    print('AMBIENT_UNIMODALITY_FAILURE_COUNTS',
          {r['basis_element']:len(r['unimodality_failures']) for r in ambient_tests})


if __name__=='__main__':main()
