"""Manually authored claim records from full passage reading, primary-source checks and exact computations.
This program serializes records; it does not infer a verdict, fate or mathematical status.
"""
import json,pathlib
B=pathlib.Path(__file__).parent
claims=[]
def C(n,items,cote,scans,lines,his,statement,status,comp,cl,fate,date,present,refs,confidence='high'):
    claims.append(dict(id=f'CL-SA07-{n}',items=[f'SA07-{i}' for i in items],cote=str(cote),scans=scans,lines=lines,his_statement=his,statement=statement,status_on_pages=status,computation=comp,**{'class':cl},fate=fate,fate_date=date,present_status='As of 2026-11-19: '+present,refs=refs,confidence=confidence))

C(201,[229],16,[3,4], '27–122', 'E^ν=Σ π_(i+ν) E π_i; les π_i sont orthogonaux',
  'For a unital ring E with a finite complete family of orthogonal idempotents π_i, the corner sums E^ν=⊕_i π_(i+ν)Eπ_i give a Z-grading and E^νE^μ⊂E^(ν+μ). Conversely a compatible grading has those corners. Multiplication changes degrees by addition, not subtraction.',
  'proof sketched; one displayed degree sign is uncertain in the transcription', 'computations.md §1: corner multiplication proof', 'B',
  'The exact ring framework occurs in Kleiman 1968, Theorem 3.15, p.382. The elementary multiplication check proves the stated reconstruction; the source theorem is stronger and concerns intrinsic recovery of the projectors. Search/open web001 and web009.',
  'Kleiman: IHES lectures 1967; publication 1968', 'Established elementary ring algebra. The possible ν−ν′ reading remains a scan alarm, not an adopted emendation.', ['Kleiman1968'])
C(202,[229],16,[3,4,5,6,7,8], '27–305', 'les π_i sont intrinsèques',
  'Suppose a Z-graded unital ring has orthogonal degree projectors π_0,...,π_2n summing to 1 and the prescribed corner grading. Suppose for each i≤n there are opposite homogeneous corner elements giving two-sided equivalences of π_i and π_(2n−i). Then these projectors are determined by the graded ring; they lie in the center of E^0 and are recovered inductively from annihilators of extremal graded pieces.',
  'proof sketched by stripping extremal degrees; the printed middle-step index is wrong', 'computations.md §1 gives the annihilator induction and the scope of the two-sided hypotheses', 'B',
  'Kleiman 1968, Theorem 3.15, p.382, states precisely this graded-ring result over an arbitrary ring, with both inverse identities. The manuscript is not evidence for the false weaker assertion that any graded ring with a nonzero top piece has intrinsic projectors. Search/open web001, web009.',
  '1968 publication; lectures 1967', 'Established under the stated corner-equivalence hypotheses. Scans 5 and 8 say i=n−1 where the terminal middle step is i=n.', ['Kleiman1968'])
C(203,[229,230],16,[6,7,8,17], '174–305;650–692', 'π_i∈F',
  'If a graded overring or graded subring F contains the homogeneous inverse data and the unit needed by the intrinsic-projector theorem, the same annihilator/inductive formulas place the degree projectors in F. The identities v_iw_i=π_(2n−i) and w_iv_i=π_i are both required and have different supports.',
  'proof sketched; later displayed support condition has the wrong projector', 'C03 in code/computations.py tests the wrong support; computations.md §1 supplies the ring argument', 'B',
  'Kleiman 1968, Theorem 3.15, p.382, is the precise published algebraic framework. His 2.9 and 2.11, pp.371–372, give the corresponding algebraicity statements. Opened web001/web009.',
  '1968', 'Established with correct supports. The literal scan17 inverse criterion is false, separately CL-SA07-211.', ['Kleiman1968'])
C(204,[230],16,[9,10,11,12,13], '265–481', 'M=Σ L^αP^i',
  'Let M=⊕_(r=0)^(2n)M^r be finite-dimensional over a field and L:M^r→M^(r+2) satisfy hard Lefschetz L^(n−i):M^i≅M^(2n−i) for i≤n. Then P^i=ker L^(n−i+1) in M^i yields the direct decomposition M=⊕_(i≤n,0≤α≤n−i)L^αP^i, and normalized lowering sends L^αp to L^(α−1)p for α>0 and p to 0.',
  'proof sketched; definition (6.5) is left blank and some later exponents are inconsistent', 'computations.md §2 gives the general kernel splitting; C02 verifies the exact abstract matrix model', 'B',
  'Kleiman 1968, §1 and §2, uses this normalized lowering convention explicitly, distinguishing it from the classical scalar-weighted operator in his introduction. It is ordinary Lefschetz linear algebra, already based on classical theory, but the exact normalization here matches that published treatment.',
  'Classical background before 1967; exact opened formulation 1968', 'Established for hard-Lefschetz graded vector spaces; the source draft has not completed every displayed formula.', ['Kleiman1968'])
C(205,[230],16,[11,12,13,51,53,55], '350–481;1861–1882;1926–1953;1996–2003', 'Démonstration à fournir',
  'For a hard-Lefschetz realization and its graded algebra of algebraic correspondences, existence of algebraic inverse Lefschetz maps, existence of algebraic normalized lowering, and the appropriate algebraic Lefschetz isomorphisms with algebraic degree projectors are equivalent. The direction reconstructing lowering/projectors is an inductive algebra statement, not a consequence of the ordinary exterior example over Z.',
  'open on the pages at scan13; later scans sketch an induction', 'computations.md §§1–2 and C02 separate the ring theorem from the defective exterior realization', 'A',
  'Grothendieck 1969, pp.196–197, formulates standard B as algebraicity of Λ and states the resulting projectors; Kleiman 1968, Proposition 2.9 and Theorem 3.15, pp.371 and382, supply the precise equivalences and ring proof. Both primary texts opened. Searches web001/web002.',
  'Kleiman 1968 (1967 lectures); Grothendieck conference 1968, publication1969', 'Established equivalence of the conditions. Their truth for every smooth projective variety remains the Lefschetz standard conjecture.', ['Grothendieck1969','Kleiman1968'])
C(206,[231],16,[13,14,33,34,36], '440–527;1246–1364;1393–1445', 'LΛ=1−Σ p_i; ΛL=1−Σ p_(2n−i)',
  'For normalized Lefschetz strings, LΛ is identity except on their bottom primitive endpoints, and ΛL is identity except on their top endpoints. Thus kerΛ is the sum of bottom primitives, kerL the sum of top primitives, and images are the complementary string positions. These p_i are endpoint projectors, not degree projectors π_i.',
  'proved there by string formulas, with shorthand notation', 'C02 and computations.md §2: each formula evaluated on every position of an arbitrary string', 'B',
  'Kleiman 1968, normalized primitive calculus in §§1–2, is the precise published convention. His introduction explains the modification of the classical Λ by numerical factors. Opened web001.', '1968 exact opened formulation',
  'Established. It fails if Λ is replaced by ordinary symplectic contraction without adjusting coefficients.', ['Kleiman1968'])
C(207,[201],16,[14], '507–525', 'sur ℤ !; satisfait à la condition de (6.1)',
  'The page claims that the ordinary exterior algebra of a rank-2n symplectic lattice, with L multiplication by ξ=Σ e_j∧f_j, satisfies its integral Lefschetz condition. For n≥2 this is false: ξ^n=n! e_1f_1...e_nf_n, so the top map is not an isomorphism of Z-lattices.',
  'false as stated under the literal ordinary-exterior and integral conventions', 'C01 exact integer exterior calculation; computations.md §3 gives the all-n combinatorial proof', 'C',
  'Searches of the published normalized Lefschetz treatment (Kleiman1968 §§1–2) and integral Fourier/divided-power literature (Beckmann–de Gaay Fortman2023, §3) identify rational theory and distinct integral refinements, not a proof of the literal model. Rationalization removes this obstruction; divided-power or changed-lattice repairs are additional choices.',
  'Rational formulation published1968; integral comparisons2023', 'Refuted exactly for the ordinary lattice when n≥2. No repair is inserted into the manuscript.', ['Kleiman1968','BeckmannFortman2023'])
