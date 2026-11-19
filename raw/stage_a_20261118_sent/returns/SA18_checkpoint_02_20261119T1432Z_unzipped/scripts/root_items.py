"""Serialize the root's individually read, manually authored Stage-1 decisions.

Every call below is a scientific decision written after reading its note and
transcription, not a rule inferred from headings, keywords or scan numbers.
"""
from pathlib import Path
import json,csv,datetime
BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'parts/root';OUT.mkdir(parents=True,exist_ok=True)
PKG='MPL_11_043-058+56'
P='SA18_texts/pro/MPL_11_043-058+56_transcription.tex'
Q='SA18_texts/pro/MPL_16+47+54+44_transcription.tex'
items=[];entries=[];events=[]
def I(nums,kind,cote,scans,lines,words,statement,reconstruction,check,reason,verdict=None):
    item_id=f'SA18-{11001+len(items)}'
    nums=[nums] if isinstance(nums,int) else nums
    items.append(dict(id=item_id,sources=[f'{PKG}#{n}' for n in nums],kind=kind,
      cote=cote,scans=scans,lines=lines,his_words=words,statement=statement,
      reconstruction=reconstruction,check=check,check_reason=reason))
    for j,n in enumerate(nums):
        v=verdict or ('kept' if j==0 else 'merged into '+item_id)
        if v=='kept':v='kept (as '+item_id+')'
        entries.append(dict(entry_id=f'{PKG}#{n}',item_id=item_id,verdict=v,reason=reason))
    events.append(dict(statement_id=item_id,date='2026-11-19',who='GPT-6 Astra Pro / inherited effort (not numerically exposed) / SA18 root',type='used and rechecked in this run',outcome='Compared each assigned note with the cited transcription; '+check+': '+reason))
    return item_id
def L(a,b,file=P):return dict(file=file,start=a,end=b)

# Correspondence pages and the reused configuration typescript.
I([1,29,30],'reading question',[11,16],{'11':[44,46,48],'16':[40,42,44,45,46,47,48,49]},[L(32,175)],'Formalisme des correspondances; A(I\u2032;I)',
 'The correspondence action in cote11 can realize the operators discussed in cote16. Draft C concerns algebraicity of inverse Lefschetz operators and so matches published standard conjecture B; draft A concerns Lefschetz on algebraic classes. No complete permutation of the draft letters B,D is justified by these selected definitions.',
 'The published-letter concordance is an editorial comparison. Cote11 itself contains no A–D list; cote16 supplies the relevant statements, with second-pass readings controlling that witness.',
 'agrees','The notes explicitly call the concordance partial and do not assign unused letters by elimination. Their claims about c16 are cross-checked in the agent16 source review; the c11 action is at lines32–44 and84–175.')
I([2,7],'unpursued implication',11,[44,46,48],[L(32,44),L(84,175),L(215,251)],'v\u2218u=p_{31*}(p_{21}^*(u)p_{32}^*(v))',
 'For smooth projective varieties over a field, Chow correspondences compose by pullback to the triple product, intersection, and proper pushforward. With target-first notation A(I\u2032;I), this identifies the written operation on powers of a fixed X with ordinary correspondence composition.',
 'Smooth projectivity, Chow codimensions, rational coefficients, idempotent completion and Tate twists belong to the modern realization, not to a completed construction on these sheets. The source leaves associativity/units for verification.',
 'agrees','The formula and factor order are actually present. The introductory note correctly labels the subsequent motives construction as an added comparison, not a manuscript theorem.')
I(3,'unproved claim',11,[44],[L(22,29)],'pas seulement mod torsion',
 'A proposed coefficient-ring version requires full Poincare duality over the chosen ring, including torsion-sensitive information. The ordinary pairing H^i→Hom(H^{D−i},R) is perfect only under suitable projectivity/duality hypotheses; it is not automatic for arbitrary integral cohomology.',
 'The explicit pairing map is the earlier run\u2019s test. The manuscript makes the duality assumption rather than asserting that all varieties satisfy it integrally.',
 'agrees','The conditional wording "lorsqu\u2019on a" and "telle que" prevents reading the sentence as an unconditional integral duality theorem.')
I([4,34],'unpursued implication',[11,16],{'11':[44,46],'16':[49]},[L(25,27),L(84,92)],'numérique, homologique; Picard, Albanese',
 'The sheet proposes cycle quotients as examples of a bivariant formalism while explicitly withholding Poincare properties. For smooth projective varieties and an adequate equivalence relation, quotienting correspondences is compatible with intersection and push–pull. Numerical motives with rational coefficients are semisimple; identifying a homological kernel with its radical needs the separate hypotheses in the cited later result.',
 'Adequacy, the completed motivic categories and Jannsen\u2019s theorem are modern specifications. No semisimplicity proof occurs in cote11.',
 'agrees','The negative sentence about being special/Poincare is retained. The later theorem is kept as literature, and the manuscript\u2019s mere list is not upgraded to its proof.')
I(5,'unproved claim',11,[44],[L(29,29)],'K(X) [jaugé par χ], considéré comme gradué de degré 0',
 'The source proposes degree-zero K-theory with Euler characteristic as trace. In a smooth proper setting pushforward is the alternating derived pushforward, and comparison with Chow theory requires a Todd-class correction in Riemann–Roch.',
 'The hypotheses and Todd correction are modern reconstruction. The note correctly does not say that the raw Chern character or total Chern class preserves χ.',
 'agrees','Only the K(X), degree-zero and χ example is on the page; the proposed comparison is explicitly separated.')
I(6,'self-flagged step',11,[44,46],[L(39,44),L(166,175)],'prendre Cy ou yC !; OK mod signes',
 'The correspondence action and composition must use a consistent graded multiplication order. For homogeneous elements of cohomological degrees c,d, interchanging them contributes (−1)^(cd); for Chow classes in even cohomological degrees this particular Koszul sign is trivial.',
 'The Koszul formula and the even-degree specialization are explicit modern checks, not a settled manuscript convention.',
 'agrees','Both order choice and final sign warning occur in the actual calculation, so the flagged issue is genuine.')
I(8,'self-flagged step',11,[46],[L(136,175)],'"axiome cartésien" oublié !',
 'Compatibility of correspondence actions with composition uses base change for the Cartesian projection square, followed by the projection formula and transitivity of pushforward. For Chow groups, the relevant base change is proper pushforward against flat pullback.',
 'The named Chow hypotheses specify one valid realization; the abstract bivariant axioms are not all stated here.',
 'agrees','The displayed calculation explicitly inserts the missing Cartesian compatibility at lines143–156.')
I(9,'self-flagged step',11,[48],[L(215,251)],'Il faut encore définir|vérifier l\u2019associativité',
 'The diagonal correspondence acts as identity by the projection formula. The stronger categorical assertions that composition is associative and diagonals are two-sided units are left as an explicit obligation in the source.',
 'In the Chow realization these assertions follow by expressing both triple composites on a fourfold product. That proof is supplied separately in the computation/proof record, not attributed to the sheet.',
 'agrees','The identity-action calculation is complete, but action alone need not establish equality of correspondences. The note correctly preserves that distinction.')
I(10,'reading question',11,[51],[L(302,325)],'base; y_1 y_2 y_3',
 'The two-factor table lists 1; y1,y2,Δ; and a top product containing an impossible third factor. Even after reading the top term as y1y2, the three middle classes need not be independent: for X=P1, Δ=y1+y2.',
 'The candidate deletion of index3 is only a scan question. "Spanning family" is a mathematically defensible interpretation of "base", but is not substituted for the ink.',
 'agrees','The note identifies both the literal index anomaly and the independent mathematical dependence issue.')
