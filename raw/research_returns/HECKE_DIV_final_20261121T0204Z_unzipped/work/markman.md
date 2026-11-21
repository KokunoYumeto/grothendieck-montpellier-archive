# Markman audit and quantitative findings

Run: HECKE_DIV_20261121. Author/checker: /root/markman, GPT-6 Astra Pro (inherited effort setting not exposed). Date: 2026-11-21. Status: proofs below read in full by the author; independent check by parent still needed. No claim of formal verification.

## Sources and exact locators

Primary local source: `source/LIT_Markman_Hodge_abelian_fourfolds_2502.03415/250531.tex`.

Public primary source: Markman, E. (2025). *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds* (arXiv:2502.03415v2). https://arxiv.org/abs/2502.03415v2 ; HTML https://arxiv.org/html/2502.03415v2 . Exact statement numbers confirmed against public HTML.

- Theorem 1.4.1, local label `main-theorem-introduction`, source lines 503–523: rank 8d reflexive sheaf on a sixfold; K translates of kappa_3 with h^3 span Qh^3 + HW.
- Theorem 1.5.1, local label `thm-algebraicity`, lines 573–578: Weil classes on all sixfolds of Weil type with discriminant −1 are algebraic.
- Corollary 1.6.1, lines 591–608: Hodge conjecture for every abelian fourfold. Reduction from sixfolds by Schoen, Proposition 10; simple fourfold Hodge ring by Moonen–Zarhin, Theorem 2.11.
- Section 7.4.2, lines 3519–3610: semiregularity theorem for twisted sheaves on abelian varieties.
- Example 8.2.3, local label `example-secant-sheaf-on-jacobian-of-genus-4-curve`, lines 3778–3861: genus four secant ideal sheaf, its Chern character, cyclic equivariance and partial-normalization alternative.
- Lemma 8.2.5, local label `lemma-ch-O-W-2`, lines 3917–3958: Chern character of W_2.
- Lemma 9.3.11, local label `lemma-semiregularity-of-twisted-sheaf-B`, lines 6807–6839: semiregularity of the sixfold twisted sheaf.
- Proof of Theorem 1.5.1, end of Section 9.3, lines 6841–6849: globalization via countable union of closed algebraic subsets and a nonempty analytic open.

The passage at lines 580–582 proposing global properness of a semistable-sheaf moduli space is a COMMENT, not part of the active proof. The active text explicitly says the semiregularity proof is special to genus three (lines 583–584). A claimed numerical cycle-degree bound cannot be attributed to this passage.

Public bibliography verification also located Markman (2023), *The monodromy of generalized Kummer varieties and algebraic cycles on their intermediate Jacobians*, JEMS 25(1), 231–321, DOI 10.4171/JEMS/1199, Theorems 1.5 and 13.4. This older source handles discriminant-one fourfolds. It was not re-proved in this run.

## M1. Scope and global complexity consequence

**Checked source audit; new consequence conditional only on the bounded-Chow lemma proved elsewhere in this run.** For any connected algebraic polarized family of abelian fourfolds and any globally defined flat rational Hodge class t, Markman's Corollary 1.6.1 and the bounded-Chow/Baire argument imply existence of N,D independent of the point, with Nt represented as a difference of effective codimension-two cycles each of degree at most D. This applies to every Hecke orbit in the family, including a split E^4 point.

**Proof.** Every fibre class is algebraic by the cited corollary. The countably many closed loci for bounded positive integer denominator and bounded degree cover the base. A nonempty analytic open of a connected smooth base is a Baire space, and a proper algebraic closed subset has empty analytic interior. Therefore one such closed locus contains an analytic open and hence the whole irreducible base. If the base is not smooth, use a smooth open and closure. This argument proves the existence of N,D, not a formula or their least values. It preserves a denominator already fixed on an analytic open, as in M4 below. End proof.

No unique numerical answer is determined by “E^4” alone: one must fix the relative polarization, the flat Weil class including its scalar normalization, and the integral lattice / component. Replacing t by t/q or the polarization by its m-th power changes denominator or degree. Any numerical statement must record these data.

## M2. Explicit clearing of twisted Chern-character denominators

Let A be a complex abelian variety, B an algebraic (or holomorphic coherent) sheaf of positive rank r twisted by a Cech 2-cocycle with values in mu_r, and suppose det(B) is trivial. Write kappa(B)=ch(B) for its normalized Chern character. Then the following rational cohomology classes are represented by integral Chow classes:

- r^4 kappa_2(B);
- 2 r^6 kappa_3(B);
- 12 r^8 kappa_4(B).

More generally p! r^(2p) kappa_p(B) is integral algebraic. No effective-degree bound is asserted.

**Proof.** Comparison identifies H^*(A,mu_r) with singular cohomology with Z/r coefficients. The cohomology of the real torus A is the exterior algebra on H^1, and [r]^* is multiplication by r^2 on H^2(A,mu_r). Thus [r]^* kills the twisting class. After refining the cover, its pulled-back cocycle is a coboundary of a mu_r-valued 1-cochain. Untwist [r]^*B with this cochain to obtain an ordinary coherent sheaf E. Since the scalars used to untwist have r-th power one, det(E)=[r]^*det(B) is trivial. If B is initially analytic, E is algebraic by GAGA. Smoothness of A gives algebraic Chern classes of E via a finite locally free resolution.

Naturality and the action of [r] on degree 2p give
ch_p(E) = [r]^* kappa_p(B) = r^(2p) kappa_p(B).
Since c_1(E)=0, the Newton identities give
ch_2(E)=−c_2(E), ch_3(E)=c_3(E)/2, and ch_4(E)=(c_2(E)^2−2c_4(E))/12.
These are equalities after cycle class. They prove the stated integers, and the general Newton identity proves p! r^(2p). End proof.

This calculation concerns cohomological algebraicity with an integral Chow representative; it does not say that an arbitrary representative is effective or has small positive and negative degrees.

For the sixfold construction with K=Q(sqrt(−3)), one safe even parameter is d=12, so r=8d=96 and the quotient q has degree (d+1)^2=169 (Markman Section 1.5, lines 561–566). M2 gives the explicit multiplier
2*96^6 = 1,565,515,579,392
for kappa_3(B). Pulling back by q does not enlarge this multiplier. Fixed further isogenies or rational K-projectors used to express a chosen normalized Weil class can enlarge it by fixed, calculable factors. This number is not claimed to be minimal and is not a bound for every arbitrarily normalized t without those factors.

At an untwisted rank-r seed, the sharper universal expression is
kappa_3(E) = ((r−1)(r−2)/(6r^2))c_1^3 − ((r−2)/(2r))c_1c_2 + c_3/2.
For r=96 its polynomial denominators divide 27,648. This seed denominator must not be asserted for arbitrary twisted deformations without further argument.

## M3. The standard genus-four cyclic seed cannot be semiregular for Q(sqrt(−3))

Let X be a genus-four Jacobian as in Markman Example 8.2.3, and let F_d=I_Z(Theta), where Z is the stated union of d+1 translates of W_2 and 2d(d+1) isolated points. Suppose Z is invariant under a free translation action by a cyclic group G of order d+1, as in that example. Then the restriction of the semiregularity map to Ext^2(F_d,F_d)^G is not injective for d>=3. In particular it fails for every integer d with Q(sqrt(−d))=Q(sqrt(−3)), since such d=3b^2>=3.

The G action on Ext is that induced from the natural equivariance of I_Z; tensoring by O(Theta) identifies the Ext groups even if O(Theta) itself has no G-linearization. Translation acts trivially on the target cohomology. This statement concerns the seed ideal sheaf and its quotient, not an arbitrary Orlov square or an arbitrary eightfold sheaf.

**Proof.** Write x=c_1(Theta), with integral x^4=24. Example 8.2.3 gives
ch(F_d) = 1+x−(d/2)x^2−(d/6)x^3+(d^2/24)x^4.
The tangent bundle of X is trivial. Hirzebruch–Riemann–Roch therefore gives
chi(F_d,F_d)= integral ch(F_d)^vee ch(F_d)=8d(d+1).
Indeed the coefficient of x^4 in the product is d^2/3+d/3, whose integral is 8d(d+1).

Let q:X→Y=X/G. The G-stable closed subscheme Z descends to a closed subscheme barZ⊂Y by finite etale descent. The ideal J=I_barZ is a simple rank-one torsion-free coherent sheaf on the smooth abelian fourfold Y, and q^*J=I_Z. Descent identifies Ext^i_Y(J,J) with Ext^i_X(I_Z,I_Z)^G. Twisting by a line bundle preserves self-Ext. Riemann–Roch and etaleness give chi(J,J)=chi(I_Z,I_Z)/(d+1)=8d.

