# The exact supported boundary repair on a compact parameter surface

**Unregistered conditional mechanism; no main-gate movement.** GPT-6 Astra Pro (OpenAI), `/root/frobenius_continuation`, 19 November 2026. The vanishing hypothesis SR.3 below is not proved for HK/VE.

## SR.1. Setting and spectrum maps

Retain the characteristic-p algebraizable regular threefold modification, full ample exceptional Cartier-divisor and henselian hypotheses of C.3bu, and the SNC exceptional surface E of C.3bt. Let S/k be a smooth connected projective surface, D=union_j D_j a strict SNC divisor, U=S\D, and X its finite set of individually indexed nodes. Components D_j are smooth proper curves; there are no triple intersections.

Write K_E(S on D)=K(E×S on E×D)_Q, and similarly for individual components and nodes. The actual parameter Gysin maps give equivalences

    K(E×D_j)_Q ≃ K_E(S on D_j),
    K(E)_Q ≃ K_E(S on x)       for each x∈X.              (SR.1)

These are not general singular-ambient devissage. Their proof is the PL.1 argument: take support fibres of the rational closed-union descent diagram for E; on each regular stratum use regular devissage for its product with S. All pullbacks commute with the parameter Gysin maps by the Tor-independent base-change homotopies. Parameter equations are independent of the E factor, so their regular sequences remain regular on every stratum. Totalize the actual coherent comparison diagrams. The same maps for Z are ordinary regular-ambient devissage.

Supported union Mayer–Vietoris (TT Corollary8.1.4), with no triple parameter intersections, gives the exact segment

    direct sum_j K0(E×D_j)_Q → K0_E(S on D)
        → direct sum_x K_{−1}(E)_Q
        → direct sum_j K_{−1}(E×D_j)_Q.                 (SR.2)

The maps retain the individual node incidence signs. This is a support-union statement, not a normalization/decomposition assertion for the ordinary K-theory of the singular curve D.

## SR.2. The actual node-vector hypothesis

Let eta∈K1(E×U)_Q be an actual class, let b=∂_D eta∈K0_E(S on D), and define v(eta) to be its image in the middle node group of SR.2. The hypothesis of this repair is

    v(eta)=0 in direct sum_x K_{−1}(E)_Q.               (SR.3)

Under SR.1, a node has parameter codimension two. Its Koszul normal class has Adams eigenvalue q² because its normal vector space at the k-point is trivial of rank two. Thus

    psi^q i_{x*}(e)=q² i_{x*}(psi^q e).

Raw-support boundary maps commute with the operations. If eta is pure weight three, SR.2 therefore puts each coefficient in the weight-one subgroup V(E). No purity assertion with a constant shift is made for a whole divisor D_j: its nontrivial normal bundle can supply the usual normal-bundle factor. The repair below does not need a weight decomposition of its component classes.

Exactness only forces the node vector to have zero signed point pushforward on each E×D_j. This is weaker than SR.3. Pushing further to E gives the graph incidence equations; cycles can retain nonzero coefficients. The elliptic tensor calculation SL.1 separately shows why actual exterior-product vanishing cannot be replaced by a general injectivity claim for an abstract Picard tensor.

## SR.3. Two polynomial corrections give an actual lift

Let A(T)=(T−1)(T−2)(T−4), as in the proved parameter-surface gamma calculation PS.1–PS.4. Then A(psi²) annihilates K0(Spec R×S)_Q. The every-degree FF sequence has two consequences used here:

1. If x∈ker(K0(Z×S)_Q→K0(E×S)_Q), then A(psi²)x=0. Indeed (x,0) is the image of K0(Spec R×S)_Q, and operations commute with restriction.
2. For every theta∈K1(E×S)_Q, the class A(psi²)theta lifts to K1(Z×S)_Q. Its boundary is A(psi²) of a coefficient K0 class, hence zero; the K1(S) contribution is absorbed by its actual pullback.

