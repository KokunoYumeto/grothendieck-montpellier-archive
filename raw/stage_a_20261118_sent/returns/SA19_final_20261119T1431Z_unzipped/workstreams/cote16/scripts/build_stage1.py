"""Serialize manually read and individually adjudicated cote-16 entries.

The source-entry JSON is used only to retain stable identifiers and headings.
No verdict or mathematical content is generated from keywords or headings.
All rows below were authored after reading the entries, the complete cote-16
transcription, the applicable doubts, and all six second-pass files.
"""
import csv, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parents[2]
entries=json.loads((BASE/'SA19_work/source_audit/MPL_16+47+54+44_entries.json').read_text())
PKG='MPL_16+47+54+44'
items=[]; verdicts=[]
def add(n, sources, kind, scans, lines, words, statement, reconstruction, check, reason, decisions):
    ident=f'SA19-{n}'
    items.append(dict(id=ident,sources=[f'{PKG}#{s}' for s in sources],kind=kind,cote=16,scans=scans,lines=lines,his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))
    for s,verdict,why in decisions:
        verdicts.append(dict(entry_id=f'{PKG}#{s}',item_id=ident,verdict=verdict,reason=why))

add(101,[1,2,25],'idea of the earlier run',[9,10,13,14],'265–349;440–527','sur ℤ !; satisfait à la condition de (6.1)',
    'For the ordinary exterior algebra of a free rank-2n integral symplectic module, ξ^n=n!·vol; hence L^n:Λ^0→Λ^{2n} is not an integral isomorphism for n≥2. Ordinary contraction acts on L^j p by j(n−i−j+1)L^{j−1}p, whereas the draft’s endpoint relations prescribe unit-step lowering. Rationalizing resolves the first obstruction but not the second normalization mismatch.',
    'The factorial and contraction tests are the earlier run’s exact counterchecks, not computations written by Grothendieck. Divided powers, other lattices, or normalized contraction are possible reconstructed models, not silent repairs of the source.',
    'agrees','The quoted integral assertion is present. The later endpoint relations determine a different lowering operator from ordinary contraction. The second pass changes the reference on scan 14 to 6.(5|15), so the old categorical quotation of (6.5) is no longer the current reading.',
    [(1,'kept','Retain the explicit integral counterexample to the literal exterior model.'),(2,'corrected','Keep the normalization objection, but replace the old unambiguous (6.5) reference by the current unresolved 6.(5|15); the blank formula on scan 10 does not define contraction.'),(25,'merged','S2 revisits the same integral and normalization issue; merged with R1 and corrected R2.')])
add(102,[3,28],'idea of the earlier run',[16,17],'598–692','Il faut donc se donner en même temps L et les πᵢ; Non',
    'In the n=1 normalized Lefschetz algebra Mat₂(ℤ)×ℤ, conjugation by 1+tL fixes L but changes Λ and the degree projectors: gΛg⁻¹=Λ+t(π₂−π₀)−t²L. Thus specifying the raising operator alone does not specify the algebra map; the prescribed grading matters. The algebra has rank five.',
    'The displayed conjugation family is supplied by the earlier run. The circled negative answer and five-element basis are on the page.',
    'agrees','The text retracts uniqueness from L alone and explicitly calls the projector condition essential. This is a resolved question within the pages, not an open modern conjecture.',
    [(3,'kept','The exact matrix example supplies the manuscript’s stated negative answer without attributing the example to the manuscript.'),(28,'merged','S5 is the same nonuniqueness and rank-five example.')])
add(103,[4],'idea of the earlier run',[19],'725–779','canoniquement autodual',
    'For a nonsingular symmetric integral matrix Q, the finite cokernel D_Q=ℤ^r/Qℤ^r has the perfect symmetric pairing xᵀQ⁻¹y mod ℤ. For Q=(−m), the value is −ab/m mod ℤ. Identifying a geometric Néron–Severi group with D_Q requires the local-surface hypotheses absent from the isolated sheet.',
    'The formula and elementary proof are the earlier run’s explanation of the printed claim, not a formula printed on scan 19.',
    'agrees','The page asserts autoduality from the intersection matrix; the entry appropriately separates the elementary lattice statement from geometric identification.',
    [(4,'kept','Preserve as an earlier-run proof supplement with the geometric hypotheses attached.')])
