#!/usr/bin/env python3
"""Assemble auditable research registers from the proof owners' records."""
from pathlib import Path
import csv,re,json,datetime
from normalize_check_events import EventNormalizer
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
'A.8b':('Unit groups in the exceptional j cases; original scan confirms unfinished question','Explicit Weierstrass automorphisms; supplied witnesses and official scan70','15:70','j0 order6 and j1728 order4 for p>3; orders24 at2 and12 at3.'),
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
    m=re.match(r'(A\.\d+[a-z]+)\b',title)
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
            if not re.fullmatch(r'[A-F]\.\d+[a-z]+',row['id']):
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
 dict(zip(FIELDS,['C.3l','Both universal abelian injectivity assertions together are equivalent to ordinary Beauville negative-index vanishing','Proved','sections/C3_global_abelian.tex','C.3h; Poincare parameterization of ordinary algebraic equivalence; Beauville2010 equation5.9','14:112–117','All algebraically closed characteristics with Q coefficients. J^r_s is evaluated from index s−1 on products with parameter Jacobians; no fixed-dimension bound or vanishing is asserted.'])),
 dict(zip(FIELDS,['C.3r','Ordinary local higher-cycle restriction is non-surjective at every boundary dimension N=2r+1','Refuted','sections/C3_fermat_boundary.tex','C.3e; two transverse Fermat-join correspondences; weak Lefschetz and Abel-Jacobi functoriality; Skalit Cor6.4(i)','14:106–109','For every r>=1 the regular strict-local source has CH^r=0 and its regular Fermat-cone divisor has an actual injected nontorsion elliptic family.'])),
 dict(zip(FIELDS,['C.3s','Exact universal local Chow and ordinary-J finiteness range over C','Refuted','sections/C3_segre_nonvanishing.tex','C.3e; Calabi-Yau generic-point diagonal obstruction; Segre projective-bundle quotient','14:106–109','For every N>=2 and1<=r<N an explicit normal strict-local Segre cone has ordinary J^r_Q nonzero. For r>=N both groups vanish by dimension. No extension of the separate modulo-algebraic-equivalence range is asserted.'])),
 dict(zip(FIELDS,['C.3v','Exact ordinary divisor quotient on the strict local Segre-quartic cone in every dimension at least two','Refuted','sections/C3_ordinary_divisor_quotient.tex','Formal logarithm and Grothendieck existence; Elkik III Picard corollary p573; proper-curve affine-coordinate rigidity','14:106–109','B1(X2)=C(additive) plus Z/4 and B1(XN)=C^(N-1) plus Z for N>=3, integrally. An explicit residue-one formal transition descends to a unique nontorsion line-bundle class. The connected-local-Picard relation is different.'])),
 dict(zip(FIELDS,['C.3z','General excellent henselian coefficient-field germs admit a regular algebraic model map and ordinary Picard subgroup point realization','Proved','sections/C3_completion_algebraization.tex','Artin1969 Theorem3.8; formal Jacobian criterion; Stacks07QY/07NT; C.3p/w; direct finite p-power kernel and fppf abelian lift','14:106–109','The actual regular A0-to-R map induces an isomorphism of completions and pulls back a regular alteration. Every proper local-Picard abelian subgroup is realized pointwise by ordinary product families. For all such germs in characteristic p and N>=4 ordinary Pic_alg restricts surjectively with p-primary kernel. No simultaneous algebraization of f or mixed-characteristic ordinary-equivalence assertion.'])),
 dict(zip(FIELDS,['C.3ax','For every smooth connected projective cone in characteristic p with normal degree-one full section ring, restriction K0(Z)[1/p] to the exceptional variety is an isomorphism; rational Chow and ordinary-B puncture groups are exactly the hyperplane quotients, and the top ordinary quotient is zero','Proved','sections/C3_positive_characteristic_cone_rigidity.tex','KerzStrunkTamme2018 TheoremA/(1.6); GeisserHesselholt2011 TheoremA; ThomasonTrobaugh1990 Theorem8.1; Fulton1998 Example15.2.16(b); C.3e','14:106–109','All algebraically closed characteristic-p fields and all cone dimensions at least two. A restricted cone theorem, not a closure of arbitrary strict-local rational top finiteness. Complete independent proof and fresh primary-source audit retained.'])),
 dict(zip(FIELDS,['C.3bm','For every algebraically closed field of positive characteristic, the ordinary rational top quotient of every algebraizable normal strict-local threefold with regular puncture is the exceptional-surface perfect-family quotient, with all component degrees explicitly removed','Proved reduction','sections/C3_general_threefold_presentation.tex; complete FF/EL/EP auxiliaries in agents/real_weil/C3_tetrahedral_endpoint_bundle.tex','Field-uniform C3bd geometry; CossartPiltant Theorem1.1/Proposition4.4; KollarWitaszek Lemmas6/8; CJS Corollary0.4; Stacks09MS; FF.4; EL.1; EP.1-4; negative exceptional intersection matrix','14:106–109','All primes including2/3, all algebraically closed coefficient fields in the stated algebraizable threefold scope. Every actual proper perfect-family relation on E is realized by endpoints of an actual cycle family on Z; no whole-family extension or negative-K boundary vanishing remains as a condition. Residual gate is the degree-zero quotient S0(E)/(J_K(E)+(S0(E) intersect exceptional image)). Intrinsic global SNC family gluing is still uncomputed; no universal vanishing, characteristic-zero statement or higher restriction result. Full root and both independent proof/source audits passed.'])),
 dict(zip(FIELDS,['F.2a','Two normalization corrections in the supplied Tate survey','Proved','sections/F_state.tex','Milne Tate survey Theorem1.6 and proof p3; Tate-structure equivalence definition p4','Literature supplied with Parts B–D','The middle-degree semisimplicity hypothesis is S^d on X×X; common finite-field extension uses crossed exponents.'])),
 dict(zip(FIELDS,['F.2b','Published correction of the supplied numerical positivity-cone statements','Known','sections/F_state.tex','Debarre–Ein–Lazarsfeld–Voisin2011 Theorem2.1 and Corollary2.2 pp1799–1801','Literature supplied with E.1','Strict cone inequality has range2≤k≤n−2; the CM-lattice rank-one approximation requires closure.']))
])
rows.append(dict(zip(FIELDS,[
 'C.3bw',
 'For any noetherian local coefficient-k algebra with algebraically closed residue field k and any fixed smooth connected projective surface S, perfect K0(R times S) has integral F_gamma^3=0 and is annihilated by (psi^2-1)(psi^2-2)(psi^2-4). In the characteristic-p fixed-product blow-up setting, the polynomial image of every actual K1(E times S)_Q class lifts to Z times S; all weight-three classes lift and the weight-three K0 restriction kernel is zero.',
 'Proved (auxiliary strengthening)',
 'sections/C3_parameter_surface_lifting.tex; PS.1-PS.8',
 'Relative Serre and first-jet incidence; actual finite etale Koszul supports; semilocal projective modules; exact gamma identities; FF every-degree fixed-product comparison',
 'none additional (auxiliary strengthening)',
 'Integral bound in every characteristic with no regularity, normality or henselian hypothesis on R. The lifting consequence is rational and characteristic p. Two complete independent mathematical audits passed the full root research proof; the polynomial variant follows by naturality on the actual surface. No supported boundary-node vanishing or symbolic-family compactification is proved; UK.7 and main statuses are unchanged.'
])))
unique={x['id']:x for x in rows}
rows=sorted(unique.values(),key=lambda x:(x['id'][0],int(re.search(r'\d+',x['id']).group()),len(re.search(r'[a-z]+$',x['id']).group()),x['id']))
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
event_normalizer = EventNormalizer(R)
for p in (sorted((R/'agents').glob('*/CHECK_EVENTS.tsv'))
          + sorted((R/'agents').glob('*/*_CHECK_EVENTS.tsv'))
          + sorted((R/'notes').glob('ROOT*_CHECK_EVENTS.tsv'))):
    if not p.exists():continue
    with p.open(newline='') as f:
        for line, row in enumerate(list(csv.reader(f,delimiter='\t'))[1:], start=2):
            if len(row)==5:
                normalized = event_normalizer.normalize(p, line, row)
                if normalized is not None:
                    events.append(normalized)
