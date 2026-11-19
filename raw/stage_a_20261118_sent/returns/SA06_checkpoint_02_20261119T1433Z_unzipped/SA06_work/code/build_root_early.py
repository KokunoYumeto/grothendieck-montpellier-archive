#!/usr/bin/env python3
"""Hand-authored judgments for all 74 early cote-15 entries.

This imports the separately authored late-packet judgments and serializes both.
The entry choices and verdicts below were made by reading the complete notes and
the Pro and Codex witnesses, never by a heading or keyword classifier.
"""
import build_root_items as b
a=b.add
p='MPL_15_034-086'
a(700,p,[1],'other',[],[],'',
 'The entry defines the historical run’s source and context abbreviations; it makes no mathematical assertion of Grothendieck.',
 'Only the supplied transcriptions and independently opened publications are primary evidence in this run. Reported Hua, RESULTS_STATE and project documents remain contextual endpoints unless actually supplied.',
 'agrees','The citation key has been read as provenance rather than as proof or as permission to treat absent documents as verified.')
a(701,p,[2,3,4,10],'other',[34,36,46,48,60,61,74,76,78,84,86],[[5,134],[274,331],[460,507],[923,1097],[1170,1211],[1264,1369]],
 'Supposons que; À vérifier!!; il peut être préférable',
 'The planning and status entries distinguish Deuring norm data, Brandt commutativity, positive commutative algebras, and reused analytic/site sheets. They do not establish a canonical rational fibre functor or an anabelian reconstruction theorem.',
 'Statements about earlier project progress are attributed to the earlier run. The current corpus supplies cote14 and B15 continuations missing from its local packet.',
 'understates','The local mathematical distinctions are supported. The current source boundary is wider, so historical claims of missing neighbouring pages are not current gaps.',{2:'corrected',3:'merged into SA06-701',4:'merged into SA06-701',10:'merged into SA06-701'})
a(702,p,[5,6],'idea of the earlier run',[34,48,78,84,86],[[5,41],[302,331],[1170,1211],[1264,1369]],
 'gerbes; catégorie de Picard de Brandt; groupe commutatif',
 'The four linear/nonlinear pairs and the A–D dictionary are modern comparisons supplied by the earlier run. Neither a place-reconstruction theorem nor a cyclotomic-normalizer result occurs in the cited leaves.',
 'The motivic and order-theoretic objects are retained in their own terms; links to La Longue Marche, Dérivateurs and S6 are separate provenance leads.',
 'agrees','The note explicitly separates analogy from result. Reading the cited leaves supports that separation; the alleged project endpoints are not manuscript cross-references.')
a(703,p,[7],'idea of the earlier run',[84,86],[[1264,1299],[1341,1369]],
 'un objet fidèle; G est commutatif',
 'The Nori arithmetic exact sequence, pure-Nori/André comparison and later homotopy-theoretic comparisons are external context. They neither identify this finite commutative band with the whole motivic group nor supply its rational neutralization.',
 'Modern results are checked in the references ledger with their exact coefficient, base-field and category hypotheses. Connectedness, period injectivity and neutrality are distinct assertions.',
 'agrees','The manuscript assumes a faithful object and a commutative multiplicative band. It contains no displayed absolute-Galois quotient sequence or general Nori construction.')
a(704,p,[8],'idea of the earlier run',[34,36,40,42,46,48,52,56,60,61,66,68,70,72,74,76,78,84,86],[[5,585],[622,751],[803,986],[1043,1097],[1170,1211],[1264,1369]],
 'À vérifier!!; il faudrait; pas ... de quasi-inverses naturels',
 'The sixteen observations comprise an editorial synthesis of norm obstruction, gerbe coherence, residual sign automorphisms, integral orders, Picard constraints, rational-point density and norm characters. Their mathematical content is split into the specific D, B and R items below.',
 'This omnibus is retained as a distinct synthesis, with no new theorem attributed to the manuscript. Its references to Sl2, centres and nonlinear reconstruction are contextual tests, not additional handwritten assertions.',
 'agrees','All sixteen observations were read with their cited passages. The substantive claims have individual records; the omnibus supplies their earlier-run organization and qualifications.')
a(705,p,[9,29,51,74],'other',[34,36,40,46,52,54,56,61,66,68,70,72,74,76,78,84,85,86],[[5,181],[274,585],[622,751],[803,986],[1043,1097],[1170,1369]],
 'À vérifier!!; NB; O* est-il tjrs égal',
 'The bibliography entries and final appended U01–U22/P01–P18 tables are editorial material. The tables preserve live doubts, unfinished unit and norm questions, local-finiteness uncertainties, and the packet’s 31 selected scans (23 subject sheets and eight reused typed sheets).',
 'Every cited publication is independently checked or explicitly marked unverified; no claim of an authorial page count is inferred from scan counts. The U-table’s extra questions are included in the problem and reading registers.',
 'agrees','The full nth-### extent, including the final ## tables, was read. These tables contain substantive leads beyond the bibliography heading; none was discarded by a heading-only extraction.')
