"""Serialize explicitly adjudicated early-package claims and searched fates.

The records below were written after reading the full supplied transcriptions,
the indexed notes, and the cited primary source passages. No keyword classifier.
"""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]; O=R/'work/early'
items={x['id']:x for x in json.loads((O/'items.json').read_text())}
claims=[]
def add(n,ii,his,statement,status,cls,fate,refs,search,computation='',confidence='high',loc=None,reconstruction=''):
 ids=['SA08-'+str(i) for i in ii]
 src=[items[i] for i in ids]
 lines=loc if loc is not None else [l for x in src for l in x['lines']]
 scans=sorted(set(s for l in lines for s in l.get('scans',[])))
 claims.append(dict(id=f'SA08-C{n:03}',items=ids,cote='136',scans=scans,lines=lines,
  his_statement=his,statement=statement,status_on_pages=status,
  computation=computation or 'No numerical computation claimed; see the textual/proof scope in CHECK_EVENTS.tsv.',
  **{'class':cls},fate=fate,fate_date='As of 2026-11-19; circulation and publication dates specified in fate.',
  present_status=fate,refs=refs,confidence=confidence,
  reconstruction=reconstruction,search_logs=['logs/early_search_'+s+'.json' for s in search]))
def loc(pkg,scans,ls):
 return [dict(file='MPL_136_'+('002-046' if pkg=='A' else '047-094')+'_transcription.tex',scans=scans,lines=ls)]
S=['exact_primary','cartan_miller','primary_open1','local_cochains']
H=['integral_models','exact_primary','arxiv_zbmath','other_primary_open']
M=['shadow_fate','shadow_exact2','shadow_refs_follow','shadow_hom_search']
T=['local_cochains','topos_comparison_search','other_primary_open']
A=['arithmetic_history','classical_open','shadow_hom_search']
D=['negative_hom_search','shadow_refs_follow','shadow_hom_search']
add(1,[5,7],'∫_c dω=∫_{∂c}ω; Th. de De Rham',
 'For a smooth manifold and smooth singular chains, integration is a cochain map from the smooth de Rham complex to real/complex singular cochains and induces the ordinary cohomology isomorphism. The sheaf proof uses the local Poincaré lemma and an acyclic resolution.',
 'stated without proof','E','Classical before these sheets. de Rham1931 is the original thesis source; Cartan1976 §§1–4 rechecks the simplicial smooth-form theory. The queried attribution of the invention of differential forms to Poincaré is not resolved by this theorem.',['deRham1931','Cartan1976'],['cohomology_classics','exact_donor_open']+S,
 'Stokes boundary cancellation independently checked in proofs.md §10 and early_computations_output.json/stokes_boundary_squared; this does not independently re-prove the complete analytic de Rham theorem.',
 loc=loc('A',[3,4,5],'17-25,56-95'))
add(2,[5],'structure supplémentaire bigraduée ... si X kählérienne compacte',
 'A compact Kähler manifold has the Hodge decomposition H^n(X,C)=⊕_{p+q=n}H^{p,q}(X), compatible with complex conjugation and the cohomology product. Compactness and the Kähler hypothesis are part of the claim.',
 'stated without proof','E','Known before the manuscript. The 1975 primary DGMS paper uses the compact-Kähler Hodge identities and establishes its stronger formality theorem; the opening list merely recalls Hodge theory. No new Hodge theorem is proved here.',['DGMS1975'],['cohomology_classics','sullivan_donor'],loc=loc('A',[3],'27-28'))
add(3,[5],'Théorème de Cartan-Serre sur variétés de Stein',
 'On a Stein manifold, coherent analytic sheaves are acyclic in positive degree; applied to holomorphic forms, the holomorphic Poincaré resolution computes complex cohomology by global holomorphic forms. The line compresses two distinct ingredients.',
 'stated without proof','E','Cartan seminar1951–52, exposés18–19, states and proves the fundamental Stein theorems; Grothendieck1966 p96 also identifies analytic de Rham hypercohomology through Poincaré. This is historical background.',['CartanStein1952','Grothendieck1966'],['cohomology_classics','exact_donor_open'],loc=loc('A',[3],'30-31'))
add(4,[5],'Dwork, Washnitzer–Monsky ... yoga cristallin ... torsion ne sont pas perdus',
 'The historical outline points to arithmetic cohomology, including crystalline theories with coefficient rings not containing Q. It does not specify a single comparison theorem or a uniform assertion that every named theory retains torsion.',
 'stated without proof','F','Not identifiable as one theorem: names and a difficult base-scheme parenthesis replace hypotheses. PD crystalline Poincaré lemmas are verified in the Stacks primary treatment, but that does not resolve the uncertain historical sentence.',['Stacks2026'],['cohomology_classics','other_primary_open','topos_comparison_search'],confidence='medium',loc=loc('A',[3],'33-34'))
add(5,[5],'Th. de Grothendieck ... signification topologique ... algébrique',
 'For a smooth finite-type complex scheme, algebraic de Rham hypercohomology maps isomorphically to analytic/singular complex cohomology; for a smooth affine scheme, global algebraic forms suffice. Broader coefficients mentioned on the page require separate regularity/comparison hypotheses.',
 'stated without proof','E','Exact own prior published theorem: Grothendieck1966 Theorems1 and1′, pp95–96. The paper identifies its original letter to Atiyah as14October1963 and notes added November1963; publication28January1966. The unspecific Deligne/Hartshorne extensions are not folded into its hypotheses.',['Grothendieck1966'],['cohomology_classics','exact_donor_open'],loc=loc('A',[3],'36'))
add(6,[6],'récupéré ... simplement connexe (sauf erreur); équivalence de cat.',
 'For connected nilpotent spaces of rational finite type, Sullivan rational forms and minimal models recover the rational homotopy type; in the simply connected case the rational homotopy groups are dual to minimal indecomposables. Without a rationalization and appropriate finiteness/duality restriction, the sentence as a categorical equivalence is incomplete.',
 'stated without proof','E','Sullivan’s Tokyo1973 lecture, published1975, is directly represented by the English donor leaves. Full published development is Sullivan1977 §§7,8,10. Its introduction dates the work mainly1971–72, not an exact first preprint day. The manuscript is recalling existing work.',['Sullivan1975','Sullivan1977'],['sullivan_donor','exact_donor_open']+H,loc=loc('A',[3,4],'37-50'))
add(7,[7,13],'résolution de Q_*; ce qui se vérifie facilement',
 'Rational polynomial forms on affine simplices are objectwise Poincaré resolutions; their degreewise simplicial groups admit the requisite contractions/extension property. Smooth and real/complex polynomial variants have the appropriate coefficient version.',
 'proof sketched','E','Swan1975 and Sullivan’s prior work supply the rational theory; Cartan1976 Theorem1 and examples pp264–265 give an exact axiomatic comparison. The two acyclicity conditions are separate, and neither says Γ preserves arbitrary quasi-isomorphisms.',['Swan1975','Cartan1976','Sullivan1975'],S,
 'Polynomial integration divides by positive integers, so this proof requires Q in the coefficient ring. The integral replacement is C008, not a reuse of that contraction.')
add(8,[9,10],'t∈J; est une résolution de S; augmentée vers S/J',
 'For a commutative PD ring (S,J,γ) and t∈J, the PD simplex with Σx_i=t and Σdx_i=0 is well defined, is obtained by eliminating one variable in the PD ideal, and its differential complex is an S-resolution. It has a separate augmentation to S/J.',
 'proof sketched','B','The universal Grothendieck construction is published in Cartan1976 §7 pp269–270; its elementary PD Poincaré ingredient also belongs to the earlier crystalline tradition. The choice t∈J is essential to the coordinate substitution.',['Cartan1976','Stacks2026'],S+['other_primary_open'],
 'Independent contraction proofs.md §1; exact finite weight matrices and d² in early_computations_output.json/pd_poincare.')
