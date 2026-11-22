# ALP-LIFT-11: a fixed-conductor determinant repair of the specified second-edge type obstruction

Author: /root/lift_accounting, GPT-6 Astra Pro, ALP_MACHINE.
21 November 2026 UTC. This result stays over
$E=\mathbf Q(\zeta_7)$ and $F=E^+$. It is not a
common-host identification with the $\mathbf Q(\zeta_{28})$
family of AM-DO-022.

AM-DO-023 supplies the primary-source-checked honest-splitting
Fock formula and the specified second-edge vanishing theorem.
They are used here as established results. The new construction
is a global splitting character of uniformly bounded finite
conductor, its exact effect on the actual first theta lift,
and the resulting removal of that particular real-type
obstruction. It does not assert nonvanishing of the next
global lift.

## 1. An explicit global norm-one character of any integral infinity type

Put $T=U(1)(E/F)$ and
$K_{T,0}=(\widehat{\mathcal O}_E)^1$.
ALP-LIFT-09 proves
\[
 T(\mathbb A_{F,f})=T(F)K_{T,0},\qquad
 T(F)\cap K_{T,0}=\mu_{14}.
 \tag{R1}
\]
In particular
\[
 T(F)\backslash T(\mathbb A_F)
       \simeq(T_\infty\times K_{T,0})/\mu_{14},
 \tag{R2}
\]
where the roots of unity are embedded diagonally. These
arithmetic statements are used here without re-proving their
Minkowski and unit-signature arguments.

Choose the three complex coordinates indexed by
$\Phi=\{1,2,3\}$, so that the rational root $\zeta$
has archimedean coordinates $(\zeta,\zeta^2,\zeta^3)$.
For any integer vector $\mathbf c=(c_1,c_2,c_3)$, put
\[
 \beta_{\mathbf c}(z_1,z_2,z_3)=
               z_1^{c_1}z_2^{c_2}z_3^{c_3},\qquad
 C_0=c_1+c_2+c_3,\quad S_0=c_1+2c_2+3c_3 .
 \tag{R3}
\]
Here each $z_i$ lies on the unit circle.

Choose one of the three split places $v_*$ over29 and its
first $E$ factor so that $\zeta$ reduces to $16$ in
$\mathbf F_{29}^{\times}$. This is possible because16 has
order7 modulo29. The element2 generates
$\mathbf F_{29}^{\times}$: $2^{14}=-1$ and
$2^4=16$ has order7. The projection of $K_{T,0,v_*}$
onto that first factor, followed by reduction, gives a
surjection
\[
 K_{T,0,v_*}\longrightarrow \mathbf F_{29}^{\times},
 \qquad \zeta\longmapsto 2^4,\quad -1\longmapsto2^{14}.
 \tag{R4}
\]
It is injective on the rational subgroup $\mu_{14}$.

Choose $r\in\{0,\ldots,13\}$ with
\[
                   r\equiv 7C_0+6S_0\pmod{14}.
 \tag{R5}
\]
Define the finite compact character $\rho_{\mathbf c}$ to
be trivial at every place other than $v_*$ and to satisfy
\[
            \rho_{\mathbf c}(2)=\exp(2\pi i r/28)
 \tag{R6}
\]
on the residue group at $v_*$. On $\zeta$ its value is
$\zeta^r$, while $\beta_{\mathbf c}(\zeta)=\zeta^{S_0}$.
Equation (R5) gives $r\equiv-S_0\pmod7$. On $-1$ the
two values are $(-1)^r$ and $(-1)^{C_0}$, and
$r\equiv C_0\pmod2$. Thus
\[
       \rho_{\mathbf c}|_{\mu_{14}}
                    =\beta_{\mathbf c}^{-1}|_{\mu_{14}}.
 \tag{R7}
\]
The product $\beta_{\mathbf c}\rho_{\mathbf c}$ therefore
descends through (R2) to a continuous unitary automorphic
character $\gamma_{\mathbf c}$ of $T$.

This construction is explicit on arbitrary ideles. Write
$t_f=\delta k$ with $\delta\in T(F)$ and
$k\in K_{T,0}$, as in (R1), and set
\[
 \gamma_{\mathbf c}(t_\infty,t_f)
      =\beta_{\mathbf c}(\delta_\infty^{-1}t_\infty)
                         \rho_{\mathbf c}(k).
 \tag{R8}
\]
If $\delta$ is changed by $\epsilon\in\mu_{14}$,
the compact factor is changed by $\epsilon^{-1}$.
Equation (R7) makes the product unchanged. Multiplicativity
follows because the torus is abelian, and the same formula
shows triviality on rational diagonal points.

