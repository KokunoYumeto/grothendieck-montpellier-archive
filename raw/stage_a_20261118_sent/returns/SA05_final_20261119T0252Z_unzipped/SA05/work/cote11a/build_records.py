"""Hand-authored close-reading records. No verdict is inferred from headings.
The source index is read only to validate the manually supplied 82 verdicts.
Run from the workspace root: python SA05/work/cote11a/build_records.py
"""
import csv,json,pathlib
ROOT=pathlib.Path('SA05/work/cote11a')
P='sources/texts/pro/MPL_11_002-042_transcription.tex'
B='sources/texts/codex/B12-01_transcription.tex'
PK='MPL_11_002-042'
items=[]; entries=[]; claims=[]; problems=[]
def item(n,src,kind,scans,lines,words,statement,reconstruction,check,reason,cote='11',file=P,extra=None):
 d=dict(id=f'SA05-{n}',sources=[f'{PK}#{i}' for i in src],kind=kind,cote=cote,scans=scans,lines=[f'{file}:{s}' for s in lines],his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason)
 if extra:d.update(extra)
 items.append(d)
def entry(i,n,v,r):entries.append(dict(entry_id=f'{PK}#{i}',item_id=f'SA05-{n}',verdict=v,reason=r))

item(1001,[1,79,80],'title, date or page count',[3,4,6,27,34,38,42],['1-1309'],
 'A; C; Algèbres simpliciales',
 'The supplied Pro file retains 39 scans: twenty handwritten subject pages and nineteen reused English GIT sheets. Their order interleaves different documents. The numerical mspage=scan−1 sequence is archive sheet numbering; the typescript also has its own chapter pagination.',
 'Counts and distinction of archive numbering from document pagination are current source inventory. No manuscript date or original total extent is asserted. The earlier run’s 696 elements, freeze time and forty hashes cannot be independently checked without its missing fragment/hash ledger.',
 'overstates','Codex comments distinguish archive sheet numbers from document numbers. The earlier entry calls the former handwritten foliation; that would falsely imply authorial continuity. Titles are present; dates are not.')
item(1002,[2,5,46,48,49],'idea of the earlier run',[3,16,27],['4-48','551-566','841-868'],
 'A; conjecture (on the reused Tits page)',
 'Cote11 supplies correspondence and Poincaré algebra formalism, not a labelled list of standard conjectures. The proposed draft-C/printed-B and draft-A/printed-A dictionary comes from the earlier run’s reported cote16 passages. The standalone draft B and D definitions remain absent from this part.',
 'The current file was read throughout. Grothendieck1969 and Kleiman1968 provide the printed side, but the cote16 source side is an unavailable external lead, even where the earlier notes describe an exact formula.',
 'overstates','The letter comparison is not direct evidence from the attached cote11 manuscript. Entry5 correctly limits cote11; its unprovided context quotations cannot be upgraded to checked witnesses.')
item(1003,[3,47],'idea of the earlier run',[],[],
 'No direct cote16 witness attached; the earlier note reports w^{-1}u=v^{-1}.',
 'For isomorphisms v:V→W and u:W→V, set w=uv. Then w^{-1}u=v^{-1}. If w has an annihilating rational polynomial with nonzero constant term, its inverse is a rational polynomial in w. This is the algebraic step connecting an opposite-direction isomorphism to the inverse Lefschetz map.',
 'Independent algebraic verification, not a new verification of the missing cote16 quotation. Kleiman Proposition2.3 and Theorem2.9 are the published comparison targets; their Weil cohomology and strong Lefschetz hypotheses remain explicit.',
 'agrees','The displayed typed maps compose correctly. The source-attribution claim remains an earlier-run lead.')
item(1004,[4],'idea of the earlier run',[],[],
 'No manuscript lowering formula in this supplied package.',
 'On a primitive Lefschetz string a,La,…,L^ma, the unit-step operator Λ and classical lowering cΛ satisfy cΛ(L^ja)=j(m−j+1)L^{j−1}a. With D|a=1 and D|L^ja=j(m−j+1), cΛ=ΛD and Λ=cΛD^{-1}; the top-string factors are 1 and (m!)².',
 'This is the earlier run’s explicit comparison of Kleiman’s conventions, rechecked independently. It must not be called a quotation from unavailable cote16/010 or /013.',
 'agrees','The order ΛD, the nonzero range1≤j≤m and the separate value on the primitive vector are essential. Saved exact code checks finite strings and the proof uses the displayed basis.')
item(1005,[6,33,77],'unproved claim',[3,5,7,9,11,13,15],['4-48','88-139','176-229','261-297','328-384','420-470','503-542'],
 'Hom(X,Y)=A(X×Y); u(x)=p_{2*}(u p_1^*x)',
 'For a product category with contravariant algebra pullbacks and covariant pushforwards, satisfying functoriality, projection formula and the particular base-change squares used, kernels A(X×Y) compose by p_XZ*(p_YZ*v·p_XY*u), have diagonal units, receive graph correspondences, and act on A(X). The manuscript writes and computes these constructions.',
 'Named projections remove ambiguous numerical subscripts. A rigorous all-degree version needs a chosen Koszul convention; the even-degree specialization avoids the specific sign failures flagged in the manuscript. This kernel category is not yet an idempotent-complete category with Tate twists.',
 'agrees','The proof is present for associativity, identities, graphs and realization, with explicit sign warnings and local typing defects. The extra chosen Lefschetz ring map belongs to unavailable cote16, separately retained in SA05-1029.')
item(1006,[7,34],'unpursued implication',[21],['681-726'],
 'A′(X)⊂A(X); système stable',
 'A unital family of subsets (subrings in the later ring version) stable under the specified pullbacks, pushforwards and products determines a subcategory with the same objects and arrows A′(X×Y). Its composition, units and external products are restrictions of those in the ambient kernel category.',
 'The inclusion functor is the identity on objects and inclusions on Hom sets. The converse argument also uses invariance under factor isomorphisms; Pro’s “stable par signe” and Codex’s “isom|somme” differ at this point.',
 'agrees','The literal restriction calculation is correct. The notes should retain the isomorphism/sign reading alarm because it bears on recovering transpose and pullback operations.')
item(1007,[8,42],'idea of the earlier run',[],[],
 'No block-matrix enlargement is written in this source.',
 'In the formal additive enlargement of a preadditive correspondence category, Hom(X,Y) is the corner e_Y End(X⊕Y)e_X. The lower-left block map and its inverse identify convolution with multiplication of compatible blocks.',
 'This is an editorial categorical construction. Cote16’s reported π_jEπ_i decomposes graded pieces, whereas these two idempotents select objects; these are different indexing systems.',
 'agrees','The construction is elementary and rechecked. The source comparison to cote16/004 is unavailable in this run, not a manuscript fact.')
