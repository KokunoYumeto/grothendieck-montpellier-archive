"""Manually authored claim census. Serialization does not determine any verdict."""
from pathlib import Path
import json
P=Path(__file__).parent
F='SA07_texts/pro/MPL_18_018-062_transcription.tex'
claims=[]
def C(n,items,scans,lines,ink,statement,status,computation,cls,fate,date,present,refs,confidence='high'):
    claims.append(dict(id=f'CL-SA07-{400+n}',items=[f'SA07-{i}' for i in items],cote='18',scans=scans,lines=[F+':'+lines],his_statement=ink,statement=statement,status_on_pages=status,computation=computation,class_=cls,fate=fate,fate_date=date,present_status='As of 2026-11-19: '+present,refs=refs,confidence=confidence))

C(1,[470],[18],'3–9','T_0(V)=U^+(V)∩U_1(V)',
  'For the formal affine space with completed symmetric coordinate algebra, finite-order distributions at the origin form its continuous dual coalgebra; tangent distributions are precisely the order-at-most-one distributions that annihilate constants.',
  'stated without proof; the sheet refers to A20 n°413 and does not supply those definitions',
  'computations.md §16: dual of A/m² splits into constants and tangent functionals; C14 checks the later contravariant types.',
  'E','Cartier’s 1955–56 seminar, §4, defines distributions and their coalgebra/tangent structure; Dieudonné 1956 describes the dual formal-series algebra. Identification of this reused sheet with a particular published draft remains unproved.','1956; Cartier lecture 1956-01-20','The reconstructed standard statement is valid; provenance of the sheet is not established.',['Cartier56','Dieudonne56'])
C(2,[401],[19,21],'14–25;55–74','P_sigma^(p)=sigma(2πi)^(-p) P_alg',
  'For a smooth complex algebraic variety, the codimension-p de Rham cycle class corresponds to (2πi)^p times the integral Betti cycle class under the manuscript residue convention; transport by a field isomorphism sigma transports the scalar too.',
  'stated without proof; diagram reductions and the analytic trace warning are given',
  'C01 and computations.md §1; explicit residue integral and push-pull scalar cancellation. Cross-package 18/015–017 provides the local residue test.',
  'B','Grothendieck 1966 Thm1/1′ is the foundational de Rham comparison, not an exact located scalar theorem. Deligne 1971 §§2.1.13–14,2.2.4–6 treats the Tate/cycle normalization; Sastry–Tong Thm4.1 explains the trace convention issue. Class A is not inferred from the related G66 comparison.','G66 letter 1963-10-14, publication 1966; exact convention sources D71 publication 1971 and ST03 publication2003','Valid after specifying orientation, comparison, and trace conventions; no universal extra-sign-free trace statement is inferred.',['G66','D71','ST03'])
C(3,[402],[19],'23–31','change P_sigma^(p) en -P_sigma^(p)',
  'Reversing the chosen complex orientation multiplies the codimension-p cycle normalization by (-1)^p. The displayed minus sign is valid for the immediately preceding p=1 example, but not uniformly in p.',
  'stated without proof; scope of the concluding sentence is ambiguous',
  'C01: conjugating 2πi changes its p-th inverse power by (-1)^p. Counterexample to uniform minus: p=2, X=P² and a point.',
  'E','This is the elementary orientation parity encoded by the Tate lattice and its conjugation in Deligne §2.1.13–14. No distinct conjecture or later discovery is identified.','Elementary calculation predating the sheet; modern convention recorded 1971','Keep the ink; mark the p=1 versus general-p scope for the scan pass.',['D71'])
C(4,[403],[21],'55–66','diagram with cohomology supported on Z and upper arrow unsure{?}',
  'Reconstruction: for a smooth closed codimension-p embedding Z→X, the local topological fundamental class and de Rham residue class correspond after shift 2p and scalar (2πi)^p. The page’s question mark does not by itself specify a general purity conjecture.',
  'open on the pages at the marked arrow; precise scope not fully specified',
  'computations.md §1 uses a transverse polydisc and product of p contour integrals; it is a local regular-embedding check, not a proof of every unsupported global diagram.',
  'C','Grothendieck’s comparison and the later trace comparison establish the regular-embedding formulation. The precise questioned arrow cannot be completely identified from the diagram and uncertain mark alone.','1966; trace comparison publication 2003','Standard regular-embedding comparison is valid; the authorial scope of the question remains uncertain.',['G66','ST03'],'medium')
C(5,[404],[23],'98–106','morphisme propre quelconque; degree q→q+2p',
  'For a proper map f:X→Y of smooth complex varieties of relative codimension p=dimY−dimX, the comparison between algebraic and topological pushforward has scalar (2πi)^(-p) in the manuscript trace normalization, and cohomological degree shift 2p.',
  'stated without proof; the preceding local calculation is used as motivation',
  'C01; computations.md §1 checks dimension, shift, and compatibility with the point trace. Trace signs beyond the manuscript convention are explicitly separated.',
  'B','The general trace–integration comparison is proved by Sastry–Tong Thm4.1. Their usual Hodge spectral-sequence convention has an additional dimension sign, so it is not a literal convention-free confirmation of the displayed formula.','First received 2001-10-18; publication 2003','Valid in a coherent chosen Gysin convention; a complete convention dictionary is needed before comparing different trace constructions.',['ST03','D71'])
C(6,[405],[25],'133–161','same linear map on the various realizations of a correspondence',
  'For a correspondence Z of codimension r on X×Y with X smooth proper of dimension d, the induced cohomology map has degree 2(r−d) and comparison scalar (2πi)^(d−r). Therefore a degree-zero correspondence, r=d, acts identically in the transported Betti and de Rham realizations.',
  'proof sketched by pullback, cup product, and pushforward; several indices remain uncertain',
  'C01 and computations.md §1 derive the exponent as -r+d. The source’s n/m and Omega_X-on-Y anomalies remain reading alarms.',
  'B','This follows from the established cycle and trace comparisons; Deligne’s cycle formalism and Sastry–Tong’s explicit trace theorem are the checked sources. No claim that all manuscript indices are correct is made.','Comparison 1966; explicit trace theorem 2003','The reconstructed degree-zero compatibility is valid.',['G66','D71','ST03'])
C(7,[406],[27,29],'186–199;233–239','alpha_infty(u)=(2πi)^(-1)v',
  'A chosen complex orientation fixes the comparison on the Tate object and thereby the integral Betti lattice inside its complex de Rham realization; complex conjugation acts on a Tate twist by its parity.',
  'stated without proof; the P¹ normalization is exhibited',
  'C01; computations.md §1 and §2. Integral statements concern the image modulo torsion, not an injected torsion module.',
  'B','Deligne §2.1.13–14 explicitly records Z(1)=(2πi)Z and the geometric orientation convention. Grothendieck’s comparison supplies the de Rham side.','1966 and 1971','Established; the alternative reading primitifs/possibles at L237 is not settled by this mathematics.',['D71','G66'])
C(8,[408],[29],'233–239','integral Betti realization is stable under conjugation',
  'For a variety over R, the action of the real involution on the underlying complex analytic space preserves integral singular cohomology and hence its torsion-free image in complex cohomology.',
  'stated without proof',
  'computations.md §2: functoriality of integral singular cochains; no transcendence or period conjecture is needed.',
  'E','Integral functoriality is classical. Deligne §2.1.14 provides the compatible Tate orientation statement; it does not identify real-locus cohomology with invariants.','Classical before the sheet; modern convention 1971','Valid for the geometric involution. It does not imply that every real structure on de Rham cohomology is the same.',['D71'])
C(9,[471,472],[22],'78–93','given two charts, psi_1^* composed with phi_1^*; definition of formal varieties',
  'A formal chart transition is a continuous substitution between completed symmetric algebras, contravariant to the map of formal spaces. The claimed category is coherent with this convention, but the printed composition has the wrong source/target order.',
  'stated without proof; type inconsistency in one displayed composite',
  'C14 and computations.md §16 explicitly list source and target. No correction of the diplomatic transcription is made.',
  'E','Dieudonné 1956 pp208–209 supplies the complete formal algebra and dual hyperalgebra framework. The manuscript’s particular chart definition is not independently attributed to a later publication.','1956','The formal construction is standard after the contravariant order is made coherent; literal composite requires scan verification.',['Dieudonne56'])
