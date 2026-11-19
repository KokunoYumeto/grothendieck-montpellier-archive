"""Manually reasoned item records; source indexing and serialization only are automatic."""
from pathlib import Path
import csv,json,datetime
P=Path(__file__).parent
SRC=json.loads((P/'source_entries.json').read_text())
items=[]; verdicts={}
FILE='SA07_texts/pro/MPL_18_018-062_transcription.tex'
def A(n,kind,scans,lines,quote,statement,reconstruction,check,reason,verdict='kept'):
    ident=f'SA07-{400+n}'
    items.append(dict(id=ident,sources=[SRC[n-1]['entry_id']],kind=kind,cote='18',scans=scans,lines=[FILE+':'+lines],his_words=quote,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))
    verdicts[n]=(ident,verdict,reason)
def M(n,to,reason,verdict='merged'):
    ident=f'SA07-{400+to}'
    next(i for i in items if i['id']==ident)['sources'].append(SRC[n-1]['entry_id'])
    verdicts[n]=(ident,verdict,reason)

A(1,'unproved claim',[19,21],'14–31;55–74','P_sigma^(p)=(1/sigma(2iπ))^p P_alg',
  'For a smooth variety X over a field k isomorphic to C and a chosen isomorphism sigma:C→k, the codimension-p cycle class in the transported Betti lattice is sigma(2πi)^(-p) times the algebraic de Rham cycle class, with the manuscript orientation and residue convention.',
  'Modern comparison terminology and explicit hypothesis p≥0 are editorial; the scalar itself is written. Torsion integral cohomology is understood through its image in complex cohomology, so it is a lattice only modulo torsion.',
  'agrees','The factor is explicitly written at L25 and the analytic direct-image warning at L69. The earlier-run global/local comparison is supported, subject to trace and orientation conventions.')
A(2,'reading question',[19],'23–31','change P_sigma^(p) en -P_sigma^(p)',
  'Changing the complex orientation changes (2πi)^(-p) by (-1)^p. The final minus sign and omitted exponent in the following lattice formula are correct in the immediately preceding example p=1, but not as uniform formulas for arbitrary p.',
  'The parity test is the earlier run’s calculation, rechecked here; a restricted p=1 scope is a possible interpretation, not a changed reading.',
  'agrees','The source explicitly moves from general p to p=1, X=P^1, then prints a minus sign. The ambiguity is scope, and no ink emendation is licensed.')
A(3,'reading question',[21],'55–74','upper-left arrow labelled unsure{?}',
  'The support-to-ordinary-cohomology arrow in the first diagram may carry an authorial question mark. For a regular codimension-p embedding, a modern purity comparison requires a cohomological shift 2p and a Tate twist.',
  'The shifted purity formulation is ours. The doubtful mark alone does not establish an authorial doubt about the entire theorem.',
  'agrees','The uncertain mark occurs on one arrow at L58; the diagram is reduced to a coefficient-level square at L63–66.')
A(4,'unproved claim',[23],'98–106','morphisme propre quelconque',
  'For a proper holomorphic map f:X→Y between smooth complex manifolds of pure relative codimension p=dimY−dimX, the comparison transports the topological Gysin map in degree q to (2πi)^(-p) times the manuscript analytic direct image in degree q+2p.',
  'The page displays even degree 2i; extending to all q is a modern reconstruction. Both trace normalizations must be specified; the factor cannot identify every modern duality convention without its signs.',
  'agrees','The boxed square contains 2i+2p and the scalar, but the extension is announced without its trace/composition proof.')
A(5,'unproved claim',[25,27],'128–161;186–199','Cet isom ... fonctoriel',
  'For smooth projective X,Y, a correspondence z of codimension r on X×Y acts by a↦pY*(pX*(a)∪cl(z)); in modern cohomological notation it maps H^i(X) to H^(i+2r−2dimX)(Y)(r−dimX). With compatible cycle and trace conventions the Betti/de Rham comparison commutes with this action.',
  'The general degree and Tate twist are editorial. The manuscript uses X^n and degree-zero correspondences and contains uncertain n/m exponents and an Omega_X at the Y target.',
  'agrees','The push-pull formula is inserted at L135 and the scalar comparison is attempted at L149–158. This is an operator-level bridge, not a complete construction of a category of motives.')
A(6,'unpursued implication',[27,29],'186–199;231–239','une des racines de -1',
  'For a topological field K≅C, an orientation of P^1_K selects a generator u of its integral degree-two Betti line and α∞(u)=(2πi)^(-1)v for the algebraic generator v. Reversing i reverses u and leaves its rank-one image lattice unchanged.',
  'Only the interpretation as a Tate comparison line is modernized; the factor and orientation choices are explicit.',
  'agrees','The two choices are explained at L199 and the exact scalar at L233; the note preserves the distinction between generator and lattice.')
A(7,'reading question',[29],'231–239','tous les éléments primitifs|possibles',
  'The set obtained by varying complete archimedean topologies must be specified before “primitive” makes sense in the one-dimensional K-space H^1(P^1,Omega^1). No fixed integral lattice is supplied in that sentence.',
  'This is a reading/quantifier alarm, not a proposal to replace the word by “possible”.',
  'agrees','L237 retains both readings. Neither the preceding formula nor the vector-space dimension defines an ambient integral primitivity condition.')
A(8,'unproved claim',[29,33,37],'239;292;399–423','stable par ce groupe Z/2Z',
  'For a motive over R with compatible integral Betti, finite-prime and complex de Rham realizations, the diagonal comparison image of the Betti lattice is stable under complex conjugation, acting geometrically at finite places and semilinearly in de Rham cohomology.',
  'An integral motivic category and torsion conventions remain unspecified; the realization-level statement for cohomology modulo torsion is the precise reconstruction.',
  'agrees','The stability is explicit at L239 and is explained by the two commuting conjugations later. It is stronger data than a bare rational comparison.')
A(9,'unproved claim',[32,33,39,40,41],'274–290;471–495;499–559','ne dépend pas de π',
  'For a fixed topological field K≅C and smooth projective X/K, the Betti real form and the Hodge filtration determine H^(p,q)=F^p∩conjugate(F^q) in degree p+q. Transport through either of the two continuous isomorphisms K≅C gives the same K-linear splitting when coefficient conjugation and the conjugate variety are both tracked. Varying the topology itself is a different question.',
  'H^(p,q) via opposed filtrations and the total degree are modern explicit reconstruction. The unqualified earlier source phrase “cohomologie de Hodge” is read here through its local de Rham notation.',
  'agrees','L283,288 and L471–495 concern a fixed topology; L533 onward separately varies T. The notes correctly resist conflating these quantifiers.')
A(10,'unproved claim',[33,35,37],'292;340–357;399–423','sigma et tau commutent',
  'For M/R, write V=H_B(M,Q), σ for coefficient conjugation on V_C, and f∞ for geometric conjugation on V. Then τ=f∞σ=σf∞ is the de Rham descent conjugation, and its real fixed space is V_R^+⊕iV_R^−.',
  'The explicit eigenspace calculation is the earlier run’s expansion of the manuscript formula. No real model is inferred from the mere Betti real form of a complex variety.',
  'agrees','L292 supplies the geometric explanation; L340 writes the fixed-vector equation; L408–415 states the product and torsor.')
A(11,'conjecture',[34,37],'298–331;415–423','pleinement fidèle en vertu des conj. de Hodge',
  'The Hodge realization of a real motive carries a rational involution f∞ exchanging Hodge bidegrees, so f∞j(z)f∞^(-1)=j(conjugate z). For homological pure motives, full faithfulness into Hodge structures with this real descent datum follows if the relevant rational Hodge classes on products are algebraic (and real descent of correspondences is imposed).',
  'The exact motivic category and product-level Hodge hypothesis are supplied in the modern conditional reconstruction. The compatibility equation itself does not prove fullness.',
  'agrees','The normalizer identity appears at L321–327 and L421; fullness is explicitly conditional at L329. “Order 2” must allow f∞=1 on some objects.')