a(706,p,[11],'unproved claim',[34],[[5,41]],
 'trivialisation; gerbes ... μ_n',
 'For a central degree-n generic algebra and its Deuring/order category, the page proposes that a determinant or norm trivialization reduces scalar automorphisms from G_m to μ_n, and describes equivalences by invertible bimodules with trivialized norm.',
 'The scalar calculation is λ↦λ^n. Equivalence of the entire category with a μ_n-gerbe requires a specified site, local existence and descent; these are not proved here. The uncertain degree/rank word is not silently resolved.',
 'agrees','The reduction of scalar band is stated, but the page’s compressed categorical equivalences remain constructions without a full descent proof.')
a(707,p,[12],'unproved claim',[36],[[46,72]],
 '0 → H^1(S,μ_n) → Brdt(C,τ) → Ram → 0',
 'The displayed sequence of norm-rigidified Brandt classes is right-exact only when every ramification class has a representative whose norm line is an n-th power. In general there is a subsequent obstruction Ram→Pic(A)/n.',
 'For a central invertible line L, replacing P by P⊗L multiplies its norm by L^n. The resulting obstruction and corrected right endpoint are our reconstruction; Pic(A)=0 suffices for the displayed surjectivity.',
 'agrees','The note correctly identifies an omitted general hypothesis and distinguishes π0 in the display from π1 in the surrounding prose. Over the principal rings used later, this specific obstruction vanishes.')
a(708,p,[13],'self-flagged step',[36],[[73,95]],
 'À vérifier!!',
 'The two Picard actions on the category Eq(C_A′,T) are asserted to admit a canonical identification compatible with the equivalence-category structure.',
 'A modern proof needs the action functors, their associativity and commutation constraints, and a compatible comparison, not merely equal groups of isomorphism classes.',
 'agrees','The exclamation-marked request for verification is explicit at the end of the page; the earlier note does not mistake it for a completed argument.')
a(709,p,[14],'unproved claim',[38],[[100,134]],
 'Supposons que ... canoniquement; un relèvement c',
 'A canonical norm object T and a functorial lift c of equivalences are assumed. Under those assumptions the page compares rigidified Brandt categories independently of a chosen representative.',
 'Objectwise lifts alone do not supply the functoriality and coherence used in the comparison. The statement is conditional, and its missing composition diagram is not filled in as manuscript text.',
 'agrees','Both suppositions precede the conclusion. The note correctly rejects an unconditional canonicity claim.')
a(710,p,[15],'unproved claim',[40,52],[[139,181],[360,393]],
 'quaternions ... ℝ; n’est pas spécial',
 'For the definite quaternion algebra ramified at p and infinity, the real specialization is the Hamilton division algebra; its associated gerbe or module category is not the split real one.',
 'The nonzero Brauer class in Br(R) and the sign torsor of norm trivializations occupy different cohomological degrees. The ambiguous prime 2|p remains an ink question.',
 'agrees','The later real calculation supports the local obstruction, but does not identify every real sign appearing in the earlier diagrams with that Brauer class.')
a(711,p,[16],'unproved claim',[40],[[139,170]],
 'm ... m^2 ... p; un groupe ...',
 'For a ramified quaternion maximal order O over Z_p, its radical m has m²=pO and reduced norm pZ_p. The norm-rigidified class (m,p) squares to the identity because Nrd(p)=p², splitting the indicated order-two extension.',
 'The claimed splitting concerns norm-rigidified classes with the stated norm convention; choosing the class does not choose a strict equivalence or erase μ2 automorphisms.',
 'agrees','The two different exponents—ideal square and reduced norm of a scalar—are exactly the reason for the split extension; the note preserves them.')
a(712,p,[17],'unpursued implication',[40],[[139,170]],
 'Z_p^*/Z_p^{*2}; Z/2',
 'The local class group is Z_p^*/Z_p^{*2}×Z/2 in this quaternion model: four elements for odd p and eight for p=2. At p=2 the Kummer exact sequence must be interpreted fppf rather than assumed étale.',
 'The square-class counts and the topology qualification are an earlier-run consequence of the displayed formula, not a separate statement written by Grothendieck.',
 'agrees','The formula is on the page. Its uniform use of μ2 leaves the site implicit, so the prime-two qualification is necessary and is now verified independently.')
a(713,p,[18],'unproved claim',[42],[[188,224]],
 'produit ... ℓ≠p,∞; Γ′; (p,(0,1),p)',
 'The comparison group is the product of away-from-p unit square classes, the local p unit square classes with a Z/2 ramification coordinate, and real signs, modulo the class translating the ramification coordinate by one and away coordinates by p.',
 'The quotient is explicitly represented by (u,v,e,w)↦(u p^(−e),v,w); p is positive at infinity. The written integral product with a real factor is not the full rational adèle ring.',
 'agrees','The product indices, positivity of p and displayed generator justify the quotient calculation; the note correctly avoids an adelic reinterpretation not stated on the page.')
