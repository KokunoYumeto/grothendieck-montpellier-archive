#!/usr/bin/env python3
"""Manually authored problem, reading and link tables; reuses checked claim locators."""
from pathlib import Path
import json,csv
P=Path(__file__).parent
claims=json.loads((P/'claims.json').read_text()); by={int(c['id'].rsplit('-',1)[1]):c for c in claims}
problems=[]
def p(n,title,nums,as_written,today,why,worth):
    cs=[by[x] for x in nums]
    problems.append(dict(id=f'MP-SA23-bt-{n:02d}',title=title,occurrences=[dict(claim=c['id'],cote=c['cote'],scans=c['scans'],lines=c['lines']) for c in cs],as_he_states=as_written,plausible_today=today,state_of_art=' '.join(c['id']+': '+c['fate'] for c in cs),why_open=why,worth=worth,refs=list(dict.fromkeys(r for c in cs for r in c['refs']))))
p(1,'Characteristic-zero restriction of augmented operator factorization',[1,17],
 'The author circles “Spécial à car.0?” beside the canonical factorization through closed one-forms.',
 'The conditional factorization follows from the formally exact stratified de Rham operator complex; ordinary formal Poincaré fails in characteristic p. Divided-power or crystalline replacements are different formulations.',
 'The sheet gives the characteristic doubt but no historical explanation of why it was left there; published Crystals §6.5 states the characteristic boundary.',
 'Worth a short convention study, chiefly to identify precisely which augmentation and order filtration were intended.')
p(2,'Stein qualification and fibrewise period criterion',[5,7],
 'The author warns that the quotient formula works as written only for a Stein morphism, then invokes fibre de Rham for the converse.',
 'Use relative de Rham hypercohomology, and state base-change/local-system hypotheses before upgrading fibrewise period vanishing to a sheaf statement.',
 'The only explanation supplied is the explicit Stein warning; no undocumented motive is assigned.',
 'Worth an editorial reconstruction because it prevents a false non-Stein extension of the argument.')
p(3,'Compatibility with the relative differential',[6],
 'The lifted operators are asserted to commute with the relative differential; the resulting cohomology formula is left to immediate verification.',
 'For an integrable splitting, Cartan’s formula makes this precise and gives splitting-independent cohomology action.',
 'The text treats it as routine, not as a suspected obstruction.',
 'Already discharged by the targeted proof check; retain as a checked omitted step, not a research problem.')
p(4,'Admitted period differentiation identity',[11],
 'Equation (15) is explicitly admitted without proof on 93/228.',
 'The period pairing intertwines Gauss–Manin differentiation and locally constant homology in the smooth complex comparison setting.',
 'The author says he will not prove it here; no stronger reason is supplied.',
 'Worth incorporating the short local proof and exact published reference into a future commentary; no new theorem is needed.')
p(5,'Nonhorizontal endpoint correction terms',[13],
 'The author asks to make μ(a,b) explicit for general sections and stops after saying the two terms must be calculated.',
 'Use the interior Lie derivative plus endpoint contractions with vertical velocities, with iterated endpoint jets for higher operators.',
 'The manuscript stops at the calculation; no external source explains why it was not completed.',
 'Worth a short clean derivation in the folder commentary, with the intersection obstruction kept visible.')
p(6,'Meaning of formal exactness and finite-order shifts',[15,16],
 'Quoted formal exactness is asserted to imply both composition sequences are exact for every P.',
 'Specify the exact principal-parts or formalized complex, the orders of D,D′, and the splitting/projectivity conditions needed for both Hom directions.',
 'The definition is absent; the marginal heading says to write up or review the relative version.',
 'High editorial value: one focused run can formulate candidate hypotheses and test small order truncations without assuming a theorem not written.')
p(7,'Injection into additive maps of closed forms',[19],
 'The arrow Diff₊→Hom_add(ker d¹,P) is marked “injectif?”.',
 'It is injective under the displayed quotient presentation, since d¹d⁰=0; the presentation’s premise remains separate.',
 'No reason for the doubt is stated. The short conditional argument resolves the question.',
 'No independent research development needed; include the two-line proof in the commentary.')
p(8,'Integrability of the principal-parts augmentation',[21],
 'The author lists a surjective augmentation E→M and further integrability conditions, without writing them.',
 'Recover a precise diagonal cocycle condition for the specified pro-map ρ∞ and determine when it comes from a stratification of a locally free E.',
 'The text explicitly leaves the conditions unwritten; the general published stratification cocycle is available.',
 'Worth a focused reconstruction with a rank-one or affine-coordinate test before making a general equivalence claim.')