C(208,[201],16,[14], '507–525', 'Λ ... contraction',
  'Ordinary symplectic contraction C on the rational exterior algebra satisfies C(L^jp)=j(n−i−j+1)L^(j−1)p for primitive p of degree i. It is not the normalized unit-step Λ of the preceding formulas, even after tensoring with Q.',
  'false as an identification of the two operators; the manuscript reference is currently (6.5|15)', 'C01 verifies exact examples and computations.md §3 derives the scalar formula from the commutator', 'B',
  'Kleiman1968 introduction and §1 explicitly modify the classical operator by scalar factors, providing the exact resolution of this convention conflict. The second-pass cross-reference supersedes the earlier reading but does not alter the mathematics.', '1968',
  'The two operators are standard and distinct. The manuscript identification must be qualified, not silently normalized.', ['Kleiman1968'])
C(209,[226,227],16,[15], '528–597', '0≤α,β≤2n−i; e^i_(αβ)e^j_(γδ)',
  'For primitive type i, the normalized string has positions 0≤α,β≤n−i. The operators E^i_(αβ)=L^αp_iΛ^β are matrix units: E^i_(αβ)E^j_(γδ)=δ_ij δ_βγ E^i_(αδ), and the universal algebra is ⊕_(i=0)^n Mat_(n−i+1)(Z). The displayed bound 2n−i is incorrect.',
  'proof sketched; false displayed bound confirmed by second pass', 'C02 exact matrices and arbitrary-string proof in computations.md §2', 'B',
  'The ring-theoretic structure is developed in Kleiman1968 Theorem3.15; searches web001/web009 found no claim validating the overlong range. The corrected matrix-unit result follows directly on the abstract string model, independently of the failed integral exterior model.', '1968 comparison; present explicit check2026',
  'Established with the position bound n−i. Ink confirmation makes this an authorial slip in the current evidence, not an undecided transcription correction.', ['Kleiman1968'])
C(210,[203,226],16,[15,16,17], '585–692', 'Il faut donc se donner en même temps L et les π_i',
  'The algebra generated by normalized shifts and primitive blocks has a universal mapping property only after specifying the grading/projector data and the relevant Lefschetz identities. A graded homomorphism preserving L and the compatible degree projectors determines lowering; an ungraded homomorphism specified only on L need not.',
  'corrected by himself later; graded hypothesis and projector compatibility appear after the failed formulation', 'C02–C03; arbitrary block argument in computations.md §2', 'B',
  'Kleiman1968 Theorem3.15 retains the graded-ring and corner data. The exact manuscript formulation is not a published universal property identified by title search, but its corrected algebraic content is checked by the matrix-unit construction.', '1968 exact related theorem',
  'Correct with the stated structure; the ungraded version is false, CL-SA07-212.', ['Kleiman1968'])
C(211,[203,230],16,[17], '650–692', '(w_i L^(n−i)−1)π_(2n−i)=0',
  'If w_i is the inverse to L^(n−i):M^i→M^(2n−i), the correct support condition is (w_iL^(n−i)−1)π_i=0, while the reverse composite is supported on π_(2n−i). The displayed use of π_(2n−i) in the first condition is false even for the length-two string.',
  'false as stated; second pass confirms the projector in the ink', 'C03: (ΛL−1)π_2=−π_2 on Q², all hard-Lefschetz hypotheses satisfied', 'B',
  'Kleiman1968 Theorem3.15 writes the two opposite inverse identities separately. Comparison with this exact published result and the explicit counterexample resolves the mathematical issue; it does not emend the scan.', '1968',
  'Refuted literal condition; refined statement is CL-SA07-203.', ['Kleiman1968'])
C(212,[203],16,[16,17], '585–692', 'Non',
  'The question whether L by itself determines the normalized lowering operator or the primitive grading in an ungraded algebra is answered negatively. In a length-two block g=1+tL fixes L under conjugation and sends Λ to Λ+t(π_2−π_0)−t²L.',
  'corrected by himself later: circled negative answer and added grading data', 'C03 exact symbolic conjugation; primitive middle block extends the n=1 universal algebra to rank5', 'B',
  'The graded hypotheses in Kleiman1968 Theorem3.15 match the corrected scope. No separate historical publication of this exact conjugation example was identified; it is our explicit verification of the manuscript withdrawal.', '1968 related theorem; explicit verification2026',
  'The negative answer is correct. The earlier-run witness is clearly distinguished from his text.', ['Kleiman1968'])
C(213,[226],16,[18], '693–724', 'co- ... anneau opposé',
  'Dualizing a finite Lefschetz module reverses cohomological degrees and exchanges the raising/lowering conventions; the associated ring operation is passage to the opposite algebra with the compatible reversed grading. The transpose reverses multiplication order.',
  'stated without full proof in the formulary', 'computations.md §2 gives the transpose calculation, not a new geometric duality theorem', 'B',
  'Kleiman1968 §§1–2 and Theorem3.15 use transpose and graded ring operations in the same algebraic setting. Search/open web001; no additional theorem about arbitrary ungraded anti-isomorphisms is inferred.', '1968',
  'Established formal linear algebra with the reversed grading made explicit.', ['Kleiman1968'])
C(214,[226],16,[18], '693–724', 'E^(2n)≠0 ... L^nΛ^n≠0',
  'In a Lefschetz algebra with the specified complete grading and nonzero primitive degree-zero block, the extreme corners are nonzero exactly when the end degree projectors are nonzero, equivalently the top-string idempotent L^nΛ^n is nonzero. This tests presence of that block, not hard Lefschetz of an arbitrary element.',
  'stated without proof', 'C02 and computations.md §2: extreme corner is the unique full-length block corner', 'B',
  'Kleiman1968 Theorem3.15 provides the precise graded corner setting. The claim is an immediate consequence of the abstract string algebra, checked here; no stronger converse is supported.', '1968 comparison',
  'Established under the finite Lefschetz decomposition; unrelated to the false top-power converse in CL-SA07-215.', ['Kleiman1968'])
C(215,[],16,[20,22], '780–859;898–944', 'L′ ... (L′)^n≠0',
  'A nonzero top power of a degree-two element does not imply hard Lefschetz. In the six-dimensional graded algebra Q[x,y]/(x⁴,y²−xy,x²y−x³), deg x=deg y=2, x is Lefschetz and y³=x³≠0, but multiplication by y:H²→H⁴ has rank1 rather than2.',
  'corrected by himself later: an attempted top-power criterion is followed by the counterexample', 'C04 exact Gröbner reduction and middle multiplication matrices', 'B',
  'Kleiman1968 retains every complementary-degree hard-Lefschetz isomorphism; the weaker top-power criterion does not occur there. Search/open of that exact framework confirms the distinction; the manuscript counterexample has been independently recomputed.', '1968 comparison; example already on pages',
  'Withdrawal is correct. The quotient has dimensions1,2,2,1 and meets every stated hypothesis of the attempted converse.', ['Kleiman1968'])
C(216,[],16,[20], '780–859', 'Λ(λL)=λ^−1Λ(L); Ω/Δ^N',
  'On the Zariski-open set of degree-two endomorphisms satisfying hard Lefschetz on a fixed finite graded vector space, normalized lowering and primitive/degree projection formulas depend rationally on the matrix entries of L; denominators are products of determinants of complementary Lefschetz maps. Scaling gives Λ(λL)=λ^−1Λ(L) for λ≠0.',
  'proof sketched by determinant/inverse formulas', 'computations.md §2 uses adjugates and finite recursive compositions; no finite experiment is used as proof', 'B',
  'Kleiman1968 Proposition2.9 and the algebraic constructions preceding it give the inverse-map formulation; exact title searches found no separate named theorem needed. The rationality assertion follows from those finite matrix inversions under fixed dimensions.', '1968 comparison',
  'Established elementary consequence on the Lefschetz open locus; no uniform denominator over an unspecified integral base is claimed.', ['Kleiman1968'])