Let e_i=dim Ext^i_Y(J,J). Rank-one torsion-free sheaves on Y are simple: an endomorphism is a rational function preserving J; it extends regularly over codimension-one points and thus globally by normality, hence is constant. Thus e_0=1. Serre duality and omega_Y=O_Y give e_4=1 and e_3=e_1. The natural scalar and trace maps split H^1(O_Y) into Ext^1(J,J), their composite being multiplication by rank(J)=1. Consequently e_1>=4, and
 e_2 = chi(J,J)+2e_1−2 >= 8d+6.

For a fourfold, the semiregularity target is
 ⊕_{q=0}^2 H^{q+2}(Y,Omega_Y^q).
Since Omega_Y^q is trivial of rank binom(4,q), its dimension is
 binom(4,0)binom(4,2)+binom(4,1)binom(4,3)+binom(4,2)binom(4,4)=6+16+6=28.
For d>=3, e_2>=30>28. Hence no linear map from Ext^2_Y(J,J) to this target can be injective. Pullback and twisting give the same noninjectivity for the equivariant part of the seed map. End proof.

The target for the trace-free problem has dimension 22 and the trace-free Ext^2 has dimension >=8d, so fixing determinant does not remove the obstruction at d=3.

For d=3, the numerical data of this seed are: four W_2 surfaces, each of Theta-degree 12, total top-dimensional degree 48; 24 isolated points; each of the six pairs of surfaces meets in six points under the general-position hypothesis. The full Ext^2 has dimension at least 102, and the G-invariant Ext^2 at least 30.

**Extension.** In Example 8.2.3 with general integer a=a_3<=1, the computed character is alpha+a beta and chi(F,F)=8d(d+a^2). If the whole subscheme is made invariant under a free cyclic group of maximal displayed order d+a^2, the same descent argument gives chi=8d and the same obstruction. This extension is conditional on existence of that equivariant general-position construction; it is not needed for d=3,a=1.

**What M3 does not prove.** It does not prove failure of bounded division. It does not exclude the partial-normalization complex F' in Example 8.2.3, whose simplicity and self-Ext dimensions require a separate calculation. It does not exclude a semiregular twisted reflexive object after applying Orlov's equivalence to an external square: the ambient dimension and semiregularity map change.

## M4. Globalization with the explicit fixed denominator

Let f:A→S be a smooth projective family over an irreducible algebraic complex base; fix a relative ample line bundle and a flat rational section t. Suppose on a nonempty analytic open U⊂S every t_s is kappa_p(B_s) for a determinant-trivial mu_r-twisted coherent sheaf B_s of fixed rank r. With N_p=r^4, 2r^6, or 12r^8 for p=2,3,4 respectively, there exists D such that for every s∈S,
 N_p t_s = [Z_s^+]−[Z_s^-], deg Z_s^±<=D.

**Proof.** M2 gives an integral Chow representative at every point of U with the same N_p. Every integral algebraic cycle is a difference of effective cycles of some finite degree, so U is covered by the closed bounded-degree loci S_(N_p,D), D∈Z_{>=0}. Baire forces one to contain an analytic open, and irreducibility forces S_(N_p,D)=S. End proof.

This sharpens the qualitative consequence by isolating an explicit denominator from the object rank. It still does not supply D, because Baire and the local analytic semiregularity theorem are ineffective. A fixed finite collection of K-correspondences and rational coefficients turns the conclusion into a bound for a chosen normalized Weil basis; the multiplier must include those coefficients.

## M5. Chern-class arithmetic check for the genus-four seed

With the preceding normalization, Newton identities give
 c_1=x,
 c_2=((d+1)/2)x^2,
 c_3=((d+1)/6)x^3,
 c_4=−((d+1)(3d−1)/24)x^4.
At d=3, the numerical intersections are integral c_2 x^2=48, integral c_3 x=16, integral c_4=−32. These equations are checks of the supplied Chern character, not a bounded-degree construction on deformed eightfolds.

The polynomial identities and the dimensions in M2/M3 were checked by SymPy; results are in `work/markman_computation.txt`. This is an algebraic computation certificate, not a formal proof certificate.

## Grothendieck locator limits

No original Grothendieck archival scan or transcription was supplied to this subtask. No cote/scan/line correction is claimed. M2 lives in the cycle-class/Chern-character and etale-isogeny framework; M3 in deformation theory of coherent sheaves; M4 in the projectivity of relative cycle parameter spaces. Exact FGA/EGA/SGA locators should be furnished by the reductions/source-audit task rather than fabricated here.

