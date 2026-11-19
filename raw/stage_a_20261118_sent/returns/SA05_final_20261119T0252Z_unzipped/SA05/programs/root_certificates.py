#!/usr/bin/env python3
"""Exact finite calculations for the root review, not automatic manuscript verdicts.

Geometric hypotheses and proofs of applicability are in root_checks.md.  These
calculations certify linear algebra, indices, and finite examples only.
"""
import json
from collections import Counter
from itertools import combinations
from pathlib import Path
import sympy as s

OUT=Path(__file__).resolve().parent/'outputs'/'root_certificates.json'
t=s.symbols('t')
cert={}

H=s.diag(1,-1); L=s.Matrix([[0,1],[0,0]])
cert['central_weight']={'H':H.tolist(),'L':L.tolist(),'commutator':(H*L-L*H).tolist(),'equals_2L':H*L-L*H==2*L,
 'real_invariant_not_positive':{'form':H.tolist(),'values_on_basis':[1,-1]}}

types=[(1,0),(0,1)]
endtypes=Counter((a-c,b-d) for a,b in types for c,d in types)
cert['weight_zero_not_trivial']={str(k):v for k,v in sorted(endtypes.items())}
cert['twist_and_level']=[{'object':'1','weight':0,'early_D_level':0},
 {'object':'Q(-1)','weight':2,'early_D_level':0},
 {'object':'h^1(E)','weight':1,'early_D_level':1}]
wi,wn,rr=s.symbols('i n r',integer=True)
cert['twist_arithmetic']={
 'literal_result':str(s.expand(wi-2*((wn-wi)/2))),
 'corrected_result':str(s.simplify(wi-2*((wi-wn)/2))),
 'pairing_target_Q_minus_rho_weight':str(s.expand(-2*(-rr))),
 'Tate_module_weight':1-2,
 'P1_top_weight_exceeds_dimension':2>1,
 'parity_preserved_samples':all((w-2*r)%2==w%2 for w in range(-5,6) for r in range(-5,6)),
 'Euler_reindex_identity_samples':all((-1)**j==(-1)**rho*(-1)**(j+rho) for j in range(6) for rho in range(6))}
sigma={0:{'1'},1:{'h1'},2:{'L','primitive2'}}
cert['primitive_alpha_zero']={str(i):sorted(v-v) for i,v in sigma.items()}

I=s.eye(2); J=s.Matrix([[1,1],[0,1]]); Z=s.zeros(1)
cert['endomorphism_L']={
 'zero_class_rank':1,'zero_L':str(1/(s.eye(1)-t*Z).det()),
 'identity_L':str(1/(I-t*I).det()),'jordan_L':str(1/(I-t*J).det()),
 'jordan_nontrivial':J!=I,'jordan_powers_1_to_5':[(J**n).tolist() for n in range(1,6)],
 'same_power_traces':[s.trace(I**n)==s.trace(J**n) for n in range(1,7)],
 'exterior_series':str((I+t*I).det()),'symmetric_series':str(1/(I-t*I).det())}
cert['ghost_characteristic_p']=[]
for p in [2,3,5,7]:
 den=s.Poly((1-t)**p,t,modulus=p)
 expected=s.Poly(1-t**p,t,modulus=p)
 assert den==expected
 derivative=s.Poly(s.diff(den.as_expr(),t),t,modulus=p)
 assert derivative.is_zero
 cert['ghost_characteristic_p'].append({'p':p,'denominator_mod_p':str(den.as_expr()),
  'binomial_identity_verified':den==expected,'derivative_mod_p':str(derivative.as_expr()),
  'not_unit_series_coefficient_at_p':1})
cert['trace_identity']={'series':str(s.series(t*s.diff(1/(I-t*J).det(),t)/(1/(I-t*J).det()),t,0,7)),
 'power_traces':[int(s.trace(J**n)) for n in range(1,7)]}

def commutant_dim(generators):
    n=generators[0].rows
    vs=s.symbols('v:'+str(n*n)); X=s.Matrix(n,n,vs)
    eq=[e for G in generators for e in X*G-G*X]
    A,_=s.linear_eq_to_matrix(eq,vs)
    return n*n-A.rank()
E12=s.Matrix([[0,1],[0,0]]); E21=E12.T
cert['commutants']={'SL2_standard_commutant_dimension':commutant_dim([s.eye(2)+E12,s.eye(2)+E21]),
 'GL2_standard_commutant_dimension':commutant_dim([s.eye(2)+E12,s.eye(2)+E21,s.diag(2,1)]),
 'both_associative_envelopes_have_dimension':s.Matrix.hstack(*[s.Matrix(M).reshape(4,1) for M in [E12,E21,E12*E21,E21*E12]]).rank()}

F=s.Matrix([[0,-5],[1,1]])
cert['frobenius_analytic_vs_algebraic']={'matrix':F.tolist(),'charpoly':str(F.charpoly(t).as_expr()),
 'discriminant':int(s.discriminant(F.charpoly(t).as_expr(),t)),
 'trace':int(s.trace(F)),'determinant':int(F.det()),
 'claim_limit':'Multiplicity independence uses the ideal argument in root_checks.md; no numerical logarithm certifies it.'}
