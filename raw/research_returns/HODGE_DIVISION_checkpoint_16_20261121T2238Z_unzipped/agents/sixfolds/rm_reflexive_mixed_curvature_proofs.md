# SF-E834. Mixed discriminant equality for stable reflexive sheaves

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** complete new proof, submitted for independent whole-proof
review. This repairs the two specific unresolved steps recorded in
reflexive_curvature_attempt.md. It uses the published admissible-metric
and general-analytic-set extension theorems at the exact locators below.
It neither assumes a full Chern--Weil current identity on a singular
space nor applies an isolated-point removal theorem to a curve.

## 1. Statement and precise published inputs

Let X be a polarized complex abelian fourfold with a genuine
Rosati-invariant real quadratic action and its orthogonal complex
rank-two tangent eigenspaces V_+,V_-. Let theta=theta_++theta_- be the
invariant positive polarization form. For a reflexive sheaf E of rank
r>0 define the rational discriminant class

\[
 \Delta(E)=c_2(E)-\frac{r-1}{2r}c_1(E)^2
          =\frac{c_1(E)^2}{2r}-\operatorname{ch}_2(E).
 \tag{E834.1}
\]

If E is slope-stable for theta, then

\[
 \int_X\Delta(E)\theta_+\theta_-\ge0.
 \tag{E834.2}
\]

Equality holds if and only if E is locally free and projectively flat.
In particular no slope-stable reflexive sheaf has normalized character
R v_q with q>0, for any rational algebraic B field, regardless of an
additional coherent finite translation/tensor action.

The analytic inputs are as follows.

* Bando--Siu, *Stable sheaves and Einstein-Hermitian metrics*, in
  *Geometry and Analysis on Complex Manifolds*, World Scientific1994,
  pp39--50, **Theorem3, p40**: a polystable reflexive sheaf on a compact
  Kähler manifold admits an admissible Hermitian--Einstein metric.
  Admissibility, defined on p39, includes square-integrable curvature.
  The complete invoked §4 proof is on pp48--49, with the preceding
  regularization construction on pp45--48. The author's original page
  images are at <https://people.math.harvard.edu/~siu/bando_joint_paper/index.html>.
* Biswas, *A criterion for holomorphic extension of principal bundles*,
  Kodai Math. J.34(2011),71--78, **Theorem3.2 and its complete proof, p77**
  (also Theorem1.2, p72): a holomorphic principal bundle for a complex
  reductive affine group extends uniquely across a closed complex
  analytic subset of codimension at least two if the Chern curvature of
  a smooth maximal-compact reduction has finite L^n norm, where n is the
  complex dimension of the ambient manifold. We use G=GL_r(C), K=U(r),
  n=4. The primary PDF is
  <https://www.jstage.jst.go.jp/article/kodaimath/34/1/34_1_71/_pdf/-char/en>.
  Its vector-bundle input is Harris--Tonegawa, *Analytic continuation of
  vector bundles with L^p-curvature*, Int. J. Math.11(2000),29--40,
  **Theorem1, p29**, DOI10.1142/S0129167X00000040. The original
  Harris--Tonegawa proof has not yet been retrieved here; no claim to
  have independently audited that upstream proof is made. The invoked
  published Biswas statement and its full proof have been read.

The final locally free equality implication is exactly the already
whole-reviewed SF-E811 in its rational-polarization scope. All new
averaging, integrability, Bianchi and local-slice arguments are supplied
below. No numerical computation is a premise of this analytic proof.

## 2. Translation averaging supplies the needed Chern--Weil pairings

Let S be the singular locus of E. A reflexive sheaf on a smooth complex
manifold is locally free in codimension two; thus dim_C S is at most one.
For this familiar fact, locally at codimension at most two a reflexive
module has full depth over the regular local ring, and the
Auslander--Buchsbaum formula gives projective dimension zero. It is also
stated explicitly in Bando--Siu, p46. Put U=X minus S.

Choose the admissible Hermitian--Einstein metric h on E restricted to U,
with Chern curvature F, and set

\[
 F^0=F-\frac1r\operatorname{Tr}(F)I,
 \qquad
 \beta=\frac1{8\pi^2}\operatorname{Tr}(F^0\wedge F^0).
 \tag{E834.3}
\]

On U this is the usual smooth Chern--Weil representative of Delta(E).
For the fixed flat base metric and the unitary fiber norm,
|beta| is at most C_r|F|². Therefore beta is integrable on X. We extend
its coefficients by arbitrary values on the measure-zero set S; no
closed-current assertion is being made at this point.

Let H1,H2 be integral ample divisor classes. Choose sufficiently large
positive integers a,b and smooth divisors of classes aH1,bH2 whose
intersection Y is a smooth compact surface. Ordinary Bertini supplies
this after very ampleness; the argument does not require Y connected.
Let t_x denote translation by x in X and let mu be Haar probability.
Except for a measure-zero set of x, the translate Y+x avoids S. Indeed
the exceptional set is contained in the image S minus Y of S times Y;
its complex dimension is at most three, while X has dimension four.
One may equivalently use a finite analytic stratification and the real
Hausdorff-dimension bound at most six.

