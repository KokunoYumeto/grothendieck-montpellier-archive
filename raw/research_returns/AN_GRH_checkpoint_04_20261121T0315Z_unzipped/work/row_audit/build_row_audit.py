#!/usr/bin/env python3
"""Reproducible text/register audit; no assertion of proof validity from keywords.

The curated entries below record the analytical dependence actually inspected.
The graph columns record register dependencies, not a reconstructed proof DAG.
"""
from pathlib import Path
import csv, collections, hashlib, json, re, shutil

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'work/row_audit'
SOURCE=ROOT/'source'
DATE='2026-11-21'
WHO='GPT-6 Astra Pro; effort not exposed; AN_GRH /root/row_audit'
RUNS={
 'ANABELIAN_A1':('recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_results.csv',121,'recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_paper.tex'),
 'ANABELIAN_SUCCESSOR':('recovered/ANABELIAN_SUCCESSOR_final_text/ANABELIAN_SUCCESSOR_results.csv',157,'recovered/ANABELIAN_SUCCESSOR_final_text/ANABELIAN_SUCCESSOR_paper.tex'),
 'LM7_PUSH':('recovered/DELTA_GT_text/LM7_PUSH/LM7_PUSH_results.csv',218,'recovered/DELTA_GT_text/LM7_PUSH/*.tex'),
 'LM8_PUSH':('recovered/LM8_PUSH_cp17_text/LM8_PUSH_results.csv',304,'recovered/LM8_PUSH_cp17_text/sections/*.tex'),
}
EXPECTED={**{k:v[1] for k,v in RUNS.items()},'ANABELIAN_A1_SUCCESSOR':210,'GT_TOWER_CHECK':180}
regs={r:list(csv.DictReader((ROOT/p).open())) for r,(p,_,_) in RUNS.items()}
reg_by={(r,x['id']):x for r,rs in regs.items() for x in rs}
blocks=collections.defaultdict(list)
term_hits=[]
term_rx=re.compile(r'GRH|Chebotarev|Dirichlet|Hooley|primitive[-\s]+root|least[-\s]+prime|Artin|Riemann|WeilCurves|WeilII|open.image|Faltings',re.I)
for run,(_,_,pattern) in RUNS.items():
 for p in sorted(ROOT.glob(pattern)):
  lines=p.read_text().splitlines()
  starts=[]
  for i,line in enumerate(lines):
   m=re.search(r'\\begin\{(?:claim|statement)\}\{([^}]+)\}',line)
   if m: starts.append((i,m[1]))
  for j,(start,id_) in enumerate(starts):
   stop=starts[j+1][0] if j+1<len(starts) else len(lines)
   loc=f'{p.relative_to(ROOT)}:{start+1}'
   text='\n'.join(lines[start:stop])
   blocks[(run,id_)].append((loc,text))
   for n,line in enumerate(lines[start:stop],start+1):
    hit=term_rx.search(line)
    if hit:
     term_hits.append(dict(run=run,row_id=id_,file=str(p.relative_to(ROOT)),line=n,term=hit[0],context=line.strip(),scope='Mechanical source text hit; not automatically an analytic dependency.'))

def clean(v):
 return str(v).replace('\r','\\r').replace('\n','\\n').replace('\t','\\t')
def write_tsv(name,rows,fields=None):
 rows=list(rows)
 if fields is None: fields=list(rows[0]) if rows else []
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n',extrasaction='ignore')
  w.writeheader()
  for row in rows:w.writerow({k:clean(row.get(k,'')) for k in fields})
def loc(run,id_):
 return '; '.join(x[0] for x in blocks.get((run,id_),[])) or (reg_by.get((run,id_),{}).get('where_proved','')+' [proof not recovered]')

curated=[]
def add(run,ids,kind,operation,field,family,alp,mas,gap='',evidence='Available statement/proof read for this analytic input; no claim that every other step was re-proved.',seed=False):
 for id_ in ids.split():
  curated.append(dict(audit_id=f'ROW-{run}-{id_}',run=run,row_id=id_,audit_kind=kind,operation=operation,
   exact_finite_field_or_object=field,L_functions=family,under_Alpoge_Dirichlet_GRH=alp,under_Masullo_all_field_Hecke_GRH=mas,
   missing_theorem_or_data=gap,source_locator=loc(run,id_),evidence_scope=evidence,
   analytic_dependency_seed='yes' if seed else 'no',source_status=reg_by.get((run,id_),{}).get('status','excerpt only; see original source'),
   date=DATE,who=WHO))

NONE='No number-field L-function is required for the stated use.'
ALREADY='Analytic input already unconditional; this hypothesis changes no existence conclusion.'
NOTFIX='Neither hypothesis supplies the stated geometric or inverse-limit existence theorem.'
FF='Finite-field L(C,chi,T)=det(1-Frob_q*T | H^1(C_bar, L_chi)); for nontrivial finite-order rank-one chi, reciprocal roots have absolute value sqrt(q). This is not a number-field Dirichlet/Hecke L-function.'
PRIM='For fixed p,ell the condition ord_ell(p)=ell-1 is a finite check. If one additionally asks for infinitely many such ell: zeta_{Q(zeta_n,p^(1/n))}(s), all squarefree n, is Hooley\'s required family.'
PRIM_ALP='The stated finite-prime criterion needs no GRH. Dirichlet GRH alone does not supply the additional Artin existence assertion.'
PRIM_MAS='The stated finite-prime criterion needs no GRH. The stipulated all-field Hecke GRH supplies Hooley\'s arithmetic primitive-root theorem, but not the simultaneous geometric conditions.'
GEO_GAP='Need, for every pointed curve (C,P), a prime ell and a first-field P-split cyclic cover for which every nontrivial finite-field twisted L-value at T=1 is a p-adic unit. Arithmetic prime density alone gives no intersection with this curve-dependent set.'