C(217,[204,211,213],16,[19], '725–779', 'canoniquement autodual',
  'In the published local-surface setting of BrauerIII §8.4—complete normal two-dimensional local ring A, algebraically closed residue field k lifted to a coefficient subfield of A, regular proper birational resolution isomorphic over the punctured spectrum—its exceptional intersection lattice has a finite discriminant group, with canonical perfect pairing [a],[b]↦aᵀQ^−1b modZ. The leaf identifies the relevant Picard/Néron–Severi quotient with this group.',
  'proof sketched, invoking Mumford; antecedent hypotheses are absent from this reused leaf', 'C05; computations.md §4 proves well-definedness and perfectness for every nonsingular integral Q', 'A',
  'Grothendieck, Le groupe de BrauerIII, §8.4, reproduces this local surface argument; Mumford1961 proves negative definiteness of the exceptional intersection form. These are separate ingredients: negativity does not alone identify Pic(U). Primary PDFs opened/downloaded; exact local passage checked.', 'BrauerIII manuscript1966, publication1968; Mumford received1960, published1961',
  'Established under the published local-surface hypotheses. The missing antecedent is an attribution limit, not a license to generalize to arbitrary singularities.', ['GrothendieckBrauer1968','Mumford1961'])
C(218,[205,211],16,[19], '725–779', 'indépendante de la résolution X′ choisie',
  'The local discriminant pairing is invariant under blow-ups at rational smooth points of the exceptional locus: the new lattice is integrally congruent to Q⊕(−1). Independence across resolutions also uses a common surface resolution and factorization into such blow-ups.',
  'stated with only the invariance conclusion on this leaf', 'C05 symbolic congruence SᵀQ′S=Q⊕(−1), detS=1; general proof in computations.md §4', 'A',
  'Grothendieck BrauerIII §8.4 states resolution independence in the local-surface setting. Mumford1961 supplies the intersection-theoretic framework, not a general higher-dimensional factorization theorem.', '1966 manuscript /1968 publication',
  'Established in the stated surface setting. The explicit matrix proof verifies the elementary step; arbitrary residue fields or higher-dimensional resolutions are outside scope.', ['GrothendieckBrauer1968','Mumford1961'])
C(219,[208,211],16,[19,21], '725–779;860–897', 'Pic^0 ... ℓ-divisible',
  'In the page’s algebraically closed geometric setting and for ℓ different from the characteristic, multiplication by ℓ on the identity Picard component is surjective on points, hence its contribution disappears from Pic/ℓ^m. It does not assert divisibility of the full Picard group.',
  'stated without proof, using the Picard component', 'No numerical computation; the isogeny/surjectivity hypothesis is part of the statement', 'A',
  'Grothendieck BrauerIII §8 uses this Picard-divisibility input in the Kummer discussion. The Picard scheme constructions in his 1962 seminar and the abelian-variety treatment make the prime-to-characteristic scope explicit.', 'Picard seminar1962; BrauerIII1966/1968',
  'Established in this scope; in characteristic p one must not transfer the statement to every nonreduced/inseparable structure or use ℓ=p in the étale Kummer sequence.', ['GrothendieckBrauer1968','GrothendieckPicard1962'])
C(220,[208],16,[21,23], '860–897;945–977', '0→NS⊗Z_ℓ→H²→T_ℓBr′→0',
  'For the proper geometric X and ℓ≠char(k) satisfying the manuscript’s finite-generation and cohomological finiteness hypotheses, inverse limits of the Kummer sequence give 0→NS(X)⊗Zℓ→H²(X,Zℓ(1))→TℓBr′(X)→0. Thus NS torsion identifies with torsion in H² and dim_Qℓ VℓBr′=b₂−ρ after rationalization.',
  'proof sketched in equations (8.3)–(8.7)', 'computations.md §4: inverse-limit exactness and torsion-free Tate-module argument', 'A',
  'Grothendieck BrauerIII §8 contains the Kummer/Tate-module comparison. The exact statements separate finite ℓ-primary torsion, Zℓ-lattices and Qℓ-vector spaces; no equality of integral groups follows merely from the dimension formula.', '1966 manuscript /1968 publication',
  'Established with the stated hypotheses and ℓ≠p. The cohomological Brauer group Br′ is retained; no unsupported replacement by an Azumaya group is made.', ['GrothendieckBrauer1968'])
C(221,[208,212],16,[23], '945–977', 'partie transcendante; Tors H³',
  'For a smooth proper surface over an algebraically closed field and ℓ≠p, Poincaré duality and nondegeneracy of the Néron–Severi intersection form identify VℓBr′ with the orthogonal complement of NS⊗Qℓ in H²(Qℓ(1)). Integral splitting/perfectness depends on the discriminant. The finite quotient of the ℓ-primary Brauer group by its divisible part is related to torsion H³(Zℓ(1)); this is an ℓ-primary statement.',
  'proof sketched; abbreviated notation can hide the ℓ-primary restriction', 'computations.md §4 distinguishes rational orthogonal decomposition from an integral unimodular splitting', 'A',
  'Grothendieck BrauerIII §8 gives the surface pairing and finite-part discussion; the nondegeneracy input is attributed there to Matsusaka. A literal assertion about the entire Brauer group from one fixed ℓ-adic group would overstate the result.', '1966/1968',
  'Established in the prime-to-p setting and with the stated lattice qualifications. Full integral pairings cannot be inferred from rational orthogonality alone.', ['GrothendieckBrauer1968'])
C(222,[212],16,[19,23], '725–779;945–977', 'canoniquement autodual',
  'In the local-surface setting of CL-SA07-217, the discriminant pairing and cohomological pairing should agree under the identified groups, including the sign, cycle/Kummer maps and trace. The published argument additionally assumes char(k)=0 to invoke local duality and predicts this restriction is unnecessary. Abstract perfectness alone does not prove compatibility.',
  'open on the pages in the later published comparison; the reused leaf itself only states discriminant self-duality', 'C05 proves the lattice pairing only, not this geometric comparison', 'C',
  'Grothendieck BrauerIII §8.4, pp.150–151, and Remark8.5, p.151, leave mutual annihilation and agreement with (8.16) unverified. Searches for this exact comparison did not identify a primary source checking its normalization. Later duality is insufficient without tracking these maps.', 'Remark published1968; searched2026',
  'Exact comparison not verified in this run. It remains a sharply specified verification problem rather than a claim that modern duality is unknown.', ['GrothendieckBrauer1968'], 'medium')
C(223,[280],16,[25,27], '978–1062;1113–1155', 'condition d’associativité',
  'For the proposed graded algebra H⁰=k,H¹=V,H²=kξ⊕W,H³=V∨,H⁴=kξ² with the displayed multiplication from alternating φ:∧²V→k, ψ:∧²V→W and symmetric Q on W, associativity is equivalent to the displayed four-variable expression being alternating. Poincaré duality additionally requires Q nondegenerate, and hard Lefschetz additionally requires φ nondegenerate; those conditions do not imply associativity.',
  'proved there by the displayed multiplication check', 'C08 supplies a counterexample to dropping associativity; computations.md §5 checks all degree patterns and derives the four-variable identity', 'D',
  'Searches of Grothendieck/Kleiman Hodge-algebra literature, arXiv and exact four-form terminology found no identified later development of this exact abstract construction. The term Hodge algebra also returns unrelated De Concini–Eisenbud–Procesi straightening algebras; those results are not assigned as its fate.', 'No exact later source identified in searches through2026',
  'The algebraic criterion is independently checked. No geometric realization theorem follows; its later historical fate remains unlocated.', ['Kleiman1968'], 'high')
C(224,[281],16,[27], '1113–1155', 'droite isotrope',
  'An isotropic line is sought in the enlarged quadratic space kξ⊕W, not necessarily in W itself. Over an algebraically closed field of characteristic different from2 a nondegenerate quadratic space of dimension at least2 has an isotropic line. Over an arbitrary field this requires an additional isotropy hypothesis.',
  'stated without proof; the field qualification appears in the discussion', 'C08 checks the basic diag(1,−1) model; computations.md §5 gives the general algebraically closed argument', 'E',
  'The claim is elementary quadratic-form algebra; searches web012–015 found no distinct new geometric theorem attached to this sentence. The exact manuscript restrictions, rather than a same-name modern Hodge-algebra paper, determine its scope.', 'Standard algebra before the manuscript; no new publication identified',
  'Correct with field and dimension assumptions. It does not yield a rational isotropic line over every field.', [], 'high')
