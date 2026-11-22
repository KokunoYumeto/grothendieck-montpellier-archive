# Independent reviews: AM-K027, ALP-LIFT-14 and ALP-LIFT-16

Reviewer: GPT-6 Astra Pro, ALP_MACHINE /root/definite_oscillator,
21 November 2026 UTC. Inherited reasoning effort is not separately
exposed. These are actual whole-proof readings of the saved reports;
the accepted display and literature theorems remain cited inputs.
No Lean compilation is claimed.

## AM-K027: PASS in the stated fixed-rank, fixed-row-weight scope

I read the complete selected_schur_exact_slope.md, the full
common-weight corollary DP51 Section6 (HA17–HA21), the source-gauge
comparison AM-K018 (K19.2), (K19.13), the entire AM-K024 selected
witness construction, and the target-normalization calculation
AM-K026 (HC16–HC26).

The extension from separated prefactors in DP51 to an arbitrary
joint integral formal prefactor is valid. The product inverse
logarithm map has zero constant term and is integral at the same
common weight in every coordinate. Each coefficient of its
composition with an arbitrary integral series is a finite sum.
This proves the required common-weight bound without introducing
a separated-product hypothesis. The unit change
\((u,v)\leftrightarrow(u+iv,u-iv)\) is integral with integral
inverse at11; it preserves that bound because the common scale
is the same for every coordinate.

The factorial conversion is exact:
\[
 \frac1{10}-\frac{121}{1220}=\frac1{1220},\qquad
 v_{11}(\alpha!)
   =\frac{|\alpha|-\sum s_{11}(\alpha_i)}{10}.
\]
The row-support estimate EX6 applies to the specified row-weight
space. Its amended wording explicitly restricts the selected-module
application to the fixed source-highest row space and does not
assign those individual row degrees to every vector of the full
source/target tensor product. This scope is necessary and correct.
The prefix-minor specialization uses a columns, while the full
fixed-row space can use b columns, exactly as EX6–EX7 state.

For the AM-K024 witness, the four growing first-column variables
and the fixed residual polynomial have disjoint variable sets.
Its digit error therefore has the bound in EX12. The upper bound
is the carried explicit primitive-kernel value and integral
weight extraction. Combining them proves the actual limit
1/1220, not merely an upper liminf. Equality of the formal and
allowed-half-orbit image ideals is used at the precise finite
jet depth supplied by AM-K022.

The target normalization is the exact positive hook ratio
\(h!H_\lambda/H_{\lambda+h e_1}\). Its finite product expression
gives both valuation bounds of EX15, including possible negative
valuations; the square root is not assumed integral. The source
class index has fixed11-valuation at fixed rank, and the source
dimension is a product of finitely many linear factors in the
growing increments. These corrections are O(log degree) in
valuation, so the normalized limit survives. The full Gaussian
and factorial creation norm remains separately displayed.

I independently recomputed the four exact rational lower bounds
in the numerical table and their ceilings. They agree:
1,372,581,866; 1,373,293,082; 825,838,183,001;
826,051,784,873. This arithmetic check is not evidence for
a display theorem or a later arithmetic image statement.

The result is about a varying selected family at fixed ranks,
with its source-highest polynomial coefficient lattice. It does
not identify the prescribed raw Xi, a later integrated image,
or an unrestricted rational Weyl-lattice normalization. Those
limitations are explicit and are preserved in this PASS.

## ALP-LIFT-14: PASS with its carried analytic inputs

I read the entire selected_even_chain_nonvanishing.md. I checked
the common-character construction against the norm-one torus
factorization and its root-unit compatibility; the common Hom
character contributes \(\eta_T^{-1}\eta_S\), so equal characters
leave the old Satake block unchanged and add the indicated
length-d segment. The dictionary agrees with the independently
checked AM-DO-028 source/tensor and doubling calculation.

I directly read Liu (2021), Definition2.8 and Theorem6.2, in the
local primary text lift_refs/liu2021_unramified_theta.txt. For
the sign+ and target rank larger than source rank, the inserted
eigenvalues are the odd paired q-powers. Expressing them with
\(Q_w=q_F^2\) gives exactly E12. The theorem includes the actual
lattice-vector nonzero image for every spherical specialization,
under its stated odd-residue-characteristic assumption.

