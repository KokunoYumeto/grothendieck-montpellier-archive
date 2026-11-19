#!/usr/bin/env python3
"""Manually composed claim map. No heading-driven verdict generation."""
from pathlib import Path
import json
P=Path(__file__).parent
claims=[]
def add(title,file,scans,lines,words,statement,page_status,verification,fate,cls='B',refs=(),confidence='high',author='Grothendieck or unattributed working hand'):
    claims.append(dict(id=f'C-SA23-ega-{len(claims)+1:03d}',title=title,source=f'sources/texts/{file}_transcription.tex',cote='26' if file.endswith('H26-01') else ('22' if file.startswith('codex/K22') else '23'),scans=scans,lines=lines,his_words=words,modern_statement=statement,page_status=page_status,present_check=verification,literature_fate=fate,classification=cls,references=list(refs),confidence=confidence,author=author,present_status_date='2026-11-19'))
J='Jean-Pierre Jouanolou (printed offprint); handwritten annotations separately attributed to the archival working hand'
K='codex/K22-01';L='codex/K22-02';E='codex/K23-06';N='codex/K23-01';Q='codex/K23-02';D='codex/K23-03';V='codex/K23-04';W='codex/K23-05';H='codex/H26-01'
add('Differential Tor criterion for a reduced quotient',K,'2','13–27','D(A) ... Tor ... A/a',
 'For an equicharacteristic regular noetherian local A with flat absolute differential module and reduced B=A/a, the intended criterion compares regularity of B with Tor_i^B(k,Omega_B); when Omega_A is free it also compares freeness of Omega_B. The surviving printed D(A) under a B-Tor is not silently substituted.',
 'stated without proof; handwritten correction of differential argument',
 'The B-module structure on Omega_A is not generally available. The annotation supplies A/a at the first occurrence; the repeated occurrence remains a reading alarm. The corrected criterion is a substantive differential regularity theorem, not established just by correcting its type.',
 'The article itself is a 1963 publication by Jouanolou. Modern geometric regularity criteria are in Stacks07EK; their hypotheses do not automatically verify the entire offprint criterion for arbitrary infinite differential modules. Exact historical proof comparison remains unverified.', 'C', ['Jouanolou1963Etude','Stacks07EK'],'medium',J)
add('Finite p-degree analytic and locality differential criteria',K,'2','29–35','Pour que A soit régulier ... D(A) soit libre',
 'The three corollaries concern reduced analytic localizations over a complete valued field of characteristic p and finite p-degree; reduced localities; and analytically reduced local noetherian rings in characteristic p with finite separated differential module. Their stated finiteness and reducedness assumptions are distinct.',
 'stated without proof',
 'The source does not assert a criterion for every noetherian ring. Nakayama applies only to the finite separated module in Cor3. The different hypotheses are retained individually rather than merged into unrestricted freeness implies regularity.',
 'Jouanolou attributes the locality case to Kunz and the separated-module case to Suzuki/Mount. Exact predecessor titles are retained in the offprint bibliography; no priority date is inferred from the annotation.', 'C',['Jouanolou1963Etude'],'medium',J)
add('Openness of singular loci under differential hypotheses',K,'2','37–45','le lieu singulier ... est fermé',
 'Proposition2: a global equicharacteristic regular ring A with free absolute differentials has closed singular locus in every affine A-algebra. Proposition3 applies to finite-type schemes over a regular group scheme over a perfect field. The latter does not state that the group scheme is finite type.',
 'stated without proof; skeptical annotation on group-scheme application',
 'The finite-type-over-perfect-field case follows from the Jacobian criterion. Without a convention making the group scheme locally of finite type/noetherian, the annotation correctly asks for missing scope. It is not a counterexample on its own.',
 'Modern J-2/excellence formalizes closed singular loci. The arbitrary group-scheme extension is not verified by finite-type Cartier smoothness.', 'C',['Jouanolou1963Etude','Stacks07EK'],'medium',J)
add('Completion and differentials with semifinite module',K,'3','52–60','D(A) ... somme directe ... libre ... type fini',
 'For noetherian local A, the completion differential kernel lies in the intersection of completed submodules with finite quotient. If Omega_A is a direct sum of a free and a finite module, the natural conormal sequence for A→Ahat is left exact.',
 'lemma and deduction stated without proof',
 'The displayed middle term (Ahat) has lost Omega/D. The intersection vanishes for semifinite modules: separate each finite set of free coordinates and the finite summand, then use faithful flatness of completion. The kernel-containment lemma itself requires extension of derivations to finite complete modules.',
 'This is a continuous-derivation argument and is distinct from universal injectivity without finiteness. Source mutation cannot be settled without ink.', 'B',['Jouanolou1963Etude'],'medium',J)
add('Separable generic extension after completion',K,'3','64–74','K_Ahat est séparable sur K_A',
 'For the stated analytically integral locality/analytic power-series situations, the completed fraction field is separable over the original fraction field. In particular Frac K[[X_1,...,X_n]] is separable over K(X_1,...,X_n). A regular local k-algebra with separable residue field has separable fraction field.',
 'stated without proof, with Cohen-structure reduction',
 'The last claim follows from geometric regularity at the closed point and generization; the fraction-field notation in several variables means the fraction field of the power-series ring, not an iterated Laurent-series topology.',
 'The local geometric regularity theorem and its localization consequences give the modern form; see Stacks07EK/07NQ. Analytic coefficient hypotheses remain as printed.', 'B',['Jouanolou1963Etude','Stacks07EK','Stacks07NQ'],'high',J)
add('C1 fraction field of one-variable convergent series',K,'3','66–70','K_A est quasialgébriquement clos (C1)',
 'For a complete algebraically closed valued field k, the fraction field of the one-variable convergent-series ring k{T} is C1. The source raises a possible gap in Lang’s proof.',
 'stated without proof; possible prior proof gap',
 'The sheet does not give the alleged gap or a self-contained proof; treating an arbitrary number of variables as C1 would be an overstatement.',
 'Attributed to Lang, Annals55(1952),373–390. Exact gap has not been independently identified. This is a historical verification task, not an unresolved modern C1 claim.', 'E',['Lang1952'],'medium',J)
add('Analytic reducedness lemma needs an injective finite extension',K,'3–4','78–105','faux si ... A→B injectif ??; C⊃A !!!',
 'Intended lemma: an analytically integral local A with separable generic formal fibre has analytically reduced localizations of finite integral-domain extensions B containing A. The printed theorem omits the injection and also mixes generic characteristic0 with hypotheses needed after passing to quotients.',
 'stated without proof; explicit objections in margins',
 'The finite inclusion case follows by embedding Bhat in a finite algebra over Frac(Ahat) and separability. A quotient B=A/q is not such an inclusion. Generic characteristic0 is localization-stable, so the isolated word faux must not be turned into a claim that characteristic changes under localization; the missing quotient/formal-fibre hypotheses are the actual risk.',
 'Modern Nagata/G-ring criteria distinguish generic formal fibres from all formal fibres. The whole printed theorem is not certified by the valid inclusion argument.', 'C',['Jouanolou1963Etude'],'high',J)
add('Finiteness of normalization from the generic formal fibre',K,'4','109–118','fermeture intégrale ... module de type fini',
 'An analytically integral noetherian local A whose completed fraction field is separable over Frac A has finite integral closure in every finite extension of Frac A. The applications to localities, analytic localities, and regular Hopf algebras have separate scope.',
 'stated without proof; marked known (Nagata), question by Hopf application',
 'The proposition is not the claim that every analytically irreducible ring is universally Japanese; separability of the generic formal fibre is retained. The Hopf application is not licensed merely by the word regular.',
 'The source explicitly attributes prior knowledge to Nagata. Nagata Local Rings(1962) is a predecessor lead; the exact general Hopf application remains unverified.', 'E',['Nagata1962','Jouanolou1963Etude'],'medium',J)
add('Two cotangent-space sequences and quasi-separability',K,'6–7','161–197','D_A(B)=0; n=n²+mB',
 'For a local injection A→B, separable residual extension gives the left-exact cotangent sequence n/(n²+mB)→Omega_B/A⊗L_b→Omega_Lb/La. In residual characteristic p the alternative denominator is n²+(n∩A[B^p])B. Vanishing of Omega implies the displayed ideal relations and relative perfection of residue fields; the converses require finite generation of Omega.',
 'stated with predecessor reference, deductions sketched',
 'The finite-generation condition is needed for Nakayama. n=n²+mB implies n=mB when n is finitely generated, but equality of maximal ideals alone does not imply modern unramifiedness without the residual/finite-type hypotheses.',
 'Modern cotangent exact sequences and formally unramifiedness distinguish Omega=0 from finite-type unramifiedness. The handwritten non ramifiée is terminological, not an equivalence without hypotheses.', 'B',['Jouanolou1963Differentielles','Stacks00TH'],'high',J)
add('Noetherian quasi-separable algebras and absolute flatness',K,'7','199–213','tout idéal premier ... maximal ... absolument plat',
 'A noetherian k-algebra with Omega_A/k=0 is a finite product of algebraic field extensions in characteristic0; in characteristic p the corresponding statement uses separable or finitely generated residue fields. Without noetherianity, the stated residual hypotheses imply all primes maximal and the reduced ring absolutely flat.',
 'stated without proof',
 'In characteristic p, a perfect field extension can have positive transcendence degree but zero differentials. The printed residual finiteness/separability clauses must not be removed. Reduced zero-dimensional commutative rings are von Neumann regular.',
 'Established through formally unramified field extensions and absolutely flat rings; matches cote23/073 only after reduction.', 'B',['Jouanolou1963Differentielles'],'high',J)
