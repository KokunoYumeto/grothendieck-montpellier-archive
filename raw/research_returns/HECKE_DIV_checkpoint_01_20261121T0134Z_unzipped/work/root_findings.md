# Root findings for independent proof checking

Run HECKE_DIV_20261121. Date 21 November 2026. Author /root, GPT-6 Astra Pro, effort setting unspecified. These are proposed findings until the separate check events are recorded.

## Setup and normalizations

Let omega satisfy omega^2+omega+1=0, K=Q(omega), E=C/(Z+Z omega), and g=2n, with n=2 or 4. A polarized Weil datum consists of an abelian variety A of dimension 2n with an integral O_K-action iota and an ample class theta whose Rosati involution restricts to conjugation on K; the tangent signature is (n,n). On A0=E^n x E^n use the action iota(a)(x,y)=(a x, conjugate(a) y) and the product principal polarization. The corresponding Hermitian form is split. Its connected unitary domain has complex dimension n^2. Pass to a finite level cover on which the rank-two rational Weil local system W=exterior_K^{2n} H^1 is trivial; a fixed nonzero rational section t, not all its rational multiples at once, is the target.

The degree of an effective codimension-n cycle Z is integral(theta^n [Z]), with no division by n!. Thus an n-dimensional graph in a principally polarized product has the n! factor below. Replacing theta by a fixed very ample multiple changes every bound by a fixed power, and does not change any boundedness equivalence.

## P0. Bounded effective degrees already bound a clearing multiplier

More generally let A->S be a connected polarized abelian scheme of relative dimension g, and let nonzero t be a global rational flat section of H^{2p} of Hodge type (p,p) on every fibre. Put d=g-p, V=integral theta^g/g!, and let h=||t|| be its polarized L2 norm for the translation-invariant Kähler metric with class theta. Both V and h are positive constants. Then any equality Nt_s=[Z^+]-[Z^-], with N a positive integer and Z^+,Z^- effective codimension-p cycles, satisfies

    N <= (deg Z^+ + deg Z^-)/(d! sqrt(V) h).

Proof. Lefschetz decomposition with respect to the flat polarization theta is a decomposition of local systems. Each primitive part of t is of Hodge type (p-j,p-j), so the Hodge-star formula on that part uses a fixed sign and factorial and a fixed power of theta. Thus beta=*t is flat in cohomology and integral t cup beta=h^2 is constant. All harmonic representatives on a polarized abelian variety are translation invariant, so beta has pointwise norm h/sqrt(V); its comass is at most that. Pair the displayed cycle equality with beta and apply Wirtinger's formula on the regular loci of the effective cycles, counted with multiplicities. This gives

    N h^2 <= (h/sqrt(V)) (deg Z^+ + deg Z^-)/d!.

Divide by h^2. QED.

Consequently, for a fixed nonzero flat class in such a family, bounding effective degrees of integral representatives of arbitrary positive integral multiples already bounds the multiples. The degree-only condition is equivalent to the sketch's two-parameter boundedness condition. This does not bound the denominators of rational cycles whose *weighted* degrees are bounded, because those rational coefficients must first be cleared. The elementary example N^{-1} f^*Z with large N illustrates this distinction.

## P1. An explicit algebraic Weil projector and its complexity

Put a=3+omega, Norm(a)=7, and T=iota(a)^* on H^{2n}(A,Q). After scalar extension, H^1=V_sigma direct-sum V_barsigma, each summand of dimension 2n. The direct summand

    exterior^r V_sigma tensor exterior^{2n-r} V_barsigma

has eigenvalue lambda_r=a^r conjugate(a)^{2n-r}. These 2n+1 numbers are distinct for n=2,4, as verified by their exact pairs in Q+Q omega. (Alternatively, a/conjugate(a) is not a root of unity; the only roots of unity in K are the sixth roots, and its explicitly computed value is not one of them.) The Weil plane is precisely the sum of the r=0 and r=2n eigenspaces. Define

    q0(X)=(X-a^{2n})(X-conjugate(a)^{2n}),
    R(X)=product_{r=1}^{2n-1}(X-lambda_r).

Both are integral polynomials because conjugation pairs their roots and all roots are algebraic integers. They are coprime. Let u(X) be the inverse of R modulo q0, of degree less than two, and P_n(X)=u(X)R(X). Then P_n(T) acts identically on W and as zero on all other displayed summands, hence is a rational cohomological projector onto W. It is induced by a rational linear combination of transposed graphs of iota(a)^j, including j=0. No Hodge conjecture is needed to produce this correspondence. Its idempotence is asserted on the homological motive h^{2n}(A), not on the total motive h(A) or as an equality modulo rational equivalence of unmodified Chow correspondences on every cohomological degree. If a projector on the total homological motive is wanted, compose with the degree-2n Kunneth projector, obtainable by Lagrange interpolation in [2]^* with eigenvalues 2^j in degree j.