add(104,[5],'idea of the earlier run',[19],'725–779','indépendant de la désingularisation choisie',
    'A point blowup changes Q to Q′=[[Q−vvᵀ,v],[vᵀ,−1]], integrally congruent to Q⊕(−1). The discriminant group and its pairing are unchanged. Resolution independence additionally uses common domination of resolutions in the stated surface setting.',
    'The block congruence is the earlier run’s computation; geometric common domination is an explicit reconstructed prerequisite.',
    'agrees','The sheet asserts resolution independence, but its proof is not on the sheet. The entry provides only the blowup linear algebra.',
    [(5,'kept','Retain the precise scope of the blowup calculation; it alone is not the complete geometric proof.')])
add(105,[6,7],'reading question',[52,54],'1883–1925;1954–1995','idéaux maximaux ... homogènes; valeurs dans k',
    'The finite étale algebra 𝔽₂³ is not generated by one element over 𝔽₂: each element has at most two distinct coordinates. A nonzero polynomial over a finite field need not have a rational nonzero value. Consequently an unqualified monogenic/discriminant argument fails. No grading is supplied that makes “homogènes” a clear replacement for “principaux”.',
    'The finite-field example is the earlier run’s counterexample. The alternative “principaux” is a mathematical reading proposal only; the second pass confirmed the ink “homogènes”.',
    'agrees','The notes correctly find two logically separate gaps: the finite-field argument and the unidentified adjective. They cannot be repaired merely by substituting the suggested word.',
    [(6,'kept','Retain the finite-field obstruction with all hypotheses checked.'),(7,'corrected','Keep the unresolved mathematical meaning, but record that “homogènes” is already confirmed by the second pass; no new ink decision is made.')])
add(106,[8],'reading question',[21,23],'860–977','autodual; sous-espace orthogonal de NS(X)',
    'For a smooth proper geometrically connected surface over an algebraically closed field and ℓ invertible, the rational Tate module of the cohomological Brauer group is the orthogonal complement of NS(X)⊗ℚℓ in H²(X,ℚℓ(1)). This is not a perfect pairing on the whole torsion Brauer group. The lattice induced on the quotient is integral and unimodular when ℓ does not divide the Néron–Severi discriminant; the finite ℓ-primary quotient is measured by torsion in H³(X,ℤℓ(1)).',
    'The full surface and coefficient hypotheses are recovered from the published context, not all repeated on the two loose pages.',
    'agrees','The distinction between rational pairing, integral Tate lattice, and finite torsion quotient is required by the text’s exact sequences.',
    [(8,'kept','Keep the warning against conflating the rational and torsion statements.')])
add(107,[9],'other',[39],'1523–1543','Théorème 3.10',
    'The fragment concerns Matlis theory over a commutative noetherian ring: indecomposable injectives are injective hulls of residue fields at primes; localization identifies the appropriate local hull, and annihilator layers are dual to successive powers of the maximal ideal. Isomorphism classes and multiplicities are unique, not a canonical direct-sum splitting.',
    'Identification with Matlis is bibliographical comparison. The surviving sheet does not give a full title or independent proof.',
    'agrees','The terminology, theorem number, and stated annihilator filtration match the cited primary article.',
    [(9,'kept','Retain as an identification and scope clarification; it is contextual reused material, not a new Jacobian conjecture.')])
add(108,[10],'unproved claim',[37],'1446–1463','Ĩ est un Module injectif',
    'For x∈X and an injective O_{X,x}-module I, the skyscraper-like direct image i_{x*}I is injective as an O_X-module, because Hom_X(F,i_{x*}I)=Hom_{O_{X,x}}(F_x,I) and the stalk functor is exact. In the noetherian affine setting the associated injective sheaf has this form; support is the closure of {x}.',
    'The adjunction proof is the earlier run’s supplied proof. The global category and noetherian setting are retained.',
    'agrees','The page states injectivity among all O_X-modules. Restricting the assertion silently to quasi-coherent objects would weaken the actual text.',
    [(10,'kept','Retain the exact-stalk proof and the all-modules conclusion.')])