A(12,'idea of the earlier run',[35],'340–359','n’est pas compatible avec le produit tensoriel',
  'For Q-spaces with rational involution f, W(V)=V^+⊕iV^−⊂V_C defines a tensor functor via ambient multiplication. The natural additive isomorphism a_V(v++v−)=v++iv− has tensor defect −1 exactly on V^−⊗U^−.',
  'The four-summand tensor calculation is earlier-run work rechecked here; Grothendieck states “Oui” for W and rejects tensor compatibility of the displayed additive map.',
  'agrees','L344 answers W’s tensor question affirmatively; L357 separately denies tensor compatibility for a_V. The two statements concern different maps.')
A(13,'idea of the earlier run',[35,37],'357–359;413–415','Il semble ... pas tensor-isom',
  'On the rational Artin category over R, let A be the sign line with A⊗A≅1 and f∞=-1. A tensor isomorphism from V to W would send a to qia, q∈Q×, forcing −q²=1. Thus no such tensor isomorphism exists on a category containing A. On the Tate-only category it does exist via e_n↦i^n e_n.',
  'This counterexample/proof is the earlier run’s explicit completion of the tentative author claim; the category restriction is essential.',
  'agrees','L359 is tentative and unspecified in scope. The sign-Artin calculation proves the whole-real-category version and the Tate test prevents an overgeneralized restriction.')
A(14,'reading question',[35,40],'347–357;512–526','H^{*|0}(X(R),Q)=V^f',
  'Usual real points are the fixed locus, not the orbit space. For X=P^1_R, H^1(X(C),Q)^f=0 whereas H^1(X(R),Q)=Q; for X=Spec C/R, real points are empty but Betti H^0 invariants are Q. Rational cohomology of X(C)/conjugation is the invariant part under the usual finite-group triangulable-action hypotheses.',
  'Both explicit tests are earlier-run mathematics, rechecked; the interpretation of X(R) in the unclear diagram remains undecided.',
  'agrees','The ambiguous *|0 superscript at L352 cannot rescue the usual fixed-point reading in both examples; L522 explicitly uses the quotient space instead.')
A(15,'idea of the earlier run',[36,37],'364–382;413–415','bar(alpha)=f_infty alpha',
  'For the comparison torsor P with specified point α∈P(C), the equality conjugate(α)=f∞α implies α is real iff f∞=1. This is not equivalent to P having some real point: the Tate Gm torsor is trivial over R since −1=i^(-1)conjugate(i), while its distinguished Tate comparison point is imaginary.',
  'The coboundary example is earlier-run analysis. The written equivalence concerns a specified point, not the torsor class alone.',
  'agrees','L364–381 states the point criterion and its Tate obstruction; it never replaces it by existence of another real point.')
A(16,'idea of the earlier run',[36,38],'383–393;441','somme de puissances tensorielles de Q(2)',
  'The live assertion that f∞=1 forces a motive to be generated by even Tate twists fails in the rational Artin–Tate category: A is the sign summand of h^0(Spec C/R), T=Q(-1), and L=A⊗T has f∞=+1 and weight 2. L is cut out algebraically in h^2(P^1_C/R), while tensors and summands of Q(2) have weights in 4Z.',
  'The counterexample belongs to earlier-run/Hua leads and is independently reconstructed here using algebraic projectors. Its relevant Hodge classes are all algebraic, so the manuscript’s Hodge-conjecture premise holds in the example.',
  'agrees','The note correctly distinguishes the live claim at L388 and L441 from a separate deleted opening argument. No uncertainty about the centrality margin is used to erase this literal live statement.')
A(17,'idea of the earlier run',[36],'383–393','G≃G_m ou G≃{e}',
  'The abstract Tannaka group Gm alone does not specify f∞: <Q(-1)> has f∞=-1, while <A⊗Q(-1)> has f∞=+1. Their generating characters t and at of μ2×Gm send the same (-1,-1) to different scalars.',
  'This earlier-run counterexample targets the displayed equivalence with an abstract group type. No assertion is made that the two categories are equivalent while preserving Tate data.',
  'agrees','The vertical equivalence at L389 omits the distinguished element. The comparison tests exactly that omission.')
A(18,'reading question',[36],'393','Q tordu ... comm.',
  'The centrality claim cannot be evaluated without identifying “Q tordu” and the intended Tate character. The ordinary Tate category already has a commutative group and central nontrivial real Frobenius.',
  'The Tate test restricts admissible reconstructions but does not select a reading of the margin.',
  'agrees','The words tordu and comm. are uncertain and the generator is not defined locally. The note appropriately leaves this in the scan-check queue.')
A(19,'withdrawn in the same text',[38],'445–465','compact maximal',
  'The normalizer/maximal-compact argument is wholly deleted. Within the deleted layer the author passes from G to G/i(Gm); only the live Hodge-torus conjugation formula elsewhere survives as an asserted identity.',
  'No theorem about maximal compact subgroups is reconstructed from the cancelled paragraph.',
  'agrees','The outer deleted block encloses L445–465, including a nested deletion and the scalar quotient. The earlier note correctly confines withdrawal to this paragraph.')
M(20,9,'The real form at 18/039 L484 and real-descent comparison at 18/040 L512–526 are the same fixed-topology construction underlying item SA07-409; the explicit distinction from a real model is retained there.')
A(21,'reading question',[40,41],'529–555','H^{p,q}(X) subset F^p H^q(X)',
  'With source H^q(X,Omega^p), the Hodge summand belongs in total cohomological degree p+q. The displayed H^q target can be correct only if q has been silently repurposed as total degree.',
  'The proposed total-degree p+q is a mathematical alternative, not an emendation.',
  'agrees','The boxed definition at L531 and repeat L546 retain q; the preceding direct sum over p,q gives the degree mismatch.')
A(22,'idea of the earlier run',[41],'553–561','K_r ... plus gd sous-corps tot. réel',
  'If K admits an embedding into C and T runs over all archimedean topologies induced by embeddings, then intersection_T(K∩R in Khat_T) equals the subfield of elements algebraic over Q whose every conjugate is real. A transcendental element can be sent to a nonreal transcendental value and the embedding extended across a transcendence basis.',
  'The quantifier over all embeddings and the field-extension proof are explicit reconstruction; the source asserts the intersection and algebraicity without proof.',
  'agrees','L559–561 gives the claimed characterization. The proof requires all archimedean places, not only a fixed family.')
A(23,'self-flagged step',[43],'571–591','comparaison possible ... ?; Définition ... ?',
  'The programme asks (1) Betti versus de Rham lattices and real splittings, (2) Betti versus ℓ-adic lattices as the archimedean topology varies, (3) a p-adic/de Rham comparison over a complete discretely valued field of residue characteristic p, and (4) a p-adic cohomology theory in characteristic p. Items (3) and (4) are distinct questions.',
  'Smoothness/properness and comparison period rings are modern refinements used in separate problem records, not supplied by this list itself.',
  'agrees','The four numbered lines are present. Oda’s degree-one theorem is only a special abelian result; modern crystalline and p-adic comparison theories must be researched separately.')
A(24,'unpursued implication',[43],'589–591','Définition de cohomologie p-adique en car p>0 ?',
  'For an abelian variety A over a perfect field of characteristic p, Oda’s M(A[p])≅H^1_dR(A) identifies its V-submodule with H^0(A,Omega^1) and recovers the Hodge exact sequence; this addresses the earlier extension-recovery question at cote54/007, not every p-adic comparison on 18/043.',
  'Literature comparison from the earlier run. The specific theorem is absent from the manuscript and its attribution is to Grothendieck’s published 1966 paper.',
  'not on the page','18/043 only states the programme. The precise Oda result and historical attribution are verified separately; no priority date is inferred for these undated leaves.')