C(225,[282,283],16,[27,29], '1113–1155;1188–1206', 'forme alternée à quatre variables; φ arbitraire à un scalaire près',
  'An alternating four-form χ on V defines a symmetric form Qχ on ∧²V by Qχ(x∧y,z∧t)=χ(x,y,z,t). With a vector ξ of Qχ-norm1, φ(x,y)=Qχ(x∧y,ξ) gives the displayed algebra when φ and Qχ are nondegenerate. Realizing an arbitrary φ up to scalar additionally requires its representing vector to have nonzero norm and a scalar normalization available in the field.',
  'construction sketched; arbitrary-φ assertion is broader than the supplied normalization argument', 'C09–C10 give fully specified rational examples; computations.md §5 distinguishes arbitrary realization from these examples', 'D',
  'Exact searches for this four-form construction and induced orbit found no identified later theorem with these quantifiers. Linear algebra identifies φ with a vector only when Qχ is nondegenerate; the norm-one condition is an independent restriction. No general geometric realization is supplied by standard-conjecture literature.', 'No exact later source found; explicit verification2026',
  'The conditional construction is correct; unrestricted arbitrary-φ realization has not been established by the page or the sources searched.', [], 'medium')
C(226,[282,283,284],16,[29], '1188–1206', 'u ... orbite infinie; aussi grande que l’on veut',
  'Under the reconstructed convention u=(∧²φ^−1)∘Qχ on ∧²V, with Qχ and φ nondegenerate and Qχ(ξ,ξ)=1, there are rational examples where the orbit of ξ is infinite. Across growing dimensions there are examples whose cyclic span has arbitrarily large dimension. Infinite orbit and unbounded cyclic dimension are separate assertions; over finite fields every orbit is finite.',
  'open on the pages; operator normalization and V/W letter remain uncertain', 'C09 proves a concrete dimV=6 infinite orbit by a positive matrix growth bound; C10 and computations.md §5 prove a rational family in dimV=4m with cyclic dimension≥m', 'D',
  'Exact four-form/orbit searches across arXiv, primary bibliographies and mathematical search indexes did not identify a later settlement of this specific abstract problem. The present certificates establish the stated reconstruction only, and do not establish the existence of a smooth projective variety realizing it.', 'No exact later fate identified; explicit certificates2026',
  'Affirmative for the explicitly specified abstract rational formulation. This is a new check in this run, not attributed to Grothendieck or to a later source. The ink-dependent operator identification remains unresolved.', [], 'high')
C(227,[232],16,[34,38], '1317–1364;1464–1522', 'P^i(X)→P^i(Y)',
  'For a smooth ample hyperplane Y⊂X of dimension n−1 in a Weil cohomology satisfying hard and weak Lefschetz, primitive restriction is an isomorphism below degree n−1 and injective at degree n−1. The middle cohomology of Y has an additional evanescent summand killed by Gysin.',
  'proof sketched; diagram and scratch indices contain errors', 'C11 and computations.md §6 describe the restriction and Gysin maps on arbitrary strings, with the evanescent summand separate', 'B',
  'Kleiman1968 Proposition2.12 and its proof, pp.372–373, use exactly this hyperplane Lefschetz decomposition. The second-pass correction i+j=n−1 rather than ≤ controls where the scratch identification is valid.', '1968',
  'Established with the cohomological Lefschetz hypotheses; incorrect draft indices are retained in readings.', ['Kleiman1968'])
C(228,[231,232],16,[33,34,36,38,40], '1246–1445;1464–1585', 'φ_*φ*=L; Ker φ_*',
  'Restriction drops the final position of each surviving X-string, Gysin raises surviving Y-strings by one position, and Gysin kills the evanescent middle part. Hence i_*i*=L_X and the indicated kernels/images are the top or bottom primitive endpoint sums. These formulas use normalized lowering and endpoint p_i.',
  'proved or sketched by the formulary, with several ill-typed scratch composites', 'C11 checks the maps; computations.md §6 gives all-position proof', 'B',
  'Kleiman1968 Proposition2.12, pp.372–373, is the exact later hyperplane argument. Its map directions prevent reading φ* twice where the target requires φ_*. Opened web001/web009.', '1968',
  'Established. An isolated scratch formula with the wrong target is not a different theorem.', ['Kleiman1968'])
C(229,[232],16,[40], '1544–1585', 'Λ_Y=φ*Λ_X²φ_*',
  'Under the same smooth hyperplane and Lefschetz hypotheses, the normalized lowering operator on Y equals i*Λ_X²i_*. It vanishes on the evanescent middle summand, and on every surviving string lowers one step.',
  'proved there as the final boxed formula', 'C11 exact examples plus arbitrary-string proof computations.md §6', 'B',
  'Kleiman1968 Proposition2.12, p.372, publishes precisely this identity and its algebraicity consequence. It is not the formula for the unnormalized classical sl₂ contraction.', '1968',
  'Established in the normalized convention.', ['Kleiman1968'])
C(230,[232],16,[36,40,42], '1393–1445;1544–1659', 'φ_*Λ_Y^mφ*=qΛ_X^(m−1)q',
  'For m≥1, let q be the projection onto the non-endpoint positions of X-strings. Then i_*Λ_Y^m i*=qΛ_X^(m−1)q. Equivalent polynomial identities include ΛL+LΛ=T−p_n and L²Λ+2LΛL+ΛL²=LT+TL for the endpoint-defined T. Iteration requires its stated range and vanishing conventions.',
  'proof sketched in the formulary; some indices and domains are abbreviated', 'computations.md §6 evaluates both sides at every string position and checks the endpoint cases; C02/C11 are finite certificates', 'B',
  'Kleiman1968 Proposition2.12 gives the operative basic identity. The higher powers are direct consequences checked here; searches did not identify a separate published claim extending them beyond the string hypotheses.', '1968 basic identity; direct verification2026',
  'Established with q and m defined as above. Unrestricted versions ignoring endpoint cutoffs are not asserted.', ['Kleiman1968'])
C(231,[232],16,[40,42,45,46], '1544–1659;1728–1784', 'C(X)⇒C(Y)',
  'The manuscript C, namely algebraicity of normalized inverse Lefschetz (published B), descends from a smooth projective X to a smooth ample hyperplane Y. The converse is not unconditional: it needs an additional algebraic inverse/surjectivity input on X or the relevant product.',
  'corrected by himself later: unconditional equivalence struck, final implication retained', 'CL-SA07-229 gives the explicit algebraic composite', 'A',
  'Grothendieck1969 pp.196–197 states stability under hyperplane sections; Kleiman1968 Proposition2.12 gives an exact necessary-and-sufficient inverse-map criterion. Opened primary sources match the direction, not the struck equivalence.', '1968/1969',
  'Established forward implication; reverse remains conditional exactly as stated.', ['Grothendieck1969','Kleiman1968'])
C(232,[232,233],16,[42,45,46,50], '1614–1659;1728–1784;1833–1860', 'A(X×X) ... C(X)',
  'Algebraic hard Lefschetz on X×X implies algebraicity of the inverse Lefschetz operator on X. The manuscript’s narrower critical-degree arguments combine known B on a smooth hyperplane with an algebraic hard-Lefschetz surjectivity condition on X×X or X×Y and iterate along hyperplane flags. Quantification over polarizations/products is essential.',
  'proof sketched through products and flags', 'computations.md §6 gives the degree bookkeeping; no numerical test proves the algebraic-cycle surjectivity premise', 'A',
  'Grothendieck1969 p.196 explicitly states A(X×X)⇒B(X). Kleiman1968 Proposition2.13, pp.372–373, gives the refined hyperplane/product criterion, and Proposition2.14 gives the universal A(k)⇔B(k) implication. Both endpoints checked.', 'Kleiman1968; Grothendieck1969 from1968conference',
  'The implications are established. Their premises are standard conjectures, not generally known truths.', ['Grothendieck1969','Kleiman1968'])