On each translate disjoint from S, the restriction of h is an ordinary
smooth Hermitian metric on the vector bundle E restricted to Y+x.
Its restricted Chern connection has curvature F restricted to the
surface. Chern--Weil applies without any Einstein condition on the
restricted metric and gives

\[
 \int_{Y+x}\beta
   =\int_{Y+x}\Delta(E|_{Y+x})
   =ab\int_X\Delta(E)H_1H_2.
 \tag{E834.4}
\]

The last identity is topological restriction: Y+x lies in the locally
free locus, so its derived restriction of E is the ordinary vector
bundle restriction, and Chern classes restrict. Translation fixes
cohomology, including the class of Y.

Here is absolute Fubini explicitly. Give Y its induced invariant-base
volume. The norm of restriction of a four-form to a tangent four-plane
is bounded by its ambient norm, up to one harmless fixed convention
constant. Translation is an isometry. Hence

\[
 \int_X\int_Y |t_x^*\beta|\,d\mathrm{vol}_Y\,d\mu(x)
 \le C\operatorname{vol}(Y)\int_X|\beta|\,d\mu
 <\infty.
 \tag{E834.5}
\]

The identity follows by Tonelli applied to |beta(x+y)| and translation
invariance of Haar measure. It controls the quadratic Chern--Weil form
by the assumed L² curvature; no pointwise bound near S was used.

The averaged current gamma_Y=integral_X [Y+x] dmu(x) is translation
invariant, closed, and has cohomology class [Y]=ab H1H2. On a torus,
translation-invariant currents have constant coefficients, hence are
smooth forms; a constant form is uniquely determined by its de Rham
class. Consequently gamma_Y is exactly ab times the product of the
invariant representatives of H1 and H2. Averaging(E834.4), justified by
(E834.5), gives

\[
 \int_U\beta\,H_1H_2
   =\int_X\Delta(E)H_1H_2.
 \tag{E834.6}
\]

This argument needs only the smooth compact translated surfaces. It
does not say that an arbitrary singular-sheaf Chern current represents
Delta(E) against all test forms. Real bilinearity extends(E834.6) to
products of classes in NS(X)_R, because the ample cone is open and spans
that vector space.

## 3. The RM mixed form lies in that precise span

Choose a trace-zero rational real-multiplication operator u with
u²=d>0. The theta-Rosati symmetry makes
lambda(v,w)=theta(u v,w) an invariant rational (1,1) form. After clearing
denominators it is an integral alternating form of type (1,1), hence
a divisor class by the usual line-bundle classification on a complex torus.
On the two eigenspaces it is respectively sqrt(d)theta_+ and
-sqrt(d)theta_-. Therefore

\[
 \lambda=\sqrt d(\theta_+-\theta_-),\qquad
 \theta_+\theta_-=\frac14\left(\theta^2-\frac1d\lambda^2\right).
 \tag{E834.7}
\]

For an explicit expression by ample products, take a positive rational
epsilon with epsilon sqrt(d)<1. Both theta+epsilon lambda and
theta-epsilon lambda are rational ample classes, and
lambda²=(theta²-(theta+epsilon lambda)(theta-epsilon lambda))/epsilon².
Thus(E834.6) gives the exact identity actually needed:

\[
 \int_X\Delta(E)\theta_+\theta_-
    =\int_U\beta\,\theta_+\theta_-.
 \tag{E834.8}
\]

This is why only divisor-pair Chern--Weil identities suffice; the
irrational individual RM planes are not treated as abelian subvarieties.

## 4. Equality removes mixed curvature on the regular locus

The Hermitian--Einstein equation implies Lambda_theta F0=0, and F0
has type (1,1). The pointwise calculation SF-E811.4 applies unchanged at
every point of U. For clarity, in unitary coordinates with
omega_+=e1+e2, omega_-=e3+e4, a real primitive (1,1) form alpha has

\[
 -\alpha^2\omega_+\omega_-
 =2\left((x_1+x_2)^2+
       \sum_{i\le2<j}(b_{ij}^2+c_{ij}^2)\right)\mathrm{vol}.
 \tag{E834.9}
\]

Here x_i are its diagonal entries and b_ij,c_ij the two real
coefficients of each off-diagonal Hermitian entry. Summing this identity
in an orthonormal skew-Hermitian matrix basis proves that the right side
of(E834.8) is nonnegative. This proves(E834.2).

If it is zero, the nonnegative smooth density is zero everywhere on U.
There are smooth endomorphism-valued real two-forms F_+,F_- on U such
that

\[
 F^0=F_++F_-,\qquad
 F_\pm\text{ has both arguments in }V_\pm,\qquad
 \Lambda_{\theta_\pm}F_\pm=0.
 \tag{E834.10}
\]

All real mixed curvature components vanish. The type (1,1) condition
already removed the (2,0) and (0,2) components; equation(E834.9) removes
the remaining mixed ones. This step concerns only U, where all forms
and metrics are smooth.

