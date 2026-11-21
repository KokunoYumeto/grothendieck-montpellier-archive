"""Consolidate actual recorded checks; retain original evidence notes unchanged."""
from pathlib import Path
import csv

ROOT=Path(__file__).resolve().parent.parent
D=ROOT/'deliverables' if (ROOT/'deliverables').is_dir() else ROOT
events=[]
allowed={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
aliases={'R25':'P0','R26/P6':'P6','R27/P2b':'P2b','ARC16':'G1','ARC16-7':'G1','ARC16-COATES':'G1'}
aliases.update({f'R28.{i}':('M7' if i<6 else 'M8') for i in range(1,7)})
aliases.update(dict(zip([f'R29.{i}' for i in range(1,8)],['SQ2','SQ3','SQ4','SQ5','SQ6','SQ7','SQ9'])))
aliases.update({f'R30.{i}':'M9' for i in range(1,4)})
aliases.update({'R31.1':'M10a','R31.2':'P1-n3','R31.3':'M10b','R31.4':'M10','R32.1':'P6','R32.2':'INTEGRATED-MATHEMATICS','R32.3':'VERIFICATION-SCOPE'})
aliases['R33']='METADATA-CONSISTENCY'
aliases['R34']='R24E–R24F'

def normalize(t):
    if t in allowed:return t
    if 'metadata' in t:return 'used and rechecked in this run'
    if 'reproof' in t or 're-proof' in t:return 'independent re-proof'
    if 'computation' in t or 'compilation' in t or 'certificate'==t:return 'computation or formal certificate'
    if 'source' in t:return 'used and rechecked in this run'
    if 'proof' in t or 'reading' in t:return 'targeted proof check'
    raise ValueError(t)

def add(sid,typ,outcome,evidence,agent='root',date='2026-11-21'):
    who=f'GPT-6 Astra Pro; effort setting not exposed; agent /root{("/"+agent) if agent!="root" else ""}; run HECKE_DIV_20261121'
    events.append(dict(statement_id=sid,date=date,who=who,type=typ,outcome=outcome,evidence=evidence))

with (ROOT/'work/reductions_check_events.tsv').open() as f:
    for row in csv.DictReader(f,delimiter='\t'):
        original=row['statement_id']; sid=aliases.get(original,original)
        typ=normalize(row['type']);outcome=row['outcome']
        if typ!=row['type']:outcome=f"Original check type: {row['type']}. "+outcome
        if sid!=original:outcome=f'Original audit event {original}. '+outcome
        if typ=='computation or formal certificate':outcome='Ordinary exact computation, not proof-assistant certification. '+outcome
        events.append(dict(statement_id=sid,date=row['date'],who=row['who'],type=typ,outcome=outcome,evidence='work/reductions_check_events.tsv; corresponding full audit note'))

with (ROOT/'work/severn_quantitative_checks.tsv').open() as f:
    for row in csv.DictReader(f,delimiter='\t'):
        typ=normalize(row['check_type'])
        # These are the section author's new derivations, followed by complete self-checks.
        if typ=='independent re-proof' and row['id']!='P3-root':typ='targeted proof check'
        add(row['id'],typ,row['scope']+'; '+row['outcome']+'. Historical intermediate requests for a second reader were closed by R29 and R32; final SQ9 uses the direct Weil comass proof.','work/severn_quantitative_checks.tsv; work/severn_quantitative_independent_check.md; work/final_integration_review.md','markman',row['date'])

rootchecks={
'R20':'Target normalization and integral effective-cycle convention; rational rescaling counterexample.',
'P0':'Flat Lefschetz decomposition and Hodge star; invariant harmonic norm; comass and exact degree/volume factorial.',
'R21':'Full bounded relative Chow component argument, flat class condition, proper images, Baire and fixed-multiplier variants.',
'R22':'Ambient rational Shimura subgroup, real approximation, H1 isogeny equivalence and SU determinant action.',
'R23':'André–Oort finite special union; strict eventual avoidance; construction of generic sequences and bounded subsequence converse.',
'R24A':'Effective bounded-divisor component selection and generic NS-rank hypothesis.',
'R24Asigned':'Integral trace-free signed-degree-zero counterexample on dense elliptic-power orbit.',
'R24B':'Finite Hilbert polynomials, constructible subgroup locus, specialization and smooth identity component in characteristic zero.',
'R24C':'Integral nilpotent unipotent automorphism counterexample and graph polarization determinant.',
'R24D':'Bounded-input scope and norm-one-torus proof that all elliptic-power Hodge classes are divisor-generated.',
'R24E':'Complete added proof read: scalar existence in every order, Rosati polarization scaling, restriction degree, pushforward eigenvalues and finite-scalar scope example.',
'R24F':'Complete added counterexample read against P2b: product orientation, integral signed divisor intersections, an effective nonzero-projection term and no uniform presentation-degree claim.',
'P1':'All eigenspace/projector arguments, homological-degree restriction, integral numerator and cycle-degree scaling, including n3.',
'P2':'Graph restriction of polarization, Weil periods, independence, SU isogeny scaling and general rational target.',
'P2b':'Full exterior expansion, graph divisor identities, saturated integral lattice, orientation, Gram and signed-product degrees.',
'P3':'Orthogonality, primitive positivity, finite integral lattice ball, irreducible K-action, Cramer denominator and converse.',
'M1':'Markman corollary plus fixed-class R21 globalization.',
'M2':'Actual mu_r cocycle killing under[r], determinant-preserving untwisting, Atiyah naturality and Newton denominators.',
'M3':'Full genus-four Euler/Ext argument including finite étale descent, trace splitting, simplicity and semiregularity dimensions.',
'M4':'Same multiplier on analytic open followed by fixed-N R21; abelian-scheme hypothesis explicit.',
'M5':'Newton identities and d3 numerical intersections, with source example scope retained.',
'M6':'Normalization coefficients retained; fixed Hilbert polynomial counterexample; source stability/properness attribution restricted.',
'MR1–MR3':'Gotzmann counts34/6760; disjoint tensor ideals; Sidman Tor-support argument; regularity445 and presentation/kernel449.',
'M7':'Complete five-step direct-image/duality/Buchsbaum–Rim/trigonal-nefness proof and strengthened isogeny/nef-twist vanishing.',
'M8':'Rank≥3 dependence loci and Chow localization; twist identities; normalized flat analytic family and persistence of six vanishings.',
'M9':'Input character, relative GRR differentiation and duality signs; invariant h0 via Lefschetz injectivity; all positivity matrices and degree expressions.',
'M10a':'Integral sqrt(-12) action, O-enlargement, index and polarization product, both Hermitian denominators, analytic-open transfer and16³M⁶.',
'M10b':'Saturated n3 Weil lattice, norm denominator648, action determinant360Q, coefficient cost, finite union and common-LCM globalization.',
'M10':'Both explicit compensation divisors, intersections and nef comparisons, proper translated intersections, common multiplier and separate sign degrees.',
'P4':'Exact consequence of the cited version-specific Severn theorem and R21, retaining manuscript status.',
'SQ1':'Complete explicit integer formula and proof linkage SQ2–SQ7, target integral action and fixed polarization product.',
'SQ2':'Primitive Rosati-symmetric group projector, source O-stability and dual-lattice polarization exponent.',
'SQ3':'Real/quaternionic parity, admissible supplier columns, finite cokernel path and cofactor coefficient bound.',
'SQ4':'Schoen incidence degree, integral orbit sum and cohomological quotient transfer, primitive projector mass; no flat quotient pullback assumption.',
'SQ5':'Middle-degree curve-power determinant pairing and character cancellation, dimension and external-product mass.',
'SQ6':'Full centralizer invariant algebra, actual globally generated2Theta divisors,40G nef comparison, proper intersection and binomial degree.',
'SQ7':'Integral Hermitian normalization, primitive isotropic direct summand over Z[omega], both2Delta denominators and uniform isogeny degree.',
'SQ8':'Projector degree mass from integral coefficients and7^(4j) pullback scaling.',
'SQ9':'Final direct Weil-plane comass estimate, integral Gram/Cramer cap, explicit closed-locus globalization, principal norm31104 and factors1265/6325.',
'P5':'Two mutually inverse homological motive maps, positive Gram sign, pure-degree Künneth projector and converse.',
'A1':'Closed-set portmanteau inequality, smooth invariant measure, Markov bound and tightness equivalence.',
'A2':'Integral block action, fixed polarization type, splitness, conductor-isogeny scaling and explicit split-prime height growth.',
'A3':'Exact minimum effective sign degree in fixed-lattice monoid and separate saturation countermodel; logical scope.',
'P6':'Full finite-type h-cover and flattening, horizontal component and trait, smooth-proper cycle specialization, same multiplier and degree, Betti comparison and spreading converse.',
'G1':'Original-scan comparison note and two-letter evidence read in full; dates/pagination retained without emending manuscript year.'
}
for sid,scope in rootchecks.items():
    add(sid,'targeted proof check','Complete proof read by root in integrated source; '+scope+' No remaining fault found under stated hypotheses.','HECKE_DIV.tex and included mathematical sections; work/final_integration_review.md')

for sid,scope in [
('M2','Complete saved proof and Markman active definitions read; cocycle, perfect determinant, Atiyah class and Newton arithmetic checked.'),
('M3','Complete saved proof and genus-four source example read; quotient, trace, simplicity, duality and target dimensions verified.'),
('M4','Complete proof checked after adding explicit abelian fibres; fixed N precedes Baire.'),
('P0','Complete proof, flat star and normalization verified.'),('P1','Complete polynomial correspondence proof verified.'),
('P2','Graph periods and SU scaling verified.'),('P3','Complete finite-lattice and Cramer proof verified.'),
('MR1–MR3','Complete input regularity proof checked against the full Sidman tensor/Tor proof;445 and449 verified.'),
('P5','Complete inverse-motive-map proof checked with sign and pure-degree correction.')]:
    add(sid,'targeted proof check',scope,'work/arithmetic_final_checks.md','arithmetic')

for sid,scope in [('A1','Complete positive-mass/first-moment proof.'),('A2','Complete conductor/block-action construction and height proof.'),('A3','Complete monoid and saturation countermodels.'),('S1','Complete Severn supplier/Brauer transfer chain, Schoen repair, parity and centralizer direction.')]:
    add(sid,'targeted proof check',scope+' Passed within the stated scope.','work/arithmetic.md','arithmetic')
add('S3','targeted proof check','Full degeneration/dominance mechanism read; effective limiting mixed Hodge structure, transversality and16-dimensional derivative verified; minor compact-dual wording recorded.','work/severn_dominance_audit.md','arithmetic')
add('S2','computation or formal certificate','Exact reconstruction of group order, scalar centre, irreducibility, parabolic basis/Gram,17 geometric logarithms and pants boundary data. Ordinary computations only.','work/severn_group.py/json; work/severn_monodromy.py/json; work/severn_pants.py/json; work/check_severn_printed.py/json')
add('P1','computation or formal certificate','Root reran consolidated n2,n3,n4 projector driver and independent integer-pair checker after adding n3; all eigenvalues/weighted costs passed. This is an ordinary arithmetic rerun, not another independent derivation.','work/projector_reproduction.txt; work/projector_independent_check.json; work/projector_n3_independent_check.json')
add('M5','computation or formal certificate','Exact polynomial/Newton and Ext-dimension arithmetic executed; no formal theorem-prover claim.','work/markman_computation.txt','markman')
add('M9–M10','computation or formal certificate','Two independent polynomial/integration orders in the author script; final constants passed. Separate reductions Fraction checker recorded in R30.2.','work/markman_output_numbers.py/json','arithmetic')

sources=[
('MARKMAN-1.4.1/1.5.1/1.6.1','Statements, characteristic/deformation scope and complete final globalization paragraph inspected; not a new reproof of entire source.','work/markman.md','markman'),
('MARKMAN-7.4/9.2/9.3','Active twisted/deformation and reflexive-output source passages inspected for M2/M7/M8; retained as cited geometric inputs.','work/markman_output_regularity.md','arithmetic'),
('MARKMAN-EX8.2.3','Full genus-four example and partial-normalization alternative inspected; does not imply failure of every transform.','work/markman.md','markman'),
('SCHOEN-1988-2.0/2.3–2.6/3.1','Exact supplier construction/nonvanishing locators read; original argument plus Severn repair distinguished.','work/arithmetic.md; work/severn_quantitative.md','arithmetic'),
('MILNE-1999-3.1–3.7','Centralizer/invariant-theory statements and relevant proofs read; full orthogonal group/parity retained.','work/arithmetic.md; work/severn_quantitative_independent_check.md','arithmetic'),
('SEVERN-A/B/11.2','Exact manuscript theorem scope inspected; version1.5/date21Oct2026 and unrefereed status retained. Source-level audits S1–S3 and computational reconstruction do not constitute a Lean verification.','work/arithmetic.md; work/severn_dominance_audit.md; work/severn_monodromy.md','root'),
('ESKIN-OH-1.2','Exact unconditional Hecke packet theorem inspected; not conflated with GRH-dependent Galois-orbit statements.','work/arithmetic.md','arithmetic'),
('HEIGHTS-2017-1.3','Theorem1.3 and conductor term inspected; sign convention checked by subtracting conductor-one case.','work/arithmetic.md','arithmetic'),
('SIDMAN-1.4/1.5/1.6','Relevant complete proofs read; Tor-support hypothesis checked in the application.','work/arithmetic_final_checks.md','arithmetic'),
('GOTZMANN-DELLACA-2.7','Exact regularity statement used with independently computed binomial lengths; original theorem number not invented.','work/markman_regularity.md','root'),
('RAICU-SAM-BR','Complete globalized Buchsbaum–Rim formula, determinant factor and surjective exactness criterion inspected,pp41–42. Local exactness also independently proved.','work/markman_output_regularity.md','arithmetic'),
('BAUER-SZEMBERG-1.1','Theorem1.1(a),(b) and full proof pp79–81 inspected; used for square global generation and cube very ampleness.','work/markman_output_regularity.md','arithmetic'),
('GRAUERT-7-SATZ3','Exact analytic upper semicontinuity statement and proof pp62–63 inspected, including proper/reduced/flat hypotheses.','work/markman_output_regularity.md','arithmetic'),
('SV-2.2.2/4.4.11/4.4.13','Mixed-characteristic cycle sheaf and flattening statements directly inspected; relevant scope checked.','work/prime_lifting_check.md','reductions'),
('ANDERSON-6.3.19/24/25','Detailed proper-cover/flattening form read in thesispp188–193.','work/prime_lifting_check.md','root'),
('SGA4-XVI-2.2','Smooth proper specialization statement inspected.','work/prime_lifting_check.md','reductions'),
('SGA6-X-7.13.10','Originalpp578–579 visually inspected for rational cycle-class specialization compatibility.','work/prime_lifting_check.md; work/sga6_page578.jpg; work/sga6_page579.jpg','reductions'),
('STACKS-054F','Full trait-realization statement/proof inspected, including finitely generated generic field choice.','work/prime_lifting_check.md','root'),
('BRUNJES-SERPE-2.3/3.1/3.4','Related complexity definition and lifting theorems inspected; exact title and arXiv year checked. P6 varying-N proof supplied separately.','HECKE_DIV.tex bibliography; work/prime_lifting_check.md','root'),
('OPENAI032-REMARK8.5','Full remarkpp50–51 read; scope includes non-CM varieties; no uniform integral degree is stated. CM-transport proof carried as cited input.','work/prime_lifting_check.md; source supplied PDF','root'),
('ALPOGE-ENTRYPOINTS/STEP5','Five Main.lean entrypoints and Statements.lean inspected; steps3/5 and footnote3 read. Full import graph not compiled.','source/ALPOGE_Main.lean; source/ALPOGE_Statements.lean; work/arithmetic.md','arithmetic'),
('MASULLO-INDEX','Supplied index read: Trace Formula13.3.1.1,p522; general Hecke-GRH theorem number not verifiable. Conditional premise unused.','source/MASULLO_STATEMENTS_INDEX.md; work/arithmetic.md','arithmetic'),
]
for sid,scope,ev,agent in sources:add(sid,'used and rechecked in this run',scope,ev,agent)
for sid,scope in [
('OPENAI032-1.1/8.3/8.4','CM-Hodge and its supplied consequences accepted as cited input under task convention; not re-proved.'),
('VANHOFTEN-SEMPLINER-I','Supplied parallel human proof theorem statement used as background, not fully re-proved.'),
('MILNE2026-2.1/3.1/3.5','Supplied report theorem scope checked and carried as background; no new Tate/standard proof claimed.'),
('SCHOEN-1998-PROP10','Carried through the stated proof of Markman Corollary1.6.1. Its historical compensation role is cited; M10 supplies a separate explicit compensation calculation. No independent source-proof verification is claimed here.'),
('SCHMID-4.12/6.16','Nilpotent-orbit and limiting-Hodge theorems at exactpp233/255 used in targeted dominance audit; deep source proofs not newly re-proved.'),
('STANDARD-COHERENT-TOOLS','GAGA, Serre duality, Kodaira vanishing, integral Chern classes, Chow localization, Thom–Porteous rank-drop formula, regularity multiplication and proper flat semicontinuity are standard inputs; application hypotheses checked in full new proofs.'),
('STANDARD-HODGE-TOOLS','Polarized Lefschetz decomposition, Hodge–Riemann, Wirtinger, invariant harmonic forms and Betti–étale compatibility are background inputs with normalizations checked in new arguments.'),
('STANDARD-ABELIAN-TOOLS','Polarization/norm identities, Riemann–Roch, theorem of the square, divisor/endomorphism correspondence and finite-isogeny trace splitting are background inputs; actual numerical applications proved in text.')]:
    add(sid,'carried as background without fault found',scope,'HECKE_DIV.tex cited locators and corresponding proofs')

for sid,ref,reason in [
('SKETCH-2.4-SIGNED-DEGREE','R24Asigned','Nonzero trace-free divisor classes have signed degree zero.'),
('SKETCH-2.4-ENDOMORPHISM-DEGREE','R24C','Extra unipotent automorphisms have isogeny degree one.'),
('SKETCH-MARKMAN-PROPER-MODULI-ATTRIBUTION','M6','The relevant source paragraph is commented and conditional; fixed Hilbert polynomial does not bound instability.'),
('FIXED-K-UNIFORM-HEIGHT','A2','The explicit conductor family has unbounded height.'),
('POSITIVITY-IMPLIES-EFFECTIVE-COERCIVITY','A3','Explicit fixed-lattice monoid and saturation countermodels.'),
('SKETCH-SINGLE-COATES-LETTER','G1','Original scans show two separate letters and different written dates.')]:
    add(sid,"refuted, with the refined statement's id",f'{ref}: {reason}','HECKE_DIV.tex; QUESTIONS.tsv; corresponding audit note')

add('SKETCH-2.4-UNQUALIFIED-LEFSCHETZ-EXCLUSION','targeted proof check','R24D proves the bounded-input scope and identifies the gap in extending it to final divisor-polynomial representatives. The unrestricted final-cycle exclusion is not itself refuted by divisor generation of the Hodge ring. This distinction was checked again in the final metadata review.','HECKE_DIV.tex; QUESTIONS.tsv; work/reductions_check_events.tsv event R33')

add('REPRODUCTION-GUIDE','targeted proof check','Complete guide reread against all actual scripts/outputs; documentation only, no redundant expensive computational rerun.','work/REPRODUCING_COMPUTATIONS.md','markman')

extra=ROOT/'work/final_verification_events.tsv'
if extra.exists():
    with extra.open() as f:
        for row in csv.DictReader(f,delimiter='\t'):
            assert row['type'] in allowed
            events.append(row)

with (D/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome','evidence'],delimiter='\t')
    w.writeheader();w.writerows(events)
assert all(x['type'] in allowed for x in events)
print(f'Consolidated {len(events)} actual source/proof/computation events.')