Let delta_n be a common coefficient denominator and write delta_n P_n(X)=sum_j c_{n,j} X^j with integral c_{n,j}. Because iota(a)^*theta=7theta and deg(iota(a))=7^{2n}, the projection formula gives, for an effective n-cycle,

    deg_theta(iota(a)^{j*} Z)=7^{nj} deg_theta(Z).

Indeed intersect with iota(a)^{j*}theta^n, divide by 7^{nj}, and use the degree 7^{2nj} of the finite flat map. Pullback is effective. Separating the positive and negative c_{n,j} therefore represents delta_n P_n[Z] by an integral difference of effective cycles, each of degree at most

    B_n deg_theta(Z),  B_n=sum_j |c_{n,j}| 7^{nj}.

Exact arithmetic in compute_projectors.py gives:

| n | delta_n | B_n |
|---|---:|---:|
| 2 | 476478450 | 3590815550 |
| 4 | 411891354565851759965785179617340330000 | 497657009489489182584908205353846834744 |

For n=2 the numerator polynomial is

    -26 X^4 +6275 X^3 -538398 X^2 +21574700 X -352829351.

For n=4 its coefficients in ascending degree are

    55139367181591318902655856665347132526,
    -23659781552033798345269599858690875,
    6177440678618900865149838094771,
    -74787357945320146306888400,
    -1124625943239818173006244,
    877467858933519076300,
    -463126331859245054,
    191445325672975,
    -58750145999.

These constants are certified upper bounds for this explicit projector, not optimal denominators or minimal cycle complexities. The script checks the polynomial identities P^2=P modulo q0 R, P=1 modulo q0, and P=0 modulo R exactly over Q. The mathematical proof above identifies that finite computation with the action on cohomology.

## P2. Explicit graph seeds and raw Hecke growth

For B in M_n(O_K), write Gamma_B={(x,Bx):x in E^n} inside A0. The graph is isomorphic to E^n. The restricted polarization is the Hermitian matrix I+B^dagger B, so

    deg_theta Gamma_B = n! det(I+B^dagger B).

This follows by expanding the top exterior power of the translation-invariant (1,1) form: its determinant is the ratio to the product principal form whose top integral is n!. In particular B=I and B=diag(omega,1,...,1) are unitary and both graph degrees are n!2^n, equal to 8 and 384 for n=2 and 4 respectively.

The complex extreme Weil form Omega=dz_1 wedge ... wedge dz_n wedge d conjugate(y_1) wedge ... wedge d conjugate(y_n) restricts to conjugate(det B) times the nonzero volume form dz_1...dz_n d conjugate(z_1)...d conjugate(z_n) on Gamma_B. Consequently the projection of each of these graphs to W is nonzero. Their periods differ by conjugate(omega), which is not rational, so their rational Weil projections are linearly independent. This constructs a rational algebraic basis t_1,t_2 of W at A0. P1 gives explicit integral representatives of delta_n t_i of degree at most D_n=n!2^n B_n:

    D_2=28726524400,
    D_4=191100291643963846112604750855877184541696.

Now take the orbit of A0 under the rational special-unitary group of the polarized datum, with compatible markings. If h is such a rational isometry on H^1, choose a positive integer m clearing its lattice denominator so that the induced rational homomorphism becomes an isogeny f:A_x->A0 with f^* on H^1 equal to m h. Then

    f^* theta0=m^2 theta_x,
    deg(f)=m^{4n},
    f^* t_i(A0)=m^{2n} t_i(A_x).

The last identity uses det_K(h)=1. Pullback of the explicit seed representatives gives an integral representative of delta_n m^{2n} t_i(A_x), with each sign's degree at most m^{2n}D_n. Thus the explicit raw formulas are

    N_x=delta_2 m^4, D_x<=D_2 m^4  (fourfolds),
    N_x=delta_4 m^8, D_x<=D_4 m^8  (eightfolds).

For t=b_1 t_1+b_2 t_2 with b_i in Q, choose b>0 with b b_i integers. Then N_x=b delta_n m^{2n} and D_x<=m^{2n}D_n (|b b_1|+|b b_2|). These are formulas for chosen representatives. They do not give a lower bound on minimal c(x) and do not disprove bounded division.

At a general unitary-similitude Hecke point, the action on the Weil plane is multiplication by det_K(h), which need not be rational. It cannot be written as a scalar c_x on an arbitrarily chosen rational line without an extra tensor-preservation condition. Restricting to the special-unitary suborbit resolves this and preserves density. A fixed prescribed rational target can alternatively be handled by the 2-by-2 change-of-basis matrix.

## P3. A bounded nonzero Weil projection gives bounded denominators effectively

Fix a connected finite-type Weil family with fixed polarization type, integral O_K-action and trivialized W as above. Let Lambda=W_Q intersect H^{2n}(A_s,Z), identified independently of s; it is a rank-two lattice. Define Q_W(u,v)=(-1)^n integral_A u cup v. W is primitive of Hodge type (n,n); the Hodge-Riemann relations make Q_W positive definite. It is constant under parallel transport.