add('Rank criterion for freeness of a finite differential module',K,'7–8','215–244','D_A(B) ... libre ... dim ...',
 'For the printed local domain injection with finite relative differential module, Omega_B/A is free iff its minimal generator number equals its rank over Frac B. Cotangent-space formulas express this as the two displayed dimension equalities. The locality corollary assumes both generic and residual separability over k.',
 'proof implicit in cited exact sequences',
 'A surjection B^r→Omega of equal generic rank has torsion kernel; the kernel is a submodule of the torsion-free free module over the domain B, hence zero. This verifies the finite-module algebra behind the criterion.',
 'Standard finite-module rank/Nakayama argument; specific differential input appears in Berger–Kunz and Jouanolou1963.', 'E',['Jouanolou1963Differentielles'],'high',J)
add('Homological dimension of differentials under separability',K,'8','246–252','L_a séparable sur L_b',
 'The intended statement assumes generic K_b/K_a and residual L_b/L_a separability, finite free Omega_A/k, and the rank equality; it concludes projective dimension of Omega_B/A at most1.',
 'stated without proof; reversed residual field order in supplied text',
 'A⊂B induces L_a→L_b, so the printed residual extension order is ill-typed except accidental equality. Candidate reversal is a reading alarm. The conormal/transitivity resolution supplies the intended bound under the corrected assumptions.',
 'Cotangent transitivity gives the modern reconstruction; exact printed predecessor proof not rechecked.', 'C',['Jouanolou1963Differentielles'],'medium',J)
add('Differential rank detects regularity',K,'8','254–260','rang dim A+{L_a:K}',
 'For a noetherian local k-algebra with separable residual extension and finite residual differential dimension, freeness of Omega_A/k of rank dim A+dim Omega_La/k implies regularity. The same implication is asserted for the separated differential module.',
 'stated without proof',
 'Cotangent exactness identifies embedding dimension with the stated rank minus residual differential dimension. Equality embedding dimension=dimension gives regularity. For the separated module, reduction modulo the maximal ideal agrees with the original module, which is the only rank datum used.',
 'A standard differential regularity criterion, with no claim that separated and ordinary differential modules coincide.', 'B',['Jouanolou1963Differentielles','Stacks07EK'],'high',J)
add('Adic isomorphism criterion',K,'10','289–313','les C_i sont plats ... u_0 ... homéomorphisme',
 'Under the surrounding separated completeness and closed-ideal hypotheses, an adic map u:B→C is a topological isomorphism iff its quotient maps are bijective and u0 is a homeomorphism; with flat target quotients C_i/A_i, u0 alone suffices.',
 'proved there by inverse limits and associated graded',
 'For nilpotent I, grA⊗B0→grB is surjective and grA⊗C0→grC is bijective. Their composite forces gr(u) bijective. Closedness/completeness and the u0 topology clause are essential; the source begins mid-statement, so omitted preceding hypotheses are not reconstructed as visible text.',
 'Standard filtered-module argument; the handwritten replacement of B_i by C_i is mathematically decisive and contrasts with uncorrected Theorem4.6.', 'E',[],'high')
add('Finite presentation commutes with arbitrary products',K,'11','320–326','M⊗P→prod M⊗P_i',
 'For a finitely presented A-module M and arbitrary modules P_i, M⊗prod P_i→prod(M⊗P_i) is an isomorphism.',
 'proved there',
 'A two-term finite free presentation of M reduces the claim to exactness of products and finite sums. Finite generation already implies surjectivity. Failure of finite presentation can cause failure of injectivity; no noetherian hypothesis is needed for the stated finitely presented case.',
 'Standard module theory, established before these notes. No noetherian hypothesis is required for this lemma.', 'E')
add('Products and countable split inverse limits are flat',K,'11','328–334','tout produit ... plats; système ... cofinal dénombrable',
 'Over a noetherian A, products of flat modules are flat. A countable-cofinal inverse system of projective modules with surjective transition maps has flat inverse limit, because the successive surjections split and the limit is a product of projectives.',
 'proved there',
 'Choose a cofinal sequence, split each map, and identify the limit with P0×prod ker(Pn+1→Pn). Kernels are projective direct summands. Countability is used in that explicit product decomposition; it is not dropped.',
 'The optimal product theorem is Chase: coherent rings iff arbitrary products of flat modules are flat. The manuscript stronger noetherian hypothesis is sufficient.', 'B',['Chase1960'],'high')
add('Theorem4.6 formal simplicity and the B/C error',K,'12–13','339–375','1) B ... 2) B ... 3) B_i ... 4) u ... isomorphisme',
 'Part(i) derives formal smoothness of B/A from property P and formal smoothness of B0/A0. In part(ii), the three conditions that should constrain the comparison algebra C are written again for B, making their equivalence to u:B→C being an isomorphism false.',
 'proof sketched; false as stated in part(ii)',
 'computation_outputs.json theorem-4.6-source-target checks A=B=Q[e]/e², C=Q, I=(e), quotient u. B/A identity meets P and smoothness, all topologies are nilpotent/discrete, u0 identity, but u has kernel(e). Candidate repair uses C in1–3, consistent with the proof and added condition5.',
 'The corrected comparison theorem is part of formal smoothness/flatness theory. Literal failure is resolved by an explicit present-run counterexample, not a claim about unpublished ink.', 'C',['Stacks07NQ'])
add('Cohen algebra definition, uniqueness and fibre criterion',K,'13–16','379–423','algèbre ... de Cohen; B ... unique à isomorphisme près',
 'The broad draft definition combines completeness, property P and formal smoothness. Given a fixed formally smooth special fibre B0, a Cohen lift is unique up to a compatible, generally nonunique, isomorphism. In the noetherian local setting flatness plus formally smooth closed fibre implies formal smoothness.',
 'proved by preceding comparison and regular-parameter reductions',
 'Do not confuse this broad topological notion with the modern narrow Cohen ring (complete DVR/residue characteristic p). The uniqueness is of isomorphism class, not of the isomorphism. Artinian reductions use powers of lifted regular parameters to produce projective quotients.',
 'Stacks07NQ proves the local equivalence without the draft finite-radicial restriction. The draft definition is subsequently criticized editorially, not wholly retracted.', 'A',['Stacks07NQ','EGAIV1'],'high')
add('Existence of a Cohen lift of a prescribed closed fibre',K,'14–16','396–419','nous ignorons ... toujours une solution; extension résiduelle ... séparable',
 'The draft asks for general lifting of a complete formally smooth noetherian algebra B0 across a nilpotent base extension. It proves the local existence result when the residual extension is separable, by lifting the residue field and adjoining formal parameters.',
 'open on the pages in broad generality; separable case proved',
 'The reduction to square-zero extensions is a deformation-theoretic reduction, not a solution. Stacks15.41.6 gives existence for complete noetherian local A and complete formally smooth local B0 over its residue field, with no extra residual separability; this does not establish the full nonlocal preadmissible draft scope.',
 'Local version established, broad topological version only partly matched. Separate these quantifiers in the problem index.', 'C',['Stacks07EK'],'high')
add('Local formal smoothness and geometric regularity',L,'17–20','7–34','formellement simple ... plat ... universellement régulière',
 'For a local homomorphism of noetherian local rings with their maximal-ideal topologies, formal smoothness is equivalent to flatness and geometric regularity of the closed fibre. Over a field, a geometrically regular noetherian local algebra is adically formally smooth.',
 'proved subject to temporary radicial hypotheses; question later marked OK',
 'Stacks07NQ and07EK exactly supply the local topology and geometric regularity quantifiers. They do not identify this with formal smoothness for the discrete topology.',
 'EGAIV0.19 develops the final form; Stacks15.41.1 and15.41.5 are verified modern formulations. The broad Cohen terminology is dropped editorially in the same draft.', 'A',['EGAIV1','Stacks07EK','Stacks07NQ'])
add('Discrete versus adic formal smoothness',L,'20–24','36–46;89–113','pour sa topologie discrète ???; Je suis pessimiste',
 'Question: does adic formal smoothness of a noetherian local k-algebra imply discrete formal smoothness, also for complete algebras and localizations of flat noetherian maps? The characteristic0 positive-dimensional power-series examples are conjectured negative.',
 'open on the pages; negative expectations',
 'Q[[t]] and C[[t]] provide negative examples: Omega⊗residue has dimension1 while generic differential dimension is infinite. If Omega were projective it would be free over the local ring, forcing incompatible ranks. This tests discrete formal smoothness using its necessary projective-differential condition.',
 'Modern regular morphisms/ind-smoothness must not be substituted for discrete formal smoothness. The present proof settles the displayed characteristic0 examples and negates the unrestricted implication.', 'B',['Stacks00TH','Stacks0593'])