item(1008,[9,39],'unpursued implication',[27,29,31,36],['841-868','895-954','992-1053','1148-1163'],
 'i′=i+d′−d',
 'For trace degree d_X on A(X), a kernel u∈A^q(X×Y) acts in degree q−d_X. In the abstract algebra notation f*:A′→A of degree i has adjoint f_*:A→A′ of degree i+d′−d.',
 'The kernel formula specializes to pullback degree0 and trace degrees additive under tensor product. This transports degrees, not the unprovided cote16 ring Φ or its generators.',
 'agrees','Direct degree balancing proves the result. Pro36 has a wrong φ-subscript in the duality display, separately alarmed.')
item(1009,[10,35,36],'reading question',[19,23,25],['656-660','744-765','785-799'],
 'identique à l’ens des f_*(1_Y); on suppose la résolution',
 'The smallest stable ring system contains all pushforwards of units. Under resolution for integral subvarieties, these give cycle generators. The literal equality of a ring with the set of individual f_*1 is false in CH_Q(Spec C): such values are nonnegative integer degrees or zero, whereas the ring contains −1 and rational multiples.',
 'Replace literal set by the appropriate additive or coefficient-linear span only as a proposed mathematical refinement. A monoid reading could differ; no ink correction is made.',
 'agrees','The earlier run isolates a real set-versus-span issue. The geometric counterexample checks smooth projectivity, grading and the proper-degree formula; resolution itself is unnecessary for the point test.')
item(1010,[11,12,41],'idea of the earlier run',[3],['31-48'],
 'objets les objets de V',
 'For Chow groups in even cohomological grading, Corr^r(X,Y)=CH^{dim X+r}(X×Y)_Q. Passing to objects (X,p,m) and morphisms q Corr^{n−m}(X,Y)p adds idempotent summands and twists. X↦(X,Δ_X,0) embeds the degree-zero correspondence category.',
 'This precise modern comparison is supplied by the earlier run and checked in Stacks0FFZ/0FG9. It is not performed in the supplied manuscript. No semisimplicity result follows from it.',
 'agrees','The reference construction and grading convention are correct. A degree-s kernel gives a morphism to twist s in these Stacks conventions; no claim that full ungraded Hom is already Corr^0 is made.')
item(1011,[13,25,58],'self-flagged step',[3,7,9,31],['4-11','176-229','261-278','1004-1053'],
 'Trouver un cas général commun; carré cartésien ... dimensions',
 'The required exchange identity is p* f_*=f′_* q* for a Cartesian square, with trace-degree balance. The manuscript verifies product and graph squares and asks whether Cartesianity plus dimensions suffices in its abstract Poincaré category.',
 'It does not suffice with freely variable gauges. Let Q_λ have algebraQ, degree0 and traceλ. Maps have pullbackid and pushforwardλ/μ. With upper-left gauge2 and all others1, all four maps are isomorphisms, the square is Cartesian, yet the two exchange composites are1 and2. This does not refute normalized geometric base change.',
 'agrees','The earlier scalar-gauge counterexample is valid and independently rechecked. The geometric Beck–Chevalley refinement remains a separate positive statement, not an automatic consequence of Cartesianity.')
item(1012,[14,24],'withdrawn in the same text',[5,7,13,17,29,31],['111-135','212','420-470','595-625','919-954','992-1001'],
 'Mais c’est faux; pourvu que les degrés ... pairs',
 'The naive tensor-pushforward formula is explicitly retracted when both degrees are not even; the next handwritten page adopts even-degree morphisms. Earlier calculations also flag unresolved graded signs.',
 'The current check verifies the even-shift restriction and the parity obstruction with stated tensor and trace conventions. The damaged final all-degree correction on29 is not silently reconstructed as an established formula.',
 'agrees','“Withdrawn” applies to the naive formula, not to the entire correspondence construction. The notes correctly retain both the retraction and the narrowed working scope.')
item(1013,[15],'unpursued implication',[7,9,13],['176-229','261-278','420-433'],
 'pour construire les unités ... q_*,q^*',
 'The identity kernel is δ_*1 and its operator isid, by the diagonal projection formula and p_2δ=id. Diagonal squares are among the exchange squares the category construction actually needs.',
 'The calculation is valid in the normalized even context, and for cohomology with a coherent graded convention. It is relevant to the unfinished selected-morphism axioms, not an assumption that arbitrary selected maps suffice.',
 'agrees','The note follows the written proof and correctly identifies the extra diagonal input.')
item(1014,[16],'self-flagged step',[15,17],['529-542','570-583'],
 'vérifier que c’est ... multiplicatif; vérifier',
 'Factor interchange gives transposition A(X×Y)→A(Y×X). The manuscript asks to check reversal of convolution and compatibility of the transposed graph/realization diagram ψsφ°=ω*A°.',
 'In even grading with symmetric base change, relabelling the three factors proves reversal. For arbitrary degrees, signs depend on conventions and are not settled solely by this relabelling.',
 'agrees','There are two unfinished checks, not merely a claim that transposition is adjoint. The separate centrality calculation is SA05-1016.')
item(1015,[17],'unproved claim',[17],['584-594'],
 'Sinon, on remplace k par A(e)!',
 'If e is final, structural pullbacks A(e)→A(X) make A(X) algebras over the scalar object A(e), and structural pushforwards are traces. Projection formulas provide A(e)-linearity subject to the stated graded/central scalar convention.',
 'This changes the coefficient algebra and its tensor products; an ordinary commutative base ring requires the appropriate central/even part. The assertion is conditional on the bivariant axioms already in force.',
 'agrees','The maps exist on the page; the qualification about central actions is necessary in a graded non-even setting.')
item(1016,[18,38],'self-flagged step',[17],['595-625'],
 'si u central; mod. signe!',
 'For a central kernel u, its factor-transpose is adjoint for the trace pairings, using projection and trace compatibility. The obstruction without centrality is the traced commutator of u with p_2*y.',
 'The ungraded/even proof is a direct rearrangement. Pro reads “Car u central!” while Codex suggests “Cas u central?!”; the initial centrality condition is secure, but the marginal punctuation needs the scan.',
 'agrees','The note identifies the exact exchange of factors. It must not erase centrality or the sign warning.')
item(1017,[19,43],'unproved claim',[19],['656-660'],
 'seulement leur structure de monoïde; Il faudrait alors',
 'The displayed composition, identity and functoriality formulas use multiplication, units and push/pull maps, suggesting a multiplicative-monoid version. The manuscript begins sign involutions and leaves axioms unfinished.',
 'The map σ^i(a)=(−1)^i a is an earlier-run encoding on a graded algebra, not multiplication-preserving as an individual σ when i is odd; the relevant law is σ^i(a)σ^j(b)=σ^{i+j}(ab). Addition is essential for preadditivity and linear spans elsewhere.',
 'agrees','The notes do not claim complete axioms. The categorical weakening can be formulated with specified operations and exchange, but no exact historical completion was located.')
