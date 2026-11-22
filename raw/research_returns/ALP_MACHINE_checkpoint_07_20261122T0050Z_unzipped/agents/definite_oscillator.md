# ALP_MACHINE: definite comparison and oscillator contribution

Author: GPT-6 Astra Pro, agent `/root/definite_oscillator`; effort inherited, not separately exposed. Run start 2026-11-21 19:35 UTC. These are work products for root integration, not a claim that all assigned tasks are finished.

## Source conventions and carried results

Use the supplied run names and statement numbers. The current run carries THETA3 A7, B9, B13, B15, B17, B19, B24 and GCT_PLETH T-052; it does not rerun their proofs. Exact local source paths follow below. The supplied source archive has reports and source manifests. In this run the needed Lean bodies were recovered centrally from the intake-pinned mirror, with hashes compared against the intake original-author archive metadata wherever that metadata contains the path. Later additional Rallis and TLiftK files have no author-hash entry in that comparison manifest and are identified as pinned-mirror reads in the events. The relevant definitions and proof bodies below were then read directly; no Lean execution or complete dependency audit is claimed.

1. `RETURN_THETA3_checkpoint_07_20261121T0604Z/documentation/paper_A7.tex`, equation (A7-lift), final two paragraphs: the multiplicity space P is totally definite exactly when the first-list complete CM type functions agree. In the balanced 2n-factor construction this forces all 2n type functions to agree, and the selected balanced tensor is divisor-generated.
2. `documentation/paper_B.tex`, B9, equations (B9a) and following coefficient calculation: the canonical right coefficient on U(2,1) has compact type det(A)d^{-2}, equivalently lowest compact weight (1,1;−2). For probability Haar and the compatible compact det test line, the LOCAL rank-zero Bessel integral is one. This is not a global period evaluation.
3. Same file, B13: actual MainX relation transfer comes from LawsX. Common geometry, tuple validity, finite support, common real action, double and last integral laws, kernel reduction, terminal factorization and row covariance are distinct hypotheses.
4. Same file, B15: literal one-active-place rank3 geometry has global Witt index zero, so abstract MainX length m=2; the remaining definite-side pattern is A2 → S → X2=T⊥Lz, with Lz of opposite sign to L. The small choice S2,T1 gives A2→S2→X2, equal ranks on the definite side. The relevant kernel identity is (B15m).
5. `documentation/paper_B17.tex`, (B17a)–(B17g): the adjoint double lift and its positive inverse are exact analytic constructions. Its upper space is A⊥H of signature (3,1) at every real place, even if P is totally definite. It is therefore not an instantiation of the arithmetic definite upper tower.
6. `documentation/paper_B19.tex`, (B19a)–(B19k) and final paragraph: actual CM-jet model and all period factors; the arithmetic functional is the fixed `abelian₂`, not a freely chosen linear functional. The proved StdPair kernel constructor requires both ranks even and strictly increasing.
7. `documentation/paper_B24.tex`, (B24a)–(B24e): in the repeated-type definite sector the actual integral Gram inverse is one specified positive scalar times an algebraic matrix. This is stronger than mere analytic existence but does not identify the MainX kernel or terminal masses.
8. `RETURN_GCT_PLETH_checkpoint_09_20261121T0546Z/work/theta/oscillator_charge_report.md`, T-052, (OC.1)–(OC.12), (OC.20)–(OC.22): r=m−2, pair U(r,1)×U(m), polynomial Fock space C[X_ai,Y_i], and all vacuum shifts.

Primary literature for the last convention: Basile, T., Joung, E., Mkrtchyan, K., & Mojaza, M. (2020), *Dual pair correspondence in physics: Oscillator realizations and representations*, arXiv:2006.07102v2, §5.2, equations (5.21)–(5.30), printed pp.29–31. This source was opened anew at https://arxiv.org/html/2006.07102v2 and https://arxiv.org/pdf/2006.07102. The new obstruction below is a calculation from the carried T-052 operators, not a claim of a theorem appearing in Basile et al.

## AM-DO-001. Explicit repeated-type definite geometry over Q(ζ7)

Let ζ=exp(2πi/7), E=Q(ζ), F=Q(ζ+ζ^{-1}), and a=ζ+ζ^{-1}. Index the three real embeddings by a↦2cos(2jπ/7), j=1,2,3. The signs of a are (+,−,−). In fact its minimal polynomial is t³+t²−2t−1, so it is an algebraic integer and a unit. Put δ=ζ−ζ^{-1}. Its imaginary parts at the complex extensions σ1,σ2,σ3 are all positive.

Carry the CM type Φ={1,2,3} of J=Jac(y²=x⁷−1) from DP_MULT DP45/DP49. Let v be its odd type function on (Z/7Z)×. The inverse type d(σ)=v(σ^{-1}) has signs (+,−,−) on σ1,σ2,σ3, since 1^{-1}=1, 2^{-1}=4, 3^{-1}=5 modulo7. Therefore the rank-one Hermitian form h_P=−a has exactly the required signs −d(σ)sign Imσ(δ) from THETA3 A6. Take both first-list types equal to v and

    V=(E³,diag(1,1,−a)),  L=Ee3,  A=L⊥=(E²,I2),
    P=(E²,δ(−a)I2) as a skew-Hermitian space.

Then V has signature (2,1) at σ1 and (3,0) at the other real places; A is totally positive definite and U(P) is compact at all real places. Its Hermitian sign model is (0,2) at σ1 and (2,0) elsewhere. V and P are globally anisotropic because each has a definite real completion. These are actual global forms over E/F, not separately prescribed incoherent local signatures.

For any nonzero ξ0∈E with ξ0^c=−ξ0 put q=N_{E/F}(ξ0)>0 at every real place and Lz=−q^{-1}L. Its Gram entry is a/q. Taking T=Lz gives X2=T⊥Lz with Gram (a/q)I2: positive at σ1 and negative at the other real places, hence totally definite. For the explicit ξ0=√−7/7, q=1/7, its Gram is 7a I2. Here √−7 can be taken as ζ+ζ²+ζ⁴−ζ³−ζ⁵−ζ⁶; its square is−7 by reduction modulo Φ7. The exact field identities and inverse-type signs are also recorded by `definite_oscillator_geometry.py` and its JSON receipt. The identity line map satisfies G_L=−q G_Lz exactly, as required by the abstract last seesaw relation.

Proof: all signatures follow from the displayed cosines and the inverse type calculation; the line relation is −a=−q(a/q). The compactness criterion and the interpretation as the repeated-type A7 multiplicity space are carried A7 inputs. The polynomial identity for a follows by ζ⁷=1 and ζ≠1. No global theta nonvanishing or arithmetic MainX law is claimed merely from this geometry.

Scope: A7 supplies nonzero canonical wedges in this repeated-type family after suitable inputs and level. If a balanced last pair is requested, it must have the same type v, so this family addresses divisor-generated lines. The alternatives (adjoint T=V versus arithmetic T=Lz) remain different. The former has indefinite upper X4 and an actual analytic inverse; the latter has definite X2 but still requires a global reverse lift, actual finite classes, kernel equations, and terminal masses. This construction does not give their numerical values.

## AM-DO-002. A canonical compact-weight obstruction for the charged oscillator

### Precise statement

Let m≥3, r=m−2, and let ω_m be the polynomial oscillator of T-052, with the fixed positive-energy convention and dual pair U(r,1)×U(m). On G=U(r,1) let K=U(r)×U(1). Let π_can be the irreducible canonical holomorphic discrete-series Harish–Chandra module with lowest K type

    κ_can(A,d)=det(A)d^(−r).