Its infinity type is exactly $\mathbf c$. Its finite
restriction to the maximal compact has conductor dividing
the first power of the fixed place $v_*$, and all those
compact values are roots of unity of order dividing28.
In particular
\[
 \gamma_{\mathbf c,f}|_{K_M}=1
                  \qquad\text{for every }M=29^e,\ e\ge1,
 \tag{R9}
\]
where $K_M$ is ALP-LIFT-10's source torus subgroup.
The finite conductor bound is independent of the size of
$\mathbf c$; the unramified values at noncompact split
places are not asserted to be roots of unity.

Every finite value is algebraic. In (R8), the finite
character value is a root of unity, and
$\beta_{\mathbf c}(\delta_\infty)$ is a product of integer
powers of conjugates of the algebraic number $\delta$.
For a fixed $\mathbf c$ these values belong to a fixed
finite coefficient field containing the normal closure of
$E$ and $\mu_{28}$.

At a nonsplit finite place $v$, every norm-one element of
$E_v^\times$ is a unit, since its valuation has norm
valuation zero. Hence $T(F_v)=K_{T,0,v}$. Our character
is trivial on that entire group, not merely on a smaller
unit subgroup:
\[
                 \gamma_{\mathbf c,v}=1
                         \quad(v\text{ nonsplit finite}).
 \tag{R10}
\]
This fact removes a potentially hidden ramified splitting
factor in the next step.

## 2. Exact change of the actual first splitting and theta integral

Let
\[
 j:\mathbb A_E^\times\longrightarrow T(\mathbb A_F),
                         \qquad j(x)=x/\bar x .
 \tag{R11}
\]
Keep the actual first pair of ALP-LIFT-09–10:
the positive group $G=U(I_2)$ and the skew line torus $T$,
with splitting characters $\chi_V=1$ and
$\chi_W=\mu_E$. Replace only the latter by
\[
              \chi_W'=\mu_E\,(\gamma_{\mathbf c}\circ j),
              \qquad\chi_V'=1 .
 \tag{R12}
\]
The restriction of the multiplying factor to
$\mathbb A_F^\times$ is1, so the required restriction
$\chi_W'|_{\mathbb A_F^\times}=\epsilon_{E/F}$ is
unchanged. Rational diagonal triviality follows from that
of $\gamma_{\mathbf c}$. Thus (R12) is an actual globally
admissible splitting character, not just prescribed
archimedean weights.

For the standard splitting used in these results, its
actual Weil operators satisfy
\[
 \boxed{\quad
 \omega'(g,t)=\gamma_{\mathbf c}(\det g)\,\omega(g,t).
 \quad}
 \tag{R13}
\]
Here are all local checks of this identity. At every
nonsplit finite place, (R10) says that
$\gamma_{\mathbf c,v}\circ j$ is literally the trivial
character of $E_v^\times$, so the local splitting has not
changed. At every split finite place, the exact determinant
root formula of AM-DO-020 evaluates the ratio on an element
$y$ with $y/\bar y=\det g$; its value is precisely
$\gamma_{\mathbf c,v}(\det g)$. This includes possible
unramified values at split places outside29. At each real
place, the character $\gamma_{\mathbf c}\circ j$ changes
the exponent $m_i$ of AM-DO-023 by $2c_i$. Its exact
Fock formula therefore changes the target determinant
power by $c_i$, giving the same scalar. The source action
depends on the unchanged opposite character $\chi_V$.
These checks prove (R13) at every place and hence globally.

For any of the actual finite Schwartz inputs and Fock
vectors already constructed, the theta series and first
theta integral consequently satisfy
\[
 \vartheta'_\phi(g,t)
       =\gamma_{\mathbf c}(\det g)\vartheta_\phi(g,t),
 \qquad
 \Theta'(\phi,f)(g)
       =\gamma_{\mathbf c}(\det g)\Theta(\phi,f)(g).
 \tag{R14}
\]
The source torus input $f$ is unchanged. In particular all
identity values, including their retained common period
and their 11-adic normalized valuations, are unchanged
exactly. The twisted first lift is nonzero whenever the
original one is nonzero. Since the character has modulus
one, the scalar automorphic $L^2$ norm and supremum norm
of the entire first lift are unchanged as well.

## 3. Removing the specified real-type obstruction in each integral convention