add('ANABELIAN_A1','A.15','FINITE_FIELD_WEIL_PURITY','Separate proper H^1 and boundary/Tate Frobenius weights in affine covers.','Finite covers of C minus P over finite fields; proper H^1 and boundary modules.',FF,ALREADY,ALREADY,evidence='A.15 proof and cited Deligne Weil I (1.5.1),(1.6) read for the weight input. Parent audits the nonanalytic point-separation chain.')
add('ANABELIAN_A1','B.2','FINITE_FIELD_CHARACTER_TEST','Relative class-number criterion via finite-character factors.','P-split Lang cover D/C attached to a finite prime-to-p quotient A of J_C(F_q).',FF,ALREADY,ALREADY)
add('ANABELIAN_A1','B.3','FINITE_FIELD_PURITY_AND_FIXED_PRIMITIVE_ROOT','Corrected second-moment pair bound and a genus-two conditional criterion.','Finite rank-one character sheaves on C/F_q; fixed p,ell and J_C(F_q) quotient.',FF+' '+PRIM,PRIM_ALP,PRIM_MAS,GEO_GAP)
add('ANABELIAN_A1','B.4','FINITE_PRIME_DECISION_NOT_PRIME_BOUND','Decide existence for one fixed ell over all constant extensions using first Frobenius periods.','Finite Frobenius action on H^1_et(C_bar,F_ell), and coherent/etale p-torsion of each finite cover.',NONE,ALREADY,ALREADY,'A terminating test for each fixed ell is not a bound on the search over ell.')
add('ANABELIAN_A1','B.5 B.32','GEOMETRIC_PRIME_SEARCH_OPEN','Existence or least witness prime over all constant extensions remains open.','Curve-dependent first-field Lang covers and finite-field twisted L-values.',FF,NOTFIX,NOTFIX,GEO_GAP)
add('ANABELIAN_A1','B.23','FINITE_CERTIFICATE_COUNTEREXAMPLE','Supersingular genus-two counterexample to nontrivial odd cyclic cover with p-rank-zero primitive part.','Explicit C/F_(2^38), conductor reduction to n=191,229, and polynomial Bezout certificates over F_(2^38).',NONE,ALREADY,ALREADY,'Degree-one convention is separate: B.24 remains open and permits the trivial cover. Parent checks the geometric argument.',evidence='Retained conductor enumeration and retained independent composition/Bezout verifier rerun successfully in this session; full proof read but geometric proof review belongs to parent.')
add('ANABELIAN_A1','B.24','GEOMETRIC_EXISTENCE_OPEN','Literal odd-degree cover existence allowing degree one.','Primitive Jacobian parts of cyclic etale covers of arbitrary C over F_p_bar.',NONE,NOTFIX,NOTFIX,'Need a theorem producing such a cover when the base itself has positive p-rank. B.23 refutes the nontrivial-cover universal version, not this degree-one-permitted version.')
add('ANABELIAN_A1','B.27','EXACT_FINITE_MINIMUM','Least witness prime is 191 for one fixed marked curve; first constant degrees ten for191 and four for229.','Specified C/F_(2^38), scalar Frobenius and finite orders; finite witnesses in B.26.',NONE,ALREADY,ALREADY,'This is a fixed-curve finite minimality proof, not an effective Chebotarev theorem.')
add('ANABELIAN_A1','B.28','FINITE_MULTIPLICATIVE_ORDER','Bound bad constant twists by (g-1)(ell-1)/ord_ell(p).','Fixed cyclic cover and eigenspaces of its finite deck group.',NONE,ALREADY,ALREADY,'No Artin existence claim is made. Large multiplicative order alone can be obtained by excluding finitely many prime divisors of p^j-1; prescribed-point control remains absent.')
add('ANABELIAN_A1','B.29','FINITE_FIELD_WEIL_BOUND','Count good base points after sufficient constant extension using Weil.','Curves D/F_q of genus1+ell(g-1), and fixed cover twists.',FF,ALREADY,ALREADY,'The base point is unspecified; this does not establish B.5 for every prescribed P.')
add('ANABELIAN_A1','B.30','EXACT_FINITE_MINIMUM','Specified F3 plane quartic has least odd witness prime5 and first field F_(3^8).','Finite Frobenius and Cartier certificates for the given quartic.',NONE,ALREADY,ALREADY)
add('ANABELIAN_A1','B.34','EXACT_FINITE_FIELD_FIRST_MINIMUM','Specified F5 quartic has least constant degree3; at that field least prime13.','Finite Jacobian orders and Cartier certificates; the all-extension least prime is not determined.',NONE,ALREADY,ALREADY,'Do not convert a field-first minimum into the global least prime over every constant extension.')
add('ANABELIAN_A1','B.35','FINITE_FIELD_WEIL_BOUND','Produce a point on a geometrically connected fibre product after large finite extension.','Finite-field fibre-product curve and ordinary elliptic prime-to-p isogeny data.',FF,ALREADY,ALREADY)
add('ANABELIAN_A1','B.42','FINITE_MULTIPLICATIVE_ORDER','Use even ord_ell(2) for a given tame cyclic cover.','Specified finite cyclic cover and Hermitian target.',NONE,ALREADY,ALREADY,'The stated conditional cover argument does not require infinitely many primitive-root primes.')