A(25,'idea of the earlier run',[34,37],'321–327;421–423','f_infty j(lambda) f_infty^-1=j(lambda prime)',
  'For a pure weight-n realization with a polarization morphism q:V⊗V→Q(-n) defined over R and Weil operator C, q(fx,fy)=(-1)^n q(x,y), fCf^-1=C^-1 and C²=(-1)^n imply B(fx,fy)=B(x,y) for B=(2πi)^n q(x,Cy).',
  'The pairing and sign cancellation are earlier-run work; a polarization is an additional datum, not produced by f∞.',
  'not on the page','The source supplies the normalizer identity. The positive-form calculation is a valid derived bridge with explicit extra hypothesis q/R.')
A(26,'unpursued implication',[34,37],'302–329;399–423','automorphisme ... x↦bar(x)',
  'For a smooth proper hyperbolic curve X/R, a section of π1(X)→Gal(C/R) acts by conjugation on geometric π1, and this action passes to abelianization and dual H^1 as real Frobenius. Conjugating a lift geometrically does not change the resulting action. This does not identify the full abelianized section cocycle.',
  'Earlier-run bridge to anabelian theory; the manuscript only defines the linear real involution. The section theorem is checked as external literature.',
  'not on the page','No arithmetic fundamental-group section appears at these lines. Retained only as an explicitly attributed project link and comparison.')
M(27,23,'The four-part programme is exactly 18/043 L575–591 already incorporated in SA07-423; earlier-note links and conjecture labels do not create an additional manuscript claim.')
A(28,'unproved claim',[45],'618–628','de dim 7; de dim 5',
  'Under the reconstructed premise that C,C′ are non-CM elliptic curves with no isogeny between them over C, the group displayed is isogenous to SL2×SL2×Gm (dimension 7), and the displayed Borel-type subgroup has dimension 2+2+1=5.',
  'The opening non-isogeny words are uncertain. Identifying K with coordinates in a Borel fibre is only a possible modern reconstruction, not determined by this leaf.',
  'agrees','The dimensions are explicit and recompute to 7 and 5. The notes correctly leave K and the first-line premise unresolved.')
A(29,'withdrawn in the same text',[45],'618–630','et non pas égal à dim G−1=6',
  'The author claims trdeg_k K≤5, writes an uncertain ≤5|4 over k(π), and rejects equality with dimG−1=6. This is a statement about this undefined K, not a refutation of full period genericity.',
  'Cross-reference to the earlier cancelled dimension-minus-one formula requires cote18/012, supplied elsewhere in this run. Chronological order of drafts is not inferred from scan order.',
  'agrees','The explicit numerical rejection is at L628. No identification with the full period field occurs locally.')
A(30,'unpursued implication',[47,49],'672–712;737','G opère diagonalement',
  'For n torsors P_i under the same smooth algebraic Q-group G of dimension d, their diagonal right quotient, after a common splitting field, is G^n/G≅G^(n−1), via (g1,...,gn)↦(g2g1^-1,...,gng1^-1). Hence its dimension is (n−1)d.',
  'The explicit quotient map and interpretation of transcendence degree componentwise are reconstruction. The adelic point is not a single ordinary field-valued point without further definition.',
  'agrees','L684–691 writes the torsors and action; the continuation at L737 states the numerical bound. The action is free after trivializing all torsors.')
A(31,'reading question',[47,49,51,55],'688;743–748;782–784;870','Qhat=product Q_l; A_f=product Z_l',
  'The full product of Q_l with product topology differs from the finite adele restricted product. For Ga it has no compact open subgroup: an open set leaves some full noncompact factor unconstrained. Product Z_l is compact open in finite adeles, but not open in the full product.',
  'This is a topology alarm, not an instruction to add a missing restricted-product prime to the ink. The scalar counterexample is ours/earlier run rechecked.',
  'agrees','The source simultaneously writes full products and compact-open language. Its exact ambient topology must be clarified before the generic-coset and approximation claims.')
A(32,'conjecture',[49,51],'737–748;782–784','conjecture de Tate renforcée ... indice fini',
  'The manuscript admits finite index of the adelic Galois image in G(Zhat), choosing G “géom.” and connected. In the usual faithful tensor-subcategory reconstruction without adjoining Q(1), M=Q(-2) gives G=Gm and cyclotomic-square image, of infinite index in product Z_l×. Thus connectedness alone is insufficient; modern adelic statements impose Hodge-maximality.',
  'The refutation concerns that precisely stated natural reconstruction; the undefined “géom.” integral model and any compulsory adjoining of Tate objects could change it. The actual page remains a conjectural input.',
  'understates','The prior note correctly reports finite index but does not flag its failure for arbitrary tensor generators. This run adds the Q(-2) test and the exact Hodge-maximality refinement.','corrected')
A(33,'self-flagged step',[49,51],'743–748;774;782','si on admet ceci',
  'For a connected affine Q-group G and a nonempty open subset of G(A_f) in the usual restricted-product topology, there is a point whose component at every prime is Q-generic in G. This follows by Baire avoidance of the countably many rational proper closed subsets in each local analytic chart; the page assumes a compact-open coset.',
  'The restricted-product topology and local smoothness/analytic-density argument are a modern repaired formulation. The full-product notation is not silently changed.',
  'agrees','The lemma is explicitly admitted at L740–748 and invoked twice on 18/051. The notes’ scalar test is weaker than the general proof supplied in this consolidation.')
A(34,'idea of the earlier run',[49],'743–748','toutes les composantes sont génériques rel./Q',
  'For Gm in product Z_l×, any nonempty open coset contains a tuple with each coordinate transcendental over Q: choose in each finitely prescribed local ball an element outside the countable algebraic closure of Q, then choose arbitrary transcendental units at other primes.',
  'The scalar construction is earlier-run work; it checks a compact integral-product variant, not the manuscript’s unspecified full-product topology.',
  'not on the page','The source admits the general lemma; it contains no scalar construction. The example is retained with its own topology and provenance.')
A(35,'idea of the earlier run',[51,50],'776–784;758–760','si on suppose ... condition d’approximation',
  'Q× is not dense in the finite idele group: Q×∩product Z_l×={±1}, while units with 5-adic residue 2 form a nonempty open set missing both. Connectedness does not imply strong approximation. The manuscript’s density hypothesis must remain separate from its genericity lemma.',
  'This is the earlier run’s counterexample to automatic approximation, not a refutation of the source’s explicitly conditional implication.',
  'not on the page','L776–780 imposes approximation. The adjacent reused SL_n proof is a genuine special case and cannot remove the hypothesis for Gm.')
A(36,'reading question',[51],'780','dépend de M; il est probable ... est|pas',
  'Galois changes of archimedean place giving commensurability may depend on the motive M. The next expectation about recovering a place from the full fibre functor is undecidable from the est|pas transcription.',
  'Earlier cote15 withdrawals of bare-functor separation and proposals with Hodge enrichment are comparisons, not a resolution of this word.',
  'agrees','Both dependence on M and the uncertain polarity are explicit at L780. The note correctly refuses a confident separation assertion.')
A(37,'unproved claim',[51],'774–784','Moyennant ... le lemme et ... approximation ... équivaut',
  'Conditional on a specified integral model, finite-index Galois image, the generic-coset lemma and strong approximation, the page sketches Galois modifications producing generic relative positions or commensurable lattices. Its claimed equivalence with “independence” is not mathematically determinate until independence and the reverse direction are defined.',
  'The forward coset argument can be reconstructed; no converse is filled in. The unconditional finite-index input requires the refinement in SA07-432.',
  'agrees','The inserted margin retains both auxiliary inputs. The body proves neither the named image conjecture nor a fully quantified converse.')