I(11,'unproved claim',11,[51],[L(311,356)],'δ²=χ y_1 y_2; δ_{12}δ_{23}=δ',
 'For a connected compact oriented positive-dimensional manifold with a normalized top class, the pairwise and small diagonal classes obey the displayed relations, subject to orientation and graded-sign conventions. In smooth projective Chow theory the self-intersection involves c_d(T_X); replacing it by χ times a chosen point is generally a cohomological simplification, not a universal equality of Chow zero-cycles.',
 'The realization and coefficients are specified here. The earlier note\u2019s P1 computation verifies a model, not all possible cycle theories.',
 'agrees','The formulas are on the page. Their missing general hypotheses remain visible; the note does not claim a general proof.')
I(12,'unproved claim',11,[53],[L(394,424)],'générateurs; relations',
 'For k factors the list counts k top-class pullbacks and binomial(k,r+1) diagonal classes of codimension r dimX. The heading for a full relation ideal is empty. Since larger diagonals are products of pairwise diagonals, the written list is not claimed minimal by a proof.',
 'The codimension convention and redundancy observation are modern clarification; no missing general presentation is filled in.',
 'agrees','The note correctly distinguishes a displayed list from an unprovided presentation.')
I(13,'reading question',11,[55,57],[L(449,464),L(553,560)],'comprenant la partie vide; card R=s',
 'If R contains the empty block and J is empty, the diagonal-block locus is isomorphic to X^(|R|−1), not X^|R|. With b the number of nonempty blocks its dimension is b dimX. The later count is consistent only after dropping the empty block from the counting convention.',
 'The coordinate isomorphism and adjusted variable b are reconstruction. Neither written convention is altered.',
 'agrees','The two literal conventions conflict; the note gives the exact one-block discrepancy.')
I(14,'unproved claim',11,[55],[L(466,508)],'du pt de vue ens.; relation d\u2019équivalence engendrée',
 'The set-theoretic intersection of diagonal-block loci is described by the join of their equivalence relations, with marked-point conditions tracked separately. The product of cycle classes additionally depends on excess intersection and cannot be inferred merely from this common set.',
 'A clean-intersection calculation supplies the excess bundle under smoothness assumptions; it is separate from the source\u2019s set statement.',
 'agrees','The qualifier is explicit on the page. Marked-point compatibility must not be erased in modernization.')
I(15,'self-flagged step',11,[57],[L(553,568)],'s+s\u2032=k+1; ! vérifier; OK',
 'After interpreting s,s\u2032 as numbers of nonempty blocks and assuming their join is connected, b+b\u2032=k+1 is the transverse/tree case. The diagonal product is the small diagonal with no excess factor.',
 'The graph/clean-intersection formulation is reconstruction; the manuscript itself places OK beside its local check.',
 'agrees','This is a source-level check accepted by the author, not an outstanding unanswered question. The earlier empty-block inconsistency remains a separate alarm.')
I(17,'self-flagged step',11,[57],[L(569,587)],'ε_R ε_{R\u2032}=χ? y_{X^k}',
 'For smooth X of dimension d>0 and connected joined partitions with b+b\u2032=k, the excess normal bundle is T_X; cohomologically its top Chern class integrates to χ(X). For larger excess, degree forces the cohomological product to vanish. In CH this gives Δ_*c_d(T_X), which need not equal χ(X) times an arbitrarily chosen degree-one zero-cycle.',
 'The excess-bundle calculation and the Chow/cohomology distinction are the present run\u2019s formulation. The handwritten χ question remains open on the page.',
 'agrees','The preceding OK does not extend to this separate coefficient; the note keeps the authored question mark.')
I(16,'reading question',11,[53,57],[L(412,417),L(567,568)],'δ_{k−1}; δ_k',
 'Both occurrences refer geometrically to the small diagonal X→X^k, but the table uses the number of lost dimensions and the equality line appears to use the number of factors as subscript.',
 'Identifying the underlying map is reconstruction; no preferred subscript is imposed.',
 'agrees','Both transcribed occurrences are cited, so this is a genuine internal notation question.')
I(18,'withdrawn in the same text',11,[57],[L(608,640)],'Stable par comp; Stable par images extraordinaires [deleted]',
 'The tautological system is asserted stable under external products, ordinary simplicial pullbacks, projections and correspondence composition. A separate extraordinary-pullback assertion is cancelled. For projection of a singleton factor, the pushforward convention must be checked rather than treating every diagonal as mapping to a diagonal unchanged.',
 'Modern closure under specified operations can be proved using diagonal/excess formulas. Cancellation records editorial status, not a counterexample to every possible refined Gysin operation.',
 'agrees','The live list and the cancelled paragraph are distinguishable at lines608–636.')
I(19,'idea of the earlier run',11,[51],[L(302,356)],'δ²=χ y_1y_2; δ_{12}δ=χ y_1y_2y_3',
 'In Z[h1,…,hk]/(hi²), the Chow ring of (P1)^k, Δ12=h1+h2 and Δ123=h1h2+h1h3+h2h3. Thus Δ12²=2h1h2, Δ123²=0 and Δ12Δ123=2h1h2h3. Also Δ12−h1−h2=0.',
 'This is the earlier run\u2019s explicit model, independently recomputed in this run; it is not a new conjecture of Grothendieck.',
 'agrees','The test is exactly for P1 and refutes universal independence without pretending to prove all abstract relations.')
I(20,'idea of the earlier run',11,[55,57],[L(466,508),L(553,581)],'Cas d\u2019inégalité',
 'For X=P1, the diagonal products for partitions {12,34} and {13,24} multiply to2h1h2h3h4. Their join is connected and their two nonempty-block counts sum to4, so this is the one-excess case.',
 'An explicit model from the prior run, independently recomputed. Its block-count conversion is essential.',
 'agrees','Exactly two squarefree monomials survive; it is a concrete witness, not the unprovided general proof.')
I(21,'unproved claim',11,[43],[L(6,18)],'The following is obvious: Corollary 3.2',
 'If a G-equivariant trivialization U_R≅G×A_R has been established and U⊂U_R is invariant open, restriction yields U≅G×σ_R^−1(U). Here the typescript writes PGL(n) for projectivities of P^n, i.e. modern PGL_(n+1).',
 'The modern group subscript is explicitly distinguished from the historical notation. This is reused typescript, not assigned authorship from its proximity to handwriting.',
 'agrees','The note correctly treats the corollary as dependent on the earlier chart and its deferred inverse checks.')
I(22,'self-flagged step',11,[45,47,49],[L(53,79),L(182,210),L(264,281)],'mechanical verifications that remain; mutually inverse',
 'For an R-partition with union {0,…,n} and each successive block meeting previous blocks in one index, the nonzero-determinant configuration chart is equivariantly PGL_(n+1)×A^(nν−n). The section fixes the first n+1 points and specified coordinates of the next ν points.',
 'The graph/tree normalization proof and low-dimensional determinant calculation are supplied separately. Missing typed page3.5 is not reconstructed as a manuscript passage.',
 'agrees','Both inverse-composition obligations are explicitly delegated to the reader; the note identifies their actual maps.')
I(23,'other',11,[49,55],[L(264,281),L(449,464)],'R-partition; (R,J)',
 'The R-partition for projective configuration charts is a family with one-point overlaps. The handwritten R for diagonals is a partition into disjoint blocks, including an empty block. These are different combinatorial constructions.',
 'No mathematical map between them is supplied or inferred merely from the shared letter.',
 'agrees','The note correctly rejects an identification by notation alone.')
I(24,'unproved claim',11,[52,54],[L(387,390),L(430,440)],'Theorem 3.8; The first part is clear',
 'For the typescript\u2019s stable regular projective configurations, the constructed quotient is a locally trivial PGL_(n+1)-torsor and has an ample descended product line bundle, hence is quasi-projective. The proof uses invariant affine opens and descent; definitions from missing earlier pages constrain the statement.',
 'No unconditional quotient theorem for arbitrary configurations is inferred. The exact stable locus is the one defined by the preceding typescript, not an invented modern substitution.',
 'agrees','The two reversed-pagination pages contain a genuine proof continuation; the first torsor assertion is compressed, the ampleness argument is sketched with citations.')