The initial unitary Satake bound makes its initial Euler product
absolutely convergent at the Rallis point. The inserted segments
give the factors \(L(\ell,\mu_r\mu_j^{-1})\) with
\(1\le\ell\le d\), with the ratio and shift as written. The
elementary 3+4cos+cos2 positivity argument proves nonvanishing
at1: angular nontriviality of both the ratio and its square
removes the possible poles, and a hypothetical zero would
contradict the positive Euler inequality. It does not incorrectly
assert absolute convergence at1.

The compact real test is the ordinary Schur integral
\(\operatorname{vol}(U(a))/\dim\rho\); the selected contragredient
component and actual bilinear convention are retained. The
anisotropic target has global Witt index0, so the lower-Witt
vanishing condition is vacuous. The report applies the cited
GQT convergent-case and holomorphy statements at those hypotheses.
Its closed-joint-kernel argument covers actual automorphic
multiplicity embeddings. The later averaging step retains
spherical representations without claiming the same original
finite test or any arithmetic denominator bound.

This review does not turn the analytic common characters into
the source's separately tied IsEtaT/Chars record. It preserves
the report's explicit distinction between this actual analytic
chain and the six arithmetic comparisons.

## ALP-LIFT-16: PASS for the fixed tests, restricted family, and masses

I read the complete spherical_tests_and_29_only_chain.md. I
independently checked the split calculation from its displayed
proof, rather than inferring its vacuum assertion from mere
local theta occurrence.

The full-rank matrix disintegration is valid: the intersection
of a rational a-plane with \(\mathcal O^B\) is saturated and
extends to an integral basis, giving transitivity under
\(K_B\times\mathrm{GL}_a(F)\). Right multiplication has
Jacobian \(|\det h|^B\). The primitive-matrix locus has measure
\(\prod_{i=0}^{a-1}(1-q^{i-B})\), fixing the constant in S6.
For the source inverse action the first convolution integral
uses \(hg^{-1}\); the equality
\(A_B(g^{-1})=A_B(g)\) gives the displayed S7. Thus the
inverse choice does not alter the resulting transform.

The one-sided Iwasawa calculation has the correct exponent
\(z-(a-1)/2\) for every diagonal variable. Multiplying its
direct and inverse Satake factors gives S9. The analytic identity
in \(T=q^{-B/2}\) is a legitimate identity theorem at an
accumulation point inside the common domain, and the explicit
Cartan bounds prove convergence at the actual rank with margin
q^-1. There is no unproved continuation from integer dimensions.
Consequently the split normalized factor is exactly
\[
 \prod_{i=0}^{a-1}(1-q^{i-b})
   =\prod_{i=1}^{a}(1-q^{-d-i})>0,
\]
also at residue characteristic2.

I directly checked Liu (2021), equation(5.1), Proposition5.6
with sign+, and Lemma6.1 in the primary local text. The odd
nonsplit factor is
\(\prod_{i=1}^{a}(1-(-1)^i q^{-d-i})\), with the same
volume1 maximal compact convention. The character ratio in
the split local test is the one in AM-DO-028, and the actual
doubling evaluation at0 equals the vacuum inner product.
This verifies the local constants without assuming an integral
dyadic diagonal/antidiagonal change of basis.

The fixed-away-from29 joint-kernel argument allows every vector
in the corresponding spherical subspace and handles multiplicity.
The source-to-target local correspondence is injective on the
stated spherical parameters outside29 and is the full type-II
Howe correspondence at29. Thus different global source types
cannot cancel in one target isotypic subspace. The full finite
Heisenberg basis then supplies a single29-supported translate,
with its stated unbounded depth and finite norm1.

The principal level \(29^{2e}\) gives displacement in
\(29^e\Lambda\), so its central half-phase and trace-one lattice
character are1. The exact group index, trivial stabilizers and
mass formula are correct. In particular
\[
 v_{11}I_n(29^{2e})
  =6\left(\lfloor n/10\rfloor+
                 v_{11}(\lfloor n/10\rfloor!)\right)
\]
is independent of e. The archimedean index cost still depends
on e, and S27 retains the Schur factor. This is not an integral
source-row or raw-Xi identification, as the report states.

The proof gives a stronger analytic test family, with exact
normalization. It does not bound the later translation depths
or transfer the kernel coefficient slope to a later image.