C(10,[409],[32,33,39,40],'274–292;471–529','fix the topology; Hodge splitting and real form',
  'For a smooth proper complex variety with a chosen complex topology, the Hodge filtration together with Betti conjugation gives an opposed Hodge decomposition. This is an analytic construction depending on the embedding/topology, not an algebraic splitting over an arbitrary field isomorphic to C.',
  'stated without proof; alternative topology choices are discussed as questions',
  'computations.md §2: identify H^(p,q)=F^p∩bar(F^q) inside H^(p+q). The page’s H^q/H^(p+q) readings remain flagged.',
  'B','Deligne Hodge II §§2.1.9,2.2.1–3 is an exact modern formulation. This does not settle the stronger topology-independent or algebraic splitting question owned by p15.','1971','Established for a chosen complex embedding; universal algebraic splitting is not supplied by these sources.',['D71'])
C(11,[410],[33,37],'288–292;399–421','sigma and tau commute; f=sigma tau',
  'For X/R, let sigma be coefficient conjugation and tau the anti-linear conjugation associated to the real de Rham form. Their product is the complex-linear geometric real involution f; sigma and tau commute, and f²=1.',
  'stated without proof in this passage; cross-package 15/203 marks the compatibility à vérifier',
  'C02 and computations.md §2 model the two commuting real structures. This uses the comparison for an actual real variety, not arbitrary unrelated anti-linear involutions.',
  'B','Deligne’s real Hodge formalism and the standard comparison support the compatible pair. The general assertion for arbitrary two anti-linear involutions would be false; the geometric compatibility is essential.','1971 modern formalism','Valid for the specified geometric structures; compatibility must remain part of the hypotheses.',['D71','G66'])
C(12,[412],[35],'340–359','W=V_R^+⊕iV_R^-; tensor? Oui',
  'Given a tensor-compatible involution f on a rational realization V, the real form W_R=V_R^+⊕iV_R^- is tensor-compatible. The evident additive map a:V_R→W_R equal to 1 on V⁺ and i on V⁻ is generally not tensor-compatible.',
  'proof sketched; affirmative tensor annotation concerns W, while the later natural isomorphism is tentative',
  'C02 checks all four sign pairs; on two odd factors a(v)⊗a(w)=-a(v⊗w). computations.md §2 supplies the general argument.',
  'E','The real-form construction is elementary Galois descent; DM12 Thm3.2 distinguishes a tensor isomorphism torsor from a chosen additive map. No historical identity with a published claim is asserted.','Classical descent; Tannakian formulation 1982/2012','W is a tensor real form, but the displayed additive map is not a tensor isomorphism.',['DM12'])
C(13,[413],[35],'357–359','Il semble ... ne sont pas tensor-isom',
  'There need not exist any tensor isomorphism between the two real fiber functors, even if each underlying vector space is isomorphic. For the sign Artin object A, multiplication A⊗A→1 is positive on V but negative on the real line iV.',
  'open on the pages; the author tentatively expects non-isomorphism, which the Artin example confirms on the full real category',
  'C02 and computations.md §2: a tensor scalar q:R→iR would require q²=-1 over R. The Artin object is obtained by (1−c)/2 on h⁰(Spec C/R).',
  'B','DM12 Prop6.17 identifies Artin motives with finite Galois representations and Thm3.2 identifies the tensor-isomorphism torsor. The sign-Artin calculation completes the tentative non-isomorphism claim; a Tate-only restriction instead has an isomorphism e_n↦i^n e_n.','Artin theory classical; Tannakian account 1982/2012','The tentative non-isomorphism holds on any category containing the sign Artin object. It need not hold on every tensor subcategory.',['DM12'])
C(14,[411],[34,37],'298–331;399–421','f j(z) f^(-1)=j(bar z)',
  'For the Hodge homomorphism j attached to a real variety, its geometric real involution conjugates j by complex conjugation. On the norm-one torus this is inversion. The involution may be the identity; order two means order dividing two.',
  'stated without proof',
  'computations.md §2: f interchanges H^(p,q) and H^(q,p); evaluate characters z^p bar(z)^q. C04 checks compatibility with polarization signs.',
  'B','Deligne §§2.1.5,2.1.15–16 gives the Hodge action and polarization framework. It proves neither the Hodge conjecture nor arbitrary motivic fullness.','1971','Valid for geometric real Hodge structures. The later deleted maximal-compact discussion is not part of this live claim.',['D71'])
C(15,[411,454],[34],'319–331','the Hodge realization is fully faithful',
  'For pure motives over R with algebraic correspondences, full faithfulness into Hodge structures equipped with the compatible real Frobenius requires the relevant Hodge classes on all tensor constructions to be algebraic and the correspondences to descend to R. Forgetting real Frobenius is not this claim. Absolute-Hodge/André abelian motives provide established variants.',
  'stated without proof under the manuscript’s Hodge-type assumptions',
  'computations.md §3 explains how tensor invariants, fullness, and Tannaka groups relate. No standard or Hodge conjecture is treated as proved.',
  'C','DM12 Prop6.25 establishes the abelian absolute-Hodge case; Arapura Thm6.4.1 identifies pure Nori with André motives and §7.1 separates the general fullness conjecture.','1982/2012; Arapura first preprint 2008-01-01, publication 2013','General algebraic-cycle fullness remains conjectural; abelian absolute-Hodge/motivated versions are established.',['DM12','Arapura13'])
C(16,[411],[34],'319–327','f together with G^0 generates G',
  'For a real motivic Galois group, generation by the identity component and real conjugation follows from an exact geometric/arithmetic sequence and connectedness of the geometric kernel. The latter is not automatic for arbitrary algebraic motives.',
  'stated without proof with background conjectural hypotheses',
  'computations.md §3: a quotient of Gal(C/R) has at most two elements only once the kernel is G⁰. If the geometric group is disconnected the inference fails.',
  'C','DM12 Props6.22–6.23 require all Hodge cycles to be absolute Hodge for geometric connectedness; footnote21 in the corrected 2012 text says the hypothesis was omitted in 1982. Prop6.25 supplies the abelian case. Kahn Thm5.10 gives a general exact-sequence framework, not automatic connectedness.','1982 original; correction 2012; Kahn 2025','Conditional in general. Do not use the uncorrected 1982 wording to remove the Hodge assumption.',['DM12','Kahn25'])
C(17,[415],[36],'364–370','bar(alpha)=f alpha; alpha real iff f=1',
  'For the distinguished comparison point alpha in its torsor, the equation bar(alpha)=f alpha implies alpha is R-rational exactly when f is the identity, by freeness of the torsor action.',
  'proof sketched by the displayed equation',
  'computations.md §2; distinguishes this single point from existence of some real point. Tate example: an imaginary comparison can lie in a split G_m-torsor.',
  'E','This is elementary torsor descent, formulated in DM12 Thm3.2. The stronger assertion that P(R) is empty iff f≠1 is not implied.','Classical; modern Tannakian formulation 1982/2012','Correct for the specified alpha; an obstruction for all real points requires the cohomology class of the cocycle.',['DM12'])
C(18,[416],[36,38],'383–393;433–441','f=1 iff the motive is generated by even Tate powers',
  'The forward direction from a direct sum of even Tate powers to f=1 is valid. The converse for motives over R is false: let A be the sign Artin motive and T=Q(-1); then f(A⊗T)=+1, but this rank-one motive has weight 2 and cannot lie in the category generated by Q(-2).',
  'false as stated under the natural category of algebraic motives over R; the live tentative equivalence is distinct from the deleted opening at L372',
  'C03 and computations.md §2 check projector algebraicity, f signs, and weights. A⊗T is an algebraic direct summand of h²(P¹_C regarded over R), so the example satisfies the geometric motive hypotheses.',
  'C','Artin motives and Tate objects are established in DM12 §§6.10,6.17. The exact proposed equivalence has no positive modern theorem under these hypotheses; the counterexample is independently reconstructed here.','Underlying objects classical; counterexample checked 2026-11-19','False in the stated natural category. Additional restrictions excluding Artin twists would be needed, and are not supplied by the page.',['DM12','D71'])
C(19,[417],[36],'387–393','abstract G≃G_m characterizes the exceptional case',
  'The abstract isomorphism type G≃G_m does not determine the Tate character or real involution. A faithful one-dimensional Tate or Artin–Tate generator can give G_m with different distinguished characters and real signs.',
  'open on the pages; an unqualified equivalence is false in the natural reconstruction',
  'C03 and computations.md §2 compare Q(-1),Q(-2),A⊗Q(-1), retaining the distinguished realization and weight. The last marginal Q-tordu wording is unreadably incomplete.',
  'C','DM12 neutral Tannaka reconstruction uses the fiber functor and its distinguished representations, not only an abstract algebraic group. Deligne’s Tate convention confirms the weight distinctions.','1982/2012 modern formalism','Abstract G_m alone is insufficient; the extra structure cannot be discarded.',['DM12','D71'])