For r=2 this is exactly THETA3 B9/B15's canonical ball-surface coefficient, with lowest weight (1,1;−2). There is no nonzero (g,K)-map from ω_m or any of its algebraic subquotients to π_can, nor from π_can to any such subquotient. The same holds after arbitrary determinant character twists of either representation and after a simultaneous contragredient convention. In particular no charge-respecting intertwiner can identify a T-052 component with this canonical 032 component.

For odd m the bare oscillator may live on the metaplectic preimage of K. In that case every displayed map means a (g, K̃)-map on a common cover, with π_can pulled back; equivalently the obstruction can first be read at the complexified Lie algebra and the traceless compact circle. Its generator H has the integral spectrum computed below, independently of the individual half-vacuum weights. This convention is already part of T-052 and does not assume an unprovided descent of the bare representation.

The statement concerns the canonical automorphic component, not arbitrary maps between entire oscillator representations after changing dual pairs, groups, coefficient systems, or taking additional tensor factors. When comparing precisely the ball surface U(2,1), the T-052 matching rank is m=4,r=2.

### Full proof

T-052 (OC.7) gives

    A_ab=Σ_i X_ai ∂_X_bi+(m/2)δ_ab,
    A_00=−Σ_iY_i∂_Y_i−m/2.

Let h=diag(1,…,1,−r) in the complexified compact Lie algebra. Its imaginary multiple generates the compact circle c(z)=diag(zI_r,z^(−r))⊂SU(r,1). Its infinitesimal oscillator action is

    H=Σ_a A_aa−r A_00=N_X+rN_Y+rm.

All monomials in the polynomial Fock model have N_X,N_Y≥0. Thus the H spectrum lies in rm+Z_{≥0}. More precisely it is rm+N_X+rN_Y. The action is diagonal on a monomial basis. Its restriction to every invariant subspace remains semisimple with this same lower bound; every algebraic quotient has only these eigenvalues as well, since it is the direct sum of its circle weight quotients.

The canonical character on c(z) is

    det(zI_r)(z^(−r))^(−r)=z^{r(r+1)}.

But rm=r(r+2)>r(r+1). Therefore the lowest K type of π_can does not occur in ω_m, or in any subquotient. A nonzero homomorphism from the irreducible π_can is injective, contradicting absence of its lowest K type. A nonzero homomorphism to π_can is surjective; exactness of taking an isotypic component for the compact circle (or simply its semisimple weight decomposition on K-finite vectors) would then force its lowest-circle-weight vector to have a preimage of that weight. Again impossible.

Every determinant character is trivial on c(z), since det c(z)=1. Changing the unitary splitting only adds such determinant characters to the fixed pair, so cannot change H. A unitary equivalent realization obtained by changing the polarization preserves the action and its spectrum. Simultaneously passing to contragredients negates both spectra; the distinguished weight −r(r+1) still lies outside the new spectrum, bounded above by −rm. The same absence argument applies. This completes the proof.

### Exact charge calculation

On the simultaneous charge-k subspace of T-052, with Q_i=Σ_aX_ai∂_X_ai−Y_i∂_Y_i=k, one has N_X−N_Y=mk. If b=N_Y, then

    H=m(k+r)+(r+1)b.

The canonical equality would require m k+(r+1)b=−r, impossible for the T-052 parameters k,b≥0. For m=4,r=2 this reads 4k+3b+8=6. The contradiction is already present before charge selection.

One can also restrict the standard U(r,1) factor to a standard U(2,1) subblock for any m≥4. Its traceless compact circle generator has spectrum N_X,selected+2N_Y+2m≥2m≥8, whereas the canonical ball-surface coefficient has weight6. Thus this standard restriction does not evade the obstruction.

### Check scope and consequence

This is a local archimedean obstruction. It survives global choices of finite Schwartz vectors, Haar measures, finite levels, and CM periods. It does not show that every conceivable comparison with Alpöge is impossible. It specifically excludes a route which first identifies T-052's actual charged module with the canonical 032 component while preserving the indicated group action. Q-ALPOGE and Q-ALPOGE-METHOD remain open for changed weights, other coefficient systems, auxiliary oscillator factors, or comparisons not passing through that component.

## AM-DO-003. Partial Fourier comparison with a definite dual pair, and its exact category obstruction

### Algebraic statement

Over Z let A be the Weyl algebra on coordinates X_ai,Y_i and derivations ∂_X_ai,∂_Y_i, with [∂_u,u]=1. Let A' be the Weyl algebra on X_ai,Z_i. The assignments

    X_ai↦X_ai,  ∂_X_ai↦∂_X_ai,
    Y_i↦∂_Z_i,  ∂_Y_i↦−Z_i

define a Z-algebra isomorphism F:A→A'. (For the half-integer oscillator constants extend coefficients to Z[1/2].) It carries the T-052 complex Lie algebra operators into the definite compact-pair oscillator operators for U(r+1)×U(m), conjugating the first matrix action by diag(I_r,−1):

    F(A_ab)=Σ X_ai∂_X_bi+(m/2)δ_ab,
    F(A_00)=Σ Z_i∂_Z_i+m/2,
    F(A_a0)=−Σ X_ai∂_Z_i,
    F(A_0a)=−Σ Z_i∂_X_ai,
    F(B_ij)=Σ X_ai∂_X_aj+Z_i∂_Z_j+((r+1)/2)δ_ij.

The exact transformed charge is

    F(Q_i)=Σ_a X_ai∂_X_ai+Z_i∂_Z_i+1.

Thus the scalar shift1 is mandatory; charge does not become the unshifted compact column degree.

Integrally, “Weyl algebra” here means precisely the algebra generated by coordinate multiplication and the ordinary derivations. It is not the full Grothendieck ring of differential operators over Z. Accordingly the target below is an integral Weyl-algebra module; after tensoring with Q it is the usual algebraic delta D-module. No divided-power differential-operator action, stratification, or crystalline Frobenius is supplied. EGA IV4, Theorem16.11.2 p54 and Remarks16.11.3(ii) p55, gives the exact distinction: the integral differential-operator basis consists of divided derivatives, and ordinary derivations do not generate them in general. This primary text was read anew.

### Full proof of the algebra identities

The only nontrivial defining relation is [−Z_i,∂_Z_j]=δ_ij; all mixed generators commute as required. The inverse sends Z_i↦−∂_Y_i and ∂_Z_i↦Y_i. For A_00 use ∂Z_i·Z_i=Z_i∂Z_i+1. For B_ij use ∂Z_j·Z_i=Z_i∂Z_j+δ_ij. The resulting constants are −m/2+m=m/2 and (r−1)/2+1=(r+1)/2. The off-diagonal signs are both negative and are exactly conjugation by diag(I_r,−1). The charge formula follows from the same normal ordering. These calculations prove all displayed identities.

### The actual module and why it is not the definite Fock space

Let Mδ be the A'-module with cyclic vector δ satisfying Z_iδ=0 and ∂_X_aiδ=0. As a Z-module it has basis X^u∂Z^vδ. The map

    U:Z[X,Y]→Mδ,  X^uY^v↦X^u∂Z^vδ

is a bijection and satisfies U(a f)=F(a)U(f). Indeed, multiplication by Y becomes ∂Z, and −Z_i∂Z^vδ=v_i∂Z^{v−e_i}δ reproduces ∂Y_i. X and ∂X are unchanged. This proves exact equivariance and shows that U preserves the ORIGINAL charges, using their transformed shifted operators. In particular Z_i∂Z_i acts on ∂Z^vδ by −(v_i+1), so the transformed charge is deg_X,column−v_i as required.