add('ANABELIAN_SUCCESSOR','A.8 A.10 A.35','FIXED_PRIMITIVE_ROOT_HYPOTHESIS','Use irreducibility of Phi_ell over F_p, or a finite multiplicative-order hypothesis.','Fixed prime p and fixed odd ell; finite Fourier inversion in F_p[Z/ell].',PRIM,PRIM_ALP,PRIM_MAS,GEO_GAP)
add('ANABELIAN_SUCCESSOR','A.11','FINITE_FIELD_WEIL_PURITY','Corrected character-sum pair estimate.','Finite rank-one sheaves on C/F_q.',FF,ALREADY,ALREADY,'Numerical inequalities must actually conflict; p>(2g-2)^2 and quotient size alone do not prove existence.')
add('ANABELIAN_SUCCESSOR','A.12','FINITE_COUNTEREXAMPLE_WITH_PRIMITIVE_ROOT','Refute a genus-two point-only test in genus three, even when2 is primitive modulo3.','C/F2:y^2+y=x^7+x^3, fixed ell=3; twisted polynomial 1+2T+3T^2+4T^3+4T^4.',NONE,ALREADY,ALREADY)
add('ANABELIAN_SUCCESSOR','A.15','GEOMETRIC_PRIME_SEARCH_OPEN','Universal nontrivial rational class-number witness existence remains open.','P-split Lang cyclic covers with all L_P(chi^i,1) p-adic units.',FF,NOTFIX,NOTFIX,GEO_GAP)
add('ANABELIAN_SUCCESSOR','A.16','NO_UNIFORM_GEOMETRIC_PRIME_BOUND','For every finite set of primes, an ordinary pointed curve excludes all of them over every constant extension.','Curve-dependent finite-prime obstructions.',NONE,ALREADY,ALREADY,'No bound depending only on(p,g) follows; a quantitative bound would need additional curve data and an existence theorem.')
add('ANABELIAN_SUCCESSOR','A.17','FIXED_PRIMITIVE_ROOT_HYPOTHESIS','Use ord_ell(2)=ell-1 with scalar Frobenius and ordinariness to obstruct all extensions.','Fixed odd ell and specified geometric cyclic covers.',PRIM,PRIM_ALP,PRIM_MAS,'The hypotheses produce an obstruction, not a prime-producing theorem.')
add('ANABELIAN_SUCCESSOR','A.19 A.24 A.31 A.72 A.74 A.91 A.92 A.93 A.95','EXACT_FINITE_MINIMUM_OR_CENSUS','Fixed-curve or finite-census small-prime exclusions and witnesses.','Explicit finite-field models, finite constant extensions, and finite Cartier/Frobenius tests.',NONE,ALREADY,ALREADY,'Least-prime assertions hold only for the specified pairs/subsets; rowsA.74,A.91 explicitly leave other pairs unresolved.')
add('ANABELIAN_SUCCESSOR','A.36 A.41 A.44 A.77 A.80','FINITE_MULTIPLICATIVE_ORDER','Scalar-Frobenius obstructions, conductor bounds, or valuation criteria at given primes/conductors.','Finite deck characters, ord_ell(p) or ord_n(2), and finite-field Frobenius.',NONE,ALREADY,ALREADY,'No primitive-root distribution theorem or analytic least-prime estimate is used.')
add('ANABELIAN_SUCCESSOR','A.38','GEOMETRIC_CHEBOTAREV_LIMITATION','Explicitly distinguish finite-field closed-point Chebotarev from prime-order theta avoidance.','Finite etale covers of a finite-field parameter space U; closed points of U.',FF,ALREADY,ALREADY,'Need prime-order points whose entire nonzero cyclic orbit satisfies the required theta avoidance/nonavoidance condition. Chebotarev for closed points does not supply it.')
add('ANABELIAN_SUCCESSOR','A.45 A.83 A.84','PURITY_NOT_SUFFICIENT_FOR_GEOMETRIC_UNIFORMITY','Counterexamples to excessive inferences from integrality, weight one, and bounded p-parts.','Weight-one Frobenius systems and specified geometric families.',FF,ALREADY,ALREADY,'Number-field GRH does not supply the missing geometric uniformity.')
add('ANABELIAN_SUCCESSOR','A.96','GEOMETRIC_PRIME_SEARCH_OPEN','Unresolved all-extension least primes outside proved finite subfamilies.','Remaining pointed finite-field quartics/genus-two pairs.',FF,NOTFIX,NOTFIX,GEO_GAP)

add('LM7_PUSH','A.16','QUALITATIVE_NONABELIAN_PRIME_DENSITY','Density2/9 of q≡4,7(mod9) for which3 is not a cube modq.','M=Q(zeta_9,3^(1/3)); [M:Q]=18. The conjugacy-stable predicate is nontrivial in both cubic factors over Q(zeta_3).','zeta_M(s); equivalently finite-order Hecke factors over Q(zeta_3) of M/Q(zeta_3).',ALREADY+' A least-prime strengthening is not supplied by Dirichlet GRH alone.',ALREADY+' A least-prime strengthening lies in the stipulated Hecke family.','Original proof missing; exact field reconstructed independently from the displayed arithmetic predicate. This does not verify the separate pro-three presentation.',evidence='Full register statement/dependencies available; A_agent.tex proof missing. The degree18 field and predicate calculation were reconstructed in this audit.',seed=True)
add('LM7_PUSH','A.25','QUALITATIVE_ARITHMETIC_PROGRESSION','Density1/3 of q≡2,5(mod9); union withA.16 has density5/9.','Q(zeta_9), Frobenius residue2 or5.','Dirichlet L(s,chi), chi modulo9; zeta_Q(zeta_9) factorization.',ALREADY+' Quantitative AP prime selection is within Dirichlet GRH.',ALREADY+' Same quantitative AP consequence.','Original proof missing; no recheck of the separate arithmetic group presentation.',evidence='Full register statement read. The density of the displayed residue classes is the unconditional Dirichlet/Chebotarev consequence.',seed=True)
add('LM7_PUSH','A.43 B.6','FINITE_ARITHMETIC_ENUMERATION','At each fixed depth enumerate fields of bounded degree, bounded ramification, and explicit discriminant bound.','F_n splits the finite action; K_n also splits target graph(s_n,rho_A_n); Omega_n is compositum of bounded-degree extensions of Q containing K_n and unramified outsideS_n.',NONE,ALREADY,ALREADY,'The register explicitly asserts no uniform finite stopping rule for every positive inverse-limit instance. Effective Chebotarev alone cannot supply a depth bound.',evidence='Full register statements read; the source proofs A_agent.tex/B_agent.tex are not recovered.')

# Main-source qualitative prime-selection inputs of LM8.
def cheb(ids,operation,field,gap='',evidence='Available full proof read for the exact finite-image Chebotarev use; other proof steps not re-proved.'):
 add('LM8_PUSH',ids,'QUALITATIVE_CHEBOTAREV',operation,field,
 'For quantitative rational-prime selection: zeta_L(s) and zeta_Q(s), where L is the stated finite Galois field over Q (or Q-normal closure). With excluded primes S use zeta_{L(sqrt(rad(2*prod(S))))}(s) and zeta_Q(s) for the explicit bound in Finding G01.',
 ALREADY+' A general nonabelian least-prime version is not covered by Dirichlet GRH alone.',
 ALREADY+' The stipulated all-field Hecke GRH supplies the Dedekind-zeta hypotheses for a least-prime version.',gap,evidence,True)