a(714,p,[19],'unproved claim',[44],[[229,269]],
 'opère trivialement; gerbe de catégories',
 'Frobenius acts trivially on the indicated quotient of classes; the text proposes an associated gerbe-level descent description.',
 'Triviality on π0 does not establish a coherent action or effective descent of the groupoid. A lift, comparison 2-isomorphisms and their cocycle condition remain to be checked.',
 'agrees','The class computation and the gerbe suggestion occur at distinct levels; the note correctly keeps the latter unproved.')
a(715,p,[20],'reading question',[46],[[274,297]],
 'F_{p^n} = F_p[T]/Φ_{p^n−1}',
 'The literal cyclotomic quotient need not be a field: at p=2,n=3, Φ7=(T³+T+1)(T³+T²+1) over F2, so the quotient is F8×F8.',
 'A chosen irreducible factor of degree n produces F_{p^n}; compatible factors and embeddings are extra data. This counterexample checks the printed p,n and exponent, without deciding the ink.',
 'agrees','The earlier note’s counterexample directly matches every explicit hypothesis of the displayed formula. The reading is preserved and sent to the scan queue.')
a(716,p,[21],'withdrawn in the same text',[46,48],[[274,331]],
 'canoniquement [deleted]; π2 = Z2',
 'The page retracts an unqualified canonical-equivalence phrase and retains a connected equivalence groupoid with a residual sign automorphism; the following 2-categorical summary has π0=π1=0 and π2=Z/2.',
 'Existence and uniqueness of a class do not imply uniqueness of its isomorphism or triviality of its automorphism 2-group.',
 'agrees','The cancellation and the remaining sign group are explicit. No choice-free strict identification is claimed after the correction.')
a(717,p,[22],'withdrawn in the same text',[48,50],[[302,355]],
 'un point can. [deleted]; avoir choisi',
 'The comparison torsor T_p is canonical, but a canonical point is deleted. The construction C(ξ) depends on a chosen class; later Deuring geometry is invoked to supply a distinguished ξ_p.',
 'A geometrically defined class must be established using that geometry; it is not obtained from the definition of a torsor alone.',
 'agrees','The note correctly distinguishes the cancellation on scan48 from the conditional construction and later geometric assertion on scan50.')
a(718,p,[23],'unproved claim',[50,52],[[336,393]],
 'neutre; n’est pas spécial',
 'The comparison gerbe G(ξ) is said to be neutral while a constituent real gerbe is nonneutral. These statements concern different objects and are not contradictory.',
 'An equivalence torsor or gerbe can be neutral even when neither endpoint has an object over the ground field. The pages must be read with their actual endpoint data.',
 'agrees','The two nouns have different arguments and roles; the note’s separation is textually justified.')
a(719,p,[24],'unproved claim',[52],[[360,393]],
 'quatern. unitaires; vaut ...',
 'Real unit signs, a sign torsor of possible norm comparisons, and the quaternionic Brauer class appear in distinct categorical degrees.',
 'In a modern cohomological dictionary these belong respectively to H0, H1 and H2 of μ2-related data. This is a reconstruction of the displayed structures, not a cohomological notation imposed on the original text.',
 'agrees','The note prevents a genuine type error: the real obstruction cannot be inferred merely by identifying all displayed two-element sets.')
a(720,p,[25],'idea of the earlier run',[54,56],[[398,455]],
 'Détermination; cristal',
 'Oda’s 1969 comparison identifies the Dieudonné module of an abelian variety’s p-kernel X[p] with H1_dR, compatibly with the Hodge exact sequence described in Corollary5.11. It does not by itself calculate the particular norm-orientation class ξ_p of these pages.',
 'This is a later-source comparison, not a theorem quoted in the manuscript. Oda’s dissertation first circulated in June1967, separately from the1969 publication.',
 'agrees','The note’s restricted use of Oda matches the determinant question rather than claiming that a general comparison theorem supplies the missing distinguished element.')
a(721,p,[26],'self-flagged step',[54],[[398,434]],
 'Détermination de ξ_p; ∧² ...; compatible',
 'Determine a distinguished determinant/norm orientation for the rank-two slope-one-half crystal and prove its compatibility with the norm of invertible order bimodules.',
 'A principal polarization supplies a rank-two alternating pairing and hence a candidate determinant identification; comparison with the specified norm functor under Morita equivalence is an additional assertion.',
 'agrees','The page asks for the determination and draws the compatibility diagram. The note correctly leaves the Morita/norm comparison as work rather than treating a polarization as the complete answer.')
a(722,p,[27],'reading question',[56],[[439,455]],
 'R ... anneau des entiers; F²+p=0',
 'A Frobenius satisfying F²+p=0 supplies an action of Z[F], not automatically the maximal order of Q(√−p). At p=7, E:y²=x³+x has trace0 but only one nonzero rational two-torsion point, preventing (1+F)/2 from being an integral endomorphism.',
 'The curve is nonsingular in characteristic7; if F=2α−1 with α an endomorphism, then F acts identically on all E[2], contrary to its rational two-torsion. This is an explicit counterexample to the asserted automatic extension, not to descent with an already specified R-action.',
 'agrees','The phrase ring of integers is stronger than the displayed quadratic relation. The note isolates exactly that excess and keeps the original wording unchanged.')