Over C, Mδ is the algebraic D-module generated by the delta section on the subspace Z=0. It is not the ordinary holomorphic polynomial Fock module C[X,Z]. There is NO nonzero linear map L:C[X,Y]→C[X,Z] satisfying L(a f)=F(a)L(f) for every Weyl generator. For f=1, ∂Y_i1=0 forces −Z_iL(1)=0, and multiplication by Z_i is injective on C[X,Z], so L(1)=0. The source is cyclic under coordinate multiplications, so L=0.

It is also not a unitary oscillator intertwiner. In positive Fischer/Fock structures Y_i†=∂Y_i and (∂Z_i)†=Z_i, whereas F(∂Y_i)=−Z_i. Thus F fails the adjoint relation. It is a complex symplectic transformation of the algebraic Weyl algebra, not a real metaplectic equivalence of these positive-energy representations. No splitting character changes this Heisenberg adjoint obstruction.

### Consequence for the actual problem

There is an explicit algebraic comparison between the formulas underlying T-052 and a totally definite compact dual pair. Its landing object is a delta D-module and its charge has the displayed shift. It does not map the prescribed Schwartz/Fock theta inputs to the corresponding definite theta inputs, and therefore does not prove any of Alpöge's lift identities, quantitative nonvanishing, or the plethysm complexity claims. Conversely it prevents the overly strong statement that there is no comparison of any kind: there is a precise comparison after changing category.

## Current state of THETA3 G1

