# Independent adversarial review of R10--R12

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, inherited effort not separately exposed, GHOSTS `/root/cm_transport`.

## Verdict

No mathematical gap found in `work/root_family_bound.md`, after the scope clarifications below. The proposed D0=132269760 is a valid coarse bound for a detecting effective surface on the normalized principally polarized, integral Eisenstein-action component. R10--R11 then give the displayed bound in terms of delta and T. This is an original quantitative consequence of the source construction, not an effectiveness statement quoted from Schoen.

1. Pass to a finite étale cover killing the determinant character of unitary monodromy, so that the rational Weil plane and the selected class t are constant. For an O_K-unimodular Hermitian lattice, the determinant lies in O_K^×=mu_6, so this is a finite cover.
2. The numerical constant does not automatically apply to an arbitrary Hecke presentation with a changed polarization or a merely rational K action. It applies on the normalized PPAV component with integral O_K action. A polarized-isogeny extension outside those hypotheses must charge its degree and polarization comparison.

## Source passages directly checked

Schoen 1988, primary PDF <https://www.numdam.org/article/CM_1988__65_1_3_0.pdf>: printed pp.12--13, including the complete r=0 construction immediately before (2.3); printed pp.24--25, definition of P and identification U=Xi*P*U'; printed pp.26--30, cyclic triple cover construction, P=3 Id-sum sigma, the dominance argument and cotangent calculation. The exact r=0 paragraph says P0=P_infinity=P_minus-infinity=|K_X|, and its primitive-character cycles are combinations of the components over this P0. Thus the asserted support is present in the proof, not inferred merely from the theorem statement.

The root's corrected use of Schoen1998 rather than the overbroad 1988 Theorem3.2 is retained. The 1988 tangent-space calculation supplies dominance on the actual Prym component; the identification with the PPAV component is supplied by the separate lattice argument below.

## Detailed checks

### Support, nonvanishing, and image components

The maps C^4→Sym^4C→Sym^4X are finite. The preimage of |K_X| is consequently two-dimensional. The cycles in the r=0 proof are combinations of components in this preimage, after pulling back from the finite quotient W0. No cycle support outside it is required by that argument.

The proper map f=P∘Abel:C^4→B is dominant, and both varieties have dimension four, so f_*f^* is multiplication by a nonzero degree on H^4(B). The source U is f*W as a subspace. Hence an algebraic combination from those supports pushes to a nonzero W class. Some irreducible source component has a nonzero W projection after pushforward; its image must have dimension two. Its Abel image lies in W4(C) and in a translate of B in the norm fiber. Conversely every point of W4(C) in that fiber is represented by an effective divisor whose norm is canonical, so the intersection has dimension at most two. The selected image is therefore an irreducible component of the intersection.

On that translate P is [3] followed by translation. Pushforward by [3] acts invertibly on rational cohomology. Thus a nonzero W projection of the image under P implies a nonzero W projection of the reduced Abel-image component itself. This justifies omitting both ordered-product multiplicity and the degree of [3] from the selected-component bound.

### Degree calculation and improper intersection

The two input degrees in the 3Theta embedding are 3^4·7!/3!=68040 and 3^4·216=17496. General projective Bézout bounds each reduced component of an intersection by the product of the degrees, even though this intersection is not of the expected dimension. Only a reduced support component is needed, so no refined-intersection multiplicity or effectivity assertion is being smuggled in. Dividing the surface degree by 3^2 gives D0=132269760.

### Principal-polarization quotient

The induced Prym polarization has type(1,1,3,3), so its kernel has order81 and is (Z/3)^4. The kernel equals B∩B^perp and B^perp is the image of Jac(X). The deck action on that image is trivial, hence acts trivially on the kernel. Every maximal isotropic subgroup of order9 is therefore stable under O_K. Polarization descent gives a principal theta on B/H with q*theta=L. The projection formula gives degree_theta(q_*S)=degree_L(S); pushforward is rationally invertible and K-equivariant, so preserves nonvanishing of the Weil component. The finite isogeny correspondence preserves the four-dimensional image.

### Integral Hermitian component

The Hermitian lattice attached to a principal alternating form E can be written explicitly as

    h(x,y)=E(omega x,y)-bar(omega)E(x,y).

Then h takes values in O_K, is linear in its first variable and Hermitian, and E(x,y)=Tr_{K/Q}(h(x,y)/sqrt(-3)). Principalness makes h unimodular. This justifies passing from the symplectic moduli problem to a unimodular Eisenstein Hermitian lattice.

Meyer's theorem supplies a rational isotropic vector in the underlying dimension-eight indefinite quadratic space. Scale and divide its O_K-content, using that O_K is a PID, to obtain a primitive integral isotropic vector e. Unimodularity gives f with h(e,f)=1. Replacing f by f+a e changes its norm by Tr(a), and Tr(O_K)=Z, so f can be made isotropic. The span is a unimodular hyperbolic plane, and splits integrally. Its orthogonal complement is a rank-two unimodular Hermitian lattice of signature(1,1), hence determinant -1. Over K it is isotropic: after diagonalization it is <a,-1/a>, and (1,a) is isotropic. Repeat the primitive-vector argument. This proves the lattice is U⊕U. A vector of norm one in U splits it as <1,-1>, so this is the product E^4 lattice with mixed signature. The proof is valid once the classical Meyer theorem is accepted as background; it does not rely on a classification table that was not supplied.

### R10--R11 constants

The projector eigenvalues and cycle signs check. Every positive or negative side has degree at most36D0. The Hodge norm bound ||[Z]||≤D0/2 follows because the total flat volume of a PPAV is one, harmonic forms are translation invariant, comass is at most Euclidean norm, and a complex surface has volume degree/2. The Weil plane is primitive (2,2), so its positive intersection form equals the Hodge metric. Thus d≤729D0^2. The middle cohomology lattice is even, giving d/2 integral. Cramer's coefficients, multiplier delta·3d^2/4, and the inequality |a|+|b|≤3delta sqrt(T)d^(3/2) are correct. The final coarse constant 531441 delta D0^4(1+4 ceil(sqrt(T))) bounds both numerator degrees and the multiplier.

### Closedness extension

After the finite monodromy cover, delta and T are constant. B01 gives the closed bounded-class locus for the chosen section t. It contains the dense Prym-quotient locus, hence the whole component. This uses the already proved bounded-specialization machinery and requires no extension of effective cycles from a fixed special fiber.

## Check event

R10--R12 | 2026-11-21 | GPT-6 Astra Pro; inherited effort not exposed; GHOSTS /root/cm_transport | independent re-proof | Entire candidate read, source support and dominance passages directly checked; all geometric, lattice, degree and linear-algebra steps checked; accepted with finite-monodromy and normalized-polarization scope clarifications. No formal certificate claimed.