I(25,'idea of the earlier run',11,[56,58],[L(538,546),L(676,688)],'it is easy to check',
 'For λ0≤⋯≤λm with sum zero, let tβ=(λ_(β+1)−λβ)/(m+1). Then λ=Σtβvβ, where vβ has β+1 entries−(m−β) and m−β entriesβ+1. This is a linear isomorphism of the sorted zero-sum cone with the nonnegative orthant.',
 'The explicit inverse is the earlier run\u2019s proof, independently rechecked symbolically here. Nonzero λ requires at least one positive tβ.',
 'agrees','The inverse has the same consecutive differences and zero sum. The last nonzero proviso links to the separate separation alarm.')
I(26,'reading question',11,[58],[L(666,684)],'existence of a linear functional ℓ',
 'The displayed separation criterion omits ℓ≠0. With ℓ=0 it holds even when the all-ones vector is interior. The extreme-ray conclusion likewise fails if the antecedent permits only the zero functional.',
 'The suggested nonzero condition is a mathematical repair to test on the ink or preceding missing page; it is not silently inserted.',
 'agrees','The positive orthant provides an immediate checked counterexample to the literal unqualified separation statement.')
I(27,'title, date or page count',11,[43,45,47,49,52,54,56,58],[L(4,4),L(49,49),L(180,180),L(256,256),L(385,385),L(428,428),L(512,512),L(648,648)],'−3.3−; −3.18−',
 'The visible typescript pagination gives chains49→47→[3.5 absent]→45→43 and58→56→[3.16 absent]→54→52. These are selected reused leaves, not a complete document or a composition date.',
 'The chains are reconstructed solely from the transcribed printed folios. No author identification is assigned.',
 'agrees','Every listed folio occurs at the relevant scan; the two missing folios remain missing.')
I(28,'other',11,[51,53,55,57],[L(283,381),L(394,424),L(449,508),L(553,641)],'relations; ! vérifier',
 'The manuscript supports a partial diagonal-ring calculation. The earlier run\u2019s claim that a separate Hua register or Lean development partly proves a general product rule cannot be verified from this archive: neither the alleged formal theorem nor its certificate is supplied.',
 'Hua and the named register remain external-project leads, segregated in Stage5. Present computations do not certify unseen Lean code.',
 'agrees','The earlier note already restricts the claimed support and lists real gaps. Its statements about unavailable files are retained only as provenance reports.')
I(31,'unpursued implication',[11,16,56],{'11':[46],'16':[40,42,45,46],'56':[20,22,32]},[L(84,175),L(1347,1376),L(1715,1736)],'p_{31*}(p_{21}^*u p_{32}^*v)',
 'The correspondence product gives the formal operation needed to compare hyperplane restriction and Λ_X i_* with the induction in cote16. Quadric examples isolate the middle kernel and cokernel. They do not establish the proposed general standard-conjecture implication.',
 'The cross-folder operation-level comparison is editorial; its exact c16 locators and current reading are supplied by the agent16 review.',
 'agrees','The note keeps the reduction at its source/programme status and claims only concrete connecting maps.')
I(32,'unpursued implication',[11,16],{'11':[44],'16':[15,16,17,18]},[L(32,44)],'Ces actions sont connues',
 'A representation of the proposed universal Lefschetz operator ring must send every specified generator, including the degree projectors, to the corresponding operator. Specifying L alone is insufficient for the uniqueness issue discussed in cote16.',
 'The realization ρ(C)(x)=pr2_*(C·pr1^*x) is explicit; comparison with Φ is an additional task, not a theorem on cote11.',
 'agrees','The source supplies the action map; the contextual all-projector qualification is retained and checked in the c16 review.')
I(33,'idea of the earlier run',[11,16],{'11':[46,48],'16':[49]},[L(84,92),L(215,251)],'jouent le rôle d\u2019unités',
 'For an idempotent e on Y in the Chow-correspondence category, the formal object (Y,e) has identity e; inclusion/projection to (Y,1) are both e, so their composites have the required identities. Additive sums use matrices, and twists shift correspondence codimension.',
 'This is an explicit idempotent-completion construction by the earlier run, not written out by Grothendieck on these sheets. It is independently checked algebraically.',
 'agrees','The note clearly marks its construction as an added comparison and preserves the source\u2019s unfinished category check.')
I(35,'idea of the earlier run',[11,16,54],{'11':[44,46],'16':[15,16,17,18],'54':[3,5,7]},[L(32,44),L(84,92)],'Ces actions sont connues',
 'For a morphism L:M→M(1) and a natural automorphism g of the realization functor, naturality reads g_(M(1))L=L g_M. The analogous Λ equation has twist−1. It is not ordinary commutation on one untwisted vector space unless further identifications are given.',
 'These equations are the earlier run\u2019s category-theoretic comparison, not an authored statement on cote11.',
 'overstates','The previous kind "unpursued implication" could suggest authorship. Reclassified as an idea of the earlier run; the mathematical equation is correct and its twist is essential.','corrected (authorship/kind: comparison belongs to the earlier run)')

# Quadric specialization, cones and the integral intersection calculations.
I(36,'self-flagged step',56,[3],[L(703,749)],'On veut étudier; ?',
 'For a flat projective quadric degeneration over a strictly henselian trait, compare special and geometric generic cohomology through nearby/vanishing cycles. The displayed specialization map is explicitly questioned.',
 'A simple ordinary quadratic degeneration, coefficient order invertible on the base, and the correct nearby-cycle conventions are needed for the familiar rank-one Picard–Lefschetz conclusions. They are not all stated here.',
 'agrees','The question mark is authored; the entry does not identify a completed construction of the map.')
I(37,'unproved claim',56,[3,5],[L(703,869)],'R^{n−1}f_* est «pur»',
 'The parity tables predict one vanishing class for a quadric of dimension n−1: a specialization kernel for n even and cokernel for n odd. The last purity assertion has no completed statement.',
 'Nontrivial order-two monodromy in the even-dimensional fibre case requires a simple discriminant parameter; replacing t by s² kills that monodromy while preserving flatness, smooth generic fibre and the singular special fibre.',
 'understates','The note correctly sees the unfinished purity sentence, but the written family hypotheses also need checking before asserting the monodromy table. The extra hypothesis is a reconstruction, not an ink correction.','corrected (scope of the parity and monodromy claim)')
I(38,'reading question',56,[7],[L(915,938)],'H^i(U_1) ≃ Φ^{i+1}',
 'The reduced cohomology of the affine smooth fibre is compared to vanishing cohomology with a shift. The unreduced degree-zero statement fails for a nonempty connected fibre.',
 'One may either exclude i=0 and handle the H⁰ terms separately, or formulate the exact sequence with reduced cohomology. The line also changes U back to X in its sequence.',
 'agrees','The entry flags the missing endpoint qualification; the transcription does contain the unrestricted formula.')
I(39,'self-flagged step',56,[11],[L(997,1059)],'ξ (ou −ξ)',
 'The Gysin boundary for the complement of the zero section of a line bundle is multiplication by its Euler/first Chern class. For the punctured affine cone the line bundle is O_X(−1), so the sign depends on whether ξ means c₁(O(1)) or c₁(O(−1)).',
 'The modern bundle identification and orientation convention explain the choice; the source itself leaves the sign undecided.',
 'agrees','The doubt is explicit, not an uncertainty introduced by the transcriber.')
I(40,'reading question',56,[11],[L(1036,1059)],'H^*(X, Ĉ−a)',
 'The cohomology-with-support term belongs to the total line bundle and its complement of the zero section, not to the base X with a subset of the total space.',
 'Replace the ambient space by the line-bundle total space when giving a mathematically defined pair; the actual ink remains unjudged.',
 'agrees','The literal pair has incompatible ambient spaces; the Gysin sequence supplies the proposed alternative.')