add(109,[11],'reading question',[19],'725–779','On trouve donc ... NS(U)',
    'The local surface identification NS(U)≅coker((C_i·C_j)) is to be read in the setting of a complete normal two-dimensional local ring, algebraically closed residue field, and a regular resolution that is an isomorphism away from the closed point. The isolated tail begins after these hypotheses.',
    'These prerequisites are imported explicitly from Brauer III §8.4; the loose leaf itself does not state them.',
    'agrees','The note correctly flags that the determinant statement is not a theorem about an arbitrary punctured local scheme.',
    [(11,'kept','Preserve the missing-context warning and label the recovered hypotheses.')])
add(110,[12],'self-flagged step',[19,23],'725–779;945–977','canoniquement autodual',
    'The lattice discriminant pairing attached to a resolution and the pairing arising from local étale duality are different constructions whose compatibility needs a geometric comparison theorem. Constructing either pairing, or showing equal group orders, does not establish their equality.',
    'The explicit warning “not verified” is found in published Brauer III, Remark 8.5, rather than on the isolated scan 19; the item’s self-flagged status therefore has a published-text locator.',
    'agrees','The entry does not confuse the elementary pairing with the unresolved comparison. A later paper on surface duality alone is not an exact settlement.',
    [(12,'kept','Keep the comparison question separate from the established finite discriminant pairing.')])
add(111,[13],'other',[19],'725–779','d’après Mumford [28]',
    'Mumford’s negative-definiteness theorem for exceptional curves supports nonsingularity of the intersection matrix in the appropriate resolution setting. His topological calculation supports an analogous discriminant group, but is not itself a proof of every ℓ-adic pairing comparison in Grothendieck’s local algebraic setting.',
    'The separation of topological and étale conclusions is an editorial scope check.',
    'agrees','The note accurately prevents a single citation from carrying a stronger compatibility conclusion than its stated result.',
    [(13,'kept','Keep as a bibliographic scope check, linked to SA19-109 and SA19-110.')])
add(112,[14],'reading question',[52],'1883–1925','premier idéal de Filting; A^p → A^q',
    'For a finitely presented module with q generators, Fitt₀(M)⊂Ann(M) and Ann(M)^q⊂Fitt₀(M). The Kähler different of B/A is Fitt₀^B(Ω_{B/A}); the presentation used to compute it must be over B. “Premier” in this passage corresponds to modern Fitt₀ notation.',
    'Modern indexing and the B-linear correction are editorial explanations. The typed spelling and coefficient A are preserved as source readings.',
    'agrees','Both the index and coefficient ring matter. The second pass confirms the literal A and “Filting”, so mathematical corrections must not be presented as new transcriptions.',
    [(14,'kept','Retain the Fitting-index and coefficient-ring warning with an explicit modern definition.')])
add(113,[15],'idea of the earlier run',[52],'1883–1925','Transitivité',
    'For composable finite flat complete-intersection algebras, block-triangular Jacobian presentations give multiplicativity of the different: D_{C/A}=D_{C/B}·D_{B/A}C. A determinant calculation proves this under its presentation hypotheses; the fragment does not state a universal formula for arbitrary maps.',
    'The two-equation determinant model is the earlier run’s test, not a proof of the unrestricted word “transitivité”.',
    'agrees','The note preserves rather than suppresses the complete-intersection hypotheses.',
    [(15,'kept','Retain the qualified determinant calculation; do not universalize the margin fragment.')])
add(114,[16],'reading question',[52],'1883–1925','différente de Dedekind',
    'Comparison of the Kähler different with the trace/Dedekind different requires finite generically separable algebras and, for the clean equality, a locally complete-intersection (in particular appropriate finite DVR) setting. In inseparable fraction-field extensions the trace pairing is degenerate.',
    'The separability and finiteness qualifications are a modern reconstruction of the applicable theorem, not ink inserted into the draft.',
    'agrees','The note correctly asks which hypotheses govern the comparison.',
    [(16,'kept','Keep the trace-versus-Kähler distinction and its exact hypotheses.')])