a(723,p,[28],'unproved claim',[56],[[439,455]],
 'module inversible ... R; det ... Z',
 'Twisting by an invertible module is meaningful after fixing the quadratic order acting on the object. An integral determinant trivialization requires an orientation; the equation F²+p=0 alone supplies neither a maximal-order action nor every claimed comparison.',
 'For an imaginary quadratic order an orientation can be selected using a complex embedding. The issue is the stated canonical compatibility, not impossibility of choosing an orientation.',
 'agrees','The note appropriately limits its objection to the specified order and norm convention.')
a(724,p,[30],'unproved claim',[60,61],[[460,507]],
 'enveloppe projective; gén. strict; jolie',
 'Under finite-projective closure and a strict generator X, the category embeds into special functors and is modeled by finitely generated projective End(X)-modules. The reasonable tensor condition follows in an additive idempotent-complete category by splitting idempotents.',
 'B15-01 scan63 lines56–68 completes the sentence left at Pro61 line507: objects have the form P⊗_O X. The phrase “et inversement?” remains a separate self-flagged question.',
 'understates','The generator qualification is correct, but the supplied Codex continuation now closes the apparent textual break. Missing-definition claims must not survive this cross-folder comparison.',{30:'corrected'})
a(725,p,[31],'unproved claim',[66,68,70],[[512,585],[622,656],[703,725]],
 'Aut(O); Is(C); classes d’anneaux',
 'Equivalences act on isomorphism classes of strict generators; the stabilizer maps to the outer automorphism group of the endomorphism ring. The resulting sequence changes from groups to pointed sets and then orbit sets.',
 'Exactness beyond the group terms means fibre/orbit exactness, not a group exact sequence. Pic(A)=0 is a sufficient simplification in the page’s model, not part of the formal orbit-stabilizer assertion itself.',
 'agrees','The note reads the maps according to their domains; it does not manufacture a group law on classes of rings.')
a(726,p,[32],'unpursued implication',[66],[[512,585]],
 'analogie; des gén.',
 'The endomorphism-ring assignment on the core of strict generators yields a homotopy-fibre description of the equivalence category and the displayed automorphism/class sequence.',
 'This is the earlier run’s precise categorical formulation of an analogy, with chosen generator and endomorphism ring. It is not a claimed reconstruction of the original geometric object from a motivic representation.',
 'agrees','The reconstruction explains the page’s sequence without adding an anabelian interpretation.')
a(727,p,[33],'reading question',[66,68],[[512,585],[622,656]],
 'idéaux ... princ.; Pic(A)',
 'The groupoid of embedded invertible two-sided fractional ideals has scalar arrows from K* (more generally Z(E)*), whereas automorphisms of the unit ideal are A* when the centre is A. The Picard groupoid of A embeds centrally as a different step.',
 'Taking isomorphism classes requires quotient by principal scalar ideals from K*, not merely units A*. The distinction persists even for a principal Dedekind domain.',
 'agrees','The note correctly identifies a quotient-level ambiguity and does not confuse it with full faithfulness of the central Picard inclusion.')
a(728,p,[34],'unproved claim',[66,68,70],[[572,585],[646,656],[703,725]],
 'Ram; H^1(k(p),Q/Z)',
 'For maximal orders over a Dedekind base, two-sided ideal exponents modulo central ideals give the direct sum of local Z/e_pZ ramification factors. This quotient is not the whole Brauer group of the completed field.',
 'Identifying Brauer residues with H1 of the residue field requires a henselian valuation setting and the appropriate unramified/ramified exact sequence; arbitrary residue fields require care.',
 'agrees','The divisor quotient and tentative Brauer explanation are distinct on the page, including its question mark.')
a(729,p,[35],'reading question',[70],[[727,745]],
 'splitté en p,∞; 4,6',
 'In the supersingular quaternion specialization the algebra is ramified at p and infinity. For characteristic not2 or3, elliptic curves with j=0 and1728 have automorphism group orders6 and4 respectively; the displayed assignment is reversed.',
 'Characteristic2 and3 have exceptional automorphism behaviour and are excluded from this correction. The actual ink, including whether the prose says split, remains undecided.',
 'agrees','Both mathematical alarms are supported independently by the quaternion classification and the explicit Weierstrass automorphism calculation.')
a(730,p,[36],'unproved claim',[70],[[727,751]],
 'orbites ... Frobenius; épim',
 'Frobenius orbits of supersingular elliptic-curve classes correspond to the order-type distinctions described on the page; the asserted quotient of the order automorphism group depends on whether the j-invariant is in F_p.',
 'This must be checked in the Deuring correspondence with the chosen maximal order and exceptional characteristics. The unfinished final O* question is not supplied with a conclusion.',
 'agrees','The note distinguishes individual curve classes from endomorphism-ring types and keeps the uncompleted unit-group question open on the pages.')
