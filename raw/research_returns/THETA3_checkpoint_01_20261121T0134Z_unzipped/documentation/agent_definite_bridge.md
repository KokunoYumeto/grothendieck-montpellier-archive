# THETA3 definite-side comparison: source audit and proved refinements

Author/checker: GPT-6 Astra Pro, inherited effort (numeric effort was not exposed), run THETA3/definite_bridge. Date: 2026-11-21. All mathematical proofs below were subsequently read in full for a targeted proof check; see the companion events TSV. This is a contribution to the parent paper, not a claim that the main requested comparison has been solved.

## 1. What the attached Alpöge evidence specifies

The four-page note has a timeline, not a statement of the required period comparison. Its p.3 step4 says a determinant gives positivity of W(1_S). Its p.4 step7 discusses determinants containing GGP periods and interlacing weights. Its step8 says the chain of totally definite unitary theta lifts wins multiplicity, and writes the parameter modification pi -> pi boxplus mu_j[t]. Its step12 says an iterated-lift period becomes a Bessel period independent of the Hecke characters, by a seesaw and Rallis. None of those entries specifies the Hermitian spaces, their dimensions, the Bessel subgroup or character, the Schwartz vector, Haar measures, normalization of the period, or the relation to a differential-form realization.

The map `sources/ALPOGE_LEAN_MAP_20261120.md` is expressly a text parsing report; its introductory paragraph says no Lean build occurred. In §4 the row for step4 has confidence “none”; step7 has confidence “medium”; step8 “medium-high”; step12 “medium”. Paths in those rows are search candidates, not theorem statements. In particular:

* Step7: `Formalism/PeriodIntegrals/BesselPeriodGGP.lean`; interlacing names in `Formalism/SharpRestriction/CuspSpanNormBounds/OscillatoryIntegralBounds.lean`.
* Step8: `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/*`; `Proofs/IwasawaDecomposition/ThetaLiftAtReferenceTupleOverEnlargedBase.lean`; `Development/WeilBound/ThetaLifts`.
* Step12: `Development/AutomorphicArithmetic/ThetaCorrespondence/RallisInnerProduct`; also `Proofs/DecoratedLatticeProofs` and `Definitions/LatticeFrames`; named literature propositions `RallisInnerProductConvergent`, `RallisTowerUnitary`, `RallisCoinvariants`.

The map §3, Level4 does quote the declaration `every_character_of_theta_integrals_local_matching` at `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean:69`. Its arguments include `ThetaIntegralsAgree`, `LocalMatching`, and `CovolumeBoundOfX`, and its conclusion is `UpperTheory.EveryCharacter`. Their mathematical definitions are not quoted. Likewise `DefiniteSideCondition` occurs as a type argument, with no definition displayed. Consequently this declaration does not identify the local matching needed here.

The only complete Lean files attached are `ALPOGE_Main.lean` and `ALPOGE_Statements.lean`; they state the cited RH and Dirichlet GRH results but contain none of the theta-period definitions. This report accepts the user's cited GRH theorem as background and draws no conclusion about validity of the absent formalization. It does not claim to have read missing files, checked their theorem bodies, or run Lean.

### Source audit finding THETA3-B0

**Statement.** The supplied material does not provide an exact mathematical statement of the Alpöge Bessel-period functional required to instantiate sketch1.7. Thus a literal equality of that functional with the period of 032 Corollary4.7 cannot currently be checked from the attached files.

**Verification.** The map has exactly the paths/names above and no displayed Bessel integral. The note has only the timeline sentence. The two attached Lean files contain only final zero-free/zero-on-line declarations. This is an evidence finding, not a mathematical refutation of the existence of such an equality.

## 2. The 032 data which must be matched

032 §4.1, pp13–14 fixes a Galois CM field E with real subfield F of degree at least2, a distinguished real place mu, a Hermitian space V of E-dimension3 with signatures (2,1) at mu and (3,0) elsewhere, and G=SU(V). Its arithmetic quotient X is a smooth compact complex surface after principal level. Its multiplicity spaces P have dimensions k=1 or2. With delta in E, conjugate(delta)=-delta, its symplectic form is

    psi_P = Tr_(E/F)(delta h_V tensor h_P).

At mu its positive Lagrangian is

    F_P = (L tensor P_mu) direct-sum (Q^* tensor P_mu^*),

where L is the negative line and Q=V_mu/L. The determinant square root contributes L^k, and the projected degree1 or degree2 Taylor tensors give Omega^1 or K_X (032 Lemma4.1 and equations4.5–4.8, pp14–16).

The auxiliary splitting Hecke characters in §4.4 satisfy chi_H|A_F=epsilon_(E/F)^dimH and chi_K|A_F=epsilon_(E/F)^dimK. Their changes act by determinant twists; they disappear on SU(V) (Lemma4.4, pp19–21). They are not the active spherical Hecke eigencharacters in §6.1, nor a specified automorphic source character on U(P). Lemma6.2 uses *bare rational metaplectic covariance*, rather than the value of a splitting character; its equation6.2 is an independent check on the scalar calculation below.

The actual 032 nonvanishing argument is Proposition4.5 (fiber spanning by Gaussian concentration), Proposition4.6 (product tensors and fixed-input continuity), and Corollary4.7 (rational approximation at compact places). It holds V, G, the finite Weil action, the single total finite input, and the quotient fixed. It varies signed positive subspaces in P at the already compact places. It does not change the signature of V at mu. Signature is locally constant on nondegenerate Hermitian forms, so the indicated continuous deformation cannot itself reach a definite V.

## 3. A precise global comparison with the finite places controlled

