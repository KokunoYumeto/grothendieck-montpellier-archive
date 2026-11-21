# Supersingular norm gap and the actual characteristic-5 endomorphism order

Author/checker: GPT-6 Astra Pro, inherited reasoning effort not exposed, run `/root/cm_transport`, 2026-11-21. This is a derivation and an exact arithmetic check, not a formal verification.

## C30. A commutator proof of the norm gap

Let E be a supersingular elliptic curve over an algebraically closed field of characteristic p, with the specified embedding O_K=Z[omega] in End(E), where omega^2+omega+1=0. Put D=End^0(E), K=Q(omega), and s=omega-bar(omega), so s^2=-3. Let n denote reduced norm, which on an actual endomorphism is its degree. The positive norm is orthogonally decomposed by D=K plus K-perpendicular. Write u=alpha+beta j, where j k=bar(k)j for k in K and j^2=-c with c>0. Then

    n(u)=Nm_K(alpha)+c Nm_K(beta),
    n_perp(u):=c Nm_K(beta),
    [omega,u]=s beta j,
    n([omega,u])=3 n_perp(u).

For an actual endomorphism u, the commutator is an actual endomorphism. The differential at the identity is zero: the one-dimensional tangent space makes d(omega) and d(u) commuting scalars. Differentials at all other points are obtained by translation, so the entire map has zero differential. If u is not in K, then beta is nonzero, hence [omega,u] is nonzero. It is therefore an inseparable isogeny of elliptic curves. Its inseparable degree is a positive power of p, and in particular

    3 n_perp(u)=n([omega,u]) is a positive integer divisible by p.

Consequently

    u notin K  ==>  n(u) >= n_perp(u) >= p/3,

and because n(u) is an integer, n(u)>=ceil(p/3). This includes the wild case p=3. In particular every actual endomorphism of norm at most 3 belongs to K when p>=11, and then belongs to O_K because O_K is the full ring of integers of K.

No canonical lift, positivity of arbitrary surface classes, discriminant estimate, or choice of maximal-order representative enters this proof. The norm identity is rational quaternion algebra; the divisibility is inseparability of an actual endomorphism.

Background locator: Milne, *Elliptic Curves*, second edition, II Proposition 6.4 (printed p.71/PDF p.76) identifies the endomorphism degree with the characteristic-polynomial determinant; II Theorem 6.9 (printed p.73/PDF p.78) gives the quaternion algebra ramified at p and infinity. The differential criterion and p-power inseparable degree also follow directly from the extension of function fields of smooth curves; the latter is reviewed in V section 7 (printed p.216/PDF p.221). These are used as standard background, while the commutator argument is proved above.

## C31. The sharp entry bound for the already established graph budget

Let h:E^2->E^2 be an isogeny, write d=deg(h), T=sum_{i,j} n(h_ij), and let Gamma_h lie in E^2 times E^2 with the product principal polarization theta. The established identity is

    deg_theta(Gamma_h)=2(1+d+T).

For the low-degree graphs used in the exact t_star argument, the projection argument gives d in {1,2} and degree at most 14. Thus T<=5 for d=1 and T<=4 for d=2. Every entry then has norm at most 3, not merely at most 5:

* If all four entries are nonzero, their norms are positive integers, so each is at most 2 when T<=5 (and at most 1 when T<=4).
* If some entry is zero, row/column permutations make h triangular. The reduced norm of its diagonal is the product of the two diagonal entry norms, equal to d. When d=1, both diagonal entries have norm 1, leaving at most 3 for the off-diagonal entry. When d=2, diagonal norms are 1 and 2, leaving at most 1 for the off-diagonal entry. If a second off-diagonal entry is also zero, the same product statement applies.

This proof works over every quaternion endomorphism order, including for inseparable entries. Combined with C30 it shows that every such h has all entries in O_K for p>=11. Hence any further hand argument that uses only the matrices of these graphs and O_K relations carries over verbatim for those primes. This implication does not by itself classify all arbitrary surfaces of degree up to 22; that separate geometric/class-cancellation step must be supplied by the primitive-class argument.

## C32. An explicit order inside End(E) at p=5

Work with

    E/F_5 : y^2=x^3+1,
    omega(x,y)=(zeta x,y),  zeta^2+zeta+1=0,
    F(x,y)=(x^5,y^5),
    pi=-F,
    s=omega-bar(omega)=1+2 omega=omega(1-omega).

There are five affine F_5-points, namely (0,1),(0,4),(2,2),(2,3),(4,0), and the point at infinity. Thus #E(F_5)=6, Frobenius trace is zero, and pi^2=-5. Since zeta^5=zeta^2, pi omega=bar(omega) pi. In particular pi and omega do not commute, so the endomorphism algebra is the quaternion division algebra of discriminant 5, by Milne II Theorem 6.9.

The kernel of s equals the kernel of 1-omega, namely

    E[s]={O,(0,1),(0,-1)}.

