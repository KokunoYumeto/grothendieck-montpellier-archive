# Exact local complexity of the explicit Weil class

2026-11-21. GHOSTS `/root/cm_transport`, GPT-6 Astra Pro, inherited effort not separately exposed. Joint work with `/root/prime_arithmetic` and `/root/bounded_specialization`. All proofs below are mathematical checks, not formal certificates.

The class and upper bound are those of P09 in `prime_arithmetic.md`. Put K=Q(omega), E the elliptic curve with j=0 and its specified O_K action, S=E^2, A=S×S, lambda the product principal polarization of S, and theta=lambda_1+lambda_2. Define

    t_star = [Gamma_1]+[Gamma_-1]-[Gamma_omega]-[Gamma_-omega],
    Gamma_a = {(x,y,ax,ay)}.

All reductions below are geometric good reductions, with the O_K action and product polarization specialized. Every Gamma_a has theta-degree 8, in every characteristic. Thus N=1,D=16 gives the upper bound everywhere. The purpose of this note is the lower bound, including small characteristics.

## C08. An algebraic Weil coordinate, with exact quaternion normalization

Use the polynomial projector e_W of P06. Its image on H^4 is the two-dimensional specialization of the rational Weil plane. The algebraic classes w=e_W[Gamma_1] and Rw are a basis; their intersection pairing is nondegenerate, and W is orthogonal to the other K-weight spaces. For an arbitrary algebraic cycle V, the coefficients of e_W[V] in this basis are rational: pair with w,Rw and invert their rational, nonsingular Gram matrix. These intersection numbers are the same in every realization. Thus the complex functional z of P08 has a well-defined algebraic continuation z(V) in K, after fixing the original embedding of K in C. In particular

    z(Gamma_1)=1,   |z(t_star)|=2 sqrt(3).

This construction uses algebraic pairings, not a positive Hermitian form on a resolution in finite characteristic.

For precise formulas, in the supersingular case write D=End^0(E)=K⊕Kj, with

    j^2=-c,   j alpha=bar(alpha)j,   c>0.

The reduced norm is N(alpha+beta j)=|alpha|^2+c|beta|^2. Write q_K=alpha and q_anti=beta j. Over a splitting coefficient field choose K-eigenvectors e,f of H^1(E), with j*e=f and j*f=-c e. Pullback reverses products, so for q=alpha+beta j,

    q*e=alpha e+beta f,    q*f=bar(alpha)f-c bar(beta)e.

Let tau=Tr_E(e∧f). The coordinate on S×S is the trace against e_1∧e_2∧f_3∧f_4 divided by -tau^2. This makes its value on Gamma_1 equal to 1, hence agrees with the normalization above. Two consequences follow by expanding exterior products:

1. For a homomorphism h:S→S, represented by a 2×2 matrix over D,

       z(Gamma_h)=conjugate(det(h_K)),                   (C08.1)

   where h_K means the matrix of K components of its entries. Transposing the two S factors conjugates this formula and does not change its modulus.

2. For graph curves C_q={(x,qx)} and C_r in the two copies of S, with anti components beta j and gamma j,

       z(C_q×C_r)=-c beta bar(gamma),
       |z(C_q×C_r)|^2=N(q_anti)N(r_anti).               (C08.2)

   Indeed the two curve traces are beta tau and c bar(gamma)tau, respectively; division by -tau^2 supplies the stated sign and constant. Coordinate fibers have zero such trace. Formula (C08.2) extends bilinearly to divisor classes. Translation does not change it.

In the ordinary case D=K and every divisor class on S is fixed by simultaneous scalar omega. One may also see this from the usual Picard decomposition of E×E. Its two nontrivial scalar-omega eigenspaces, denoted T, therefore receive no divisor classes. The same exterior-product calculation gives (C08.1) with h_K=h.

## C09. Low degree surfaces that dominate both factors are small graphs

Let V⊂S×S be an integral surface. On a resolution put L_1=f*lambda and L_2=g*lambda. Define a=deg f and b=deg g if the projections are dominant and set the degree to zero otherwise. Let c_V=L_1 L_2. The surface Hodge index theorem for nef divisors, valid in every characteristic, gives

    L_1^2=2a,  L_2^2=2b,  c_V≥2 sqrt(ab),
    D_V=theta^2[V]=2(a+b+c_V).                           (C09.1)