The exact arithmetic equation, inherited B15m, is

    volLev(X_j,U_{j,α}) θ_{K,j}(h_{j,α,a},h_{j+1,γ,a'};Φ_{j,P})
      = c_{K,j} abelian₂_{j,α,γ,a,a'}(mvZ(1,s_{j,τ}I)(castP P)).

The functional `abelian₂` is fixed by the specified arithmetic theta section, its character factors, and its period frame. It cannot be defined post hoc from the analytic left side. The terminal condition `ClsT.Is.tail` includes top-level covolumes and reciprocal stabilizer masses. Its exact recovered statement has now been read directly in `OnFramesRdApply.lean`, `ClsT.Is.tail`:

    volLev(T,U_T) Σ_{β,a} stabOrd(U_T,h_a)^(−1)
       ell_{β,a,G}(low(rd_m(ψ) evaluated on emb(h_a,1)))
      = cP·tail(ψ,G).

The separate `top` clause says that the translated terminal automorphic function at h_a k is the functional ell_{β,a,G} applied to the fixed archimedean coefficient J(v,k). Thus the terminal equation must match the actual top representation and its branching map; it is not merely the total mass of the finite class set.

Paths: `Development/AbelianVarietyTheory/Definitions/LatticeFrames/OnFramesRdApply.lean`, `ClsK.Core` lines108–113, class masses115–121, `ClsT.Is.tail`147–150, `ClsPinD`152–153; `LevChiEqOne.lean`, `abelian₂`73–77; `SplitPart.lean`, `StdPair`38–49; `KernelPartLawsOfColumnPins.lean`, `clsKL_is`22–52; `ThetaKernelSplitPlacesEqJetClassicalTheta.lean`, `thetaKernel_eq_jet_thC`46–71.

Approaches inspected:

- Repeated CM type supplies an actual totally definite P, and AM-DO-001 makes the forms explicit over the same cyclotomic field as the main Jacobian. It leaves the finite class matrices and global reverse lift unconstructed.
- The exact adjoint double lift B17 has an indefinite upper space. Repeated types do not fix that signature; this is a carried source conclusion.
- The B15 rank-one terminal alternative has the required upper signature and locally compatible archimedean representations, but neither finite local occurrence for the chosen global data nor the global reverse realization is supplied.
- B24 makes the actual kernel inverse algebraic up to one retained scalar in this sector. Algebraicity/proportionality of an inverse is not equality with the fixed MainX functional, and cannot set terminal masses.
- The StdPair constructor only covers strictly increasing even ranks. It cannot directly be applied to the natural rank2/3 analytic pair, nor to the small equal-rank definite side. This is a limitation of that constructor, not a proof that abstract MainX is impossible.
- Arbitrarily rescaling a test vector to make one Bessel period equal1 does not solve the common kernel equations; that would lose the fixed input and uniformity.

Thus question2 is not settled by this contribution. Its current gate is simultaneous construction of the chosen global two-step theta representation and finite arithmetic class/jet matrices, with exact covolumes and terminal masses, for the concrete repeated-type data. No pairing value satisfying MainX has been computed here.


## AM-DO-004. A simultaneous sign obstruction to the common positive arithmetic pin

### Statement with all hypotheses

Let E/F be a CM extension and let X0,X1,X2 be nonzero Hermitian spaces, each definite at every real place, with signs ε_j(τ)∈{+1,−1}. On the oriented matrix space W_j=Hom_E(X_j,X_{j+1}) use the exact source form

    h_j(x,y)=tr(G_j^(−1) y* G_{j+1} x),
    B_j(x,y)=Tr_{E/F}(ξ0 h_j(x,y)),  ξ0^c=−ξ0.

A **label-preserving positive transport** means: identify each abstract matrix group with the corresponding positive definite one, replace all node Gram matrices by positive definite ones, use one common ξ0 and one common additive character ψ_b(x)=ψ(bx) (b∈F×), and identify each oriented matrix oscillator space by an E-linear map, intertwining the fixed two group actions and carrying its Heisenberg form to the new form with that common additive character. No conjugation of the E action, exchange with a contragredient, or separate additive character for different edges is allowed in this definition.

A necessary condition for such a transport is

    ε_j(τ) ε_{j+1}(τ)=sign τ(b)   for j=0,1,

and hence ε0(τ)=ε2(τ) at every real place. More generally in a chain all even-indexed node signs must agree and all odd-indexed node signs must agree.

For the literal rank-zero MainX geometry of a one-active-place compact 032 ball surface, this necessary condition fails at every compact real place. Consequently its signed definite side cannot be transported to the common all-positive `PinX`/`StdPair` geometry by label-preserving positive transports, even after one common change of additive character. This does not refute the abstract signed `MainX` construction.

### Exact source locator

`Formalism/LocalToGlobal/IndefiniteReal/LocalNewformFunction.lean`: `hO` lines25–26, `symplO`28–29, `heisO`34–35, `actO`37–38, and `IsWeilDatumO.om_heis`62–63. The actual formula uses the SOURCE Gram inverse; this is why a scalar edge ratio is q_{j+1}/q_j rather than its product.

`Development/AbelianVarietyTheory/Definitions/LatticeFrames/SplitPart.lean`: `StdPair.gS`, `gT`, `cc`, `xi`38–49. `LevChiEqOne.lean`: `PinX.xs` and `vc` specify Cartan involution1, orthonormal frame1 and standard lattice for every node, all with the same ψ. The abstract `DefSp.Is.pm`, in `JointSmooth.lean`, instead allows signs+1 or−1 separately at every real place. `PlaceLaws.lean`, `WeilOK.tau`165–166, imposes the opposite-line Gram equation.

### Full proof

Fix a real place τ. Write G_j=ε_j P_j with P_j positive definite. For x≠0,

    h_j(x,x)=ε_j ε_{j+1} tr(P_j^(−1) x* P_{j+1} x).

The trace on the right is positive: it is the sum of squared absolute values of the matrix P_{j+1}^{1/2} x P_j^{−1/2}. Thus h_j is definite of sign ε_j ε_{j+1} on the complex vector space W_j.

Let h_j^+ be the Hermitian form for the transported positive pair and T_j the required complex-linear map. Equality of the real symplectic forms with additive-character scaling says

    Tr_{C/R}(ξ0 h_j(x,y))
      = b Tr_{C/R}(ξ0 h_j^+(T_jx,T_jy)).

Because T_j is complex linear, replacing x by ix also gives equality of the complementary real part. Since ξ0 is nonzero purely imaginary, the two real equalities imply

    h_j(x,y)=b h_j^+(T_jx,T_jy).

For x=y≠0 the right side has sign sign b. Therefore sign b=ε_j ε_{j+1}. Multiplying the two edge equalities gives ε0ε2=(sign b)^2=1, proving the necessary condition. Repeating this argument along the chain proves the parity assertion. The same proof covers arbitrary positive Gram matrices; it is not limited to scalar forms.

For the ball surface, write V=A⊥L and X2=T⊥Lz in the literal m=2 last-step pattern. At a compact real place τ, V is definite, so A and L have the same sign. The exact line relation

    τ_line* G_L τ_line=−N_{E/F}(ξ0) G_Lz

has a totally positive norm factor, and therefore Lz has the opposite sign to L. Since X2 is definite and contains Lz, it has Lz's sign. Hence X0=A and X2 have opposite signs at τ. This contradicts the necessary condition. Such a compact real place exists because the 032 construction under discussion has [F:Q]>1 and only one active place.

This argument does not say that U(qI) and U(I) are different algebraic groups; they are literally the same matrix group. It says that the E-linear symplectic embeddings and their common Heisenberg character cannot simultaneously be the positive ones. Splitting-character twists multiply group actions by determinant characters but do not change the Heisenberg commutator form, so they cannot remove this obstruction. A common change ξ0↦cξ0 is already absorbed into b. Changing the middle sign multiplies both edge signs by−1 and still leaves them opposite. Rescaling the original definite completion of V changes both A and L together and again leaves the endpoint sign opposition unchanged. This completes the proof.

### The scalar equations after fixing a Hermitian middle-space conversion

The endpoints of AM-DO-001 have q0=1 and q2=a/q, where q=Nξ0>0. Its middle object P is initially skew-Hermitian, with Gram δ(−a)I2. A comparison with the oriented Hermitian `hO` model must first specify the skew-to-Hermitian conversion, the source-dual convention and the group labels. In particular one must not silently declare the middle Hermitian Gram to be −aI2 while independently choosing ξ0. Suppose that actual conversion gives a scalar Hermitian Gram q1=s∈F×. The edge ratios are then

    r0=s,   r1=a/(qs).

An E-linear scalar matrix map x↦c_jx into the standard positive model would have to satisfy

    b N_{E/F}(c_0)=s,
    b N_{E/F}(c_1)=a/(qs).

Their product gives b²N(c_0c_1)=a/q, independently of s. The left side is totally positive, while a/q has two negative real embeddings. Thus there is no solution. If a compatible convention separately proves s=−a, the displayed equations specialize to bN(c0)=−a and bN(c1)=−1/q; that specialization is not an additional claim here. The obstruction itself uses only the endpoints and the necessary real sign of a norm, so neither the unresolved middle conversion nor possible finite norm obstructions affect this exclusion.

### Meaning for the open questions

This refutes one concrete attempt to solve THETA3 G1: transport both edges of its literal two-step definite side into the already-built positive-identity arithmetic kernel constructor while keeping the E labels, charges and a common additive character. It leaves the signed arithmetic kernel/covolume equations themselves open. They would require a new signed CM-type comparison (or a different global realization), with explicit conjugations, characters and periods. The theorem does not obstruct Q1's already-positive abstract definite tower; it is specific to importing the 032 one-active-place geometry into that same positive pin.

### Extension allowing whole-edge E/F conjugation

The same route still fails if each edge identification is allowed to be either E-linear or E-conjugate-linear globally over F, with the corresponding conjugation of its group labels. Write η_j=+1 in the former case and η_j=−1 in the latter. Each η_j is independent of the real place: the only nontrivial E/F automorphism is complex conjugation at all of them. The necessary condition becomes

    sign τ(b)=η_j ε_j(τ) ε_{j+1}(τ),
    ε0(τ) ε2(τ)=η0η1.

To prove the first equality, the E-linear case is already proved. In the conjugate-linear case, put T(ix)=−iT(x) in the two symplectic equalities. They give h_j(x,y)=−b overline(h_j^+(T x,T y)), so the sign is −sign b. Multiplying the two edge conditions proves the second equality.

For the one-active-place ball geometry, ε0ε2 is +1 at the active place because A and Lz are both positive, and −1 at every compact place because Lz has the opposite sign to A there. It is therefore not constant, contrary to η0η1. Thus whole-edge global conjugation does not repair the obstruction either. Independent conjugations at selected real places are not E/F-semilinear maps of the rational oscillator space; no claim about constructions that replace that global space and its rational theta lattice is made here.

## Additional source and proof checks

After recovering the actual Lean files, the agent read all of `OnFramesRdApply.lean` through the ClsK/ClsT definitions and conversion lemmas; all of `ValLastX.lean`; `StdPair` and `xiN` in `SplitPart.lean`; `TwDat`, `abelian₂`, `PinX`, `PinColT` in `LevChiEqOne.lean`; `DefSp`, `KerDat`, `BesAt`, `JacAt` in `JointSmooth.lean`; `WeilOK` in `PlaceLaws.lean`; and the complete proof bodies `clsKL_is` and `thetaKernel_eq_jet_thC`. The dependency chain has not been compiled or audited in full.

Root's AM-R-002 was independently whole-read and checked: content ideal and local detector denominator, dual norm and quotient by kernel, scaling/product-formula invariant, arithmetic-degree sign, actual normalized coefficient matrix and stabilizer masses all pass. Its formula must be applied to the actual terminal lift vector and actual invariant lattice; it does not supply them for the present signed seesaw.


## AM-DO-005. An explicit charge-preserving local bicanonical comparison

This gives a nonzero comparison after changing the target coefficient weight. It is included to make the exact scope of AM-DO-002 clear; it does not turn the canonical 032 class into an Alpöge arithmetic column.

### Data, splitting and polarization

Set m=4, r=2 in T-052. The real dual pair is U(2,1)×U(4) acting on the real symplectic space underlying C^{2,1}⊗C⁴, with the T-052 convention ω=Im(h_{2,1}⊗h_4). Use its positive compatible complex structure i on the positive summand and −i on the negative summand. The polynomial Fock space is C[X_ai,Y_i], a=1,2 and i=1,…,4. On K_G×U(4) the bare vacuum character has square

    χ0²=(det A)^4 d^(−4) det g,

so it is (det A)²d^(−2)χ_W(g), with χ_W²=det g on the indicated metaplectic pullback. These are the exact T-052 conventions, not newly inferred global splitting data.

Twist the G=U(2,1) action by det_G^(−2), and untwist the compact U(4) factor by χ_W^(−1), just as T-052 untwists its ordinary column action. Both combined actions then descend in this selected model. The former is an honest determinant character. In the archive's `splitFacO` convention, changing the character attached to the compact member by κ(z)=(z/\bar z)² produces this det_G^(−2) factor: if x/\bar x=det g, then κ(x)^(−1)=det(g)^(−2). This states the splitting CHANGE relative to the fixed model; it does not invent a global absolute character or its finite components. The polarization is unchanged.

### Explicit lowest vector and intertwiner

Put Δij=X_{1i}X_{2j}−X_{1j}X_{2i} and f=Δ12Δ34. Then

    C_1 f=C_2 f=0,    Q_i f=f for every i,
    (N_X,N_Y)=(4,0),  α=(2,2), k=1, b=0.

Each column occurs once and f contains no Y, which proves the first two assertions directly. Under U(2), f transforms as det²; with the vacuum shifts, its bare lowest K_G weight is (4,4;−2). After the determinant twist it becomes (2,2;−4), the bicanonical compact type from THETA3 B14. Its restriction to the traceless compact circle has weight12, consistently with H=8+N_X+2N_Y. This does not contradict AM-DO-002, which excludes weight6.

The polynomial f expands into four distinct squarefree monomials, each with coefficient±1. Under the Fischer norm its squared norm is therefore4. Let e=f/2. The G-cyclic module generated by e lies in the T-052 irreducible lowest-weight Howe summand indexed by α=(2,2),b=0. This irreducibility is a carried T-052 (OC.6),(OC.20)–(OC.22) input, not an assertion made for an arbitrary lowest vector. After the determinant twist it is the irreducible bicanonical holomorphic discrete series π_2.

Choose a unit lowest vector v_2 in a fixed π_2 model. The explicit intertwiner on algebraic vectors is

    I(u·e)=u·v_2,   u∈U(gl_3(C)),

where the action on the source includes the det^(−2) twist. This is well-defined: the carried irreducible lowest-weight identification gives the same annihilator ideal of the fixed lowest type in the two modules; equivalently both are the same irreducible lowest-weight quotient. It is a bijection. Its unit-vector normalization fixes its scalar uniquely, and invariance of the positive forms makes it unitary on completion. Because the G action commutes with every Q_i, its whole domain has charge(1,1,1,1). Thus the comparison preserves the prescribed charge sector.

An actual nonzero coherent target may be obtained from any nonzero canonical wedge ξ supplied by A7: ξ² is a nonzero section of K_X², and its automorphic coefficient generates a copy of π_2. This observation specifies the archimedean recipient. No compatibility with the finite Weil action or membership in the global U(4) theta image follows from it.

### The multiplicity factor cannot be discarded

The charge-one lowest space is the multilinear component of S_(2,2)(C⁴). It has basis

    f1=Δ12Δ34,  f2=Δ13Δ24,

with the third pairing f3=Δ14Δ23 satisfying f1−f2+f3=0. Their Fischer Gram matrix is [[4,2],[2,4]]. The ordinary S4 action is its irreducible Specht module [2,2], of dimension2. This is also T-052 (OC.4) at n=1,λ=(2,2,0,0), with its vacuum untwist. Consequently the full charge-selected local comparison retains

    π_2 ⊗ [2,2],

rather than mapping the S4 multiplicity to a scalar. For example choose the two orthonormal lowest vectors e1=f1/2 and e2=(f2−f1/2)/√3 and send u·e_j to (u·v_2)⊗w_j, where w1,w2 are the corresponding orthonormal basis of [2,2]. This fixes the whole G×S4 intertwiner; S4 acts through its exact Gram-compatible matrices on the second factor.

For all n≥1 this is the T-052 parameter family λ=(n+1,n+1,n−1,n−1), since α=(2,2),k=1,b=0. The ordinary S4 comparison may include the source's sign^(n+1), but [2,2] is self-conjugate and hence unchanged up to its specified Specht isomorphism. This parameter observation is carried from (OC.1) and (OC.4), not a new plethysm computation.

### A normalization with an actual local value

For the compact subgroup U(2)⊂U(2,1), e1 has character det² in the twisted representation. With probability Haar measure and the compact test representation det²,

    ∫_{U(2)} <e1,π_2(diag(A,1))e1> det(A)^(−2) dA=1.

The integrand is identically1. This is precisely the q=2 specialization of the carried THETA3 B9/B14 local calculation. It is not the global kernel/covolume or terminal-mass value requested in question2.

### Consequence

A blanket assertion that no charge-preserving comparison with a ball-quotient representation exists would be false: this is one, with the dual pair, covering/splitting adjustment, polarization, vector, multiplicity factor and normalization given explicitly. It uses a bicanonical coherent section. THETA3 B14 shows why that differs from the ordinary canonical cohomology class and why a diagonal cup-product argument does not return it to that class. Finite-place compatibility, actual global theta occurrence, arithmetic columns and controlled period costs remain separate. Q-ALPOGE and Q-ALPOGE-METHOD therefore remain open in their original global form.

## AM-DO-006. Full charge torus obstruction to a polarized compact tensor comparison

### Exact scope and statement

Keep the T-052 positive polarization and m≥3, r=m−2. Let T=(U(1))^m be the individual column-charge torus. Its action on the creation space E_m has character multiset

    E_m = ⊕_{i=1}^m (C_{e_i}^{⊕r} ⊕ C_{−e_i}),

where e_i are the independent coordinate characters. In particular dim_C E_m=m(m−1). Vacuum and splitting characters do not occur in this formula: these are the commutator weights on creation operators, so a scalar twist of the whole oscillator cancels.

A **polarized full-charge tensor comparison** to a totally definite dual pair U(a)×U(b) means a real symplectic isomorphism of the full Heisenberg spaces, preserving the specified positive compatible polarizations, together with a torus homomorphism T→U(a)×U(b), such that the isomorphism intertwines the individual charge torus. The two compact factors may be dualized, and either common orientation of the symplectic form may be used. These changes only dualize one or both defining representations and do not change their tensor-product form. A comparison of this kind requires ab=m(m−1).

There is no such comparison with a,b≥2. In particular, even when dimensions happen to agree, it cannot identify the T-052 full charged oscillator with a single one of Alpöge's nonzero even-rank, totally definite tensor-pair oscillators while keeping all individual charges and the indicated positive polarizations.

This statement does not concern a map only on a chosen simultaneous-charge eigenspace, a map of Harish–Chandra modules which does not intertwine the Heisenberg action, changes of the real form or polarization not identified in the hypothesis, extra oscillator factors, or a rank-one compact factor. It is a precise obstruction to one proposed direct comparison, not a proof that Q-ALPOGE has no solution by any method.

### Elementary support lemma

Let m≥3 and S={±e_1,…,±e_m}⊂R^m. If A and B are nonempty finite sets of vectors with A+B=S, then A or B is a singleton.

Proof. Suppose each set has at least two elements. Choose distinct α,α′∈A and β,β′∈B and form

    x=α+β,  y=α′+β,  z=α+β′,  w=α′+β′.

All lie in S, and x+w=y+z. Adjacent vertices in this displayed rectangle differ, because the selected α's and β's differ. If x=w, then x=(y+z)/2; y≠z, since otherwise x=y would follow. This contradicts the fact that every element of S is an extreme point of its convex hull. The same argument excludes y=z. Thus x,y,z,w are four distinct elements of S.

The sum of two distinct elements of S is either zero, when they are opposite, or a vector with exactly two nonzero coordinates equal to ±1. In the latter case the sum uniquely determines the unordered pair of vertices. Since the two pairs {x,w} and {y,z} are disjoint, their common sum must therefore be zero. Hence

    α+α′+β+β′=0.

Now fix α,α′ and β and vary β′ over B\{β}. This equality determines β′ uniquely. It follows that B has at most two elements. By symmetry A has at most two elements. But then A+B has at most four elements, whereas S has 2m≥6. This contradiction proves the lemma. The proof uses no lattice or integrality hypothesis. ∎

### Full proof of the representation obstruction

Preservation of the positive polarization identifies the complex creation spaces equivariantly for T. Restrict the defining a- and b-dimensional compact-factor representations along the claimed torus homomorphism. Compactness makes each a direct sum of characters. Write their character multisets as {α_1,…,α_a} and {β_1,…,β_b}, absorbing any contragredient into the signs of these characters. The creation space of the definite tensor pair then has character multiset

    {α_p+β_q : 1≤p≤a, 1≤q≤b}.

All multiplicities are nonnegative, so its support is exactly A+B, where A and B are the two character supports. The required isomorphism forces A+B=S. By the support lemma one factor, say A, consists of one character α. That factor representation therefore consists of a copies of α. Every character multiplicity in its tensor product is divisible by a. But every negative character −e_i in E_m has multiplicity1. Consequently a=1. If B is the singleton, the same argument gives b=1. Either conclusion contradicts a,b≥2.

This proof also shows why scalar splitting shifts do not help. They only multiply an entire oscillator representation by a character; the adjoint weights of the creation operators remain unchanged. If one allows an affine common shift of all creation weights in an intermediate notation, it can be absorbed into one factor's α's before applying the same argument. Passing to a common cover to define half-integral vacuum characters similarly leaves the proof intact. ∎

### Algebraic geometry and K-theory form

For the split torus T_Z=G_m^m the creation module is the free T_Z-equivariant vector bundle

    E_m = ⊕_i (L_{e_i}^{⊕r} ⊕ L_{−e_i})

on Spec Z, with character class rΣ_i t_i+Σ_i t_i^(−1) in K_0^{T_Z}(Spec Z)=Z[t_1^±1,…,t_m^±1]. The theorem says that this positive character cannot be a product of two positive character classes of ranks at least2. The adjective positive means actual representations or vector bundles; virtual K-theory factorizations with negative coefficients are not excluded. Thus an ordinary Grothendieck-group equality is weaker than the tensor-bundle identification needed for the positive oscillator construction.

The exact Grothendieck-framework locator for the weight decomposition is SGA3, Exposé I, Proposition4.7.3; Corollary4.7.3.1 gives its graded-algebra/equivariant-affine-scheme form. Both were read anew in the French recomposed text. The relevant archive framework in the supplied materials is cote133 scan006 (pre-λ Grothendieck groups and universal identities in classifying topoi), while the exact mathematical input and new statement are T-052 (OC.3), (OC.7)–(OC.12) and AM-DO-006 here. No assertion that SGA3 or cote133 proves this factorization obstruction is made.

## AM-DO-007. Canonical rank cap for a compact middle source

### Statement

For the real dual pair U(n,1)×U(d), let the second factor be totally definite and n≥1, d≥1, q≥1. In the positive-energy orientation, if the irreducible holomorphic coefficient representation of the qth canonical power occurs as a subquotient of the oscillator, with arbitrary determinant splitting twists, then

    d≤q(n+1).

The same necessary bound holds in the simultaneous contragredient convention. In the opposite oscillator orientation with the original holomorphic target, no occurrence is possible. As in AM-DO-002, the comparison is made on a common metaplectic cover when necessary.

For the unchanged canonical coefficient of the 032 ball surface, n=2 and q=1, the compact source must have d≤3. Therefore the first definite edge A_2→S_d in a literal MainX realization cannot at the same time satisfy the existing `StdPair.rk` conditions d>2 and Even d. Enlarging the middle totally definite rank cannot put that canonical realization into this particular arithmetic constructor.

### Full proof

Here n and d are independent; no T-052 relation between them is assumed. The general U(n,1)×U(d) oscillator formulas are the same creation-annihilation formulas carried in T-052 (OC.7), with a=1,…,n and i=1,…,d. Equivalently they are Basile et al. (2020), §5.2, equations (5.21)–(5.30), specialized to q=1 negative direction and d compact columns. The positive compact diagonal operators have vacuum shift d/2 each, and the negative diagonal operator is −N_Y−d/2. Consequently the generator of diag(zI_n,z^(−n))⊂SU(n,1) is

    H=N_X+nN_Y+nd,

with every eigenvalue at least nd. The qth canonical coefficient has compact character det(A)^q d_0^(−nq), where d_0 denotes the last U(1) entry, and therefore has the weight qn(n+1) for this circle. Its lowest vector must appear in any nonzero subquotient realization. Exactness of compact weight decomposition, as proved in AM-DO-002, gives nd≤qn(n+1). Division by n>0 proves the bound.

Every determinant splitting twist is trivial on this traceless circle. Reversing the entire oscillator orientation replaces its spectrum by eigenvalues at most−nd, which excludes the unchanged positive canonical lowest weight. Simultaneously dualizing the target negates its lowest weight too and gives the same inequality. These cover the two definite signs of the auxiliary Hermitian space with fixed additive-character convention.

For the ball, d≤3 follows. The actual source `SplitPart.lean`, `StdPair.rk` lines43–44, requires 0<rank A<rank S and both ranks even; since rank A=2, it requires d≥4. The inequalities are incompatible. This proves the last assertion. ∎

### Consequence and boundary

This obstruction is additional to the simultaneous sign obstruction AM-DO-004. Even at the active real place alone, the unchanged canonical coefficient prevents using a larger even middle group to meet the strict kernel-constructor range. A signed equal-rank kernel theorem, a different arithmetic constructor, or a change of coherent coefficient is therefore needed for that route to G1. The bound is necessary and not sufficient: it does not prove finite local occurrence, global nonvanishing, the kernel identity, or the terminal mass equation when d≤3. At q=2, d=4 is allowed by this bound and the explicit AM-DO-005 lowest vector realizes the corresponding local bicanonical component.

## T-053, the Fourier comparison, and the precise geometric category

Carry T-053, `work/theta/charged_incidence_rees_report.md`, (IR.1)–(IR.5), (IR.12)–(IR.14). Its incidence ring is B=Q[X,Y]/(R_a), R_a=Σ_iX_aiY_i, and its actual frame Rees algebra is ⊕_{k≥0}B_(k,…,k). The source gives the generator maps, multiplication and quotient scheme; these are settled results and are not rederived here. In particular its equal-charge construction is an algebraic torus-weight operation in SGA3 I4.7.3 and4.7.3.1.

The partial Fourier map AM-DO-003 has the exact additional formulas

    F(R_a)=Σ_i X_ai∂_Zi,
    F(C_a)=−Σ_i Z_i∂_Xai,

where C_a=Σ_i∂_Xai∂_Yi. These follow by substitution into the already-proved Weyl-algebra isomorphism. They exchange the displayed multiplication constraints and differential constraints with off-diagonal compact Lie operators. They do not carry them to multiplication by polynomials in the ordinary positive definite coordinates X,Z: indeed

    [F(R_a), Z_j]=X_aj≠0,

whereas every such coordinate multiplication operator commutes with Z_j. This proves that this specific Fourier map does not give a morphism to the ordinary definite polynomial incidence scheme preserving the positive coordinate polarization. It remains an exact Weyl-module comparison into the delta realization, and the original Rees algebra still has its own carried scheme interpretation. No assertion that an arbitrary algebraic comparison between selected Rees pieces is impossible follows.

Likewise AM-DO-006 concerns the full creation-space tensor factorization, not a factorization of a single equal-charge quotient B_(k,…,k). It therefore does not refute T-053, its positive row-weight counts, or its exact remaining highest-type and Specht projectors. It excludes the proposed direct identification of the whole charged oscillator with one nontrivial compact tensor-pair oscillator under the named polarization and charge requirements.

Primary framework locators read in this run: Grothendieck, EGA IV4 (1967), Theorem16.11.2 and Remarks16.11.3(ii), pp54–55, https://www.iut-theory.org/divers/ega44.pdf; Demazure–Grothendieck, SGA3, Exposé I, Proposition4.7.3 and Corollary4.7.3.1, French recomposed edition, https://www.iut-theory.org/divers/SGA3I.pdf. The former distinguishes full differential operators from the integral Weyl algebra; the latter identifies actual torus-equivariant modules and schemes with gradings. Neither identifies these realizations with an integral theta lift, a Dieudonné crystal, an ℓ-adic sheaf with a specified Frobenius, or a motive. Those require additional structures and actual comparison maps.

## AM-DO-008. The actual kernel equation as period-rescaling and lattice-membership tests

This is a reduction of the already displayed MainX equation, not a computation of its missing theta entries. It makes precise which finite calculations would certify a selected arithmetic column, and which additional identity is needed for the source's full `ClsK.Core`.

### Polynomial and period equations

Fix one edge j, all finite charts and class representatives, the actual arithmetic `abelian₂` functionals, and the corresponding analytic kernel. Index a finite list of tests by i=(α,γ,a,a′,µ), where P_µ is a monomial polynomial. Put

    Θ_i = volLev(X_j,U_j,α) θ_K,j(h_j,α,a,h_j+1,γ,a′; Φ_j,Pµ),
    A_i = abelian₂_j,α,γ,a,a′(castP P_µ),
    d_i,τ = degree of P_µ in the variables at τ.

The exact source equation restricted to these tests is

    Θ_i = c_j (∏_τ s_j,τ^(d_i,τ)) A_i,              (DO8.1)

where c_j=cK_j≠0 and every s_j,τ=sc_j,τ≠0. No covolume has been omitted from Θ_i. If the c_j or s_j,τ are already fixed by the arithmetic pin, (DO8.1) must use those values.

For freely allowed complex rescalings c_j,s_j,τ, a finite system (DO8.1) is solvable if and only if:

1. A_i=0 exactly when Θ_i=0;
2. on the nonzero indices, with r_i=Θ_i/A_i and u_i=(1,(d_i,τ)_τ), one has

       ∏_i r_i^(v_i)=1

   for every integer relation Σ_i v_i u_i=0.

In particular all ratios belonging to the same multidegree must be identical. For a single homogeneous coefficient space, every two-by-two minor Θ_i A_l−Θ_l A_i must vanish, together with the stated support condition; a nonzero analytic period alone does not impose these identities.

Proof. The scalar matrix substitution in `mvZ(1,sI)` multiplies a monomial by ∏_τs_τ^(d_i,τ), proving (DO8.1). Nonzero scalars prove condition1; multiplying the equations according to an integer relation proves condition2. Conversely let M be the integer matrix with rows u_i for the nonzero indices. Choose integer unimodular matrices U,V with UMV=D in Smith form, whose nonzero diagonal entries are δ1,…,δh>0. Replacing target ratios by r′_k=∏_i r_i^(U_ki) and the torus variables by x_l=∏_k y_k^(V_lk) changes the system into

    y_k^(δk)=r′_k  (k≤h),   1=r′_k  (k>h).

The zero rows are integer relations and therefore their equations hold by condition2. Each nonzero complex number has a δkth root, so choose those roots and arbitrary nonzero unused variables. Undoing the unimodular substitutions solves the system. The equal-multidegree criterion is exactly the specialization where all u_i agree. This proves every assertion. Over a number field K the same proof additionally requires the indicated r′_k to be δkth powers in K×; it does not silently adjoin those roots or identify periods with algebraic numbers. ∎

### Integral finite-input equations

If a finite-dimensional ansatz for the finite Schwartz input has been specified, the analytic left side of (DO8.1) is linear in its input coefficients. After choosing actual integral generators, fixing the period scalars, and making a common algebraic denominator clearing that has itself been justified, write a localized system as

    Cx=b,   C∈Mat_(q×s)(O_v),  b∈O_v^q.          (DO8.2)

Here b is the specified jet vector including c_j and the period scales. Let π be a uniformizer. Suppose UCV has nonzero Smith diagonal π^(a_1),…,π^(a_h), with U,V invertible over O_v, and put b′=Ub. Then an integral solution exists exactly when

    b′_i=0 for i>h, and v(b′_i)≥a_i for i≤h.     (DO8.3)

Assuming the zero-row conditions hold, the least d≥0 admitting a solution x∈π^(−d)O_v^s is

    max(0, max_(i≤h)(a_i−v(b′_i))),              (DO8.4)

with v(0)=+∞ and an empty maximum contributing no positive bound.

Proof. Smith form over a DVR follows by choosing a matrix entry of least valuation, moving it to the top left, and clearing its row and column using divisibility by that entry. Repeat on the smaller submatrix; multiplication by units turns every nonzero diagonal entry into π to its valuation. All row and column operations are invertible over O_v. With y=V^(−1)x, (DO8.2) becomes π^(a_i)y_i=b′_i for i≤h and 0=b′_i afterwards. This proves (DO8.3). Permitting y_i∈π^(−d)O_v changes the first inequalities to v(b′_i)≥a_i−d, giving (DO8.4). These basis changes preserve the lattice, so the criterion does not depend on the selected Smith bases. ∎

This is a conditional integral criterion for a *specified* finite-input span. Allowing a larger Schwartz space may change C; choosing arbitrary analytic coordinates and treating them as integral does not instantiate (DO8.2). For the terminal detector, the analogous rank-one image-ideal and archimedean-norm costs are precisely AM-R-002, applied to the actual terminal vector and the fixed mass-weighted row lattice. Its stabilizer and Fock denominators must be retained.

### The remaining all-degree and family requirements

The actual `OnFramesRdApply.lean` definition `ClsK.Core`, lines108–113, quantifies over every polynomial P. Thus a finite matrix check certifies its restriction to the chosen monomial span, not the entire predicate. A full witness needs the equality for every degree, or a proved equality of the relevant analytic theta germs from which every jet follows. The finite class sets do not make the polynomial quantifier finite.

The source's `ClsK.Kval`, lines115–121, subsequently uses fixed finite weight spaces and the reciprocal stabilizer masses. The terminal `ClsT.Is.top/tail`, lines143–150, must hold for all the stated terminal vectors and rows, with one fixed branching map, level and top covolume. AM-R-002 supplies the cost of normalizing one already constructed detector; it cannot substitute for those simultaneous identities. Finally `PinColT.cst` in `LevChiEqOne.lean` fixes cK_j from the actual covolume, finite datum multiplier, vacuum scalar and determinant-root characters, so the free rescalings in the first criterion represent the most permissive test. Failure of that test is an obstruction; success does not override the specified normalization.

For the repeated-type geometry AM-DO-001 the actual matrices Θ,A,C,b and terminal mass matrix have not been calculated. Consequently no global value for the requested G1 pairing follows from this reduction. The concrete remaining calculation is the signed equal-rank first kernel, with its all-degree CM-jet identity, followed by the compatible second kernel and terminal row equations. AM-DO-004 and AM-DO-007 show why the existing common positive, strictly increasing constructor does not supply these entries.


## AM-DO-009. Exact tensor-to-oriented-Hom comparison, including the source dual

### The global symplectic and group map

Use the first-argument-linear Hermitian convention of 032, §4.2, equation(4.4), printed pp14–15. Let V and P have Gram matrices G_V and G_P, and let δ and ξ0 be nonzero purely imaginary elements of E. The 032 space is

    W032 = V⊗_E P,
    B032(x,y)=Tr_{E/F}(δ (h_V⊗h_P)(x,y)).

Define S to be the algebraic E-dual P^∨, with Hermitian Gram

    G_S=(ξ0/δ) G_P^(−t).                         (DO9.1)

The ratio ξ0/δ belongs to F×. In the dual basis of S and the given basis of V, identify a tensor with its coefficient matrix:

    I: V⊗P → Hom_E(S,V),
    I(Σ_(i,a) X_ia v_i⊗p_a)=X.                 (DO9.2)

Then I is E-linear and an exact isometry of the F-valued alternating spaces. It intertwines the tensor action of U(V)×U(P) with the oriented action of U(S)×U(V) under

    (g,k) ↦ (k^(−t),g),
    I((g⊗k)x)=g I(x) k^t.                      (DO9.3)

This is an explicit underlying rational oscillator comparison. It is not a comparison with the all-positive `StdPair` pin, and it does not alone establish any MainX kernel or covolume identity.

### Full proof

The dual Hermitian Gram G_P^(−t) is Hermitian: this follows by transposing and conjugating the identity G_P*=G_P. Scaling it by ξ0/δ∈F× preserves Hermitian symmetry and nondegeneracy. If k*G_Pk=G_P, transpose and invert this equality to obtain

    (k^(−t))* G_P^(−t) k^(−t)=G_P^(−t).

Thus k^(−t) lies in U(S), proving that the group map is well-defined. The ordinary action on the algebraic dual is k^(−t), so its inverse acts on the right of Hom matrices as k^t. This proves(DO9.3).

Write x=Σ X_ia v_i⊗p_a and y=Σ Y_jb v_j⊗p_b. The first-argument-linear convention gives

    (h_V⊗h_P)(x,y)
      =Σ_(i,a,j,b) conjugate(Y_jb)(G_V)_ji(G_P)_ba X_ia
      =tr(G_P^t Y* G_V X).

By(DO9.1), G_S^(−1)=(δ/ξ0)G_P^t. The exact source definition `hO` therefore gives

    hO(S,V)(I(x),I(y))
      =tr(G_S^(−1)Y*G_VX)
      =(δ/ξ0)(h_V⊗h_P)(x,y).

Multiplying by ξ0 and taking Tr_{E/F} proves

    symplO(S,V)(I(x),I(y))=B032(x,y).

The same equality remains true after Tr_{F/Q} and at every completion. The tensor-to-Hom map is bijective on the displayed bases, completing the proof. ∎

### Polarization, additive character, splitting and measure scope

Transport 032's actual positive Lagrangian through I_C. At the active place its two blocks are exactly the images of L⊗P_μ and Q*⊗P*_μ from032(4.5); at the compact places they are the images of the specified embedding blocks. The positivity equation is preserved because the alternating forms are equal. This describes the chosen polarization rather than replacing it by an all-positive coordinate pin.

Choose the SAME global additive character and transport one rational Schrödinger position space and its self-dual measures through I. The associated Heisenberg groups then identify by (x,t)↦(I(x),t), with central coordinate and character unchanged. On the transported Schrödinger function spaces the intertwiner is explicitly f↦f∘I^(−1) on the position spaces. The Weil actions coincide when both are pulled back from the same metaplectic representation and its same lifts. This assertion needs no change of additive character and no partial complex Fourier transform. The predicate `IsStdChar D ψ (-1)` of the recovered source must separately be compared with 032's fixed theta multiplier; equality of alternating forms does not discharge that predicate. The map also does not identify separately chosen lattice measures or finite theta structures; those must be transported and compared.

The group relabelling in(DO9.3) changes determinant-root labels. Choose idele roots t,y with

    t/c(t)=det k,  y/c(y)=det g.

Then the source root for k^(−t) is t^(−1), and Alpöge's oriented character factor is

    splitFacO(χ_S,χ_V)(t^(−1),y)
      =χ_V(t) χ_S(y).                          (DO9.4)

This follows from `LocalNewformFunction.lean`, line51. The root condition is `TiedWeil.lean`, `IsDetRoot`, lines64–66. At a split place `IsDetAt`, lines77–78, fixes the particular root t=e·det k+(1−e); the same inverse substitution applies. The arguments of these characters are the determinant roots, not the determinants. Moreover `IsWeilDatumO.om_split` retains a separate positive real factor r; (DO9.4) describes only its character factor.

Any proposed identification with already fixed 032 circle splittings must match these roots and this character factor. Transporting the existing metaplectic lifts gives one consistent comparison; matching arbitrary independently prescribed Hecke-character splittings additionally requires their determinant-character ratio. On SU(V) the ratio of two group splittings is trivial, as carried032 Lemma4.4, printed pp20–21, states. This does not set an arbitrary χ_S(y) to1 for every possible root y. No unprovided finite components of a global Hecke character, positive normalization r or universal Weil-index scalar are assigned here.

### The explicit Q(ζ7) middle form

For AM-DO-001, G_P=−a I2. Formula(DO9.1) gives

    G_S=s I2,  s=−ξ0/(δa).                      (DO9.5)

With ξ0=√−7/7 and δ=ζ−ζ^(−1), the signs of ξ0/δ at σ1,σ2,σ3 are(+,+,−): the quadratic Gauss sum √−7 is fixed by σ2 and negated by σ3, whereas all three imaginary parts of δ are positive. As sign(a)=(+,−,−), the signs of s are(−,+,−). In particular S is still totally definite. The scalar Gram −aI2 would give the wrong exact symplectic normalization for this independently fixed ξ0; it is not used here.

The literal definite chain has endpoint forms G_A=I2 and G_X2=(a/q)I2, q=Nξ0. Its actual oriented edge ratios are s and a/(qs). Their product is a/q, so AM-DO-004's simultaneous positive-pin obstruction applies unchanged. The conversion solves the rational symplectic and source-label issue; it does not solve the finite CM-jet, character, covolume, all-degree kernel or terminal-mass gates.

## AM-DO-010. The evaluation-point CM tori are explicit primitive-J powers

Carry B19a's exact rational E-Hodge decomposition for one multiplicity line at the rational negative line x=[Ee3]:

    H^1(A_x,Q) ≃ U(d)^⊕2 ⊕ U(dflip),
    A_x ∼_E B(d)^2 × B(dflip).                 (DO10.1)

The action is the specified geometric E-action of B19a. In AM-DO-001, the positive set of d is{1,4,5}; changing the active pair gives the positive set of dflip as{4,5,6}.

For s∈(Z/7Z)×, write J^(s) for the same abelian variety J with its E-action precomposed by σ_s. Its H^{1,0} type is sΦ, where Φ={1,2,3} is the carried type of J. Therefore

    B(d) ∼_E J^(4),   B(dflip) ∼_E J^(6),
    A_x ∼_E (J^(4))^2 × J^(6).                 (DO10.2)

Forgetting the E-action, A_x is isogenous to J^3. The two repeated multiplicity inputs of AM-DO-001 consequently use CM abelian varieties whose product is isogenous to J^6.

Proof. On a type-τ eigenspace, replacing ι(a) by ι(σ_s(a)) changes its eigencharacter to τ∘σ_s. The Galois group is abelian and identified with multiplication modulo7, so the new type is sΦ. Direct multiplication gives

    4Φ={4,1,5}={1,4,5},
    6Φ={6,5,4}={4,5,6}.

Each rank-one rational E-Hodge structure is determined by this type. Thus its E-Hodge structure is isomorphic to that of the indicated twist of J. The carried equivalence between rational Hodge maps in weight one and homomorphisms of complex abelian varieties up to isogeny, already used to prove B19a, supplies the two E-isogenies. Inserting them into(DO10.1) proves(DO10.2). The underlying abelian variety of every J^(s) is J, giving the final two assertions. ∎

This is an isogeny and a type identification, not an identification of the actual polarization, symmetric theta line, finite theta structure, integral lattice, or algebraic tangent frame. The exact B19 comparison still retains c_i, p_i, N_i, M_i and κ_x from(B19c)–(B19f). In particular a model by J powers makes the primitive CM source explicit but does not turn its theta-null period into1 or its arithmetic functionals into freely chosen linear maps. Root's AM-R-003 explains why these simple primitive-J powers cannot simultaneously be the old elliptic Serre-tensor model.