C(20,[411],[37,38],'399–439','real forms of the period group and torsor',
  'A compatible involution f gives a real descent datum on the complex comparison torsor and an inner twist of its automorphism group. Existence of a real tensor comparison is governed by the cocycle class, not by whether a chosen representative f equals 1.',
  'proof sketched with torsor points alpha,beta,gamma; the precise earlier definitions are only partly visible locally',
  'C02,C08 and computations.md §§2,4. The distinction between point reality and torsor neutralization is independently checked.',
  'B','DM12 Thm3.2 gives the tensor-isomorphism torsor and descent formalism; BC16 §§2.1–2.3 separates comparison points from generated torsors. No blanket neutrality follows.','1982/2012; BC first preprint 2013','The modern descent statement is established; the manuscript’s numerical real-point inference needs the stated hypotheses.',['DM12','BC16'],'medium')
C(21,[422],[41],'538–561','K_r=intersection of R_T; K_r algebraic over Q',
  'For an abstract field k isomorphic to C, intersect the inverse images of R over all field isomorphisms k→C. The result is the algebraic totally real closure of Q inside k: those algebraic elements whose every Q-conjugate is real.',
  'stated without proof',
  'computations.md §5 proves both inclusions using extension of embeddings and a transcendence basis; no choice of a single topology is silently fixed.',
  'E','This is a field-theoretic consequence of extension of embeddings. Searches for the manuscript formulation did not locate a separate theorem or publication; D71 addresses the distinct fixed-topology Hodge construction.','Classical field theory before the sheet; no exact historical attribution established','Valid for the full family of field isomorphisms. Restricting to one embedding or continuous automorphisms changes the statement.',['D71'])
C(22,[423],[43],'575–591','relations between Betti, de Rham, l-adic, and a characteristic-p cohomology',
  'The page proposes comparisons between integral/rational realizations, variation with complex topology, and p-adic/de Rham cohomology over complete mixed-characteristic fields; it asks for a characteristic-p cohomology. It does not assert a naive integral isomorphism in every case.',
  'open on the pages; a four-part programme, not a proved construction',
  'No authorial finite computation. computations.md §6 records which coefficient extensions and torsion hypotheses are necessary in the cited modern theorems.',
  'C','G66 gives complex comparison. Oda Cor5.11 answers the abelian A[p]/H¹_dR subquestion; Illusie79 Thm3.2 computes crystalline cohomology by de Rham-Witt. BMS18 Thms1.7–1.8 construct A_inf comparison; BS22 Thm1.8 gives bounded-prism comparison with perfect-prism hypotheses for its étale part. RT26 Thms4.2.3–4.3.2 give an integral Nori framework in characteristic zero. Topology-independent algebraic splitting and general integral tensor-torsor neutrality remain separate.','G66 1963 letter/1966 publication; Oda1969; Illusie1978 lecture/1979; BMS2016/2018; BS2019/2022; RT2024/2026','Major comparison components are established with precise coefficient rings, bases and hypotheses; the entire informal programme is not one solved theorem.',['G66','Oda69','Illusie79','BMS18','BS22','RT26'])
C(23,[428],[45],'618–623','dim G=7; G isogenous to SL₂×SL₂×G_m',
  'For two non-CM elliptic curves over C that are not isogenous, their Hodge group is SL₂×SL₂; the Mumford–Tate group is the equal-determinant subgroup of GL₂×GL₂, hence dimension 7 and isogenous to SL₂²×G_m.',
  'stated without proof; nonisogeny/non-CM hypotheses are uncertain in the transcription and are explicit reconstruction here',
  'C05: dim(GL₂²)−1=7; computations.md §7 checks both determinant and central-isogeny descriptions.',
  'B','Moonen–Zarhin Cor3.9 gives the product Hodge group and attributes the elliptic-product result to Imai; the original Imai publication metadata was opened. These results apply only after the reconstructed hypotheses are imposed.','Imai received 1974-11-12, publication 1976; MZ first 1999-01-26, publication 1999','Correct under the explicit hypotheses; no numerical result for the ambiguous literal reading is asserted.',['MZ99','Imai76'],'medium')
C(24,[428],[45],'623–626','dim B=5',
  'A Borel subgroup of the equal-determinant subgroup of GL₂×GL₂ has dimension 3+3−1=5, and its flag quotient has dimension 2.',
  'stated without proof',
  'C05 and computations.md §7 count upper-triangular parameters and one determinant relation.',
  'E','Elementary dimension theory once the preceding group is identified. MZ99 Cor3.9 supplies the conditional group identification; it does not prove the manuscript’s unnamed field bound.','Group calculation classical; elliptic-product identification published 1976','Correct for that group and a Borel.',['MZ99'])
C(25,[429],[45],'628–629','trdeg K≤5; ≤5|4 over the field containing pi; 6 rejected',
  'The displayed transcendence-degree estimate cannot be uniquely formulated because K and the relevant quotient or stabilizer are not defined on the supplied sheet. The number 5 is compatible with a Borel dimension, but that numerical coincidence is not a proof.',
  'open on the pages; one rejected bound and one uncertain alternative remain',
  'C05 certifies only the dimensions. No fabricated field model is substituted for K.',
  'F','Searches on elliptic product periods found MZ99 for the Hodge group and BC16 for period torsors, but neither identifies this K or establishes this precise bound.','Searches 2026-11-19; relevant papers 1999 and 2016','Unidentifiable as a definite theorem until the missing definition or adjacent sheet is found.',['MZ99','BC16'],'low')
C(26,[430],[47,49],'672–708;737–739','dim of diagonal quotient at most (n−1)dim G',
  'For n torsors under a d-dimensional algebraic group G, their product modulo the free diagonal G-action has dimension (n−1)d whenever the indicated geometric quotient exists; after trivialization it is G^(n−1). The manuscript applies this to comparison realizations.',
  'proof sketched through diagonal quotient notation',
  'C05 and computations.md §7: normalize the first coordinate, with the appropriate left/right torsor convention; dim nd−d.',
  'E','The dimension identity is standard torsor algebra, compatible with DM12 Thm3.2. BC16’s generated torsor versus point distinction remains essential for transcendence conclusions.','Classical; Tannakian formulation 1982/2012','Valid under the geometric-quotient/torsor hypotheses. It is not a proof that a given period tuple is generic.',['DM12','BC16'])
C(27,[432],[49],'736–749','Tate renforcée; G géom.; finite-index adelic image',
  'The page assumes a connected group marked géom. and a finite-index integral adelic Galois image. Natural reconstruction: the image should be open in G(Z-hat). This is not a valid universal statement for the tensor subcategory generated by M=Q(-2), if Q(1) is not automatically adjoined and G is its rank-one Mumford–Tate/Tannaka group.',
  'open on the pages; explicitly a strengthened Tate-type premise, not proved; G’s exact meaning is ambiguous',
  'C06 and computations.md §8: for M=Q(-2),rho=chi²; reduction at r odd primes gives index at least 2^r. Category, lattice, group, and no-adjoined-Q(1) convention are stated. This refutes only that reconstruction.',
  'C','Cadoret–Moonen ThmA(ii) obtains an abelian adelic openness theorem with Mumford–Tate and Hodge-maximality hypotheses; §2.6 explains the isogeny obstruction, and §6.3 shows twists matter. It does not validate the ambiguous unqualified premise.','First preprint 2015-08-26; online 2018-06-07; volume 2020','Unqualified natural reconstruction is false; exact ink remains an open ambiguous premise. Appropriate maximality hypotheses give established or conjectural refined statements.',['CM20'],'high')
C(28,[433],[49],'743–748','a coset of a finite-index subgroup contains a generic point at every l',
  'Let G/Q be geometrically connected smooth affine, K a compact open subgroup of its restricted adelic points, and U⊂K an open subgroup. Every coset of U contains an adelic point whose l-component is Q-generic in G for every prime l.',
  'stated without proof; admitted as an auxiliary lemma',
  'computations.md §8 gives a Baire-category proof: countably many rational proper subvarieties, each local zero set nowhere dense, and a compact product box inside the coset. Finite index alone needs closedness to imply openness.',
  'E','The argument reduces to classical Baire category and local analytic nonvanishing. Searches of the exact generic-coset phrase found no separately attributed theorem; CM20 supplies the modern adelic-openness context, not this proof.','Classical ingredients; independent proof 2026-11-19','Valid under the stated topological and geometric hypotheses; does not establish the preceding Galois-image premise.',['CM20'])