cheb('A.16','Positive density of rational primes with complex-conjugation Frobenius class.','M/Q finite Galois containing the actual normalizer field L; target Cl(c) in Gal(M/Q).')
cheb('A.20','Split/inert quadratic prime sets refute an invalid density-intersection inference.','Any nontrivial quadratic extension L/K; targets identity versus nonidentity in Gal(L/K). For quantitative rational-prime bounds use the Q-normal closure.','Both sets have positive prime-ideal density overK but are disjoint. ChoosingK=Q gives an elementary Dirichlet-family instance. The logical counterexample is already unconditional.')
cheb('B.20 B.22','Hilbert specialization followed by a degree-one prime of a finite torsor fibre.','Choose characteristic finite quotient Q (metabelian inB.20, finite quotient of S_m inB.22), Galois-close the coefficient/deck-constant field K, choose a Hilbert point a; L is the Q-normal closure of the specialized Q-torsor fibre.','A bound applies after Q,K,a are explicit. GRH does not provide a uniform separating-quotient depth or Hilbert specialization height.')
cheb('D.11','Detect a nontrivial finite reduction of an infinite compact linear image.','L_{M,k}/L is fixed field of ker(rho_{M(-1)} mod ell^(k+1)); use its Q-normal closure for a rational-prime bound.','The finite precision k must already have been chosen; no uniform k is supplied by GRH.')
cheb('D.8','Infinitely many completely splitting primes in a fixed elliptic five-division field.','Q(E_c[5],mu_5), with E_c the stated elliptic curve; target identity.')
cheb('D.3 D.28','Choose each q_r in a specified actual Heisenberg Frobenius class with v5(q_r+1)=r.','L_r=Qbar^ker(g -> (s_0(g) mod5, chi_5(g) mod5^(r+1))); finite image in H_5 semidirect (Z/5^(r+1))^times, H_5 of order125. Target(exp C,-1+5^r).','Each stage has a finite prime bound after its actual representation is specified; no uniform bound on the whole infinite prime sequence follows.')
cheb('D.44 D.48 D.62 D.63 D.65','Construct infinitely many split-prime residue classes and a nonzero lim1.','Joint splitting field of actual action rho_{s,r} on W_r=A_s/m^r A_s and chi_5 mod5^r; D.63 usesr+1. Target identity. D.65 explicitly inheritsD.48.','The field and excluded set vary with coefficient precision; effective stagewise choice is not a finite decision for an infinite tower.')
cheb('D.60 D.61 D.66','Separate a finite additive cocycle nonzero on its action kernel.','L_{s,r,z}=Qbar^ker(g -> (z(g),rho_{s,r}(g))) with actual finite affine image W_r semidirect im(rho_{s,r}); target(z(delta),1), rho(delta)=1,z(delta)≠0.','The finite action and actual cocycle must be specified. In Baire constructions this remains a stagewise effective enhancement.')
cheb('D.67 D.69 D.71 D.73','Separate a nonabelian finite cocycle via its actual affine image.','Finite coefficient group H_r (H_m inD.73), actual action rho_{a,r}, and L=base_bar^ker(g -> (z(g),rho_{a,r}(g))) in H_r semidirect im(rho); target(z(delta),1), z(delta)≠1. D.71 inheritsD.70.','Use the Q-normal closure when the base is a number field. No arbitrary formal affine group may replace the actual image.')
cheb('D.70','Finite affine witnesses over an arbitrary number field; no principal-prime restriction.','Over k, L_{a,r,z}=kbar^ker(g -> (z(g),rho_{a,r}(g))); use Q-normal closure for rational primes. Principal divisors h*v are used only after choosing the prime.','The class-number multiplier h affects the required local coefficient depth, not the Chebotarev target existence.')
cheb('D.78 D.79 D.80 D.81 D.82 D.83 D.84 D.85 D.86 D.87','Force finite Cartier-dual cocycles to descend to the actual operator image; detect local/global triviality.','At each original finite coefficient module W (Cartier dual in the finite-Sha applications), L_{s,W,z}=Qbar^ker(g -> (z(g),rho_{s,W}(g))); target nonzero translation with identity linear part.','RowsD.79–D.82,D.84–D.86 explicitly reuse the finite affine argument. Only finite coefficient instances acquire a least-prime bound.')
add('LM8_PUSH','C.30','QUALITATIVE_ARITHMETIC_PROGRESSION','Infinitely many primes p≡5(mod12) for independent beta-defect characters.','Q(zeta_12), target5.','Dirichlet L(s,chi) for chi modulo12.',ALREADY+' Quantitative prime selection is within Dirichlet GRH.',ALREADY+' Same quantitative AP consequence.',seed=True)
add('LM8_PUSH','D.1','QUALITATIVE_ARITHMETIC_PROGRESSION','Choose q_r≡1(mod5^r) in a lim1 construction.','Q(zeta_(5^r)), target1.','Dirichlet L(s,chi) for chi modulo5^r.',ALREADY+' Each quantitative stage is within Dirichlet GRH.',ALREADY+' Same stagewise AP consequence.','The growing infinite prime sequence has no single finite stopping bound.',seed=True)
add('LM8_PUSH','D.58','QUALITATIVE_ARITHMETIC_PROGRESSION','Choose q≡17(mod30) outside the primes dividingc.','Q(zeta_30), target17, with finite excluded set.','Dirichlet L(s,chi) for chi modulo30; finite exclusions can be built into an enlarged cyclotomic modulus.',ALREADY+' Quantitative AP prime selection is within Dirichlet GRH.',ALREADY+' Same quantitative AP consequence.',seed=True)
add('LM8_PUSH','E.1 E.2','QUALITATIVE_CM_RAY_CLASS_CHEBOTAREV','Realize every required ray-class residue in the orbit of a generator P of E_6[12].','K=Q(i); K(P)/K is finite abelian of degree16 by the stated CM calculation. Use the Q-normal closure for rational prime bounds.','Finite-order Hecke L_K(s,chi) for characters of Gal(K(P)/K), or zeta_K(P)(s); not generally Dirichlet characters overQ.',ALREADY+' Dirichlet GRH alone does not give the general quantitative CM prime statement.',ALREADY+' Quantitative ray-class Chebotarev is within all-field Hecke GRH.','Original use is qualitative; no new class-number computation or L-value nonvanishing theorem follows merely from GRH.',seed=True)
add('LM8_PUSH','A.32 A.33','QUALITATIVE_SERRE_OPEN_IMAGE','Use openness of the non-CM elliptic Tate-module image and Zariski density of the commutator.','F_a/Q: y^2=x^3-3x+a, a=6 or -6; j=-216; rad(2N_Fa)=6. The recovered proof then restricts rho_{F_a,ell} to its chosen finite number field L; A.33 explicitly reuses the same F_a and A.32 Serre argument.','The original qualitative Serre input and the unconditional Lombardo index refinement require no GRH L-function. The separate conditional G06.1-G06.2 refinement uses Dedekind zeta_M(s) for the actual finite auxiliary fields and avoidance composita in G-MW1/G-CHEB, supplied by trivial-character Hecke GRH over those fields; no Hasse-Weil L(F_a,s) hypothesis is used.','Original qualitative openness and commutator Zariski density are already unconditional. Also unconditionally, the adelic index over L is <[L:Q]*exp(10^21483)*max{1,h_F(F_a)}^(4.8*10^10), by Lombardo over Q and restriction. The separate Mayle-Wang numerical mod-ell refinement is established here under H_M; it is not established from Dirichlet GRH alone.','The original qualitative conclusion remains unconditional. Under H_M, for every prime ell>964*log(6)+5760, the mod-ell image over Q is GL_2(F_ell); after restriction to the actual L its index in GL_2(F_ell) is at most [L:Q]. This does not assert full GL_2(F_ell) image over L. The adelic Lombardo bound in the preceding column is unconditional.','Descent to Q is explicit in the recovered models, so no descent gate remains. Numerical evaluation of the unconditional adelic bound requires the actual [L:Q] and stable Faltings height h_F(F_a). The bounds do not determine the exact restricted image; the source rows only require qualitative openness.',evidence='Targeted source reread: A.32 explicitly defines F_a/Q and uses Serre after restriction to L; A.33 displays the same F_a and inherits that non-CM/Serre argument. The complete newly written G06 proof and G06_source_audit.md were read; discriminant, j, point counts and the image-index restriction argument were rechecked. Lombardo and Mayle-Wang are cited results, not independently re-proved here; no whole-proof certification of A.32 or A.33 is claimed.')
add('LM8_PUSH','A.46 A.47 A.48','CRYSTALLINE_COMPARISON_NOT_EFFECTIVE_FALTINGS_SERRE','Use crystalline comparison and special-fibre p-rank.','Actual proper H^1 and crystalline period comparison.',NONE,ALREADY,ALREADY,'This Faltings citation is not a finite Frobenius trace-equality criterion.')
add('LM8_PUSH','A.49','CRYSTALLINE_COMPARISON_AND_ELEMENTARY_PRIME_CHOICE','Use the preceding crystalline criterion; choose p≡3(mod4),p∤n by the explicit Euclidean proof.','Actual proper H^1; auxiliary primes supplied by a prime divisor of4*prod(p_i)-1.',NONE,ALREADY,ALREADY,'No analytic prime theorem is needed for this auxiliary choice. A new sharper least-prime bound could alternatively use Dirichlet L-functions modulo4.')
add('LM8_PUSH','A.54','FIXED_FINITE_FIELD_PRIMITIVE_ROOT','Choose a generator of F_q^times for q=41 or61 to label a reduction place.','Two explicitly fixed finite fields F_41 and F_61.',NONE,ALREADY,ALREADY,'Every finite-field multiplicative group is cyclic; this is not Artin\'s varying-prime conjecture.')
add('LM8_PUSH','A.55','ROOT_OF_UNITY_NOT_ARTIN','Choose a primitive p^n-th root of unity to identify mu_(p^n) withZ/p^n.','Finite Kummer target mu_(p^n).',NONE,ALREADY,ALREADY)
add('LM8_PUSH','A.69','RIEMANN_HURWITZ_FALSE_POSITIVE','The abbreviation DS/RH means Deuring–Shafarevich and Riemann–Hurwitz.','p-ranks and genera of special components of a dihedral stable model.',NONE,ALREADY,ALREADY,evidence='Full sections/A_dihedral_two_power_fixed.tex read at the explicit Deuring–Shafarevich and Riemann–Hurwitz references (lines151,173,180); RH is not Riemann Hypothesis.')
add('LM8_PUSH','B.28','EXACT_FROBENIUS_COMPUTATION','Explicit trace5 and determinant13 on y^2=x^3+16 atq=13.','Specified elliptic curve overF_13; #E(F_13)=9.',NONE,ALREADY,ALREADY)
add('LM8_PUSH','D.25','FALTINGS_FINITENESS_NOT_EFFECTIVE_SERRE','Apply Faltings finiteness of rational points in genus≥2.','The stated genus≥2 curve overQ.',NONE,ALREADY,ALREADY,'Faltings Satz7 supplies finiteness, not an effective height/cardinality bound or a finite Tate-module comparison.')
add('LM8_PUSH','D.31','ARTIN_BRAID_ACTION_FALSE_POSITIVE','Explicit Artin action of braid generators.','Finite/integral braid-group and free-group calculations.',NONE,ALREADY,ALREADY)
add('LM8_PUSH','D.93','ELEMENTARY_FIXED_PRIME_ORDER','Use that2 topologically generates Z_5^times and elementary factorization of2^(5^r)-1.','Fixed coefficient prime5; ord_5(2)=4 and v5(2^4-1)=1.',NONE,ALREADY,ALREADY,'No distribution of primes or Artin primitive-root conjecture is used.')
add('LM8_PUSH','P.7','DIRICHLET_CHARACTERS_NOT_GRH','Describe characters of a finite/compact unit group.','Cyclotomic character group as a representation-theoretic object.',NONE,ALREADY,ALREADY,'The word Dirichlet identifies characters; no zero location of their analytic L-functions is invoked.')

