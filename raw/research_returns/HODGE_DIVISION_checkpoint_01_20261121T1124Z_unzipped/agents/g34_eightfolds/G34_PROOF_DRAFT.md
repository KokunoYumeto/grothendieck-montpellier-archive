# Target 3: an independently reconstructed G34 route

Run HODGE_DIVISION; agent /root/g34_eightfolds. Date 2026-11-21.
Model: GPT-6 Astra Pro (session identity). Effort: inherited, not externally exposed.
This is a proof draft with exact computational certificates. Its actual check history is recorded separately. A theorem stated here is not marked checked merely because it appears in this file.

## Scope and dependency policy

Put K=Q(omega), omega^2+omega+1=0, and O=Z[omega]. We study the natural rank-six K-representation of G34 and its multiplicity factor for twenty involution branch points over P^1. The target is the split Weil family of abelian eightfolds, signature (4,4), determinant class 1.

The numerical input below originates in Benjamin Severn's unrefereed Hexagon manuscript, work 2610.00387v2, internal version v1.5 dated 21 October 2026. The portal metadata calls it *Weil classes on every abelian sixfold of Weil type for Q(sqrt(-3))*; the actual PDF and TeX title say *Weil classes on abelian sixfolds and eightfolds of Weil type for Q(sqrt(-3))*. This mismatch must remain visible. No Severn theorem, rank claim, printed monodromy matrix, or printed Gram matrix is a premise here. His ten roots, cocycle representatives, and interval list are numerical data which our separate exact program reconstructs and verifies. Any conclusion obtained merely by citing his main theorem would remain conditional under the user's rule. Markman/032 is not used.

The primary published inputs used below are Davis's description of G34; Chevalley--Weil; Dettweiler--Wewers's topological interpretation of parabolic cohomology; Schmid's nilpotent-orbit and limiting-MHS theorems; Schoen's explicit construction with the local repair proved below; Brauer induction; and Milne's theorem on Lefschetz classes. Exact locators are collected in SOURCES.md.

## D-G34-01. The finite group, branch tuple and eightfold

Use the standard positive Hermitian form <x,y>=bar(x)^t y on K^6. The ten column roots are the rows of the following displayed array:

    (1, -1-omega, 1, omega, -1-omega, omega)
    (1, 0, 0, 1+omega, 0, 0)
    (0, 1, 1+omega, 0, 0, 0)
    (1, omega, -1-omega, omega, -1-omega, 1)
    (1, -1-omega, -1-omega, -1-omega, -1-omega, omega)
    (1, -1-omega, omega, omega, omega, omega)
    (0, 0, 1, 0, 0, -1)
    (1, omega, omega, -1-omega, 1, -1-omega)
    (1, -omega, 0, 0, 0, 0)
    (0, 1, 0, 0, 0, -1).

Define s_i=I-2 v_i bar(v_i)^t/<v_i,v_i> and t=(s_1,s_1,...,s_10,s_10). The root norms are 2 or 6; hence these are involutive reflections and product(t)=1.

**Identification certificate.** Let R be the following 756 vectors of norm 2:

- omega^a e_i-omega^b e_j, i!=j, a,b in {0,1,2}: 270 vectors;
- +/- (omega^(a_1),...,omega^(a_6))/(1+2omega), sum a_i=0 mod 3: 486 vectors.

The exact program checks that every s_i permutes R, that their generated action is transitive on R, and that its permutation-group order is 39,191,040. The action is faithful because R spans K^6. Davis, Theorem 5.1 and its proof, gives standard G34 generators as the reflections with normals e_i-e_j, e_1-omega e_2, and (1,1,1,1,1,1), and gives invariant degrees 6,12,18,24,30,42. Their order product is 39,191,040. One root reflection in our group, together with its transitive action on R, supplies the reflections in every root direction, including those standard generators. Thus the published G34 is a subgroup of our group; the equal exact orders prove equality. This identifies the group, rather than identifying it solely by an order coincidence.

