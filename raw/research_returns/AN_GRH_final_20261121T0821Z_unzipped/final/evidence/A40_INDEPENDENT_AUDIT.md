# A40 independent complete-proof review

Date: 2026-11-21 UTC. Reviewer: GPT-6 Astra Pro; effort not exposed; /root/effective_galois.

**PASS.** I independently read the complete five-step proof and its final consequence. I found no mathematical gap. I checked the final matrix-normalization addition and the source-credit-only addition separately. This is a complete mathematical proof review, not a formal proof-assistant verification or an independent reconstruction of every cited theorem.

## Exact source and revisions reviewed

- Source: `work/gt_certificates/positive_rank_theta/A40_INVERSE_DIHEDRAL.tex`.
- Final SHA256: `883b929b9b8b633340ea0c75452ba0d7d885c092bc2f2b17d5a1374545fa641d`.
- Initial complete-read SHA256: `397ab7b7ba43114d2eb278d19c10cf91849d8f1373e53e213c9acfdf2b9c485d`.
- Intermediate SHA256: `bc403f8bfcc174ec4214d802a79c2c0cbf83fa2873a1f0c4af5970f468d6fbe6`. Its changes were the aligned opening display, the exact miracle-flatness citation, and the squared-deck normalization recovering the specified real-multiplication endomorphism. All were checked.
- The final change adds the Kumar--Mukamel source-credit paragraph and bibliography. It changes no mathematical inference. The published primary paper also confirms the stated characteristic-zero genus-six correspondence example.
- No source or canonical final file was edited by this reviewer.

## Complete mathematical review

### 1. Residual correspondence, signs, and intersection numbers

The relation T^2+T-1=0 makes T an automorphism with inverse T+1. Its characteristic polynomial on a four-dimensional rational Tate module is the square of that irreducible rational quadratic: rationality forces the two root multiplicities to coincide. Consequently the traces of T and T^dagger T are -2 and 6. The Rosati intersection formula on a principally polarized surface gives Theta dot T(Theta)=3, whereas either self-intersection is two. Hence T(Theta) is not a translate of Theta.

For F_t(P,Q)=T(z_P-z_t)-z_Q, every fibre is an intersection of those two distinct irreducible curves, and is finite. The generic intersection length is three. The canonical Gauss map is nonconstant, so the two differential directions are generically independent; the finite map is generically separable. Both surfaces are smooth, and the local dimension equality for a finite map meets the exact hypotheses of miracle flatness. Thus finite-flat intersection pullback is applicable, including its multiplicities.

The vertical divisor V_t is contained in F_t^*Theta with multiplicity exactly one. Its generic normal derivative is the stated conormal pairing and is not identically zero because the Gauss map is nonconstant. Any other vertical component would give a nonzero translation stabilizing a principal theta divisor, which is impossible; a horizontal component would make T(Theta) a translate of Theta. Subtracting V_t therefore gives an effective Cartier divisor with both projection degrees two. For P different from t, the divisor Q+R has class K_E+T([P-t]); its unique effective representative and the Abel map away from the canonical class determine both the scheme multiplicities and the positive sign of the induced correspondence.

The intersection calculation is consistent: (F_t^*Theta)^2=6, F_t^*Theta dot V_t=2, V_t^2=0, so D_t^2=2. Its bidegree gives D_t dot K_(E times E)=8, and adjunction gives arithmetic genus six.

### 2. Integrality and reducedness

Because no component is vertical or horizontal, a reducible or nonreduced effective divisor of bidegree (2,2) must have two (1,1) components, counted with multiplicity. Each is a graph of an automorphism: its normalization has degree one over each smooth factor. There is no embedded-component issue, since the divisor is Cartier on a smooth surface.

If u and v are the corresponding polarized Jacobian automorphisms, T=u+v and w=u^{-1}v give T^dagger T=2+w+w^{-1}. Since T is Rosati symmetric, w+w^{-1}=-1-T. The latter element satisfies the same quadratic relation. Multiplication by w^2 gives Phi_5(w)=0, so w has order five; w=1 would make multiplication by five zero. Faithfulness of the curve action on the Jacobian then gives an order-five automorphism of E.