# Excerpt-only cases remain explicitly unverified at proof level.
EXCERPT='Only the attached BRIDGE_FLAGS.tsv statement/context excerpt is available; full proof not recovered. Classification is limited to the displayed input.'
add('ANABELIAN_A1_SUCCESSOR','B.113 B.114','QUALITATIVE_CHEBOTAREV_CANDIDATE','Complex-conjugation Frobenius class / CM normalizer obstruction.','M/Q finite Galois containing the normalizer fieldL, as specified in the attached statement.','For an effective refinement: zeta_M(s), or the exclusion compositum inG.1.',ALREADY+' General quantitative form is not Dirichlet-only.',ALREADY+' General quantitative form is inside the stipulated Hecke family.','Need the full proof and B.112 hypotheses before claiming a complete audit.',EXCERPT)
add('ANABELIAN_A1_SUCCESSOR','B.27 B.30','EXACT_FINITE_MINIMUM_EXCERPT','Fixed-curve least-prime statements; corresponding earlier A1 rows are fully recovered.','Explicit finite-field curves and finite Frobenius/Cartier tests from the earlier A1 return.',NONE,ALREADY,ALREADY,'Latest successor proof unavailable; the earlier A1 proof is not a substitute for verifying every later revision.',EXCERPT)
add('GT_TOWER_CHECK','C.1.21','LEAST_INDEX_NOT_LEAST_PRIME','J_N is the least index with v_ell((J_N+4)!)≥N.','Factorial valuation at a fixed coefficient primeell.',NONE,ALREADY,ALREADY,'Full proof unavailable; the displayed minimum is an integer index, not the least prime in an AP or Frobenius class.',EXCERPT)
add('S6_SERIES_GRIND','maps:src:F.2.36','GRH_DISABLED_IN_REPORTED_COMPUTATION','The attached context explicitly says class/unit groups were certified with GRH=false.','Reported certified class/unit-group computation; full computation source unavailable.',NONE,'No conditional GRH computation is evidenced by this excerpt.','No conditional GRH computation is evidenced by this excerpt.','Full source and certificates would be needed to verify the reported computation.',EXCERPT)
add('RESEARCH_SA07','F.3.6','FALTINGS_HOM_NOT_EFFECTIVE_SERRE','Use Faltings Hom theorem in an anabelian comparison.','Abelian varieties and their Tate modules; no finite trace set specified.',NONE,ALREADY,ALREADY,'A finite Faltings–Serre test requires actual integral representations, a residual image/deviation field and effective Chebotarev; these are not provided by the excerpt.',EXCERPT)

