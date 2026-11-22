# AM-DO-017–020: literal moved-theta operators, a mixed-CM family, and exact split-place phases

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`, 21 November 2026 UTC. The inherited reasoning effort is not separately exposed. This file gives full proofs of the new finite-operator assertions. AM-R-004, AM-DO-011–016, ALP-LIFT-07 and the source definitions are retained at their recorded status. Write **Σ_tr** for AM-DO-015's normalized Mumford translate of F₁; it is distinct from the leading-coefficient-normalized hyperelliptic sigma function σ_q used in the parallel calculation.

## 1. The recovered literal source object

The source definition sought in `I.J.V.thMoved` has now been recovered and read. Its exact file is

`Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/IsDiscriminantTwelfthRootOfIdealLatticeIffDelta1.lean`.

The relevant locators are:

| Source lines | Exact content |
|---|---|
| 18–24 | `lamOf`, elliptic ideal lattice; the discriminant twelfth-root pin; an un-killed elliptic two-torsion point |
| 36–51 | `La`, `Hf`, `al`, `U`, `Iop` |
| 110–118 | `VacIn`: an elliptic `PeriodPair`, its prescribed lattice, half-period, `IsoKG`, its complex-linear extension, and `KapIn` |
| 130–138 | `thMM`, `thZero`, `thHalf`, `thMoved` |
| 140–141 | `eNat = chiFac · thMoved` |
| 173–185 | literal conversion to the earlier `Formalism.L2.Ker.Base` record |

In mathematical notation its averaging operator is

\[
 I_{21}F=q_{21}^{-1/2}
       \sum_{x\in\Lambda_2/(\Lambda_1\cap\Lambda_2)}\alpha(x)U_xF,
 \qquad q_{21}=[\Lambda_2:\Lambda_1\cap\Lambda_2],
\tag{DO17.1}
\]

where the positive real square root is used and

\[
 U_xF(z)=e^{-\pi H(z,x)-\pi H(x,x)/2}F(z+x).
\tag{DO17.2}
\]

The source's `La₁.addSubgroupOf La₂` is the intersection regarded as a subgroup of Λ₂; this matters for the index. Its sign is `al(x)=(-1)^{round((√d/2)H(x,x))}`. In the admitted integral situations it is a sign semicharacter, so α⁻¹=α.

Writing Λ₀₀, Λ₁₀, Λ₁₁ for the standard, first-lattice-moved, and both-lattices-moved period lattices, the source literally uses

\[
 \mathrm{thMoved}_{L,L'}=I_{\Lambda_{10},\Lambda_{11}}
                       I_{\Lambda_{00},\Lambda_{10}}
                       \mathrm{thZero},
 \qquad\mathrm{thZero}=\mathrm{thMM}^{\boxtimes NN'}.
\tag{DO17.3}
\]

The exact seed is not left arbitrary: `Formalism/LocalToGlobal/KernelLattices/LateralTheory.lean`, lines23–29, defines `IsThM` by membership in the specified theta line and the fourth-tensor equation

\[
              \theta^{\boxtimes4}=\kappa\,\mathrm{kernel4}(L,\omega_0,\Lambda_M,g_C),
\tag{DO17.4}
\]

and takes `thM` by choice from that predicate. The same file, lines128–178, repeats the complete base record and moved formulas. Lines230–238 separately name `SignP` (comparison with the direct one-step average, up to sign) and `OrderP` (equality of the two orders of moving the lattice factors). Thus phase and order compatibility are actual source obligations; norm preservation alone cannot replace them.

These additional modules were retrieved from the pinned mirror commit `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`, with individual hashes in `source_recovery_20261121T204914Z.json` and `source_recovery_20261121T205055Z.json`. The intake does not supply original-author hashes for these paths. Retrieval and reading do not constitute a Lean build or a transitive proof audit.

## AM-DO-017. Exact normalized averaging between principal theta lines

Let V be a complex vector space, H a positive Hermitian form linear in its first variable, and E=Im H. Let Λ₁,Λ₂ be commensurable full lattices selfdual for E:

\[
 \Lambda_i=\{v\in V:E(v,\Lambda_i)\subset\mathbf Z\}.
\tag{DO17.5}
\]

Let αᵢ:Λᵢ→U(1) satisfy

\[
 \alpha_i(x+y)=\alpha_i(x)\alpha_i(y)e^{\pi iE(x,y)},
\tag{DO17.6}
\]

and suppose their restrictions to Λ₀=Λ₁∩Λ₂ agree. Write T(Λᵢ,αᵢ) for the holomorphic functions satisfying U_λF=αᵢ(λ)F. On this space use the probability-Haar norm

\[
 \|F\|_i^2=\frac1{\operatorname{vol}(D_i)}
     \int_{D_i}|F(z)|^2e^{-\pi H(z,z)}\,dz,
\tag{DO17.7}
\]

where Dᵢ is any fundamental domain for Λᵢ and dz is any fixed Lebesgue measure. This is independent of Dᵢ and of rescaling dz.

Then q=[Λ₂:Λ₀]=[Λ₁:Λ₀] is a positive finite integer and

\[
 \boxed{I_{21}F=q^{-1/2}\sum_{x\in\Lambda_2/\Lambda_0}
             \alpha_2(x)^{-1}U_xF}
\tag{DO17.8}
\]

is a well-defined nonzero isometry T(Λ₁,α₁)→T(Λ₂,α₂). In the source's sign-valued case this is exactly (DO17.1), including its square-root index. Both spaces are one-dimensional. No unspecified positive scalar occurs in (DO17.8).

### Proof

Direct multiplication of the factors in (DO17.2) gives

\[
 U_xU_y=e^{-\pi iE(x,y)}U_{x+y},\qquad
 U_xU_y=e^{-2\pi iE(x,y)}U_yU_x.
\tag{DO17.9}
\]

Also

\[
 |U_xF(z)|^2e^{-\pi H(z,z)}
       =|F(z+x)|^2e^{-\pi H(z+x,z+x)}.
\tag{DO17.10}
\]

Thus translations are isometries whenever both sides are viewed on a common lattice on which their norms are periodic.

Because Λᵢ is selfdual, the alternating integral matrix of E on any Z basis of Λᵢ is unimodular. Its Pfaffian has absolute value1. Consequently both lattices have the same symplectic covolume, hence the same covolume for dz. Since Λ₀ has finite index in each, division of covolumes gives [Λ₁:Λ₀]=[Λ₂:Λ₀]=q. A fundamental domain for Λ₀ is, up to null sets, the disjoint union of q translates of a fundamental domain for Λᵢ. For a Λᵢ-periodic norm density, dividing its integral by the domain volume therefore gives precisely (DO17.7). Thus the normalized norm on the common lattice equals the norm on either original lattice; there is no extra q in changing domains.

For x∈Λ₂, the function U_xF lies in T(Λ₀,α₀), since E(x,Λ₀) is integral. The operators V_x=α₂(x)⁻¹U_x form an ordinary representation of the additive group Λ₂ by (DO17.6) and (DO17.9). If x∈Λ₀, then V_xF=F. Consequently the sum (DO17.8) is independent of coset representatives and is fixed by all V_y, y∈Λ₂. It is therefore in T(Λ₂,α₂).

The finite pairing

\[
 (\Lambda_1/\Lambda_0)\times(\Lambda_2/\Lambda_0)
       \longrightarrow U(1),\qquad
 (\lambda,x)\longmapsto e^{2\pi iE(\lambda,x)}
\tag{DO17.11}
\]

is well-defined and nondegenerate. Indeed, if x∈Λ₂ pairs trivially with every λ∈Λ₁, then selfduality of Λ₁ implies x∈Λ₁, hence x∈Λ₀. The same argument applies to the other variable. The two groups have order q, so this is a perfect finite pairing.

For distinct x,y modulo Λ₀, choose λ∈Λ₁ for which e^{2πiE(λ,x−y)}≠1. The operator U_λ is unitary on T(Λ₀,α₀), by (DO17.10). By (DO17.9), U_xF and U_yF are its eigenvectors with eigenvalues α₁(λ)e^{−2πiE(λ,x)} and α₁(λ)e^{−2πiE(λ,y)}. Their eigenvalues are distinct and have absolute value1. Taking their inner product and using unitarity shows that they are orthogonal. Each has norm ||F||₁. Therefore

\[
 \|I_{21}F\|_2^2
     =q^{-1}\sum_{x\in\Lambda_2/\Lambda_0}\|U_xF\|_0^2
     =\|F\|_1^2.
\tag{DO17.12}
\]

This proves the isometry and nonvanishing.

For completeness, dimension one is the elementary principal-theta dimension statement. Choose a symplectic Z basis of Λᵢ, normalize its first half to the real standard basis, and write the second half as the columns of τ with Im τ positive. After a linear exponential gauge, the real-period relation gives a Fourier expansion indexed by Z^g. The τ-period relation successively determines every Fourier coefficient from one coefficient, with the usual Gaussian factor exp(πinᵗτn) and the semicharacter shifts. Positivity gives normal convergence of that theta series. Hence the dimension is exactly one. Equivalently this is h⁰=1 for a principal polarization. ∎

The theta line on V/Λ₀ used in this proof has degree q: its symplectic covolume is q times that of a principal lattice. The q orthogonal vectors above are consistent with its q-dimensional space of sections. The argument did not confuse this degree with q², the order of its full theta kernel.

### Exact transport and exact residual phase

If C:V→V′ is complex-linear with H′(Cx,Cy)=H(x,y), CΛᵢ=Λᵢ′ and αᵢ′(Cx)=αᵢ(x), then pullback by C commutes **exactly** with (DO17.8). Indeed it commutes with each U_x, induces a bijection of the finite quotient sets, and preserves q. Thus any specified base equality with scalar c extends to the entire two-step family with that same scalar c.

For three such lattices, choose a nonzero F∈T(Λ₁,α₁). Since all three theta lines have dimension one, there is a unique phase

\[
 \mu_{321}=\frac{\langle I_{31}F,I_{32}I_{21}F\rangle_3}{\|F\|_1^2},
 \qquad |\mu_{321}|=1,
 \qquad I_{32}I_{21}=\mu_{321}I_{31}.
\tag{DO17.13}
\]

Our convention makes the inner product linear in its second argument. This phase is independent of F. It is explicitly a finite Gauss sum: expand the three averages, use (DO17.9), and use

\[
 \frac{\langle U_zF,U_tF\rangle}{\|F\|^2}
 =\begin{cases}
 e^{\pi iE(z,t)}\alpha_1(t-z),&t-z\in\Lambda_1,\\
 0,&t-z\notin\Lambda_1.
 \end{cases}
\tag{DO17.14}
\]

The zero case follows from the same perfect-pairing argument (using a common finite-index lattice for the finitely many vectors); the nonzero case follows from U_{−z}U_t=e^{πiE(z,t)}U_{t−z}. Equations(DO17.8), (DO17.9), and (DO17.14) are an exact finite prescription for μ, with all normalizations included. Neither its value1 nor its value±1 is automatic from nonvanishing. The special `SignP` and `OrderP` assertions in the original constructor must therefore be checked in a new constructor.

## AM-DO-018. A trace-one mixed-CM moved family with explicit finite inputs

Retain the actual principally polarized J of AM-R-004. Let V=C³ in algebraic u coordinates, Λ=DΦ(O_E), and H(u,v)=Σu_i conjugate(v_i)/G_i. In the first-argument-linear convention, E_H=Im H is the negative of the displayed Riemann intersection form in AM-R-004; changing this sign does not change selfduality. Put

\[
 w_0=-(\zeta+\zeta^2+\zeta^4),\qquad
 w_0+\bar w_0=1,
\]

acting through the actual CM action. On every w₀-stable E_H-integral lattice define

\[
             \alpha_{\rm tr}(x)=e^{\pi iE_H(x,w_0x)}\in\{1,-1\}.
\tag{DO18.1}
\]

This is a semicharacter, and its formula agrees on intersections of lattices. It is the Appell–Humbert semicharacter of the rigidified trace-one Poincaré line L_{w₀}.

**Proof.** The Rosati adjoint of w₀ is bar(w₀). Hence

\[
 E_H(x,w_0y)+E_H(y,w_0x)
       =E_H(x,(w_0-\bar w_0)y)
       =2E_H(x,w_0y)-E_H(x,y).
\]

For integral stable lattices, its exponential times πi equals exp(πiE_H(x,y)). Expanding E_H(x+y,w₀(x+y)) proves (DO17.6). For the line identification, the Poincaré line pulled back by the principal polarization is m*L⊗p₁*L⁻¹⊗p₂*L⁻¹. Its Hermitian form on V×V is H(z,w′)+H(w,z′) and its semicharacter on (λ,μ) is exp(πiE_H(λ,μ)), by the semicharacter identity for any representative L. Pullback by (1,w₀) has Hermitian form H, since w₀+bar(w₀)=1, and semicharacter (DO18.1). This proves the assertion with the canonical rigidifications. ∎

As an explicit sign check in the actual period basis, E_R004(ζʲ,w₀ζʲ)=Tr(ξ bar(w₀))=−1 for each j=0,…,5, with ξ=(ζ−ζ⁻¹)/7. Thus α_tr takes value−1 on each adjacent-cycle generator γⱼ. AM-DO-012/ALP-LIFT-07's characteristic K∞=(101|111) gives exactly these six signs. This checks the trace-one line against the analytic Σ_tr convention rather than merely matching Chern classes.

### Matrix-lattice family

Fix positive integers a,b. For full O_E-lattices N⊂E^a and N′⊂E^b that are selfdual for their standard Hermitian forms, let

\[
 M(N,N')=\operatorname{Hom}_{O_E}(N,N')\subset M_{b\times a}(E),
 \qquad\Lambda(N,N')=D\Phi(M(N,N')).
\tag{DO18.2}
\]

Here DΦ is applied entry by entry, and the Hermitian form is the sum of H on all ab entries. These lattices are full, commensurable, selfdual for the product E_H, and stable under w₀. To check selfduality, localize at a rational prime and choose arbitrary module bases g,h of N,N′. Their Hermitian Gram matrices G_N=g* g and G_N′=h* h are integral and unimodular because the lattices are Hermitian selfdual. Writing X=hZg⁻¹ identifies the matrix pairing with the trace pairing whose Gram operator is Z↦G_N′ Z G_N⁻¹; this is an integral module automorphism. The scalar trace pairing is perfect on O_E because ξO_E is the codifferent, as proved in AM-R-004. Hence the matrix trace pairing is perfect on every local Hom lattice. Intersecting the local duals proves the global assertion. Equivalently the argument is projective-module duality Hom(N,N′)≃N*⊗N′. This includes every lattice pair obtained from the standard lattices by finite adelic unitary moves. No local classification of ramified or dyadic unimodular Hermitian lattices, and no global rational unitary basis, is assumed.

Let

\[
 F_{00}(u)=\prod_{i=1}^{b}\prod_{j=1}^{a}\Sigma_{\rm tr}(u_{ij}),
\]

and put

\[
 F_{N,N'}=I_{\Lambda(N,O_E^b),\Lambda(N,N')}
          I_{\Lambda(O_E^a,O_E^b),\Lambda(N,O_E^b)}F_{00},
\tag{DO18.3}
\]

using (DO17.8) and the common sign(DO18.1). This is an actual, nonzero holomorphic section of the corresponding principal trace-one line on V^{ab}/Λ(N,N′). Every averaging coefficient and every finite quotient is specified. It has exactly the same probability-Haar L² norm as F₀₀.

Write

\[
 q_1=[\Lambda(N,O_E^b):\Lambda(N,O_E^b)\cap\Lambda(O_E^a,O_E^b)],\quad
 q_2=[\Lambda(N,N'):\Lambda(N,N')\cap\Lambda(N,O_E^b)].
\tag{DO18.4}
\]

The two q's are concrete integral lattice indices, computable by Smith normal form in the integral period basis. They are not arbitrary group volumes.

### Explicit rational Heisenberg intertwining

Use normalized complex coordinates z and the convention ψ∞(r)=exp(2πir), ψ_f(r)=exp(−2πir) on Q. For t=A+τB with A,B∈Q³ define on finite Schwartz functions

\[
 (W_t\phi)(q_f)=\psi_f(-A^tq_f+A^tB/2)\,\phi(q_f-B).
\tag{DO18.5}
\]

Let Rφ(z)=e^{Q(z)}Σ_{q∈Q³}φ(q)e^{πiqᵗτq+2πiqᵗz}. Then

\[
                     R(W_t\phi)=U_t(R\phi).
\tag{DO18.6}
\]

**Proof.** The multiplier from Q(z+t)−Q(z)−πH(z,t)−πH(t,t)/2 equals exp(2πiBᵗz+πiBᵗτB+πiAᵗB). In the theta sum for Rφ(z+t), replace q by q′−B. The remaining coefficient is φ(q′−B)exp(2πiAᵗq′−πiAᵗB), exactly(DO18.5) on rational points. Absolute convergence on compact sets permits this reindexing and all derivatives. The same calculation entry by entry proves the matrix version. ∎

For reference this map is injective on finite Schwartz functions: compact support gives a common denominator M with rational support in M⁻¹Z³; restricting z to the real cube of side M, Fourier uniqueness recovers every φ(q) times its nonzero Gaussian coefficient. The diagonal Q is dense in A_f, so a locally constant function vanishing on Q is zero. The same holds in all matrix dimensions.

Let φ₀ be the tensor product of AM-DO-016's specified input

\[
 -i\,1_{\delta/2+\widehat{\mathbf Z}^3}(q_f)\,
             \psi_f(-q_f^t\varepsilon/2),
 \qquad\delta=(1,1,1),\ \varepsilon=(1,0,1).
\]

Replace each U_t in (DO18.3) by W_t, with the same α_tr(t) and the same positive q_i⁻¹/², to define the finite Schwartz function φ_{N,N′}. Every t lies in the rational span of the standard period lattice, so (DO18.5) applies. The output is compactly supported and locally constant, with algebraic coefficients. AM-DO-016 and (DO18.6) give the **whole moved-family equality**

\[
 \boxed{R\phi_{N,N'}=\theta[0;0](0;\tau)^{ab}\,F_{N,N'}.}
\tag{DO18.7}
\]

The period scalar is the same for every N,N′ at these fixed ranks. This is more than a nonzero period or a single-fiber identity. It is an actual family of finite inputs and all-degree holomorphic theta equalities. It still does not identify φ_{N,N′} with the prescribed split Weil translate of φ₀; that further assertion is addressed below.

### Normalization and explicit elementary costs

Carry the exact norm from AM-R-004(R4.12), with κ=1, and the isometry of normalized Mumford translation. Then

\[
 \|F_{N,N'}\|^2
     =\det(2Y)^{-ab/2}|\theta[0;0](0;\tau)|^{-2ab}.
\tag{DO18.8}
\]

Thus the phase-preserving scalar that changes (DO18.7)'s reduced seed to norm1 is

\[
 c_{\rm unit}=\theta[0;0](0;\tau)^{ab}\det(2Y)^{ab/4},
 \qquad \|c_{\rm unit}F_{N,N'}\|=1.
\tag{DO18.9}
\]

This is an explicit local analytic normalization, not the terminal automorphic mass pairing in G1.

AM-R-006 now computes the algebraic scalar between the two actual seeds:
Σ_tr=cσ_q, where the phase is fixed by (R6.3), c⁸=R_S²/4⁸, v₂(c)=−2,
v₇(c)=1/2, and the other finite valuations are zero. Consequently, if the
same averages are applied to σ_q^{⊠ab}, then (DO18.7)'s common period is
exactly (θ₀c)^{ab}. Its squared norm is (DO18.8) divided by |c|^{2ab},
and the phase-preserving norm-one scalar is (θ₀c)^{ab}det(2Y)^{ab/4}.
These equalities follow from linearity of each specified average. They
do not select an arbitrary algebraic root for c or absorb it silently
into an unspecified period.

If normalized valuations satisfy v_p(p)=1, the algebraic values of the constructed Schwartz input satisfy the elementary bound

\[
 v_p(\phi_{N,N'}(q_f))\ge-\tfrac12v_p(q_1q_2)
\tag{DO18.10}
\]

where a zero value has valuation +∞. Indeed the original nonzero coefficients, α_tr signs and finite additive-character values are roots of unity; the only displayed denominators are the two inverse square roots of positive integers. The ultrametric inequality proves the claim, and cancellation may improve it. This is a statement about **finite Schwartz coefficients**, not an assertion that the corresponding reduced CM Taylor series is integral at a nonordinary prime.

At the fixed complex embedding, AM-DO-015 and triangle inequality give the completely explicit growth bound

\[
 |F_{N,N'}(u)|<49^{ab}\sqrt{q_1q_2}\,
      \exp\!\left(\frac\pi2\sum_{i,j,k}|u_{ij,k}|^2/G_k\right).
\tag{DO18.11}
\]

Each normalized U_t preserves the Gaussian envelope, while a q-term average costs at most √q. The corresponding polydisk Cauchy bound follows exactly as in AM-R-004. This does not claim that √(q₁q₂) is optimal. L² norm preservation does not by itself eliminate this displayed pointwise cost for varying lattices.

## AM-DO-019. Exact boundary between this mixed family and the prescribed constructor

There are two distinct questions.

**Unchanged elliptic `VacIn`.** The recovered record fixes an elliptic period lattice and a complexification of an isomorphism over the quadratic CM subfield; its base fourfold kernel is built from that elliptic data. AM-R-003 proves that the primitive Φ={1,2,3} Jacobian J has no nonzero homomorphism to or from an elliptic curve and no isogeny with an elliptic power. Therefore a full, line-preserving CM/Hodge transport from that unchanged elliptic constructor to J (or the corresponding powers) does not exist. This conclusion uses the actual category demanded by the record, not the false inference that absence of a canonical map excludes all maps. Arbitrary vector-space maps, selected coefficient maps, and a new mixed-CM constructor are not excluded.

**A new mixed-CM constructor.** Equations(DO18.1)–(DO18.11) give its trace-one theta seed, every moved lattice, every finite input, the exact average/covolume factors, and one common analytic period. The remaining prescribed-Weil equality is

\[
 \omega_{\psi,\chi}(g,h)\phi_0
       \stackrel{?}=\chi(x)^{-1}\chi(y)\,\phi_{N,N'},
 \quad x/\bar x=\det g,\quad y/\bar y=\det h.
\tag{DO19.1}
\]

The roots x,y are determinant roots, as in the actual source `IsDetRoot`; substituting det(g),det(h) is generally wrong. The source also fixes ψ∞ with the opposite sign from (DO18.5); its polarization/character transport must be included before testing(DO19.1). In a common realized Heisenberg representation the two sides lie on the same one-dimensional lattice vacuum line, so their quotient is a phase once both are norm1. Its value must be computed from the chosen splitting on generators, or from the finite Gauss sum(DO17.13) together with the specified determinant-root character. Merely saying that both vectors are nonzero gives no equality.

The exact recovered source makes this distinction visible. `MovedWeilVacuumEqVacuumOfMovedLattices.lean`, theorem `vac_moved`, proves preservation of the moved lattice vacuum, theta membership and nonvanishing. It does **not** conclude the common c₀/determinant-root formula. `LevChiEqOne.lean`, lines87–101, places that formula in `VacT` and `PinX.mv`. `ThetaKernelSplitPlacesEqJetClassicalTheta.lean`, theorem `thetaKernel_eq_jet_thC`, takes the equation `xiN(om(g,h)vac)=κE` as an explicit hypothesis and then transports it to every polynomial jet. Thus the missing phase is exactly where the source says it is.

A failure to prove(DO19.1) is not a proof that it is false. Conversely, (DO18.7) does not prove it by construction, because the φ_{N,N′} were defined through the two fixed finite averages, while the source fixes a group representation and its splitting independently. Nor do these analytic equalities prove the full integral row-lattice identities, the nonordinary formal-gauge comparison, the `MainX` cohomological/topological bounds, or the terminal-mass equation from THETA3 G1. Those remain their stated separate gates.

## AM-DO-020. The phase is exactly the splitting character for relative split-place moves

The previously open phase in(DO19.1) can be resolved in a substantial precise scope: moves supported on finite places of F that split in E. This includes the primes above11 and29 for E=Q(ζ₇), and also the relative split dyadic places. This assertion is conditional on a Weil representation with the displayed covariance, unitarity and split-normalization axioms; it proves the required phase from those axioms, rather than replacing the prescribed representation by a new family of unrelated operators. It does not extend the old quadratic `StdPair.xi` pin to the primitive type.

### Local statement

Let k be a nonarchimedean field of characteristic zero, O its integers, and ψ a nontrivial additive character. Put E_v=k×k with conjugation interchanging factors. Choose the split Schrödinger polarization of the rational symplectic Hom space. After identifying the momentum space with the ψ-dual of the position space X, write its form and Heisenberg action as

\[
 B((x,y),(x',y'))=\langle y,x'\rangle-\langle y',x\rangle,
 \qquad
 [\rho(x,y)\phi](t)=\psi(-\langle y,t\rangle+\langle y,x\rangle/2)
                           \phi(t-x).
\tag{DO20.1}
\]

Let L⊂X be a full O-lattice and L* its annihilator under ψ. The split O_E-lattice is Λ_L=L⊕L*. An integral trace-one endomorphism is w₀=(w,1−w), with w,1−w∈O. Its local semicharacter is

\[
 \alpha_L(x,y)=\psi\bigl((w-\tfrac12)\langle y,x\rangle\bigr),
       \qquad (x,y)\in L\oplus L^*.
\tag{DO20.2}
\]

Here the pairing is taken in the additive-character conductor convention, so its integral values and their O-multiples are killed by ψ. Formula(DO20.2) is the local factor of α_tr=exp(πiE_H(x,w₀x)): globally α_tr=ψ_f(B(x,w₀x)/2), using E_H=−B and the product formula for the additive character. It follows immediately that

\[
 \alpha_L(x,y)^{-1}\rho(x,y)\phi(t)
                   =\psi(-\langle y,t\rangle)\phi(t-x)
       \quad\text{for }(x,y)\in\Lambda_L.
\tag{DO20.3}
\]

Indeed the extra scalar is ψ((1−w)〈y,x〉)=1. This cancellation is valid at residue characteristic two as well. Dropping the half-pairing term without the trace-one semicharacter would not justify that dyadic assertion.

The common eigenspace

\[
 \rho(\lambda)\phi=\alpha_L(\lambda)\phi
                     \quad(\lambda\in\Lambda_L)
\tag{DO20.4}
\]

is precisely the line spanned by1_L. For y∈L*, the modulation relation forces the support into (L*)*=L; for x∈L, the translation relation makes the function constant there. Conversely1_L satisfies the relations by(DO20.3). With any fixed Haar measure dt on X, its positive norm-one generator is

\[
                         v_L=\operatorname{vol}(L)^{-1/2}1_L.
\tag{DO20.5}
\]

For two position lattices L₀,L, the averaging operator(DO17.8), realized by ρ, satisfies the exact equality

\[
                             I_{L,L_0}v_{L_0}=v_L.
\tag{DO20.6}
\]

Our index notation in(DO20.6) means that the output lattice is L; equivalently I_{21}v_{L₁}=v_{L₂}.

### Proof of the exact index and value in(DO20.6)

Let M=L∩L₀, N=L+L₀, u=[L:M], and v=[L₀:M]. Duality gives

\[
 L^*\cap L_0^*=N^*,\quad
 [L^*:N^*]=[N:L]=[L_0:M]=v.
\]

Therefore

\[
 q=[\Lambda_L:\Lambda_L\cap\Lambda_{L_0}]=uv,
 \qquad \operatorname{vol}(L)/\operatorname{vol}(L_0)=u/v.
\tag{DO20.7}
\]

Use representatives x∈L/M and y∈L*/N* in the finite average. By(DO20.3), its value on1_{L₀} at t is

\[
 (uv)^{-1/2}\sum_{x\in L/M}\sum_{y\in L^*/N^*}
               \psi(-\langle y,t\rangle)1_{L_0}(t-x).
\tag{DO20.8}
\]

The possible support is N. For t∈N, finite character orthogonality makes the inner sum equal v when t∈L and zero otherwise. For t∈L there is exactly one class x∈L/M with t−x∈L₀. Hence(DO20.8) equals √(v/u)1_L(t). Multiplying by vol(L₀)⁻¹/² gives(DO20.6). In particular its value at position0 is strictly positive. This proof also gives

\[
 I_{L_3,L_2}I_{L_2,L_1}=I_{L_3,L_1}
\tag{DO20.9}
\]

on the corresponding lattice-vacuum line. Thus the triangle phase is1 and the two orders of moving the source and target Hom-lattice factors agree in this split scope.

### Comparison with the independently prescribed split Weil action

At a split place the unitary pair is GL_a(k)×GL_b(k). On its position Hom space, (g,h) acts by A:Z↦hZg⁻¹. Its determinant is

\[
                    \det_k A=(\det h)^a(\det g)^{-b}.
\tag{DO20.10}
\]

The explicit unitary Schrödinger change-of-variables operator

\[
 T_A\phi(t)=|\det A|_k^{-1/2}\phi(A^{-1}t)
\tag{DO20.11}
\]

has the requisite covariance, and sends v_{L₀} to v_{AL₀}. Its positive value at0 is vol(AL₀)⁻¹/².

Let ω(g,h) be the prescribed unitary Weil action and let its split-normalization character be

\[
             \chi_T(x)^{-1}\chi_S(y),\qquad
               x/\bar x=\det g,\quad y/\bar y=\det h.
\tag{DO20.12}
\]

Covariance transports(DO20.4), so ω(g,h)v_{L₀}=λv_{AL₀} for some λ; the elementary uniqueness of that line above suffices, without a further abstract irreducibility assertion. Unitarity gives |λ|=1. The functional ℓ(φ)=φ(0) is invariant under all momentum Heisenberg operators. It is therefore exactly a functional to which the source `om_split` condition applies. That condition gives

\[
 \ell(\omega(g,h)v_{L_0})
       =r\,\chi_T(x)^{-1}\chi_S(y)\,\ell(v_{L_0}),\qquad r>0.
\tag{DO20.13}
\]

Both ℓ(v_{L₀}) and ℓ(v_{AL₀}) are positive. Comparing(DO20.13) with λv_{AL₀}, and using |λ|=1, proves

\[
 \boxed{\omega(g,h)v_{L_0}
           =\chi_T(x)^{-1}\chi_S(y)\,v_{AL_0}.}
\tag{DO20.14}
\]

The positive scalar r is forced to be

\[
                    r=\bigl(\operatorname{vol}(L_0)/
                                  \operatorname{vol}(AL_0)\bigr)^{1/2}
                      =|\det A|_k^{-1/2}.
\tag{DO20.15}
\]

This computes both the phase and the positive normalizing factor. It does not silently discard the r in the source's split axiom.

### Global consequence for the mixed family

Apply this place by place to finite adelic g,h supported at relative split places. The finite quotients defining the global averages decompose into their primary components. The character and Heisenberg factors decompose in the same way; on the common lattice their weighted translation operators are an ordinary additive-group representation, so the local factors commute. The positive square-root normalization is the product of the positive local square roots. Consequently the two-step input φ_{N,N′} of(DO18.7) is exactly the product of the positive local lattice-vacuum vectors at the moved places, with the original factors elsewhere. Equations(DO20.6) and(DO20.14) prove(DO19.1) in this scope, with its determinant-root character and the common scalar θ₀^{ab} retained by(DO18.7).

For the even ranks of `StdPair`, the restriction of χ_S and χ_T to A_F^× is η_{E/F}^{even}=1. Therefore changing determinant roots by fixed-field ideles does not change(DO20.12). For arbitrary ranks the statement uses the specified supported determinant roots; one must retain the splitting's stated root dependence.

There is an explicit way to align additive-character signs with the recovered source. Use its ψ_F=(ψ_Q⁻¹)∘Tr_{F/Q}, whose real sign is−1, and set ξ₀=−ξ in `symplO`, where ξ=(ζ−ζ⁻¹)/7. Then ψ_F(Tr_{E/F}(ξ₀h))=ψ_Q(Tr_{E/Q}(ξh)), the actual Heisenberg central character used above. This is a simultaneous form/character transport, so it leaves the realized representation unchanged. It changes the old constructor's fixed quadratic ξ₀ condition, which is already part of the mixed-CM constructor gate. It does not assert that the unchanged source `StdPair.xi` is satisfied.

### A concrete rank-two to rank-four moved lattice

Take a=2, b=4, π=2−ζ, and r=π/bar(π). The exact norm is

\[
 N_{E/\mathbf Q}(\pi)=\Phi_7(2)=127.
\]

The primes (π) and (bar π) are distinct: ζ is2 modulo(π), while its inverse is64, and2≠64 in F₁₂₇. Put

\[
              N=rO_E\oplus O_E,\qquad N'=O_E^4.
\tag{DO20.16}
\]

The lattice N is Hermitian selfdual since r bar(r)=1. Its Hom lattice has four entries r⁻¹O_E and four entries O_E. For one changed entry,

\[
 O_E\cap r^{-1}O_E=\bar\pi O_E,
 \qquad [O_E:\bar\pi O_E]=[r^{-1}O_E:\bar\pi O_E]=127.
\]

Hence the exact global indices in(DO18.4) are

\[
                         q_1=127^4,\qquad q_2=1.
\tag{DO20.17}
\]

One may choose the finite adelic unitary element g with components diag(r,1) at127 and identity elsewhere, h=1. Its support is relative split because127≡1 mod7. A determinant root is the finite idele whose127-components are π and whose other components are1. For trivial splitting characters at these even ranks, the character in(DO20.14) is1, so the actual split Weil translate equals the explicitly averaged input, with no residual phase. The finite average has127⁴ terms and exact coefficient127⁻², before signs and Heisenberg characters. Its elementary coefficient denominator bound is v₁₂₇≥−2. Its fixed-embedding Gaussian bound is49⁸·127². Its exact analytic period in(DO18.7) isθ₀⁸, and its norm-one comparison scalar isθ₀⁸ det(2Y)². These are concrete values for this moved kernel family, not a terminal mass or a proof that a selected rank-four row lies in a global theta-lift image.

### What fails to transport at the ramified prime7

The recovered source phase proof is more specific than a generic metaplectic uniqueness argument. `.../KernelLattices/ColumnData/ColumnDataEquations/MuFinal.lean`, theorems `muOneL_of` and `muOneR_of`, uses `J.negOneNorm D (4*e)` to find an integral l with

\[
                         l\bar l\equiv-1\pmod{4e}.
\tag{DO20.18}
\]

Together with an even-rank row/column symmetry this makes the source's triangle factor1. The source `SplitPairOfGen.lean`, theorem `splitPair_of_gen`, explicitly obtains `IsCMUnram` from `HostDer.unramEF`.

For E=Q(ζ₇), (DO20.18) has no solution when7|e. Reduction at the unique prime above7 makes conjugation the identity on F₇, so the congruence would say l²=−1 in F₇. The squares are0,1,2,4 and do not contain6. This disproves that auxiliary congruence in the mixed example and prevents directly reusing that particular proof. It does not disprove the desired phase identity, which might be obtained with a different normalization or a more precise ramified computation. The present calculation closes split-place phases and leaves a sharply located nonsplit/ramified phase check, together with the independent global integral and terminal-mass gates.
