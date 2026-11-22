# Part A working notes

## 20 November 2026: checked source limits

SGA 2 XII, Corollaries 3.4–3.6 (2005 reprint pp.119–121) have been opened and read. XII.3.4 gives effective Lefschetz for a smooth projective X of dimension at least 3 and an effective ample Cartier divisor Y. Regularity allows line bundles algebraized on a neighborhood of Y to extend to X. XII.3.6 still requires H1(Y,O(-mY)) and H2(Y,O(-mY)) vanishing for a group isomorphism. It does not settle A1 without vanishing.

SGA2 XII.4, editorial note 5, reprint p.128 explicitly distinguishes Kodaira counterexamples and the unanswered surjectivity question for thickenings. The 2024 paper Cotner–Zavyalov, Examples 3.3.6 and 3.4.6, likewise distinguishes Picard-scheme failure from Picard-group failure; footnote6 says the conditional group counterexample is not known there to occur.

Lauritzen–Rao, §2 (arXiv six-page version pp.4–5), proves nonvanishing only in degree 3n−4 on a variety of dimension 3n−3, n≥3. It explicitly proves vanishing in all lower degrees. Thus this cited family does not answer A3. Its hyperplane restrictions do not automatically move the failure down to degree 1.

## New reduction to test and include

If a smooth projective n-fold, n≥2, and a very ample L have H1(L^-1)≠0, then there is a smooth projective surface with a very ample M and H1(M^-1)≠0. For n>2 choose the largest a≥1 with H1(L^-a)≠0 (finite by Serre duality and Serre vanishing). A general Y∈|L| is smooth, and 0→L^(-a-1)→L^-a→L^-a|Y→0 gives an injection of the nonzero H1 into H1(Y,L^-a|Y). M=L^a|Y is very ample. Iterate. This is a reduction, not existence.

If A1 fails in dimension n>4, choose a sufficiently high-degree smooth complete intersection hyperplane D transverse to Y, with PicX≅PicD and PicY≅Pic(Y∩D) by XII.3.6 and negative-twist vanishing on X,Y,D,Y∩D. The square transfers the same failure down one dimension. Iterate to n=4, preserving that Y∩D is a hyperplane for the restricted original embedding. Need spell out choosing degrees simultaneously via exact sequences and Serre duality.

## Approaches tried, not conclusions

1. Standard SGA2 isomorphism: stops at the unprovided vanishing hypotheses.
2. Bhatt–de Jong local theorem: only injective up to p-primary torsion; their local counterexamples do not give smooth projective global examples.
3. Flat-cohomology Lefschetz (Cotner–Zavyalov): requires strong ampleness/Hodge equivalence, stronger than very ampleness. Scheme tangent failure does not prove group failure.
4. Lauritzen–Rao examples: high cohomological degree; H1 is zero.
5. Raynaud/Mukai surfaces: ample line bundle needs an independent very-ampleness check; cannot replace ample by very ample via a power since nonvanishing can disappear.
6. Finite covering trick: might make a globally generated ample line bundle very ample after a tame cover, but fails directly for a line bundle with base locus. No claimed construction yet.

## 2026-11-20 15:10 UTC: refined A3 gate and homogeneous tests

Enokizono arXiv2104.00197v2 Th4.20 gives q_nil>=h0(L) for any very ample H1-negative counterexample. On a surface h0(L)>=5 because embeddings into P2/P3 have H1(O)=0. Terakawa1999 Th1.6 and Zhang arXiv2103.04268v7 corrected Th3.1 exclude every nongeneral-type surface: a very ample bundle on the general cuspidal genus-one fibre has degree>=3, above both corrected vanishing bounds. Terakawa also gives L²<=K_min² for p>=3 and its max(K²,K²−3χ+2) bound in p2. Langer Cor11.2 excludes smooth W2-liftable examples. These deductions are now written in A3n/A3s.