add('Finite p-basis positive case',L,'22','89–95','p-base finie ... en la complétant par les t_i',
 'In characteristic p, for separable K/k with finite p-basis relative to k, adjoining the formal variables to a p-basis of K/k gives a p-basis of K[[t1,...,tn]]/k under the stated relative Frobenius identification. This yields discrete formal smoothness in this case.',
 'proof sketched',
 'Finite p-basis is essential: coefficient expansions can then be grouped into finitely many p-monomials, each with a formal-series coefficient that is a pth power. Infinite relative differential dimension is treated separately on scans24–25.',
 'Field/p-basis criteria are standard; no blanket positive statement for all characteristic-p power-series algebras follows.', 'B',['Stacks07EK'],'medium')
add('Infinite coefficient differentials prevent a splitting',L,'24–25','113–142','n’a pas d’inverse à gauche',
 'If dim_K Omega_K/k is infinite and n>0, the coefficient map Omega_K/k⊗K K[[t1,...,tn]]→Omega_K[[t]]/k has no left inverse.',
 'proof sketched, final coefficient choice unfinished',
 'A hypothetical retraction gives a derivation into a direct sum of A. Quotient by finitely many coefficient differential directions to kill D(t_i). Each coordinate derivation is adically continuous since it kills t_i. Choose a countable independent sequence da_n and f=sum a_n t1^n: infinitely many differential coordinates of Df are nonzero, contradicting direct-sum support. Detailed proof in proof_notes.md.',
 'A valid manuscript obstruction. The stronger nonprojectivity argument is an earlier-run development and is recorded separately, not attributed to this proposition.', 'B',['Stacks00TH'])
add('Geometric regularity locus for a flat noetherian map',L,'20–21','46–65','Lieu ... est-il ouvert? ... bons anneaux',
 'For a flat map A→B of noetherian rings, is the locus where the local fibre ring is geometrically regular open? The text recognizes a need for good rings, asks generization stability and discusses a characteristic0 resolution route.',
 'open on the pages; conditional sketches',
 'With finite presentation this is the smooth locus and is open. Without finite presentation, merely naming excellence does not constitute an exact theorem. Geometric regularity localizes, but generization stability alone does not imply openness in a noetherian space.',
 'Finite-presentation part established; strongest arbitrary-noetherian good-ring formulation not fully identified. The manuscript’s unresolved term bons anneaux is retained as a scope ambiguity.', 'C',['Stacks07EK','Stacks00R8'],'medium')
add('Flat locus of arbitrary noetherian maps',L,'21','67','Lieu ... B est plat sur A ... ouvert?',
 'Does every map of noetherian rings have open flat locus? The displayed reduction asks generic flatness for the corresponding domain maps.',
 'open on the pages',
 'Negative: choose a characteristic-p noetherian local domain whose regular locus is not open. For absolute Frobenius the flat locus is exactly the regular locus by Kunz. Frobenius induces the identity on the prime spectrum, so localization quantifiers match. No finite-type hypothesis is available.',
 'Brodmann–Rotthaus(1982) and Nishimura(2012) supply bad-regular-locus examples; Murayama’s2025 MO answer points out this exact application. Finite-presentation openness is a different positive theorem.', 'B',['Kunz1969','Stacks0EC0','Nishimura2012','MO500040'])
add('Differential kernel need not descend to the smaller field',L,'27,29','150–176;209–221','N_K/k ... ne ... être défini sur k',
 'There exist k⊂K in characteristic p such that k∩K^p=k^p but ker(Omega_k⊗k K→Omega_K) is nonzero, even one-dimensional and not defined over k. The two scans construct a transcendental example and a finite separable-then-inseparable variant.',
 'proved by coefficient uniqueness; several overwritten formulas',
 'For p=2 take K=F2(x,b,c), y=b²x+c², k=F2(x,y). Kernel=K(dy−b²dx), b² notin k. Relative p-degree and coefficient comparison give k∩K²=k². Finite variant uses F4/F2 and a∉F2, y=ax+c². See proof_notes.md and matrix certificate.',
 'The phenomenon is reflected in EGAIV0.22.5.10(i), but its exact printed coefficient field must be checked independently; a transcription typo there is not assumed.', 'A',['EGAIV1'])
add('Trace, norm, divisors and idèles',L,'28,30','181–205;226–258','formules (31)–(45)',
 'For a finite extension of the valued/global fields in the missing preceding context, pullback of divisors has ramification coefficients e(P), pushforward has residue degrees f(P); norm∘pullback multiplies divisors by n, trace∘extension multiplies répartitions by n, and norm∘extension raises idèles to the nth power. Principal divisors and degrees are compatible.',
 'stated with elementary verification and earlier references',
 'All formulas follow placewise from v(Nx)=sum f(P)v_P(x) and sum ef=n. The latter requires the no-defect/global discrete-valuation setting of the source, which is not visible here; no arbitrary valued-field theorem is inferred. Scan30 precedes28 in the reused typescript.',
 'Classical algebraic function-field/idèle theory, not a new EGA theorem. Exact reused typescript identification remains open.', 'E',[],'medium','Unidentified reused typescript')
add('Adjunction for a smooth complete intersection',E,'4–5','11–74','Omega^n ... det E ... det M ...',
 'For P=P(E) in the quotient convention, rank E=r+1, and smooth complete intersection X/S of relative dimension n=r−p cut out by graded locally free equation modules M_di of ranks alpha_i, omega_X/S≅f*(det E⊗tensor det M_di^{-1})⊗O_X(sum alpha_i di−r−1).',
 'proved there by Euler and conormal determinant sequences',
 'Exterior powers and tensor twists have been recomputed. The general non-smooth situation supplies a dualizing line under regular-immersion hypotheses, not necessarily top exterior Kähler differentials. The source says rang incorrectly as degré in one sentence; keep as reading alarm.',
 'Classical adjunction, later standard duality/complete-intersection formalism. Calabi–Yau degree sum gives a line pulled back from S, not automatic global triviality.', 'E')
add('Elliptic cubic equation has weight6',E,'5','85–95','M ... L^{⊗6}',
 'For the elliptic cubic bundle with E filtered by O,L²,L³ and omega_X/S=f*(L^{-1}), its rank-one cubic equation module M is L^6.',
 'proved there',
 'det E=L^5; adjunction gives L^{-1}=L^5⊗M^{-1}, hence M=L^6. Descent of equality from X to S uses the section (or f* faithful on line bundles), supplied by elliptic-curve context. Exact exponent certificate saved.',
 'Standard Weierstrass weight calculation. It does not depend on the erroneous discriminant exponent on the next leaf.', 'E')
add('Discriminant degree and smoothness criterion',E,'6','98–134','(k−1)(r+1)',
 'The literal text assigns degree(d−1)(r+1) to the universal discriminant of a degree-d hypersurface in P^r. Correct coefficient degree is (r+1)(d−1)^r. Its nonvanishing detects smoothness of the hypersurface in the universal discriminant setting.',
 'stated without proof; false degree as written',
 'Plane cubics give6 in the source and12 correctly. Binary forms and quadrics cannot distinguish the two formulas. The line-bundle character also includes det E: locally Disc transforms by det(change coordinates)^{d(d−1)^r}, not just by the equation-line scaling.',
 'Buse–Jouanolou arXiv1210.4697 Prop4.7 gives exact homogeneity; Prop4.13 gives coordinate-change exponent. First arXiv circulation17Oct2012 is distinct from final publication metadata.', 'B',['BuseJouanolou2012'])
add('Integrability of a varying complex structure',E,'7','143–174','bar partial phi ... phi wedge partial phi=0',
 'The reused English leaf derives the Maurer–Cartan integrability equation for a vector-valued (0,1)-form phi(t) describing a differentiable family of complex structures, with phi(0)=0. Its derivative at0 is bar-partial closed.',
 'proved from an earlier coordinate identity absent here',
 'The bracket convention explains the one-half in the common notation barpartial phi−[phi,phi]/2=0. The final vector index nu/lambda mismatch is typographical in the supplied text. Missing formula(2) prevents an exact sign/coordinate audit.',
 'Kodaira–Spencer deformation theory is the established setting. Exact paper/author of this reused third page has not been identified, so no archival attribution or priority is claimed.', 'F',[],'medium','Unidentified English reused typescript')
add('Topological exponential and logarithm identities',E,'9','184–228','log(gg′)=log g log g′',
 'In a separated complete linearly topologized Q-algebra, exp and log are inverse on topologically nilpotent elements and1+such elements; natural under continuous algebra maps; preserve closed one-sided ideals in the indicated sense. For commuting elements, exp(x+y)=exp x exp y and log(gg′)=log g+log g′.',
 'stated without proof; logarithm identity false as written',
 'Dual numbers g=g′=1+t give log(gg′)=2t whereas the printed product is0. Formal power-series identities and convergence verify the corrected assertions. A closed subalgebra must contain the relevant unit for the exp statement.',
 'Classical exponential formal calculus. The source’s literal missing plus is left for scan checking.', 'E')
add('Group-like and primitive elements under exp/log',E,'10–13','235–368','pi(U) ... gamma(U)',
 'For a complete augmented cocommutative Q-bialgebra with topologically nilpotent augmentation ideal, exp identifies primitive and group-like elements; BCH transfers the group law. After a nilpotent augmented scalar extension Lambda, relative primitives and relative group-likes are likewise identified.',
 'proof sketched by coproduct calculation',
 'Delta(exp x)=exp(x⊗1+1⊗x)=exp x⊗exp x. Conversely the commuting factors g⊗1 and1⊗g give primitivity of log g. The tensor intersection is computed from split augmentations U=k⊕I(U), Lambda=k⊕I(Lambda), without flatness. The displayed target1+pi0 is false: reduced coproduct of exp(tx)−1 has t²x⊗x.',
 'Cartier1956 and BCH formalism supply the established context. The nilpotence/connectedness hypotheses must not be inferred solely from the shortened later checklist.', 'E',['Cartier1956','CartierExamples1956'])
