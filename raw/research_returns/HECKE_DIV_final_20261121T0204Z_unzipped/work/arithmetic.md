# Arithmetic route and independent supplier audit

Run: HECKE_DIV_20261121. Agent: /root/arithmetic. Model: GPT-6 Astra Pro (inherited); effort setting not exposed. Date: 21 November 2026. This is a working research note for the parent, not a claim that the E8 bound is proved by the arithmetic arguments.

## A1. Positive-density criterion from Hecke equidistribution (proved)

Assume the corrected bounded-complexity construction: S is an irreducible smooth complex Shimura variety carrying a polarized abelian scheme and a fixed rational flat Hodge section t; c(s) is the least max(N,D) for an equality N t_s=[Z^+]-[Z^-] with N a positive integer and each effective cycle of degree at most D. Put S_C={c<=C}, and assume the relative Chow argument has established that S_C is closed algebraic. Let mu_j be probability measures supported on finite Hecke multisets of a CM point and converging weakly to the invariant probability measure mu on S(C).

Then either S_C=S for some C, or for every finite C,

    lim_j mu_j(S_C)=0.

In particular, a fixed C and limsup_j mu_j(S_C)>0 imply S_C=S. A uniform first-moment estimate sup_j integral c dmu_j <=M implies S_{ceil(2M)}=S. More generally, tightness of the distributions of c is equivalent to the existence of a uniform global bound, provided this equidistributed sequence exists.

Proof. A proper complex algebraic subset of a smooth connected complex manifold has real measure zero for every smooth volume form, by local stratification into lower-dimensional complex manifolds. Thus if S_C is proper then mu(S_C)=0. It is also closed in the analytic topology. The closed-set inequality for weak convergence gives limsup mu_j(S_C)<=mu(S_C)=0. For the first-moment assertion, Markov's inequality gives mu_j(c<=2M)>=1/2 (replace 2M by a larger integer if necessary), contradicting convergence to zero unless that S_C is S. Tightness supplies one C with positive mass bounded below, whereas a global bound makes all the distributions supported on one finite interval. QED.

This is a precise gate for an arithmetic attempt, not an estimate on c. Improving a convergence rate of mu_j does not supply the required positive mass of bounded-cycle points. Indeed, if every S_C is proper, equidistribution proves escape of complexity in probability, consistently with algebraicity at every individual Hecke point.

Primary equidistribution input: Eskin, A., & Oh, H. (2006). Ergodic theoretic proof of equidistribution of Hecke points. Ergodic Theory and Dynamical Systems, 26, 163–167, Theorem 1.2; arXiv:math/0409507v1, PDF p.2. The statement applies to a connected noncompact Q-simple real algebraic group, an arithmetic lattice, and any sequence of commensurator double cosets whose degrees tend to infinity. It gives convergence against bounded continuous functions. Passing from Gamma\G to Gamma\G/K by pushforward yields the criterion on the Shimura domain quotient. The special unitary derived group of signature (4,4) fits the relevant simple real-group setting. The introduction, PDF p.1, explicitly notes unconditional convergence rates from Clozel–Oh–Ullmo for smooth functions in their congruence setting. Thus full Hecke-packet equidistribution must not be identified with a GRH-dependent Galois-orbit assertion.

Sources: https://arxiv.org/pdf/math/0409507 (web ref turn654371097view0, theorem at extracted lines 55–63); https://doi.org/10.1017/S0143385705000428. The role of GRH is separate: a theorem using abelian class-field character sums may become effective under the corresponding GRH, but its identification with these Hecke measures and any rate needed must be supplied, not inferred merely from the names 'Hecke' and 'CM'.

## A2. Fixed CM field does not bound height on the polarized Weil Hecke orbit (proved in an explicit polarization type)

Let K=Q(omega), omega^2+omega+1=0, O_f=Z+f O_K, E_f=C/O_f and E=E_1. Put

    T = [[0,-1],[1,-1]],   H = [[2,-1],[-1,2]].

For any n>=1 let B_f=E_f^{2n}; put iota(omega)=diag(T,...,T), and let lambda_f be the polarization whose matrix relative to the product principal polarization is diag(H,...,H).

Then (B_f,iota,lambda_f) has Weil signature (n,n) and fixed polarization type (1^n,3^n). All these triples lie in one polarized K-linear rational-isogeny orbit, with a concrete isogeny phi_f:B_f->B_1 of degree f^{2n} and phi_f^*lambda_1=f lambda_f. Their Hermitian spaces are split. For n=4, this is a fixed polarized split E8 Hecke datum.