a(731,p,[37],'unproved claim',[72],[[803,868]],
 'génériquement ... intérieurs; spéciaux',
 'Assuming the relevant generic algebra automorphisms are inner, rank-one invertible bimodules can be represented by embedded fractional ideals; scalar morphisms are central elements of E*.',
 'For central simple algebras the innerness is Skolem–Noether; it is an explicit hypothesis for the wider class of algebras considered here.',
 'agrees','The page names the generic-inner condition before constructing its ideal model. The note correctly retains it.')
a(732,p,[38],'unproved claim',[72],[[847,868]],
 'pas ... de quasi-inverses naturels',
 'The equivalences with embedded-ideal models do not come with natural quasi-inverses in the choices described. This is compatible with a canonically transported commutativity constraint.',
 'Canonical structure up to coherent equivalence is weaker than a choice-free strict model. The warning does not refute the later explicit generator-change proof.',
 'agrees','The warning is explicit, and its scope is the quasi-inverse rather than the existence of the Brandt Picard structure.')
a(733,p,[39],'unproved claim',[74],[[923,950]],
 '(C) ... LM=ML',
 'Condition(C) requires commutation of invertible two-sided ideals in the specified generic ideal model. It holds for maximal orders over a Dedekind domain by the classical local prime-power description; it is a substantive hypothesis for general nonmaximal orders.',
 'The category is not made commutative merely by calling its objects bimodules. Each use below retains(C).',
 'agrees','The note correctly recognizes both the explicit hypothesis and its known maximal-order case, without claiming a new general maximal-order theorem.')
a(734,p,[40],'unproved claim',[74],[[951,986]],
 'cat. de Picard ... stricte',
 'Under(C), the embedded-ideal groupoid is the Picard groupoid of the two-term complex Z(E)*→I(O). Its π1 is Z(O)* and π0 is I(O)/principal central ideals.',
 'Strict commutativity is realized in this abelian ideal model and transported. In the usual tensor-product category the associativity constraints are isomorphisms, not literal equalities of sets.',
 'agrees','The note makes the strict model explicit while retaining the distinction between that model and the original bimodule tensor category.')
a(735,p,[41],'unproved claim',[74],[[951,986]],
 'par transport; produit des biidéaux',
 'For commuting embedded ideals I,J the bimodule commutor is μ_JI^(−1)μ_IJ through their common product ideal. It need not be the elementwise flip x⊗y↦y⊗x over a noncommutative order.',
 'Multiplication identifies the tensor products with IJ=JI because the bimodules are invertible. This supplies naturality and the coherence identities through multiplication.',
 'agrees','The explicit transported commutor accurately captures the written ideal-product construction.')
a(736,p,[42],'unproved claim',[76],[[1043,1053],[1060,1097]],
 'can. indép.; P.L; P...P^−1',
 'Changing the generator by an invertible Morita bimodule P transports I to PIP^−1, preserving the product and hence the commutor; these transports compose as T_QT_P=T_QP. A change of representative P by PS gives the same result under(C).',
 'This is an actual proof under the page’s hypotheses. It does not rely on the questionable universal bracket about all autoisomorphisms.',
 'agrees','The displayed multiplication and composition identities prove the particular generator-change assertion. The note correctly saves this argument from an overbroad negative verdict.')
a(737,p,[43],'self-flagged step',[76],[[1054,1058]],
 'les autoisomorphismes ... transportent ... en elle-même',
 'On the literal Pro reading, the bracket suggests that every monoidal autoisomorphism preserves a given Picard commutor. This is false for a fixed tensorator: a strict monoidal coordinate permutation of the F2³ example changes the specified alternating bilinear commutor.',
 'Codex K15-02 line317 offers auto-intérieurs as a possible reading. Inner autoequivalences have a substantially narrower scope; the counterexample targets only the broad literal Pro assertion.',
 'understates','The earlier counterexample is sound for its literal formulation, but the independent Codex reading supplies a material narrower alternative that must be sent to the scans.',{43:'corrected'})
a(738,p,[44],'idea of the earlier run',[76],[[1054,1058]],
 'il faudrait ... préciser',
 'For the F2³ counterexample, changing the tensorator by α(x,y)=x1(y2+y3) repairs the underlying coordinate-permutation functor so that it becomes symmetric.',
 'This is a different monoidal functor with the same underlying ordinary functor. It does not rescue a claim about the originally fixed tensorator and is not an argument written on the page.',
 'agrees','The note explicitly makes the change of tensorator; the exhaustive finite calculation is reproduced separately.')
