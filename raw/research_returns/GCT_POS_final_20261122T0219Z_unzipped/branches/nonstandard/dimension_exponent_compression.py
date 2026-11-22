"""N021: exact exponent-compression mechanism and source degree metadata.

This does not optimize dimension rings or rerun the settled rank-three
dimension tables.  It implements the integer-minor construction, checks
a dependent-row example, and compresses a two-label associative table
whose two extra-pair exponents start arbitrarily far from the origin.
"""
from pathlib import Path
from collections import defaultdict
import hashlib,itertools,json,time
import sympy as sp

HERE=Path(__file__).resolve().parent


def compress_integer_system(rows,rhs,known,degree_bound):
    n=len(known);m=len(rows)
    assert all(sum(abs(x) for x in row)<=4 for row in rows)
    assert all(abs(x)<=4*degree_bound for x in rhs)
    A=sp.Matrix(rows) if m else sp.zeros(0,n)
    b=sp.Matrix(m,1,rhs);old=sp.Matrix(known)
    assert A*old==b
    independent=list(A.T.rref()[1]);r=len(independent)
    bound=n*(degree_bound+1)*4**n if n else degree_bound
    if not r:
        new=sp.zeros(n,1);pivots=[];det=1
    else:
        R=A.extract(independent,range(n))
        pivots=list(R.rref()[1]);free=[j for j in range(n) if j not in pivots]
        H=R.extract(range(r),pivots);det=int(H.det());modulus=abs(det)
        assert 0<modulus<=4**r
        assert all(abs(int(x))<=4**(r-1) for x in H.adjugate())
        new=sp.zeros(n,1)
        for j in free:new[j]=int(old[j])%modulus
        residual=b.extract(independent,[0])-R.extract(range(r),free)*new.extract(free,[0])
        solved=H.inv()*residual
        assert all(x.q==1 for x in solved)
        for j,x in zip(pivots,solved):new[j]=x
    assert A*new==b and all(abs(x)<=bound for x in new)
    return {'rows':rows,'rhs':rhs,'original':[int(x) for x in old],
            'compressed':[int(x) for x in new],'rank':r,
            'independent_rows':independent,'pivot_columns':pivots,
            'signed_minor_determinant':det,'proved_bound':bound}


def check_matching_example():
    n=2;slots=list(itertools.product(range(n),repeat=3))
    # The true unital ring has x^2=1+x.  Every replacement x^2=1+f(q)x
    # is associative.  Add two cancelling pairs at exponents +/-N.
    true={(0,0,0):{0:1},(0,1,1):{0:1},(1,0,1):{0:1},
          (1,1,0):{0:1},(1,1,1):{0:1}}
    old=[10**40,-10**40];budget=2
    tokens={slot:[] for slot in slots}
    for slot,p in true.items():
        for exponent,coefficient in p.items():
            tokens[slot]+=[((0,)*budget,exponent)]*abs(coefficient)
    for t in range(budget):
        coeff=tuple(int(i==t) for i in range(budget))
        tokens[1,1,1]+=[(coeff,0)]*2
    def plus(a,b):return tuple(x+y for x,y in zip(a[0],b[0])),a[1]+b[1]
    def value(a,x):return a[1]+sum(c*z for c,z in zip(a[0],x))
    equations=set();matching_count=0
    def match(left,right):
        nonlocal matching_count
        L=defaultdict(list);R=defaultdict(list)
        for a in left:L[value(a,old)].append(a)
        for a in right:R[value(a,old)].append(a)
        assert L.keys()==R.keys()
        for exponent in L:
            assert len(L[exponent])==len(R[exponent])
            for a,b in zip(L[exponent],R[exponent]):
                row=tuple(x-y for x,y in zip(a[0],b[0]));rhs=b[1]-a[1]
                assert sum(abs(x) for x in row)<=4
                if any(row) or rhs:equations.add((row,rhs))
                matching_count+=1
    for i,j,k,m in itertools.product(range(n),repeat=4):
        left=[plus(a,b) for ell in range(n) for a in tokens[i,j,ell] for b in tokens[ell,k,m]]
        right=[plus(a,b) for ell in range(n) for a in tokens[j,k,ell] for b in tokens[i,ell,m]]
        match(left,right)
    for slot in slots:
        match(tokens[slot],[(tuple(-x for x in a),-c) for a,c in tokens[slot]])
    eq=sorted(equations)
    certificate=compress_integer_system([list(row) for row,rhs in eq],[rhs for row,rhs in eq],old,0)
    new=certificate['compressed']
    def table(x):
        result={}
        for slot,items in tokens.items():
            p=defaultdict(int)
            for term in items:p[value(term,x)]+=1
            if p:result[slot]=dict(p)
        return result
    def product_poly(p,q):
        out=defaultdict(int)
        for e,a in p.items():
            for f,b in q.items():out[e+f]+=a*b
        return dict(out)
    def check_table(tab):
        for i,j,k,m in itertools.product(range(n),repeat=4):
            left=defaultdict(int);right=defaultdict(int)
            for ell in range(n):
                for e,c in product_poly(tab.get((i,j,ell),{}),tab.get((ell,k,m),{})).items():left[e]+=c
                for e,c in product_poly(tab.get((j,k,ell),{}),tab.get((i,ell,m),{})).items():right[e]+=c
            assert left==right
        for slot,p in tab.items():assert p=={-e:c for e,c in p.items()}
        for i in range(n):
            for j in range(n):assert tab.get((0,i,j),{})==tab.get((i,0,j),{})==({0:1} if i==j else {})
        mass=sum(sum(p.values()) for p in tab.values())
        true_mass=sum(sum(abs(c) for c in p.values()) for p in true.values())
        assert (mass-true_mass)//2==budget
    before=table(old);after=table(new);check_table(before);check_table(after)
    assert new==[0,0] and after[1,1,1]=={0:5}
    certificate.update({'matching_equations':len(eq),'matched_monomial_pairs':matching_count,
                        'old_pair_score':2,'new_pair_score':2,
                        'compressed_relation':'x^2=1+5x','bar_and_unit_preserved':True})
    return certificate


