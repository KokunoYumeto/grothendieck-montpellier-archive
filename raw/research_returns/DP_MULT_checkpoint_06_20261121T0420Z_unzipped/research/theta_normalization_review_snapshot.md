# Theta normalization, the integral connection, and the exact harmonic obstruction

Agent: `/root/step2_higher`. Model: **GPT-6 Astra Pro**. Effort setting: **not exposed**. Date: 2026-11-21 (UTC). This is a source-interface and mathematical research memo, not a Lean execution report. It does not audit RH or question the accepted Alpoge theorems. The main paper was not edited.

The source root in all locators below is
`/workspace/scratch/97b2cc84526f/DP_MULT_work/research/external_lean/`.
All newly recovered files came directly from the author's split archive, not merely a mirror. Their exact archive members and SHA256 values are in `theta_normalization_sources_consolidated.json`.

## 1. Result of the concrete source trace

The source does **not** obtain its theta jets merely by taking invariant derivatives of an integral algebraic theta function. Its precise local expression is

\[
 \operatorname{nabVal}(f;P)
   =\left.P(D)\bigl(f\,\exp(kh_L)\bigr)\right|_0,
 \qquad h_L(X)=h(X,[w_0]X).
\tag{TN1}
\]

Here the algebraic germ and the formal group, action and biextension cocycles have integral models. The rational gauge $h$ is required to satisfy specified exponential coboundary, symmetry and adjoint identities; its exponential is not required to be an integral series. Crucially, the source **does prove** integrality of the conjugated connection and invariance of the selected harmonic values under changes of canonical gauge. These are supplied theorems, not unfilled definition names.

Consequently, an unbounded denominator result for the entire series $f\exp(kh_L)$ cannot by itself obstruct the selected harmonic jets. Conversely, the source's harmonicity is a family of **sums over columns**. It is not the stronger family of individual per-column contractions which would make every axes-vanishing exponential invisible. Sections 5–7 give exact proofs and counterexamples.

The local Poincaré cocycles in DP36 can be made equivariant by a concrete integral averaging construction (Section 4), once the actual dual torus characters have been identified. This removes a substantial local existence issue. It does not identify the source's geometric theta normalization or its global path/minor data with an arbitrary local kernel.

## 2. Exact definitions and integral input

### 2.1 Formal biextension and gauge

`ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/CocycleRightZeroThd.lean` contains:

| Locator | Content used here |
|---|---|
| `FB`, lines 86–158 | Integral formal group $F$, $O$-action, two partial-addition cocycles `ph1`, `ph2`, symmetry cocycle `sy`, and adjoint cocycles `ad`; axes, associativity, interchange, symmetry and adjoint identities. |
| `FB.IsCanonGauge`, lines 174–183 | $h(0,Y)=h(X,0)=0$; the two cocycles are the exponentials of the corresponding addition coboundaries of $h$; $\mathrm{sy}=\exp(h(Y,X)-h(X,Y))$; $\mathrm{ad}(a)=\exp(h([a]X,Y)-h(X,[a^*]Y))$. |
| `FB.hL`, line 185 | $h_L(X)=h(X,[w_0]X)$. |
| `FB.nabVal`, lines 187–189 | Equation (TN1), by definition. |

The axes identities imply that every monomial of $h$ uses variables from both arguments. In particular $h_L$ has zero constant and linear terms. They do not imply coefficientwise integrality of $h$ or $\exp(kh_L)$.

`Formalism/LocalToGlobal/ProjectiveLattices/ThGerm.lean` defines `IsGerm` at lines 172–181, `ChartAt` at 189–206, and `IsNab` at 208–217. A chart includes a generic canonical gauge and the comparison between its formal series and actual line-bundle frames. `IsNab` identifies the global differential rule with (TN1) whenever the corresponding `IsGerm` relation holds.

`Formalism/SharpRestriction/Divisibility/GeneratorPowers/ExpTieAlg.lean`, theorem `nabVal_eq_const` at lines 413–419, spells out the same normalized invariant-derivative identity. `GeneratorPowers/ExpTiePf.lean`, theorem `tie_holds` beginning at line 328, constructs the exponential germ

