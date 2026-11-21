# SF-E835. Every semistable torsion-free balanced sheaf reduces to the checked hull gate

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** complete new proof, submitted for independent whole-proof
review. Its new analytic premise is SF-E834, which is separately frozen
and under review. This section does not promote that premise before its
review. The remaining steps are algebraic and are proved in full below.
The statement concerns actual semistable torsion-free sheaves; it does
not extend to unstable sheaves or arbitrary perfect complexes.

## 1. Statement

Retain the genuine polarized RM abelian fourfold X and theta=theta_++theta_-
of SF-E834. Let E be any theta-slope-semistable torsion-free coherent
sheaf of positive rank R, and suppose

\[
 e^B\operatorname{ch}(E)
   =R\left(1-\frac q2\theta_+^2\right)
      \left(1-\frac q2\theta_-^2\right),
 \qquad B\in\operatorname{NS}(X)_{\mathbb Q},\quad q\in\mathbb Q_{>0}.
 \tag{E835.1}
\]

Then the actual hull \(H=E^{\vee\vee}\) is locally free and has a filtration by
subbundles whose quotients are stable projectively flat vector bundles
of the same theta-slope. The quotient H/E is supported on finitely many
points or is zero. Consequently E is not weakly G-semiregular for any
specified coherent effective finite translation/tensor action on E in
the scope of SF-E818.

This supplies the hypotheses on the hull which were explicitly assumed
in E818. In particular a singular reflexive hull or a singular stable
factor in a locally free hull is no longer an unchecked semistable
escape, once E834 is established. No chosen stable-factor filtration is
assumed to be preserved by G.

## 2. Stable torsion-free factors and stability of their hulls

Choose a finite slope-stable-factor filtration

\[
 0=E_0\subset E_1\subset\cdots\subset E_s=E,
 \qquad Q_i=E_i/E_{i-1},\qquad r_i=\operatorname{rk}Q_i>0,
 \tag{E835.2}
\]

with torsion-free quotients of slope mu_theta(E). Here is a direct
existence argument adequate for this use. If a semistable torsion-free
sheaf is not stable, choose an equal-slope proper subsheaf of smallest
positive rank and saturate it. Saturation adds a torsion quotient whose
codimension-one cycle is effective. Any increase of slope would
contradict semistability of the ambient sheaf; thus the saturated sheaf
still has equal slope. Minimality of its rank makes it stable. The
saturated quotient is torsion-free and semistable: a larger-slope
subsheaf of the quotient would lift to a larger-slope subsheaf of the
ambient sheaf. Induction on rank gives(E835.2). This does not assume
local freeness of its factors.

Set

\[
 H_i=Q_i^{**},\qquad T_i=H_i/Q_i,
 \quad \alpha_i=\frac{c_1(Q_i)}{r_i}=\frac{c_1(H_i)}{r_i},
 \quad \alpha=\frac{c_1(E)}R,\quad\delta_i=\alpha_i-\alpha.
 \tag{E835.3}
\]

Every H_i is stable reflexive. Indeed, for any proper positive-rank
subsheaf M of H_i with 0<rank(M)<r_i, the intersection M with Q_i
has the same rank and
first Chern class as M: the quotient is supported in codimension at
least two, since H_i/Q_i is. Stability of Q_i then gives
mu(M)=mu(M intersection Q_i)<mu(Q_i)=mu(H_i). Each T_i has support
dimension at most two.

The first Chern component of(E835.1) gives B=-alpha. Equality of the
factor slopes implies integral_X delta_i theta³=0. Hence each invariant
representative delta_i is primitive for theta.

## 3. Mixed discriminant equality eliminates all surface defects

Let Delta be the discriminant convention(E834.1). Additivity of Chern
characters in(E835.2) gives the exact variance identity