A(38,'unpursued implication',[53,61],'815–834;1035','k ... pas alg. sur k0 ... transc. infini',
  'For algebraically closed k≅C and finitely generated k0⊂k, restriction Aut(k/k0)→Gal(k0bar/k0) is surjective with kernel Aut(k/k0bar). The full group is not an absolute profinite Galois group; in its pointwise topology a transcendental stabilizer has infinite index. The finite-prime representations factor through the algebraic quotient whereas the archimedean semilinear action may see the kernel.',
  'Surjectivity and noncompactness are modern field-theoretic proofs. The notation Gal on these pages must not silently import profinite hypotheses.',
  'agrees','The margin at L818 explicitly insists on transcendental k/k0; L1035 identifies the geometric kernel. The earlier note preserves this distinction.')
A(39,'unproved claim',[55,57],'867–881;926–939','g ... mod ... G(Z); bien déterminé',
  'For specified integral tensor fibre functors on <M>, the page asserts their comparison by g in product G(Z_l)×G(C), unique modulo diagonal G(Z). If this existence assertion holds in a faithful lattice model, fixing all finite Galois components kills diagonal ambiguity because Z→Z_l is injective, and hence determines the archimedean component.',
  'The uniqueness argument is valid conditional on existence and faithful integral representations. Integral isomorphism of arbitrary fibre functors is not furnished by rational Tannakian reconstruction.',
  'agrees','The existence assertion is written at L875–879, with uncertain “On vérifie|On considère”; L930 asserts uniqueness after fixing finite components.')
A(40,'withdrawn in the same text',[55,57],'890–900;926–935','les fibres sont de card. 2 (conj. complexe)',
  'For the orbit of a complete complex place v under Γ=Aut(k/k0), the stabilizer is Γ∩{1,c_v}; its size is 2 exactly when c_v fixes k0 and otherwise 1. The universal cardinal-two statement and following quotient construction are deleted.',
  'The stabilizer computation is the earlier run’s reconstruction using continuity of isometries of C. Its target is the orbit, not every conceivable noncomplete place.',
  'agrees','The boxed note and map are enclosed in deletions at L890–900; the normalized archimedean map on scan57 is a later live construction.')
A(41,'unpursued implication',[57,59],'942–971','posant psi_v=phi_v^-1',
  'The written right-cocycle law φ(τσ)={}^τφ(σ)φ(τ) becomes the usual left-cocycle law ψ(τσ)=ψ(τ){}^τψ(σ) after pointwise inversion ψ=φ^-1.',
  'This is a direct noncommutative algebra check; it does not prove effectiveness of the subsequent transcendental descent.',
  'agrees','L944 and L948 explicitly record both orders. The uncertain ψ|φ opening at L971 matters to the convention.')
A(42,'self-flagged step',[59],'970–978','À vérifier / OK',
  'Given a neutral Tannakian category with specified Betti and de Rham tensor fibre functors over k0, Isom^⊗(ωdR,ωB⊗k0) is an affine torsor and its comparison trivializes it over k. The automorphism-indexed cocycle on a transcendental extension must arise from this torsor or from a genuine fpqc datum over k⊗k0 k before effectiveness is asserted.',
  'The Tannakian hypotheses and distinction between arbitrary group-action data and fpqc descent are modern reconstruction. The author’s OK is evidence of his check, not a proof supplied to the reader.',
  'agrees','The torsor and isomorphism-functor description occur at L971–973; the margin records both checking request and OK at L974.')
A(43,'conjecture',[59,61],'976–980;1020–1027','conjecture de transcendance N°1 ... générique',
  'The comparison point of the Betti/de Rham torsor is conjectured generic over its definition field k0; the page reformulates this as Zariski density of the actual image of the corrected automorphism-indexed map. For classical pure motives over an algebraic number field this is the period-genericity conjecture, conditional on the chosen motivic category.',
  'The distinction between k0-generic and k-closed points, and between image and subgroup generated by it, is essential modern clarification. Genericity over arbitrary finitely generated k0 requires additional qualifications.',
  'agrees','The conjecture label and “image Zariski dense” are explicit. No calculation on scan61 proves arithmetic period genericity.')
A(44,'withdrawn in the same text',[61],'1020–1027','au lieu de g^-1 g^sigma',
  'For a k-point g of an algebraic group defined over k0, φ(σ)=({}^σg)^(-1)g satisfies the source’s right-cocycle law. The k-isomorphism x↦x^-1g carries the Aut(k/k0)-orbit of g to the image; its inverse is y↦gy^-1.',
  'The orbit/genericity equivalence additionally uses the largeness of k to extend coordinate-field isomorphisms, a modern field-theoretic argument. The later expression {}^σg g^-1 is related by inversion and conjugation, not equality.',
  'agrees','L1020 expressly replaces the old order and L1027 discusses orbit values. The note’s calculation matches the live correction.')
A(45,'idea of the earlier run',[53,59],'815;981','π transcendant sur k0...',
  'The minimum transcendence degree of a field of definition does not itself imply π is transcendental over it. The elliptic family y²=x³−3t/(t−1728)x−2t/(t−1728) has j=t; at t=π a curve-level minimal field has transcendence degree one and may contain π.',
  'The earlier run’s example is explicitly curve-level. Passing from minimal definition of a curve to that of its h^1 motive up to isogeny requires an additional descent argument; none is asserted here.',
  'not on the page','The unfinished margin is only a qualification; the j calculation is external analysis and does not settle its intended motivic formulation.')
A(46,'idea of the earlier run',[57,61],'944–948;1029–1035','l’hom total sigma↦sigma_*',
  'A left cocycle ψ yields a homomorphism σ↦(ψ(σ),σ) into G(k)⋊Aut(k/k0). It need not be a homomorphism into G(k) alone: for g=t, σ(t)=t+1, τ(t)=t+2, φ(τσ)=t/(t+3) differs from φ(τ)φ(σ)=t²/((t+2)(t+1)).',
  'The semidirect target and rational-function test are earlier-run reconstruction. They expose a missing convention in “hom total”, without refuting the tentative closure statement by themselves.',
  'not on the page','The cocycle law has an action term; the displayed adelic target of L1031 suppresses it. The note correctly distinguishes cocycle from group homomorphism.')
A(47,'conjecture',[61],'1033–1036','Il me semble ... un sous ... ouvert',
  'The author expects the closure of the combined finite-prime/archimedean image to be an open subgroup and says that the kernel of the finite part still has dense archimedean image. A precise modern formulation must specify the semidirect action, topology and integral image/maximality hypotheses.',
  'No exact published theorem is assigned to this ambiguous target. Zariski density of a period orbit and topological adelic openness are distinct.',
  'agrees','The openness is explicitly tentative, with a doubtful marginal question. The previous cocycle construction does not make it a proved homomorphism theorem.')
A(48,'unpursued implication',[62],'1040–1082','phi_w(sigma)=g_infty^sigma phi_v(sigma) g_infty^-1',
  'For M-equivalent places with Mw^Z=gMv^Z, the finite comparison component remains σ_l and the archimedean right cocycle changes by φ_w(σ)={}^σg∞ φ_v(σ)g∞^-1. After inversion, ψ_w(σ)=g∞ψ_v(σ){}^σg∞^-1, so the left-cocycle classes agree.',
  'The cohomology-class language is modern; actual descent remains subject to SA07-442. The deleted formula lacking a final inverse is not used.',
  'agrees','L1063 supplies finite cancellation and L1078 the boxed corrected law. All factors are retained in order.')
A(49,'other',[47,53,55,57,59,61,62],'672–712;815–834;867–900;926–980;1020–1082','bien déterminé; psi=phi^-1; Il me semble',
  'The earlier-run Hua synopsis is supported only as a lattice→normalized comparison→cocycle→torsor chain. Its missing conventions include diagonal G(Z), the inverse left-cocycle convention, the transcendental automorphism group, and the conjectural status of genericity/openness.',
  'The external Hua register itself is not supplied in this part; this audit checks the synopsis quoted by the indexed note, not any unseen completion.',
  'agrees','All qualified steps occur in the transcript. The note correctly refuses to certify the truncated ending; project status stays a lead.')
