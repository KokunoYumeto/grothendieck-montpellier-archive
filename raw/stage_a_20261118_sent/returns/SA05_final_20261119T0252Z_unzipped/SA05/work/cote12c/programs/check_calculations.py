"""Exact checks for late cote12. Each finite computation supplements the written proof.
No source verdict is generated here. Run from the workspace root.
"""
import json, itertools, math
from pathlib import Path
import sympy as s

OUT = Path('SA05/work/cote12c/outputs')
OUT.mkdir(parents=True, exist_ok=True)
out = {}

# Localization: connected proper ambient -> two deleted points. In degree zero
# restriction is diagonal. Normalized two-line ambient has two components.
diag = s.Matrix([[1],[1]])
normal = s.eye(2)
out['two_lines'] = {'rank_restriction':diag.rank(), 'Hc1_X':2-diag.rank(),
                   'Hc1_Y':2-diag.rank(), 'Hc1_normalization':2-normal.rank(),
                   'Hc1_U':1-s.Matrix([[1]]).rank(),
                   'hypotheses':'a,b distinct smooth points, one on each line, neither the crossing; T connected, normalization disconnected'}
assert out['two_lines']['Hc1_X']==out['two_lines']['Hc1_Y']==1
assert out['two_lines']['Hc1_normalization']==out['two_lines']['Hc1_U']==0

# Pure arithmetic self-extension and the finite ramified torsion variant.
U=s.Matrix([[1,1],[0,1]]); N=U-s.eye(2)
out['unipotent']={'eigenvalues':{str(k):v for k,v in U.eigenvals().items()},
                  'rank_U_minus_1':N.rank(), 'N_squared':str(N*N),
                  'power_5':str(U**5), 'power_2_mod_2':str((U**2).applyfunc(lambda x:x%2)),
                  'nonidentity_mod_2':U!=s.eye(2)}
assert N*N==s.zeros(2) and N.rank()==1
assert (U**2).applyfunc(lambda x:x%2)==s.eye(2)

# Tate degeneration: geometric Frobenius, nonzero tame monodromy.
q=s.Integer(5); F=s.diag(1,q)
assert F*N*F.inv()==N/q
out['Tate_degeneration']={'F':str(F), 'N':str(N), 'FNF_inverse':str(F*N*F.inv()),
                         'invariant_weight':0,'coinvariant_weight':2,
                         'H1_inertia_weight_after_twist_minus1':4,
                         'proposed_weight_bound_i_n_j_1':3}

# Legendre discriminant and c4, nonconstant j, and split nodal tangent cones.
t,x,y=s.symbols('t x y')
disc=s.factor(16*s.discriminant(x*(x-1)*(x-t),x))
c4=16*(t*t-t+1); j=s.factor(c4**3/disc)
assert disc==16*t*t*(t-1)**2 and s.diff(j,t)!=0
out['Legendre']={'discriminant':str(disc),'c4':str(c4),'j':str(j),
                 'c4_at_0':str(c4.subs(t,0)), 'c4_at_1':str(c4.subs(t,1)),
                 'minus1_is_square_F5':any(a*a%5==4 for a in range(5)),
                 'tangent_at_0':'y^2=-x^2; splits over F5',
                 'tangent_at_1':'y^2=(x-1)^2; splits over F5',
                 'geometric_monodromy_input':'Deligne1980 Lemma3.5.5: nonconstant j gives SL2; hence invariants0',
                 'Hc1_weight0_subspace_dimension_at_least':2,
                 'H1_weight4_quotient_dimension_at_least':2}