item(1018,[20],'self-flagged step',[21],['681-726'],
 'E ⊂ Fl(V); généralisation',
 'The source asks to replace all morphisms by selected classes in the stable-system/correspondence formalism. A useful system must contain identities and required diagonals/projections and be closed under the compositions/base changes actually invoked.',
 'Those closure axioms are a current sufficient formulation, not a recovered statement from the blank on scan21. Relative correspondence theories are comparisons, not exact completions of this fragment.',
 'agrees','The source leaves the selected-map generalization unfinished. Its scope cannot be inferred solely from the ambient stable-system theorem.')
item(1019,[21,37],'unproved claim',[23,25],['744-765','785-799'],
 'A′ et E; multiplication OK',
 'The source describes the stable system generated by a stable A′ and additional kernels E through values of multilinear correspondence operations, then checks closure under composition and multiplication.',
 'For a system of subrings or submodules, additive and scalar closure must also be included. The earlier run’s operation interpretation is correct; a literal union of individual operation values need not already be additive.',
 'agrees','There is a proof sketch, but “unproved” in the entry is too coarse unless it means the fully specified additive version. This qualification is retained in the claim.')
item(1020,[22],'unproved claim',[27,34,36],['841-868','1110-1121','1148-1161'],
 'f_* = φ_B^{-1} ... φ_A',
 'For finite projective graded algebras with perfect trace pairings, every degree-zero algebra map f*:B→A has a unique adjoint f_*:A→B, defined by κ_A(f*b·a)=κ_B(b·f_*a). It is functorial and satisfies the corresponding projection formula. For degenerate gauges, existence requires the dual image to land in imφ_B and uniqueness requires φ_B injective.',
 'The finite-projective dual identifications, degree shift and choice of left/right pairing are spelled out in the current statement. The manuscript explicitly provides the weaker-gauge criterion on34.',
 'agrees','These claims are proved by the displayed pairing calculations, though notes label their proof state coarsely. A wrong φ_A in36 is a transcription alarm, not a new mathematical obstruction.')
item(1021,[23],'unpursued implication',[27,34,42],['843-845','1093-1097','1309'],
 'pas nécessairement compatible avec les jauges; bon isom.',
 'An underlying algebra isomorphism between Poincaré objects need not preserve the gauge; its adjoint is inverse pullback followed by multiplication by f_*1. It is a bivariant isomorphism when f_*1 is invertible, and gauge-preserving (“good”) when f_*1=1. The final scalar twist realizes the freedom explicitly.',
 'For one-dimensional Q with traceλ, the pushforward for identity pullback is λ/μ. This is the gauge freedom used by SA05-1011; normalizing geometric traces removes this particular counterexample.',
 'agrees','The note correctly distinguishes algebra and gauge isomorphisms. The final formula has been checked against its trace identity.')
item(1022,[26,59],'self-flagged step',[34],['1077-1091'],
 'pour f_* de degré δ ... (−1)^{δj}',
 'For homogeneous a,b and graded-commutative algebras, the right and left projection identities differ by (−1)^{δ deg b}, where δ is the pushforward degree. They coincide for even δ; the page chooses a convention and then restricts degrees.',
 'The exponent follows by commuting b through a and f_*a: ij+j(i+δ)≡δj mod2. This does not settle the separate all-degree tensor convention on29.',
 'agrees','The earlier parity calculation is correct and re-executed on all parities.')
item(1023,[27],'unproved claim',[36],['1161-1163'],
 'Pour avoir des constructions universelles ... sortir de la catégorie',
 'The source motivates a wider category of gauged graded algebras because desired universal constructions may leave the Poincaré class. No particular universal construction, diagram or claimed universal property is specified here.',
 'Finite projectivity and perfectness are not preserved by arbitrary algebraic limits/colimits, but that general observation cannot identify the exact intended construction.',
 'agrees','This is a programme-level statement with an unidentified exact target; it is not a theorem that all limits fail.')
item(1024,[28],'unproved claim',[29,38],['895-918','1185'],
 'produit ... A et B de Poincaré',
 'For commutative Poincaré objects, tensor product with tensor trace is again Poincaré and realizes the product in the category of commutative gauged bivariant algebras, even for cones whose source pairing is degenerate: the unique algebra map A⊗B→E has a unique adjoint because the target A⊗B is Poincaré. For arbitrary noncommutative source algebras, the two factor images must commute, so the ambient category matters.',
 'The current adjoint proof establishes the larger commutative-category assertion, not merely the Poincaré full subcategory. This is an explicit reconstruction of the ambient convention. Without Poincaré targets, adjoints can fail to exist.',
 'agrees','The notes correctly locate the caveat; the exact ambient category must be recorded rather than importing the ordinary algebra universal property without adjoints.')
item(1025,[29,45,57],'reading question',[38,42],['1188-1198','1294-1301'],
 'spécial; équivalence de catégories',
 'The indexing category is finite nonempty sets, with all set maps, contravariantly. “Special” means that disjoint unions give tensor-product isomorphisms. Evaluation at one point can recover such a special algebraic power system; an unrestricted equivalence for all finite-set systems is false.',
 'The earlier partition example B(I)=Q^{Part(I)}, with pullback along partition restriction and fiber-sum adjoints, has B(1)=Q but B(2)=Q² and is not special. The map from the constantQ system is an isomorphism at one point but not at two points. The current proof checks variance and both bivariant maps. Hua’s November2026 paper §1 Theorem1.2 was opened and its prose proof read: it imposes specialness and multiplicative gauges in the commutative ungraded case. Its reported Lean verification was not run; the pinned appendix URL remains inaccessible.',
 'agrees','Read the equivalence in the preceding special context. The counterexample refutes only the unrestricted reading; it does not refute the qualified proposition attributed to Hua.')
item(1026,[30,52],'reading question',[40],['1242-1258'],
 'A_n ⊂ H*(X^n); graphes',
 'A stable power system requires symmetry invariance, external products landing in A_{n+m}, all indicated pullbacks/pushforwards landing in the corresponding A_m, and the necessary graph classes lying in A_{n+m}.',
 'Two occurrences in the Pro file give only ambient H* targets. Those conditions would be vacuous as written. The n,m≥0 clause also requires an explicit extension to the empty power/unit, since the preceding category used nonempty sets.',
 'agrees','These are scan alarms and statement qualifications, not authorized text changes.')
