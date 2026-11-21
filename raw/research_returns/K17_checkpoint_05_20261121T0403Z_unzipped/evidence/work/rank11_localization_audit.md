# Independent audit: localized codimension-two Steinberg homology

Reviewer: /root/tripod_integral, GPT-6 Astra Pro; effort not exposed. Date: 21 November 2026 UTC.

**PASS.** I read the entirety of §8, pp.56–59, of Brück–Miller–Patzt–Sroka–Wilson, *On the codimension-two cohomology of SL_n(Z)*, arXiv:2204.11967v3, local work/codimension_two_sl_n.pdf and .txt. The proof yields the following integral localization, although Theorem B itself is stated rationally:

    For n>=3 and R=Z[1/(n+1)!],
    H_2(SL_n(Z); St_n(Q) tensor R)=0,
    H_2(GL_n(Z); St_n(Q) tensor R)=0.

Here St_n(Q) means the integral Steinberg module, the reduced integral homology of the rational Tits building. Its Q argument specifies the field of the building, not coefficients already tensored with Q.

## 1. Exactness survives the chosen localization

Proposition 8.5, p.57, gives an exact sequence over Z

    C_(n+1)(BAA_n,BAA'_n) -> C_n(BAA_n,BAA'_n)
        -> C_(n-1)(BAA_n,BAA'_n) -> St_n(Q) -> 0.

Its proof uses the integral connectivity and homology identifications in Lemmas 8.3–8.4. Localizing Z is flat. Thus tensoring this exact sequence with R preserves exactness. It remains to check projectivity of the three chain modules over R[SL_n(Z)] and vanishing of the degree-two coinvariants.

## 2. The precise prime bound for finite stabilizers

Let q divide the order of a finite subgroup of GL_n(Z). Cauchy's theorem supplies an element g of order q. Over characteristic zero, g is diagonalizable and at least one eigenvalue is a primitive q-th root of unity. Its rational characteristic polynomial is therefore divisible by Phi_q, of degree q−1. Hence q−1<=n, or q<=n+1.

Equivalently, if g is any finite-order element of SL_n(Z), every prime dividing its order is at most n+1. In R all these primes, and consequently the whole element order, are units. Lemma 8.7, p.58, now applies directly.

For clarity, the source proof first embeds each spanning-simplex stabilizer in a finite signed-permutation group. Its Lemma 8.6 expresses the corresponding orbit chain module as induction of a rank-one orientation representation of that stabilizer. Since the stabilizer order is invertible, the signed averaging idempotent makes this rank-one representation projective. Induction preserves projectivity, and the entire chain module is a direct sum of these projective modules. This argument is valid over R, with no field assumption.

## 3. The orientation argument uses only inversion of 2

Lemma 8.9 is stated with Q coefficients, but its entire proof only produces an orientation-reversing element of SL_n(Z) in each top-simplex stabilizer. In coinvariants this gives sigma=−sigma, hence 2 sigma=0. Since 2 is invertible in R, the same proof gives

    C_(n+1)(BAA_n,BAA'_n; R)_(SL_n(Z))=0.

The explicit stabilizers are valid integrally:

- For a double-double simplex, the source exchanges two disjoint pairs of basis vectors. The determinant is +1. On the simplex vertices there is an additional exchange of the two sums, so the total vertex permutation is odd.
- For a double-triple simplex with v0=v2+v3 and v1=v2+v4, the source uses v2 -> −v2, v3 -> v2+v3, v4 -> −v4, fixing the remaining basis vectors. Its determinant is +1. On unoriented primitive lines it exchanges v0 and v3 and fixes the remaining vertices, so again reverses the simplex orientation.

The double-double case only occurs for n>=4; the double-triple case covers n=3 as in the source. There is no use of division by another scalar in this step.

## 4. Homology and passage to GL_n

The three projective modules give the beginning Q_2 -> Q_1 -> Q_0 -> St_n(Q) tensor R of a projective resolution. It can be extended to the left by choosing free modules that surject onto successive kernels. No exactness at Q_2 has been assumed in advance.

Applying the coinvariant functor computes group homology. Since (Q_2)_(SL_n(Z)) is already zero, its degree-two homology is zero regardless of the earlier differential. This proves the SL_n statement directly in homology; no Borel–Serre duality or rational-cohomology identification is required.

For

    1 -> SL_n(Z) -> GL_n(Z) -> C_2 -> 1

and the natural GL_n-action on St_n(Q) tensor R, the homological Hochschild–Serre spectral sequence has

    E^2_(a,b)=H_a(C_2; H_b(SL_n(Z); St_n(Q) tensor R)).

Because 2 is a unit in R, averaging makes the C_2-coinvariant functor exact and all terms with a>0 vanish. Thus the degree-two abutment is the C_2-coinvariant quotient of the already zero SL_n homology. This proves the GL_n statement. No assumption about the quotient's action on that zero group is needed.

At n=11, this gives the exact term

    H_2(GL_11(Z); St_11(Q) tensor Z[1/12!])=0.

This audit checks that term and its coefficient localization. The separate use of the term in the DEKM Remark 6.6 K_12 reduction is owned by the parent and is not silently included in this source audit.

## Exact source locators

Primary source: https://arxiv.org/pdf/2204.11967v3.

- Definition 8.2 and Lemmas 8.3–8.4, pp.56–57: relative complex and integral homology.
- Proposition 8.5, p.57: integral partial resolution.
- Lemmas 8.6–8.7, p.58: projectivity over general coefficient rings with finite orders inverted.
- Lemma 8.9, pp.58–59: both explicit orientation-reversing stabilizers.
- Theorem B proof, p.59: the homological use of the partial projective resolution.

The source locators were read from the local primary PDF/text supplied in this workspace. The prime-bound and localization refinements above were independently reconstructed; they are not quoted as a separately named theorem in the source.
