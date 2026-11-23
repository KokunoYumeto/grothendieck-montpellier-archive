# Mathematical dictionary and proof bridges

These are translations of the precise proved statements, not additional claims about every part of Grothendieck's programme. Current checking scope is in CHECK_EVENTS.tsv. Source claims outside the selected papers remain distinguished from current certification.

## Record: workbench/records/paper_1/DICTIONARY.md

# Paper 1: schemes over the integers, line bundles, and wild inertia

## Persistent Picard classes and cohomological dimension

Earlier IDs: SA12:A:A2-persistent-arithmetic-counterexample, SA12:A:A2-quadratic-step, SA12:A:A2-wreath-calculation, and SA12:A:A2-sharp-curve-consequences.

Algebraic geometry: there is an excellent Dedekind domain R with 2 invertible, algebraic fraction field K over Q, cd₂(K)=1, and cd₂(U)=2 for every nonempty affine open U of Spec R. For every nonempty open U, Pic(U)/2 has infinite dimension. All residue fields are nonorderable. Thus even after shrinking, the field dimension and the supremum of residue-field dimension plus codimension do not control the scheme's dimension in the proposed way.

Proof bridge: each quadratic step makes previously selected primes inert, preserves ideal classes modulo two, and doubles the class-group dimension. The wreath-transfer calculation supplies preservation; genus theory supplies growth. Eventual inertness makes the integral tower a noetherian Dedekind domain, an aspect already present in Popescu's 2022 construction. Additional dyadic controls and norm arguments kill the two-primary Brauer group after every finite extension. The Kummer sequence then turns the surviving Picard classes into degree-two étale cohomology. Removing finitely many closed points kills only finitely many independent class generators.

Programme: this is a regular one-dimensional scheme over Spec Z[1/2], generally not of finite type. It answers the persistent Pic/2 and cohomological-dimension questions actually written in cote31, archive sheet84 (the 85th image in the scan numbering). It does not disprove a theorem restricted to finite-type arithmetic schemes. In K-theory language, for each affine Dedekind open the rank-and-determinant map identifies K0 with Z⊕Pic: a positive-rank projective module over a Dedekind domain is the direct sum of a free module and its determinant ideal. Consequently the reduced K0 modulo two is also infinite-dimensional in this example. This is a translation of the Picard assertion, not a new λ-ring theorem or a statement about higher K-groups. The standard rank-and-determinant identification and its proof are in Daniel R. Grayson, Weight filtrations in algebraic K-theory, author version dated13November1992, p12: https://www.graysonfamily.org/dan/Papers/seattle.pdf (opened; retrieval details in DICTIONARY_SOURCE.json).

## A mixed-characteristic wild class

Earlier ID: SA12:A:wild-affine-counterexample.

Algebraic geometry: for A=W(F2-bar)[[t]] and U=Spec A[1/t], one has H³(U,F2)≠0 and cd₂(U)=3, although A is complete regular local of dimension two. The decisive class is the wild symbol with coefficient 1+t.

Proof bridge: localize at the vertical height-one prime, compare the Brauer class with the two-dimensional purity sequence, and use the exact Kato filtration and refined differential in Suzuki's formulation. The differential has a nonzero dt component and cannot come from a class over the original mixed-characteristic ring. Gabber–Orgogozo's upper bound closes the equality. The original concern about the filtration locator is resolved in the source-check and separate-reproof records.

Programme: this concerns the residue-characteristic part of étale cohomology. It does not alter the prime-to-residue-characteristic purity statements. No weight or motivic decomposition is inferred from the nonzero wild class.

## Birational invariance of the torsion Picard scheme

Earlier IDs: SA12:B:L6-R1-vanishing, SA12:B.1, SA12:B.1b, and SA12:B.1c.

Algebraic geometry: a proper birational map from a normal integral scheme to a regular integral noetherian scheme has R¹f*O=0 in the stated positive-characteristic setting. This is already covered by Ishii–Yoshida's theorem. For proper varieties over an algebraically closed field, pullback also identifies the whole torsion Picard group scheme, including its nonreduced part. Finite-torsor invariance already gives that consequence, as compared explicitly with Li–Wang.