a(739,p,[45],'unproved claim',[78],[[1170,1195]],
 'est une équivalence de 2-catégories',
 'For a connected 2-groupoid over a point with a chosen base object and its coherent automorphism Picard groupoid B, C′↦Eq(C,C′) is an equivalence with B-torsors.',
 'A version over a site additionally needs stackification, local connectedness and effective descent; the pointwise formal result does not prove these hypotheses.',
 'agrees','The note states the formal result with its base-object and connectedness conditions and does not claim an unproved sitewise equivalence.')
a(740,p,[46],'unproved claim',[76,78],[[1060,1097],[1170,1195]],
 'canoniquement équivalentes; même catégorie ... B',
 'The common Brandt Picard category is identified through the explicit compatible Morita transports; the word canonical means coherent equivalence in this construction.',
 'No preferred skeletal category, ordinary equality of all categories, or canonical quasi-inverse follows from it.',
 'agrees','The note correctly ties canonicity to the preceding displayed coherence data rather than to a global unmentioned choice.')
a(741,p,[47],'unproved claim',[78],[[1196,1211]],
 'si les C_A′ satisfont les mêmes conditions',
 'Base change induces the claimed Picard functor and compatible action provided the base-changed categories satisfy the same hypotheses.',
 'The condition is not automatic for arbitrary extensions or orders. The torsors classify equivalence data in this category, not archimedean places.',
 'agrees','The conditional clause is written and cannot be removed by the later comparison to other projects.')
a(742,p,[48],'idea of the earlier run',[72,74,76,78],[[803,868],[923,986],[1043,1097],[1170,1211]],
 'LM=ML; indépendamment',
 'The earlier run’s assessment of Hua combines a valid ideal-model proof with an overbroad universal autoisomorphism bracket. A bounded literature search cannot establish novelty merely by finding no matching title.',
 'Hua’s document is not independently supplied; its reported claim is checked through the quoted note and the actual manuscript witnesses. The present work claims neither priority nor a new general Morita theorem.',
 'agrees','The substantive positive and negative distinctions survive comparison with the text; the independent Codex reading further narrows the negative conclusion.')
a(743,p,[49],'other',[74,76,78],[[923,986],[1043,1097],[1170,1211]],
 'Conclusion',
 'The historical results-register entry reports the earlier run’s bookkeeping choices; it does not update an external register and is not a manuscript mathematical claim.',
 'Its claims are represented by the separately checked Brandt items. External run names are recorded as leads only.',
 'agrees','The source is an editorial ledger statement; no absent register was treated as read or modified.')
a(744,p,[50],'unproved claim',[74],[[923,950]],
 'localement; dedek.|noeth.; complétions',
 'If all localizations of two finitely generated embedded ideals commute, their global products agree. Over a Dedekind base the converse for all local invertible ideals follows by extending local ideal data. Completion/henselization versions need their own descent hypotheses.',
 'The Pro marginal phrase differs from Codex, which specifies completions if A is noetherian. Faithful flatness proves detection of equality after completion; extending arbitrary completed ideals is a different issue.',
 'understates','The elementary localization proof is valid. The independent marginal reading changes the asserted completion scope and is now explicitly retained as an unresolved scan question.',{50:'corrected'})
a(745,p,[52],'unproved claim',[84],[[1264,1299]],
 'G commutatif; un objet fidèle',
 'The discussion assumes a commutative group of multiplicative type over Q and a finite faithful object with a polarization. These hypotheses place the argument in a finite commutative Tannakian situation.',
 'They do not identify the whole conjectural motivic category with this finite subcategory. In a commutative Lie algebra every map from sl2 is zero; its centre is the whole algebra.',
 'agrees','The note correctly limits the scope and prevents importing a nontrivial Lefschetz sl2 or a centre-free conclusion into the stated commutative band.')
a(746,p,[53],'unproved claim',[84],[[1281,1299]],
 'U; fermé ...; compact',
 'For a positive adjoint involution on the finite-dimensional real endomorphism algebra, elements u with uu′=1 lie on a positive trace-norm sphere; the closed unitary locus is compact.',
 'If U is a connected Q-torus, its rational points are Zariski dense and identities checked there extend to U. Rational points themselves are generally not a compact topological group.',
 'agrees','The note supplies the finite-dimensional norm argument and identifies exactly where rational-point density is required.')
a(747,p,[54],'unproved claim',[84,86],[[1281,1299],[1341,1355]],
 'produit ... corps; involution',
 'A finite-dimensional commutative Q-algebra with a positive involution is reduced and decomposes into number fields, with positive involution on each factor.',
 'Positivity excludes nilpotents using the positive trace form. The factors may be totally real with identity involution or CM with complex conjugation; positivity alone does not exclude the former.',
 'agrees','The note correctly separates the valid field-product step from the stronger CM-only assertion.')
a(748,p,[55],'reading question',[86],[[1341,1355]],
 'extensions quadratiques ... totalement réels',
 'The literal claim that every field factor is CM omits totally real factors with identity involution. The unit object gives B=Q with its positive identity involution.',
 'A pure nonzero-weight or other exclusion might remove that example, but no such restriction is inserted into the manuscript. The counterexample addresses the algebraic hypotheses actually used.',
 'agrees','The note’s real-factor caveat is mathematically necessary under the stated algebraic assumptions; the reading remains unchanged.')