If D_V≤14 and a,b>0, then ab≤2. To check the integer threshold: ab≥3 implies a+b≥4 and the integer c_V≥4, so D_V≥16. Therefore one projection has degree one. The rational map from S to the other S extends everywhere, because rational maps from a smooth variety to an abelian variety extend. Its closed graph equals V, and the resulting morphism is a homomorphism followed by a translation. After swapping the factors if needed, V is a translate of Gamma_h with

    n=deg h in {1,2}.

Write T_h=sum_{i,j} deg(h_ij), with deg(0)=0. Intersect h*lambda with the two coordinate fibers of S to obtain

    lambda h*lambda=T_h,
    D_V=2(1+n+T_h).                                    (C09.2)

Hence n=1 implies T_h≤5, and n=2 implies T_h≤4. Degrees here include inseparable degree.

For later use, if h has a full row or column in K, then

    |det(h_K)|^2≤deg h.                                (C09.3)

For example, write h=[[a,b],[c,d]] with a,b in K and a≠0. Schur factorization gives deg h=N(a)N(d-ca^{-1}b). Projection to K is K-bilinear and decreases the positive reduced norm, so this is at least |a d_K-b c_K|^2. If the available K pivot is zero, permute rows or columns; the case of a zero row is singular. The column case follows in the same way. A matrix with a zero entry also satisfies the inequality: after permutation it is triangular, its degree is the product of the norms of its two diagonal entries, and projection to K decreases each norm.

### Consequence for p>3

For j=0 in characteristic p>3, Aut(E)=mu_6⊂K. Therefore a non-K integral endomorphism has degree at least two. Under the budgets above, h has at most one non-K entry. Here is the complete two-entry exclusion. Three such entries cost at least six. With exactly two, their cost is at least four. If they occupy opposite corners, the remaining cost is at most one, so at least one other corner is zero and deg h is the product of the two non-K norms, at least four. If they occupy one row or column, the remaining row or column costs at most one; at budget five, the only nonsingular possibility has one remaining unit and has degree at least two, contradicting n=1. At budget four it has a zero row or column, contradicting n=2. Thus at most one non-K entry occurs, and (C09.3) applies. By C08,

    D_V≤14 and a,b>0 imply |z(V)|≤sqrt(2), for p>3.       (C09.4)

This includes ordinary reductions. It does not extend the unrestricted complex Cauchy–Schwarz inequality to all supersingular surfaces.

## C10. Nondominant projections factor through effective divisors

Suppose the first projection of V has image an integral curve C⊂S. Let nu:C_tilde→C be the normalization and let V_tilde be the closure of the inverse image over the smooth open part of C, inside C_tilde×S. It is an integral Cartier divisor in a smooth threefold and maps birationally to V. It dominates the smooth curve C_tilde, hence is flat over it. Restrict its line bundle to a geometric fiber; its divisor delta is effective, of constant class and degree d_delta. There is no extra generic multiplicity: the map to V is birational over the original open subset.

The H^2⊗H^2 Kunneth component of [V] is exactly

    [C]⊗[delta].                                      (C10.1)

To see this, decompose c_1(V_tilde) in H^2(C_tilde×S). Its H^0(C_tilde)⊗H^2(S) part is 1⊗[delta]; pushforward by nu×id sends this to [C]⊗[delta]. The other two terms map to H^3(S)⊗H^1(S) and H^4(S)⊗H^0(S), so cannot contribute. Also

    c_V=(lambda C)(lambda delta)=d_C d_delta.           (C10.2)

If the first image is a point, its Weil coordinate is zero directly. If the second projection is the nondominant one, interchange factors.

Every effective divisor on S of lambda-degree one is a coordinate fiber. An integral divisor of degree two with both E-projections dominant has degrees (1,1), so is a translated graph of an automorphism E→E. An integral divisor of degree three with both projections dominant has degrees (1,2) or (2,1), so is a translated graph of a degree-two endomorphism, up to interchanging the E factors. An integral divisor with one projection constant is exactly a coordinate fiber and has degree one. These statements also classify effective divisor cycles of degree at most three, by summing integral components with their positive integer multiplicities.

For p>3, all degree-two graph automorphisms are in K, so every effective divisor of degree≤2 has zero T component. If z(V)≠0 in (C10.1), both C and delta must have nonzero T component, so both degrees are at least three. Consequently

    z(V)≠0 and a b=0 imply D_V≥2 d_C d_delta≥18,
    for p>3.                                          (C10.3)

In the ordinary case all divisor classes have zero T component, so every nondominant V has z(V)=0, without a degree restriction.

## C11. Characteristic two

The endomorphism order of the unique supersingular elliptic curve in characteristic two is the Hurwitz order

    O_H={w+xi+yj+zk: w,x,y,z all integers or all half-integers},