cert['HS_invariants_coinvariants']={name:{'kernel_dim':len((M-s.eye(M.rows)).nullspace()),
 'cokernel_dim':M.rows-(M-s.eye(M.rows)).rank(),
 'invariants_map_to_coinvariants_rank':s.Matrix.hstack(M-s.eye(M.rows),*[(v) for v in (M-s.eye(M.rows)).nullspace()]).rank()-(M-s.eye(M.rows)).rank()}
 for name,M in [('semisimple',s.diag(1,2)),('unipotent',J)]}
cert['absolute_odd_restriction']={'unit_over_Fq_degrees':[0,1],
 'restriction_multipliers':[1,2,3,4,5],
 'colimit_over_Q':'Q, since all positive integer restriction multipliers are invertible',
 'geometric_etale_H1_unit':'0; not the same colimit construction'}
cert['weight_intervals']=[{'i':i,'rho_allowed_by_two_written_inequalities':[r for r in range(-2*i-2,3)
 if (r+i-1<=0<=r+2*i-2) or (r+i<=0<=r+2*i)]} for i in range(1,7)]

def legendre_symbol(x,p):
    x%=p
    return 0 if x==0 else (1 if pow(x,(p-1)//2,p)==1 else -1)
leg=[]
for p in [5,7,13,17,29]:
    counts={a:1+sum(1+legendre_symbol(x*(x-1)*(x-a),p) for x in range(p)) for a in range(2,p)}
    traces={a:p+1-N for a,N in counts.items()}
    epsilon=1 if p%4==1 else 0
    leg.append({'p':p,'fiber_counts':counts,'sum_frobenius_traces':sum(traces.values()),
     'Hc1_trace':-sum(traces.values()),'predicted_Hc1_trace':2*epsilon,
     'total_points':sum(counts.values()),'predicted_total':p*p-p-2+2*epsilon,
     'match':sum(counts.values())==p*p-p-2+2*epsilon})
cert['legendre_point_counts']=leg

def cech_differential(n_vertices,p,q):
    """Restriction on H^q of intersections of coordinate planes in P^3."""
    src=[I for I in combinations(range(n_vertices),p+1) if q%2==0 and q<=2*(2-p)]
    dst=[I for I in combinations(range(n_vertices),p+2) if q%2==0 and q<=2*(1-p)]
    M=s.zeros(len(dst),len(src))
    for r,Jset in enumerate(dst):
        for j in range(len(Jset)):
            Iset=Jset[:j]+Jset[j+1:]
            if Iset in src: M[r,src.index(Iset)]=(-1)**j
    return M,src,dst
rows=[]; coho=Counter()
for q in [0,2,4]:
    d0,src,dst=cech_differential(4,0,q); d1,_,end=cech_differential(4,1,q)
    assert d1*d0==s.zeros(d1.rows,d0.cols)
    dims=[len(src),len(dst),len(end)]
    ranks=[d0.rank(),d1.rank()]
    hs=[dims[0]-ranks[0],dims[1]-ranks[0]-ranks[1],dims[2]-ranks[1]]
    rows.append({'q':q,'dimensions':dims,'differentials':[d0.tolist(),d1.tolist()],
     'ranks':ranks,'cohomology_dimensions':hs})
    for p,v in enumerate(hs):
        if v:coho[(p+q,q)]+=v
xcoho=Counter(coho)
for (degree,weight),v in coho.items():xcoho[(degree+2,weight+2)]+=v
cert['SNC_singular_counterexample']={'cech_rows':rows,
 'D_geometric_cohomology_degree_weight':{str(k):int(v) for k,v in sorted(coho.items())},
 'X_D_times_P1_degree_weight':{str(k):int(v) for k,v in sorted(xcoho.items())},
 'H4_arithmetic_X_Ql1_dimension':int(xcoho[(3,2)]+xcoho[(4,2)]),
 'hypotheses':'D is four coordinate planes in P3 over Fq, X=D×P1, proper finite type, ell != char(Fq), singular.'}

cert['brauer_residue_rank']=[{'removed_closed_points':r,'sum_matrix':s.ones(1,r).tolist(),
 'sum_matrix_rank':s.ones(1,r).rank(),'kernel_corank':len(s.ones(1,r).nullspace())} for r in range(1,7)]
cert['lattice_H1']={'M':'Z with trivial continuous action of Zhat','H1_continuous':0,
 'invariants_M_tensor_QmodZ':'Q/Z','missing_quotient_image':'Q maps onto Q/Z'}
cert['curve_and_surface_tests']={
 'genus2_possible_degrees_with_R_nonnegative':[d for d in range(1,10) if 2-2*d>=0],
 'Enriques_Betti':[1,0,10,0,1],
 'supersingular_E2_b2':int(s.binomial(4,2)),
 'supersingular_E2_b1':4,
 'warning':'The geometry establishing these examples is checked separately; b1=4 prevents using E×E as an all-positive-invariants-vanish example.'}
cert['duality_shift']={'regular_immersion_codimension_d':'Ri!1=1(-d)[-2d]',
 'finite_field_absolute_pairing':'H^i(Fq,V) dual to H^(1-i)(Fq,V*)',
 'finite_type_regular_dimension_n_proposed_shift':'2n+1; arithmetic duality needs its stated cohomology theory and support convention'}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(cert,ensure_ascii=False,indent=2,default=lambda v:int(v))+'\n')
print(json.dumps({'certificate_file':str(OUT),'families':len(cert),'SNC_H4_dimension':cert['SNC_singular_counterexample']['H4_arithmetic_X_Ql1_dimension'],'Legendre_examples_verified':all(x['match'] for x in leg)},indent=2))