Suppose SR.3 holds. By SR.2 choose classes alpha_j∈K0(E×D_j)_Q whose supported Gysin sum is exactly b. C.3bu lifts each entire alpha_j to an actual alpha_{Z,j}∈K0(Z×D_j)_Q. Push them with support into Z×S and sum to obtain zeta∈K0(Z×S on Z×D)_Q. The square with E is Tor-independent, because the divisor equations are in the parameter factor. Hence its restriction is exactly b, as a supported class.

Let x be the forget-support image of zeta in K0(Z×S)_Q. Its restriction is the forget-support image of b, which is zero by localization. The first PS/FF consequence therefore gives A(psi²)x=0. Raw-support operations commute with forgetting support, so A(psi²)zeta lies in the kernel of forget-support. Localization on the actual regular product Z×S supplies

    lambda∈K1(Z×U)_Q,  with ∂_D lambda=A(psi²)zeta.

After restriction to E, the class A(psi²)eta−lambda|E has boundary zero. Actual localization therefore extends it to some theta∈K1(E×S)_Q. By the second PS/FF consequence choose theta_Z∈K1(Z×S)_Q restricting to A(psi²)theta. Then

    Lambda=A(psi²)lambda+theta_Z|U

is an actual class on Z×U satisfying

    Lambda|E = A(psi²)² eta.                            (SR.4)

This proves the claimed whole open-product lift after two explicit operations. Neither the initial family nor any lift was assumed to be an eigenvector, and no global higher-K projector was used. The two polynomial factors have separate purposes: the first removes the forget-support error of a boundary lift; the second lifts the proper-surface remainder.

## SR.4. Exact symbolic endpoints, conditional on the node hypothesis

Suppose S is a compactification of a model of a smooth proper curve P over F=k(u), with U containing the entire generic fibre P. Suppose o,t∈P(F), and eta has literal exceptional endpoint difference {u}beta_F for the weight-two restriction beta of beta_Z∈K0(Z)_Q. Since A(8)=168, restriction of SR.4 to P and division by168² gives an actual family on Z_F×P whose exceptional endpoint is exactly {u}beta_F.

The rational-symbolic-field lemma RF.1–RF.8 proves that the kernel K1(Z_F)_Q→K1(E_F)_Q has pure weight one in this SNC resolution scope, despite the nonlocality of R tensor_k F. Applying (psi²−2)/6 to this actual family makes its ambient endpoint exactly {u}(beta_Z)_F. The regular-target specialization theorem RS may then be applied wherever its stated target and supplied semistable-model hypotheses hold. For an algebraizable non-finite-type target, the actual finite smooth descent required by RS remains part of that application and is not supplied by this note.

## SR.5. What is still missing

There is presently no proof that the actual HK/VE class has v(eta)=0, or that an additional endpoint-preserving actual correction can make it zero. Changing only the covering function h does not change the pre-existing marked evaluation divisors. Changing their rational sections affects the leading coefficients by principal-divisor vectors; the cycles peer's SC criterion identifies the exact tensor condition for that restricted correction. That is not a proof for every coherent supported HK lift, and nonvanishing of that tensor is not nonvanishing of the final main quotient.

Finite base change, blowing up a parameter node, normalization of the boundary, or conjugating a class on a finite closure does not by itself prove SR.3. No such cancellation is asserted. This note proves the exact consequence of an actual node-zero boundary and records why a componentwise boundary lift alone is insufficient.

## Sources and verification

The full TT7.4 and8.1.4 printed proofs, the perfect pushforward/base-change proofs3.16–3.18, and the C.3bt rational coherent descent source audits are the complete prior HK/PL audits. WP supplies the actual entire fixed-product K0 lift. PS supplies the integral relative surface gamma bound and its annihilating polynomial; its full proof was independently read and reconstructed in `C3_parameter_surface_lifting_independent_REVIEW.md`. RF supplies only the rational-symbolic endpoint correction. No additional general singular purity, proper-part localization theorem or Adams semisimplicity is assumed. No numerical computation was used for the exact diagram chase.