C(29,[434],[51],'774–780','generic adelic components give algebraically independent coefficients',
  'Conditional on open adelic image and the generic-coset lemma applied to a power of G, one can choose finitely many Galois elements so their relative l-adic comparison tuple is generic in G^(n−1) for every l. Thus the relevant function field has transcendence degree (n−1)dimG.',
  'proof sketched; depends on the unproved strengthened Tate premise',
  'C05 and computations.md §§7–8; apply the previous Baire argument to the product group. The period interpretation must specify the generated field.',
  'C','The auxiliary construction is valid, but Cadoret–Moonen shows the openness premise requires extra conditions. BC16 distinguishes this genericity statement from mere generation of a torsor.','Modern refinements 2015–2020; independent conditional proof 2026-11-19','Conditional construction; no general adelic openness or period conjecture is proved.',['CM20','BC16'])
C(30,[435,436],[51],'776–780','if G(Q) is dense in G(Q-hat), the lattices can be made commensurable',
  'Conditional on the page’s explicit strong-approximation assumption and its preceding open Galois-image premise, a coset contains a rational point and the corresponding lattices can be made commensurable. Strong approximation is not asserted to hold for every motivic group; it fails for G_m.',
  'open on the pages; the conclusion is explicitly motive-dependent and one est/pas reading is uncertain',
  'C07 and computations.md §8: Q×∩Z-hat×={±1}; an open set requiring 1 mod3 and 2 mod5 contains neither. This blocks density of Q× in finite ideles.',
  'C','The sheet’s separate SL_n proof is sound in its domain. Cadoret–Moonen does not imply strong approximation, and Tannakian theory alone does not remove torus/double-coset obstructions.','Classical strong-approximation distinctions; searched 2026-11-19','The conditional coset argument is valid; applicability to a given motivic group remains a separate question.',['CM20','DM12'])
C(31,[437],[51],'780–784','an equivalence involving independence is left without its assertion',
  'No complete mathematical equivalence can be extracted: independence, its quantifiers, and the compared fields are not defined in the supplied fragment.',
  'open on the pages; unfinished statement',
  'No executable calculation; C05 bounds only dimensions in the separately defined torsor setting.',
  'F','Targeted searches on adelic/period independence led to CM20 and BC16 but no source reconstructing this missing assertion. Broad subject overlap cannot establish its fate.','Searches 2026-11-19','Unidentified, not a claimed open modern conjecture with fixed quantifiers.',['CM20','BC16'],'low')
C(32,[439],[55],'870–879','M_w^Z=g M_v^Z; existence of an integral adelic g',
  'Given compatible integral tensor fiber functors at two embeddings, the page asserts or contemplates an isomorphism represented by g∈∏_l G(Z_l)×G(C). Existence is separate from rational/complex comparison and from the ambiguity once g exists.',
  'stated without proof or open on the pages; verifies/considers wording uncertain',
  'computations.md §9 checks the action and stabilizer only. Rational Tannakian torsor representability does not prove integral points exist.',
  'C','DM12 Thm3.2 establishes an isomorphism torsor over a field. BMS18 and BS22 supply integral comparison in specific geometric settings with period rings. RT26 constructs integral Nori categories and realizations under its precise hypotheses; this does not show that every integral comparison torsor has an integral point.','1982/2012; BMS2016/2018; BS2019/2022; RT2024/2026','The stated existence needs an integral category, lattice compatibility, and local point hypotheses; it is not verified in this generality.',['DM12','BMS18','BS22','RT26'],'medium')
C(33,[439],[55,57],'875–881;926–939','g unique modulo diagonal G(Z); fixed finite components remove ambiguity',
  'Assuming g represents an integral tensor comparison, changing the integral Betti identification multiplies by diagonal G(Z). Fixing every finite component removes this ambiguity when G(Z) injects into the product of G(Z_l); this holds for a faithful torsion-free integral realization.',
  'proof sketched',
  'computations.md §9: a matrix integral at all l and equal to the identity in one Q_l is the identity over Q; distinguish uniqueness from existence.',
  'E','This is elementary faithfulness and intersection of integral lattices; DM12 gives the fiber-functor language. No period-genericity hypothesis is required for this conditional stabilizer calculation.','Classical; Tannakian account 1982/2012','Correct under the explicitly faithful integral model, once g exists.',['DM12'])
C(34,[440],[55],'890–900','all fibers have two elements',
  'For the deleted map from Gamma=Aut(k/k0) to complete complex places, a place v:k≅C has stabilizer Gamma∩{1,c_v}, where c_v is the conjugation induced by v. Its orbit-map fibers therefore have two elements exactly when c_v fixes k0, and otherwise one. The universal two-element claim is not a live theorem.',
  'corrected by himself later: the whole fiber-size-two discussion at L890–900 is deleted',
  'computations.md §9: an automorphism preserving the complete complex absolute value is continuous, fixes R by density of Q and sends i to ±i. Taking its intersection with Aut(k/k0) gives the exact stabilizer. This checks the actual deleted place map, not an unrelated motivic-group quotient.',
  'E','The stabilizer calculation is elementary field and topological algebra. Targeted searches of complete complex places and automorphisms gave the standard identity/conjugation fact, but no separately attributed source for this deleted formulation. DM12 is surrounding descent context only.','Classical elementary fact; searched and independently checked 2026-11-19','Withdrawn on the page. The two-element fiber conclusion requires the missing real-base hypothesis k0⊂k^{c_v}.',['DM12'],'high')
C(35,[441],[57],'944–948','phi(tau sigma)=tau(phi(sigma)) phi(tau)',
  'With the manuscript composition convention, phi is an inverse/right nonabelian cocycle. Its inverse psi satisfies the usual left cocycle law psi(tau sigma)=psi(tau) tau(psi(sigma)).',
  'proved there by the displayed comparison calculation',
  'C08 free-word reduction and computations.md §10; inversion reverses the product order. This is an exact symbolic certificate, not a commutative numerical test.',
  'E','Classical nonabelian descent; DM12 Thm3.2 uses the corresponding torsor formalism. The convention must be preserved when importing standard cocycle formulas.','Classical before the sheet','The written inverse cocycle is coherent and becomes a left cocycle on inversion.',['DM12'])
C(36,[442],[59],'971–974','the cocycle defines a torsor; A vérifier / OK',
  'The comparison cocycle defines a torsor by descent when its coefficients and semilinear action are defined over the stated descent field. For an arbitrary abstract automorphism group, algebraic effectivity and finite-type descent still require the usual descent data.',
  'proof sketched; marked à vérifier and subsequently OK',
  'C08 verifies the cocycle identity; computations.md §10 distinguishes that algebraic identity from effectivity of descent.',
  'B','DM12 Thm3.2 establishes the tensor-isomorphism torsor directly, giving a rigorous realization of the intended construction. It does not turn arbitrary discontinuous abstract cocycles into algebraic torsors without hypotheses.','1982; corrected text 2012','Established in neutral Tannakian descent; literal informal construction needs its coefficient/action hypotheses.',['DM12'])
C(37,[443],[59,61],'976–980;1027','period point generic iff the actual cocycle image is Zariski dense',
  'Let P be a geometrically integral finite-type torsor over a finitely generated subfield k0⊂k≅C, and alpha∈P(k). The Aut(k/k0)-orbit of alpha is Zariski dense in P iff alpha is k0-generic. Translating the orbit by alpha identifies this with density of the actual comparison-cocycle image in G_k.',
  'proof sketched; presented as a reformulation of a period conjecture',
  'computations.md §11 proves the orbit assertion by algebraic loci and extension of field embeddings. C15 shows the subgroup generated by an image can be dense while the image is not.',
  'B','BC16 Cor2.11 and Conj2.12 distinguish point closure from generated period torsors. The conditional orbit equivalence is elementary field theory; genericity itself is the period conjecture, not a consequence of it.','BC first preprint 2013; publication 2016','Equivalence valid with full Aut(k/k0), finite-type and geometric-integrality hypotheses. The general period genericity premise remains open.',['BC16','DM12'])
C(38,[444],[61],'1020–1024','phi(sigma)=(sigma g)^(-1)g replaces g^(-1)sigma g',
  'The right-cocycle coboundary associated to g is phi(sigma)=(sigma g)^(-1)g. The opposite expression is the inverse left-cocycle convention and cannot be substituted while keeping the manuscript’s multiplication order.',
  'corrected by himself later: old g^(-1)sigma g is replaced at L1020–1024',
  'C08 free-word certificate; computations.md §10 derives both conventions and shows which satisfies L944.',
  'E','Classical descent/coboundary convention; DM12 provides the torsor setting. No new cohomology theorem is claimed.','Classical before the sheet','Corrected formula is coherent; retain the deleted alternative as the author’s correction.',['DM12'])