add(115,[17],'unproved claim',[54],'1954–1995','Algèbres étales sur A → Algèbres étales sur A/I',
    'For a nilpotent ideal I⊂A, reduction induces an equivalence between the categories of étale A-algebras and étale A/I-algebras, and between their finite étale subcategories. This includes morphisms and uniqueness up to unique lift, not only a bijection of isomorphism classes.',
    'The full categorical formulation is standard and makes explicit the arrow on the page.',
    'agrees','The fragment states an equivalence, and the entry retains its categorical strength.',
    [(17,'kept','Retain as a recognized published theorem, not an open deformation conjecture.')])
add(116,[18,19],'reading question',[41],'1586–1613','On laisse au lecteur',
    'Coherence/quasi-coherence of RHom(L,M) holds with L bounded above and coherent and M bounded below with the corresponding finiteness, or with the stated bounded-below L and uniform finite Ext-dimension alternative. It is false with arbitrary unbounded inputs: over a field, zero-differential complexes having one copy of k in every nonnegative degree give H⁰RHom=∏_{i≥0}k, not a finite-dimensional vector space.',
    'The infinite-product counterexample is the earlier run’s test. It refutes an extension without boundedness, not the qualified proposition printed on the page.',
    'agrees','Both boundedness alternatives are present and must be retained. The finite Ext-dimension alternative is not redundant.',
    [(18,'kept','Retain the exact boundedness and uniform Ext hypotheses.'),(19,'merged','The unbounded counterexample tests the missing hypothesis of the same item.')])
add(117,[20],'reading question',[43],'1706–1716','Vider|Virer (ii) sauf raison sérieuse',
    'The galley contains a proposed deletion of part (ii), not an unequivocal authorial cancellation. The current ink reading has an unresolved imperative but a resolved “raison sérieuse”. Its relation to EGA IV₄, 18.11.6–18.11.7 must be established by comparing both actual texts, not by matching a remembered statement.',
    'Whether the request caused the published omission is a historical inference unless an editorial record supplies the causal link.',
    'agrees','The second pass resolves one noun but leaves Vider/Virer undecided. The old note’s diplomatic quotation therefore needs updating.',
    [(20,'corrected','Update to the current Vider|Virer ... raison sérieuse reading; distinguish a request to delete from a proven publication-history claim.')])
add(118,[21],'reading question',[26],'1063–1112','Corrections à S.G.A.D. XV, XVI, XVII',
    'The correction sheet targets seminar exposés XV–XVII of SGA 3 and includes a generic-fibre Cartan subgroup spreading statement. Old page/line numbers cannot be identified with the 1970 volume without checking editions and the surrounding hypotheses; not every listed correction is a standalone theorem.',
    'Identification of the later publication and exact correction targets is bibliographical work; missing scheme and group hypotheses are not supplied by fiat.',
    'agrees','The note correctly treats pagination and hypothesis recovery as unresolved, rather than declaring every correction incorporated.',
    [(21,'kept','Retain the edition-control question and the limitation of the loose-page fragment.')])
add(119,[22],'reading question',[54,56],'1954–1995;2004–2050','B finie ... fibres ... étales',
    'A finite algebra with étale fibres need not be étale unless flatness is supplied. For A=k[t] and B=A×A/(t), every residue-field fibre is a product of copies of that field, but B has t-torsion and is not flat. The nearby correct criterion is finite flat plus étale fibres.',
    'The counterexample is the earlier run’s. It refutes the literal isolated criterion only; omitted ambient hypotheses could change its intended meaning.',
    'agrees','The page gives no visible flatness hypothesis in the local sentence, while the neighbouring definitions explicitly distinguish flatness.',
    [(22,'kept','Keep the counterexample and the possible missing-context qualification.')])