with norm w^2+x^2+y^2+z^2. An embedding of O_K is represented, after an automorphism of this normed order, by omega=(-1+i+j+k)/2. This last reduction is elementary: every trace-minus-one, norm-one element is (-1±i±j±k)/2, and a signed permutation of the imaginary coordinates with determinant one takes its axis to (1,1,1). The orthogonal projection to K sends

    w+xi+yj+zk to w+((x+y+z)/3)(i+j+k).

The 24 norm-one elements have K-projection modulus 1 if they lie in K and 1/sqrt(3) otherwise. Every norm-two element has K-projection modulus at most 2/sqrt(3). Both facts follow by listing the integer and half-integer coordinates of the indicated small norms. In particular a non-K unit has anti-K norm 2/3.

For a graph of degree at most 14, C09 leaves matrices with entry-norm sum at most five. A zero entry is covered by the triangular bound (C09.3). If all four entries are nonzero, the only patterns are (1,1,1,1) and (2,1,1,1).

For pattern (1,1,1,1), if all entries are in K, |z|^2=deg h≤2. Otherwise at least one of the two determinant products has modulus at most 1/sqrt(3), while the other has modulus at most one. Thus |z|≤1+1/sqrt(3)<5/3.

Pattern (2,1,1,1) occurs only when deg h=1. A full K row or column gives |z|≤1 by C09.3. Otherwise put the norm-two entry in the top left corner. If its opposite unit is non-K, the two determinant products have moduli at most 2/3 and 1, giving |z|≤5/3. If that opposite unit lies in K, the absence of a full K row or column forces both adjacent units to be non-K. The bound is then 2/sqrt(3)+1/3<5/3. Therefore

    D_V≤14 and a,b>0 imply |z(V)|≤5/3, in p=2.          (C11.1)

For a nondominant projection, nonzero z requires both divisor degrees in C10.1 to be at least two. Since d_C d_delta≤7, they are (2,2), (2,3), or (3,2). A degree-two divisor with nonzero T part is a non-K unit graph and has anti-K norm 2/3. A degree-three effective divisor is either a degree-two endomorphism graph, whose anti-K norm is at most two, or a unit graph plus a coordinate fiber, which gives a still smaller bound. The coordinate formula C08.2 therefore gives

    |z(V)|^2≤(2/3)·2=4/3.                             (C11.2)

Every z-nonzero component has degree at least eight, by C09.1 in the dominant case and C10.2 in the nondominant case.

## C12. Characteristic three

Over an algebraic closure of F_3 take E:y^2=x^3-x. The automorphisms

    omega:(x,y)↦(x+1,y),
    i:(x,y)↦(-x,s y),  s^2=-1,

satisfy omega^2+omega+1=0, i^2=-1 and i omega=bar(omega)i. The order

    O=O_K⊕O_K i

has reduced discriminant three: the trace Gram matrix on 1,omega,i,omega i has determinant -9, of absolute value nine. The containing quaternion algebra is ramified exactly at three and infinity. Thus O is maximal and, since it is already contained in End(E), equals End(E). Its norm is

    N(A+B i)=N_K(A)+N_K(B).

The norm-one elements have K-projection modulus one or zero; the norm-two elements have K-projection modulus one, since there are no Eisenstein integers of norm two. A non-K unit has anti-K norm one.

Again consider the patterns (1,1,1,1) and (2,1,1,1). In the first, either all entries lie in K, giving |z|^2=deg h≤2, or at least one K-projection is zero, leaving at most one nonzero determinant product and |z|≤1. In the second, if all three units lie in K there is a full K row and (C09.3) gives |z|≤1; otherwise one K-projection vanishes and the same bound follows directly. Zero-entry matrices are triangular. Hence every dominant V of degree≤14 has |z(V)|≤sqrt(2).

For nondominant V, C10 forces divisor degrees (2,2), (2,3), or (3,2) whenever z is nonzero. The anti-K norm bounds are one for degree-two unit graphs and at most two for degree-three divisor cycles. C08.2 gives |z(V)|≤sqrt(2). Every z-nonzero component again has degree at least eight.

The standard Q-model used in P02 is bad at three, but this argument covers good reductions at three after a field extension; it is not an assertion of good reduction of that particular Q-model.

## C13. Exact complexity at every geometric good reduction

In every characteristic, effective surface degrees are even by C09.1 and additivity. An effective cycle of degree≤14 has at most one z-nonzero component, with multiplicity one, because each such component has degree at least eight. The preceding bounds therefore give

    |z(T)|≤sqrt(2) for p>3 or p=3,
    |z(T)|≤5/3 for p=2,

