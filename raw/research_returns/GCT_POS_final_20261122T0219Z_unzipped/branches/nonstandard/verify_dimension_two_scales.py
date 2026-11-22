"""Certificate-only replay of N-022, with no constructor imports.

The true trace is parsed directly from the supplied coefficient expressions.
Arithmetic uses Laurent dictionaries.  An explicit product of two matrix
algebras and two scalar algebras checks the entire proposed multiplication.
This is a second arithmetic path by the branch author, not an independent
agent proof review.
"""
from pathlib import Path
from itertools import product
import json,time,sys
import sympy as sp
HERE=Path(__file__).resolve().parent

def add(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,0)+v
    return {k:v for k,v in c.items() if v}

def scale(a,n):return {k:v*n for k,v in a.items() if v*n}

def mul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():c[i+j]=c.get(i+j,0)+x*y
    return {k:v for k,v in c.items() if v}

ONE={0:1};D={-1:1,0:2,1:1};ZERO={}

def dpoly(coeff):
    ans={};power=ONE
    for c in coeff:
        ans=add(ans,scale(power,c));power=mul(power,D)
    return ans

def matmul(a,b):
    return [add(mul(a[2*i],b[j]),mul(a[2*i+1],b[2+j])) for i in (0,1) for j in (0,1)]

def vecadd(a,b):return [add(x,y) for x,y in zip(a,b)]
def vecscale(a,c):return [mul(x,c) for x in a]
def algmul(a,b):return [mul(a[0],b[0]),mul(a[1],b[1])]+matmul(a[2:6],b[2:6])+matmul(a[6:10],b[6:10])

def main():
    started=time.time()
    refined='--refined' in sys.argv
    input_name='dimension_two_scales_refined_verified.json' if refined else 'dimension_two_scales_verified.json'
    cert=json.loads((HERE/input_name).read_text())
    table={(r['input1'],r['input2'],r['output']):dpoly(r['D_coefficients']) for r in cert['table']}
    labels=['mu','Sigma']+['g%d_%s'%(i,x) for i in (1,2) for x in ('1','12','2','21')]
    assert len(table)==132
    v=sp.Symbol('v');true={}
    for row in json.loads((HERE/'dependencies'/'e3_constants.json').read_text()):
        expression=sp.expand(sp.sympify(row['c']))
        result={}
        for term in sp.Add.make_args(expression):
            coefficient,power=term.as_coeff_exponent(v)
            assert power.is_Integer and int(power)%2==0 and coefficient.is_Integer,(row,term)
            e=int(power)//2;result[e]=result.get(e,0)+int(coefficient)
        true[row['b'],row['bp'],row['bpp']]={k:c for k,c in result.items() if c}
    assert len(true)==132
    score=bottom=dim_mass=trace_mass=0
    for key in set(table)|set(true):
        dim=table.get(key,{});tr=true.get(key,{})
        for e in set(dim)|set(tr):
            d,c=dim.get(e,0),tr.get(e,0)
            assert d>=abs(c) and (d-c)%2==0,(key,e,d,c)
            score+=(d-abs(c))//2
            if key[2]=='Sigma':bottom+=(d-abs(c))//2
        assert dim=={-e:c for e,c in dim.items()}
        if key[0]!='mu' and key[1]!='mu':
            dim_mass+=sum(dim.values());trace_mass+=sum(map(abs,tr.values()))
    expected=(4194,3614,12812,4424) if refined else (4196,3616,12816,4424)
    assert (score,bottom,dim_mass,trace_mass)==expected
    for x,y in product(labels,repeat=2):
        if x=='mu' or y=='mu':
            z=y if x=='mu' else x
            assert {k:p for (a,b,k),p in table.items() if (a,b)==(x,y)}=={z:ONE}
    def sigma(x):
        if not x.startswith('g'):return x
        return x[:3]+x[3:].translate(str.maketrans('12','21'))
    def opposite(x):return x[:3]+x[3:][::-1] if x.startswith('g') else x
    for (x,y,z),c in table.items():
        assert table[sigma(x),sigma(y),sigma(z)]==c
        assert table[opposite(y),opposite(x),opposite(z)]==c
    products={(a,b):{k:p for (x,y,k),p in table.items() if (x,y)==(a,b)} for a,b in product(labels,repeat=2)}
    def times(X,Y):
        ans={}
        for a,p in X.items():
            for b,q in Y.items():
                for k,r in products[a,b].items():ans[k]=add(ans.get(k,{}),mul(mul(p,q),r))
        return {k:p for k,p in ans.items() if p}
    for a,b,c in product(labels,repeat=3):
        assert times(products[a,b],{c:ONE})==times({a:ONE},products[b,c]),(a,b,c)
    u=dpoly([-2,1]);h={1:D if refined else u,2:D};character_h={1:u,2:D}
    a=dpoly([2,-3,1]);W=dpoly([-8,7])
    L={1:u if refined else D,2:dpoly([4,-10,3])};G={1:scale(mul(W,a),2),2:mul(W,a)};S=scale(mul(W,mul(a,a)),2)
    identity=[ONE,{}, {},ONE]
    vectors={'mu':[ONE,ONE]+identity+identity,'Sigma':[{},S]+[{} for _ in range(8)]}
    determinants=[]
    for i in (1,2):
        A=[h[i],ONE,{},{}];B=[{}, {},L[i],h[i]]
        matrices={'1':A,'2':B,'12':matmul(A,B),'21':matmul(B,A)}
        # One exact rational evaluation is sufficient for generic independence.
        flat=sp.Matrix([[sum(c*sp.Rational(2)**e for e,c in p.items()) for p in matrices[x]] for x in ('1','12','2','21')])
        det=flat.det();assert det!=0;determinants.append(str(det))
        for x,m in matrices.items():
            character=G[i] if len(x)==1 else mul(character_h[i],G[i])
            vec=[{},character]+[{} for _ in range(8)]
            vec[2+4*(i-1):6+4*(i-1)]=[mul(a,p) for p in m]
            vectors['g%d_%s'%(i,x)]=vec
    for x,y in product(labels,repeat=2):
        rhs=[{} for _ in range(10)]
        for z,c in products[x,y].items():rhs=vecadd(rhs,vecscale(vectors[z],c))
        assert algmul(vectors[x],vectors[y])==rhs,(x,y)
    out={'status':'PASS_CERTIFICATE_AND_MATRIX_REALIZATION','true_source_constants':132,
         'pair_score':score,'bottom_score':bottom,'nonunit_dimension_mass':dim_mass,
         'nonunit_absolute_trace_mass':trace_mass,'associativity_triples':1000,
         'matrix_products':100,'matrix_basis_determinants_at_q2':determinants,
         'bar_dynkin_opposite_symmetries':True,'seconds':time.time()-started}
    output_name='dimension_two_scales_refined_independent_certificate.json' if refined else 'dimension_two_scales_independent_certificate.json'
    (HERE/output_name).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