C(39,[443],[61],'1027','the Galois orbit of the comparison matrix is generic',
  'The orbit of the chosen period/comparison matrix is generic in its motivic torsor precisely if the relevant Grothendieck period genericity conjecture holds. This assertion is stronger than generation of the torsor by the point.',
  'open on the pages; conjectural genericity assertion',
  'computations.md §11 establishes the equivalence, not the conjecture. No computed finite set can prove algebraic independence of arbitrary periods.',
  'C','BC16 Conj2.12 states full genericity over Qbar, while Cor2.11 and Prop2.13 separate weaker torsor-generation and cycle statements. No checked source establishes the general assertion.','Grothendieck note circulated 1963, publication 1966; BC 2013/2016','General genericity remains open. Modern partial results must be matched to the exact generated-torsor versus point-closure formulation.',['BC16','G66'])
C(40,[445],[59],'981','pi transcendental over k0',
  'The unfinished pi-transcendence qualification cannot be inferred merely from minimal transcendence degree of a curve’s field of definition: an elliptic curve with j=pi forces such a field to contain pi. The page concerns a motive, however, and passing from this curve test to minimal motivic descent needs an additional isogeny/descent argument not supplied by the j calculation.',
  'open on the pages; the sentence is unfinished',
  'C09 verifies j(E_j)=j for y²=x³−3j/(j−1728)x−2j/(j−1728); at j=pi the discriminant is nonzero. computations.md §11 explains the curve-level minimum1, and expressly does not identify it with a minimum for the motive.',
  'C','Grothendieck 1966 note10 and BC16 formulate period questions relative to specified coefficients/base fields. The independent elliptic-curve test exposes the missing qualification but does not by itself settle the unfinished motivic assertion.','Curve-level test checked2026-11-19; comparison sources1966 and2016','The curve-level unrestricted inference is false; the exact unfinished motivic formulation remains undetermined.',['G66','BC16'],'medium')
C(41,[446],[61],'1029–1035','homomorphisme total',
  'A semilinear comparison cocycle gives an ordinary homomorphism only after adjoining the automorphism action, into an appropriate semidirect product. The raw cocycle values in G alone need not form a homomorphism.',
  'stated without proof; target structure is implicit',
  'C08 and computations.md §10: (psi(sigma),sigma)(psi(tau),tau)=(psi(sigma) sigma(psi(tau)),sigma tau). Use the inverse convention if phi rather than psi is retained.',
  'E','This is standard semilinear descent in the tensor-isomorphism torsor setting of DM12. The manuscript does not specify the topology of the resulting enlarged group.','Classical before the sheet','Correct after the semidirect-product target and order conventions are explicitly supplied as reconstruction.',['DM12'])
C(42,[447],[61],'1035','closure of the total image should be open',
  'The page proposes an adelic/archimedean openness expectation. To formulate it one must specify the total target, topology, restricted product, and permitted arithmetic base field; a general motivic openness assertion also requires maximality hypotheses.',
  'open on the pages; tentative expectation',
  'C06 and computations.md §8 show the power-character obstruction to an unqualified finite-adelic version. No claim about a product topology involving G(C) is proved.',
  'C','CM20 treats precise integral and finite-adelic Mumford–Tate statements. It does not prove this unspecified total archimedean closure assertion. BC16’s Zariski-genericity statements concern a different topology.','CM first 2015, publication 2020; searches 2026-11-19','Partly identifiable: finite-adelic refinements are known in specific cases; the exact total statement remains unformulated.',['CM20','BC16'],'medium')
C(43,[448],[62],'1047–1058;1074–1078','phi_w(sigma)=sigma(g_infty) phi_v(sigma) g_infty^(-1)',
  'Changing the reference comparison by g_infty transforms the right cocycle by the displayed gauge formula. The inverse on the final factor is necessary; the earlier line missing it is deleted.',
  'proved there by cancellation; corrected by himself later at L1078 after deleted L1074',
  'C08 exact free-word simplification and computations.md §10; no commutativity assumption.',
  'E','Standard nonabelian coboundary equivalence, formulated in the torsor language of DM12. The correct order is independently verified against the source convention.','Classical before the sheet','Correct as written in the final live formula.',['DM12'])
C(44,[448],[62],'1063','sigma_l g_l sigma_l^(-1) sigma_l g_l^(-1)=sigma_l',
  'The finite comparison component cancels in the total semilinear expression, leaving the arithmetic automorphism sigma_l. This is a group-word identity, not a commutativity claim.',
  'proved there by the displayed cancellation',
  'C08 freely reduces the exact five-factor word; computations.md §10 records the action convention.',
  'E','Elementary group algebra; DM12 provides only the surrounding descent interpretation. The identity does not establish openness of the total image.','Elementary identity predating the sheet','Valid with the displayed order.',['DM12'])

# Auxiliary reused sheets and further claims are appended below; the package does not
# attribute their authorship or dating solely from the enclosing archival cote.

C(45,[473,474],[20],'38–40','Q=L0∩V′; P=projection(L0); P=Q+Zv′',
  'For type A_l in the hyperplane of R^(l+1) with coordinate sum zero, Q=Z^(l+1)∩V, P is the orthogonal projection of Z^(l+1), and P/Q is cyclic of order l+1 generated by v′=e1−(sum ei)/(l+1).',
  'stated without proof as an editorial instruction',
  'C10 computes v′ exactly for arbitrary symbolic l and example ranks; computations.md §12 proves the lattices and quotient order.',
  'B','Bourbaki Lie ChVI §4 no5(VIII), English pp218–219, contains this precise description. The publication match is verified; the contribution’s individual authorship is not.','Original French 1968; opened English translation 2002; draft circulation date unknown','Established formula; keep this reused root-system sheet separate from motivic claims.',['BourbakiLie4to6'])
C(46,[473],[20],'41–51','factorial divisions; gamma=(4l−2)(l+1); denominator 4; l=2 reducible',
  'These are edits to numbered formulas and tables in an absent root-system draft. The supplied leaf does not reproduce enough of those formulas to test the numerical corrections or all boundary cases.',
  'stated without proof; antecedent formulas absent',
  'No ungrounded numerical reconstruction. C10 checks only the separately explicit A_l and G2 formulas, not these missing tables.',
  'F','Bourbaki’s published root-system tables were located, but the exact draft numbers and normalizations are not established from the fragment. A comparison with the missing draft is still required.','Published book 1968; identification searches 2026-11-19','Unidentified at the level of the specific edits; not a modern open theorem.',['BourbakiLie4to6'],'low')
C(47,[475,476],[28,24],'210–226;113–115','proof supplied by Borel: P closed and P∩(-P)=empty',
  'In a finite crystallographic root system R, every subset P closed under root addition and disjoint from −P lies in the positive roots of some chamber. The proof uses absence of positive zero sums, a separating vector, and induction on rank.',
  'proof sketched across 18/028→024; literal zero-sum and summation-index slips interrupt its validity until interpreted as reading alternatives',
  'computations.md §12 independently proves the theorem by the zero-sum argument and convex separation, checking the nonreduced collinear case; the published four-step proof is collated separately. No scan emendation. C10 supplies only independent root-coordinate examples.',
  'B','The four-step argument is preserved in Bourbaki Lie ChVI §1 no7 Prop22, English pp176–177. Its complete zero-sum and excluded indices match the mathematical repairs suggested by the manuscript.','French 1968; draft attributed to Borel on the sheet; exact earlier circulation unknown','The theorem and repaired argument are established; the supplied diplomatic reading remains unchanged.',['BourbakiLie4to6'])
C(48,[477],[26],'173','contract an order-3 edge by replacing xi,xj with xp',
  'For a positive-definite finite Coxeter graph, contracting an edge of order 3 and retaining adjacent edge labels gives another positive-definite Coxeter form. In a tree, no external vertex is adjacent to both endpoints.',
  'proof sketched as an editorial explanation',
  'computations.md §12 restricts the quadratic form to xi=xj=xp: the diagonal coefficient is 2−2cos(pi/3)=1. Positive definiteness is inherited by restriction.',
  'B','Bourbaki Lie ChVI §4 no1 Lem6, English pp202–203, contains the precise contraction and quadratic-form argument.','French 1968; opened English 2002','Valid under the finite positive-definite/tree hypotheses, which are supplied by the missing draft context and stated in the reconstruction.',['BourbakiLie4to6'])
C(49,[478],[26],'181','labels 5 or p≥7 cannot come from root systems',
  'For a crystallographic finite root system, the Coxeter orders of pairs of simple reflections belong to {2,3,4,6}; thus H3,H4 and dihedral I2(m) with m=5 or m≥7 are noncrystallographic.',
  'stated without proof; a reference and later realization argument are requested',
  'C10 and computations.md §12: a_ij a_ji=4cos²(pi/m) is an integer in {0,1,2,3}; monotonicity excludes m≥7 and exact irrationality excludes m=5.',
  'B','Bourbaki Lie ChVI §2 no5 Remark2, English pp193–194, and §4 classification give the precise criterion.','French 1968; mathematical criterion classical before publication','Established. This does not decide the author’s separate doubts about absent Lemmas3–4.',['BourbakiLie4to6'])