Proof. Direct matrix multiplication gives T^2+T+I=0 and T^t H T=H. The eigenvalues of H are 1 and 3, so H defines an ample polarization. Its Smith invariants are 1 and 3; repeating blocks gives the claimed type. T has eigenvalues omega and conjugate omega, each once on the complex tangent of E_f^2, and hence multiplicities (n,n). The identity map on C induces E_f->E because O_f is contained in O_K with index f; it has degree f. Its 2n-fold product commutes with T. On a curve, pullback of the principal polarization has degree f, so matrix H on each pair pulls back to fH. The product degree is f^{2n}. To see the Hermitian space is split, write each rational H1 as Q^2_T tensor H1(E_f,Q). The polarization is the product of the symmetric H-form on Q^2_T and the alternating form on H1(E_f,Q). For any nonzero rational a in H1(E_f,Q), Q^2_T tensor Qa is a K-line on which the alternating form and its K-skew lift vanish. The direct sum of these n lines is totally isotropic and has half the K-dimension. QED.

The stable Faltings height satisfies the exact difference formula

    h_F(E_f)-h_F(E)= (1/2) log f -(1/2) sum_{p|f} e_f(p) log p,
    e_f(p)= ((1-chi_{-3}(p))/(p-chi_{-3}(p)))
             * ((1-p^{-v_p(f)})/(1-p^{-1})).

This is the Nakkajima–Taguchi conductor correction, equivalently the difference between Theorem 1.3 at conductor f and at conductor 1 in Barquero-Sanchez et al. (2017). For f=l^r with a fixed split prime l (e.g. l=7), e_f(l)=0, so

    h_F(B_{7^r})=2n h_F(E)+n r log 7.

In particular h_F(E_{7^r}^8)=8h_F(E)+4r log 7 tends to infinity. Additivity of the stable Faltings height on products follows immediately from the determinant of invariant differentials with the product metric. No GRH is involved. The field discriminant stays -3 throughout. The growth comes from nonmaximal endomorphism orders/lattices, not a changing CM field.

Source: Barquero-Sanchez, A., Cadwallader, L., Cannon, O., Genao, T., & Masri, R. (2017). Faltings heights of CM elliptic curves and special Gamma values. Research in Number Theory, 3, Article 13, Theorem 1.3 and the definition of e(p) immediately after Theorem 1.1. https://doi.org/10.1007/s40993-017-0077-7 . The source defines e(p) with the opposite sign from the positive e_f(p) used above; substitution gives exactly the displayed negative correction. Primary source web ref turn270904604view1, lines 75–99. Nakkajima–Taguchi's original formula is cited there as reference 13; no unverified theorem number has been invented.

Scope caution. This explicit sequence is contained in a proper decomposable locus of the full unitary moduli space; it proves unboundedness of height on the orbit, not genericity of the sequence, failure of bounded cycles, or unboundedness of c. It is already sufficient to show that a bound c(x)<=F(h_F(A_x)) with unbounded F need not furnish a uniform bound. Passing to a different prescribed polarization lattice requires the usual rational isogeny comparison; this note asserts the fixed type explicitly displayed.

For the same reason, treating Colmez's formula as a function only of the fixed field K would miss the conductor correction. General Colmez formulas are in terms of virtual Artin characters; abelian CM fields reduce to Dirichlet characters. The full nonabelian formula is not a consequence of a Hecke-GRH premise alone. The 2026 primary preprint Maillot–Rössler, arXiv:2603.28536, Conjecture 2.1, still distinguishes the general conjecture from the established abelian case. This broader issue is unnecessary for the exact K=Q(omega) calculation above.

## A3. Positivity alone has no effective-cycle coercivity (proved as a logical obstruction)

Fix V=Q^2 with its positive definite form Q(x,y)=x^2+y^2, target t=(1,0), and degree functional d(x,y)=x. For m>=1 let the effective monoid M_m be generated by u_m=(m,1) and v_m=(m+1,1). Every nonzero effective vector has positive integral degree, M_m-M_m=Z^2, and t=v_m-u_m. Yet the least value of max(d(z^+),d(z^-)) over t=z^+-z^- with z^+,z^- in M_m is exactly m+1, although Q(t)=1 for every m and the ambient lattice is fixed and saturated.

Proof. The determinant of the matrix with columns u_m,v_m is -1, so the two generators form a Z-basis of Z^2. Writing z^+=a u_m+b v_m and z^-=c u_m+d v_m with nonnegative integer coefficients, uniqueness of the difference expression gives a-c=-1 and b-d=1. Thus c>=1 and b>=1. Therefore d(z^+)>=m+1 and d(z^-)>=m, with equality achieved by v_m and u_m. QED.

A separate denominator example is V=Q, Q(x)=x^2, integral Hodge lattice Z, and algebraic sublattice mZ. The target 1 has norm one and least positive N with N*1 in mZ equal to m. A positive definite form on the rational realization does not bound this saturation index.

