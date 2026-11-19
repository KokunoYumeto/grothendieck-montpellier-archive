"""Record actual checks; never infer mathematical truth from keywords or headings."""
from pathlib import Path
import json,csv
P=Path(__file__).resolve().parents[1]
items=json.loads((P/'items.json').read_text());claims=json.loads((P/'claims.json').read_text());refs=json.loads((P/'reference_registry.json').read_text())
WHO='GPT-6 Astra Pro; effort inherited/unspecified; run SA16-2026-11-19-cote62'
events=[]
def event(id,typ,outcome,artifact,refined=''):
    events.append(dict(statement_id=id,date='2026-11-19',who=WHO,type=typ,outcome=outcome,artifact=artifact,refined_statement_id=refined))
for item in items:
    event(item['id'],'used and rechecked in this run','Entry/passage comparison: '+item['check']+'. '+item['check_reason'],'items.json; '+item['lines'])
for claim in claims:
    event(claim['id'],'used and rechecked in this run','Actual transcription passage and exact literature scope compared. Page status: '+claim['status_on_pages']+'. '+claim['fate'],'claims.json; search_log.tsv; '+claim['lines'])
# These are mathematical arguments actually written in P1--P7. The outcome states
# their limited scope; no source theorem is silently promoted to a re-proof.
proofs={
1:'P1 derives fibre ranks and applies the opened base-change criterion using vanishing/unit sections; the general proper-flat theorem is used, not reproved.',
2:'P1 supplies the genus-one length-two Riemann--Roch argument and excludes degrees1,2.',
3:'P1 derives graded lines from divisor sequences and proves universal injectivity by locally free cokernels.',
4:'P1 proves filtered generation by leading-pole induction and distinguishes the homogeneous ring.',
5:'P1 localizes derivations and computes the leading symbol−n.',
6:'P1 checks the flex divisor and primitive local Cartier equation; the standard relative embedding theorem is used.',
7:'P1 checks weights and admissible frames; algebraicity/smooth atlas is used from the primary reference.',
11:'P1 verifies the monic twelfth-root algebra, faithful flatness and etaleness condition.',
12:'P1 verifies completing the square, depressing the cubic and the centralμ2 kernel.',
14:'P2 proves barycentre descent by changing the chosen affine origin.',
18:'P2 derives the centralizing involution and checks the explicit group action.',
19:'P2 proves the relative normalizer as a group scheme over every Z[1/6]-base, using fppf-local matrix lifts, trace(PR)=1, clopen scalar signs and explicit commuting/anticommuting equations. Beauville supplies only the field comparison.',
22:'P2 gives inverse descent constructions on objects and isomorphisms for trisections and torsors with an equivariant map.',
23:'P3 checks generic-map extension by integrality under a normal base and an already-etale full ordering torsor; mere cubic normalization is insufficient.',
24:'P3 derives DVR square/cube criteria and checks every hypothesis of the singular normal A1 counterexample.',
26:'P2 separates the fixed bisection from the sign cover by their quadratic classes.',
27:'P2 reconstructs the square-root-line lift and degree-one conic line. Abstract rigidification/Kummer theorems are used, not reproved.',
28:'P2 applies complete-local henselianity and residue equivalence; no proof of those general theorems is claimed.',
29:'P4 completes the Rees-module proof of Artin--Rees.',
30:'P4 proves the series criterion and quotient-completeness argument with the nonseparated convention explicit.',
31:'P4 compares finite coefficient conditions for the product and (I,X)-adic topologies.',
32:'P4 gives successive graded error correction and strict surjectivity.',
33:'P4 gives the inverse-limit quotient/graded argument.',
34:'P4 gives the strict metrizable-group completion argument and both weakening counterexamples.',
35:'P4 proves noetherianity through the filtered quotient of Sym(g), without an unnecessary PBW-freeness hypothesis.',
36:'P4 gives the graded finite-generation/noetherian lifting argument, including separated completeness.',
37:'P4 proves complete Nakayama by convergent coefficients, without assuming the target module finite.',
38:'P4 checks Artin--Rees, finite-presentation tensor identity and ideal-criterion flatness; faithful flatness requires the Jacobson hypothesis.',
39:'P4 checks finite intersection and colon identities by flat preservation of kernels.',
40:'P1 derives the Lie-frame scaling weights;6 invertible is an explicit reconstructed hypothesis.',
42:'P5 separates independence from incomparability by a concrete pair of rank-two composed valuations.',
43:'P5 checks the maximal-local extension and integral-closure mechanism; general valuation existence is also matched to the opened Stacks proof.',
44:'P5 supplies value-coset/residue independence and the torsion/convex-subgroup calculation.',
46:'P6 gives the fundamental-parallelogram residue/argument-principle proof and compactness consequences.',
47:'P6 proves the even-function field theorem via the degree-two quotient, then decomposes into even and odd parts.',
48:'P6 checks normal convergence and lattice parity; this is an analytic argument, not a numerical convergence certificate.',
49:'P6 derives the Weierstrass cubic from principal parts and Laurent coefficients.',
50:'P6 checks inverse-integral differentiation with the branch/normalization fixed.',
51:'P6 derives zeta/sigma parity and logarithmic derivatives from the regularized definitions.',
52:'P6 gives the quasiperiod and Legendre contour argument.',
53:'P6 matches every pole order with zeta or a derivative ofwp and computes the factorial.',
54:'P6 computes the divisor-product multiplier and the correcting exponential sign.',
55:'P6 gives the principal-parts/constant method for addition and the duplication limit; exact primary formulas were also compared.',
57:'P6 proves meromorphic square-root existence on C for an even divisor and fixes translation signs by sigma normalization.',
59:'P6 derives first/second-order Jacobi equations from the squared relations.',
60:'P6 derives the cn modulus square and pole residues from the differential equations.',
62:'P6 derives Laurent/Taylor recurrence from the ODE and logarithmic integration.',
63:'P6 derives parity and period/antiperiod signs of halfperiod sigma ratios.',
64:'P7 derives Fourier reindexing, normal convergence and coefficient recurrence.',
65:'P7 derives sigma normalization and tau shifts from the theta series.',
66:'P7 reindexes the bilateral series to verify the literal Gaussian identity.',
67:'P7 checks the heat derivative and final S normalization; the modular transformation theorem is also used from DLMF.',
69:'P7 checks the even-theta identification, zero-derivative obstruction and quartic root normalization.',
70:'P7 computes period homogeneity directly from lattice terms.',
71:'P7 checks special values by square/equianharmonic symmetries; global lattice classification is used from Sutherland, not independently reproved.',
72:'P6 derives the initial-value Taylor and degeneration formulas.',
73:'P6 compares divisor/period tables through theta quotients and their quasi-laws.',
74:'P6 composes quarter-period shifts and derives the sign ofdn atKdoubleprime.',
75:'P6 checks squared Weierstrass/Jacobi relations and sigma denominators by divisors.',
76:'P6 checks theta/ODE normalization of the three quotients and addition identities; universal classical formulas also source-checked.',
77:'P6 proves the degree assertion by argument principle; full uniformization is used from Sutherland Theorem15.1/Corollary15.12.',
78:'P2 proves descent of the centralizing involution, its involutive action on unpointed trisections, and the etale fixed bisection; it explicitly does not preserve the pointed open U.',
79:'P5 compares the manuscript maximal-subextension proof with the opened exact Deuring/Gardam theorem. The initial extension into some residue overfield is a stated valuation-theoretic input; algebraic closedness then fixes the target.'}
for n,outcome in proofs.items():
    # Wording explicitly marks partial arguments; these are targeted checks when
    # a general external theorem remains a substantial part of the conclusion.
    typ='targeted proof check' if n in [1,6,7,27,28,43,55,67,71,76,77,79] else 'independent re-proof'
    event(f'C-SA16-{n}',typ,outcome,'proof_checks.md')