add(120,[23],'other',[19,21,23,26,37,39,41,43,52,54,56],'725–977;1063–1112;1446–1613;1706–1716;1883–2050','[Bibliography is in the research notes, not a manuscript sentence.]',
    'The bibliography attached to R9–R22 supplies external leads for injectives, Brauer groups, étale algebras, differents, and EGA/SGA fragments. Its references are to be verified separately and cannot count as manuscript claims.',
    'Entirely an earlier-run bibliography.',
    'not on the page','This is deliberately a notes-only bibliography entry. Each result used in the consolidation is checked against its source.',
    [(23,'kept','Retain as bibliography, not as an attributed mathematical assertion.')])
add(121,[24],'reading question',[33,44,45,46,48,49,50],'1246–1316;1717–1882','C(X); D(X); A(X)',
    'The draft’s C(X), where defined by algebraicity of inverse Lefschetz operators, matches published standard conjecture B(X), not the published Künneth conjecture C(X). Published D denotes numerical equals homological equivalence, but a local undefined draft letter D cannot be mapped solely by its shape. The ℓ|χ side condition remains context-dependent.',
    'This is an operational dictionary based on the actual property in each sentence; undefined letters retain uncertainty.',
    'agrees','The note’s normalization warning is essential. Second-pass interpretations that identify surface projectors directly with this stronger C are not adopted as theorem statements.',
    [(24,'kept','Retain the operational dictionary and the undefined-letter caveat.')])
add(122,[26],'idea of the earlier run',[14,15,16],'482–649','base sur ℤ; unités matricielles',
    'For the reconstructed universal normalized-string representation with one string of length n−i+1 for each i=0,…,n, the integral algebra generated by unit raising and lowering is ∏_{i=0}^n Mat_{n−i+1}(ℤ), of rank (n+1)(n+2)(2n+3)/6. Bottom-string projectors are obtained by differences of eΛ^rL^re, e=1−LΛ; matrix units are L^b e_i Λ^a.',
    'This is the earlier run’s replacement model. It is not the literal ordinary-contraction exterior model on scan 14; it becomes an explanation of the intended algebra only after that distinction is made.',
    'agrees','The construction supplies integral matrix units for normalized strings, while the source’s literal model has the factorial and normalization defects of SA19-101.',
    [(26,'kept','Retain as a labelled earlier-run reconstruction and recompute its matrices.')])
add(123,[27],'reading question',[15],'528–597','0≤α,β≤2n−i',
    'A primitive string beginning in degree i has exponents 0,…,n−i, so its matrix units are indexed by 0≤α,β≤n−i. The written larger bound 2n−i yields nonexistent or zero operators and cannot index a basis of that block.',
    'The corrected exponent bound is mathematical inference only. The second pass confirms the literal larger bound, which remains the source reading.',
    'agrees','The entry’s mathematical diagnosis survives, but uncertainty about what the transcription currently says does not: it says 2n−i.',
    [(27,'corrected','Record the confirmed source bound and mark n−i as a mathematical correction, not a newly decided reading.')])
add(124,[29],'unproved claim',[3,4,5,6,7,8,16,51,53,55],'27–264;598–649;1861–1882;1926–1953;1996–2003','πᵢ appartiennent à E',
    'For a finite graded ring or faithful graded module with homogeneous inverse pairs for each complementary Lefschetz degree, the degree projectors can be recovered by induction. Statements require finite support, prescribed degree bounds, homogeneous maps and both inverse identities. A proof that uses a global identity operator must include source and target cutoffs.',
    'The modern formulation collects hypotheses distributed over several pages. The present audit identifies the missing target cutoff in scan 53 separately from the theorem’s validity.',
    'agrees','The earlier note rightly demands the full setup; its acceptance of every displayed induction formula is refined by the new cutoff check.',
    [(29,'corrected','Keep the intrinsic-projector theorem with full hypotheses; flag the displayed scan-53 proof step and scan-11 support convention.')])
add(125,[30],'unproved claim',[9,10,13,16,48,51],'265–349;440–481;598–649;1797–1818;1861–1882','isomorphismes; Λ∈E',
    'Hard Lefschetz is a cohomological isomorphism theorem. Algebraicity of its inverse, or of normalized lowering, is the additional standard conjecture B. Deligne’s hard-Lefschetz theorem does not settle that algebraicity question in general.',
    'Modern terminology and subsequent theorem attribution are external commentary, not part of the 1960s text.',
    'agrees','The note correctly separates linear invertibility from realization by algebraic cycles.',
    [(30,'kept','Retain this separation throughout the claim map.')])