add('Base change of primitive elements and Cartier reconstruction',E,'13','344–370','Lambda ... plat ... purement exacte; U≃U(g)',
 'Primitive base change is exact when Lambda is flat or the defining reduced-coproduct kernel sequence is pure. For a connected cocommutative Hopf algebra over a characteristic0 field, the enveloping algebra of its primitive Lie algebra recovers it; finite-dimensional primitives give a formal power-series dual.',
 'stated with Cartier/PBW attribution',
 'Purity is exactly the kernel-preservation condition. The shortened finite-subcomodule/no-group-likes checklist is insufficient over a nonclosed field: functions C3→R have only the trivial real group-like and zero primitives, yet dimension3. Cartier’s original connected filtration starts U0=k and is exhaustive; that extra condition excludes the example.',
 'Cartier’s talk27Jan1956 defines the connected filtration (Exp2,pp1–2); his Exp3 gives examples/enveloping structure. This is an old result, not a novel theorem of these notes.', 'E',['Cartier1956','CartierExamples1956'])
add('Nilpotent derivations and unipotent automorphisms',E,'14–16','374–469','dérivations nilpotentes ... automorphismes unipotents',
 'Over a Q-algebra, a globally nilpotent linear endomorphism D is a derivation of a bilinear product iff exp D preserves the product. For an augmented Lambda with I^N=0, Lambda-automorphisms of B reducing to identity correspond under log to Lambda-derivations into IB.',
 'stated; polynomial argument implicit',
 'exp(mD)=(exp D)^m for all integers m. If exp D preserves multiplication, the polynomial identity in m holds for infinitely many rational integers; comparing its linear coefficient proves the derivation law. Conversely the iterated Leibniz/binomial formula proves multiplicativity. Fixed vectors, commuting operators and invariant submodules are preserved because exp and log are polynomials.',
 'Standard nilpotent Lie/group correspondence over Q. Global nilpotence is supplied by I^N=0 in the deformation application; no characteristic-p extension is claimed.', 'E')
add('Derivations after augmented scalar extension',E,'16','442–469','B tensor_Lambda k≃Lambda',
 'For B=A⊗k Lambda, Der_Lambda(B,B)=Hom_A(Omega_A/k,A⊗Lambda), and those reducing to0 correspond to Der_k(A,A⊗I). The special fibre is A, not Lambda. When Lambda is finite free over k or Omega_A/k finite projective over A, the latter module is Der_k(A,A)⊗I.',
 'proved by Hom adjunction; base-change conditions continued on scan17',
 'The quotient B⊗Lambda k=A follows from associativity of tensor products and gives a literal type correction. Hom/tensor exchange requires the stated finiteness/duality hypotheses; it is not automatic for arbitrary infinite differential modules.',
 'Standard Kähler differential base change and Hom adjunction. BCH supplies the group law after the previous claim.', 'E')

add('Finite augmentation and infinitesimal thickening hypothesis',N,'17–19','4–73','gr^I Lambda ... localement libre [donc I^n=0]',
 'The jet/deformation construction takes a finite locally free augmented O_S-algebra Lambda with locally free associated graded and treats Spec Lambda as a nilpotent thickening of S. The bracketed implication to nilpotence is false unless support/nilpotence is separately assumed.',
 'construction stated; false implication in its hypotheses',
 'Lambda=k×k with first projection has I=0×k, I²=I, gr0=k and higher graded pieces0. It is finite free, all graded pieces free, but no I^n vanishes. The ensuing equalities of underlying spaces require an additional nilpotent augmentation hypothesis.',
 'Finite infinitesimal algebras/Weil restriction are established once nilpotence is explicit. The counterexample is saved with its multiplication certificate.', 'C')
add('Deformations as bitorsors and Weil-restriction sections',N,'19–23','26–181','Iso_T^{X0}(xi,X) ... faisceau des sections',
 'For T/S finite locally free with nilpotent augmented ideal and smooth X/T, write X0=X×T S and xi=X0×S T. Local isomorphisms xi→X inducing identity on X0 form an Aut(X)/Aut(xi) bitorsor; evaluation on the canonical section identifies it with sections over X0 of Res_T/S X→X0.',
 'proof sketched',
 'Smoothness gives local lifts of X0 and formal étaleness of an isomorphism modulo nilpotence gives the required local trivializations. Evaluation and functor-of-points adjunction verify the identification. Global triviality is not asserted: the torsor may have no global section.',
 'Weil restriction and infinitesimal deformation torsors are standard; representability must be handled as an algebraic space in general, or under the usual scheme hypotheses.', 'B',['StacksWeilRestriction'],'medium')
add('Principal-parts functor and jet sections',N,'24–27','193–353','P^n ... d^n ... epsilon ...',
 'For X/S with finite locally free nth diagonal neighbourhood Delta^n over X and a suitable X-scheme Y, Res_Delta^n/X(Y×X Delta^n) represents nth jets of sections. Evaluation epsilon and prolongation d^n satisfy epsilon d^n=id; order truncations commute with them and pass to a formal-neighbourhood limit.',
 'constructed by universal property; locality explicitly left to verify',
 'Restriction to U⊂X commutes with the diagonal neighbourhood because its two projections have the same underlying point for nilpotent thickening. Weil restriction adjunction then gives locality and the displayed identities on every test scheme. It is a sheaf construction even when scheme representability needs added hypotheses.',
 'EGAIV principal parts and modern Weil restriction establish the represented cases. The formal inverse limit need not be an ordinary finite-type scheme.', 'A',['EGAIV4','StacksWeilRestriction'])
add('Infinitesimal transformations, connections and functorial action',N,'28–32','359–557','connexions d’ordre n; g↦u g v^{-1}',
 'Compatible pairs of automorphisms (u of Y,v of X) with f u=v f act on sections by g↦u g v^{-1}; their jet prolongations act on connection/jet sheaves. Reduction to identity yields infinitesimal actions.',
 'definitions and action sketched; one page of left/right-algebra construction cancelled',
 'Composition proves the action law. The statements need compatible source/target convention: the source sometimes switches labels. The cancelled scan30 is retained as a rejected construction layer, not used to prove a global connection-existence theorem.',
 'Functorial jet/connection formalism developed extensively. The algebraic diagrams on scan29 are too incomplete to match a unique theorem beyond the explicit action.', 'C',['StacksWeilRestriction'],'medium')
add('Naturality and product compatibility of transformations',Q,'33','3–22','h ... tilde w(g)=tilde w′(hg)',
 'Prolonged infinitesimal transformations commute with compatible morphisms, products and any composition law expressible by such morphisms.',
 'stated as immediate consequences',
 'Apply the action g↦u g v^{-1} and compatibility h u=u′h. Then h(u g v^{-1})=u′(h g)v^{-1}. Products are checked componentwise; no additional differential identity is needed.',
 'Elementary functoriality, already implicit in the construction.', 'E')
add('Two inseparable curve examples',Q,'35–36','37–80','F=aX^p+bY^p−1; F=Y²−X^p+a',
 'Example(i) mixes a cancelled pth-power curve with a new form aX^p+bY^p−1 and asks whether k is algebraically closed in its function ring/field. Example(ii), for p≠2 and a∉k^p, is the regular affine curve Y²−X^p+a=0 that becomes singular after adjoining a pth root of a.',
 'examples sketched; relative algebraic closure left open in(i)',
 'For(ii), away from Y=0 the derivative2Y gives smoothness. At the unique point(Y,X^p−a), the maximal ideal is generated by Y because X^p−a=Y²; the dimension is1. Over k(a^{1/p}) the origin of Y²−Z^p has embedding dimension2. In(i), the displayed old isomorphism cannot be applied to the new equation without its coefficient hypotheses.',
 'Regular versus geometrically regular curves are standard. The exact new(i) coefficient assumptions and meaning of algebraically closed in A remain an incomplete manuscript problem.', 'C',['Stacks07EK'])
add('Differential and diagonal criteria need precise hypotheses',Q,'37','87–119','Omega=0 ... non ramifié; plat ... f∈A',
 'The sheet lists vanishing differentials, étaleness, radicial diagonals and equalizers. Modern forms: Omega_B/A=0 iff formally unramified; finite-type is needed for unramified, finite presentation plus flatness gives étale. The equalizer of B⇉B⊗A B is A for faithfully flat A→B.',
 'unproved checklist with question marks; some literal statements false',
 'A=Z→B=Q is flat and injective but B⊗A B=Q, so delta f=0 for every f∈Q, while f need not lie inZ. For a nontrivial finite separable field extension, the diagonal ideal is idempotent, so every finite infinitesimal difference vanishes although the ordinary diagonal difference need not. These counter the unrestricted flat and formal-diagonal claims.',
 'Descent and unramified criteria establish the repaired forms. A p-basis calculation for ker d=A[B^p] requires the actual p-basis hypotheses and is not a theorem about every characteristic-p algebra.', 'C',['Stacks00TH','Stacks08WE'])