Proof bridge: the birational map is an isomorphism away from codimension at least two in the regular target. Moret–Bailly's finite-flat-torsor purity and uniqueness over normal schemes extend the equivalence of torsors. Cartier duality converts torsors into morphisms from finite commutative group schemes to the Picard scheme. Such finite groups detect every proper commutative group scheme: prime-to-p torsion is dense in its reduced abelian part; torsion points meet its components; a finite Frobenius kernel detects the remaining infinitesimal part. This proves the Picard deduction in the paper without replacing a group-scheme assertion by a point-group assertion.

Programme: the direct manuscript connection is cote29, sheet71 and its following discussion. The result concerns the degree-one Picard object and its torsion components. It does not imply invariance of every Chow group, motive, or higher direct image. These claims are credited as known theorems or explicit consequences, not announced as new.

## A neighborhood of the entire boundary

Earlier IDs: SA12:D:boundary-neighborhood, SA12:D:fixed-boundary-positive, and SA12:D:finite-exceptional-wild.

Algebraic geometry: the quotient of the étale fundamental group obtained by killing the inertia along the original codimension-one boundary is finitely generated if the entire boundary lies in one quasi-projective open. In particular a normal proper variety punctured at one closed point of codimension at least two has finitely generated fundamental group. The stated extension to a possibly nonnormal proper variety is also proved.

Proof bridge: the projective tame theorem gives finite generation on a projective model. A Chow modification that is an isomorphism near the boundary has new exceptional divisors inside the original open; covers from that open have no ramification there. The finite exceptional wild-inertia criterion records exactly what must be controlled for more general modifications. Normalization and a finite gluing graph give the nonnormal variant. Esnault–Kerz, including their erratum, and the precise Drinfeld, Mehta–Nori–Paranjape and Raynaud inputs are compared in the records.

Programme: the proved neighborhood case closes the specified one-point question. The unrestricted boundary question remains: can exceptional wild inertia on a projective modification have finite image in the indicated quotient? The deeper reductions asserted elsewhere in the attached run are registered as source claims unless a current check explicitly certifies them. This work does not claim a solution of the full local-fundamental-group programme.

## Original divisors and valuations on later models

Paper1 Example4.3 (ROOT:original-boundary-strict-tame) proves that, for the diagonal translation quotient of P1 times P1 in characteristic p, the group for the original point boundary is Z/p while the all-valuation tame group is trivial. The proof bridge is purity on the smooth covering surface followed by the identity tangent action on its blowup. In the language of schemes and covers, this distinguishes two Galois categories; it gives no new assertion about motives, weights, lambda-rings or K-theory. The distinction concerns the boundary questions already tied to the cited Montpellier notes; no extra archival attribution is asserted.



## Record: workbench/records/papers_2_3/DICTIONARY.md

# Dictionary of findings: papers2 and3

All identifiers here are provisional record aliases. Permanent WB identifiers are assigned on filing, not by this worker.

## Polarization classes (G1)

Algebraic geometry: a polarization component of the relative Picard sheaf has a section functorial in every polarized abelian scheme of fixed type exactly when its alternating two-torsion form has rank at most2. Symmetric classes correspond to quadratic refinements. Rank0 has the zero refinement; rank2 has the refinement1 on all nonzero vectors of the nondegenerate quotient. In rank at least4, symplectic transvections obstruct an invariant refinement.

Programme: this is a universal choice of a divisor class on abelian schemes over Z[1/2], with an obstruction concentrated at2. It concerns relative Picard classes, not automatic existence of a global representing line bundle on every total space. Cote59sheet13 supplies the canonical torsor context. No further lambda-ring, K-theory or motivic conclusion is claimed.

## A very ample negative-H1 surface (A3)

Algebraic geometry: a smooth projective characteristic2 surface has a very ample L with h0(L)=562, h1(L^-1)=1 and h1(O)=565. A Raynaud-type cyclic surface provides a generated ample Q with exactly one negative first-cohomology class. A generic basis of Q^9 has556 members. Simultaneously adjoining their ninth roots makes the pullback of Q very ample and preserves precisely that class. The proof explicitly handles smoothness, geometric connectedness, local coordinate generation and every character summand.

Programme: the nonvanishing gives a one-dimensional tangent kernel for restriction of Picard schemes to a smooth hyperplane section. It makes no assertion that a nonzero rational point lies in the Picard restriction kernel. The construction is related to the Picard hyperplane questions in the attached dossier; no unsupported archive quotation has been added for that relation. Its numerical assertions have independent Riemann--Roch and principal-parts verifications.

## Local versus Artinian universal models (P and pro7)