A(50,'unpursued implication',[59],'971–980','isom de foncteurs ... ce point générique',
  'The earlier-run comparison to Bost–Charles identifies the genericity language with the modern torsor statement only after the motivic category, base field, and cycle/tensor conventions are fixed. De Rham–Betti cycle fullness is a distinct, generally weaker assertion.',
  'This is a literature comparison. The modern theorem/ conjecture numbering is not manuscript text.',
  'not on the page','The source’s generic-point wording is clear; modern inclusions and conjectures require independent source verification and are not a historical category identification.')
A(51,'unpursued implication',[45,59],'628;976–980','conjecture de transcendance',
  'Grothendieck’s 1966 de Rham paper, note 10, provides a printed elliptic period/quasiperiod conjectural witness; 18/059 adds the torsor-generic-point formulation. The source paper is a 14 October 1963 letter with most added notes dated November 1963.',
  'Bibliographic comparison; the publication/circulation dates are obtained from the opened primary source, not from the undated archive leaves.',
  'not on the page','The manuscript labels a conjecture but does not cite that paper locally. The historical link is retained with both endpoints verified.')
A(52,'idea of the earlier run',[59,61],'980;1020–1027','image Zariski dense',
  'For G=Gm, k0=Q, k=C and g=1+√2, the actual coboundary image is {1,−3−2√2}, hence not Zariski dense, while the subgroup it generates is infinite and therefore Zariski dense in Gm. Image-density and generated-subgroup-density are inequivalent.',
  'Earlier-run counterexample, rechecked algebraically; this does not assert g is a generic period point.',
  'agrees','The exact word “image” at L980 is preserved. The example supplies a valid test against a stronger paraphrase found in previous notes.')

M(53,5,'MB01 repeats the explicit correspondence push-pull bridge on 18/025 L133–161; the modern degree/twist formula and absence of a full historical category construction are already retained in SA07-405.')
A(54,'unpursued implication',[37,55],'399;877–879','G=Aut_tensor(T_B); motifs subordonnés à M',
  'For a neutral Q-linear rigid abelian tensor category C=<M> with an exact faithful tensor functor ω, naturality forces g_N′ω(a)=ω(a)g_N for every morphism a:N→N′ and g∈Aut^⊗(ω); neutral Tannakian reconstruction identifies C with Rep_Q(G).',
  'The category axioms and reconstruction theorem are modern. The manuscript uses the generated category and automorphism notation without defining all its morphisms or integral structures.',
  'agrees','Both endpoint formulas occur at L399 and L879. The earlier-run comparison correctly does not identify the historical category with a particular modern construction.')
A(55,'idea of the earlier run',[27],'197–199','xi(Z(-1))',
  'On a rational Lefschetz string v_j=L^jv, 0≤j≤m, set E v_j=v_(j+1), Λv_j=v_(j−1), Fv_j=j(m−j+1)v_(j−1), Hv_j=(2j−m)v_j. Then [E,F]=H, [H,E]=2E, [H,F]=−2F, and F and Λ are converted by the displayed rational coefficients.',
  'Earlier-run operator computation based on cote16/013–014; 18/027 supplies only the P^1 Tate test object. The conversion is rational and does not identify unit-step Λ with the source’s integral contraction.',
  'not on the page','The cited p18 line is only a realization object. Reading cote16/013–015 L440–583, with second-pass clarification of the contraction convention, supports a separate abstract rational model.')
A(56,'idea of the earlier run',[27],'197–199','xi(Z(-1))',
  'For W=⊕_(m=0)^d V_m with one standard string of each length, B=1−EΛ and T=1−ΛE give B_m=BΛ^mTE^mB. E^b B_m Λ^a are matrix units, so Q[E,Λ]=∏Mat_(m+1)(Q). The sl2 Casimir H²+2H+4FE acts by m(m+2), and rational interpolation recovers the same images.',
  'Earlier-run proof for the explicitly specified model. Extra multiplicity spaces are acted on by identities. This neither proves an integral equality nor repairs the integral exterior contraction model of cote16.',
  'not on the page','The abstract matrix-unit computation is valid, but not written on 18/027. Current second-pass readings retain the erroneous 2n−i bound in cote16/015; this calculation uses 0≤a,b≤m.')
A(57,'idea of the earlier run',[27],'197–199','H^2(P^1)=Z(-1)',
  'On H*(P^1)=Qe0⊕Qe2, E sends e0 to e2 and F reverses it, whereas the Tate group acts by diag(1,z). The Lefschetz SL2 action cannot factor through that Tate representation because it moves the unit; nevertheless conjugation scales E by z, F by z^-1, and E:h^0→h^2(1) is equivariant.',
  'Earlier-run matrix test, not a manuscript identification of Lefschetz and motivic groups.',
  'not on the page','The Tate object is named at L197. The full matrices and obstruction are an explicitly labelled reconstruction and are verified in computation output.')
A(58,'idea of the earlier run',[27,34],'197–199;331','epsilon:G→G_m',
  'For smooth projective X of dimension d, cohomological grading w(t)|H^i=t^i and Lefschetz grading λ(t)|H^i=t^(i−d) differ by t^-d. Their conjugation on endomorphisms agrees. If ε is the character on Q(-1), then ε∘w=t², not t.',
  'Earlier-run convention calculation; the comparison to the section ε∘j=id on cote18/011 is external to this local p18 passage.',
  'not on the page','The source gives a Tate line and ε but no identity of the two grading cocharacters. The exponent calculation prevents a false identification.')
A(59,'idea of the earlier run',[45],'618–628','SL(2)×SL(2)×G_m',
  'For an elliptic curve E, the Lefschetz sl2 acts trivially on H^1(E), since L:H^1→H^3 and Λ:H^1→H^-1 vanish and the Cartan weight is zero. Its non-CM Mumford–Tate derived SL2 acts by the nontrivial standard representation on H^1.',
  'Earlier-run representation test; it distinguishes two actions without challenging the conditional product-group assertion for two nonisogenous non-CM elliptic curves.',
  'not on the page','The product group is written on scan45 but no equality with Lefschetz sl2 is asserted there. The notes correctly label the test as their own.')
A(60,'reading question',[25,27],'133–161;186–199','sur la catégorie des motifs',
  'The operational dictionary compares manuscript A with algebraic hard Lefschetz (printed A), manuscript C with algebraic inverse Lefschetz (printed B). The suggestions manuscript B→printed D and manuscript D→printed C remain inferences from uses, because exact manuscript definitions are not supplied.',
  'This is a cross-package terminology audit of cote16/044–051, not content of 18/025–027. The second-pass readings do not settle the two inferred matches.',
  'not on the page','Reading cote16 L1723–1756 and L1803–1829 supports the two operator matches. The p18 pages add no definition; the uncertainty retained by the earlier notes is correct.')
A(61,'self-flagged step',[25,27],'133–161;186–199','no singular-hypersurface reduction here',
  'Cote16/047 retracts a reduction through smooth hypersurfaces after Serre’s simply-connectedness objection and proposes reformulating standard conjectures for singular varieties. The corresponding cote14 programme is not available in this part.',
  'A cross-package programme, not a p18 claim. Presence of singularities on the anonymous reused 18/044 leaf does not identify the intended reduction.',
  'not on the page','Cote16 L1791 explicitly supplies both withdrawal and new proposal; no link to a completed cote14 proof is established. This item should merge with the p16 programme in final integration.')
A(62,'other',[34,57],'319;933–948','G/G^0; phi_v:Gal(k/k0)→G(k)',
  'For rational Nori motives over Q and a fixed embedding Qbar→C with compatible Betti functors, the modern sequence is 1→G_Nori(Qbar)→G_Nori(Q)→constant Gal(Qbar/Q)→1, dual to base change and inclusion of Artin motives.',
  'Earlier-run literature comparison; neither the real component-group statement nor the cocycle on these pages prints this Q-sequence. Modern source hypotheses must be retained.',
  'not on the page','The historical formulas involve a real involution or a semilinear cocycle. The note correctly avoids attributing the modern exact sequence to them.')
