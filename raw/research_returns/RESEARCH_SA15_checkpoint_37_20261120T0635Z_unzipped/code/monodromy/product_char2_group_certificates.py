#!/usr/bin/env python3
"""Binary matrix certificates for possible exact product monodromy proofs.

Only exact finite-field arithmetic.  No smoothness or group conclusion
is asserted by this script; the ordinary coherent bundle exists on the
entire parameter projective space, including singular sections.
"""
import itertools,json,random,time
from pathlib import Path
import sympy as sp

started=time.perf_counter();root=Path(__file__).resolve().parents[1]
ns={'__file__':str(Path(__file__).with_name('ordinary_abelian_surface.py'))}
source=Path(ns['__file__']).read_text().split("u,v,w,z=sp.symbols('u v w z')")[0]
exec(compile(source,ns['__file__'],'exec'),ns)
rank,apply,components,cmatrix2=map(ns.get,['rank','apply','components','Cmatrix'])

def charpoly(cols):
    """Similarity reduction to upper Hessenberg, then determinant recurrence."""
    n=len(cols)
    rows=[sum(((cols[j]>>i)&1)<<j for j in range(n)) for i in range(n)]
    for k in range(n-2):
        pivot=next((j for j in range(k+1,n) if rows[j]>>k&1),None)
        if pivot is None:continue
        if pivot!=k+1:
            rows[pivot],rows[k+1]=rows[k+1],rows[pivot]
            for i in range(n):
                if ((rows[i]>>pivot)^(rows[i]>>(k+1)))&1:
                    rows[i]^=(1<<pivot)|(1<<(k+1))
        for i in range(k+2,n):
            if rows[i]>>k&1:
                rows[i]^=rows[k+1]
                for j in range(n):
                    if rows[j]>>i&1:rows[j]^=1<<(k+1)
    polys=[1]
    for i in range(1,n+1):
        z=polys[-1]<<1
        if rows[i-1]>>(i-1)&1:z^=polys[-1]
        prod=1
        for k in range(i-2,-1,-1):
            prod&=(rows[k+1]>>k)&1
            if not prod:break
            if rows[k]>>(i-1)&1:z^=polys[k]
        polys.append(z)
    return polys[-1]

def pdiv(a,b):
    q=0;d=b.bit_length()-1
    while a and a.bit_length()-1>=d:
        s=a.bit_length()-1-d;q^=1<<s;a^=b<<s
    return q,a
def pmod(a,b):return pdiv(a,b)[1]
def pmul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
    return z
def gcd(a,b):
    while b:a,b=b,pmod(a,b)
    return a
def fieldmul(a,b,f):return pmod(pmul(a,b),f)
def fieldsquare(a,f):return fieldmul(a,a,f)
def fieldinv(a,f):
    assert a
    u,v,g1,g2=a,f,1,0
    while u!=1:
        j=u.bit_length()-v.bit_length()
        if j<0:u,v,g1,g2,j=v,u,g2,g1,-j
        u^=v<<j;g1^=g2<<j
    return pmod(g1,f)
def irreducible(f):
    n=f.bit_length()-1
    if n==1:return True
    primes=list(sp.factorint(n))
    tests={n//q for q in primes};z=2
    for i in range(1,n+1):
        z=fieldsquare(z,f)
        if i in tests and gcd(z^2,f)!=1:return False
    return z==2
def reciprocal(f):
    n=f.bit_length()-1
    return sum(((f>>i)&1)<<(n-i) for i in range(n+1))
def pstr(f):
    return '+'.join('1' if i==0 else 'T' if i==1 else 'T^'+str(i)
                    for i in range(f.bit_length()-1,-1,-1) if f>>i&1)

def inverse_cols(cols):
    n=len(cols)
    rows=[sum(((cols[j]>>i)&1)<<j for j in range(n))|(1<<(n+i)) for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if rows[i]>>j&1)
        rows[pivot],rows[j]=rows[j],rows[pivot]
        for i in range(n):
            if i!=j and rows[i]>>j&1:rows[i]^=rows[j]
    return [sum(((rows[i]>>(n+j))&1)<<i for i in range(n)) for j in range(n)]

def fieldrank(rows,f):
    rows=[r[:] for r in rows];m=len(rows);n=len(rows[0]);r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if rows[i][j]),None)
        if pivot is None:continue
        rows[pivot],rows[r]=rows[r],rows[pivot]
        inv=fieldinv(rows[r][j],f)
        rows[r]=[fieldmul(x,inv,f) for x in rows[r]]
        for i in range(r+1,m):
            z=rows[i][j]
            if z:rows[i]=[a^fieldmul(z,b,f) for a,b in zip(rows[i],rows[r])]
        r+=1
        if r==m:break
    return r

def factor_bits(f):
    T=sp.Symbol('T')
    P=sp.Poly(sum(T**i for i in range(f.bit_length()) if f>>i&1),T,modulus=2)
    return [(sum((int(c)%2)<<int(m[0]) for m,c in z.terms()),e)
            for z,e in sp.factor_list(P)[1]]