add('Transported structures and associated bundles',Q,'38','123–138','structures d’espèce ... condition C',
 'The reused typed page constructs an associated structure bundle from a group action after quotienting by the action kernel, subject to a condition ensuring that the chosen morphism family detects the structure.',
 'fragment of a proof; definitions and condition C′ truncated',
 'The algebraic core is independence under changes of frame. No representability or existence theorem follows without the missing definitions of the species and condition C.',
 'Associated-bundle formalism is classical; exact Bourbaki/reused-typescript identity not found in the supplied material.', 'F',[],'low','Unidentified reused typescript')
add('Finite-order differential functors and coordinate frames',Q,'39–41','140–180','foncteur différentiel d’ordre n ... caractériser',
 'On smooth relative-d schemes with étale maps, a finite-order natural construction should descend from the frame torsor of truncated coordinates, under the automorphism group of the truncated polynomial algebra. The text asks for a characterization of the image.',
 'open construction question, cancelled diagram',
 'Given an equivariant object, associated-bundle descent constructs a natural object. The converse requires a precise definition of finite order and the ambient category; the notes do not supply them, so no full equivalence is certified.',
 'Natural-bundle and jet-group descriptions are established in several settings. No exact algebraic theorem with these unspecified quantifiers is identified here.', 'C',[],'medium')
add('Lê Dũng Tráng’s meromorphic denominator correction',Q,'44–47','185–247','S ... sections régulières ... tout ouvert',
 'Lê’s11Jan1968 letter corrects EGAIV20.1 and21: the denominator subsheaf consists of sections that remain non-zero-divisors on all open restrictions. For arbitrary schemes its stalk need not equal all non-zero-divisors of the local ring, nor are global meromorphic sections automatically the total quotient ring of global regular functions.',
 'errata supplied; author explicitly unsure about proof consequences',
 'The sheaf condition is essential. For locally noetherian schemes, finite generation of an annihilator allows shrinking a local non-zero-divisor to a regular section, recovering the familiar stalk equality. The cancelled suggestion to add local noetherianity to21.2.12 is not treated as an adopted correction.',
 'Stacks31.24/71.10 makes the denominator sheaf and noetherian special case explicit. The primary EGAIV4 formulas are compared separately when the PDF is available.', 'B',['EGAIV4','StacksMeromorphic'],'high','Lê Dũng Tráng')
add('Gluing unramified sections across a dense open and thickening',Q,'49','249–266','U schématiquement dense ... Y0 ...',
 'For unramified X→Y, a schematically dense open U⊂Y and closed Y0⊂Y with the same underlying space, compatible sections on U andY0 are asserted to glue uniquely.',
 'stated without proof',
 'Uniqueness follows from the open diagonal plus schematic density in the appropriate separated/local argument. Existence is subtler: unramified is not formally smooth. A blanket appeal to nilpotent invariance of étale sites would not establish this statement for arbitrary unramified X.',
 'Related to effective descent and unramified envelopes; exact quantifiers of this unproved gluing assertion have not been matched to a verified published theorem.', 'C',[],'medium')
add('Finite epimorphism descent for unramified sections',Q,'49','272–301','Y′ fini épimorphisme ... éliminer noeth ... entier?',
 'For locally noetherian Y, finite scheme epimorphism Y′→Y and a surjective Y′′→Y′×Y Y′, the text asserts exactness of X(Y)→X(Y′)⇉X(Y′′) for unramified X→Y, and asks to drop noetherianity and replace finite by integral.',
 'stated without proof; generalization open',
 'Épimorphisme must not be silently weakened to surjective: a nonreduced scheme’s reduction is finite surjective but cannot universally descend closed-immersion sections. Equalities after Y′′ use unramified diagonal properties. Effective descent of étale objects alone does not settle all unramified objects.',
 'Modern universal subtrusiveness/descent results address related categories. Exact finite-epimorphism statement remains a targeted source-verification problem, with a clear warning against the surjective replacement.', 'C',[],'medium')
add('Nonnoetherian regular sequences and the Koszul replacement',D,'51–54','11–108','(x,y) régulière ... (y,x) ne l’est pas',
 'Outside the noetherian case, regular sequences need not be permutable. The proposed replacement uses vanishing of positive Koszul homology, gives a quasiregular ideal, is independent of minimal generators, descends fpqc, and composes for immersions. In the noetherian case the notions agree.',
 'proof claims partly checked by Berthelot; editorial plan to correct EGA',
 'Explicit counterexample in proof_notes.md: R0=k[x,y]_(x,y), M=k(x) with y acting0, R=R0⋉M. x is regular, M/xM=0 and y regular modulo x, but y killsM. Koszul acyclicity is permutation invariant. The transcribed degrees0 in line67 misses the > sign: H0 is the nonzero quotient.',
 'Primary SGA6VII by Berthelot, printed416–421, was visually checked: Def1.1, Prop1.3, Def1.4,1.4.2–3 andProp1.5 exactly implement the replacement. Stacks0638 retains separate terminology and verifies composition.', 'A',['SGA6VII','Stacks0638'])
add('A-modules versus B-modules in adic separation',D,'56,58','120–131;178–207','tout quotient de tout sous-module de M',
 'Deligne rejects the assertion that all A-subquotients of a finite B-module are J-adically separated when A,B are noetherian and JB⊂radB. It is valid for finite B-subquotients, not arbitrary A-subquotients. The graded example also fails for nongraded quotients.',
 'counterexamples in letter; earlier objection reinstated15Dec1966',
 'Take A a nonfield DVR, B=A[[T]]. The A-submodule A[T]≅A^(N) surjects onto A[1/pi], a countably generated A-module with piM=M, hence nonseparated. For B0[T] andJ=(T), quotient byT−1 is nonzero andJ acts invertibly. This verifies both objections with explicit modules.',
 'Artin–Rees/Krull intersection supports the finite B-module alternative. The23Oct/15Dec chronology matters: the later letter does not withdraw the counterexample.', 'B',['EGAIV4'],'high','Pierre Deligne')
add('Deligne’s objections to EGAIV16.1.5 and16.1.6',D,'56–57','146–159','J=0 ... voisinages ... non triviaux; noyau ... type fini?',
 'Deligne gives X=Spec k[T], Y=Spec k[T] disjoint union Spec k to contest an infinitesimal-neighbourhood proof, while explicitly not knowing whether the proposition is true. He also doubts that a finitely presented algebra B overA has finitely generated kernel A→B.',
 'proof objection and open question',
 'The finite-presentation kernel implication is false: B=A_f is finitely presented, but ker(A→A_f)=the f-power torsion can be non-finitely generated in a nonnoetherian ring. A concrete idealization construction is given in proof_notes.md. His first proof objection is not promoted to a counterexample to the proposition itself.',
 'Modern infinitesimal neighbourhood definitions and finite-presentation lemmas distinguish relation ideals in polynomial presentations from kernels of arbitrary algebra maps. Exact EGA proof comparison is recorded as a separate check.', 'B',['EGAIV4'],'high','Pierre Deligne')
add('Separation-free implication in the regular-sequence criterion',D,'58–59','199–218','19.5.5 b)⇒c) ... sans ... séparation',
 'Deligne claims implicationb⇒c in EGAIV19.5.5 requires no separation hypothesis, citing the one-element case of a Schwartz-style proof and enclosing a redaction absent from this file.',
 'stated without included proof',
 'The exact b/c conditions must be read in EGAIV4. The missing enclosure is not reconstructed from the claim. His alternative separation hypothesis involves kernels M⊗N→M⊗P for finite A-modules N,P.',
 'Related Koszul-regularity improvements are verified in SGA6, but they do not by themselves identify this precise implication.', 'C',['EGAIV4','SGA6VII'],'medium','Pierre Deligne')
add('Algebraic solution sets are not linearly compact affine spaces',D,'60','240–244','19.3.12 ... canulé ... pas une variété linéaire',
 'Deligne identifies an error in EGAIV0.19.3.12: sets of algebra homomorphism lifts across a non-square-zero ideal need not be affine linear spaces. Infinite systems of polynomial conditions over an infinite field can have all finite subsystems solvable and no global solution.',
 'counterexample and proof criticism',
 'For an infinite fieldk, equations(x_infty−u)y_u=1 for everyu∈k have each finite subsystem solvable by choosing x_infty outside the finite forbidden set; no full solution exists because x_infty itself equals someu. Primary EGAIV1 printed85–86 visibly calls the lift set a closed linear variety. This invalidates that proof, not automatically the theorem.',
 'The exact published proof defect is independently confirmed. Countable adic lifting has a separate successive-lift proof (EGA19.3.10/11); no uncountable theorem repair is inferred from it.', 'C',['EGAIV1'],'high','Pierre Deligne')
add('Auslander–Buchsbaum by a derived tensor-Hom spectral sequence',D,'60–61','248–298','dim proj M=prof A−prof M',
 'For nonzero finite M over a noetherian local A with finite projective dimensiond, depthM=depthA−d. Deligne derives it from RHom(k,A) derived-tensor M≅RHom(k,M) and the spectral sequence Tor_{−p}(Ext^q(k,A),M)⇒Ext^{p+q}(k,M).',
 'proved there',
 'Take a minimal finite free resolution of M. Its last tensor withk is nonzero; Ext^a(k,A) is a nonzero k-vector space fora=depthA. The unique corner(−d,a) survives, with no differentials into or out of the lowest possible total degree. Saved index computation checks the degree arithmetic.',
 'Auslander–Buchsbaum is prior work; Deligne explicitly says the fuller result is in Northcott and notes Auslander. The proof itself is a useful archived reformulation, not a priority claim.', 'E',['StacksAuslanderBuchsbaum'],'high','Pierre Deligne')
