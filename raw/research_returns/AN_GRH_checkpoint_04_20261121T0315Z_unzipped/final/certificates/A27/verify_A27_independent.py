#!/usr/bin/env python3
"""Independent finite certificate for the written A27 all-extension argument.

Imports no census or probe implementation. Uses brute-force affine y-solution
enumeration, a quartic companion matrix, exact Bareiss determinants, complete
trial division, and direct multiplicative-order iteration.
The all-extension induction and the Frobenius-block proof are written proofs.
"""
import json
from pathlib import Path

def ff_product(a,b,polynomial):
    raw=0
    for i in range(b.bit_length()):
        if (b>>i)&1:raw^=a<<i
    degree=polynomial.bit_length()-1
    while raw.bit_length()-1>=degree:
        raw^=polynomial<<(raw.bit_length()-1-degree)
    return raw

def affine_points(n,polynomial,u):
    q=2**n
    pairs=[]
    for x in range(1,q):
        inv=next(z for z in range(1,q) if ff_product(x,z,polynomial)==1)
        cube=ff_product(ff_product(x,x,polynomial),x,polynomial)
        rhs=ff_product(u,cube,polynomial)^x^ff_product(u,inv,polynomial)
        for y in range(q):
            if ff_product(y,y,polynomial)^y==rhs:
                pairs.append([x,y])
    return {'field_degree':n,'modulus_bits':polynomial,'u_bits':u,
            'affine_pairs':pairs,'ramified_points':['x=0','x=infinity'],
            'total_points':len(pairs)+2}

def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def det_bareiss(matrix):
    a=[row[:] for row in matrix]
    n=len(a); denominator=1; sign=1
    for k in range(n-1):
        if not a[k][k]:
            pivot=next((i for i in range(k+1,n) if a[i][k]),None)
            if pivot is None:return 0
            a[k],a[pivot]=a[pivot],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%denominator==0
                a[i][j]=num//denominator
        for i in range(k+1,n):a[i][k]=0
        denominator=pivot
    return sign*a[-1][-1]

def factor_integer(n):
    original=n; answer={}; divisor=2
    while divisor*divisor<=n:
        exponent=0
        while n%divisor==0:
            n//=divisor; exponent+=1
        if exponent:answer[divisor]=exponent
        divisor+=1
    if n>1:answer[n]=answer.get(n,0)+1
    product=1
    for p,e in answer.items():
        assert p>=2 and all(p%d for d in range(2,int(p**0.5)+1))
        product*=p**e
    assert product==original
    return answer

def order_two(p):
    assert p%2
    value=1
    for d in range(1,p):
        value=(value*2)%p
        if value==1:return d
    raise AssertionError('order not found')

def polynomial_product(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def main():
    fields=[affine_points(2,0b111,2),affine_points(4,0b10011,6)]
    assert [r['total_points'] for r in fields]==[6,28]
    assert ff_product(6,6,0b10011)^6^1==0
    a1=fields[0]['total_points']-5
    twice_a2=a1*a1-(17-fields[1]['total_points'])
    assert twice_a2%2==0
    polynomial=[1,a1,twice_a2//2,4*a1,16]
    assert polynomial==[1,1,6,4,16]
    assert polynomial_product([1,-1,4],[1,2,4])==polynomial
    assert polynomial_product([1,-2],[1,2,4])==[1,0,0,-8]
    # Characteristic polynomial T^4+T^3+6T^2+4T+16.
    F=[[0,0,0,-16],[1,0,0,-4],[0,1,0,-6],[0,0,1,-1]]
    identity=[[int(i==j) for j in range(4)] for i in range(4)]
    power=[row[:] for row in identity]
    rows=[]
    expected_N=[6,28,60,256,996,3976,16764,66016,260340]
    expected_max=[1,9,19,13,1,81,1,13,361]
    for m in range(1,10):
        power=multiply(power,F)
        N=4**m+1-sum(power[i][i] for i in range(4))
        cardinality=det_bareiss([[identity[i][j]-power[i][j] for j in range(4)] for i in range(4)])
        fac=factor_integer(cardinality)
        all_orders={p:order_two(p) for p in fac if p>2}
        eligible=[]
        for p,order in all_orders.items():
            if order==p-1:
                upper=p**min(4,fac[p])
                assert upper<N
                eligible.append({'prime':p,'order_of_2':order,'valuation':fac[p],'quotient_size_upper_bound':upper})
        upper=max([1]+[x['quotient_size_upper_bound'] for x in eligible])
        assert N==expected_N[m-1] and upper==expected_max[m-1]
        rows.append({'m':m,'Q':4**m,'curve_points':N,'jacobian_points':cardinality,
                     'complete_factorization':fac,'orders_of_2_at_odd_factors':all_orders,
                     'eligible':eligible,'uniform_upper_bound':upper})
    assert 31**4 < 4**10+1-4*2**10
    assert 34**4 < 2*31**4
    result={'result':'PASS','model':'y^2+y=u*x^3+x+u/x over F4, u^2+u+1=0',
            'independence':'No imports from the census or exploratory probes. Direct y-solutions and quartic companion determinants replace trace tests and two quadratic trace recurrences.',
            'scope':'Exact finite inputs for the written all-extension proof. No formal proof assistant and no exhaustive cover test.',
            'fields':fields,'weil_polynomial':polynomial,'rows':rows,
            'large_m_anchor':{'m':10,'torsion_bound':31**4,'curve_lower_bound':4**10+1-4*2**10},
            'growth_anchor':{'numerator':34**4,'twice_denominator':2*31**4}}
    out=Path(__file__).with_name('A27_INDEPENDENT_CERTIFICATE.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'result':'PASS','counts':[6,28],'verified_small_degrees':[1,9],
                      'large_degree_anchor':10,'output':str(out)}))

if __name__=='__main__':main()
