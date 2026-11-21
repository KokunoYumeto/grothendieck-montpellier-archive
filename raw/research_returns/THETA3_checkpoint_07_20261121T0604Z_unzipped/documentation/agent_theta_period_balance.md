# Cross-type CM period comparison: the positive tangent relation and the residual determinant

Reviewer/author: GPT-6 Astra Pro, sub-run `/root/theta_032`, 2026-11-21. Inherited effort label not exposed. These are complete mathematical deductions at the stated hypotheses; the CM Hodge conjecture is used only as accepted background, and the theta-null modular normalization is being sourced independently by `/root/definite_bridge`.

## 1. The tangent-period product does satisfy the balanced relation

Let E be a Galois CM field, G its Galois group, c its central complex conjugation, and U(d) the rank-one E Hodge structure of 032 section 2.2, equation (2.2), p.7. Its embedding line at tau has type (1,0) exactly when d(tau)=1. Equation (2.3) sends that line under scalar conjugation g to the line labelled g*tau.

Suppose d1+d2=d3+d4 pointwise. Fix the common distinguished label mu=1. The lines

    L12 = U(d1)_mu tensor U(d2)_mu,
    L34 = U(d3)_mu tensor U(d4)_mu

have equal Hodge types after every scalar conjugation: their respective holomorphic degrees are ((1+d1(g))+(1+d2(g)))/2 and the corresponding sum for 3,4. Choose nonzero Betti vectors over Qbar. Extend a nonzero map L12→L34 by zero on the other embedding tensor lines. All its scalar conjugates are Hodge maps, so 032 Lemma 2.1 applies in the rational Hom space and expresses it as a Qbar-linear combination of rational Hodge maps.

Under the accepted CM Hodge conjecture for products of the auxiliary CM abelian varieties, these maps are induced by algebraic correspondences. The degree-one Kunneth factors and the embedding projectors are algebraic: the former can be given by interpolation in multiplication-by-N, and the latter by the E action. Duals can be implemented with the polarization correspondences. The cycle classes may be represented over Qbar: spread each cycle in the fixed projective product to a Hilbert-scheme component and specialize to a Qbar point; its Betti class remains constant. Therefore the corresponding de Rham maps have algebraic coefficients.

Write the Betti–de Rham comparison on each selected line as multiplication by a nonzero period. Commutativity with the correspondence shows that the product of the first two periods divided by the product of the other two is in Qbar×. The same conclusion holds for the dual tangent periods, with the reciprocal convention. In B19's notation this proves p1*p2/(p3*p4) ∈ Qbar× once the algebraic tangent frames and the common mu label have been fixed. It does not identify the full H1 direct sums or the ordinary Hodge determinants.

## 2. The ordinary top Hodge determinant has an autocorrelation type

Put h_d(tau)=(1+d(tau))/2 and Phi_d={tau:h_d(tau)=1}. Choose an algebraic-Betti basis vector e_tau in each embedding line of U(d). The top holomorphic determinant line of B(d) is spanned by

    v_d = wedge_{tau in Phi_d} e_tau.

After scalar conjugation by g, its holomorphic degree is exactly

    A_d(g) = sum_{tau in G} h_d(tau)*h_d(g*tau).

Indeed g sends each selected basis vector to the embedding line g*tau, which is holomorphic exactly when h_d(g*tau)=1. Its antiholomorphic degree is s-A_d(g), where [E:Q]=2s. This is an autocorrelation of the entire CM type, not the linear function d.

For the actual oscillator torus at the rational negative line, B19 proves

    H1(A_x,d) = U(d)^2 direct-sum U(flip_mu(d)).

The selected ordinary top Hodge determinant has weight 3s and complete holomorphic degree

    T_d(g) = 2*A_d(g) + A_flip_mu(d)(g).

Consequently the pointwise balance d1+d2=d3+d4 does not, by itself, balance these determinant tensor lines. This concerns the ordinary determinant of the holomorphic cotangent space used by Siegel modular forms. The E-linear determinant of a fixed E-module is a different object and must not be substituted for it.

## 3. Explicit valid 032 sign data showing the distinction

