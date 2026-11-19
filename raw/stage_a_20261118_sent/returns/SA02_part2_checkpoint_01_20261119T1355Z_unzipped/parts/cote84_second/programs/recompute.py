"""Independent exact checks for SA02 cote84/146-193.

Polynomial identities are checked over Z[parameters] (hence survive all base
changes). Finite enumerations are separately labelled; they do not prove a
universal statement. This file does not decide any uncertain transcription.
"""
from pathlib import Path
import json, itertools, datetime
import sympy as s

W=Path(__file__).resolve().parents[1]
out={}
chi,t1,t2,gamma,delta,lam,mu=s.symbols('chi tau1 tau2 gamma delta lambda mu')
I=s.eye(2)
P=lambda t:s.Matrix([[chi,t],[0,0]])
Q=lambda t:chi*I-P(t)
zero=lambda M:all(s.expand(x)==0 for x in M)
def certify(name,M):
    ok=zero(M) if isinstance(M,s.MatrixBase) else s.expand(M)==0
    assert ok,(name,M)
    out[name]={'certificate':'identically zero over the integer polynomial ring','residual':str(s.simplify(M))}

# 146,148,150,152,156,158,164: complementary endomorphisms and ansätze.
for name,M in [('P+Q',P(t1)+Q(t1)-chi*I),('PQ',P(t1)*Q(t1)),
               ('QP',Q(t1)*P(t1)),('P_squared',P(t1)**2-chi*P(t1)),
               ('Q_squared',Q(t1)**2-chi*Q(t1))]:certify(name,M)
sig=I-gamma*P(t1)
certify('involution_defect',sig**2-I-gamma*(gamma*chi-2)*P(t1))
certify('chi2_involution',(I-P(t1)).subs(chi,2)**2-I)
certify('corrected_scalar_identity',-chi*(1-gamma*chi)+2*chi*(1-gamma*chi)+gamma*chi**2-chi)
G=s.groebner([lam**2+1-chi,lam*mu+1,mu**2-gamma],lam,mu,gamma,chi)
assert G.reduce(gamma*(chi-1)-1)[1]==0
out['second_ansatz']={'consequence':'gamma*(chi-1)=1','groebner_basis':[str(v) for v in G.polys],
 'combined_with_gamma_chi_2':'gamma=1, chi=2; combination of ansätze is an added hypothesis'}
l,m,h,L,M,Hh=s.symbols('l m h L M H')
U=s.Matrix([[l,h],[0,m]]);Vh=s.Matrix([[L,Hh],[0,M]])
conj=lambda Z:s.trace(Z)*s.eye(2)-Z
certify('triangular_trace_anti_involution',conj(U*Vh)-conj(Vh)*conj(U))
certify('triangular_trace_double_involution',conj(conj(U))-U)
certify('triangular_Cayley_Hamilton',U*U-s.trace(U)*U+U.det()*s.eye(2))
out['coefficient_cancellation_counterexamples']={
 'scalar_from_module_equality':'R=Z/4, M=R/2R, scalar2 annihilates id_M but2 is nonzero inR',
 'cancelling_chi':'R=Z/4, chi=2, beta=0,gamma=2: chi*beta=chi*gamma while beta!=gamma',
 'cancelling_pi_image':'R=Z/4, pi=2 onE=R, chi=2: pi^2=chi*pi and scalar2 annihilates image(pi) without vanishing'}
A=s.kronecker_product(P(t1),I);B=s.kronecker_product(I,P(t2))
alpha=-chi*(1-delta*chi);beta=1-delta*chi
F=s.simplify(alpha*s.eye(4)+beta*(A+B)+delta*A*B)
target_boundary=s.zeros(4,3);target_boundary[0,0]=chi;target_boundary[0,1]=t2;target_boundary[0,2]=t1
certify('full_F_boundary_columns',F[:,:3]-target_boundary)
desired=s.Matrix([delta*t1*t2,-t1,-t2,chi])
res=s.simplify(F[:,3]-desired)
out['full_F']={'basis':['LL','LM','ML','MM'],'matrix':str(F),
 'strict_pullback_residual':str(res),'sufficient_condition':'delta*chi=2',
 'missing_MM_column_matters':True}
certify('symmetrizer_at_chi2_delta1',F.subs({chi:2,delta:1})-
 (s.eye(4)+s.kronecker_product(I-P(t1).subs(chi,2),I-P(t2).subs(chi,2))))