add('Relative finite Tor dimension and Tor/pro-completion',D,'61,65','294–320;531','lim Tor(N/m^kN,M)=Tor(N,M)^hat',
 'For local noetherian A→B, finite A-moduleN, finite B-moduleM and idealm⊂A, the pro-systems Tor_p^A(N/m^kN,M) and Tor_p^A(N,M)/m^k are asserted isomorphic. Deligne uses this toward the relative depth formula with finite Tor dimension and revisits the proof at the letter’s end.',
 'proof sketched using flat cover; author flags awkwardness and cannot give the simpler direct proof',
 'For finite modules over a single noetherian ring the pro-vanishing statement follows from Artin–Rees on a finite free resolution. For relative M finite only overB, his flat-cover/Cohen-factorization reduction is substantive. Ordinary inverse-limit equality is weaker than the claimed pro-isomorphism and is not substituted for it.',
 'Formal-functions/pro-Tor methods and Cohen factorizations supply the modern framework. Exact general pro-isomorphism proof is reconstructed separately with its flat-cover input; no finite computation can establish it.', 'B',['Stacks07NN','EGAIII'],'medium','Pierre Deligne')
add('Deligne’s minimal Cohen factorization',D,'61–63','322–396','C plat sur A; C0 régulier ... degrés0 et1',
 'For local noetherian A→B withB complete, seek A→C→B withC complete local noetherian, C→B surjective, C flat overA, regular closed fibre, and induced graded fibre map bijective in degrees0 and1. The proof treats transcendental, separable algebraic, then purely inseparable residue extensions.',
 'proof sketched; purely inseparable presentation and flatness left to check',
 'Stacks07NN/09Q9 gives a possibly nonminimal complete factorization after completingA; quotienting by lifts of independent linear relations in the regular closed fibre gives minimality. Flatness survives this quotient by the local flatness criterion. The handwritten exponent m^n versus iterationi inQ_ni is a reading alarm.',
 'Modern Cohen factorizations are named and systematically developed by Avramov–Foxby–Herzog1994; the dated17Oct1966 letter is earlier evidence for this formulation. No historical priority beyond the dated source is asserted.', 'B',['Stacks07NN','Stacks09Q9','AvramovFoxbyHerzog1994'],'high','Pierre Deligne')
add('Algebraic field extensions as filtered complete intersections',D,'62–63','349–396','toute extension algébrique ... relever P_i ... plat',
 'An algebraic extensionK/k admits a presentation by successive finite monic relations, so arbitrary lifts of the chosen finite triangular relations to an Artinian local base yield flat algebras; the full construction is a filtered colimit.',
 'property noticed but author says he has not isolated it well',
 'For each finite tower choose one minimal monic polynomial at a time. Lifting coefficients gives a finite free iterated algebra with the same basis. Infinite algebraic extensions require a directed presentation compatible with denominators and previous stages; not every arbitrary presentation has the lifting property.',
 'Field extensions are ind-complete intersections in the appropriate cotangent-complex sense. The triangular-presentation formulation is the precise elementary content, rather than a claim about all polynomial presentations.', 'B',['Stacks09Q9'],'medium','Pierre Deligne')
add('Regular sequence equivalences via Tor, graded algebra and Ext',D,'63–64','405–470','Sym(I/I²)=gr; wedge(I/I²)=Tor; Ext^i=0',
 'For a proper idealI of a noetherian local ringA, minimally generated byn elements, the usual regular-sequence criterion is equivalent to Koszul acyclicity, free conormal with symmetric associated graded, exterior self-Tor, and Ext^i_A(A/I,A)=0 fori<n. The module variant uses finite nonzeroM and its grade.',
 'proved there by local reduction, cone/Nakayama and prime avoidance',
 'Finite generation is needed for the cone/Nakayama step and associated-prime argument. For the Ext⇒M-regular implication, if M=0 some definitions of regular sequence fail; take M nonzero andI proper in the maximal ideal. The reduction modulo an M-regularf has degree bound i<n−1, not the doubtful ≤ alternative.',
 'Standard noetherian complete-intersection/grade criteria; outside noetherianity the equivalences separate, as the postscript emphasizes.', 'E',['Stacks0638','Stacks09Q9'],'high','Pierre Deligne')
add('Nagata’s generalized finite prime avoidance lemma',D,'64','472–477','a⊂union b_i union p_i',
 'If an ideal a lies in the union of finitely many idealsb_i and finitely many prime idealsp_j, then either a⊂union b_i or a⊂p_j for somej, after omitting redundant ideals contained in the chosen prime.',
 'proved there; attributed Nagata',
 'For one primep not containing anyb_i, choose x∈a outside unionb_i. For y∈a∩intersectionb_i, x+y remains outside everyb_i, so lies inp, hencey∈p. Primality and b_i notsubsetp implya⊂p. Induct on the number of primes. The finite-family hypothesis is indispensable.',
 'Classical prime avoidance variant, correctly used to find a regular element outside mI.', 'E',['Nagata1962'],'high','Pierre Deligne')
add('Flatness versus topological formal projectivity',D,'64–65','483–505','M plat sur A ... formellement projectif',
 'For local noetherian A→B and finite B-moduleM, with maximal-ideal topologies, flatness overA is equivalent to topological formal projectivity overA. Deligne reduces to ArtinianA and dual pro-Tor/ind-Ext conditions.',
 'proof sketched',
 'The arbitrary moduleN in the lifting criterion cannot be replaced byk without the stated devissage and uniform ind-zero condition. Artin–Rees identifies the pro-Tor system; finite B-module separation then detects Tor1^A(M,k)=0, and the local flatness criterion applies.',
 'This is a module analogue of the formal smoothness/flatness comparison, developed in EGA0.19.2 and modern local flatness theory. Ordinary Ext vanishing ofM as a discrete module is not asserted.', 'A',['EGAIV1'],'medium','Pierre Deligne')
add('Further Deligne errata and suggested simplifications',D,'64–65','481;507–527','homomorphisme local ... signe ... K′=K tensor Ahat faux',
 'The letter proposes: drop a noetherian hypothesis in0.16.1.9 by Bourbaki integrality; weaken formal-projectivity assumptions in0.19.4.6; use semi-exactness of Exalcotop in0.19.4.7; insert local in0.19.8.3; reverse the chosen dx sign in0.20.4.6; remove integral-closure hypothesis in0.20.4.13(iv); and rejects EGAIII4.3.6 K′=K⊗A Ahat generally.',
 'errata and unproved simplification suggestions, with question mark',
 'Sign conventions must be propagated consistently through all subsequent maps; opposite universal derivations are both valid conventions. The field-tensor assertion fails for A=k[t]_(t), K=k(t): K⊗A k[[t]]=k((t)) is a field here, so this example does NOT refute it; one needs the actual definition of K′/ambient modules from EGAIII before constructing a counterexample. No fabricated counterexample is offered.',
 'Individual exact numbered comparisons require the primary statements, not just thematic modern analogues. The local-homomorphism corrections are consistent with local residue-field hypotheses. The scope of remaining numbered suggestions is explicitly a historical verification gap.', 'C',['EGAIV1','EGAIII'],'medium','Pierre Deligne')

add('Zariski Main Theorem without finite presentation',V,'67–68','14–30','quasi-fini séparé ... élimination ... présentation finie',
 'A quasi-finite separated morphism factors as an open immersion followed by a finite morphism. The sheets compare a global compactification proof, noetherian approximation, and an étale-local proof, then remove a finite-presentation hypothesis.',
 'proof strategy and precise published cross-references',
 'Quasi-finite includes finite type. Separatedness is essential; it is not a theorem about arbitrary maps with finite fibres. EGAIV8.12.3/18.12.12 are the specific archival reference trail.',
 'Established in EGAIV. Modern Zariski Main Theorem gives the exact finite-type separated scope without requiring finite presentation over a nonnoetherian base.', 'A',['EGAIV3','EGAIV4','StacksZMT'])
add('Approximation type versus affine factorization',V,'70–71','34–68','essentiellement de présentation finie; essentiellement affines',
 'The draft compares filtered inverse limits of finitely presented Y-schemes with affine transition maps, a factorization through an affine map to a finitely presented Y-scheme, and a finite-presentation approximation of its quasi-coherent algebra. It proves/states equivalence of the first and third and, over locally noetherianY, all three.',
 'propositions stated without proof; definition revised on next leaf',
 'This use of essentially finite presentation is historical and differs from the modern local-algebra phrase essentially of finite presentation (localization). Quasi-compact/quasi-separated hypotheses in composition and cancellation are preserved. A factorization alone does not visibly give global algebra approximation without a completeness property of the base.',
 'Modern approximation-type theory (Rydh) and EGA limit methods develop these distinctions. Exact strengthened scope should be matched to a specified approximation theorem rather than relabelled.', 'C',['EGAIV3','RydhApproximation'],'medium')
