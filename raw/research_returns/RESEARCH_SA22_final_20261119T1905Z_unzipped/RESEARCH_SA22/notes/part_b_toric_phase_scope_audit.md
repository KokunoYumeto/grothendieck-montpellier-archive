# Focused adversarial audit: the exact phase in the toric non-descent example

**Reviewer:** GPT-6 Astra (OpenAI), `/root/part_b_cycles`.
**Completed:** 2026-11-19 17:06:08 UTC.
**Statement:** `A1-toric-nondescent` in
`sections/part_a567_toric_descent.tex`, especially lines182–275.
**Outcome:** the exact least-index phase specifies a complete counterexample
under the brief's stated proof standard. No mathematical gap, TeX correction,
new unresolved status, or numerical refinement is required. This is a targeted
recheck of the existing proof, not new movement in the research ledger.

## The standard actually imposed

The attached `upload/PROMPT(20261119-110314).md`, lines137–143 and261–263,
requires a complete counterexample with every hypothesis verified, and a
program check when the counterexample is finite. It does not require every
real or complex constant in an analytic construction to have an elementary
closed form, a decimal expansion, or a numerically evaluated index.

The present counterexample consists of canonical analytic cap maps, their
welded four-punctured Riemann surface, and two embedded analytic circles.
It is not a finite combinatorial object. The use of a finite natural-number
index to specify a phase does not turn that analytic object into a finite
enumeration problem. No program verification of an evaluated integer is
claimed in the manuscript.

## All data precede the phase selection

The one-cap pant is fixed by its positive boundary length and its two
ordered cusps. The normalization `(cap centre, cusps)=(0,1,infinity)` and
positive cap derivative remove the coordinate rotation. Consequently the
function `r(lambda)`, the normalized cap germ `g_lambda`, and the ordered
labelled pant `P(r)` used here are uniquely defined geometric objects.
The proved strictly increasing bijection `r:(0,infinity)->(0,4)` makes each
inverse-radius prescription unique.

The formulas

\[
r_1=r(1),\quad r_*=r(1/2),\quad
r_2=\frac{r_*^2}{4r_1},\quad r_0=\frac{r_*}{2},\quad R=r_0^2
\]

therefore leave no free radius parameter. Since `0<r_*<r_1<4`, all four
radii lie in the required interval; indeed `r_2<r_0<r_*`, giving
`0<lambda_2<lambda_0<1/2`. In particular `R>0` and `R<4<16`, within the
proved geodesic range `0<|q|<16` of `A1-small-ranges`.

The unequal pair and balanced pair have these **fixed** cap shapes. Their
plumbing coordinates satisfy `g_1 g_2=t`, while the actual toric boundary
rule is `u_1 u_2=eta`; because `g_i=r_i u_i`, the actual parameter is
`t=R eta` for each pair. The phase is not substituted for the plumbing
parameter without its radius factor.

The two cross-ratio functions are defined from these fixed families and
the four fixed labels. They do not depend on a previously chosen `N`, on
the desired non-descent conclusion, or on an unspecified selected surface.
The order of definitions is therefore noncircular:

1. Fix the normalized pants and all radii.
2. Define their two plumbing families and labelled cross-ratios.
3. Define their difference `Delta`.
4. Prove that `Delta` is not identically zero.
5. Select the unique least candidate index, and construct its welded surface.

## The analytic domain supports the selection argument

The explicit smaller collar radius

\[
a(\lambda)=r(\lambda)
\exp\!\left(\frac{\arctan(\operatorname{csch}(\pi\lambda))}{2\lambda}\right)
>r(\lambda)
\]

lies strictly inside the established cap extension and avoids the external
marks. Hence both fixed-shape plumbing families exist on the common disc
`|t|<R rho` with `rho>1`, as given at lines201–219. The cross-ratios are
holomorphic there, including the central nodal parameter after extension.
The labelled sections are distinct for nonzero `t`; their normalization
therefore creates no cross-ratio pole in this disc. Enlarging the original
small plumbing discs gives the same family on the overlap by
`A1-welding-plumbing`, so the Taylor coefficient calculation applies to
these larger families.

Thus

\[
\Delta(c)=\Lambda_U(Rc)-\Lambda_G(Rc)
\]