add(9,[11],'Mais ... en général ... ne sera pas isom.',
 'The arbitrary-triple simplex construction is not asserted to compute H*(X,S) for every X. Objectwise exactness does not supply the needed simplicial/section acyclicity; the text expressly rejects that inference.',
 'stated without proof','B','Cartan1976 Theorem1 and §6 make the extra comparison conditions explicit. The universal weighted case is established separately in §7. No later source located turns arbitrary (S,J,t) into an unrestricted ordinary S-cochain theory.',['Cartan1976'],S+T)
add(10,[12,3],'Γ^pΦ⊗Λ^qΨ; degré ext',
 'The universal simplex object is a differential bigraded algebra with exterior/cochain degree q, total weight w=p+q, differential (p,q)→(p−1,q+1), and a marked closed T of weight1 and exterior degree0. Alternation is in exterior degree.',
 'proof sketched','B','Cartan1976 §7 gives the same weighted PD algebra and simplicial operators. The literal contradictory grading gloss in an earlier interpretation is excluded by the formula and later exterior-degree wording.',['Cartan1976','Roby1963'],S,
 'T²=2T^[2] computed in early_computations_output.json/small_counterexamples; d² matrices in pd_poincare.')
add(11,[13,14],'Φ ... homotope à0 donc ... Γ^p ... si p≠0',
 'An actual simplicial contraction of Φ induces one after applying the indicated functors, so the coefficient objects with positive complementary degree are acyclic. The p=0 endpoint is exceptional; the adjacent contrary reading is flagged.',
 'proof sketched','B','Cartan1976 §7 supplies the homotopy calculation. Pursuing Stacks §111 originalpp455–456 later distinguishes actual homotopy invariance from the false assertion that componentwise Γ preserves every quasi-isomorphism.',['Cartan1976','GrothendieckPS1983'],S+['other_primary_open'],
 'Functorial preservation of a simplicial homotopy is a structural proof; no arbitrary derived-functor invariance is certified.')
add(12,[3,15,53,95,102],'tronquée ... degré n; H^q ... T^[w]',
 'For each weight w, the universal or admissible PD complex has H^q≅H^q(X,k)T^[w] for0≤q≤w and zero above w, under the stated exactness and acyclicity hypotheses. The last coefficient term need not be acyclic. H⁰ for all q is a false literal alternative.',
 'proof sketched','B','Exact published counterpart: Cartan1976 §7 p271, including the endpoint. Garvín et al.1998 Theorem4.2 p176 independently proves its fixed-length integration comparison for any simplicial set in the strict range p<q; its looser Theorem4.3 wording is not used to infer the endpoint. The paper describes Miller1978 as the finite-simplicial-complex predecessor. The Cartan source match resolves the weighted theorem, not the scan reading.',['Cartan1976','Miller1978','GarvinEtAl1998'],S+['garvin_alternates','bib_author_follow'],
 'Poincaré contraction and bounded dimension-shifting argument; see proofs.md §§1,8. The calculation is weightwise; totalization over infinitely many weights is separate.')
add(13,[16,17],'compatibles ... multiplicatives; récupérer ... accouplements',
 'The weighted cohomological product corresponds to binom(r+s,r) times ordinary cup product. Varying sufficiently large weights recovers the ordinary pairing because those coefficients generate the unit ideal. This does not identify a single unweighted alternating PD algebra with ordinary cohomology.',
 'stated without proof','B','Cartan1976 Theorem3 p267 proves cohomological multiplicativity under flat-cycle hypotheses; §7 p271 gives this exact coefficient and coprimality conclusion for Grothendieck’s theory.',['Cartan1976'],S,
 'Binomial structure constants and differently weighted F2 square test in early_computations_output.json; common prime-local no-carry choices prove the gcd claim.')
add(14,[17,43,44],'qième ombre; tous pleinement fidèles',
 'For every commutative k and finite N≥0, M↦ω_N(M)=⊕_{i≥N}MT^[i] is fully faithful; its homogeneous S-linear morphisms are induced by one k-linear map.',
 'proved there','C','The elementary exact theorem is proved on the supplied pages and independently re-proved here. Searches found no exact all-module theorem citation under “ombres/shadows”; Nagpal–Snowden2016/2017 §9 develops related tail reconstruction for nearly finitely presented modules with additional complete noetherian-base hypotheses, not the manuscript’s unrestricted category.',['NagpalSnowden2017'],M,
 'proofs.md §2; finite-field relation matrix checks are supplemental (tail_field_tests).',confidence='high')
add(15,[18,58],'RΓ ... plus l’accouplement de cup-produit',
 'Recover the derived k-module RΓ(X,k) together with its derived cup pairing from the full weighted object through a suitable shadow localization. This includes linear and monoidal assertions beyond finite-tail Hom full faithfulness.',
 'open on the pages','C','The exact unrestricted derived/monoidal quotient is not established by the searched sources. Cartan1976 recovers weighted cohomology and cup products; Nagpal–Snowden §9 provides a restricted exact quotient. Neither identifies the proposed enhanced shadow category. Negative search results are not a novelty claim.',['Cartan1976','NagpalSnowden2017'],S+M,
 'Weight2 multiplication between first shadows is ×2, not an isomorphism: proofs.md §8 and small_counterexamples.',confidence='medium')
add(16,[19],'Γ_k(T)/(T−1) ≃ k_Q',
 'The ordinary quotient ring Γ_k(T)/(T−1) is canonically k⊗Z Q, for every commutative ring k, including the zero quotient when appropriate.',
 'stated without proof','E','An elementary consequence of the standard divided-power identities (Roby; Stacks divided powers), independent of any topological comparison. The manuscript’s global cochain specialization is C017.',['Roby1963','Stacks2026'],['other_primary_open']+M,
 'Universal inverse maps given in proofs.md §8; factorial product identities checked in specialization_and_binomial.')
add(17,[19,20,21],'C_DRS(X,k_Q)≃C_DRpd(X,k)/(T−1); plus gén.',
 'The asserted global rational specialization requires a choice of weight assembly and commutation with limits. For direct-sum assembly and an infinite discrete X, it can yield only rational-valued functions with a common denominator. The bracketed arbitrary (S,J,t) extension has the same issue.',
 'stated without proof','C','Coefficient specialization is valid; the unrestricted global sentence is not established without finiteness/completion hypotheses. Cartan’s fixed-weight theorem and Sullivan’s rational theory do not themselves identify this total specialization. Exact matching searches in the Cartan–Miller and shadow literature did not resolve the assembly convention.',['Cartan1976','Sullivan1977'],S+M,
 'Conditional counterexample and distinction from ordinary product quotient, proofs.md §8.',confidence='high')
add(18,[22,24,25],'on peut se demander si ... induit une équivalence',
 'Ask whether simply connected finite-type integral homotopy types are recovered, and perhaps categorically modelled, by suitably admissible bigraded PD differential algebras or their coalgebra duals after the intended weak equivalences.',
 'open on the pages','C','Mandell’s integral object classification (preprint3Nov2003; publication2006) concerns E∞ Z-cochains and is faithful but not full. Horel’s cosimplicial binomial model (preprint4Nov2022; publication2024) is fully faithful for connected nilpotent finite-type spaces, Theorem5.4 in the opened author version. Neither identifies these PD categories.',['Mandell2006','Horel2024','GrothendieckPS1983'],H,confidence='medium')
add(19,[27],'modèles minimaux ... Je n’ai rien fait',
 'Construct integral minimal models within the proposed PD framework and extract homotopy groups under the connectedness and finite-generation conditions of the opening question.',
 'open on the pages','C','Ekedahl’s numerical minimal models (preprint30June2001; publication2002, Theorem2.7; arXivv2 Theorem2.9) realize connected nilpotent finite-type spaces by numerical simplicial objects. They are not models in the undeclared manuscript PD category; integral minimal numerical models are not generally unique up to strict isomorphism.',['Ekedahl2002','Horel2024'],H,confidence='medium')
add(20,[28],'pas développé une formule de Künneth; plats sur k{T}',
 'Find a Künneth comparison for products retaining all PD and weight structures, with derived tensor over Γ_k(T) where necessary. k-flatness alone does not imply Γ_k(T)-flatness.',
 'open on the pages','C','Cartan’s cohomological product theorem and Horel’s binomial-model Künneth argument are available but have different targets. A full Γ_k(T)-linear structured product theorem for this formulation was not located in the recorded searches.',['Cartan1976','Horel2024'],S+H+M,confidence='medium')