The ten roots span K^6, and their nonorthogonality graph is connected, both checked exactly. To see absolute irreducibility, any invariant complex subspace W has invariant orthogonal complement. The rank-one image of each 1-s_i lies wholly in W or W^perp. Nonorthogonal roots cannot fall into opposite summands. Connectedness forces every root into the same summand, and their span is the whole space. Thus W is zero or all of K^6 after extension to C. The program also verifies scalar omega I belongs to the group. Consequently the character field is precisely K: it is contained in K by the matrix realization and contains K because tr(omega I)=6omega. The rational simple block is Mat_6(K), with Schur index one.

Riemann existence supplies a connected G34-cover C->P^1 with local tuple t. Its Hurwitz component is finite etale over a nonempty open part of the ordered configuration space M_0,20; its dimension is 17. Riemann--Hurwitz gives

    2g(C)-2=|G|(-2+20/2)=8|G|,
    g(C)=4|G|+1=156,764,161.

For the natural complex character and its conjugate, each inertia generator has one eigenvalue -1 and five eigenvalues 1. Chevalley--Weil therefore gives holomorphic multiplicity

    -6+20/2=4

for each. A rational primitive idempotent in Mat_6(K) cuts out an abelian variety A of dimension 8; the two K-embeddings have holomorphic dimensions (4,4). The parabolic H^1 multiplicity space V has K-dimension 8. The actual parabolic quotient computation below independently verifies this dimension.

## D-G34-02. Exact parabolic and boundary-monodromy certificate

Use left cocycles u(gh)=u(g)+g u(h). Write u_i=lambda_i v_ceiling(i/2), Q_i=t_1...t_(i-1). Parabolic cocycles form the kernel of

    (lambda_i) |-> sum_i Q_i lambda_i v_ceiling(i/2).

Coboundaries are u_i=(1-t_i)a. In lambda-coordinates their 20 by 6 matrix has row 2 bar(v_i)^t/<v_i,v_i>, with roots repeated twice. The relation matrix has rank 6, the coboundary matrix has rank 6, and their product is zero. Thus the quotient has dimension 20-6-6=8.

The first four chosen cocycles have lambda_(2j-1)=lambda_(2j)=1, for j=1,...,4, with all other coefficients zero. The last four are supported at indices

    (1,3,5,7,10,12,14,16,18,20)

and have respective coefficient rows

    (1,0,0,0,1+omega,1,0,-1-omega,0,-1+omega)
    (0,1,0,0,1+omega,2/3-2omega/3,-1,-2/3-omega/3,0,1+2omega)
    (0,0,1,0,-1/3-2omega/3,-2/3-omega/3,1+omega,0,1+omega,-omega)
    (0,0,0,1,1+omega,1,-2-omega,-1-omega,0,3omega).

All eight are checked to satisfy the relation; adjoining the six coboundary columns gives rank 14. They are therefore a basis of the quotient, not just eight candidate vectors.

For an auxiliary pairing certificate, put F_i(u)=sum_(j<i) Q_j u_j and compute

    S(u,v)=sum_i < Q_i^(-1)F_i(u)+u_i/2, v_i >.

Here u_i/2 is a solution of (1-t_i)a_i=u_i. This is the customary left-cocycle cup-form expression, comparable with Dettweiler--Wewers, Poincare duality, Theorem 2.5. The analytic proof below does not need that identification: S is used only as an explicitly verified auxiliary form and as a convenient way to display positive matrices. The program evaluates it directly and checks S^*=-S, rank(S)=8. Its first four basis vectors span an isotropic space I, and the upper-right 4 by 4 block is diag(3,1,1,3). All 64 entries, encoded as pairs of rational coefficients of 1 and omega, are in g34_reconstruction_result.json.

Consider the following intervals [a,b] and return powers k:

| j | a | b | k | rank N_j |
|---:|---:|---:|---:|---:|
|1|1|8|1|4|
|2|1|18|1|1|
|3|2|8|2|3|
|4|3|8|1|3|
|5|4|8|2|2|
|6|5|6|1|1|
|7|5|8|1|2|
|8|7|8|1|1|
|9|9|10|1|1|
|10|9|12|1|2|
|11|9|16|1|4|
|12|9|17|2|4|
|13|9|18|1|4|
|14|11|12|1|1|
|15|13|14|1|1|
|16|13|16|1|2|
|17|15|16|1|1|

These intervals are pairwise disjoint or nested; each determines a stable partition. They give 17 disjoint, nonisotopic essential circles on the twenty-punctured sphere, hence a maximal boundary point of Mbar_0,20. For c=t_a...t_b, the indicated k satisfies c^k=1. The kth boundary twist fixes the tuple exactly. Its pullback on cocycles is

    u'_i = u_i+(1-t_i) u(c^k),  a<=i<=b;
    u'_i = u_i,                 otherwise;
    u(c^k)=(1+c+...+c^(k-1)) sum_(i=a)^b (t_a...t_(i-1))u_i.

Indeed a boundary twist conjugates an inside loop gamma_i by the boundary word gamma_a...gamma_b; apply the cocycle identity to that conjugation and then use c^k=1. This derives the matrices from the fundamental-group action. They are not copied from Severn's printed matrices.

Reduce each transformed cocycle modulo the coboundary columns, using the verified quotient basis. The resulting matrices satisfy

    T_j=1+N_j, N_j^2=0, N_i N_j=0,
    N_j=[[0,X_j],[0,0]], T_j^* S T_j=S.

The exact program supplies every X_j and all ranks in the table. With D=diag(-3,-1,-1,-3), the Hermitian matrices -D X_j are positive semidefinite: the program verifies all 15 nonempty principal minors of each. The leading principal minors of their sum are

    96, 2379, 58722, 2344041,

all positive. Hence every positive weighted sum of the N_j has rank 4, with image and kernel I.

Flatten each X_j row by row over K. The 16 by 16 matrix obtained from rows j=1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17 has determinant 1728. Thus their K-span is all Mat_4(K), and their complex span under either embedding of K is all Mat_4(C). The supplementary rational flattening has rank 16 and a nonzero minor 64; the K-minor, rather than a rational dimension count alone, is what proves complex tangent rank.

Every assertion in this section is an exact rational/quadratic-field computation in g34_reconstruct.py. The program inputs only the ten roots, cocycle basis, and interval list. It outputs the full matrices and principal-minor data. It uses Sympy only for the finite permutation-group order; all parabolic arithmetic, reductions, ranks and determinants are implemented with fractions and the relation omega^2+omega+1=0.

## D-G34-03. Analytic bridge: the period map has rank exactly 16

**Statement.** The above Hurwitz family has period-map rank 16 at some smooth points. Its image contains an analytic open subset of the split, signature-(4,4) unitary period domain, and its algebraic moduli map is dominant onto its connected Weil component.

**Proof.** Pass to a finite marking cover of the Hurwitz space so the G-cover and chosen multiplicity factor are families and the local-system monodromy is the actual parabolic action. Around the boundary point specified above, the universal stable pointed sphere has independent plumbing parameters q_1,...,q_17. Its smooth locus is a product of punctured discs. The Hurwitz cover has finite topological degree there. A finite Kummer base change q_j=z_j^(e_j) therefore trivializes its finite permutation monodromy on that punctured polydisc. Any remaining finite central marking action is killed by a further common multiple. The resulting multiplicity VHS has unipotent monodromies whose logarithms are

    M_j=epsilon c_j N_j,  c_j positive integers,

where epsilon is the single common sign arising from the choice of positive twist versus cohomological pullback. Using marked loops and the same convention for every plumbing coordinate prevents independent sign choices. Dettweiler--Wewers, Variation of local systems, Lemma 2.2 and Theorem 2.5, identify this cocycle action with Gauss--Manin monodromy.