item(1027,[31,56],'self-flagged step',[42],['1294-1304'],
 'pleinement fidèle; axiomes à préciser; à vérifier',
 'The source proposes recovering a special gauged finite-set system from its one-point algebra and diagonal data, and asks whether specifying δ_* suffices. A finite projective commutative Frobenius algebra with counit determines the comultiplication uniquely; coassociativity follows from adjointness to associative multiplication.',
 'This proves a precise finite-projective/even reconstruction ingredient, not the full unspecified category of all degenerate gauges. Kock Proposition2.4.10 and the finite-set PROP are exact modern comparisons with their hypotheses and inclusion of the empty set kept visible.',
 'agrees','The earlier dual-number example verifies a model, not a proof of every possible axiom system. The page explicitly defers axiom formulation.')
item(1028,[32],'unproved claim',[42],['1283-1305'],
 'X lisse propre ... H*(X^I)',
 'For smooth proper X with a Weil cohomology over a field, Künneth and Poincaré duality make the power cohomologies a special finite-set Poincaré system, with pullbacks, trace-adjoint pushforwards and Koszul tensor symmetry.',
 'The page names k as a distinguished object in degree0; it does not impose H^0(X)=k. No connectedness restriction is added. The Weil-cohomology axioms and the chosen graded conventions are the hypotheses.',
 'agrees','The note has the right construction under the stated Künneth and Poincaré axioms. Degree interval[1,d] is separately alarmed.')
item(1029,[40,44],'idea of the earlier run',[],[],
 'No supplied direct witness for Φ→E, L and π_i.',
 'The earlier notes compare the kernel realization with an independently specified universal Lefschetz algebra map Φ→E, including prescribed projector images, and with nonuniqueness from L alone. Cote11 provides a place for such operators, but no such chosen map appears in this segment.',
 'Cote16/015–018 and /051 are unprovided endpoints. This is retained in the external-project/other-folder links only; no theorem or completed motive construction is attributed to the current manuscript.',
 'agrees','The notes distinguish their comparison from written construction; that distinction must survive consolidation.')
item(1030,[50],'reading question',[15],['503-519'],
 '= x (at the end of the graph computation)',
 'The graph correspondence of f:X→Y acts as f_* on A(X); the final x in the displayed calculation must have target A(Y) and should mathematically be f_*x.',
 'Both Pro and Codex retain terminalx, so this is a shared reading/source-slip alarm. No scan is available to decide which.',
 'agrees','Earlier lines explicitly state the desired f_* action; the terminal equality is incorrectly typed except in special identity situations.')
item(1031,[51],'reading question',[36],['1152-1161'],
 'φ_A(f_*(x))',
 'With f_*:A→B, the adjointness diagram uses φ_B(f_*x), not φ_A(f_*x). Its degrees balance as i′=i+d′−d.',
 'This is a domain/codomain diagnosis, independent of the eventual choice of graded transpose convention.',
 'agrees','The formula on34 already has the correct target duality map. The scan must decide the symbol on36.')
item(1032,[53],'reading question',[42],['1283-1286'],
 'degrés [1,d]; Objet particulier ... k de degré0',
 'The interval[1,d] excludes a degree-zero unit, contradicting the next distinguished object k in degree0 and the preceding nonnegative graded-algebra setup.',
 'The mathematically coherent alternative is[0,d], but it is a proposed reading only.',
 'agrees','The internal contradiction is immediate and cannot be resolved by importing a different grading silently.')
item(1033,[54],'reading question',[42],['1287-1298'],
 'A_∅ or A_ω (uncertain)',
 'The displayed scalar/augmentation object is ambiguous between an empty-index object and the coefficient/gauge object. The finite-set category at this point was explicitly nonempty, so an empty object would require enlargement.',
 'Keep both alternatives until the scan is read; the modern unital PROP includes the empty set but does not settle the ink.',
 'agrees','The index affects unit and counit axioms, so it is not harmless notation.')
item(1034,[55],'idea of the earlier run',[3,7,11,27,42],['31-48','176-229','378-384','841-868','1300-1304'],
 'No dual-number example is written on these pages.',
 'For A=Q[t]/(t²),deg t=2 and κ(t)=1,κ(1)=0, u=a+bt₁+ct₂+dt₁t₂ acts on basis(1,t) as [[b,a],[d,c]]. Convolution is matrix multiplication; Δ=t₁+t₂ acts as identity. The four kernels t₁,t₂,t₁t₂,1 give the matrix units.',
 'This is an earlier-run example, now independently computed. It models H*(P¹) and gives a precise nonindependence test for later “basis” lists. It does not certify the unspecified universal Φ algebra from another folder.',
 'agrees','All coefficient identities and diagonal/Frobenius identities are reproduced in saved code with exact coefficients.')
item(1035,[60],'idea of the earlier run',[],[],
 'No Oda theorem or Dieudonné module assertion occurs here.',
 'The earlier run suggests comparing de Rham realization of correspondences with Oda’s relation between H¹_dR of an abelian variety over a perfect characteristic-p field and the Dieudonné module of its p-kernel. Its broader smooth proper comparison uses the dual module of the Picard p-torsion, with a k-point hypothesis.',
 'Oda1969 Corollaries5.11–5.12, printedp131, are checked for these precise comparisons. The p-kernel is not silently replaced by its full p-divisible group. No equivalence for every motive, all degrees, or arbitrary bases is inferred. The external archive endpoints remain leads.',
 'agrees','This is a research lead and is not promoted to a manuscript conjecture or theorem.')
item(1036,[61],'idea of the earlier run',[3,11,13,21,23,25],['31-48','378-384','420-470','681-726','744-765','785-799'],
 'u(x)=p_{2*}(u p_1^*(x)); de type A′',
 'The earlier note explicitly reports the cote47 kernel functor Rp2*(Lp1*F⊗L) and its K-class operator [F]↦p2*([L]p1*[F]), comparing the same pull–multiply–push pattern on these cote11 pages. It asserts no equivalence of derived and correspondence categories.',
 'The cote47 endpoint and its relative/properness hypotheses are absent here. A separate current model with X proper flat of finite presentation overS and perfectL is certified by Stacks0FYP; this does not identify the missing historical setup.',
 'agrees','Retained as the note’s specific K-class comparison, with modern conditional support and an explicitly unavailable archive endpoint. No Lefschetz or realization-injectivity question is substituted.')
item(1037,[62],'unproved claim',[4],['57-75'],
 'SL(n+1) ... PGL(n); r_i multiples de n+1',
 'In the reused GIT typescript, SL_{n+1} linearizes O(1) on P^n; suitable powers descend through its central μ_{n+1} to the projective linear group. Requiring each r_i divisible by n+1 is a sufficient condition for the tensor product line bundle on configurations.',
 'The text is identified with Mumford’s GIT by matching mathematical passages, not assigned to Grothendieck as author. Under the diagonal action, total weight divisible by n+1 is the sharper central-kernel criterion; it is an editorial refinement, not a correction of the stated sufficient condition.',
 'agrees','The external Chapter1 reference is real; the physical typescript date/version is not determined by the textual match.')
