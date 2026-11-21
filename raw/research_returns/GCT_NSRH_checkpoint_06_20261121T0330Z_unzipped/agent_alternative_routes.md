# Alternative routes: ordinary orbit schemes and ambient pure categories

Date: 2026-11-21 Europe/Berlin. Run/author/checker: `/root/rectangular_and_theta`, GPT-6 Astra Pro, inherited effort not exposed. Requested follow-up: test ordinary commutative geometry and restriction from standard quantum/Hecke geometry before declaring the main transfer unavailable. Read together with `MAIN_PROOF_DRAFT.md` (F1–F5) and the proofs T-PROJ, T-PATH, T-BASIS in `agent_rectangular_theta.md`.

## Outcome

Two constructive routes were pursued. Ordinary orbit closures certainly have commutative models over Z and ordinary intersection-cohomology purity over finite fields; this does not require a new RH. But their coherent graded coordinate-ring multiplicities are not their intersection-cohomology dimensions. A concrete family of polarized projective lines proves that the latter data cannot recover the former without additional input.

The ambient-standard-geometry route has a sharper obstruction, already visible in the actual rank-one nonstandard Hecke inclusion. Its nonnegative ambient KL cone meets the nonstandard algebra only in scalars. Therefore merely taking an effective additive subcategory of the usual tensor-product Hecke category cannot realize the full nonstandard algebra through that inclusion. This is a refutation of that specific inheritance route, not of a different categorical realization or of the signed positivity conjectures in GCT VIII. The same rank-one algebra has positive multiplication internally, showing precisely that the missing issue is the effective structure/character map, not algebraic nonnegativity itself.

## A-ORBIT: constructive spreading of the commutative orbit closure

Let W_Z be a finite free Z-module and f∈W_Z an integral polynomial tensor, for instance det_n or the padded permanent. Let G_Z=GL_N,Z act on W_Z through a representation of group schemes. The orbit morphism G_Z→W_Z gives a homomorphism

`Z[W_Z] → Z[G_Z]`.

Let I be its kernel and define X_Z=Spec(Z[W_Z]/I). This is a finite-type affine scheme because the source polynomial algebra is noetherian. Since C is flat over Z, taking kernels commutes with base change to C. Thus X_C is the scheme-theoretic image of the complex orbit morphism. In this setting Z[G_Z] is reduced, so its kernel is radical; X_C is the usual reduced orbit closure. The same construction after projectivization gives a projective model for the projective orbit closure.

**Limited conclusion.** There is no obstacle to applying ordinary étale/constructible sheaf theory to these commutative schemes. Finite-field reductions admit geometric Frobenius and intersection complexes. For an equidimensional geometrically irreducible projective reduction X/F_q of dimension d, with smooth dense open j:U→X, the perverse intersection complex `IC_X=j_!* Q_l[d]` is pure of weight d; hence `IH^j(X)=H^{j−d}(X_bar,IC_X)` is pure of weight j. This is a cited standard consequence of BBD 5.3.2 (including its second proof for arbitrary open embeddings) and the proper direct-image weight estimates BBD 5.1.14. It is not a newly proved result here. The relevant statements were read in the root's supplied primary-source text `primary_sources/BBD.txt`.

**Base-change boundary.** The assertion just proved about the complex fibre uses flat base change. It does not assert that the fibre X_Fp is the orbit closure of f_Fp for every p: formation of a scheme-theoretic image need not commute with arbitrary nonflat base change. A chosen good-prime/spreading statement must be proved separately before identifying those objects. Ordinary étale theory applies to the resulting finite-field scheme either way.

**Where this route stops.** The GCT coefficients are coefficients of the graded representation `[C[X]_d]`, not the graded dimensions of IH^*(X). Projectivization relates graded coordinate-ring pieces to coherent global sections of a polarization only with the required saturation hypotheses or in the appropriate sufficiently large degrees; no equality in every degree is assumed here. The data of the line bundle, its tensor powers, its G-linearization, and its equivariant coherent sections have not been replaced by an identified constructible IC multiplicity. Purity of the latter is therefore a valid theorem about an existing geometric object, but not yet a theorem about the desired coefficient.

The Hilbert/Quot representability in FGA constructs parameter schemes for coherent quotients and fixed Hilbert polynomials; it does not identify the universal coherent sheaf with a constructible IC complex or make the relevant strata affine-paved. In particular, representing the functor of objects is different from proving that a desired multiplicity is the dimension of a pure even cohomology group of that parameter scheme.

## A-HILB: exact mismatch between ordinary Weil cohomology and coherent Hilbert data

**Proposition.** The Frobenius-graded ordinary or intersection cohomology of a smooth projective scheme does not determine its polarized coherent Hilbert function. It also does not determine a G-linearized coherent character, even in a trivial geometric family.

**Proof of the first assertion.** Fix X=P¹_Fq. For each positive integer r put L_r=O_X(r). For d≥0, the degree-rd homogeneous monomials in two variables form a basis of H⁰(X,L_r^d), hence