Write z_j=exp(2pi i w_j) on the universal cover. Schmid's multivariable nilpotent-orbit theorem, Theorem (4.12), gives

    F(w)=exp(sum_j w_j M_j) Psi(z),

where Psi extends holomorphically to the unpunctured polydisc with values in the compact dual. Let F_0=Psi(0). Restrict to the positive diagonal z_1=...=z_17=z. Its logarithm is M=sum M_j. The semidefinite certificate shows rank_K M=4 and im M=ker M=I. On the underlying rational H^1, rank M=8. The weight filtration centered at weight one is therefore

    W_0=W_1=I_Q, W_2=V_Q.

Schmid's one-variable limiting-MHS theorem, (6.16), applies to this diagonal restriction and the same F_0. Since F_0^0=V_C and F_0^2=0, its weight-zero graded piece has only type (0,0). Thus F_0^1 intersects I_C trivially. On either K-embedding block, F_0^1 has dimension 4, and

    V_sigma=I_sigma direct_sum F_(0,sigma)^1.

The tangent space to the compact dual Gr(4,V_sigma) at F_(0,sigma)^1 is Hom(F_(0,sigma)^1,V_sigma/F_(0,sigma)^1). Under the displayed decomposition, the infinitesimal action of M_j is the map from F_(0,sigma)^1 to I_sigma induced by c_j X_j, up to a common sign and a fixed invertible change of complement. These maps span all 16 tangent dimensions because the K-minor is 1728.

For completeness, nonzero limiting tangent rank gives actual interior rank, not just an infinitesimal boundary heuristic. Differentiate F(w) and translate tangent vectors back by exp(-sum w_j M_j). The jth derivative becomes

    M_j Psi(z)+2pi i z_j (partial Psi/partial z_j).

The second term tends to zero and the first tends to M_j F_0. Choose the sixteen columns with the nonzero limiting determinant. In any holomorphic coordinate chart about F_0, their determinant has nonzero limit. It is nonzero for some sufficiently small point with every z_j nonzero. Translating by the group action preserves rank. Hence the smooth period map has rank at least 16. The unitary period domain has complex dimension 4*4=16, so its rank is exactly 16.

Finally, I is totally isotropic for the actual geometric polarization, independently of the auxiliary form S. Indeed M_1 is a logarithm of a geometric polarized monodromy, so it is skew-adjoint; its image is I and M_1^2=0. For vectors u,v, the polarization evaluates on M_1u,M_1v as minus its value on u,M_1^2v, hence vanishes. Thus the rank-eight K-Hermitian multiplicity space has a K-rational isotropic 4-space. Its form is split, with determinant class 1. The period image therefore lies in the required split Weil component. Rank 16 makes it analytically open locally; the induced algebraic map to its Shimura moduli component is dominant. This completes the bridge. No comparison of source and target dimensions was used as a sufficient rank test.

## D-G34-04. Local repair for the Schoen supplier construction

**Statement.** In Schoen's paired-branch blowup construction, the primitive-character cohomology of the exceptional inverse image vanishes for every cyclic order m, including when all inertia exponents are m/2.

**Proof.** Work over C. Let a cyclic m-cover of a smooth base have normal-crossing branch divisors, and suppose two divisors with nonzero exponents a and -a mod m are blown up along their transverse intersection K. On the exceptional divisor E=P(N_(K/Y)), a P^1-bundle p:E->K, the exponent is a+(-a)=0 mod m, so the normalized cyclic pullback is generically unramified along E. The strict transforms of the two divisors meet E in two disjoint sections. Every other branch divisor meets E in the full inverse image of its intersection with K. These assertions follow directly in local parameters s,t from the two blowup charts and the equation y^m=unit*s^a*t^(m-a)*product u_l^(a_l); removing the mth power of the exceptional parameter gives the asserted restrictions.