item(1038,[63],'unproved claim',[6],['146-174'],
 'arithmetic moduli; characteristic p',
 'The reused GIT text motivates arithmetic moduli and announces a quotient construction for configurations overZ, while warning about characteristic-p difficulties in the preceding general theory.',
 'This is Mumford’s programme in the reused document, not a new motivic conjecture. The subsequent configuration construction is partly supplied across both cote11 packages; broad later moduli theory does not identify every announced application.',
 'agrees','The note correctly distinguishes announcement from proof. The later book match confirms provenance and development, not the date of this sheet.')
item(1039,[64,66],'self-flagged step',[8,10,12,14,16],['238-259','303-325','391-418','476-501','558-566'],
 'left to the reader; any subset S',
 'For finitely many rational linear forms and a rational positive-definite norm, the normalized piecewise-linear weight attains its extremum on a rational ray, under the nonempty-domain assumptions. Proposition2.17 reduces normalized numerical weights to finitely many such cases. Proposition2.18 uses boundedness and a uniform positive stable margin to preserve stability for a large tensor power.',
 'The printed assertion “any subset S” needs S≠∅; if it also requires an actual cocharacter ray, the relevant cocharacter space must be nonzero. Neither an empty infimum nor an empty spherical building has an attaining point. Exact inequalities are checked separately.',
 'agrees','The earlier empty-set alarm is sound; the trivial-group/rank-zero edge is added by this run. The positive mathematical result is standard GIT with those quantifiers.')
item(1040,[65],'conjecture',[16,18],['551-566','631-653'],
 'Tits ... centre',
 'The reused text reports Tits’s centre expectation for a suitable convex subset of the spherical building, alongside convexity consequences of numerical instability. The exact class of convex subsets in this informal formulation must be retained.',
 'The modern centre theorem for convex subcomplexes and Kempf’s optimal destabilizing parabolic are distinct results. Ramos-Cuevas completes the exceptional building cases; Kempf treats unstable vectors with an invariant rational norm. Neither is cited as proving every informal convex-subset wording automatically.',
 'agrees','Attribution is to Tits in Mumford’s reused text. The broader geometric building claim and the GIT instability case are separated in the claims map.')
item(1041,[67],'unproved claim',[20],['665-678'],
 'independent of the torus',
 'The apartment segment between two cocharacter rays is intrinsic to the spherical building; commuting cocharacters give the needed inclusion of parabolics along positive linear combinations.',
 'The current excerpt starts an argument whose continuation is not in that scan. A root-space proof is supplied as an independent check; it does not manufacture the missing sheet.',
 'agrees','The notes correctly identify an incomplete local sequence, while the published GIT text contains the statement.')
item(1042,[68],'unproved claim',[22],['733-739'],
 'Tits; geodesic',
 'The reused text cites the intrinsic geodesic statement for nonopposite points of a spherical building and the apartment/antipode lemma. Uniqueness is only for distance<π, not antipodal endpoints.',
 'This is building theory attributed to Tits. The exact radius qualification is indispensable; no new proof by Grothendieck is asserted.',
 'agrees','The source expressly cites external work rather than supplying a full proof here.')
item(1043,[69],'unproved claim',[24],['769-782'],
 'hemispheres; spherical simplex',
 'For a parabolic subgroup, the compatible rays in an apartment are cut out by root half-space inequalities and form the corresponding spherical face/simplex, with the central torus treated separately.',
 'The source itself restricts the simplex assertion to semisimpleG. For general reductiveG it gives only the root-half-space intersection; no missing semisimplicity hypothesis is alleged.',
 'agrees','The note correctly records two abbreviated derivations; the source explicitly qualifies the simplex assertion by semisimplicity.')
item(1044,[70],'reading question',[26],['803-810'],
 'theorem [blank]',
 'The reused proof invokes extension of a rational character from a torus to an appropriate parabolic in order to distinguish cocharacter classes under a finite-kernel representation; it leaves the reference blank.',
 'A character extends exactly when it is trivial on the coroot directions of the derived Levi. A statement that distinct positive rays always admit χ(λ₁)=0 but χ(λ₂)≠0 misses the negatively proportional case; the surrounding parabolic condition must handle that branch separately.',
 'agrees','The blank is real; a later bibliographic match does not reveal what was written in the original blank. The potential antipodal branch is separately alarmed.')
item(1045,[71],'reading question',[28,30],['878-892','963-990'],
 'P(λ); λ belongs to the radical',
 'The reused text defines P(λ) by existence of lim_{t→0}λ(t)gλ(t)^{-1}, calculates its root spaces and its Levi limit, and derives invariance of numerical weights under P(λ). A local deletion affects part of the proof, not the whole theorem.',
 'For GL(V), an entry of weight r_i−r_j has the indicated limit exactly when nonnegative. This provides a concrete independent check; the general root statement is compared to the published GIT/Kempf treatment.',
 'agrees','The notes correctly avoid treating a local cancellation as wholesale withdrawal. Missing continuation remains identified as such.')
item(1046,[72],'unproved claim',[28,32],['878','1060-1075'],
 'proper; QED',
 'The GIT proper-action argument uses a valuative criterion and a one-parameter-subgroup factorization to identify the relevant limit; its announced equality has a visible concluding QED on the earlier scan28 in the reused-sheet order.',
 'This is a nontrivial GIT theorem with reductivity and stability hypotheses, not a claim that every group action on a stable-looking subset is proper. The document pagination, not scan order, supplies the continuation.',
 'agrees','The earlier notes correctly locate the visible continuation. The check here verifies linkage and statement, not a new complete proof of the valuative theorem.')
item(1047,[73],'unpursued implication',[35],['1129-1145'],
 'SGA 8 §1',
 'The GIT quotient construction descends the determinant line bundles and their invariant sections along its principal bundle. The cited “SGA8” is an exposé reference to faithfully flat descent, not an otherwise nonexistent eighth seminar volume.',
 'SGA1 ExposéVIII Theorem1.1 gives effective descent of quasi-coherent modules and Proposition1.10/Remark1.12 preserve locally free rank1 objects; section descent follows from full faithfulness. Those hypotheses must be checked on the stated principal bundle.',
 'agrees','Both the source phrase and the published descent theorem were checked. The exact historical typescript numbering remains a bibliographic qualifier.')