p(9,'Weakening smoothness in the lift comparison',[22,88],
 'A marginal note says local T-isomorphism over X₀ suffices in place of smoothness.',
 'Local isomorphism suffices for the torsor property; the displayed derivation/tangent formulas additionally need the appropriate actual ideal, flatness and local-freeness hypotheses.',
 'The margin does not state which later assertions the weakening covers.',
 'Worth isolating the weakest valid theorem; a few hours can separate the torsor statement from the coefficient identifications.')
p(10,'Constructing a derived morphism from local homotopies',[23,25,26,29],
 'The author seeks a derived morphism K′→K″ from a torsor and homotopy data.',
 'Use the additive Hom-complex relation, the degree−1,0 extension resolution and the correctly linear coefficient category; arbitrary homotopy choices do not disappear.',
 'The pages are a worked construction with compressed and conflicting notation, not a stated unsolved conjecture.',
 'Highest commentary priority: the exact published counterpart in Crystals §3.4 can be compared line by line after scan adjudication.')
p(11,'Tensor-invariant lemma with a sketched proof',[37],
 'Serre says he will only sketch the known reductive invariant-tensor lemma.',
 'The stabilizer of all mixed tensor invariants is the reductive group in characteristic zero, as a group scheme and hence on all algebra points.',
 'Serre explicitly calls the result well known and omits details for that reason.',
 'Already checked at the stated level; no research novelty is suggested.')
p(12,'Immediate dual and tensor Hodge–Tate check',[39],
 'Serre calls the dual formula immediate and states tensor stability.',
 'Dual weights negate and tensor weights add; this does not make the two-weight subcategory tensor closed.',
 'The source treats the verification as elementary.',
 'Discharged by direct decomposition; retain for convention control only.')
p(13,'Temporarily admitted torsion ramification lemma',[51],
 'Lemma3 is provisionally admitted on scan15 and then proved on scans15–16.',
 'The exact e≥c p^(nh) estimate holds for the stated one-dimensional finite-height formal groups, with strict threshold for the unique-minimum valuation step.',
 'It did not remain open: the proof is completed on the next sheet.',
 'No new research task; the useful work is preserving the proof completion and strict inequality.')
p(14,'General formal-group centralizer equality',[53],
 'Serre states that the Lie algebra is the centralizer of geometric End(F), but omits the more complicated proof; a margin refers to Sen.',
 'Use the exact one-dimensional formal-group hypotheses and Sen’s theorem, distinguishing the scalar special case already proved.',
 'Serre expressly describes the omitted proof as analogous but more complicated.',
 'Worth a later original-paper proof audit if needed; the present search establishes the attribution and does not label the result open.')
p(15,'Direct proof of inertia openness',[54],
 'Serre gives an indirect proof but says he knows no direct proof.',
 'The inertia and full images have the same Lie algebra in the formal-group setting; a separate task could compare proof methods.',
 'The source’s reason is methodological, not a gap in the established conclusion.',
 'Moderate expository interest; no need to relabel a proved theorem as conjectural.')
p(16,'Ramification filtration versus Lie filtration',[55],
 'Serre asks whether the indices satisfy w=e_K v+O(1).',
 'State Sen’s bounded-shift inclusions for upper ramification and a standard p-power Lie filtration in the totally ramified mixed-characteristic setting.',
 'The later annotation names Sen; no other reason for the earlier open state is documented.',
 'Already settled; useful only as a carefully normalized historical comparison, especially before any equal-characteristic analogy.')
p(17,'Hodge cocharacter generation of the neutral envelope',[57],
 'The course calls the neutral-component generation statement probable and notes Sen’s later proof.',
 'Retain the neutral component and the course’s algebraically closed residue field; for general K formulate the inertia version.',
 'The summary states a conjecture, and the later note records its resolution; no proof-history beyond the verified publication dates is invented.',
 'High value for correcting overstatements, but not a new open theorem.')
p(18,'Two-weight group classification and realization',[61],
 'The course ends with an attempted classification and a later Springer/Jordan annotation.',
 'Separate the established classical/minuscule algebraic possibilities from their realization as Galois groups of BT objects; Jordan pairs require the correct representation data.',
 'Serre1979 p.185 explicitly separates the realization question; no claim that every possibility was already realized is supported.',
 'Worth a bounded classification table with exact representation hypotheses; realization questions require a distinct subsequent literature search.')