\[
 \Delta(E)=\sum_i\Delta(Q_i)-\frac12\sum_i r_i\delta_i^2
          =\sum_i\Delta(H_i)+\sum_i\operatorname{ch}_2(T_i)
                         -\frac12\sum_i r_i\delta_i^2.
 \tag{E835.4}
\]

For example, subtracting the first expression from the definition of
Delta(E) reduces to
sum_i r_i(alpha_i-alpha)²=sum_i r_i alpha_i²-R alpha², using
sum_i r_i alpha_i=R alpha. The second expression uses
c1(Q_i)=c1(H_i) and ch2(Q_i)=ch2(H_i)-ch2(T_i).

Every mixed pairing on the right side is nonnegative:

* E834 applies to the stable reflexive H_i.
* The leading-character/support-cycle identity makes ch2(T_i) the
  effective surface cycle with positive generic lengths. E818§1 proves
  that every nonzero effective surface has strictly positive pairing
  with theta_+theta_- on a genuine RM fourfold.
* The elementary primitive mixed sum-of-squares formula E811.4 gives
  -integral_X delta_i² theta_+theta_- nonnegative.

The left side has zero mixed pairing, by(E835.1). Each nonnegative
summand therefore vanishes. E834's equality case makes every H_i a
locally free projectively flat stable bundle. Strict mixed positivity
eliminates every two-dimensional component of T_i. The equality case of
E811.4 makes every delta_i block diagonal for V_+ direct sum V_- and
primitive on each plane separately. Thus

\[
 \operatorname{ch}(H_i)=r_i e^{\alpha_i},\qquad
 \dim\operatorname{Supp}T_i\le1,
 \qquad \delta_i=\delta_{i,+}+\delta_{i,-},\quad
 \delta_{i,\pm}\theta_\pm=0.
 \tag{E835.5}
\]

The forms in the last identities are invariant forms on the indicated
planes. No claim that those planes are rational subvarieties is made.
The complete strict-surface proof is E818§1, including its Pluecker and
Albanese argument, not a supposition of general-position positivity.

## 4. The cubic character eliminates all curve defects

On each rank-two complex plane, delta_i,plus³=delta_i,minus³=0. Therefore

\[
 \delta_i^3=3\delta_{i,+}^2\delta_{i,-}
                 +3\delta_{i,+}\delta_{i,-}^2,
 \qquad \theta\delta_i^3=0.
 \tag{E835.6}
\]

Multiplication by theta kills the two summands either by excess plane
degree or by the separate primitivity in(E835.5). The actual K0
identity E=sum_i H_i-sum_i T_i and B=-alpha give

\[
 0=\left(e^{-\alpha}\operatorname{ch}(E)\right)_3
     =\frac16\sum_i r_i\delta_i^3-\sum_i\operatorname{ch}_3(T_i).
 \tag{E835.7}
\]

Here e^-alpha leaves the third character of each T_i unchanged because
T_i already has support dimension at most one. Multiply by theta and
integrate. The first term is zero by(E835.6). Each ch3(T_i) is its
effective curve cycle, with positive generic-length weights. The ample
theta has strictly positive degree on every nonzero effective curve.
Thus every T_i has support dimension zero or is zero. Let P be the
finite union of their supports and put U=X minus P.

The exact leading-character source is the same as in E818: Fulton,
*Intersection Theory*, second edition, Example18.3.11 p363 together
with Theorem18.3(3) p353, since the tangent bundle of X is trivial.
No sign is lost when replacing a sheaf by its effective leading support
cycle. The actual short exact sequences Q_i into H_i supply the positive
weights; this argument would not apply to virtual defect differences.

## 5. Extensions of vector bundles extend across these points

We give the required algebraic extension step rather than assuming that
a reflexive hull preserves exact sequences. For any two vector bundles
V,W on the smooth projective fourfold X, restriction gives an isomorphism

\[
 \operatorname{Ext}^1_X(V,W)
       \xrightarrow{\ \sim\ }
 \operatorname{Ext}^1_U(V|_U,W|_U).
 \tag{E835.8}
\]

