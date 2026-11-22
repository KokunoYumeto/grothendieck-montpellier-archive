# C.3bi: full proof and targeted primary-source audit

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode; run RESEARCH_SA06, `/root/frobenius`; inherited effort setting not separately exposed. Independent agent, not an independent model. Completed 19 November 2026, **14:32:02 UTC**.

## Verdict and exact scope

**PASS** on the complete seven-step text in `agents/real_weil/C3_higher_integral_kernel_draft.tex`, including the subsequently inserted explicit F125 incidence pair, actual fifth-power triviality, and finite spectral-sequence filtration. The proof gives an actual ordinary algebraically trivial codimension-two cycle of exact order five, nonzero on the regular puncture of a five-dimensional excellent normal strictly henselian local algebra, whose restriction to the regular principal punctured divisor is zero. It does not give a rational failure, an all-prime statement, or an all-dimensional statement.

The cubic twisted cup calculation was independently rederived in the separate review `C3_cubic_line_cup_independent_REVIEW.md`. The explicit incidence construction was contributed by this reviewer in `C3bi_cubic_incidence_geometry_RESEARCH.md`, then independently read and passed by the owner. The present K-theoretic and Chow argument is an independent full read of the owner's proof; the overlap in geometric authorship is disclosed rather than represented as an independent discovery.

## 1. Geometry and the actual family

The F125 element lambda satisfies lambda^3+lambda+1=0 and lambda^12=2-lambda. The two sections a0=z0*w0+z1*w1 and a1=z0*w2+lambda*z2*w3 have independent coefficient rows at every point of the Fermat quartic. Their base curve is the explicit cubic cover A0*s^3+B0*t^3=0 of C, with twelve simple, disjoint zeros of each coefficient. The three excluded values of lambda^12 are exactly 1,3,4. The branch proof covers every geometric point, not just the finite-field points.

The incidence differential is nonzero above the base curve because da0,da1 are independent. The Segre contraction and strict-local regularity arguments from C.3bf apply to the additional smooth cubic factor. The projection to W remains an actual morphism on the nonsplit resolution, so O(D) really extends. The three canonical coefficients g0,g1,g2 are independent, while their products with c1(D) span a rank-two space. This supplies a finite Verschiebung-kernel point with a nonzero cup product because those finite points span the full three-dimensional extension image over k.

The Picard-family construction is correctly performed on a fixed proper curve P inside J^(5). It starts from an actual normalized Poincare bundle and uses the vanishing of the mixed H1(O) obstruction under Verschiebung. The difference of two lifts is a constant morphism from P to the vector group, and normalization at zero removes it. H2(V×P,L^n)=0 for n≥2 then lifts the whole actual family. Proper formal existence, finite-presentation descent including the first-jet isomorphism, and henselian lifting modulo m^2 produce an actual family on the fixed Z×P. The equality m O_Z=I_V makes that matching sufficient. Endpoint uniqueness and Elkik show actual target triviality and actual fifth-power triviality. No abstract Picard-functor point is substituted for the product family.

## 2. The K1 boundary really vanishes

For the smooth proper curve, the localization segment has kernel k* at k(C)*, and the other term is a quotient of a direct sum of copies of k*. Both are divisible. An extension of divisible abelian groups is divisible, so K1(C) is divisible. The integral projective-bundle and regular-blow-up decompositions give K1(V)=K1(C)^18: three summands from P2, six exceptional summands, and a factor two from P1. No rational Chern character or isogeny has entered.

On a finite affine cover and all its finite intersections, the square-zero relative K-groups in each of the finitely many degrees needed for K0 descent have bounded five-power exponent by Geisser–Hesselholt. Finite Mayer–Vietoris induction preserves bounded five-power exponent, so K0(E,V) has that property. A homomorphism from a five-divisible group to such a group is zero. Therefore the map K0(E,V)→K0(E) is injective. This resolves the actual relative-to-absolute obstruction and is stronger than merely observing a nonzero tangent class.

## 3. Nonsplit K2 gluing and the surviving product

The use of the dual-number theorem is valid locally because V is smooth over k and I is invertible: the affine square-zero algebra admits a k-algebra splitting and a local frame. The relative homotopy K2 is the usual kernel in such a split chart. With 2 invertible, the van der Kallen isomorphism identifies it with I tensor Omega1_V/k.

The change-of-splitting issue is handled correctly. If a lift of u changes by an infinitesimal unit, the difference of the relative symbols is {1+i,1+j}. This is zero for a rank-one square-zero ideal when 2 is invertible; under the local isomorphism its expression contains the factor epsilon*d(epsilon)=0. Changes of frame rescale the I coefficient. Hence the isomorphism glues on the actual nonsplit E, and the normalization {1+tau*c,u}↦tau*c*dlog(u) is the stated negative of Weibel's Dennis–Stein convention. Perfectness of k makes the absolute differentials agree with relative differentials over k.

The relative descent spectral sequence has a bounded cohomological index because the underlying noetherian space V has dimension four. The line-bundle class with its chosen trivialization on V supplies a permanent H1(I) class; the absolute extended divisor supplies a permanent H1(K1) class. Their product has leading term a cup c1(D) in H2(I tensor Omega1), with the correct integral coefficient. The only possible incoming differential is d2 from H0(I). Every such section is represented by the actual global unit 1+u, so this differential vanishes. Higher incoming terms have negative cohomological index. Outgoing differentials vanish by the multiplicative module structure and permanence of the factors. Thus the nonzero term survives to the finite associated graded of relative K0, and injectivity from Section2 detects it in absolute K0(E).

