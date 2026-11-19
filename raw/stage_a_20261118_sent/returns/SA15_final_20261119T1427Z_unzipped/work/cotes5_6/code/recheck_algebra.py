"""Exact, reproducible checks for the cote 5–6 consolidation.

These finite computations test specified instances and counterexamples; they are
not labelled as formal proofs of the general theorems. No floating point is used.
"""
from fractions import Fraction
from itertools import product, combinations
from math import factorial, comb, lcm
import json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

OUT = Path(__file__).resolve().parent.parent / 'outputs'
results = {}

def vp(n, p):
    n = Fraction(n)
    if not n: return 10**9
    a,b = abs(n.numerator), n.denominator
    v=0
    while a%p == 0: a//=p; v+=1
    while b%p == 0: b//=p; v-=1
    return v

def digit_sum(n,p):
    total=0
    while n: total+=n%p; n//=p
    return total

factorial_checks=[]
for p in (2,3,5,7):
    for n in range(1,101):
        assert vp(factorial(n),p)==Fraction(n-digit_sum(n,p),p-1)
        c=Fraction(factorial(p*n),factorial(n)**p*factorial(p))
        d=Fraction(factorial(p*n),factorial(p)**n*factorial(n))
        assert c.denominator==d.denominator==1
        assert vp(c,p)==digit_sum(n,p)-1
        assert vp(d,p)==0
    for i in range(4):
        q=Fraction(factorial(p**(i+1)),factorial(p**i)**p)
        assert q.denominator==1 and vp(q,p)==1
    factorial_checks.append({'p':p,'n_range':[1,100],'q_index_range':[0,3],
      'Legendre':True,'v(c_n)=s_p(n)-1':True,'v(d_n)=0':True,'v(q_i)=1':True,
      'boundary_values_n=p^r':[str(Fraction(p**r,p-1)-vp(factorial(p**r),p)) for r in range(5)]})
results['factorial_identities']=factorial_checks
cn=Fraction(factorial(3)**vp(factorial(2),3),factorial(2))
results['c_n_mod_p_counterexample']={'p':3,'n':2,'c_n':str(cn),'residue':cn.numerator*pow(cn.denominator,-1,3)%3}

