"""Certificate-only exact replay for N-024; no constructor imports.

Laurent dictionaries, direct supplied trace expressions, all associativity
triples, and a product of explicit matrix algebras check the four witnesses.
Finite identities used in the all-degree lower-bound proof are also checked;
the proof's arbitrary-support arguments are mathematical, not sampled.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
import json,time
import sympy as sp
HERE=Path(__file__).resolve().parent

def add(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,0)+v
    return {k:v for k,v in c.items() if v}

def scale(a,n):return {k:v*n for k,v in a.items() if v*n}
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():c[i+j]=c.get(i+j,0)+x*y
    return {k:v for k,v in c.items() if v}

def power(a,n):
    out={0:1}
    for _ in range(n):out=mul(out,a)
    return out

def bar(a):return {-k:v for k,v in a.items()}
def positive(a):return all(v>=0 for v in a.values())
def load_poly(a):return {int(k):int(v) for k,v in a.items() if v}
def absolute(a):return {k:abs(v) for k,v in a.items()}
def divisible(a,n):return all(v%n==0 for v in a.values())
def half_difference(a,b):
    out=sub(a,b);assert divisible(out,2)
    return {k:v//2 for k,v in out.items()}

ONE={0:1};D={-1:1,0:2,1:1};u={-1:1,1:1};a=mul(sub(D,ONE),u)
delta=mul(sub(D,ONE),sub(D,scale(ONE,4)))
K2=add(sub(scale(power(D,2),2),scale(D,5)),scale(ONE,4))
H0=add(sub(scale(D,10),power(D,2)),scale(ONE,-8))
R=add(scale(power(D,2),3),scale(D,2))
T=absolute(mul(delta,power(u,2)))
Cmin=add(T,{-4:2,4:2})

def matmul(A,B):
    return [add(mul(A[2*i],B[j]),mul(A[2*i+1],B[2+j])) for i in (0,1) for j in (0,1)]
def vecadd(A,B):return [add(x,y) for x,y in zip(A,B)]
def vecscale(A,b):return [mul(x,b) for x in A]
def algmul(A,B):return [mul(A[0],B[0]),mul(A[1],B[1])]+matmul(A[2:6],B[2:6])+matmul(A[6:10],B[6:10])

def true_table():
    v=sp.Symbol('v');out={}
    for row in json.loads((HERE/'dependencies/e3_constants.json').read_text()):
        expr=sp.expand(sp.sympify(row['c']));p={}
        for term in sp.Add.make_args(expr):
            c,e=term.as_coeff_exponent(v)
            assert c.is_Integer and e.is_Integer and int(e)%2==0
            k=int(e)//2;p[k]=p.get(k,0)+int(c)
        out[row['b'],row['bp'],row['bpp']]={k:c for k,c in p.items() if c}
    assert len(out)==132
    return out

def finite_proof_inputs():
    assert T=={-4:1,-3:1,-2:2,-1:3,0:2,1:3,2:2,3:1,4:1}
    # Least coefficientwise nonnegative polynomial >=T congruent to aR mod4.
    ar=mul(a,R);support=set(T)|set(ar)
    least={e:T.get(e,0)+(ar.get(e,0)-T.get(e,0))%4 for e in support}
    assert {e:c for e,c in least.items() if c}==Cmin
    assert sum(Cmin.values())==20
    # Evaluate Laurent polynomials at primitive fourth and third roots.
    # Integer pairs represent 1,i and 1,omega, respectively.
    residues4=[(1,0),(0,1),(-1,0),(0,-1)]
    residues3=[(1,0),(0,1),(-1,-1)]
    def root_eval(p,residues):
        return tuple(sum(c*residues[e%len(residues)][j] for e,c in p.items()) for j in (0,1))
    assert root_eval(a,residues4)==root_eval(a,residues3)==(0,0)
    assert root_eval(Cmin,residues4)==(4,0)
    assert root_eval(Cmin,residues3)==(-4,0)
    assert [n for n in range(12) if n%4==2 and n%3==0]==[6]
    # Baseline W=3D: all comparisons other than second-cell U2,V2,aL.
    W=scale(D,3);G1=scale(mul(W,a),2);G2=mul(W,a);S=scale(mul(W,power(a,2)),2)
    U=sub(scale(W,2),D);U1=sub(scale(W,2),u)
    J=mul(u,sub(scale(W,2),ONE));V=sub(scale(mul(W,u),2),D)
    K1=sub(scale(D,5),scale(ONE,4))
    checks=[
      ('a',a,absolute(delta)),('aD',mul(a,D),absolute(mul(delta,D))),
      ('au',mul(a,u),absolute(mul(delta,D))),('aDu',mul(mul(a,D),u),absolute(mul(delta,power(D,2)))),
      ('W',W,D),('uW',mul(u,W),power(D,2)),
      ('G1',G1,scale(mul(D,sub(D,ONE)),4)),
      ('G2',G2,mul(power(D,2),sub(D,ONE))),
      ('uG1',mul(u,G1),scale(mul(power(D,2),sub(D,ONE)),4)),
      ('S',S,scale(mul(power(D,2),power(sub(D,ONE),2)),4)),
      ('U',U,D),('U1',U1,D),('uU',mul(u,U),power(D,2)),
      ('J',J,K1),('uJ',mul(u,J),mul(D,K1)),('uV',mul(u,V),mul(D,K1))]
    diffs={}
    for name,p,t in checks:
        h=half_difference(p,t);assert positive(h),(name,h);diffs[name]=h
    assert H0.get(-2)==H0.get(2)==-1 and min(H0)==-2 and max(H0)==2
    assert sum(a.values())==6 and sum(T.values())==16 and sum(R.values())%4==0
    assert divisible(sub(H0,R),4)
    return {'baseline_half_differences':diffs,'T':T,'Cmin':Cmin,
            'Cmin_at_i':[4,0],'Cmin_at_omega':[-4,0],
            'mass_lower_bounds':{'F':2,'Lambda':4,'bar_Lambda':8}}

def main():
    started=time.time();cert=json.loads((HERE/'dimension_scale_family_certificate.json').read_text())
    true=true_table();finite=finite_proof_inputs()
    labels=['mu','Sigma']+[f'g{i}_{x}' for i in (1,2) for x in ('1','12','2','21')]
    def sigma(x):return x[:3]+x[3:].translate(str.maketrans('12','21')) if x.startswith('g') else x
    def opposite(x):return x[:3]+x[3:][::-1] if x.startswith('g') else x
    results=[];all_tables=[]
    for case in cert['cases']:
        table={(r['inputs'][0],r['inputs'][1],r['output']):load_poly(r['q_coefficients']) for r in case['table']}
        F=load_poly(case['F']);W=load_poly(case['W']);L=load_poly(case['Lambda'])
        assert len(table)==132 and positive(F)
        assert W==add(scale(D,3),scale(F,4))
        H=add(H0,scale(mul(D,F),4))
        assert positive(sub(H,L)) and divisible(sub(L,R),4)
        assert positive(sub(mul(a,L),T))
        w=sum(W.values());l=sum(L.values());f=sum(F.values())
        score=bottom=dim_mass=trace_mass=0;is_bar=True
        for key in set(table)|set(true):
            p=table.get(key,{});t=true.get(key,{})
            for e in set(p)|set(t):
                d,c=p.get(e,0),t.get(e,0)
                assert d>=abs(c) and (d-c)%2==0,(case['name'],key,e,d,c)
                score+=(d-abs(c))//2
                if key[2]=='Sigma':bottom+=(d-abs(c))//2
            is_bar=is_bar and p==bar(p)
            assert table[sigma(key[0]),sigma(key[1]),sigma(key[2])]==p
            assert table[opposite(key[1]),opposite(key[0]),opposite(key[2])]==p
            if key[0]!='mu' and key[1]!='mu':
                dim_mass+=sum(p.values());trace_mass+=sum(map(abs,t.values()))
        assert trace_mass==4424 and dim_mass==578*w+74*l+364
        assert score==1438+1156*f+37*l==case['expected_score']
        assert is_bar==case['name'].startswith('bar')
        expected=(3898,3654,12220) if not is_bar else (4046,3634,12516)
        assert (score,bottom,dim_mass)==expected
        products={(x,y):{z:p for (xx,yy,z),p in table.items() if (xx,yy)==(x,y)} for x,y in product(labels,repeat=2)}
        for b in labels:assert products['mu',b]==products[b,'mu']=={b:ONE}
        def times(X,Y):
            ans={}
            for x,p in X.items():
                for y,q in Y.items():
                    for z,r in products[x,y].items():ans[z]=add(ans.get(z,{}),mul(mul(p,q),r))
            return {z:p for z,p in ans.items() if p}
        for x,y,z in product(labels,repeat=3):assert times(products[x,y],{z:ONE})==times({x:ONE},products[y,z])
        G={1:scale(mul(W,a),2),2:mul(W,a)};S=scale(mul(W,power(a,2)),2)
        identity=[ONE,{}, {},ONE]
        vectors={'mu':[ONE,ONE]+identity+identity,'Sigma':[{},S]+[{} for _ in range(8)]}
        determinants=[]
        for i in (1,2):
            A=[D,ONE,{},{}];B=[{}, {},u if i==1 else L,D]
            matrices={'1':A,'12':matmul(A,B),'2':B,'21':matmul(B,A)}
            flat=sp.Matrix([[sum(Fraction(c)*Fraction(2)**e for e,c in p.items()) for p in matrices[x]] for x in ('1','12','2','21')])
            determinant=flat.det();assert determinant!=0;determinants.append(str(determinant))
            for x,m in matrices.items():
                char=G[i] if len(x)==1 else mul(G[i],u if i==1 else D)
                vector=[{},char]+[{} for _ in range(8)]
                vector[2+4*(i-1):6+4*(i-1)]=[mul(a,p) for p in m]
                vectors[f'g{i}_{x}']=vector
        for x,y in product(labels,repeat=2):
            rhs=[{} for _ in range(10)]
            for z,c in products[x,y].items():rhs=vecadd(rhs,vecscale(vectors[z],c))
            assert algmul(vectors[x],vectors[y])==rhs
        if case['name']=='general':
            assert mul(a,L)==add(Cmin,{6:4})
            assert sub(H,L)=={-1:16,0:12,2:4,3:12}
        elif case['name']=='bar':
            assert L==sub(scale(power(D,2),3),scale(D,10))
            assert sub(H,L)==sub(scale(D,12),scale(ONE,8))
        elif case['name']=='bar_alternative':
            assert L==add(sub(scale(power(D,2),3),scale(D,14)),scale(ONE,16))
            assert sub(H,L)==sub(scale(D,16),scale(ONE,24))
        results.append({'name':case['name'],'pair_score':score,'bottom_score':bottom,
                        'nonunit_dimension_mass':dim_mass,'F_mass':f,'Lambda_mass':l,
                        'bar_invariant':is_bar,'dynkin_opposite':True,
                        'associativity_triples':1000,'matrix_products':100,
                        'generic_matrix_basis_determinants_at_q2':determinants})
        all_tables.append(table)
    assert len(all_tables)==4 and all_tables[0]!=all_tables[1] and all_tables[2]!=all_tables[3]
    assert all_tables[1]=={key:bar(p) for key,p in all_tables[0].items()}
    assert 6*3898==23388 and (23388*4**3898).bit_length()==7811
    out={'status':'PASS_EXACT_WITNESSES_AND_FINITE_PROOF_INPUTS','cases':results,
         'finite_proof_inputs':finite,'general_family_minimum':3898,'bar_family_minimum':4046,
         'all_table_optimum':'OPEN','arbitrary_support_lower_bound':'PROVED_IN_TEX_NOT_FINITE_EXTRAPOLATION',
         'N021_general_box':{'factor':23388,'base':4,'power':3898,'binary_digits':7811},
         'N021_symmetric_unimodal_box_unchanged':9327,
         'seconds':time.time()-started}
    (HERE/'dimension_scale_family_verified.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='finite_proof_inputs'},indent=2))

if __name__=='__main__':main()