A(63,'other',[37,55],'399;879','Aut_tensor(T_B); motifs subordonnés',
  'In the chosen embedding/PID setting, Choudhury–Gallauer identify Nori’s and Ayoub’s motivic Hopf algebras. In Arapura’s rational pure category the comparison with André motives uses motivated correspondences; replacing all motivated classes by algebraic cycles is an additional standard-conjecture issue.',
  'Earlier-run modern comparison, not a theorem written in the archive. It supplies no integral lattice from an unspecified rational representation.',
  'not on the page','The source invokes a category and its fibre automorphisms only. The notes’ separation of constructions and algebraicity hypotheses is retained.')
M(64,11,'MB11 repeats the explicit Hodge-conjecture dependency at 18/034 L329. Its separate modern Nori-fullness comparison is literature context, already distinguished from the conditional historical statement in SA07-411.')
A(65,'other',[25,37],'133–161;399','correspondence action; Aut_tensor(T_B)',
  'For smooth projective varieties, rational homological correspondence classes map onto numerical classes. Jannsen’s semisimplicity theorem concerns the numerical category with characteristic-zero coefficients. Factoring a given Weil realization through it requires homological and numerical equivalence to agree.',
  'Earlier-run literature comparison; the quotient and extra equality are not proved on these p18 leaves.',
  'not on the page','The push-pull action does not kill all numerically trivial cycles by itself. The note correctly preserves the extra kernel condition.')
A(66,'unpursued implication',[27,55],'186–199;879','xi⊗Z_l≃xi_l',
  'For genus≥2 smooth proper geometrically connected curves over a common number field K, a dominant map induces an arithmetic fundamental-group map; geometric pro-ℓ abelianization gives the covariant Tate-module map on Jacobians. Faltings identifies the abelian Hom space, while Mochizuki’s open-homomorphism theorem reconstructs curve maps in its sub-p-adic setting.',
  'Earlier-run anabelian comparison. The covariant Jacobian and quotient by geometric inner automorphisms must be specified; no fundamental-group reconstruction is in this manuscript.',
  'not on the page','The manuscript supplies ℓ-adic realization language only. This is segregated as a project lead, with modern theorem references checked independently.')
A(67,'idea of the earlier run',[27,37],'197–199;399','Tate object; Aut_tensor(T_B)',
  'Semisimplicity does not imply trivial centre: rational Gm representations split into characters, while Gm→Inn(Gm) has kernel Gm. In the hyperbolic geometric fundamental-group setting the centre is trivial, allowing reconstruction of the extension as the pullback through Aut→Out.',
  'Earlier-run contrast through the actual conjugation kernel; no motivic centre theorem is inferred.',
  'not on the page','The archive’s Tate example supports the scalar test, but the anabelian assertion is external. The note does not conflate these properties.')
A(68,'other',[27,57],'197–199;933–948','Tate line; arithmetic cocycle',
  'Stix’s cuspidal criterion uses both an open arithmetic image of a normalizing subgroup and its specified cyclotomic conjugation action on pro-ℓ inertia. For number-field abelian varieties a weight argument excludes a nonzero Galois map Z_l(1)→T_lA. Open normalizer image alone does not verify the criterion.',
  'Earlier-run LM6 comparison. The truncated external LM6 A.50 result and open A.22 question are not supplied here and their claims are not certified.',
  'not on the page','The source contains no such inertia subgroup or character identity. The notes correctly retain the missing premise.')
M(69,39,'MB16 concerns exactly the integral comparison existence and diagonal G(Z) ambiguity of 18/055 L870–881. SA07-439 retains both, including the limit of rational Tannakian comparisons.')
A(70,'unproved claim',[18],'5–9','module tangent; transposee de l’application diagonale',
  'In the reused formal-kernel source, distributions U(V) inherit a chart-independent filtered coalgebra; the completed function algebra is its dual, T(V)=U_+∩U_1, and a formal map acts covariantly on distributions and on tangent modules. The asserted universal mapping description to a free module uses the earlier formal-polynomial hypotheses.',
  'Auxiliary reused source, not established authorship as Grothendieck’s motives draft. The exact finite-rank/divided-power conventions require the adjacent formal pages.',
  'agrees','L5–9 states all these constructions and refers to earlier propositions rather than proving chart independence here. No identification with restricted Lie or Dieudonné objects is written.')
A(71,'reading question',[22],'83–93','phi_2*=psi_1* circle phi_1*',
  'With φ_i*:P(M_i)→A and ψ_1*:P(M_2)→P(M_1), conventional composition is φ_1*∘ψ_1*, whereas Definition 3 writes the reversed order. Definition 5 later uses the standard composable order φ*^-1 f* ψ*.',
  'This type-check suggests a source typo or composition convention to inspect. No source correction is made.',
  'agrees','Both map directions are explicitly fixed at L83 and L91, making the inconsistency local and concrete.')
A(72,'unproved claim',[22],'85–93','on vérifie aisément ... au Pape ou au Général',
  'Compatible formal charts are claimed to form an equivalence relation, the morphism condition need only hold in one pair of charts, and identity/composition make formal kernels a category. Once the pullback-order convention is repaired, these are formal consequences of composition of continuous augmented algebra maps.',
  'The proof is an editorial reconstruction; the text explicitly delegates its completion. General completeness and finite-rank hypotheses are inherited from the reused source.',
  'agrees','L85,89,93 state the properties and delegate isomorphisms. The note accurately records a proof omission, not a failed theorem.')
A(73,'withdrawn in the same text',[20],'38–51','Diviser par la factorielle; mettre un 4 au dénominateur',
  'The root-system editorial leaf orders numerical/rank corrections and a semidirect-product description. It also writes Q=L0∩V′, P=orthogonal projection of L0 and P=Q+Zv′ in the A_l model, with (l+1)v′=(l,−1,...,−1). Exact factorial, gamma and denominator corrections need the cited source pages 195–201.',
  'Auxiliary source correction. The complete target formulas are not reconstructed from instructions alone; “R=R” remains an unresolved likely decoration issue.',
  'agrees','The listed changes are affirmative editorial commands at their exact source positions. The indexed note properly leaves unsupplied formulas unverified.')
A(74,'reading question',[24],'121–123','pouahs et copouahs; pois radiciels; poix',
  'The reused source calls Q(R) the lattice generated by roots and P(R) the lattice dual to the coroot lattice Q(R*), asking for the inclusions. The humorous spellings concern terminology, not different lattice definitions.',
  'Modern root/coroot terminology is explanatory. Chronological order relative to cote44 terminology drafts is unknown.',
  'agrees','The definitions are explicitly coupled to Q and P at L123. The note’s external comparison needs the separate cote44 endpoint.')
A(75,'unproved claim',[28,24],'214–226;113–115','démonstration ... fournie par Borel',
  'For a finite crystallographic root system and a closed subset P with P∩(-P)=empty, the source argues that P lies in a positive system: exclude zero sums, obtain a separating nonzero vector, then induct lexicographically on the orthogonal root subsystem.',
  'The complete antecedent of Proposition15 is not supplied; the root-system/closedness hypotheses are reconstructed from the proof. Literal zero-sum typos are separately flagged.',
  'agrees','The proof begins on scan28 and continues on scan24. The notes correctly recover source order 28→24 while preserving diplomatic scan order.')
A(76,'reading question',[28],'220–224','y1+yq=0; sum_(i≠j) y_(1|i)',
  'The induction needs the full zero sum y1+...+yq=0, and replacing y1,yj by y1+yj requires excluding both indices 1 and j. The written two-term assumption and remaining sum do not give that induction literally.',
  'Mathematical alternatives only. Neither an ellipsis nor a second omitted index is inserted into the source.',
  'agrees','At q=3 the written two-term equality cannot imply -y1=y2+y3. The subsequent sum also retains the first term.')