Algebraic geometry: the functor P(R)={x in R^h_(t):x^p=0} is an arbitrary fpqc sheaf with finitary and complete-local effectivity properties, yet is not a separated locally quasi-finite scheme. Its Artinian model does not represent all local tests. With both premise and conclusion explicitly relative to each complete base A, replacing local universality by the Artinian universal property gives the representability theorem. P satisfies both fixed-base and relative actual propagation, but not relative pro-modular propagation. The proof assembles finite formal branches, separates them by valuation tests, and descends through completion.

Programme: this identifies which local universal property belongs in Grothendieck's scheme representability programme. The direct source is cote131sheets13,34,36; Murre1965p247 announced a locally-quasi-finite analogue but did not specify this full modified list or prove it. The counterexample has alpha_p closed fibre and does not contradict the published unramified theorem. No excellence is used in the stated corrected criterion.

## Modularity openness and adic effectivity (L1 and L2)

Algebraic geometry: fixed-base propagation7_S does not make the locally modular locus open. Over S=Spec F_p[t], H(R)={x:x^p=0 and x=t a x for some a} satisfies all the fixed-base axioms and every noetherian-adic effectivity condition, but M(S,0)={(t)}. After passage to F_p[[t]], its zero pair violates propagation. The corrected openness theorem uses7_rel, with both premise and conclusion for F_A on A-schemes; a uniform Artin--Rees test controls directions transverse to strata. This is an explicit replacement of the hypothesis, not a silent base change or an asserted implication7_rel=>7_S.

Programme: these results distinguish algebraization of compatible infinitesimal data from a local universal property on schemes. They do not assert that all moduli functors satisfy the axioms. The manuscript's unrestricted axiom8 is itself too broad for represented functors; a finite-type qualification is explicitly recorded.

## Finite semilocal descent in every Artinian rank (A4)

Algebraic geometry: vanishing of additive Amitsur H1 on all radical quotients is equivalent to vanishing of GL_r H1 for any one fixed positive finite rank, hence all finite ranks, and to effective descent of arbitrary flat modules on those Artinian quotients. It implies finite flat descent before completion. Over an Artinian base, all flat base changes preserve all-rank effectiveness. The rewritten proof normalizes additive primitives modulo the radical and removes a matrix cocycle one nilpotent order at a time. A uniform nilpotence argument works for all column-finite matrices; Artin--Rees corrects approximate finite bases before completion. This replaces the earlier unipotent-orbit route.

Programme: this proves the descent theorem stated in cote128sheet25 while separating its finite-rank and arbitrary-rank quantifiers. It is a theorem about quasi-coherent flat modules and effective descent; no additional K-theory or lambda-ring conclusion is inferred. The arbitrary-rank analogue over a non-Artinian semilocal base remains outside the theorem.

## Uniform local cohomology and metabelian covers (F8, F10, F11)

Algebraic geometry: on a fixed SNC resolution of a complete normal local surface, first étale cohomology with tame finite F_p coefficients is bounded linearly in the coefficient rank, independently of the monodromy group and its tame inertia orders. A root stack removes the inertia. Frobenius gives a common pole cutoff, while generic stabilizer characters cancel the growing number of root-divisor layers. Published local refined-Swan integrality bounds the entire abelian conductor vector by the inverse negative intersection matrix. Together with the Kummer adjugate bound and Suzuki's finitely generated abelian quotient, this makes the abelian inertia kernel finite.

Programme: one finite cover then removes all abelian inertia at once, giving the rank-linear cohomology control needed for finite metabelian quotients. Complement counting gives a common generator bound and compactness gives finite generation of the maximal metabelian quotient. This advances the specific metabelian part of Grothendieck's local fundamental-group question; it does not prove finite generation of the full group or arbitrary solvable derived length. The full wild-coefficient estimate is a precise remaining gate. The three main assertions have independent same-model reproofs and adversarial comparison; exact literature overlap and priority are separately unsettled.


## Smooth-surface tangent-line exclusion (current closure)

The exact row SA14_SA19:A2Gs-cross now has a complete proof, at ROOT_SMOOTH_TORSOR_CHECK.md and Paper2 Proposition prop:tangent-ample. In geometric language, a smooth ample curve cannot be an everywhere-regular leaf of a tangent line subbundle equal to its negative divisor bundle. In K-theory the short exact sequence gives [T_Z]=[O_Z(-D)]+[Q]; applying the Chern-class homomorphism yields c2(Z)=(-D)(D-K_Z), and adjunction forces K_Z.D=0. These are the precise bridges to the intersection argument. Differentiating the stated finite-flat torsor gives exactly that forbidden K-class decomposition under both smoothness assumptions. No claim about general lambda-rings, weights, or a motivic obstruction follows, and no additional archival cote is inferred. The geometric Picard-point kernel remains open.