add(126,[31],'reading question',[10,13,14,33,40],'306–349;440–527;1246–1316;1544–1585','LΛ=1−Σπᵢ,₀; ΛL=1−Σπⱼ,₀',
    'On a normalized Lefschetz string L kills the top and Λ kills the bottom; LΛ is identity away from the bottom and ΛL away from the top. Cancelled versions of these formulas cannot be counted as final assertions; the live endpoint equations on scan 14 govern the later formulas.',
    'Endpoint matrix tests are an editorial verification. The manuscript’s cancelled alternatives remain in the diplomatic evidence.',
    'agrees','The note appropriately uses the final endpoints and distinguishes the cancellations on scans 10 and 33.',
    [(31,'kept','Retain exact endpoint and cancellation tracking.')])
add(127,[32],'unproved claim',[33,34,36,38,40,42,45,46],'1246–1705;1728–1784','C(X) ⇔ C(Y) et A(X×Y)',
    'For a smooth hyperplane Y⊂X and a Weil cohomology satisfying hard and weak Lefschetz, algebraicity of lowering on X is equivalent to the corresponding property on Y together with the appropriate algebraic-cycle Lefschetz condition on X×Y (or X×X). Iterating along a smooth flag gives a universal implication from the collection of A-properties to B. This is not the pointwise implication A(X)⇒B(X).',
    'Letters are translated operationally; twists and degree bounds are supplied explicitly in the claim records. The equivalence is a theorem about the conjunction, not a proof that the conjectures hold.',
    'agrees','The note correctly emphasizes quantifiers, hyperplane hypotheses, and the necessary product variety.',
    [(32,'kept','Retain the quantified reduction and do not state a pointwise A-to-B implication.')])
add(128,[33],'reading question',[50],'1833–1860','A′; A″; A′°; A″°',
    'The weakened hyperplane conditions use a mixture of codimension inequalities and cohomology-degree labels. A precise claim requires fixing whether i indexes cycles or H^i and then checking all Gysin shifts. The displayed factorization has degree +4 in even dimension and +2 in odd dimension; the unresolved local inequalities cannot be silently replaced.',
    'Any clean modern weak-condition statement is a reconstruction, separate from the unidentifiable exact literal version.',
    'agrees','The note’s degree audit is necessary and the current second-pass alternatives do not settle every index.',
    [(33,'kept','Retain as a scan-dependent formulation problem, not a proven literal equivalence.')])
add(129,[34],'unproved claim',[48,49],'1797–1832','polynôme caractéristique à coefficients rationnels',
    'If v=L^{n−i}:H^i→H^{2n−i} is invertible and some algebraic u:H^{2n−i}→H^i is invertible, and uv has a rational characteristic polynomial with nonzero constant term, Cayley–Hamilton gives v⁻¹=(uv)⁻¹u as a rational polynomial correspondence. Algebraic isomorphisms do not supply their inverse without the polynomial-coefficient hypothesis or another argument.',
    'The unambiguous order (uv)⁻¹u is a modern typed reconstruction of the proof, whose local operator letters are uncertain.',
    'agrees','The note correctly isolates the finite-dimensional algebra argument and its rationality hypothesis.',
    [(34,'kept','Retain the exact inverse construction and the distinction between algebraic existence and algebraic inverse.')])
add(130,[35],'withdrawn in the same text',[44,48,49],'1717–1727;1797–1832','je m’étais laissé entraîner',
    'The author retracts a claim of independence of positive-characteristic standard conjectures from the chosen Weil cohomology. Independence from polarization is a separate, established formal theorem and does not establish independence from cohomology theory.',
    'The modern separation of the two parameters is editorial; the retraction and request for a proof are explicit.',
    'agrees','The retraction must survive consolidation. Neither finite-field Künneth projectors nor polarization independence settles the broad retracted statement.',
    [(35,'kept','Retain as an authorial withdrawal with both the assertion context and retraction locator.')])