# Non-row programme/intake requests are tracked without inventing numbered rows.
add('INTAKE_ANABELIAN_149_FINAL_20261114','section3.3_route2','ARTIN_ARITHMETIC_PLUS_MISSING_GEOMETRY','Proposed primitive-root-on-a-theta-support-set route.','Arithmetic family K_n=Q(zeta_n,p^(1/n)), n squarefree; independently a curve-dependent set of primes supporting a theta point of exact ell^a order.','zeta_K_n(s) for all squarefree n; these are included as trivial Hecke characters overK_n in the stipulated Masullo hypothesis.','Not supplied: Kummer fields are generally nonabelian overQ.','Hooley\'s arithmetic theorem is supplied; the full route remains beyond the hypothesis.',GEO_GAP+' A positive-density set can be disjoint from all suitable primes: ell≡1(mod8) has both2 and-1 square. Lifting primitivity fromell toell^a also needs a prime-power condition.','Intake lines212–220 and Hooley §7 theorem in the 1968 Russian translation of the 1967 paper read. This is a proposed programme step, not an existing register theorem.')
add('INTAKE_ANABELIAN_149_FINAL_20261114','D.30 D.31','GEOMETRIC_RAMIFICATION_GATE','Legendre pullback irreducibility/modularity and local-cusp obstruction.','Actual pulled-back Legendre Tate system rho_{s,ell}; finite-order characters can be killed in a finite extension for a qualitative trace contradiction.','Finite-field Frobenius Weil bounds and qualitative finite-extension splitting suffice for the displayed contradiction; no number-field GRH is the missing input.',NOTFIX,NOTFIX,'Need finite ramification of one rho_{s,ell}, the actual local-section/modularity hypotheses, and exclusion of the stated finite cusp-label pattern. GRH alone gives none of these.','Intake summary and its explicit dependency cautions read; original D_legendre proof not recovered.')
add('AN_GRH','A06','UNIVERSAL_PRIMITIVE_ROOT_THETA_CONDITION_REFUTED','For the explicit B.23 curve, no odd prime ell with ord_ell(2)=ell-1 has a nonzero theta point of orderell.','C/F_(2^38) and Theta=C-P; scalar Frobenius -2^19. Only191,229,419,457,571,647 can survive the difference bound; only419 hasprimitive2, and its H=<119> has three ordered pairs with difference2.',NONE,'The universal T(C) assertion is false.','The universal T(C) assertion is false.','This does not refute A1 or settle the positive-p-rank restricted theta problem; B.23 curve has p-rankzero.','Parent supplied the complete new geometric proof in b23_section.tex; child read it and independently recomputed its finite prime/order/difference obstruction. Geometry recheck belongs to parent.')
add('ARCHIVE_149','scan037_Artin_elementary_variety','ARTIN_ELEMENTARY_VARIETY_FALSE_POSITIVE','The manuscript refers to a variete elementaire d\'Artin anabelienne and a translation stabilizer lemma.','Algebraic variety, generalized Jacobian and open subset; no prime distribution.',NONE,ALREADY,ALREADY,'This is a geometric use of the name Artin, unrelated to Artin\'s primitive-root conjecture.','Attached scan037 transcription read at line5; this is a manuscript passage, not an invented numbered register row.')

# Repair source locators of excerpt and intake entries from actual attachments.
flags=list(csv.DictReader((SOURCE/'BRIDGE_FLAGS.tsv').open(),delimiter='\t'))
flag_map=collections.defaultdict(list)
for i,x in enumerate(flags,2):flag_map[(x['run'],x['row_id'])].append((i,x))
for x in curated:
 key=(x['run'],x['row_id'])
 if key in flag_map and key not in blocks:
  x['source_locator']='; '.join(f'source/BRIDGE_FLAGS.tsv:{i}; reported {r["file_and_line"]}' for i,r in flag_map[key])
 if x['run'].startswith('INTAKE_'):x['source_locator']='source/INTAKE_ANABELIAN_149_FINAL_20261114.md; section3.3 or D.30/D.31 table as specified'
 if x['run']=='AN_GRH':x['source_locator']='work/root/b23_section.tex; work/row_audit/verify_theta_small_independent.py; work/row_audit/theta_small_independent.out'
 if x['run']=='ARCHIVE_149':x['source_locator']='source/ARCHIVE_149_scan037.tex:5'
 if x['run']=='INTAKE_ANABELIAN_149_FINAL_20261114' and x['row_id']=='section3.3_route2':
  x['missing_theorem_or_data']='The universal primitive-root theta condition is now refuted by FindingA06 on the B.23 curve. The positive-p-rank restricted geometric problem remains unresolved. '+x['missing_theorem_or_data']

assert len({(x['run'],x['row_id']) for x in curated})==len(curated)
cur_by={(x['run'],x['row_id']):x for x in curated}
seeds=collections.defaultdict(set)
for x in curated:
 if x['analytic_dependency_seed']=='yes':seeds[x['run']].add(x['row_id'])
depgraphs={}
paths={}
for run,rs in regs.items():
 ids={r['id'] for r in rs}
 def dependency_ids(raw):
  found=re.findall(r'\b[A-Z]\.\d+(?:\.\d+)*',raw)
  found += [f'{p}.{n}' for p,n in re.findall(r'\b([A-Z])(\d+)\b',raw)]
  for prefix,a,prefix2,b in re.findall(r'\b([A-Z])\.?(\d+)\s*(?:--|–|-)\s*(?:([A-Z])\.?)?(\d+)',raw):
   if (not prefix2 or prefix2==prefix) and int(a)<=int(b)<=int(a)+500:
    found += [f'{prefix}.{i}' for i in range(int(a),int(b)+1)]
  return [d for d in dict.fromkeys(found) if d in ids]
 graph={r['id']:[d for d in dependency_ids(r.get('depends_on','')) if d!=r['id']] for r in rs}
 depgraphs[run]=graph
 for id_ in ids:
  reached={};q=collections.deque([(id_,[id_])]);visited=set()
  while q:
   v,path=q.popleft()
   if v in visited:continue
   visited.add(v)
   if v in seeds[run]:reached[v]=' -> '.join(path)
   q.extend((w,path+[w]) for w in graph[v] if w not in visited)
  paths[(run,id_)]=reached

