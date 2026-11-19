"""Explicit per-entry decisions and problem formulations, manually composed."""
import csv,json
from pathlib import Path
B=Path('SA05/work/cote12c'); P='sources/texts/pro/MPL_12_099-149_transcription.tex'
entries=[]
def e(n,item,v,r): entries.append(dict(entry_id=f'MPL_12_099-149#{n}',item_id=f'SA05-{item}',verdict=v,reason=r))
e(1,3001,'kept','Provenance register only: internal run status is not a checked theorem; project leads remain separate.')
e(2,3002,'kept','The three textual units and supplied-face scope agree with the retained source; continuation beyond149 is unavailable.')
e(3,3003,'kept','Virtual Betti is named on99; the additive formula is an explicitly labelled reconstruction.')
e(4,3004,'kept','The non-generic base-change difficulty is explicit on142 and is not repaired by postulating a field map.')
e(5,3005,'kept','Proper top-weight quotient, not full normalization injectivity; checked against99/106.')
e(6,3006,'kept','The two-lines localization calculation refutes the written injectivity hope; source question remains a question.')
e(7,3007,'kept','Purity and geometric versus arithmetic semisimplicity are separated; the arbitrary arithmetic counterexample does not refute motivic semisimplicity.')
e(8,3007,'merged into item','Same semisimplicity restriction, now in the coefficient-devissage argument on114.')
e(9,3008,'kept','The Ext weight order and geometric restriction are checked in Weil II3.4.3–4.')
e(10,3009,'corrected','Realization bounds kept; add the source105 top-two-piece strict-level alarm, whose literal reading fails for an elliptic curve.')
e(11,3010,'kept','E2 degeneration concerns the weight-indexed SNC sequence, not every later Leray sequence.')
e(12,3011,'kept','Strong resolution is admitted. Alterations are a later substitute for some arguments, not proof of that exact hypothesis.')
e(13,3012,'kept','Nonseparated scope question retained; Hodge III8.3.7 does not certify the exact geometric-level conjecture.')
e(14,3013,'kept','Derived splitting under hard Lefschetz checked in Deligne1968; arbitrary subquotient reduction remains separate.')
e(15,3014,'kept','A point with elliptic H¹ coefficient detects missing j; the displayed formula is retained as a scan alarm.')
e(16,3015,'kept','Compact-support attachment is essential; ordinary lower weights do not answer this margin.')
e(17,3016,'kept','Local Tate degeneration satisfies the smooth-projective coefficient hypothesis and gives weight4 against3.')
e(18,3015,'merged into item','The global Legendre boundary invariants answer the same compact-support lower-bound question as entry16.')
e(19,3016,'merged into item','Global Legendre version answers both sharp upper-bound questions; separate local/global certificates are retained in C3016/C3030.')
e(20,3017,'kept','Dual-weight set and Tate-sign calculations give scan alarms, not editorial corrections.')
e(21,3018,'kept','Joint geometric filtration is stronger than separate numerical constraints; canonical weights do not settle geometric level.')
e(22,3019,'kept','Deleted broader hypothesis and replacement by strictly special coefficients are represented with the conditional recovery.')
e(23,3011,'merged into item','Radicial invariance and resolution are separate inputs to the same reduction programme.')
e(24,3007,'merged into item','Cor5.2 uses filtration devissage, not a collapse of every extension into a strictly special object.')
e(25,3020,'corrected','Codex reads sous conj. type Tate where Pro reads sans; an unconditional author assertion cannot be fixed without the scan.')
e(26,3021,'kept','The elliptic endpoint refutes literal2(n−i+j); proposed2n−i+j remains an unadopted reading.')
e(27,3022,'kept','Positive-dimensional constant-coefficient local pattern retained with source dimension, SNC resolution and geometric-level qualifications.')
e(28,3022,'merged into item','Independent Hodge-box derivation and finite enumeration verify the realization-level gain of the same local bound.')
e(29,3022,'merged into item','The n=0/nonboundary exception belongs to the same bound and is explicitly retained.')
e(30,3023,'corrected','Double blowup refutes identification with the entire E2 term, but Codex intervient avec gives a weaker viable reading.')
e(31,3024,'kept','Open immersion refutes naive fibre-dimension replacement; this is not a refutation of the locally defined d_y invariant.')
e(32,3025,'corrected','Keep Hodge level/coniveau/source-dimension type distinct, and add that early12/035–036 uses a different Tate-stable convention.')
e(33,3026,'kept','SNC top Tate class refutes the minus-one bound for the late untwisted type definition only.')
e(34,3026,'merged into item','The Tate-twist issue is the same late-definition obstruction, not a blanket failure of every dimension-type convention.')
e(35,3027,'kept','Three Leray layers and middle-row E3 stability checked; whole-sequence degeneration is not inferred.')
e(36,3027,'merged into item','The last reduction is explicitly to verify/develop; Hua is a prior interpretive account, not a diplomatic witness.')
e(37,3028,'kept','Geometric stalks alone forget arithmetic descent; no unprovided relative presentation is supplied.')
e(38,3029,'kept','Durfee/Saito is a later comparison; exact link theorem and local geometric-level target have different hypotheses.')
e(39,3030,'kept','Linear Tate and nonlinear anabelian Hom are comparisons from the prior run, not source equivalences.')
e(40,3030,'merged into item','Jacobian multiplication-by2 preserves neither principal polarization nor curve map data; explicit multiplier4 check retained.')
e(41,3031,'corrected','Deligne–Milne2.23 is stated for connected affine groups; retain that hypothesis and do not infer centre-freeness.')
e(42,3032,'kept','Polarization/compact-real-form and Stix real-section theorem are distinct statements with checked hypotheses.')
e(43,3033,'kept','Tate weight/cyclotomic conventions are explicit; no nonlinear point-detection conclusion follows.')
e(44,3033,'merged into item','The all-prime/prime-to-p distinction is part of the same external comparison, not a proof of project B9.')
e(45,3033,'merged into item','Internal newer-status labels remain unverified project provenance; they do not settle the prior scope.')
e(46,3034,'kept','One-prime/two-prime conjecture retained with invertibility loci; NOS settles a restricted case.')
e(47,3035,'kept','Almost-all-prime integral comparison requires a reference system; the excerpt does not fully define it.')
e(48,3035,'merged into item','Non-finitely-generated Hom tests only the weakened arbitrary-lattice axiom, not a normalized integral category.')
e(49,3036,'kept','Normal-base generic full faithfulness and componentwise abelianness checked conditionally on the rational category.')
e(50,3037,'kept','Ramified finite unipotent extension refutes extension-closed interpretation; weaker subquotient closure survives.')
e(51,3038,'kept','Internal Serre quotient proof needs one common denominator/reference lattice and does not require ambient thickness.')
e(52,3039,'kept','Internal Hom does not imply rigidity; torsion duality obstruction is a modern inference, not an author claim.')
e(53,3040,'kept','Both sources say proper smooth; do not narrow to projective because of Hua’s paraphrase.')
e(54,3041,'kept','Dualized finite-component sequence has finite term in kernel; margin order is a reading/convention issue.')
e(55,3042,'kept','Full faithfulness uses generic morphisms and extension of existing objects; it does not prove essential image.')
e(56,3043,'kept','Deleted certainty is followed by an explicit sufficiency question and mixed-characteristic doubt.')
e(57,3043,'merged into item','Vasiu–Zink positive low-ramification criterion and negative high-ramification example qualify the same essential-image question.')
e(58,3043,'merged into item','All-prime unramifiedness of the punctured-base example is checked separately at l=p and l≠p.')
e(59,3043,'merged into item','Raynaud–Gabber historical antecedents prevent attributing first counterexample to2010.')
e(60,3043,'merged into item','Prime-index/order reduction is retained separately as C3050/P3018, within the essential-image item.')
e(61,3004,'merged into item','Same non-generic pullback obstruction as entry4; relative modern theories are comparisons under different hypotheses.')
e(62,3044,'kept','Criterion name and prime index/order remain scan questions; no attribution is guessed.')
e(63,3043,'merged into item','The one-prime/extension bridge is restricted to NOS over traits, not arbitrary higher-dimensional bases.')
e(64,3045,'kept','Universal property is an equivalence of additive functor categories, including natural transformations.')
e(65,3045,'merged into item','Finite biproducts are part of the same additive completion hypotheses; deletion does not remove their mathematical role.')
e(66,3046,'kept','Hom-finiteness follows from the End of a biproduct; the missing-additivity obstruction is retained.')
e(67,3047,'kept','Intertwiner quotient agrees with the corner definition; explicit algebra checked.')
e(68,3047,'merged into item','Idempotent splitting belongs to the same completion construction and needs no semisimplicity.')
e(69,3048,'kept','Generalized inverse proof reconstructed in semisimple matrix corners without assuming abelianness in advance.')
e(70,3049,'kept','Reverse-block projection is ill-typed as pr2; proposedpr1 is a scan alarm.')
e(71,3049,'merged into item','Both attached texts say every morphism; the prior monomorphism-only paraphrase is corrected.')
e(72,3050,'kept','Semisimple finite-dimensional End criterion yields finite-length abelian category; JannsenLemma2 checked.')
e(73,3045,'merged into item','Variance/deletion question qualifies the same universal property and remains unresolved on ink.')
e(74,3045,'merged into item','Equivalence rather than literal bijection is the same categorical universal-property correction.')
e(75,3051,'kept','Biadditive and monoidal extension follows by tensoring projectors; no duals/fibre functor is added.')
e(76,3052,'kept','Characteristic-zero averaging projectors checked; no identical integral Schur claim.')
e(77,3053,'kept','Cote16 endpoints are unavailable in this part; retain exact external retrieval lead only.')
e(78,3054,'kept','Jannsen proves numerical semisimplicity and abstract criterion, not all standard conjectures for homological motives.')
e(79,3055,'kept','P¹ matrices distinguish degree-changing Lefschetz sl2 from tensor automorphisms and central weights.')
e(80,3056,'corrected','A–D dictionary is checked through root-owned witnesses where available; unavailable14/117 is not a verified endpoint.')
e(81,3057,'kept','No attached cote14/16 singular-hypersurface endpoint; thematic resemblance remains a retrieval lead.')
e(82,3058,'kept','Nori exact sequence is a later descent theorem under neutral compatible fibres, absent from these manuscript leaves.')
e(83,3058,'merged into item','Artin quotient, component quotient, connectedness and splitting remain distinct assertions.')
e(84,3059,'kept','Period conjecture absent here; modern torsor statement checked independently and not attributed to this source.')
e(85,3059,'merged into item','18/059 is unavailable exact retrieval lead, not a source quotation or a newly checked conjecture.')
e(86,3060,'kept','Arapura6.4.1 checked over a subfield ofC with rational coefficients and smooth bases; motivated need not mean algebraic.')
e(87,3061,'kept','Nori–Ayoub Hopf comparison checked for PID coefficients and k embedded inC; it does not settle cycle conjectures.')
e(88,3055,'merged into item','The lack of rigidity/fibre functor is the same limit on reading a Tannakian group into a tensor completion.')
e(89,3062,'kept','Oda abelian p-kernel/Dieudonné/H¹dR isomorphism checked with perfect-field characteristic-p hypotheses.')
e(90,3062,'corrected','OdaCor5.12 for general proper smoothX assumes X(k) nonempty and gives an injection, not a universal isomorphism.')
e(91,3017,'merged into item','All weight, twist and table-index alarms are consolidated in readings.tsv without changing transcription.')
e(92,3027,'merged into item','Final words and curve reduction variants qualify the same unverified-step item.')
e(93,3063,'kept','S/K and realization-symbol ambiguities retained as type-sensitive scan questions.')
e(94,3064,'kept','Self-flag index resolves to substantive claims/problems, not duplicated unproved theorems.')
e(95,3064,'merged into item','Dependency inventory supplements the same coverage register; admitted inputs are not proofs.')
e(96,3002,'merged into item','Documentary headings corroborate the three units; no new mathematical item.')
e(97,3002,'merged into item','Internal numbering and extent are distinguished from the36 retained scan faces.')
e(98,3065,'kept','Printed Local Cohomology cover and proof mark20.3.68 are distinct from surrounding manuscript dating.')
e(99,3065,'merged into item','Unretained faces121/123 mentioned in the previous return are not reconstructed or counted as read.')
e(100,3002,'merged into item','Smooth-motive cover identifies the unit, not its exact historical date.')
e(101,3002,'merged into item','Envelope cover and first continuation are recorded without borrowing Hua’s later geometric example.')
e(102,3002,'merged into item','Retained-face count verified from actual markers; missing faces do not imply a continuous51-page text.')
e(103,3029,'merged into item','Durfee historical comparison retained with actual opened Durfee–Saito theorem and access limits for the1983 paper.')
assert [x['entry_id'] for x in entries]==[f'MPL_12_099-149#{n}' for n in range(1,104)]
with (B/'entries.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(entries)
problems=[]
def p(n,title,claims,as_he,plausible,state,why,worth,refs):
 cs=json.loads((B/'claims.json').read_text()); sel=[x for x in cs if int(x['id'].split('C')[-1]) in claims]
 problems.append(dict(id=f'MP-SA05-{n}',title=title,occurrences=[loc for x in sel for loc in x['lines']],as_he_states=as_he,plausible_today=plausible,state_of_art=state,why_open=why,worth=worth,refs=refs,claims=[x['id'] for x in sel]))
p(3001,'Normalization pullback and lower weights',[3002,3003],
 'The normalization/desingularization diagram asks whether the relevant map is injective.',
 'For properX, only the weight-i quotient ofH^i is detected injectively by a resolution; compact-support full injectivity is false.',
 'Deligne HodgeIII8.2.5 identifies the proper lower-weight kernel; the independently checked two-lines example hasH_c¹=Q_l and normalizationH_c¹=0.',
 'The source itself only records a question. The obstruction is lower-weight gluing cohomology; no historical reason for abandonment is asserted.',
 'Useful as a short explanatory example, not as an unsolved research problem.',['Deligne1974HodgeIII'])
p(3002,'Nonseparated level bounds',[3013],
 'Can the nonseparated smooth case retain niveau≤2n−i?',
 'Separate the Hodge-type question overC from the stronger geometric-generation filtration, and retain the nonseparated finite-type assumptions.',
 'HodgeIII8.3.7 constructs the nonseparated mixed Hodge structure by étale hypercovers and distinguishes the additional weight assertion; no exact general geometric-level theorem was found in the logged searches.',
 'No source explains why the question was dropped; the source lacks the separated compact-support route.',
 'Worth one focused run to test doubled-boundary examples and precise filtration conventions.',['Deligne1974HodgeIII','Bondarko2018Dimension'])
p(3003,'Devissage from subquotients to direct summands',[3015,3023,3024],
 'The insertion possible ici? questions devissage; Theorem5.1 deletes broader coefficients and Cor5.2 assumes Tate semisimplicity.',
 'A valid theorem should preserve strictly special/direct-summand coefficients unless a Serre-stable geometric presentation argument supplies the broader class.',
 'Deligne1968Theorem1.5/§2.4 splits smooth-projective direct images. WeilII gives numerical mixed direct-image theorems but does not identify arbitrary geometric subquotients with direct summands arithmetically.',
 'The manuscript explicitly identifies semisimplicity as the missing step. No additional historical explanation is claimed.',
 'High-value short proof audit after fixing the geometric class; unlikely to settle motivic semisimplicity in a few hours.',['Deligne1968Lefschetz','Deligne1980WeilII'])
p(3004,'Sharpened coefficient weight bounds',[3016,3030],
 'Can2n+2j or2i+2j be replaced by2n+j or2i+j, and can local weights be≤2min(i,n)+j?',
 'Retain the coarser total-space estimates or impose finite/local-trivial monodromy hypotheses strong enough to remove the Tate degeneration.',
 'WeilII1.8.4/3.5.5 and the Legendre example yield local and global weight4 fori=n=j=1, refuting all the specified sharp upper bounds.',
 'The manuscript leaves question marks; the obstruction is nonzero unipotent boundary monodromy, not merely a missed proof.',
 'Worth a short counterexample exposition and corrected-hypothesis table, not further pursuit of the false unrestricted claim.',['Deligne1980WeilII','Ito2020WeightMonodromy'])
p(3005,'Compact-support lower weight with coefficients',[3017],
 'Are the compact-support weights at leastj?',
 'Use the lower bound independent ofj supplied by total-space geometry, with special improvements only under additional boundary conditions.',
 'The Legendre boundary invariant lines injectQ_l² intoH_c¹(U,F), whileF has weight1; WeilII3.5.5 certifies the lack of global invariants.',
 'The prior affirmative Hua argument used ordinary cohomology and therefore did not address the source’s support convention.',
 'Worth keeping as the companion to the upper-bound counterexample.',['Deligne1980WeilII'])
p(3006,'Weight intersections and joint geometric level',[3021,3022],
 'It is not tautological that two weight presentations give their intersection; joint weight/level is stronger than the conjunction.',
 'A common filtration with geometric constituents is the precise target; numerical eigenvalue or Hodge-type bounds alone are weaker.',
 'WeilII3.4.1 gives unique numerical weights. Grothendieck1969 distinguishes effective Hodge structures from geometric support. No exact all-purpose identification of the source geometric joint class was found.',
 'The pages identify the existential-filtration difficulty; no source states why the programme was later abandoned.',
 'High mathematical interest but only definition comparison and low-dimensional cases fit one research run.',['Deligne1980WeilII','Grothendieck1969HodgeFalse'])
p(3007,'Unweighted admissibility under direct image',[3025,3035,3037],
 'Cor5.3 assertsR^i f_! preservation, with Pro sans and Codex sous conj. type Tate; the later proof asks for complete reducibility.',
 'First decide the preposition from the scan; then prove the conditional statement or isolate an Artin-curve argument that avoids semisimplicity.',
 'WeilII numerical mixedness and deJong4.1 alteration descent are relevant but do not directly prove this source-defined geometric category closure.',
 'The exact premise is textually unsettled, and the manuscript exposes the missing reducibility input.',
 'High priority scan check followed by a bounded proof audit; no broad theorem should be announced now.',['Deligne1980WeilII','deJong1996Alterations'])
p(3008,'Strong resolution versus alteration replacement',[3023,3035],
 'Strong resolution is admitted, and purely inseparable base change is separately required in the spread-out reduction.',
 'Rebuild rational realization arguments using alterations/proper hypercovers while preserving explicit losses in integral and level assertions.',
 'deJong1996Theorem4.1 gives a regular projective alteration with SNC boundary and generically étale alteration over perfect fields; the introduction constructs hypercovers. This does not prove strong birational resolution.',
 'The author labels the resolution input as assumed; later replacement reflects a genuinely weaker geometric operation.',
 'Worth a few-hour dependency chart, not a purported solution of resolution in all characteristics.',['deJong1996Alterations'])
p(3009,'Local constant-coefficient level gain',[3028,3029],
 'The local bound improves to min(i,2n−1−i), with a top-piece claim whose verb differs between transcriptions.',
 'For positive-dimensional boundary points with an SNC resolution, prove the Hodge bound from the common coordinate box; retain the geometric-level statement conditionally and do not identify a wholeE2 term with its surviving quotient.',
 'Riou2010Props2.2–2.3 gives local SNC purity. HodgeIII proper bounds yield the box. Durfee–Saito1990Thm4.1 proves link intersection-cohomology weight estimates with different dimensions/supports. Double blowup obstructs the strong identification.',
 'No historical abandonment evidence; the prior notes conflated a mathematical survival assertion with the Pro verb.',
 'High interest and feasible in one run as a carefully scoped local-Hodge exposition after the scan check.',['Riou2010Purity','Deligne1974HodgeIII','DurfeeSaito1990'])
p(3010,'Local level with varying geometric coefficients',[3030,3032],
 'The coefficient weight and level improvements are questioned on120 and developed incompletely on122.',
 'Separate the refuted weight bound from any still plausible Hodge/geometric-level bound, and state the required degeneration hypotheses explicitly.',
 'Deligne1968 splitting, RiouSNC formulas and WeilII monodromy are exact ingredients. The logged searches did not identify a theorem with the remaining source geometric-level quantifiers.',
 'The source stops amid dimension estimates; a weight counterexample alone does not answer the separate level question.',
 'Worth one run to formulate the strongest surviving coefficient theorem and test elliptic degenerations.',['Deligne1968Lefschetz','Riou2010Purity','Deligne1980WeilII'])
p(3011,'Refinement by local image dimension',[3031],
 'Can the immersion estimates use the definedd_y(f) in a more general setting?',
 'Preserve the definition through closure of the local image; actual fibre dimension is insufficient even for an open immersion.',
 'Riou2.2 gives a nonzero localR¹j_* forG_m→A¹ despite zero-dimensional nonempty fibres. Durfee–Saito supplies related but not identical link estimates.',
 'No reason for abandonment is documented; the exact proposed replacements are marginal and partly ambiguous.',
 'Moderate priority: first formalize the invariant and enumerate basic immersion/projection tests.',['Riou2010Purity','DurfeeSaito1990'])
p(3012,'Unfinished coefficient spectral-sequence calculation',[3032],
 'Theq-indexed fibre dimensions andE2 bounds at the end of122 are left to work out.',
 'A corrected calculation must use the actual dimensions of every SNC stratum and the coefficient family’s relative dimensionj.',
 'Deligne1968 and Riou2.3 justify the inputs; the saved Legendre and Hodge-box computations expose which candidate targets already fail.',
 'The source is unfinished rather than a published false theorem; no historical explanation is supplied.',
 'Feasible technical run once the target is corrected, with useful value for the companion commentary.',['Deligne1968Lefschetz','Riou2010Purity','Deligne1980WeilII'])
p(3013,'Late dimension type and the minus-one bound',[3033,3035,3036],
 'Define type≤d by smooth projective sources of dimension≤d, then seek direct-image boundsd+d′ andd+d′−1.',
 'Keep the untwisted late type distinct from the early Tate-stableD_d. The strict minus-one target is false; a non-strict bound may be the viable target under the manuscript inputs.',
 'RiouSNC purity givesQ_l(−r) in top local degree; Weil purity excludes it from untwisted type≤r−1. Bondarko2018 concerns a different motivic filtration and cannot be substituted without a comparison theorem.',
 'The source changes conventions and later weakens a bound; the obstruction is substantive under the late definition.',
 'High priority as a cross-package definition concordance, with no claim of solving motivic dimension filtration.',['Riou2010Purity','Deligne1980WeilII','Bondarko2018Dimension'])
p(3014,'Curve reduction and the remaining type layers',[3037,3038],
 'Reduce tod′=1, then handle the three rows of the coefficient curve family; final reduction is marked à vérifier/développer.',
 'After correcting the type target, distinguish the two-row affine compact-support sequence from the three-row proper Leray sequence, whose middle row stabilizes atE3.',
 'Deligne1968 splitting and deJong’s curve-fibration argument are relevant established ingredients, but not an exact published closure theorem for this source type.',
 'The author explicitly flags the missing reduction and cancels an earlier semisimplicity-dependent induction.',
 'Good bounded proof-audit task; full categorical closure may exceed one run.',['Deligne1968Lefschetz','deJong1996Alterations'])
p(3015,'One or two primes detect smooth motives',[3040],
 'One invertible prime, or two distinct primes on their invertibility loci, should detect all-prime smoothness.',
 'NOS answers the abelianH¹/trait case. Any generalization must specify the motive category, compatible system, normal base and residue-characteristic exclusions.',
 'Serre–Tate1968Theorem1 is the precise good-reduction criterion; Vasiu–Zink shows that all-prime unramifiedness still does not imply object extension over arbitrary regular mixed-characteristic bases. No exact broad independence theorem found in recorded searches.',
 'No published source explains why this exact manuscript formulation was dropped; do not infer a solution from compatibility alone.',
 'High conceptual interest, but one run should produce an exact case table and dependency list.',['SerreTate1968GoodReduction','VasiuZink2010'])
p(3016,'Coherent integral reference lattices',[3041,3044,3045],
 'Integral realization systems are almost everywhere integral and Hom is finitely generated, but the reference structure is not fully specified.',
 'Specify a common integral realization system up to finite denominators; then prove Hom finiteness, tensor/internalHom closure and the rational Serre quotient.',
 'Tate1966’s integral Hom comparison and Faltings’ extension theorem are concrete cases. The independent arbitrary-lattice counterexample proves that the weakened wording cannot suffice.',
 'The source explicitly leaves aspects of the category informal; no historical reason for omission is established.',
 'High feasibility in a few hours as a precise axiomatic reconstruction labelled as ours.',['Tate1966Endomorphisms','Faltings1986Finiteness','DeligneMilne1982Tannakian'])
p(3017,'Weight-one essential image over regular bases',[3048,3049],
 'Are weight1 effectivity and nonramification sufficient? The source suspects failure in regular mixed-characteristic dimension2.',
 'Use healthy/quasi-healthy regular local bases or explicit low-ramification hypotheses; unrestricted sufficiency is false.',
 'Vasiu–ZinkThm28 gives the exact high-ramification counterexample; Cor4 givesp∉m^p positive extension. Lemma27 converts a finite-flat failure into nonextension of an abelian scheme. Faltings§2Lemma1 addresses morphisms between existing schemes, not this object-existence problem.',
 'The manuscript already retracts certainty and identifies the obstruction’s setting; later work confirms it.',
 'Worth a focused historical/mathematical commentary, not an open unrestricted extension project.',['VasiuZink2010','Faltings1986Finiteness','Stacks0BMA'])
p(3018,'Prime-index versus prime-order reduction',[3050],
 'A finite-flat obstruction may reduce to indice premier or ordre premier; the sources disagree.',
 'Inspect the scan before selecting a reduction theorem, then match finite-flat hypotheses and epimorphism-on-puncture conditions exactly.',
 'Vasiu–ZinkLemma27 proves a broad transfer from finite-flat non-surjectivity to nonextendable abelian schemes; the exact prime restriction was not verified.',
 'Textual ambiguity and absent proof are both explicit; no theorem name is guessed from the uncertain criterion.',
 'Scan-first task with a narrow subsequent literature search.',['VasiuZink2010'])
p(3019,'Pullback without a generic field map',[3051],
 'How to pull back a generically defined integral motive whenS′→S does not meet the generic point?',
 'A relative motivic category with specialization/base-change functors is required; a mapK→K′ cannot be invented.',
 'ArapuraThm6.4.1 compares pure Nori and André motives over smooth characteristic-zero bases; KahnThm5.10/10.2 handles finite Galois descent under neutral fibres. Neither is the exact integral arbitrary-base construction.',
 'The writer states the obstruction directly; later categories change coefficients and hypotheses.',
 'Useful definition-comparison task, with limited prospects for constructing the full category in one run.',['Arapura2013MotivicSheaves','Kahn2025Descent'])
p(3020,'Universal-property coherence and variance',[3052,3055,3060],
 'The envelope property is stated with grain de sel, a variance deletion and eventual equivalence language.',
 'Use an equivalence of additive functor categories and extend natural transformations; monoidal coherence then descends through projectors.',
 'Demazure§3Proposition1 gives the published projector completion and universal extension; JannsenLemma2 gives the additional semisimplicity criterion, logically separate from completion.',
 'The source concerns formulation/coherence, not an unresolved existence theorem in present mathematics.',
 'Very feasible concise reconstruction; keep the remaining variance ink question in the scan queue.',['Demazure1971Motifs','Jannsen1992Motives'])
p(3021,'Geometric level and standard-conjectural motives',[3004,3022,3024,3056],
 'The weight/level programme presupposes motivic and semisimplicity inputs; the attached introduction B12-01 says the structures should exist motivically and be l-independent.',
 'Separate numerical weights, Hodge types, algebraic generation, numerical motives, homological motives and motivated cycles before making any unconditional identification.',
 'JannsenTheorem1 proves numerical pure semisimplicity, not numerical=homological. Arapura6.4.1 compares pure Nori with André; Choudhury–Gallauer9.1 compares Nori/Ayoub Hopf algebras. None proves algebraicity of all motivated correspondences.',
 'The supplied introduction explicitly calls the motivic framework conjectural; no later comparison is evidence that all its standard conjectures are solved.',
 'Highest conceptual value as a dependency map shared with root; a few hours can clarify scope, not settle cycle conjectures.',['Jannsen1992Motives','Arapura2013MotivicSheaves','ChoudhuryGallauer2017','Grothendieck1969HodgeFalse'])
p(3022,'Wrong-order extensions of pure pieces',[3006],
 'The scan104 margin asks whether an extension in the proposed weight order is possible.',
 'For lisse pure sheaves on a smooth finite-field base, keep arithmetic Ext and geometrically nonsplit Ext distinct and use integral weight difference withwt(F)≥wt(G), strict for geometric non-splitting.',
 'WeilII3.4.3–3.4.4 supplies the extension restrictions. Equal-weight arithmetic unipotent self-extensions still exist, so the conclusion is not arbitrary arithmetic semisimplicity.',
 'The question is explicit; no source documents later abandonment. The modern weight formalism answers the precise finite-field lisse interpretation.',
 'Useful short lemma for the companion, already settled under the specified hypotheses.',['Deligne1980WeilII'])
p(3023,'Coefficient and duality yoga to verify',[3018,3026],
 'Scan109 ends with a question after a coefficient bound omittingj; scan115 asks to verify the yoga after a level formula.',
 'Carry the coefficient weight through total-space splitting and duality; candidate corrections must first be confirmed on the scans.',
 'Deligne1968 splitting andHodgeIII elliptic Hodge types show the point-coefficient and elliptic endpoint failures. These tests locate missingj and the likely2n−i+j expression, not the intended ink.',
 'The author flags uncertainty and the transcriptions preserve problematic formulas. No historical cause beyond the unfinished calculation is inferred.',
 'High feasibility scan-and-formula audit, with counterexamples already established.',['Deligne1968Lefschetz','Deligne1974HodgeIII'])
p(3024,'Virtual Betti programme',[3001],
 'Scan99 names Serre’s virtual Betti numbers among the intended applications, without a full formula.',
 'Use the alternating compact-support weight-graded dimensions; identify the precise geometric and coefficient setting before comparing with motivic invariants.',
 'HodgeIII8.2.6 and8.2.8 give the exact mixed-Hodge/compact-support sequence from which additivity follows. This run does not establish Serre’s first announcement date.',
 'Only a programme label is present, so no unfinished proof or abandonment story is reconstructed.',
 'Low research priority but a useful bounded bibliographic/expository task.',['Deligne1974HodgeIII'])
(B/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
print(f'{len(entries)} entry verdicts; {len(problems)} problems')
