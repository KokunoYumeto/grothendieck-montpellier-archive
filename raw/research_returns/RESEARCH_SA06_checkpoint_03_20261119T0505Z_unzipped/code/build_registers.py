#!/usr/bin/env python3
"""Assemble auditable research registers from the proof owners' records."""
from pathlib import Path
import csv,re,json,datetime
R=Path(__file__).resolve().parents[1]
FIELDS=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
DESCRIPTIONS={
'A.1a':('The unrestricted F_(p^2) determinant formulation is false','Explicit p=3 maximal order and F=4J sigma','15:54','F²=-48; determinant multiplier48 has no Tate isomorphism over F9.'),
'A.1b':('Exact finite-field Tate determinant criterion; algebraic-closure existence','Scalar centralizer; integral Hilbert90','15:54','Over Fp² exactly F²=±p; over Fpbar every determinant is Tate.'),
'A.1c':('Unique integral rank-two slope-half crystal and oriented O-actions','Dieudonné–Manin; minimal-index lattice argument','15:54','All primes; centralizer ambiguity Zp*.'),
'A.1d':('Choice-independent Deuring rule from oriented reconstruction and cup trace','A.1c; Voight42.4.8; A.6a; integral Hom comparisons','15:50,54','All rules form a torsor under Zp*/Zp*²; two classes for odd p and four for p=2.'),
'A.1e':('Terminating geometric reconstruction and explicit intertwiner prescription','A.1b–d','15:54','Abstract rule proved; general algorithm not executed on arbitrary orders.'),
'A.1f':('Maximal quadratic order is not equivalent to all trace-zero descents','E:y²=x³+x over F7; rational 2-torsion test','15:56','Correct order is Z[sqrt(-p)]; maximal extension iff full rational E[2] for p=3 mod4.'),
'A.1g':('Corrected restriction equivalence of determinant rules on maximal-order descents','Pic(R) transitivity; A.1d; A.8c','15:56','Equivalence of rule torsors, not equality of all descent objects; normalized norm line required.'),
'A.1h':('Unique descent of the geometric rule on the exact finite-field Tate domain','A.1b; A.1d; equivariant bijection of nonempty Zp*-torsors','15:54','All primes and both F² signs; finite-only rules have separate constants unless geometric base-change compatibility is required.'),
'A.2a':('Integral adelic base, Kummer group, local Brandt image and splitting','R2 independently checked; norm of ramified ideal','15:40–46','A_int=R×product Z_l; f=([p],(1,1),[p]).'),
'A.2b':('Canonical quotient comparison torsor and trivial profinite Frobenius action','A.2a; positive global Eq(C) transport','15:42–48','Uniqueness among comparison-induced maps, not all abstract torsor maps.'),
'A.2c':('Neutral comparison gerbe and geometric section at every place','A.1d; A.2b; A.4a','15:50','The neutral p-component is part of this gerbe construction, not a split quaternion algebra.'),
'A.3a':('Positivity fixes real comparison class, leaving two automorphisms','A.4a; H¹ and H⁰ of real mu2','15:48,50,52','Residual sign is central mu2; no unique natural isomorphism.'),
'A.4a':('Quaternionic Hermitian realization with exact sign ambiguity','Deuring Hom lines; positive degree; Skolem–Noether','15:52','All H-linear maps are morphisms; unitary natural isomorphisms form {±1}.'),
'A.5a':('Rigidified Picard equivalence under symmetric condition C','Homotopy fibre of the norm functor; commutator coherence','15:36,74–78','Includes Pic(A prime) nonzero; Kummer Pic[n] term retained.'),
'A.5b':('Base-change admissibility condition and maximal-order case','Local two-sided ideal description; A.5a','15:16,36','Arbitrary nonflat ramified fibre must be tested; counterexample in A.5c.'),
'A.6a':('Unique Phi-normalized norm-line trivializations and determinant transport','Pic(A)=0; Phi∩A*=1; Phi A*=K*; Hasse–Schilling','15:21–22','For Z and Bp the generator is positive; identifies geometric degree with reduced norm.'),
'A.6b':('Bare uniqueness without the positive norm normalization is false','Sign gauge on distinct endomorphism-ring isomorphism classes','15:21–22','The p=11 j=0 and j=1728 classes separate the systems.'),
'A.7a':('Supersingular comparison determines the motivic mu2 pushout','Tate-dependent R3 band; Bp splitting-module gerbe','15:7–11,42–50','Local invariants 1/2 at p and infinity,0 elsewhere; compact component not determined.'),
'A.8a':('All Fp supersingular class counts and correction of triple identification','Voight30.9.2,30.9.10; exhaustive small-prime classification','15:56,70','p>3: h(-4p),4h(-p),2h(-p); p2=3,p3=4; trace-zero counts distinguished.'),
'A.8b':('Unit groups in the exceptional j cases; truncated question not recoverable','Explicit Weierstrass automorphisms; supplied witnesses','15:70','j0 order6 and j1728 order4 for p>3; orders24 at2 and12 at3.'),
'A.8c':('Maximal-order trace-zero triples have class number h(R)','Waterhouse4.1,4.2,4.5; Pic(R) action','15:56','Includes p2,p3; different from all Fp isomorphism classes.')}

