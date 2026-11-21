# Exact complexity 16 at every good prime of the explicit product

Date: 2026-11-21. Run: GHOSTS. Author/checker: GPT-6 Astra Pro, inherited effort not separately observable, agent `/root/bounded_specialization`. This supplement independently checks the low-degree classification and characteristic-2 coordinate estimates developed jointly with `/root/prime_arithmetic` and `/root/cm_transport`. These are ordinary mathematical proofs; no formal verification is claimed.

## F01. Fixed data and statement

Let K=Q(omega), omega^2+omega+1=0, and take E: y^2+y=x^3 over K. Its discriminant is -27, so the displayed model is smooth at every finite prime of residue characteristic p != 3. Let B=E^2, A=B x B, lambda the product principal polarization on B, and theta=lambda_first+lambda_second on A. The K-action on A is diag(k,k,bar(k),bar(k)). Let

    Gamma_a={(x,y,ax,ay)},
    t_star=[Gamma_1]+[Gamma_-1]-[Gamma_omega]-[Gamma_-omega].

At every geometric good fiber and for every auxiliary ell != p, the minimum

    min max(N,deg_theta Z^+,deg_theta Z^-)

over positive integers N and effective integral surface cycles with cl_ell(Z^+-Z^-)=N t_star,ell is exactly 16. Consequently the same minimum requiring simultaneous equality in all compatible realizations is 16: the lower bound already holds in one ell-adic realization, and the displayed four graph cycles give the simultaneous upper bound.

Degrees mean theta^2[V], with no factorial division. The characteristic-zero result was independently proved in `tstar_independent_check.md`. The proof here excludes every multiplier N, every integral effective sum, and arbitrary irreducible surfaces, including surfaces that are not graphs or abelian subvarieties.

## F02. Numerical classification of a low-degree irreducible surface

Let V be an irreducible surface in B x B over an algebraically closed field. Resolve V by a smooth projective surface S, and write f,g:S->B for its projections. Set P=f^*lambda, Q=g^*lambda and

    a=P^2/2, b=Q^2/2, c=P.Q.

Projection formula gives a=deg(f) when f is dominant and a=0 otherwise, and similarly for b. The integers a,b,c are nonnegative. Hodge index for nef divisors gives c>=2sqrt(ab), and

    deg_theta V=2(a+b+c).

These assertions are valid in arbitrary characteristic. Surface resolution and the algebraic Hodge index theorem, rather than a Hodge-theoretic positivity statement in positive characteristic, are the background inputs.

If both projections are dominant and deg_theta V<=14, the integer argument a+b+c<=7 implies ab<=2. Indeed ab>=3 forces a+b>=4 and c>=4. Hence one of a,b equals 1. After interchanging the two B factors, V is the graph of a rational map B-->B: its first projection is birational. Weil's extension theorem makes this a morphism, and rigidity makes it a homomorphism followed by a translation. Thus V is a translate of the graph of an isogeny h:B->B with degree d=1 or 2. Translation changes neither degree nor cohomology class.

Write h=(h_ij) in M_2(End(E)). On its graph,

    c=lambda.h^*lambda=sum_ij deg(h_ij)=T,
    deg_theta Gamma_h=2(1+d+T).

For the mixed-degree equality, restrict h^*lambda to each coordinate elliptic curve in B; its degree is the sum of the degrees of the two corresponding entries. Thus the budget is T<=6-d: T<=5 for d=1 and T<=4 for d=2. It includes inseparable isogenies, since degrees and projection formula include inseparable degree.

If a projection has point image, its Weil projection is zero: the Kunneth degree on that B factor is 4, whereas the Weil plane occurs in degree 2 on each B factor. The curve-image case is treated completely next.

## F03. Precise factorization when a projection has curve image

