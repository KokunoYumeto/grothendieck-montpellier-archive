# Independent review of root contribution SN-10 through SN-14

Reviewer: GPT-6 Astra Pro; effort setting not exposed; SIGN_NEXT child `/root/critical_lefschetz`.
Date: 21 November 2026. Review began at 03:14:34 UTC; conclusions recorded at 03:18:16 UTC and subsequently supplemented with the three-dimensional model below.
Source reviewed in full: `SIGN_NEXT/work/root/root_contribution.tex`, from the start of SN-10 through the closing motivic/arithmetic paragraphs. The root source was not edited.

## Verdict

- SN-10: passed. The new restriction/Gysin formulas and weighted critical right inverse were independently derived from Lefschetz strings. Classical algebraicity is correctly cited.
- SN-11: the cited implication chain and its scope passed. This was a check of applications and exact cited statements, not an independent proof of the CM Hodge theorem or Milne's theorem.
- SN-12: passed by independent reconstruction of every new step. The explicit CM fourfold counterexample is sound under the supplied CM Hodge theorem. The predecessor U-02 quotation is exact.
- SN-13: passed by independent re-proof. Both the left-ideal and right-ideal arguments have the correct order of multiplication.
- SN-14: **the revised three-dimensional rigid-tensor proof passed a full independent recheck at 03:26:41 UTC.** The initial two-dimensional proof had required an explicit ambient lambda-category; root replaced it by the coherent `Rep(G_a x G_m)` construction below. The old review is retained as revision history, not as an outstanding fault.

## SN-10 independent derivation

A Lefschetz string starting in primitive degree p has vectors L^r v for 0 <= r <= g-p. Its ending degree is 2g-p >= g, and its starting degree is p <= g. Therefore unit lowering Lambda satisfies Lambda L = 1 in degrees k<g, while L Lambda=1 in degrees k>g. Since j_*j^*=L, the claimed left inverse in degrees k<=g-1 and right inverse in source degrees k+2>=g+1 follow exactly, including the endpoints.

For T of dimension d, any string meeting degree d+2 has primitive degree p<=d-2. The string coordinate there is r=(d+2-p)/2>=2. Hence L^2 Lambda^2=1 on H^(d+2). This independently verifies the algebraic right inverse j^* Lambda^2 to L j_* in the even critical diagram.

The identity Lambda_Y=j^*Lambda_X^2j_* is correctly cited from cote16 scan040 / Kleiman2.12. Kleiman1968 Theorem2A11(2), p377, explicitly states hard Lefschetz and B(X) for abelian X; this is the exact historical-C input. Milne1999a Theorem5.9 is indeed the stronger Lefschetz-class statement. The author's online erratum corrects its proof, rather than withdrawing the theorem.

Minor wording precision: Betti cohomology is directly available over C; for arbitrary algebraically closed characteristic-zero bases one should say either ell-adic cohomology or Betti cohomology after spreading the finite data to a field embeddable in C. This is not a fault in the algebraic correspondence conclusion.

## SN-11 source and scope check

I read the exact statements of the supplied 032 Theorem1.1 and Corollary8.4 in the locally extracted source, and reopened Milne2002 Theorem3.3(a),(b), author PDF p8. The implication stated by root is exactly the published theorem: CM Hodge over C implies homological=numerical and Hodge-standard positivity for abelian varieties over every algebraically closed field, for ell-adic cohomology with ell invertible. The supplied Corollary8.4 explicitly includes rational ample polarizations and explains rescaling. Root's primitive exponent g-2r+1 and pairing exponent g-2r are correct.

I read Kleiman1968 Theorem3.11, Corollaries3.12 and3.14 in full. They respectively supply the positive adjoint trace, semisimplicity including adjoint-stable subalgebras, and algebraic splitting of injections/surjections. Products required by the hypotheses are again abelian, so there is no missing positivity hypothesis in this application.

SG-04's stated hexagonal case is followed by an explicit Remark extending its complex proof to every CM elliptic curve, and its finite-field proof to every elliptic curve over a finite field. Thus root's elliptic-power extension is warranted. I did not reprove SG-04.

The theorem-number difference is a **version crosswalk, not an error in the human deposit**. Root subsequently located the 16-page March26/August14 2001 author version `2002aS.pdf`; I independently opened it and verified Theorem4.6(a),(b) on printed pp13--14. This exactly matches the deposit's section1.1.2. The later September19 2001 version `2002aP.pdf` has the corresponding theorem at3.3, printed pp8--9. Root has revised the paper to explain the versions and removed unverified journal-page precision. My initial suggestion that the deposit had a theorem-number error is withdrawn.

## SN-12 independent reconstruction

### Polynomial and field

For f=T^4-5T^2+T+1 the values at -3,-2,-1,0,1,2,3 are respectively 34,-5,-4,1,-2,-1,40. The four disjoint intervals listed in the proof therefore contain all four roots, which are real and distinct.