### THETA3-B1 (rank-three definite neighbors)

**Statement.** Let E/F and V be the 032 data above. There exists a global Hermitian space V^- of dimension3, with signature (0,3) at mu and (3,0) at every other real place, such that V^-_v is isometric to V_v at every finite place v. In contrast there is no globally positive definite V^+ isometric to V at all finite places. For any finite nonsplit place v0 of E/F there is a globally positive definite space V^(v0) isometric to V at every finite v other than v0; at v0 its determinant norm class is the opposite of that of V.

**Proof.** For each local Hermitian space use the sign epsilon_v of its determinant in F_v^*/Norm(E_v^*); at real v this is (-1) raised to the negative index. A coherent global collection satisfies product_v epsilon_v=1. Local dimension and determinant classify finite Hermitian spaces, and the product condition, together with specified real signatures, suffices for a global Hermitian space by Landherr's theorem. An exact accessible source is B.H.Gross, *Incoherent definite spaces and Shimura varieties* (25 February2018), §3 Theorem3.1, pp6–7, https://people.math.harvard.edu/~gross/preprints/incoherent.pdf.

Replacing the negative index1 at mu by3 preserves its determinant sign; keep every other local space. The product remains1, and Landherr gives V^-. Replacing the negative index1 by0 reverses that sign. Keeping all remaining local spaces would give product -1, proving impossibility. Reverse also the determinant norm class at any finite nonsplit place v0. There are exactly two local dimension3 Hermitian spaces there, so this is possible; their product of signs is again1. Landherr gives V^(v0). Its signatures are positive definite at all real places. QED.

**Scope.** This concerns Hermitian spaces and their oscillator embeddings. In odd dimension, scalar multiplication of a Hermitian form can leave its unitary group unchanged. An isomorphism of abstract groups does not identify the dual-pair embeddings, Weil representations, splitting scalars, or chosen testvectors. The impossibility assertion is about holding the finite *Hermitian local isometry classes* fixed, not about holding abstract finite unitary groups fixed.

**Motivic interpretation.** The complex ball quotient and its definite neighboring Shimura datum can be compared outside {mu,v0}. This gives the finite set of places where an automorphic/realization comparison must supply new data; it does not produce an algebraic correspondence between their motives.

## 4. The archimedean tensor detects which neighbor can work

### THETA3-B2 (bare scalar-weight calculation)

**Statement.** Retain delta and the multiplicity-space sign from 032 at mu. Let k=dim_E P be1 or2. Write r=t^2 for the standard double cover of the scalar circle in U(P_mu), so t records the bare metaplectic square-root character. The cohomological tensor used by032 has scalar weight t^(-3k). For the negative-definite replacement V^-_mu of B1, the polynomial tensor module

    direct-sum_(j>=0) (det F^-)^(1/2) tensor Sym^j F^-

has only weights t^(3k+2j), j>=0. Therefore the weight t^(-3k) is absent. For the positive-definite replacement V^+_mu the vacuum line (det F^+)^(1/2) has exactly weight t^(-3k).

**Proof.** In the convention of032 equation4.5, scalar r on P acts by r on L tensor P, of dimension k, and by r^(-1) on Q^* tensor P^*, of dimension2k. Thus det F_P has scalar r^(-k), whose chosen metaplectic square root is t^(-k). The projected degree-k tensor has scalar r^(-k)=t^(-2k). Their product has scalar t^(-3k). For k=1 this is precisely the active exponent -3 in the square of the scalar in032 Lemma6.2.

Write delta_mu=i a with a real nonzero. The chosen sign of h_P is -sign(a), by032 Lemma4.1. If h_V becomes negative definite, then a h_V h_P is positive definite, and the positive Lagrangian is the full nonconjugate embedding summand. It has dimension3k and scalar r. Hence its half determinant has weight t^(3k), while Sym^j contributes t^(2j). All its polynomial weights are as stated, none equal t^(-3k). If h_V becomes positive definite, the positive Lagrangian is the full conjugate summand, with scalar r^(-1) and dimension3k, so its half determinant is t^(-3k). QED.

**Exact limitation.** This is a calculation of the specified covariant polynomial/tensor model and its bare scalar circle. Actual infinite Schrödinger coefficient vectors transform by the dual action in032 equation4.13, so their scalar weights are the reciprocals of the displayed weights in both models; the mismatch and the positive-definite vacuum agreement are unchanged. It is not a claim that an unspecified global theta packet is empty. If one twists both models by the same honest scalar character, both spectra shift equally and the mismatch persists. Choosing different splitting characters can shift one spectrum differently; that change must be recorded and matched globally. The same *names* for splitting characters do not themselves establish equality of the two bare-to-circle corrections. Positive-definite compatibility of the vacuum weight is a necessary local condition, not a sufficient theorem identifying the two periods.

**Consequence for the main gate.** B1 alone removes a coherence obstruction by choosing V^-; B2 shows why this easiest finite matching does not transport the particular032 tensor. The positive-definite neighbor preserves its necessary scalar type and requires one compensating finite place. Thus the next concrete comparison is at the pair {mu,v0}, with the finite models elsewhere fixed.

## 5. A local sign change can destroy a fixed period

### THETA3-B3 (one-dimensional epsilon test)

**Statement.** Fix a nonsplit quadratic local extension E/F, an additive character, delta, a skew-Hermitian line W, splitting character chi_W, and a character alpha of the norm-one torus. Let H_+ and H_- be the two Hermitian lines of opposite determinant class. After identifying their unitary groups with E^1, exactly one of the two theta lifts of alpha to W is nonzero.