For iterates of the absolute operation psi2, the line-bundle formula gives leading relative term 4^j times the original cup product. This uses only absolute Adams operations and restriction. It does not require a separate relative Adams weight theorem on the nonsplit scheme.

## 4. Exceptional image and integral Chow detection

If beta vanished on X, localization would express it as i_*gamma for gamma in Pic(V). Its restriction to V is zero because the endpoint bundle is trivial there. Self-intersection therefore gives L*gamma=0 (the conormal sign is immaterial to this equation).

The injectivity of L on Pic(V) is integral, including the Pic0 torsion. Writing gamma=gamma0+b*h gives gamma0=-b*c and b*c^2=0. Multiplication by c and degree yields b*deg(c^3)=0 in Z; here deg(c^3)=36 is a positive integer, not its reduction in k. Thus b=0 and gamma0=0. Consequently beta would already be zero in CH2(Z).

The integral cycle map sends the two-divisor product to x modulo coniveau F3, by the Cartier exact-sequence calculation. Iwasa–Kai's absolute coniveau lemma applies to the separated regular noetherian fivefold Z and gives (psi2-2^q)Fq⊂F(q+1), with F6=0. Therefore beta=0 would imply P(psi2)x=0 for P(T)=(T-8)(T-16)(T-32). Restricting to E and using the unique relative lift gives leading term P(4)*a cup c1(D). Since P(4)=-1344 is 1 modulo five, this is nonzero, a contradiction. This step preserves integral coefficients throughout.

Intersecting the actual Picard family with the actual extended divisor proves ordinary algebraic triviality. Actual target triviality and fifth-power triviality of the line bundle prove target vanishing and order dividing five of the Chow product. Nonvanishing then makes its order exactly five. The finite-type-model/strict-etale-limit framework already used for these regular punctures supports the localization, refined pullback and intersection operations; no completion-only Chow conclusion is being substituted.

## 5. Freshly opened primary sources and exact locators

- **Iwasa–Kai:** complete 17-page author file dated 9 January 2020, https://ryomei.com/papers/K0CHmodulus.pdf . Proposition3.4 and proof authorpp9–10, Lemma3.10 and full proof p11, Theorem4.2 and full proof p12 were freshly read. The precise hypotheses are regular separated noetherian schemes of finite dimension, and the integral graded Adams action is explicit. The relative-modulus affine-neighbourhood hypothesis is not invoked. The owner separately records the published22-page pagination; this review does not conflate those versions.
- **Huybrechts:** complete456-page author final draft, https://www.math.uni-bonn.de/people/huybrech/Notes.pdf . Chapter4 Proposition2.4 authorp178 was freshly opened together with Lemma2.1 and its proof p177 and the derivation preceding the proposition. The field is algebraically closed, with no characteristic-zero restriction in this statement.
- **Khan:** complete24-page author file dated1February2020, https://www.preschema.com/papers/kblow.pdf . Corollary3.6 authorp12 and Corollary4.4 authorp16, including the surrounding perfect-category argument and the classical regular-immersion specialization onp3, freshly read. These are integral spectrum decompositions for additive invariants. The direct arXivv3 opening failed; the successful author-hosted primary source is explicitly recorded.
- **van der Kallen:** https://webspace.science.uu.nl/~kalle101/K2nd1971.pdf . The original four-page scan was freshly opened, and printedpA1204 was rendered locally and visually reread, including the theorem and corollary requiring only 1/2. The previously completed full-proof audit of A1205–A1207 is reused, not falsely described as a new four-page visual read. Fresh image: `output/C3bi_vdK_A1204.png`.
- **Weibel:** https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf . ChapterIII Exercise5.14(a)–(c), authorpp46–47, was freshly read, including the square-zero kernel and the dual-number isomorphism. The earlier Definition5.11 sign audit is reused.
- **Reused exact primary audits:** Geisser–Hesselholt TheoremA printedp29; Thomason–Trobaugh Theorems8.1 and10.3 and Section3.15; Illusie Theorem2.6/formula2.7.2; Brion original-category Ext identification; actual Poincare, GAGA, Popescu, finite-presentation and henselian lifting, and Elkik puncture comparison. Their relevant scopes were rechecked against the new argument; no fresh opening of each of these is claimed here.

Kai's current author webpage was also opened while checking source status. Its warning of a Whitney-sum proof gap concerns the separate2019 paper *Chern classes with modulus*. The present argument uses neither that Whitney-sum theorem nor that paper's Proposition3.4. This is a source-identification check, not a claim that the warned theorem is false.

## 6. Computation and limitations of this receipt

The exact geometry certificate has16 successful checks, started14:26:08.725769UTC, completed14:26:08.919093UTC, runtime0.193337592seconds. This reviewer wrote and actually ran it. The earlier unused shifted-coefficient trial is explicitly recorded as incomplete; only its first affine chart reached the unit ideal, and it does not enter the proof.

This receipt does not certify a standalone build that has not yet been inspected. The proof remains owned by `/root/real_weil`; root/owner control its promotion and registration. No priority claim is made.