Modulo3, f=T^4+T^2+T+1 has values 1,1,2 at 0,1,2. Reduction modulo the three irreducible monic quadratics gives T+1,1,2T+1, respectively. Thus f is irreducible modulo3. Modulo2, (T+1)(T^3+T^2+1) is the exact factorization, and the cubic has no root. Both reductions are squarefree. Consequently the transitive Galois group contains a 4-cycle and a 3-cycle. Its order is divisible by12; an index-two subgroup of S4 is A4 and has no 4-cycle. Hence the group is S4.

The splitting field N is totally real since it is generated by the four real roots. It is therefore disjoint from Q(i). The Galois group of NQ(i) is S4 x C2. The subgroup fixing E=FQ(i) is S3 x {1}.

### Overgroups and primitive type

I independently classified all overgroups of S3 x {1}. Their projection to S4 is S3 or S4. The first option gives S3 x {1} or S3 x C2. In the second option, the kernel in C2 is full, giving the full product, or trivial, giving a graph of a character S4 -> C2. The graph contains S3 x {1} only when the character is trivial, since sign is nontrivial on S3. Thus the only intermediate fields are E,F,Q(i),Q. In particular the only proper CM subfield is Q(i).

A CM type with two embeddings over each embedding of Q(i) cannot be induced from the quadratic subfield (which would choose all four extensions of a single embedding). It is primitive. MilneCM Propositions3.12--3.13, checked in the local primary text, give a simple fourfold with full endomorphism field E, exactly as used.

### Weil classes and divisors

H^1 is free of rank one over E and rank four over K=Q(i). Each K eigenspace V_+,V_- has complex dimension four; balanced signature gives two (1,0) and two (0,1) vectors in each. The two determinant lines therefore have Hodge type (2,2). They descend together to the two-dimensional rational Weil subspace.

Rosati restricts to complex conjugation on E, so the NS/Rosati identification gives NS_Q=F, dimension four. In an embedding eigenbasis, a polarized alternating form pairs only conjugate E-characters; multiplying by F spans all four paired directions. The corresponding cohomological divisor classes therefore have K-bidegree (1,1). Products of two divisors have K-bidegree (2,2), whereas the determinant lines have (4,0) and (0,4). These are disjoint summands of the exterior algebra. No nonzero Weil class is a divisor polynomial. The supplied CM Hodge theorem makes all rational Weil classes algebraic. This proves the claimed counterexample.

The source U-02 line was checked directly at HODGE_SIGN.tex line2556. It really does say every algebraic class on arbitrary CM abelian varieties is Lefschetz; it must not be conflated with positivity.

## SN-13 independent re-proof

Use B(a,b)=tau(a^dagger b). Symmetry follows by applying dagger inside the trace; positivity is assumed. L_(u^dagger) is adjoint to L_u. If a belongs to eR, then a=e a and its image on V lies in eV. Thus ua=0 and injectivity of u on eV force a=0 by faithfulness. The rational linear map L_u on eR is injective, and remains injective after extension to R. Its Gram operator L_(u^dagger u) is positive definite and invertible on eR.

The element z=u^dagger u belongs to eRe. Its action on eR has an annihilating polynomial with nonzero constant term, so a rational polynomial in z (whose constant is interpreted using identity e) is its inverse. The representation eRe -> End_Q(eR) is faithful: applying an operator to e detects the element. Hence the inverse is an actual two-sided inverse in eRe. Multiplying by u^dagger proves vu=e.

For surjectivity, a in Rf satisfies a=af. If au=0, it vanishes on fV=im(u), hence on all V; faithfulness gives a=0. The adjoint of right multiplication by u is right multiplication by u^dagger, using cyclicity. Its Gram operator on Rf is right multiplication by uu^dagger, in the order stated by root. The same argument in fRf gives the asserted right inverse. No sign, corner-identity, or order error was found.

## SN-14 initial-proof checks and resolved category clarification

For the printed 2x2 model, direct multiplication gives J^(-1)N^tJ=N, N^2=0, and F^tJF=c^2J. The radical is QN. Every coefficient trace is 2a0 c^s and tau(N^dagger N)=0. This is a valid counterexample to the proposed inference from those algebra and trace data.

The nonsplit sheaf on Spec F_q is also valid: the continuous additive projection Z-hat -> Z_ell followed by z -> I+zN is a continuous representation, because N^2=0. Its Frobenius is nontrivially unipotent but has only eigenvalue1 in every finite extension. It is punctually pure of weight0 and is not arithmetically semisimple. This does not contradict geometric semisimplicity statements for pure sheaves.

The exterior/tensor/dual filtration argument is correct in the tensor category of Frobenius modules, and induced tensor coefficient algebras preserve the corresponding filtrations. But Q[epsilon]/epsilon^2 itself has no characteristic-zero Hopf structure with epsilon primitive: the proposed coproduct sends epsilon^2 to 2 epsilon tensor epsilon, not zero. Therefore K0 of all modules over that algebra must not be silently treated as the lambda-ring. Add one sentence identifying the Frobenius-module lambda-ring, or use the following stronger model.

### Coherent rigid-tensor replacement, now adopted

Set

N = [[0,1,0],[0,0,1],[0,0,0]],
J = [[0,0,1],[0,-1,0],[1,0,0]],
U(t)=I+tN+t^2 N^2/2,
F=c U(1), c=q^r>0.