**Proof.** Borade–Franzel–Girsch–Yao–Yu–Zelingher, *On tori periods of Weil representations of unitary groups*, Selecta Math31 (2025), article49, Theorem3.5, gives the criterion

    epsilon_(E/F)(chi_W^(-1) alpha_E, psi, delta)
       = epsilon(H) epsilon_delta(W),

where alpha_E(x)=alpha(x/conjugate(x)). The left side is fixed and is a sign. The two right sides are opposite signs. Exactly one equality holds. QED.

This is an immediate application of the cited theorem, not a new epsilon-dichotomy theorem. In the compatible torus seesaw of that paper §3.2.2 and §4.2.2, it is a concrete local test for a period. It proves that a comparison cannot suppress local signs merely because the global L-parameter or a multiplicity dimension is the same. It does not claim that every Bessel period of Alpöge is a torus period of this exact theorem.

Exact primary source: https://link.springer.com/article/10.1007/s00029-025-01047-4 . The compatibility of splitting characters is spelled out in §3.2.1 and §4.2.1, before their seesaw identities. This is the same paper as032 reference[5].

## 6. What positivity gives quantitatively after fixing normalization

### THETA3-B4 (no unnormalized lower bound)

**Statement.** Nonvanishing of the032 theta mixed period, or positivity of a definite period, implies no strictly positive lower bound independent of scalar normalizations of its input and constant determinant-line trivializations.

**Proof.** The theta construction is linear in the finite Schwartz input. If a mixed pairing is B(phi,psi), scaling both inputs by a positive real epsilon multiplies B by epsilon^2. A nonzero value remains nonzero and tends to0. Even if an input is fixed,032 after Lemma4.1 explicitly permits arbitrary nonzero complex choices of constant-line trivialization; their rescaling has the same effect. Therefore a numerical lower bound must name normalizations. QED.

### THETA3-B5 (compact multiplicity gives a normalized selection bound)

**Statement.** Let M be an N-dimensional unitary representation of a compact group H. Normalize Haar measure to mass1, and let P=integral_H rho(h)dh. If the invariant space has dimension r>0, then for every orthonormal basis of M, some r-by-r principal minor of P has determinant at least 1/binomial(N,r). In particular if r=1, the invariant functional of operator norm1 has absolute square at least1/N on some basis vector.

**Proof.** Haar invariance gives P^2=P. Invariance under inversion and unitarity give P^*=P. Its image is M^H, so P is an orthogonal projection of rank r. Choose an N-by-r matrix U with orthonormal columns spanning the image. Then P=UU^*. For each r-element index set I, its principal minor is det(P_I)=det(U_I U_I^*)=|det U_I|^2. Cauchy–Binet gives sum_I |det U_I|^2=det(U^*U)=1. There are binomial(N,r) summands, all nonnegative, so one is at least the reciprocal. For r=1 write P=uu^*, ||u||=1. The invariant functional ell(v)=<v,u> has norm1, and |ell(e_i)|^2=P_ii, proving the final assertion. QED.

**GGP use.** In a compact branching problem take M=pi tensor sigma^vee and H the subgroup, so a multiplicity-one branching statement says r=1. With these fixed Hilbert norms, the result selects data with squared normalized period at least 1/(dim pi dim sigma). It gives no formula for the unnormalized global automorphic period; that needs its Haar/Tamagawa and algebraic-period factors.

### THETA3-B6 (iteration needs an overlap bound)

**Statement.** Positive rank-one projectors at successive stages do not bound their nonzero composite away from zero. If instead T_j are maps of Hilbert spaces with ||T_j v|| >= b_j ||v|| on the image of T_(j-1)...T_1, where b_j>0, then ||T_m...T_1 v|| >= product_j b_j ||v||.

**Proof.** In C^2 let P project to e_1 and Q_theta project to u_theta=(cos theta,sin theta). Both have rank1 and nonzero eigenvalue1. But ||Q_theta P||=|cos theta|, which approaches0 as theta approaches pi/2 and equals0 at pi/2. For the stated positive result, apply the lower bound for T_1 to v, then the bound for T_2 to T_1v, and continue inductively. All the arguments belong to the specified image at each step. Multiplying the inequalities proves the claim. QED.

Thus the “multiplicity won lift by lift” in Alpöge step8 is not by itself a lower bound for the size of a fixed mixed period. A chain may supply additional arithmetic divisibility and overlap information; its actual theorem is needed.

### THETA3-B7 (arithmetic Gram certificate)

**Statement.** Let K be a CM field with real subfield K0 of degree d. Let G be a Hermitian r-by-r matrix with entries in K, positive definite under every embedding sigma:K0->R. Assume D G has algebraic-integer entries for some positive integer D, and tr(G_sigma)<=T_sigma with known T_sigma>0. At a chosen embedding sigma0,

    lambda_min(G_sigma0) >= D^(-r d)
          product_(sigma != sigma0) (r/T_sigma)^r
          ((r-1)/T_sigma0)^(r-1)                  (r>=2).

For r=1 omit the final factor. For every a in C^r, a^*G_sigma0 a is at least the right side times ||a||_2^2.

**Proof.** Let Delta=det G. It lies in K0 because G is Hermitian. The determinant D^r Delta of D G is an algebraic integer in K0. All its real conjugates are positive, so its norm is a positive integer and at least1. Consequently product_sigma det G_sigma>=D^(-r d). At every sigma different from sigma0, positivity and arithmetic–geometric mean give det G_sigma <= (T_sigma/r)^r. Dividing these bounds gives

    det G_sigma0 >= D^(-r d) product_(sigma != sigma0) (r/T_sigma)^r.