I(41,'unproved claim',56,[11,13],[L(997,1059),L(1098,1150)],'mod torsion; H^i_a(C) ≃ H^{i−1}(E)',
 'For a cone C with vertex a and punctured cone E, contractibility gives local cohomology H^i_a(C)≅H^{i−1}(E) for i≥2, with H⁰_a=H¹_a=0 under connectedness. The Gysin sequence describes E by kernels and cokernels of multiplication by ξ; primitive/quotient shorthand only after the stated torsion qualification.',
 'Over C this is singular cohomology of the topological cone; the étale version needs invertible torsion and contraction/invariance hypotheses. It is not a universal integral splitting.',
 'agrees','The note preserves the manuscript’s mod-torsion qualification and does not turn it into an integral direct-sum theorem.')
I([42,43],'reading question',56,[15],[L(1200,1230)],'H^{2ν−2}(E)=Z/2',
 'For the punctured cone over Q^{2ν−1} over C, integral torsion occurs in H^{2ν}(E), not H^{2ν−2}; for Q^{2ν}, the extra free class is in H^{2ν}(E), not H^{2ν−1}. For Q¹ the circle-bundle Euler number is −2 and H²(E)=Z/2.',
 'The second degree correction is an additional finding of this run. With arbitrary finite coefficients the integral answer must be tensored in the derived sense; 2-torsion creates an additional adjacent-degree contribution.',
 'understates','The notes correctly test the odd-dimensional case but overlook the second wrong middle degree, shared by the Pro and Codex transcriptions.','corrected (both parity tables require an alarm)')
I(44,'conjecture',56,[17],[L(1242,1274)],'on est amené à prévoir; ??',
 'For the particular contracting cone and coefficient object under consideration, compare cohomology supported at the vertex with compactly supported cohomology of the cone.',
 'A general modern formulation uses a positive-weight contracting action and a weakly equivariant constructible complex. The source does not state those hypotheses or a theorem for arbitrary spaces.',
 'agrees','The expectation and double question mark are on the page. The note correctly refuses a universal duality assertion.')
I(45,'idea of the earlier run',56,[17],[L(1264,1274)],'H^*_a(C) ≃ H^*_c(C) ??',
 'Braden’s contraction comparison supplies a precise later instance: for a positive-weight vector bundle with zero section, extraordinary restriction followed by compact support agrees with compact support of the equivariant complex.',
 'This is a published-comparator construction of the earlier run; a general singular cone is not literally the vector-bundle special case and requires its own contraction lemma.',
 'agrees','The entry’s explicitly restricted example is supportable by Braden Lemma6 and the adjunction paragraph; it does not settle every version of the handwritten hope.')
I(46,'self-flagged step',56,[20],[L(1291,1378)],'Que se passe-t-il pour i=0,1,n,n+1 ??; n≠1',
 'For U^n=Q^n\Q^{n−1}, n≥1, over C the ordinary integral cohomology is Z in degrees0,n, with the two degrees coinciding as rank2 when n=0 is treated separately; compact support is dual. At n=1, U¹≅G_m, so endpoint terms cannot be suppressed.',
 'The affine quadric retracts onto S^n for n≥1. Étale coefficients require characteristic invertibility and twists; the handwritten tables use a different indexing of ν.',
 'agrees','The source expressly isolates the endpoint problem and n≠1; the note correctly records it as unfinished on the page.')
I(47,'unproved claim',56,[20],[L(1330,1354)],'multiplication par 2',
 'For even n, H_c^n(U^n,Z)→H^n(U^n,Z) has absolute multiplier2, and for odd n it is0. With the complex orientation and compatible dual generators its signed self-intersection is (−1)^{n/2}2.',
 'The target’s compact-support decoration is uncertain in the Pro witness. A change of just one independent generator changes a matrix sign; the geometric self-pairing sign is fixed once duality orientations are fixed.',
 'understates','The note correctly tests the absolute factor but must keep the orientation-sensitive sign and the target-reading alarm.','corrected (separate absolute index from the signed pairing)')
I(48,'self-flagged step',56,[20,22],[L(1362,1427)],'par',
 'The hyperplane-section Gysin exact sequence has a middle extension when n is odd. Its integral map is fixed by the two ruling classes and the primitive difference; the written sentence stops before giving the extension data.',
 'The full matrices are supplied in the computation record, using the integral Chow basis. They are not an implicit completion of the sentence.',
 'agrees','The unfinished text is visible and cannot be treated as a proved extension formula.')
I(49,'self-flagged step',56,[22],[L(1407,1453)],'Énoncé dual; Si n pair',
 'Two announced statements are blank: the compact-support dual of the affine cohomology table and a subsequent even-dimensional case.',
 'Poincaré duality and the quadric Chow table give modern completions, separately labelled; no wording is reconstructed as manuscript text.',
 'agrees','The source visibly announces but does not write the continuations.')
I([50,51],'unproved claim',56,[24,30],[L(1497,1525),L(1693,1705)],'φν=(ξ^ν+λν)/2',
 'For Q^{2ν}, let α,β be the two maximal-linear-space classes. Then h^ν=α+β and λ=α−β, so <h^ν,λ> has index2 in H^{2ν}(Q,Z); α=(h^ν+λ)/2 is integral though the displayed sublattice does not contain it.',
 'The matrix in the ordered basis α,β is [[1,1],[1,−1]]; Smith normal form is diag(1,2). In étale cohomology the classes carry twistν.',
 'agrees','Both note entries describe this same integral lattice calculation; the matrix check has been rerun.')
I(52,'reading question',56,[24,26],[L(1488,1503),L(1543,1571)],'λ_{2ν}; ξ_i↦ξ_{i+2}',
 'The primitive class is in codimensionν, hence cohomological degree2ν. Hyperplane pushforward increases codimension by1 and degree by2.',
 'The notation may be mixing these two index conventions. The proposed alternatives are λν and ξ_i→ξ_{i+1} when subscripts denote codimension.',
 'agrees','The entry’s λ-index concern is valid; this run also flags the nearby pushforward index for the same reason.')
I([53,54],'reading question',56,[26],[L(1543,1571)],'λν²=ξ^{2ν}',
 'With λ=α−β on Q^{2ν}, λ²=(−1)^ν h^{2ν}=(−1)^ν2[pt]. In Q²=P¹×P¹, λ=a−b has square−2ab whereas h²=2ab.',
 'This refutes the literal universal plus sign without determining whether the ink contains a lost sign or an unstated convention incompatible with the later α−β formula.',
 'agrees','The source’s formula and its later identification of λ permit the counterexample; the two entries merge into one sign issue.')
I(55,'reading question',56,[26,30],[L(1573,1597),L(1693,1705)],'effaçable; λν↦0',
 'The primitive middle difference restricts to zero on a smooth hyperplane quadric and pushes to zero in the larger odd-dimensional quadric. It is not generally an effective cycle.',
 'Pro reads effaçable, Codex offers effective/ineffective; the actual vanishing maps favor effaçable but no scan decision is made.',
 'agrees','The note identifies a real mathematical distinction, and the independent transcription adds a conflicting witness.')
I(56,'other',56,[28],[L(1619,1635)],'Q⁰; Q¹; Q²; Q³; Q⁴; Q⁵; Q⁶',
 'The low-dimensional table lists even-degree cohomology generators for Q⁰ through Q⁶. Odd cohomology vanishes for smooth split projective quadrics with the stated coefficient qualification.',
 'The apparent cancellation of the odd-cohomology sentence differs between Pro and Codex. The table is checked as mathematics without deciding that deletion.',
 'agrees','The indexed note correctly treats the table as a check rather than an independent universal presentation.')
I(57,'unproved claim',56,[30],[L(1657,1692)],'×2',
 'The restriction–boundary and dual compact-support composites in the quadric hyperplane diagram have the factor2 at the critical degree, corresponding to α+β and α−β spanning an index-two sublattice.',
 'Integral matrices, boundary orientations and the coefficient2 must be kept separate; a general finite coefficient ring can make2 noninjective.',
 'agrees','The factor appears twice and is independently matched to the same lattice calculation.')