Suppose that for every s in a subset T there exists an effective n-cycle Z_s of degree at most D with P_n[Z_s] nonzero. Then for any fixed rational t in W there are integers N>0 and D'>0, depending only on the fixed family data, t and D, such that every s in T has integral effective cycles Y_s^+,Y_s^- with

    N t_s=[Y_s^+]-[Y_s^-],  deg Y_s^+<=D', deg Y_s^-<=D'.

Proof. Choose the translation-invariant Kähler representative of theta on each fibre and put V=integral theta^{2n}/(2n)!, a positive constant. Harmonic forms on a flat polarized complex torus are translation invariant. For any w in W, the primitive Hodge-Riemann identity identifies its L2 norm squared with Q_W(w,w); since the pointwise norm is constant, its pointwise squared norm is Q_W(w,w)/V. The comass is at most the pointwise norm. Wirtinger's formula gives vol(Z_s)=deg(Z_s)/n!. The projection P_n is orthogonal to its complement for the intersection pairing: an extreme K-character can pair to the top character only with the other extreme character. Thus, for every Q_W-unit vector w,

    |Q_W(P_n[Z_s],w)|=|integral_{Z_s} w| <= D/(n! sqrt(V)).

Taking the supremum over unit w proves

    ||P_n[Z_s]|| <= D/(n! sqrt(V)).

By P1 the vector v_s=delta_n P_n[Z_s] belongs to Lambda and is nonzero. Hence it belongs to the finite set

    F_D={v in Lambda: 0<||v||<=delta_n D/(n! sqrt(V))}.

The endomorphism T=iota(3+omega)^* on W has the non-real eigenvalue a^{2n}. Therefore v,Tv are Q-linearly independent whenever v is a nonzero rational vector: otherwise a rational eigenline would give a rational root of its irreducible quadratic minimal polynomial. For each v in F_D solve uniquely t=r_v v+s_v T v with rational r_v,s_v. Choose N clearing their finitely many denominators. By P1 each v_s is represented by an integral difference of effective cycles whose two degrees are at most B_n D; applying T multiplies these degrees by 7^n. The required representation has degrees at most

    D'=N B_n D max_{v in F_D} (|r_v|+7^n|s_v|).

Increase D' to an integer. This proves the assertion, with an explicit finite algorithm once D, Lambda, its pairing, and t are specified. QED.

A numerical denominator bound without enumerating all v is also available. Let G be the positive Gram matrix of Q_W in an integral basis of Lambda, let d_t clear the coordinates of t, and write a^{2n}=u+v_a omega. Since T scales the positive form by Norm(a)^{2n} and rotates by arg(a^{2n}),

    |det(v,Tv)|=sqrt(3)|v_a| ||v||^2/(2 sqrt(det G)).

Here the determinant is in the chosen integral basis, hence a nonzero integer. Let

    R=max(1,floor(sqrt(3)|v_a| delta_n^2 D^2 /
                  (2 sqrt(det G) (n!)^2 V))).

Cramer's rule shows that N=d_t lcm(1,...,R) clears all r_v,s_v. This is very inefficient but effective. The fixed integer v_a equals 55 for n=2 and 1265 for n=4.

Conversely, a bound Nt_s=[Y_s^+]-[Y_s^-] with nonzero t forces one of the two effective cycles to have nonzero Weil projection; its degree is bounded. Therefore the full bounded-division assertion for any nonzero t is equivalent to the existence of one uniformly bounded effective cycle with nonzero Weil projection. This conversion removes a separate denominator problem once that geometric degree bound is known. It does not itself produce the cycles.

## P4. Consequence of the newly located eightfold theorem

Severn, Hexagon 2610.00387v2, Theorem A, states that all Weil classes on every split eightfold for Q(sqrt(-3)) are algebraic. The source has two distinct parts: supplier/centralizer transfer and dominance from explicit G34 monodromy. In this run the former received a full targeted reading and verification of its Schoen/Milne interfaces; the latter received independent exact reconstruction of the group, all cocycles, the cup pairing, and all 17 monodromy logarithms, followed by an independent reading of the nilpotent-orbit/spreading argument. No failure has been found so far; final use awaits the consolidated check report.

If this theorem is retained as the checked manuscript input, corrected R21 immediately gives a single finite N,D for each fixed rational Weil section on the entire fixed split family. The bound is consequently uniform on its E8 Hecke orbit and on every subset thereof. This is a qualitative conclusion; the manuscript and the Baire argument do not output the numerical D. It does not use either GRH premise, Colmez's formula, or Alpöge's spectral positivity. It establishes algebraicity of the Weil plane on all members, and the full Hodge conjecture on powers of members with full special-unitary Hodge group (Severn, Theorem 11.2). It does not automatically establish the full Hodge conjecture for extra Hodge classes at arbitrary special members.

The final report must distinguish P4 as an implication of an independently checked cited manuscript from a new proof of that manuscript's Hodge theorem, and distinguish it from the still unresolved request for explicit uniformly bounded cycle representatives and numerical constants in Markman's construction.