An exploratory Euler-polynomial search through 9216 complete-intersection/target polarizations on P(F*Udual) over Gr(2,n), n3..8, p2,3,5,7,11,13, coefficients1..4, found no negative Euler characteristic. The formulas were independently checked in243 Frobenius-incidence hypersurface cases for n3; they remain exploratory until a full geometry/K-theory audit. This does not exclude H1-negative examples. A direct finite-field graded-relation calculation for n4, p2/3 is running to look for a dimension excess that could be tested for saturation and smoothness.

## 2026-11-20 15:29 UTC: exact Raynaud Cech search and proposed full-family exclusion

The exploratory n4 incidence quotient calculation returned dimensions116 versus chi113 in characteristic2, and263 versus chi267 in characteristic3. This is not a sheaf-cohomology calculation: saturation and missing global sections can change the answer. For p2, the homogeneous variety can have25 global sections of H+B whereas its displayed bilinear embedding supplies only24, which plausibly accounts for the discrepancy after three cuts. This route has not yielded a counterexample. Cutting by three merely semiample H divisors also has a smoothness obstruction: the Frobenius-incidence projection to projective space has differential rank one along its P1 fibres, so three pullback hyperplanes cannot define a smooth codimension-three surface by that displayed morphism. This last observation is still an approach note, not a promoted result.

The exact new script search_raynaud_cech.py tests C:y^p-y=x^(pr-1), with t=y/x^r, D=(r(p-1)-2)infinity, extension class t^-1 in H1(O(-D)), and N=O((degD/ell)infinity). At infinity x=t^-p w with w=1+t^(p(degD+1)+1)w^(-degD-1). A morphism Sym^n E→O(c infinity) has coefficients a_i in the affine curve ring with pole<=c+i; the transition requires sum binom(j,i)(-t^-1)^(j-i)a_i to have valuation>=j degD-c. The finite matrix therefore exactly tests this explicitly stated Cech model, subject to the independently checked projective-bundle convention. It ran1008 cases in10.692seconds. No case with a>=ell had nonzero H1. Four stated-range p2/p3 edge cases disagree with Zheng2015v1 Th3.7; this is under independent and journal-version review, not yet a certified correction. The journal web endpoint returned403; arXiv lists onlyv1.

A proposed general explanation is under targeted review by dgj. If 0→O→E→L→0 is nonsplit, degL>0, and F*E splits, then for0<=n<p and degM<n degL one expects Hom(Sym^n E,M)=0: the Frobenius-pulled map kills its top L^(pn) summand by degree, while horizontality for the canonical connection forces it to kill all lower summands because the second fundamental map L^p→Ω is nonzero and the integers1,...,n are invertible. For a=ell the cyclic-cover R1 summands have n=i(p+1)/ell-1<p and degM-n degL=-(i+b)degN<0. Thus H1 would vanish at a=ell. The exact sequence for adding the positive section injects H1(a+1,b) into H1(a,b), extending vanishing to every a>=ell,b>0. All a<ell fail fibre very ampleness by A3f. If the connection/convention check passes, this excludes the entire two-parameter Raynaud family, not only the published sufficient range. It does not solve A3 outside that family.


## 2026-11-20 16:09 UTC: main A routes after A3

A3 is now fully proved in A3_very_ample.tex, superseding the earlier surface-existence gate. Its cover is explicit over the algebraic closure of F2 in556² independent coefficient variables; it preserves h1=1 while making the first power very ample.

Reopened Bhatt–de Jong Theorem2.9 and introduction: arbitrary semiample big divisor still gives only a finite p-primary Pic-tau kernel. The introductory classical injectivity sentence does not assert a new positive-characteristic theorem. Opened Badescu1978 Theorem on p170 and proof Steps1–4 pp171–172: its injectivity assumes all negative Hq(O(m)) vanish, so it does not remove the A2 gate. Source https://www.cambridge.org/core/services/aop-cambridge-core/content/view/400E2F7B98BDDF3C97F65700BE9FB361/S002776300002170Xa.pdf/remark_on_the_grothendiecklefschetz_theorem_about_the_picard_group.pdf .