I(58,'reading question',56,[30],[L(1657,1665)],'illégible; ⊗',
 'The faint first display may suggest a tensor or derived-tensor operation, but the surviving symbols do not determine its objects, shifts, or statement.',
 'No theorem is inferred from this display. A scan review is required before a precise derived assertion can be assigned.',
 'agrees','The note correctly withholds a mathematical completion of the illegible expression.')
I(59,'unproved claim',56,[32],[L(1713,1728)],'injectif; surjectif',
 'On Q^{2ν}, multiplication by h in codimensionν−1 is Z→Z²,1↦(1,1), with free rank-one cokernel; in codimensionν it is (a,b)↦a+b, with kernel Z(1,−1). Other nonzero adjacent maps are isomorphisms.',
 'This uses the primitive integral cycle basis, not only powers of h.',
 'agrees','The manuscript distinguishes the two exceptional maps and their primitive generators correctly, subject to index readings.')
I(60,'unproved claim',56,[32],[L(1729,1739)],'multiplication par 2',
 'On Q^{2ν−1}, multiplication by h across the middle is Z→Z,1↦2, giving cokernel Z/2 and zero integral kernel.',
 'With arbitrary finite coefficients both kernel and cokernel must be recalculated; the integral claim is the source of the punctured-cone torsion degree.',
 'agrees','The note correctly connects the middle map to the cone calculation, with no assumption that2 is invertible.')
I(61,'unproved claim',56,[35],[L(1752,1779)],'équivalence linéaire',
 'Split smooth projective quadrics have cellular Chow groups generated by linear isotropic subspaces; in even middle codimension there are two rulings, and above the middle h^i is twice the primitive generator.',
 'The modern statement is modulo rational equivalence. The historical expression équivalence linéaire should not silently be identified with divisor linear equivalence in every codimension.',
 'agrees','The notes preserve the geometric representatives, but the equivalence convention remains an editorial qualification.')
I(62,'title, date or page count',56,[2,9],[L(692,702),L(988,996)],'3 p|30; 12 p',
 'Two covers precede three selected vanishing-cycle sheets and twelve selected cone/quadric sheets. These are supplied-scan counts, not complete original dossier extents.',
 'The count3p/30 and part of the title remain uncertain; no inferred page is added.',
 'agrees','The notes’ selected-page counts match the actual scan blocks and explicitly preserve the uncertain cover readings.')
I(63,'idea of the earlier run',[11,16,47],{'11':[44,46,48],'16':[30],'47':[3]},[L(22,44),L(84,175)],'cohomologies algébriques',
 'The supplied pages provide correspondence actions and local duality structures. They do not construct the global height pairing or the local-to-global transport invoked by the earlier WG H9 programme.',
 'This is a contextual research lead, retained only in the separate our-projects table. The unavailable research return is not treated as evidence.',
 'agrees','The entry itself describes the missing comparison morphism and does not claim the height programme is proved.')
I(64,'idea of the earlier run',54,[5,7],[L(2721,2730,Q)],'H¹ de Rham; groupe fini',
 'For an abelian variety over a perfect field of characteristic p, Oda identifies the Dieudonné module of A[p] with H¹_dR(A), with Frobenius/Verschiebung and the Hodge filtration.',
 'The exact modern realization is supplied by Oda Cor5.11, not by the correspondence formulas in cote11. It is merged with the directly sourced cote54 problem during integration.',
 'agrees','The note’s restricted comparison is supported by the actual c54 question; it does not assert a general filtered realization for arbitrary schemes.')

# Reused SGA3 typescript: revisions and exact scope matter as much as its results.
I(65,'withdrawn in the same text',56,[4,18,25],[L(750,797),L(1275,1290),L(1526,1542)],'deleted: Théorème1.7',
 'The cancelled theorem collects rank semicontinuity, local existence/conjugacy of maximal tori, and nilpotent-fibre assertions. Later sheets reorganize the results and insert locally constant reductive rank where needed.',
 'Cancellation records a draft state; it is not by itself a mathematical refutation of every constituent proposition.',
 'agrees','The whole block is deleted and its revised successors must be cited alongside it.')
I(66,'withdrawn in the same text',56,[6,8],[L(870,914),L(939,987)],'deleted: 1. Tores maximaux',
 'The cancelled opening invokes Borel/Chevalley field results before the revised exposé describes scheme-theoretic structure over an arbitrary base.',
 'It is a superseded introduction, with the credited field inputs retained as historical background rather than new claims.',
 'agrees','The note correctly distinguishes cancellation of the opening from withdrawal of Borel’s theorem.')
I([67,104],'self-flagged step',56,[8],[L(939,987)],'avec avantage ab ovo; devrait être complètement refondu',
 'The author proposes rebuilding classical structure theory directly over general base schemes and revising exposés XI,XII,XV,XVI; he hopes to remove affineness restrictions where possible.',
 'This is a methodological programme, not a precise theorem that all structure results extend to all group schemes.',
 'agrees','The two entries describe the same revision programme; modal wording and future exposé references are preserved.')
I(68,'self-flagged step',56,[12],[L(1060,1097)],'On verra au N°5; est possible',
 'The maximal-torus parameter scheme is said to be affine, with proof deferred; an alternative finite-torsion method is proposed. Broader representability claims are cancelled.',
 'The later printed SGA3 theorem is compared with its actual hypotheses; a proposed alternative proof is not called completed merely because the result is known.',
 'agrees','The source distinguishes future proof, alternative method, and crossed-out generalization.')
I(69,'self-flagged step',56,[14],[L(1176,1199)],'Il reste à vérifier; donc',
 'For the stated smooth affine group scheme, the maximal-torus functor is represented by a smooth separated scheme of finite type; the finite-type check proceeds locally from G/N.',
 'The last sentence on this same page completes the announced check; it is not an open problem of the source after that point.',
 'agrees','The note correctly reads the continuation through its conclusion instead of stopping at Il reste à vérifier.')
I(70,'unproved claim',56,[21,16],[L(1379,1397),L(1231,1241)],'une esquisse',
 'For an étale separated quasi-finite group scheme, the geometric fibre group injects under generization after the appropriate strict henselian reduction; cardinality is lower semicontinuous, and local constancy of the fibre cardinality characterizes finiteness.',
 'The finite-presentation/quasi-finite convention and separatedness are essential. The argument runs from scan21 to scan16, contrary to scan order.',
 'agrees','The proof is labelled a sketch and its continuation is actually present.')
I([71,102],'reading question',56,[16],[L(1236,1241)],'R et T deux sous-tores tels que R⊂T',
 'The assertion W_G(R) is a subquotient of W_G(T) for arbitrary nested subtori is false. In SL₄ over C the explicitly checked tori R with weights(3,1,−1,−3) and T=ker(1,2,−7,4) have W(R)=C₂ and W(T)=1.',
 'A valid refinement assumes T maximal; the printed SGA3 XII2.3 repeats the broad wording but its proof uses maximality. This run does not silently insert maximal into the transcription.',
 'agrees','The notes give the exact counterexample rather than a generic rank objection. All character-lattice and centralizer hypotheses have been rechecked.')
I([72,73],'unproved claim',56,[18],[L(1281,1290)],'Il n’est pas difficile de construire',
 'Over R=Z_(3), G=Spec R[x,(1+3x)⁻¹] with product x+y+3xy is smooth affine, has generic fibre G_m and special fibre G_a.',
 'The equations are the earlier run’s explicit realization of the source’s existence remark; no such equations occur on the sheet.',
 'agrees','The construction is correct and separate from the quoted existence claim; associativity, inverse and fibres are checked directly.')
I(74,'unproved claim',56,[25],[L(1526,1535)],'si T est maximal',
 'A torus R commuting with a maximal torus T lies in T: the product image RT is again a torus and maximality forces equality.',
 'The scheme-level statement uses the source’s smooth affine/base hypotheses and the cited representability of the product image.',
 'agrees','The short proof is on the page; no arbitrary noncommuting inclusion is asserted.')