add(21,[29,30,39],'coreprésentant ... sans condts de finitude; commute ... quelconques',
 'A differential bigraded coalgebra with divided copowers is announced to corepresent the cochain functor for all coefficient algebras, commute with coefficient extension, and preserve ordinary colimits in the simplicial input. Unrestricted reflexivity and derived base change are stronger and not established by these assertions.',
 'stated without proof','C','Free representable/colimit constructions and duality explain a route to the ordinary corepresentability assertion. The full PD/coalgebra comparison requires later manuscript data; searches in Sullivan, Cartan, Horel and Grothendieck’s retrospective found no exact all-finiteness-free equivalence.',['GrothendieckPS1983','Horel2024','Cartan1976'],H+S+T,confidence='medium')
add(22,[31,4],'On aimerait ... mais y en a-t-il tjrs ?',
 'Do sufficiently structured flasque replacements exist for every relevant augmented differential PD algebra on a ringed topos, so that structured derived direct images can be defined?',
 'open on the pages','C','Ordinary injective/acyclic resolutions do not automatically preserve the algebra, marked parameter and divided powers. Cartan’s comparison axioms and standard sheaf-derived methods are only partial context. The later explicit De Rham condition is a restriction on topoi, not an existence theorem for every topos.',['Cartan1976','Stacks2026','GrothendieckPS1983'],T+S,confidence='medium')
add(23,[32],'Pb est ouvert ... posé par Deligne; Non',
 'The cosimplicial-topos test is open on scan16; scan91 later answers negatively for the specifically formulated De Rham condition. The second statement must not silently be treated as a resolution of every possible structured-derived-image question.',
 'corrected by himself later','F','The text supplies an early question and a later negative answer, but no identified general theorem with matched quantifiers. Searches of Deligne/cosimplicial/PD and the explicit condition did not identify an external exact settlement. Retain the two formulations separately.',['GrothendieckPS1983','Cartan1976'],T+S,confidence='medium')
add(24,[33,90],'paracompacts ... si souvenirs sont exacts',
 'A paracompact/smooth or analytic construction is recalled tentatively. On later sheets, local constant coefficients and Poincaré-type simplex/cube arguments give a supported comparison under local geometric and acyclicity hypotheses.',
 'proof sketched','C','Cartan1976 examples pp265–266 verify standard smooth and polynomial theories. That does not certify the manuscript’s broader wording for arbitrary topological spaces or for arbitrary presheaves.',['Cartan1976'],S+T,confidence='medium')
add(25,[34,35,92],'D=ΓΦ⊗ΛΦ; D/(dT); par dT',
 'For the full PD Koszul object D, quotient by dT and kernel of multiplication by dT identify the smaller complex with a shifted kernel as complexes, with the appropriate sign. The kernel’s ambient multiplication is zero because (dT)^2=0; a transported product is a different structure.',
 'corrected by himself later','B','Cartan1976 §7 pp269–270 gives the full algebra/quotient calculation. The manuscript itself retracts multiplicative compatibility on scan75 and later distinguishes operations. Thus the additive identification survives while the naive ambient-product assertion fails.',['Cartan1976'],S,
 'Independent exterior-algebra argument: (a dT)(b dT)=0. Necessary degree/sign conventions explained in proofs.md §§1,8.')
add(26,[22,36,93],'J’ignore si ... C ... D ... suffit; à expliciter',
 'Determine which extra operations on the larger simplicial object or its homotopy/cohomology data recover the full PD multiplicative invariant, and whether C or D already suffices.',
 'open on the pages','C','Cenkl–Porter1982 Theorems1–2 p11 extend integration to a bar-coalgebra/DASH morphism and construct wedge-i products; Cenkl1989 develops higher operations further. Mandell and Horel give other enhanced reconstruction models. No opened source equates the author’s unresolved C/D package with those complete invariants.',['CenklPorter1982','Cenkl1989','Mandell2006','Horel2024'],S+H+['cochain_obstruction_find','cenkl_final'],confidence='medium')
add(27,[41],'c_ij≠0(p) sss ...; c_ij≡∏c_uε,vε(p)',
 'For prime p, c_{i,j} is nonzero modulo p exactly when adding i and j in base p has no carry; its residue is the product of the digitwise binomial coefficients. The recursive formulas on scan21 are consequences.',
 'proved there','E','Lucas1878 supplies the digit congruence and hence the no-carry criterion. The manuscript independently derives the needed form by Frobenius. The exact original Lucas pp51–52 was opened through Numdam; theorem content is also independently proved here.',['Lucas1878'],A,
 'proofs.md §2; early_computations_output.json/arithmetic, 32,805 digit tests and the scan21 recurrences.')
add(28,[42],'Alors on a x_N=x_N+1',
 'Let E be a Z_(p)-module, p^e≥N+1, I={N}∪{N+p^ε:0≤ε≤e}. If binom(j,i)(x_j−x_i)=0 only for i=N,N+1 and j∈I,j>i, then x_N=x_N+1. Other x_j need not coincide.',
 'proved there','D','The exact sparse lemma was not located under the recorded arithmetic/shadow queries; its induction is valid after preserving the displayed ranges. This classification records an unlocated external development, not mathematical novelty. It follows from the digit-unit recursion.',['Lucas1878'],A+M,
 'Manuscript induction checked; explicit F2 counterexample to the stronger conclusion exhaustively enumerated in sparse_F2.')
add(29,[43],'binom ji(x_j−x_i)=0 ... Alors ... x_i=x_N',
 'For any abelian group E and family x_i,i≥N, the all-pairs binomial relations force the family to be constant. No bounded exponent, finite generation or completion is needed.',
 'proved there','C','The supplied proof and the independent prime-local common-index proof settle the statement. Related later tail theory appears in Nagpal–Snowden §9 with substantially narrower coefficient/object hypotheses; no exact general theorem citation was found in the recorded zbMATH/arXiv/MathOverflow/Numdam searches.',['Lucas1878','NagpalSnowden2017'],A+M,
 'proofs.md §2; tail_field_tests give finite-field consistency checks, not the arbitrary-group proof.')
add(30,[44,45],'ω_N est pleinement fidèle; π_N ... adjoint à droite',
 'The shadow functor is fully faithful. Its right adjoint is the module of compatible families in the homogeneous pieces of a graded S-module, with all binomial transition equations; on a shadow the evaluation map is an isomorphism.',
 'proved there','C','The compatible-family description is a standard Hom/adjunction calculation once the tail is fixed. Full faithfulness is C014/C029. Nagpal–Snowden’s fp-envelope results are a later related development, not an identification of these unrestricted adjoints.',['NagpalSnowden2017','Stacks2026'],M+T,
 'Direct Hom calculation and common-index constancy, proofs.md §§2–4. The same-page “Bijectivité?” is answered, not left open.')
add(31,[47,49,61],'adjoint ... tronquage; Hom^d(M*,φ_NN*)',
 'In the graded category, inclusion of objects supported in degrees≥N is left adjoint to tail truncation, and tail truncation has the separately constructed right adjoint. Truncation is not fully faithful on all modules, and the written contrary variance cannot be true.',
 'false as stated','E','The corrected directions are ordinary graded-module adjunctions. Standard category/sheaf sources confirm adjunction variance; the exact manuscript reversal is refuted directly. No novel adjunction theorem is inferred.',['Stacks2026'],T+M,
 'Counterexample S=Q[T], Hom_gr(S,TS)=0 but End_gr(TS)=Q, proofs.md §4 and small_counterexamples.',
 reconstruction='Refined statement: i_N ⊣ τ_N ⊣ φ_N; source support and grading conventions must be specified.')
add(32,[48,53],'τ_0 φ_N τ_N(M⊗S)≃M⊗S',
 'For M concentrated in degree0, and more generally the specified nonnegative induced graded objects, the nonnegative part of the right-adjoint recovery reconstructs M⊗S from any finite tail. Removing nonnegative support is invalid.',
 'proved there','C','The stronger weighted-family theorem proves this intended finite-tail unit statement. Later nearly-finitely-presented fp-envelopes in Nagpal–Snowden have related recovery behavior under additional hypotheses; they do not remove this support restriction.',['NagpalSnowden2017'],M,
 'proofs.md §§3–4; weighted_family identity checks; the nonnegative bound is part of the proof.')