Let beta:F->E be the finite inverse image. For a faithful character chi of mu_m, put F_chi=(beta_* C)_chi. At a point with nontrivial inertia, the chi-stalk is zero: the stalk representation is the permutation representation on the fibre and its chi-isotypic part is nonzero precisely when chi is trivial on the stabilizer. On the complement of the branch sections and other branch divisors, F_chi is a rank-one local system. Consequently on a P^1 fibre not lying in another branch divisor, F_chi is the extension by zero of a rank-one local system on P^1 minus two points with monodromy exp(2pi i a/m)!=1. On a fibre lying in another branch divisor its restriction is zero.

The compactly supported cohomology of C^* with nontrivial rank-one monodromy vanishes in every degree. One can see the ordinary cohomology from the two-term cellular differential lambda-1, which is invertible; compactly supported cohomology follows by duality. Proper base change for p therefore gives R p_* F_chi=0. In etale language the precise standard locators are SGA4 XII, Theorem5.1(iii), and XVI, Theorem4.1 for comparison: take finite coefficients at a prime not dividing m, adjoin the mth roots of unity, use the same invertible cellular differential, and pass to characteristic-zero coefficients. This also gives the stated classical-topology vanishing. Since beta is finite and proper, R beta_* C=beta_* C. It follows that H^*(F,C)_chi=0. The inverse image of the original center K has the same vanishing: every point over K has inertia containing the nontrivial subgroup generated by a, so its faithful-character pushforward sheaf is zero. Compare the compact-support localization sequences for the common complement before and after the blowup. Both closed terms have zero faithful-character cohomology, so the corresponding primitive parts are identified. This is the exceptional-cohomology assertion needed in Schoen Lemma 2.8; in particular no new primitive character is introduced by the blowup. The argument applies at every step because the branch divisors retain normal crossings. This proves the statement.

**Why the repair is included.** In the printed proof of Lemma 2.8 (p.18), Schoen chooses a prime p|m whose degree-p quotient remains ramified at the selected branch point. Such a prime need not exist: for m=12 and exponent 6, all prime-degree quotients are unramified there. The local-system proof above establishes the needed vanishing without that choice. We use the rest of Schoen's published construction (Theorem 2.0, Lemmas 2.2--2.6, and Corollary 3.1), whose paired exponents and local geometry are exactly the hypotheses just checked.

## D-G34-05. All necessary supplier determinant characters are algebraic

**Statement.** Let C be any smooth connected G-cover of P^1 whose inertia groups have order two. For every subgroup H<=G and every linear character chi:H->C^* of order m>=3, put C_chi=C/ker chi and X=C/H. Let P_chi be the primitive cyclotomic factor of J(C_chi), with F=Q(zeta_m). If its rank over F is h>0, then h is even, its Hodge numbers at every primitive embedding are (h/2,h/2), and its F-determinant classes are algebraic.

**Proof.** The quotient C_chi->X is a connected cyclic m-cover. Its inertia is an image of an intersection with a conjugate order-two inertia subgroup of C. Each nontrivial image is therefore -1 in mu_m. If m is odd the cover is unramified. If m is even every nonzero local exponent is m/2. The relation in the abelianized punctured surface group makes the sum of these exponents zero mod m; hence the number s of nonzero exponents is even. The exponents pair with their negatives. At every primitive embedding the nonzero local eigenangle is 1/2. Thus Chevalley--Weil, or elementary cyclic-cover Riemann--Roch, gives

    h=2g(X)-2+s,
    h^(1,0)_chi=h^(0,1)_chi=g(X)-1+s/2=h/2.

In particular h is even. The cyclic cover is simple in Schoen's precise sense. His explicit construction supplies algebraic determinant classes on C_chi^h; D-G34-04 establishes the exceptional-cohomology step for the present inertia. The Jacobian correspondence and cyclotomic projector then give the determinant subspace W_F(P_chi)=wedge_F^h H^1(P_chi,Q) as algebraic, as in his Corollary 3.1. A zero-dimensional factor is omitted. This proves the statement.