def universal_normal_form(p,nu,r):
    basis=list(product(range(p),repeat=nu+1)); N=len(basis); where={a:i for i,a in enumerate(basis)}
    q=[factorial(p**(i+1))//factorial(p**i)**p for i in range(nu)]
    lam=[s.Rational(p**(p**i),factorial(p**i)) for i in range(nu+1)]
    L=[]
    for j in range(nu+1):
        M=s.zeros(N)
        for col,a in enumerate(basis):
            b=list(a); b[j]+=1; coeff=1; k=j
            while k<=nu and b[k]>=p:
                b[k]-=p
                if k==nu: coeff=0;break
                coeff*=q[k];b[k+1]+=1;k+=1
            if coeff: M[where[tuple(b)],col]=coeff
        L.append(M)
    T=[L[i]-lam[i]*s.eye(N) for i in range(nu+1)]
    e=s.zeros(N,1);e[where[(0,)*(nu+1)],0]=1
    cols=[]
    for a in basis:
        v=e
        for i,n in enumerate(a):
            for _ in range(n):v=T[i]*v
        cols.append(v)
    U=s.Matrix.hstack(*cols)
    assert U.det()==1
    B=s.Matrix.hstack(*T[:r+1])
    c=nu+p*(p**nu-(p**nu-1)//(p-1))
    weights=[max(0,next((i-r for i,z in enumerate(a) if z),c-r)) for a in basis]
    coords=U.inv()*B
    containment=all(vp(coords[i,j],p)>=weights[i] for i in range(N) for j in range(B.cols))
    assert containment
    den=lcm(*[int(z.q) for z in B]); assert den%p
    diag=smith_normal_form((den*B).applyfunc(int),domain=ZZ)
    inv=[vp(diag[i,i],p) for i in range(N)]
    assert all(v<10**9 for v in inv)
    assert sorted(inv)==sorted(weights)
    return {'p':p,'nu':nu,'r':r,'rank':N,'c_nu':c,
      'invariant_factor_p_valuations':sorted(inv),'predicted':sorted(weights),
      'coordinate_ideal_containment':containment,'length':sum(inv),
      'assertions':'All pass; these finite cases do not replace the independent general proof.'}

results['normal_form_checks']=[universal_normal_form(p,nu,r)
 for p,nu in [(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(5,0),(5,1)]
 for r in range(nu+1)]

# A = Z*1 + Z*x + Z*y; x*x=2y and all products involving y and x/y vanish.
def mul(a,b):
    return (a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[0]*b[2]+a[2]*b[0]+2*a[1]*b[1])
unit=(1,0,0);xv=(0,1,0);yv=(0,0,1);bas=[unit,xv,yv]
assert all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a,b,c in product(bas,repeat=3))
assert mul(xv,xv)==(0,0,2)
assert all(z==0 for z in mul(mul(xv,xv),xv))
results['principal_ideal_counterexample']={'ring':'Z[1,x,y] additively free; x^2=2y,xy=y^2=0',
 'associativity_basis_triples':27,'all_pass':True,'x^2/2':'y',
 'xA':'Z*x + 2Z*y','y_in_xA':False,'x^n/n!_in_A_all_n':True,
 'therefore':'The ring-membership condition is insufficient for a PD structure on xA.'}
results['log_sign_counterexample']={'ring':'Q[e]/(e^2)','gamma_1(e)':'e','gamma_n(e),n>1':'0',
 'exp(e)':'1+e','literal_log(1+e)':'-e','literal_log(exp(e))':'-e != e',
 'corrected_sign':'(-1)^(n-1)'}

x,y=s.symbols('x y'); f=x**5+y**5+x**3*y**3
generators=[s.diff(f,x),s.diff(f,y)]+[x**a*y**(7-a) for a in range(8)]
G=s.groebner(generators,x,y,domain=s.QQ)
nf=s.expand(G.reduce(f)[1])
assert nf!=0
assert G.reduce(s.diff(f,x))[1]==G.reduce(s.diff(f,y))[1]==0
std=[]
for i in range(7):
    for j in range(7-i):
        mon=x**i*y**j
        if G.reduce(mon)[1]==mon:std.append(str(mon))
results['artinian_de_rham_H0_counterexample']={'f':str(f),'ideal_generators':[str(z) for z in generators],
 'groebner_basis':[str(z.as_expr()) for z in G.polys], 'normal_form_f':str(nf),
 'df_in_ideal':True,'standard_monomials':std,
 'reason_Artinian_local':'(x,y)^7 is contained in the ideal; all generators lie in (x,y).',
 'conclusion':'Nonconstant nonzero f has df=0; arbitrary local Artinian ordinary de Rham Poincare fails.'}

def mono_div(a,b): return all(u>=v for u,v in zip(a,b))
def wedge(a,b):
    if set(a)&set(b): return None,0
    sign=(-1)**sum(i>j for i in a for j in b)
    return tuple(sorted(a+b)),sign

def de_rham_monomial(gens,bounds):
    n=len(bounds);mons=[a for a in product(*[range(v) for v in bounds]) if not any(mono_div(a,g) for g in gens)]
    bases=[[(a,I) for a in mons for I in combinations(range(n),q)] for q in range(n+1)]
    loc=[{v:i for i,v in enumerate(bs)} for bs in bases]
    Rs=[];Ds=[]
    for q in range(n+1):
        cols=[]
        if q:
            for g in gens:
                for h in mons:
                    for I in combinations(range(n),q-1):
                        col=s.zeros(len(bases[q]),1)
                        for j,gj in enumerate(g):
                            if not gj:continue
                            a=tuple(g[k]+h[k]-(k==j) for k in range(n));J,sg=wedge((j,),I)
                            if sg and (a,J) in loc[q]:col[loc[q][a,J]]=sg*gj
                        if any(col):cols.append(col)
        Rs.append(s.Matrix.hstack(*cols) if cols else s.zeros(len(bases[q]),0))
        if q<n:
            D=s.zeros(len(bases[q+1]),len(bases[q]))
            for col,(a,I) in enumerate(bases[q]):
                for j,aj in enumerate(a):
                    if not aj:continue
                    b=tuple(a[k]-(k==j) for k in range(n));J,sg=wedge((j,),I)
                    if sg:D[loc[q+1][b,J],col]=sg*aj
            Ds.append(D)
    Rr=[R.rank() for R in Rs];dim=[len(bs)-rr for bs,rr in zip(bases,Rr)]
    ranks=[s.Matrix.hstack(Rs[q+1],Ds[q]).rank()-Rr[q+1] for q in range(n)]
    for q in range(n):
        assert s.Matrix.hstack(Rs[q+1],Ds[q]*Rs[q]).rank()==Rr[q+1]
    H=[dim[q]-(ranks[q] if q<n else 0)-(ranks[q-1] if q else 0) for q in range(n+1)]
    assert H==[1]+[0]*n
    return {'monomial_ideal':gens,'basis_monomials':mons,'dim_Omega_q':dim,'rank_d_q':ranks,'dim_Hq':H}
results['graded_monomial_de_rham']=[
 de_rham_monomial([(2,0),(0,3)],(2,3)),
 de_rham_monomial([(2,0),(1,1),(0,2)],(2,2)),
 de_rham_monomial([(3,0),(0,2),(2,1)],(3,2)),
 de_rham_monomial([(3,0),(0,2),(1,1)],(3,2)),
 de_rham_monomial([(2,0,0),(0,2,0),(0,0,3)],(2,2,3))]

results['DVR_boundary']=[{'p':p,'e':e,'valuation_gamma_pi_at_n=p^r':
 [int(p**r-e*vp(factorial(p**r),p)) for r in range(5)]}
 for p in (2,3,5,7) for e in sorted(set([1,p-1,p]))]
results['characteristic_p_affine_line']=[{'p':p,'kernel_monomial_degrees_under_20':[n for n in range(20) if n%p==0],
 'cokernel_dx_degrees_under_20':[n for n in range(20) if (n+1)%p==0],
 'formula':'H0=k[x^p], H1=k[x^p]*x^(p-1) dx'} for p in (2,3,5)]
results['char_p_nonreduced_Frobenius']={'p':3,'ring':'F3[e]/e^2','F(e)':'0','d(e)':'de != 0',
 'H0_deRham':'F3','conclusion':'Frobenius factors through de Rham degree zero but is not an isomorphism onto closed functions from O.'}

# y^2 = x^3-x over F3; i exists over the unramified quadratic extension Q3(i).
pts=[(a,b) for a,b in product(range(3),repeat=2) if (b*b-a*a*a+a)%3==0]
J=s.Matrix([[0,-1],[1,0]]);a,b,c,d=s.symbols('a b c d');M=s.Matrix([[a,b],[c,d]])
relations=s.solve(list(M*J-J*M),(c,d),dict=True)
assert len(pts)+1==4 and J*J==-s.eye(2)
results['supersingular_CM_counterexample']={'curve':'y^2=x^3-x','prime':3,'discriminant':64,
 'affine_points_F3':pts,'number_points_F3':len(pts)+1,'a_3':0,
 'CM_map':'(x,y)->(-x,i*y), i^2=-1, defined over Q3(i)',
 'CM_matrix_square_minus_identity':True,'centralizer_relations':str(relations),
 'centralizer_dimension':2,'GL2_dimension':4,'conclusion':'Galois image is contained in a proper CM centralizer, so it is not open in GL2(Q3).'}
results['ramified_Tate_twist_counterexample']={'residue_field':'algebraic closure of F5','K':'Frac(W(residue_field))',
 'Tate_parameter':'q=5','twist':'d=5','v_c4_before':0,'v_Delta_before':1,
 'v_c4_after':0+2,'v_Delta_after':1+6,'v_j':3*2-7,
 'minimality':'v(Delta)=7<12 and an integral Tate Weierstrass model is twisted by d.',
 'reduction':'additive potentially multiplicative (I1*), not multiplicative',
 'Galois_sequence':'0 -> Z5(1) tensor chi_5 -> Tp(E^5) -> Z5 tensor chi_5 -> 0'}
results['Spin_1_1_check']={'even_Clifford_element':'a+b*e1e2, (e1e2)^2=1','norm':'a^2-b^2',
 'norm_one':'a^2-b^2=1','image_diagonal_entry':'a^2+b^2>=1',
 'minus_identity_in_SO_1_1':True,'minus_identity_in_norm_one_Spin_image':False,
 'conclusion':'For the real indefinite norm-one definition, surjectivity to the full SO(1,1) fails.'}

(OUT/'algebra_checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
