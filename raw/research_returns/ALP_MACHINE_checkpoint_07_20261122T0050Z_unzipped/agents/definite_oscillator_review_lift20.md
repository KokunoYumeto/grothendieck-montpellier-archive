# Independent whole-proof review of ALP-LIFT-20

Reviewer: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`.
Inherited reasoning effort is not separately exposed. Completed
22 November 2026 UTC.

**Verdict: PASS in the exact local theorem and stated conditional
global corollary.** I read the complete
`raw_first_g_steinberg_bridge.md` and directly checked the source
definitions in `FiniteSumNonzeroLargeDepth.lean`.

For `m=2,m2=0`, the source ranks give `r=a+1,c0=1,c1=0`.
Both index permutations in `entB` are the identity. Its only
nonzero scaling is multiplication of the last source column
by q. The initial frame is forced to be one by `zero_h`,
and the target argument of `PsiAt` is one by definition.
Thus the source's `Loc.om` factors are exactly one here.

With the allowed class `y=q^(-1)e_a mod O^b`, the enlarged
matrix is `[X,e_a]` modulo q. Reading every `PhiG` and
`PhiGS` clause gives precisely the affine upper-unipotent
residue support `X0 U_a`. The leading `(a+1)` determinant
is one. The extra sharp-column condition is automatic;
the additional simple-root term in the unsharp character
is zero. Hence both raw factors have value `psi_U(u)`.
Changing y by an integral vector changes its scaled column
by q times that vector, so the identity holds for the actual
`repY` independently of its representative choice.

The finite Fourier calculation is exact: the support is
an affine space of dimension `a(a-1)/2`; its Fourier support
is the complementary affine annihilator, with constant
coefficient modulus `q^(a(a-1)/2-ab)`. Thus its raw norm,
number of frequencies, and coefficient absolute sum in
(RG8–10) are correctly normalized in additive matrix measure.

For the actual source action
`eta(det g)^(-1)|det g|^(b/2)f(Xg)`, multiplication by
`eta(det t)` on the free orbit conjugates to the right
regular finite action. It leaves the raw U-supported
vector unchanged. The complete Steinberg isotypic projection
is then computed by the one-dimensional generic eigenspace
in the finite Steinberg representation. Formula (RG15)
has the correct conjugate-linear-first inner-product sign.
It identifies both multiplicity directions, so the result
is the single coefficient `m`, not merely a nonzero
component in some undetermined copy.

Its inner product with the raw vector is `d_q`, and its
squared finite-group norm is `|G_q|/d_q`. Therefore the
projection scalar is exactly `d_q^2/|G_q|`. The compact
matrix-coefficient filter is `1/d_q` times the corresponding
rank-one projector, giving (RG17). All other residue orbits
are invariant and contribute zero. These checks establish
the full projection and filter statements, including their
denominators and exact norms.

The global filter commutes with the independent29 operator
and the real differential polynomial. Applying it inside
the compact definite theta integral gives the factor
`A_G/(I d_rho d_G)` while retaining the raw G function in
the original kernel. The raw norm relation
`Gamma_U=A_G Gamma_St` and all 11-adic formulas follow
from the actual local counts. The same actual y-class can
be imposed at the distinct G places by fractional-lattice
CRT with its other prescribed components retained.

The text correctly assumes the separately proved actual
theta-family/selected-jet realization. In particular a
permitted29 Weyl translate is still present in the global
corollary. The result alone does not identify the complete
unshifted `XiCpl1`, its T/Q factors, or the admissibility
of that additional29 translate under the literal raw datum.
These are retained gates, not consequences of finite
Steinberg occurrence.

Directly read source locators, recovered commit
`7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`:

- `Formalism/LocalToGlobal/Columns/FiniteSumNonzeroLargeDepth.lean`,
  `fIdx/scE/entB`684–694; `PhiG/lamGvS/PhiGS`780–810;
  `PhiAt/omPhi`927–945; `joinCol/PsiAt`981–986;
  `zero_h`1019–1023; `ybSet/repY/XiCpl1`1125–1138.
- `Columns/RecLevel.lean`50–52, the inverse adelic type.
- The finite Steinberg normalization and literal source
  action are the independently checked DO033 inputs.

No repeated numerical test was needed for this review:
the author and root had already replayed the finite
diagnostic. This event records my whole mathematical
and source review, not a new certificate execution or
a Lean build.