## D-G34-06. Brauer transfer covers the desired Weil character

**Statement.** Both K-Weil lines of the G34 eightfold are algebraic. More generally the transfer applies to a non-self-dual multiplicity determinant whenever the factor is realized by a rational group-algebra idempotent as in D-G34-01. No assertion is made that an arbitrary Schur-index representation admits a one-copy rational abelian factor.

**Proof.** Let J=J(C), H=H^1(J,Q), and U=Cent_(Sp(H))(G), the full algebraic centralizer, not only its identity component. Over C, decompose H into irreducible G-types. A non-self-dual pair tau,bar(tau) has multiplicity spaces M_tau and M_tau^*, giving a GL(M_tau) factor of U. A self-dual orthogonal G-type gives a symplectic multiplicity factor; a self-dual quaternionic G-type eta gives an orthogonal multiplicity factor. Therefore

    X^*(U_C)=Z^(nonselfdual pairs) direct_sum (Z/2)^(quaternionic types).

For a complex G-representation V define a(V) to have free coordinates mult_tau(V)-mult_bar(tau)(V) and torsion coordinates mult_eta(V) mod 2. This map is additive on the representation ring.

For a subgroup character chi, Frobenius reciprocity identifies Hom_H(chi,H_C) with the chi-eigenspace of H^1(C_chi,C). Its determinant character under U is exactly a(Ind_H^G chi): the free factors act with the indicated determinant powers, the symplectic factors contribute no character, and the orthogonal factors contribute the indicated parity. No irreducible type is omitted from this calculation.

Brauer's integral induction theorem writes the natural character sigma as an integer linear combination sum n_i Ind_(H_i)^G chi_i of linear subgroup characters. Apply a. Since sigma is a single non-self-dual irreducible, a(sigma) is the unit vector e_sigma for det M_sigma. Characters of order one or two have a=0. Their free coordinates vanish because they are real; on a quaternionic representation their eigenspaces inherit a nondegenerate alternating form, so their dimensions are even. Terms whose chi-eigenspace in H_C is zero also contribute zero. All remaining columns are supplied by D-G34-05. Thus

    e_sigma=sum_i n_i a(Ind chi_i)

is an integral relation using only algebraic supplier determinant lines. Replacing chi_i by chi_i^(-1) reverses its free character and has the same parity character, hence negates its full character. Negative coefficients therefore cause no gap.

Here is an explicit contraction argument turning the character relation into algebraicity. For each remaining supplier choose a nonzero rational algebraic determinant class y_i. Under extension to C its components in every primitive embedding determinant line are nonzero: these lines form the embeddings of a rank-one F_i-space, and a nonzero rational element has no zero embedding. For the sign of n_i choose the corresponding determinant line L_i in H^(h_i)(P_i,C), with U-character sign(n_i)a(Ind chi_i). Let L_i^dual denote the complementary top exterior line in H^(2dim P_i-h_i)(P_i,C). The cup pairing is perfect on L_i times L_i^dual, and the latter has the inverse character because U preserves the polarization and hence the total determinant.

On B=product_i P_i^(|n_i|), choose a pure tensor z in the product of these complementary lines, and let x be a nonzero vector of the desired line det M_sigma in H^8(A,C). The tensor Gamma=z tensor x on B times A is U-invariant by the integral character relation.

Each P_i is an algebraic isogeny factor of J(C): use quotient-curve pullback and its rational cyclotomic idempotent. A is likewise cut out by a rational G-idempotent. These maps commute with U, so Gamma lifts to a U-invariant cohomology class on a power of J by a U-equivariant rational H^1 splitting and its exterior algebra. The Lefschetz group S(J) is contained in U because End^0(J) contains Q[G]. By Milne, Theorem 3.2, every S(J)-invariant class on every power of J is generated by divisor classes. Thus the lift and its image Gamma are algebraic with complex coefficients.

