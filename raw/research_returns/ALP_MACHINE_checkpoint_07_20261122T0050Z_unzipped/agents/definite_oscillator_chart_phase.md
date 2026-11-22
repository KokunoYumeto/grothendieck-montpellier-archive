# AM-DO-027: exact common-chart phases and an integral unit normalization

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`;
inherited reasoning effort not separately exposed; 21 November 2026 UTC.

This result closes the scalar compatibility in `PinColT.cst` once
the raw arithmetic finite datum has actually been realized. The
normalization is permitted by the literal `IsRatDatum` definition,
not by changing the vacuum or inventing a new meaning for that
predicate. On equal-volume charts with compact determinants it
uses only roots of unity. It therefore has no additional finite
denominator, content, or norm cost. An explicit example also shows
why unramifiedness of the CM extension does not make these character
phases disappear automatically.

## 1. The precise common-character scalar equation

Fix one even-rank edge \(a\to b\) of the common
\(E'=\mathbf Q(\zeta_{28})\) host, with the same actual
splitting character \(\mu\) on both members, as required by
`PinColT.om`. Its restriction to \(\mathbb A_{F'}^\times\)
is trivial. Write
\[
 \nu_\mu(t)=\mu(x),\qquad x/\bar x=t.
 \tag{DO27.1}
\]
Hilbert 90 and the displayed restriction make this a well-defined
character of the norm-one torus. For source and target chart base
elements \(k_\alpha,k'_\gamma\), define
\[
 u_\alpha=\nu_{\mu,f}(\det k_\alpha)=\mu(x_\alpha),
 \qquad
 u'_\gamma=\nu_{\mu,f}(\det k'_\gamma)=\mu(x'_\gamma).
 \tag{DO27.2}
\]
The roots are exactly the source's `xr`, not the determinants
themselves. Its `TwDat.Is.kA` requires these root equations.
Let \(v_\alpha\) be the actual source chart level volume.
The literal condition is
\[
        c_K=v_\alpha w_{\alpha\gamma}c_0
                         u_\alpha(u'_\gamma)^{-1}
                   \quad\text{for every }\alpha,\gamma,
 \qquad c_0=C^{2ab}.
 \tag{DO27.3}
\]
This is `LevChiEqOne.lean`, `PinColT.cst`, lines113–114.

For unchanged raw scalars \(w_{\alpha\gamma}=1\), a common
nonzero \(c_K\) exists if and only if

- all source volumes \(v_\alpha\) are equal;
- \(u_\alpha\) is constant on the source chart set;
- \(u'_\gamma\) is constant on the target chart set.

Here both chart sets are assumed nonempty. To prove necessity,
fix a target chart and compare two source charts in (DO27.3).
The absolute values give equality of their positive volumes,
because \(|u_\alpha|=1\); the phases then give equality of
the \(u_\alpha\). Fixing a source chart similarly proves the
target assertion. Conversely those three conditions make the
right side independent of the charts. This is a necessary and
sufficient criterion, not merely a sufficient normalization rule.

Equivalently, the determinant conditions are
\[
 \det(k_\alpha k_{\alpha_0}^{-1})\in\ker\nu_{\mu,f},
 \qquad
 \det(k'_\gamma(k'_{\gamma_0})^{-1})\in\ker\nu_{\mu,f}
                         \quad\text{for all }\alpha,\gamma.
 \tag{DO27.4}
\]
If the determinant representatives are compact and the finite
character is trivial on the maximal norm-one compact, these
conditions hold automatically. Relative unramifiedness of
\(E'/F'\) alone imposes no such triviality on the chosen character.

## 2. Linearity is present in the actual source definitions

The relevant definitions were read directly, rather than inferred
from their names. In
`Formalism/LocalToGlobal/IndefiniteReal/LocalNewformFunction.lean`,
lines238–261, the source has:

1. `IsSBHalf e Λ Φ`: support in the idempotent half, a common
   integral period, and a common denominator support condition.
2. `IsPlaceModel … f₀ T`: \(T\) is explicitly a complex-linear
   map on functions, intertwines translations and modulations,
   and satisfies the unchanged vacuum normalization
   \(T(c\,\mathrm{halfInd})=f_0\).
3. `IsThetaAt … f₀ Φ f`: `AllSome` of those models with the
   assertion \(f=T\Phi\).

`IsRatDatum`, at lines25–29 of its namesake file, is the existence
of such \(\Phi\), with its rational restriction equal to the
specified arithmetic coefficient function \(\Xi\), and with
that `IsThetaAt` assertion. It follows that, for any complex scalar
\(z\),
\[
 \boxed{\operatorname{IsRatDatum}(\Xi,f_0,f)
       \Longrightarrow
       \operatorname{IsRatDatum}(z\Xi,f_0,zf).}
 \tag{DO27.5}
\]
The level idempotent, lattice, vacuum, additive character, and
`IsPlaceModel` normalization are unchanged.

**Proof.** Use \(z\Phi\) as the new witness. Its support is
contained in that of \(\Phi\), its same integral period works,
and its same denominator works. Thus it remains `IsSBHalf`.
Its rational restriction is \(z\Xi\). Keep exactly the existing
models \(T\); each is linear, so
\(T(z\Phi)=zT\Phi=zf\). This proves the new assertion for every
such model as well as for its existing witness, regardless of the
`AllSome` packaging. The condition \(T(c\,\mathrm{halfInd})=f_0\)
is untouched. This proves (DO27.5). \(\square\)

For a nonzero \(z\), the support of the finite coefficient family
is unchanged. `JointSmooth.lean`, lines20–24, defines
\[
 \operatorname{comb}(d,f_0)=\sum_xd_x\operatorname{heis}(x)f_0,
 \tag{DO27.6}
\]
and `IsFinComb` says that every support point has zero infinite
part. Consequently
\(\operatorname{comb}(zd,f_0)=z\operatorname{comb}(d,f_0)\),
and `IsFinComb` is retained. In particular this is a permitted
rescaling of actual finite Schwartz inputs. Any fixed compact
eigencharacter or real covariance of the input is also unchanged.

## 3. Actual normalized finite inputs and the common constant

Assume that for every chart pair there is an **actual raw datum**
\[
 \operatorname{IsRatDatum}(\Xi_{\alpha\gamma},f_0,
                         \phi^0_{\alpha\gamma}),
 \qquad
 \phi^0_{\alpha\gamma}
            =\operatorname{comb}(d^0_{\alpha\gamma},f_0),
 \tag{DO27.7}
\]
with the specified finite support condition. The arithmetic
\(\Xi_{\alpha\gamma}\) in this assumption is the source's
`A.xi`; it has not been replaced by a freely chosen function.
Its existence is an independent input to this proposition.

Fix any reference positive volume \(v_*\), and set
\[
 w_{\alpha\gamma}
   =\frac{v_*}{v_\alpha}\,u_\alpha^{-1}u'_\gamma,
 \quad
 d_{\alpha\gamma}=w_{\alpha\gamma}d^0_{\alpha\gamma},
 \quad
 \phi_{\alpha\gamma}=w_{\alpha\gamma}
                                  \phi^0_{\alpha\gamma}.
 \tag{DO27.8}
\]
Then (DO27.5)–(DO27.6) give exactly `PinColT.dat`, with its
required scalar multiple \(w_{\alpha\gamma}\Xi_{\alpha\gamma}\).
Substitution in (DO27.3) gives, for every chart pair,
\[
                          \boxed{c_K=v_*c_0.}
 \tag{DO27.9}
\]
The common period is unchanged. No new choice of the source vacuum
or of its unit norm is made. This proves the simultaneous `dat`
and `cst` assertions from (DO27.7), not only a formal consistency
of the numbers in `cst`.

Suppose now that the source levels are conjugate to one fixed level
inside the finite unitary group. A reductive local group is
unimodular, so conjugation preserves Haar measure; their volumes
are all the same \(v_*\). Suppose also that all the determinants
in (DO27.2) belong to the maximal compact norm-one torus. The
restriction of a continuous finite-adelic unitary character to that
compact group has finite image. Indeed the compact is profinite,
its character image is a compact profinite subgroup of the circle,
and such a subgroup is finite. Therefore
\[
                 w_{\alpha\gamma}=u_\alpha^{-1}u'_\gamma
                           \quad\text{is a root of unity.}
 \tag{DO27.10}
\]
It follows exactly that
\[
 \|\phi_{\alpha\gamma}\|_2
       =\|\phi^0_{\alpha\gamma}\|_2,
 \qquad
 v_\mathfrak p(w_{\alpha\gamma})=0
                              \quad\text{at every finite prime}.
 \tag{DO27.11}
\]
Multiplication by this scalar is an invertible integral map on
every coefficient lattice containing the character values. It
preserves its content, all elementary divisors, and its saturation
index. Every complex embedding also has absolute value one. These
are equalities, not upper estimates.

There is no assertion that a later selected Schur projection has
unit content. The statement concerns this particular scalar
normalization of the existing chart inputs. Its root-of-unity
change neither cures nor worsens a previously uncomputed lattice
or projection denominator.

If the chart volumes differ, the exact remaining extra scalar is
\(v_*/v_\alpha\). For commensurable compact opens it is rational:
with \(C_\alpha=U_*\cap U_\alpha\),
\[
 \frac{v_*}{v_\alpha}
        =\frac{[U_*:C_\alpha]}{[U_\alpha:C_\alpha]}.
 \tag{DO27.12}
\]
The norm changes by that positive ratio and its local content
changes by its valuation. Thus the character phase and the
volume cost are separated by an exact formula. Neither is
discarded when equal-volume hypotheses have not been verified.

On the present host compact-determinant representatives are
available. R009 proves the norm-one finite torus has class number
one. If \(g\) is any finite unitary representative, write
\(\det g=\delta u\), with \(\delta\in T'(F')\) and \(u\)
compact. Left multiplication by the rational unitary matrix
\(\operatorname{diag}(\delta^{-1},1,\ldots,1)\) makes its
determinant compact without changing its finite double class.
This observation does not by itself prove that an independently
pinned arithmetic chart has already made this representative
choice; its frames must be transported along that rational action.

## 4. An explicit nonconstant phase on unchanged lattices

The following example uses the same character on the two members
of an even-rank edge and the same unramified CM host. It shows
that the root-of-unity normalization in section 3 can be necessary.

Let \(a=6,b=20\). On the six real torus coordinates indexed by
\(\Phi'=\{1,3,9,15,17,23\}\), prescribe the character
\[
                         \beta(t)=\prod_{\tau\in\Phi'}t_\tau^{-8}.
 \tag{DO27.13}
\]
At one split place \(v_*\) above 29 choose the first component so
that \(\zeta_{28}\mapsto2\bmod29\), and define its residue
character by
\[
                         \rho(2)=\zeta_{28}^{12}.
 \tag{DO27.14}
\]
Take the other finite compact components trivial. Since
\(\sum\Phi'=68\), the value of (DO27.13) on the rational
\(\zeta_{28}\) is \(\zeta_{28}^{-544}=\zeta_{28}^{16}\).
Thus (DO27.14) is exactly its inverse on \(\mu_{28}\).
The torus class-number-one decomposition from R009 constructs
an actual unitary automorphic character \(\gamma\) with these
infinity and finite compact restrictions. Put
\[
                  \mu=\gamma\circ(z\mapsto z/\bar z).
 \tag{DO27.15}
\]
Then \(\mu|_{\mathbb A_{F'}^\times}=1\), and
\(\mu_\tau(z)=(z/\bar z)^{-8}\) at every selected place.
This is an admissible same-character splitting for the two
even-rank members. It also has an actual source `HCParam`
instance with admissible numerical `Ranks` data:
\(k=6,t=13,m=2,\mathrm{ord}=3\),
\(u=(11/2,9/2,7/2,5/2,3/2,1/2)\),
\(v=(5,4,3,2,1),b=(0,16),e=(8,24)\).
The required interlacings hold, the final \(u\)-entry is positive,
and both successive gaps equal \((t+3)/2=8\).
The numerical rank conditions are also immediate:
\(m+3=5\le6\), \(k+m-1+5=12\le13\), \(3m=6<13\),
\(m\le2\mathrm{ord}=6\le k\), and \(m^2=4\le34\).
No claim about further `Hyp3` hypotheses is needed for this phase example.

Let the source charts use the common principal congruence level
modulo 29 at all six places above 29 and the standard maximal
compact elsewhere. Take two source base elements \(k_0=1\)
and \(k_1\), where at \(v_*\)
\[
                 k_1=\operatorname{diag}((2,2^{-1}),1,1,1,1,1)
                        \in U(6)(F'_{v_*}),
 \tag{DO27.16}
\]
under the relative split identification, and at all other places
\(k_1=1\). Both lie in the standard integral compact and hence
preserve the identical selfdual lattice. Their source levels are
equal, so their volumes are equal. Choose the target identity
base chart. The determinant roots give
\[
                 u_0=1,\qquad u_1=\zeta_{28}^{12}
                         =\zeta_7^{3},\qquad u'_0=1.
 \tag{DO27.17}
\]
The two source level classes are distinct. If \(k_1=qu\), with
\(q\in U(6)(F')\) and \(u\) in the stated principal level,
then \(q\) is integral at every finite place. Its determinant
is therefore a norm-one unit, hence a member of \(\mu_{28}\).
At any other place over 29 that determinant reduces to 1.
Reduction there is injective on \(\mu_{28}\), so \(\det q=1\).
At \(v_*\) the congruence would instead give \(\det q=2\bmod29\),
a contradiction.

For unscaled raw inputs, (DO27.3) asks simultaneously for
\[
                         c_K=vc_0,
             \qquad      c_K=\zeta_7^{3}vc_0,
 \tag{DO27.18}
\]
which is impossible since \(v>0,c_0\ne0\). This failure is a
real character phase on actual different level classes, despite
unchanged lattices. The underlying standard trivial-character
vacuum is fixed, while the prescribed common-character source
Weil action is
\[
                    \omega_\mu(k_1,1)\phi_0
                           =\zeta_7^{-3}\phi_0.
 \tag{DO27.19}
\]
Equation (DO27.19) is the exact inverse source determinant-root
factor of AM-DO-022. The theta reading is injective and its
entire vacuum germ is nonzero, so this is an actual kernel phase,
not just a formal determinant computation. A sufficiently high
polynomial jet detects it even if the origin value of the section
vanishes.

The normalization of section 3 sets \(w_{00}=1\) and
\(w_{10}=\zeta_7^{-3}\). It solves (DO27.18) in the literal
`PinColT.cst` convention, retaining the actual determinant-root
factors in the kernel. Its scalar is already in \(E'\), is a
unit at every finite prime, and has absolute value one at every
complex embedding. The example is therefore a counterexample
to automatic phase constancy, together with an exact permitted
repair. It is not a counterexample to existence of `PinColT`.

## 5. Uniform character phases for the selected exponents

The same one-place construction works for arbitrary integer
selected exponents \(-e_{j,\tau}\). Give the real torus that
infinity type, and at the chosen place over 29 put
\[
 \rho_j(2)=\zeta_{28}^{r_j},\qquad
            r_j\equiv\sum_{\tau\in\Phi'}\tau e_{j,\tau}
                                               \pmod{28}.
 \tag{DO27.20}
\]
The inverse root-unit condition follows by evaluating at
\(\zeta_{28}\), exactly as in section 4. Extend it using the
same torus class decomposition and compose with \(z/\bar z\).
This produces actual admissible equal-character edges with the
selected infinity exponents. For compact-determinant chart
representatives every scalar in (DO27.8) then lies in
\(\mu_{28}\subset E'\), uniformly in the degrees and ranks.
There is no new coefficient-field extension for these phases.

If a particular source instance has already fixed different
characters \(\mu_j\), the construction in (DO27.20) does not
replace them. Sections 1–3 apply to those characters as they
stand; their actual compact values determine the unit scalars.
Likewise, normalizing each edge does not establish the separate
row-lattice, Schur-projection, or terminal-mass identities. It
does establish that, once the raw finite datum is available,
the common-chart character phases in `PinColT.cst` can be
removed within the expressly permitted scalar parameter, with
the exact volume cost (DO27.12) and no additional unit cost.

## Exact source and carried-result locators

- `Formalism/LocalToGlobal/IndefiniteReal/LocalNewformFunction.lean`,
  `IsSBHalf`, lines238–241; `IsPlaceModel`, lines248–255;
  `IsThetaAt`, lines257–261; `splitFacO`, line51.
- `Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsRatDatum.lean`,
  definition `IsRatDatum`, lines25–29.
- `Development/AbelianVarietyTheory/Definitions/LatticeFrames/JointSmooth.lean`,
  `comb` and `IsFinComb`, lines20–24.
- `Development/AbelianVarietyTheory/Definitions/LatticeFrames/LevChiEqOne.lean`,
  `TwDat.Is.kA`, lines52–53; `PinColT.dat` and `cst`, lines111–114.
- AM-DO-022, exact standard finite splitting and determinant roots;
  AM-DO-025, selected infinity exponents; AM-DO-026, actual kernel
  normalization and chart equation; corrected AM-R-009, the
  common-host norm-one torus class decomposition and character
  extension. The published class-number input is carried through
  R009, not re-proved here.

No Lean compilation or complete `PinColT` instantiation is claimed.
The raw arithmetic datum (DO27.7) and the remaining fields of that
record are explicitly retained as separate requirements.