Root independently noticed that Cotner–Zavyalov2024 Example3.4.6(ii) asks incompatible smooth one-form injectivity and alpha_p torsor noninjectivity. FHI checked with a direct natural injection H1(alpha_p)→H0Ω1. Full short proof appended to A; this removes that apparent counterexample route but does not by itself move the universal A1/A2 gate.

Exploratory constructions considered (no theorem claimed): a p-torsion line bundle trivial on a smooth ample divisor yields a Cartier-fixed logarithmic form vanishing along that divisor; normalization of its mu_p torsor may change it into an inseparable residue extension along the divisor. Products of curves and Frobenius graphs do not immediately help because the natural foliation leaves have nonpositive self-intersection. A3 infinitesimal kernels alone cannot be promoted to geometric-point kernels.


## 2026-11-20 16:25 UTC: complete supersingular Igusa audit

Root independently passed all steps of DGJ D4s, including the dyadic-section construction, canonical elliptic subgroup, graph classification, exact quartic hull and flat Pic-tau. Detailed audit: D4_supersingular_audit.md.


## 2026-11-20 16:32 UTC: current-source and logarithmic-form routes for A

Opened Krishna–Majumder, arXiv:2601.12177v2 (8 November 2026), Proposition 11.2 pp66–67 and Definition10.8 p63. Its injectivity statement requires Diff(3,0), i.e. negative differential/coherent cohomology vanishings; it does not resolve A1/A2 without vanishing. The earlier Majumder thesis arXiv:2501.00931v1 Proposition9.4.1 pp134–135 also explicitly imposes the q=0 vanishing hypotheses. No scope strengthening is inferred from snippets.

An unproved route being explored: an order-p restriction-kernel class gives a Cartier-fixed logarithmic one-form on smooth X whose restriction to Y is zero. The conormal sequence and H0(OY(-Y))=0 force vanishing as a section of OmegaX along Y. Exact (Cartier-zero) differentials can have ample vanishing in positive characteristic, so the general differential-form vanishing route is false; one needs a special constraint on the Cartier-fixed subspace. The simple smooth-total-space mu_p-cover argument is insufficient because the torsor can be nonnormal along Y. Normalizing it yields a twisted infinitesimal torsor controlled by negative cohomology, precisely the existing gate; this observation is not promoted to a theorem.


## 2026-11-20 16:37 UTC: counterexample routes tested for A1/A2

1. Wild hypersurfaces: the smooth ample hypersurface sum x_i^p*y_i=0 in P2xP2 is a projective-line bundle over the x-plane, so both Picard generators still restrict to generators; its inseparable projection to the y-plane does not yield a Picard counterexample. General quasilinear plane hypersurfaces require a very restrictive coefficient differential isomorphism for smoothness.
2. A relative Frobenius cover of a smooth family of curves can kill a global p-torsion class, but a multisection that embeds smoothly after that cover must be transverse to the vertical foliation; for an étale multisection its normal bundle is inverse relative canonical, obstructing ampleness in the nef relative-canonical setting. This tests a class of constructions, not all possible foliations.
3. A Frobenius-killed extension 0→O→E→L→0 gives P(E) with a positive-normal section and a disjoint inseparable multisection. The latter prevents the section from being ample. Contracting that negative multisection creates a singularity; its normal degree carries a factor p, so the direct smooth blow-down construction does not apply. Whether a suitable wild smoothing supplies a counterexample remains unproved.
4. Logarithmic-form normalization can have residue degree p along Y (e.g. z^p=1+t^p*a); this defeats a claimed isomorphic reduced lift and any argument that assumes total ramification. Exact and Cartier-fixed one-forms must be kept distinct.