whenever T is effective of degree≤14. Both bounds are strictly less than sqrt(3). If

    N t_star=[T^+]-[T^-],  N≥1,

and both effective degrees were at most 14, we would have

    2N sqrt(3)=|z(T^+)-z(T^-)|<2 sqrt(3),

a contradiction. Thus every representative of every positive multiple has maximum numerator degree at least 16. The graph formula with N=1,D=16 attains it. Consequently

    c_theta(t_star)=16

at every geometric good reduction, for one fixed prime-to-p realization or simultaneously for all realizations. The complex minimum is P09. No effectiveness of a lift of a special-fiber cycle was assumed anywhere.

The same proof gives c_{theta^tensor k}(t_star)=16k^2 in every such fiber for k≥1.

## C14. Why the unrestricted supersingular inequality fails

In characteristic five let j be Frobenius on the trace-zero j=0 elliptic curve, so j^2=-5 and j omega=bar(omega)j. The homomorphism

    h=[[2,j],[-j,2]]

is an automorphism: its product with [[2,-j],[j,2]] is -I. Thus the two projection degrees of Gamma_h are both one. But h_K=2I, so C08.1 gives z(Gamma_h)=4. Its theta-degree is 2(1+1+18)=40. Hence the unrestricted assertion |z(V)|≤sqrt(ab) is false in finite characteristic, while the degree-restricted substitute proved above is sufficient. The larger example [[1-p,pi],[pi,1]] at an inert prime has determinant degree one and z=1-p, with degree 2p^2+8.

## Primary background and exact locators checked

* Milne, *Abelian Varieties*, corrected 2 January 2022, Corollary 2.2 and Theorem 3.1, pp. 3–4; rational maps to abelian varieties extend and are translates of homomorphisms. Proposition 12.9, p. 23, identifies degree with the Tate-module determinant. <https://www.jmilne.org/math/xnotes/AVs.pdf>.
* Milne, *Elliptic Curves*, second edition, Theorem II.6.9, printed p. 73 / PDF p. 78, for the endomorphism-algebra alternatives and quaternion ramification; Proposition IV.7.13, printed p. 140 / PDF p. 145, for j=0 automorphisms in characteristic different from two and three. <https://jmilne.org/math/Books/EC2.pdf>.
* Castryck–Houben–Vercauteren–Wesolowski, *On the decisional Diffie–Hellman problem for class group actions on oriented elliptic curves*, Research in Number Theory 8 (2022), article 99, footnote 2, explicitly identifies the characteristic-two endomorphism ring with the Hurwitz order. <https://link.springer.com/article/10.1007/s40993-022-00399-6>. The small-norm bounds above are independently derived, not imported from that paper.
* The existence of resolutions of algebraic surfaces and the surface Hodge index theorem in arbitrary characteristic are classical background. These are used only in the numerical inequality C09.1. No characteristic-p Hodge positivity conjecture is used.

## Actual check events

| statement | who | type | outcome |
|---|---|---|---|
| C08 | cm_transport | targeted proof check | Both quaternion formulas derived explicitly from e,f and cup products; normalization checked against Gamma_1; rationality via algebraic Gram matrix checked |
| C09 | cm_transport | targeted proof check | Complete low-degree graph reduction, exact degree budget, Schur norm comparison and two-non-K-entry case split checked |
| C10 | cm_transport and bounded_specialization | independent re-proof | Curve normalization, flat divisor family, Kunneth pushforward and absence of extra multiplicity checked; low-degree curve classification gives the needed divisor bounds |
| C11 | prime_arithmetic, independently read by cm_transport | independent re-proof | Short Hurwitz small-norm proof checked; enumeration is corroborative only and unnecessary to the proof; product-coordinate normalization checked in C08 |
| C12 | cm_transport, independently read by prime_arithmetic | independent re-proof | Explicit automorphisms and order discriminant checked; norm-one/two patterns and graph/divisor inequalities checked |
| C13 | cm_transport | targeted proof check | Entire lower-bound deduction, multiplicities, parity, all-realization upper bound and small-prime scope checked |
| C14 | prime_arithmetic and cm_transport | independent re-proof | Matrix inverse, projection degrees, K block, norm sum and degree40 checked; it refutes only the unrestricted positivity inference |

Dates for all rows: 2026-11-21. Model for all agents: GPT-6 Astra Pro; inherited effort not separately exposed. No Lean or other formal verification is claimed.