These examples do not refute any geometric Hodge conjecture. They refute the formal inference 'positive realization pairing + bounded norm of a Hodge vector => bounded effective-cycle representatives or bounded saturation index'. A cycle-theoretic estimate linking the positive form to an effective decomposition and its integral lattice remains indispensable.

Alpöge input convention: the user's supplied RH and Dirichlet-GRH theorems are carried as cited theorems. The available Main.lean declares `riemannHypothesis`, `riemannZeta_eq_zero_re`, `LFunction_ne_zero_of_half_lt_re`, `LFunction_eq_zero_re`, `LFunction_eq_zero_re_of_isPrimitive`; Statements.lean defines the corresponding assertions. Their imported proof trees are not in this ZIP. The note's spectral sign sketch is at Remark, p.3, footnote 3 and steps 3/5 (step 5 continues p.4). Neither those entrypoints nor the quoted sign sketch states the needed Chow-degree/coercivity or integral-cycle saturation bound. The map's §4 gives only tentative Lean paths for step 5, namely Formalism/PeriodIntegrals/ExplicitFormulaCounts and Formalism/LandauZeroFreeBounds/ExceptionalZeroBounds/ExplicitFormulaErrorOfHostConditions. This run has not compiled or independently checked those unavailable files.

Masullo convention: Hecke GRH is a conditional premise attributed to §1.2 by the user's prompt. Only an automatically extracted, truncated index is supplied. It lists Theorem 13.3.1.1 (Trace Formula), PDF p.522; the immediately following entry contains editorial placeholders for the main theorems. The index does not suffice to state or independently verify a numbered GRH theorem. No argument above depends on Masullo.

## S1. Independent targeted reading of Severn §§4–5 (no fault found in this chain)

New source identified by root: Severn, B. (2026). Weil classes on abelian sixfolds and eightfolds of Weil type for Q(sqrt(-3)). Hexagon 2610.00387v2, source date 21 October 2026 (version 1.5). Source URL https://hexagonmath.org/api/v1/works/2610.00387v2/source?path=weil-qsqrt3-v1.5.tex . Web refs turn341571605view0, turn895175109view0. Theorem A claims the exact split eightfold Weil-class statement. This note audits §§4–5 only, not the dominance computation or the entirety of Theorem A.

The section-number interface was read in full, including source labels `lem:schoen`, `lem:schoenR`, `prop:supply`, `cor:everymember`, and `thm:brauer` (source lines 204–326). The following checks were made:

1. The multiplicity formula for a primitive cyclic character is h=2q-2+s even when some branch exponents are not coprime to m: a faithful character detects every nontrivial local inertia, so each branch point removes one invariant local section. The primitive Prym rational summand is selected by the sum of the Galois-conjugate character idempotents.
2. Schoen's actual definition of a simple tuple is pairing alpha with -alpha, and his Theorem 2.0 and Corollary 3.1 have the stated scope. Checked in Schoen (1988), printed pp.11–12 and 24–25, with noncoprime local exponents treated on printed p.10. Source: https://www.numdam.org/item/CM_1988__65_1_3_0.pdf, refs turn185373769view0 and turn384566713view1. His Lemmas 2.4–2.5, printed pp.14–15, give the SNC/blow-up geometry used in the repair.
3. Repair lemma: for finite beta_i, proper base change identifies a character stalk with the character part of the finite fibre permutation module. A primitive character is faithful, hence every point with nontrivial inertia has zero stalk. The exceptional divisor is unramified at its generic point because alpha_{2i-1}+alpha_{2i}=0 mod m. On an exceptional P1 fibre away from other branch divisors, the resulting sheaf is extension by zero of a rank-one local system on C* with nontrivial monodromy. Its compactly supported H0 and H2 vanish and Euler characteristic is zero, hence all cohomology vanishes. Fibres lying in another branch divisor have zero restriction. Proper base change for the exceptional P1-bundle therefore gives the claimed total vanishing. No step requires a prime-order quotient retaining inertia. I found no fault in this replacement proof.
4. The centralizer U decomposes as GL multiplicity factors for nonself-dual representation pairs, O for quaternionic representations, and Sp for orthogonal representations. Its determinant character quotient has free coordinates for GL and order-two coordinates for O. The O parity is retained; it is not discarded by passing incorrectly to the identity component.
5. In `prop:supply`, the complementary product Z_i of all determinant eigenspaces except the selected one has the negative character because the full product is top cohomology. The resulting Gamma is U-invariant; the signs of negative Brauer coefficients are implemented by inverse characters, and parity makes absolute values harmless on the order-two coordinates. The degree count is deg(Gamma)=2dim(B)-h_B+p, giving a correspondence H^{h_B}(B)->H^p(X).
6. The inclusion S(J(C)) subset U is in the correct direction because S(J(C)) centralizes all endomorphisms, hence Q[G]. Milne (1999), Theorem 3.2 and Lemma 3.1, directly give algebraicity of the U-invariant pullback to J(C)^R. His definition of S(A) on preprint p.6 is the full (possibly disconnected) centralizer in the symplectic group. Checked primary source: https://jmilne.org/math/articles/1999aP.pdf, refs turn531132820view0 and turn419156328view0, preprint pp.14–15. The retract pi o iota=[N0] makes pullback injective and carries algebraicity back.
7. A nonzero rational vector in a one-dimensional cyclotomic vector space has nonzero components at all embeddings; thus the contraction with the chosen complement selects a nonzero multiple of the target line. Rational descent from containment after tensoring with C is ordinary faithful flatness of vector spaces.
8. Brauer induction is applied in the complex representation ring, with integer coefficients, and Frobenius reciprocity gives the character identity. Linear real characters (order 1 or 2) have zero free coordinates; their multiplicities in a quaternionic representation are even because the invariant alternating form restricts nondegenerately to that self-dual one-dimensional isotypic subspace. Terms of h=0 contribute no coordinates occurring in H1(C).
9. If a local branch element g is conjugate to g^{-1} by w, the map H'x<g> -> H'xw<g> is well-defined and bijective, preserving the minimal return exponent and inverting cyclic local monodromy. The branch-exponent multiset is therefore inversion-stable. Globally the sum of all cyclic branch exponents is zero because the commutators in the base curve relation map to zero in a cyclic group. The number of self-inverse exponents m/2 is consequently even; all exponents can be paired. Every surviving Brauer supplier is admissible.