C(233,[224,235],16,[44], '1717–1727', 'A+I⇒B',
  'Under hard Lefschetz, algebraic Lefschetz surjectivity and the Hodge-type positivity form imply equality of numerical and homological equivalence on rational algebraic cycles. The manuscript letters are local: its B here is inferred from context and must not be confused with published standard B.',
  'stated without a new proof in the letter; positive-characteristic cohomology-independence claim is qualified', 'computations.md §7 separates positivity/nondegeneracy from finite-dimensionality', 'A',
  'Grothendieck1969 pp.197–198 explains A plus Hodge-type positivity and numerical=homological equivalence; Kleiman1968 §3 gives the precise positivity argument. The exact manuscript letter dictionary remains partly contextual.', '1968/1969',
  'Established implication under positivity. General characteristic-p positivity remains conjectural.', ['Grothendieck1969','Kleiman1968'])
C(234,[234],16,[48], '1797–1818', 'polynôme caractéristique rationnel',
  'If an invertible algebraic cohomological endomorphism u has characteristic polynomial in Q[t], its inverse is a polynomial in u with rational coefficients by Cayley–Hamilton. Applied to the correctly ordered composite of an algebraic complementary-degree isomorphism and a Lefschetz map, with degree projectors if needed, this gives an algebraic inverse.',
  'proof sketched; abbreviated powers and multiplication order need a type check', 'computations.md §7 writes u^−1=−a_0^−1(u^(r−1)+a_(r−1)u^(r−2)+...+a_1)', 'B',
  'Kleiman1968 Proposition2.9, p.371, states the equivalence using the rational characteristic-polynomial condition and algebraic complementary isomorphisms. His Proposition2.11 handles algebraic isomorphism inverses. This is the exact published comparison.', '1968',
  'Established conditional argument. Rationality of characteristic polynomials of arbitrary correspondences is a substantive premise in positive characteristic.', ['Kleiman1968'])
C(235,[234,235],16,[48,49], '1797–1832', 'indépendant de L',
  'Once the Lefschetz standard conjecture holds for one ample polarization on X, the algebraic inverse/isomorphism criterion shows it for every ample polarization; the condition is intrinsic to X and the cohomology theory.',
  'stated as consequence', 'No additional computation beyond Cayley–Hamilton and inverse-map criterion', 'B',
  'Kleiman1968 Corollary2.10, p.371, proves independence of the chosen polarization. Opened exact locator, not merely a survey assertion.', '1968',
  'Established. This does not itself prove independence of the entire cohomology theory without further standard-conjecture hypotheses.', ['Kleiman1968'])
C(236,[234,237],16,[48,49], '1797–1832', 'l’inverse est algébrique',
  'Under the Lefschetz-standard hypotheses for the relevant smooth projective varieties, an algebraic correspondence inducing an isomorphism of their cohomology has algebraic inverse. Within a fixed degree corner the rational characteristic-polynomial argument is a sufficient criterion.',
  'proof sketched', 'computations.md §7 distinguishes a square isomorphism from arbitrary injection/surjection', 'B',
  'Kleiman1968 Proposition2.11, pp.371–372, is the exact inverse-isomorphism theorem. The later splitting statement uses positivity in addition and is CL-SA07-238.', '1968',
  'Established under the stated standard hypotheses; not a theorem that every inverse of an arbitrary linear map is algebraic.', ['Kleiman1968'])
C(237,[236,237],16,[49], '1819–1832', 'C(X) et I(X×X) ... semi-simple',
  'If the Lefschetz standard conjecture B(X) and Hodge-type positivity for algebraic cycles on X×X hold, the Q-algebra of homological algebraic correspondences acting on H*(X) is finite-dimensional and semisimple. A faithful positive trace form with the adjoint involution rules out a nonzero nilpotent radical.',
  'proof sketched as a conditional algebra argument', 'computations.md §7 gives the radical/involution argument and identifies positivity as the key input', 'B',
  'Kleiman1968 Proposition3.12 and Lemma3.13, p.381, exactly prove this conditional homological semisimplicity. Jannsen1992 Theorem1 proves unconditional semisimplicity for numerical motives, a different quotient; it cannot be substituted for the manuscript statement.', 'Kleiman1968; Jannsen submitted1991/published1992',
  'Conditional theorem established. General homological=numerical equivalence remains unproved; numerical semisimplicity is established.', ['Kleiman1968','Jannsen1992'])
C(238,[237],16,[49], '1819–1832', 'u injectif ... inverse à gauche',
  'For algebraic correspondences between polarized cohomologies with the standard Lefschetz and product-positivity hypotheses, injective maps admit algebraic left inverses and surjective maps algebraic right inverses. The proof uses a positive adjoint and inversion of u†u on the source, with the exact ambient product hypotheses retained.',
  'stated without a detailed proof on the leaf', 'computations.md §7 checks source/target of u†u and the inverse composite', 'B',
  'Kleiman1968 Proposition3.14, pp.381–382, is the precise published splitting result. It uses positivity; the weaker inverse-isomorphism proposition alone does not prove every injection splits algebraically.', '1968',
  'Established with the stated positivity and algebraicity hypotheses.', ['Kleiman1968'])
C(239,[238,239],16,[49], '1819–1832', 'catégorie ... semi-simple',
  'A pseudo-abelian Q-linear category whose endomorphism algebras of all finite direct sums are finite-dimensional semisimple is semisimple abelian. Applying this to homological motives is conditional on the manuscript standard-conjecture inputs; applying it to numerical motives is a separate established theorem.',
  'open on the pages as a construction programme supported by the conditional semisimplicity assertion', 'computations.md §7 explains why finite direct sums are needed to control all Hom spaces', 'B',
  'Jannsen1992 Theorem1, p.448, and Lemma2, p.449, prove numerical semisimplicity and the categorical criterion. His Corollary1 discusses nilpotent kernels under algebraic Künneth projectors. This does not identify the numerical quotient with an arbitrary Weil-cohomological quotient.', 'Submitted12July1991; published1992',
  'Numerical category established unconditionally over any field with characteristic-zero coefficients. The manuscript homological category remains conditional in general.', ['Jannsen1992','Kleiman1968'])
C(240,[234,235,240],16,[44,48,50], '1717–1727;1797–1818;1833–1860', 'projecteurs ... car. pol. rationnel',
  'Algebraic Künneth projectors isolate cohomological degrees, allowing traces of algebraic correspondences to be related to intersection numbers. With the further standard-conjecture framework, characteristic polynomials have rational/integral coefficients and theory-independence properties. Existence of separate projectors in one realization is not by itself a uniform ℓ-independent cycle construction.',
  'stated conditionally; overly rapid positive-characteristic independence suggestion is qualified on scan44', 'computations.md §7 separates rational traces, fixed denominators and integrality', 'A',
  'Grothendieck1969 pp.194–195 states the characteristic-polynomial question and the Künneth/denominator argument; pp.197–198 distinguish uniform cycles across ℓ. Kleiman1968 Theorem3.16, pp.382–383, gives consequences under standard conjectures. Katz–Messing1974 proves finite-field algebraic Künneth projectors, not all inverse Lefschetz conjectures.', '1969; finite-field result1974',
  'Several conditional consequences and finite-field Künneth cases are established; universal standard B and every asserted theory-independence statement must retain their hypotheses.', ['Grothendieck1969','Kleiman1968','KatzMessing1974'])
C(241,[235,241,242],16,[45,46,47], '1728–1796', 'surfaces; variétés abéliennes; dimension trois',
  'The letters regard the Lefschetz standard condition as known for curves, surfaces and abelian varieties, while seeking reductions for higher dimension. Algebraic hard Lefschetz in characteristic zero and small dimension is weaker than algebraicity of every inverse; the product conditions can raise the dimension to five or six.',
  'stated as known cases and open extension programme', 'computations.md §6 provides dimension/degree bookkeeping only', 'A',
  'Kleiman1968 Theorems2A9–2A11, pp.376–377, prove the H¹/surface/abelian cases; Grothendieck1969 p.197 lists complete intersections, Grassmannians and abelian varieties. Current primary Tankeev2011 result covers complex threefolds with Kodaira dimension<3, not all threefolds. Searches web002 rejected unsupported 2026 claimed general solutions.', 'Classical cases consolidated1968/1969; Tankeev received2009/published2011',
  'The known classes are established. General Lefschetz standard B remains open; no accepted general solution was identified as of the search date.', ['Kleiman1968','Grothendieck1969','Tankeev2011'], 'high')