An ordinary genus-two curve in characteristic two has precisely three geometric branch points in its separable hyperelliptic map. Every automorphism acts on the unique hyperelliptic quotient and permutes those three points. The kernel is the order-two hyperelliptic group, and the group of base automorphisms injects into S_3. Thus its order divides twelve. This excludes the order-five automorphism and proves that every D_t is integral and reduced.

### 3. Generic smoothness, including the removed component

The canonical Gauss map gamma is the separable hyperelliptic double map. On every normalized component of the reduced fibre product Z defined by gamma(Q)=Tbar gamma(P), both projections are nonconstant and generically separable: after deleting the branch values this is a fibre product of finite etale double covers. Since the differential of multiplication by two is zero, dh=dT dz_P for h=Tz_P-2z_Q is generically nonzero.

If an image component h(Z_0) lay in T(Theta), the inverse of the closed embedding Tz would define a map s with Tz_s=h. Differentiation forces gamma(s)=gamma(P). On the integral source this gives s=P or s=iota(P). The first alternative forces the nonconstant Q-image into finite J[2]. The second makes Tz_P-z_Q a constant point of J[2]. This remains valid for the possibly nonreduced group scheme, because the source is reduced and connected. Surjectivity of the two projections would then make T(Theta) a translate of Theta. Both alternatives are impossible. Thus every h(Z_0) meets T(Theta) in finitely many points.

Away from P=t, singularity of the pullback of the smooth theta divisor forces gamma(R)=gamma(Q)=Tbar gamma(P). The alternative R=iota(Q) would force P=t; the other alternative lies in the finite set just proved. Thus only finitely many parameters can give an off-vertical singularity.

Along V_t, the local equation aG correctly defines the residual equation G. The restriction G(0,Q), up to a unit, is the conormal pairing. Its zero is simple at a non-Weierstrass Q because gamma is etale there, so the derivative of G in the Q direction is nonzero. Excluding the at most six parameters whose transformed Gauss direction is a branch value therefore handles all residual points on V_t. This proves smoothness on a nonempty open of parameters for each fixed E; it does not assume a generic curve in a moduli space.

### 4. Integral dihedral action and the quotient genus

The degree-two projections from genus six to genus two are separable. A purely inseparable degree-two map of smooth curves over a perfect field has the same genus at source and target, so cannot occur here. Their involutions therefore exist, and the pullback/norm identities and correspondence sign yield the stated matrix NU. Its determinant 3+T has product five with 2-T, so NU is an isogeny. The image of U has dimension four and the complementary kernel of N has dimension two. In characteristic two the differential of NU has invertible off-diagonal blocks dT, which also verifies that the connected kernel used here is an abelian subvariety.

I manually multiplied the two displayed involution matrices and checked their product, determinant, trace, and cyclotomic relation in the exact ring Z[T]/(T^2+T-1). On the four-dimensional image the product sigma satisfies Phi_5(sigma)=0; on the complementary dimension-two subvariety it is the identity because each involution acts as -1. The isogeny decomposition then gives sigma^5=1 on all of J_D, while its action is nontrivial. Faithfulness on the curve proves actual order five, and conjugation by either reflection gives inversion. The resulting group has order ten.

The final added normalization also checks exactly: sigma^2 has matrix [[0,-1],[1,T]], so sigma^2 U_1=U_2 and N_1 sigma^2 U_1=T. Thus changing to the squared deck generator recovers the original specified integral RM embedding.