add('Normal/geometrically unibranch approximation',V,'70','58','X_i géom. unibranches (resp. normaux)',
 'Over a universally Japanese base, the draft expects an essentially finitely presented geometrically unibranch (respectively normal) scheme to admit approximants with the same property.',
 'stated without proof',
 'Normalization finiteness for the approximants and descent of finite data are the proposed mechanism. The sentence gives geometrically unibranch on the left even for the normal parenthesis; that cannot be used literally to characterize normality without its corresponding left-hand hypothesis.',
 'EGA approximation/normalization methods are the natural source, but the exact global form and parenthesis need source reconstruction. No broad normal approximation theorem is claimed solely from the citation.', 'C',['EGAIV3','RydhApproximation'],'medium')
add('Zero-dimensional schemes, patch topology and absolute flatness',V,'73','72–118','tous points fermés; anneaux locaux ... corps',
 'For a scheme, all points are closed iff every local ring of Xred is a field; affine charts are then compact Hausdorff Stone spaces. Under the stated quasi-separatedness, the constructible topology agrees locally with the original topology and affine opens are clopen. For reducedX these are equivalent to flatness of every module.',
 'equivalences with brief proofs',
 'Compact means Hausdorff compact in this text; every affine scheme is merely quasi-compact, so modern quasi-compact would make the statement false. Reduced zero-dimensional rings are absolutely flat. Global Hausdorffness is not asserted for a nonseparated scheme. The marginal converse reconstructs a scheme from a locally compact totally disconnected space with a sheaf of fields; compact-open charts provide the ring spectrum.',
 'Standard von Neumann regular/Stone-space correspondence, with the local-versus-global topology qualifications essential.', 'E',['StacksAbsolutelyFlat'])
add('Effective descent of étale sheaves under four coverings',V,'74','126–153','Théorème9.4 ... entier ... propre ... plat lfp ... X discret',
 'A surjective morphism is effective descent for étale sheaves under any of: integral; proper; flat locally of finite presentation; or discrete target. The descent sheaf is the equalizer of the two pullbacks on each étale test object.',
 'theorem and start of proof on reused typescript',
 'The category is all sheaves on the small étale site, not automatically finite étale schemes or arbitrary schemes. Equalizer construction gives a sheaf; essential surjectivity uses the listed geometric hypotheses.',
 'The exact reused theorem is SGA4VIII9.4. Primary comparison is made by printed location; modern descent theory also treats universal submersions/subtrusive maps.', 'A',['SGA4VIII'],'high','Reused SGA4 typescript')
add('Clopen detection and field-base-change invariance',V,'75–77','157–228','condition(h0); OF(S)→OF(T) injective',
 'A morphismf:T→S satisfies h0 when every nonempty clopen subset ofS meetsf(T), equivalently pullback of finite étale coverings is conservative and faithful in the stated setting. For k-schemes, h0 is preserved by arbitrary base extension by a k-scheme and reflected by a nonempty one. The clopen square is cartesian.',
 'proved by algebraic closure, Galois saturation and descent',
 'Over algebraic closure, the Galois-saturation of a clopen set is open; its image inS is closed because the base extension is integral, and saturation is its inverse image. Faithfully flat descent then gives a clopen subset downstairs. The cartesian square follows by testing the two descent pullbacks, using h0 again.',
 'Established connected-component/descent formalism. The abelian-scheme morphism extension diagram on scan77 uses rigidity plus descent and is conditional on a given descent cover, not a new unconditional extension theorem.', 'B',['SGA4VIII'],'medium')
add('Faithful/full faithful pullback of finite étale covers',V,'78','252–277','pi0(Y′)→pi0(X′) ... fidèle (pleinement fidèle)',
 'For finite étale test coversX′/X, clopen-set detection or bijectivity after pullback is equivalent to faithfulness or full faithfulness of the finite étale pullback functor; the locally noetherian component formulation uses pi0-surjectivity/bijectivity.',
 'proof by graphs and internal Hom indicated',
 'Equalizers of maps between finite étale covers are clopen. Sections of finite étale internal Hom detect morphisms, giving the equivalences. The parentheses are two distinct strengths and must not be merged.',
 'Standard Galois-category connectedness criteria. They concern finite étale covers, distinct from all étale schemes on scan80.', 'A',['SGA1','SGA4VIII'])
add('All étale schemes: separatedness and submersiveness caveat',V,'80','294–322','avec réserve ... séparés ... submersif',
 'The analogous clopen criteria for all étale schemes are asserted with a reservation: graph arguments work for separated étale schemes; arbitrary étale objects may require a universally/étale-locally submersive map. Density controls the non-parenthetical faithfulness condition.',
 'partly proved; caveat and open hypothesis refinement',
 'For nonseparated étale objects, an equalizer need only be open, so clopen information is insufficient for the full-faithfulness argument. The source itself notices this and mentions stability under finite base change for qcqs schemes.',
 'Modern descent of étale morphisms uses universal subtrusive conditions; this is a genuine hypothesis distinction, not a missing one-line proof.', 'C',['SGA4VIII','RydhDescent'],'medium')
add('Constructibility of a finite direct image and truncated cohomological comparison',V,'79,81','282;327–381','f_*F′ ... constructible; R^1p_* ...',
 'The reused page79 proves constructibility of a direct image by noetherian induction, étale localization and decomposition into radicial pieces near a generic point. Page81 has R1-base-change sketches and a cancelled derived comparison corollary whose inequality signs are absent.',
 'proof fragment on79; diagrams and cancelled truncated claim on81',
 'Without the preceding finite/quasi-finite hypotheses onf, page79 cannot imply constructibility for every morphism. The missing comparison-degree inequalities on81 prevent reconstruction of a unique statement. It is recorded as F for that fragment, with no invented sign repair.',
 'Constructible étale direct-image results appear in SGA4; the exact page79 antecedents and page81 corollary remain unidentified.', 'F',['SGA4VIII'],'medium','Unidentified reused SGA-style typescripts')
add('One-equation dimension drop and a wrong quantifier',W,'83–84','10–99','codim(Y,V(x))≥r−1 ... existe i,k',
 'The lower bound for a single equation is valid. Equality requires a component condition at a minimal-codimension point: the equation must avoid every top-dimensional component of the localized scheme there. The source says existence of one component and later has a reversed containment.',
 'proof sketched; equality criterion false literally',
 'A=k[x,y,z]_(x,y,z)/(xy), Y=closed point, f=x: dimA=2 and one component is not inV(f), but dimA/(x)=2, not1. This verifies every printed noetherian/local hypothesis and refutes the existential criterion. The lower-bound proof is the principal ideal theorem.',
 'Classical dimension theory; the corrected local criterion follows from dimR/f=max over minimal components. The affine/quasi-affine wording of the existence part remains a reading issue.', 'E',['StacksDimension'])
add('Parameters in an ideal and the quotient typo',W,'84','92–99','x_i ... dans p ... paramètres de A/p',
 'For a noetherian local ring and idealI of heightr, one can choose r elements inI with generated ideal of heightr; under the appropriate local component conditions they extend to parameters. The final statement writes that elements in p form part of a parameter system of A/p.',
 'corollaries stated; final quotient assertion false literally',
 'Every x_i∈p maps to0 inA/p, so cannot be a nonzero parameter there. Candidate A instead ofA/p is mathematically natural. The marginal equivalence between heightp and successive avoidance of all irreducible components may need equidimensional/catenary qualifications and is not accepted automatically.',
 'Standard system-of-parameters selection uses prime avoidance. Exact manuscript formulation needs scan adjudication and separation of maximal-dimension versus all components.', 'C',['StacksDimension'])
add('Graded shift-category draft',W,'85','104–162','partial-catégorie ... Hom_n ... X(1)',
 'A mostly cancelled draft introduces a graded additive category with shift objects representing degree changes. The final surviving formulas relate Hom_n(X,Y), Hom_{n−1}(X(−1),Y), and Hom_n(Y,X(−1)).',
 'withdrawn/unfinished definition',
 'The proposed degree conventions change within the cancellations; no differential or triangulated axioms survive. It is not evidence that a full derivator or triangulated-category theory is asserted here.',
 'Graded categories and shifts are classical homological language. Exact intended partial-category structure is not identifiable.', 'F')
add('Serre S_k under a finite algebra',W,'87–90','167–220;244–257;295–370','prof_A=inf prof_B; dim_A=sup dim_B',
 'For finite A→B and finite B-moduleM in the noetherian setting, depth_Ap M_p is the minimum of depths at primesq overp, and dimension_Ap M_p is the maximum of their support dimensions. Consequently S_k overA implies S_k overB; the converse holds if these local support dimensions are equal for allq overp.',
 'proved by depth/dimension comparison; earlier unconditional converse cancelled',
 'The inequality chain in scan87 is valid. The proof correctly inserts the equal-dimension condition for the converse. Example A local with finite productB=A×A/p andM=B shows why dimensions may differ and why CM/S_k as aB-ring is not automatically the same as anA-module.',
 'Standard depth under finite maps and Serre conditions. The later scratch page correctly recognizes the missing converse hypothesis.', 'E',['StacksDepth'],'medium')