def line_certificate(A,B):
    """B invertible; det(A+tB) monic of full degree n."""
    n=len(A);Bi=inverse_cols(B);BA=[apply(Bi,c) for c in A]
    h=charpoly(BA);assert h.bit_length()-1==n
    facts=factor_bits(h);tests=[]
    rebuilt=1
    for f,e in facts:
        assert irreducible(f)
        for _ in range(e):rebuilt=pmul(rebuilt,f)
    assert rebuilt==h
    for f,e in facts:
        alpha=pmod(2,f)
        R=[[((A[j]>>i)&1)^(((B[j]>>i)&1)*alpha) for j in range(n)] for i in range(n)]
        S=[[0]*n for _ in range(n)]
        Sq=[[fieldsquare(z,f) for z in row] for row in R]
        for i in range(n):
            for k in range(n):
                if not Sq[i][k]:continue
                for j in range(n):
                    if R[k][j]:S[i][j]^=fieldmul(Sq[i][k],R[k][j],f)
        r=fieldrank(R,f);r2=fieldrank(S,f)
        tests.append({'factor_bits':f,'factor':pstr(f),'multiplicity':e,
                      'rank_M':r,'rank_M_squared_twist_M':r2})
        if r2<n-1:return False,{'determinant_bits':h,'factors':tests}
    return True,{'determinant_bits':h,'determinant':pstr(h),'factors':tests,
                'full_degree':n,'leading_coefficient':1}

# Check the custom characteristic polynomial against independent SymPy
# calculations on twenty binary matrices of varying dimensions.
rng=random.Random(2026111906)
for n in (3,5,9,12):
    for _ in range(5):
        C=[rng.getrandbits(n) for _ in range(n)]
        Z=sp.Symbol('Z');P=sp.Matrix(n,n,lambda i,j:(C[j]>>i)&1).charpoly(Z).as_poly()
        ref=sum((int(c)%2)<<int(m[0]) for m,c in P.terms())
        assert charpoly(C)==ref

out={'scope':'Finite matrix certificates, generic-group proof external',
     'random_seed':2026111906,'custom_charpoly_independent_checks':20}
M1=[[[1,0,0],[0,0,1],[0,0,0]],[[0,0,1],[0,1,0],[0,0,1]],[[0,1,0],[1,0,0],[0,1,1]]]
T=list(itertools.product(range(3),repeat=2))
MS=[[sum(M1[a][i][j]*M1[b][k][l]<<z for z,(i,k) in enumerate(T))
       for j,l in T] for a,b in T]
def cmatrix1(s):
    R=[0]*9
    for i,C in enumerate(MS):
        if s>>i&1:R=[a^b for a,b in zip(R,C)]
    return R

for d,n,cmatrix in [(1,9,cmatrix1),(2,36,cmatrix2)]:
    res={'W_dimension':n,'relative_dimension':n-1}
    if d==1:
        a=258;C=cmatrix(a);f,r=pdiv(charpoly(C),3);assert not r and irreducible(f)
        assert rank(C)==9 and f!=reciprocal(f)
        res['irreducible_frobenius']={'section_bits':a,'columns':C,
             'nontrivial_factor_bits':f,'nontrivial_factor':pstr(f),
             'self_reciprocal':f==reciprocal(f)}
        D=cmatrix(27)
        assert rank(D)==9 and charpoly(D)==771 # (T+1)^9
        res['other_frobenius']={'section_bits':27,'charpoly_bits':charpoly(D)}
    else:
        found1=found2=False
        for attempt in range(1,30001):
            s=rng.getrandbits(n);C=cmatrix(s)
            if rank(C)!=n:continue
            cs=components(s)
            if rank(cs)!=4:continue
            if not found1:
                cp=charpoly(C);f,r=pdiv(cp,17) # (T+1)^4=T^4+1
                assert not r
                if irreducible(f) and f!=reciprocal(f):
                    res['irreducible_frobenius']={'section_bits':s,'columns':C,
                         'character_components':cs,'attempt':attempt,
                         'nontrivial_factor_bits':f,'nontrivial_factor':pstr(f),
                         'self_reciprocal':False};found1=True
                    print('degree2 irreducible factor found at',attempt,flush=True)
            if not found2:
                image=[C[j]^(1<<j) for j in range(n)]+[s]
                r0=rank(image)
                if rank(image+cs)==r0:
                    res['no_fixed_complement_frobenius']={'section_bits':s,'columns':C,
                        'character_components':cs,'attempt':attempt,
                        'rank_image_C_minus_I_plus_s':r0,
                        'rank_after_character_components':rank(image+cs),
                        'charpoly_bits':charpoly(C)};found2=True
                    print('degree2 no-complement certificate found at',attempt,flush=True)
            if found1 and found2:break
        res['frobenius_search_attempts']=attempt
        assert found1 and found2
        # Independent integer characteristic polynomial, reduced modulo two,
        # for both retained 36-dimensional Frobenius certificates.
        for key in ('irreducible_frobenius','no_fixed_complement_frobenius'):
            cols=res[key]['columns'];Z=sp.Symbol('Z')
            P=sp.Matrix(n,n,lambda i,j:(cols[j]>>i)&1).charpoly(Z).as_poly()
            ref=sum((int(c)%2)<<int(m[0]) for m,c in P.terms())
            assert ref==charpoly(cols)
            res[key]['independent_sympy_charpoly_verified']=True
        second_K,rem=pdiv(res['no_fixed_complement_frobenius']['charpoly_bits'],17)
        assert rem==0 and second_K.bit_count()%2==0
        res['no_fixed_complement_frobenius']['K_charpoly_bits']=second_K
        res['no_fixed_complement_frobenius']['K_charpoly_has_root_one']=True
    for attempt in range(1,401):
        a=rng.getrandbits(n);b=rng.getrandbits(n);A=cmatrix(a);B=cmatrix(b)
        if rank(B)!=n:continue
        yes,cert=line_certificate(A,B)
        if yes:
            cert.update({'section_a_bits':a,'section_b_bits':b,'A_columns':A,'B_columns':B,
                         'attempt':attempt});res['line_certificate']=cert
            print('degree',d,'line certificate found at',attempt,flush=True);break
    else:raise AssertionError('No good line certificate found')
    out['degree'+str(d)]=res
    out['runtime_seconds']=time.perf_counter()-started
    (root/'outputs'/'product_char2_group_certificates.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