Let lambda_1 be the smallest eigenvalue at sigma0. The other r-1 positive eigenvalues have sum at most T_sigma0, so their product is at most (T_sigma0/(r-1))^(r-1). Divide the determinant lower bound by this product upper bound to obtain the displayed inequality. For r=1 the determinant itself is the eigenvalue. The last assertion is the spectral theorem. QED.

**Why all the data matter.** Integrality and total positivity alone do not bound one embedding from below: (3-2 sqrt(2))^m is a totally positive algebraic unit of norm1 tending to0 at the indicated embedding, while the other conjugate tends to infinity. Thus the other-embedding bounds in B7 cannot simply be dropped.

**Application form.** On a finite definite Shimura set, algebraic-valued vectors with rational mass weights give such a Gram matrix once an algebraic coefficient field, denominator D, and all conjugate trace bounds have been supplied. On the ball side, the raw (2,0)-form period is not an integral intersection number merely because H^2(X,Z) exists. One must first identify its normalized algebraic/motivic period coordinates and control the denominators of the correspondences or Hodge maps. B7 is an explicit certificate with these hypotheses, not a claim that the note supplies them for032.

## 7. A transfer formula with the unresolved input isolated

### THETA3-B8 (two-place quantitative transfer, conditional identity)

**Statement.** Suppose the ball and a definite neighbor have been equipped with compatible theta data and normalized period formulas

    I_ball = C_ball L product_(v in S) Z_(ball,v),
    I_def  = C_def  L product_(v in S) Z_(def,v),

where every term is positive real, the same nonzero L-factor occurs, and identical local data make Z_(ball,v)=Z_(def,v) outside T={mu,v0}. If I_def>=b, C_ball/C_def>=c>0, and the two specified local ratios Z_(ball,v)/Z_(def,v)>=a_v>0 for v in T, then

    I_ball >= b c a_mu a_v0.

**Proof.** Divide the two displayed identities. The common L-factor and every factor outside T cancel. Multiplying the remaining three lower bounds with I_def>=b gives the result. QED.

The statement is a proved implication; existence of the two matching formulas for the precise032 input and Alpöge Bessel period remains open here. B1 and B2 reduce a natural positive-definite matching candidate to two places. B3 shows why local nonvanishing must be proved, B5 supplies normalized compact test-data selection, B6 isolates the overlap needed for iterations, and B7 supplies the quantitative arithmetic certificate once algebraic normalizations are known. Parent's compact-place perturbation theorem can then pass a norm bound to the desired mixed period.

## 8. Rallis locator audit

Gan–Qiu–Takeda, *The Regularized Siegel–Weil Formula (The Second Term Identity) and the Rallis Inner Product Formula*, arXiv:1207.4709v3, §11.3, p52, gives the doubling seesaw, including its determinant-character twist. It is an appropriate locator for the general structure. Its §11.4 imposes d(n)<m<=2d(n) before Proposition11.1, and Theorem11.4 repeats that range. For unitary groups d(n)=n, so a lift U(1)->U(3) has (n,m)=(1,3) and lies outside those stated hypotheses. Even Proposition11.1(ii), the convergent-case clause, occurs under the restricted range. Do not cite it as a checked theorem for this specific U(1)->U(3) lift. The larger convergent range has classical formulas, but the exact version and all normalizations have not been supplied in the attachments or proved in this contribution. Parent has fetched BMM Acta2016, §§10–11; those formulas use their own direction/dimension conventions and require the same check.

Primary URL: https://arxiv.org/pdf/1207.4709v3 . The source equation in §11.6 defines the normalized local zeta factor by division by the local standard L-factor; spherical factors still contain the normalizing Euler product d_v(s,chi_V), so one must not silently set every normalized unramified factor to1 without absorbing that product into C or L.

## 9. Approaches attempted and exact state

1. **Direct statement extraction from Alpöge map:** exhausted attached quotations; Bessel functional and local matching definitions absent. This leaves source-identification gate B0.
2. **Literal deformation in032:** V and its active signature remain fixed; varying P at compact places cannot change signature. It proves a same-signature mixed pairing, not a new definite Bessel equality.
3. **Keep all finite Hermitian data, choose negative-definite rank3:** global coherence succeeds (B1), but prescribed bare cohomological scalar tensor cannot match (B2).
4. **Use positive-definite rank3 instead:** necessary scalar type succeeds; coherence reduces to one finite invariant flip (B1–B2). Remaining gate is explicit matching at mu and v0, with fixed source character/splittings and nonzero testvectors.
5. **Infer a bound from determinant positivity/interlacing alone:** refuted by B4 and B6 for arbitrary normalizations or fixed composite data; B5 and B7 give precise positive substitutes with complete proofs.
6. **Invoke a general Rallis theorem immediately:** checked range excludes the naive U1->U3 citation. B8 is the correct conditional transfer implication until an applicable normalized formula and equality with the Alpöge period are established.

No unproved equality is being represented as a theorem. The original sketch1.7 remains undecided, with a narrowed finite and archimedean matching problem and a missing exact source functional.

## 10. Later source recovery: exact archive definitions obtained from a public mirror

The preceding attachment-only audit B0 remains correct as a statement about the supplied ZIP, but its missing-source gate has now been reduced. At the parent's request this agent fetched the exact named files from `https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/main/src/`, into `work/alpoge_mirror/`. The repository describes itself as a byte-for-byte mirror of Alpöge's published archive. This secondary provenance is explicitly retained; no complete comparison with the primary archive and no Lean build was performed by this agent. The fetched `Main.lean` and `Statements.lean` are byte-for-byte equal to the user's attachments. Their SHA256 values are respectively `017645ca448f2fd1f6fd5c4c2cb2c6e96e472725be13f6e180ca6e1574360939` and `79ef7ca776e42abe1f46caee13ea09bd19f1e2d0b1620d8d5d200258f33b47bf`.