`dim H⁰(X,L_r^d)=rd+1`.

The scheme X is the same for all r. Its ordinary/intersection cohomology is Q_l in degree 0 and Q_l(−1) in degree 2, zero in other degrees, with Frobenius eigenvalues 1 and q. Thus all r give identical pure Weil-cohomology data, while the Hilbert functions vary with r. This proves non-determination. The cohomology of P¹ used here is the standard projective bundle formula; the coherent dimension formula was checked directly by the displayed monomial basis.

**Proof of the character assertion.** Let G=G_m and X=Spec F_q, with the trivial G-action. For any integer r, put a G-linearization of weight r on the one-dimensional vector bundle O_X. Its dth tensor power has coherent character z^(rd). The underlying scheme and its ordinary Weil cohomology remain the same one-dimensional weight-zero space. Thus forgetting the equivariant coherent linearization loses the character even when the polarization and underlying geometry are fixed. No claim is made that an enriched equivariant realization carrying additional Chern/character data is impossible; the example proves that that additional data must actually be provided. □

**Constructive attempt using section schemes.** One can form the affine scheme associated with the vector space M_d=H⁰(X,L^d); its F_q-points number q^(dim M_d). If a characteristic-zero multiplicity space of dimension m has already been constructed and spread out as a finite free module, the same construction gives an affine space of dimension m on its finite-field fibres. Formation of isotypic spaces is not being asserted to commute automatically with reduction modulo p. Its top compact-support cohomology is a Tate line of weight twice that dimension. This produces pure geometry only after the multiplicity space and its dimension have been encoded in the construction. It yields no formula for that dimension and no canonical combinatorial indexing set; the required information is already the unknown rank. This is the same exact limitation isolated by T-PROJ for Gram determinants.

**Grothendieck dictionary.** The coherent classes `[L_r^d]` and their pushforwards live in K_0 and its Euler-characteristic operations; their tensor powers and λ-operations retain r. The ordinary constant-sheaf realization of X forgets that input. FGA's Hilbert/Quot schemes remember a chosen coherent quotient and Hilbert polynomial, while SGA4/5 constructible cohomology has a different coefficient object. A comparison theorem, not the shared use of the word cohomology, is required. This example does not assert failure of Riemann–Roch: Riemann–Roch explicitly uses ch(L_r^d), which is exactly the extra datum varying here.

## A-SUB: the precise purity that ambient inheritance really supplies

**Lemma.** Let V be a finite-dimensional algebraic Weil module over a number field, pure of weight w in every complex embedding. Every Frobenius-stable subquotient W of V is pure of weight w. More generally, a Frobenius-stable subquotient of End(V), with Frobenius acting by conjugation, is pure of weight 0.

**Proof.** In a basis adapted to a Frobenius-stable subspace, the Frobenius matrix is block upper triangular. Its characteristic polynomial is the product of those on the subspace and quotient. Hence all eigenvalues of every subquotient are among those of V, counted with no greater multiplicity. This proves the first statement in every embedding. Eigenvalues on End(V)=V⊗V* are the ratios α/β of eigenvalues on V. Both numerator and denominator have absolute value q^(w/2), so every ratio has absolute value 1; apply the first statement to End(V). Semisimplicity is unnecessary. □

**Application boundary.** If the nonstandard objects and operations were already realized as Frobenius-stable subquotients in a standard pure realization, no new eigenvalue estimate would be needed for those subquotients. The unspecified items would instead be the realization, the Frobenius-stability proof, the identification of the quantum parameter with the grading/weights, and the effective basis/convolution compatibility. Giving a finite-dimensional vector space a trivial Frobenius by decree proves only an artificial weight-zero assertion and supplies none of these identifications.

For perverse sheaves a corresponding true statement is BBD Proposition 5.3.1: perverse subquotients preserve the appropriate weight bounds. But an algebraic subalgebra of a Grothendieck ring is not itself automatically a subcategory of the perverse heart. The next computation proves that this distinction is essential for the actual nonstandard inclusion.

## A-AMBIENT: rank-one obstruction to inheriting the ambient positive KL category

### Exact source and normalization

GCT IV, arXiv:cs/0703110v4, §1.4 equation (8) and Definition 11.1, equation (93), defines

`P_s=C'_s⊗C'_s+C_s⊗C_s`

inside H_r⊗H_r. The primary PDF was opened and these numbered formulas checked. In §3.1 the conventional rank-one definitions are `C'_s=T_s+v^−1`, `C_s=T_s−v`, with `(T_s−v)(T_s+v^−1)=0`. The later printed §11.1 swaps v and v^−1 in those expressions while retaining the idempotent assertion. The following proof fixes the earlier consistent normalization and is independent of that editorial slip. Write `δ=v+v^−1`, `c=C'_s`, so `c²=δc` and `C_s=c−δ`.

### Proposition and proof