C(242,[242],16,[47], '1785–1796', 'Il faut donc renoncer ...',
  'The hope to reduce arbitrary varieties to smooth hypersurfaces is explicitly withdrawn after Serre points out the simply connectedness obstruction in the relevant dimension. The next sentence asks whether singular hypersurfaces might serve instead.',
  'corrected by himself later on the same leaf: smooth-hypersurface proposal withdrawn', 'No computation; this is a checked logical and historical withdrawal, not a new general non-domination theorem', 'A',
  'The published standard-conjecture accounts retain product/hyperplane-section implications and known smooth complete-intersection cases, not this unrestricted reduction (Grothendieck1969 pp.196–197; Kleiman1968 §2). No exact later theorem restoring the withdrawn proposal was found.', 'Withdrawal on manuscript; published accounts1968/1969',
  'Record as withdrawn. The precise geometric relation originally intended is not fully specified, so the fundamental-group sentence is not expanded into a stronger theorem.', ['Grothendieck1969','Kleiman1968'])
C(243,[242],16,[47], '1785–1796', 'hypersurfaces singulières ?',
  'Could a suitably controlled construction using singular hypersurfaces yield the desired standard-conjecture reduction? The page does not define the singularity class, replacement cohomology, correspondence relation or implication to smooth motives.',
  'open on the pages', 'None: the geometric reduction is not specified sufficiently to compute', 'F',
  'Searches of standard-conjecture reductions, Grothendieck1969 and Kleiman1968 found established smooth product/hyperplane reductions but no theorem matching this unspecified singular-hypersurface hope. General modern intersection-cohomology results are not automatically a solution.', 'Searched2026; no exact identified formulation',
  'Not identifiable as a single modern theorem without a reconstructed reduction statement.', ['Grothendieck1969','Kleiman1968'], 'medium')
C(244,[233],16,[42,50], '1614–1659;1833–1860', 'A′; A″',
  'The weak conditions A′ and A″ aim to retain only the critical algebraic hard-Lefschetz surjectivity needed on X×X or X×Y and then induct along hyperplane sections. The manuscript switches between codimension and cohomological degree; only an explicitly degree-correct reconstruction yields a theorem.',
  'proof sketched; definitions are not consistently indexed as written', 'computations.md §6 gives dim(X×X)=2n, dim(X×Y)=2n−1 and the corresponding degree2/4 shifts', 'A',
  'Kleiman1968 Proposition2.13 publishes precise restricted product criteria, and Grothendieck1969 p.196 states the cleaner A(X×X)⇒B(X). These are verified replacements at the mathematical-statement level, not changes to his draft notation.', '1968/1969',
  'The corrected reductions are established. The literal A′/A″ draft cannot be cited as a final unambiguous theorem.', ['Kleiman1968','Grothendieck1969'])
C(245,[233,235],16,[50], '1833–1860', 'pour déduire les conjectures de Weil',
  'Deriving the Weil bounds from the Lefschetz-standard machinery also uses Hodge-type positivity on the relevant product. The line mentioning only the lettered Lefschetz conditions is insufficient unless I is retained from context; positivity is not a consequence of their names.',
  'stated in abbreviated form; missing positivity hypothesis if read in isolation', 'computations.md §7 identifies the positive adjoint estimate used in the standard-conjecture proof', 'C',
  'Grothendieck1969 p.197 explicitly states B(X)+Hdg(X×X) as the sufficient standard-conjecture input. Deligne1980 proves the Weil conjectures by another method; their truth does not retrospectively prove the missing logical implication or the standard conjectures.', 'Grothendieck1969; Deligne WeilII1980',
  'Weil conjectures are established; the manuscript deduction must retain positivity. General standard conjectures remain open.', ['Grothendieck1969','DeligneWeilII1980'])
C(246,[230],16,[51,53,55], '1861–1882;1926–1953;1996–2003', 'algèbre homogène ... transposition ... ξ et l’inverse',
  'For a graded correspondence algebra stable under the stated transpose and containing the Lefschetz operator and inverse data, recursive removal of primitive blocks constructs algebraic degree projectors and normalized lowering. The final notes sometimes use L for the lowering operation while ξ raises degree; their symbols must be typed locally.',
  'proof sketched with explicit induction; two exponents have inconsistent signs', 'computations.md §§1–2 reconstructs the induction with sources/targets; C02 supplies exact block certificates', 'B',
  'Kleiman1968 Proposition2.9 and Theorem3.15, pp.371,382, are the exact later algebraic results. They justify the correctly typed reconstruction, not every scratch exponent on scans53/55.', '1968',
  'Established after type-correct reconstruction. The manuscript exponents are preserved as reading alarms.', ['Kleiman1968'])

C(247,[221],16,[26], '1063–1112', 'C_η se prolonge en un sous-groupe de Cartan C de G',
  'The editorial correction says that a generic Cartan subgroup in the indicated subgroup H extends, after shrinking the base, to a Cartan subgroup C of G contained in H. This is used within the constructibility proof, with H a torus centralizer; it is not an arbitrary extension theorem without finite presentation and generic hypotheses.',
  'stated as a replacement paragraph in corrections to SGA D XV–XVII', 'Text comparison, not an independent proof of the group-scheme theorem', 'A',
  'SGA3 XV, proof of Proposition6.2(iii), reedition p.273 (original marginal427–428), PDFp41, is the exact paragraph. It writes Cartan of H_η in the first sentence; the manuscript writes G_η. Proposition1.2, p.234, also contains the requested XVII App.III reference. Other draft page numbers remain individually bibliographic, not all identified by this one match.',
  'Original notes1964 per SGA3 XV introductory footnote; Springer publication1970; reedition PDF2008',
  'Established contextual argument. This is a reused editorial leaf in SGA3, separate from SGA4 material in cote15.', ['SGA3XV'])
C(248,[209],16,[39], '1523–1543', 'Theorem3.1; Proposition3.2 [Matlis]',
  'Over a commutative noetherian ring A every injective module is a direct sum of indecomposable hulls E(A/p), with unique multiplicities up to isomorphism. For the hull of k(p), the submodules annihilated by powers of pA_p have successive quotients dual to the associated-graded pieces of A_p, hence the displayed equal dimensions.',
  'stated as an explicitly cited theorem of Matlis on a reused typescript, not as an original Grothendieck result', 'computations.md §8 explains the Hom/annihilator filtration and uniqueness qualification', 'E',
  'Matlis1958 Theorem2.5, Proposition3.1, Theorem3.3 and Theorem3.10, pp.515–525, give decomposition, classification, multiplicity uniqueness and the dual graded pieces. Full passages opened/read. The embedded summands are not canonically unique.', 'Received10April1958, revised9June1958; published1958',
  'Established before these notes. The reused page cites the correct source, but its word uniquely means up to the stated isomorphism data.', ['Matlis1958'])
C(249,[210],16,[37], '1446–1463', 'the sheaf Ĩ is injective in the category ... of all O_X-modules',
  'For A noetherian, p∈SpecA and I the injective hull of k(p), the associated sheaf is the pushforward from the local one-point ringed space at p and is injective among all O_X-modules. The following proposition begins the decomposition of quasi-coherent injective sheaves into these hull sheaves on a locally noetherian scheme; its continuation is not supplied on this leaf.',
  'proved there for the hull sheaf by exactness of stalks and adjunction; next proposition only begins', 'computations.md §8 gives the adjunction proof and distinguishes this from arbitrary quasi-coherent sheaves', 'B',
  'Matlis1958 Lemma3.2 and localization results justify the local hull description. Stacks09T1 Lemma36.8.1 confirms a related flasqueness result for injective quasi-coherent sheaves; it is not falsely cited as the full all-modules injectivity theorem. Exact source of this reused typescript was not securely identified.', 'Matlis1958; precise reused-typescript provenance unlocated',
  'Hull-sheaf lemma independently verified. No claim that a general quasi-coherent sheaf is injective is made; the missing continuation limits exact textual attribution.', ['Matlis1958','Stacks09T1'])