## Abelian torsors, changing structure group, and the full Picard space

Current results ROOT:E4-abelian-pushout and ROOT:E4-abelian-torsor-Picard prove that a scheme torsor under an abelian scheme remains a scheme after pushout by any homomorphism to another abelian scheme, and that its entire fppf Picard space is a separated scheme locally of finite presentation over any base. The kernel of the homomorphism need not be finite, flat or of constant dimension. No projectivity or normality is assumed. The fresh main-statement-only reconstruction and the post-freeze reciprocal manuscript check are fully closed with root PASS. The complete proof and root targeted source comparison are in E4_RESEARCH_CONTINUATION.md and ROOT_E4_TRANSFER_COMPARISON.md; ROOT_E4_FRESH_COMPARISON.md records the fresh comparison.

The bridge is geometric, not merely an equality of cohomology classes. A single affine neighborhood over a local base gives the AF property under a connected group action. A finite normalization makes the source torsor and target group projective; a finite flat multisection and Raynaud's two-cover criterion then produce the descended scheme. The full Picard sheaf is a torsor over the varying Néron–Severi scheme, obtained by a pushout of two scheme torsors. The symmetric-class torsor proves that the component torsor on the abelian scheme is schematic without assuming a global representative line bundle.

In the schemes-over-Z programme this is an arbitrary-base representability result, including mixed characteristic and nonreduced bases. It controls when divisor-class moduli are schemes rather than algebraic spaces; it does not prove a new lambda-ring, K-theory, motive, correspondence or weight identity. Those languages supply no additional conclusion here. The attached E4 record connects the broader question with cote57, archive sheet314 (PDF page315; the inherited locator used the PDF page); the proof settles the abelian-torsor construction explicitly left open in its lines81–93, while the general normal/integral-family question remains open. The Picard conclusion is credited to its earlier statement in Achter–Casalaina-Martin §1.7.2, with the arbitrary-base proof and component-torsor details stated here.


## Projective modifications of abelian-surface torsors (M2)

Paper2 Theorem4.1 (p9 in the current fresh build) proves the following over an arbitrary base S. Let Q be a torsor under an abelian surface scheme, let X be a proper, flat, finitely presented S-scheme with geometrically integral fibres, and let X→Q be projective. If every geometric-fibre map is birational, or if the map is an isomorphism above a dense open of Q, then Q is a scheme. No normality assumption on S is made. The rank-one pushforward is a line bundle times an ideal with a finite flat quotient; its nonempty defect supplies a splitting multisection, and its empty defect forces the modification to be an isomorphism. Noetherian approximation treats both formulations.

The complete proof/source comparison and the independent main-statement-only root comparison are closed with PASS. The full reciprocal review is frozen PASS and has been read entirely by root; that checking gate is closed. The frozen full proof is E4_MODIFICATION_PROOF.md and the root comparison is ROOT_E4_MODIFICATION_COMPARISON.md. This closes the abelian-surface modification branch of the inherited schematicity construction. It does not settle the projective-bundle branch, higher-dimensional modifications, or the general geometrically normal/integral-family Picard schematicity question. The rank-one surface-sheaf structure is credited to Su–Wang; no priority claim is inferred.

## Auxiliary constraints on the geometric Picard-point kernel (A2)

Paper2 Section9 supplies two further constraints, with full targeted proof and primary-source checks. Proposition9.1 (p20) says that a smooth purely inseparable multisection R of degree q≥2 of a smooth quasi-elliptic surface over a smooth curve C satisfies R²≤(2−5q/3)(g(C)−1). It therefore excludes ampleness when g(C)≥1. Its hypotheses do not include arbitrary multisections with a separable part.

Proposition9.2 (p21) treats the normalization N of the mu_p-torsor attached to a nontrivial order-p line bundle trivial on a smooth ample curve Y. The logarithmic differential is proved to have order pa along Y for some a≥1, with nonzero tangential leading coefficient. The divisor D=π*Y is reduced, integral, ample and Cartier, and

    2g(Y)−2 = apY² + (ell + 2delta)/(p−1),