For a first Fock vector of fixed CM multidegree
$\mathbf d=(d_1,d_2,d_3)$, put
\[
                         \boldsymbol\nu=(0,0,1).
 \tag{R15}
\]
AM-DO-023 proves that the actual first target compact types
are
\[
              \pi_i=\det^{\nu_i}\operatorname{Sym}^{d_i}
                               (\mathbf C^2),
 \qquad\operatorname{HW}(\pi_i)=(d_i+\nu_i,\nu_i).
 \tag{R16}
\]
The specified next positive Hom edge
$U(2)\longrightarrow U(4)$ with both splitting characters
trivial has source types
\[
 \det^{-2}S_\lambda((\mathbf C^2)^*),\qquad
 \operatorname{HW}=(-2-\lambda_2,-2-\lambda_1),
 \quad\lambda_1\ge\lambda_2\ge0.
 \tag{R17}
\]
In particular the untwisted types (R16) do not occur.
This is the already proved scoped vanishing of AM-DO-023,
not a universal no-go for every chain.

### The conjugated-input integral

First use the Hermitian theta integral
$\int\vartheta(g,h)\overline{f(g)}\,dg$, as in
ALP-LIFT-09. Its source compact type must match that
of $f$ itself.

Choose in the global construction of section1
\[
                         c_i=-d_i-2-\nu_i .
 \tag{R18}
\]
By (R13)–(R14), the actual twisted first image now has
dominant weights
\[
 (d_i+\nu_i+c_i,\nu_i+c_i)=(-2,-d_i-2).
 \tag{R19}
\]
These are exactly the weights in (R17) for the one-row
partition $\lambda=(d_i,0)$. Thus the twisted first
compact representation occurs in the second oscillator,
with the same degree $d_i$ at each place. The repair
uses a genuine global splitting of finite conductor
bounded independently of $\mathbf d$.

For the explicit nonzero first vector of ALP-LIFT-09,
$\mathbf d=(2,0,2)$ and $\boldsymbol\nu=(0,0,1)$.
One takes
\[
 \mathbf c=(-4,-2,-5),\qquad C_0=-11,\quad S_0=-23,
 \qquad r=9 .
 \tag{R20}
\]
The residue character at29 is
$\rho(2)=\exp(2\pi i\,9/28)$, and the repaired first
weights are
\[
                       (-2,-4),\quad(-2,-2),\quad(-2,-4).
 \tag{R21}
\]
All these occur in the specified second source model.

A single fixed repair also works for any finite prefix of
degrees. Given bounds $D_i$ and $0\le d_i\le D_i$, use
$c_i=-D_i-2-\nu_i$. The resulting source weights are
$(d_i-D_i-2,-D_i-2)$, which occur for
\[
                    \lambda_i=(D_i,D_i-d_i).
 \tag{R22}
\]
The next Fock degree is then $2D_i-d_i$. This variant
changes the needed polynomial degree and any corresponding
archimedean coefficient norm; it is not a zero-cost
identification of the next Fock vectors.

Conversely, for this conjugated-input composition with
two fixed positive Hom edges and fixed
splitting characters, the second source spectrum has a
fixed upper bound on its highest-weight entries. Equation
(R16) then excludes sufficiently large $d_i$. The
degree-dependent repair or a finite-prefix repair changes
that datum. This observation concerns the displayed
orientation and character choices; it does not apply
without checking the alternating signs, contragredients
and pins in a different proposed source chain.

### The source's literal bilinear integral has a fixed repair

The recovered source liftT instead uses
\[
                   \int_{[G]}\vartheta(g,h)f(g)\,dg .
 \tag{R23}
\]
Its local matching condition pairs the oscillator
source type with the contragredient of the input
type. In this convention a stronger, degree-independent
repair is available. Choose
\[
              \mathbf c=\mathbf 2-\boldsymbol\nu=(2,2,1).
 \tag{R24}
\]
Then the actual first image has weights
$(d_i+2,2)$, whose contragredient weights are
\[
                        (-2,-d_i-2).
 \tag{R25}
\]
They are precisely (R17) for $\lambda=(d_i,0)$,
for every nonnegative degree $d_i$ simultaneously.
The next Fock degree stays $d_i$. Thus neither a
degree-dependent splitting nor a finite-prefix
enlargement of the next polynomial degree is needed
for the bilinear convention.

Here $C_0=5$, $S_0=9$, and (R5) gives $r=5$.
The fixed finite character is
$\rho(2)=\exp(2\pi i\,5/28)$, and
\[
       (m_1,m_2,m_3)+2\mathbf c=(3,3,3).
 \tag{R26}
\]
Consequently one actual fixed character
$\chi_W'=\mu_E(\gamma_{(2,2,1)}\circ j)$
repairs all of these real types in the literal
bilinear composition. This is an independent
convention-specific conclusion; it does not turn
the two different theta integral conventions into
the same map.