def rank_three_metadata():
    path=HERE/'dependencies/e3_constants.json';raw=path.read_bytes();data=json.loads(raw)
    v=sp.Symbol('v');values=[]
    for row in data:
        coefficients=defaultdict(int)
        for monomial in sp.expand(sp.sympify(row['c'],locals={'v':v})).as_ordered_terms():
            coefficient,exponent=monomial.as_coeff_exponent(v)
            assert coefficient.is_Integer and exponent.is_Integer and int(exponent)%2==0
            coefficients[int(exponent)//2]+=int(coefficient)
        values.append({'slot':[row['b'],row['bp'],row['bpp']],
                       'absolute_mass':sum(abs(c) for c in coefficients.values()),
                       'max_abs_q_exponent':max((abs(e) for e,c in coefficients.items() if c),default=0)})
    d0=max(v['max_abs_q_exponent'] for v in values);M=max(v['absolute_mass'] for v in values)
    assert len(values)==132 and d0==5 and M==576
    assert sum(v['absolute_mass'] for v in values)==4443
    general_budget=7276;unimodal_budget=9040
    K=general_budget*(d0+1)*4**general_budget
    return {'source_sha256':hashlib.sha256(raw).hexdigest(),'nonzero_constants':132,
            'true_absolute_mass':4443,'max_constant_absolute_mass':M,'q_degree':d0,
            'inherited_verified_general_pair_upper_bound':general_budget,
            'general_degree_bound':'43656*4^7276','general_degree_bound_bit_length':K.bit_length(),
            'inherited_verified_unimodal_pair_upper_bound':unimodal_budget,
            'unimodal_degree_bound':(M+2*unimodal_budget-1)//2,'per_constant_metadata':values}


def main():
    started=time.time();example=check_matching_example()
    distant=10**40
    dependent=compress_integer_system([[2,-1,1],[0,1,-1],[2,0,0]],[3,1,4],[2,distant+1,distant],1)
    assert dependent['compressed']==[2,1,0] and dependent['rank']==2
    metadata=rank_three_metadata()
    assert metadata['general_degree_bound_bit_length']==14568 and metadata['unimodal_degree_bound']==9327
    result={'status':'PASS_MECHANISM_NOT_GLOBAL_OPTIMIZATION','matching_example':example,
            'dependent_row_example':dependent,'rank_three':metadata,'seconds':time.time()-started}
    (HERE/'dimension_exponent_compression_verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'pair_example':example['compressed'],
                      'dependent_example':dependent['compressed'],
                      'degree_bound':metadata['general_degree_bound'],'bound_bits':14568,
                      'unimodal_bound':9327,'seconds':result['seconds']},indent=2),flush=True)


if __name__=='__main__':main()