is an independently defined holomorphic function on `|c|<rho`. In
particular the whole unit circle, including the candidate limit point1,
is inside its open domain. The argument would be invalid if only a formal
germ or a disc ending at the unit circle had been established; neither
limitation is present in the actual proof.

For this focused audit the already proved third-order formula was read
and used, not recomputed. Together with the explicitly verified strict
radius inequalities, it gives

\[
[c^3]\Delta(c)<-\frac{31R^3}{369920}<0.
\]

This proves nonidentity before the phase is selected. No comparison of
an asymptotic leading term with an uncontrolled remainder at `|c|=1` is
being made. The nonzero coefficient is used only to invoke the identity
theorem for the genuine holomorphic function.

## Existence, uniqueness and meaning of the least-index rule

Put `c_n=exp(i/n)`. These are distinct: their arguments belong to `(0,1]`
and two such distinct arguments cannot differ by an integer multiple of
`2 pi`. They satisfy `|c_n|=1` and converge to1. If every `c_n` were a zero
of `Delta`, the identity theorem at this interior accumulation point would
force `Delta` to vanish identically, contradicting its cubic coefficient.
Therefore

\[
A=\{n\in\mathbf Z_{>0}:\Delta(c_n)\ne0\}
\]

is nonempty. The well-ordering of the positive integers supplies a unique
least member `N`, and `eta_*=c_N` is consequently one uniquely specified
phase, with `Delta(eta_*)!=0`.

There is a stronger useful observation: **all sufficiently large integers
belong to `A`**. A nonzero holomorphic function has isolated zeros near1.
If1 is not a zero, a neighborhood contains no zeros; if1 is a zero, a
punctured neighborhood contains no zeros. In either case, `c_n!=1` and
`c_n->1` prove the assertion. Equivalently the compact unit circle meets
the discrete zero set in only finitely many points. No estimate of the
number or location of those zeros is required for this existence and
uniqueness proof.

The manuscript's definition is therefore exact, in the ordinary classical
mathematical sense. It is not an arbitrary unmade choice of a good phase.
It also is **not asserted to be an executable procedure that decides exact
equality of analytic values**, nor is a decimal value or a numerical upper
bound for `N` asserted. Those would be separate effective refinements.
Their absence is not a missing hypothesis of the specified construction.

## The selected object really gives the fixed-surface counterexample

With this unique phase, the unequal welding defines one four-labelled
punctured sphere `X`, up to its stated labelled biholomorphism convention,
and an actual analytic seam `C`. The two-cusp pants on either side verify
that this seam is simple and essential. Its bank identification is toric
by construction, and raw capping recovers the fixed normalized components
and tensor `q=R eta_*`.

The balanced comparator `X_G` has equal canonical boundary lengths, hence
a geodesic seam and the same tensor. Its cross-ratio differs because
`Delta(eta_*)!=0`. Four distinct external labels are essential here:
they fix the cross-ratio convention and the normalized three-pointed
components, so an unlabelled permutation cannot erase the inequality.

The complete hyperbolic surface `X` has a unique geodesic representative
`C_geo` of the essential isotopy class of `C`; it is simple and analytic.
Cutting along it gives the canonical hyperbolic pants, so their seam
identification is toric. If its raw tensor also equalled `R eta_*`, the
previously proved **geodesic** reconstruction theorem would identify `X`
with `X_G`, a contradiction. That theorem was proved from the cap-radius
inverse and equal-length welding; it did not assume the raw toric isotopy
invariance being refuted. Thus no circular dependence enters this final
step either.

The unequal seam and its own geodesic representative lie on the same `X`
and have different tensors. The argument does not merely compare two
different surfaces in a fixed-target fibre. The corrected statement remains
the separately proved construction that first takes the geodesic
representative; no status change is needed.

## Audit operations

This audit read the current descent fragment, the unequal-toric definitions,
the tensor and welding/plumbing identities, the geodesic inverse/range,
and the exact counterexample requirements in the attached prompt. It used
hand logical and analytic reasoning. No symbolic computation, numerical
evaluation, finite test, source-access request, or new program was run.
No runtime is invented for an unexecuted computation. An optional explicit
numerical phase family was not pursued because no concrete proof gap was
found.