add(33,[50,51],'la sous-cat. épaisse ... négligeables',
 'The class of all graded modules whose elements are individually annihilated by a sufficiently high divided-power tail is claimed thick/Serre. This is false, already over F_p, so the proposed unrestricted quotient requires a replacement category.',
 'false as stated','C','Refuted by the exact sequence0→I/I²→S/I²→S/I→0. Nagpal–Snowden2016/2017 Proposition9.8 proves a restricted quotient equivalence with finitely generated torsion objects in the nearly finitely presented category over a suitable complete noetherian base. This is a genuine restricted analogue, not the false unrestricted claim.',['NagpalSnowden2017'],M,
 'proofs.md §5 and negligible_counterexample; refined statement C034.')
add(34,[51,58],'ombres virtuelles ... à degrés≥0?',
 'A usable category of eventual shadows needs a precisely specified torsion class, support and morphism localization. The pages do not finish an unrestricted abelian/derived/monoidal quotient with the asserted recovery properties.',
 'open on the pages','C','A concrete modern restricted replacement is Nagpal–Snowden §9.2: fp-envelope exactness and equivalence Mod^fp≃Mod^nfp/(finitely generated torsion), under complete noetherian hypotheses. Its relation to every manuscript coefficient module and to the cup pairing remains to be supplied.',['NagpalSnowden2017'],M,
 'The obstruction to the literal class is C033; the finite pairing ×2 test is proofs.md §8.',confidence='medium')
add(35,[52],'Cor ... Ext^i ...',
 'For S=Γ_k(T), every k-module M, N≥0, i≥0 and n>0, the page asserts Ext^n_gr(τ_{N−i}(S)[−i],M⊗_kS)=0; only0≤i<N is nontrivial. This is stronger than the established equality of Hom groups, and no derived proof is supplied on this page.',
 'stated without proof','C','Nagpal–Snowden Theorem8.3 and Lemma9.4 give related graded Ext invariance for finitely presented targets over suitable complete noetherian bases. Their Remark8.4 uses target D/(x), not an induced M⊗D, so it does not refute this exact corollary. Neither completeness nor finite presentation is assumed here, and an exact unrestricted printed proof has not been identified.',['NagpalSnowden2017'],M,
 'No computation is represented as proving this general Ext statement; the later paper’s explicit noncomplete-base example is a hypothesis check.',confidence='medium')
add(36,[53,54],'c_ℓ,k ξ_k=c_ℓ,k−i ξ_k+ℓ; ξ_k=binom ki ξ',
 'For0≤i≤N and any abelian group M, every family satisfying the weighted binomial recurrence is uniquely ξ_k=binom(k,i)ξ. Several proof lines have inconsistent c_{k,k−i} indices; the intended statement is determined by the correctly displayed formula.',
 'proved there','C','The exact family theorem is proved by the manuscript and independently re-proved here. Its role is the nonnegative tail unit. Nagpal–Snowden is related later tail theory; no exact general coefficient theorem under another name was located.',['Lucas1878','NagpalSnowden2017'],A+M,
 'proofs.md §3; weighted_family identities, gcd witnesses, and ratio checks in actual output.')
add(37,[56],'les deux quantités ... égales; l’un unité ssi l’autre',
 'For j′≥j≥0, c_{j′−j,j+i}/c_{j′−j,j}=c_{i,j′}/c_{i,j}. If the two c_{i,*} are p-local units, the recurrence coefficients are simultaneously units and vanishing propagates between the corresponding good indices.',
 'proved there','E','A factorial identity and elementary localization argument, used within the manuscript proof. Lucas arithmetic is prior background; no separate later theorem is needed or asserted.',['Lucas1878'],A,
 'Exact Fraction identities for0≤i,j,j′<10 in weighted_family; general cancellation proof in proofs.md §3.')
add(38,[53,57],'k′=p^r−1; les mêmes conditions; cqfd',
 'Arbitrarily large good indices exist; a common index p^r−1 has all needed binomial units and compares any finite set of coefficients. The proof’s zero-versus-nonzero line must be read consistently with the unit condition.',
 'proved there','E','A direct consequence of Lucas’s congruence, used in the independent weighted-family proof. The deleted carry proof is superseded on the manuscript page; it is not an additional open lemma.',['Lucas1878'],A,
 'Common-index proof in proofs.md §§2–3; the literal =0 reading is separately flagged.')
add(39,[60],'v_p(n!)=(n−chif_p n)/(p−1)',
 'Legendre’s valuation identity and its p-typical specialization show that (p^{r+1})!/((p^r!)^p p!) is a p-local unit. The isolated unfinished (n+1)! line does not add another proved formula.',
 'proved there','E','The valuation formula is classical and the p-typical relation is standard divided-power arithmetic. The manuscript calculation is correct with factorial parentheses and localization, not completion.',['Lucas1878','Roby1963'],A+M,
 '1,505 exact factorial valuations and16 p-typical unit cases in arithmetic/p_typical_units; proofs.md §6.')
add(40,[61],'indépendant ... du choix de α',
 'The shifted truncation/right-adjoint identity holds with the target support bound; consequently Hom^{−d}(τ_αM_S,N_S), d>0, is canonically independent of α≥d by passing to a common sufficiently high cutoff.',
 'proof sketched','D','No exact negative-Hom cutoff theorem was found in the recorded module-tail and negative-degree searches. Its support argument follows from the proved nonnegative recovery theorem; this is an independent proof, not a novelty claim.',['NagpalSnowden2017'],D+M,
 'General adjunction/support proof in proofs.md §4; no finite numerical test is substituted for it.')
add(41,[63],'d≥β−α; mT^[j]↦c_dj u(m)T^[d+j]',
 'For β≥α≥0 and d≥β−α, Hom^d_S(τ_αM_S,τ_βN_S)≅Hom_k(M,N), with the displayed binomial multiplier.',
 'corrected by himself later','C','The page replaces the insufficient bound d≥0 by the correct support bound. It follows from finite-tail recovery; related later tail reconstruction is found in Nagpal–Snowden, but an exact all-module printed formula was not located.',['NagpalSnowden2017'],M+D,
 'Formula checked symbolically by the weighted recurrence; proofs.md §4.')
add(42,[64],'c_d,β−d u=0; α≤j<β−d',
 'For0≤d<β−α, the same parameter u must obey c_{d,j}u=0 exactly for α≤j<β−d. The inclusive endpoint in the vertical list is false; the subsequent strict inequality gives the valid version.',
 'false as stated','E','This is a direct support calculation, not a new literature theorem. Exact module-tail searches locate no reason to add the excluded endpoint. The F2 example refutes the inclusive reading while preserving the author’s following corrected range.',['NagpalSnowden2017'],M+D,
 'F2 α1 β3 d1 multiplication-by-T counterexample, proofs.md §4 and small_counterexamples.',
 reconstruction='Refined statement: strict upper bound j<β−d as already written in the next display.')
add(43,[60,66],'T_r^p=pν′_rT_r+1; ... a comme base',
 'For k a Z_(p)-algebra, the p-typical generators T_r=T^[p^r] obey T_r^p=pν′_rT_{r+1}, with unit ν′_r, and finite digit monomials0≤i_r<p form a basis. The tail degree criterion is valid for those digits.',
 'proof sketched','E','Standard divided-power arithmetic, checked through primary PD/module sources. The omitted digit restriction is necessary and is not supplied as an ink reading.',['Roby1963','NagpalSnowden2017','Stacks2026'],A+M+['other_primary_open'],
 'Legendre and normal-form calculations in proofs.md §6; unit coefficients in p_typical_units.')