add('Normalization criterion via codimension one and S2 extension',W,'88–90','244–285','normalisé fini ... a) ... b)',
 'For a domainA that is a quotient of a regular noetherian ring, the draft proposes finite normalization iff only finitely many height-one localizations are nonregular and each has finite normalization. Its proof tries to make an S2 finite extension that is normal in codimension one.',
 'proof sketched, spread over pages in reverse order; a literal support error',
 'The statement Z=Supp(B/A) has codimension>1 is generally false whenB repairs height-one nonnormality: A=k[t²,t³]_(t²,t³), B=k[t]_(t) gives support at the height-one closed point. A candidate construction should remove a codimension≥2 non-S2 locus after first repairing codimension one; the supplied Z definition cannot do that.',
 'S2-ification/normalization criteria over rings admitting dualizing data are established. The exact global quotient-of-regular theorem and correct open subset require a matched reference; the flawed proof is not marked complete.', 'C',['StacksNormalization'],'medium')
add('Lefschetz and parafactorial marginal leads',W,'87,90','220;375–393','Pic(X−a)=0; pi1(Y′)→pi1(X′)',
 'Margins connect depth≥2/3 with fundamental-group surjectivity/isomorphism and depth≥3/4 plus local punctured Picard vanishing with Picard restriction. A complete-intersection dimension≥4 parafactorial statement and a factoriality criterion are suggested.',
 'fragmentary unproved claims and question-mark arrows',
 'The dimensions, exceptional set a, meaning of closure-dimension1 and local hypotheses are partly illegible. The classical local complete-intersection parafactorial theorem applies to punctured spectra in dimension≥4, but it is not an exact match for every marginal arrow.',
 'SGA2 local Lefschetz/parafactoriality is the relevant published development. Modern local Picard work refines the singular setting. Only the identifiable dimension≥4 core is classA; remaining fragments are F within this composite record.', 'C',['SGA2'],'medium')
add('Fibre-product construction of a bad Cohen–Macaulay-locus jump',W,'92–94','407–518','codim ... saut dans la mauvaise direction',
 'Glue local integral schemesX′ andX′′ of different dimensions along a one-dimensional closed integralD. A compatible nonzero f0 onD lifts to a non-zero-divisorf on the fibre-product ring. Arrange the special hypersurface to be Cohen–Macaulay away from the closed point while the complement has a larger non-CM locus.',
 'construction and algebra sketched; existence choices asserted',
 'The fibre-product quotient identity is verified using f0 non-zero-divisor. Normality ofX′,X′′ gives S1 hypersurface sections. To make V(f′) meet the non-CM locus only at the vertex, that locus must have dimension≤1 locally; merely taking any normal non-CM projectiveS′ does not ensure this. An isolated non-CM point onS′ would supply the needed cone geometry.',
 'Openness and semicontinuity theorems for relative CM properties include equidimensionality/finiteness distinctions. The precise intended example is only partly verified until an explicit projectiveS′ with the required locus is chosen.', 'C',['Stacks00RD'],'medium')
add('Graded split algebra extension: kernel and generation',W,'96','523–564','a) ... b) ... b′)',
 'For connected nonnegative gradedK-algebras A→B→C with degreewise split surjectivephi, the claimed equivalence kerphi=psi(A+)B iff A⊗C→B from sections is surjective requires the extra condition phi psi(A+)=0.',
 'stated without proof; false without missing composition hypothesis',
 'A=B=C=k[t], psi=phi=id gives a andsurjective multiplicationv, but kerphi=0 differs from(t). With phi psi killingA+, induction on degree gives b⇒b′ and b′⇒b. The mapsu:C→B are right inverses ofphi, despite the text saying inverse à gauche.',
 'A graded Nakayama/filtration lemma. Corrected proof is supplied in proof_notes.md; literal missing hypothesis is recorded for ink review.', 'E')
add('Graded isomorphism, sections and flat/projective summands',W,'97','569–579','v^n bijectif ... ne dépend pas ...?',
 'Ifv:A⊗K C→B is a gradedK-module isomorphism, psi is injective and B’s graded pieces are flat/projective iff allA,C pieces are so. With the augmented-composition and kernel hypotheses, isomorphism is independent of the chosen sections.',
 'first claims stated; independence explicitly left to check',
 'A_n andC_n are direct summands ofB_n becauseA0=C0=K; the converse uses finite sums of tensor products in each degree. For section independence, the difference lowersC-degree and is triangular for the finite degree filtration. Without augmented composition, B=k[x,y], A=k[x], C=k[t], phi(x)=phi(y)=t has sectiony giving an isomorphism and sectionx failing.',
 'Elementary graded triangularity resolves the intended open check without finite-generation restrictions, once the missing complex condition is explicit.', 'E')
add('Poincaré-series criterion needs prior surjectivity',W,'97–98','582–621','moyennant a ... P_B << P_A P_C',
 'The coefficientwise rank inequality and equality criterion need b/b′ as well asa. If all graded pieces are finite projective andv is surjective, equality of fibre ranks forcesv to be an isomorphism; over localK the closed point suffices.',
 'stated without proof; missing hypothesis makes literal form false',
 'a alone: A=k, B=k[t], C=k contradicts degree1 inequality. Even equal series with finite free pieces does not implyv iso: A=k[x]→B=k[u,v] sendsx→0, B→C=k[v] killsu. Then P_B=P_A P_C butv missesu. Saved certificates verify these exact examples.',
 'Finite projective rank/Nakayama proves the repaired criterion. The corollary’s omittedb is a substantive dependency, not a cosmetic adjustment.', 'E')
add('Graded flatness questions',W,'98','624–633','A plat/K⇒C plat/B',
 'Under the stated good graded conditions, question(i) asserts A/K flat⇒C/B flat; (ii) asserts C/K flat⇒B/A flat; (iii) then givesB/K flat ifA,C areK-flat.',
 'open on the pages; first implication false',
 '(i) fails even with all intended hypotheses: A=B=k[t], C=k, v identifiesA⊗C withB, but Tor1^B(k,k)=k. (ii) is true becausev isA-linear and givesB≅A⊗K C asA-modules; (iii) follows by transitivity. This completely separates the three arrows.',
 'No new flatness theorem is needed for(ii)/(iii); the literal(i) is refuted. The intended reversal of one arrow cannot be chosen without the scan.', 'E')
add('Polynomial quotient gives a polynomial extension',W,'99','637–652','C≃K[t1,...,tr] ... B≃A[t1,...,tr]',
 'With the corrected graded extension hypotheses and C a polynomial algebra on positive-degree homogeneous generators, choose lifts of these generators. The induced A-algebra map A[t1,...,tr]→B is an isomorphism exactly under the good conditionv iso.',
 'corollary stated without proof',
 'The free polynomial algebra gives an algebra sectionC→B. Section independence ofv then identifies the underlying module map, so it is an algebra isomorphism. Choice of section is equivalent to choosing homogeneous lifts of a basis of indecomposables; an arbitrary nonhomogeneous linear lift is outside the graded formulation.',
 'Elementary polynomial universal property, contingent on the repaired preceding lemma.', 'E')
add('Cote26 plan and functor notation are programmatic',H,'2–3,5,7–11','1–352','Plan, Notations; Problèmes ouverts',
 'The folder plans descent, quotient, tangent/normal, coherent-module and representability theory; Hilbert/Quot/Picard, norms, curves and invariant theory; and defines functor names for Hilb, Quot, Div, Hom, Isom, Aut, Imm and Weil restriction. The list is not an assertion that all these functors are schemes without hypotheses.',
 'plan, definitions, interleaved cancelled revisions and open questions',
 'The cover’s cancelledV differs from catalogueVI. Sections1/2,8/9 and duplicate21 are actual revisions. Picard presheaf and its sheafification are distinguished. A crossed plan is not evidence that the corresponding mathematics was proved or disproved.',
 'FGA, SGA and later algebraic-space representability distribute these subjects across different works. The problem index matches each explicit question separately.', 'F',['FGA'],'high')
add('Points of the étale topos are geometric-point functors',H,'4,6','77–126;176–239','7.9.3 ... points géométriques ...',
 'The reused typescript reconstructs a geometric point from a fibre functor on the étale topos, using its restriction to opens and filtered pointed étale neighbourhoods; it identifies the local inverse limit with strict localization.',
 'proof fragment, cancelled as reused leaf',
 'A point functor is a left-exact colimit-preserving functor tosets. Its category of elements is filtering in the appropriate opposite convention. A unique generic point uses sobriety of the scheme’s topology. Strict localization is a limit of étale neighbourhoods, not an ordinary point of the original affine scheme.',
 'SGA4 theory of points of topoi provides the published form; root independently checked the related cote2 text. Cancellation of the reused sheet does not refute the theorem.', 'A',['SGA4VII'],'high','Reused SGA4 typescript')
add('Points of a slice topos',H,'6','176–239','points ... couples(phi,xi∈phi(Y))',
 'Points ofE/Y correspond to a pointphi ofE together with an elementxi∈phi(Y); the associated point functor is obtained by the fibre overxi.',
 'proved in the reused fragment',
 'ForZ→Y, take the fibre ofphi(Z)→phi(Y) overxi. Conversely compose a slice point with the base geometric morphism and recoverxi from the diagonal/universal section. These constructions are inverse on morphisms as well as objects.',
 'Standard topos slicing, published inSGA4. This is not a conclusion about all topoi having enough points.', 'A',['SGA4VII'],'high','Reused SGA4 typescript')

if __name__=='__main__':
    (P/'claims.json').write_text(json.dumps(claims,indent=2,ensure_ascii=False)+'\n')
    print(f'{len(claims)} manually composed claims saved')