item(1048,[74],'unproved claim',[35],['1138-1145'],
 'U_stable; ample',
 'The stable configuration locus is defined by strict inequalities #(points inL)/(m+1)<(dimL+1)/(n+1) for proper projective linear subspaces L. The typescript announces openness and ampleness of a descended tensor line bundle on its quotient.',
 'The completion is visible in the other supplied Pro package:11/054 L430–440 and11/052 L387. It proves the quotient is quasiprojective using invariant affine neighborhoods. This link was read at both endpoints.',
 'understates','The entry’s local page lacks the conclusion, but the supplied second package contains it. The two-package status is stronger than an unresolved announcement.')
item(1049,[75],'unproved claim',[37,39],['1169-1179','1205-1238'],
 'Proposition3.3; QED',
 'The reused GIT text characterizes configurations with finite projective stabilizer by their indecomposability under complementary projective subspaces, expresses this through R-partitions, and begins gluing the resulting local quotients.',
 'The criterion concerns the precise configuration group and the stated regular locus. The proof spans the reversed typescript pagination of scans39 and37; the quotient programme continues in the later package.',
 'agrees','The source contains a proof of the covering/regular-locus proposition; labelling the whole entry “unproved” should not hide that proof.')
item(1050,[76,78],'unproved claim',[41],['1265-1279'],
 'cone C_x; Proposition3.6',
 'The nonvanishing determinant incidence vectors generate a rational cone. A stable configuration is characterized by existence of monomials of multidegrees (N−N₀,N,…,N) and their permutations, with N≥N₀>0. The proof reduces this to the interior of the cone and a greedy independent-point flag.',
 'Continuation is supplied in MPL_11_043-058+56_transcription.tex:58 L650–689 and56 L514–550; the separating functional must be nonzero. Typed page3.16 remains absent, so the final inequality step is a reconstruction even though the modern criterion is known.',
 'understates','The local entry ends unfinished, but much of the continuation is attached in the adjacent package. Both sides were actually read.')
item(1051,[81,82],'other',[],[],
 'No historical source passage; these are the prior run’s audit and bibliography lists.',
 'The earlier note lists searches, finite calculations and primary references used in its run. Their named scripts, frozen ledgers and retrieved cards were not included in the present attachment. This run repeats the computations it relies on and records newly opened references independently.',
 'A listed or DOI-linked reference is not automatically verified; every citation in the current bibliography states whether theorem text, abstract or metadata was actually inspected. Hua’s appendix remains unavailable.',
 'overstates','The earlier note’s verification labels report its own run. They are not evidence that the underlying code or references were opened in this run.')

# Codex leads: no index verdict rows; scans are kept exactly as each witness labels them.
item(1052,[],'withdrawn in the same text',[22,66],['2-17'],
 'démonstration ... 11.9.6; plus néc que A′ soit projectif',
 'Cancelled EGA-style drafts develop preservation of a separating family after flat base change, using generic freeness and induction on associated points/support. The lemma weakens projectivity to generic freeness after every integral quotient, but its preceding proposition and some formula slots are absent.',
 'The mathematically expected generic-freeness clause is B′_h free overB_h for B=A/p and B′=B⊗_A A′. Pro12/072 L444–449 repeats Codex12/066 L13–17 with the same defect but a different scan label. Exact equality of this fragment with a final EGA proposition requires the missing hypotheses.',
 'agrees','Codex notes correctly identify a cancelled proof fragment. It is attributed to Grothendieck–Dieudonné’s EGA drafting context, not to the motive construction; exact typist/date are unknown.',cote='12',file=B,extra={'lead_sources':['sources/notes/codex/B12-01_notes.md'],'parallel_lines':['sources/texts/pro/MPL_12_051-098_transcription.tex:444-449']})
item(1053,[],'conjecture',[68],['22-30'],
 'B est-il intègre ? ... nous ignorons',
 'A cancelled draft asks: for a flat local homomorphism of Noetherian local rings A→B with geometrically integral closed fiber and excellent geometrically unibranch A, is B integral? The text says one may reduce to normalA and reports characteristic-zero and essentially-finite-type positive cases, but ignorance even for completeA,B with trivial residue extension.',
 'The intended question is about reduced/integralA (the preceding discussion concerns integrality). Modern geometric unibranchness alone permits nilpotents, so literal wording without reducedness has the elementary counterexample A=B=k[ε]/ε². That counterexample does not settle the intended normal-base question.',
 'agrees','The exact open question, known cases and cancellation are retained. It is not dismissed merely because the paper is reused.',cote='12',file=B,extra={'lead_sources':['sources/notes/codex/B12-01_notes.md']})
item(1054,[],'unproved claim',[68],['26'],
 'A⊗_R C ... étale ... non intègre',
 'The draft gives an integral complete real node A=R[[X,Y]]/(X²+Y²), unibranch but not geometrically unibranch; its finite étale complexification is not integral, because X²+Y²=(X+iY)(X−iY). It also describes a nodal-curve étale example.',
 'Double brackets are a reconstruction from “complet”; the diplomatic notation leaves them blank. The algebraic point explains why ordinary unibranchness is insufficient. The real quadratic has no real linear factors, so the completed plane-curve quotient is a domain.',
 'agrees','The counterexample is mathematically sound with the reconstructed power-series notation; the notation itself remains an ink question.',cote='12',file=B)
item(1055,[],'unproved claim',[70,83],['59-78','107-123'],
 'Théorème7.5.1; toutes les fibres ... Q géométrique',
 'The cancelled EGA draft proposes a general local-to-all-fibers criterion for a flat local mapA→B with finite residue extension: a local propertyR stable under lifting across regular elements and open on finiteB-algebras, with A universally Japanese and regular generic loci on finite integralA-algebras, ascends geometrically from the closed fiber to all fibers. It lists depth/codepth, Serre, Cohen–Macaulay, regularity, normality, integrality and reducedness variants.',
 'The text alternatesR andQ and has missing relation signs. Final EGAIV2 §7.5 is the comparison target, but each property’s auxiliary hypotheses must be read individually; excellentB is a convenient common sufficient assumption, not an automatic omitted hypothesis.',
 'agrees','The drafting comment says the old statement was too narrow for what the proof established. Cancellation is recorded without implying that every listed case is false.',cote='12',file=B)
item(1056,[],'unproved claim',[81],['83-100'],
 'Proposition4; Proposition5; Corollaire6',
 'A cancelled EGA fragment gives: a length-one hypersurface section criterion for a unique generically reduced component and a regular parameter; reducedness ofF from reducedF/tF whenV(t) contains no component ofSuppF; specialization of associated components under an F-regular t; and descent of the no-embedded-components condition fromF/tF toF.',
 'The preceding conditions1/1(ii), the exact definition of a reduced module and the missing inequality are not supplied. Standard local statements can be compared, but a theorem with all original quantifiers cannot be recovered by filling these slots.',
 'agrees','The last three arguments refer to other numbered results and the visible corollary; a “reste à prouver” followed by that reference is not necessarily a surviving open problem.',cote='12',file=B)