full=[]
for run,rs in regs.items():
 for r in rs:
  key=(run,r['id']);c=cur_by.get(key);p=paths[key]
  full.append(dict(run=run,row_id=r['id'],statement_original=r['statement'],source_status=r['status'],declared_dependencies=r.get('depends_on',''),
    register_source=RUNS[run][0],proof_locator=loc(*key),proof_availability='Full numbered block available' if key in blocks else 'Register only; proof unavailable',
    direct_audit_id=c['audit_id'] if c else '',direct_classification=c['audit_kind'] if c else 'No curated analytic input identified by term/dependency screen; not a proof-independence certificate',
    recorded_qualitative_prime_seeds='; '.join(sorted(p)),recorded_dependency_paths='; '.join(p[k] for k in sorted(p)),
    L_functions=c['L_functions'] if c else '; '.join(f'{seed}: {cur_by[(run,seed)]["L_functions"]}' for seed in sorted(p)),
    inherited_scope='Mechanical paths in the source register depends_on column; not independent proof verification. Each referenced seed has its exact field/family in ROW_ANALYTIC_LEDGER.tsv.' if p else '',
    under_Alpoge_Dirichlet_GRH=c['under_Alpoge_Dirichlet_GRH'] if c else ('See exact seed fields; qualitative input already unconditional.' if p else 'No promotion established by this screen.'),
    under_Masullo_all_field_Hecke_GRH=c['under_Masullo_all_field_Hecke_GRH'] if c else ('See exact seed fields; only a quantitative enhancement is new.' if p else 'No promotion established by this screen.'),
    missing_theorem_or_data=c['missing_theorem_or_data'] if c else ('Other proof steps and geometric claims are not validated by this screen.' if key in blocks else 'Full proof and complete analytic dependency audit are unavailable.'),
    evidence_scope=c['evidence_scope'] if c else ('Full source mechanically screened; register dependencies parsed; full proof not re-proved.' if key in blocks else 'Full statement/dependencies mechanically screened; proof unavailable.')))

old_flags=list(csv.DictReader((OUT/'ROW_FLAG_AUDIT.tsv').open(),delimiter='\t'))
new_flags=[]
for r in old_flags:
 key=(r['run'],r['row_id']);c=cur_by.get(key)
 if c:
  r.update(audit_kind=c['audit_kind'],L_functions=c['L_functions'],classification=c['under_Masullo_all_field_Hecke_GRH'],missing_statement_or_data=c['missing_theorem_or_data'],evidence_scope=c['evidence_scope']+' '+c['source_locator'])
 elif key in reg_by:
  r['missing_statement_or_data']='Full register recovered. '+('Main proof block is available and mechanically screened; other proof steps not independently verified.' if key in blocks else 'This numbered proof block has not been recovered.')
  r['evidence_scope']+='; supplemented by ROW_FULL_REGISTER_AUDIT.tsv; source status is not promoted by keyword screening'
 new_flags.append(r)

unique=[]
for key,rr in collections.OrderedDict.fromkeys((r['run'],r['row_id']) for r in new_flags).items():
 group=[r for r in new_flags if (r['run'],r['row_id'])==key]
 r=group[0].copy();r['all_flag_ids']='; '.join(x['audit_id'] for x in group);r['all_categories']='; '.join(dict.fromkeys(x['category'] for x in group));unique.append(r)

excerpt=[]
for run in ['ANABELIAN_A1_SUCCESSOR','GT_TOWER_CHECK']:
 summary=(SOURCE/f'SORTED_{run}.md').read_text()
 ids=set(re.findall(r'`([A-Z]\.\d+(?:\.\d+)*)`',summary))|{id_ for rr,id_ in flag_map if rr==run}
 for id_ in sorted(ids):
  c=cur_by.get((run,id_));entries=flag_map.get((run,id_),[])
  excerpt.append(dict(run=run,row_id=id_,available_in='; '.join((['summary'] if re.search(r'`'+re.escape(id_)+r'`',summary) else [])+(['bridge flags'] if entries else [])),
    flag_statement='; '.join(dict.fromkeys(x['statement'] for _,x in entries)),source_locator='; '.join(f'BRIDGE_FLAGS.tsv:{i}; {x["file_and_line"]}' for i,x in entries),
    classification=c['audit_kind'] if c else 'Excerpt/identifier only; no complete proof audit possible',
    limit='This is an actually visible identifier, not an invented list of all '+str(EXPECTED[run])+' rows. Full register/proof missing.'))

events=[dict(statement_id='AUDIT-INVENTORY',date=DATE,who=WHO,type='computation or formal certificate',outcome='Parsed all575 flag records/525 distinct run+id pairs/23runs; six summaries claim1190 rows. Recovered800 full register rows and591 numbered proof blocks. Counts are source availability, not proof verification.',locator='ROW_FULL_REGISTER_AUDIT.tsv; SOURCE_RECOVERY_MANIFEST.tsv; inventory.json')]
for r in unique:
 events.append(dict(statement_id=f'{r["run"]}:{r["row_id"]}',date=DATE,who=WHO,type='computation or formal certificate',outcome='Deterministic metadata/text screen of attached flag statement/context. '+r['audit_kind']+'. This event does not certify a proof.',locator=r['all_flag_ids']))
for c in curated:
 if (c['run'],c['row_id']) in blocks or c['run'].startswith('INTAKE_') or c['run']=='LM7_PUSH':
  events.append(dict(statement_id=c['audit_id'],date=DATE,who=WHO,type='used and rechecked in this run',outcome='The specified analytic input/classification was checked at the stated evidence scope. '+c['evidence_scope'],locator=c['source_locator']))