## 5. Bianchi and clean slices bound both curvature blocks

Work in a small holomorphic product coordinate box in the universal
cover, using the two parallel complex planes. Take a closed larger
product box contained in the coordinate chart, and a strictly smaller
product box inside it. The intersection of S with the closed larger
box is compact and has complex dimension at most one. Its projection
to either two-dimensional complex coordinate factor has real measure
zero. Choose a point b in the smaller second factor outside the
projection to that factor, and a point a in the smaller first factor
outside the other projection. The horizontal slice through b and the
vertical slice through a, taken over the closed intermediate factor
boxes, are compact and disjoint from S. They consequently have positive
distance from S and bounded smooth curvature. This choice is made
against the compact larger box, not only against S in the smaller open
box.

Bianchi gives d_nabla F0=0: it holds for F, and the scalar trace
curvature is closed. For constant real vectors v,w in V_+ and z in
V_-, its component is

\[
 (\nabla_zF^0)(v,w)+(\nabla_vF^0)(w,z)
                      +(\nabla_wF^0)(z,v)=0.
 \tag{E834.11}
\]

The last two terms vanish because the corresponding mixed components
are identically zero. Thus every coefficient of F_+ is parallel along
the second-factor directions. The corresponding statement holds for
F_- along the first-factor directions. The connection on End(E) is
unitary for the Hilbert--Schmidt norm, so each block norm is constant
along every path in its transverse factor fiber that avoids S.

Every such punctured factor fiber is path connected. Its removed set
is a proper closed analytic subset of a two-dimensional complex box,
of complex dimension at most one. To see connectedness directly,
join two points outside that subset through complex line segments
inside the convex box. On each complex line through an outside point,
the analytic intersection is discrete, since the line is not contained
in the subset. Small detours within the line avoid the finitely many
intersection points on a compact segment. An intermediate outside point
and two such paths therefore connect the chosen points. No simple
connectedness or flatness along that fiber is required.

For a point (z1,z2) of the smaller box outside S, connect z2 to b within
the second-factor punctured fiber with first coordinate z1. Parallel
norm transport gives

\[
 |F_+(z_1,z_2)|=|F_+(z_1,b)|.
 \tag{E834.12}
\]

The right side is bounded uniformly by the clean compact horizontal
slice. Similarly
|F_-(z1,z2)|=|F_-(a,z2)| is uniformly bounded by the clean vertical slice.
Hence F0 is locally bounded near every point of S. This proof works
also when S contains curves, and never identifies the punctured
universal cover with a product.

## 6. Smooth determinant normalization and a general-set bundle extension

The determinant of a reflexive sheaf on the smooth X is a holomorphic
line bundle. Choose any smooth Hermitian metric h0 on that determinant.
On U, let g be the positive smooth ratio h0/det(h), and replace h by

\[
 h'=g^{1/r}h.
 \tag{E834.13}
\]

Then det(h')=h0. Scalar metric rescaling changes the Chern connection by
a scalar one-form, so it leaves the induced End(E) connection and its
trace-free curvature unchanged. It also leaves the norm of every
endomorphism unchanged. Thus the curvature of h' is

\[
 F'=F^0+\frac1rF_{h_0}I.
 \tag{E834.14}
\]

The first term is locally bounded by section5, and the second extends
smoothly across S. Hence F' is locally bounded on X. Compactness gives
finite L^4 norm. The metric h' need not be Hermitian--Einstein, and that
property is not required in the extension theorem.

Apply Biswas Theorem3.2 with the holomorphic frame GL_r bundle of E|U
and the U(r) reduction supplied by h'. The base is the smooth complex
fourfold X, S is a closed analytic subset of codimension at least three,
and the curvature has finite L^4 norm. Every hypothesis is now supplied.
There is a holomorphic vector-bundle extension Ebar on X. Both Ebar and
the original E are reflexive and agree outside codimension at least two,
so they are uniquely isomorphic: reflexive sheaves on a smooth normal
space equal the pushforward of their restriction across such a subset.
Thus E is locally free.

Now apply the already proved stable-bundle theorem SF-E811 to E. The
same discriminant class has zero mixed pairing, so E is projectively
flat. Conversely a locally free projectively flat E has Delta(E)=0,
which proves the equality characterization.

## 7. The balanced consequence and exact boundary

For e^B ch(E)=R v_q with q>0, the first two terms imply
Delta(E)=Rq(theta_+²+theta_-²)/2. It pairs to zero with theta_+theta_-,
but its pairing with theta² is positive. The equality theorem would
force Delta(E)=0, a contradiction. A finite translation/tensor action
cannot alter this obstruction on the underlying stable reflexive sheaf.

This theorem does not directly assert the result for an unstable sheaf,
a semistable sheaf with an unexamined filtration, or a perfect complex.
Nor does it claim that the singular Hermitian--Einstein connection itself
has been smoothly extended by the new argument: only the holomorphic
bundle extension is needed, followed by the existing locally free
result. The translated-surface averaging and clean-slice bounds are the
new steps; the published analytic existence and extension theorems are
stated inputs with their source status explicit.