a(749,p,[56],'unpursued implication',[86],[[1341,1369]],
 'groupe ... norme',
 'A CM field factor L/K contributes Res_K/Q(U(1)) to the real unitary group; a totally real factor F with identity involution contributes Res_F/Q μ2, a finite component group.',
 'The identity component stays compact, but ignoring the real factors loses finite sign data.',
 'agrees','This is a correct consequence of the corrected field decomposition, explicitly distinguished from the manuscript’s CM-only wording.')
a(750,p,[57],'unpursued implication',[84],[[1281,1299]],
 'engendrée par ... G(Q)',
 'The Q-algebra generated by rational points need not detect a disconnected group of multiplicative type. The 3-torsion of the norm-one Q(i)-torus has only the identity Q-point although its natural representation is nontrivial.',
 'This is a representation-theoretic test of the proposed method, not a construction of such a band from an actual geometric motive. Connectedness makes the usual density argument available.',
 'agrees','The earlier note correctly labels the example’s scope and does not claim a geometric motivic counterexample.')
a(751,p,[58],'unproved claim',[86],[[1356,1369]],
 'NB ... ε ... normes',
 'For a CM factor L/K on which the representation satisfies ρ(u)overline(ρ(u))=ε(u), the relative norm equals ε viewed in Res_K/Q G_m, whereas the absolute norm equals ε^[K:Q].',
 'For a real factor with identity involution the corresponding relation is ρ²=ε. The exact weight exponent must be fixed by the polarization convention; a missing ε^w is not silently supplied.',
 'agrees','The note distinguishes relative and absolute norm equations, which the compressed NB alone does not spell out.')
a(752,p,[59],'self-flagged step',[86],[[1356,1369]],
 'retrouver ... ε',
 'Recovering a character ε from absolute norm characters requires integral divisibility in X*(G), not only division over Q. For a torus multiplication by a nonzero integer is injective, giving uniqueness if a root exists; coprime degrees give a Bézout reconstruction.',
 'Disconnected groups can have torsion characters and lose uniqueness. The page’s norm remark does not prove divisibility or settle these finite components.',
 'agrees','The note makes the precise integral obstruction explicit rather than treating a rational character equation as an integral one.')
a(753,p,[60],'self-flagged step',[86],[[1356,1369]],
 'j; normes',
 'Recovering the weight cocharacter is an integral lattice problem. For Res_Q(i)/Q G_m every rational split cocharacter has even composite with the norm; hence the norm has no Q-cocharacter section, although weight-two lifts exist.',
 'A compact real kernel has no nonzero split real cocharacter, so a prescribed composite determines at most one lift. Existence remains an integral question.',
 'agrees','The earlier note’s example identifies the difference between uniqueness and existence and does not replace the manuscript’s j by a new convention.')
a(754,p,[61],'reading question',[84,86],[[1264,1299],[1341,1369]],
 'φ(u)φ(u)′=ε(u)1; polarisation',
 'The written similitude identity uses ε once. A modern weight-w polarization may use ε^w, depending on whether ε denotes the Tate character or the particular multiplier.',
 'No pure-weight convention is supplied here that permits changing the exponent. The relevant notation must be resolved by surrounding text or scans.',
 'agrees','The note correctly treats the convention as a visible hypothesis and not as permission to normalize the manuscript.')
a(755,p,[62],'reading question',[86],[[1341,1355]],
 'l’un des s/c tt. réels',
 'For a CM field with the stated positive involution, the fixed field is its unique maximal totally real subfield.',
 'Codex reads the set of totally real elements rather than one of the totally real subfields. This is a mathematical and witness-based reason to revisit the phrase, without deciding it here.',
 'understates','The substantive correction is sound, and the independent Codex alternative strengthens the scan-review case.',{62:'corrected'})
a(756,p,[63],'unpursued implication',[40,52,84,86],[[139,181],[360,393],[1264,1299],[1341,1369]],
 'n’est pas spécial; compact',
 'Compactness of the real unitary group does not imply neutrality of the associated real gerbe. The quaternionic class and finite sign data survive as separate obstructions.',
 'This connects the Deuring and positive-involution sheets without identifying their bands or assuming the same category.',
 'agrees','Both endpoint passages are supplied and read; the comparison is a limitation on inference, not an unproved equivalence of categories.')
a(757,p,[64],'unproved claim',[86],[[1341,1355]],
 'traces ... proportionnelles',
 'For a representation of a number field L on a finite-dimensional Q-vector space V, Tr_V(a)=[dim_L V]Tr_L/Q(a). This supplies the asserted proportionality for the actual representation trace.',
 'An arbitrary positive linear functional on L_R need not be proportional to the field trace. Positivity alone does not prove the written trace assertion.',
 'agrees','The note correctly identifies the representation-theoretic hypothesis that makes the proportionality valid.')