C(250,[218,219],16,[41], '1586–1613', 'Corollary2.2 ... coherent ... good exercise ... way-out functors',
  'On a locally noetherian scheme, RHom(L,M) has coherent (respectively quasi-coherent) cohomology when L∈D^- has coherent cohomology and M∈D^+ has coherent (respectively quasi-coherent) cohomology. The second case permits L∈D^+ provided internal Ext^i(F,M)=0 uniformly for i>N and every coherent F. It concludes coherence, not boundedness below of RHom.',
  'self-flagged step: proof left to the reader; the uniform-vanishing hypothesis is explicit', 'C12 tests necessity of an extra hypothesis; computations.md §8 gives the truncation/way-out argument and its local formulation', 'B',
  'Stacks0D0C Lemma36.11.5 is the precise bounded-above/bounded-below coherent result. Stacks0G4H Lemma47.15.2 proves the finite-injective-dimension module analogue. Neither source is represented as proving boundedness in the second case. The source typescript remains unattributed.', 'Modern Stacks versions opened2026; classical derived-coherence framework predates them',
  'Established with the relevant boundedness or uniform Ext control. Without that control L=M=⊕_(i≥0)k[−i] over a field has H⁰RHom=∏_(i≥0)k, disproving coherence; it does not satisfy the page’s extra hypothesis.', ['Stacks0D0C','Stacks0G4H'])
C(251,[220],16,[43], '1706–1716', 'Vider (ii) sauf raison sérieuse',
  'The EGA correction removes the second draft assertion and emphasizes the residue-field separability obstruction at the closed point of a complete local k-algebra finite over a power-series ring. The exact draft (ii) is not available in this leaf.',
  'corrected by himself later in an editorial note', 'No numerical computation; the obstruction follows because an unramified closed fibre is a separable field extension', 'A',
  'Published EGAIV4 Remark18.11.6 retains precisely the non-closed-prime restriction and explains the inseparable residue-field obstruction; the draft two-part statement is absent. The primary PDF was located but oversized in the web tool; exact primary-page verification is recorded separately in the reference record, not inferred from a modern translation.', 'EGAIV4 published1967',
  'The correction has a published counterpart. Full equality with the missing draft(ii) cannot be asserted.', ['EGAIV4'], 'medium')
C(252,[214],16,[52], '1889–1904', 'premier idéal de Filting de Ω_A(B)',
  'For a finitely presented A-algebra B, define the Kähler different as Fitt⁰_B Ω_(B/A). It commutes with arbitrary base change and its vanishing set is the ramification locus. For a module M generated by r elements, Ann(M)^r⊂Fitt⁰(M)⊂Ann(M). The presentation used for Ω must be a B-module presentation, not the displayed A^p→A^q.',
  'definitions and properties stated without proof; presentation ring is ill-typed', 'computations.md §9 gives the minors/base-change and annihilator arguments', 'B',
  'Stacks0BVV, Definition49.7.1 and Lemmas49.7.2–49.7.4, are exact modern counterparts, including the square Jacobian formula. This verifies the mathematics while leaving Filting/Fitting and A/B as separate ink questions.', 'Classical Fitting theory before manuscript; exact opened modern formulation2026',
  'Established in the stated finite-presentation setting. Fitting indexing conventions are explicitly translated.', ['Stacks0BVV'])
C(253,[215],16,[52], '1906–1908', 'Si ... C intersection complète locale sur B, la formule ... marche',
  'A safe precise transitivity statement is: for a tower of finite locally free complete-intersection algebras A→B→C, the Kähler different satisfies D_(C/A)=D_(B/A)C·D_(C/B). The manuscript’s abbreviated condition only on C/B does not specify the required relative dimension or antecedent finiteness assumptions.',
  'open on the pages as a requested exposition: dire ce qu’on sait', 'computations.md §9 derives the product from a block-triangular Jacobian; the finite-flat complete-intersection hypotheses ensure the square presentations', 'B',
  'Stacks0BWE and0BWD give the local square presentation and Jacobian different for quasi-finite syntomic maps; Stacks0BWG identifies it with the dualizing different. Stacks0BT4 gives only a transitivity map of dualizing modules in general, so it is not cited as an unconditional ideal equality.', 'Modern formulation checked2026; classical special case known earlier',
  'Established with the stated sufficient hypotheses. Broader literal scope of the shorthand remains undetermined.', ['Stacks0BWE','Stacks0BWD','Stacks0BWG','Stacks0BT4'])
C(254,[216],16,[52], '1910–1912', 'différente de Dedekind ... coïncide ... valuation discrète',
  'For a finite extension of discrete valuation rings A⊂B with separable fraction-field extension, the trace-dual Dedekind different agrees with the Kähler different. More generally the trace comparison and complete-intersection equality require the noetherian finite-flat/generic-étale hypotheses specified by the relevant source; arbitrary inseparable towers are not covered.',
  'stated as a theorem to include, with proof reference to an unavailable draft chapter', 'computations.md §9 separates trace-dual definition from the Jacobian calculation', 'E',
  'Stacks0BW0 defines the trace-dual different with precise total-quotient hypotheses; Stacks0BTC Lemma49.9.2 compares it to the dualizing different, and0BWG handles the complete-intersection Kähler equality. These exact definitions establish the safe scope, not an equality without separability.', 'Classical different theory before the manuscript; current precise sources opened2026',
  'Established in the stated DVR setting.', ['Stacks0BW0','Stacks0BTC','Stacks0BWG'])
C(255,[216],16,[52], '1912–1916', 'si A et B sont réguliers ... intersection complète relative',
  'A morphism locally of finite type between regular schemes is a local complete intersection morphism. In the noetherian ring formulation a finite-type map of regular rings admits local factorizations through polynomial rings by regular immersions. Finiteness is necessary to specify the standard notion used here.',
  'stated without proof in the editorial outline', 'computations.md §9 gives the polynomial-ring factorization argument', 'B',
  'Stacks068E Lemma37.62.11 is the exact statement and proof. It supplies the missing locally-finite-type hypothesis rather than treating every abstract map of regular rings as a finitely presented complete intersection.', 'Modern exact statement opened2026',
  'Established with the finiteness convention made explicit.', ['Stacks068E'])
C(256,[207],16,[52], '1914', 'R monogène ssi les idéaux maximaux ... homogènes',
  'The literal criterion has no defined grading, so homogènes cannot be given a mathematical meaning from this leaf. Even the tempting alternative principaux is false for arbitrary finite k-algebras with étale semisimple quotient: F₂³ has principal maximal ideals and is not monogenic over F₂.',
  'not identifiable literally; the suggested alternative is false without extra field hypotheses', 'C06 exhaustively evaluates all eight candidate generators; computations.md §9 proves the cardinality obstruction', 'F',
  'Searches in étale-algebra/local-structure sources found only qualified primitive-element and standard-étale statements. Stacks0G1A Lemma10.144.2 explicitly records a finite-field failure of a global standard-étale presentation, consistent with the obstruction. The referenced Bourbaki draft proposition was not supplied.', 'Searches2026; no exact intended statement identified',
  'Requires scan/context recovery. No new reading is adopted.', ['Stacks0G1A'])