## 2026-11-20 17:00 UTC: Kollár/de Jong depth route

Opened Kollár2021 Families of varieties of general type, Th2.93 and5.53–5.59. The all-characteristic local torsion-freeness theorem requires depth at least3. Its application to the section cone requires H1(X,O_X(m))=0 for all integers m, precisely an extra hypothesis unavailable here. Raising depth by adjoining polynomial variables leaves a positive-dimensional axis where the pulled-back reflexive sheaf is not invertible, so it does not preserve the required punctured Picard class. BCE independently checked the delta proof and the unit-extension use of depth(D)>=2. No unconditional A2 conclusion follows from this source.

## 2026-11-20 17:18 UTC: further A routes and the nilpotent Picard shortcut

Reopened Mukai, RIMS preprint1736, Theorem2 and Sections1.3–2.1, pp5–8. The iterated Tango–Raynaud construction gives ample negative-H1 polarizations in all dimensions, but that by itself gives no geometric-point Picard restriction failure. A proposed logarithmic variant starts from a curve with a p-torsion divisor and uses a regular dlog form. Its pullback may have an ample total zero divisor while the visible support consists of a negative inseparable multisection and vertical fibres. No smooth ample component has been obtained; the new cover coordinate has simple zero along its branch, so its dlog has a pole and is not a regular replacement.

The relative Veronese candidate X=P_B(Sym^2 W), Y=P_B(W), for a rank-two bundle W on a surface B, has relative Picard degree2 but fails ampleness: the normal bundle on Y is O(4) tensor det(W)^(-2), the square of the relative anticanonical bundle. Its restriction to the ruled surface over any base curve has self-intersection0. A smooth ample divisor cannot have this normal bundle. Cones and contractions change smoothness; set-theoretic complete-intersection Veronese examples do not meet the Cartier hypothesis.

Opened Lipman1976, The Picard group of a scheme over an Artin ring, Proposition2.5 pp30–32 and Corollary2.11 p33, https://www.numdam.org/item/PMIHES_1976__46__15_0.pdf. For a nilpotent immersion the full kernel and cokernel are unipotent algebraic groups; the map on component groups has finite etale p-primary kernel and cokernel. The proof establishes connectedness for a single square-zero kernel, but does not establish connectedness of the kernel of an arbitrary composition. Thus this exact source does not justify an assumed nil-invariance of NS or remove the surviving p-primary obstruction in A2. An extension of connected kernels need not apply, because the image in an earlier connected kernel need not be connected. We retain this as an unsuccessful shortcut, not a counterexample to A2.

## 2026-11-20 17:42 UTC: special hyperplanes, logarithmic forms, and finite matrix tests

Opened Kweon, Bounds on the torsion subgroups of Neron-Severi groups, arXiv2008.01908v2, §7 pp16–19. Theorem7.2 identifies a restriction kernel with connected Cartier dual, which must not be misread as a connected kernel. Question7.7 explicitly separates geometric-point injectivity from closed embedding. A3 supplies a negative answer to the latter only. Kweon–Venkatesh arXiv2601.16505, Computing Picard schemes, gives algorithms for Pic-tau in Theorems6.10/6.16; this suggests computations for a fixed pair, but does not supply a universal theorem.

A new exact fixed-pair result is proved in work/root/A2_determinantal.tex and independently audited by BCE. For nontrivial p-torsion M, dlog(M) is nonzero. If M restricts trivially to a smooth ample Y, the conormal sequence and H0(O_Y(-Y))=0 force dlog(M) to vanish as a section of Omega_X along Y. Thus fixed M has only finitely many smooth bad hyperplanes. They are precisely the maximal-minor locus of the linear matrix H1(M(-L)) tensor O(-1) to H1(M) tensor O. At a bad smooth point its rank is a-1, giving the necessary bound h1(M)-h1(M(-L)) >= h0(L)-2. This supplies a computable finite gate, but no argument yet proves that every resulting point belongs to the discriminant.