add(44,[67],'les relations sont ... T_s^(p−1)t_s=pν′_st_s+1',
 'Those relations are necessary for a map from the p-power tail, but do not by themselves present that ideal as an S-module. Cross-generator syzygies are also required.',
 'false as stated','E','Basic module presentation theory and the explicit F2 quotient refute sufficiency. Modern coherence/presentation work of Nagpal–Snowden does not validate this abbreviated list. The negative-degree proof only uses necessity.',['NagpalSnowden2017'],M+D,
 'Omitted syzygy y e_x+x e_y in S/(x)e_x⊕S/(y)e_y, proofs.md §6 and small_counterexamples.',
 reconstruction='Refined statement: every actual map satisfies these relations; no converse without all syzygies.')
add(45,[68],'ξ_s=pν′_sξ_s+1; partie divisible',
 'A negative-degree map over a p-local base yields a coherent chain of p-roots after unit rescaling. The k-submodule generated by that chain is divisible; mere membership in every p^hM would not suffice.',
 'proof sketched','D','The exact graded-Hom factorization was not located externally. The difference between infinite height and divisibility is classical abelian-group theory and is explicitly illustrated by the opened MathOverflow primary discussion; no claim of novelty is made for the witness.',['InfiniteHeightMO2022','NagpalSnowden2017'],D,
 'General coherent-root proof in proofs.md §7; necessary p-typical relation checks.')
add(46,[68,69],'N₀=∩nN le plus grand sous-module divisible',
 'For an arbitrary module N, the intersection of all integer multiples need not be divisible and need not equal the maximal divisible submodule.',
 'false as stated','E','The infinite-height distinction is standard. The explicit presentation A=<x,y_n|px=0,p^ny_n=x> appears in the opened MathOverflow discussion and independently gives intersection≅Z/p. It refutes the literal identification, not the coherent-root argument of C045.',['InfiniteHeightMO2022'],D,
 'Complete proof and finite presentation Smith checks in proofs.md §7 and infinite_height_finite_stages.',
 reconstruction='Refined target for the globally stated factorization is N_∞=∩nN, without the word divisible.')
add(47,[68,61],'u se factorise par N₀S; si k de torsion ... Hom=0',
 'For arbitrary commutative k, d>0 and α≥d, every degree−d map τ_αM_S→N_S has coefficients in N_∞=∩_{n≥1}nN. In particular it vanishes when N_∞=0, including every module over a unital torsion ring.',
 'proof sketched','D','The global intersection-target formulation survives the false divisibility label by localization and detection in N/nN. No exact external statement was found in the recorded negative-Hom/module searches. It is proved here under precisely the stated support conditions.',['InfiniteHeightMO2022','NagpalSnowden2017'],D+M,
 'Local-to-global coefficient proof and bounded exponent corollary, proofs.md §7. Do not promote N_∞ to a globally divisible module.')
add(48,[79],'commute aux lim inductives ... représentable',
 'For a small indexing category Δ, a contravariant set-valued functor on simplicial sets carrying all small colimits to limits is determined by and represented by its values on standard simplices, via the density presentation X=colim_{Δ/X}Δ[n].',
 'proof sketched','E','Presheaf density/Yoneda is established category theory. The Stacks treatment of cohomology on a category uses the same representable resolution mechanism. This is an ordinary representability statement, not Brown representability in a homotopy category.',['Stacks2026'],T,
 'Direct density calculation: F(X)=lim_{σ∈Δ/X}F(Δ[n]); naturality gives the representing simplicial object.')
add(49,[81,82],'i_n*(M)_p; Λ^(n+1)Φ_*; T∧',
 'For simplicial modules, that is presheaves on Δ, the right adjoint to evaluation at [n] has value at [p] equal to the product of M indexed by Hom_Δ([n],[p]). Standard normalized simplex cochains identify with Λ^{n+1}Φ and differential wedge by T, with degeneracies included.',
 'proof sketched','E','Standard simplicial normalization and representable/coinduced functors; Cartan1976 pp261–264 spells out faces, degeneracies and normalized groups. A reversed Hom index in the manuscript is a reading alarm.',['Cartan1976','Stacks2026'],S+T,
 'Simplicial boundary cancellation in proofs.md §10; no identification of historical “semi-simplicial” with a face-only category.')
add(50,[83,88],'Stokes; et unique; A_p^n=0 si n>p',
 'For a simplicial cochain object resolving a constant coefficient object and vanishing above simplex dimension, there is a unique natural integration chain map to normalized standard cochains inducing the identity on degree-zero coefficients. Its construction proceeds by dimension induction and ∂²=0.',
 'proved there','B','Exact published counterpart is Cartan1976 Theorem2 p266 and interpretation p267. The manuscript additionally phrases a universal quotient and extension to an abelian-category setting; those formal variants follow the same induction after specifying exactness and existence of the relevant products.',['Cartan1976'],S,
 'proofs.md §10 and stokes_boundary_squared. The proof checks additive chain compatibility, not strict multiplicativity.')
add(51,[85,86],'Hom(A/X, ...); faisceaux / cofaisceaux',
 'The slice topos of a simplicial set X is equivalent to presheaves on Δ/X. A formula omitting /X describes the wrong presheaf category. For sheaf coefficients, right Kan extension uses products; for the dual covariant/cosheaf construction, left Kan extension uses sums.',
 'proof sketched','E','The category-of-elements equivalence and Kan-extension variance are standard; the primary Stacks category-cohomology construction supplies a direct consistent model. The notation defect does not create a new cohomology theory.',['Stacks2026'],T,
 'Objectwise category-of-elements verification; no numerical calculation.')
add(52,[87,88],'si F ... loc. constant ... C*(X,F)≃Γ(C_X*⊗F)',
 'For a locally constant coefficient sheaf on the simplicial slice, the standard local-coefficient cochains identify with sections of the tensor resolution and compute the corresponding cohomology, under the usual bounded-below totalization for complexes.',
 'proof sketched','E','Classical local-coefficient simplicial cohomology and its category resolution; the Stacks category-cohomology complex computes derived sections for arbitrary coefficients by a different product-over-arrows construction. That result does not validate the manuscript’s particular tensor model for arbitrary F.',['Stacks2026','Cartan1976'],T+S,
 'The distinction is checked by the full arbitrary-presheaf counterexample C053, proofs.md §9.')
add(53,[87],'sans hypothèse de loc. constance ... à vérifier ce point',
 'The global sections of C_X^*⊗F are claimed to compute RΓ(X,F) for every presheaf F, and similarly hypercohomology. With this literal objectwise tensor construction, the assertion is false even for a field and the simplicial circle.',
 'false as stated','C','The author flags the step. Standard category/sheaf resolutions do compute derived sections, but the tensorized simplex resolution need not be section-acyclic. The explicit F on Δ/(Δ¹/∂Δ¹) has zero tensor-cochain sections but H¹(F)=k. This is a correction, not an unresolved cohomology conjecture.',['Stacks2026'],T,
 'Full variance, injective coinduction, section and H¹ calculation in proofs.md §9.',
 reconstruction='Refined statement C052 requires locally constant coefficients or an independently proved tensor-acyclicity hypothesis.')
add(54,[84,88],'K_n; homomorphisme de complexes; normalisé',
 'The individual degree-n integration functionals need not form a simplicial morphism before assembly. The assembled natural map on simplicial cochains is a chain map by Stokes and factors through normalization because degenerate simplices give the required zero values.',
 'proved there','B','Cartan1976 Theorem2 gives the assembled map with uniqueness. Its claim is exactly additive naturality and chain compatibility, preserving the distinction made by the manuscript.',['Cartan1976'],S,
 'proofs.md §10; boundary-squared cancellation rechecked.')
add(55,[89],'Reste à voir ... multiplicatif',
 'Does the integration comparison identify the cohomological wedge and cup products? A natural additive chain map by itself does not prove this, and strict chain-level multiplicativity is a stronger assertion.',
 'open on the pages','B','Cartan1976 Theorem3 p267 proves the cohomological result under flatness of cycles in both cohomological theories; it applies to the integral free-term example. Cenkl–Porter later addresses higher homotopies. This does not assert a strict multiplicative integration map.',['Cartan1976','CenklPorter1982'],S+['cochain_obstruction_find'],
 'Hypotheses checked against the published theorem, not inferred from the existence of Stokes integration.')