C(50,[479],[30],'251–257','u=Ab,v=bA; bAa→baA→aAb→Aba',
  'Coxeter transformations in a finite reflection group are conjugate. The displayed local word moves use commutation of generators at unlinked vertices and cyclic permutation, which is conjugation; the proof needs the finite forest structure.',
  'proof sketched as amendments to an absent longer proof',
  'computations.md §12 verifies each of the three displayed moves and describes the forest induction. It does not infer conjugacy from connectedness alone for arbitrary graphs.',
  'B','Bourbaki Lie ChV §6 no1 Prop1 and Lemma1, English pp121–122, supplies the finite-forest proof. The accessible OCR has a commutes/conjugate corruption in the lemma statement; its proof and manuscript moves determine the intended hypothesis.','French 1968; opened English 2002','Established in the finite reflection-group setting. The local word calculation is valid with its stated commutation condition.',['BourbakiLie4to6'])
C(51,[480],[30],'259','(ii) is false with G reducible',
  'The source instructs that an unspecified proposition on exponents retain only (ii),(iii) and assume irreducibility. Since (ii) itself is absent, its exact false reducible form cannot be extracted.',
  'corrected by himself later within the editorial instruction; original assertion not supplied',
  'No invented counterexample to an unknown formula. Published Coxeter exponents are inspected only as a lead.',
  'F','Bourbaki Lie ChV §6 separates irreducible exponent statements and reducible product behavior. No one-to-one match of the draft’s (ii) has been verified.','French 1968; searches 2026-11-19','The need for some irreducibility restriction is recorded, but the exact claim remains unidentified.',['BourbakiLie4to6'],'low')
C(52,[483],[46],'656–660','each coset of p^n Z_p has measure p^(-n)',
  'Normalized additive Haar measure on Q_p, with mass1 on Z_p, gives every coset of p^nZ_p mass p^(−n), and these masses determine it.',
  'stated without proof in the surviving beginning, which continues an earlier page',
  'C15 and computations.md §13: partition Z_p into p^n equal cosets; negative n follows by finite index in the opposite direction; compact-open cosets determine a Radon measure.',
  'B','Bourbaki Intégration ChVII §1 no6, Example, French pp27–28, is an exact published continuation; official metadata dates the volume to1963.','French 1963; draft date unknown','Established; archival placement does not establish individual authorship.',['BourbakiHaar63'])
C(53,[483],[46],'662–664','local translation-invariant positive measure extends uniquely',
  'A nonzero positive Radon measure on an open subset V of a locally compact group G, invariant under every translation that remains inside V, extends uniquely to a left Haar measure on G.',
  'proved there by translating and gluing measures on overlapping open sets',
  'computations.md §13 checks overlap compatibility, global translation invariance, nonzero mass and uniqueness. Positivity/Radon convention is required.',
  'B','The same proof is Bourbaki Intégration ChVII §1 no7 Prop9, French p28; the draft calls it Prop7.','French 1963; draft circulation date unknown','Established, with a verified renumbered publication match.',['BourbakiHaar63'])
C(54,[483],[46],'666–668','local isomorphism carries Haar measure to a unique Haar measure',
  'A local group isomorphism between identity neighborhoods transports the restriction of a Haar measure to the restriction of a unique Haar measure on the target group.',
  'proof sketched but cut off at the bottom of the supplied sheet',
  'computations.md §13 completes the local-neighborhood argument, then translates a smaller neighborhood to cover the original neighborhood.',
  'B','Bourbaki Intégration ChVII §1 no7 Corollary, French pp28–29, includes the missing final paragraph.','French 1963; draft date unknown','Established; the missing manuscript continuation is found in the published text.',['BourbakiHaar63'])
C(55,[484],[48],'719–731','e(v_i/v)=v_i(a)',
  'For a Dedekind-domain extension A⊂B and pB=∏p_j^e_j, localizing at p_i kills the other factors. If a is a uniformizer of A_p and v_i is normalized on B_p_i, then v_i(a)=e_i.',
  'proved there by localization of the ideal factorization',
  'computations.md §14 derives p_jB_p_i=B_p_i for j≠i and compares powers of the local uniformizer; C11 illustrates the valuation arithmetic.',
  'E','Milne ANT §3, factorization in extensions, p59, and Remark7.43 p124 state the same normalized valuation relation. The exact Bourbaki draft number392 has not been independently dated.','Classical Dedekind theory; checked exposition version2020','Valid with Dedekind/local-DVR hypotheses.',['MilneANT20'])
C(56,[487],[52],'792–800','A0 and A are completions of A and K for ideal topology',
  'For a nonfield Dedekind domain A with fraction field K, the product of local valuation-ring completions is the completion of A for its nonzero-ideal topology, and the restricted product of local fraction fields is the corresponding completion of K. The diagonal K is additively dense.',
  'proof sketched from earlier approximation and completion propositions',
  'computations.md §14 proves CRT density, common-denominator reduction and completeness. The restricted product is essential; the full product used on18/047 is a different object.',
  'E','Milne ANT Prop3.28 supplies CRT approximation. MathOverflow points to Bourbaki Algèbre commutative VII §2 no4, but that exact published text has not yet been collated; publication metadata alone is not a theorem verification.','Classical; Bourbaki volume1964–65, precise draft chronology unknown','Valid for the stated restricted product; not an identification with an unrestricted product of Q_l.',['MilneANT20','BourbakiAC65'])
C(57,[485,512],[50],'758–760','SL(n,K) dense in SL(n,A)',
  'For the restricted finite adele ring of a Dedekind domain and n≥2, diagonal SL_n(K) is dense in SL_n(A). For n=1 the statement is trivially true.',
  'proved there using additive approximation, elementary matrices and density of finite-support elements; one bibliography slot is blank',
  'computations.md §14 supplies Gaussian-elimination generation over each local field and checks restricted-product density. No strong approximation for G_m follows.',
  'E','The exact printed locator Bourbaki Algèbre commutative VII §2 no4 Prop4 was found through MathOverflow; full printed theorem was not collated at this stage. The supplied proof is independently checked and Milne’s CRT approximation supplies its arithmetic input.','Bourbaki volume1964–65; theorem’s earliest circulation not established','Established by the independently rechecked proof; blank draft citation remains a bibliographic alarm.',['MilneANT20','BourbakiAC65'])
C(58,[486],[50],'764–766','finitely generated torsion module has finite length',
  'If A is a noetherian domain whose nonzero primes are maximal, every finitely generated torsion A-module has finite length.',
  'proof sketched via associated primes and a cited earlier proposition',
  'computations.md §14: a common nonzero annihilator makes the support finite and zero-dimensional; a prime filtration has only maximal prime quotients. No normality hypothesis is needed.',
  'E','Stacks Lem10.62.1 gives a finite prime filtration; Lem10.62.3 is the local support criterion. The general statement follows by the displayed finite filtration.','Classical module theory; checked Stacks2026','Valid for the exact stated noetherian one-dimensional-domain hypotheses.',['StacksSupport','StacksLength'])
C(59,[486],[50],'768–770','length of filtered union equals supremum of lengths',
  'For a directed increasing family of submodules T_i with union T, length(T)=sup_i length(T_i), allowing infinity.',
  'proof sketched; the last sentence continues beyond the supplied sheet',
  'computations.md §14: unbounded case is immediate; in the bounded case choose maximal finite length and use directedness and additivity to show every larger common stage equals it, hence contains all T_i.',
  'E','Stacks §10.52 gives length and additivity; the directed-union assertion is independently proved from those definitions. No noetherian assumption is needed.','Classical module theory; checked2026','Valid as stated.',['StacksLength'])
C(60,[488],[56],'909–921','every nonzero ideal has a unique factorization into maximal ideals',
  'Every nonzero integral ideal of a Dedekind domain factors uniquely as a finite product of nonzero prime ideals; fractional ideals form the free abelian group on those primes.',
  'proof sketched using localization, valuation exponents and finite support',
  'C11 and computations.md §14: local DVR exponent determines each factor, and equality is checked after all maximal localizations.',
  'E','Milne ANT Thm3.7 pp49–50 and Thm3.20 p53 give the integral and fractional versions. Stacks Lem10.120.17 verifies the local-DVR characterization.','Classical Dedekind theory; modern checked exposition2020','Established. The unnamed equivalent conditions on another fragment are not reconstructed from this theorem.',['MilneANT20','StacksDedekind'])