where ell is the residual conductor defect along D and delta is its normalization genus defect, both nonnegative. Equality forces D to be smooth and N to be regular near D and Gorenstein everywhere; isolated Gorenstein singularities away from D are still permitted. The statement does not assume N smooth or Gorenstein at the outset. This conductor calculation is distinct from the local-group Swan-conductor bound.

These are auxiliary exclusions and identities, **not a closure of general A2**. In particular, the geometric Picard-point kernel remains open; the previously proved smooth-surface tangent-line exclusion is Proposition8.1 and its torsor consequence is Corollary8.2 in the current numbering. Root reports complete expert, newcomer and individual-page visual coverage of the accepted 33-page PDF, SHA256 `13ef80588f15e256a9557a4aca9b9673e06b9c2aabef680e0e16e557cb7740f4`; all final changed pages were reread and inspected.


## Equality action and singularity constraints,23November2026,08:56UTC

In the smooth-surface order-p geometric Picard kernel, equality in the conductor bound yields a genuine torsor under the classical line-twisted deformed multiplicative Kummer kernel (Paper2 Cor9.3). Its normalized cover has a locally free tangent sheaf even if singular; the zero scheme of the divided logarithmic form on the smooth base has length c2(X)+apY² and pulls back to the Fitting singular scheme (Prop9.4). For a=1, a resolution has Kodaira dimension at most zero, and a nonzero plurigenus forces the normal canonical class to be torsion (Cor9.5). The full proof comparison is ROOT_A2_EQUALITY_SINGULARITY_COMPARISON.md with its exposed worker records.

In the broader programme, this distinguishes geometric points of a Picard kernel from tangent directions and replaces an unsupported smoothness step by a finite singularity invariant. The Chern and Koszul calculation belongs to intersection theory and K-theory of vector bundles; no new lambda-ring, motivic or weight consequence is claimed. The archive connection is the Picard restriction question already authenticated in the dossier, not a newly assigned cote. General point-kernel existence remains open.

## Projective bundles over normal-base abelian torsors

If S is normal, Q is an algebraic-space torsor under an abelian S-scheme, and E is a finite locally free sheaf of everywhere positive rank on Q, schematicity of P_Q(E) forces schematicity of Q. In the programme on relative Picard representability, this excludes all normal-base projective-bundle realizations of the nonschematic-torsor route; the arbitrary proper geometrically integral-family question is still open. The proof uses Ramanujam--Samuel to make affine boundaries Cartier, the homomorphisms of abelian varieties associated with global line bundles, and the projective-bundle intersection formula on a curve. If the line-bundle homomorphisms have a positive-dimensional common kernel, the top tautological intersection is zero while every affine boundary forces it positive. Normal noetherian approximation extends the result to arbitrary normal bases. The reference to Grothendieck's cote57 sheet314 is the same Picard-family question already quoted in Paper2, not a new archival identification. This conclusion makes no assertion about lambda operations, motives or weights. Root's complete proof/source comparison passes; the new independent main-statement-only reconstruction is still in progress.
# Smallest Picard-kernel equality case after Ekedahl — 23 November 2026

`ROOT:A2-ekedahl-smallest-equality` concerns a smooth projective surface X over an algebraically closed field of characteristic p, a smooth ample curve Y, and a nontrivial order-p line bundle M that restricts trivially to Y. In the smallest conductor case a=1 with 2g(Y)-2=pY², Ekedahl's published foliation theorem reduces the surface to two alternatives: a degree-p purely inseparable image of a ruled surface, or characteristic two with ample canonical bundle, chi(O_X)=1, omega_X²=O_X(2Y), and the normalized Kummer cover having rational double points and K3 resolution. The latter alternative has 1≤Y²=K_X²≤9 and explicit singular-scheme lengths.

The proof bridge is the saturated annihilator of the divided logarithmic form, with line bundle O_X(pY)omega_X^{-1}. Adjunction puts it on the boundary of Ekedahl I.2.4(ii). The invariant field K^p(u), together with the identity k(N)^p=K^p(u), identifies the theorem's cover with the normalization belonging to M. This converts a Picard-restriction question into a precise foliation and surface-classification gate. It does not provide an example or exclude the two remaining branches. No additional implication for lambda-rings, arithmetic schemes, weights, or motives is asserted. The archival connection remains the existing Picard-dossier question; this application introduces no new archive quotation or cote.