add(56,[90],'lemme de Poincaré; cubes ...',
 'For the specified smooth/analytic local model, differential forms resolve constants and can be compared through simplex or cube integration, provided local Poincaré exactness and the stated extension/acyclicity conditions hold.',
 'proof sketched','E','Cartan1976 examples and the prior smooth de Rham theorem support these local cases. The distinct cubical theory of Cenkl–Porter1984 Theorem4.1 p44 gives all-degree comparison for finite-type simplicial complexes and coefficient Q_q, where primes≤q are inverted; it does not remove local geometric or coefficient hypotheses from this claim.',['Cartan1976','deRham1931','CenklPorter1984'],S+T+['reference_gaps','final_reference_routes','cenkl_final'],
 'The pointwise contraction is mathematical background; no new universal flasque theorem is certified.',confidence='medium')
add(57,[35,91],'est faux; i(x)i(y)=0; flasque si p≥0',
 'After passing from the full algebra to the kernel of wedge by dT, the ambient product of two kernel elements is zero. Surjectivity after sections is supported for positive complementary degree; extending it to p=0 ignores the nontrivial cohomological obstruction.',
 'corrected by himself later','B','Cartan1976 §7 computes the exceptional homotopy of the exterior terms and the quotient construction. The author’s own retraction on scan75 and qualification “épi si p≠0” on scan76 support the corrected positive range.',['Cartan1976'],S,
 'Exterior square-zero calculation in proofs.md §§6,8. The scan75 p≥0 reading is registered, not silently amended.')
add(58,[91,92],'H^{00}=k^{π₀(X)}; puissances divisées ... nulles',
 'The larger complex has the displayed constant corner k^{π₀(X)} and the wedge-by-dT row has an exceptional p=0 cohomology range. In its positive ideal, kernel elements locally divisible by dT have higher divided powers zero, so the proposed operations descend to the image of the quotient map.',
 'proof sketched','B','Cartan1976 §7 verifies the related homotopy computation. PD vanishing is a structural consequence of the graded divided-power axioms in the full exterior model; it does not put divided powers on ordinary unweighted cohomology.',['Cartan1976','Roby1963'],S,
 'Local form y=(dT)z, (dT)^2=0 and the graded PD product rule; constant-corner/positive-range distinction checked from both pages.',confidence='medium')
add(59,[93],'les seules données supplémentaires ... plus les axiomes divers',
 'Products and divided powers away from complementary degree0 are forced by the stated quotient/module identities. Exceptional complementary-degree-zero operations, together with compatibility axioms, remain additional data; their existence and sufficiency as a homotopy invariant are not established.',
 'open on the pages','C','Cenkl1989 constructs higher cochain operations on a Cartan–Miller model. It does not prove that the manuscript’s residual binary/PD list is a complete structure or model for homotopy types.',['Cenkl1989','Horel2024'],S+H+['cochain_obstruction_find'],confidence='medium')
add(60,[94],'trouver des splittings canoniques; p=1,q=1 ... unique',
 'For p≥1 the asserted projectivity gives splittings of the displayed simplicial-module short exact sequences. A simple canonical choice is sought. In the special case p=q=1, vanishing of Hom(Φ⊗Ψ,Φ) implies uniqueness once existence is supplied.',
 'proof sketched','C','Standard simplicial normalization and projective lifting support the conditional argument. No exact general canonical-splitting formula was found in Cartan/Roby or the topos searches. The special uniqueness argument is valid because evaluation in degree0 gives Φ₀⊗Ψ₀=0.',['Cartan1976','Stacks2026'],S+T,
 'Adjunction calculation checked; existence and canonical choice are distinguished.',confidence='medium')
add(61,[95,96,3],'u:Z→Φ; a) plat b) ... tensorisation avec tout faisceau',
 'Let0→Z→Φ→Ψ→0 be exact on a topos, with Ψ Z-flat, and assume every positive Γ^iΦ and Λ^iΦ remains section-acyclic after tensoring with every abelian sheaf. Then K=ΓΦ⊗ΛΨ resolves ΓZ(T), coefficient base change preserves the resolution, and the terms with positive complementary degree are acyclic; the weightwise comparison follows.',
 'proof sketched','C','The underlying flat Koszul/PD construction is standard and Cartan’s universal simplicial example is established. The exact all-topos test-embedding formulation and its existence are not supplied by a general literature theorem found in the recorded searches. The stated strong tensor-acyclicity hypothesis is retained.',['Roby1963','Cartan1976','Stacks2026'],T+S,
 'Local splitting/filtered-flat reduction and PD Poincaré proof; weightwise bounded dimension shifting. No claim that arbitrary topos embeddings satisfy the hypothesis.')
add(62,[97],'Corollaire plus général ... f_* ... Rf_*',
 'For f:X→Y, the same weightwise relative comparison follows if the coefficient terms are f_*-acyclic with the required base-change stability. Absolute Γ(X,−)-acyclicity alone does not supply this relative hypothesis.',
 'stated without proof','C','Standard derived-image acyclic resolution theory establishes the corrected conditional statement. The page’s stronger automatic relative conclusion is not justified by an absolute-only interpretation of “flasque”; the term’s intended strength must be retained as a hypothesis question.',['Stacks2026'],T,
 'Hypothesis audit, not a proof that the manuscript’s test object is relatively acyclic in every situation.',confidence='medium')
add(63,[96,99],'universellement injectif; Ker de rang1; ΓL',
 'For a short exact sequence0→L→Φ→Ψ→0 with flat terms/quotient in the specified ringed-topos setting, ΓΦ⊗ΛΨ resolves ΓL. A pure monomorphism means stability under tensoring; it is not an initial object. The later marked-parameter model specializes to L of rank1.',
 'proof sketched','E','The PD Koszul construction is prior algebra; primary Roby/Stacks and Cartan’s free case support the mechanism. Flatness is needed for the sheaf and base-change reduction; rank1 enters only when identifying ΓL with k{T}.',['Roby1963','Stacks2026','Cartan1976'],T+S,
 'Free split local calculation is proofs.md §1; arbitrary-module nonflat exactness is not asserted.')
add(64,[98],'λu=u′; μu=u′; comparaison ...',
 'Maps of admissible embeddings induce structure-preserving comparisons. Two choices λ,μ should yield the same comparison after passing through common enlargements and the intended localization; composition requires coherence/transitivity, not just pairwise existence.',
 'proof sketched','C','The manuscript develops a common-enlargement route and later admissibility sheets continue it. Cartan’s natural comparison theorem is narrower. No external theorem was located identifying this exact localized PD category or proving the requested full coherence from the early proof sketch alone.',['Cartan1976','GrothendieckPS1983'],T+S+H,confidence='medium')
add(65,[100],'quasi-isomorphisme universel; après ⊗_{k{T}}k′{T}',
 'The coefficient-comparison map is claimed to remain a quasi-isomorphism after ordinary tensor extension over the marked divided-power coefficient algebra. The needed flatness/derived-tensor and section-acyclicity justification is not completed in the early passage.',
 'open on the pages','C','Standard derived base change and the weightwise flat examples are partial evidence only. Neither Cartan’s additive theorem nor ordinary k-flatness proves unrestricted Γ_k(T)-linear universal quasi-isomorphism. Exact formulation searches found no general settlement.',['Cartan1976','Stacks2026'],T+S+M,confidence='medium')
add(66,[101,102,103],'structures ... spéciales ... catégories de fractions; toutes ... quasi-isos',
 'A special marked k-PD de Rham structure has H^{*,0}=k{T}, vanishing positive exterior cohomology, and flat terms. Maps preserving all structures and the fixed k and T then induce the identity coefficient algebra and are quasi-isomorphisms. The printed vanishing line must exclude exterior degree0; otherwise it contradicts the first axiom.',
 'stated without proof','C','With the reconstructed positive-degree qualification, the quasi-isomorphism assertion is immediate. This defines an ordinary category of fractions; no model/infinity enhancement or nonempty/coherent comparison theorem follows just from the definition. Literature comparisons remain partial.',['Cartan1976','GrothendieckPS1983'],T+S+H,
 'Degree-zero contradiction checked directly; no reading changed. Fixed coefficient/marked parameter hypotheses are indispensable.')