# Hodge coordinates of every possible proper-stratum term in the local Leray
# sequence, for a finite range of n. The universal inequality is also written
# in the proof dossier; this enumeration is not a proof for all dimensions.
rows=[]
for n in range(1,9):
  for i in range(0,2*n+1):
    pairs=[]
    for r in range(0,min(n,i)+1):
      degree=i-r; dim=n-1 if r==0 else n-r
      lo=max(0,degree-dim); hi=min(degree,dim)
      for a in range(lo,hi+1):
        for b in range(lo,hi+1):
          if a+b<=degree:
            pairs.append((a+r,b+r,r))
    if pairs:
      lev=max(abs(a-b) for a,b,r in pairs)
      wt=max(a+b for a,b,r in pairs)
      assert lev<=min(i,2*n-1-i)
      assert wt<=2*min(i,n)
      rows.append({'n':n,'i':i,'maximum_level':lev,'bound':min(i,2*n-1-i),'maximum_weight':wt,'weight_bound':2*min(i,n)})
    else:
      rows.append({'n':n,'i':i,'terms':0})
out['local_Hodge_boxes']=rows

# Exact arithmetic on displayed tables, and elliptic/point edge tests.
n,i,p,r=s.symbols('n i p r',integer=True)
out['display_arithmetic']={
 'boundary_level':str(s.expand(2*(n-p-1)-(i-p))),
 'correct_second_weight_scan118':str(2*(i-n)+5),
 'correct_q2_level_scan118':str(2*n-i-4),
 'correct_third_weight_scan120':str(2*(i-n)+4),
 'dual_weight':str(2*n-i),
 'scan115_elliptic_literal_level':2*(1-1+0),
 'scan115_elliptic_corrected_level':2*1-1+0,
 'scan105_top_piece_elliptic_literal_bound':2*1-1-1,
 'scan105_top_piece_elliptic_actual_level':1,
 'scan120_point_literal_uniform_level':min(0,-1),
 'scan120_point_actual_level':0,
 'missing_j_point_bound':0,'missing_j_point_H1_elliptic_weight':1}

# Double blowup: independent degrees of d2. Exactness kills H1,H2;
# E2^{0,2} maps injectively to E2^{2,1}, leaving one H3 Tate summand.
intersection=s.Matrix([[-2,1],[1,-1]])
residue=s.Matrix([[1],[-1]])
out['double_blowup']={'intersection_matrix':str(intersection),'determinant':int(intersection.det()),
                     'd2_01_to_20_rank':intersection.rank(),'d2_02_to_21_rank':residue.rank(),
                     'E2_02_dim':1,'E_infty_02_dim':1-residue.rank(),
                     'H1_dim':2-intersection.rank(),'H2_dim':0,
                     'H3_dim':2-residue.rank(),'H3_weight':4,
                     'independent_abutment':'absolute purity for punctured strictly henselian regular surface: H0=Q_l,H3=Q_l(-2), other positive degrees0'}

out['SNC_type']=[{'d':d,'rank_Rd_j_at_origin':math.comb(d,d),'weight':2*d,'max_weight_if_type_d_minus1':2*d-2} for d in range(1,9)]

# Refined inverse on rectangular maps; verify all identities exactly over Q.
u=s.Matrix([[1,2,3],[2,4,6]])
v=s.Matrix([[1,0],[0,0],[0,0]])
pi=v*u; varpi=u*v
checks={'uvu=u':u*v*u==u,'vuv=v':v*u*v==v,'pi^2=pi':pi*pi==pi,
        'varpi^2=varpi':varpi*varpi==varpi,'u*pi=u':u*pi==u,
        'varpi*u=u':varpi*u==u,'pi*v=v':pi*v==v,'v*varpi=v':v*varpi==v}
assert all(checks.values())
out['generalized_inverse']={'u':str(u),'v':str(v),'pi':str(pi),'varpi':str(varpi),'identities':checks}