Full proof: Paper2, `prop:normalized-mup-ekedahl`. Complete checks: `ROOT_A2_EKEDAHL_COMPARISON.md` and the frozen `a3_a2_ekedahl_audit/AUDIT.md`. This is an attributed application of a known theorem, not a claim of historical priority.



## Conditional K3 structure in the smallest Picard-kernel equality case

ROOT:A2-ekedahl-smallest-equality applies Ekedahl's exact foliation theorem to the saturated annihilator of the logarithmic differential. The fixed-field computation identifies the theorem's cover with the normalized Kummer torsor. It reduces a=1 equality to almost-ruled surfaces or a characteristic-two canonical surface with chi=1 and K3 normalization; it does not decide either existence branch.

ROOT:A2-k3-ample-curve-vanishing is a Cartier-adjunction and duality lemma. It supplies the cohomology needed to split the singular tangent bundle in ROOT:A2-k3-derivations, where global squares are scalar and Matsumoto's rational-quotient theorem gives rational domination in degree four of the base. ROOT:A2-k3-paracanonical identifies the exact additive cover and the torsion twist of the canonical curve, by comparing quotient line bundles and saturated foliations. ROOT:A2-k3-singularity-types applies the known local classification and independently computes its Fitting lengths. These statements describe the geometry and flat-torsor obstruction in the Picard programme; they make no additional claim about schemes over Z, lambda-rings, motives or weights. No unsupported archive identification is assigned. Complete proofs and sources are in ROOT_A2_K3_STRUCTURE_COMPARISON.md and the paper's Section10.3.



## Very ampleness and the smallest equality branch

ROOT:A2-small-degree-curve-bound applies Kadets's geometric monodromy theorem after proving nonstrangeness by the Euler sequence. Linear general position and a Hilbert-deficit sum bound the genus, in every characteristic. ROOT:A2-very-ample-numerical-obstruction combines that bound with adjunction and regular-immersion self-intersection: the last ambient dimension would require d²=17d−12, impossible for integral d. ROOT:A2-very-ample-equality-almost-ruled uses the fully checked conductor identity and Ekedahl reduction to exclude the exceptional K3 branch for a smooth very ample curve. This is a strict reduction of a Picard point-kernel construction; it gives no general injectivity theorem and no geometric-point counterexample. For merely ample curves the K3 branch remains. These are statements about torsion line bundles and projective embeddings in the Picard programme, with no additional claim about lambda-rings, motives or weights and no invented archival locator. Complete proofs, the exposed comparison and exact source scope are in ROOT_A2_VERY_AMPLE_COMPARISON.md.



Positive-genus fibration notation: C is the ruling curve; B=C^(p); f:X→B and h:N→C; F is a general fibre on X and b=Y.F. The proven degree bound is b≥p+2 for a=1. The higher-conductor formula assumes the additional ruled model. See ROOT_A2_POSITIVE_GENUS_COMPARISON.md.

## Equality torsors, Euler characteristic and rational domination

The deformed height-one torsor has an intrinsic vector-bundle flag. Its weight quotients express its K-theory class as the sum of O(iaY) twisted by a p-torsion character. Additivity of Euler characteristic turns this identity into the exact general-conductor formula. For a rational normalized cover, the failure of rational singularities is measured by epsilon=h0(R1r_*O); in characteristics other than three this defect is positive and at least p-1. An extended ruling would force the defect to vanish, so any example must have indeterminacy. In characteristic two, Betti numbers, the canonical class and the explicit divisor/fibre intersection matrix exclude the entire positive-genus branch. The normalized torsion cover must be rational, while its smooth purely inseparable quotient remains nonruled. These strictly smaller gates concern the Picard dossier question, not a new general theorem about motives or lambda-rings. Exact archive connections remain those cited for the original Picard question. Proofs: ROOT_A2_EULER_COMPARISON.md and ROOT_A2_CHAR2_RATIONAL_COMPARISON.md; full text is in the two corresponding paper subsections. General A2 remains open.

## Canonical-section obstruction for the rational torsion cover — 2026-11-23T13:33:24.417958+00:00