I(75,'withdrawn in the same text',56,[25,29],[L(1535,1542),L(1636,1642)],'inserted: rang réductif localement constant',
 'For the source’s commutative group, or connected nilpotent-fibre group, locally constant reductive rank yields the stated unique maximal torus; in the nilpotent case it is central.',
 'The inserted hypothesis controls existence over the base. The G_m-to-G_a model shows why fibrewise uniqueness alone is insufficient.',
 'agrees','The note retains the actual insertion and the proof continuation; it does not revive the unqualified earlier wording.')
I(76,'unproved claim',56,[23],[L(1454,1465)],'tout homomorphisme … se factorise',
 'For the specified commutative smooth group, the largest subgroup of multiplicative type is characterized by universal factorization of maps from groups of multiplicative type and commutes with base change.',
 'This universal property belongs to the reductive-centre construction, not to an arbitrary set-theoretic centre; the exact representability assumptions are restored from the printed exposé.',
 'agrees','The source does assert the base-change and factorization properties, within its running hypotheses.')
I(77,'reading question',56,[23],[L(1454,1465)],'H∩G/Z⁰=0; Exp.VI §…',
 'The intersection must take place inside the quotient G⁰/Z⁰ (or the corresponding ambient quotient in the proof). Several section numbers in the references are blank.',
 'The parentheses and precise cited propositions are supplied only in the commentary after comparison with the published proof, not as new readings.',
 'agrees','The literal expression is ill-typed and the bibliography slots are unfinished.')
I(78,'unproved claim',56,[27],[L(1598,1610)],'les fibres sont affines',
 'Under the preceding fibre criterion and source hypotheses, existence of the reductive centre reduces to the asserted properties on geometric fibres; the affine-fibre case is proved in the displayed argument.',
 'This is not a theorem that every group scheme with affine fibres is affine over an arbitrary base.',
 'agrees','The proof is actually completed here; its scope is the numbered criterion, not an unconstrained affineness test.')
I(79,'self-flagged step',56,[27],[L(1610,1618)],'Nous verrons … Exp.XIII; Nous allons',
 'An affine group scheme over a field has the reductive centre asserted in Theorem4.4. The selected page gives a future reference to a product decomposition and starts, but does not finish, an alternative proof.',
 'Published SGA3 supplies the completed result; the excerpt alone supplies only a statement and reference.',
 'agrees','The unfinished ending and deferred proof are both retained.')
I(80,'withdrawn in the same text',56,[29],[L(1643,1651)],'Conditions équivalentes',
 'For H⊂G under the stated conditions, a torus T⊂H is maximal in G exactly when it is maximal in H and the relevant reductive ranks agree.',
 'The rewritten equivalence is the operative draft reading. No converse is detached from the equal-rank condition.',
 'agrees','The note tracks the author’s revision rather than treating both versions as simultaneous assertions.')
I(81,'unproved claim',56,[29],[L(1652,1656)],'W=Norm(T)/Centr(T)',
 'For the specified torus in a smooth affine group scheme, the normalizer-centralizer quotient is the Weyl group scheme, with the printed exposé’s representability, étaleness, finiteness and base-change qualifications.',
 'General subtori can have locally varying normalizer data; the exact hypotheses of the numbered proposition must remain attached. The handwritten line is compressed.',
 'agrees','The note preserves the quotient object and base-change claim instead of treating a fibrewise abstract group as a universal constant group.')
I(82,'self-flagged step',56,[31],[L(1706,1709)],'nous nous dispensons de reproduire',
 'Parts(a),(b) of the reductive-centre argument are omitted by explicit reference.',
 'The referenced published arguments are evidence for the later theorem, not a proof present on this sheet.',
 'agrees','The omission is authored and needs a bibliographic check, not a conjectural classification.')
I(83,'self-flagged step',56,[31],[L(1707,1712)],'Le centre réductif de G/Z est unité',
 'The quotient by the reductive centre has trivial reductive centre in the theorem’s setting; the selected conjugation argument stops mid-sentence.',
 'The printed continuation provides a comparator, while the manuscript witness remains incomplete.',
 'agrees','The exact unfinished point is preserved; the note does not pretend the selected text proves it.')
I(84,'unproved claim',56,[33],[L(1740,1747)],'max; il suffit',
 'Maximality of a torus is an open condition in the indicated smooth torus parameter space; this gives the maximal-torus subfunctor and its smooth separated structure.',
 'The source’s functor and base hypotheses remain part of the assertion. The displayed local proof is finished.',
 'agrees','The note correctly classifies the completed local argument separately from adjacent cited statements.')
I(85,'unproved claim',56,[33],[L(1747,1751)],'conséquence immédiate',
 'Local conjugacy of maximal tori is deduced from the cited field/group-scheme result, with the topology stipulated in the exposé.',
 'The proof on this page is a reference, not an independent derivation of conjugacy.',
 'agrees','The entry correctly treats the compressed dependency as a checked citation obligation.')

# Delzant's signed 1962 offprint is not silently attributed to Grothendieck.
I(86,'other',56,[36],[L(1780,1802)],'note de M. Antoine Delzant',
 'For a field F of characteristic≠2, the group completion of nondegenerate quadratic spaces with orthogonal sum and tensor product is GW(F); rank gives an augmentation.',
 'The source uses its own notation Q(F). Identifying it with GW, rather than the Witt quotient, is editorial translation.',
 'agrees','The construction retains the rank and therefore is not the ordinary Witt ring. Authorship belongs to Delzant.')
I(87,'unproved claim',56,[36,37],[L(1804,1843)],'Proposition; Corollaire',
 'The square-class group ring surjects onto GW(F). Its kernel is generated by binary isometry relations; binary nondegenerate forms are classified by dimension, discriminant and the quaternion/Hasse invariant.',
 'Nondegeneracy, characteristic≠2 and the convention that square classes are written additively are essential. This is Delzant’s compressed presentation with a Witt reference.',
 'agrees','The note accurately separates the presentation proposition from the cited binary-form classification.')
I(88,'idea of the earlier run',56,[36,38],[L(1791,1802),L(1928,1934)],'I; grad²',
 'Let J=ker(rank:GW→Z) and I⊂W be the even-rank ideal. The quotient GW→W restricts to a multiplicative isomorphism J≅I, carrying J^r to I^r, hence J²/J³≅I²/I³.',
 'The filtration bridge is proved in this run, because it is needed to compare Delzant’s actual ideal with modern Milnor invariants. It is not written out in the offprint.',
 'agrees','The note supplies precisely the missing comparison instead of conflating the two ideals.')
I(89,'unproved claim',56,[37],[L(1845,1877)],'w(a+b)=w(a)w(b)',
 'Rank together with total Stiefel–Whitney class defines Delzant’s filtered-ring map from GW(F) to Z×(1+H^{>0}(F,Z/2)); the degree-one and degree-two terms are the square-class sum and pairwise cup sums.',
 'The target has Grothendieck’s Chern-class ring law, not ordinary componentwise multiplication. Its exact convention is checked against the 1958 source.',
 'agrees','The note keeps the indispensable rank component and the nonstandard target ring law.')
I(90,'unproved claim',56,[37],[L(1877,1889)],'u(q)=w²(q)',
 'Delzant identifies a normalized Clifford-type invariant u(q) with w₂(q). A raw Brauer difference [C(q)]−[C(〈1,…,1〉)] does not equal w₂ for all ranks and discriminants without the specified correction.',
 'A rank4 real example checks the raw-difference reading, not Delzant’s intended normalized definition. The offprint’s reference to Springer must be resolved before declaring its invariant false.',
 'overstates','The earlier note treats the normalization as already settled. This run distinguishes a normalized invariant from an unjustified all-rank raw Clifford difference.','corrected (Clifford normalization requires explicit convention)')