computations={
5:'Exact derivatives of pole monomials.',8:'Exact full general Weierstrass discriminant via completed-square cubic.',
16:'Exact scratch-family discriminant and invariant normalization.',17:'Exact cubic resultant, discriminant and depression.',
18:'Exact six-map invariance, multiplication table and sigma matrix identities.',19:'Exact commuting and anticommuting matrix equations, trace and determinant identities for the relative centralizer proof.',20:'Exact cyclic quotient derivative and branch factors.',
21:'Exact invariant identities, reciprocal symmetry and equal-invariant factorization.',25:'Exact vanishing orders at the harmonic and cyclotomic points; dual-number counterexample.',
26:'Exact alternating polynomial and sign-cover class.',40:'Cubic/scaling normalization algebra; not an ink reading.',
49:'Exact Laurent recurrence; cubic invariants independently recomputed.',51:'60-digit parity spot checks.',
52:'60-digit quasiperiod checks at the recorded nonspecial lattice.',55:'60-digitwp,zeta,sigma addition/duplication/four-translate checks.',
56:'Exact Mobius expression satisfies Jacobi ODE and the specified initial value/derivative.',57:'Exact halfperiod translation ODE and product relation.',
59:'Jacobi squares and first derivatives numerically checked; second derivatives derived in P6.',62:'Exact Laurent and sigma Taylor coefficients.',
64:'60-digit theta quasi-period checks; coefficient recurrence derived in P7.',65:'60-digit sigma/theta normalization checks.',
66:'60-digit literal Gaussian identity check at the recordeda,b,c.',67:'60-digit theta heat and modularS checks with chosen branch.',
68:'Counterexample T=1/2+i, exact real parts1/2,2/5; equianharmonic height obstruction.',
69:'60-digit derivative and all three halfperiod-root theta formulas.',71:'Exact anharmonic relationi=1−j/1728.',
72:'Exact sn coefficients throughz9 and cn,dn throughz6; degeneration counterexample at0.',
73:'60-digit primitive/common periods, anti-periods, finite value table and residues.',
74:'60-digit quarter/imaginary shifts; literaldn(Kdoubleprime) plus sign has nonzero residual, corrected minus sign passes.',
75:'Exact Weierstrass halfperiod relation and product; denominator comparison is analytic in P6.',
76:'60-digit all three addition laws and theta quotients.',78:'Exact sigma-square, fixed polynomial and centralizer identities; general descent is the P2 argument.'}
for n,outcome in computations.items():event(f'C-SA16-{n}','computation or formal certificate',outcome+' Symbolic rows and numerical rows are separately labelled; no external Lean certificate was run.','code/check_math.py; outputs/math_checks.json; outputs/math_checks.txt')
for claim in claims:
    if 'refined_statement' in claim:
        event(claim['id'],"refuted, with the refined statement's id",'The literal transcribed substatement/formula fails as explained in the claim and P1--P7. This does not identify the ink as an authorial error. Refined statement: '+claim['statement'],'claims.json; proof_checks.md; readings.tsv',claim['refined_statement']['id'])
for ref in refs:
    typ='used and rechecked in this run' if ref['note']=='verified' else 'carried as background without fault found'
    event(ref['key'],typ,ref['verification_scope']+' Locator: '+ref['locators']+' URL: '+ref['url'],'reference_registry.json; search_log.tsv')
with (P/'check_events.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(events[0]),delimiter='\t');w.writeheader();w.writerows(events)
print('check events',len(events))