events.extend([
 dict(statement_id='ANABELIAN_A1:B.23:conductor-enumeration',date=DATE,who=WHO,type='computation or formal certificate',outcome='Reran retained primitive_conductors.py; bound68590, candidate list of13 conductors, final survivors191,229; PASS.',locator='B23_recheck/primitive_conductors.py; B23_recheck/conductor_recheck.out'),
 dict(statement_id='ANABELIAN_A1:B.23:retained-independent-verifier',date=DATE,who=WHO,type='computation or formal certificate',outcome='Reran retained primitive_verify.py after resolving missing python-flint runtime dependency. Hashes, encodings, independent compositions and full Bezout identities PASS for191 and229. This is reuse of the retained independent implementation, not a new independent implementation.',locator='B23_recheck/primitive_verify.py; B23_recheck/bezout_recheck.out; primitive_certificates/*.bin'),
 dict(statement_id='DELIGNE-WEIL-I-1.6',date=DATE,who=WHO,type='used and rechecked in this run',outcome='Read primary paper theorem(1.6) and trace formula(1.5.1), printed276: finite-field cohomological weights are unconditional. No number-field GRH inference.',locator='https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf; theorem1.6'),
 dict(statement_id='MILNE-CFT-V3.23',date=DATE,who=WHO,type='used and rechecked in this run',outcome='Checked exact finite-Galois qualitative Chebotarev statement: conjugacy class density|C|/|G|, with no GRH hypothesis. This supplies existence/density, not the new explicit least-prime bound.',locator='https://www.jmilne.org/math/CourseNotes/CFT.pdf; ChapterV theorem3.23'),
 dict(statement_id='HOOLEY-1967-THEOREM',date=DATE,who=WHO,type='used and rechecked in this run',outcome='Read and visually checked §7 theorem of the Russian translation, printed47/PDFpage10, including squarefree Kummer-field RH hypotheses and primitive-root conclusion. Original English publisher page was access-blocked; full analytic proof not re-proved.',locator='https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=455&what=fullt; §7'),
 dict(statement_id='AN_GRH:A06:independent-finite-obstruction',date=DATE,who=WHO,type='computation or formal certificate',outcome='New independent elementary Python implementation enumerated all candidate primes≤704, computed orders of2, and checked all differences inH union{0}. Six candidate primes; only419 hasprimitive2; its difference2 has exactly three ordered pairs. PASS. This checks the finite arithmetic portion, not the geometric input.',locator='verify_theta_small_independent.py; theta_small_independent.out'),
])

write_tsv('ROW_ANALYTIC_LEDGER.tsv',curated)
write_tsv('ROW_FULL_REGISTER_AUDIT.tsv',full)
write_tsv('ROW_SOURCE_TERM_HITS.tsv',term_hits)
write_tsv('ROW_FLAG_AUDIT.tsv',new_flags)
write_tsv('ROW_UNIQUE_AUDIT.tsv',unique)
write_tsv('ROW_ANALYTIC_CANDIDATES.tsv',curated)
write_tsv('ROW_EXCERPT_ONLY_AUDIT.tsv',excerpt)
write_tsv('ROW_CHECK_EVENTS.tsv',events)
write_tsv('LM7_PROOF_BLOCKS.tsv',[dict(run='LM7_PUSH',row_id=id_,source_locator=loc(run,id_)) for run,id_ in sorted(blocks) if run=='LM7_PUSH'])

recovery=[
 ('ANABELIAN_A1_checkpoint_03.zip','libfile_8e7e8d255c008191805244d2be534fc5','file_0000000046c881f4a51d35548b0bdce1','2026-11-17T04:13:20.180254Z','recovered/ANABELIAN_A1_checkpoint_03.zip','ANABELIAN_A1'),
 ('ANABELIAN_SUCCESSOR_final.zip','libfile_7037c305a5988191aa7a9a536b07ae02','file_00000000d98481f481441774e0ee66ad','2026-11-16T12:45:24.770271Z','recovered/ANABELIAN_SUCCESSOR_final.zip','ANABELIAN_SUCCESSOR'),
 ('LM8_PUSH_checkpoint_17.zip','libfile_e13c7e9666cc8191a3666719d2f60660','file_00000000acd082438da3581e4e7a7900','2026-11-16T03:00:52.555891Z','recovered/LM8_PUSH_checkpoint_17.zip','LM8_PUSH'),
 ('DELTA_2-3_reciprocity_of_frames_on_GT.zip','libfile_ccb39ae5e3108191a506bc4be4a9a1ed','file_0000000058f081f49ba1ab9ef54fdb4f','2026-11-20T22:59:03.290336Z','recovered/DELTA_2-3_reciprocity_of_frames_on_GT.zip','LM7_PUSH'),
]
manifest=[]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
for title,libid,fid,created,p,run in recovery:
 path=ROOT/p
 if not path.exists():
  candidates=list((ROOT/'recovered').glob('*DELTA*.zip')) if run=='LM7_PUSH' else []
  if len(candidates)==1:path=candidates[0];p=str(path.relative_to(ROOT))
 manifest.append(dict(role='recovered source archive; exclude giant archives from deliverable',run=run,title=title,library_file_id=libid,file_id=fid,library_created_at=created,local_path=p,size_bytes=path.stat().st_size,sha256=sha(path),register_rows=RUNS[run][1],proof_blocks=sum(1 for rr,_ in blocks if rr==run)))
 for f in [ROOT/RUNS[run][0],*sorted(ROOT.glob(RUNS[run][2]))]:
  manifest.append(dict(role='recovered register' if f.suffix=='.csv' else 'recovered main proof source',run=run,title=f.name,library_file_id=libid,file_id=fid,library_created_at=created,local_path=str(f.relative_to(ROOT)),size_bytes=f.stat().st_size,sha256=sha(f),register_rows=RUNS[run][1] if f.suffix=='.csv' else '',proof_blocks=len(re.findall(r'\\begin\{(?:claim|statement)\}\{',f.read_text())) if f.suffix=='.tex' else ''))
write_tsv('SOURCE_RECOVERY_MANIFEST.tsv',manifest)

# Preserve the compact recovered registers as audit evidence, not the enormous ZIPs.
evidence=OUT/'evidence/registers';evidence.mkdir(parents=True,exist_ok=True)
for run,(p,_,_) in RUNS.items():shutil.copyfile(ROOT/p,evidence/f'{run}_results.csv')
inventory=dict(date=DATE,who=WHO,source_sha256=sha(SOURCE/'BRIDGE_FLAGS.tsv'),flag_records=len(flags),flag_distinct_rows=len(unique),flag_runs=len({r['run'] for r in flags}),
 expected_full_register_rows=sum(EXPECTED.values()),recovered_full_register_rows=len(full),recovered_numbered_proof_blocks=len(set(blocks)&set(reg_by)),
 recovered_register_counts={k:len(v) for k,v in regs.items()},proof_block_counts={r:sum(1 for rr,id_ in blocks if rr==r and (rr,id_) in reg_by) for r in RUNS},
 missing_full_registers={'ANABELIAN_A1_SUCCESSOR':210,'GT_TOWER_CHECK':180},visible_identifiers_in_missing_runs=dict(collections.Counter(r['run'] for r in excerpt)),
 curated_ledger_rows=len(curated),qualitative_prime_input_seeds={r:sorted(s) for r,s in seeds.items() if s},register_rows_reaching_qualitative_prime_seed=sum(bool(x) for x in paths.values()),
 limitations='No complete audit of all1190 statements is possible from the recovered sources. Mechanical dependency paths and term hits are not proof verification. Source Proved labels are preserved only as source metadata.')
(OUT/'inventory.json').write_text(json.dumps(inventory,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in inventory.items() if k not in ['qualitative_prime_input_seeds']},indent=2))