p(19,'Equal-characteristic generic-fibre full faithfulness',[62],
 'Serre hopes Raynaud’s proof of Tate’s mixed-characteristic theorem may adapt to equal characteristic.',
 'Use de Jong’s theorem over an integrally closed Noetherian integral domain, retaining normality and the exact fraction-field Hom statement.',
 'The course only records the hope; de Jong supplies the later theorem. The erratum does not retract it.',
 'Settled in the stated modern scope; worth documenting the date and erratum accurately, not developing as an open problem.')
p(20,'Technical gaps in a Serre–Tate proof method',[63],
 'Tate’s alternative sheaf-theoretic proof is reported to have unresolved technical difficulties, while the 1964 theorem is already known.',
 'The nilpotent p-nilpotent deformation equivalence is established by the later crystalline/Drinfeld proofs, with compatibility data included.',
 'The source explicitly identifies difficulties of a proof method, not doubt about the theorem.',
 'A historical comparison is possible; no new mathematical theorem is presently required.')
p(21,'Extending crystalline and filtered data tensorially',[66,70],
 'The author asks to extend the BT F-isocrystal, filtration and Hodge comparison to M^BT, compatibly with tensor and internal Hom.',
 'First settle the generator and base-field readings. The actual BT-generated crystalline category has the standard period functor; the literal all-two-weight Hodge–Tate category is larger.',
 'The text asks the question but gives no reason for not resolving it; the definitional ambiguity is observed now, not assigned as his historical motive.',
 'Highest value after scan checking: one run can formulate the two distinct questions and test exact essential-image conditions.')
p(22,'Uniqueness of the extended functor',[71],
 'The extension is asked to be unique up to unique isomorphism.',
 'Fix the category, variance, comparison data and admissibility; distinguish canonicity of the standard period construction from uniqueness of arbitrary unrigidified tensor functors.',
 'No historical explanation is supplied. The later torsor/cocycle pages exhibit the kinds of choices at issue.',
 'Worth developing only after the extension problem is made precise; otherwise uniqueness has no stable quantifiers.')
p(23,'Unique Hodge cocharacter and torsor triviality',[69,72],
 'The cocharacter is called unique, followed by unfinished “Du moins si”; R is called trivial with an ambiguous qualifier.',
 'A specified tensor grading determines a unique cocharacter; a filtered fibre functor’s splitting torsor is generally noncanonically split under the explicit Ziegler hypotheses.',
 'The qualifier is unfinished and the torsor notation compressed; no reason for abandonment is stated.',
 'Worth resolving alongside the twist-sign scan check; a theorem with only π-invariance would be too weak.')
p(24,'Existence of a full semilinear Γ action',[74,75],
 'The pages package descent and Frobenius data as a group extension and discuss its sections, conditional on a section existing.',
 'Specify Γ, π, π̃, the coefficient group, topology and Frobenius action before computing the extension obstruction; splitting existence is not provided by the H¹ parametrization.',
 'The manuscript supplies insufficient definitions here; this is an identifiability limit, not evidence of an undeveloped theorem.',
 'High prerequisite value: a few hours can produce a precise candidate model and list which axioms are genuinely on the page.')
p(25,'Relative nonabelian uniqueness and deletion scope',[76,77,79,80,81],
 'The final paragraph asks whether extensions agreeing on π are conjugate, reformulates restriction injectivity or trivial kernel, and replaces torsor by homogeneous space. Codex marks the whole upper block deleted; Pro does not.',
 'The neutral fibre is normalized cocycles modulo A^π, with stabilizer A^Γ. Full injectivity requires twisted fibres. Bare rank-one models violate uniqueness; extra admissibility conditions must be explicit.',
 'The local torsor-to-homogeneous correction is visible, but whether the whole question was later cancelled cannot be adjudicated without scans.',
 'Worth a focused reconstruction after Γ is fixed; retain the countermodels as boundary tests and do not silently revive a possibly cancelled question.')
