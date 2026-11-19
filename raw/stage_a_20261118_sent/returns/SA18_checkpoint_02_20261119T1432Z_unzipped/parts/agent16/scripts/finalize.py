"""Serialize the individually authored final review and its audit tables.

No verdict is inferred by this script. The dictionaries below are the agent's
manual mathematical judgements; the loops only serialize and check coverage.
"""
from pathlib import Path
import csv, json, runpy, collections

O=Path(__file__).resolve().parents[1]
S=O/'scripts'
runpy.run_path(str(S/'build_stage1.py'), run_name='__main__')
d=runpy.run_path(str(S/'build_dossier.py'))
I,C,R=d['I'],d['C'],d['R']
runpy.run_path(str(S/'polish_claims.py'))['polish'](C,I,R)
DATE='2026-11-19'
WHO='GPT-6 Astra Pro / inherited effort / agent16'
F='SA18_texts/pro/MPL_16+47+54+44_transcription.tex'

def writejson(name,obj):
    (O/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def tsv(name,fields,rows):
    with (O/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def rr(keys):
    return [dict(key=k,url=R[k]['url'],locator=R[k]['locator'],verification=R[k]['verification']) for k in keys]

R['SGA3XV']=dict(key='SGA3XV',title='SGA3 Exposé XV: Compléments sur les sous-tores',author='Michel Raynaud',year='1970; consulted2008 re-edition',url='https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo15.pdf',locator='Proposition6.2(iii)(b), originalpp427–428/PDFp41; Remark6.2.1 originalp424/PDFp40',verification='verified: primary re-edition opened and matching paragraphs read; not the original galley',doi='',date_note='Consulted version December2008; original SGA3 publication1970.')
R['SGA3XVII']=dict(key='SGA3XVII',title='SGA3 Exposé XVII: Groupes algébriques unipotents',author='Michel Raynaud',year='1970; consulted2008 re-edition',url='https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo17.pdf',locator='AppendixIII C.1–C.3, originalpp627–628/PDFpp46–47',verification='verified: primary re-edition opened and specified paragraphs read',doi='',date_note='Consulted version18November2008; original SGA3 publication1970.')
R['Stacks09T1']=dict(key='Stacks09T1',title='The coherator for Noetherian schemes',author='The Stacks Project Authors',year='2026 consulted',url='https://stacks.math.columbia.edu/tag/09T1',locator='Lemma36.8.1: injective quasi-coherent sheaves are flasque; not a general all-sheaf injectivity theorem',verification='verified: statement and proof opened/read',doi='',date_note='')
R['Stacks09TH']=dict(key='Stacks09TH',title='The coherator for Noetherian spaces',author='The Stacks Project Authors',year='2026 consulted',url='https://stacks.math.columbia.edu/tag/09TH',locator='Lemma75.12.1, affine noetherian injectives via Matlis;75.12.3 flat qcqs pushforward preserves injectives',verification='verified: statements and proofs opened/read',doi='',date_note='')
R['Garrett1997']=dict(key='Garrett1997',title='Buildings and Classical Groups',author='Paul B. Garrett',year='1997',url='https://www.ndl.ethernet.edu.et/bitstream/123456789/9667/1/131.pdf',locator='Search-located discussion of locally finite hyperplane arrangements and adjacent chambers; exact section not verified',verification='UNVERIFIED: PDF open timed out; search metadata only',doi='',date_note='Metadata from search; no theorem is attributed on this basis.')
R['HHLLMM2025']['locator']='§3.2 liftability alternatives;§4.1 and Theorem4.5; Theorem5.5 with Z[1/(2g+d+1)!]; Theorem7.3 additionally invertsν(θ), where degθ=ν(θ)^2'
I[21]['statement']='Off-topic reused S.G.A.D. errata: several references can now be matched to SGA3 XV and XVII. The Cartan-subgroup replacement matches XV proof6.2(iii)(b); the references to XVII AppendixIII1,2,3 match C.1,C.2,C.3. This is a partial provenance match, not a complete collation of the old galley.'
I[21]['reconstruction']='The consulted2008 re-edition has C_eta a Cartan subgroup of H_eta in the first sentence, whereas the manuscript replacement says G_eta. Their common surrounding argument is identifiable; that local variation is retained. No original galley pagination is invented.'
I[21]['check_reason']='Read the supplied errata and compared the actual primary re-edition paragraphs. Bibliographic identification is stronger than the earlier note, while exact typography and every old page number remain unresolved.'
I[86]['his_words']='“est nul sur H^j, j≠k” (the transcription marks j|i as uncertain).'
for n in [23,43,64,85]:
    I[n]['his_words']='No author quotation: this indexed entry is the earlier run’s bibliography, not a manuscript statement.'
for c in C:
    n=int(c['id'].rsplit('-',1)[1])-16000
    # Class A is reserved for an exact match in Grothendieck's own opened work.
    # A later exposition by Kleiman or Stacks is class B, irrespective of influence.
    if n in [17,31,32,34,35,36,37,41,102,117]:c['class']='B'
    if n==21:
        c.update(his_statement=I[21]['his_words'],statement=I[21]['statement'],status_on_pages='Editorial correction list, with old galley pagination.',computation='Compared c16:26 lines1066–1105 against SGA3 XV proof6.2(iii)(b), Remark6.2.1, and XVII AppendixIII C.1–C.3. No new group-scheme theorem is inferred.',**{'class':'C'},fate='Partial exact identification in published SGA3; several references and the Cartan paragraph match. The complete galley collation remains unperformed.',fate_date='SGA3 publication1970; consulted2008 re-edition; checked2026-11-19',present_status='Provenance partly resolved. Preserve the G_eta/H_eta variant and remaining old page-number uncertainty.',refs=rr(['SGA3XV','SGA3XVII']),confidence='medium')
    if n==86:c['his_statement']=I[86]['his_words']
    if n>=100:c['his_statement']=I[n]['his_words']
    if n==10:c['refs']=rr(['Matlis1958','Stacks09T1','Stacks09TH'])
    if n==79:
        c['search_group']='chambers'
        c['fate']='The elementary arrangement assertion is independently proved. Targeted searches located a later textbook treatment, but its PDF timed out; no exact source attribution for this reused leaf is established.'
        c['refs']=rr(['Garrett1997'])
    if n==116:c['search_group']='rootcounter'
    if n in [38,39]:c['search_group']='jannsen'
    if n==39:c['computation']+=' Jannsen Corollary1 assumes the Künneth components of the diagonal are algebraic; that premise is not omitted here.'
    if n==62:c['search_group']='fouriersign'
    c['present_status']='As of 2026-11-19: '+c['present_status']
    c['refs']=rr([r['key'] for r in c['refs']])
writejson('SA18_items.json',[I[k] for k in sorted(I)])
writejson('SA18_claims.json',C)
writejson('reference_audit.json',R)

CM={int(c['id'].rsplit('-',1)[1])-16000:c for c in C}
P=[]
def problem(n,title,ns,states,today,art,why,worth,keys):
    occ=[]
    for j in ns:
        x=I[j]
        occ.append(dict(item=x['id'],claim=CM[j]['id'] if j in CM else '',cote=x['cote'],scans=x['scans'],lines=x['lines']))
    P.append(dict(id=f'MP-SA18-{16000+n}',title=title,occurrences=occ,as_he_states=states,plausible_today=today,state_of_art=art,why_open=why,worth=worth,refs=rr(keys)))

problem(1,'An integral algebra of normalized Lefschetz operators',[1,2,26,27,29,102,120],
 'The author seeks relations for L and Λ and polynomial expressions for the projectors, using an exterior model over Z and later prescribed grading projectors.',
 'The unit-step string algebra is the product of integral matrix algebras. A separate question is the precise integral order generated by exterior multiplication and raw symplectic contraction, with its factorial divisibility.',
 'Kleiman1968 supplies the normalized rational correspondence formalism. Akhtar–Joshua uses a weighted rational sl2 algebra. Neither opened text identifies the two integral orders. The exterior top-power obstruction and matrix algebra were computed here.',
 'The source leaves formula(6.5) blank and changes normalization without an explicit integral comparison. No historical reason beyond those visible gaps is asserted.',
 'Worth a focused run: an integral change-of-basis and denominator theorem would resolve a precise ambiguity with small exact calculations.',
 ['Kleiman1968','AkhtarJoshua','BF2023'])
problem(2,'Can L alone recover the grading?',[3,29],
 'The page asks whether the homomorphism can be defined from L without the π_i and answers “Non”, already for n=1.',
 'No in general. Retaining all π_i and the two-sided Lefschetz inverse conditions gives the distinct positive universal statement.',
 'Independent conjugation by1+tL proves nonuniqueness. Later normalized Lefschetz expositions do not erase the grading hypothesis.',
 'It is not left open: the negative answer is on the page.',
 'Useful as an editorial clarification; it is already settled and does not merit a new broad research programme.',
 ['Kleiman1968','AkhtarJoshua'])
problem(3,'The deferred primitive-projector implication',[102,31,86],
 'The abstract equivalence leaves an implication to prove, and a later induction asserts off-degree vanishing of ξ^(n−k)T_k.',
 'A split-string proof gives the abstract equivalence; in the later induction both a source and a target cut are needed: π_k=u_kT_kL^(n−k)T_k.',
 'The normalized formalism is published in Kleiman1968. The P² counterexample and target-cut repair are this review’s reconstruction, not a source emendation.',
 'The page itself postpones one implication; the later induction contains a specific omitted cut. No biographical explanation is inferred.',
 'Worth a short proof-editing task because it gives a complete corrected argument with a transparent counterexample.',
 ['Kleiman1968'])
problem(4,'Algebraicity of the Lefschetz inverse',[24,30,34,35,40,41],
 'Draft C asks for algebraic correspondences inducing the inverse Lefschetz operators; the letters discuss polarization and realization dependence.',
 'Published standard conjecture B for smooth projective varieties and the specified Weil cohomology. Polarization independence follows under the published rationality criterion; realization independence is a separate issue.',
 'Deligne1980 gives cohomological hard Lefschetz; Katz–Messing gives finite-field Künneth projectors. Neither proves B. ACLS2025 proves additional fibration cases under Ngô/support hypotheses and applications including LSV/OG10. The general assertion remains unresolved.',
 'The source retracts an overstrong assertion; contemporary sources describe a standard conjecture. No claim is made about a personal reason for abandoning it.',
 'High mathematical interest, but a few-hour task should audit one exact implication or special case, not promise to solve B.',
 ['Groth1969','Kleiman1968','Deligne1980','KatzMessing1974','ACLS2025'])
problem(5,'Hyperplane induction and critical-degree cycle conditions',[32,33],
 'Assuming the lower-dimensional conjecture, the mixed correspondence Λ_Xφ_* and weak algebraic-cycle conditions should recover C(X).',
 'For a smooth hyperplane section, retain the polarization, critical degree and lower-dimensional B(Y) hypothesis; first distinguish cycle codimension from cohomological degree in A′ and A″.',
 'Kleiman’s published A/B implications and the verified string identities support the qualified criterion. The ambiguous A′/A″ draft is not uniquely identified by those references.',
 'The manuscript has degree and letter ambiguities; no external explanation for nonpublication of the exact formulation was found.',
 'Worth a narrowly scoped reconstruction because the endpoint maps and degree audit can be completed in one run.',
 ['Groth1969','Kleiman1968'])
problem(6,'Positive trace, algebraic splittings and semisimplicity',[36,37,38,39],
 'C(X) together with the Hodge index relation should imply a semisimple correspondence algebra and algebraic left/right inverses.',
 'For a finite-dimensional rational algebra with the specified positive trace involution, the radical is zero and the adjoint argument supplies splittings. General homological semisimplicity remains conditional.',
 'Kleiman3.11–3.14 proves the conditional statements. Jannsen1992 proves numerical-motive semisimplicity and a nilpotent-kernel statement; it does not replace positivity or prove B.',
 'The source explicitly says the index relation seems needed; that is the documented obstruction.',
 'Worth a concise dependency diagram and proof audit; it prevents a substantial false modern-resolution claim.',
 ['Kleiman1968','Jannsen1992'])
problem(7,'Brauer and discriminant pairings',[4,5,11,12,105,106],
 'Identify the local intersection discriminant pairing with the cohomological pairing on the local Néron–Severi group.',
 'Under the complete normal equicharacteristic surface hypotheses of BrauerIII§8.4, construct the exact comparison, with its boundary map and sign conventions.',
 'Mumford1961 proves negative definiteness. BrauerIII§8.4 identifies the groups under its hypotheses, but Remark8.5 expressly leaves this pairing verification undone. The searches located no exact later proof matching the conventions.',
 'The published author explicitly reports not having done the verification. This is a retained proof obligation, not a claim that all modern local duality is open.',
 'Very suitable for a focused run: explicit local-duality maps can settle the comparison or isolate the sign.',
 ['BrauerIII','Mumford1961','Stacks03PK'])
problem(8,'The unit-fibre compatibility in Fourier inversion',[46,47,49,50,51,52],
 'The constructed comparison Rp_*P→e_*τ[−g] must become the required isomorphism after derived pullback to the unit; the vanishing proof is also admitted.',
 'For dual abelian schemes with normalized Poincaré bundle in the appropriate perfect category, establish the canonical kernel theorem, including τ=detLie and the actual comparison morphism.',
 'Mukai1981 establishes the field inversion theorem. Laumon1996 Theorem1.2.4 and Lemma1.2.5 give the relative determinant-line formulation. The local Koszul computation alone does not check the chosen map.',
 'The source explicitly marks the compatibility as to verify and cancels its vanishing proof. The later theorem is established.',
 'Worth a historical proof completion, not a claim of new Fourier inversion.',
 ['Mukai1981','Laumon1996','Stacks0621','Stacks0DJT'])
problem(9,'Proper-support and three-kernel Fourier identities',[45,110],
 'The margin suggests flat-group, proper-support and three-kernel versions of the convolution/tensor identity.',
 'Specify kernels, derived categories, Tor conditions and properness of the relevant support projections; then use convolution of kernels and derived base change.',
 'Laumon’s general Fourier constructions and Stacks Fourier–Mukai/base-change criteria supply qualified mechanisms. Proper support by itself does not ensure every perfect-category preservation statement.',
 'The source gives a margin programme, not a full theorem; no later exact match to all its unspecified categories was found.',
 'Worth a short theorem-design task with one explicit support hypothesis and counterexamples to omitted hypotheses.',
 ['Laumon1996','Stacks0FYP','Stacks0DJT','Stacks0G99'])
problem(10,'Integral Fourier duality and torsion',[54,55,57,58,111],
 'The source asks whether its cycle formulas remain true integrally, with torsion retained.',
 'Separate existence of an integral lift of the Fourier kernel, integral identities, and equality modulo torsion; keep a genuine symmetric ample principal line bundle when invoking the principally polarized equivalences.',
 'Beckmann–deGaayFortman2023 Theorem3.8 relates the integral transform to minimal-cycle conditions and Question3.9 retains a general open case. HHLLMM2025 works over Z[1/(2g+d+1)!], with smooth quasi-projective base and lifting conditions; its sl2 refinement also inverts the polarization degree. This is not full integrality.',
 'The factorial denominators and torsion are real obstructions. The source also has an independent Chern coefficient mistake, explicitly corrected here.',
 'High interest: one few-hour run can compare a selected dimension or polarization and quantify exactly which primes remain.',
 ['Mukai1981','BF2023','HHLLMM2025'])
problem(11,'Relative Todd and determinant factors',[47,48,59,60,61,63],
 'The relative product-exchange and duality formulas involve τ, Todd classes and an undefined check operation; one display has an incomplete factor.',
 'Fix the Poincaré and duality conventions and retain T_A T_B ch(ω_A) until the precise base hypotheses justify cancellation.',
 'Laumon supplies derived inversion/duality. Moonen2026§2.4 corrects a bundle-duality error and§2.7 proves the qualified Todd statement; stronger Chern vanishing has extra assumptions. The first preprint is July2024.',
 'The draft mixes K0, derived and rational Chow formulas. No further historical motive for stopping is inferred.',
 'Worth a small convention table, especially because a recent correction makes broad unqualified summaries unreliable.',
 ['Laumon1996','Moonen2026','HHLLMM2025'])
problem(12,'Duality of the universal vector extensions',[65,66],
 'Identify the tangent sequence of the universal vector extension with de Rham cohomology and verify the degree-one pairing before taking exterior powers.',
 'Use the canonical perfect de Rham pairing of dual abelian schemes under the hypotheses of the chosen universal-extension comparison theorem.',
 'Coleman1998 Theorems1.1 and2.2 compare the constructions for a reduced base or one flat over Z. This covers the characteristic-zero setting on the page; the opened article does not justify an arbitrary-base generalization.',
 'The source explicitly leaves the degree-one verification for later. The qualified modern result is established.',
 'A useful short task would track the precise map and repair the A/B differential-sheaf typo.',
 ['Coleman1998','Oda1969'])
problem(13,'Recover H¹ de Rham from A[p]',[67,68,69],
 'Does the finite group scheme A[p] determine the Hodge extension with its restricted p-operation?',
 'Over a perfect field of characteristic p, recover H¹_dR(A), its F,V operators and Hodge subspace from the Dieudonné module of A[p].',
 'Oda1969 Corollary5.11 proves the functorial comparison and identifies VM with the Hodge subspace; the thesis dates to June1967. SGA3VII_B4.4.1 supplies the restricted-Lie/height-one comparison.',
 'The page asks the question; Oda supplies the later solution. The source does not ask about an arbitrary base or only geometric p-torsion points.',
 'Historical and expository value is high; a small run can write the exact dictionary without proposing a new theorem.',
 ['Oda1969','SGA3VIIB','Coleman1998'])
problem(14,'Intermediate algebraic Jacobians in every codimension',[72,75,113,114],
 'Construct J^i or P^i as an abelian quotient of cycle families by an Albanese-type relation that the author says is not securely defined; obtain duality and Lefschetz properties.',
 'First specify the equivalence relation and universal regular property. Modern algebraic representatives are established in selected codimensions, not in the source’s full undefined generality.',
 'Kahn2021 corrects the codimension2 existence proof. ACMV2023 develops relative regular homomorphisms. Ottem–Suzuki shows that the codimension3 Abel–Jacobi map need not be universal. ACMV’s2026 torsor refinement presupposes a regular homomorphism.',
 'The unknown relation and lack of boundedness are explicit in the letters. No claim about unseen project context is used.',
 'High interest but too broad for one short run; choose one codimension and one exact universal property.',
 ['PicardVI1962','MumfordLetter1964','Kahn2021','ACMV2023','OttemSuzuki2020','ACMVtwist2026'])
problem(15,'Uniform dimension bounds and Tate-module injection',[73,74],
 'Bound all abelian quotients from cycle families by half the relevant odd Betti number, first through a Tate-module subquotient and then hopefully an injection.',
 'In codimensions1,2,d, use a surjective regular map and a miniversal cycle of degree r. For ℓ≠p with ℓ∤r, the precise torsion-free cohomology target supports the verified injection.',
 'Kahn’s boundedness proof resolves codimension2. ACMV2023 Proposition8.2 states the exact codimension, ℓ and miniversal-degree qualifications. It is not an all-codimension, all-prime theorem.',
 'The source needs a uniform bound over all families, not a bound on one chosen Abel–Jacobi image.',
 'Worth a focused prime-by-prime comparison to isolate whether the exceptional primes are intrinsic or a proof artefact.',
 ['Kahn2021','ACMV2023','MumfordLetter1964'])
problem(16,'Positivity of the middle-cycle polarization',[72,77],
 'A symmetric divisor correspondence on the intermediate Jacobian should come from an ample class after the specified sign and primitive correction; the author says he cannot prove positivity.',
 'Separate descent, symmetry, nondegenerate isogeny and ampleness. Formulate positivity only for a precisely defined algebraic representative and cycle-induced class.',
 'ACMV2025 Theorem12.12 constructs qualified symmetric isogenies in the threefold setting. Section13 derives positivity under lifting and other stated hypotheses; it does not establish the draft’s general characteristic-p assertion.',
 'The source explicitly singles out positivity after several other unproved steps. A negative ample class is only a logical test that symmetry/nondegeneracy alone do not imply ampleness.',
 'High value: a small run can audit exactly which cycle-origin hypotheses distinguish the class from an arbitrary symmetric isogeny.',
 ['ACMV2025','PicardVI1962','MumfordLetter1964'])
problem(17,'Pencil intersections and Néron–Tate heights',[76],
 'Compare the height pairing on a generic pencil member with intersection upstairs, assuming the inserted geometrically integral fibre condition.',
 'Fix the cycle quotient, model, height normalization, vertical corrections, exponent and sign before asking for an equality.',
 'The8August1964 Serre letter gives the surface-fibration comparison. Künnemann2001 concerns higher heights on abelian varieties over number fields; it is a partial comparator, not a proof of this unspecified pencil formula.',
 'Several symbols and hypotheses are incomplete on the page. No exact later theorem matching the full display was found.',
 'Worth one short run on the surface/divisor case; the general higher-cycle version requires a separate formulation.',
 ['SerreLetter1964','Kunnemann2001'])
problem(18,'Numerical equivalence versus τ-equivalence',[78],
 'The theorem list asserts numerical equivalence equals τ-equivalence, without defining τ locally.',
 'If τ means algebraic equivalence after multiplying by a nonzero integer, the all-codimension statement is false; retain the valid divisor case as a separate statement.',
 'Clemens1983 supplies nonzero rational Griffiths groups, contradicting this higher-codimension interpretation. Matsusaka1957 metadata was located, but its full theorem text was inaccessible and is not used as verified proof here.',
 'The local notation is missing. The dossier distinguishes ambiguity from a proved counterexample to one explicit interpretation.',
 'Worth a brief notation/provenance task before drawing historical conclusions.',
 ['Clemens1983','Matsusaka1957'])
problem(19,'Infinite orbits and unbounded cyclic spans',[80,81,82,83,84],
 'For the operator built from the alternating four-form and inverse bivector, the author asks about infinite orbits, dimension4 versus6, and unbounded dimension of the generated span.',
 'Over a specified infinite field and with a fixed tensor normalization, distinguish infinite orbit from cyclic rank. The reconstructed dimension6 witness and perturbation family establish qualified existence and unboundedness.',
 'No exact later development of this algebra model was located in the recorded searches. Kleiman and Akhtar–Joshua are contextual operator-algebra comparators, not solutions of this precise problem.',
 'The page leaves the operator scaling and4-versus6 minimum uncertain. No geometric-realization condition is supplied.',
 'A good short research task is to settle the dimension4 boundary with exact symbolic algebra under one explicit normalization.',
 ['Kleiman1968','AkhtarJoshua'])
problem(20,'Normalization of ξ in the four-form model',[119,82],
 'A convenient choice of ξ is said to give any desired nondegenerate φ up to scalar, while Q(ξ,ξ)=1 is also required.',
 'The inverse image of φ under nondegenerate Q must be nonisotropic, and the necessary norm must be a square in the base field to normalize by scalar. Isotropic functionals and square-class obstructions are excluded.',
 'The finite-dimensional linear-algebra correction is proved directly; no exact later publication of this formulation was located. The opened Lefschetz comparators do not remove these field restrictions.',
 'The source’s “up to scalar” qualifier does not itself justify the normalization. This is a mathematical restriction, not an ink decision.',
 'Worth combining with the orbit task because the normalization changes the quantifiers of every proposed example.',
 ['Kleiman1968','AkhtarJoshua'])
problem(21,'Generic flattening and the marginal ideal criterion',[70,118],
 'A reused PropositionA gives a universal flattening locus after shrinking; a strengthened freeness corollary is cancelled, and an ideal-adic criterion appears in a compressed margin.',
 'Separate generic freeness from representability of a flattening functor. State finite presentation, the chosen affine cover, completeness, separation and Tor hypotheses explicitly.',
 'Stacks051R verifies generic freeness. Stacks05P7 is a definition only; the opened page was not mistaken for the full flattening theorem. Completion lemmas00MB/00MC require their noetherian/Jacobson conditions.',
 'The marginal symbols and missing antecedents prevent a unique exact criterion. The source itself cancels part of the claimed strengthening.',
 'A focused source-identification task is worthwhile; proving an unspecified criterion is not.',
 ['Stacks051R','Stacks05P7','Stacks00MB','Stacks00MC'])
problem(22,'Crystallographic integrality from the cancelled root axioms',[115,116],
 'The cancelled paragraph claims primitive roots and integral coroots follow from reducedness, lattice generation and reflection stability.',
 'Add an explicit integrality or suitable primitivity condition. Reflection uniqueness holds independently; a modern root datum also requires a perfect integral pairing.',
 'Conrad2014 Definition1.3.3 imposes crystallographic integrality separately and proves uniqueness of the reflection. The exact eight-root counterexample here satisfies the cancelled axioms and has a2/3 coroot pairing.',
 'The whole paragraph is cancelled on the manuscript. No explanation of the cancellation is asserted beyond the counterexample found in this review.',
 'Settled as written; useful for a short corrected-axiom note and not an open root-system problem.',
 ['Conrad2014','Milne2018'])

writejson('SA18_problems.json',P)

# All entries below are mathematical reading alarms or second-pass resolutions.
# The line numbers are absolute in F, not a reset page-local numbering.
READ=[]
def rd(c,s,line,reading,alternative,evidence,weight='high',confidence='mathematical diagnosis high; ink undecided in this run'):
    READ.append(dict(cote=c,scan=s,line=f'{F}:{line}',reading=reading,alternative=alternative,evidence=evidence,weight=weight,confidence=confidence))
rd(16,4,'75,85','E^(ν) as the object being graded','E* is mathematically expected','Second-pass001–018_changes line26 confirms the first E^(ν) in ink; line118 leaves the later instance unresolved. Do not silently repair.')
rd(16,4,'87','ν−ν′ | ν+ν′','ν+ν′','Matrix-diagonal multiplication adds degrees. Second-pass changes line119 retains the sign doubt.')
rd(16,4,'109','π_(j+ν)u with sum indexed i/α','Consistent i or j through the identity','The homogeneous relation requires one fixed source index. Cancellation and index ambiguity remain.')
rd(16,5,'146–148','Σ_(α<i)π_i and Σ_(α>2n−i)π_i','π_α in each sum','Tail projectors must sum the varying index; otherwise the asserted equalities fail.')
rd(16,6,'176','u_(2n−i) | π_(2n−i)','A projector-characterization phrase may be intended','The preceding paragraph concerns uniqueness of the endpoint idempotent; this is a contextual suggestion only.','medium')
rd(16,8,'236–242','sur-anneau | sous-anneau','sur-anneau','Second pass001–018_changes line36 resolves sur-anneau; E⊂F agrees. No live ambiguity remains from this run.','medium','resolved by supplied second pass, not newly inspected')
rd(16,10,'308–314','(6.5) brace and dots','No formula may be inserted as transcription','The blank is confirmed in second-pass changes line71. The normalized operator is a reconstruction.')
rd(16,11,'350–365','ascendante | descendante','ascendante','Second-pass changes line43 confirms ascendante; induction expands the known extreme degrees.','medium','resolved by supplied second pass')
rd(16,13,'444','Possible cancellation of first L^(α−1)','Keep first L^(α−1) live','Second-pass changes lines74–77 explicitly confirms the live L. Removing it breaks degree and string action.')
rd(16,13,'453','i≤n−1 | i<n−1','i≤n−1','Second-pass changes line45 confirms ≤.','medium','resolved by supplied second pass')
rd(16,13,'458','Λ∈E^(2)','Λ∈E^(−2) mathematically','Second-pass changes line46 confirms positive2 in ink; this is an author slip, not an inferred corrected reading.')
rd(16,13,'469','α | i ≤n−1','i≤n−1 in the dual-degree formula','The bound concerns the paired lower degree, while α indexes string position.')
rd(16,14,'504–525','Exterior model over Z satisfies hard Lefschetz','Over Q, or with a different integral lattice','Second-pass changes line70 confirms the literal Z model. ξ^n=n!vol refutes the unqualified integral statement.')
rd(16,14,'525','Reference(6.5) | (6.15)','Retain both; do not fill blank(6.5)','Second-pass changes line49 adds6.15 as an ink alternative; different lowerings cannot be identified from that reference alone.')
rd(16,15,'535','0≤α,β≤2n−i','0≤α,β≤n−i mathematically','Second-pass changes lines74–75 confirms2n−i; longer indices give zero vectors, not matrix units.')
rd(16,15,'582–590','comme au n°6','comme au n°1','Second-pass changes line53 resolves1, affecting the prescribed-grading context.','high','resolved by supplied second pass')
rd(16,16,'603–611','Cancelled phrase ends par les π_i','Cancelled phrase ends par(1.3)','Second-pass changes line58 gives the controlling reading. The live map still sends everyπ_i.')
rd(16,17,'668','(w_iL^(n−i)−1)π_(2n−i)=0','Useπ_i in this inverse equation','The equation acts on the source degreei; the second-pass notes confirm the written wrong projector. See CL-SA18-16120.')
rd(16,17,'690','en même temps, possibly struck','en = temps, live','Second-pass changes lines63,72 confirms the live conclusion requiring L and allπ_i.','high','resolved by supplied second pass')
rd(16,19,'725–779','Unqualified local Picard/discriminant claims','Recover the missing §8.4 hypotheses explicitly','Published BrauerIII includes k⊂A, complete normal dimension2 and algebraically closed residue field. Missing antecedents are not an ink correction.')
rd(16,22,'898–944','Small circle read as composition','Subscript0','Second-pass019–036_changes line70 resolves the circle; prime and subscript details remain uncertain.')
rd(16,25,'984–1061','Alternating three/four-variable signs and Q pairing','Keep the exact slot order','Associativity reduces to an alternating four-form; swapping the last two slots changes the sign. Computation records the chosen order.')
rd(16,27,'1127','kξ+V | kξ+W','kξ+W mathematically','α takes values in the even degree-two space, not the odd spaceV.')
rd(16,29,'1191–1204','checkφ, its square and tensor square not cleanly separated','Fix inverse-bivector and exterior/tensor-square normalization','The operator depends on these constants; an infinite orbit is sensitive to scalar changes. No ink choice is made.')
rd(16,34,'1328','H^(2(n−1)+i)(Y) | H^(2(n−1)−i)(Y)','The minus degree fits Lefschetz','The lower arrow raises degree by2(n−1−i).')
rd(16,34,'1354–1360','E^(n−1) cancellation extent','E^(n−1) live; ≃Ker clause cancelled','Second-pass019–036_changes lines177–178 controls the cancellation boundary.')
rd(16,36,'1401,1419','P^j | P^i; i/j mixed in bounds','Use a consistent primitive-degree index','The string decomposition and pushed-forward projector shift by2 fix the mathematical types.')
rd(16,38,'1471','i+j≤n−1 in earlier note','i+j=n−1','Second-pass037–053_changes line36 confirms equality; this selects endpoint summands.','high','resolved by supplied second pass')
rd(16,38,'1507','p_X in an operator onY','p_Y mathematically','The target summands lie inH*(Y); both domain and degree must be checked on the scan.')
rd(16,38,'1518','Λ_Xφ* where source isY','Λ_Xφ_* mathematically','The typed composition with p_Y is otherwise ill-typed. The local glyph remains a scan task.')
rd(16,40,'1579','Inserted L | Λ','Λ gives the projector identity in the tested convention','Second-pass037–053_changes line40 keeps both. Degree and string test supportΛ without deciding ink.')
rd(16,42,'1619','φ_i | φ_*','φ_* mathematically','Λ_Xφ_* is the natural left inverse of restriction. Second-pass changes line42 retains the glyph doubt.')
rd(16,44,'1717–1727','Letter dated6.1.1966','Do not silently replace by1967','Chronology suggests a question, but the literal date is retained.','medium','date reading not decided here')
rd(16,45,'1750','j−2 | j2','j−2 mathematically','A Gysin map raises degree2, so its right inverse lowers degree2.')
rd(16,47,'1785–1796','π1 in first pass/CSG','π_i','Second-pass037–053_changes line57 resolves allπ_i for surfaces; older transcriptions do not override it.','high','resolved by supplied second pass')
rd(16,48,'1804–1817','Polynomial in u after definingw=uv','Polynomial inw mathematically','Cayley–Hamilton applies to the invertible endomorphismw; u has a different source/target.')
rd(16,50,'1833–1859','Cycle dimension and cohomological index intermixed','Write every degree explicitly before identifyingA′/A″','Second-pass changes line72 confirms overtyped index remains unresolved; doubling convention matters.')
rd(16,50,'1843','φ^+ | φ*','φ* mathematically','The written simple cross remains leading ink reading; no substitution made.')
rd(16,51,'1869','L!','Possible lowering symbol or label, not automaticallyL′/L0','Doubts record a stroke and dot; the theorem seeks the lowering operator and projectors.','medium')
rd(16,52,'1889–1902','Filting; A^p→A^q→Ω_A(B)','Fitting; B^p→B^q mathematically','Second-pass changes line81 confirms Filting spelling; Ω is a B-module. Historical first ideal means modernFitt0.')
rd(16,52,'1914','Idéaux maximaux homogènes','Principaux is a mathematical guess only','Current supplied reading retains homogènes. F2³ refutes the claimed monogenic conclusion even under the plausible replacement.')
rd(16,53,'1932–1936','L^(n−k)T_k vanishes off degreek','T_kL^(n−k)T_k is the corrected cut','P², n2,k1 is an exact counterexample. This is an author-proof error, not an automatic transcription correction.')
rd(16,53,'1938–1946','n−k−j | n−k+j; no targetcut','n−k+j and targetT_(k−2j) mathematically','The target degree is2n−k+2j. The same off-degree defect affects the primitive induction.')
rd(16,55,'1998','n−k+j | n−k−j','n−k+j mathematically','Degree calculation and the preceding primitive-string inverse fix the needed exponent.')
rd(47,3,'2097,2108','D_parf | D_prof','Perfect category plausible; proper-support alternative requires definition','Repeated subscript remains unresolved; category preservation is a hypothesis, not a typographic convenience.')
rd(47,4,'2223','K0 square=(−1)^g inversion','Include[τ_A] in the relative formula','The next derived page explicitly insertsτ_A[−g].')
rd(47,5,'2260','Composite transform isid','Inversion pullback and determinant shift','The theorem was corrected but the old proof target remains. Antidiagonal support is explicit on scan6.')
rd(47,6,'2316','Lψ*(τ[−g])','Lψ*(e_*τ[−g])','The left object lives over the dual abelian scheme; the omitted zero-section pushforward is forced by the domain.')
rd(47,6,'2322','O_K described as perfect after deletingflat','Perfectness from regular zero-section and flatpullback','Flatness ofψ is the displayed sufficient hypothesis. O_K need not be a flat C-module.')
rd(47,8,'2400–2407','e_(−t) then e_t','Consistent translation sign after fixingT_t(b)=b+t','Under that convention the kernel character is trivial at−t. The overwritten glyph needs scan inspection.')
rd(47,9,'2434–2459','χL′^(−1/χ) and Chern coefficients','Rational Chern character, not a fractional line bundle; correctedc2,c3','Mukai’s ample pullback formula and exact binomial expansion determine the qualified meaning.')
rd(47,10,'2507','ch(a) | ch(x)','ch(x)','The left-hand argument isx and the identity is natural inx.','medium')
rd(47,11,'2531–2548','Ordinary product where convolution is needed; incompleteTodd factor','Convolution andT_A T_B ch(ω_A)','Track the two products and both abelian schemes throughGRR; Moonen comparator has precise base conditions.')
rd(47,11,'2553–2557','checkF undefined; shift n|−n','Specify checkF=(−1)*F∨ if retainingP, with shift+n','Derived duality changes P toP∨ and addsω_A[g]. This is one compatible reconstruction, not the ink definition.')
rd(54,3,'2625–2654','S_A/S_B and tangent/cotangent roles','Retain dual abelian variety in each exact sequence','The universal vector extension ofA has Lie algebraH1_dR(B); swappingA/B changes the Hodge sequence.')
rd(54,5,'2687','H^q(B,Ω_A^p)','H^q(B,Ω_B^p) mathematically','The differential sheaf must be onB. No second pass for this cote.')
rd(54,7,'2718–2731','A→A^(p)→V|A; p-operation notation','A as finalgroup; preserve restrictedp-operation','F followed byV gives[p]; ordinary Lie algebras lose essential information.')
rd(54,6,'2705–2713','Compressed ideal-adic flatness margin','No unique reconstructed theorem','Completeness, separation and Tor hypotheses cannot be supplied from a few ambiguous words.','high','low for a unique textual reconstruction')
rd(44,3,'2807–2843','TF and completion category; entire draft cancelled','KeepTF undefined and cancellation visible','Exact/faithful completion holds for the qualified graded category, not all finite ungradedmodules.')
rd(44,4,'2844–2867','Height sign, exponentm, insertedfibrecondition','Fix normalization and retain geometricallyintegralfibres','The source gives no unique numerical convention; modern partialcomparators cannot decide ink.')
rd(44,4,'2868–2886','Finite-kernel clause inTh6','Retain cancelled status','Do not revive the struck strengthening through a modern analogy.')
rd(44,5,'2891–2937','Primitive-root and integral-coroot claim; pairedlattices','Add hypotheses mathematically, leave wholeparagraphcancelled','Eight-root counterexample checks every written rootaxiom. Rational perfectness does not imply integral perfectness.')
rd(44,6,'2944','τ-equivalence undefined','Conditional algebraic-equivalence-up-to-multiple interpretation','Highercodimension conclusion changes radically withmeaning; no notation supplied from memory.')
rd(44,8,'2977–2984','TangentH^i(Ω^(i−1)); antistruckbefore symmetric','Ambient tangentcomparison; symmetric is live','The functorJ^i is underdefined; symmetry does not prove positivity. The cancellation is mathematically material.')
tsv('SA18_readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],READ)

LINK=[]
def lk(kind,a,b,what,evidence,ns):
    LINK.append(dict(kind=kind,**{'from':a,'to':b},what=what,evidence=evidence,note_ids='; '.join(f'MPL_16+47+54+44#{n}' for n in ns)))
lk('folder','c16:14, lines504–525','c16:15–17, lines528–692','Exterior model versus normalized universal algebra','Both passages read; first has factorial obstruction, second prescribes grading and unit lowering. Their equality is not assumed.',[1,2,3,25,27,28,29])
lk('folder','c16:9–13, lines265–481','c16:51,53,55, lines1861–1882,1926–1953,1996–2003','Earlier inverse/projector argument and later induction','Both endpoints use inverse operators to construct primitive projectors; later off-degree claim needs target cut.',[2,29,30,31])
lk('folder','c16:33–42, lines1246–1705','c16:45–46, lines1728–1784','Hyperplane identities reused in the letter','SameΛ_Xφ_* criterion and critical-degree product; exactsource formulas read.',[32,33,34])
lk('folder','c16:44, lines1717–1727','c16:48–50, lines1797–1860','Retraction and qualified repair','Both letter layers read; rational characteristic polynomial is material, date remainsliteral.',[35,36,37,38])
lk('folder','c16:19, lines725–779','c16:21,23, lines860–977','Local discriminant and global Kummer/Brauer constructions','Both passages read; local compatibility is not supplied by the global exact sequence.',[4,5,8,11,12,13])
lk('folder','c47:4–5, lines2157–2278','c47:6–8, lines2279–2419','Inversion theorem and kernel proof','The theorem correctsidentity toinversion; proof identifiesantidiagonal and leavesunitcompatibility.',[45,46,47,48,49,50,51,52])
lk('folder','c47:8–9, lines2396–2471','c47:10–11, lines2472–2573','Bundle calculation to rational Chow transform','Chern expansionandGRR read; integral/torsion conclusions distinguished.',[54,55,56,57,58,59,60,61])
lk('folder','c47:5–7, lines2227–2379','c54:3,5, lines2609–2655,2682–2704','Dual abelian tangent lines and Hodge/deRham comparison','Both endpoints read; shared determinant/tangent objects, not an explicit author crossreference.',[47,51,65,66])
lk('folder','c54:5, lines2682–2704','c54:7, lines2714–2733','Degree-one duality and p-torsion question','Cartierduality and restrictedpoperation are explicitatbothendpoints.',[66,67,68,69])
lk('folder','c44:2, lines2780–2806','c44:8–9, lines2966–3001','IntermediateJacobian theorem list and positivity letter','The laterletteradmitsundefinedrelationandunprovedpositivity; doesnotproveearliertheorems.',[72,73,74,75,77])
lk('folder','c44:4, lines2844–2888','c16:49, lines1819–1832','Height/positivity programme and algebraic splittings','Both endpoints read; common positivity dependence is an editorial comparison, not an explicit quotation.',[37,38,76,77])
lk('folder','c16:25,27,29, lines978–1062,1113–1155,1188–1206','c16:14–18, lines482–724','Abstract Hodge algebra versus Lefschetz operator formalism','Both read; neither geometrical realization nor identical normalization is inferred.',[1,2,3,80,81,82,83,84])
for ns,scans,key,loc,what in [
 ([24,30],'c16:44–50, lines1717–1860','Groth1969','§§2–3','Partial dictionary draftC→publishedB anddraftA→publishedA'),
 ([32,34,35],'c16:42,48, lines1614–1705,1797–1818','Kleiman1968','2.9–2.10','Qualified algebraic inverse and polarization criterion'),
 ([36,37],'c16:49, lines1819–1832','Kleiman1968','3.11–3.14','Conditional positive-trace semisimplicity and splitting'),
 ([38,39],'c16:49, lines1819–1832','Jannsen1992','Theorem1;Corollary1','Later comparison only: numerical semisimplicity and nilpotent kernel'),
 ([40],'c16:48–49, lines1797–1832','KatzMessing1974','Theorem2','Finite-field Künneth projectors; no generalLefschetzinverse'),
 ([30],'c16:51,53,55, lines1861–2003','Deligne1980','Théorème4.1.1','Cohomological hardLefschetz only'),
 ([4,5,8,11,12,13],'c16:19,21,23, lines725–977','BrauerIII','§8.2–8.5','Local/globalBrauertext, including explicitpublishedcompatibilitygap'),
 ([9,10],'c16:37,39, lines1446–1463,1523–1543','Matlis1958','2.5,3.1,3.9–3.10','Named priorinjective-moduletheory; Englishleafauthorshipnotinferred'),
 ([21],'c16:26, lines1063–1112','SGA3XV','6.2(iii)(b);6.2.1','Partialexacterratamatch,withG_eta/H_etavariant'),
 ([21],'c16:26, lines1066–1068,1079,1095','SGA3XVII','AppendixIII C.1–C.3','Exactreferencedappendixsections'),
 ([], 'c16:35, lines1365–1391','Karoubi1966','firstpage','Reusednamed-authorleafmatches1966definitionsnote'),
 ([44,46,47,54],'c47:3–9, lines2086–2471','Mukai1981','Theorem2.2;Proposition3.11','Fieldinversionandqualifiedlinebundletransform'),
 ([46,47,50,52,63],'c47:5–8,11, lines2227–2419,2528–2573','Laumon1996','1.2.4–1.2.5;1.3','Relativedeterminantline,unitkernelandduality'),
 ([58],'c47:9, lines2420–2471','BF2023','Theorem3.8;Question3.9','Integraltransformconditionsandremaininggeneralquestion'),
 ([58],'c47:9, lines2420–2471','HHLLMM2025','§3.2;§4.1;§5','Factorialandpolarization-degreeinversionlimits'),
 ([60],'c47:11, lines2528–2573','Moonen2026','§2.4–2.7','RelativeToddcorrection,firstpreprint2024'),
 ([65,66],'c54:3,5, lines2609–2655,2682–2704','Coleman1998','Theorems1.1,2.2','CanonicaldeRhamdualityunderbasehypotheses'),
 ([67,69],'c54:5,7, lines2682–2733','Oda1969','Corollary5.11;§1','Perfect-fieldA[p]reconstructionandCartierduality'),
 ([68],'c54:7, lines2714–2733','SGA3VIIB','Corollary4.4.1','RestrictedLie/height-oneequivalence'),
 ([72,73],'c44:2,8, lines2780–2806,2966–2984','PicardVI1962','p242','Publishedintermediate-Jacobianquestion;notall-codimsolution'),
 ([72,73,74],'c44:8, lines2966–2984','MumfordLetter1964','p89,31August1964','UniformBettiboundprogramme'),
 ([73,74],'c44:2,8, lines2780–2806,2966–2984','Kahn2021','Theorem1','Correctedcodimension2boundedness/existence'),
 ([73,74],'c44:2,8, lines2780–2806,2966–2984','ACMV2023','Proposition8.2','Exactcodimension,primeandminiversal-degreehypotheses'),
 ([77],'c44:2,8–9, lines2780–2806,2966–3001','ACMV2025','Theorem12.12;§13','Symmetricisogenyversusqualifiedpositivity'),
 ([76],'c44:4, lines2844–2867','SerreLetter1964','8August1964,p186','Surfacefibrationheight/intersectioncomparison'),
 ([78],'c44:6, lines2939–2947','Clemens1983','IntroductionandTheorem','Counterexampletooneexplicitall-codimτinterpretation'),
 ([], 'c44:5, lines2891–2937','Conrad2014','Definition1.3.3','Integralityisaseparateaxiom;reflectionuniqueness'),
]:
    lk('published work',scans,R[key]['url']+' | '+loc,what,'Both the cited source passage and the specified external locator were read; see reference_audit.json for verification limits.',ns)
tsv('SA18_links.tsv',['kind','from','to','what','evidence','note_ids'],LINK)
tsv('SA18_project_links.tsv',['kind','from','to','what','evidence','note_ids'],[])

# Actual-query mappings are authored by subject, not inferred from a title match.
GROUP={
 'integral':[(1,3),(15,1),(26,0)],'normalized':[(15,3),(21,1),(26,0),(29,2)],
 'brauer':[(10,0),(11,0),(20,0),(23,2),(26,3)],'brauerpair':[(10,0),(20,3),(23,2)],
 'etale':[(11,2),(24,3),(31,1)],'injective':[(11,1),(34,2)],'derived':[(31,2)],
 'ega':[(11,2),(24,3)],'groups':[(31,3)],
 'standard':[(10,2),(15,0),(13,1)],'standardcurrent':[(13,1),(15,0)],
 'hodge':[(20,2),(21,0),(23,0),(24,0)],
 'fourier':[(1,0),(1,1)],'fouriergeneral':[(1,1),(29,3)],
 'fourierchern':[(1,0),(1,3)],'integralcurrent':[(1,3),(13,2),(15,1)],
 'fouriertodd':[(1,1),(1,2),(13,2)],'fouriersign':[(1,0),(1,1),(34,3)],
 'derham':[(10,1),(31,0)],'flattening':[(29,1)],'completion':[(28,3)],
 'jacobian':[(6,0),(6,1),(6,2),(13,0),(15,2),(17,0)],
 'jacobianpositivity':[(6,0),(13,0),(17,0)],'height':[(13,3),(23,1)],
 'equivalence':[(26,1),(26,2)],'hodgealgebra':[(21,2),(29,2),(26,0)],
 'english':[(17,1),(20,1),(23,3),(24,1),(24,2),(28,2)],
 'karoubi':[(17,2)],'jacobiantangent':[(29,0),(13,0),(17,0)],
 'rootcounter':[(21,3),(28,0),(28,1),(34,1)],'chambers':[(34,0),(35,0)],'jannsen':[(35,1),(15,0)]}
Q={}
for p in sorted((O/'research').glob('web_*.json')):
    x=json.loads(p.read_text());num=int(p.stem.split('_')[-1])
    for engine in ('system1_search_query','system2_search_query'):
        for i,q in enumerate(x.get('request',{}).get(engine,[])):
            Q[(num,i)]=(q['q'],engine,p.name)
SEARCH=[]
def searchrows(sid,groups,refs,result,match):
    seen=set()
    for group in groups:
        for key in GROUP[group]:
            if key in seen:continue
            seen.add(key)
            q,engine,log=Q[key]
            SEARCH.append(dict(statement_id=sid,date=DATE,query=q,engine=engine,source_families='arXiv; Numdam; primary author/journal sites; published EGA/SGA; bibliographies; MathOverflow leads where relevant; zbMATH access attempts separately logged',opened_urls='; '.join(r['url'] for r in refs),locators='; '.join(r['key']+': '+r['locator'] for r in refs),result=result,exact_hypothesis_match=match,verification_limits='; '.join(r['key']+': '+r['verification'] for r in refs),request_log='research/'+log))
for c in C:
    searchrows(c['id'],[c['search_group']],c['refs'],c['fate'],c['statement']+' '+c['present_status'])
for p in P:
    groups=[]
    for o in p['occurrences']:
        if o['claim']:
            n=int(o['claim'].rsplit('-',1)[1])-16000
            if CM[n]['search_group'] not in groups:groups.append(CM[n]['search_group'])
    searchrows(p['id'],groups,p['refs'],p['state_of_art'],p['plausible_today'])
tsv('literature_search.tsv',['statement_id','date','query','engine','source_families','opened_urls','locators','result','exact_hypothesis_match','verification_limits','request_log'],SEARCH)

EV=[]
def ev(sid,typ,out):EV.append(dict(statement_id=sid,date=DATE,who=WHO,type=typ,outcome=out))
for x in I.values():
    ev(x['id'],'targeted proof check','Source-alignment check only: read the indexed entry, its transcription passage, doubts and applicable second-pass controls. '+x['check_reason'])
for c in C:
    ev(c['id'],'targeted proof check',c['computation']+' Literature comparison: '+c['fate']+' This event does not assert an independent proof beyond the stated check.')
COMPS={1:'exterior_rank2,4,6,8,10',2:'exterior_rank2,4,6,8,10',3:'forget_grading',4:'discriminant_pairing',5:'discriminant_pairing (blowup_congruence field)',6:'F2_cube',15:'different_tower',26:'normalized_strings_n1..n5',27:'normalized_strings_n1..n5',31:'normalized_strings_n1..n5',32:'normalized_strings_n1..n5',34:'cayley_hamilton_inverse',51:'koszul_fibre',55:'chern_coefficients; elliptic_product',57:'chern_coefficients',80:'hodge_associativity',81:'hodge_associativity (isotropic_line_norm field)',83:'six_dimensional_model',84:'cyclic_family_m1..m4',86:'scan53_projective_plane',104:'same_top_power_not_lefschetz',115:'eight_root_counterexample',120:'scan17_wrong_projector'}
for n,name in COMPS.items():
    path='outputs/root_counterexample.json' if n==115 else 'outputs/computations.json'
    ev(CM[n]['id'],'computation or formal certificate',name+'; exact arithmetic/code and output saved in '+path+'. Scope is the finite calculation and separately stated general argument, not an automated literature verdict.')
for n in [3,4,5,26,31,34,36,37,79,80,81,84,86,100,101,103,104,115,116,119]:
    ev(CM[n]['id'],'independent re-proof',CM[n]['computation']+' Full scope and assumptions are in the claim and source_review.md; no stronger historical attribution is made.')
for n in [1,6,27,55,86,115,120]:
    ev(CM[n]['id'],'refuted, with refined ID',f'The literal or explicitly overstrong statement is refuted; refined statement is retained in the same claim {CM[n]["id"]} and item SA18-{16000+n}. '+CM[n]['present_status'])
for k,r in R.items():
    full=r['verification'].lower().startswith('verified:')
    ev(k,'used and rechecked in this run' if full else 'targeted proof check',r['verification']+' Locator: '+r['locator']+'. '+('This means the specified source content was read, not every proof in the work independently verified.' if full else 'No inaccessible theorem is counted as verified.'))
ev('SUPP-parent-c55','independent re-proof','Checked the parent-supplied literal lattice and proposed replacement, plus the stated RP² constant-sheaf counterexample. See supplemental_torus_check.md. This agent did not inspect c55 source pages; parent owns source verification and canonical claim IDs.')
tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],EV)

bib=[]
for k,r in R.items():
    verified=r['verification'].lower().startswith('verified:')
    fields={'title':r['title'],'author':r['author'],'year':r['year'],'url':r['url'],'note':'verified' if verified else 'unverified','annote':r['locator']+'; '+r['verification']+'; '+r.get('date_note','')}
    if r.get('doi'):fields['doi']=r['doi']
    bib.append('@misc{'+k+',\n'+',\n'.join('  '+a+' = {'+str(b).replace('{','(').replace('}',')')+'}' for a,b in fields.items())+'\n}')
(O/'SA18_references.bib').write_text('\n\n'.join(bib)+'\n')

counts=dict(entries=85,items=len(I),claims=len(C),problems=len(P),readings=len(READ),links=len(LINK),external_project_links=0,references=len(R),literature_search_rows=len(SEARCH),check_events=len(EV),claim_classes=dict(collections.Counter(c['class'] for c in C)),item_kinds=dict(collections.Counter(x['kind'] for x in I.values())))
writejson('outputs/finalize_counts.json',counts)
print(json.dumps(counts,ensure_ascii=False,indent=2))