## Check events (for parent incorporation)

2026-11-21 | M1 | targeted proof check | Full reading of argument, global flat-section and irreducibility hypotheses made explicit | passes assuming bounded-Chow lemma.
2026-11-21 | Markman Theorem 1.5.1, Corollary 1.6.1 | used and rechecked in this run | Read exact statements, introduction route and full globalization paragraph; not entire 96-page proof | scope verified, carried as cited background theorem.
2026-11-21 | Markman Example 8.2.3 | used and rechecked in this run | Read full active example, checked coefficient calculations | character verified; original claim only predicts eventual failure, M3 proves failure already for d=3 for the stated cyclic ideal seed.
2026-11-21 | M2 | targeted proof check | Full proof read: coefficient comparison, mu_r cocycle trivialization, determinant preservation, Newton identities, GAGA | passes.
2026-11-21 | M3 | targeted proof check | Full proof read: descent, self-Ext simplicity, trace splitting, RR, Serre duality, target dimension | passes for stated seed; deliberately excludes Orlov-square inference.
2026-11-21 | M4 | targeted proof check | Full proof read, fixed denominator before Baire | passes assuming bounded-Chow lemma.
2026-11-21 | M5 | computation or formal certificate | SymPy polynomial verification (computation only) | passes; no formal proof certificate claimed.

## M6. Stability audit and the precise denominator-transfer limitation

**Source audit completed 2026-11-21.** The supplied Markman paper does not establish slope stability, slope semistability, or Gieseker semistability for every deformed sixfold sheaf B, nor for all its pullbacks under [r]. The only explicit Gieseker/relative-properness passage, lines 581–582, is commented out and has the additional hypothesis that E is Gieseker–Maruyama h-stable. The comment at lines 6501–6504 proposes an unproved divisibility calculation from which a generic deformation might be “very twisted” and slope stable; it too is inactive. Active stability statements in the construction concern auxiliary bundles on the genus-three curve, not the resulting sheaf on every sixfold. Simplicity/reflexivity/semiregularity must not be silently replaced by stability.

A fixed flat Chern character and a fixed polarization imply a fixed Hilbert polynomial after the pointwise [r] untwisting: Riemann–Roch expresses it using h and r^(2j) kappa_j. This observation does not supply global existence of the sheaves or boundedness of their family. Even for an elliptic curve, L^n⊕L^(−n), with deg L=1, has fixed rank and Hilbert polynomial while its instability is unbounded. Therefore fixed Hilbert polynomial alone does not justify the proposed moduli argument.

M4 remains valid without any stability assumption. It globalizes integral cycle representatives and their fixed multiplier from an analytic open; it does not globalize the original sheaf. On a finite cover on which the Weil local system is trivial, the normalized characteristic class kappa_3 is a definite flat section. This is the section to which N0=2r^6 applies directly.

For a different normalized flat Weil class t, suppose fixed rational linear algebra supplies

 t = sum_i c_i (a_i^(−1) f_i)^* kappa_3 + c_h h^3,

where each f_i is an actual K-linear endomorphism, the positive integers a_i clear the rational endomorphisms, and h is an integral relative polarization. Since rational endomorphism pullback on H^6 scales as a_i^(−6), any positive integer N divisible by N0 times the denominator of every c_i/a_i^6, and by the denominator of c_h, makes Nt an integral algebraic class on the analytic open. The same N then globalizes by M4. All these factors are constant on the fixed marked family. In particular no denominator varying with the Hecke point is introduced by this step. But the rational coefficients and endomorphism denominators must actually be calculated before a numerical value of N is advertised for t.

For T5, the sixfold-to-fourfold passage additionally uses Schoen's product/compensation correspondence (Markman Corollary 1.6.1). Its fixed rational normalization must also be cleared. The displayed 2*96^6 is therefore a rigorous multiplier for Markman's sixfold characteristic section, not by itself an explicit universal integer for an unspecified fourfold Weil class. The qualitative fourfold uniform bound follows already from Corollary 1.6.1 plus the bounded-Chow lemma, but numerical D and a normalized numerical N for T5 are not extracted by this audit.

Check event: M6, used and rechecked in this run, full search of all stability/properness mentions followed by reading the relevant contexts; active theorem scope separated from comments; no stability result found for the needed global object. M4 and the coefficient-transfer argument were read in full again after this audit; no gap found under their stated global-flat-section hypotheses.