ROOT:A2-rational-canonical-defect,ROOT:A2-char2-strict-very-ample andROOT:A2-char3-rational-residual strengthen the surface gate ofSA14_SA19:A2. The global torsor flag gives the structure-sheaf class in K-theory and hence its Euler characteristic. For a rational resolution, Leray identifies the singularity defect with H²(O_N); Serre duality turns it into a canonical section. The canonical divisor has degree zero on the smooth ample inverse-image curve, so any such section is nowhere zero. The defect is therefore at most one, and when nonzero the canonical line bundle is trivial. Finite-flat determinants bring this identity back to a p-torsion canonical twist on X. Noether's formula and the independently established projective-embedding obstruction then exclude characteristic-two smallest equality. This is a concrete bridge from the K-theory Euler class to Picard geometry and intersection theory. It introduces no new motive, weight filtration or lambda-operation, and no additional archive cote is inferred. For odd p the stated residual ruled-cover gates remain exactly those in the paper; no global point-kernel vanishing theorem is asserted.

## Separable multisections and the Neron–Severi obstruction

ROOT:A2-positive-genus-ns-obstruction andROOT:A2-positive-normal-separability narrowSA14_SA19:A2. The positive normal degree makes an inseparable multisection incompatible with the tangent degree of a positive-genus base, once the actual smooth product open is established. The ruling-field intersection A∩K=A^p factors every map to an abelian variety through the Frobenius-twisted base. Albanese universality and Picard duality identify Pic0(X)_red with the base Jacobian. Separable function fields cannot acquire the purely inseparable root defining an order-p line bundle, so an offending class must survive in NS(X). This is a Picard/Albanese and divisor-class statement; no new motivic decomposition, weight filtration or lambda-operation is inferred.

ROOT:surface-double-point-inequality is the known Chern-class excess formula, reconstructed with full finite scheme lengths. Applied toROOT:A2-char3-rational-residual it givesd≥22. Its K-theory content is the tangent-normal exact sequence and total Chern quotient; the nonnegative remainder is a genuine zero-cycle, not a proposed weight. No additional archival cote is inferred.

## Generic-fibre torsion obstruction

ROOT:A2-generic-fibre-torsion-obstruction strengthens the positive-genus equality gate. A generic trivialization of an order-p line bundle would give a vertical divisor E and a base function u with div(u)=pE. Triviality on the separable multisection makes u a pth power in a separable extension, hence already on the base, forcing E principal. Thus a possible class survives both in NS and in the Picard group of the regular, potentially geometrically singular generic curve. This is a divisor-class obstruction; no additional motivic or lambda-ring consequence or archival cote is claimed.



## Record: workbench/records/paper_4/DICTIONARY.md

# Programme dictionary

## Grothendieck's pro-Artinian lifting assertion

Algebraic formulation: a formally smooth topological algebra lifts maps across a closed ideal that becomes nilpotent in each Artinian quotient, provided squares of open source ideals remain open. Proof: affine compatibility is solved in Artinian modules after reducing to square-zero kernels; closed powers then reconstruct the target. Geometric formulation: compatible infinitesimal maps into arbitrary pro-Artinian thickenings can be assembled even without a countable cofinal family. Exact source: EGA0_IV19.3.12 and its later withdrawal. No additional assertion about lambda-rings, K-theory, motives, or weights is inferred.

## Nonlocal Cohen lifting

Algebraic formulation: a complete noetherian adically formally smooth algebra admits a flat, complete, formally smooth lift across a square-zero noetherian base extension, uniquely up to reduction-preserving isomorphism; both explicitly defined topological projectivity conditions persist. The proof is carried by projective adic reductions of the cotangent complex, Ext vanishing for finite complete coefficients, and Artin–Rees. Geometric formulation: the corresponding affine formal scheme has an unobstructed deformation over the infinitesimal thickening of its base, without requiring a local coordinate ring. Archival connection: cote22, Definition4.7 on sheet12 and the square-zero existence question on sheet13. The missing earlier definition of conditionP is not reconstructed by guesswork.

## Deligne's algebraic extensions

Algebraic formulation: every algebraic field extension admits a well-ordered monic triangular presentation, and arbitrary Artinian lifts of its equations define a free algebra over the lifted residue-field base. Proof: finite subsets of the residue relations are regular; a finite nilpotent filtration preserves Koszul acyclicity and flatness. Geometric formulation: the chosen presentation of the field-valued point yields flat infinitesimal models even when the lifted equations acquire later variables. Exact archival connection: cote23sheet62. No motivic or K-theoretic consequence is claimed without an additional argument.

## Known EGA corrections