Equivalently, (R23) is the conjugated-input lift
of $\bar f$, whose compact type is the
contragredient. This reformulation is useful when
applying an inner-product theorem written with
the conjugated-input convention.

## 4. Integral class values and the actual cost scope

The identity values and scalar automorphic norms are
preserved by (R14) without choosing representatives.
An integral class-value claim requires a specified
finite target level and its coefficient lattice.
AM-R-008 proves the relevant precise statement: with
compact-determinant representatives and a character
trivial on $\det K$, multiplication by
$\gamma_f(\det g)$ is a diagonal root-of-unity map.
It preserves the entire local content and the mass
norm, with the coefficient action twisted by
$\gamma_\infty^{-1}$ in that note's left-equivariant
convention. This inverse is consistent with the positive
right-translation twist in (R14); the two statements
use their respective explicit function conventions.

For the explicit group level of AM-R-008, (R9) verifies
its character hypothesis. There is consequently no
additional denominator, content or logarithmic norm
cost for the determinant twist on that class module.
All its displayed finite class scalars have order
dividing28.

The source torus stabilizer $K_M$ in ALP-LIFT-10 must
not be confused with a proved target $U(2)$ stabilizer.
This note does not assert that the original first
vectors are invariant under the particular target
group level of AM-R-008 without checking that
target action. Every finite family of their Schwartz
vectors has an open target stabilizer; it can be
refined inside the kernel of $\gamma_f\circ\det$.
Applying a compatible compact-determinant class
presentation then transports its actual class-value
module by the same root-of-unity diagonal map.
Its original stabilizer index, mass and coefficient
lattice remain costs to be computed if needed.

Likewise this does not identify the transported module
with an independently pinned arithmetic row. The
first edge has ranks1 and2 and already lies outside
the source's even-rank equal-character StdPair
constructor. The later PinX.mv and PinColT.om
interfaces require the same specified character
on both members of an even-rank edge. Changing
only $\chi_W$ in (R12) is a valid actual first
theta lift, but is not a verification of those
different equal-character pins.

## 5. What remains for a second actual lift

The repaired first input has exactly the real
representation required by the chosen second
oscillator, and it retains the actual nonzero
first value and first norm. Local occurrence at
infinity is a necessary condition, not a proof
that its global next theta integral is nonzero.
One must still select actual finite second-kernel
inputs, prove a nonzero global pairing, and retain
the resulting mass and norm factors. A formal
Gram picture or a hyperbolic Witt-tower persistence
theorem does not establish this for a sequence of
positive definite groups.

The $\mathbf Q(\zeta_{28})$ host, the full DP65
conjugated-action rows, source tied direction
matrices, and the terminal six-identity family
remain separate comparisons. This construction
removes a specific real-type obstruction without
claiming the complete requested chain.

## Exact source locators

- ALP-LIFT-09, actual_torus_first_lift.md, (V2)–(V11),
  torus class number and the original global splitting,
  and (V32)–(V38), actual first lift and projectors.
- ALP-LIFT-10, permitted_orbit_first_image.md, (O21),
  (O23)–(O28), (O31)–(O35), the exact fixed source
  levels, normalized values and input costs.
- AM-DO-020, exact split-place determinant-root
  covariance; AM-DO-023,
  definite_oscillator_real_second_edge.md,
  (DO23.4)–(DO23.11), actual honest real target
  weights and the trivial-source-character case.
  Its corrected nontrivial source-character sign
  is not needed here.
- Konno, T., & Konno, K. (2007). On doubling construction
  for real unitary dual pairs. Kyushu Journal of
  Mathematics, 61(1), 35–82. Proposition4.4(ii),
  pp.68–69, and Lemma5.2(i), p.73.
  https://www.jstage.jst.go.jp/article/kyushujm/61/1/61_1_35/_pdf
- AM-R-008, compact_determinant_twist_accounting.md,
  (R8.2), (R8.10)–(R8.15), the actual integral
  class-value and mass isometry with its stated
  level hypothesis.
- The actual source bilinear convention is
  WittSmallGroupEmbeddingMemPointwiseStabilizerIso.lean,
  liftT_apply, lines160–167, as directly checked
  in AM-DO-023/024's source audit.

## Check status

The exact finite-residue and weight calculations are
included in fixed_conductor_type_repair_certificate.py.
Author and independent whole-proof checks, with their
actual scope and time, are recorded separately in
lift_accounting_CHECK_EVENTS.tsv. No Lean execution is
claimed.