A(77,'self-flagged step',[26],'171–175','Mieux expliciter le procédé d’identification',
  'The source contracts an order-three edge (i,j) to p, carries adjacent edges and labels to p, and replaces variables ξ_i,ξ_j by ξ_p. It requests explanation of this construction inside the classification argument.',
  'Auxiliary graph construction, not a claim about motivic Galois groups. The full quadratic-form hypothesis is not supplied.',
  'agrees','L173 specifies the map itself. The remaining request is its proof role, not absence of a construction.')
A(78,'self-flagged step',[26],'181','5 ou des p≥7 (référence); nous verrons plus loin',
  'For finite crystallographic root systems, rank-two Coxeter labels are 2,3,4,6; hence labels 5 and p≥7 cannot arise. The source separately promises realization of the remaining finite crystallographic diagrams later.',
  'The rank-two Cartan-integer computation is modern explicit reconstruction. The promised full classification proof is not present in these fragments.',
  'agrees','The request for a reference and the later-construction promise are both explicit at L181.')
A(79,'self-flagged step',[30],'251–257','connexion du graphe donne la conjugaison voulue',
  'The source asks for a proof of conjugacy of Coxeter words via graph connectivity, cyclic moves and commutation of nonadjacent generators, exhibiting bAa→baA→aAb→Aba. For finite Coxeter groups, Coxeter elements are conjugate; the complete local presentation is not supplied here.',
  'The identification with the standard finite-Coxeter theorem is a reconstruction requiring that scope. It is not a general statement for every Coxeter group.',
  'agrees','The explicit word moves and explanation request appear at L255–257. The note does not confuse this with a separate Cartan-conjugacy lead.')
A(80,'withdrawn in the same text',[30],'259','(ii) est faux avec G réductible',
  'The editor withdraws the unrestricted assertion (ii) about exponents and requires irreducibility of G. The actual assertion (ii) is absent from this leaf, so a specific counterexample to its exact text cannot be supplied.',
  'A documentary correction, not an inferred reconstruction of the missing proposition.',
  'agrees','The phrase is explicit. No missing assertion or mathematical novelty is guessed.')
A(81,'reading question',[44],'597–614','polynomial in n; variety of singularities',
  'An anonymous English reused page states a polynomial-degree induction for an Euler-characteristic-like quantity and direct-image comparison under a modification that is an isomorphism away from the singular locus. Its variables, initial hypotheses, author and source remain unidentified.',
  'The symbol printed X may be chi; that reading is not changed. Shared singularity vocabulary does not connect this fragment to the standard-conjecture programme.',
  'agrees','The proof is mid-argument and carries printed32 plus marginal p192. These are source-identification clues, not a complete theorem.')
A(82,'withdrawn in the same text',[45],'632–649','On définit aussi',
  'The lower Čech/presheaf passage proposes derived-functor and local Čech formulas but is cancelled as a whole. Its cancellation does not extend to the live elliptic-group computation above.',
  'No mathematical statement is reconstructed from the rotated/deleted formulas beyond the withdrawal.',
  'agrees','An outer deleted block encloses L632–649. The note confines its verdict to that textual layer.')
A(83,'unproved claim',[46],'656–668','Définition locale d’une mesure de Haar',
  'For a locally compact group G and a nonzero positive Radon measure on a nonempty open V whose restrictions are invariant under every translate remaining inside V, the translated local measures glue uniquely to a left Haar measure. The corollary transfers Haar measure through a local group isomorphism.',
  'The Radon interpretation follows the measure source’s setting; no motivic meaning is inferred. The proposition proof is present, but the corollary continuation is cut off.',
  'agrees','L664 gives overlap agreement and gluing; L668 starts the corollary proof. The upper line also records the usual Q_p measure normalization.')
A(84,'unproved claim',[48],'719–731','e(v_i/v)=v_i(a)',
  'Under the inherited finite Dedekind-extension hypotheses, localizing aB=∏p_j^e(j) at p_i gives aB_pi=p_i^e(i)B_pi; with normalized v_i this yields e(v_i/v)=v_i(a). Residue fields are A/p and B/p_i.',
  'The antecedent extension hypotheses are reconstructed from the localized ideals because the leaf starts at parts(c),(d).',
  'agrees','Every localization equality is printed at L723–728. No relation to the period torsor is asserted.')
A(85,'unproved claim',[52,50],'792–800;758–760','SL(n,K) est dense dans SL(n,A)',
  'For the restricted adele ring of a Dedekind domain, density of the fraction field and elementary generation over each local field imply density of SL_n(K) in SL_n(A) (n≥2; n=1 is trivial). The argument uses I+aE_ij and finite-support approximation.',
  'Auxiliary standard approximation result. It does not imply strong approximation for the arbitrary motivic group on scan51.',
  'agrees','Scan52 proves additive density and continuity; scan50 gives the elementary-matrix proof. The unfinished textbook citation is retained separately.')
A(86,'reading question',[50],'762–770','Le théorème de Krull-Akizuki',
  'If A is a noetherian domain of dimension≤1, a finitely generated torsion A-module has finite length. If T is a directed union of submodules T_i, its length is sup length(T_i), allowing infinity. The visible proof of the second lemma stops after choosing a maximum index.',
  'The first hypotheses are written; the directed-union proof can be completed mathematically but its missing source continuation is not invented.',
  'agrees','L764–766 proves finite length using associated primes; L768–770 states the supremum formula and leaves a cut-off index issue.')
A(87,'unproved claim',[56,54],'909–921;842–865','div(a:b)=div(a)−div(b)',
  'In a Dedekind domain, nonzero fractional ideals factor uniquely into prime powers. Valuation exponents add/subtract for product/quotient, take minimum for sum, maximum for intersection. Prescribed finitely many local approximations can be achieved by an element integral at every other prime.',
  'Auxiliary standard theorem; the approximation proof on scan54 only treats the integral-target beginning, with further source text absent.',
  'agrees','The ideal factorization and four formulas are explicit; the Chinese-remainder reduction is shown at L861–865.')
A(88,'reading question',[58,56],'956–968;907–909','Montrons que c) implique d); ... semi-local ... principal',
  'The fragment proves several implications in a missing equivalence list for Dedekind rings. The independent stated proposition is that a semilocal Dedekind domain is a PID, by choosing one element with prescribed valuations at its finitely many maximal ideals.',
  'Noetherian or finite-character assumptions in the missing g) are not reconstructed. The PID proof spans scan58→56.',
  'agrees','The equivalence antecedents are absent, but the semilocal proposition and its valuation proof are visible in both places.')
A(89,'reading question',[60,26],'987–1015;177','Système de racines de type G2',
  'The reused diagram shows the twelve G2 roots with simple roots α1,α2 and positive highest root 3α1+2α2. Source n383 is also the rédaction requested on scan26.',
  'The standard rank-two root realization can verify labels, not the drawing’s exact pen geometry. No action on a motive is supplied.',
  'agrees','All six positive labels and their opposite rays are present; the note correctly treats this as a source-layer link.')

# Duplicate self-flag registers were individually read. These mappings are manually chosen
# from the same textual event, with source-specific reasons rather than keyword inference.
M(90,73,'SF01 records the same two factorial divisions, denominator4 and rank changes on 18/020 L38–51 as R04; these remain source-correction tasks.')
M(91,3,'SF02 is the same uncertain question mark on the upper-left arrow of 18/021 L58; uncertainty of the glyph remains explicit.')
M(92,72,'SF03 quotes the delegated category verification at 18/022 L93 already recorded with the chart hypotheses in SA07-472.')
M(93,77,'SF04 is the order-three edge-contraction explanation request at 18/026 L173; the construction itself is already written there.')
A(94,'self-flagged step',[26,60],'177;987','lemmes3 et4 ... canulés ... revenir à l’état3',
  'The editor questions the formulation or correctness of source lemmas3 and4 and requests an earlier rédaction n383. Their statements are not contained in the supplied leaves; the n383 G2 drawing is only an internal source marker.',
  'This is an unresolved documentary problem with no theorem reconstructed from the criticism.',
  'agrees','The criticism at L177 is distinct from the preceding edge contraction and deserves its own item; the notes correctly withhold a mathematical verdict on absent lemmas.')