# Independent change-of-splitting calculation, including the sign.
a,b,rho,c,a2,b2=s.symbols('a b rho c a2 b2')
transition=a*t2+t1*b+chi*a*b
S1=s.Matrix([[1,a],[0,1]]);S2=s.Matrix([[1,b],[0,1]])
S=s.kronecker_product(S1,S2)
new_tensor_split=S*s.Matrix([0,0,0,1])
g=s.Matrix([[chi,t2,t1,0]])
certify('pushout_splitting_increment',(g*new_tensor_split)[0]-transition)
old_pull=s.Matrix([0,-t1,-t2,chi])
new_pull=s.Matrix([0,-(t1+chi*a),-(t2+chi*b),chi])
certify('pullback_splitting_increment',S*new_pull-old_pull-s.Matrix([-transition,0,0,0]))
certify('comparison_shear_obstruction',
 delta*((t1+chi*a)*(t2+chi*b)-t1*t2)-2*transition-(delta*chi-2)*transition)
out['sign_obstruction']={'pushout_transition':str(transition),'pullback_transition':str(-transition),
 'strict_shear_equation':'k_new-k_old=2*transition',
 'candidate_shear':'delta*tau1*tau2','candidate_defect':str((delta*chi-2)*transition)}

# Earlier run's local chi-groupoid. This is a re-proof, not attribution to 146-193.
star=lambda t,u,x,y:s.expand(x*u+t*y+chi*x*y)
h=star(t1,t2,a,b)
certify('local_groupoid_target',(t1+chi*a)*(t2+chi*b)-t1*t2-chi*h)
left=star(t1*t2,rho,h,c)
right=star(t1,t2*rho,a,star(t2,rho,b,c))
certify('local_groupoid_associativity',left-right)
certify('local_groupoid_commutativity',h-star(t2,t1,b,a))
certify('local_groupoid_unit',star(t1,1,a,0)-a)
certify('local_groupoid_interchange',h+star(t1+chi*a,t2+chi*b,a2,b2)-star(t1,t2,a+a2,b+b2))
out['local_groupoid_triple_arrow']=str(left)

# 172-192: polynomial product in the actual quotient algebra.
u,v,b1,b2,c1,c2,z=s.symbols('u1 u2 b1 b2 c1 c2 z')
GB=s.groebner([u*u+b1*u+c1,v*v+b2*v+c2],u,v,order='lex',domain=s.ZZ[b1,b2,c1,c2])
red=lambda x:s.expand(GB.reduce(s.expand(x))[1])
V=2*u*v+b2*u+b1*v; bb=b1*b2; cc=b1*b1*c2+b2*b2*c1-4*c1*c2
certify('quadratic_product_relation',red(V*V+bb*V+cc))
certify('multiplicative_discriminant',bb*bb-4*cc-(b1*b1-4*c1)*(b2*b2-4*c2))
Sg1=s.Matrix([[1,-b1],[0,-1]]);Sg2=s.Matrix([[1,-b2],[0,-1]])
T=s.eye(4)+s.kronecker_product(Sg1,Sg2)
# Tensor order 1,u2,u1,u1u2; same as LL,LM,ML,MM in preceding checks.
inc=s.Matrix([[1,0],[0,b1],[0,b2],[0,2]])
quo=s.Matrix([[2,-b2,-b1,bb],[0,0,0,1]])
certify('symmetrizer_factorization',inc*quo-T)
certify('reverse_composite_2',quo*inc-2*s.eye(2))
certify('symmetrizer_squared',T*T-2*T)
certify('duality_factor_2',inc.T*quo.T-2*s.eye(2))
out['quadratic_maps']={'tensor_basis':['1','u2','u1','u1*u2'],'i':str(inc),'q':str(quo),'T':str(T),
 'kernel_proof':'i(r+s*t)=0 iff r=0 and 2s=b1s=b2s=0',
 'split_injection_criterion':'(2,b1,b2)=R; proved by existence of a row splitting and conversely its coefficient of t'}
out['trace_duality_checks']={'adjoint_matrix':str(Sg1.T),'boundary_trace_values':['2','-b2','-b1'],
 'raw_Pro_178_literal_counterexample':'R=Q, b1=b2=0,c1=c2=1,f=u1: T(f)=0 but f-T(f)=u1 and boundary Tr(f)=0'}

# All four blocks of the pairing on the two pushouts, at chi=2.
# A generators: tensor basis followed by scalar 1_A.
# E generators: dual tensor basis followed by scalar e.
qA=quo.row_join(s.Matrix([1,0]))
qE=s.Matrix([[1,0,0,0,0],[0,b1,b2,2,1]])
H=s.zeros(5);H[:4,:4]=T.T
H[3,4]=1;H[4,0]=1
certify('integral_descended_pairing',qA.T*qE-H)
relA=s.Matrix([[1,0,0],[0,1,0],[0,0,1],[0,0,0],[-2,b2,b1]])
relE=s.Matrix([[0,0,0],[1,0,0],[0,1,0],[0,0,1],[-b1,-b2,-2]])
certify('all_A_boundary_pairings',relA.T*H)
certify('all_E_boundary_pairings',H*relE)
out['integral_pairing']={'matrix_on_presentations':str(H),'matrix_on_abstract_bases':'I_2',
 'scope':'chi=2, quadratic locally free algebras, dual rank-two modules, the specified trace pushout presentations',
 'conclusion':'perfect over every commutative base, without dividing by 2; canonical formulas make descent local-to-global',
 'not_claimed':'unqualified general-chi pushout/pullback identification or resolution of uncertain ink'}