### Exact local Bessel functional

`Formalism/PeriodIntegrals/BesselPeriodGGP.lean` defines a real local nonvanishing proposition, rather than the global period in step12. Its ambient Hermitian matrix is `Hpk k r` from `Formalism/FormalDegreeBessel/StatementG.lean`: it is a sum of r hyperbolic planes and a block of signature(k,1), hence signature(k+r,r+1). The subgroup `UWset k r z` fixes the hyperbolic basis vectors and a negative vector z, and is compact U(k). The unipotent `Nset k r` has the generic character `psiGen`.

The displayed integral in the proposition is

    integral_(h in U(W_z), n in N)
      <sigma(x0)w, sigma(h n)sigma(x)w>
      conjugate(psiGen(n)) pi(h)^(-1) dh dn.

It is operator-valued in the finite-dimensional pi-space. Its hypotheses specify a discrete-series sigma of Harish-Chandra parameter `lam48`, a compact pi of parameter u, a lowest-K-type unit vector w, interlacing, and half-integral weight differences. It asserts the existence of x,x0 making the integral nonzero. It does *not* assert that every period has value0 or1. `GapBig` appears in a separate `RealPlaceNumericalSetting`, not among the assumptions of the actual `BesselPeriodGGP` definition.

### THETA3-B9 (an exact normalized local period for the canonical wedge)

**Statement.** Specialize the archive's local Bessel functional to k=2,r=0,z=e_3, and use probability Haar measures. Let sigma be a unitary representation of U(2,1) containing a unit vector w with

    sigma(diag(A,d))w = det(A)d^(-2)w,
    A in U(2), d in U(1).

Let pi(diag(A,1))=det(A) on C. Then at x=x0=1 the archive's Bessel integral equals1. This vector type is the right-regular automorphic coefficient type of a holomorphic canonical2-form on a ball quotient. The numerical parameters

    lambda=(1,0,-1), v=(1), b=(0,1), u=(3/2,1/2), epsilon=(+,+,-)

satisfy the archive's interlacing, Harish-Chandra integrality, and half-integral difference conditions; its lowest K-weight is(1,1;-2), and the compact pi highest weight is(1,1).

**Proof.** For r=0, the `Nset` matrix equations force every matrix entry to equal that of the identity, so N={1}; its character is1. For z=e_3, a unitary matrix fixing z preserves its positive orthogonal complement, so `UWset` is exactly diag(U(2),1). In the convention where the Hermitian inner product is linear in the second variable,

    <w,sigma(diag(A,1))w> = det(A)||w||^2 = det(A).

Multiplication by pi(diag(A,1))^(-1) cancels this scalar. The integrand is identically1 and both measures have mass1, proving the claimed value. Compactness gives absolute convergence.

For the geometry, at the standard negative line o the tangent space is Hom(L,Q). The derivative of k=diag(A,d) is A/d; on a tangent2-vector its determinant is det(A)d^(-2). If xi is a nonzero holomorphic2-form on a compact quotient, define its automorphic coefficient by

    f_xi(g)=(g^*xi)_o(e_1,e_2)

for a fixed tangent2-frame at o. Left lattice invariance follows from that of xi. Pullback under gk gives

    f_xi(gk)=det(A)d^(-2)f_xi(g).

The right-regular representation therefore has the asserted K-character. Its L2 norm is finite and nonzero on the compact quotient; normalize it to obtain w. The character is trivial on the center of U(2,1), so the same coefficient type can be regarded on the U(2,1) extension of the projective special-unitary action used in032. This avoids confusing the coefficient representation with the dual convention on the canonical-bundle fibre.

Finally the archive defines rho_C=(1/2,-1/2,0) and rho_N=(1/2,1/2,-1) for epsilon=(+,+,-), giving lambda+rho_N-rho_C=(1,1,-2). For compact U(2), rho_N=0 and rho_C=(1/2,-1/2), so u-rho_C=(1,1). The interlacing inequalities are 3/2>1>1/2>0, while lambda=(v,-b0,-b1) is strictly decreasing. Each u_i-lambda_j is an integer plus1/2; lambda_j-1 and u_i-1/2 are integers, as required. QED.

**Status and scope.** This directly evaluates the actual archive-defined local functional on the relevant canonical coefficient type; it does not require the general archive theorem. It does not by itself prove that an arbitrary automorphic cyclic representation is irreducible discrete series, although the numerical lowest K-type matches the canonical holomorphic discrete-series parameter. If the full `BesselPeriodGGP` proposition is to be invoked rather than this direct evaluation, its `IsDSHpk` hypothesis still needs the appropriate representation-theoretic identification. No global Bessel or Rallis period is set equal to1. This result supplies an exact archimedean compact normalization at the ball place, while the global factor and finite matching remain explicit gates.

### THETA3-B10 (the actual global matching range)

**Source reading.** The mirror's `Development/AbelianVarietyTheory/BlockTheory/DivisorBase/WeilTensorModels.lean` defines `LocalMatching` at line581 and `ThetaIntegralsAgree` at line585. The source models two theta integrals from U(V), dimension a, and U(V'), dimension a', to U(W), dimension a+a'. The matching quotients have compatible real Lie/compact actions and compatible finite local actions. `IsConst` at line491 is the exact relation I_V(Phi)=c I_V'(Phi') for matched data; `OneConst` at line503 requires a unique c and c nonzero. `StepAlpha` and `StepBeta` at lines571 and559 give recursive scalar relations involving partial Hecke L-values and explicitly defined local epsilon/Gauss factors.