I([91,92],'reading question',56,[37],[L(1891,1895)],'Q(A)→H(A)',
 'The rank-plus-total-class construction is natural under field extension. If the final displayed H omits the tilde/rank component, it cannot mean the same filtered-ring target without further explanation.',
 'Naturality is verified on rank-one generators; the missing decoration is a scan alarm, not an amended reading.',
 'agrees','The two entries concern the same final naturality display and its target convention.')
I(93,'unproved claim',56,[38],[L(1896,1927)],'le rang et les classes',
 'Over a number field, a nondegenerate quadratic form is classified by rank and all its Stiefel–Whitney classes: finite-place rank/discriminant/Hasse data and real signatures are recovered. At a real place, w_j is binomial(r,j)u^j for r negative squares, so the powers-of-two coefficients recover r.',
 'This is Delzant’s application of local classification and Hasse–Minkowski. Rank cannot be dropped, and a fixed finite truncation independent of rank does not recover all signatures.',
 'agrees','The note retains both the rank and the real-place binary-digit argument.')
I([94,96],'conjecture',56,[38],[L(1928,1934)],'On ne sait pas si … injectif',
 'Delzant asks whether the degree-two graded map J²/J³→H²(F,Z/2) is injective. Under J≅I, it is the degree-two Milnor/Clifford invariant; degree-two expansion on products of rank-zero line elements gives cup symbols.',
 'The literature answer is matched to this actual map, using both the filtration bridge and its symbol calculation. The offprint’s question is Delzant’s, with an earlier Grothendieck letter parallel in c45.',
 'agrees','The notes correctly distinguish the exact degree-two question from the much stronger all-degree Milnor conjecture.')
I([95,97],'conjecture',56,[38],[L(1928,1934)],'engendré par les algèbres de quaternions',
 'For a field F of characteristic≠2, is every 2-torsion Brauer class a sum of quaternion classes? The Kummer sequence identifies H²(F,μ₂) with Br(F)[2].',
 'Merkurjev’s degree-two norm-residue theorem answers yes. The field assumption removes the Pic(F)/2 term; arbitrary schemes require a different statement.',
 'agrees','The note’s Kummer bridge is exact in the field setting and the generated-subgroup formulation matches the source question.')
I(98,'title, date or page count',56,[36,37,38,39],[L(1780,1789),L(1944,1958)],'Antoine Delzant; 10 septembre1962',
 'The signed offprint is Delzant’s Comptes rendus255(1962),1366–1368, with a separate printer/imprint sheet. Its date is not a date for adjacent manuscript leaves.',
 'The colophon establishes publication/session provenance, not first circulation or the manuscript’s date.',
 'agrees','Title, author, printed pagination and date are explicitly visible; attribution to Grothendieck would be wrong.')
I(99,'idea of the earlier run',[16,56],{'16':[15],'56':[15,32]},[L(1200,1230),L(1729,1739)],'×2',
 'The rank-one exterior model e↦f is unimodular, whereas the conic hyperplane map in primitive integral bases is multiplication by2. They coincide only after changing normalization or inverting2.',
 'This is a comparison proposed by the earlier run, not an identification made by the manuscript. Cote16’s integral exterior obstruction is checked independently.',
 'agrees','The comparison detects a real integral normalization obstruction without claiming a universal motivic model.')
I(100,'idea of the earlier run',[47,56],{'47':[3],'56':[17]},[L(1242,1274),L(2097,2124,Q)],'proper; ??',
 'Cote47’s proper-support transform remark and cote56’s vertex/compact-support question both require attention to f_! versus f_*, but they concern different spaces and functors.',
 'No natural transformation connecting those two particular constructions is supplied. The link is a research lead, not an equality of Fourier and contraction operations.',
 'agrees','Both endpoint passages are present; the absence of an exact connecting map is explicitly recorded.')
I(101,'idea of the earlier run',None,[],[],'no corresponding passage',
 'The note reports searches for LM7 E.23 and LM7_PUSH D.44 objects in the supplied material; the full external runs and their proofs are unavailable.',
 'Only the lead and the note’s stated qualifications are retained. No theorem status is inherited from an unseen research return.',
 'not on the page','This is a record about other projects, not a claim of the manuscripts. It belongs in the segregated project-leads table.')
I(103,'reading question',56,[20],[L(1330,1345)],'Je m’y perds … signe près',
 'The source appears to flag a sign ambiguity in the affine quadric generators. Codex instead reads a conditional sentence about odd n and determination up to sign.',
 'The mathematical sign issue is real, but the Pro first-person sentence is not established without scans; both witnesses are retained.',
 'overstates','The note calls the phrase probably authorial. The independent conflicting transcription makes the exact wording unresolved.','corrected (retain both transcription witnesses)')
I(105,'unproved claim',56,[4,14],[L(750,797),L(1151,1175)],'ρ_u=0',
 'For the nonnegative upper-semicontinuous unipotent-rank function in the theorem’s setting, its zero locus is the open set ρ_u⁻¹((−∞,1)).',
 'This is the elementary last step from the stated semicontinuity theorem, not a new independent result about arbitrary families of groups.',
 'agrees','The note’s exact locus calculation is valid and keeps the rank theorem’s hypotheses and revisions.')
I(106,'self-flagged step',56,[18],[L(1275,1283)],'artinien; réductif; XIV',
 'Containment of a torus in a maximal torus is deferred to a later exposé, under the revised artinian/local-reductive alternatives recorded on the page.',
 'The inserted/deleted base conditions cannot be collapsed into an unconditional global statement; the published SGA3 comparator is separate.',
 'agrees','The entry correctly quotes a forward-reference obligation, not an available proof.')
I(107,'other',None,[],[],'records/context_concordance_review.md; progress.log',
 'The earlier run claims a104-query context audit and hash checks of50 page files. Those supporting records and separate page files are not among the attachments.',
 'The present run rechecks the supplied combined transcription and makes a new audit; it cannot certify unseen earlier logs.',
 'not on the page','The note is documentary metadata. Its claimed computations are not accepted on authority; the unavailable records are explicitly identified.')

# Source-derived items in cote55: Codex leads have no NOTES_INDEX verdict rows.
K='SA18_texts/codex/K55-01_transcription.tex'
I([],'unproved claim',55,[2,4],[L(2,52,K),L(78,113,K)],'X espace de Stein compact',
 'For a Stein compact K (compact with a Stein-neighbourhood basis) in a complex analytic space, coherent O_K-modules admit finite global presentations, and Γ identifies them with finitely presented modules over Γ(K,O_K).',
 'Cartan A and B plus compactness supply the finite presentations. Noetherianity of the global ring requires additional hypotheses; it is not part of the unqualified equivalence.',
 'agrees','The theorem and presentation argument are actually written. This source-derived item has no indexed Pro note; the analytic setting is kept separate from the later abstract LemmaA.')
I([],'unproved claim',55,[6,10],[L(148,168,K),L(285,314,K)],'X quasi-compact; H¹(X,J)=0',
 'The main abstract LemmaA claims an equivalence between finitely presented global modules and coherent sheaves from compactness, coherent O with noetherian stalks, and H¹-vanishing alone. It is false for the constant-C ringed space RP² and its sign local system.',
 'The separate marginal variant adds a compact-open neighbourhood basis and restricts to global presentations; it is not refuted by the RP² example. The later generation conditionβ repairs the main gap.',
 'understates','The Codex lead notices unfinished β; this run verifies an actual counterexample to the unqualified main lemma, with all written hypotheses checked.')
I([],'self-flagged step',55,[6,10,12],[L(172,190,K),L(285,314,K),L(356,400,K)],'α; β; engendré par ses sections',
 'With compactness, coherence, exactness of sections on finite presentations and global generation of every coherent sheaf, tensoring with O and taking sections give the expected finite-presentation equivalence.',
 'The source proves parts of α but leaves β unfinished. The corrected equivalence is independently reproved; it does not assert a theorem for all ringed spaces satisfying H¹=0.',
 'agrees','The visible gaps concern generation and polynomial-extension arguments, not merely omitted routine notation.')