add(131,[36],'unproved claim',[49],'1819–1832','algèbre semi-simple',
    'Let A be a finite-dimensional rational algebra with a positive involutive trace form Tr(a*a)>0 for nonzero a. Its Jacobson radical is zero: the involution preserves the radical, a*a is radical and nilpotent, hence has trace zero. Applying this to correspondences requires the relevant algebraicity and index hypotheses and a justified finite-dimensional rational algebra.',
    'The radical proof is the earlier run’s explanation of the conditional assertion. Mere inclusion of a Q-algebra in a finite-dimensional Qℓ-space does not prove finite Q-dimension.',
    'agrees','The note supplies the missing rational-finiteness qualification rather than treating positivity as an unconditional geometric theorem.',
    [(36,'kept','Retain the precise algebraic theorem and the geometric hypotheses needed for its use.')])
add(132,[37],'unproved claim',[49],'1819–1832','rétraction à gauche ... à droite',
    'In a semisimple category of the relevant algebraic correspondences, monomorphisms and epimorphisms split. A positivity argument on End(H*(X)) alone does not justify an algebraic splitting for a map X→X′; the ambient category or the endomorphism algebra of X⊕X′ must satisfy the corresponding hypotheses.',
    'The ambient direct-sum requirement is an editorial completion of the conditional argument, not a hypothesis printed in full on the loose page.',
    'agrees','The note correctly resists promoting arbitrary linear splittings to algebraic correspondences.',
    [(37,'kept','Keep the conditional splitting statement and specify the ambient semisimple category.')])
add(133,[38,39],'other',[49],'1819–1832','semi-simple',
    'Jannsen proves semisimplicity for pure numerical motives with characteristic-zero coefficients. This does not unconditionally prove semisimplicity for homological motives. Under algebraic Künneth projectors a homological-to-numerical kernel can be a nilpotent radical, which is weaker than vanishing of that radical.',
    'Both comparisons concern later literature; neither theorem is written on this manuscript page.',
    'agrees','The two notes address the same dangerous overidentification and are consolidated with the distinction explicit.',
    [(38,'kept','Retain numerical motives as the precise later unconditional result.'),(39,'merged','Merge the nilpotent-versus-zero radical refinement into the same later-literature item.')])
add(134,[40],'other',[44,48,49],'1717–1727;1797–1832','coefficients rationnels',
    'Over finite fields, Katz–Messing provides algebraic rational Künneth projectors and characteristic-polynomial comparisons for algebraic correspondences in the specified cohomology theories. These results address that finite-field setting and do not prove the full Lefschetz standard conjecture over every field.',
    'Entirely a later-literature comparison. Its exact theorem scope is checked in the primary paper.',
    'agrees','The note’s scope is appropriately narrower than the retracted universal independence assertion.',
    [(40,'kept','Keep the finite-field theorem and exclude a universal standard-conjecture conclusion.')])
add(135,[41],'title, date or page count',[46,47,48],'1759–1818','dim X≤2; 6.1.1966',
    'The letters’ low-dimensional known/unknown statements are historical claims in their dated context. The written January 1967 dates and the separately written 6.1.1966 must both be retained; interpreting the latter as 1967 is a chronological inference, not a corrected ink reading.',
    'Modern status and a proposed chronological slip are explicitly external to the transcription.',
    'agrees','The second pass confirms 6.1.1966 even while its checked-notes commentary proposes 1967. The confirmed reading takes precedence.',
    [(41,'corrected','Preserve the actual 1966 reading and identify the 1967 explanation only as inference; date all historical status claims.')])
add(136,[42],'other',[47],'1785–1796','Hodge ... article de 1938; πᵢ',
    'The manuscript points to Hodge’s 1938 paper on algebraic correspondences between surfaces, received through Tate, and to algebraicity of the degree projectors. The current second-pass reading is πᵢ, not specifically π₁. Claims about how widely the paper was neglected require evidence beyond this letter.',
    'Bibliographic identification is externally checked. A claim about mathematical reception is not established by authorial surprise alone.',
    'agrees','The entry’s initial index reading must be corrected, and its reception discussion remains explicitly unverified.',
    [(42,'corrected','Use the current πᵢ reading; retain the primary bibliographic identification without an unsupported neglect narrative.')])