Indeed both groups are H1 of the corresponding bundle V dual tensor W,
since the first argument is locally free. The reduced finite set P is
locally cut out by four regular parameters. For a locally free sheaf K,
its local-cohomology sheaves with support P vanish in degrees below4.
Explicitly, the augmented Cech complex on those four parameters computes
local cohomology; regularity of the sequence makes its cohomology vanish
except in degree4, and tensoring with the free stalk of K preserves this
statement. This is precisely Stacks Lemma36.6.9, tag0G7P, whose complete
proof was read. The local-to-global support spectral sequence therefore
gives H_P^j(X,K)=0 for j<4. The support triangle and its long exact
sequence, Stacks §20.21 tag0A39, now give H1(X,K) isomorphic to H1(U,K|U).
This proves(E835.8). No analytic/algebraic comparison on the nonproper U
is used: the sheaves and the actual extensions being restricted are
algebraic; holomorphic sheaves on the original projective X may first be
algebraized by GAGA.

On U, each Q_i agrees with H_i. The restricted filtration(E835.2) is
therefore a filtration by vector bundles with vector-bundle quotients.
Inductively construct vector bundles K_i on X extending E_i|U with a
filtration of the prescribed kind. Set K_1=H_1. Given K_(i-1), the actual
sequence on U is

\[
 0\longrightarrow K_{i-1}|_U\longrightarrow E_i|_U
             \longrightarrow H_i|_U\longrightarrow0.
 \tag{E835.9}
\]

Its extension class lifts by(E835.8) to an actual sequence on X

\[
 0\longrightarrow K_{i-1}\longrightarrow K_i
                    \longrightarrow H_i\longrightarrow0.
 \tag{E835.10}
\]

The middle term is locally free: on an affine local ring the free
quotient H_i splits the sequence. The new inclusion is a subbundle
inclusion, again because its quotient is locally free. Restriction to U
identifies(E835.10) with(E835.9), including the indicated subobject and
quotient. Induction produces K_s with stable locally free quotients H_i
of the same theta-slope.

The original hull H and K_s are reflexive and agree on U. The complement
has codimension4, so the usual reflexive Hartogs extension property
identifies them uniquely. Thus H is K_s and has the claimed actual
subbundle filtration. The canonical injection E into H is an isomorphism
on U, so H/E is supported on the finite set P.

## 6. Applying the existing categorical obstruction

All hypotheses of SF-E818 have now been proved for E: its actual hull is
locally free with stable locally free same-slope factors, and it has the
same balanced character. If H/E is nonzero, the canonical double-dual
sequence and the given coherent action give the point-defect kernel of
SF-E817, of dimension at least1+3s for s support orbits. If H/E is zero,
SF-E813 excludes the locally free sheaf with this filtration. Equivalently
one may invoke the complete theorem E818 directly.

Neither the chosen stable-factor filtration(E835.2) nor its hull factors
need carry separate G actions. The only action used at the final step is
the specified coherent action on E and its canonical functorial actions
on H and H/E, as proved in E817/E818. The scalar twisting and Serre
adjunction inputs are inherited in exactly their reviewed scopes.

## 7. Source and review boundary

The new analytic premise E834 is explicitly separate and must pass its
own whole-proof reviews. The strict surface positivity, leading support
cycle, point-defect and locally free filtration results are the reviewed
E818/E817/E813 statements. All stable-hull, variance, curve, extension-
lifting and actual-filtration steps above are new complete arguments.
The exact local-cohomology inputs were freshly read in full at
<https://stacks.math.columbia.edu/tag/0G7P> and
<https://stacks.math.columbia.edu/tag/0A39>; the depth form was also
checked at tag0AVZ. No finite numerical certificate is needed or claimed.
An unstable sheaf or a perfect complex outside these actual sheaf
hypotheses remains an open construction route.