add(67,[6,109],'Step1 ... Step2 ... construct the minimal model',
 'The reused English source constructs a simply connected minimal rational/real de Rham model by adjoining closed generators to hit new cohomology and generators with decomposable differentials to kill the next kernel, under its connectedness and finiteness conventions.',
 'proof sketched','E','Exact donor identified as Dennis Sullivan, Differential Forms and the Topology of Manifolds, Tokyo1973 lecture, published1975 pp37–49; author-hosted typescript pp4–6 matches these leaves. Later complete development is Sullivan1977. This is reused prior literature, not an original Grothendieck construction.',['Sullivan1975','Sullivan1977'],['sullivan_donor','exact_donor_open'],
 'Inductive degree argument checked; the donor’s finite displayed lists do not authorize arbitrary finite-dimensionality assumptions beyond its setting.',
 loc=loc('B',[51,53],'169-197,257-290'))
add(68,[6,109],'Theorem B ... rank ... Hurewicz ... Whitehead products',
 'For a simply connected triangulated space in the rational finite-type setting, a minimal model’s degree-i indecomposables are dual to π_i⊗Q; the Hurewicz image is read from closed indecomposable generators and the quadratic differential is dual to Whitehead products. The formulation requires the usual choice of compatible minimal generators.',
 'stated without proof','E','Word-for-word donor counterpart is Sullivan1975 author typescript p6, TheoremB, followed by a Postnikov/Hirsch proof description. Sullivan1977 §§7–10 supplies the developed theory. The conference date1973 and publication1975 are distinct; the donor sheet itself is undated.',['Sullivan1975','Sullivan1977'],['sullivan_donor','exact_donor_open'],
 'Small-degree generator/Hurewicz example is a formal consequence of the stated minimal-model theorem, carried as background rather than independently re-proved.',
 loc=loc('B',[49,51,53],'86-107,169-177,257-290'))

# Reused donor leaves: the 1972 publication predates the new PD work.
# Classification A means an exact own published counterpart to this earlier
# typescript; it does not date the physical donor or make it a later discovery.
G=['sga_donor_exact','sga_hodge_picard_search']
add(69,[72],'pour un tore T, on a F(T)=0',
 'For a relative complex analytic torus T, the lattice-to-Lie comparison E(T)=R(T)⊗Z O_S→Lie(T) is an isomorphism, so F(T)=0. In the semiabeloid extension setting this identifies E^t with the toric Lie subbundle, gives F(A^natural)=F∩E^f, and supplies the stated filtered exact sequences when the lattice spans the Lie algebra.',
 'proof sketched','A','Exact own published counterpart: SGA7 I, Exposé IX13.4.10–16, printed495–497 (PDF500–502),1972. This precedes the new 1975–76 PD work; the donor draft date is not established. The hypotheses come from13.3.16 and13.4.2–4, not from an arbitrary ringed-topos PD structure.',['SGA7IX1972'],G,
 'For T=(C*)^r, R(T)=(2πiZ)^r spans C^r; the assertion is the relative version. Text/source correspondence checked independently of the PD theory.',loc=loc('A',[36],'1035-1054'))
add(70,[73,74,75],'B≃E^ab/(F^ab+R^ab); structures de Hodge mixtes',
 'On the locus where the lattice R is locally constant, a semiabeloid analytic group with the stated torus/abeloid decomposition yields a mixed Hodge structure with weights−2,−1,0. The abeloid quotient is reconstructed from its lattice and Hodge subbundle as E^ab/(F^ab+R^ab). The text notes this model motivated Deligne’s higher-dimensional Néron conjectures; it does not prove those conjectures.',
 'proof sketched','A','Exact own published counterpart SGA7 IX13.4.17–18, printed497–498,1972. Original13.4.6 printed494 itself reverses the ±1 filtration indices relative to its later degree description: this is a source-level inconsistency, not grounds to change the manuscript reading. The modern decreasing-filtration reconstruction is explicitly separate.',['SGA7IX1972'],G,
 'Lattice quotient and filtration-kernel calculation checked formally; no new proof of higher-dimensional Néron conjectures. Published pages499 and503 were inspected as images.',
 loc=loc('A',[38,46],'1124-1138,1438-1446'),reconstruction='Modern decreasing convention: F^(−1)E=E, F^0E=F, F^1E=0; this reverses the two literal printed extreme indices.')
add(71,[76],'dépend ... fonctoriellement ... commute aux changements de base quelconques',
 'For the relative complex analytic groups in the preceding lattice dictionary, the lattice-to-Lie sequence0→F→E→Lie(A) is functorial. When the lattice spans the Lie fibers and is locally constant, it is a short exact sequence of locally free modules and has the stated base-change compatibility. The preceding more general assertion concerns the analytic group construction, not arbitrary kernels of an arbitrary nonflat sheaf map.',
 'stated without proof','A','Direct own published counterpart SGA7 IX13.4.2–6 printed494,1972. This exact analytic statement is separate from the manuscript’s later Γ_k(T)-linear universal quasi-isomorphism question C065; similarity of the words “base change” does not identify them.',['SGA7IX1972'],G,
 'Locally split short exact sequences commute with ordinary base change; the non-locally-constant lattice regime is carried as the published analytic construction, not re-proved.',loc=loc('A',[46],'1422-1446'),confidence='medium')
add(72,[71],'accouplement ... séparant ... indépendant de la polarisation',
 'In the semistable abelian-variety setup of IX10.4, rational nondegeneracy of the monodromy pairing is independent of the chosen polarization and can be checked on one ℓ-adic realization with ℓ≠p using IX9.2. The following section decomposes the finite étale component group into its prime-primary summands.',
 'proof sketched','A','Exact own published counterpart SGA7 IX, end10.4 and11.0, printed448,1972. This is a deduction in the earlier monodromy theory. It neither introduces a new PD de Rham pairing nor independently proves the deeper integral positivity/duality theorem10.4.',['SGA7IX1972'],G,
 'Linear-algebra reduction through an isogeny and finite-primary decomposition checked; the donor invokes9.2 for geometric input.',loc=loc('B',[55],'366-388'))
add(73,[71],'Lemme11.6.8 ... étale ... immersion ouverte',
 'Under the semistable Néron-model hypotheses, for n a power of a fixed prime ℓ the quotient of n-torsion by its fixed part is flat, separated and quasi-finite, with the indicated constant finite generic fiber. Its special fiber is the corresponding component-group torsion, hence étale. Normality extends the generic map to the finite constant target; trivial generic kernel and separated étale uniqueness make the extension an open immersion.',
 'proved there','A','Exact own published counterpart SGA7 IX11.6.4–9, printed457–458,1972; uses SGA3 VI_A3.2/VI_B9.2 for the quotient and EGA IV17.9.1 for an étale monomorphism. These source citations were checked through the published argument; the complete SGA3 quotient theorem was not independently re-proved.',['SGA7IX1972','EGAIV4'],G,
 'Generic-fiber identification, special-fiber étaleness, and kernel argument audited as separate steps; hypotheses retained.',loc=loc('B',[71,73],'1065-1087,1140-1158'))
add(74,[71],'N extension ... tore ... groupe unipotent connexe',
 'For a proper reduced curve over an algebraically closed field, normalization induces a surjection on identity Picard schemes whose connected linear kernel is an extension of a torus by a connected unipotent group. Its toric character/cocharacter lattices are computed from branch incidence as in12.3.3–6. The nodal case has no unipotent part.',
 'proof sketched','A','Exact own published counterpart SGA7 IX12.3.1–6, printed470–471,1972, with the local-unit calculation cited to EGA IV21.8.5. The general branch-incidence formula remains meaningful without restricting to the simpler dual graph for ordinary double points.',['SGA7IX1972','EGAIV4'],G,
 'Character lattice is the kernel of the branch-incidence map to the singular-point and component vertices; a finite nodal example is checked in early_sga_graph_output.json.',loc=loc('B',[61,59],'594-609,541-559'))