C(61,[487],[54],'842–849','ideal product, quotient, sum and intersection valuations',
  'For nonzero fractional ideals I,J of a Dedekind domain, v_p(IJ)=v_p(I)+v_p(J), v_p(I:J)=v_p(I)−v_p(J), v_p(I+J)=min and v_p(I∩J)=max of the two exponents.',
  'proved there by localization at each maximal ideal',
  'C11 gives exact integer-exponent checks; computations.md §14 proves the formulas in a DVR and globalizes by localization.',
  'E','Milne ANT Thm3.20 and Cor3.13 supply the factorization/localization framework. The arithmetic equalities are independently re-proved.','Classical Dedekind ideal theory','Valid for fractional ideal quotient; an integral truncated quotient would require max(0,a−b), a different convention.',['MilneANT20'])
C(62,[487],[54],'853–865','approximate finitely many values and remain integral elsewhere',
  'For a Dedekind domain A, its fraction field K, distinct nonzero primes p_i and targets x_i∈K, one can find x∈K with arbitrarily large v_p_i(x−x_i) and v_q(x)≥0 for every other prime q.',
  'proof sketched in the special case that all targets are integral; the general reduction is not on the supplied leaf',
  'computations.md §14 gives the missing common-denominator CRT reduction, including congruences at extra denominator primes. C11 checks a concrete rational example.',
  'E','Milne ANT Prop3.28 p56 is the integral CRT case. The fractional-target extension with integrality elsewhere is independently proved here; no completeness assumption is required.','Classical approximation theorem; checked2026','Valid under the Dedekind hypotheses; manuscript proof is incomplete only at the fractional-target reduction.',['MilneANT20'])
C(63,[488],[58,56],'966–968;907','a semilocal Dedekind domain is principal',
  'A Dedekind domain with finitely many maximal ideals is a principal ideal domain.',
  'proof sketched across the out-of-order leaves58→56',
  'computations.md §14 chooses an element with prescribed valuation at each of the finitely many primes by CRT; it generates the given ideal. The field case is immediate.',
  'E','Milne ANT Cor3.14 p51 gives this exact semilocal statement and CRT proof.','Classical Dedekind theory; checked exposition2020','Established; continuation order is certain from the sentence and proof.',['MilneANT20'])
C(64,[488],[58],'956–964','conditions a)...g) equivalent',
  'The fragment proves implications among labels a through g, but the actual seven conditions are absent. It is not legitimate to substitute one of the familiar lists of characterizations of Dedekind domains.',
  'proof sketched for unidentified conditions',
  'No calculation is possible without the conditions. computations.md §14 checks only the separately explicit claims on adjacent leaves.',
  'F','Stacks Lem10.120.17 and Milne §3 provide modern equivalent conditions, but neither establishes that its list is this missing a–g list.','Searches2026-11-19','Unidentified source fragment, not an unresolved theorem.',['StacksDedekind','MilneANT20'],'low')
C(65,[489],[60],'987–1015','G2 simple roots; highest root3alpha1+2alpha2',
  'For the displayed G2 simple-root convention with alpha1 short and alpha2 long, the positive roots are alpha1,alpha2,alpha1+alpha2,2alpha1+alpha2,3alpha1+alpha2,3alpha1+2alpha2; the last is the highest root.',
  'stated with a diagram and coordinates; proof not supplied',
  'C10 exact coordinates, lengths, Cartan entries, six positive roots and highest root; computations.md §12 describes the convention.',
  'B','Bourbaki Lie PlateIX, English pp289–290, records the same highest-root convention.','French1968; draft n383 date unknown','Established; the drawing alone must not be used to reverse the short/long labels.',['BourbakiLie4to6'])
C(66,[481],[44],'597–599','X(V*,K_n*) is polynomial of degree at most s',
  'An anonymous English proof fragment deduces polynomial growth of an Euler-characteristic-like function from a first difference of degree at most s−1. The sheaf, twisting sequence, dimension s and induction hypotheses are not supplied.',
  'proof sketched as the end of an absent induction',
  'computations.md §15 verifies only the elementary finite-difference implication over characteristic zero. No specific geometric Hilbert polynomial is identified from the initials.',
  'F','Exact phrase searches, Numdam/zbMATH-directed queries and broader Hilbert-polynomial searches did not identify the document. A general Hilbert polynomial theorem would not determine this fragment’s author or assumptions.','Searches2026-11-19','The finite-difference step is valid under its natural assumptions; the geometric claim and source remain unidentified.',[],'low')
C(67,[481],[44],'601–614','direct-image maps are isomorphisms away from the singular locus',
  'In the anonymous fragment, f is said to be an isomorphism over V minus its singular locus, and induced sheaf maps are consequently isomorphisms on that open set. Exact maps depend on missing definitions of K,K′,K*. ',
  'proof sketched by restriction to an isomorphism locus',
  'computations.md §15 checks the formal restriction argument only, not the unavailable construction of f.',
  'F','The same exact-source searches as CL-SA07-466 were unsuccessful. No attribution or birational-resolution theorem is manufactured.','Searches2026-11-19','The local formal inference is sound if the asserted isomorphism and sheaf identifications hold; the full claim is unidentified.',[],'low')
C(68,[482],[45],'632–649','Čech H^q(F)(X)=Čech H^q(C-hat_/X,F)',
  'A site/Čech-cohomology definition or identification is written in a wholly deleted block. The category, presheaf convention, and comparison map are not developed in the supplied fragment.',
  'corrected by himself later: entire block is deleted on the same sheet',
  'No computation warranted; the insertion says presheaf and is retained as evidence of the abandoned formulation.',
  'F','Site-cohomology searches found Giraud64 §1, especially the distinct derived-functor definitions and comparison spectral sequences(1.12)–(1.14). These distinguish presheaf Cech constructions from sheaf cohomology but do not identify the deleted formula or recover its absent conventions. A general Cech-to-sheaf-derived comparison cannot be imported without its hypotheses.','Giraud lectureMay1963/publication1964; identification searches2026-11-19','Withdrawn fragment. Do not promote it to a theorem or new research problem without restoring its definitions.',['Giraud64'],'low')
C(69,[414],[35,40],'347–357;512–526','H^{*|0}(X(R),Q)=V^f; later X_top=X(C)/pi',
  'For a finite group acting on a triangulable space, rational cohomology of the orbit space identifies with invariant rational cohomology. The analogous claim for the fixed real locus is false; the manuscript’s earlier X(R) notation is ambiguous and its later display explicitly uses the quotient.',
  'stated without proof; earlier notation admits a false usual-fixed-locus reading, later quotient display is explicit',
  'computations.md §2: P¹_R gives H¹(RP¹,Q)=Q while H¹(CP¹,Q)^f=0; Spec C/R gives an empty real locus but H⁰ invariants Q. Averaging on an equivariant subdivision proves the quotient formulation.',
  'E','Finite-group averaging is classical; FOT08 §3.3 Thm3.27 gives the quotient statement and Thm3.28 proves the cochain averaging identity, attributing the quotient theorem to Bredon. Deligne’s Hodge theory concerns the complex realization and does not supply a fixed-locus identification; real section results such as Wickelgren concern a different invariant.','Classical topology; opened monograph2008; checked2026','Quotient statement valid under the stated hypotheses; no choice of * versus0 salvages the usual fixed-locus reading in both examples.',['FOT08','D71','Wickelgren12'])
C(70,[421],[40,41],'529–555','H^(p,q)(X)⊂F^pH^q(X)',
  'The Hodge summand obtained from H^q(X,Omega^p) lies in total degree p+q. The printed target H^q can be correct only with an unstated reindexing of q as total degree.',
  'stated without proof; literal total-degree mismatch',
  'computations.md §2 checks the spectral-sequence bidegree convention; no source text is changed.',
  'B','Deligne Hodge II §2.2.1–3 gives the total-degree convention. This supports a mathematical alarm, not an ink decision.','1971','Expected target is F^pH^(p+q); retain the diplomatic q until scans are checked.',['D71'])
C(71,[419],[38],'445–465','normalizer of maximal compact; passes to G/i(G_m)',
  'The entire maximal-compact/normalizer discussion is deleted, including a scalar quotient. It is not a surviving assertion that a proposed compact subgroup is maximal or self-normalizing.',
  'corrected by himself later: whole paragraph deleted, not only its first sentence',
  'No positive theorem is reconstructed. The live Hodge-torus conjugation equation is checked separately in CL-SA07-414.',
  'F','Deligne’s Hodge and polarization framework and DM12 Tannakian theory explain nearby objects, but no exact retained compact-group theorem remains to identify.','Searches2026-11-19','Withdrawn; historical interest only until a corrected version is located.',['D71','DM12'],'medium')