A related unpromoted formulation uses Cartier-fixed closed one-forms vanishing along Y; the Cartier logarithmic sequence should identify these exactly with the p-torsion kernel. The forward direction is already proved by the dlog argument. The exact sheaf-theoretic converse and finite stable-space procedure have not been cited and written in full, so they are not used as completed results.

Opened Hoshi, A Note on the Existence of Tango Curves, RIMS1917 (2020), all four pages. For odd p, q=p^N, the construction starts with ordinary E and q-torsion e, and a tame cover C of degree qn+1 ramified at o,e. Its logarithmic differential has divisor qn(o_C+e_C). This gives a regular logarithmic form with positive zeros on a curve, but in the higher-dimensional Tango–Raynaud construction its visible pullback zero components remain vertical fibres and a negative inseparable multisection. No smooth ample zero component has been constructed.

An A1 candidate considered is a smooth divisor of bidegree (p,F) in W^3 times P1, where H1(W,F^(-m)) is nonzero, producing possible H2 formal obstruction layers on the fourfold. Bidegree1 is only the blowup of a pencil and gives no Picard cokernel. The purely inseparable pencil equation u^p f0+v^p f1 requires the pencil to have no critical point away from its axis for smoothness; an ample pencil generally fails this. A separable additive binary equation might change the geometry, but no verified example or cokernel class has been obtained. Relative Veronese and cone constructions remain excluded for the previously recorded ampleness/smoothness reasons.

The simultaneous-root-cover argument also suggests that an ample-divisor counterexample could be converted to a very-ample one: first root a full basis of a sufficiently large prime-to-p power to make the pullback globally generated; then apply the existing globally generated-to-very-ample root construction. Smoothness would require transverse branch divisors with respect to the designated smooth divisor. Prime-to-p norm preserves a nontrivial p-torsion class. This is a construction route awaiting a starting ample counterexample, not an asserted counterexample.

## Further main-question attempts after the second formal review

We tested a height-one inseparable cover of an ordinary abelian surface or a product of ordinary elliptic curves, with local equation z^p=f for a section of L^p. Writing df=a eta1+b eta2 makes the pullback of eta1 vanish over b=0 away from a=0. This alone is not a counterexample: a and b necessarily have common zeros when their line bundle is ample, so the cover is singular there; after resolving, one must verify both smoothness and ampleness of the reduced zero component. In the simplest characteristic-two nondegenerate critical-point model z^2=xy, the reduced zero divisor has positive intersection with the exceptional (-2)-curve, but the global intersection calculation for an irreducible derivative divisor gives negative self-intersection. Thus the earlier informal claim that every exceptional curve automatically has zero intersection was too strong; the actual obstruction in this tested model is the global intersection calculation. No general exclusion is inferred.

Purely inseparable binary pencils on products do not automatically give a Picard cokernel. For example x0 v^p-x1 u^p=0 in P^3 times P^1 is smooth and very ample of type (1,p), but the resulting projective bundle still has its two Picard generators restricted from the ambient product. The incidence coordinate already supplies the candidate pth root, so this is not a counterexample. Relative conic/Veronese constructions have the previously recorded normal-bundle obstruction and remain excluded.

A new checked necessary condition is being written separately: a closed regular one-form vanishing along a smooth ample divisor has vanishing order divisible by p, since otherwise its leading term is a section of the negative conormal twist. For a Cartier-fixed logarithmic form this leading term is Cartier-exact on the divisor, giving an explicit nonzero Frobenius kernel in negative H1 on that divisor. DGJ independently checked the first argument and is writing the twisted leading-term proof. We do not infer universal injectivity from it. Search phrases included closed differential/ample divisor/characteristic p, logarithmic differential/vanishing/ample, and Cartier/zero divisor/Picard; none of the returned primary sources supplied a resolution of the remaining lifting problem.