Contract Gamma with the rational algebraic class product_i y_i^(external |n_i|) and push forward along B. Only the chosen embedding component pairs with each complementary exterior line. The result is a nonzero scalar multiple of x. It is therefore algebraic with complex coefficients. Apply the same argument to the conjugate line. Since the rational Weil subspace and rational algebraic cycle-class subspace are defined over Q, their inclusion after tensoring with C implies inclusion over Q. This proves algebraicity of the whole rational Weil space.

For the degree-bounded version one uses a middle-degree variant of the same contraction. On the curve power C_i^(h_i), the determinant line L_i is in H^1(C_i)^(tensor h_i); the inverse-character determinant line in the conjugate eigenspace is its dual under integration. Thus both lines have degree h_i. The contraction tensor on (product C_i^(h_i|n_i|)) times A has degree ell+8, ell=sum |n_i|h_i. It lifts to a U-invariant H^1 tensor on a power of J just as above. This observation is the exact interface to the supplied quantitative SQ construction; no inverse Lefschetz operator with uncontrolled denominators is needed.

## D-G34-07. Quantitative interface, with scope made explicit

The supplied file HECKE_DIV.tex, SQ1--SQ7, already contains a full elementary degree estimate conditional only on the following geometric premises: the rank-eight split G34 multiplicity family dominates; all involution-quotient suppliers are algebraic with nonzero primitive projections; and the integral Brauer relation accounts for every centralizer character, including orthogonal parity. D-G34-01--06 provide those premises, subject to the check status of these new proofs. Its quantitative proof has been read in full during this run; the exact bound below is not newly attributed to Severn.

Write G=39,191,040 and g=4G+1, and set

    R=(2G+1) G! G^G,
    L=2gR,
    S0=G^(2g) (g!)^2,
    SB=(L/2)! S0^R,
    k=L/2+4,
    B0=(40G)^k binom(k,4) SB 8! G^8.

For an O-stable target lattice with polarization elementary divisors d_1,...,d_8 and Delta=product d_i, let

    N=4 G^8 Delta,
    D8(Delta)=N^8 B0.

The supplied SQ estimates then give an effective integral four-cycle of degree at most D8(Delta) detecting the Weil space on the dominant analytic open set. The user's already supplied bounded-cycle closedness/transport results extend the bound over the connected fixed-data Weil family. Their degree-to-division theorem gives

    c_t <= ceil(C_(4,3+omega)(delta,T)) D8(Delta)^4

in the notation of the input theorem. If that theorem already defines an integer C, the ceiling is redundant. This statement is for maximal-order O-stable lattices. An arbitrary smaller endomorphism order requires a conductor factor; it is not silently included in D8(Delta).

The estimates use: an integral Brauer relation of coefficient mass at most R; supplier ranks h_i<=g; Schoen orbit-sum and Ramanujan-projector cycle mass at most S0; integral globally generated divisor representatives bounded numerically by 40G times the product polarization; Delta_A dividing G^8 for the source factor; and a rational split-lattice comparison cleared by 4G^8 Delta. These arithmetic estimates do not assert that a bare dimension inequality proves dominance. The analytic rank certificate is D-G34-03.

## Open review points, not concealed assumptions

1. The independent code establishes the finite assertions. It is not a proof of the analytic bridge by itself.
2. A second reader should check D-G34-03's common orientation, finite marking base change, limiting-MHS transversality, and derivative limit as one complete argument.
3. A second reader should check D-G34-04 through D-G34-06 as one complete supplier/transfer argument, including disconnected orthogonal characters.
4. Immutable copies of the actual served PDF and raw TeX are now saved and hashed. The TeX hash agrees with the source portal. The source ZIP returned HTTP403, so no downloaded ZIP is claimed. See SOURCES.md and SHA256SUMS.json.
5. The Severn manuscript is unrefereed and the metadata/title discrepancy is real. Its theorem is not promoted to a published input.
