"""Serialize manually authored close-reading decisions; never infer verdicts from headings.
Run from workspace root. Source indexing is used only to validate exact coverage.
"""
from pathlib import Path
import csv, json

OUT=Path('SA05/work/cote11b')
P='MPL_11_043-058+56'
PRO=f'sources/texts/pro/{P}_transcription.tex'
K4='sources/texts/codex/K11-04_transcription.tex'
B2='sources/texts/codex/B12-02_transcription.tex'
DATE='2026-11-19'
WHO='GPT-6 Astra Pro; inherited effort; SA05/cote11b'
items=[]; entries=[]; claims=[]; problems=[]; readings=[]; links=[]; events=[]; searches=[]; references=[]

def dump(name,data):
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def tsv(name,fields,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
def event(sid,typ,outcome):events.append(dict(statement_id=sid,date=DATE,who=WHO,type=typ,outcome=outcome))
def item(num,source_numbers,kind,cote,scans,lines,quote,statement,reconstruction,check,reason,verdicts=None,author='Alexander Grothendieck',source_file=PRO):
    sid=f'SA05-{2000+num}'
    sources=[f'{P}#{n}' for n in source_numbers]
    items.append(dict(id=sid,sources=sources,kind=kind,cote=str(cote),scans=scans,lines=[f'{source_file}:{lines}'],his_words=quote,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason,author=author))
    for j,n in enumerate(source_numbers):
        v=(verdicts or {}).get(n,'kept' if j==0 else 'merged')
        entries.append(dict(entry_id=f'{P}#{n}',item_id=sid,verdict=v,reason=reason))
    event(sid,'carried as background without fault found','Provenance and wording compared with the actual supplied passage; this event does not assert a proof. '+reason)
    return sid

item(1,[1,29,30],'other',11,[44,46,48],'20-46,82-177,213-253','On a de même les opérations sur les cycles',
     'The attached pages construct operations and correspondences; they contain no A–D list of standard conjectures. The notes report a draft C-to-published-B identification from cote16 and leave draft B/D unresolved.',
     'The C-to-B match is a contextual claim of the earlier run. The cited cote16 passages are not attached here; no exact draft-letter assertion is adopted.', 'not on the page',
     'No cited cote16 definition is present in this package. Retain the reported identification only as an unverified external lead, not a statement read in cote11.',{1:'corrected',29:'merged',30:'merged'})
item(2,[2,33],'unpursued implication',11,[46,48],'92-105,213-253','Il reste à vérifier',
     'For a suitable adequate cycle equivalence on smooth projective varieties, pull–multiply–push gives a correspondence category. Its additive idempotent completion with Tate twists has objects (X,e,m) and Hom((X,e,m),(Y,f,n))=f CH^{dim X-m+n}(X×Y)_Q e in the contravariant convention.',
     'The explicit Chow-motive formula, rational coefficients, idempotent completion and Tate inversion are the earlier run/current reconstruction; they are not all carried out on these sheets.', 'overstates',
     'The pages establish the correspondence construction and diagonal calculation, then leave axioms to check; they do not themselves perform the complete Chow-motive construction.',{2:'corrected',33:'merged'})
item(3,[3],'other',11,[44],'23-29','On suppose que la dualité de Poincaré vaut entièrement',
     'The initial example assumes full perfect Poincaré duality over the coefficient ring, without first quotienting torsion; coefficients are not required to form a field.',
     'This is a conditional algebraic hypothesis, not an assertion that every integral cohomology theory satisfies ordinary-module perfect duality.', 'agrees',
     'The words entirely and modulo torsion contrast are explicit. The Codex wording of the parenthesis differs but does not remove the hypothesis.')
item(4,[4],'other',11,[44],'25-27','pas des systèmes spéciaux',
     'The indicated numerical, homological, algebraic, Picard and Albanese quotients retain the operations being discussed; the text expressly does not assert specialness or Poincaré duality for all of them.',
     'The list is read under the equivalence relations for which the displayed operations descend; no universal nondegeneracy is inferred.', 'agrees',
     'The qualification in the transcription prevents promoting operation compatibility to full duality.')
item(5,[5],'other',11,[44],'29','K(X), placé en degré 0, et comme jauge χ',
     'The degree-zero K-theoretic example is equipped with the Euler-characteristic trace. Comparison with a cohomological trace via Chern character requires a Todd factor in Riemann–Roch.',
     'The Todd qualification is modern explanatory context, not a claim written on this sheet.', 'agrees',
     'Only K(X), its degree, and χ are stated. No uncorrected trace-preserving Chern-character comparison appears.')
item(6,[6],'self-flagged step',11,[44,46],'32-44,169-175','Il faudra choisir entre Cy et yC',
     'The correspondence action convention is still being chosen. Reordering homogeneous classes in a graded-commutative theory introduces the displayed Koszul signs.',
     'The exact convention must be fixed globally before an action/composition identity is asserted.', 'agrees',
     'The choice is explicitly unresolved on44 and both order-sensitive formulas are explored on46.')
item(7,[7,8,9],'self-flagged step',11,[46,48],'92-175,230-251','axiome cartésien oublié !',
     'With target-first notation A(I′;I), composition is integration over the middle factor of the product of the pulled-back correspondences. Projection formula and the requisite Cartesian base-change identity prove action compatibility, associativity and diagonal units in a suitable oriented theory.',
     'The general proof is supplied in the current commentary; the text proves the diagonal calculation but leaves associativity and units to verification. Line129 also drops a pushforward in one intermediate expression.', 'agrees',
     'The omitted Cartesian axiom is an authorial flag, and48 explicitly retains category axioms to verify. The concrete operations are present, not merely proposed.')
item(10,[10,19,28],'reading question',11,[51],'285-356','base',
     'The small-factor diagonal/point classes give natural spanning expressions. They are not a universally linearly independent basis: for X=P¹, Δ12=h1+h2. The two-factor table writes y1y2y3 and puts δ in H^n(X), both inconsistent with its ambient product.',
     'The P¹ counterexample is independently recomputed here. No supplied Lean certificate establishes the earlier Hua claim.', 'understates',
     'The notes correctly warn against universal independence; the actual two-factor table has two concrete target/index alarms. The earlier formalization claim remains documentary, not a proof checked here.',{10:'corrected',19:'merged',28:'merged'})
item(11,[11,20],'unproved claim',11,[51,57],'319-368,567-581','δ²=χ y1y2',
     'For a positive-dimensional oriented Poincaré space with normalized top class y, diagonal self-intersection is Euler class and the displayed two- and three-factor products follow. A four-factor P¹ loop product equals 2h1h2h3h4.',
     'General excess formulas require the smooth/oriented diagonal normal-bundle calculation; the P¹ check alone proves only that model. The four-factor computation is an earlier-run example redone here.', 'agrees',
     'The small tables and the still-questioned excess coefficient are distinguished. All stated small P¹ identities are recomputed.')
item(12,[12,16],'unproved claim',11,[53,57],'400-425,567-581','Relations',
     'The r-factor generators comprise point classes and diagonals for subsets, with the listed binomial counts. The general relations are not supplied; δ-subscript conventions shift from r+1 factors on53 to k factors on57.',
     'A presentation by partition diagrams would be a reconstruction. The empty relations heading is not itself a conjectured completeness theorem.', 'agrees',
     'The transcription ends the relations section before any list and uses the two different diagonal conventions.')
item(13,[13],'reading question',11,[55,57],'452-477,555-559','s=card R',
     'A partition includes an empty block. Its geometric equality locus has one free X-coordinate per nonempty block not constrained by the marking. For J empty its dimension is (card R−1)dim X, not card R dim X.',
     'The dimension correction is conditional on counting the mandatory empty block in card R, as the preceding definition does.', 'agrees',
     'The set membership of the empty block is explicit;57 uses a count that needs either exclusion of that block or correction.')
item(14,[14,15,17],'self-flagged step',11,[55,57],'480-508,567-581','OK !; χ ?',
     'The intersection of two equality loci is the locus for their joined equivalence relation; marked blocks become point constraints. When the constraints are transverse the cohomology classes multiply without excess. In the first redundant unmarked loop the excess factor is the Euler class and hence χ times a normalized point class.',
     'The general clean-intersection interpretation is current reconstruction. The source locally accepts the transverse case but keeps a question mark on the first excess coefficient.', 'agrees',
     'Set-theoretic intersection, transverse intersection class, and excess class are three different assertions; the passage does not collapse them.')
item(18,[18],'withdrawn in the same text',11,[57],'608-640','stable par ...; [cancelled paragraph]',
     'External products, selected coordinate pullbacks and pushforwards, and correspondence composition are proposed to preserve the generated system. A paragraph about extraordinary pullbacks is cancelled.',
     'Pro and Codex disagree on the exact words inside the cancellation and on a final cup/comp abbreviation; cancellation itself is common to both.', 'agrees',
     'Record the withdrawn extension separately from the surviving stability claims; no proof of closure under all extraordinary inverse images is supplied.')
item(21,[21],'self-flagged step',11,[43],'12-18','The proof is obvious',
     'In Mumford’s reused quotient-chart argument, the inverse image of an invariant open subset restricts an existing product PGL(n+1)×A_R to PGL(n+1)×B.',
     'This is a restriction of the established equivariant trivialization, not a new quotient theorem.', 'agrees',
     'The short corollary is actually on the page and depends on the preceding chart.',author='David Mumford (reused GIT typescript)')
item(22,[22,23,27],'self-flagged step',11,[43,45,47,49,52,54,56,58],'47-81,178-212,254-282,383-440,511-551,647-690','We leave to the reader the verification',
     'The R-partition charts normalize selected projective points by determinant coordinates and identify the indicated open set with PGL(n+1)×A_R. The two physical pagination chains contain absent pages3.5 and3.16. R-partitions of labels in the GIT chart are not the diagonal partitions on55.',
     'Missing pages prevent certifying the complete printed coordinate verification from this package alone. The GIT attribution follows textual continuity with Mumford, not a handwritten authorship inference.', 'agrees',
     'The deferred checks, determinant conditions and both missing pagination steps are read directly. No completion is invented.',author='David Mumford (reused GIT typescript)')
item(24,[24],'self-flagged step',11,[52,54],'387,433-440','The first part is clear',
     'The stable projective-configuration locus has the stated locally trivial PGL quotient; the line bundle descended from the chosen linearization is ample and the quotient is quasi-projective, under the GIT stable-locus hypotheses established in surrounding pages.',
     'This claim is restricted to that locus and chosen linearization, not an assertion about arbitrary free actions.', 'agrees',
     'The first part is compressed, and the proof of ampleness continues on52 with explicit EGA/SGA references.',author='David Mumford (reused GIT typescript)')
item(25,[25,26],'reading question',11,[56,58],'514-546,652-689','a linear functional ℓ',
     'The cone of ordered weights λ0≤⋯≤λm with sum0 is generated by the m step vectors vβ with first β+1 entries −(m−β) and last m−β entries β+1. Separating a point from a cone interior requires a nonzero functional; omitting nonzero makes the criterion false.',
     'The coefficient formula (λβ+1−λβ)/(m+1) is independently proved and checked. The zero-functional counterexample is current verification.', 'agrees',
     'The cone calculation follows the sorted-weight reduction. Both separation statements on58 omit an explicit nonzero condition.',author='David Mumford (reused GIT typescript)')
item(31,[31,32,35],'idea of the earlier run',11,[44,46],'32-44,92-105','γ_C',
     'Earlier-run context proposes hyperplane induction, universal operator projectors, and twist-bearing naturality g_{M(1)}L=Lg_M. These require their actual operators and source categories to be checked separately; twist naturality alone is not untwisted commutation.',
     'Cote16 and the named research context are not attached to this part. Current11 only directly supplies the correspondence action.', 'not on the page',
     'Retain the contextual maps as leads, with their missing endpoints explicit; do not promote them to read claims on44–46.',{31:'corrected',32:'merged',35:'merged'})
item(34,[34],'idea of the earlier run',11,[46,48],'92-105,230-251','composition des correspondances',
     'For rational adequate cycle equivalences, the homological-to-numerical quotient is a correspondence quotient. Jannsen proves numerical motives semisimple; his nilpotent-radical corollary for homological correspondences assumes algebraic Künneth components.',
     'This is later context, not an assertion of the current manuscript. Semisimplicity is not transferred wholesale to the homological category.', 'agrees',
     'The note’s distinction is mathematically necessary and is checked against Jannsen’s theorem and corollary.')
item(36,[36,37],'self-flagged step',56,[3,5],'710-739,799-867','spécialisation ?; action non triviale',
     'A flat projective one-parameter family has smooth generic quadric and one singular special quadric. The manuscript asks for specialization and describes parity-dependent vanishing cohomology and inertia. Nontrivial sign monodromy requires an ordinary quadratic smoothing without an even ramified base change; the listed hypotheses alone do not imply it.',
     'The regular-total-space/ordinary-smoothing hypothesis is a refinement introduced here. The family Σx_i²=t²x_n² over C[[t]] is a counterexample to the unrestricted nontrivial-monodromy assertion.', 'understates',
     'The specialization arrow and final purity line are visibly unfinished; the notes do not fully expose the missing monodromy hypothesis.',{36:'corrected',37:'merged'})
item(38,[38],'reading question',56,[7],'921-935','H^i(U1)=Φ^{i+1}',
     'The affine special cone is contractible in the complex model, so positive-degree cohomology vanishes. Identification with shifted vanishing cycles in degree0 must use reduced cohomology or retain the H⁰ term.',
     'The degree-zero repair is a mathematical alternative for scan checking, not an alteration of the diplomatic text.', 'agrees',
     'The long exact sequence and the unqualified displayed isomorphism cannot both be used literally at degree0. The X/U label also needs checking.')
item(39,[39,40,41],'reading question',56,[11,13],'1022-1057,1102-1130','ξ (ou −ξ ?)',
     'For the punctured affine cone E=O_X(−1)^× over a smooth connected projective complex X, the Gysin map is cup product with c1(O_X(−1))=−h. Contractibility of the full cone gives H_a^i(C)=\u007eH^{i−1}(E); H_a^0=H_a^1=0 when E is connected. Primitive quotients are here taken modulo torsion.',
     'The boxed target H*(X,C−a) probably needs H*(C−a), but ink has not been checked. The primitive convention is read literally.', 'agrees',
     'The explicit sign doubt, target mismatch and local-support calculation are all present; ordinary and reduced cohomology must be distinguished.')
item(42,[42,43,59,60],'reading question',56,[15,32],'1207-1224,1715-1736','Z/2Z',
     'For Q^D split smooth complex and E=O_Q(−1)^×, D odd gives H⁰=Z,H^{D+1}=Z/2,H^{2D+1}=Z. D even>0 gives Z in degrees0,D,D+1,2D+1. The odd table writes the torsion two degrees too low; the even table also writes its lower middle free group one degree too low. Hyperplane maps on32 yield the corrected degrees.',
     'The even-table correction is new in this consolidation. The full formulas follow from the integral Gysin sequence and verified quadric lattice.', 'understates',
     'The conic test confirms the odd error; Q²=P¹×P¹ confirms the additional even error. Both are alarms, not revised readings.',{42:'corrected',43:'merged',59:'merged',60:'merged'})
item(44,[44,45],'self-flagged step',56,[17],'1260-1268','H_a^*(C) ≃ H_c^*(C) ??',
     'The local-to-compact comparison is expected for the positively contracting cone. For weakly equivariant constructible complexes on a space contracted by G_m to its vertex, the contraction lemma gives the appropriate costalk-to-compact-cohomology comparison.',
     'Braden’s lemma applies after specifying the equivariant complex and ambient contraction; it is not an unrestricted assertion for arbitrary sheaves or any singular space.', 'agrees',
     'The author’s double question mark is retained. The earlier quadric-cone example is validated under explicit equivariance.')
item(46,[46,47,48,49,103],'self-flagged step',56,[20,22],'1294-1376,1401-1443','Je m’y perds ... à un signe près',
     'For the smooth complex affine quadric U of dimension D>0, ordinary cohomology is Z in degrees0,D and compactly supported cohomology in degreesD,2D. The natural middle map is multiplication by the oriented vanishing-sphere self-intersection, zero for odd D and ±2 for even D. The dimension-zero case must be separated. The Gysin induction has unfinished middle extension/duality slots.',
     'The sign is convention dependent until generator and orientation are fixed; the source’s positive2 alone is not automatically an error. Untwisted integral topology is a specialization of the source’s finite-coefficient setting.', 'agrees',
     'The endpoint exclusions and unfinished slots are real; they are not all resolved by counting Betti numbers. The author’s sign remark is itself a doubtful transcription.')
item(50,[50,51,57],'unproved claim',56,[24,30],'1503-1519,1671-1702','2φ=ξ^ν+λ^ν',
     'The middle lattice of Q^{2ν} has ruling basis α,β. Hyperplane h^ν=α+β and primitive λ=α−β span an index2 sublattice, with matrix [[1,1],[1,−1]], cokernel Z/2. Thus φ=(h^ν+λ)/2 can be integral without h^ν,λ being an integral basis.',
     'The matrix and Smith invariants are independently recomputed. The boundary/restriction multiplier2 uses the same sum/difference lattice once source normalizations are fixed.', 'agrees',
     'The displayed factor2 is meaningful integrally and must not be erased by passing silently to rational coefficients.')
item(52,[52],'reading question',56,[24],'1468,1491-1500','λ^{2ν}; Q2⊂Q1; ξ_i↦ξ_{i+2}',
     'The written primitive-generator index, direction of quadric inclusion, and pushforward shift conflict with adjacent source conventions. For a hyperplane inclusion Q^{D−1}→Q^D, pushforward raises codimension by1.',
     'The alternatives λ^ν, the reverse inclusion, and an index+1 shift are conditional on the codimension indexing used in the adjoining formulas.', 'agrees',
     'Each alternative is mathematical evidence for ink review; none is inserted into the source.')
item(53,[53,54,55,56,61],'reading question',56,[26,28,30,35],'1558-1593,1624-1633,1696-1702,1753-1773','λ^ν λ^ν=2ξ^{2ν}',
     'For Q^{2ν}, with λ=α−β in the two maximal-isotropic families, λ²=(−1)^ν h^{2ν}; hλ=0. Primitive λ restricts to the adjacent lower-dimensional quadric and pushes to the adjacent higher-dimensional quadric as0. The geometric cycle classes and Q⁰–Q⁶ ranks support these identifications.',
     'The λ-square sign is reconstructed using the explicit α−β convention, not inferred from a chosen abstract primitive generator. The phrase équivalence linéaire remains the source’s historical terminology.', 'understates',
     'The Q² calculation λ²=−2ab contradicts the uniform positive sign. Rank tables alone do not establish product signs.',{53:'corrected',54:'merged',55:'merged',56:'merged',61:'merged'})
item(58,[58],'reading question',56,[30],'1661','L(F)⊗L(G)=... ',
     'The faint tensor expression does not determine whether the symbol denotes a derived tensor construction. A contextual derived-functor interpretation from cote16 is a lead only.',
     'Neither the missing ink nor the unavailable cote16 endpoint is supplied by the current mathematical analogy.', 'agrees',
     'Keep the diplomatic uncertainty and avoid declaring an identification.')
item(62,[62],'title, date or page count',56,[2,9],'692-702,988-996','3 p | 30; 12 p',
     'Cover annotations can be reconciled with selected handwritten blocks, but the first number remains an uncertain reading and neither annotation dates the whole mixed package.',
     'The match to page blocks is an inference from the attached sequence, not a resolution of the ink.', 'agrees',
     'The heterogeneous physical package includes unrelated verso texts; cover counts cannot be applied to all its pages.')
item(63,[63,100,101],'idea of the earlier run',56,[20,30],'1342-1376,1671-1702','2',
     'Earlier-run links to WG H9, cote44, cote47, LM7_E23 and LM7_PUSHD44 relate local pairings, proper support, section classes or descent. Current supplied pages directly establish only the local quadric maps and correspondence operations.',
     'No global Néron pairing, derived Fourier transform, section-class solution or external referee status is inferred.', 'not on the page',
     'The external project passages are not attached; the links remain separately labelled leads, not checked two-endpoint results.',{63:'corrected',100:'merged',101:'merged'})
item(64,[64],'idea of the earlier run',11,[44],'25-27','Picard, Albanese',
     'For an abelian scheme A over a perfect field k of characteristic p, Oda identifies the contravariant Dieudonné module of A[p] with H¹_dR(A/k), compatibly with Frobenius/Verschiebung and the Hodge subspace. The notes associate this with an unavailable cote54 question.',
     'The theorem and its hypotheses are verified as later context; no cote54 source claim is treated as read.', 'not on the page',
     'The mere Picard/Albanese list on11/44 is not the missing comparison conjecture.',{64:'corrected'})
item(65,[65,66,67,104],'withdrawn in the same text',56,[4,6,8,18,33],'753-783,870-914,941-984,1278-1287,1744-1747','barré; Exp. XII; A. Grothendieck',
     'The cancelled SGA3 opening states semicontinuity of reductive/nilpotent/unipotent ranks, equivalence of locally constant reductive rank with local maximal tori, and local conjugacy. Surviving later sheets restate the program; the scheme-theoretic Chevalley advantage is a hope, not a proved structure theorem on8.',
     'Cancellation is editorial reworking, not evidence these mathematical results were abandoned. Borel/Chevalley are cited inputs, not new Grothendieck claims.', 'agrees',
     'The signature fixes authorship here. The revised sections and later published SGA3 locate the surviving results.')
item(68,[68,69,84],'self-flagged step',56,[12,14,33],'1061-1093,1176-1197,1744-1747','Il reste à vérifier ... de type fini',
     'For a smooth finitely presented group scheme satisfying the stated rank hypotheses, the maximal-torus functor is an open subfunctor of the torus functor and has smooth separated local representing schemes and étale local sections. The local finite-type check on14 is immediately supplied via a surjective orbit map G/N(T); the affineness proof is postponed and an alternative argument via finite torsion subtori is rewritten.',
     'These are distinct proof stages; affineness is not proved merely by the finite-type sentence.', 'agrees',
     'The notes rightly do not leave the locally finite-type check open after the following argument. Rewritten alternatives retain their cancellation status.')
item(70,[70],'unproved claim',56,[21,16],'1393-1397,1234','semi-continu',
     'For a separated quasi-finite étale group over a locally noetherian base, fibre order is lower semicontinuous; local constancy of the order gives local finiteness. The proof reduces to a trait and injects the special fibre group into the generic fibre after a suitable strictly henselian/completed reduction.',
     'The reduction hypotheses are retained; this is not a claim for arbitrary nonseparated étale spaces.', 'agrees',
     'The proof begins on21 and continues on16; source order must be restored before assessing its completeness.')
item(71,[71,102],'unproved claim',56,[16],'1236-1241','R⊂T deux tores',
     'The literal claim that W_G(R) is a subquotient of W_G(T) for any nested tori is false. For G=SL4(C), R has cocharacter (3,1,−1,−3), while T is the connected kernel in the diagonal torus of character (1,2,−7,4); then R⊂T, W_G(R)=C2 and W_G(T)=1. The usual proof works when T is maximal.',
     'The counterexample, all connectedness/centralizer/normalizer hypotheses, and the refined maximal-torus statement are checked in this run. Printed SGA3 XII2.3 retains the broad wording while its proof uses maximality.', 'agrees',
     'A genuine scope problem survives publication; this is not only a blank citation or generic warning about missing hypotheses.')
item(72,[72,73],'unproved claim',56,[18],'1285','G_m ... G_a',
     'Over R=Z_(3), Spec R[x,(1+3x)^{-1}] with law x⋆y=x+y+3xy is a smooth group whose generic fibre is G_m and special fibre G_a. This realizes the asserted possible drop in reductive rank.',
     'The explicit model is the earlier run’s construction, independently verified here; the manuscript only asserts existence.', 'agrees',
     'The localization, inverse −x/(1+3x), smoothness and both fibres are all necessary and have been checked.')
item(74,[74,75,80,85,105,106],'unproved claim',56,[14,18,25,29,33],'1163-1172,1278-1287,1532-1540,1646-1650,1744-1747','rang réductif localement constant',
     'A torus commuting with a maximal torus lies in it. Under the stated smooth finite-presentation and locally constant reductive-rank hypotheses, commutative/nilpotent fibres have the described unique/central maximal tori; conjugacy is étale local. For G⊃H⊃T with equal reductive ranks, maximality in G is equivalent to maximality in H. The zero-unipotent-rank locus is open. The converse existence over artinian bases or locally reductive groups is deferred to XIV.',
     'The inserted rank condition and forward-reference hypotheses are retained. The statements are separated into claims below rather than read as one general assertion.', 'agrees',
     'The amendments are mathematically substantive; their cancellation/replacement and the references to Borel/XI/XIV are visible.')
item(76,[76,77,78,79,82,83],'unproved claim',56,[23,27,31],'1456-1465,1601-1616,1710-1712','H∩G/Z⁰=0',
     'A reductive centre is a central multiplicative-type subgroup with the universal factorization property after base change. With affine-fibre hypotheses the fibrewise condition gives the universal one; affine algebraic groups over fields have such a centre. The centre of the quotient by the full reductive centre is trivial under the stated smooth connected hypotheses. A literal intersection formula on23 is ill-typed and some references/parts are absent.',
     'The expected intersection is H∩(G⁰/Z⁰)=1. Printed SGA3 provides the completed argument, but it is not backfilled into the unfinished source.', 'agrees',
     'The unfinished proof, affine-fibre insertion, blank references and changed forward-exposé numbering all need separate recording.')
item(81,[81],'unproved claim',56,[29],'1654-1656','N(T)/C(T)',
     'For a smooth algebraic group over a field and a maximal torus T, the Weyl quotient N_G(T)/C_G(T) is finite étale; its geometric points are the abstract geometric Weyl group and commute with field extension.',
     'The maximal-torus hypothesis is explicit here, unlike the problematic comparison lemma on16.', 'agrees',
     'The note matches the passage and helps identify the missing hypothesis in the earlier lemma.')
item(86,[86,87],'other',56,[36,37],'1787-1829,1842-1843','Q(A)',
     'For a field F of characteristic≠2, Delzant’s Q(F) is the Grothendieck–Witt ring of nondegenerate finite-dimensional quadratic forms, not the Witt ring. Diagonal rank-one forms generate it and the kernel of Z[F*/F*²]→GW(F) is generated by the binary isometry relations stated in the offprint.',
     'Modern GW notation is explanatory. Additive notation for square classes means multiplication of field elements, not addition in F.', 'agrees',
     'The monoid group completion and binary relation proof identify the exact object and prevent dropping the rank coordinate.',author='Antoine Delzant (1962 offprint)')
item(88,[88,96],'idea of the earlier run',56,[36,37,38],'1787-1829,1845-1877,1928-1933','J²/J³',
     'The rank-zero ideal J⊂GW(F) maps isomorphically to the fundamental ideal I⊂W(F), hence J^r→I^r. For d_a=⟨a⟩−1, the degree-two Stiefel–Whitney class of d_a d_b equals (a)∪(b), and J³ maps to zero in degrees≤2.',
     'The ideal identification and coefficient calculation are the earlier run/current reconstruction, not a formula explicitly proved in the offprint.', 'agrees',
     'Both are independently re-proved; they identify the actual map in Delzant’s question rather than a merely related invariant.',author='Earlier-run reconstruction of Antoine Delzant’s offprint')
item(89,[89,90,91,92],'reading question',56,[37,38],'1845-1893,1924-1926','Z × (1+Ĥ⁺)',
     'Delzant uses a filtered total-class ring retaining rank. Rank-one forms map to their Kummer classes; the construction is natural under field homomorphisms. The Clifford invariant is normalized relative to the same-rank unit form. If the displayed untilded target were read as omitting rank, injectivity would be false, e.g. ⟨1⟩ and ⟨1,1⟩ have identical positive classes.',
     'The interpretation of a typographical untilded target is a scan alarm; the final theorem expressly includes rank.', 'agrees',
     'The rank coordinate is defined on37 and needed in38. No rankless theorem is silently substituted.',author='Antoine Delzant (1962 offprint)')
item(93,[93],'unproved claim',56,[38],'1904-1926','rang ... classes de Stiefel-Whitney',
     'Over a number field, a quadratic form is determined by its rank and all cohomological Stiefel–Whitney classes. Local finite places use dimension, discriminant and Clifford invariant; at real places the total class recovers the number of negative squares through binary binomial coefficients, and Hasse’s principle globalizes.',
     'The offprint cites its local classification and Hasse inputs. Their use is checked with exact hypotheses, not reclassified as a new Grothendieck theorem.', 'agrees',
     'The proof’s division into nonarchimedean, real, and global steps and the retained rank are explicit.',author='Antoine Delzant (1962 offprint)')
item(94,[94,95,97],'conjecture',56,[38],'1928-1933','il serait intéressant ... injectif',
     'Delzant asks whether J²/J³→H²(F,Z/2) is injective and whether 2-torsion Brauer classes are sums of quaternion classes, for arbitrary fields of characteristic≠2. Identifying J²/J³ with I²/I³ and H² with Br(F)[2], these are settled by Milnor’s degree-two comparison and Merkurjev’s norm-residue theorem.',
     'The exact map comparison is independently checked; the questions belong to Delzant. The finite-field Kummer identification uses Pic(Spec F)=0.', 'agrees',
     'The later theorem matches the coefficient, characteristic and degree exactly, not just the broad quadratic-form subject.',author='Antoine Delzant (1962 offprint)')
item(98,[98],'title, date or page count',56,[36,38,39],'1780-1786,1935-1946','Antoine Delzant',
     'The mathematical offprint is Delzant’s 1962 Comptes rendus note, volume255 pages1366–1368, presented by Jean Leray at the session of10September1962; the following colophon is not another page of mathematics.',
     'Its physical presence in Grothendieck’s papers establishes preservation, not authorship by Grothendieck or a date for neighbouring manuscripts.', 'agrees',
     'The signature, session, pagination and colophon are directly read in the supplied offprint.',author='Antoine Delzant (1962 offprint)')
item(99,[99],'idea of the earlier run',56,[24,32],'1503-1519,1715-1736','2',
     'In Λ_Z(e1,f1,e2,f2), ξ=e1f1+e2f2 satisfies ξ²=2e1f1e2f2. This gives the same rank-one cokernel Z/2 as the conic hyperplane map; it does not identify the full quadric or correspondence algebra.',
     'The exterior model is the earlier run’s analogy, independently recomputed. No unseen external source is used to strengthen it.', 'agrees',
     'The common integer matrix is a precise local comparison; a global ring equivalence would overstate it.')
item(107,[107],'other','11,56',[],'1-1958','[documentary limits]',
     'The current sources permit the full close reading recorded here. Earlier-run hashes, Lean certificates, review freezes and external registers are not among the attachments and are not certified.',
     'Current computations and logs are saved separately and make no claim to reproduce missing prior execution environments.', 'agrees',
     'The reproducibility note is retained with its documentary limits; current checks are new events, not inherited certificates.')

# Codex leads receive items and claims, but deliberately no NOTES_INDEX verdict rows.
item(110,[],'title, date or page count',12,[117],'23-45','Le 27 Mars 1968; 17H45',
     'A secretary’s letter reports progress on typing corrections and stencil distribution. Its date applies to the letter, not to the whole motifs manuscript or the reused reflection text.',
     'The uncertain signature is not resolved to a named person.', 'agrees','Dated administrative evidence only.',author='Unidentified secretary/correspondent',source_file=B2)
item(111,[],'other',12,[121],'47-51','Solution ... λ-structure',
     'The report credits Deligne with exterior-power operations on perfect complexes, using Dold–Puppe, and the special λ-ring identities on K⁰. It expressly limits the theory then written to a base field of arbitrary characteristic.',
     'This is a report of Deligne’s work and its then-written scope, not a new unsolved conjecture of Grothendieck.', 'agrees','The historical description of the earlier open problem is not its current status.',author='Grothendieck reporting Pierre Deligne’s work',source_file=B2)
item(112,[],'unproved claim',12,[123],'54-56','prouvé par Deligne modulo ... Lefschetz',
     'The report describes degeneration of the Leray spectral sequence for smooth projective morphisms, conditional on fibre hard Lefschetz, with a Kähler analytic analogue and an intended application to twisted-coefficient Weil properties.',
     'The hard-Lefschetz hypothesis is retained; the truncated final applications paragraph does not formulate a full weights theorem.', 'agrees','Root owns the detailed Deligne literature merge; this item documents the actual conditional source statement.',author='Grothendieck reporting Pierre Deligne’s work',source_file=B2)
item(113,[],'other',12,[126,128,130,132,134,136,138],'59-202','§3. Groupes engendrés par des réflexions',
     'The reused sheets develop finite real reflection groups: essential reduction, chamber-wall generators, pair angles, simple-root basis, Coxeter presentation, simple transitivity on chambers, positive-root and stabilizer corollaries. They then start properly discontinuous affine reflection groups, orthogonal product reduction and local finiteness of mirrors.',
     'Textual correspondence strongly identifies Bourbaki’s reflection-group development; the sheets do not explicitly name an author or date. Number383 is not sufficient to identify a seminar exposé. Attribution remains qualified until the archival typescript is matched.', 'agrees','The seven text pages III-1..7 are in reverse physical order and not Grothendieck’s original motifs claims.',author='Reused Bourbaki-type collective typescript; exact document attribution not verified',source_file=B2)
item(114,[],'reading question',12,[130,136],'104,158','composantes connexes de la réunion; cos(e′i,e′j)=cos(π/mij)',
     'Chambers must be components of the complement of the union of mirrors. The asserted equality for angles of the dual basis is false in rank3: for A3, m13=2 but the dual-vector cosine is1/3. The corollary that chamber vectors have nonnegative inner product remains correct by inverse-Gram positivity.',
     'Both corrections are new mathematical alarms. No ink is changed. The cosine identity may be a typescript error rather than a transcription error.', 'understates','The Codex notes omit these two mathematical issues; the supplied prose and formula require them.',author='Reused Bourbaki-type collective typescript; exact document attribution not verified',source_file=B2)

def flush_stage1():
    dump('items.json',items)
    tsv('entries.tsv',['entry_id','item_id','verdict','reason'],sorted(entries,key=lambda x:int(x['entry_id'].split('#')[1])))
    tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
    expected={r['entry_id'] for r in csv.DictReader(open('sources/notes/NOTES_INDEX.tsv'),delimiter='\t') if r['package']==P}
    actual=[r['entry_id'] for r in entries]
    assert len(actual)==107 and set(actual)==expected and len(set(actual))==len(actual)
flush_stage1()

# Bibliographic identity agrees with the supplied diplomatic reading.
event('SA05-2098','used and rechecked in this run','Final source recheck at56/036 line1785 corrected our draft first-name error: the supplied text reads Antoine Delzant. The source SHA256 is unchanged. Exact title/year/pages match Laborde1976 and the identity is corroborated by the ENS memorial; no first-name scan alarm remains.')

def claim(n,its,cote,scans,lines,his,modern,status,computation,cls,fate,date,now,refs,confidence='high',author='Alexander Grothendieck',family='correspondences',source_file=PRO):
    cid=f'SA05-C{2000+n}'
    claims.append(dict(id=cid,items=[f'SA05-{2000+i}' for i in its],cote=str(cote),scans=scans,
       lines=[f'{source_file}:{lines}'],his_statement=his,statement=modern,status_on_pages=status,
       computation=computation,**{'class':cls},fate=fate,fate_date=date,present_status=f'As of {DATE}: {now}',
       refs=refs,confidence=confidence,author=author,search_family=family))
    event(cid,'carried as background without fault found','Source statement and page status read directly. '+status+'. Literature extent is specified in search_log/reference_checks; no proof is claimed by this provenance event.')
    return cid

claim(1,[3,4],11,[44],'23-27','Full Poincaré duality; cycle quotients have the indicated operations but are not special.',
 'A finite projective graded coefficient module with a perfect trace pairing is a Poincaré algebra over its coefficient ring. Compatible cycle quotients inherit pullback/product/proper pushforward only for the equivalences for which those operations descend; perfect duality is not asserted for every quotient.',
 'stated without proof','No numerical computation. Conditional hypotheses checked; no claim that arbitrary integral cohomology is free.','B',
 'Modern correspondence formalism separates operation compatibility from duality; Stacks45.3 and Jannsen’s adequate-equivalence framework match that distinction. The brief Picard/Albanese names alone do not identify a new general theorem.',
 'Jannsen publication1992; source first circulation not determined','Valid as conditional examples; do not infer nondegeneracy for all listed equivalences.', ['StacksCorr','Jannsen1992'])
claim(2,[5],11,[44],'29','K(X) in degree0, with gauge χ.',
 'For smooth projective X, K₀(X) has Euler-characteristic functional χ(X,−). Under Chern character its cohomological integral is ∫ch(−)Td(T_X), not ∫ch(−) without the Todd class.',
 'stated without proof','Trace formula checked against Riemann–Roch statement; no source numerical example.','A','Grothendieck’s Riemann–Roch formalism supplies the Euler trace; no stronger Chern-character assertion is on this page.','1957 original Riemann–Roch proof (as dated in SGA6 contents); SGA6 publication1971','Established example, with the Todd correction when comparing traces.',['SGA6Front','StacksHRR'],family='Ktheory')
claim(3,[7],11,[46],'92-105','A(I′;I), composition by pullback, multiplication and projection.',
 'For smooth projective X,Y,Z over a field and rational cycles modulo a compatible adequate equivalence, β∘α=(pXZ)_*(pXY*α·pYZ*β). In the manuscript’s target-first order, the factors are correspondingly reversed.',
 'proof sketched','outputs/proof_notes.md §1; outputs/checks.json P1_correspondence_composition checks16basis products.','A','The same correspondence algebra underlies Grothendieck1969 §1 and later Chow motives; Stacks45.3 spells out the operations.','Published1969; exact draft date not identified','Established with stated push–pull axioms and convention.',['GrothStandard1969','StacksCorr'])
claim(4,[6,7],11,[44,46],'32-44,119-175','Choose Cy or yC; action of a composite.',
 'For homogeneous correspondences in a graded-commutative oriented theory satisfying Künneth, projection formula and Cartesian base change, pull–multiply–push intertwines correspondence composition with composition of operators, with the Koszul sign dictated by the chosen ordering.',
 'proof sketched','outputs/proof_notes.md §1; the source’s line129 requires the omitted outer pushforward.','B','The modern cycle/correspondence compatibility is explicit in Stacks45.3.1; the graded version is a formal signed extension, not a separate theorem located by title search.','Modern reference checked2026; first circulation not established','Valid after globally fixing grading/order; source calculation has a target alarm.',['StacksCorr'],family='correspondences')
claim(5,[7],11,[48],'230-247','The diagonal gives the identity action.',
 'For smooth projective X in the same oriented theory, Δ_X acts as id on H*(X); the formula is the projection formula for Δ followed by p∘Δ=id.',
 'proved there','outputs/proof_notes.md §1; P1 matrix identity checked exactly.','A','Grothendieck’s published correspondence formalism and Stacks45.3.3 use the diagonal unit.','Publication1969; earlier origins not dated here','Established; the text supplies the essential calculation.',['GrothStandard1969','StacksCorr'])
claim(6,[7],11,[48],'251-253','Il reste à vérifier ... associativity and units.',
 'Associativity and both diagonal unit laws hold for the correspondence composition of C2003 under projection and Cartesian base-change identities.',
 'open on the pages','Independent four-factor re-proof outputs/proof_notes.md §1;64basis triples in P1 model.','B','Stacks45.3.1 and45.3.3 give the exact category statement.','Modern statement checked2026; not claimed first publication','Closed by the standard push–pull proof; the page itself leaves the check open.',['StacksCorr'])
claim(7,[11],11,[51],'291-356','y_i²=0; Δ_ij²=χy_iy_j; Δ12Δ23=δ123; δ123²=0.',
 'For connected smooth projective complex X of positive complex dimension d, rational cohomology, normalized y∈H^{2d}(X) and consistently oriented diagonal classes, all displayed2/3factor identities hold, including δ123·y_i=y1y2y3 and Δij·δ123=χ(X)y1y2y3.',
 'stated without proof','All source small tables recomputed forP1 in checks.py; general derivation via diagonal normal bundle in proof_notes.md §2.','B','Self-intersection/excess and Poincaré–Hopf explain the exact χ coefficient. Searches located the standard correspondence/excess formalism, not a publication of this exact table.','Classical ingredients; exact first occurrence of table not established','True in the stated cohomological setting; not evidence of linear independence.',['StacksSelfIntersection','FultonExcess','MOEulerLead'],family='diagonals')
claim(8,[10],11,[51],'319-368','The listed classes are a base.',
 'Universal linear independence of the displayed classes for all smooth projective X satisfying Künneth/Poincaré duality is false.',
 'false as stated','X=P1(C) satisfies every stated geometric and cohomological hypothesis; Δ12=h1+h2 in Z[h1,h2]/(h1²,h2²). See checks.json P1_tables and proof_notes.md §2.','C','Projective-bundle calculations give an explicit counterexample. A universal formal diagram algebra may have a basis before realization, but no such formal algebra is constructed on this page.','Counterexample recomputed2026; projective-bundle formula is classical','Retain spanning/generating formulas; separate formal universal objects from realized cohomology.',['StacksProjectiveBundle'],family='diagonals')
claim(9,[12],11,[53],'400-425','General diagonal generators; Relations [empty].',
 'For X^r, take r point classes and one small diagonal for each subset of cardinality≥2, with binomial counts by subset size. These generate the defined tautological subalgebra; a complete ideal of relations is not stated.',
 'open on the pages','Combinatorial count C(r,s) by choosing subsets; no numerical specialization replaces a missing relation ideal.','C','Standard diagonal/excess methods establish many relations. Recorded searches did not identify this exact all-X presentation or prove that the listed small relations are complete.','Search as of2026-11-19; no first-publication claim','Generators are clear; complete universal kernel depends on cohomological realization and remains unspecified here.',['StacksSelfIntersection','FultonExcess'],family='diagonals')
claim(10,[13],11,[55,57],'452-477,555-559','∅∈R; dimZ_R=sn with s=cardR.',
 'If a partition includes the empty block and J is empty, Z_R≅X^{s−1}, so dimZ_R=(s−1)dimX. More generally count unmarked nonempty blocks.',
 'false as stated','Direct coordinate isomorphism; forI={1},R={∅,{1}}, source s=2 butZ_R=X, notX². Every partition axiom on55 holds.','C','The correction is elementary and consistent with diagonal geometry; no literature result is needed to repair the count. Exact heading searches yielded no source-specific erratum.','Refutation2026-11-19','Repair the counting convention; preserve source reading for scan review.',['StacksCorr'],family='diagonals')
claim(11,[14],11,[55,57],'480-508,567-568','Intersection by joined partition; transverse case markedOK.',
 'Equality constraints for partitions intersect in the locus of the joined equivalence relation; point constraints propagate to the joined blocks. If these smooth embeddings are transverse, the product of fundamental classes is that intersection class.',
 'proof sketched','Coordinate-equality proof and tangent-space rank count in proof_notes.md §2. Source s+s′=k+1 uses nonempty block counts and a connected join.','B','Standard transverse-intersection formalism establishes the claim once the source’s block count is corrected.','Classical; exact manuscript-specific publication not identified','Established under the explicitly reconstructed transversality/counting hypotheses.',['FultonExcess'],family='diagonals')
claim(12,[14,11],11,[57],'569-581','k=s+s′ gives χ?; larger excess vanishes by degree.',
 'For a connected join of two unmarked diagonal partitions of k factors, with nonempty block counts s,s′, the excess bundle is T_X^{⊕(k+1−s−s′)}. Excess0 gives the small diagonal; excess1 gives χ(X) times the point class; excess≥2 vanishes in ordinary cohomology fordimX>0.',
 'open on the pages','Independent normal-bundle proof §2; four-factorP1 loop product2h1h2h3h4 saved.','B','Clean/excess intersection proves this precise refinement. The source retainsχ? and does not spell out the excess bundle.','General excess formalism later published in Fulton; exact first appearance not claimed','Closed for smooth oriented cohomological realization; Chow coefficients require c_d(T_X), not automaticallyχ times a chosen point.',['FultonExcess','StacksSelfIntersection'],family='diagonals')
claim(13,[18],11,[57],'608-640','Stable par⊠, coordinate pullbacks/pushforwards; stable parcomp.',
 'The subspaces generated by marked diagonal classes in cohomology are stable under external products, coordinate permutations/projections and the resulting correspondence compositions, provided integration and the point/Euler normalization are available. The separately cancelled extraordinary-pullback extension is not claimed.',
 'proof sketched','Proof_notes.md §2 explains forgetting a constrained/free coordinate and top-degree integration; closure follows from preceding product rule.','B','Modern push–pull formalism supplies these operations. Search found no justification for restoring the cancelled assertion under arbitrary extraordinary pullbacks.','Established formal closure; source-specific date unknown','Valid within the stated generated system and selected maps; cancellation retained.',['StacksCorr','FultonExcess'],family='diagonals')
claim(14,[2],11,[46,48],'92-105,230-251','Correspondence construction (completion not carried out here).',
 'For rational Chow correspondences, pass to finite sums, split every idempotent e and add Tate twists. The identity of(X,e,m)is e and an idempotent q=eqe splits as(X,q,m).',
 'stated without proof','Independent algebraic splitting in proof_notes.md §1; reconstruction expressly attributed to this run/earlier notes.','B','Stacks45.4 gives the completed Chow-motive category.','Modern reference; early motive constructions1960s, exact first circulation not fixed here','Established construction; these sheets do not themselves complete it.',['StacksMotives'],family='correspondences',author='Earlier-run/current reconstruction from Grothendieck’s correspondence sheets')
claim(15,[34],11,[46,48],'92-105,230-251','Later context: numerical quotient and semisimplicity.',
 'For a fieldk and coefficient field of characteristic0, the category of pure motives modulo numerical equivalence is semisimple abelian. For homological equivalence with algebraic Künneth projectors, the kernel on each correspondence endomorphism algebra is its nilpotent Jacobson radical.',
 'stated without proof','Theorem1 andCorollary1 ofJannsen read; proof not independently reproved.','B','Jannsen1992 Theorem1 andCorollary1 exactly distinguish numerical semisimplicity from the conditional homological kernel statement.','Received1991-07-12; published1992; receipt is not asserted to be first circulation','Established with the algebraic-Künneth qualification in the corollary.',['Jannsen1992'],family='motives',author='Uwe Jannsen; later context, not manuscript assertion')
claim(16,[21],11,[43],'12-18','Corollary3.2: invariant open restriction of product.',
 'Under the R-chart equivariant isomorphism U_R≅PGL(n+1)×A_R, every invariant open U⊂U_R equalsPGL(n+1)×B for the openB obtained by restricting the slice.',
 'proof sketched','Direct argument: invariant open membership is constant alongPGL orbits; pullback along identity slice is open.','B','MumfordGIT chapter3 Corollary3.2 retained in opened1982 text.','GIT first edition1965, checked reproduction1982; draft circulation not determined','Established; attribution is Mumford.',['MumfordGIT1982','MumfordGITPublisher'],author='David Mumford (reused typescript)',family='GIT')
claim(17,[22],11,[45,47,49],'53-81,184-212,260-281','The mapsφ andψ are inverse; R-partition chart.',
 'For an R-partition of the specified index set satisfying its connectivity/nonvanishing determinant conditions, normalizing the distinguished projective frame and the listed coordinates gives an equivariant isomorphismU_R≅PGL(n+1)×A_R, withA_R the explicit affine slice.',
 'proof sketched','Source inverse-map checks are deferred; independent frame normalization proof in proof_notes.md §3. Missing typepage3.5 not supplied.','B','OpenedGIT1982 chapter3 Proposition3.1 andCorollary3.2 contain the corresponding chart; OCR limits exact formula collation.','First book1965; checked2ndedition1982; first circulation of this typescript unknown','Established underR-partition and invertible-minor hypotheses. Exact manuscriptψ/φ reading remains undecided.',['MumfordGIT1982','MumfordGITPublisher'],author='David Mumford (reused typescript)',family='GIT')
claim(18,[22,25],11,[56,58],'514-546,652-689','Monomial degrees/cone criterion and greedy flag argument.',
 'For a projective configuration, the determinant monomials nonvanishing at the point define a cone of multi-degrees. Membership of the positive target multi-degree in its interior is equivalent to the required nonvanishing monomials in all coordinate directions, and separation reduces failure to sorted zero-sum weights. The greedy independent-set algorithm realizes the minimum determinant weight along the associated flag.',
 'proof sketched','Sorted cone coefficients checked symbolicallym=1..8; general difference proof in§3. Greedy flag proof checked by exchange argument. The final3.16typepage is absent.','B','The openedGIT1982 Proposition3.6/Corollary3.7 proof chain gives the same stability mechanism; separation requiresℓ≠0.','1965firstedition;1982textchecked','Established after the separating-functional correction; source proof chain alone is physically incomplete.',['MumfordGIT1982'],author='David Mumford (reused typescript)',family='GIT')
claim(19,[24],11,[52,54],'387,433-440','Theorem3.8: geometric quotient, locally trivialPGL bundle, ample descended line.',
 'For the stable configuration openU_stable⊂(P^n)^{m+1} defined by the text’s linearization, there is a geometric quotientZ₀; U_stable→Z₀ is a Zariski locally trivial principalPGL(n+1)-bundle and the descended tensor-product polarization is ample, soZ₀ is quasi-projective.',
 'proof sketched','Descent proof read in continuation52 and correspondingGIT1982 pp76–77; no separate computation.','B','MumfordGIT Theorem3.8 is an exact match, including principal-bundle and ampleness conclusions.','1965firstedition; checked1982edition','Established; do not generalize to arbitraryGITstable actions without checking stabilizers.',['MumfordGIT1982','EGAII'],author='David Mumford (reused typescript)',family='GIT')
claim(20,[25],11,[58],'668-689','Extreme rays of ordered zero-sum weights.',
 'For m≥1, λ0≤⋯≤λm andΣλi=0, λ=Σβ=0^{m−1}((λβ+1−λβ)/(m+1))vβ, wherevβ hasfirstβ+1entries−(m−β),remainingm−βentriesβ+1.',
 'proof sketched','checks.json ordered_weight_cone and general successive-difference proof in§3.','B','The cone decomposition is the elementary ordered-weight step inMumford’s stability proof; no independent later novelty is claimed.','Source typescript undated;GIT1965/1982','Exact formula established for allm by telescoping differences.',['MumfordGIT1982'],author='David Mumford (reused typescript)',family='GIT')
claim(21,[25],11,[58],'652-668,676-689','A separating linear functionalℓ [nonzero omitted].',
 'For a full-dimensional closed finitely generated convex coneC, x∉intC iff some nonzero real linear functionalℓ is nonnegative onC and satisfiesℓ(x)≤0. In lower-dimensional ambient spaces, use relative interior and the appropriate quotient.',
 'false as stated','C=R²_{≥0},x=(1,1)∈intC,ℓ=0 satisfies the literal weak inequalities. Full-dimensional hypotheses checked.','C','The standard separation theorem repairs the omission;GIT’s argument requires a genuine separating weight.','Elementary correction recomputed2026','Insert/checkℓ≠0; additional relative-interior qualification is needed if the cone does not span.',['MumfordGIT1982'],author='David Mumford (reused typescript)',family='GIT')

claim(22,[36],56,[3,5],'725-739,799-867','Specialization kernel/cokernel; Φ only in degreen.',
 'For a proper flat family over a strictly henselian trait, smooth generic fibre and a special quadric with a single ordinary quadratic singularity, the specialization sequence is the vanishing-cycle long exact sequence. WithD=n−1 and appropriate prime-to-residue-characteristic coefficients, the sole local vanishing-cycle degree isD; the sourceΦ convention shifts it to n.',
 'open on the pages','Source’s even/odd rank comparison checked against integralquadric lattice; primitive λ need not generate the integral cokernel unless2is inverted.','B','DeligneWeilI §4.2–4.4 states specialization under regular-total-space hypotheses. SGA7II XII/XV located inpublisher metadata; full theorem text not retrieved there.','SGA7seminar1967–69;publication1973;WeilI1974','Established in the standard ordinary-quadratic setting; degree convention and2-torsion must be explicit.',['DeligneWeilI','SGA7II'],family='quadrics')
claim(23,[36],56,[5],'829,867','For n odd, inertia acts nontrivially onΦ^n.',
 'Under the source’s stated flat/projective/singular-special/smooth-generic assumptions alone, nontrivial inertia is false. For a regular ordinary quadratic smoothing withD=n−1 even and coefficient characteristic≠2, the vanishing line has the quadratic sign character; D odd gives trivial action on the vanishing cycle.',
 'false as stated','Ramifiedfamilyx0²+x1²+x2²=t²x3² overC[[t]] satisfies all listed assumptions but is generically constant; checks.json records every hypothesis.','B','DeligneWeilI §4.2 explicitly requiresXregular and §4.3 describes the parity characters. The source drops this necessary control on ramification.','Published1974;SGA7II1973metadata verified','False in written generality; regular ordinary-smoothing refinement established.',['DeligneWeilI'],family='quadrics')
claim(24,[38],56,[7],'921-935','Affinecone has no higher cohomology; H^i(U1)=Φ^{i+1}.',
 'OverC, an affine coneC is contractible andH⁰(C,Z)=Z. For its smooth affine quadric deformationU, reduced cohomology—not unmodifiedH⁰—fits the shifted vanishing-cycle identification.',
 'false as stated','The degree0unit survives; forUconnectedH⁰(U,Z)=Z, while reducedH⁰=0. Explicit sphere model inproof_notes.md §4.','B','Ordinary quadratic vanishing-cycle theory inDeligneWeilI §4 verifies the reduced/local formulation; no generalH⁰vanishing is asserted there.','Publication1974; topology classical','Keep the H⁰term or use reduced cohomology.',['DeligneWeilI'],family='quadrics')
claim(25,[39],56,[11],'1022-1057','Cone contractible; Gysinξ(ou−ξ?); boxed target.',
 'For smooth projective complexX, the complementEof the cone vertex isO_X(−1)^×. The Gysin long exact sequence has cup mapc₁(O_X(−1))=−h and computesH*(E), not the ill-typed boxed relative target.',
 'open on the pages','Line-bundleGysin proof§4; sign follows fromdualityO(1)↔O(−1).','B','Classical self-intersection/Gysin formalism supplies the sign and exact sequence; same input used in later quadric cohomology.','Classical ingredients; earliest exact cone computation not dated','Resolved mathematically under stated topology; scan reading remains open.',['StacksSelfIntersection','KarpenkoQuadrics'],family='quadrics')
claim(26,[39],56,[13],'1102-1130','Primitive groups modulo torsion; H_a⁰=H_a¹=0.',
 'For a connected positive-dimensional projective complexX with connectedE=O_X(−1)^× and contractible coneC, H_a^i(C,Z)≅\u007eH^{i−1}(E,Z). In particular the low groups0,1vanish. The source defines its primitive quotients after discarding torsion.',
 'proof sketched','Long exact sequence of pair(C,E), withunitH⁰(C)→H⁰(E)an isomorphism.','B','This is standard local-cohomology/topological-pair formalism, compatible with the contraction comparison; the primitive quotient’s exact historical notation is not modernized.','No exact first publication established','True with connectedness and positive-dimensional base; dimension0requires separate treatment.',['Braden2003'],family='quadrics')
claim(27,[42],56,[15,32],'1207-1211,1732-1736','Oddquadricpuncturedcone torsion in2ν−2.',
 'ForQ^{2ν−1}overC,ν≥1, E=O_Q(−1)^×, integralH*isZindegrees0,4ν−1andZ/2indegree2ν. WithZ_ℓcoefficients the torsion survivesonlyℓ=2; finite2-primarycoefficients add the adjacent kernel group.',
 'false as stated','Full integralGysinmatricesD=1..8saved;Q¹=P¹withO_Q(1)=O_P¹(2)givesH²(E)=Z/2,H⁰(E)=Z.','B','KarpenkoTheorem1.10 gives the exact integralquadric lattice;Gysin yields corrected torsiondegree.','KarpenkolectureNov2003; laterexpositionnotfirstdiscovery','Literal degree false; refinement computed. Coefficientμ/M unresolved.',['KarpenkoQuadrics','StacksSelfIntersection'],family='quadrics')
claim(28,[42],56,[15,32],'1220-1224,1715-1729','Evenquadricpuncturedcone groups in2ν−1,2ν+1.',
 'ForQ^{2ν}overC,ν≥1, E=O_Q(−1)^×hasfreeintegralcohomologyindegrees0,2ν,2ν+1,4ν+1. The source’s lower middledegree2ν−1must be2νin this interpretation.',
 'false as stated','Q²=P¹×P¹: cup byh sendsZ→Z²by(1,1), thenZ²→Zby(1,1). ThusH²(E)=Z,H³(E)=Z. MatricesandallD≤8saved.','B','The verified integralquadric ring plusGysin supplies the exact correction; not previously isolated bythe notes.','Currentrefutation2026; ingredientstextchecked2003lecture','False written degree; corrected formula established.',['KarpenkoQuadrics'],family='quadrics')
claim(29,[44],56,[17],'1260-1268','H_a*(C)≃H_c*(C)??',
 'For a positivelyG_m-contracted affine coneCwithfixedvertexa and a weaklyequivariantconstructible complexF, the natural contraction comparison identifiesi_a!F withRΓ_c(C,F), underthe coefficients allowed inBraden’ssetup.',
 'open on the pages','BradenLemma6hypotheses checked by embeddingCinA^Nandapplyingthe lemma to theclosedpushforwardofF; proof_notes.md §4.','B','Braden2003 Lemma6 gives the applicable contraction lemma.','arXivfirstsubmission2002-02-24;publication2003','Established withweak equivariance; no arbitrary-sheafgeneralization.',['Braden2003'],family='quadrics')
claim(30,[46],56,[20,22],'1300-1337,1405-1443','Ordinary/compactcohomologytable foraffinequadrics.',
 'ForU={Σ_{i=0}^D z_i²=1}⊂C^{D+1},D>0, H^*(U,Z)=Zindegrees0,D; H_c^*(U,Z)=ZindegreesD,2D. D=0is twopointsandcannot beinsertedinto repeated-indexrows.',
 'proof sketched','Explicit identificationU≅TS^Danddeformationretraction;Poincaréduality. Integralresulttensoringfinitecoefficientsis validherebecausegroupsfree.','B','The quadrics chapterofSGA7IImatches thetopic; actual latercohomological computation checkedusingKarpenko’sringandtheGysinsequence.','SGA7II1973metadata; classicaltopology','Tables are correct afterendpointseparation and consistentdimensionnotation.',['KarpenkoQuadrics','SGA7II'],family='quadrics')
claim(31,[46],56,[20,22],'1339-1342,1413-1443','Compact-to-ordinary map hasmiddlecoefficient2.',
 'For the complexaffinequadricUofevencomplexdimensionD=2ν,the middlecompact-to-ordinarymap identifieswithvanishing-sphereself-intersection(−1)^ν2aftercanonicalcomplexorientationandcompatiblegeneratorchoice;forDoddthe mapiszero.',
 'open on the pages','TS^DdescriptionandEulerclassgiveabsolutevalue2/0;Q²λ²=−2computesfirsteven sign.','B','DeligneWeilI §4.1–4.3 explicitly relates vanishingcycles andsignedself-intersection; source’sabstract2mayabsorborientation.',
 'Published1974; priorSGA7II1973','Magnitude/parityestablished; sourcegenerator/twistsmustbefixedbeforecallingitspositive2false.',['DeligneWeilI'],family='quadrics')
claim(32,[46,53],56,[20,22,28],'1347-1376,1401-1443,1624-1633','InductionviaGysinsequences; middleextensionunfinished.',
 'ForhyperplaneQ^{D−1}⊂Q^DandsmoothaffinecomplementU^D, thelocalization/GysinsequencecomputesfreeevencohomologyofQ^D,rank2onlywhenDevenanddegreeD; oddcohomologyvanishes. Themiddleextensionisfree,soit splitsasgroups,notcanonicallyasallgeometricdata.',
 'proof sketched','AllLmatricesD≤8andQ0..Q6ranks checked;Q0hasrank2inH0. Sourceunfinisheddual/even slotsnotfilleddiplomatically.','B','KarpenkoTheorem1.10 anditscellularbasisgive theexactlattice andresolveextensionrankambiguity.','Nov2003lectureischeckedexposition,notfirstcirculationoftheclassicalresult','Establishedcohomology; choicesofdualitymapsstillrequireconventions.',['KarpenkoQuadrics'],family='quadrics')
claim(33,[50],56,[24,30],'1503-1519,1671-1702','Index2[h^ν,λ];2φ=h^ν+λ.',
 'InH^{2ν}(Q^{2ν},Z), rulingclassesα,βformabasis,h^ν=α+β,λ=α−β; thepair(h^ν,λ)hascokernelZ/2andα=(h^ν+λ)/2isintegral.',
 'proof sketched','ExactSmithnormalformandmatrixinverse saved;image paritychecked.','B','KarpenkoTheorem1.10andproof give thetwo rulingclasses andintegralrelation.','2003checkedexposition; classicalresult','Established; rationalizationlosestheindex2data.',['KarpenkoQuadrics'],family='quadrics')
claim(34,[53],56,[26,30],'1564,1696-1702','λ²=+2ξ^{2ν}.',
 'Withλ=α−βonQ^{2ν}andh^ν=α+β, λ²=(−1)^νh^{2ν}; hλ=0. A uniformpositiveλ-squareisfalse.',
 'false as stated','Q²=P¹×P¹,λ=a−b,h=a+b,a²=b²=0: λ²=−2ab,h²=2ab. Allhypothesescheckedin§4.','B','KarpenkoTheorem1.10statesruling-self-intersectionparity,matchingthissignedrefinement.','Currentrefutation2026;2003primarylecturechecked','Correctwithparitysign; sourceinknotchanged.',['KarpenkoQuadrics'],family='quadrics')
claim(35,[53],56,[26],'1575-1593','λis effaçable andévanescente.',
 'TheprimitiveλinmiddlecohomologyofQ^{2ν}restrictsto0onQ^{2ν−1}andpushesforwardto0onQ^{2ν+1}; bothmapskillthe differenceofrulingclasses.',
 'stated without proof','HyperplaneLmaps andsum/differencebasisverifykernels; generaldegree/pairingargumentin§4.','B','TheintegralquadricrulingbasisinKarpenkoTheorem1.10identifiesthe mapswithoutusingthe ambiguouswordsalone.','Classical;checkedexposition2003','Established; codimensionpushforwardshiftis1.',['KarpenkoQuadrics'],family='quadrics')
claim(36,[42],56,[32],'1715-1736','Hyperplaneinjections/surjections andorder2cokernel.',
 'ForQ^{2ν}, multiplicationh: H^{2ν−2}→H^{2ν}hasmatrix(1,1)^t andh:H^{2ν}→H^{2ν+2}hasmatrix(1,1); outside these places theinteriorrank1mapsareisomorphisms. ForQ^{2ν+1}, thecentralrank1mapismultiplication2.',
 'stated without proof','MatricesD=1..8,Smithcokernelsandkernelsrecomputed; formulaestablishedforallDusingcellbasis.','B','KarpenkoTheorem1.10isexactintegralbasisandmultiplicationmatch.','2003exposition;notclaimedfirstdiscovery','Established;finitecoefficientsrequirekernelaswellascokernelof2.',['KarpenkoQuadrics'],family='quadrics')
claim(37,[53],56,[35],'1753-1773','Maximalisotropicfamiliesgivecyclebasis;linéaire.',
 'For a split smooth projective quadric over a field ofcharacteristic≠2, linear subspaces frommaximalisotropicfamilies, together withhyperplanepowers,giveitsintegralChowbasis andcorrespondingcohomologicalbasisaftercycleclass. In even dimension therearetwofamilies.',
 'proof sketched','Cellular/rulingargumentreadandQ0..Q6rankscrosschecked. Historicaléquivalencelinéaireisnotreplacedinthetranscription.','B','KarpenkoTheorem1.10providesprecisepublishedmodernChow formulation.','2003checkedlecture;classicaloriginnotdated','Establishedsplitquadricresult;unsplitarithmeticChowgroupsareoutsideclaim.',['KarpenkoQuadrics'],family='quadrics')

dump('claims.json',claims)
flush_stage1()

claim(38,[65],56,[4,14,18],'753-783,1153-1172,1283-1287','ρr lower semicontinuous; ρn and ρu upper semicontinuous.',
 'For a smooth affine group scheme of finite presentation over S, the geometric reductive rank is lower semicontinuous; the nilpotent rank and their difference, the unipotent rank, are upper semicontinuous. The ranks commute with arbitrary base change.',
 'proof sketched','The source fpqc descent argument and smooth-centralizer dimension step were read; no independent proof of the structural input is claimed.','A','Published as SGA3 XII Theorem1.7(a).','Seminar1963–64; publication1970; revised text checked2008','Established under the published affine/smooth hypotheses. The proposed wider recasting on8 is not silently treated as the proved theorem.',['SGA3XII'],family='SGA3')
claim(39,[65,68],56,[4,18,33],'759-768,1287-1290,1744-1747','Locally constant rank iff local maximal tori.',
 'For a smooth affine group scheme of finite presentation over S, locally constant geometric reductive rank is equivalent to existence of maximal tori étale locally, and also fpqc locally; these conditions are stable under base change.',
 'proof sketched','Source cancellation/restatement and maximal-torus functor openness checked; structural representability input is cited, not reproved.','A','SGA3 XII Theorem1.7(b) is the exact published statement.','Seminar1963–64; publication1970','Established. The cancelled early version remains part of the drafting history.',['SGA3XII'],family='SGA3')
claim(40,[65,74],56,[4,14,33],'770-783,1153-1160,1747-1751','Tori locally conjugate; ρn locally constant when ρr is.',
 'Under C2039, any two maximal tori are conjugate étale locally. If the reductive rank is locally constant then the nilpotent and unipotent ranks are too; the latter follows from the smooth centralizer of a local maximal torus.',
 'proof sketched','Final proof cites XI5.4bis and Borel; the centralizer dimension step is explicitly checked on14.','A','SGA3 XII Theorem1.7(c,d).','Seminar1963–64; publication1970','Established; these conclusions retain smoothness and the local-rank assumptions.',['SGA3XII'],family='SGA3')
claim(41,[68],56,[12,14,33],'1061-1093,1176-1197,1744-1747','Torus functor smooth separated finite type; affine later.',
 'For a smooth affine group scheme of finite presentation over S with locally constant reductive rank, the maximal-torus functor is represented by a smooth separated finite-type S-scheme, locally isomorphic to G/N_G(T); it is in fact affine over S.',
 'proof sketched','The finite-type check after its authorial flag is present; affineness is deferred. Quotient quasi-compactness proof checked.','A','SGA3 XII Corollary1.10 and Corollary5.4 supply the two distinct conclusions.','Seminar1963–64; publication1970','Established, including the later deferred affineness; alternative cancelled proof route is not required.',['SGA3XII'],family='SGA3')
claim(42,[74],56,[25],'1532-1535','Commuting torus R lies in maximal T.',
 'If T is a fibrewise maximal torus in a group scheme G and R is a torus commuting with T, under the source’s finite-presentation/image hypotheses, the image of R×T→G is a torus containing T; maximality forces R⊂T.',
 'proved there','Independent product-image argument in proof_notes.md §5; the existence of the torus image is the cited SGA3 input.','A','SGA3 XII Lemma1.14.','Publication1970','Established under the specified scheme-theoretic maximality and image theorem.',['SGA3XII'],family='SGA3')
claim(43,[74],56,[25,29],'1536-1542,1638-1641','Unique maximal torus for commutative/nilpotent fibres.',
 'A commutative smooth affine group scheme with locally constant reductive rank has a unique maximal torus containing every torus. For smooth affine G with geometrically connected nilpotent fibres and the same rank condition, its unique maximal torus is central.',
 'proof sketched','Inserted rank conditions and the reduced-fibre Nullstellensatz argument read directly. Descent of the unique local torus is formal.','A','SGA3 XII Corollaries1.15–1.16.','Publication1970','Established; removing local constancy is contradicted by the G_m-to-G_a degeneration.',['SGA3XII'],family='SGA3')
claim(44,[74],56,[14],'1163-1172','ρu(s)=0 gives a neighbourhood of constant ρr,ρn.',
 'Under C2038, if ρu(s)=0 then a neighbourhood of s has ρr=ρn=ρr(s), hence ρu=0 there.',
 'proved there','Independent inequality proof: shrink so ρr(t)≥r and ρn(t)≤r; use ρr(t)≤ρn(t).','A','SGA3 XII Corollary1.9.','Publication1970','Established by the exact semicontinuity inequalities.',['SGA3XII'],family='SGA3')
claim(45,[74],56,[18,29],'1278,1646-1650','Maximality equivalence; converse deferred to XIV.',
 'For finite-type group schemes G⊃H⊃T, T is fibrewise maximal in G iff it is fibrewise maximal in H and the geometric reductive ranks of H and G agree at every point. Containment-maximal subtori need not be fibrewise maximal over general bases; the converse is asserted only over artinian bases or in the locally reductive case.',
 'proof sketched','The equivalence follows fibrewise by equality of dimensions of maximal tori. The stronger containment/existence converse is a forward reference, not proved in the supplied sheets.','A','SGA3 XII Proposition1.17 and remarks following Definition1.3 retain the distinction and refer forward to XIV.','Publication1970','Established distinctions; no general-base converse is claimed.',['SGA3XII'],family='SGA3')
claim(46,[70],56,[21,16],'1393-1397,1234','Finite étale fibres specialize injectively.',
 'For an étale separated quasi-finite group scheme of finite presentation over S, the geometric fibre-group class is lower semicontinuous for the subgroup-inclusion order used in the source. Local constancy of fibre order is equivalent locally to finiteness.',
 'proof sketched','The complete-trait finite open-and-closed subgroup gives an actual injection of special into generic fibre; equal order makes it an isomorphism. Finiteness uses the valuative argument.','A','SGA3 XII Lemma2.2 has the same specialization proof.','Publication1970','Established with separation, quasi-finiteness and finite-presentation hypotheses.',['SGA3XII','EGAII'],family='SGA3')
claim(47,[81],56,[29],'1654-1656','W=N(T)/C(T) finite étale, compatible with base extension.',
 'For a smooth affine algebraic group G over a field and maximal torus T, N_G(T)/C_G(T) is finite étale; after an algebraic closure it is the constant group of normalizer/centralizer points. Formation is compatible with field extension.',
 'proof sketched','Normalizers/centralizers and quotient representability are cited XI5.9; scope and base-change statement read.','A','SGA3 XII §2 opening, using XI5.9.','Publication1970','Established, with maximality explicit in this source passage.',['SGA3XII'],family='SGA3')
claim(48,[71],56,[16],'1236-1241','For any R⊂T, W(R) is a subquotient of W(T).',
 'The unrestricted comparison for nested subtori in a smooth affine algebraic group over an algebraically closed field is false.',
 'false as stated','SL4(C), v=(3,1,−1,−3), a=(1,2,−7,4); connected R⊂T, both centralizers diagonal, |W(R)|=2 and |W(T)|=1. All24 permutations, character primitivity and weight-distinctness checked in checks.py; geometric reduction proved in§5.','C','Printed SGA3 XII Lemma2.3 repeats the wording; its proof invokes maximality. No exact published erratum was located in the recorded title/MO/SGA searches.','SGA3 publication1970; refutation2026-11-19','False as printed and transcribed in this generality; refined statement C2049 holds.',['SGA3XII'],family='Weyl')
claim(49,[71],56,[16],'1236-1241','Proof intended for maximal T (reconstructed).',
 'For smooth affine G over an algebraically closed field, if R⊂T and T is a maximal torus of G, W(R) is a quotient of the subgroup (N(R)∩N(T))/C(T) of W(T).',
 'stated without proof','Independent proof§5: for n∈N(R), T and nTn⁻¹ are maximal tori of C_G(R)⁰; conjugate them there, obtaining a representative in N(R)∩N(T).','A','This is the hypothesis used in the proof of SGA3 XII Lemma2.3 and in its intended application.','Publication1970; missing-hypothesis refinement explicit2026','Established refinement; do not represent it as a corrected diplomatic reading.',['SGA3XII'],family='Weyl',author='Current refinement of Grothendieck’s lemma')
claim(50,[72],56,[18],'1285','There is a smooth affine degeneration G_m→G_a.',
 'For R=Z_(3), G=Spec R[x,(1+3x)⁻¹] with x⋆y=x+y+3xy is smooth affine over R, with generic fibre G_m and special fibre G_a.',
 'stated without proof','Associativity, identity, inverse, generic coordinate and special law verified exactly; open-in-A¹ smoothness checked.','A','SGA3 XII Remark1.6 repeats the existence assertion; the explicit model here certifies it.','Publication1970; model independently checked2026','Established; illustrates failure of naive global maximal-torus existence.',['SGA3XII'],family='SGA3')
claim(51,[76],56,[27],'1601-1610','Fibrewise reductive-centre criterion, affine fibres inserted.',
 'For a group scheme G of the stated finite-presentation type with affine fibres, a subgroup Z is its reductive centre iff Z is of multiplicative type and each geometric fibre is the reductive centre of the corresponding fibre of G; the universal central factorization property is stable under arbitrary base change.',
 'proof sketched','Source proof combines fibrewise centrality, the image of H×Z and equality detected on fibres. Precise cited image theorem is not independently proved.','A','SGA3 XII Definitions4.1–4.2 and Proposition4.3.','Publication1970','Established with affine-fibre and finite-presentation hypotheses; source’s inserted condition is retained.',['SGA3XII'],family='SGA3')
claim(52,[76],56,[23,27],'1456-1465,1614-1618','Every affine algebraic group over k has a reductive centre.',
 'An affine algebraic group over a field has a largest central subgroup of multiplicative type with the universal base-change factorization property defining the reductive centre.',
 'proof sketched','Reduction to commutative centre and finite rank argument read; source proof on23 ends before the final cited image step. Literal H∩G/Z⁰=0 is ill-typed.','A','SGA3 XII Theorem4.4 supplies the completed statement/proof and corrected structural forward reference.','Publication1970','Established. The source’s missing parentheses and unfinished continuation are documentary alarms.',['SGA3XII'],family='SGA3')
claim(53,[76],56,[31],'1710-1712','G/Z has trivial reductive centre; proofs(a,b) omitted.',
 'For a smooth affine group scheme G of finite presentation with geometrically connected fibres and reductive centre Z as in SGA3 XII4.7(b), the quotient G/Z has trivial reductive centre. Parts(a,b) of the surrounding source statement cannot be recovered solely from the supplied proof fragment.',
 'proof sketched','Source inner-action argument read to its abrupt end; printed proof checked through the Hom-of-tori rigidity conclusion.','A','SGA3 XII Theorem4.7(b), proof on printedpp134–135.','Publication1970','Established under the published connected-fibre hypotheses; missing source statement not reconstructed as quotation.',['SGA3XII'],family='SGA3')

DA='Antoine Delzant (1962 offprint)'
claim(54,[86],56,[36],'1787-1829','Q(A) and its group-ring presentation.',
 'For a field F with charF≠2, the Grothendieck group of nondegenerate quadratic spaces under orthogonal sum, with tensor product multiplication, is GW(F). The surjection Z[F*/F*²]→GW(F) has ideal generated by binary isometry relations.',
 'proof sketched','Witt chain-equivalence/cancellation inputs identified; basic diagonalization and the binary replacement reduction checked.','E','Witt1937 supplies the classical diagonalization and binary-invariant background; Becher’s virtual-forms paper §4.4–4.6 gives an exact later presentation.','Witt publication1937; Delzant note1962; later exposition date not inferred','Established; this is GW, retaining rank, rather than W.',['Witt1937','BecherVirtual'],author=DA,family='Delzant')
claim(55,[86],56,[36,37],'1831-1843','Binary relations determined by discriminant and quaternion class.',
 'For nondegenerate binary forms over F, charF≠2, equality of determinant square class and of the associated Hasse/quaternion invariant is equivalent to isometry; this gives Delzant’s stated binary relation generators.',
 'proof sketched','Witt1937 Satz8 on printedp36 read in image; source use compared with its exact rank2 scope.','E','Witt1937 Satz8 is the cited rank2 classification input.','Published1937; first circulation not established','Established for rank2; these invariants do not classify arbitrary-rank forms over arbitrary fields.',['Witt1937'],author=DA,family='Delzant')
claim(56,[89],56,[37],'1845-1877','Rank plus total Stiefel–Whitney class defines filtered ring map.',
 'For a field F of char≠2, rank-one forms map to Kummer classes in H¹(F,Z/2); the binary relations define the natural rank-plus-total-class map GW(F)→Z×(1+∏_{i>0}H^i(F,Z/2)) with Grothendieck’s special total-class multiplication. Whitney addition holds; for diagonal forms w₁=Σ(a_i), w₂=Σ_{i<j}(a_i)∪(a_j).',
 'proof sketched','Binary relation compatibility and the source’s rank coordinate read; symbol expansions checked in checks.py.','B','Grothendieck1958 §4 remark2 gives the target ring. Laborde1976 §III extends the classes to schemes and identifies its field restriction with Delzant’s.','Grothendieck1958; Delzant1962; Laborde talk1975/publication1976','Established; retain the rank coordinate and special multiplication.',['GrothChern1958','Laborde1976'],author=DA,family='Delzant')
claim(57,[89],56,[37],'1879-1889','u(q)=w²(q), normalized relative to same-rank unit form.',
 'The Galois descent obstruction comparing the Clifford algebra of q with that of the same-rank unit form (even Clifford algebra in odd rank), using Delzant’s indicated twisting construction, gives the cohomological Hasse–Witt invariant w₂(q). This is not an unqualified equality with the bare Brauer class of any chosen Clifford algebra.',
 'stated without proof','Normalization and parity cases compared with the printed passage. Original Springer1959 article located by DOI but full text unavailable; no independent full proof certified.','B','Later quadratic-form literature retains the normalized invariant; Milnor1970 treats Stiefel–Whitney/Hasse invariants. The specific Springer descent construction remains reference-level, not fully reproved here.','Springer1959 bibliography/DOI located; Delzant1962; Milnor1970','Established standard invariant with normalization; confidence medium because the cited original proof was not opened beyond metadata.',['Milnor1970','Springer1959'],confidence='medium',author=DA,family='Delzant')
claim(58,[89],56,[37],'1891-1893','w is natural under field maps.',
 'For a homomorphism of fields F→E of characteristic≠2, restriction in Galois cohomology sends the total Stiefel–Whitney classes of q to those of q_E; rank is unchanged.',
 'proof sketched','Independent reduction to diagonal rank-one forms and functorial Kummer classes; Whitney multiplication gives the result.','B','Laborde1976 lists functoriality and identifies the field construction with Delzant; Stacks59.28 gives the Kummer sequence.','Delzant1962; scheme extension1976','Established. The untilded target in prose must not remove rank.',['Laborde1976','StacksKummer'],author=DA,family='Delzant')
claim(59,[93],56,[38],'1904-1926','Over a number field, rank and all w_i classify forms.',
 'For a number field F, the map q↦(rank(q),w(q)) is injective on GW(F). Finite completions use rank, determinant and Hasse invariant; real completions use rank and the total binomial series, and Hasse–Minkowski gives the global injection.',
 'proof sketched','Witt1937 p43 Satz21 andp44 summary read; real binomial bits checked n=0..64, general Lucas/characteristic2 factorization proof in§6. Virtual forms handled by adding a common positive form.','B','The local/global ingredients predate the offprint; Delzant1962 assembles them into its Stiefel–Whitney formulation, retained in later treatments.','Witt1937 antecedents; Delzant publication1962-09-10 session','Established, including virtual classes by group completion.',['Witt1937','Milnor1970'],author=DA,family='Delzant')
claim(60,[89],56,[38],'1913-1926','Untilded H target might suggest rankless injectivity.',
 'If the literal diagram is interpreted as mapping only to positive Stiefel–Whitney classes, injectivity is false: over R, ⟨1⟩ and ⟨1,1⟩ both have total class1 but have different ranks. The intended final assertion includes rank.',
 'false as stated','The two positive definite forms are nondegenerate over char0, have unequal dimensions and all Kummer entries0.','C','The target defined one page earlier and the final sentence fix the intended rank-bearing formulation; Grothendieck1958 §4 remark2 confirms its rank factor.','1962 printed note; alarm checked2026','This is a literal-target alarm, not a refutation of the offprint’s final rank-plus-classes theorem.',['GrothChern1958'],author=DA,family='Delzant')
claim(61,[88],56,[36,38],'1787-1829,1928-1933','Earlier-run comparison J⊂GW and I⊂W.',
 'For a field F of characteristic≠2, projection GW(F)→W(F) restricts to an isomorphism from rank-zero ideal J onto the even-rank ideal I. It identifies J^r with I^r for every r≥1.',
 'stated without proof','Independent proof§6: kernel of GW→W is Z·h, rank(h)=2; rank-zero lift of an even-rank Witt class is q−rank(q)h/2. Multiplicativity on ideals follows from hq=rank(q)h.','B','This standard comparison links Delzant’s filtration to Milnor1970 Theorem4.1; exact map is proved here rather than inferred from a name.','Delzant1962; Milnor1970; independent comparison2026','Established; the map is an ideal-ring isomorphism, not a rank-preserving isomorphism of the entire unital rings.',['Milnor1970','BecherVirtual'],author='Earlier-run/current reconstruction',family='Delzant')
claim(62,[88],56,[37,38],'1872-1877,1928-1933','Earlier-run coefficient comparison of the degree2 arrow.',
 'For d_a=⟨a⟩−1 and d_b=⟨b⟩−1 in J, w₁(d_ad_b)=0 and w₂(d_ad_b)=(a)∪(b); J³ is invisible in cohomological degrees≤2.',
 'stated without proof','Exact formal-power-series computations overF2 to degree2 for two and three factors saved in checks.json Delzant_symbol; general generation argument in§6.','B','Milnor1970 §3–§4 and Merkurjev’s degree2 theorem identify this as the norm-residue symbol after J²/J³≅I²/I³.','Milnor1970; Merkurjev1981','Established exact map match, not merely an analogy between filtrations.',['Milnor1970','Merkurjev2006'],author='Earlier-run/current reconstruction',family='Delzant')
claim(63,[94],56,[38],'1928-1931','Is grad²Q(A)→H²(A,Z/2) injective?',
 'For every field F of characteristic≠2, Delzant’s map J²/J³→H²(F,Z/2) is an isomorphism.',
 'open on the pages','J/I and symbol identifications independently checked inC2061–C2062; cited theorem text checked, no full independent proof of Merkurjev.','B','Milnor1970 Theorem4.1 gives K₂^M(F)/2≅I²/I³; Merkurjev’s degree2 norm-residue isomorphism completes the exact map.','Milnor publication1970; Merkurjev publication1981; first circulation not separately established','Solved, with char≠2 and degree2 exactly as asked.',['Milnor1970','Merkurjev1981','Merkurjev2006'],author=DA,family='Delzant')
claim(64,[94],56,[38],'1931-1933','Is every Brauer element of order2 a sum of a.b?',
 'For every field F of characteristic≠2, each class in Br(F)[2] is a finite sum of quaternion classes (a,b); equivalently the degree2 norm-residue symbol is surjective.',
 'open on the pages','Merkurjev2006 Theorem2.2 and original1981 bibliographic reference checked; Kummer coefficient identification separately checked.','B','Merkurjev’s theorem gives an isomorphism K₂^M(F)/2→Br(F)[2], stronger than the requested surjectivity.','Original publication1981; author’s later proof2006; circulation date not established','Solved for exactly the requested fields and2-torsion.',['Merkurjev1981','Merkurjev2006','StacksKummer'],author=DA,family='Delzant')
claim(65,[94],56,[36],'1831-1834','H²(F,Z/2) identifies with Br(F)[2].',
 'For charF≠2, μ₂≅Z/2 and the étale Kummer sequence, together with Pic(SpecF)=0, identifies H²(F,μ₂) with the2-torsion subgroup of the cohomological Brauer group, equal to the field Brauer group.',
 'stated without proof','Exact sequence read in Stacks59.28; the Picard term vanishes because every one-dimensional vector space overF is trivial.','E','Kummer theory is the classical input; its exact sequence is checked in Stacks59.28.','Established before1962; earliest date not assigned','Established under2invertible; no characteristic2 substitution is made.',['StacksKummer'],author=DA,family='Delzant')
claim(66,[64],11,[44],'25-27','Contextual Oda comparison; no cote54 witness here.',
 'For an abelian scheme A over a perfect field k of characteristic p, Oda gives M(A[p])≅H¹_dR(A/k), identifying VM with H⁰(A,Ω¹) and respecting the associated filtered exact sequence.',
 'stated without proof','Oda1969 Corollary5.11 and its exact hypotheses read. This does not verify the unavailable source question from cote54.','B','Oda1969 Corollary5.11 is the exact later comparison, including the Hodge subspace.','Based on Harvard dissertationJune1967; published1969; dissertation date is not a claim of earlier public circulation','Established comparison; keep the external manuscript attribution unverified.',['Oda1969'],author='Tadao Oda; contextual result reported by earlier notes',family='Oda')
claim(67,[99],56,[24,32],'1503-1519,1715-1736','Rank-one exterior-algebra comparison from earlier notes.',
 'In Λ_Z(e1,f1,e2,f2), ξ=e1∧f1+e2∧f2 has ξ²=2e1∧f1∧e2∧f2. The resulting rank-one cokernel isZ/2, matching the conic hyperplane map as an integer map.',
 'stated without proof','Exact signed exterior multiplication and Smith invariant saved. No identification of complete rings or representations is asserted.','B','The comparison is elementary; the checked quadric ring supplies the matching map. Recorded searches found no reason to strengthen it to a full operator-algebra equivalence.','Earlier-run idea; independently checked2026','Correct local matrix analogy only.',['KarpenkoQuadrics'],author='Earlier-run idea, independently checked',family='quadrics')

claim(68,[7],12,[102],'3-20','Cycle maps commute with f*, f_*; correspondences identified with Hom.',
 'For smooth projective connected schemes X,Z over k and ℓ invertible in k, rational ℓ-adic Künneth and Poincaré duality identify total cohomological correspondences with graded linear operators, with Tate twists and degree shifts made explicit. The algebraic operators are those represented by algebraic cycle classes.',
 'proof sketched','The displayed Hom isomorphism suppresses gradings/twists; source continuation stops before the action formula. Compare11/44–46 and the published standard-conjectures introduction.','A','Grothendieck1969 §1 gives the corresponding algebraic-operator formalism.','Published1969; reused-sheet date not inferred from nearby1968letter','Established with the omitted grading/Tate conventions restored as explanatory reconstruction.',['GrothStandard1969'],author='Grothendieck-related reused standard-conjecture text; exact edition not identified',family='correspondences',source_file=B2)
claim(69,[111],12,[121],'50','Deligne solved the λ-structure problem on perfect-complex K⁰ over a field.',
 'For a scheme X over a field, the Grothendieck group of perfect complexes admits the exterior-power operations and special λ-ring identities compatible with vector-bundle operations. The report says Deligne had written this theory in that scope; it does not claim an unrestricted result for all ringed topoi at that date.',
 'stated without proof','Source’s base-field restriction and Dold–Puppe construction route read; modern operation comparison theorem read, not independently reproved.','B','Köck–Zanchetta2025 explains exterior operations on Perf(X), compares constructions on schemes and verifies λ identities in the stated equivariant scope. It confirms the established modern scheme result, not the exact date of Deligne’s unavailable manuscript.','Report undated; bibliography SGA6 publication1971; modern comparison published2025-02-21','Established for schemes; attribution of the historical solution to Deligne is the source’s report. General ringed-space scope is not certified.',['KockZanchetta2025','SGA6Front'],confidence='medium',author='Grothendieck reporting Pierre Deligne',family='Ktheory',source_file=B2)
claim(70,[112],12,[123],'54-56','Leray degeneration conditional on fibre Lefschetz.',
 'For a smooth projective morphism and rational cohomology, a relative ample class satisfying hard Lefschetz on the fibres yields Deligne’s splitting/degeneration of the Leray spectral sequence. The analytic claim needs the corresponding relative Lefschetz class, not merely Kähler fibres in isolation.',
 'stated without proof','Conditional language is explicit. Root owns the detailed published theorem comparison and cross-package merge.','B','Deligne’s degeneration criterion and hard-Lefschetz theorem settle the smooth-projective case; the current source’s Kähler generalization requires checking its relative polarization hypothesis.','Deligne1968 degeneration paper; later hard Lefschetz1980; root verifies exact references','Established in the smooth-projective setting; broader analytic wording is conditional and must not be universalized.',['Deligne1968Degeneration'],confidence='medium',author='Grothendieck reporting Pierre Deligne',family='DeligneDegeneration',source_file=B2)
claim(71,[113],12,[138],'182-201','Essential subspace W and conjugation of reflections.',
 'For a finite real orthogonal reflection group G on E, W=(E^G)^⊥ is invariant, restriction identifies G faithfully with an essential reflection group on W, and g s_H g⁻¹=s_{gH}.',
 'proved there','Orthogonal decomposition and conjugation checked directly; fixed complement is pointwise fixed.','E','Coxeter1934 §§4–7 develops essential/reducible reflection groups and chamber structure.','Received1933-06-16; publicationJuly1934; receipt not claimed first circulation','Established classical structure. Reused typescript authorship remains qualified Bourbaki, not Grothendieck.',['Coxeter1934','Bourbaki1968'],author='Reused Bourbaki-type typescript; document identification qualified',family='reflection',source_file=B2)
claim(72,[113],12,[136],'158-164','Wall reflections generate G; chambers form a transitive G-set.',
 'For a finite real orthogonal group generated by a G-stable finite set of reflecting hyperplanes, the walls of any chamber in the complement generate G and G acts transitively on the chambers.',
 'proved there','Nearest-orbit-point argument read and independently checked: reflecting across a separating wall strictly reduces distance. Chamber definition requires complement.','E','Coxeter1934 §§4–8 supplies the classical chamber/generator structure.','Publication1934; before the reused manuscript','Established with the corrected complement definition.',['Coxeter1934'],author='Reused Bourbaki-type typescript',family='reflection',source_file=B2)
claim(73,[113],12,[134,136],'148,172-174','(e_i,e_j)=−cos(π/m_ij), negative values≤−1/2.',
 'For inward unit normals of distinct chamber walls in a finite real reflection group, the angle formula uses the order m_ij≥2 of the product of wall reflections. Hence off-diagonal inner products are nonpositive and any negative one is≤−1/2.',
 'proved there','Two-dimensional dihedral reduction checked; cos(π/3)=1/2 is elementary. The missing-reference joke does not make it an open problem.','E','Coxeter1934 §8 uses exactly the dihedral anglesπ/m and Coxeter relations.','Publication1934','Established for the normals, not for their dual basis in rank≥3.',['Coxeter1934'],author='Reused Bourbaki-type typescript',family='reflection',source_file=B2)
claim(74,[113],12,[132,134],'130-142,150-152','Simple normals form a basis; Coxeter presentation; simple transitivity.',
 'In the same finite reflection-group setting, inward normals to a chamber’s walls are a basis of the essential subspace. G has presentation s_i²=(s_is_j)^{m_ij}=1 and acts simply transitively on chambers.',
 'proof sketched','Source linear-independence argument uses nonpositive mutual products and a common positive functional; the representation/presentation proof cites earlier absent sections.','E','Coxeter1934 Theorem8 gives the presentation; Theorem4 gives the simplicial fundamental region.','Publication1934','Established; current source proof imports preceding sections not attached.',['Coxeter1934','Bourbaki1968'],author='Reused Bourbaki-type typescript',family='reflection',source_file=B2)
claim(75,[113],12,[130],'106-120','Positive roots; simple reflection permutes other positive roots; all reflections found.',
 'Every inward normal to a mirror is a nonnegative combination of simple normals. A simple reflection permutes the positive normals other than its own. The G-stable generating mirror set is all mirrors, and |G| equals the chamber count.',
 'proved there','Coefficient proof and comparison of chamber counts read; positif is interpreted as≥0 as in the proof, not all coefficients strictly>0.','E','These are classical finite-reflection consequences of the Coxeter chamber theorem; Coxeter1934 §§4–8 provides the foundational result.','Publication1934 antecedent; precise Bourbaki wording later1968','Established; nonnegative coefficients are the mathematically supported meaning.',['Coxeter1934'],author='Reused Bourbaki-type typescript',family='reflection',source_file=B2)
claim(76,[113],12,[128,130],'84-90,122-124','Closed chamber fundamental domain; point stabilizers generated by mirrors through point.',
 'For a finite real reflection group, each orbit meets a closed chamber in exactly one point. Intersections of chamber closures are closed faces; a point stabilizer is generated by reflections whose mirrors contain the point. The element carrying a chamber is unique, but g in x=g(y) need not be unique on a boundary.',
 'proof sketched','Source cites prior face/coxeter lemmas; the distinction between unique y and nonunique g read directly. No erroneous uniqueness of g is inferred.','E','Classical chamber/Coxeter structure; modern Bourbaki chapterV confirms subject/edition metadata, while Coxeter1934 provides the underlying fundamental-domain construction.','Coxeter1934; Bourbaki publication1968','Established; retain exact uniqueness quantifier.',['Coxeter1934','Bourbaki1968'],author='Reused Bourbaki-type typescript',family='reflection',source_file=B2)
claim(77,[113],12,[126,128],'64-74,94-98','Proper affine reflection groups split orthogonally.',
 'For a discrete group of affine orthogonal isometries generated by affine reflections acting properly on finite-dimensional Euclidean E, the linear parts fix W′ pointwise, all displacements lie in W=(W′)^⊥, and an invariant orthogonal decomposition splits G into the corresponding reflection subgroups. A fixed factor is retained when G is not essential.',
 'proved there','Every reflecting normal lies in one invariant summand; its reflection acts trivially on the other, so independent generators give the product surjection.','E','Coxeter1934 Lemma5.1 and Theorem6 give the classical decomposition.','Publication1934','Established with properness/discreteness and the fixed-factor qualification.',['Coxeter1934'],author='Reused Bourbaki-type typescript',family='reflection',source_file=B2)
claim(78,[113],12,[126],'76-78','The family of affine mirrors is locally finite.',
 'For the proper discrete affine action in C2077, any G-stable generating set of distinct reflecting hyperplanes is locally finite.',
 'proof sketched','Source proof is cut off. Independent completion§7: infinitely many mirrors meeting a compact ball force infinitely many reflections with g(K)∩K≠∅, contradicting properness.','E','The discrete reflection-group framework of Coxeter1934 requires locally separated mirror geometry; the exact compactness proof is independently supplied here.','Classical discrete-group fact; exact first formulation not dated','Established; source page ends mid-proof.',['Coxeter1934'],author='Reused Bourbaki-type typescript',family='reflection',source_file=B2)
claim(79,[114],12,[130,132],'104,142','Dual-basis angle equals cos(π/m_ij).',
 'The displayed dual-basis cosine equality is false for typeA3, even though the corollary that vectors in a common chamber have nonnegative scalar product is true. The correct dual Gram matrix is the inverse of the simple-normal Gram matrix.',
 'false as stated','A3 normal Gram [[1,−1/2,0],[−1/2,1,−1/2],[0,−1/2,1]] has inverse with dual cosine13=1/3, butm13=2 givescos(π/2)=0. Exact certificate saved.','C','The classical normal-angle formula in Coxeter1934 does not imply the stated dual equality. Inverse positivity proves the valid corollary. No exact typescript erratum was found.','Current refutation2026; classical corrected linear algebra','Correct the proof/scan reading; retain the nonnegative-angle corollary.',['Coxeter1934'],author='Reused Bourbaki-type typescript',family='reflection',source_file=B2)
claim(80,[1,31],11,[44,46,48],'20-46,82-177,213-253','Contextual draft standard-conjecture letters and operator projectors.',
 'The current package does not identify draft B/D or the complete cote16 operator statements reported by the earlier notes. Published standard-conjecture names cannot determine those missing draft definitions.',
 'open on the pages','No mathematical computation is possible for an unidentified external statement; manuscript absence checked.','F','Grothendieck1969 was opened to compare published naming, but no unavailable cote16 witness is invented.','Published1969; contextual manuscript date not established','Exact contextual claim not identifiable from this package.',['GrothStandard1969'],confidence='low',family='context')
claim(81,[36],56,[5],'861-867','R^{n−1}f_* est “pur” ...',
 'The final purity phrase does not specify the relevant coefficient category, weight normalization, extension functor or precise assertion. A modern middle-extension/purity theorem cannot be quoted as its exact solution without those data.',
 'open on the pages','Truncated wording and adjacent monodromy calculation read; no hidden completion supplied.','F','Searches in DeligneWeilI and SGA7 metadata identify the surrounding theory, not an exact purity theorem matching the fragment.','Search as of2026-11-19','Unidentified purity formulation; recover source context/ink before assigning a modern theorem.',['DeligneWeilI','SGA7II'],confidence='low',family='quadrics')

dump('claims.json',claims)
flush_stage1()
