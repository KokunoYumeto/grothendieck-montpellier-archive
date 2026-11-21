# Independent audit of the numerical CM construction and lattice transfer

Run HODGE_DIVISION; 2026-11-21, approximately 12:01–12:14 UTC.
Reader: `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed.

**Outcome: PASS for SF-QC01–05 in the current
`agents/sixfolds/quantitative_cm_seed.md`, and for the complete proof of
HD-CM6 in `research/cm_lattice_transfer.tex`.** The use of Perry remains the
authorized, explicitly identified preprint input. The checks below are
mathematical whole-proof checks, together with independent exact exterior
arithmetic; they are not proof-assistant formalizations.

## SF-QC01: the strengthened finite orbit

The Gaussian matrix count is a valid overcount. Semipositivity bounds the
norm of every entry by 16. Since every prime of N is larger than P, each
nonzero entry is a unit in Z[i]/N, using its conjugate divided by its norm.
Thus one nonzero row is surjective and its kernel has at most N^4 points.
The exact-order-N denominator exceeds N^6/2. The sum of the two failure
probabilities is strictly less than one. The isogeny of degree eight is an
isomorphism on odd-order torsion, so sampling upstairs does not affect the
curve-difference estimate.

I checked the uniformity in Pic^0. A divisor numerically equivalent to 2Theta
has at most twelve distinct components. If it and a translate had no common
component, their intersection would have theta degree 24, contradicting the
3N contribution from the disjoint curves. At most 144 cosets of proper
subgroups of the cyclic H cannot cover H because their indices exceed P.
Some component is therefore H-stable. Both it and its effective complement
are nef, giving a nonzero pullback matrix between zero and 4I. Invariance
kills the chosen torsion point under its polarization homomorphism, which
contradicts the chosen matrix-kernel avoidance. No continuum search is
being smuggled into the finite construction.

## SF-QC02: coherence, projective dimension, action, and full character

The change of variables makes the two ideals independent pullbacks, so the
product is their intersection and the stated length-four exact sequence is
valid. The sum map from C times C factors through the smooth theta divisor:
nonhyperellipticity makes the degree-two Abel map injective and immersive,
including at a double point. The degree-two symmetric quotient is finite
flat. Consequently each torsion summand is a vector bundle on a smooth
Cartier divisor after pushforward, and has local projective dimension one.

The ranks of W and U are 8 and 8N. The strengthened orbit makes W to U
injective on every fibre, so its cokernel Q is a vector bundle. Dualizing
the two-term complex [Q to T], in cohomological degrees 1 and 2, yields
the displayed sheaf extension 0 to Q* to E to T^D to 0. In particular E
has rank 8d and projective dimension at most one; no purity or locally-free
output theorem is assumed.

The equivariance proof transports an actual descent action through tensor,
inversion, Fourier–Mukai, duality, and shift. It retains a faithful finite
subgroup of the translation/tensor group. The trace argument is the same
three-component Hochschild Künneth argument previously checked in D-SR-02.
Ordinary negative Ext vanishes because the resulting object is a sheaf.

My independent `positive_rank_gaussian_certificate.py` reconstructs the
original one-plane exponential, all twelve exterior generators, the dual
and shift, and the complete displayed polynomial P_d. It checks ten
arithmetic cases, including d=12 and rank 96, without invoking a generic
rank or geometry claim. It also checks the complete normalized character,
the codimension-three polarization coefficient, H times t equal to zero,
and integral t squared equal to -8dN^2. The formulae in the proof agree
symbolically with this independent derivation.

The Weil action, its positive compatible polarization, and the split
Hermitian space all check: the scalar-block operator squares to -d, its
polarization product is skew, and a rational symplectic Lagrangian copied
in the two factors is a K-stable maximal isotropic space. The determinant
terms are independent and have nonzero conjugate coefficients.

## SF-QC03: all regularity steps

I checked each cohomology reduction. In the dual-bundle calculation the
relative canonical bundle introduced by curve duality cancels under total
Serre duality. The two output fibre matrices are antiample for q at least
one. This gives the asserted 7-regularity.

The evaluation kernel is 14-regular: the higher groups follow from positive
twists and the already proved vanishings, while the H^1 group follows from
the actual section multiplication map. The Buchsbaum–Rim complex has the
correct determinant factor. Its locally split exactness follows from the
polynomial de Rham strands and Euler contraction in characteristic zero.

I verified the Fourier pullback identity for W and the matrix of Q_0,
including the sign of the cross term. Its eigenvalues are plus and minus
2sqrt(2). The bounds reg(C_k) at most 69+8k and reg(J_0) at most 112 use
only the first six terms; the subsequent cohomology is above dimension six.
The evaluation-kernel sequence then gives the same bound for Q*.

For the torsion dual, the sum-map pullback is 4(F1+F2)-Delta. The proof that
3(F1+F2)-Delta is nef covers both possible transitive degree-three monodromy
groups. In the cyclic case Riemann–Hurwitz gives five transverse fixed
points and each graph has self-intersection -4, so the required intersections
are positive. The decomposition of the twisting class is ample for q at
least three. Kodaira vanishing on the smooth fivefold gives 8-regularity.

The stronger pullback-and-nef-twist assertion also checks. Only H^j of the
evaluation kernel for j at least two is needed. The six relevant pulled
Buchsbaum–Rim terms have positive least eigenvalue, with worst bound
168-26sqrt(2). The finite-etale base change of the torsion divisor is smooth,
and the rewritten twisting class is an ample class plus a nef class.

## SF-QC04: ordinary normalization and honest finite group

The equality gcd(8d,N)=1 makes the N-torsion lifts of translations unique
and additive. Canonical deck linearizations of the pulled-back degree-zero
line bundles supply the commuting coherence maps. The resulting subgroup
A[r] times G is faithful: its translation terms have coprime torsion orders,
and multiplication by r is injective on dual N-torsion. There is no hidden
central kernel. Deck descent and then G-invariants identify precisely the
original semiregular invariant obstruction space. Tensor conjugation
preserves the coherent action and its faithful underlying subgroup.

The determinant twist cancels c1 exactly, and the entire character is the
pullback of kappa. For B-field zero, Perry's section 6.2 proof starts with
zero Kummer class. Band pushout preserves zero; the ambient category remains
ordinary Perf. I read this exact inference in the versioned primary text,
Theorem 6.3 and section 6.2, printed pp.25–28.

The concentration, flatness, and projective-dimension conditions are open
near the special fibre of the ordinary perfect family, by the local
amplitude/flatness argument stated in the proof and properness. The final
regularity matrix has determinant d(d^2+64)>0. Its decomposition against
112r^2H_b gives all six required vanishings. The stated polynomial
R=14344d^2+16d+6 is exactly 224r^2+r(d+2)+6.

## SF-QC05: effective detector and numerical bound

The evaluation kernel is a vector bundle because the coherent quotient has
projective dimension at most one. Its 7-regularity uses section multiplication
in degree one and ordinary positive-twist vanishings in higher degrees.
Twisting gives a globally generated vector bundle. I independently expanded
the inverse Chern polynomial and the twisting formula; every term and sign
in S_k agrees with the displayed equation. The Weil term is -2r^6t.

General sections give the expected codimension-three degeneracy locus for
a globally generated bundle; its class is c3. The nonzero Weil component
excludes emptiness and rank less than three. Thus this step supplies an
effective integral cycle, without a Chow denominator.

The Riemann–Roch calculation is correct: the Weil term pairs trivially with
h^3, and the coefficient estimate follows from convolution with the
exponential of a_d. It gives k at most M. All discarded terms in S_k are
nonpositive, because d exceeds one and k is at least three. The displayed
degree formula is therefore valid.

For the simplified bound, the independent estimates are
r at most 2^3 d, R less than 2^14 d^2, R+r^2 less than 2^14 d^2,
V less than 2^20 d^3, M less than 2^97 d^16, and A2 less than 2^9 d^5.
After multiplying by V the three terms are bounded by 2^47 d^11,
2^154 d^25, and 2^317 d^51. Their sum is less than 2^318 d^51.
The substitution d=4mL^2 gives exactly 2^420 m^51 L^102.
The class normalization also agrees: delta=2 and
T for r^6t equals 2^39 d^13 N^2.

## HD-CM6: the sharper source-to-target map

I read the complete TeX proof and independently reconstructed its basis
calculation. In the K-basis from the first Jacobian, the raw source lattice
is (Z+(u/d)Z)^6. Writing the maximal-order generator as a+u/f_s gives
the source Hermitian matrix k times the integral symplectic matrix, with
k=3du/f_s. It is integral because f_s divides d. This proves the normalization
including the factor three in the very ample source polarization.

F=diag(I,kI) pulls the standard hyperbolic Hermitian form back to this
source form. The matrix dF sends the raw lattice into O_K^6. It therefore
gives an actual K-linear isogeny after transporting the complex structure,
with polarization pullback d^2h. Its degree is 729d^15, but the detector
cost is d^6, as required by the projection formula.

For every class-number-one ring, including the non-Euclidean ones, the
saturated isotropic submodule is a free direct summand. The block Gram
calculation gives a two-sided denominator 2Delta for comparison with the
standard hyperbolic lattice. Composing yields the claimed degree cost
(2dDelta)^6 and bound 2^324 d^57 Delta^6. The finite-level correspondence
identifies the full period domains. The smaller-order lattice argument and
conductor exponent 72 are also correct.

The HD-CM4 numerical expression follows algebraically from its separately
stated HD-COMP premise and this sixfold function. This audit does not claim
a new independent whole-proof check of HD-COMP itself.