The invariant rational Tate module consists exactly of the complementary dimension-two Jacobian factor; Phi_5(1)=5 excludes invariant vectors from the other factor. Norm and pullback for the quotient identify its Jacobian with this invariant part up to isogeny, so the quotient C has genus two. Riemann--Hurwitz then gives zero different for the degree-five cover, hence etaleness. The reflections act as -1 on J_C; their quotient has genus zero and they are the hyperelliptic involution of C. These arguments use rational Tate modules with a prime different from two and five where appropriate; no claim about integral invariants in wild characteristic is needed.

### 5. Descent, arbitrary prescribed image, and exact scope

All choices in the construction are algebraic and finite in number. A finite constant extension therefore defines the theta characteristic, a parameter from the nonempty smoothness open, the curve and both projection maps. The separable double maps have unique nontrivial deck involutions, which descend to that field as well; so do sigma and the quotient.

For an arbitrary prescribed geometric R on E, choose a point P' above it and make these points rational after one further finite extension. All five sigma translates of P' are then rational and distinct because the quintic cover is etale. Thus its fibre above P is split and the deck group is constant. There is no requirement to identify R with the auxiliary parameter t. No rank assertion about C or Weierstrass assertion about P is smuggled into the conclusion.

The A13/A38 consequence uses a fixed canonical class of exact order 4159. Its order remains unchanged under constant extension. Thus it supplies an actual transferred image failing the A29 canonical-prime condition, rather than only an arbitrary point of the RM locus. The final paragraph correctly preserves the remaining distinctions: this does not force failure at both reflection images, for all covers, or in the rank-one-source/Weierstrass-point subcase. It gives no section collision.

## Primary-source check scope

I directly opened the following primary sources and read the specified statements and proof portions. I do not claim to have read the entirety of these books or papers.

1. J. S. Milne, *Abelian Varieties*, author version 2 January 2022, <https://www.jmilne.org/math/xnotes/AVs.pdf>. I read Lemma 8.3, printed p. 13, with its complete displayed proof, for finite-flat intersection pullback. I read Proposition 12.9, printed pp. 23--24, and its proof for the integral characteristic polynomial. I read Theorem 17.3 and its proof, pp. 35--36, including the supporting Lemma 17.4, to check the Rosati trace normalization. Relevant retrieval references: turn776653183view0, turn182907063view1, turn791947295view2, turn182907063view0, turn791947295view0.

2. J. S. Milne, *Jacobian Varieties*, author version 12 June 2021, <https://www.jmilne.org/math/xnotes/JVs.pdf>. I read Theorem 12.1(b), printed pp. 38--39, and its entire uniqueness argument. It supplies faithfulness of curve automorphisms on their Jacobians in arbitrary characteristic. I did not claim to recheck the existence part of Torelli in the following section. Relevant retrieval references: turn776653183view1, turn182907063view2, turn791947295view1, turn146215028view0.

3. Stacks Project, Lemma 10.128.1, Tag 00R4, <https://stacks.math.columbia.edu/tag/00R4>. I read its complete statement and displayed proof, and checked regularity, Cohen--Macaulayness, and the dimension equality for the finite morphism of smooth surfaces here. Retrieval reference: turn776653183view2.

4. A. Kumar and R. E. Mukamel, *Real multiplication through explicit correspondences*, LMS Journal of Computation and Mathematics 19, Special Issue A (2016), pp. 29--42, DOI 10.1112/S1461157016000188. I opened the published primary PDF and checked Theorem 1, p. 30, and the discriminant-five example in Section 3, p. 35, together with the introduction's description of correspondences. They confirm the background credit for the characteristic-zero genus-six (2,2) example. I did not reread the entire paper, certify its example, or use it as a premise for the characteristic-two smoothness proof. The versioned arXiv PDF fetch failed; the published PDF succeeded. Retrieval reference: turn270350467view0. Published URL: <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1478E13EEB8BAE631C6D1CA10809A86B/S1461157016000188a.pdf/real-multiplication-through-explicit-correspondences.pdf>.

No arithmetic program was rerun for this review. The matrix identities above were checked manually in the integral quadratic ring. The author's separate matrix certificate is additional evidence, not represented here as a verifier run by this reviewer.