\[
 g=\bigl(f\exp(kh_L)\bigr)\circ\varphi
\]

and identifies its factorial coefficients with the normalized jet values. In the proof, the selected germ is explicit at line 333. `GeneratorPowers/ExpTie.lean`, `IsExpGaugeOf` at lines 53–59, compares the exponential frame with the algebraic frame by the jet of $\exp(-h_L\circ\varphi)$.

These latter units live in jet rings over a **rational coefficient algebra**. Their being units is not a claim that their coefficients lie in the integral valuation ring.

### 2.2 What the integral chart does and does not supply

`Formalism/LocalToGlobal/ProjectiveLattices/ChartDirectionsIntegral.lean`:

* `IsIntPS`, lines 16–17, means every coefficient is in the image of the valuation ring.
* `IntData`, lines 61–89, includes the integral abelian model, tangent eigenbases, a theta section, comparisons of rigidified line bundles, and section pullbacks.
* `IntData.θgen`, lines 74–75, says that the theta section generates the **global section module** over the valuation ring.
* `IsGenFibreChart`, lines 111–151, and `IntegralChartA3`, lines 155–179, supply integral lifts of the formal group, action, partial-addition cocycles, symmetry and adjoint cocycles, and directions. The generic gauge is a field-valued datum in `ChartAt`.

No field in these definitions says that the first nonzero homogeneous Taylor part of the theta germ is primitive. Global section generation must not be renamed as that stronger local assertion. Even a primitive whole power series can have nonprimitive first homogeneous part, as $p-X$ shows. A separate constant-multiplicity or tangent-cone theorem could establish primitivity for a particular theta divisor; none was proved in this source pass for the genus-three example.

`GeneratorPowers/GaugeIntCut.lean` defines `IntBelow`, `SmallUnits`, `ExpLogIntSt` and `LawLogIntSt` at lines 14–30. These are explicitly truncated assertions under the assumption that the relevant small integers are units. They do not state all-order integrality of the exponential gauge.

### 2.3 Relation to the previously recovered B0 input

`Formalism/SharpRestriction/Divisibility/ProductZerothFirstParts.lean`, lines 181–201, defines `B0` by an identity expressing the logarithmic theta series as an integral series times a specified exponential correction; `AdmB` includes B0 through B4. Here `be` is a general multivariable power series and `beSum` sums its copies; B0 does not itself assert that this correction is quadratic. `JetPolynomialLogs/OneLetterJetKernel.lean`, theorem `kernel_from_twist_holds` at lines 54–90, consumes that identity. The source therefore has an actual normalized-theta identity at its height-two interface. The requested higher-height replacement needs a new realization of that identity, or an appropriate replacement estimate for the selected connection; simply taking an arbitrary integral algebraic theta germ does not instantiate B0.

## 3. The connection and harmonic transfer are supplied theorems

Write $s_i(X)=-\partial_{Y_i}h(X,0)$ and $S_{ij}=[X_j]s_i$. On the auxiliary ring $K[[X,Z]]$, the source's connection is

\[
 \nabla_{u,\phi}
 =D_u+\sum_i(D_us_i+\phi_i)\partial_{Z_i}
   -k\sum_i(Z_i-s_i)u_i.
\tag{TN2}
\]

Its integral lattice is

\[
 H_h=\{(u,\phi-Su):u,\phi\in R^d\}.
\tag{TN3}
\]

Exact locators are `TaylorDiscriminants/ConnectionKillsSeries.lean`: `sgOf`18–19, `sg1`21–22, `nabla`31–34, `Hset`41–43, `betaH`48, `ConnectionIntegrality`77–83 and `AdmissibilitySecond`101–108. The alternating form is
$\beta_H((u,\phi),(u',\phi'))=\phi'\cdot u-\phi\cdot u'$.

### 3.1 Actual integral-connection theorem

In `TaylorDiscriminants/WickVanishing/ExpConjConnectionIntegral.lean`:

* `exp_conj_connection_integral`, lines 40–82, proves that for integral $u',\phi'$ and integral $G(X,Z)$,