The generic formal fibre is a localization inside the completed fraction field, not necessarily the whole fraction field. Meromorphic functions must use locally regular denominators; outside the noetherian setting their stalks can be smaller than the local total quotient rings. These are already EGA's own erratum and Kleiman1979, respectively, and enter only as source clarification.



## Record: workbench/records/papers_5_6/DICTIONARY.md

# Dictionary for the cycles and gerbe results

These translations describe the precise mathematical scope. They do not assert a new connection to λ-rings or K-theory where none was proved.

## P05-E3e: integral Albanese equivalence has the required odd-cohomology consequence

**Algebraic geometry.** Let N^i(X) be generated by correspondences applied to degree-zero cycles in Albanese kernels. In positive characteristic, an integral family from an abelian variety which is zero in CH^i_alg/N^i acts trivially on the indicated rational and integral prime-to-characteristic odd cohomology. The essential lemma is vanishing of Bloch's torsion cycle map on N^i∩CH^i[ell∞]. Its proof specializes the entire finite relation, preserves the Albanese condition via integral H1, and uses finite-field torsion plus Bloch's theorem.

**Motives and correspondences.** This supplies a realization-theoretic implication for the quotient intended to retain the abelian part of algebraically trivial cycles. It does not identify the quotient with an abelian variety or prove a categorical universal property. The integral premise matters: an elliptic curve over F5bar gives a rationally zero point-group map with nonzero H1 action. The actual archive connection is cote14, Theorem3.1 on sheet37, continued sheet38.

## P05-C1f/C1j/C1k/C2k: algebraic equivalence and the Lefschetz programme

**Algebraic geometry.** Except for degree zero and the middle identity, the universally proposed Lefschetz surjectivity modulo algebraic equivalence fails. Iterated incidence blow-ups of a Clemens quintic give finite source and infinite target in every required pair. The universal finiteness, cycle-map injectivity and algebraic=numerical assertions hold only in codimensions0,1,n. Primitive middle positivity is semidefinite, with radical exactly the kernel of ample multiplication on the middle Griffiths group; strict positivity beyond dimensions0,2 remains undecided here.

**Motivic programme.** The failure is specific to the quotient by algebraic equivalence. It does not refute hard Lefschetz in cohomology or settle the usual standard conjectures for homological equivalence. The divisor, curve and codimension-two homological=numerical results used for comparison follow classical Hodge theory. Archive connection: the letter to Serre of27August1965 is cote14 sheets43–45 (Conjectures A,B and finiteness consequences).

## P05-C4: the integer obstruction to Jacobian factors

**Algebraic geometry.** The scalars whose multiplication maps factor through products of Jacobians form a nonzero ideal. Its positive generator divides (2g−1)!; for surfaces it divides gcd(2,δ(A)), for threefolds gcd(6,δ(A)), where δ is the gcd of Euler characteristics of line bundles. Scalar1 means a direct product decomposition as abelian varieties. The proof combines the known exact Matsusaka scalar, known principally polarized constructions, principalization by subgroup schemes, Poincare Euler characteristic and integral interpolation. The remaining prime2, or primes2,3, are exact unresolved obstructions; their actual occurrence is not proved.

**Motives and K-theory language.** The factorization takes place integrally on abelian varieties and thus controls the abelian h1 contribution under the corresponding functorial realization. Euler characteristic supplies an integer through Riemann–Roch; no new λ-ring theorem or integral Chow-motive decomposition is claimed. There is no manuscript sheet quoted for this deduction beyond the authenticated cycle-programme context.

## P06-known-Hasse/class: weights and the finite-field gerbe

**Algebraic geometry and arithmetic.** With the full Weil-number definition, M=Γ^0/μ∞ is a rational Galois module, complex conjugation acts by−1, and H^0=D(M) is a protorus. Division lattices kill the derived-limit H1 term, giving the compact Hasse principle. Artin rigidification yields H^0×Gm; Artin–Tate rigidification yields H^0×μ2. The known global class is the pair of a valuation class supported at p and the quaternion class supported at p and infinity.

**Grothendieck's programme.** Milne's Weil-number germs identify the same character module; his finite-level Hasse statement, inverse-limit theorem and global fundamental class already yield these conclusions. Thus this is a dictionary to a known theorem, not a new research paper. Identification with all numerical pure motives needs the stated full Tate and symmetry hypotheses, and the real positivity interpretation keeps its additional assumption. No archive quote is invented to support a stronger claim.