event_normalizer.save()
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
('A.8','Open as a full historical-text task; counts and units proved','A.8a–c','Official scan70 itself ends after égal; adjacent scans and the next handwritten page supply no continuation. The missing comparison cannot be reconstructed uniquely.'),
('B.1','Proved, m=1','B.1a–b','Semisimple numerical-motive statement justified separately from an unproved general realization functor.'),
('B.2','Proved in every weight','B.1a;B.2a;B.3b','All p,q, positive/zero weights and listed examples; finite étale schemes allowed in degree0.'),
('B.3','Proved; proposed class obstruction refuted','B.3a–b','Weight-one factors may lie in an extension number field; fixed-field obstruction is a different assertion.'),
('B.4','Exact cokernel proved; unpowered-point premise refuted','B.4a–g','Unit-norm 2-part, full extension, finite lifting test, explicit exponent2hdr; base-change direction specified.'),
('C.1','Universal A/A-prime/A-double-prime and consequence ranges settled; exact positivity and image gates proved','C.1a–q','Nori complete intersections close all non-top A-prime/A-double-prime ranges. Universal B_alg is equivalent to all shifted Griffiths injections h^(n-2i+1); on all projective-space stabilizations of a fixed abelian variety it is exactly vanishing of its negative and grade-zero Griffiths pieces. Every threefold times an odd-dimensional projective space satisfies its own B; that individual premise does not imply a semisimple correspondence ring. For a fixed target the universal image criterion is exactly standard D plus its Griffiths-group vanishing. C.1q gives the exact ample blow-up primitive kernel and excludes the specified products; no primitive Griffiths witness is constructed. The universal positivity and standard-conjecture gates remain open.'),
('C.2','Pencil equivalence, critical reduction and conditional consequences proved; conjectural implications remain','C.2b–k','Affine-to-Gysin implication is exactly standard A; positivity-alone implication over C also has this gate. Complete positive-involution, algebraic-image, and conditional Weil arguments supplied. Classical D is proved in codimensions0,1,2,n−1,n over C, hence in every degree for n<=4; the first remaining case there is codimension3 on a fivefold. The arbitrary-source image quantifier remains.'),
('C.3', 'Entire ordinary complex local restriction table classified; integral finiteness refuted in every nonzero codimension and positive characteristic; global and rational top gates remain', 'C.3a–be;C.1f', 'For every r>=2 over C, ordinary J^r restriction is universally injective exactly for N<=r, universally surjective exactly for N<=r+1, and universally an isomorphism exactly for N<=r, integrally and rationally. C.3ao supplies all remaining higher kernels via an actual full-Picard kernel and an absolute differential product detector; C.3ap exhausts every dimension. For r=1 injection holds exactly for N=1 or N>=3, surjection exactly for N<=2, and isomorphism exactly for N=1. C.3ae–aj supply all cokernel ranges and stronger Jacobian quotients where stated. Ordinary J^r_Q can be nonzero for every1<=r<N; universal local finiteness holds only for r>=N. The previously stated degree-one characteristic-p table keeps its coefficient-field and p-primary qualifications. Fpbar ordinary-J groups vanish rationally. Exact B1 quotients are nonfinite in all positive local dimensions where divisors occur; C.3aa gives rational non-top B^r examples over C for2<=r<=N−2. C.3an/aq treat dimension3 and C.3as gives an explicit integral top quotient. C.3ba/bb extend this to an explicit integral B^r quotient onto(k,+) for every algebraically closed characteristicp>0, every N>=2 and every1<=r<=N−1, including Fpbar. Thus integral finiteness is false in every positive codimension in which cycles can occur. The geometric Segre extension and actual Cartier endpoint retain ordinary families and use maps only on resolutions. Its exponent-p target gives no rational or complex nonvanishing. C.3at and C.3av prove ordinary restriction nonsurjectivity in every positive characteristic for every r>=1 and r+2<=N<=2r+1, with regular ambient source and actual nontorsion families over specified transcendental algebraically closed fields. C.3aw and C.3ay prove ordinary restriction noninjectivity in every positive characteristic for r>=2 and r+1<=N<=2r; the critical construction vanishes integrally on the target even when p divides r. C.3be proves CH_1(Spec R)_Q=CH^(N−1)(puncture)_Q=0 for every excellent local domain of dimension N>=2 with residue field Fpbar, including mixed characteristic; neither henselianity, normality, a regular puncture, nor a finite-type field model is required. Finite semilocal normalization replaces the earlier single henselian branch. The ordinary quotient vanishes wherever defined. The proof uses a normalized surface through each curve, finite K0 detection, determinant, and the negative exceptional intersection matrix; it does not require higher-dimensional resolution. This residue-field-restricted result does not settle the universal arbitrary-field top gate. C.3bd supplies the earlier algebraizable normal dimension2/3 corollary with the stated regular puncture. C.3ab/ad/ar/au/ax/az/bc are additional restricted positive top theorems; bc proves the stronger top rational Chow vanishing over Fpbar for the stated algebraizable SNC resolution with an ample negative exceptional combination, using explicit weight-preserving descent and a negative-definite component matrix; az computes the top rational Chow quotient for an algebraizable germ with one smooth connected exceptional Cartier divisor and ample conormal, without assuming a retraction; au settles the specified complex Fermat-quintic cone by a whole-family first-jet trace argument; ax computes every rational Chow and ordinary-B cone quotient in positive characteristic for the stated normal degree-one full section rings; ar settles external-product polarizations on products of curves over Qbar after extension to C, without closing the unrestricted rational top gate; C.3ac settles the finite-field abelian branch, with its stronger2026-qualified consequence separate. Remaining main gates are universal global projective Griffiths/Beauville injectivity, rational top B^(N−1) for N>=3 including the complex case, and higher-degree positive-characteristic restriction beyond the proved intervals (injectivity for N>=2r+1 and surjectivity for N>=2r+2, r>=2). The proof register distinguishes full proofs, primary-source audits, finite certificates and reconstruction records; restoration itself is not counted as mathematical movement.'),
('C.4','Integral splitting results and an exact numerical surface-class gate proved; real-multiplication and supersingular families settled; general nonprincipal cases remain','C.4a–ab','In dimensions2,3 over every algebraically closed field, actual splitting is equivalent to integral numerical algebraicity of P²/2 or P⁴/24 on A×dual(A). The obstruction divides gcd(2,delta(A)) or gcd(6,delta(A)); all supersingular surfaces and all supersingular threefolds in p>=5 are affirmative. Full maximal real multiplication with compatible polarization gives delta=1 in characteristic zero, at good reductions and for ordinary varieties. In arbitrary positive characteristic, even nonordinary, delta is a p-power and equals1 under the intrinsic Lie Grothendieck condition; total ramification implies that condition, including p2/3. In the characteristic-zero/ordinary scope, local maximality only at2 for a surface or2,3 for a threefold suffices. C.4y excludes the integral Chern subring generated by semihomogeneous bundles on an End=Z type(1,2) surface product. C.4z proves an abstract correlated three-colour graph obstruction at every positive integral level. These are method results. C.4aa refutes the unrestricted transfer from algebraic minimal classes to common coloured graph splittings by an actual principally polarized abelian-surface monodromy countermodel. Thus z requires additional geometric hypotheses; no nonalgebraicity statement about arbitrary cycles follows. C.4ab gives an exact integral partial Fourier parity criterion in the stated complex type(1,2) Hodge-endomorphism scope, equivalent both to actual Jacobian-product splitting and to algebraicity of the first integral Kunneth projector. It excludes the stated residual fibre-product construction but does not shrink the main gate. Generic End=Z type(1,2) surfaces, general nonprincipal threefold integrality and arbitrary supersingular threefolds in p2/3 remain undecided.'),
('C.5','Settled over the two requested fields','C.5a–f','All chain statements hold over Fpbar and fail universally over C. The requested field-specific implications follow from these truth values; no arbitrary-field structural equivalence is asserted.'),
('D.1','Proved criterion and correction; D(Q) repair refuted','D.1a–e','Odd denominators, maximal Galois-stable domain, q25 exact example; canonical even grading distinct from slope parity.'),
('D.2','Proved in the stated finite-lattice and full-group settings','D.2a–b','Real orbit classification; rational mod2 invariant and q17 counterexample; no unproved infinite-rank extension.'),
('D.3','Proved under the stated R3 band identification','D.3a–b','Class has infinite order by actual-gerbe evaluations of all orders r; inversion does not lift.'),
('D.4','Abelian-family compatibility proved; all-motives effectivity has exactly the Tate gate','D.4a–g','Under the stated semisimple numerical/faithful-realization framework, integral-spectrum effectivity is equivalent to all Tate cycle surjectivity. Common geometric polarization is proved for arbitrary abelian families with extending correspondences, using the cited2026 theorem; general geometric motives remain.'),
('E.1','Proved with exact cone-definition distinction','E.1a–e','Bipolar saturation; additive and root-saturated counterexamples; closed convex lattice version proved.'),
('E.2','Arithmetic statement proved; motivic assertion conditional','E.2a–e','Full integral cocharacter and global finiteness false; finite-field slope orbit recovered; effectivity of motives retains Tate.'),
('E.3','Settled in the requested scope: forward implication proved in every characteristic; complex converse refuted even rationally by a specified sixfold and elliptic family','E.3a–u','The full morphic Abel-Jacobi map kills N and gives the stronger necessary Lawson-cylinder vanishing criterion. A geometric generic degree14 hypersurface in split Q6, its two-plane difference gamma, and E:y²=x³−x give a whole family with zero integral Betti class and nonzero rational Lawson cylinder. The specified generic elliptic point is nontorsion modulo N after every complex embedding. Thus N is strictly smaller than the finite Walker kernel even rationally; the previous surface-generation equality is false. Exact fixed-variety criteria and the proved low-dimensional/support cases remain valid. The one-motivic sheaf quotient is identified integrally without a finite-type assertion.'),
('E.4','Literal values refuted; corrected all-twist proper/open theory and finite comparison proved','E.4a–p','Specified real-place-retaining complexes cover Fq and every finite-prime open of Spec Z. Exact wild support is retained at twists≤0; full purity holds for twists≥2. Classical low-degree Lichtenbaum comparison is distinguished from bounded Flach–Morin conventions.'),
('E.5','General torsor expectation settled; unspecified motivic model/phrase open','E.5a–g','Algebraically closed uniqueness; perfect-field and even cd1 pro-torsor counterexamples; smooth finite-type Witt torsors versus a genuine pro-limit obstruction; varying Newton slopes.'),
('E.6','Proved','E.6a–b','Decomposition-group Artin class; trivial Tate part; tuple over k⊗Q_l.'),
('F.1','In progress while mathematical tasks remain','Statement register','Each proved proposition separated from scope of its parent item.'),
('F.2','In progress; opened/not-obtained record maintained','Bibliography and source registers','Exact numbered primary inputs and unsuccessful retrievals recorded.'),
('Lead A1','Proved on corrected domain','A.1d–e','Crystalline principal polarization with norm/degree compatibility.'),
('Lead A2','Proved under R3 hypotheses','A.7a','Comparison refinement; full compact component distinct.'),
('Lead A3','Class-count part proved; proposed wording open','A.8a–c','Both supplied witnesses and the now-inspected official original end at the same unfinished phrase.'),
('Lead A4','Proved with normalization','A.6a','Canonical positive norm line.'),
('Lead B1','Proved and strengthened','B.1a;B.3a','m=1 unrestricted; m=i also gives same-field factors after base extension.'),
('Lead B2','Refuted as realization obstruction; exact lattice repair proved','B.3a;B.4a–f','Class group alone omits unit and torsion/normalization issues.'),
('Lead C1','Proved with stated integral and polarization qualifications','C.4a,c,e','Degree1 theorem; generic-cycle criterion; ppav minimal-class equivalence.'),
('Lead D1','Refuted as proposed protorus repair; criterion proved','D.1a,c,d','Hom(mu2,D(Q))=0; slope parity does not decide all real-functor existence.'),
('Lead E1','Proved for full finite-CM rational slope cones','E.2d','Facet normal orbit and decomposition field; no integral normalization asserted.'),
('Lead E2','Literal integral identification refuted; rational pattern proved','E.4a–d','An unspecified real-place modification is not silently identified with standard Weil–étale theory.'),
('Lead E3','Structured interpretation proved; exact historical identification open','E.5c–d','F-crystals/lattices and B(G) distinguished; the directly inspected original191/193 explicitly calls F,V extra structure but supplies no formal definition of continuous H¹.'),
('Lead E4','Rational equivalence of the assertions proved; the universal complex converse and rational equality both refuted; literal integral biconditional refuted','E.3c,g–u','Over C the rational and integral whole-family converses are equivalent to N=ker(finite Walker). The specified sixfold refutes this equality even rationally and supplies an elliptic-family witness. The specified fourfold still separates the integral family converse from ordinary integral Abel-Jacobi equality by an order-two cycle. Thus the rational equivalence in the Lead is valid, while its literal integral reading is false.'),

]
if 'C.3bh' in unique:
    TASKS = [
        (item, state + '; entire integral ordinary divisor restriction table classified in every positive characteristic',
         statements.replace('C.3a–be', 'C.3a–bh'),
         scope + ' C.3bf supplies the first characteristic-five kernel. C.3bg constructs an injected (Z/p)^{min(3,N-1)} in the actual ordinary integral Picard restriction kernel for every prime p and every N>=3, with examples over Fpbar and hence over every algebraically closed field of characteristic p. C.3bh completes the integral ordinary divisor dimension table in the full excellent henselian normal coefficient-field scope of C.3z: universally injective exactly for N=1, universally surjective exactly for N<=2 or N>=4, and universally an isomorphism exactly for N=1. Explicit finite-order elliptic boundary classes cover N=2 and N=3 even over Fpbar. The rational table and all higher-codimension remaining ranges are unchanged.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
elif 'C.3bf' in unique:
    TASKS = [
        (item, state + '; integral ordinary divisor injectivity refuted in characteristic five for N>=4',
         statements.replace('C.3a–be', 'C.3a–bf'),
         scope + ' C.3bf gives an injected (Z/5)^3 in the actual ordinary Picard restriction kernel for every N>=4 over F5bar, using a specified nonsplit Fermat-quartic Segre model and a fixed proper-curve family. This is an integral negative result; the rational assertions and all higher-codimension remaining ranges are unchanged.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bi' in unique and 'C.3bj' not in unique:
    TASKS = [
        (item, state + '; integral codimension-two injectivity refuted at p=5,N=5',
         statements.replace('C.3a–bh', 'C.3a–bi'),
         scope.replace('The rational table and all higher-codimension remaining ranges are unchanged.',
                       'The rational divisor table is unchanged.')
         + ' C.3bi constructs a fully specified ordinary codimension-two class of exact order five over F5bar in the kernel at local dimension five. Its actual fixed-curve family, finite-field incidence geometry, relative-to-absolute K0 injection, exceptional Chow boundary, and integral Adams separation are proved. This removes the integral p=5,r=2,N=5 instance from the higher restriction gate; the rational instance and all other unproved characteristic/dimension cases remain. The later all-prime K-cohomology approach is research in progress and is not included in this certified conclusion.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bj' in unique and 'C.3bk' not in unique:
    TASKS = [
        (item, state + '; integral ordinary codimension-two injectivity table classified in every positive characteristic',
         statements.replace('C.3a–bh', 'C.3a–bj'),
         scope.replace('The rational table and all higher-codimension remaining ranges are unchanged.',
                       'The rational divisor table is unchanged.')
         .replace('higher-degree positive-characteristic restriction beyond the proved intervals (injectivity for N>=2r+1 and surjectivity for N>=2r+2, r>=2)',
                  'higher-degree positive-characteristic restriction beyond the proved intervals (rational injectivity for N>=2r+1,r>=2; integral injectivity for N>=2r+1,r>=3; surjectivity for N>=2r+2,r>=2)')
         + ' C.3bi retains the fully specified p=5,r=2,N=5 example and its independent integral K-theory/Adams proof. C.3bj constructs an actual ordinary codimension-two class of exact order p in the restriction kernel for every prime and every N>=5, already over Fpbar and every algebraically closed extension. Its rank-one relative Milnor differential quotient, divisible preceding K-cohomology group, entire exceptional Picard-image calculation and finite-type Chow-product comparison include p=2. Together with aw/ay this proves universal integral codimension-two injectivity exactly for N<=2 when quantifying over all algebraically closed coefficient fields in each characteristic. The N3/N4 counterexamples in aw/ay retain their specified transcendental fields; no claim that those cases occur over every fixed field is made. Rational higher-range injectivity, integral codimension at least three, and higher-range surjectivity remain undecided; the all-r extension is unregistered research.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bk' in unique and 'C.3bl' not in unique:
    TASKS = [
        (item, state + '; universal integral ordinary injectivity classified through codimension three in every positive characteristic',
         statements.replace('C.3a–bh', 'C.3a–bk'),
         scope.replace('The rational table and all higher-codimension remaining ranges are unchanged.',
                       'The rational divisor table is unchanged.')
         .replace('higher-degree positive-characteristic restriction beyond the proved intervals (injectivity for N>=2r+1 and surjectivity for N>=2r+2, r>=2)',
                  'higher-degree positive-characteristic restriction beyond the proved intervals (rational injectivity for N>=2r+1,r>=2; integral injectivity for 2r+1<=N<=3r-2,r>=4; surjectivity for N>=2r+2,r>=2)')
         + ' C.3bi retains the specified p=5,r=2,N=5 example and its independent integral K-theory/Adams proof. C.3bj constructs actual ordinary codimension-two classes of exact order p in the restriction kernel for every prime and every N>=5, already over Fpbar and every algebraically closed extension. C.3bk extends the actual-family/relative-Milnor construction to r2,N>=4; r3,N>=7; and r>=4,N>=3r-1, over every fixed algebraically closed field of positive characteristic. Its whole integral exceptional-image proof retains all Picard torsion. Together with aw/ay, this classifies universal integral ordinary restriction injectivity in codimensions two and three: it holds exactly for N<=r, quantifying over all algebraically closed coefficient fields in each characteristic. The earlier lower-dimensional aw/ay witnesses retain their specified transcendental fields; bk supplies a new Fpbar witness at r2,N4. Rational higher-range injectivity, integral injectivity for r>=4 and 2r+1<=N<=3r-2, and higher-range surjectivity remain undecided. The primitive whole-boundary auxiliary and its proposed stronger application are unregistered research.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bl' in unique:
    TASKS = [
        (item, state + '; entire universal integral ordinary injectivity classification in positive characteristic completed',
         statements.replace('C.3a–bh', 'C.3a–bl'),
         scope.replace('The rational table and all higher-codimension remaining ranges are unchanged.',
                       'The rational divisor table is unchanged.')
         .replace('higher-degree positive-characteristic restriction beyond the proved intervals (injectivity for N>=2r+1 and surjectivity for N>=2r+2, r>=2)',
                  'higher-degree positive-characteristic restriction beyond the proved intervals (rational injectivity for N>=2r+1,r>=2; surjectivity for N>=2r+2,r>=2)')
         + ' C.3bi retains the specified characteristic-five codimension-two example and its independent integral K-theory/Adams proof. C.3bj and C.3bk retain their independently proved all-prime codimension-two and product-cubic safe ranges. C.3bl constructs actual ordinary codimension-r restriction-kernel classes of exact order p for every prime, every r>=2, and every N>=2r, already over Fpbar and every algebraically closed extension. Its fully proved primitive relative-Milnor boundary lemma handles the entire integral Smith kernel: the selected cup kills the saturated ample image through a free primitive lattice, and the remaining canonical-curve-line products vanish by a lift-independent additive map from divisible Pic0. The all-r m0 geometry and actual fixed proper-curve families are proved. Together with aw in the lower interval and bh for divisors, universal integral ordinary restriction injectivity is now classified in every codimension r>=1: it holds exactly for N<=r, with universality over all algebraically closed coefficient fields in each positive characteristic. The earlier lower-interval witnesses retain their specified transcendental fields; no claim about every fixed field in that interval is made. These finite-order classes do not alter rational injectivity. The entire integral injectivity branch is removed from the remaining main gate; rational injectivity for r>=2,N>=2r+1 and higher surjectivity for r>=2,N>=2r+2 remain undecided.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bm' in unique:
    TASKS = [
        (item, state + '; algebraizable positive-characteristic threefold top gate reduced to its intrinsic exceptional-surface quotient',
         statements.replace('C.3a–bl', 'C.3a–bm'),
         scope + ' C.3bm now removes the ambient endpoint-lifting condition for every algebraizable normal strict-local threefold with regular puncture over every algebraically closed field of positive characteristic. The existing resolution construction is verified uniformly in the field; EL/EP realize every actual proper gamma-two perfect-family endpoint relation on the exceptional surface by an actual ordinary cycle relation on Z. An explicit negative intersection matrix removes all component-degree coordinates. The remaining gate in this branch is precisely S0(E)/(J_K(E)+(S0(E) intersect the exceptional-cycle image)); globally compatible perfect families across SNC intersections remain to be computed. No original whole-family extension is required. The characteristic-zero and other-dimensional rational top questions, and the higher restriction questions, remain as stated.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bn' in unique:
    TASKS = [
        (item, state + '; endpoint lifting proved in every dimension under the stated resolution hypotheses',
         statements.replace('C.3a–bm', 'C.3a–bn'),
         scope + ' C.3bn proves the actual proper-family endpoint comparison and intrinsic top quotient presentation in every dimension d+1>=2 under the displayed algebraizable regular projective modification and full-support exceptional Cartier divisor with ample conormal. The reduced exceptional support need not have normal crossings. Determinantal representatives and a regular threefold flag remove the ambient endpoint-lifting condition in this resolved scope. Existence of arbitrary-dimensional resolutions, characteristic-zero comparison, and computation of the intrinsic singular perfect-family quotient remain unresolved; no whole-family extension is asserted.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bo' in unique:
    TASKS = [
        (item, state + '; all exceptional-component Albanese coordinates removed by actual proper relations',
         statements.replace('C.3a–bn', 'C.3a–bo'),
         scope + ' C.3bo further proves that the weighted exceptional Picard-to-component-Albanese map is an isogeny and that its entire image is already in the actual proper-family subgroup J_K. Thus the algebraizable positive-characteristic threefold branch reduces to S00(E), the simultaneous component-degree-zero and component-Albanese-zero perfect subgroup, modulo the separate intersections with J_K and the exceptional-cycle image. Component Albanese kernels and globally compatible double/triple-stratum perfect families remain; no residual vanishing is asserted.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bp' in unique:
    TASKS = [
        (item, state + '; mixed intersection reduction proved in every supplied SNC resolved dimension',
         statements.replace('C.3a–bo', 'C.3a–bp'),
         scope + ' C.3bp extends the component degree and Albanese elimination to every d>=2 in the supplied SNC-resolution branch of C.3bn. Successive high smooth cuts give the mixed Picard polarizations in every characteristic; actual Poincare families multiplied by H^(d-2) give the required ordinary relations in the stated characteristic-p setting. The residual quotient is exactly S_d,00 with the separate family and exceptional denominator intersections. Non-SNC support, existence of higher-dimensional resolutions, component Albanese kernels and global proper-family compatibility remain outside this conclusion.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bq' in unique:
    TASKS = [
        (item, state,
         statements.replace('C.3a–bp', 'C.3a–bq'),
         scope + ' C.3bq proves that the component-restriction kernel is generated by actual proper perfect families when the rational dual H2 vanishes, or more generally every signed triple-point Pic0 period vanishes. Combined with zero rational Albanese kernels on all components, this gives ordinary top vanishing in the stated resolved threefold class. Nonzero periods are not proved to survive all families, and neither the period hypothesis nor component-kernel vanishing is asserted universally. This restricted case does not by itself change the main remaining gate.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3br' in unique:
    TASKS = [
        (item, state,
         statements.replace('C.3a–bq', 'C.3a–br'),
         scope + ' C.3br separately proves complete ordinary top vanishing for triple-free resolved SNC surfaces with surjective joint rational component-to-edge Picard restriction. Its actual graph families and finite divisor corrections remove every component degree-zero class, including Albanese kernels. Negative rational double curves force the joint restriction hypothesis. Positive-genus edges without that hypothesis and all triple-point extensions remain outside the theorem; these additional restricted cases do not alone change the universal main gate.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bs' in unique:
    TASKS = [
        (item, state,
         statements.replace('C.3a–br', 'C.3a–bs'),
         scope + ' C.3bs extends the preceding component-family theorem to triple strata when H² of the dual complex vanishes and the full joint rational Picard restriction is onto. Constant pullbacks split the edge-to-triple map on every parameter K-group, giving the actual coherent fixed-product lift. In negative exceptional threefold geometry, rational double curves supply Picard surjectivity, and all component degree-zero classes are removed. Nonzero H² and unsatisfied Picard surjectivity remain outside this restricted theorem; this does not alone reduce the universal main gate.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bt' in unique:
    TASKS = [
        (item, state + '; whole exceptional component-restriction kernel removed by actual marked proper families',
         statements.replace('C.3a–bs', 'C.3a–bt'),
         scope + ' C.3bt removes the entire component-restriction kernel in the general negative SNC exceptional-surface branch of C.3bm, with no dual-H2, triple-period or full Picard-restriction hypothesis. The component map is onto; finite marked-divisor interpolation gives actual integral K1 families on smooth curve products whose marked restrictions vanish on the whole proper parameter, and actual rational closed-union totalization removes all coherent edge/triple ambiguity. The exact remaining threefold gate is T_E/(phi(J_K intersect S00)+phi(Q intersect S00)), where T_E is the direct sum of the rational Albanese kernels of all smooth components and Q is the exceptional cycle image. This strictly replaces the earlier S00 gate by removing its entire component-map kernel. In particular vanishing holds whenever all component Albanese kernels vanish, independently of periods. The remaining component Albanese-kernel quotient is not computed; no characteristic-zero or higher-dimensional universal vanishing is asserted.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bu' in unique:
    TASKS = [
        (item, state,
         statements.replace('C.3a–bt', 'C.3a–bu'),
         scope + ' C.3bu strengthens C.3bn by lifting the entire prescribed proper-curve perfect-K0 family in top gamma degree over the original fixed local base. Finite perfect corrections lift integrally through regular surfaces; these correct the full p-power curve lift. For exceptional dimension at most two the whole rational K0 restriction is onto, and the exact fixed-product blow-up sequence gives K_-1(R times P)_Q=0. This auxiliary result constructs no missing globally compatible exceptional component family and does not reduce the remaining UK.7 quotient. It supplies neither affine-parameter compactification nor a theorem after the generally nonlocal scalar extension R tensor_k k(u).')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bv' in unique:
    TASKS = [
        (item, state, statements.replace('C.3a–bu', 'C.3a–bv'),
         scope + ' C.3bv proves integral rank-plus-determinant and square-zero augmentation for R times a fixed proper smooth curve over any local coefficient base. For normal R in characteristic p the entire K1 family on E times that curve lifts after inverting p, in every dimension of the supplied regular-modification scope. The fixed-base endpoint kernel is the residue-zero unit image; a polynomial corrects a literal weight-three endpoint under the additional henselian point hypothesis. It does not supply a family over a nonlocal symbolic extension or change UK.7.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
if 'C.3bw' in unique:
    TASKS = [
        (item, state, statements.replace('C.3a–bv', 'C.3a–bw'),
         scope + ' C.3bw proves the integral gamma-degree-three bound on a fixed proper parameter surface over the original local base. The polynomial (psi^2-1)(psi^2-2)(psi^2-4) kills its whole K0; in characteristic p its image on every exceptional K1 surface family lifts on the actual fixed product. Weight-three classes lift and have zero K0 restriction kernel. The supported boundary-node obstruction in compactifying a varying curve remains unproved, so this auxiliary mechanism does not change the main quotient or status.')
        if item == 'C.3' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
stop_record = None
for receipt in sorted((R/'logs').glob('scheduled_review_*.json')):
    candidate = json.loads(receipt.read_text())
    if candidate.get('stop_rule_reached'):
        stop_record = candidate
if stop_record is not None:
    TASKS = [
        (item, 'Record delivered; mathematical programme incomplete', statements,
         'Every task and Lead is recorded with its precise state; delivery is not mathematical completion.')
        if item == 'F.1' else
        (item, 'Literature record delivered with access limitations explicit', statements,
         'Opened primary sources and exact locators are distinguished from unsuccessful retrievals and unaudited originals.')
        if item == 'F.2' else (item, state, statements, scope)
        for item, state, statements, scope in TASKS
    ]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
lines=['INCOMPLETE','','| Item | Current outcome | Statement IDs | Scope / exact remaining gate |','|---|---|---|---|']
for row in TASKS:lines.append('| '+' | '.join(row)+' |')
lines += ['',f'Updated: {stamp}.','',
'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. We distinguish proofs of stated propositions, imported theorems with checked deductions, computations of finite examples, and unresolved tasks. The current outcome table governs the scope of the return. Earlier dated research notes preserve intermediate states and are superseded where a later certified statement says so. Delivery of this record is not completion of the mathematical programme.',
'','## Primary findings and qualifications','',
'The all-weight Frobenius realization problem has a direct unconditional solution: extract an i-th root, apply Honda–Tate in weight1, and use the i-fold product. This argument is already present in Milne (1994, Proposition2.6, proof). It gives m=1. The class group of the originally chosen CM field cannot obstruct a realization that is allowed to use a larger number field.',
'',
'The corrected Deuring rule is the crystalline cup-trace pairing transported from the uniquely reconstructed oriented supersingular curve. We prove independence, the exact unit-squareclass torsor, field-automorphism invariance, and Morita norm compatibility. The literal finite-field crystal domain has an explicit p=3 counterexample, and the maximal quadratic-order/descent equivalence has an explicit F7 counterexample. The ramified F9 base change also refutes the universal Picard assertion.',
'',
'The cycle analysis separates algebraic-equivalence counterexamples from unresolved assertions about algebraic classes in cohomology. An incidence blow-up construction shifts the quintic Griffiths group and gives failure of universal A in every nontrivial degree range. This is not evidence for failure of the distinct higher injectivity statement. Modern integral curve-class counterexamples on very general principally polarized abelian varieties are taken from the opened 2026 version of Engel–de Gaay Fortman–Schreieder, with their preprint status explicit.',
'',
'The complex Albanese-family converse is refuted even rationally by E.3u. A specified degree14 hypersurface in split Q6 carries a two-plane difference whose Betti class is zero but whose Lawson s-image is nonzero. Its product with an elliptic point gives a whole zero-cylinder family detected by full morphic Abel–Jacobi. This proves that the generated Albanese relation is strictly smaller than the finite Walker kernel; the previously isolated generation gate is false. The forward theorem in every characteristic and the exact fixed-variety/support statements remain valid.',
'','## Root computations','',
'All scientific programs and their exact outputs are retained. The root programs use exact integer/Fraction/SymPy or finite-field arithmetic; no floating-point inference is used.',
'',
'| Program | Inputs and scope | Output |','|---|---|---|',
'| code/check_quaternion_crystal.py | p=3 order basis, quaternion multiplication and trace discriminant, F=4J sigma; local unit squareclasses | code/check_quaternion_crystal_output.json |',
'| code/check_supersingular.py | Complete general-Weierstrass orbit enumeration at2,3; odd primes5,7,11,13,17,19,23,29,31,37,43; F7 counterexample; reduced forms/class numbers | code/check_supersingular_output.json |',
'| code/check_small_automorphisms.py | Automorphisms of the exceptional supersingular curves over F4,F9 | code/check_small_automorphisms_output.json |',
'| code/check_local_cone.py | Fermat quartic points, regular hyperplane, three projective Jacobian certificates, blow-up chart | logs/local_cone_certificate.json |',
'',
'All programs and outputs are indexed in code/PROGRAM_INDEX.md and code/program_files_output.json, with byte-identical contributed copies consolidated under code/retained_programs. Missing timings were recorded in one scoped rerun in code/computation_timing_output.json; full stdout is retained. Exact run times are embedded in the JSON outputs. The general all-p formula and proofs do not rest on extrapolation from this finite list. The general crystalline reconstruction algorithm is specified mathematically and has not been run on arbitrary input orders.',
'','## Check-event metadata normalization','',
'The aggregate CHECK_EVENTS.tsv now uses the requested check-type categories and expands verified agent identities. Original owner labels and outcomes remain in logs/check_event_normalization.tsv; administrative requests, retrieval-only entries and duplicate receipts remain in logs/check_event_auxiliary_provenance.tsv and are excluded from mathematical check counts. Explicit row-level overrides, their independent audit and the fail-closed classification program are retained. No earlier archive or owner event file was rewritten. This changes metadata and counts only; it creates no independent re-proof and no movement of a mathematical gate.',
'','## Root readings and corrections','',
'We read the attached prompt, the relevant sweep-3 and SA05 arguments, and the transcriptions at15:16–22,34–78. We opened Deuring1941, Voight2021 Chapters14/30/42, Waterhouse1969, Yu2026, and the primary sources identified in the collaborators’ records. R1,R2,R4 and LeadsA1–A4 are checked at the paragraphs that use them. Classification solely by Brauer class omits degree: the rank-one categories of M2(Q) and M3(Q) have nonisomorphic endomorphism algebras. The sign at infinity is separated into an H¹ class fixed by positivity and an H⁰ automorphism group left equal to {±1}.',
'',
'The phrase at15:70 has no supplied completion, and the subsequently retrieved official original scan itself stops after égal. The adjacent scans and the next handwritten page supply no continuation. Michel Hua’s project likewise writes “page s’arrête sur une question” and quotes the same unfinished words (15.modern.tex, surrounding the discussion of archive page69). We credit that witness only for confirming the truncation; it supplies no missing mathematical assertion. We independently checked the exceptional automorphism orders and the reversed 4/6 association in the transcription.',
'',
'A preliminary orientation formula using the conjugate action on M/FM was corrected before the checkpoint: with D(f)=(f-dual)*, the raw action is the tangent-space orientation. The earlier draft’s statement that an unimplemented all-p algorithm leaves the explicit rule unproved was removed: the mathematical formula and terminating reconstruction are proved, while execution scope is separately recorded. The former unresolved A.5 base-change paragraph is superseded by the explicit F9 counterexample.',
'','## Typesetting verification','']
layout=R/'logs/latest_layout.json'
if layout.exists():
    d=json.loads(layout.read_text());lines += [f"Latest completed build: {d['utc']}; overfull boxes: {d['overfull_count']}, over2pt: {d['overfull_gt_2pt']}, maximum: {d['maximum_overfull_pt']}pt; missing characters: {d['missing_characters']}.",'','Visual inspection and before/after layout counts are recorded in logs/QA_RECORD.md when performed.']
else:lines += ['The first full LuaLaTeX build and visual inspection are in progress. No unverified PDF is certified as publication-ready.']
lines += ['','## Contributor proof, computation, source and approach records','',
'The following records preserve the exact limitations and failed approaches. Earlier retrieval failures remain documented even when a later source was obtained; the later dated successful opening supersedes the initial unavailable status. Raw third-party PDFs and text extractions are research inputs and are excluded from deliverable ZIPs.','']
review_paths = ['agents/frobenius/REPORT.md','agents/frobenius/A_review.md']
review_paths += [str(p.relative_to(R)) for p in sorted((R/'agents/frobenius').glob('*REVIEW.md'))]
review_paths += [str(p.relative_to(R)) for p in sorted((R/'agents/frobenius').glob('*REPORT.md'))]
review_paths += [str(p.relative_to(R)) for p in sorted((R/'notes').glob('ROOT*.md'))]
review_paths += [str(p.relative_to(R)) for p in sorted((R/'agents/cycles').glob('*REPORT.md'))]
review_paths += [str(p.relative_to(R)) for p in sorted((R/'agents/cycles').glob('*REVIEW.md'))]
review_paths += [str(p.relative_to(R)) for p in sorted((R/'agents/real_weil').glob('*REVIEW.md'))]
review_paths += [str(p.relative_to(R)) for p in sorted((R/'agents/real_weil').glob('*SOURCE_AUDIT.md'))]
review_paths += [str(p.relative_to(R)) for p in sorted((R/'agents').glob('*/*RESEARCH.md'))]
review_paths += ['agents/cycles/STATUS.md','agents/cycles/notes/source_record.md','agents/cycles/notes/c4_source_scope_after_checkpoint13.md','agents/cycles/notes/quintic_cover_method_limits.md','agents/cycles/notes/generation_gate_0650.md','agents/real_weil/REPORT.md','agents/real_weil/SOURCE_AUDIT.md','agents/real_weil/TOP_QUOTIENT_RESEARCH.md','agents/real_weil/PATEL_RAVINDRA_TORSION_SCOPE.md']
if stop_record is not None:
    lines += ['## Scheduled stopping decision', '',
              f"Research stopped at scheduled review {stop_record['review']} ({stop_record['actual_utc']}) after {stop_record['dry_streak']} consecutive scheduled reviews without qualifying main-gate movement. The user's stopping rule applies. The mathematical work remains INCOMPLETE; subsequent assembly, verification and saving are administrative and do not count as movement.", '']
    review_paths += [stop_record['assessment']]
for rel in dict.fromkeys(review_paths):
    p=R/rel
    if p.exists():lines += ['---','',f'### Record: {rel}','',p.read_text(),'']
(R/'RESEARCH_SA06_report.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'statements':len(rows),'check_events':len(events),'task_and_lead_rows':len(TASKS),'updated':stamp}))