I([],'unproved claim',55,[6],[L(175,178,K)],'exact; plat; cohérent',
 'Under the corrected equivalence hypotheses, all stalks O_x are flat over A=Γ(O), and A is coherent.',
 'These are consequences of the corrected lemma, not consequences of its false original hypotheses alone. Finite matrix kernels suffice to prove them.',
 'agrees','Both corollaries are on the page; their dependence on LemmaA is explicit and must be repaired with it.')
I([],'reading question',55,[6],[L(179,181,K)],'Si X est «pur»',
 'The maximal-ideal correspondence uses an undefined condition pur; the text alone does not determine the intended separation or purity condition.',
 'No general maximal-spectrum theorem is reconstructed from the word. Even stalks all equal to a field do not distinguish points of a constant ringed space.',
 'agrees','The quotation marks and missing definition prevent an exact theorem identification; this is a documentary limit, not evidence of an open conjecture.')
I([],'conjecture',55,[8,10],[L(223,245,K),L(303,314,K)],'J∩A; J∩B_m; cohérent?',
 'For coherent A and a finitely generated ideal J⊂A[T], must J∩A, or each bounded-degree part J∩A[T]≤m, be finitely generated over A? In this generality the answer is no.',
 'An independently checked counterexample uses A=∏ k[[u,v]] and J=(u−vT,(v^n)_n). The nth contraction is(u,v)^n and needs n+1 generators. The noetherian and monic-generator cases are positive refinements.',
 'understates','The question is explicitly authored; the Codex notes do not settle it. A direct elimination counterexample is supplied rather than equating it with the different polynomial-coherence question.')
I([],'self-flagged step',55,[8,12],[L(223,245,K),L(356,400,K)],'O_X[T₁,…,T_n] cohérent',
 'The author strengthens the assumptions to coherence of all polynomial structure sheaves and acyclic compact neighbourhoods, aiming to extend the correspondence to finitely presented algebras and their finite modules.',
 'The α argument alone does not finish global generation. Noetherian Stein compact polyhedra give a safe established setting; arbitrary coherent rings do not automatically satisfy polynomial coherence.',
 'agrees','The assumptions and unfinished continuation are visible, and no unqualified Hilbert-basis theorem for coherent rings is inferred.')
I([],'self-flagged step',55,[14],[L(444,465,K)],'Lemme B; préciser ce point',
 'The proposed noetherianity criterion assumes compactness/coherence, noetherian stalks, and a uniform local unique-continuation property on coherent integral quotients; it asserts stabilization of increasing coherent subsheaves and noetherianity of A.',
 'The application to compact analytic polyhedra is explicitly left to precision. Frisch and Siu provide exact later analytic noetherianity criteria; the fully abstract LemmaB is separately qualified, not declared equivalent to their results.',
 'agrees','The local condition is written, but its application and proof are not completed in the supplied text.')
I([],'unproved claim',55,[3,5],[L(53,77,K),L(133,144,K)],'rang; engendré; dimension',
 'For a local map of noetherian local rings A→B with zero-dimensional closed fibre, dimB≤dimA. For a general local map dimB≤dimA+dim(B/m_AB), with equality when flat under the usual noetherian hypotheses.',
 'The source proof incorrectly says m_A is generated by dimA elements; a system of parameters generating an m_A-primary ideal repairs the argument. No regularity of A is assumed.',
 'agrees','The propositions are standard dimension bounds, but the displayed generation phrase needs a reading/proof alarm.')
I([],'unproved claim',55,[5,7],[L(114,144,K),L(192,222,K)],'dim(X×Y)=dimX+dimY; extension du corps',
 'For nonempty schemes of finite type over a field, dimension is invariant under field extension and additive on products. At a point x, dim_xX=dimO_X,x+trdeg_kκ(x) with the appropriate local-dimension convention.',
 'The finite-type-over-a-field condition is essential to these versions; the typed proof supplies it even where the isolated line is compressed.',
 'agrees','The reused typescript contains both the field reduction and the product argument; the modern statement restores their scope.')
I([],'unproved claim',55,[7],[L(199,218,K)],'image; quasi-fini',
 'For a morphism of finite-type k-schemes, dim closure(f(X))≤dimX, with equality for quasi-finite f onto its image closure. The corresponding inequality fails for unrestricted morphisms, as the included trait example illustrates.',
 'Closure is necessary for a nonclosed image, and no conclusion about arbitrary scheme maps is imported.',
 'agrees','The source includes the scope restriction and its counterexample; the contextual source is not a general topological image theorem.')
I([],'unproved claim',55,[9],[L(246,282,K)],'Ass; diviseur de zéro; réduit',
 'For finite modules over noetherian rings, associated primes commute with finite direct sums, zero divisors form the union of associated primes, an ideal contains a nonzerodivisor exactly when it avoids that union, and a noetherian ring is reduced iff generically reduced with no embedded associated primes.',
 'The finite/noetherian setting and prime-avoidance hypothesis remain attached. The concluding reduced-module definition is unfinished and does not follow merely by replacing ring by module.',
 'agrees','Four substantive standard statements and their proof sketches are present on the reused page.')
I([],'unproved claim',55,[11],[L(315,355,K)],'dimension; image continue',
 'Krull dimension is monotone under subspaces in the stated noetherian/topological setting, is the maximum over a finite closed cover, and equals the supremum of its local values. A continuous image may have larger dimension.',
 'The two-point discrete-to-Sierpiński map in the source is a valid counterexample to naive image monotonicity; topology conventions are spelled out in the claims map.',
 'agrees','The example and the separate inequalities are actually written, and are not confused with the finite-type algebraic image theorem.')
I([],'unproved claim',55,[13],[L(401,443,K)],'codim; dimY+codim(Y,X)≤dimX',
 'For closed irreducible subsets, concatenating chains gives dimY+codim(Y,X)≤dimX and the corresponding superadditivity of codimension. A noetherian T₀ space of dimension0 is finite discrete.',
 'No equality is asserted without catenarity/equidimensionality assumptions. T₀ matters for the final point-set conclusion.',
 'agrees','The source gives chain arguments and retains the required topology qualification.')
I([],'unproved claim',55,[15],[L(466,518,K)],'équidimensionnel et équicodimensionnel et caténaire',
 'The claimed equivalence between all maximal chains having equal length and the stated three properties is false. The corrected condition requires each irreducible component to be equicodimensional.',
 'The exact later EGA0IV14.3.3 erratum and the Gabber semilocal counterexample are checked. This identifies a printed-text error rather than deciding the manuscript ink.',
 'understates','The Codex notes do not flag this substantive error; the literal typescript matches the known EGA proposition with the same deficient condition.')
I([],'unproved claim',55,[17,18],[L(519,574,K)],'tore … non algébrique; e₁+ik e₂',
 'There exist nonprojective complex2-tori fibred in elliptic curves over an elliptic curve, but the written lattice <e₁,ie₁,e₂,e₁+ik e₂> is a direct-product lattice and does not exhibit one.',
 'The alternative <e₁,ie₁,e₂,k e₁+i e₂> with real irrational k is proved to have no elliptic complement. It is explicitly this run’s reconstruction, not a chosen transcription alternative.',
 'understates','The Codex note reports the claimed example without detecting that subtracting the first generator from the fourth splits the lattice. The following proof also divides through a possibly zero coordinate.')
I([],'reading question',55,[9],[L(283,284,K)],'Module réduit',
 'The phrase begins a definition for reduced modules but stops before a usable criterion.',
 'No particular later definition of reduced module is assigned to this fragment.',
 'agrees','This uncompleted source fragment remains classF in the claims map; reading the surviving word is not checking a theorem.')

def save():
    (OUT/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
    for name,rows,fields in [('entries.tsv',entries,['entry_id','item_id','verdict','reason']),('CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])]:
        with (OUT/name).open('w') as f:
            w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
    print('Root manually reviewed items:',len(items),'entry verdicts:',len(entries))
if __name__=='__main__':save()