The hypotheses `Geo.IsGood`, lines360–370, require

    a'<a;  a+a' even;
    2(p+q)+1 < floor((a-a')/2);
    2(p+q)+1 < a';
    signatures V=(a-p,p), V'=(q,a'-q), W=(a+a'-p-q,p+q).

Moreover `Spc.IsHerm` and `Spc.IsSkew`, lines182–200, impose their stated signatures at *every* real place, and `Base.IsGood` includes CM/Galois and unramified-integral-extension conditions. These are real restrictions, not absent metadata.

**Deduction.** The rank3 one-active-place032 configuration does not directly satisfy this particular global matching theorem. Even ignoring the other-place signature mismatch, p=1,q=0 forces a'>3 and (a-a')/2>3; with the parity condition, the smallest numerical pair is(a,a')=(12,4). This follows because a'>=4 and the positive even difference a-a' must be at least8. Thus a proposed use of this statement must stabilize the rank and deal with all archimedean signatures, then prove descent or an algebraic extraction to the original surface. Merely assigning a=3 to the theorem fails its numerical hypotheses.

The recovery changes B0's attachment-only missing-data gate to an explicit global representation/rank/signature matching gate. It provides a genuine local answer B9 but does not complete sketch1.7.

## 11. A direct global bridge through a definite subgroup

The inner-form comparison B1–B3 is one route, not a prerequisite for every comparison. There is a more direct global construction that keeps the rank3 ball group and uses a totally definite rank2 subgroup. Its period is a genuine unitary GGP/Bessel period. It is important to distinguish this restriction period from the full norm of a form on the ball. The finite-frame identity A5, developed independently by the theta agent, supplies a further exact comparison of those norms after an explicit positive operator correction.

### THETA3-B11 (orthogonal restriction seesaw, with every character retained)

**Statement.** Let E/F be CM, let V=V_H perpendicular-sum L be a Hermitian space with L a line, and put G=U(V), H=U(V_H), embedded in G by fixing L. Let W be a skew-Hermitian source, T=U(W). Assume [H]=H(F)\\H(A_F) and [T] are compact, or more generally assume the absolute convergence of all the displayed theta sums and integrals. Fix an additive character and compatible global splittings so that the oscillator representation for V restricted to H times U(L) times T is the tensor product of those for V_H and L. In particular the splitting character attached to V is the product of those attached to V_H and L; the source splitting choices also agree under this tensor identification.

Choose a finite sum of compatible Schwartz tensors

    Phi = sum_a Phi_(H,a) tensor Phi_(L,a).

For a unitary automorphic character eta of T, define

    F_eta(g) = integral_[T] theta_V(g,t;Phi) eta(t)^(-1) dt.

For any continuous automorphic test function e on [H], define the global Bessel/GGP period and the reverse definite theta lift by

    B_e(F_eta) = integral_[H] F_eta(h) conjugate(e(h)) dh,
    Theta_(H->T)(e;Phi_H)(t)
        = integral_[H] theta_(V_H)(h,t;Phi_H) conjugate(e(h)) dh.

Then the exact restriction seesaw is

    B_e(F_eta)
      = sum_a integral_[T] Theta_(H->T)(e;Phi_(H,a))(t)
              theta_L(1,t;Phi_(L,a)) eta(t)^(-1) dt.             (B11)

The Haar measures are exactly the ones displayed on both sides. No unrecorded scalar is introduced. This identity applies to a polynomial Fock coefficient of a theta differential form after its coefficient vector and its orthogonal tensor decomposition have been identified with Phi. That identification is part of the input; the identity does not identify bundle-valued forms merely from their degree or group name.

**Proof.** In a polarization compatible with the orthogonal decomposition, the rational lattice indexing the theta series is the direct sum of the rational lattices for V_H and L. By the stipulated tensor identity for the oscillator action, for each pure tensor the summand at (x_H,x_L) is the product of the two corresponding summands. Absolute convergence allows separation of the two sums. Hence

    theta_V((h,1),t;Phi_(H,a) tensor Phi_(L,a))
       = theta_(V_H)(h,t;Phi_(H,a)) theta_L(1,t;Phi_(L,a)).

Add this identity over the finite index set a, multiply by eta(t)^(-1) conjugate(e(h)), and integrate over [H] times [T]. Absolute convergence permits Fubini. The factor involving L and eta does not depend on h, so the inner h integral is precisely Theta_(H->T). This proves (B11). In the compact case, continuity of e and uniform convergence of the theta series on compact representative sets supply the required absolute integrability. QED.

**Exact normalization and source comparison.** In the recovered archive the orthogonal tensor rule is stated by `GlobalTheory.T.thetaTensorRule_orthogonalSum_source` in `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaTensorRuleOrthogonalSumSourceStatement.lean`; its actual proof is in the same path without `Statement`. The restriction is packaged as `TensorSource` in `BlockTheory/TwistedDiscreteSeries/ConjugateAdjointDagger.lean`. The adjacent target-sum rule is used in `LastSeeSawThetaIdentity.lean`. These actual source declarations provide the correct comparison object; the statement above proves the needed classical kernel identity directly and retains its exact splitting hypothesis.

The actual recovered archive uses a bilinear integrand phi(h) f(n emb_A(h)) conjugate(psi_Bes(n)). Thus put phi=conjugate(e), and put G=eta^(-1) in its bilinear theta lift. The exact declaration is in `Definitions/TwistedInnerProducts/WittSmallGroupEmbeddingMemPointwiseStabilizerIso.lean`, lines157–181.

**What (B11) does and does not establish.** It converts a genuine global H period on the ball group into a pairing involving a definite theta lift. The source character eta remains on the right. Thus it does not by itself prove the character cancellation stated informally in Alpöge step12. Such cancellation requires the additional compatible iterated data and normalized relation theorem described below. It also does not say that the full ball norm equals the norm of its restriction to [H].

### THETA3-B12 (a nonzero canonical form gives a definite Bessel coefficient, with a finite mass bound)

**Statement.** Let X be a compact smooth congruence ball surface obtained from a rank3 Hermitian V with signature(2,1) at one real place mu and positive definite at every other real place. Let xi be a nonzero holomorphic2-form on X. Then there is an E-rational negative line L in V_mu such that H=U(L-perp) is totally definite of rank2 and a finite-level automorphic test function e on [H] for which

    integral_[H] f_xi(h) conjugate(e(h)) dh != 0,

where f_xi is the scalar automorphic canonical coefficient based at the point L. This is evaluation of a canonical-bundle coefficient along a finite Shimura set, not pullback of H^2(X) to a point.

More precisely, take probability measure on [H], let K_H be a compact open finite level fixing f_xi, and let R be the finite-dimensional space of scalar automorphic functions with that finite level and the same one-dimensional H_infinity type as f_xi. Put N_H=dim R. If m_0 is the positive mass of the identity double coset and b=|f_xi(1)|, then for any orthonormal basis (e_j)_(j=1..N_H) of R,

    sum_j |B_(e_j)(f_xi)|^2 = ||f_xi|_[H]||_2^2 >= m_0 b^2,
    max_j |B_(e_j)(f_xi)|^2 >= m_0 b^2/N_H.              (B12)

The basis can be chosen inside automorphic spectral summands, so these are global period coefficients against definite automorphic forms. In particular the following conditions are equivalent: xi is nonzero; integral_X xi wedge conjugate(xi)>0 with the complex orientation; some rational definite subgroup H and some such global Bessel coefficient are nonzero.

**Proof.** The nonzero locus of xi is a nonempty open subset of the ball. E-rational vectors are dense in the active complex vector space: in an E-basis of V, the image of E in C contains Q plus Q times a nonreal element, and this is dense in C. Equivalently one may use weak approximation simultaneously at all infinite places. Negativity and nonvanishing are open conditions, so there is a nonzero z in V(E) whose line belongs to the nonzero locus and has h_mu(z,z)<0. At every other real place the form on V is positive definite, so h_tau(z,z)>0 automatically. The orthogonal complement V_H=L-perp therefore has signature(2,0) at every real place. Thus H is totally definite and [H] is compact.

Base the automorphic realization of the canonical bundle at L, choose a nonzero tangent2-frame there, and set f_xi(g)=(g^*xi)_L(frame). As in B9, at the active compact subgroup diag(A,d) its right character is det(A)d^(-2). On H_infinity, which fixes L pointwise, this restricts to det(A); at the other real factors the scalar coefficient has the prescribed compact type, trivial for the usual trivial coefficient system. In particular its absolute value is constant on the right H_infinity orbit. Its value at identity is nonzero by the choice of L. Adelic realization at the given congruence level supplies a compact open K_H fixing it on the right.

Because H is totally definite, the double coset set H(F)\\H(A_F)/(H_infinity K_H) is finite. On each double coset, the scalar one-dimensional infinity type determines a function by one complex value, subject only to its finite stabilizer condition. Consequently R is finite-dimensional. With Haar measure on [H] normalized to total1, let m_i>0 be the masses of its finitely many double cosets. The identity coset contributes exactly m_0|f_xi(1)|^2 to the integral of |f_xi|^2; all remaining contributions are nonnegative. This proves the lower bound on the restriction norm. If Haar on H_infinity and K_H is normalized consistently, m_i is proportional to the reciprocal of the finite stabilizer order; the proportionality is fixed by sum_i m_i=1. At neat level all these stabilizers are trivial and all masses are equal.

Expand the restriction in an orthonormal basis of R. Parseval gives the displayed exact sum of squares, and at least one of N_H terms is at least the average. A unitary automorphic spectral decomposition of the compact quotient refines this finite-dimensional space into the relevant finite-level, fixed-type pieces, permitting an orthonormal basis of automorphic spectral test vectors. No algebraic-value claim about their normalization is needed for this argument.

For the equivalence, the forward implication has just been proved. Conversely a nonzero period forces the coefficient f_xi, hence xi, to be nonzero. In complex dimension2, writing xi=a dz1 wedge dz2 gives xi wedge conjugate(xi)=4|a|^2 dx1 dy1 dx2 dy2 in the standard positive orientation. Therefore its integral is positive exactly when xi is nonzero. QED.

**Quantified rational selection.** Suppose a chosen local unit-frame coefficient has absolute value b_0>0 at a point p, a certified Lipschitz constant L_xi on a neighborhood, and a negative Hermitian margin there. Choose a rational point within a radius no larger than b_0/(2L_xi) (omit this restriction if L_xi=0) and within the radius preserving the negative margin. Then b>=b_0/2, so B12 gives a coefficient of squared size at least m_0 b_0^2/(4N_H). Q3's Minkowski-coordinate rounding supplies such a rational point with an explicit denominator once the coordinate matrix, margin and radius are supplied. The finite class mass m_0 and dimension N_H must still be computed or bounded at the resulting level. This is a fully specified certificate, not a universal numerical constant independent of level or analytic normalization.

**Comparison with the desired mixed period.** For two restrictions in the same R, Parseval also gives

    integral_[H] f conjugate(f') = sum_j B_(e_j)(f) conjugate(B_(e_j)(f')).

This remains a restriction identity. A5 obtains the full ball inner product by finitely many such restrictions and the positive inverse frame operator Q^(-1). Whether that correction is algebraic, and whether it equals the archive's particular iterated normalization, remain additional questions.

## 12. Exact recovered step12: a common normalized functional

### THETA3-B13 (relation transfer gives a character-independent scalar)

**Archive witness.** The commit-pinned source `Development/AbelianVarietyTheory/Definitions/LatticeFrames/ValLastX.lean` defines the actual family seesaw. `Comm` (lines28–57) fixes spaces V_j, their discrete-series models, definite spaces X_j, measures, Bessel/Jacobi decompositions, final T and an orthogonal decomposition X_m=T perpendicular-sum L_z. `Tup` (79–113) supplies the varying Weil representations, finite translation combinations, row functions and normalizing constants. The common real data are separate from the varying tuple; the condition `RealEq` (182–184) equates the real Weil actions for all tuples.

`Tup.perF` (119–120) is a finite sum of Bessel periods of right translates. `per` (122–123) inserts a row function and an automorphic realization. `perT` (137–138) is the final definite restriction period. `up` (166–167) iterates two definite theta operators with intermediate S, and `dn` (169–170) composes the reverse automorphic lift maps. The products are

    cTop(n) = product_(i=0..n-1)(cV(2i)cK(2i)cK(2i+1)) cP,
    cBot = product_(j=0..m-1)cI(j).

`LawsX` (212–221) contains the common-data validity, tuple validity, finite support, common real action, double-step and last-step integral laws, definite kernel reduction, final period factorization, and row covariance. The actual proof witness is `GlobalTheory.SeeSaw.mainX_of_lawsX`, in `Proofs/DecoratedLatticeProofs/SeesawTransportRelationsOfFamilyLaws.lean`, lines25–37. Its signature is CuspRapidDecay -> HarishChandraModules -> LawsX t -> MainX t. The wrapper `GlobalTheory.T.seesawTransportRelations_of_familyLaws` is in the matching `Statement.lean`, line12. This is a source-body reading, not a Lean compilation or complete dependency audit.

`MainX` (ValLastX.lean lines244–251) says that for every finite family of tuples, input columns and terminal automorphic vectors, every scalar relation among

    A_s = cTop_s(n+1) tail_s(up_s(n+1) psi_s,F_s)

implies the same scalar relation among, for every fixed y,v,

    B_s(y,v) = cBot_s per_s(psi_s, dn_s(2n+1) ioT_s(F_s);y,v).

Here m=2n+2 and the permitted columns lie in the specified Ram subspaces. Thus the exact recovered independence is a shared normalized functional on this family, not a claim that arbitrary unnormalized Bessel periods are equal to1 or are unchanged when characters vary freely.

**Elementary consequence and proof.** For any family of pairs (A_s,B_s) of complex numbers, if every finitely supported relation sum alpha_s A_s=0 implies sum alpha_s B_s=0, then there is a scalar a such that B_s=a A_s for every s. If all A_s vanish, the one-term relations force all B_s=0 and a=0 works. Otherwise choose s_0 with A_(s_0)!=0 and put a=B_(s_0)/A_(s_0). For each s the two-term relation A_(s_0) A_s - A_s A_(s_0)=0 forces A_(s_0) B_s - A_s B_(s_0)=0. Division proves B_s=a A_s. The scalar is unique when some A_s is nonzero. This checks the complete logical inference from MainX and proves the claimed common normalized scalar at each fixed y,v. QED.

**Concrete rank/signature gate, distinct from B10.** The abstract `Comm`/`BesAt` framework allows more flexible signatures. `DefSp.Is` in `Definitions/LatticeFrames/JointSmooth.lean` lines56–62 requires compactness and a Cartan involution equal to plus or minus identity at every real place, hence definiteness, but does not itself require the same sign at every place. `BesAt` (107–115) is an orthogonal line plus a hyperbolic decomposition, so its rank-zero Bessel specialization contains the pair U(2,1),U(2) at the active real place. However the *particular arithmetic tower construction* in `ChainParSucc.lean` lines56–60 requires `s.V.sig tau = sigYD D.R j` at every embedding tau, independently of tau. `ExistsDatOfTower.lean` lines151–171 constructs its Bessel step using a globally negative line nLine, with signature(0,1) at every real place. Thus that constructed tower is not immediately the one-active-place032 V when F has more than one real place. This is now an exact instantiation gate, not a missing-source gate.

**Orientation resolved.** `Definitions/TwistedInnerProducts/WittSmallGroupEmbeddingMemPointwiseStabilizerIso.lean` lines176–181 defines the integrand as phi(h) f(n emb_A(h)) times conjugate(psi_Bes(n)), and integrates over the displayed fundamental domains. Its `liftS_apply` at line163 integrates theta(g,h)G(h), with no conjugation on G. Therefore B11 matches the archive exactly by taking phi=conjugate(e) and G=eta^(-1); no orientation ambiguity remains.

**Shimura-datum precision.** The H in B11/B12 fixes the chosen line pointwise. A standard central lift of the Shimura cocharacter may factor through U(V_H) times U(L), rather than H alone. The argument uses the finite definite adelic module and evaluation at its rational negative-line point; it does not assert an unspecified morphism of Shimura data H->G.