item(1057,[],'unproved claim',[85],['128'],
 'On se gardera de croire ... intersection',
 'Flat finite-type base change need not preserve an infinite intersection of ideals. For a DVR A and J_i=m^i, their intersection is zero, but for B=Frac(A)=A[1/π], everyJ_iB=B.',
 'B is a flat finite-typeA-algebra (one localization generator). This checks every displayed hypothesis; no faithful-flatness or locality is asserted here.',
 'agrees','The draft’s counterexample is correct and explains the distinction from finite intersections. Missing intersection symbols are scan alarms.',cote='12',file=B)
item(1058,[],'self-flagged step',[85],['130-138'],
 'Nous ignorons si ... S quelconque; relativement à S; cf SGAD IX4.2',
 'The draft asks whether a schematically dominant family over a field stays so after every base change, defines universal schematic dominance, and states lifting across a nilpotent closed base when X and allZ_i are flat overS. It reports the locally Noetherian case as positive.',
 'EGAIV3 Proposition11.10.6 answers the arbitrary field-base-change question affirmatively; Definition11.10.8 and Theorem11.10.9 organize the relative version. The ordinary nilpotent lemma is false without more hypotheses: for S=Spec Q[x,ε]/(ε²,xε), X=S and Z=D(x), density holds over S_0=Spec Q[x] but fails overS. The opened SGA3II ExposéIX Lemma4.2 and EGAIV3 11.9.15 require every J^n/J^(n+1) locally free on S_0, which need not itself be reduced.',
 'agrees','The draft is faithfully recorded, but its ordinary nilpotent assertion is refuted. The field-base-change question is answered in the later publication. The universal-relative variant is kept distinct.',cote='12',file=B)
item(1059,[],'unproved claim',[100],['160-180'],
 'Formalism of Algebraic Cohomology Classes; ρ_X:C^i(X)→H_l^{2i}(X)',
 'The English reused sheet constructs a rational cycle-class map by trace adjointness to restriction, asserts independence of rational equivalence and multiplicativity, and defines cohomological equivalence as its kernel.',
 'To state it precisely use smooth proper equidimensionalX over an algebraically closed field, ℓ invertible, and Tate twistH^{2i}(X,Q_ℓ(i)); singularZ requires its fundamental class/trace on top compactly supported cohomology, not Poincaré duality onZ. Those hypotheses may belong to missing preceding pages. The author of this English sheet is not identified by an explicit byline.',
 'understates','The text assumes a cohomology formalism already established. Merely defining the functional on cycles does not prove rational-equivalence invariance or intersection compatibility; these are separate asserted results.',cote='12',file=B)