This is an etale subgroup scheme because deg(s)=3 and p=5. Frobenius F fixes it pointwise, so 1+pi=1-F kills it as a group scheme. A homomorphism killing the kernel of a separable isogeny factors uniquely through that isogeny. Equivalently, the quotient E/E[s] is the codomain of s, and descent along this finite etale quotient applies. Therefore there is an ACTUAL endomorphism q of E such that

    q s=1+pi,
    q=(1+pi)s^{-1}.

The division is on the RIGHT. This sign and side are part of the construction. With pi=+F on this particular F_5 model, 1+pi acts as multiplication by 2 on E[s], so the same right quotient would NOT be integral. Left division cannot silently be substituted either.

Using pi s=-s pi, write

    q=s^{-1}-s^{-1}pi.

It follows that

    q^2=-2,
    q omega=bar(omega)q+1,
    trd(q)=0,
    n(q)=2.

The lattice O=O_K plus O_K q is closed under multiplication by these relations and is contained in End(E). In the ordered Z-basis (1,omega,q,omega q), its reduced-trace pairing trd(xy) has matrix

    [ 2 -1  0  1 ]
    [-1 -1  1 -1 ]
    [ 0  1 -4  2 ]
    [ 1 -1  2 -3 ].

The determinant is -25, so its reduced discriminant is 5. Voight, *Quaternion Algebras*, Theorem 15.5.5 (printed p.241), proves that an order is maximal exactly when its reduced discriminant equals the quaternion-algebra discriminant. Thus O is maximal. Since it is already embedded in the order End(E),

    End(E)=O_K plus O_K q.

This argument does not assume a class number, uniqueness of a maximal-order conjugacy class, or an unverified optimal embedding. It constructs the inclusion and uses maximality only after the inclusion is established.

For alpha,beta in O_K, its orthogonal K-projection and perpendicular norm are therefore exactly

    pr_K(alpha+beta q)=alpha+beta/s,
    n_perp(alpha+beta q)=(5/3) Nm_K(beta),
    n(alpha+beta q)=Nm_K(alpha+beta/s)+(5/3) Nm_K(beta).

All geometric j=0 elliptic curves in characteristic 5 are isomorphic to this model. Transporting the chosen order-three automorphism gives omega or bar(omega), which merely conjugates the K coordinates. The displayed formula is consequently valid for the marked geometric endomorphism ring after making that explicit choice; no descent to the residue field itself is being asserted.

## Actual check events

* 2026-11-21, C30: entire argument rederived, including the actual-endomorphism differential, centralizer/nonzero condition, inseparable degree, and factor 3. Background quaternion theorem directly read from Milne's primary PDF.
* 2026-11-21, C31: all zero-pattern and positive norm-budget cases checked by hand. The conclusion is explicitly restricted to the stated graph budget; the full primitive-class classification is not assumed.
* 2026-11-21, C32: actual inclusion proved using the etale kernel, with the Frobenius sign corrected before using the proposed order. Relations, all 16 trace Gram entries, determinant -25, and the six F_5-points independently checked using exact rational SymPy arithmetic. Voight Theorem 15.5.5 and its entire proof directly read in the downloaded primary text, with the inclusion hypothesis checked separately.

## C33. Independent complete check of V01–V04

The complete text `GHOSTS_package/sections/primitive_weil.tex` was read on 2026-11-21 after its author supplied it. No flaw was found. The accepted theorem is exact complexity 16 for the primitive class t0=t_star/2 over C and every geometric good reduction with p>3. It does not assert the primitive minimum at p=2 or p=3.

The following delicate steps were independently rederived, rather than accepted from the summary: (1) the coordinate-pair projection argument showing a degree-one pair for every integral surface of degree at most6; (2) extension of its rational coordinate maps from E² and equality with the closed graph; (3) the mixed-pair calculation with f=[[1,0],[a,b]], g=[[0,1],[c,d]], including the order of every quaternion factor in deg(b)g f^{-1}; (4) the equality degree=2(1+T_U), also for a norm2 inseparable entry; (5) injectivity of either main odd coefficient from degree pairs (1,1),(2,8),(8,2); (6) exactly one nonzero odd correction per numerator, covering multiplicities and optional zero-odd components; (7) the resulting bound T_M,T_N<=3 and exclusion of non-K entries for p>3; (8) the rank-one trace inequality with a monomial unitary main matrix; (9) the final one-entry/cofactor contradiction when both main matrices have three unit entries.

The stated odd-coefficient matrices use the chosen duality convention; transposition/Rosati adjunction under another convention preserves every equality, rank, norm, and degree argument actually used. The proof is therefore sound once that convention is used consistently.

V01's integral even-Kunneth projection, all six graph intersections, and square-divisibility primitiveness argument were checked. V04's norm identity, triple gcd, lattice-index relation h²|27, exact denominator q_n, and effective upper representation were also checked.

The new proof is stronger than the norm-gap transfer: its main matrices have only unit entries, so the automorphism group at j=0 suffices for every p>3. The norm-gap lemma C30 remains independently useful but is not a required step in V03.
