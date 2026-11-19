"""Exact symbolic rechecks of explicit calculations; proof scope in computations.md.
No source verdict is computed. Finite enumerations are labelled as such.
"""
import itertools,json,math,pathlib
import sympy as s
B=pathlib.Path(__file__).resolve().parents[1]
out={}
x,y,z,t=s.symbols('x y z t')
f=x*x+y+1;g=x+y*y+2
out['dlog_product']={v.name:str(s.simplify(s.diff(f*g,v)/(f*g)-s.diff(f,v)/f-s.diff(g,v)/g)) for v in (x,y)}
lam=s.Function('lambda')(x);a=s.Function('a')(x);u=s.Function('u')(x)
out['connection_frame_change']=str(s.simplify(s.diff(lam*u,x)+a*lam*u-u*s.diff(lam,x)-lam*(s.diff(u,x)+a*u)))
pure_a,pure_b,mixed=s.symbols('pure_a pure_b mixed')
out['kunneth_bookkeeping']={'restriction_A':str(pure_a),'restriction_B':str(pure_b),'after_pure_vanishing':str(mixed),'scope':'The mixed scalar is undetermined; this is not the missing universal-extension normalization.'}
F=x**3+y**3+z**3
out['veronese_cubic']={'ambient_dimension':math.comb(3+2,2)-1,'X_dimension':2,'gradient':[str(s.diff(F,v)) for v in (x,y,z)],'gradient_zero_locus':'x=y=z=0 over C, excluded in projective space','genus':(3-1)*(3-2)//2,'hilbert_polynomial':str(s.expand(((t+2)*(t+1)-(t-1)*(t-2))/2)),'Pic0_dimensions':[0,1]}
R=s.Matrix([[1,1]])
out['segre_restriction']={'matrix':R.tolist(),'kernel':[list(v) for v in R.nullspace()],'degree_1_minus_1':int((R*s.Matrix([1,-1]))[0])}
L=s.Matrix([[1,t]])
out['source_field_distinction']={'row':[[str(a) for a in L]],'extended_kernel':[str(v) for v in L.nullspace()[0]],'over_k':'1,t are linearly independent over k; no geometric theorem is claimed.'}
quad=x*y-z*z
out['quadric_cone']={'equation':str(quad),'gradient':[str(s.diff(quad,v)) for v in (x,y,z)],'singular_locus':[{str(k):str(v) for k,v in d.items()} for d in s.solve([s.diff(quad,v) for v in(x,y,z)],(x,y,z),dict=True)],'normality_reason':'Irreducible hypersurface => Cohen–Macaulay/S2; the isolated singularity has codimension2 => R1; Serre criterion gives normality.'}
out['vertical_exponents']={'coefficients':[1,2],'equations':'1−n=0 and2−n=0','solutions':s.solve([1-t,2-t],t)}
out['nonaffine_extension']={'section':'[x:y]','on_punctured_x_axis':'[1:0]','on_punctured_y_axis':'[0:1]','origin_base_ideal':'(x,y)','generic_Vx_defined':'y is nonzero at its generic point'}
out['coupled_descent_equation']={'equation':'phi*psi1=psi2','point_satisfying':[2,3,6],'changing_phi_only_fails':bool(5*3!=6),'scope':'An elementary coupling test, not a geometric counterexample to affine representability.'}
inc=s.Matrix([[-1,1],[-1,1]])
out['two_node_gluing']={'incidence_matrix':inc.tolist(),'rank':inc.rank(),'torus_kernel_dimension':2-inc.rank(),'invariant':'lambda1/lambda2'}
fs=s.symbols('f0:4'); cs={}
for n in (1,2):
    for p in range(3):
        I=list(itertools.combinations(range(4),p+1));J=list(itertools.combinations(range(4),p+2))
        c={ii:s.Symbol('c_'+'_'.join(map(str,ii))) for ii in I}
        d={jj:sum((-1)**a*fs[jj[a]]**n*c[jj[:a]+jj[a+1:]] for a in range(len(jj))) for jj in J}
        for m in (n+1,n+2):
            tc={ii:s.prod(fs[k] for k in ii)**(m-n)*c[ii] for ii in I}
            dt={jj:sum((-1)**a*fs[jj[a]]**m*tc[jj[:a]+jj[a+1:]] for a in range(len(jj))) for jj in J}
            residual=[s.expand(dt[jj]-s.prod(fs[k] for k in jj)**(m-n)*d[jj]) for jj in J]
            assert all(v==0 for v in residual)
            cs[f'n{n}_m{m}_p{p}']='all symbolic transition-compatibility residuals0'
        if p<2:
            K=list(itertools.combinations(range(4),p+3))
            dd=[s.expand(sum((-1)**a*fs[kk[a]]**n*d[kk[:a]+kk[a+1:]] for a in range(len(kk)))) for kk in K]
            assert all(v==0 for v in dd)
out['cech_koszul']=cs
out['graded_degree']={'indices':[0,1,2],'degrees':[2,3,5],'numerator_degree':31,'power':3,'correct_localized_degree':31-3*(2+3+5),'omitted_index_degree':31-3*(2+3),'difference':3*5}
finite=[]
for n in range(0,9):
    mult=s.zeros(n+1)
    for j in range(n):mult[j+1,j]=1
    ker=mult.nullspace(); assert len(ker)==1
    expected=s.zeros(n+1,1);expected[n,0]=1;assert ker[0]==expected
    if n:
        projection=s.eye(n+1)[:n,:]
        assert projection*ker[0]==s.zeros(n,1)
    finite.append({'n':n,'rank':mult.rank(),'kernel_dimension':len(ker),'kernel_basis':f't^{n}','transition_to_previous':'zero' if n else 'not applicable'})
out['finite_free_complex']=finite
out['lattice_counterchain']=[{'n':n,'generator':2**n,'next_index':2,'saturated':n==0} for n in range(7)]
out['divergent_formal_series']=[{'n':n,'coefficient':math.factorial(n),'successive_ratio':n+1} for n in range(1,9)]
out['constant_elliptic_boundary']={'base':'C[[t]]','H1_O':'C[[t]], infinite length','Pic_formal_comparison':'isomorphism by proper formal existence','tower_transition_kernel':'additive C at each step','scope':'Already complete base, outside the analytic finite-length criterion.'}
out['component_counterexample']={'map':'mu2 -> Gm over C','kernel':'trivial connected','source_pi0_order':2,'target_pi0_order':1}
out['elliptic_product_tower']=[{'m':m,'n':n,'kernel_dimension':m-n,'kernel':f'E^{m-n}','cokernel':'0','kernel_vector_group':False} for n,m in [(1,2),(2,4),(3,6)]]
GB=s.groebner([quad,x*x,x*z,z*z],x,y,z,order='lex')
out['prime_square_not_primary']={'ring':'Q[x,y,z]/(xy-z^2)','prime':'(x,z)','remainder_x':str(GB.reduce(x)[1]),'remainder_y_times_x':str(GB.reduce(y*x)[1]),'y_not_in_prime':True}
assert GB.reduce(x)[1]!=0 and GB.reduce(y*x)[1]==0
out['primary_not_prime_power']={'ideal':'(x^2,y^3)','radical':'(x,y)','quotient_basis':['1','x','y','xy','y^2','xy^2'],'length':6,'not_m_power':'x^2 belongs but y^2 does not; m^3 misses x^2'}
checks=[]
for ni in [(1,1),(2,3),(2,3,4),(3,3,3)]:
    bound=sum(a-1 for a in ni)+1
    candidates=list(itertools.product(*(range(a) for a in ni)))
    max_degree=max(map(sum,candidates))
    assert max_degree==bound-1
    checks.append({'individual_nilpotence_exponents':ni,'manuscript_bound':sum(ni),'sharp_monomial_bound':bound,'max_unforced_monomial_degree':max_degree})
out['nilpotence_bound_examples']=checks
mat=s.Matrix([[1,2,0],[0,1,1],[1,0,1]])
out['linear_system_basis_change']={'matrix':mat.tolist(),'determinant':int(mat.det()),'inverse_exists':mat.det()!=0}
out['curve_closed_point_bound']={'curve':'P1 over R','closed_point_degree':2,'D':'0','h0_O':1,'h0_O_Q':3,'increase':2,'conclusion':'The +1 bound requires a rational point.'}
A0,A1,B0,B1=s.symbols('A0 A1 B0 B1',commutative=False)
eps=s.symbols('epsilon')
expansion=s.expand((A0+eps*A1)*(B0+eps*B1))
out['bilinear_product_rule']={'formal_expansion':str(expansion),'linear_term_order':'A1*B0 + A0*B1','scope':'epsilon is a bookkeeping scalar; the general proof uses bilinearity and norm estimates, preserving factor order.'}
out['elliptic_quotient_conic']={'parametrization':['u^2','u*v','v^2'],'equation_X0X2_minus_X1squared':str(s.expand(x*x*y*y-(x*y)**2)),'smoothness':'gradient=(X2,-2X1,X0), no common projective zero over C','scope':'normalized elliptic quotient model; not the missing theta-coordinate identification'}
assert all(v=='0' for v in out['dlog_product'].values())
assert out['connection_frame_change']=='0'
def encode(v):
    if isinstance(v,s.Basic):return str(v)
    raise TypeError(type(v))
json.dump(out,open(B/'outputs/calculations.json','w'),ensure_ascii=False,indent=2,default=encode)
print(json.dumps({'calculation_groups':len(out),'all_exact_assertions_passed':True,'scope':'Finite symbolic checks accompany, and do not replace, the general proofs in computations.md.'}))