(P/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')

readings=[]
def r(cote,scan,line,reading,alt,evidence,weight='high',confidence='medium'):
    readings.append(dict(cote=cote,scan=scan,line=line,reading=reading,alternative=alt,evidence=evidence,weight=weight,confidence=confidence))
r('93',221,'3–8','isomorphism and coefficient g* in initial quotient','Check map direction, isomorphism sign, coefficient and E on preceding sheet','The retained page does not define the quotient objects; the apparent theorem cannot be identified.')
r('93',221,'10–22','all operators “à coeff cts”','Check that this denotes the later augmentation kernel, and whether characteristic-zero qualification is live','Diff₊ is explicitly defined on231; translation-invariant and augmentation-zero operators are different notions.')
r('93',221,'24–26','g⁻¹dg valued in ordinary closed forms','Check preceding commutative-group hypothesis or a bracket-modified closedness condition','Maurer–Cartan gives dθ=−θ∧θ; closedness is not automatic for noncommutative groups.')
r('93',224,'81–82','ne marche tel quel que si X→S est steinien','Check negative/restrictive wording and exact attachment of the margin','The global-form quotient is generally not degree-one hypercohomology outside acyclic settings.')
r('93',227,'151–162','horizontal a,b imply μ=0','Check for a lost additional condition, cancellation, or different scope','Product A¹ family, ω=dx,D=id,a=0,b=1 satisfies the stated hypotheses but gives μ=1. No correction is adopted.')
r('93',227,'155–161','1-cycle with a boundary in subsequent phrase','Possibly path/chain or a change of subject; verify ink','A cycle has zero boundary, while endpoint primitives concern chains. Source doubts explicitly preserve the word cycle.')
r('93',228,'164–176','deleted bar on D in equation15','Check whether D acts on the class or a lifted operator acts on the form','The two sides live in different objects unless the action/lift distinction is preserved.')
r('93',229,'178–189','one may suppose both sections horizontal','Check omitted disjointness/tangent condition or the scope of the reduction','Intersecting sections a=0,b=s at s=0 have incompatible horizontal tangents.')
r('93',230,'208–220','relative closedness implies closed pullback, block deleted','Preserve full cancellation scope; verify relative versus absolute differential','ω=t dx pulls back to t du with d=dt∧du. This is not reinstated as a surviving assertion.')
r('93',231,'229–244','Diff order shifts i,i+1,i+2','Check order assumptions on D,D′ and meaning of formally exact','The bounds require compatible operator orders; ordinary exactness alone does not imply both Hom exactness sequences.')
r('93',231,'251–262','δ_i^E and Diff₊','Verify section and augmentation direction, plus sign versus other subscript','The kernel definition and quotient representation depend on the stratification section and left module structure.')
r('93',232,'269–271','Ω or Ω² in previous operator term','Ω² is the type-consistent candidate','The differential composing into Ω¹→P is d¹:Ω¹→Ω²; ink still decides.')
r('93',232,'281–295','δ_i exponent and ρ_i source','Check E superscript and image Oρ_i(E)','The represented quotient imposes annihilation of the correct stratification image.')
r('93',234,'325–347','local isomorphism replaces all smoothness hypotheses; tangent tensor formula','Check scope of margin and actual ideal coefficient','Local nonemptiness gives a torsor, while J≅I⊗O_X₀ and tangent-tensor identification need flatness/local freeness.')
r('93',235,'384–393','u(pg)=u(p)v(g), additive v, u(g)=dh+hd','Candidate additive relation u(p+g)−u(p)=d_Hom k(g)','u is defined on P, not G; the printed1968§3.4 uses a coherent additive Hom-complex formulation.')
r('93',235,'385–393','h or k; K′ or K″ in homotopy domain','Check homotopy letter and domain so k:G→Hom^(−1)(K′,K″)','The chain map into Hom(K′,K″) requires this source/target. Geometric endomorphism homotopy on234 must be transported correctly.')
r('93',235,'414–418;236:424–432','L degrees0,1 then degrees−1,0','Check degree labels or intended shift','The augmentation L→Z[0] and Hom-complex chain map require degrees−1,0.')
r('93',236,'430–442','φ⁰|P=u|v and φ⁰i=u','Check u/v labels and additive relation','The restriction to P is u, while the restriction to G must be the Hom differential of k.')
r('93',236,'445–450','O_X≃RHom(K′,K″)','Candidate arrow without isomorphism, or an intermediate resolution quasi-isomorphism','At a point K′=K″=k² gives dimensions1 and4; published counterpart has a morphism, not universal equality.')
r('93',236,'445–460','tensor and derived Hom over O_X','Check which inverse-image base coefficient ring is intended','De Rham d is base-linear but not O_X-linear; ordinary Hom→RHom need not be an isomorphism.')
r('161-5',10,'690','M=I_alg (Sen)','Possible missing neutral-component superscript0','Ramified quadratic weight-zero character has M=1 but I_alg=μ₂; exact later theorem keeps the connected component.')
r('161-5',14,'816–839','End(F) versus End_A(F)','Verify geometric versus base-field endomorphisms and integral versus rational tensor','Lie commutant uses finite extensions, whereas Galois commutant uses the original base.')
r('161-5',16,'896','inserted strict < in valuation threshold','Check that the inequality is strict','Formal G_m at p=2,x=−2 cancels exactly at the boundary.')
r('161-5',17,'963','Lubin paper dated1961','1967 bibliographical candidate','Official Annals85(2),296–302 metadata gives1967; archival text remains unchanged.','medium','high')
r('161-5',19,'1007','residue field algebraically closed','Verify this standing hypothesis carries into course assertions20–21','Full-image open-envelope and weight-zero finite-image assertions require that context.')
r('161-5',21,'1062','V_C=V(0)+V_C(1)','Candidate V_C(0) in the first summand','The equation is a decomposition over C; subsequent dimensions use C-summands.')
r('161-5',23,'1127–1145','M^(u|1), effective M^(n), category generated by M^(1)','Check superscripts and whether generators are all two-weight HT objects or the actual BT subcategory','Tate curves show these two generated categories differ; this is the key extension-problem quantifier.')
r('161-5',23,'1147–1154','T_p to Modf(Q_p), called fibre at Ω','Keep codomain Q_p; do not change it to Ω merely because of the name','The neutral group is over Q_p and scalar extension is a separate operation.')
r('161-5',23,'1181–1184;24:1190','T_DR|T_DE, L|K vector space, later T_cr','Check whether crystalline and de Rham functors are distinct and which field each uses','F-isocrystal lives over L=Frac W, filtration over K; names cannot be harmonized by preference.')
r('161-5',24,'1190','T_DR=T_cr⊗_K L','Candidate T_DR=T_cr⊗_L K','The preceding field tower is L⊂K; current displayed tensor direction is ill-typed for the intended spaces.')
r('161-5',25,'1290–1293; Codex02:310','Pro τuτ⁻¹; Codex τ⁻¹uτ','Retain both inverse orders for scan adjudication','Right-action conventions affect compatibility, but mathematics cannot decide which witness reads the ink.')
r('161-5',26,'1296–1307','π=Aut_L Ω','Possibly Aut_K Ω or a deliberate switch from π to π′','On23 π=Gal(Kbar/K),π′=Gal(Kbar/L); descent field changes if these are exchanged.')
r('161-5',26,'1344; Codex02:333','Pro S_Ω(i); Codex S_Ω(−i)','Retain both twist signs; identify whether Tate line or its dual is named','Cancelling the eigenspace character fixes a sign only after the Tate-line convention is known.')
r('161-5',26,'1357–1365','unique … Du moins si [unfinished]','Check any lost qualification after the phrase','A tensor grading determines its cocharacter, but π-invariance alone does not.')
r('161-5',27,'1393–1415','R trivial; can(uni|mais); U′ or U″; G′ or G″','Check qualifiers and every prime before making a canonical identification','A torsor may be trivial without a canonical section; contracted products identify inner forms, not necessarily original G.')
r('161-5',27,'1423–1441','descent L→K, P_K≃P^(f|φ), π̃ and π','Check field direction, Frobenius exponent, and whether π is kernel or another subgroup','The extension/cocycle problem depends on these data; no normality follows from mere subgroup notation.')
r('161-5',28,'1445–1477','G′_S(S|Ω)','Check base object S and its point argument','Identifying fixed points with G′_L(L) requires specified descent, not just a looped letter.')
r('161-5',29,'1489–1495','injectif … noyau nul','Check qualifier and whether weaker neutral-fibre formulation is intended','Nonabelian H¹ has pointed sets; the A₅ computation shows trivial neutral fibre does not imply injectivity.')
r('161-5',29,'1479–1498; Codex02:407–418','Pro live upper paragraph; Codex whole upper paragraph deleted','Do not adjudicate cancellation without the scan','This changes whether the final cohomology question survives, independently of the local torseur→homogeneous correction.')
r('161-5',29,'1496–1498','torseur deleted, esp. homogène inserted','Preserve local correction separately from disputed larger cancellation','Stabilizer is A^Γ, so a single orbit need not be free.')
r('161-5',29,'1521–1551','T_K argument Q_p|deleted K; Ñ_K≃g_K×Z_K; O|0 subscripts','Check every point argument and generic/special/integral base label','T(Q_p)=K× whereas T(K)=(K⊗K)×; Néron generic and special fibres differ.')
r('161-5',29,'1540–1551','oblique π and point-group isomorphism','Possible uniformizer ϖ, distinct from the earlier Galois group π','A uniformizer splits the valuation sequence noncanonically; the label cannot be decided from shape-free mathematics.')
def tsv(name,rows,fields):
    with (P/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
tsv('readings.tsv',readings,['cote','scan','line','reading','alternative','evidence','weight','confidence'])
print(len(problems),'problems;',len(readings),'mathematically material reading flags')

links=[]
def link(kind,src,dst,what,evidence,ns):
    links.append(dict(kind=kind,**{'from':src,'to':dst},what=what,evidence=evidence,note_ids='; '.join('MPL_93_221-236+161-5#'+str(x) for x in ns)))
link('folder','93/221:10–26','93/231–233:245–313','Augmentation-zero differential operators and characteristic qualification','Both source ends read. Same Diff₊ construction; no explicit cross-reference is written.',[6,20,21,22,23,24,25])
link('folder','93/224–228:79–176','93/234–236:316–460','Cartan homotopy underlying cohomological independence and derived comparison','Both ends read. Shared formula and construction, without identifying every coefficient category.',[11,13,26,34,35,97])
link('folder','161-5/008–009:591–677','161-5/023,026:1114–1186,1324–1386','Hodge–Tate grading, cocharacter and twisted descent','Both ends read; the handwritten twist sign remains witness-dependent.',[39,57,63,64,65])
link('folder','161-5/020:1051–1056','161-5/029:1521–1528','Restriction-of-scalars torus and T_E(Q_p)=E×','Both ends read. An object-level internal parallel, not an explicit author cross-reference.',[49,90,92])
link('folder','161-5/021:1082–1086','161-5/022:1088–1105','Serre–Tate deformation theorem and ordinary canonical lift','Both ends read in the printed course report; no date transferred to adjoining handwriting.',[53,54])
link('folder','161-5/024:1200–1202','161-5/028–029:1454–1498','Tensor-extension uniqueness and later semilinear action/conjugacy question','Both ends read; a related reformulation with undefined Γ data, not proved equivalence of complete problems.',[68,69,81,82,83,85])
link('published work','93/224:79–85','bt_GrothCrystals1968 §1.2 pp.307–308; §3.2–3.3 pp.324–326','Hypercohomology, Stein simplification and connection','Both source and exact published passages opened and read.',[10,11,13,14])
link('published work','93/231–233:224–314','bt_EGAIV4 §16.8.1–16.8.4 pp.39–41; bt_GrothCrystals1968 §6.2–6.5 pp.345–350','Principal parts, formalization and characteristic-zero Poincaré lemma','Both ends read. This does not identify the unspecified exact finite-order “formal exactness” premise.',[6,20,21,22,23,24,25])
link('published work','93/234–236:316–460','bt_GrothCrystals1968 §3.4 pp.326–329','Exact torsor-extension/derived-comparison construction','Both ends read. Published text has additive affine Hom relation, degrees−1,0 and a morphism into derived Hom. Talks1966/publication1968; archival leaf undated.',list(range(26,36))+[97])
link('published work','93/233:310–313','bt_GrothCrystals1968 Appendix pp.356–357','Stratification diagonal cocycle and integrable connection','Both ends read. General cocycle framework, not a complete quotient-specific converse.',[25])
link('published work','161-5/004:494','bt_Serre1967 footnote p.118','Grothendieck’s suggestion to replace Lie algebras by algebraic groups in relation to motives','Attached published endpoint and publisher identity checked. This credits an idea; it does not identify the universal group on023 with a motivic Galois group.',[1,36])
link('published work','161-5/010,020:690,1040–1046','bt_Sen1973; bt_Serre1979 Theorem2 and Corollary3 pp.159–160','Sen annotation and neutral-envelope generation','Publisher metadata and exact later theorem read; original Sen full proof not read. Neutral-component qualification is required.',[3,47,48])
link('published work','161-5/017:939–954','bt_Sen1972; bt_FontaineOuyang A.85 pp.197–200','Bounded-shift ramification/Lie-filtration comparison','Exact later formulation opened and matched; original Sen metadata verified.',[3,46])
link('published work','161-5/021:1069–1077','bt_Springer1973 §11 via bt_Serre1979 p.182, bibliography p.187','Jordan-algebra classification annotation','Source and Serre’s exact locator read; Springer publisher page is later reprint metadata, not a proof reading of original§11.',[3,50,51])
link('published work','161-5/021:1078–1083','bt_deJongICM1998 Theorem2 p.261; bt_deJongErratum1999 p.225','Equal-characteristic generic-fibre full faithfulness','Exact theorem and erratum read. Normal Noetherian integral hypotheses retained.',[52])
link('published work','161-5/021–022:1082–1105','bt_Katz1981 Theorem1.2.1 p.143; Theorem2.1 pp.148–149','Serre–Tate deformation and ordinary parameters','Exact hypotheses and statements read. Messing metadata is additional historical attribution only.',[53,54])
link('published work','161-5/023–024:1137–1202','bt_Liu2013 Theorem2.2.1 p.666 and Remark2.2.5 p.670; bt_Gunton2021 §1.2/Example3.4','BT essential image and noncrystalline Tate-curve boundary','Both exact modern endpoints read. All two-weight HT generators are not silently replaced by BT generators.',[60,61,68,78,79,80])
link('published work','161-5/026–027:1357–1415','bt_Ziegler2015 Theorem3.6; Theorems4.13–4.16,4.39','Grading/cocharacter and filtered-functor splitting torsor','Exact theorem statements read. Conditional identification of the source’s R; no canonical section asserted.',[65,66,70,71])
link('published work','161-5/029:1521–1551','bt_JordanRibetScholl2024 §1.1 and Proposition1.4','Néron multiplicative model, valuation and Weil restriction','Both mathematical endpoints read. This diagnoses base/model ambiguities without deciding the handwritten diagram.',[89,90,91,92])

# Earlier-context endpoints are intentionally quarantined, not counted as
# verified archival/published-work links. Their names are copied from read notes.
def lead(src,dst,what,ns):
    link('our projects',src,dst,what,'Lead only: the source note and current transcription endpoint were read; the named earlier-run file was not supplied, so its endpoint is unverified. No proof or status is imported.',ns)
lead('MPL_93_221-236+161-5 notes#1–5','Hua hua_project/161-5.modern.tex I; README.md; notes/RESULTS_STATE.md Orientation','Offprint identity, dates and census; earlier MPL_93_002-046 C01 scans037–046 has different typed composition.',range(1,6))
lead('93/221','Hua 93.modern.tex XVIII scans219–221; MPL_93_002-046 E26/P06 scans023,036','Missing preceding group/operator construction and characteristic comparison.',[6,7])
lead('93/222–230','Hua 93.modern.tex XIX scans222–230; XI scans142–160; XII scans162–167','Analytic periods, endpoints, Stein warning and prior Manin-style construction.',range(8,20))
lead('93/222–230','MPL_93_002-046 P04–P08 scan036; P09 scans044–046','Earlier Schwarzian/projective operator not identified with the present Gauss–Manin family.',[8,9,11,13,16,17,19,93,95])
lead('93/231–233','Hua 93.modern.tex XX and XI scan160; XIII scans168–187','Formal exactness, augmentation and integrability; characteristic-p classes.',range(20,26))
lead('93/234–236','Hua 93.modern.tex XXI; notes/RESULTS_STATE.md finding93-derived-morphism-homotopy-torsor','Earlier register reports unresolved search and partly proved Lean card; neither status is upgraded from that label.',list(range(26,36))+[97])
lead('93/234–236','MPL_93_002-046 C25,C30,C33 scans044–046','First-order canonical comparison method; full crystal programme not proved by these leaves.',[35,77,96,97])
lead('161-5/003–022','Hua 161-5.modern.tex I; notes/RESULTS_STATE.md Orientation','Printed Serre text and later annotation comparisons; dates separated from handwriting.',range(36,59))
lead('161-5/023–027','Hua 161-5.modern.tex II–III','Field tower, generator category, fibre functors, variance, twist and action conventions.',range(59,81))
lead('161-5/021','MPL_93_002-046 C14,C28','Serre–Tate proof-method history; no endorsement of an earlier proof claim.',[53])
lead('93/234–236;161-5/024','MPL_93_002-046 C02 scan038','Integral nil-invariance lead; smooth first-order derived comparison is a different statement.',[77])
lead('161-5/023–024','MPL_93_002-046 C06,C35 scans039,043–044','Integral F–V essential image is not settled by rational Tate embedding or the tensor-extension question.',[68,78])
lead('161-5/024','MPL_93_002-046 C17–C19 scan043','No universal alternating F–V exactness assertion occurs in the retained rational data.',[76])
lead('161-5/024','MPL_93_002-046 C12,C24 scans041,044–046','Internal-Hom/duality variance requires a fixed covariant normalization.',[79])
lead('161-5/027–029','Hua 161-5.modern.tex III–IV','Γ reconstruction, normalized cocycles and rank-one countermodel; the model is independently checked only with its stated hypotheses.',range(81,89))
lead('161-5/029','Hua 161-5.modern.tex V','Néron/torus interpretation, point groups and possible uniformizer label.',range(89,93))
lead('93/221–236;161-5/023–027','README.md S20; MPL_93_002-046 P04–P09','Thematic cluster does not identify a single uniformization–Cartier–p-curvature construction.',[93])
lead('93/224,234;161-5/021','MPL_93_002-046 E26 scan023; MPL_5+6_001-037 cote6 scan007 item10; Hua93 XIII','Cartan homotopy, Cartier duality and Cartier operator are distinct; no third operation inferred from names.',[94])
lead('93/224–229;161-5/022–024','MPL_93_002-046 E06,E26,P08,C25,C33 scans004,023,044–046; prior Legendre/Hasse computation','Conditional arithmetic comparison; absent family/matrix never treated as a checked endpoint.',[95,96])
lead('93/221–236;161-5/023–029','README S20 cotes159 and64; MPL_93_002-046 P09','Same-family and coefficient-category comparison remains unverified; target cotes not in assigned source set.',[98])
lead('161-5/028–029','SECTIONS_OVER_Q A1; EXIT_TOWER E.49; FINMON; notes/RESULTS_STATE.md','Splittings of a torsor-action extension give no direct implication for arithmetic fundamental-group sections or minimal-category results.',[99])
tsv('links.tsv',links,['kind','from','to','what','evidence','note_ids'])
tsv('project_leads.tsv',[a for a in links if a['kind']=='our projects'],['kind','from','to','what','evidence','note_ids'])

events=[];who='GPT-6 Astra Pro; effort not independently exposed; run SA23-20261119; owner bt'
def ev(s,t,o):events.append(dict(statement_id=s,date='2026-11-19',who=who,type=t,outcome=o))
background={32,47,53,55,56,57,58,59,60,62,63,64,65,70,71,72,85,89}
unknown={2,15,16,74,84,87}
refuted={10:9,12:13,14:13,28:29,42:41}
independent={3,4,8,9,13,19,20,23,24,25,26,27,30,31,39,45,51,73,75,76,77,78,79,80,81,82,83,86}
for n,c in by.items():
    if n in refuted:ev(c['id'],'refuted','Literal implication refuted by the explicit counterexample in computation/proof_checks; qualified or replacement statement: '+by[refuted[n]]['id']+'. '+c['computation'])
    elif n in unknown:ev(c['id'],'used and rechecked in this run','Typing/identifiability audit only, not a proof of the undefined claim. '+c['computation'])
    elif n in background:ev(c['id'],'carried as background without fault found','Exact theorem and scope used; no independent proof of the deep external input claimed. '+c['computation'])
    elif n in independent:ev(c['id'],'independent re-proof',c['computation'])
    else:ev(c['id'],'targeted proof check',c['computation'])
for n,block in {1:'characteristic_p_coefficient_check',9:'horizontal_arc_counterexample',10:'horizontal_arc_counterexample',12:'simultaneous_horizontal_obstruction',13:'endpoint_formula',14:'relative_closed_pullback',17:'characteristic_p_coefficient_check',28:'derived_Hom_counterexample',45:'determinant_cocharacter;positive_binomial_factor_sample',46:'simply_laced_classification_checks',51:'valuation_recurrence_example;strict_boundary_example',77:'H1_neutral_fibre_not_injectivity',86:'End_weight_decomposition'}.items():
    ev(by[n]['id'],'computation or formal certificate','Executed compute_checks.py; exact saved output block(s): '+block+'. Universal claims use the separate proof; finite experiments are not unrestricted proofs.')
for a in json.loads((P/'items.json').read_text()):
    ev(a['id'],'used and rechecked in this run','Note-to-transcription claim/scope comparison, not blanket proof certification: '+a['check']+'. '+a['check_reason'])
for a in json.loads((P/'reference_checks.json').read_text()):
    ev(a['key'],'carried as background without fault found','Bibliographic/source verification extent: '+a['locator']+'. '+a['checked'])
tsv('check_events.tsv',events,['statement_id','date','who','type','outcome'])
print(len(links),'links including',sum(x['kind']=='our projects' for x in links),'quarantined leads;',len(events),'check events')
# Preserve the final manually audited authorial/editorial separation on rebuild.
import runpy
runpy.run_path(str(P.parents[1]/'integration/apply_bt_spaces_problem_origins.py'))['apply_owner']('bt')