Suppose the first image is an integral curve C in B. Normalize i:C_tilde->C->B. Over the normal locus of C, take the inverse image of V in C_tilde x B and let V' be its closure. Then V' is integral and (i x id)_*[V']=[V], with coefficient one, because this map is birational over the generic point of C.

The ambient C_tilde x B is smooth of dimension 3, so V' is an effective Cartier divisor. It dominates C_tilde. Its structure sheaf is torsion-free over each local discrete valuation ring of C_tilde, hence V' is flat over C_tilde. For any geometric point u of C_tilde, its fiber is an effective divisor D_u on B. The cohomology class delta=[D_u] is independent of u, since it is the restriction of the line bundle O(V') in this constant smooth projective family.

In the Kunneth decomposition of [V'] in H^2(C_tilde x B)(1), the H^0(C_tilde) tensor H^2(B) component is 1 tensor delta. The other two components have first degrees 1 and 2. Applying (i x id)_* shifts the first degree by 2. Therefore the exact H^2(B) tensor H^2(B) component of [V] is

    [C] tensor delta.                                      (F03.1)

There is no omitted generic degree: any fiber multiplicities are contained in the effective divisor D_u. The two other Kunneth terms have degrees (3,1) and (4,0) and have no Weil component. Intersecting (F03.1) with lambda tensor lambda gives

    c=(lambda.C)(lambda.D_u).                              (F03.2)

Let T_B be the sum of the two nontrivial scalar-omega eigenspaces in H^2(B). The fourfold Weil plane is the sum of the two conjugate opposite-character lines in T_B tensor T_B. Thus a nonzero Weil component of V requires nonzero T_B components of BOTH C and D_u. This necessary condition is valid even if the second projection is also nondominant.

## F04. Effective curves of lambda-degree at most 3

For an irreducible curve C in E x E, let d_1,d_2 be the degrees of the maps from its normalization to E, with degree zero for a constant map. Then lambda.C=d_1+d_2. If one is zero, C is a coordinate fiber and has degree 1. If lambda.C=2 and neither is zero, d_1=d_2=1. Its normalization is E, and C is a translated graph of an automorphism E->E. If lambda.C=3 and neither is zero, the pair is (1,2) or (2,1), and C is a translated graph, or transposed graph, of a degree-2 endomorphism.

The same statement for an effective integral divisor of total degree <=3 follows by adding components with multiplicities. Every contribution to T_B comes from at most one graph of an endomorphism of degree 1 or 2, with multiplicity one. The remaining components are coordinate fibers. In particular, a degree-1 effective divisor has zero T_B component.

When p>3 and j(E)=0, Aut(E,0)=mu_6 is contained in O_K. Every degree-2 effective divisor is therefore scalar-omega invariant: coordinate fibers are invariant in cohomology, and a translated graph of a unit in O_K commutes with scalar omega. Hence a divisor with nonzero T_B component has degree at least 3. By F03, a curve-image surface with nonzero Weil projection then has

    deg_theta V>=2c>=2*3*3=18.                             (F04.1)

So at p>3, EVERY nondominant-projection surface of degree <=14 has zero Weil component. This does not assume the Neron-Severi group remains unchanged at supersingular primes; new divisor classes are allowed and force the degree threshold.

## F05. A normalized algebraic Weil coordinate

The same rational projector e_W from P06 of `prime_arithmetic.md` defines the Weil plane in every good fiber. Give its rational specialization space the K-valued coordinate z characterized in characteristic zero by

    z(V)=(1/4) integral_V dz_1 dz_2 dbar(z_3) dbar(z_4),
    z(Gamma_a)=bar(a)^2.

Thus z(t_star)=2(1-omega), of complex modulus 2sqrt(3). In positive characteristic the symbol z below is an algebraic coordinate on explicit projected classes, not an integral of differential forms over a finite field.

For a supersingular fiber, put D=End(E) tensor Q, a definite quaternion algebra with canonical conjugation as the dual involution and reduced norm n(u)=deg(u). It contains K. Choose j in K-perp with j^2=-delta, delta>0, so D=K+Kj and j a=bar(a)j. Write u=a+bj, and let pi_K(u)=a. Then

    n(u)=|a|^2+delta|b|^2,
    n_perp(u):=n(u)-|pi_K(u)|^2=delta|b|^2.

The absolute values here use the fixed complex embedding of K, solely to estimate elements of K. For an ordinary fiber D=K and pi_K is the identity.

For h=(h_ij), let h_K=(pi_K(h_ij)). Then

    z(Gamma_h)=conjugate(det h_K),
    |z(Gamma_h)|=|det h_K|.                                (F05.1)

To verify the formula in ell-adic cohomology, extend coefficients to split K, choose its two H^1(E) eigenlines, and represent u=a+bj by the 2x2 block matrix with diagonal a,bar(a) and offdiagonal b,-delta*bar(b), up to the harmless choice of which eigenline is first. On the graph, wedge the two first-block eigenforms with the two pulled-back opposite eigenforms from the second block. All terms involving the first character again vanish. The remaining coefficient is det(bar(h_K)). Its normalization is fixed by Gamma_1. All coefficients lie in K, so the class is the specialization of a rational element of the original Weil plane. Swapping the two B factors conjugates z and does not change its modulus.

For curves Gamma_u and Gamma_v in the two B factors one obtains

    |z(Gamma_u x Gamma_v)|
       =sqrt(n_perp(u)*n_perp(v)).                         (F05.2)

One direct sign-and-scale check is to choose formal eigenforms x,y on E with integral x y=1 and matrices u^*x=a x+b y, u^*y=-delta*bar(b)x+bar(a)y. Then integral_Gamma_u x_1 x_2=b and integral_Gamma_v y_3 y_4=delta*bar(b_v). Since the normalized fourfold coordinate is minus the coefficient paired with x_1x_2y_3y_4, its product value is -delta*b_u*bar(b_v), or its conjugate if the factors were transposed. Its modulus is exactly (F05.2). Coordinate fibers contribute zero. This also verifies the normalization independently of an abstract Hermitian-matrix identification of divisors.

For the low-degree cycles classified here, (F05.1), (F05.2), and F03 show that every projected class has a K-valued z coordinate. Therefore an ell-adic equality between such classes gives equality in K (via its injection into a chosen algebraic closure of Q_ell), and the complex absolute value may be applied to that equality. No identification of arbitrary Q_ell-linear Tate classes with rational Betti classes is assumed.

## F06. Dominant graphs at p>3

At an ordinary prime every entry of h is in O_K, so d=|det h_K|^2 and |z|<=sqrt(2). At a supersingular prime p>3, every non-K endomorphism has integer norm at least 2, because norm-one elements are automorphisms and all automorphisms are in O_K.

If a 2x2 quaternion matrix has at most three nonzero entries and is invertible, permutations make it triangular. Its degree is the product of the norms of its two diagonal entries, while |det h_K| is at most the square root of that product. Thus again |z|<=sqrt(d).

If it has four nonzero entries, the norm sum budget T<=5 permits at most one non-K entry: two would already cost at least 2+2+1+1=6. More generally, whenever one whole row or column is in K, quaternionic elimination gives

    d>=|det h_K|^2.                                       (F06.1)

For example, if the bottom row is (c,d_0) in K with d_0 != 0, the reduced norm of h is n(d_0)*n(a-b*d_0^(-1)*c). Projection pi_K is a K-bimodule map; hence the K-part of that Schur complement is a_K-b_K*d_0^(-1)*c. Its norm is bounded by the whole quaternion norm. Multiplication by n(d_0) gives (F06.1). If a pivot is zero, the triangular argument applies; transposition and quaternionic adjoint handle the other rows and columns.

Thus every dominant graph of degree <=14 has |z|<=sqrt(2) at every p>3. Together with F04 this replaces the complex period inequality for all low-degree irreducible surfaces at these primes.

## F07. Hurwitz coordinates at p=2

Here End(E) is isomorphic to the Hurwitz order

    O={q_0+q_1 i+q_2 j+q_3 k:
       all q_i in Z, or all q_i in Z+1/2},
    i^2=j^2=k^2=ijk=-1.

One can choose the isomorphism, and if necessary conjugate the chosen K embedding, so that omega=(-1+i+j+k)/2. This follows because every order-three Hurwitz unit has real part -1/2 and imaginary coordinates all +/-1/2, and signed permutations of the imaginary axes preserving their orientation preserve O and act on these choices. Put s=i+j+k, s^2=-3. Orthogonal projection to K=Q(s) is

    pi_K(q)=q_0+(q_1+q_2+q_3)s/3.

The 24 norm-one elements are the eight +/-1,+/-i,+/-j,+/-k and the sixteen (+/-1+/-i+/-j+/-k)/2. Direct substitution shows that the six units in K have |pi_K|=1, while the other eighteen have

    |pi_K|^2=1/3, n_perp=2/3.                            (F07.1)

A norm-two Hurwitz element cannot have all half-integral coordinates: four odd squares have sum 4 modulo 8, whereas four times norm two is 8. It therefore has exactly two integer coordinates equal to +/-1 and the others zero. Its K projection has squared norm either 0 or 4/3, so

    |pi_K(q)|<=2/sqrt(3) when n(q)=2.                    (F07.2)

No norm-two element belongs to K, since 2 is inert in O_K. These statements are explicit lattice calculations, not an enumeration of matrices.

## F08. Characteristic-2 dominant graph bound without exhaustive enumeration

The budget is again T<=5 for d=1 and T<=4 for d=2. If at most three entries are nonzero, triangularization gives |z|<=sqrt(d)<=sqrt(2). If four are nonzero, their integer norms are either (1,1,1,1), or (2,1,1,1); the latter occurs only when d=1.

For the all-unit pattern, if all entries lie in K then |z|=sqrt(d). If one is outside K, one of the two determinant products has modulus at most 1/sqrt(3), and the other at most 1. Hence

    |z|<=1+1/sqrt(3)<5/3<sqrt(3).

For the (2,1,1,1) pattern, put the norm-two entry in the upper-left corner. If a whole row or column is in K, (F06.1) gives |z|<=1. Otherwise either the opposite unit is outside K, or both adjacent units are outside K. In the first case (F07.1)--(F07.2) bound the two determinant terms by 2/3 and 1. In the second case they are bounded by 2/sqrt(3) and 1/3. Thus

    |z|<=max(5/3,2/sqrt(3)+1/3)=5/3<sqrt(3).             (F08.1)

This proves the needed bound for every low-degree dominant graph at p=2 with a short finite case proof. The existing C++ enumeration is an optional independent computation check, not a required proof dependency.

## F09. Characteristic-2 nondominant surfaces

For a curve-image surface V, let C,D be the effective curves of F03. A nonzero Weil component requires both degrees at least 2 by F04. If deg_theta V<=14, equation (F03.2) gives

    (lambda.C)(lambda.D)<=7.

The only degree pairs are (2,2),(2,3),(3,2). By F04, a degree-2 divisor with nonzero T_B component is a translated graph or transposed graph of a non-K unit, so its n_perp is 2/3. A degree-3 effective divisor has the same T_B class as at most one graph or transposed graph of an endomorphism of norm at most 2; its n_perp is at most 2. Applying (F05.2) to the exact middle component [C] tensor [D] gives

    |z(V)|<=sqrt((2/3)*2)=2/sqrt(3)<sqrt(3).              (F09.1)

In addition, every such nonzero-Weil component has degree at least 2*2*2=8. This treats arbitrary surfaces with a curve projection; it is not a search restricted to product surfaces. The factorization of their middle cohomology is what permits the product-coordinate estimate.

## F10. Completion for effective sums, multiplicities, and all multipliers

At every good p != 3, a nonzero-Weil irreducible surface has degree at least 8: use F02 for two dominant projections, F04/F09 for a curve projection, and the zero statement for a point projection. Consequently an effective integral surface cycle of degree <=14 contains at most one component with nonzero Weil projection, and that component occurs with multiplicity one.

For p>3 its z coordinate has modulus at most sqrt(2), by F04 and F06. At p=2 it has modulus at most 5/3, by F08 and F09. Both bounds are strictly smaller than sqrt(3). Therefore no equality

    [Z^+]-[Z^-]=N t_star, N>=1,

with both effective degrees <=14 can hold even in one ell-adic realization: projecting to W and applying z would give

    2N sqrt(3)<=|z(Z^+)|+|z(Z^-)|<2sqrt(3).

All surface degrees are even by F02, so bounds 15 and 14 are identical. Every representation of every positive multiple must have at least one numerator degree >=16. The four original degree-eight graphs give degree16 on each side with N=1, in every realization, at every good p != 3. This proves F01.

The proof also gives exact 16 k^2 for theta replaced by theta^tensor k at all these primes, since the numerator degree lower bound excluded every multiplier and surface degrees scale by k^2.

## F11. Audit of the exact-integer C++ check

I read `hurwitz_low_degree.cpp` in full. It represents a quaternion by twice its coordinates, includes all elements of norm<=5 (coordinate bounds -4..4 are sufficient since a coordinate of absolute value5 would give norm>5), and uses the all-equal-parity condition for the Hurwitz lattice. The reported norm counts 1,24,24,96,24,144 for norms0..5 agree with the direct low-norm descriptions.

The degree formula is

    n(a)n(d)+n(b)n(c)-Tr(a*bar(c)*d*bar(b)),

the reduced norm of a 2x2 quaternion matrix. Since stored real coordinates are doubled, the code subtracts exactly the stored real coordinate of the quaternion product, namely its reduced trace. Quaternion multiplication divides by2 at each product to maintain the representation, and the assertions check integrality. The K projection uses numerator (3a_0,a_1+a_2+a_3)/6 in basis1,s. Its determinant has denominator36; its norm numerator is u^2+3v^2 with denominator1296, exactly as printed.

The filters d in {1,2} and T+d<=6 describe precisely the dominant graph budget in F02. The output maxima 19/9 for d=1 and16/9 for d=2 are both below3. The hand proof F08 already supplies the strict inequality needed, so the theorem does not rely on exhaustive runtime output. I have checked the source and its mathematical scope; I have not yet independently rerun the binary, and I do not label this as a second independent computational execution.

## Source locators and level of checking

- Milne, *Abelian Varieties*, version2.00 (2008), Chapter I, Theorem3.2 (printed p.17), Corollary3.7 (printed p.19): extension of rational maps from smooth varieties into abelian varieties, and translation followed by a homomorphism. Author PDF: https://www.jmilne.org/math/CourseNotes/AVc.pdf . Exact statements and immediate proofs read in this run (PDF indices22 and24). Web refs: `turn750926826view0`, `turn750926826view1`.
- Silverman, *The Arithmetic of Elliptic Curves*, second edition, ChapterIII, Theorem10.1 (printed p.103) and Corollary10.2 (p.104): automorphism order24 for j0 in characteristic2 and mu6 for j0 in characteristic>3. Primary text mirrored at https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf ; author's bibliographic page https://www.math.brown.edu/johsilve/AECHome.html . Statements read; full characteristic2 appendix proof is background. Web refs: `turn554801576search34`, `turn412312030search5`.
- Voight, *Quaternion Algebras*, stable post-publication version1.0.5 (2024), Section42.1.3 and Theorem42.1.9, printed pp.769--772: positive standard involution and supersingular maximal order. Lemma11.1.2, Section11.2, and Theorem11.5.14, printed pp.159--161,170: Hurwitz lattice/units and the characterization of an order with24 units. Combining the last characterization with Silverman's Aut24 identifies End(E) atp2 as the Hurwitz order. Downloaded directly from author-hosted https://jvoight.github.io/quat-book-v1.0.5.pdf to `work/text/voight-v1.0.5.pdf`; extracted text and the cited full statements/proofs read. Web limit prevented opening the whole10.6MB PDF, but direct download succeeded. Indexed theorem reference: `turn718434905search37`. Author version page: https://math.dartmouth.edu/~jvoight/quat.html . The entire quaternion-algebra theory is background, not reproved here.
- Lipman, *Desingularization of two-dimensional schemes*, Ann. Math.107 (1978),151--207, unnumbered theorem in the introduction, p.151: resolution for excellent surfaces. Author-hosted PDF: https://www.math.purdue.edu/~jlipman/papers-older/%5B1978%5D%20Desingularization%20of%20two-dimensional%20schemes.pdf . Exact statement read via primary indexed text (`turn718434905search36`); proof retained as background.
- Hodge index for smooth projective surfaces in arbitrary characteristic: Hartshorne, *Algebraic Geometry*, ChapterV, Theorem1.9. The nef inequality used here follows by ample perturbation. Background theorem; no new proof certificate.

## Check events (tab-separated)

statement_id	date	who	type	outcome
F02	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	independent re-proof	All low-degree dominant surfaces classified using surface Hodge index and rational-map extension; inseparable degree retained
F03	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	independent re-proof	Normalized curve-image factorization proved via a flat Cartier divisor and Kunneth pushforward; coefficient-one and fiber multiplicities checked
F04	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	independent re-proof	All irreducible and effective curves of degree<=3 classified; p>3 threshold18 for nonzero-Weil nondominant surfaces proved
F05	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	independent re-proof	Graph determinant and product divisor coordinate normalization checked in a split K eigenbasis; no analytic finite-field period assumption
F07-F09	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	independent re-proof	Hurwitz unit/norm2 projection bounds, hand graph cases, and arbitrary nondominant surface bound checked
F10	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	targeted proof check	Effective sums, multiplicities, even degree, and every positive multiplier covered; exact16 at every good p!=3 proved from stated background inputs
HURWITZ-CODE-AUDIT	2026-11-21	GPT-6 Astra Pro; inherited effort; GHOSTS /root/bounded_specialization	targeted proof check	Read complete C++ source and output; lattice coverage, determinant, scaling, and scope verified; no claim of independent rerun