def paragraph_titles(text):
    for m in re.finditer(r'\\paragraph\{',text):
        pos=m.end();depth=1;j=pos
        while depth and j<len(text):
            if text[j] in '{}': depth += 1 if text[j]=='{' else -1
            j+=1
        yield text[pos:j-1]

rows=[]
for title in paragraph_titles((R/'sections/A_deuring.tex').read_text()):
    m=re.match(r'(A\.\d+[a-z])\b',title)
    if not m:continue
    id=m.group(1)
    if id not in DESCRIPTIONS:continue
    statement,deps,pages,notes=DESCRIPTIONS[id]
    status='Refuted' if '(Refuted' in title else 'Known' if '(Known' in title else 'Proved under stated hypotheses' if '(Proved under' in title else 'Proved'
    rows.append(dict(zip(FIELDS,[id,statement,status,'sections/A_deuring.tex; paragraph '+id,deps,pages,notes])))
for p in (sorted((R/'agents').glob('*/results.csv'))
          + sorted((R/'agents').glob('*/*_results.csv'))):
    with p.open(newline='') as f:
        for row in csv.DictReader(f):
            row={k:row.get(k,'') for k in FIELDS}
            if not re.fullmatch(r'[A-F]\.\d+[a-z]',row['id']):
                continue  # Audit-only rows remain in their source review files.
            row['where_proved']=str(p.parent.relative_to(R))+'/'+row['where_proved']
            rows.append(row)