add(75,[71],'M≃H₁(Γ(C),Z); Ker(Z^(K)→Z^(I×J))',
 'For a curve with at most two branches at each singular point, the toric character lattice is H₁ of the usual dual graph, and its dual is H¹. The displayed intermediate incidence target Z^(I×J), taken literally, is false: it must be the direct sum Z^I⊕Z^J. The two-branch scope is inherited from12.3.5; for arbitrary multiple branches one uses the bipartite incidence graph rather than all pairwise edges.',
 'false as stated','A','SGA7 IX12.3.7–14, printed472–473,1972, contains the same product-target defect, confirmed on original PDF477. Its map v₀(C_i)=(0,C_i) exposes the intended direct sum. The corrected graph theorem is the standard own published calculation; this is not an alleged new counterexample to Picard theory.',['SGA7IX1972'],G,
 'Triangle of three rational components and three nodes: product target has kernel rank0, bipartite incidence has kernel rank1. Exact matrices/ranks in programs/early_sga_graph.py and logs/early_sga_graph_output.json; full explanation in proofs.md §13.',
 loc=loc('B',[57,59],'480-507,541-559'),reconstruction='Replace only in the mathematical reconstruction I×J by I⊔J; the transcription remains unchanged.')
add(76,[71],'Q=P/E ... néronien; P⁰≃A⁰',
 'Let S be a strictly local trait and f:X→S proper flat of relative dimension1, with f_*O_X=O_S and every local ring of X factorial. Assume d^t=1 in the multiplicity notation of IX12.1.2 (the gcd of multiplicities after their radicial factors); this is the explicit hypothesis of12.1(b), stronger than merely citing cohomological flatness without qualification. Quotienting the relative Picard functor P by the closure E of the identity then yields a smooth separated Néron group Q. With geometrically integral generic fiber its degree-zero finite-type subgroup A is the Néron model of the generic Picard variety, and P⁰≅A⁰. Smooth generic fiber and a degree-one zero-cycle give the sufficient case12.1.11.',
 'stated without proof','A','Exact own published counterpart SGA7 IX12.1.6–12, printed467–468,1972, explicitly based on Raynaud’s Picard theory. The supplied excerpt starts in the middle of the hypotheses; full published12.1 is used to bound the statement. A general singular or nonregular family is not licensed by the fragment.',['SGA7IX1972'],G,
 'Hypotheses/source comparison, not an independent proof of representability or the Néron mapping property. Original printed465–468 read; d^t=1 in12.1(b) visually checked at PDF471.',loc=loc('B',[63],'688-710'),confidence='high')
add(77,[71],'B=A^natural/T ... unique structure d’extension',
 'Near a base point of the analytic family in IX13.3, a chosen torus in the special fiber extends to a closed relative torus subgroup. The quotient B is smooth separated with connected fibers; when its special fiber is abeloid, it is relatively abeloid nearby. A specified torus-by-abeloid extension on that fiber extends uniquely to the stated local analytic extension, in the paper’s lattice dictionary.',
 'proof sketched','A','Exact own published counterpart SGA7 IX13.3.9–16, printed492–493,1972. The uniqueness concerns the extension induced by that chosen lattice/torus data and shrinking neighborhood, not all abstract degenerations with the same special fiber.',['SGA7IX1972'],G,
 'Lattice quotient and openness argument followed through the published13.1.5 reference; carried as the earlier analytic theorem.',loc=loc('B',[90,92],'1972-1994,2058-2093'),confidence='medium')
add(78,[26],'résultats partiels négatifs ... auto multiplicatifs ... rien d’intéressant',
 'The lecture outline reports partial negative results for the specific attempt to obtain Steenrod/Whitney-type operations using multiplicative automorphisms of the universal simplicial PD de Rham object. This is not a prohibition of higher operations on a richer structure, and “négatifs” describes the outcome rather than a cohomological degree.',
 'stated without proof','C','Cartan–Miller higher operations, especially Cenkl1989, develop a different higher-product route; later E∞ and binomial reconstructions use different targets. The exact automorphism classification is developed on later manuscript pages and is not proved by the outline. No exact external classification for this restricted object was located.',['Cartan1976','Cenkl1989','Mandell2006','Horel2024'],S+H,
 'Scope check against the literal outline; no numerical or proof claim.',loc=loc('A',[14],'297'),confidence='medium')

add(79,[80],'Mais c’est ... faux déjà pour M=0',
 'The cancelled construction on scan48 is explicitly rejected by the author at M=0. The surviving transcription does not identify its precise long-exact-sequence or splitting assertion well enough to state and test a theorem.',
 'corrected by himself later','F','The density/coinduction and integration literature was searched around the surrounding construction, but no source identifies the illegible cancelled proposition. Preserve the authorial withdrawal within the same leaf and do not manufacture an exact external fate or a counterexample to an unspecified assertion.',['Cartan1976','Stacks2026'],S+T,
 'No fully typed computation is possible for this specific rejected target; neighbouring valid density and integration statements are C048–C050.',loc=loc('B',[48],'35-79'),confidence='high')

add(80,[23],'compatible ... puissances divisées ... cohomologie',
 'In the stipulated differential PD algebra, dγ_n(x)=γ_(n−1)(x)dx makes γ_n(x) a cocycle for every even cocycle x in the PD ideal. This alone does not show that the cohomology class of γ_n(x) is independent of the representative; descent needs an additional boundary compatibility hypothesis.',
 'proof sketched','E','The differential PD identity is standard before these notes (Roby’s free divided-power algebra and the crystalline de Rham tradition). Cartan’s weighted product theorem does not identify unrestricted cohomological PD operations. The exact boundary condition must be checked when forming the author’s stronger cohomological invariant.',['Roby1963','Cartan1976','Stacks2026'],S+['other_primary_open'],
 'Direct substitution of dx=0 proves the cocycle assertion. The CP² counterexample in proofs.md §11 refutes an unrestricted ordinary integral cohomology-ring reading, not this differential identity.')
add(81,[46],'idéal à p.d. engendré ... deleted; S^+(N)',
 'The divided-power ideal generated by T^[N] is replaced in the text by the full graded tail S^+(N). These differ in general: in Γ_F₂(T), the ideal with divided powers generated by T^[3] has no degree4 element, whereas the tail contains T^[4].',
 'corrected by himself later','E','The correction follows from the standard homogeneous divided-power algebra and is verified directly. Lucas arithmetic explains the zero coefficient in characteristic2; no separate later published theorem is required.',['Roby1963','Lucas1878','Stacks2026'],A+M,
 'T^[1]T^[3]=4T^[4]=0 over F₂, while every higher divided power of T^[3] has weight≥6. Exact small counterexample recorded in early_computations_output.json.',loc=loc('A',[23],'589-591'))

# Update after independently checking both the earlier restricted proof and
# late/proofs.md section5, with a second independent review by root.
for c in claims:
 if c['id']=='SA08-C035':
  c['fate'] += ' The exact arbitrary-base nonnegative theorem is proved in this run: the coefficient functor i(M)=M⊗Γ_k(T) has an exact left adjoint L, whose prime-local presentation is a filtered colimit of degree evaluations at ℓ^r−1. Thus i preserves injectives; the finite-cutoff adjunction and the binomial unit give R^nρτi(M)=0 for n>0. This proof is in work/late/proofs.md §5 and independently checked by early and root. It establishes the manuscript corollary without claiming novelty or identifying a published exact match. The earlier F_p-algebra and rational proofs in work/root/tail_ext_restricted_proof.md remain valid partial checks. The corresponding unrestricted abstract categorical inference is false; its special PD repair is essential.'
  c['present_status']=c['fate']
  c['computation'] += ' The arbitrary-base proof is structural, not a finite experiment: L(P)=(⊕P_n)/([T^[m]x]_(n+m)−binom(n+m,n)[x]_n), and L(P)_(ℓ)=colim_r P_(ℓ^r−1),(ℓ) with unit-normalized transition maps. The former restricted Frobenius/telescope proof was also checked; root_tail_ext_checks.json verifies its finite coefficients.'
  c['confidence']='high'

(O/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'claims':len(claims),'range':[claims[0]['id'],claims[-1]['id']],'all_have_search_logs':all(c['search_logs'] for c in claims)},indent=2))