C(257,[206],16,[54], '1980', 'P≠0 ... donc x∈R tel que P(x)≠0',
  'A nonzero polynomial on a finite-dimensional vector space over an infinite field has a rational nonvanishing point. Over a finite field this inference is false; the discriminant polynomial for generators of F₂³ is nonzero geometrically but vanishes at every F₂-rational point.',
  'proof sketch with a missing or implicit infinite-field antecedent', 'C06; computations.md §9 identifies the Vandermonde discriminant and the finite-field failure', 'E',
  'The primitive-element/local étale structure in Stacks0G1A distinguishes local presentation from global monogeneity. Exact draft antecedents were unavailable. The elementary nonvanishing fact is known before the manuscript; its application here is conditional on that omitted antecedent.', 'Classical fact; exact context unlocated',
  'Correct over infinite k; finite-field counterexample refutes the unrestricted fragment, not necessarily its missing original theorem.', ['Stacks0G1A'])
C(258,[222],16,[54,56], '1972–1988;2010–2026', 'B finie ... fibres étales ... B étale finie',
  'Finite geometric fibres that are reduced and separable do not imply flatness of a finite algebra. A=k[t], B=A×A/(t) has every geometric fibre a product of copies of the residue field but is not flat. Adding finite presentation and flatness gives the étale criterion explicitly stated on scan56.',
  'false as an unrestricted finite-fibre criterion; later definition explicitly includes flatness', 'C06 symbolic torsion and complete fibre calculation', 'A',
  'EGA étale theory and the exact current Stacks00U2/0257 formulations retain flatness. The source fragment refers to missing preceding conditions, so the example isolates the missing hypothesis rather than asserting the full original theorem was false.', 'EGA1967; current statement checked2026',
  'The flat criterion is established; the unrestricted fibre-only version is refuted.', ['Stacks00U2','Stacks0257'])
C(259,[217],16,[54], '1992', 'équivalence ... algèbres étales finies sur A et ... A/I',
  'For a nilpotent ideal I of a ring A, base change induces an equivalence between finite étale A-algebras and finite étale A/I-algebras, including uniqueness of lifted maps.',
  'open on the pages as an appendical theorem to be included; reference Voir SGA', 'computations.md §9 explains formal étaleness/patching, without conflating it with monogeneity', 'A',
  'Stacks0BQB Lemma58.8.3 proves finite-étale invariance for thickenings and hence this case. This is a standard SGA étale result; the manuscript does not specify an exposé/proposition, so no unverified exact SGA locator is invented.', 'SGA theory1960s; exact opened modern locator2026',
  'Established, including arbitrary nilpotent thickenings.', ['Stacks0BQB'])
C(260,[222],16,[54,56], '1958–1960;2008–2046', 'étale=non ramifiée+plate; chgt d’anneau; complétions',
  'For finitely presented ring maps, étale means flat and unramified. Étaleness is stable under composition and arbitrary base change and descends faithfully flatly; an étale algebra over a reduced base is reduced. In the noetherian local essentially-finite-type setting it can be checked on completions; with equal residue fields the complete local rings are isomorphic. Finite étale algebras of fixed rank split after faithfully flat base change and étale maps are locally standard étale.',
  'stated as a list of established properties to arrange in an exposition', 'computations.md §9 separates the finite-rank splitting from the local standard presentation; no new numerical calculation', 'A',
  'Opened Stacks00U2 Lemma10.143.3,0257 Lemma41.11.3 and0G1A Proposition10.144.4 match composition/base change, completion and local structure respectively. The noetherian and finite-presentation assumptions are retained. Individual statements are standard EGA/SGA theory.', 'EGA/SGA1960s; exact current locators checked2026',
  'Established with the stated hypotheses. The connected-base qualification in the fixed-copy splitting statement controls constant rank.', ['Stacks00U2','Stacks0257','Stacks0G1A'])
C(261,[223],16,[52], '1920–1922', 'extraire la racine n-ième d’une uniformisante ... exp(2iπ/n)',
  'In a complete discretely valued tame totally ramified situation, a Kummer description by an nth root of a suitably chosen uniformizer additionally depends on the relevant roots of unity and residue/unit hypotheses. Analytically z=w^n has a distinguished positive-loop monodromy w↦exp(2πi/n)w. This local monodromy scalar is not the global comparison normalization (2πi)^−p for cycle traces.',
  'stated as an example and exposition direction, with complete/tame qualifications', 'computations.md §9 gives the analytic continuation calculation and distinguishes the period normalizations', 'E',
  'The local example is classical Kummer/covering theory. Searches of the cited étale/different sources and the independent cote18 period formulas confirm that no identification with a trace-normalization factor is supplied. The arithmetic statement is not expanded beyond a qualified Kummer case.', 'Classical before manuscript; cross-package endpoints checked2026',
  'Analytic example established. Arithmetic hypotheses and period-comparison direction must remain explicit.', [], 'high')
C(262,[223],16,[28,30], '1156–1187;1207–1219', 'H^r(A,G)=0 for r>2',
  'The reused leaf proves a vanishing assertion by reduction to a residue field k, finite group-scheme duality, a smooth part G_s and Tate’s abelian-variety result. The hypotheses on A, G and the topology are missing; the displayed formula is not a universal cohomological-dimension theorem for every flat sheaf.',
  'proof sketched in a continuation from an unidentified theorem; author is not named on the leaf', 'No computation can recover the omitted antecedent hypotheses', 'F',
  'The bibliography explicitly names Shatz, Cohomology of artinian group schemes over local fields (published1964, DOI10.2307/1970403), and Tate’s1959 notes. Shatz1966, The cohomological dimension of certain Grothendieck topologies, is a plausible source but its exact Proposition14/15 text was not obtained. Searches of exact phrases, author bibliography, Annals and zbMATH links did not secure the match.',
  'Shatz1964 received29January1963 per author-history source; candidate1966 publication',
  'Exact claim not identifiable. In particular finite cohomological dimension for all fppf sheaves is not inferred from this representable-group vanishing.', ['Shatz1964','Shatz1966'], 'low')
C(263,[223],16,[30], '1221–1233', 'For each s>0, the complex C(s) is acyclic',
  'For a purely inseparable extension K/k, the row formed by H^s(K^(⊗r)/k,G_m) and alternating face maps is claimed acyclic for s>0. Under the usual flat/étale G_m interpretation and finite purely inseparable extension, reduction of each tensor algebra to K identifies all terms and all face maps; the row is exact in positive Čech degrees, while its degree-zero cohomology is H^s(K,G_m). Thus the word acyclic needs its degree/augmentation convention.',
  'stated without proof as Proposition15 on a reused leaf; the cohomology convention is absent', 'computations.md §9 computes the alternating identity differentials 0,id,0,id and explains the degree-zero qualification', 'F',
  'Exact-phrase searches found Pareigis–Rosenberg1964 Addendum, pp.33–44, and its explicit credit to a letter of Shatz, but not this exact proposition. Shatz1966 is a candidate, not a verified attribution. The related Amitsur theorem is not automatically identical to the displayed cohomology row.',
  'Related Addendum1964; exact source unlocated in2026 search',
  'Positive-degree exactness has a clear finite-extension reconstruction. Literal acyclicity including degree zero is generally too strong; source conventions need recovery.', ['PareigisRosenberg1964','Shatz1966'], 'medium')
C(264,[],16,[35], '1365–1392', 'Cohomologie des catégories de Banach ... par Max Karoubi',
  'This reused leaf is explicitly by Max Karoubi. It defines the split Grothendieck group of an additive category and proposes cohomological groups K^n for Banach categories related to Bott periodicity. The visible definition of Banach category is incomplete because the leaf ends after bilinearity of composition.',
  'stated as another author’s research introduction, not a motive conjecture of Grothendieck', 'No computation; attribution and exact bibliographic comparison', 'B',
  'Karoubi’s own bibliography lists Cohomologie des catégories de Banach, CRAS263 (1966), pp.275–278,341–344,357–360. The first note was opened; his1968 Annales ENS paper develops the theory in ChapterII, §§2.1–2.4. The programme was developed by its named author, not inferred from a later same-title source.',
  'CRAS1966; full development1968',
  'Established external-context K-theory material; keep segregated from the motive claims.', ['Karoubi1966','Karoubi1968'])

exec((B/'claims_later.py').read_text())
exec((B/'claim_amendments.py').read_text())

if __name__=='__main__':
    (B/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
    print(f'{len(claims)} manually authored claims saved: {claims[0]["id"]}–{claims[-1]["id"]}')