# Per-entry judgments are manual, after reading each complete entry and source.
V={
1:(1001,'corrected','Keep the 39/20/19 inventory; freeze/hash/696-element claims are reports of the earlier run, not independently available evidence.'),
2:(1002,'corrected','The printed side is checkable, but all draft-letter cote16 endpoints are absent. Preserve the qualified earlier-run dictionary as a lead.'),
3:(1003,'kept','The inverse-map identity is correct and independently proved; its cote16 attribution remains an unavailable witness.'),
4:(1004,'kept','The coefficients, composition order and factorial-square identity are correct; finite-string computations repeated.'),
5:(1002,'merged','Confirms no standard-conjecture list in cote11; the surrounding universal-quantifier claims depend on absent cote16.'),
6:(1005,'kept','Kernel, graph and realization maps occur on3,9,11–13; the additional Φ→E comparison is retained separately in SA05-1029.'),
7:(1006,'kept','The restriction functor has exactly the stated maps; add the isomorphism/sign reading qualification from Codex.'),
8:(1007,'kept','Correct formal additive construction, explicitly editorial; object corners do not silently identify graded-piece corners.'),
9:(1008,'kept','Degreeq−d_X follows from the trace-degree convention; the dual map typo is retained in SA05-1031.'),
10:(1009,'kept','The literal-set/ring objection is valid already at a point; additive closure is a proposed refinement only.'),
11:(1010,'kept','The completion and twist maps match the opened Stacks convention and are not attributed to these pages.'),
12:(1010,'merged','Same precise modern correspondence/motive comparison; independent bibliographic checks recorded.'),
13:(1011,'kept','Exchange is deferred and specific squares are used; the general Cartesian criterion is genuinely asked on31.'),
14:(1012,'kept','Sign warnings and the explicit29 retraction are present; distinguish them from the successful even-degree continuation.'),
15:(1013,'kept','The source identifies and proves diagonal units and their action.'),
16:(1014,'kept','Both transpose multiplicativity and the graph/realization compatibility are explicitly marked for checking.'),
17:(1015,'kept','The coefficient replacement maps occur, with central/graded scalar qualifications.'),
18:(1016,'kept','Centrality is used in the trace exchange; Codex marginal punctuation remains uncertain.'),
19:(1017,'kept','The monoid proposal and parity involutions are unfinished; the editorial encoding is explicitly separated.'),
20:(1018,'kept','Selected-morphism generalization is a real deferred step; exact closure axioms are not supplied.'),
21:(1019,'corrected','A multiplication/composition proof sketch exists. Additive or scalar closure still needs to be explicit for a ring system.'),
22:(1020,'corrected','Adjoint pushforward is defined and its projection/functoriality identities are checked on27/34; “unproved” alone understates the page.'),
23:(1021,'kept','Gauge freedom and the distinction between algebra and good isomorphisms are present, including the42 scalar twist.'),
24:(1012,'merged','Same tensor-pushforward retraction and even-degree restriction asH02.'),
25:(1011,'merged','Same general exchange question asH01, now with the exact31 criterion and independent scalar-gauge counterexample.'),
26:(1022,'kept','The projection-formula parity discrepancy is explicit and independently computed.'),
27:(1023,'kept','Keep as a programme statement; no particular universal construction is specified.'),
28:(1024,'corrected','Tensor of Poincaré targets is a product even in the wider commutative gauged bivariant category, by a separately checked adjoint argument; arbitrary noncommutative sources require commuting factor images.'),
29:(1025,'kept','The equivalence is safest under the preceding special condition; unrestricted evaluation is refuted, without changing the text.'),
30:(1026,'corrected','Two ambient cohomology targets are too weak; preserve the proposed A_m/A_{n+m} readings and empty-power issue as alarms.'),
31:(1027,'kept','Full faithfulness, axioms and sufficiency ofδ_* are explicitly deferred. Frobenius results address a precise restricted model.'),
32:(1028,'kept','The smooth-proper construction follows from the specified Künneth and Poincaré axioms, with an explicit graded convention; no H^0=k restriction is written.'),
33:(1005,'merged','Same kernel-realization construction; the unavailable cote16 comparison remains a lead.'),
34:(1006,'merged','Same stable-system inclusion map; no identification of kernels with their operator images is inferred.'),
35:(1009,'merged','Cycle generators under resolution fit the literal-set issue; span and coefficient closure remain necessary.'),
36:(1009,'merged','Same point counterexample and monoid-versus-ring qualification; the monoid programme also appears in SA05-1017.'),
37:(1019,'merged','Same generated-system operations; compositions are explicit but additive closure must be supplied.'),
38:(1016,'merged','Same central-kernel adjointness computation; even cycle classes are a specialization, not a proof of all graded signs.'),
39:(1008,'merged','Same degree transport, with distinct kernel and operator degrees.'),
40:(1029,'corrected','The chosen Lefschetz-map/projector data are not attached; preserve only as attributed earlier-run comparison.'),
41:(1010,'merged','Same idempotent/twist completion comparison, with precise Stacks arrows.'),
42:(1007,'merged','Same object-corner construction; missing cote16 endpoint remains explicit.'),
43:(1017,'merged','Same monoid weakening, not a completed additive or motivic category.'),
44:(1029,'corrected','Cote16/051 is absent; no direct verification of its nonuniqueness claim is possible in this part.'),
45:(1025,'corrected','Specialness comparison is mathematically correct; pinned Hua source was inaccessible in this run and remains unverified, not a checked theorem.'),
46:(1002,'corrected','Cote11/027 A names the Poincaré category. No standalone draft-letter dictionary is licensed by this source.'),
47:(1003,'merged','Same correct inverse-map calculation; its historical comparison still has an absent endpoint.'),
48:(1002,'corrected','The isolated source letters/primitive-projector comparison relies on absent cote16; do not infer a four-letter permutation.'),
49:(1002,'corrected','Keep quantified comparison to printed statements as an external lead, including polarization and product hypotheses.'),
50:(1030,'kept','Terminalx is incorrectly typed; both independent transcriptions retain it, so the scan/source slip remains unresolved.'),
51:(1031,'kept','φ_A(f_*x) has the wrong target. Earlier adjoint formula and degree balancing suggestφ_B.'),
52:(1026,'merged','Same missing stable-system target conditions asH18; not corrected in the diplomatic text.'),
53:(1032,'kept','[1,d] contradicts the distinguished coefficient object in degree0; proposed[0,d] remains a scan alarm.'),
54:(1033,'kept','Empty-set versus scalar-object notation changes the indexing category and must await ink.'),
55:(1034,'kept','The dual-number realization, convolution and diagonal calculations are correct and re-executed, without certifying absentΦ data.'),
56:(1027,'merged','The Frobenius/diagonal example is a restricted model forH19, not a full proof of unspecified axioms.'),
57:(1025,'merged','The partition example refutes only unrestricted evaluation and fails specialness exactly as stated.'),
58:(1011,'merged','The Cartesian gauge square is a valid abstract counterexample; all arrows, dimensions and universal property checked.'),
59:(1022,'merged','Same complete parity calculation for the two projection formulas.'),
60:(1035,'kept','Oda is a separate research lead; Cor5.11 is checked with its abelian/perfect-field/H¹ restrictions.'),
61:(1036,'corrected','The note gives the explicit K-class pull–multiply–push comparison; retain that formula, distinguish a verified modern perfect-kernel model, and mark cote47 hypotheses unavailable. No equivalence or injectivity assertion is supplied.'),
62:(1037,'kept','Linearization and sufficient divisibility are standard GIT content, attributed to the reused document; exact physical edition/date unknown.'),
63:(1038,'kept','Arithmetic moduli is an announcement in the reused GIT programme, not a new motive claim.'),
64:(1039,'kept','The rational-ray exercise is a real omitted verification; the finite rational cone hypotheses are retained.'),
65:(1040,'corrected','Separate Tits convex-subcomplex centre theorem from Kempf instability and the potentially broader informal convex-set formulation.'),
66:(1039,'merged','S≠∅ is required for attainment; add the rank-zero/empty-ray edge. No transcription alteration.'),
67:(1041,'kept','The intrinsic-line argument is locally incomplete and has a standard root/parabolic interpretation.'),
68:(1042,'kept','Retain Tits attribution and the nonantipodal-distance qualification.'),
69:(1043,'kept','Root half-spaces and the semisimple spherical-simplex claim are stated with abbreviated derivations; the source already gives the semisimple qualification.'),
70:(1044,'kept','The character-reference blank is real; exact extension and antipodal-ray qualifications are preserved.'),
71:(1045,'kept','The local cancellation does not withdraw the whole faithful-representation/parabolic proof.'),
72:(1046,'kept','The proper-action proof really continues toQED at28; document pagination resolves reversed scan order.'),
73:(1047,'kept','The SGA exposé descent reference is checked againstSGA1 VIII, with the principal-bundle hypothesis retained.'),
74:(1048,'corrected','The announced ampleness is completed in the attached second package,11/054 and11/052; both endpoints read.'),
75:(1049,'corrected','The regular-locus covering proposition has a visible proof; the later quotient programme is a separate continuation.'),
76:(1050,'corrected','Much of the cone proof continues in attached11/058 and11/056; typed3.16 still absent and nonzero separator is essential.'),
77:(1005,'merged','Summary entry covers the handwritten line, consolidated acrossSA05-1005–1033; it is not a distinct mathematical assertion.'),
78:(1050,'merged','Summary entry covers the reused typed line, consolidated acrossSA05-1037–1050; no duplicate claims created.'),
79:(1001,'corrected','Archive sheet numbering is not established authorial manuscript foliation; keep titles and archive locators distinct.'),
80:(1001,'merged','Document titles and internal typescript pagination are recorded, without inferring a composition date.'),
81:(1051,'corrected','Prior audit artifacts are not attached; current code/output and search events are independently saved.'),
82:(1051,'corrected','Reverify each reference at its actual opened depth; no inherited verified status, especially forHua.')}
for i in range(1,83):entry(i,*V[i])

def dump():
 ROOT.mkdir(parents=True,exist_ok=True)
 for name,data in [('items',items),('claims',claims),('problems',problems)]:
  if data:(ROOT/f'{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'entries.tsv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(entries)
 expected={r['entry_id'] for r in csv.DictReader(open('sources/notes/NOTES_INDEX.tsv'),delimiter='\t') if r['entry_id'].startswith(PK+'#')}
 assert expected=={r['entry_id'] for r in entries} and len(entries)==82
 assert len({i['id'] for i in items})==len(items)
 print(f'Manual entries={len(entries)}; consolidated items={len(items)}; all82 index IDs covered exactly once.')

if __name__=='__main__':dump()