add(137,[43],'other',[3,9,14,15,33,44,45,46,47,48,49,50,51,53,55],'27–2003, selected passages','[Bibliography is in the research notes, not a manuscript sentence.]',
    'The bibliography attached to S1–S19 supplies leads on standard conjectures, hard Lefschetz, numerical motives, Künneth projectors and Hodge. It is not another mathematical assertion of Grothendieck.',
    'Earlier-run bibliographic apparatus only.',
    'not on the page','Each work used in the present audit is independently opened; prior-run bibliographic confidence is not inherited.',
    [(43,'kept','Retain the bibliography as bibliography and link its verified results separately.')])
add(138,[80],'idea of the earlier run',[25],'978–1062','Pour avoir une algèbre associative',
    'For the displayed graded-commutative algebra H⁰=k,H¹=V,H²=kξ⊕W,H³=V∨,H⁴=kξ², associativity imposes the boxed quadratic identity on φ, ψ and Q. Nondegeneracy of alternating φ and symmetric Q controls Lefschetz and duality, but does not imply that associativity identity. The two-dimensional symplectic example with W=0 violates associativity.',
    'The counterexample is an earlier-run check of an unjustified inference, not a refutation of Grothendieck’s conditional associativity criterion.',
    'agrees','The page explicitly separates the associativity equation from the later nondegeneracy requirements.',
    [(80,'kept','Keep the independence test and do not attribute the refuted inference to Grothendieck.')])
add(139,[81],'idea of the earlier run',[27],'1113–1155','χ=0',
    'Over a field of characteristic different from two, take the orthogonal space kξ⊕kw with Q(ξ,ξ)=1,Q(w,w)=−1, and send x∧y to φ(x,y)(ξ+w), where φ is symplectic. Its image is an isotropic line not contained in W, so the induced four-form χ is zero while the Lefschetz alternating form is nondegenerate.',
    'The rational explicit model is the earlier run’s construction. The manuscript gives the isotropic-line mechanism, with its own field assumptions.',
    'agrees','The example checks the page’s assertion without conflating nondegeneracy of φ with nonisotropy of individual vectors.',
    [(81,'kept','Retain the exact isotropic-line realization and field restrictions.')])
add(140,[82,83,84],'idea of the earlier run',[29],'1188–1206','infinité ... dimensions arbitrairement grandes',
    'The earlier run fixes a normalized operator U=(Λ²φ♯)Q♭, absent as a fully specified convention in the source. Its six-dimensional rational model and varying-dimensional family can then test infinite forward orbits and unbounded cyclic dimensions. These calculations establish only that explicit normalization and the stated families; they do not decide the manuscript’s unresolved W/V parenthesis or its proposed dimension-four threshold.',
    'The normalization, matrices and parameter family are earlier-run reconstructions. The manuscript asks the orbit and cyclic-dimension questions tentatively. Recomputing existing examples is within this audit; extending them is deferred.',
    'agrees','The three entries are one conditional construction chain and should not appear as three independent settlements of the exact ambiguous manuscript question.',
    [(82,'kept','Retain the normalized-operator caveat as the governing formulation.'),(83,'merged','Merge the six-dimensional certificate with the operator convention it uses.'),(84,'merged','Merge the varying-dimensional family with the same conditional formulation; do not claim the dimension-four case.')])

assert len(items)==40
expected=set(range(1,44))|set(range(80,85))
assert {int(r['entry_id'].split('#')[-1]) for r in verdicts}==expected
assert len(verdicts)==48
(ROOT/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
with (ROOT/'entries.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(sorted(verdicts,key=lambda x:int(x['entry_id'].split('#')[-1])))
print(f'Serialized {len(items)} manually adjudicated items covering {len(verdicts)} assigned entries exactly once.')
print('Verdicts:',{v:sum(r['verdict']==v for r in verdicts) for v in sorted({r['verdict'] for r in verdicts})})