# Generator change is checked before asserting an isomorphism/gluing.
a1,a2,r1,r2=s.symbols('a1 a2 r1 r2')
uprime=a1*u+r1;vprime=a2*v+r2
b1p=a1*b1-2*r1;b2p=a2*b2-2*r2
c1p=a1*a1*c1-a1*b1*r1+r1*r1;c2p=a2*a2*c2-a2*b2*r2+r2*r2
shift=a1*b1*r2+a2*b2*r1-2*r1*r2
Vp=2*uprime*vprime+b2p*uprime+b1p*vprime
certify('affine_generator_change',Vp-(a1*a2*V+shift))
certify('factor1_equation_change',s.expand(uprime*uprime+b1p*uprime+c1p)-a1*a1*(u*u+b1*u+c1))
certify('product_linear_coefficient_change',b1p*b2p-(a1*a2*bb-2*shift))
certify('product_constant_coefficient_change',
 b1p*b1p*c2p+b2p*b2p*c1p-4*c1p*c2p-
 ((a1*a2)**2*cc-a1*a2*bb*shift+shift**2))
out['generator_change']={'formula':str(a1*a2*z+shift),'hypothesis_for_isomorphism':'a1 and a2 units'}
beta0,ct=s.symbols('beta c')
mult=s.Matrix([[mu,-lam*ct],[lam,mu-lam*beta0]])
certify('trace_lambda_u_mu',s.trace(mult)-(2*mu-lam*beta0))
certify('norm_lambda_u_mu',mult.det()-(mu*mu-lam*mu*beta0+lam*lam*ct))
out['norm_multiplication_matrix']=str(mult)

# Finite checks from earlier notes222, repeated independently.
grids={}
for p in (2,3,5):
    counts={'tuples':0,'rank1':0,'rank2':0,'root_counts':{'0':0,'1':0,'2':0},'both_etale':0}
    for B1,C1,B2,C2 in itertools.product(range(p),repeat=4):
        counts['tuples']+=1
        rank=1 if all(x%p==0 for x in (2,B1,B2)) else 2
        counts['rank'+str(rank)]+=1
        bc=B1*B2;cc0=B1*B1*C2+B2*B2*C1-4*C1*C2
        roots=sum((x*x+bc*x+cc0)%p==0 for x in range(p))
        counts['root_counts'][str(roots)]+=1
        counts['both_etale']+=((B1*B1-4*C1)%p!=0 and (B2*B2-4*C2)%p!=0)
    grids[str(p)]=counts
out['finite_field_enumerations']=grids
out['small_ring_kernel_sizes']=[{'modulus':n,'b1':x,'b2':y,'kernel':[(r,t) for r,t in itertools.product(range(n),repeat=2) if r==0 and all(v*t%n==0 for v in (2,x,y))]}
 for n,x,y in [(4,0,0),(4,2,0),(4,1,0),(6,0,0),(6,3,0)]]
out['F2_etale_products']=[{'c1':x,'c2':y,'product_constant':(x+y)%2,'roots':[z for z in (0,1) if (z*z+z+x+y)%2==0]} for x,y in itertools.product((0,1),repeat=2)]

# Nonmathematical leaves: counts verify counts only, not their philosophical uses.
pairs=['action–inaction','activity–passivity','waking–sleep','subject–object',
 'engendering–conceiving','execution–conception','dynamism–balance','impetus–foundation',
 'ardour–perseverance','impetuosity–patience','passion–serenity','tenacity–detachment',
 'knowing facts–knowing intimately','explaining–understanding']
folios={147:'475',149:'475bis',151:'478',153:'476',155:'479',157:'486',159:'487',161:'489',163:'488',165:'477',167:'482',169:'483',171:'484',173:'491',175:'490',177:'492',179:'493',181:'494',183:'495',185:'496',187:'500',189:'497',191:'498',193:'499'}
out['editorial_counts']={'hexagrams':len(list(itertools.product((0,1),repeat=6))),
 'pairs':len(pairs),'pair_list':pairs,'typed_folios':folios,'typed_count':len(folios),
 'not_in_this_package':[v for v in range(475,501) if str(v) not in folios.values()],
 '17_October_1976_weekday':datetime.date(1976,10,17).strftime('%A')}
assert len(pairs)==14 and len(folios)==24
out['run_metadata']={'date':'2026-11-19','sympy_version':s.__version__,'scope':'exact identities and finite checks; no scan emendation'}
(W/'outputs/recomputed.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