Then N^3=0, N^2 nonzero, N^t J+JN=0, and J is nondegenerate symmetric. Consequently U(t)^t J U(t)=J and F^dagger F=c^2 I. The algebra R=Q[N] is Q[epsilon]/epsilon^3 with nonzero radical, stable under dagger because N^dagger=-N. For every a=a0 I+a1 N+a2 N^2 and every integer s>=0,

Tr(a F^s)=3a0 c^s,

yet tau(N^dagger N)=-Tr(N^2)=0 and F is not semisimple. All eigenvalues of F equal c, so they have pure weight2r.

The representation of G_a x G_m given by (t,z) -> z U(t) is a genuine rational algebraic representation. Its endomorphism algebra is the centralizer of a single 3x3 Jordan block, namely R. The filtration ker N contained in ker N^2 contained in V has three one-dimensional quotients with the same G_m character. Thus in the actual rigid tensor representation category,

[V]=3[Q(1)], lambda_t([V])=(1+[Q(1)]t)^3.

Evaluating the G_m element at c gives the desired Frobenius notation. The form J is G_a-invariant and has the appropriate G_m similitude character. This simultaneously provides purity, symmetric self-duality, all tensor/exterior/dual operations, a nonsemisimple endomorphism algebra, and nonsemisimple Frobenius. It is still a formal linear-algebra/tensor countermodel, not a geometric counterexample.

### Exact revised text recheck, 03:26:41 UTC

I reread the complete new SN-14 proof in `root_contribution.tex` (whole-file SHA256 `b927656f39ba6f59e67c9f4bb9d83428ffe3a5444cd0104a761fe2bf48a12ae9`). It implements the three-dimensional construction exactly. The action is algebraic because exp(tN) is a finite polynomial; its centralizer is Q[N] because N is one full Jordan block. The displayed J satisfies N^t J + JN=0. This gives exp(tN)^dagger=exp(-tN), F^dagger F=c^2 I, and dagger-stability of the nonsemisimple endomorphism algebra.

I independently expand F^s=c^s(I+sN+s^2N^2/2). Multiplication by a0 I+a1 N+a2 N^2 has constant coefficient a0 and all other terms have zero trace, giving exactly 3a0 c^s. On the invariant flag, every induced coefficient operator acts on the associated graded by its constant term. Tensor, exterior-power and dual filtrations therefore preserve the claimed trace equalities. The proof correctly limits the insertions to induced coefficient operators; no assertion about arbitrary new endomorphisms of tensor powers is required.

The lambda identity is now in the actual rigid tensor category, so there is no Hopf-structure gap. The one-dimensional notation Q_c is explicitly explained as the torus character evaluated at c. The sheaf representation z -> I+z_l N+z_l^2 N^2/2 is continuous for every invertible ell, including ell=2: division by2 is a fixed scalar in Q_ell, and the polynomial is continuous. Its group law follows from N^3=0. Frobenius (or its inverse) is nontrivially unipotent, all extension eigenvalues remain1, and the determinant is (1-T)^3. This is an exact arithmetic Frobenius counterexample and is correctly distinguished from geometric standard-conjecture counterexamples.

The revised Betti-base precision and SGA6 V Lemma2.2.1 locator were also read and accepted. No outstanding mathematical or locator fault remains from this review.

### Optional Lefschetz tensor observation and scope

No extra tensor observation is necessary for SN-14's stated conclusion. If desired, tensor the three-dimensional object with a chosen formal Lefschetz module and let L and its lowering act on the latter factor. The radical survives in the coefficient endomorphism algebra even though the formal Lefschetz operators are present. Such a sentence must stay explicitly formal; it is not a construction of a smooth projective variety violating positivity.

## Additional locators checked

- Milne1999a author erratum: https://www.jmilne.org/math/articles/1999a.html, correction to proof of5.9. It explicitly states that Lambda is not inverse to L on the whole cohomology; root correctly uses only the needed degrees.
- Milne2002: https://www.jmilne.org/math/articles/2002aP.pdf, later author version, Theorem3.3(a),(b), printed pp8--9, and introduction p2 for the Milne1999a5.9 assertion. The earlier author version https://www.jmilne.org/math/articles/2002aS.pdf instead has Theorem4.6(a),(b), printed pp13--14; the exact latter statement was independently reopened in this review.
- SGA6, Expose V, Definition2.1 and Example2.2(b) are valid broad locators. Lemma2.2.1 is the sharper exact locator for the exterior-power filtration.
- SGA4, Expose XVI, Corollary2.2 is the correct smooth proper specialization locator. Its printed statement needs locally constant coefficients (known erratum), which is satisfied by the constant coefficients in root's application.
- EGA IV3,8.8.2 was carried as background without fault found; I did not reopen its full source in this check.
- SGA5 III3 and5.1--5.3 were carried as background; no claim to have checked their full statements here.

## Check-depth limits

This review independently re-proved the new elementary/geometric arguments. It did not re-prove the stipulated CM Hodge theorem, SG-04, the settled sign-only theorem, Milne's global theorem, or the classical Kleiman theorems. Those were source/application checks or carried background, as individually recorded in the review check-events file.