C(72,[415],[38],'429–439','R(gamma)=R(beta,gamma)=R(beta,alpha)=R(alpha)',
  'If beta is a rational point of the indicated real torsor and alpha and gamma determine one another algebraically using beta, then adjoining coordinates of alpha or gamma to R gives the same field. The local sheet does not repeat all earlier definitions.',
  'proof sketched through beta∈Q(R)',
  'computations.md §2 explains the two inverse coordinate-field inclusions. The displayed gamma/sigma reading and exact torsor notation stay uncertain.',
  'E','This is elementary coordinate-field invariance under an R-defined torsor translation, within the formalism of DM12 Thm3.2. The exceptional-case classification invoked afterward is separately false in the natural category.','Classical torsor algebra; checked2026','Conditional field equality is valid; it does not rescue the even-Tate classification.',['DM12'],'medium')
C(73,[418],[36],'393','central f_infty iff G commutative; Q tordu and Q(2)',
  'The marginal equivalence among centrality of real Frobenius, a generator called Q tordu, and commutativity cannot be fixed without the missing generator and character conventions.',
  'open on the pages; multiple uncertain words in a marginal assertion',
  'computations.md §2 tests the ordinary Tate category: f is central and nontrivial in G_m. This constrains possible readings but does not select one.',
  'F','DM12 and Deligne’s Tate convention show why distinguished characters matter. Searches did not identify an exact published formulation of this margin.','Searches2026-11-19','Unidentified margin; no unqualified centrality theorem is claimed.',['DM12','D71'],'low')
C(74,[470],[18],'5–9','formal maps to M are linear maps U(V)→M vanishing on U0',
  'For a formal affine space whose coordinate algebra is the completed symmetric dual of its filtered distribution coalgebra, pointed formal maps to a finite free module M correspond to linear coefficient maps from distributions to M that vanish on degree zero, subject to the source’s topological-module conventions.',
  'proof sketched by choosing a chart and referring to an absent earlier remark',
  'computations.md §16 writes the homogeneous coefficient correspondence and explains the finite-free/completion conditions; no assertion for arbitrary nonseparated modules is made.',
  'E','Cartier §4 and Dieudonné pp208–209 provide the dual distributions/formal-series framework. Exact notation P-hat for arbitrary separated modules belongs to the missing draft.','1956','Valid in the finite-free standard setting; the most general stated module context requires the absent definitions.',['Cartier56','Dieudonne56'],'medium')
C(75,[438,447],[53,61],'815–834;1035','Gal(k/k0) acts semilinearly; finite part factors through algebraic Galois',
  'For k≅C of infinite transcendence degree over finitely generated k0, the page’s Gal(k/k0) means full field automorphisms. Its l-adic arithmetic action factors through Gal(k0bar/k0), whereas the de Rham scalar action remains semilinear on k.',
  'stated without proof; the nonalgebraicity of k/k0 is explicitly underlined',
  'computations.md §10 separates the restriction map from the full automorphism group and its semidirect action. This prevents a false profinite interpretation of the archimedean orbit.',
  'B','DM12’s arithmetic/geometric exact sequences and BC16’s period-torsor setup supply the modern separation. Neither identifies the full abstract automorphism group with an absolute Galois group.','1982/2012; BC2013/2016','The distinction is correct and essential to the generic-orbit argument.',['DM12','BC16'])
C(76,[473],[20],'41','lift W and compute symmetric invariants before restricting',
  'For type A_l, the Weyl group acts as S_(l+1) on coordinate space and preserves the zero-sum hyperplane. Its invariant algebra on that hyperplane is generated by symmetric polynomials of degrees2,…,l+1; averaging requires the factorial denominator over characteristic zero.',
  'stated without proof as an editorial instruction; the precise targeted factorial line is absent',
  'computations.md §12 gives the elementary-symmetric-polynomial restriction and explains averaging. It does not certify the absent numbered coefficient.',
  'B','Bourbaki Lie ChVI §4 no5(IX)–(X), English p219, contains the lifting and invariant-ring computation.','French1968','The reconstructed invariant calculation is established; the exact draft factorial correction remains CL-SA07-446.',['BourbakiLie4to6'])
C(77,[477,494],[26],'173–177','one branch point with all labels3, or a chain with at most one larger label',
  'For a connected finite Coxeter graph, either it is a chain with at most one edge of order≥4, or it has a unique trivalent vertex and all edges have order3. The editorial source omits the finite/positive-definite setup but it is present in the published classification argument.',
  'stated without proof on this sheet; neighboring Lemmas3–4 are explicitly doubted',
  'computations.md §12 uses positive-definite Gram submatrices, order3 contraction, and the star/path obstruction. It does not identify the absent draft Lemmas3–4.',
  'B','Bourbaki Lie ChVI §4 no1, English pp201–204, contains the finite-graph setup and contraction lemmas leading to this alternative.','French1968','Valid under the stated finite irreducible Coxeter hypotheses; not a statement about arbitrary Coxeter graphs.',['BourbakiLie4to6'])
C(78,[479],[30],'245','d has leading monomial e^(w0), so one coefficient is1',
  'The fragment refers to divisibility by a non-zero-divisor d and a leading-monomial argument in a group algebra. The definitions of Qe^x, w0, the order, and assertion(ii) are missing.',
  'proof sketched as a continuation from an absent page',
  'No formula is supplied from which the claimed unique coefficient can be independently computed.',
  'F','Bourbaki Lie ChVI §3 on exponential invariants was searched as the likely publication context. Exact equality with a specific Weyl-denominator proposition was not established.','Searches2026-11-19','Unidentified continuation; retain as part of the complete census rather than filling it from a remembered formula.',['BourbakiLie4to6'],'low')

C(79,[415],[36],'374–381','epsilon(f_infty)=-1, hence alpha not real if M contains Tate',
  'If the tensor category contains the ordinary Tate object and epsilon is its character, geometric real Frobenius has epsilon(f_infty)=−1. Hence f_infty≠1 and the distinguished comparison point is not R-rational.',
  'proved there by the displayed Tate sign and point criterion',
  'C01,C03 and computations.md §2: complex conjugation reverses orientation on P¹(C), so acts by−1 on H² and its Tate generator.',
  'E','The sign is encoded in Deligne §2.1.13–14. It does not imply the tensor-isomorphism torsor has no other real point.','Classical orientation fact; published convention1971','Correct with the explicitly included ordinary Tate object.',['D71','DM12'])
C(80,[407],[29],'237','all elements primitifs|possibles obtained by varying topology',
  'The claim about all primitifs or possibles in H¹(P¹,Omega¹) cannot be fixed because the noun is uncertain and no target set is specified. In a fixed algebraic basis, the displayed comparison coefficient is an automorphic image of (2πi)^−1 and therefore cannot range over all nonzero algebraic scalars.',
  'stated without proof; decisive word uncertain',
  'computations.md §1 records invariance of algebraic/transcendental status under field automorphisms. This is a restriction on reconstructions, not an ink decision.',
  'F','Grothendieck’s comparison and Deligne’s Tate convention verify the scalar model but do not identify this indefinite target set. Exact phrase searches did not locate a published version.','Searches2026-11-19','Unidentified quantifier/reading; do not silently replace it by every nonzero vector.',['G66','D71'],'low')

C(81,[447],[61],'1035','the kernel of the finite arithmetic representation still has dense archimedean image',
  'Assume the comparison point is generic in a geometrically integral finite-type torsor over finitely generated k0, inside k≅C. Its orbit under Aut(k/k0bar) remains Zariski dense, because k0bar/k0 is algebraic. If the finite realization factors through Gal(k0bar/k0), the kernel of that realization contains this subgroup and therefore also has Zariski-dense archimedean cocycle image.',
  'stated without proof under the surrounding period-genericity conjecture; separate from the tentative topological openness in the same paragraph',
  'computations.md §§8,11: apply the generic-orbit proof over the algebraic closure of the coefficient field. This proves a conditional Zariski-density implication, not adelic or analytic openness.',
  'C','BC16 Conj2.12 identifies the missing arithmetic period-genericity premise. BT22 Thm4.25 is a geometric/function-field result and does not remove that premise. The kernel inclusion follows from the arithmetic realization, not from treating full Aut(k/k0) as profinite.','BC first2013/publication2016; BT first2022/publication2025','Conditional implication valid; general arithmetic genericity remains open. Target topology and finite-realization factorization must be explicit.',['BC16','BT22'],'high')

def save():
    for c in claims:
        c['class']=c.pop('class_',c.get('class'))
    (P/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':
    save()
    print(f'Saved {len(claims)} manually authored claim records.')