Let A=Z[v,v^−1], let H=A1⊕Ac with c²=δc, and equip H⊗_A H with the positive ambient KL cone

`C_+ = A_+·(1⊗1) + A_+·(c⊗1) + A_+·(1⊗c) + A_+·(c⊗c)`,

where A_+=N[v,v^−1]. Put `P=c⊗c+(c−δ)⊗(c−δ)` and B=A[P]⊂H⊗H. Then:

1. `P²=δ²P`, and B is free with basis {1,P}.
2. `B∩C_+=A_+·1`.
3. Consequently B has no A-basis all of whose elements are nonnegative in the ambient tensor-product positive KL basis. In contrast, its internal basis {1,P} has nonnegative multiplication constants.

**Proof.** Put b=c−δ. Then cb=c²−δc=0, and b²=c²−2δc+δ²=−δb. Hence

`P²=(c⊗c)²+(b⊗b)²=δ²(c⊗c)+δ²(b⊗b)=δ²P`;

the cross terms vanish. Therefore every polynomial in P lies in A1+AP. Expanding P in the ambient basis gives

`P=δ²·1−δ(c⊗1+1⊗c)+2c⊗c`.

Since the coefficient of c⊗c is 2, P and 1 are A-linearly independent, so B=A1⊕AP. For x=a+bP the four ambient coefficients are

`a+δ²b, −δb, −δb, 2b`.

If x∈C_+, then 2b∈A_+ forces every coefficient of b to be nonnegative. If b≠0, δb is a nonzero Laurent polynomial with nonnegative coefficients, so −δb has a negative coefficient. This contradicts x∈C_+. Thus b=0, and then a∈A_+. The converse inclusion is immediate. This proves the cone equality. All ambient-positive vectors in B therefore span at most its rank-one scalar summand, so no such basis exists. Internally 1 is the unit and P²=δ²P, with `δ²=v²+2+v^−2∈A_+`; this proves the last claim. □

The argument also works with Q[v,v^−1] and nonnegative rational coefficients. It is about Laurent-polynomial cones; it does not silently extend to arbitrary rational functions with a different positivity convention.

### Exact categorical consequence

Suppose a graded additive category C has a split Grothendieck ring identified with H⊗H, with classes of its indecomposable objects corresponding to the ambient KL basis and grading shifts corresponding to v. Every actual finite direct sum of shifted indecomposables then has class in C_+. Any additive graded subcategory whose objects map into B has all its object classes in B∩C_+=A_+1. Its split Grothendieck image is therefore contained in A1 and cannot be the rank-two algebra B.

This proves that taking an effective additive subcategory of the ordinary tensor-product KL category, with the fixed nonstandard inclusion as its character map, cannot directly realize the full nonstandard algebra. Passing to arbitrary derived complexes permits virtual signs and evades that obstruction, but loses the automatic effective-simple-object interpretation; one then needs a new heart, grading/sign normalization, or other mechanism. This is exactly the missing structure that a pure-eigenvalue argument alone cannot supply.

### Scope and relation to GCT VIII

This is not a counterexample to GCT VIII 3.4, which explicitly allows signed factors and uses prescribed normalizations. It does not say that P must be one of VIII's canonical-basis elements. The stronger cone statement instead addresses *every* possible basis contained in this rank-two algebra under the fixed inclusion and the fixed ambient nonnegative KL cone. It refutes a specific proposed shortcut: deriving the required effective nonstandard basis merely by restriction from the already positive ambient KL basis.

The example also does not preclude a different positive realization. Indeed the internal multiplication table is already positive. Thus “all routes fail” would be an unjustified conclusion; the exact conclusion is that this natural inherited-effective-category route fails and must be replaced by additional categorical data.

## Check events

- MAIN-F1–F5: **used and rechecked in this run** — read the full root draft, checked that the alternative routes do not supply its S1/S2 trace identification or spectral parity. No claim of an independent complete re-proof of F1–F5 is made in this follow-up.
- A-ORBIT: **targeted proof check** — checked kernel construction, finite type, reduced image and flat C-base-change; explicitly excluded arbitrary finite-field fibre identification. Standard IC purity is cited, not re-proved.
- A-HILB: **targeted proof check** — read full two examples and verified monomial count rd+1 and character z^(rd); same underlying Frobenius cohomology in each family. It refutes determination from the specified underlying data only.
- A-SUB: **targeted proof check** — read full block-triangular characteristic-polynomial proof and ratio argument; no semisimplicity assumption needed.
- A-AMBIENT: **targeted proof check** — checked normalization against §3.1, read source equations (8)/(93), expanded P, checked cb=0 and P², checked free rank two and positive-cone intersection argument. Exact symbolic argument, no numerical extrapolation.
- SRC-BBD-WEIGHTS: **used and rechecked in this run** — read BBD 5.3.1–5.3.3 in `primary_sources/BBD.txt`; used ordinary proper-pushforward weight formalism as cited background.

All proofs in this report were read end-to-end after writing. The root should record its independent check separately.