M(95,78,'SF06 repeats the explicit missing reference after excluding labels5 or p≥7 on 18/026 L181.')
M(96,78,'SF07 records the separate promise of later root-system realizations in the same 18/026 L181 sentence; both tasks are retained in SA07-478.')
M(97,79,'SF08 quotes the exact graph-connectivity/conjugacy explanation request at 18/030 L255.')
M(98,80,'SF09 records the explicit irreducibility correction at 18/030 L259; the missing assertion(ii) remains unknown.')
M(99,11,'SF10 repeats the explicitly conditional Hodge-fullness sentence at 18/034 L329; no unconditional fullness is attributed.')
M(100,12,'SF11 is the locally answered tensor-formation question at 18/035 L344, distinct from the additive-map tensor defect in L357; both are handled in SA07-412.')
M(101,13,'SF12 is the tentative tensor-nonisomorphism statement at 18/035 L359; the sign-Artin proof and Tate-only exception qualify its category scope.')
A(102,'withdrawn in the same text',[36],'372','si on admet conj. de Hodge',
  'The opening deduction from f∞=1 toward the connected scalar group is deleted. It is distinct from the subsequently live even-Tate converse and its Artin–Tate refutation.',
  'Only the deletion event is retained; the erased argument is not a live proof.',
  'agrees','L372 is an outer deleted sentence. The note correctly separates this withdrawal from L383–393.')
M(103,16,'SF14 records the live Hodge-conditional even-Tate assertion at 18/036 L383–393 and /038 L441; the actual Artin–Tate counterexample checks its stated premise.')
M(104,19,'SF15 duplicates the wholly cancelled normalizer/maximal-compact block at 18/038 L445–465.')
M(105,9,'SF16 concerns the author’s affirmative fixed-topology independence checks at 18/039 L475,495, not words of doubt; SA07-409 preserves this distinction.')
M(106,23,'SF17 is problem3 at 18/043 L589, the complete discretely valued p-adic/de Rham comparison question, separately tracked in the problem index.')
M(107,23,'SF18 is problem4 at 18/043 L591, the positive-characteristic cohomology construction question, distinct from problem3.')
M(108,29,'SF19 repeats the explicit rejected value6 at 18/045 L628; the undefined K prevents interpreting it as a refutation of full period genericity.')
M(109,82,'SF20 is the cancelled lower Čech block of 18/045 L632–649, not the live elliptic calculation.')
M(110,32,'SF21 records the same admitted finite-index strengthened-Tate premise at 18/049 L740; this consolidation adds the maximality/counterexample qualification.',verdict='corrected')
M(111,33,'SF22 records admission and re-use of the generic-coset lemma at 18/049 L740–748 and /051 L774,782; the topology caveat is retained.')
A(112,'reading question',[50,52],'760;800','Alg., chap.III,3e éd., blank section/number',
  'The proof cites elementary generation of SL_n over a field and the adjugate polynomial formula, but leaves section and proposition numbers blank. These are bibliographic gaps, not a stated mathematical doubt.',
  'Modern references can verify the facts without pretending to fill the edition-specific blank from memory.',
  'agrees','The unfinished references are printed at L760 and L800. The earlier note identifies a reference gap rather than a failed proof.')
M(113,35,'SF24 repeats the explicitly imposed approximation hypothesis at 18/051 L776–780; the Gm obstruction is a test of automatic density, not of the conditional implication.')
M(114,36,'SF25 repeats the est|pas uncertainty and dependence-on-M warning at 18/051 L780.')
M(115,37,'SF26 is the inserted “le lemme et” in the equivalence margin at 18/051 L782; both inputs and the missing converse are retained.')
M(116,39,'SF27 concerns the uncertain affirmative verb and integral generated-category isomorphism at 18/055 L879; existence and conditional uniqueness are distinguished.')
M(117,40,'SF28 duplicates the deleted cardinal-two assertion and following quotient map at 18/055 L890–900.')
M(118,41,'SF29 records “On vérifie aussitôt” and ψ=φ^-1 at 18/057 L942–948; this is an asserted check whose algebra is rechecked here.')
M(119,42,'SF30 is the exact À vérifier/OK margin at 18/059 L974 accompanying the torsor identification.')
M(120,43,'SF31 repeats the explicitly labelled generic-period-point conjecture at 18/059 L976–980; it remains distinct from the subgroup-generated density test.')
M(121,45,'SF32 is the unfinished π qualification at 18/059 L981. The curve-level j example tests a possible paraphrase without completing the motive descent argument.')
M(122,44,'SF33 duplicates the corrected coboundary order at 18/061 L1020; the old expression is not treated as live.')
M(123,47,'SF34 is the tentative open-subgroup closure at 18/061 L1035 with uncertain marginal mark at L1036; topology and target remain necessary.')
M(124,48,'SF35 announces the small verification whose actual finite-component cancellation and archimedean formula occur at 18/062 L1063,1078.')
M(125,48,'SF36 records the deleted line L1074 and corrected boxed line L1078 with final inverse; the live formula is the one checked.')
A(126,'title, date or page count',[31,42],'261–266;564–568','Corps de base top.; Variation du réseau discret; Critère de transcendance',
  'Two local title sheets name topological base fields R or C (Hodge/de Rham functors) and variation of the discrete lattice with an archimedean place (transcendence criterion). They carry manuscript numbers30 and41, with no date or total extent.',
  'The titles are documentary, not mathematical assertions. No sequence length is assigned from a cover alone.',
  'agrees','Both cover texts and manuscript numbers are present; the note does not invent a written 45-page total.')
A(127,'title, date or page count',list(range(18,63)),'2–1083','manuscript page numbers17–61',
  'The supplied selection has45 scan markers18–62 and manuscript numbers scan−1=17–61; the first17 is uncertain. Printed source numbers identify distinct reused texts and do not replace the scan locator.',
  '45 is our count of supplied scan markers, not an authorial page-count statement.',
  'agrees','Every scan has the corresponding manuscript marker, and the source table in the note matches the read transcription.')
A(128,'title, date or page count',[18,22,24,28,48,50,52,54,56,58],'3;79;111;204;717;754;790;840;905;954','A–18; A–20; 2–3 through2–12',
  'Recovered source order is formal22(A18)→earlier16(A19)→18(A20), closed-root proof28→24, and Dedekind58→56→54→52→50→48, with visible gaps in printed source pagination.',
  'These are local textual continuations, not chronological ordering of the autograph notes.',
  'agrees','Each endpoint numbering or sentence continuation is visible. The earlier-package formal scan16 is checked by the p15 reader and in the cross-package evidence.')
A(129,'title, date or page count',[32,35],'269–274;335–340','BURES-SUR-YVETTE (S.-&-O.); 928-48-53',
  'The identical IHÉS letterhead and telephone on scans32 and35 supply no written date or page count.',
  'No date is inferred from the telephone/address without independent documentary evidence.',
  'agrees','Both headings are transcribed, and neither leaf contains a date.')

def write():
    (P/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
    with (P/'entries.tsv').open('w') as f:
        w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['entry_id','item_id','verdict','reason'])
        for n in sorted(verdicts):w.writerow([SRC[n-1]['entry_id'],*verdicts[n]])
    assert set(verdicts)==set(range(1,130))
    assert sum(len(i['sources']) for i in items)==129
    print(f'Written {len(items)} manually authored items and {len(verdicts)} verdicts; all129 source entries covered once.')

if __name__=='__main__':write()