Take E=Q(zeta_7), G=C6, with a generator gamma and c=gamma^3. Let the distinguished embedding be gamma^0 and take representatives 0,1,2. For (a,b)∈{±1}² put

    d_(a,b) = (1,a,b,-1,-a,-b).

All are odd and have d(1)=1. The pairs (++),(--) and (+-),(-+) obey the required pointwise balance. Flip_mu changes entries 0 and 3. Directly counting the six terms in the preceding formula gives:

| d | A_d(gamma^j), j=0,...,5 | T_d(gamma^j), j=0,...,5 |
|---|---|---|
| ++ | (3,2,1,0,1,2) | (9,6,3,0,3,6) |
| -- | (3,2,1,0,1,2) | (9,6,3,0,3,6) |
| +- | (3,2,1,0,1,2) | (9,4,5,0,5,4) |
| -+ | (3,0,3,0,3,0) | (9,2,7,0,7,2) |

Thus the determinant-pair type difference is

    T_++ + T_-- - T_+- - T_-+ = (0,6,-6,0,-6,6).

The proposed map between those two selected determinant tensor lines is not a Hodge map after every scalar conjugation. No Tate twist corrects a nonconstant difference of this form. Hence the accepted CM Hodge conjecture does not supply an algebraic correspondence between these particular lines by the balanced-sign argument.

This does NOT prove that an accidental numerical period ratio is transcendental, and does NOT refute literal sketch statement 1.7. It identifies exactly why the proposed proof of that ratio from linear sign balance fails.

## 4. The constant-line factor kappa in compatible Betti coordinates

At a rational negative line x=Ez choose an E-basis e1,e2,z of V and an E-basis of each multiplicity line. In 032 equation (4.5), every positive-Lagrangian summand at x is then Qbar-defined: the active summands are L and its annihilator, and the compact summands are full E-embedding summands. The trace pairing and the identifications via h_V and h_P also have Qbar coefficients.

Choose a rational symplectic basis. The positive Lagrangian is transverse to the second fixed real Lagrangian: a nonzero vector in their complexified intersection would have zero positivity pairing. Thus it is the graph of a matrix Z. Since the graph itself and the projection map are Qbar-defined, Z has entries in Qbar. Its standard graph frame e_Z has Qbar coefficients.

The wedge maps giving det F ≅ L² tensor C in 032 equation (4.6), pp.15–16, are then maps between Qbar lines. Choose Qbar frames of their constant factors and compatible square-root frames. Any scalar needed for the square roots is algebraic because its square is algebraic. Choose the ball coordinates by the line spanned by z+z1*e1+z2*e2; their tangent and cotangent frames at zero are also Qbar-defined. It follows that the remaining conversion between the first Taylor tensors and this fixed Betti-coordinate canonical fibre has algebraic scalar, apart from the prescribed universal oscillator normalization. Equal rank and equal differential order give the same universal factor for both pairs, so their kappa ratio is algebraic.

This is a choice of compatible algebraic Betti frames. 032 explicitly allows arbitrary nonzero complex constant-line vectors; if those are used, their scalar rescalings must be retained. Crucially, the above calculation uses only rational/CM Betti linear algebra and no algebraic de Rham differential frame on the CM abelian varieties. It therefore contains no inverse Siegel Hodge-period determinant that could cancel the residual determinant motive in section 2.

## 5. Consequence of the precise theta-null modular comparison, once sourced

Under the standard orientation omega_alg=Omega*dz, the expected/source-verified normalization supplied by the definite agent is

    c_i² ∈ Qbar× * det(Omega_i)/(2*pi*i)^(3s),

or the same statement after a fixed finite even power if a multiplier has to be killed. With the algebraic kappa ratio from section 4 and the balanced tangent-period ratio from section 1, the ratio of the squares of B19's comparison constants still contains

    det(Omega_1)*det(Omega_2) / (det(Omega_3)*det(Omega_4))

up to algebraic factors. Universal powers of 2*pi*i cancel because all four tori have the same dimension. The remaining determinant relation is additional arithmetic content. A sufficient Hodge-theoretic test is equality T_d1+T_d2=T_d3+T_d4; under that extra equality the same CM-correspondence argument as section 1 applies. The explicit C6 switch fails that test.