# Intertwiner quotient -> p' Hom p via a -> p'a p. The common annihilator
# is precisely its kernel; shown by solving a nontrivial finite model.
a,b,c,d,e,f=s.symbols('a b c d e f')
A=s.Matrix([[a,b,c],[d,e,f]])
equations=list(A*pi-varpi*A)
sol=s.linsolve(equations,(a,b,c,d,e,f))
intertwiner_dim=len(set().union(*(z.free_symbols for z in next(iter(sol)))))
images=[varpi*s.eye(2)[:,row]*s.eye(3)[col,:]*pi for row in range(2) for col in range(3)]
corner_rank=s.Matrix.hstack(*(m.reshape(6,1) for m in images)).rank()
out['corner_quotient']={'intertwiner_solution':str(sol),'intertwiner_dim':intertwiner_dim,
                        'corner_dim':corner_rank,'common_annihilator_dim':intertwiner_dim-corner_rank}

# One-way Hom counterexample without biproduct hypothesis.
e12=s.Matrix([[0,1],[0,0]])
out['additivity_needed']={'individual_End':'Q and Q, each semisimple',
                         'End_of_formal_direct_sum':'upper triangular2x2 algebra',
                         'nonzero_radical_generator':str(e12),'square':str(e12*e12)}

# Symmetrizer/antisymmetrizer on (Q^2)^{tensor3}, using exact rationals.
basis=list(itertools.product(range(2),repeat=3)); index={b:j for j,b in enumerate(basis)}
S=s.zeros(8); Alt=s.zeros(8)
for perm in itertools.permutations(range(3)):
  mat=s.zeros(8)
  for col,bv in enumerate(basis): mat[index[tuple(bv[perm[k]] for k in range(3))],col]=1
  sign=(-1)**sum(perm[a]>perm[b] for a in range(3) for b in range(a+1,3))
  S+=mat/s.Integer(6); Alt+=sign*mat/s.Integer(6)
assert S*S==S and Alt*Alt==Alt
out['Schur']={'symmetrizer_rank':S.rank(),'antisymmetrizer_rank':Alt.rank(),
              'both_idempotent':True,'denominator':6,'char_restriction':'division by r! requires r! invertible'}

# Lefschetz P1 test and Jacobian scalar map.
L=s.Matrix([[0,0],[1,0]]); W=s.diag(0,2); H=s.diag(-1,1)
assert H*L-L*H==2*L and W*L-L*W==2*L
out['P1']={'L':str(L),'Cartan':str(H),'weight_grading':str(W),'Cartan_plus_identity_equals_weight':H+s.eye(2)==W,
           'L_kills_unit':L*s.Matrix([1,0])==s.zeros(2,1),'L_commutes_with_weight':W*L==L*W}
J=s.Matrix([[0,1],[-1,0]])
out['Jacobian_times2']={'polarization_multiplier':4,'matrix_check':(2*s.eye(2)).T*J*(2*s.eye(2))==4*J}

primes=list(s.primerange(2,40))
out['lattice_system']={'sample_primes':primes,'hom_contains':[str(s.Rational(1,l)) for l in primes],
                       'proof_of_nonfinite_generation':'Any finite generating set has one common denominator D; choose a prime l not dividing D. Then1/l is in Hom but not in that generated subgroup.',
                       'scope':'counterexample only to weakened axiom lacking a fixed almost-all-prime reference lattice'}
out['torsion_nonrigidity']={'Hom_Z_Zmodl_to_Z':0,'nonzero_object':'Z/l','triangle_identity_possible':False}
out['Vasiu_Zink_ring']=[{'p':p,'dimension':2,'ramification_index':2*(p-1),'positive_threshold':p-1,
                        'm_generators':'x,y','relation':f'p=(xy)^{p-1}','p_not_in_m_power_p':2*(p-1)<p} for p in [2,3,5,7]]

# Root-owned K12-06 auxiliary arithmetic alarm.
out['zero_eigenvalue_loss']={'characteristic_polynomial':'t','reciprocal':'1','L_series':'1',
                            'trace_series':'0','dimension_class':1,'injectivity_N_category':False}

(OUT/'calculations.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('All exact assertions passed; '+str(len(out))+' calculation families saved.')
for name in out: print(name)