\[
 e^{-kh_L}\nabla_{u',\,\phi'-Su'}(e^{kh_L}G)
       \in R[[X,Z]].
\tag{TN4}
\]

  Its hypotheses are an integral formal biextension, a canonical gauge, and $w_0+w_0^*=1$. It does **not** assume that $e^{kh_L}$ is integral.
* `connection_first_identity`, lines 84–90, packages this as the proposition `ConnectionIntegrality`.

This is paired with `WickVanishing/ConnectionSecondOfCommute.lean`, theorem `connection_second_identity` at lines 50–51, and `WickVanishing/ConnectionKillsSeries.lean`, theorem `connection_kills_series` at lines 117–120. The latter kills functions depending only on $X$ when the tangent component is zero. The former gives the central commutator $k\beta_H$.

`WickVanishing/HarmonicValueIntegral.lean`, theorem `harmonic_value_integral` at lines 144–147, proves `ValueSt`. Despite the filename, this particular conclusion is the equality of a constant coefficient of the connection expression with an invariant differential value; its statement must not be paraphrased as an unconditional positive-divisibility theorem.

### 3.2 Actual ordered-column estimate

`TaylorDiscriminants/GermSC.lean`, `SCSt`29–41, gives the complete formal hypotheses:

1. A fractional $R$-submodule $J\subset K$ with $1\in J$.
2. An integral formal biextension and canonical gauge, and $w_0+w_0^*=1$.
3. Integral-lattice directions $\xi_\ell\in H_h$, and corrections $\psi_\ell$ whose entries lie in $J$.
4. A color $c(\ell)$ and a two-side label $s(\ell)$, with all three displayed symplectic pairings vanishing unless colors agree and sides are opposite.
5. An integral polynomial $P$ with
   $\sum_c\min(\text{degree on side + in color }c,\text{degree on side − in color }c)\le e$
   on each monomial of its support.
6. An integral algebraic germ $f$.

The conclusion is that the ordered connection value on $e^{kh_L}f$ lies in $J^e$. `GermSCCols.lean`, `SCColsSt`10–22, gives the corresponding multi-column product/sum expression, with a bound on the sum of the columnwise `pairMin` values.

These estimates are **supplied without residual theorem assumptions** in `WickVanishing/Closed.lean`:

| Theorem | Exact locator | Conclusion |
|---|---|---|
| `lemma_H_columns` | lines 22–23 | `LemmaHColsSt`, the selected ordered-connection / invariant-derivative comparison under its displayed second-order annihilation. |
| `symmetric_canonical_gauge` | lines 25–26 | `SCSt`, using the supplied first, second and killing identities. |
| `scaled_connection_columns` | lines 47–63 | `SCColsSt`. |

The proof route is also explicit in `SCMain.sc_of`28–83, `SCCols.scaled_connection_columns`35–36, and `LemmaHCols.lemmaHCols_of` beginning at line 223. The general estimate involves **controlled denominators**, not the new positive formal-function slopes: for $J=p^{-b}R$ it gives valuation at least $-be$. It contains no height-$h$ positive slope for the normalized connection.

### 3.3 Actual canonical-gauge independence

`WickVanishing/CanonB.lean`, theorem `canonGauge` at line 334, supplies `CanonGaugeSt` for a finite free reduced $\mathbb Z$-algebra $O$ with involution. `Development/AbelianVarietyTheory/Proofs/FormalGroupCharts/CanonGaugeIndependenceAll.lean`, theorem `GlobalTheory.canonGauge_independence_all` at lines 23–26, supplies

\[
 \texttt{AdmissibilitySecond}\ \wedge\ \texttt{GaugeExpSt}\ \wedge\
 \texttt{GaugeIndependenceColumns}\ \wedge\ \texttt{NabTransSt}.
\]

It explicitly instantiates the generic exponential, substitution, biadditivity, quadratic-derivative and Wick identities in `G2Assumption.galois_twist_preserves_siegel_bound` (lines 11–52). Thus this is not an unconstructed gauge-independence gate.

For two canonical gauges, their difference is symmetric, biadditive and adjoint-balanced. In logarithm coordinates it is a balanced bilinear form; its diagonal $X\mapsto (h'-h)(X,[w_0]X)$ is quadratic. The selected value is unchanged when the **displayed associated second-order operator** kills $P$. This controls these quadratic gauge ambiguities; it does not automatically annihilate higher-degree terms of the primitive Poincaré splitting.

## 4. DP37 companion: an integral equivariant Poincaré frame

**Proposition (integral finite-group averaging).** Let $R$ be a complete unramified valuation ring of residue characteristic $p$, and let $\Gamma$ be a finite group of order $N$ prime to $p$. Suppose an integral normalized biextension on a product of formal groups carries a $\Gamma$-action preserving its group laws and axial rigidifications. Then an integral axis-normalized frame can be chosen $\Gamma$-invariant.

If, in logarithm coordinates of the actual pair $G_h\times G_h^D$, the action is

\[
 (x,y_1,\ldots,y_{h-1})\longmapsto
 (\zeta x,\zeta^{-p}y_1,\ldots,\zeta^{-p^{h-1}}y_{h-1}),
 \qquad \zeta^{p^h-1}=1,
\tag{TN5}
\]

then the integral partial-addition cocycles admit a rational logarithmic splitting $\beta$ which is invariant, vanishes on both axes, and has no bidegree-$(1,1)$ term. Here existence of the rational splitting is the already proved formal biextension splitting from DP35; the identification of the actual torus action with (TN5) is the separate torus calculation in DP37.

**Proof.** Start with an integral normalized frame $e$. Write $g(e)=c_g e$. Preservation of the rigidifications gives $c_g\in1+I$, where $I$ is the formal-origin ideal and the restrictions of $c_g$ to either axis are one. Put

\[
 U=\prod_{g\in\Gamma}c_g,\qquad u=U^{1/N}\in1+I.
\]

The normalized $N$th root exists uniquely and integrally: solve each homogeneous coefficient of $u^N=U$ in increasing degree, dividing only by the unit $N$. It restricts to one on either axis. The cocycle identity is $c_{\sigma g}=\sigma(c_g)c_\sigma$, so

\[
 \sigma(U)=U/c_\sigma^N.
\]

By uniqueness of the normalized root, $\sigma(u)=u/c_\sigma$. Consequently $\sigma(ue)=ue$. This proves the first assertion. Its two addition cocycles are integral normalized units and are invariant, because all defining structure maps and the frame are equivariant.

Choose any rational logarithmic splitting $\beta_0$ of those cocycles, normalized on the axes. Then
$\beta=N^{-1}\sum_g g(\beta_0)$
is still a splitting, since the two additive coboundary operators commute with the action and the logarithms of the cocycles are invariant. It remains axis-normalized and is invariant. A bidegree-$(1,1)$ monomial has the form $xy_i$ and character $\zeta^{1-p^i}$. For $1\le i<h$, $p^i-1$ is positive and strictly smaller than $p^h-1$, so this character is not trivial. Hence no such coefficient survives averaging. ∎

This proves the local **existence of a splitting with the DP36 symmetry/cocycle/no-bilinear-term hypotheses**, once the genuine Cartier-dual action is identified. It makes no assertion that $\exp\beta$ is integral. Its coefficients can have the unbounded denominators established in DP35.

## 5. Fischer pairing and the exact harmonic ideal

Let $K$ have characteristic zero. For a polynomial $P$ and a formal series $f$, use the factorial pairing
$\langle P,f\rangle=P(\partial)f(0)$.
For every polynomial $Q$ one has

\[
 \langle P,Qf\rangle=\langle Q(\partial)P,f\rangle.
\tag{TN6}
\]

**Proof.** It suffices to take $P=Z^\alpha$, $Q=Z^\beta$ and $f=Z^\gamma$. Both sides vanish unless $\alpha=\beta+\gamma$, and in that case both equal $\alpha!$. Linearity and the finiteness of the jet read by $P$ prove the assertion for formal $f$. ∎

Therefore, if every $Q_j(\partial)P=0$, then $P$ annihilates the closed formal ideal $(Q_j)$. If $\eta\in(Q_j)$ has zero constant term, then
$\exp\eta-1=\eta\sum_{n\ge1}\eta^{n-1}/n!\in(Q_j)$,
so

\[
 \langle P,f\exp\eta\rangle=\langle P,f\rangle
 \quad\text{for every formal }f.
\tag{TN7}
\]

The mathematical shortcut proposed by the parent is thus correct **when the claimed ideal containment is true**. The next section identifies why the source hypotheses do not give that containment for an arbitrary axes-vanishing higher-order kernel.

### Exact source contractions

`Formalism/LocalToGlobal/ProjectiveLattices/RowDeg.lean` defines

\[
 \Delta_{\tau,a,a'}=
 \sum_{b,b'}h^{-1}_{bb'}\,
   \partial_{Z_{\tau,a,b}}\partial_{Z_{\bar\tau,a',b'}}
\]

in `lap`21–25. `harmK`27–30 is the intersection of the corresponding kernels. `HHa`43–44 specializes $h^{-1}$ to the identity, giving

\[
 \Delta_{\tau,a,a'}=
 \sum_b\partial_{Z_{\tau,a,b}}\partial_{Z_{\bar\tau,a',b}}.
\tag{TN8}
\]

`RowInv`37–38 adds invariance under adding an earlier row to a later row, `RowDeg`40–41 fixes each row's total degree, and `HaO`46–48 adds integral coefficients. `IsThRule.lean`, `harmA`86–87, uses exactly this definition with complex conjugation and `InPsi H`. Thus the dual ideal is generated by **column sums** $\sum_b Z_{\tau,a,b}Z_{\bar\tau,a',b}$, not all individual products.

For the pure CM type $\Phi=\{1,2,3\}\subset(\mathbb Z/7)^\times$, its conjugate is $\{6,5,4\}$ and there is no overlap. If one applies this same formula with row multiplicity one on $\Phi$ and zero outside it, every contraction has an empty row index on one side. Harmonicity is then vacuous. In particular, the height-three line of character3 and dual directions of characters1,2 do **not** acquire the individual contractions $\partial_x\partial_{y_i}$ from (TN8). This is a precise obstruction to that proposed shortcut. It does not construct a replacement `Datum` in the old induced-type host; DP25 already distinguishes those global structures.

## 6. DP39(a): unbounded gauge denominators can be completely invisible to harmonic jets

**Proposition.** For every prime $p$, there are integral formal-biextension data satisfying all the source's canonical-gauge identities, two canonical gauges, and a primitive integral algebraic germ $f=1$, such that the normalized series in one gauge has unbounded denominators but all the selected harmonic values are unchanged. More strongly, the equality holds for every germ $f$ when the polynomial is killed by the relevant contraction.

**Construction and proof.** Let $R=\mathbb Z_p$, $K=\mathbb Q_p$, let $F=\widehat{\mathbb G}_a^2$, and put $O=\mathbb Z\times\mathbb Z$ with involution $(a,b)^*=(b,a)$. Let $(a,b)$ act by $(X_1,X_2)\mapsto(aX_1,bX_2)$. Give the biextension the trivial cocycles `ph1=ph2=sy=ad=1`, namely the source's `FB.triv`.

Both

\[
 h_0(X,Y)=0,\qquad
 h_1(X,Y)=X_1Y_2+X_2Y_1
\]

are canonical gauges. The axes vanish. Biadditivity makes both addition coboundaries zero. Symmetry gives $h_1(Y,X)-h_1(X,Y)=0$. Finally

\[
 h_1((aX_1,bX_2),Y)
 =aX_1Y_2+bX_2Y_1
 =h_1(X,(bY_1,aY_2)),
\]

which is exactly the adjoint condition.

Take $w_0=(1,0)$. Then $w_0+w_0^*=1_O$ and
$h_{1,L}(X)=h_1(X,(X_1,0))=X_1X_2$.
For $k=1$ and $f=1$ the normalized series is

\[
 \exp(X_1X_2)=\sum_{n\ge0}(X_1X_2)^n/n!.
\]

Its coefficient valuations $-v_p(n!)$ tend to $-\infty$. Nevertheless, if
$\partial_U\partial_VP=0$,
then $P$ is a sum of a polynomial in $U$ alone and one in $V$ alone. Restricting $\exp(X_1X_2)$ to either axis gives one, so for every $f$,

\[
 P(\partial_1,\partial_2)\bigl(f\exp(X_1X_2)\bigr)(0)
 =P(\partial_1,\partial_2)f(0).
\]

Equivalently this follows from (TN7) for $Q=X_1X_2$. In the source's `AdmissibilitySecond` normalization, the matrix of the diagonal quadratic has off-diagonal entries one, so the displayed `secondOrder` is $2\partial_U\partial_V$. Its kernel over $K$ is the same. For $f=1$ all positive-degree harmonic values vanish and the constant value is one. ∎

This example concerns a trivial additive formal biextension. It is not claimed to be an ample theta divisor or a primitive Poincaré class. Its purpose is exact: even a primitive initial term of $f$ and unbounded full-series denominators do not by themselves imply a failure of harmonic selected-jet integrality.

## 7. DP39(b): the actual-pair two-column test defeats the stronger shortcut

This part uses the explicit primitive Poincaré coefficient proved in **DP38**, `primitive_poincare_first_coefficient_DP38.md`, SHA256 `4209c45180d5d45f8a8837c30d05642b110e00a13c6c7fd5d6aff74c0123d6d3`. I independently read and challenged that whole saved memo, including its cyclic-display calculation against the displayed Zink source formulas, and reported PASS at the observed clock01:56:49 UTC. The calculation below is independent of that display derivation. The exact required input is restated for clarity.

**Input.** Let $p$ be odd, $h\ge2$, $d=h-1$, and use the actual pair $G_h\times H$, $H=G_h^D$, of DP32. In logarithm coordinates let $B(x,\mathbf y)$ be a normalized rational splitting of the primitive Poincaré class with

\[
 B(x,0)=B(0,\mathbf y)=1,
 \qquad [x^p y_1]B=\kappa/p,
 \quad\kappa\in R^\times.
\tag{TN9}
\]

DP38's explicit invariant normalization has $\kappa=1$; only the fact that it is a unit is used. Define a two-copy kernel

\[
 \Theta=B(x_1,\mathbf y^{(1)})^{1/2}
             B(x_2,\mathbf y^{(2)})^{1/2}
\]

and the integral polynomial

\[
 P=X_1^pY_{1,1}-pX_1^{p-1}X_2Y_{1,2}.
\tag{TN10}
\]

**Claim 1: the full displayed HaO-type conditions hold.** Give the positive type one row, the negative type $d$ rows, and use two columns. Put row degrees $p$ on the positive row, $1$ on the first negative row and $0$ on its other rows. Coefficients are integral. Each monomial has exactly these row degrees. The sole positive row admits no row operation. The polynomial uses only the first negative row; the source's operations add an earlier row to a later row and therefore do not change it. Finally, for

\[
 \Delta_i=\partial_{X_1}\partial_{Y_{i,1}}
            +\partial_{X_2}\partial_{Y_{i,2}},
\]

one has $\Delta_iP=0$ for $i>1$ because these variables do not occur, and

\[
 \Delta_1P=pX_1^{p-1}-pX_1^{p-1}=0.
\]

Thus this polynomial satisfies the exact formal `harmK`, `RowInv`, `RowDeg`, and integral-coefficient requirements. It need not satisfy the stronger separate per-column contractions: the first contraction of the first term is nonzero.

**Claim 2: its primitive-kernel value is a unit.** Because $B-1$ vanishes on each axis, every monomial in it has positive $x$-degree and positive total $\mathbf y$-degree. Hence terms of order at least two in $(B-1)$ cannot contribute to a coefficient linear in $y_1$. The binomial expansion gives
$[x^p y_1]B^{1/2}=\kappa/(2p)$.
The first monomial in (TN10) therefore contributes

\[
 p!\,\kappa/(2p)=\kappa(p-1)!/2.
\]

The second contributes zero: on the first copy it takes $p-1>0$ derivatives in $x_1$ with all $\mathbf y^{(1)}=0$, and that factor is identically one. Thus

\[
 P(\partial)\Theta(0)=\kappa(p-1)!/2\in R^\times.
\tag{TN11}
\]

**Claim 3: every integral function on the actual product has a value divisible by $p$ for the same invariant polynomial.** Let $f$ be any integral function on $(G_h\times H)^2$. The coefficientwise height-$\ge2$ derivative bound gives
$D_{x_1}^p(R[[G_h\times H\times G_h\times H]])\subset pR[[G_h\times H\times G_h\times H]]$.
This also follows directly from the general bound at $n=p<q$: $v_p(p!)=1$ and $\lfloor(p-1)/(q-1)\rfloor=0$.
The remaining integral invariant derivations preserve that ideal and commute. The second summand in $P(D)$ has its explicit factor $p$ and otherwise only integral invariant derivations. Therefore

\[
 P(D)f(0)\in pR.
\tag{TN12}
\]

Equations (TN11)–(TN12) refute the proposed implication that the source's **summed harmonicity alone** transfers the entire integral-formal-function derivative bound through the primitive Poincaré exponential. All statements are stable under replacing the exponent $1/2$ by any $p$-adic unit, with the corresponding unit factor in (TN11).

**Scope.** This is an actual-formal-pair test with precisely the source-shaped HaO algebraic conditions, using the independently checked DP38 coefficient. It does not assert that $U=1$ is the algebraic germ of a global theta section, or that these row labels already define a new mixed-type global correspondence. It disproves a local implication; it does not exclude all possible weighted selected-connection estimates, all extra vanishing conditions on geometric theta sections, or all shorter global chains.

## 8. The precise remaining interface

The source trace closes several overly broad missing-data statements. Integral algebraic charts, canonical gauges, the normalized derivative identity, integrality of the conjugated connection, and harmonic gauge-independence all have exact source interfaces and supplied formal theorems. Moreover the finite-group averaging proposition supplies an equivariant local Poincaré splitting of the type used in DP36, once its genuine torus action is fixed.

For a new mixed-type genus-three construction, the first geometric identification still to supply is a relation between **the prescribed theta normalization** and the actual-pair kernel. A concrete sufficient form is an equality, or equality under all intended selected Fischer evaluations,

\[
 \bigl(f\exp(kh_L)\bigr)\circ(E_0,\mathcal E)
 \ \sim\ U(E_0,\mathcal E)\exp((\sigma/2)\beta),
\tag{TN13}
\]

with $U$ integral, the relevant actual Poincaré class and torus action, the stated path, and all normalization factors explicitly controlled. An allowable quadratic gauge change can be removed by the source's harmonic theorem; arbitrary higher-degree terms cannot be discarded by invoking that theorem. DP39(b) supplies a concrete obstruction to the latter shortcut.

The corresponding quantitative operator route must estimate the actual mixed-type lattice $H_h$, its corrections $\psi$, the chosen polynomial/minor module and its path after the integral conjugation (TN4). The existing SC theorem already handles the algebra of that passage, but only with its specified denominator module and contraction count. Its hypotheses do not automatically give the higher-height positive slope. The operator/entry norm, nonvanishing minors, and path identifications are still new geometric quantitative data.

At the global end, the source's induced-type/Serre-tensor host cannot be retained for the genus-three mixed CM type (DP25). A new source and terminal correspondence, its allowed harmonic module, and the period/norm/rank/level/polarization/covolume costs must be specified before an integer lift saving follows. Neither the existence of a finite numerical saving under a fictitiously fixed budget (DP26) nor the sharp local scalar slope resolves those identities.

## 9. Provenance and actual check record

The consolidated source manifest records **421 newly extracted unique Lean modules**, **3,799,539 bytes**, and **526 total local Lean modules** after adding them to the previous 105. The broad recovery was used to locate the concrete definitions and theorem providers. It is not a claim that every recovered module was read. No Lean process was run.

The following are actual source-reading and proof-check events performed by this agent on 2026-11-21, continuing the earlier source trace from approximately 01:41 UTC. Final event metadata and math-block hashes are recorded in `theta_normalization_checks.json`.

* **TN-S001:** Read `CocycleRightZeroThd.lean` completely (224 lines), the complete `ChartDirectionsIntegral.lean`, and `ThGerm.lean` completely through its end; checked the precise meanings of `IsCanonGauge`, `hL`, `nabVal`, integral cocycles and global theta generation.
* **TN-S002:** Read `IsExpChart.lean` completely and `PlaceBelow.lean`1–85; re-read the selected `ExpTie`/`ExpTieAlg` statements and complete main `ExpTiePf.tie_holds` proof previously inspected; read the complete `GaugeIntCut.lean` and `ExpGUPf.lean`. Distinguished generic jet units from integral coefficients.
* **TN-S003:** Read the complete `ConnectionKillsSeries.lean` definitions; complete `ExpConjConnectionIntegral.lean`, `ConnectionSecondOfCommute.lean`, `WickVanishing/ConnectionKillsSeries.lean`, `SCMain.lean`, `SCCols.lean`, `GermSC.lean`, `GermSCCols.lean`, and `Closed.lean`. Read the complete `LemmaHCols.lean` file and the terminal equality proof in `HarmonicValueIntegral.lean`. Verified actual supplied theorem declarations rather than treating definition names as proof.
* **TN-S004:** Read `G2Assumption.lean` and `CanonGaugeIndependenceAll.lean` completely; read the `canonGauge` theorem statement and its opening construction in `CanonB.lean`. This is a source-interface check, not a claim that every imported theorem was independently reconstructed.
* **TN-S005:** Read `RowDeg.lean`, `IsThRule.lean`, and `HarmonicChartValues.lean` completely. Checked summed contractions, row-operation orientation, fixed row degrees, the integral coefficient condition, and the actual `harmA` specialization.
* **TN-P001:** Independently proved the finite-group normalized-root construction in Section4, checking the cocycle orientation, equivariance of the new frame, axial normalization, the integral root construction, and absence of invariant bidegree-$(1,1)$ terms.
* **TN-P002:** Independently checked the factorial Fischer adjunction (TN6), formal-ideal closure and exponential consequence (TN7), including the reason only finitely many coefficients enter each evaluation.
* **TN-P003:** Checked the full DP39(a) example: every formal-biextension/gauge axiom, $w_0+w_0^*=1$, the diagonal quadratic, factorial denominators, the exact second-order contraction and every selected value.
* **TN-P004:** Checked all algebraic steps of DP39(b), including the two-column cancellation, row-invariance orientation, fixed row degrees, the square-root coefficient and both operator valuations. The required DP38 coefficient has subsequently been independently checked in TN-P005; no global theta realization is claimed.
* **TN-P005:** Read all of the saved DP38 memo (hash above), independently challenged the cyclic display/dual, both telescoping defect formulas and their signs, weighted homogeneity of the particular Witt carry, injectivity after reduction to a nilpotent degree quotient, invariance under bilinear or integral frame changes, the exact low-degree torus-monomial classification, the logarithm-coordinate substitution, and the integral-function comparison. Compared Zink's published extracted text at Definition19/(22), Theorem81/(146), Proposition106, and (218). Result: **PASS**. This is a completed independent proof check, not merely a reviewer request. The source comparison used the published PDF's extracted text; it is not recorded as a fresh visual page check.
* **TN-P006:** Read the entire saved memo after integrating DP38, rechecked all four proof blocks and their precise source/application scope, and corrected the B0 description to avoid calling a general power-series correction quadratic. Result: **PASS**.
* **TN-I001 (reported independent review):** `/root/formal_bound` read the full memo and directly compared `RowDeg`, `IsCanonGauge` and `AdmissibilitySecond`; independently challenged both DP39 examples, including the row-shift orientation, factor two in the first contraction, and the actual-pair coefficient and operator divisibility. Reported **PASS**. This is a completed review report; its separately saved snapshot/hash is controlled by that reviewer.
* **TN-I002 (reported independent review):** `/root` read the full memo and independently checked DP39(a),(b), Fischer adjunction, the invariant-frame proof and the exact source distinction. Reported **PASS**, with the B0 wording correction now applied. This does not turn the source-reading events into a Lean execution.