rows.extend([
 dict(zip(FIELDS,['C.2e','Universal A-prime implies A by a generic-pencil and codimension induction','Proved under stated hypotheses','sections/C2_pencil.tex','Extension-stable A-prime; weak and hard Lefschetz; rational Chow blow-up and transfer','14:44–47,130–131','All characteristics with ell not p. The geometric generic field and the descent to k(t) are explicit.'])),
 dict(zip(FIELDS,['C.2f','A implies A-prime; affine-vanishing implication has exactly the universal standard-A gate','Proved','sections/C2_pencil.tex','C.2b; C.2e; projection formula; Kleiman1968 Cor2.14','14:44–47','Equivalence with universal quantifiers; no geometric counterexample to the conjectural homological statement is claimed.'])),
 dict(zip(FIELDS,['C.2g','Critical-dimension A-prime implies every degree case by projective-bundle stabilization','Proved under stated hypotheses','sections/C2_pencil.tex','Critical A-prime; Bertini; Chow projective bundle and localization','14:45','Works for homological and algebraic equivalence in smooth very ample hyperplane setting; no false homological localization used.'])),
 dict(zip(FIELDS,['C.2h','Universal middle positivity gives all primitive degrees; product standard hypotheses give positive trace form','Proved under stated hypotheses','sections/C2_pencil.tex','Weak Lefschetz; algebraic inverse Lefschetz; product positivity; Kleiman3.7,3.11','14:45–46','Finite-dimensional rational correspondence algebra proved directly from positive rational trace pairing.'])),
 dict(zip(FIELDS,['C.2i','Semisimplicity and algebraic preimages for every algebraic cohomological map','Proved under stated hypotheses','sections/C2_pencil.tex','C.2h; radical argument; rational-polynomial pseudoinverse','14:46','General image criterion uses uvu=u; positivity alone retains exact standard-A gate.'])),
 dict(zip(FIELDS,['C.2j','Conditional Weil integrality, functional equation, absolute values and Frobenius semisimplicity','Proved under stated hypotheses','sections/C2_pencil.tex','Algebraic Kunneth projectors; bounded power sums; positive trace form; Poincare duality','14:45–46','All-prime integrality includes p; zero of P_i has inverse eigenvalue magnitude; determinant functional-equation sign retained.'])),
 dict(zip(FIELDS,['C.3e','Integral strict local cone injection for rational and algebraic equivalence','Proved','sections/C3_local.tex','Blow-up of cone; Chow localization; section Gysin and self-intersection; finite-data descent','14:106–109,113–117','The quotient CH^r(V)/LCH^(r−1)(V) injects into the punctured strict henselization; no surjectivity or completion claim.'])),
 dict(zip(FIELDS,['C.3f','Explicit strictly local threefold counterexample to finiteness and Gysin vanishing','Refuted','sections/C3_local.tex','C.3e; Fermat quartic generic-point diagonal obstruction; explicit hyperplane f=x2−wx3','14:106–108','Non-torsion algebraically trivial gamma survives strict henselization; regular hypersurface Gysin hits gamma and open restriction kills it.'])),
 dict(zip(FIELDS,['C.3g','Universal strict local high-degree finiteness fails in every nonempty proposed range','Refuted','sections/C3_local.tex','C.1i; C.3e; Fermat Calabi–Yau generic zero-cycle diagonal argument','14:106,109','All N≥3 and ceil((N+1)/2)≤r≤N−1; for r<N−1 the counterexample remains nonzero modulo algebraic equivalence over Q.'])),
 dict(zip(FIELDS,['C.3h','Exact Beauville-graded gates for both abelian Lefschetz injectivity assertions','Proved','sections/C3_abelian.tex','Beauville2010 Theorem4.2, Proposition5.2,5.5,5.11; invariant algebraic-equivalence subgroup and quotient','14:112–117','All characteristics with Q coefficients. First remaining tests are B²_(-1) in dimension5 and J²_(0) in dimension4; their vanishing is not asserted.'])),
 dict(zip(FIELDS,['F.2a','Two normalization corrections in the supplied Tate survey','Proved','sections/F_state.tex','Milne Tate survey Theorem1.6 and proof p3; Tate-structure equivalence definition p4','Literature supplied with Parts B–D','The middle-degree semisimplicity hypothesis is S^d on X×X; common finite-field extension uses crossed exponents.'])),
 dict(zip(FIELDS,['F.2b','Published correction of the supplied numerical positivity-cone statements','Known','sections/F_state.tex','Debarre–Ein–Lazarsfeld–Voisin2011 Theorem2.1 and Corollary2.2 pp1799–1801','Literature supplied with E.1','Strict cone inequality has range2≤k≤n−2; the CM-lattice rank-one approximation requires closure.']))
])
unique={x['id']:x for x in rows}
rows=sorted(unique.values(),key=lambda x:(x['id'][0],int(re.search(r'\d+',x['id']).group()),x['id']))
with (R/'RESEARCH_SA06_results.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows)
events=[]
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; /root; effort setting not separately exposed'
for row in rows:
    if row['id'].startswith('A.') and row['id'] in DESCRIPTIONS:
        events.append([row['id'],'2026-11-19',who,'targeted proof check',row['status']+': '+row['notes']])
for ids,program,scope in [(['A.1a','A.1b','A.1d'],'check_quaternion_crystal.py','Exact quaternion multiplication, discriminant and semilinear determinant contradiction; unit squareclass cardinalities.'),
                        (['A.1f','A.8a','A.8c'],'check_supersingular.py','Complete Weierstrass orbit enumeration at p=2,3; specified odd primes through43; exact F7 counterexample and reduced quadratic forms.'),
                        (['A.8b'],'check_small_automorphisms.py','Exact automorphism enumeration over F4 and F9:24 and12.')]:
    for id in ids:events.append([id,'2026-11-19',who,'computation or formal certificate',program+': '+scope])
for id,detail in [('R1','Condition C checked by local bi-ideal powers; symmetric norm homotopy fibre proved in A.5a; arbitrary-base-change claim refuted in A.5c.'),
                  ('R2','Recomputed all local components, the diagonal Brandt image and quotient in A.2a.'),
                  ('R4','Positive norm construction proved in A.6a; Brauer classification needs degree/type, as M2(Q) versus M3(Q) shows.'),
                  ('Lead A1','Proved on the corrected geometric domain in A.1d; unrestricted finite-field version refuted in A.1a.'),
                  ('Lead A2','Proved as a degree-one comparison refinement of the mu2 pushout in A.7a; does not determine compact component.'),
                  ('Lead A3','Class-number part proved; suggested completion of the truncated words remains unsupported.'),
                  ('Lead A4','Positive determinant norm structure and degree compatibility proved in A.6a.')]:
    events.append([id,'2026-11-19',who,'used and rechecked in this run',detail])
for p in (sorted((R/'agents').glob('*/CHECK_EVENTS.tsv'))
          + sorted((R/'agents').glob('*/*_CHECK_EVENTS.tsv'))
          + [R/'notes/ROOT_CHECK_EVENTS.tsv']):
    if not p.exists():continue
    with p.open(newline='') as f:
        for row in list(csv.reader(f,delimiter='\t'))[1:]:
            if len(row)==5:events.append(row)
with (R/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)

TASKS=[
('A.1','Refuted as stated; corrected all-p geometric and finite-field rules proved','A.1a–h','Unrestricted Fp² crystals and maximal-order/descent equivalence are false. The geometric rule descends exactly when F²=±p.'),
('A.2','Proved with the specified comparison meaning','A.2a–c','Integral adelic ring, positive global transport, right torsor, neutral comparison gerbe and all local components.'),
('A.3','Proved; unique-isomorphism claim refuted','A.3a','Positivity selects H¹ class; H⁰={±1} remains.'),
('A.4','Proved up to exactly two unitary natural isomorphisms','A.4a','Quaternionic realization, adjoints and degree norm.'),
('A.5','Refuted for arbitrary base change; qualified theorem proved','A.5a–d','Explicit F9 ramified fibre has noncommuting rigidified classes; condition C/Azumaya theorem includes nontrivial Picard groups.'),
('A.6','Proved with Phi normalization; bare uniqueness refuted','A.6a–b','Positive generator gives canonical multiplicative transport; gauge ambiguity otherwise.'),
('A.7','Proved under the stated Tate-dependent band identification','A.7a;D.0a;D.3b','Supersingular part determines mu2 class at every place, not the full compact-band class.'),
('A.8','Open as a full historical-text task; counts and units proved','A.8a–c','Missing end of Question: O* est-il tjrs égal cannot be reconstructed uniquely from the supplied witnesses.'),
('B.1','Proved, m=1','B.1a–b','Semisimple numerical-motive statement justified separately from an unproved general realization functor.'),
('B.2','Proved in every weight','B.1a;B.2a;B.3b','All p,q, positive/zero weights and listed examples; finite étale schemes allowed in degree0.'),
('B.3','Proved; proposed class obstruction refuted','B.3a–b','Weight-one factors may lie in an extension number field; fixed-field obstruction is a different assertion.'),
('B.4','Exact cokernel proved; unpowered-point premise refuted','B.4a–g','Unit-norm 2-part, full extension, finite lifting test, explicit exponent2hdr; base-change direction specified.'),
('C.1','Full universal A/A′/A″ and consequence ranges proved; exact positivity gate remains','C.1a–m','Nori complete intersections close all non-top A′/A″ ranges. B_alg is equivalent to injectivity of the primitive Griffiths map. Correspondence algebras are universally finite semisimple exactly in dimensions0 and1.'),
('C.2','Pencil equivalence, critical reduction and conditional consequences proved; conjectural implications remain','C.2b–j','Affine-to-Gysin implication is exactly standard A; positivity-alone implication over C also has this gate. Complete positive-involution, algebraic-image, and conditional Weil arguments supplied.'),
('C.3','Strict local high-range finiteness refuted; exact abelian injectivity gates proved; general and low-local gates remain','C.3a–h;C.1f','Integral strict local cone injection closes the localization gap and refutes all proposed high finiteness ranges. Abelian injectivity is equivalent to vanishing of negative B pieces, respectively nonpositive J pieces; the first test groups are identified exactly.'),
('C.4','Integral results and sharper bounds proved; residual nonprincipal cases open','C.4a–q','Exact factorization obstruction divides gcd(2,delta(A)) for surfaces and gcd(6,delta(A)) for threefolds. Proper-abelian-subvariety curves have an exact kappa(e) cross-class obstruction, a method limitation rather than a general counterexample.'),
('C.5','Settled over the two requested fields','C.5a–f','All chain statements hold over Fpbar and fail universally over C. The requested field-specific implications follow from these truth values; no arbitrary-field structural equivalence is asserted.'),
('D.1','Proved criterion and correction; D(Q) repair refuted','D.1a–e','Odd denominators, maximal Galois-stable domain, q25 exact example; canonical even grading distinct from slope parity.'),
('D.2','Proved in the stated finite-lattice and full-group settings','D.2a–b','Real orbit classification; rational mod2 invariant and q17 counterexample; no unproved infinite-rank extension.'),
('D.3','Proved under the stated R3 band identification','D.3a–b','Class has infinite order by actual-gerbe evaluations of all orders r; inversion does not lift.'),
('D.4','Abelian-family compatibility proved; all-motives effectivity has exactly the Tate gate','D.4a–g','Under the stated semisimple numerical/faithful-realization framework, integral-spectrum effectivity is equivalent to all Tate cycle surjectivity. Common geometric polarization is proved for arbitrary abelian families with extending correspondences, using the cited2026 theorem; general geometric motives remain.'),
('E.1','Proved with exact cone-definition distinction','E.1a–e','Bipolar saturation; additive and root-saturated counterexamples; closed convex lattice version proved.'),
('E.2','Arithmetic statement proved; motivic assertion conditional','E.2a–e','Full integral cocharacter and global finiteness false; finite-field slope orbit recovered; effectivity of motives retains Tate.'),
('E.3','Forward implication proved in every characteristic; integral biconditional refuted; exact Walker quotient proved under surface support','E.3a–l','For one-cycles with CH0 supported on a surface, the Albanese-equivalence quotient is canonically the Walker Jacobian integrally. The family converse is true on the explicit fourfold where ordinary Abel–Jacobi equality fails. General intermediate-codimension converse retains the Walker-kernel gate.'),
('E.4','Literal values refuted; corrected all-twist proper/open theory and finite comparison proved','E.4a–p','Specified real-place-retaining complexes cover Fq and every finite-prime open of Spec Z. Exact wild support is retained at twists≤0; full purity holds for twists≥2. Classical low-degree Lichtenbaum comparison is distinguished from bounded Flach–Morin conventions.'),
('E.5','General torsor expectation settled; unspecified motivic model/phrase open','E.5a–g','Algebraically closed uniqueness; perfect-field and even cd1 pro-torsor counterexamples; smooth finite-type Witt torsors versus a genuine pro-limit obstruction; varying Newton slopes.'),
('E.6','Proved','E.6a–b','Decomposition-group Artin class; trivial Tate part; tuple over k⊗Q_l.'),
('F.1','In progress while mathematical tasks remain','Statement register','Each proved proposition separated from scope of its parent item.'),
('F.2','In progress; opened/not-obtained record maintained','Bibliography and source registers','Exact numbered primary inputs and unsuccessful retrievals recorded.'),
('Lead A1','Proved on corrected domain','A.1d–e','Crystalline principal polarization with norm/degree compatibility.'),
('Lead A2','Proved under R3 hypotheses','A.7a','Comparison refinement; full compact component distinct.'),
('Lead A3','Class-count part proved; proposed wording open','A.8a–c','Two supplied witnesses end at the same unfinished phrase.'),
('Lead A4','Proved with normalization','A.6a','Canonical positive norm line.'),
('Lead B1','Proved and strengthened','B.1a;B.3a','m=1 unrestricted; m=i also gives same-field factors after base extension.'),
('Lead B2','Refuted as realization obstruction; exact lattice repair proved','B.3a;B.4a–f','Class group alone omits unit and torsion/normalization issues.'),
('Lead C1','Proved with stated integral and polarization qualifications','C.4a,c,e','Degree1 theorem; generic-cycle criterion; ppav minimal-class equivalence.'),
('Lead D1','Refuted as proposed protorus repair; criterion proved','D.1a,c,d','Hom(mu2,D(Q))=0; slope parity does not decide all real-functor existence.'),
('Lead E1','Proved for full finite-CM rational slope cones','E.2d','Facet normal orbit and decomposition field; no integral normalization asserted.'),
('Lead E2','Literal integral identification refuted; rational pattern proved','E.4a–d','An unspecified real-place modification is not silently identified with standard Weil–étale theory.'),
('Lead E3','Structured interpretation proved; exact historical identification open','E.5c–d','F-crystals/lattices and B(G) distinguished; continuous H¹ not defined by supplied text.'),
('Lead E4','Rational equivalence proved; literal integral biconditional refuted','E.3c,g–l','On the same explicit fourfold, the entire-family converse holds but equality of the integral equivalence relations fails. Under CH0 support on a surface the discrepancy is exactly the finite Walker-isogeny kernel.')]

stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
lines=['INCOMPLETE','','| Item | Outcome at this checkpoint | Statement IDs | Scope / exact remaining gate |','|---|---|---|---|']
for row in TASKS:lines.append('| '+' | '.join(row)+' |')
lines += ['',f'Updated: {stamp}.','',
'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. We distinguish proofs of stated propositions, imported theorems with checked deductions, computations of finite examples, and tasks still being pursued. This is a current research checkpoint, not a claim of completion.',
'','## Primary findings and qualifications','',
'The all-weight Frobenius realization problem has a direct unconditional solution: extract an i-th root, apply Honda–Tate in weight1, and use the i-fold product. This argument is already present in Milne (1994, Proposition2.6, proof). It gives m=1. The class group of the originally chosen CM field cannot obstruct a realization that is allowed to use a larger number field.',
'',
'The corrected Deuring rule is the crystalline cup-trace pairing transported from the uniquely reconstructed oriented supersingular curve. We prove independence, the exact unit-squareclass torsor, field-automorphism invariance, and Morita norm compatibility. The literal finite-field crystal domain has an explicit p=3 counterexample, and the maximal quadratic-order/descent equivalence has an explicit F7 counterexample. The ramified F9 base change also refutes the universal Picard assertion.',
'',
'The cycle analysis separates algebraic-equivalence counterexamples from unresolved assertions about algebraic classes in cohomology. An incidence blow-up construction shifts the quintic Griffiths group and gives failure of universal A in every nontrivial degree range. This is not evidence for failure of the distinct higher injectivity statement. Modern integral curve-class counterexamples on very general principally polarized abelian varieties are taken from the opened 2026 version of Engel–de Gaay Fortman–Schreieder, with their preprint status explicit.',
'','## Root computations','',
'All scientific programs and their exact outputs are retained. The root programs use exact integer/Fraction/SymPy or finite-field arithmetic; no floating-point inference is used.',
'',
'| Program | Inputs and scope | Output |','|---|---|---|',
'| code/check_quaternion_crystal.py | p=3 order basis, quaternion multiplication and trace discriminant, F=4J sigma; local unit squareclasses | code/check_quaternion_crystal_output.json |',
'| code/check_supersingular.py | Complete general-Weierstrass orbit enumeration at2,3; odd primes5,7,11,13,17,19,23,29,31,37,43; F7 counterexample; reduced forms/class numbers | code/check_supersingular_output.json |',
'| code/check_small_automorphisms.py | Automorphisms of the exceptional supersingular curves over F4,F9 | code/check_small_automorphisms_output.json |',
'| code/check_local_cone.py | Fermat quartic points, regular hyperplane, three projective Jacobian certificates, blow-up chart | logs/local_cone_certificate.json |',
'',
'Exact run times are embedded in the JSON outputs. The general all-p formula and proofs do not rest on extrapolation from this finite list. The general crystalline reconstruction algorithm is specified mathematically and has not been run on arbitrary input orders.',
'','## Root readings and corrections','',
'We read the attached prompt, the relevant sweep-3 and SA05 arguments, and the transcriptions at15:16–22,34–78. We opened Deuring1941, Voight2021 Chapters14/30/42, Waterhouse1969, Yu2026, and the primary sources identified in the collaborators’ records. R1,R2,R4 and LeadsA1–A4 are checked at the paragraphs that use them. Classification solely by Brauer class omits degree: the rank-one categories of M2(Q) and M3(Q) have nonisomorphic endomorphism algebras. The sign at infinity is separated into an H¹ class fixed by positivity and an H⁰ automorphism group left equal to {±1}.',
'',
'The phrase at15:70 has no supplied completion. Michel Hua’s project likewise writes “page s’arrête sur une question” and quotes the same unfinished words (15.modern.tex, surrounding the discussion of archive page69). We credit that witness only for confirming the truncation; it supplies no missing mathematical assertion. We independently checked the exceptional automorphism orders and the reversed 4/6 association in the transcription.',
'',
'A preliminary orientation formula using the conjugate action on M/FM was corrected before the checkpoint: with D(f)=(f-dual)*, the raw action is the tangent-space orientation. The earlier draft’s statement that an unimplemented all-p algorithm leaves the explicit rule unproved was removed: the mathematical formula and terminating reconstruction are proved, while execution scope is separately recorded. The former unresolved A.5 base-change paragraph is superseded by the explicit F9 counterexample.',
'','## Typesetting verification','']
layout=R/'logs/latest_layout.json'
if layout.exists():
    d=json.loads(layout.read_text());lines += [f"Latest completed build: {d['utc']}; overfull boxes: {d['overfull_count']}, over2pt: {d['overfull_gt_2pt']}, maximum: {d['maximum_overfull_pt']}pt; missing characters: {d['missing_characters']}.",'','Visual inspection and before/after layout counts are recorded in logs/QA_RECORD.md when performed.']
else:lines += ['The first full LuaLaTeX build and visual inspection are in progress. No unverified PDF is certified as publication-ready.']
lines += ['','## Contributor proof, computation, source and approach records','',
'The following records preserve the exact limitations and failed approaches. Earlier retrieval failures remain documented even when a later source was obtained; the later dated successful opening supersedes the initial unavailable status. Raw third-party PDFs and text extractions are research inputs and are excluded from deliverable ZIPs.','']
for rel in ['agents/frobenius/REPORT.md','agents/frobenius/A_review.md','agents/frobenius/C4_REVIEW.md','agents/frobenius/C4_prym_REVIEW.md','agents/frobenius/C4_pt6_REVIEW.md','agents/frobenius/C4_residual_REVIEW.md','agents/frobenius/Nori_independent_REVIEW.md','agents/frobenius/C3_E4_independent_REVIEW.md','agents/frobenius/C3_abelian_independent_REVIEW.md','agents/frobenius/E3_walker_independent_REVIEW.md','agents/frobenius/D4_refinements_independent_REVIEW.md','agents/frobenius/F2_independent_REVIEW.md','notes/ROOT_SOURCE_AUDIT.md','agents/cycles/STATUS.md','agents/cycles/notes/source_record.md','agents/real_weil/REPORT.md','agents/real_weil/SOURCE_AUDIT.md']:
    p=R/rel
    if p.exists():lines += ['---','',f'### Record: {rel}','',p.read_text(),'']
(R/'RESEARCH_SA06_report.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'statements':len(rows),'check_events':len(events),'task_and_lead_rows':len(TASKS),'updated':stamp}))