Conclusion of this bounded audit: Severn's supplier and Brauer chain is supported by a complete targeted proof reading and by verification of the Schoen/Milne interfaces; no fault was found. This is not a formal certificate and does not certify the independent monodromy/dominance component. If root verifies that component, this literature input closes the qualitative split E8 Weil-class bound by the Chow boundedness argument, independently of GRH. It does not by itself provide numerical least degrees and denominators on the Hecke orbit.

## Grothendieck locators

The supplier construction is in the category of homological abelian motives with correspondences (finite quotients, group-algebra projectors, exterior powers, products, and Gysin maps), and the final Milne step identifies a tensor-invariant realization with the divisor-generated subspace. The repair's proper-base-change interface has the classical SGA 4, Exposé XII, Théorème 5.1 formulation for torsion étale cohomology; its complex constructible-sheaf analogue is the one actually used here. No archival cote/scan was supplied or consulted, so this note asserts no transcription correction and invents no archival locator. The exact published locators above should be retained separately from the requested but unavailable archival mapping.

## Check events for import by root

| Statement | Date | Type | Outcome |
|---|---|---|---|
| A1 | 2026-11-21 | targeted proof check | Whole elementary proof read after drafting; closed-set inequality and Markov constants checked; assumes S_C closed and genuine weak equidistribution. |
| Eskin–Oh Thm 1.2 | 2026-11-21 | used and rechecked in this run | Primary statement and hypotheses read; not reproved. |
| A2 | 2026-11-21 | targeted proof check | Whole proof read; matrix identities, lattice index, polarization type, isotropic K-line argument and height correction sign checked. |
| Barquero-Sanchez et al. Thm 1.3 | 2026-11-21 | used and rechecked in this run | Exact source statement read; conductor-f minus conductor-1 specialization used. |
| A3 | 2026-11-21 | targeted proof check | Whole monoid and lattice proofs read; exact minimal degrees checked by unique basis coefficients. |
| Alpöge RH/Dirichlet GRH | 2026-11-21 | carried as background without fault found | Cited under user convention; entrypoint statements inspected; no Lean rebuild or proof-tree audit. |
| Alpöge step 5 cycle implication | 2026-11-21 | targeted proof check | No cycle coercivity/saturation statement identified; no claimed implication used. |
| Masullo Hecke GRH premise | 2026-11-21 | carried as background without fault found | Conditional claim only; supplied index cannot support independent proof check; not used in A1–A3. |
| S1 supplier/Brauer chain | 2026-11-21 | targeted proof check | Complete proof reading of Severn §§4–5, no fault found; excludes dominance. |
| Schoen 1988 Thm 2.0, Cor 3.1, Lem 2.4–2.5 | 2026-11-21 | used and rechecked in this run | Exact primary statements and local geometry read. |
| Severn lem:schoenR | 2026-11-21 | independent re-proof | Faithful-character j_! fibre cohomology and proper-base-change argument reconstructed; agrees with source. |
| Milne 1999 Thm 3.2, Lem 3.1 | 2026-11-21 | used and rechecked in this run | Exact source statements and centralizer definition read; no independent proof claimed. |

All events above were performed by /root/arithmetic, GPT-6 Astra Pro, effort unspecified, run HECKE_DIV_20261121. Parent should record any further independent checks as separate events.