a(758,p,[65],'idea of the earlier run',[86],[[1341,1369]],
 'tore; normes',
 'Later Serre-torus constructions provide a character-lattice method for organizing CM norm relations; these pages do not identify their group with the universal Serre torus or prove its universal property.',
 'The comparison is retained as a research direction with its exact missing map and hypotheses.',
 'agrees','The note distinguishes a useful later method from an identification absent from the text.')
a(759,p,[66],'title, date or page count',[67,69,71,73,75,77,79,85],[[590,618],[661,698],[758,798],[875,917],[994,1039],[1102,1165],[1219,1259],[1304,1336]],
 'La méthode des majorantes; Résolution des équations analytiques',
 'The reused analytical sheets have their own printed-folio order:16,17,23,24,25,26,30, while scan85 is a separate SGA site-comparison leaf. Archive scan order is not proof order.',
 'These are independent mathematical texts reused as paper, not a sequence of motivic arguments. Source attribution is made only where the textual match is verified.',
 'agrees','All eight reused sheets were read; the note correctly separates their order and subject from the handwritten work.')
a(760,p,[67],'reading question',[67],[[590,618]],
 'pα(1−√(...))',
 'The displayed square-root solution of v′=M/[(1−αt)(1−pαv)(1−αΣw)] has the wrong prefactor on the literal reading. Its initial derivative is p²α²M/(1−αΣw), not M/(1−αΣw). The corrected prefactor is1/(pα).',
 'This is an algebraic test under nonzero denominators; p here is the number of unknowns, not the arithmetic prime of the Deuring sheets.',
 'agrees','The initial-value equation gives a direct mathematical alarm without relying on a guessed later printed edition.')
a(761,p,[68],'reading question',[79],[[1219,1235]],
 '(1−Σ binom(2n,n)x^n)²=1−4x',
 'The literal binomial identity fails: its x² coefficient is−8. The expansion of √(1−4x) instead uses binom(2n,n)/(2n−1).',
 'This reproduces a coefficient test and offers a scan candidate, not an emendation. B15-03 scan49 contains the associated square-root discussion and is separately compared.',
 'agrees','The coefficient failure is exact in characteristic0, the setting of the reused analytic sheet.')
a(762,p,[69],'reading question',[71],[[758,798]],
 'α assez petit',
 'For a coefficient bound by Mα^n through factors(1−αt)^−1, α must be sufficiently large relative to the reciprocal convergence radius; decreasing α is not a general majorization method.',
 'The geometric series with coefficients β^n is a direct test: no fixed M bounds all coefficients when0<α<β.',
 'agrees','The note’s alarm follows from the written denominator convention; it does not assert what the ink must say.')
a(763,p,[70],'unproved claim',[69,73,75],[[661,698],[875,917],[994,1039]],
 'intégrabilité; fonctions holomorphes',
 'The reused Frobenius argument is the analytic integrability theorem: a compatibility defect satisfies a homogeneous linear ODE with zero initial condition and therefore vanishes. The associated formal implicit-function recurrence determines each coefficient from lower degrees.',
 'This Frobenius theorem has no connection to the arithmetic Frobenius of the Deuring calculations. Analytic convergence and formal uniqueness remain distinct steps.',
 'agrees','The note correctly separates the two meanings and recognizes the ordinary ODE/implicit-function proofs on these sheets.')
a(764,p,[71],'reading question',[77],[[1102,1114]],
 '−1 ... carré mod p; p≡1(4)',
 'The arithmetic scratchwork concerns whether−1 is a square modulo an odd prime. The criterion is p≡1 mod4; the Codex witness has an inserted negation and p≡−1 mod4.',
 'The Pro and Codex lines cannot be collapsed into one securely read assertion. They may preserve different cases or a negation missed by one witness.',
 'understates','The note’s warning against combining scratch fragments is sound; the independent Codex alternative now identifies the precise sign/negation to check.',{71:'corrected'})
a(765,p,[72],'unproved claim',[85],[[1304,1336]],
 '4.1; petits et grands sites; Leray',
 'The reused étale-site leaf proves a small/big-site comparison using full faithfulness, exactness and a Leray argument. It belongs to SGA4’s site formalism rather than to the canonical-point question for motivic gerbes.',
 'Blank universe symbols and reference slots are preserved. The published proposition must be matched by text and numbering rather than inferred from the topic alone.',
 'agrees','The note correctly identifies a different local-to-global argument with explicit site hypotheses.')
a(766,p,[73],'reading question',[69],[[680,680]],
 '\\mathbf{v}érifient',
 'A TeX command crosses a French word boundary in the supplied diplomatic file. This is markup damage rather than a mathematical disagreement about the ink.',
 'No transcription is edited in this run. The issue is recorded separately from high-impact mathematical reading alarms.',
 'agrees','The malformed command is visible in the supplied text and does not change the underlying mathematical argument.')

if __name__=='__main__':b.save()
