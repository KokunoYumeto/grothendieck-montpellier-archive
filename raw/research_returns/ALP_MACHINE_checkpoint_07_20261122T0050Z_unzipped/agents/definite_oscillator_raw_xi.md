# AM-DO-029: the actual raw Xi as a finite Heisenberg vector, its exact cost, and the 29-only mismatch

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`;
inherited reasoning effort is not separately exposed; 21 November 2026 UTC.

This finding concerns the **prescribed** `xiAt` and the finite clauses of
`IsRatDatum`. It uses the carried THETA3-A12/A13/A15 finite-model results
at their checked status, and the actual mixed host and normalization of
AM-DO-022/026. It does not replace a prescribed array by an arbitrary
Schwartz function. The new conclusions are its explicit finite-window
realization on the mixed host, exact norm and denominator accounting,
and a precise obstruction to identifying it with the previously
constructed input supported only at 29.

## 1. Literal source interface and local windows

All source paths below are relative to
`work/research/alpoge_source`, pinned to commit
`7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`. Reading these recovered
definitions is not a Lean compilation or a transitive dependency audit.

| Source | Locator | Content used |
|---|---|---|
| `Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsRatDatum.lean` | 19–28 | `IsFinComb`; the three clauses of `IsRatDatum` |
| `Development/AbelianVarietyTheory/Definitions/LatticeFrames/LevChiEqOne.lean` | 68–71 | actual `TwDat.xi`, obtained from `xiAt` and the specified frames |
| `Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/XiAtPenultimateEqXiCpl1.lean` | 146–163 | the three branches `XiEntry`, `XiCpl1`, `xiLast`; all contain `phiT` |
| `Formalism/LocalToGlobal/Columns/FiniteSumNonzeroLargeDepth.lean` | 646–648; 927–948; 981–986 | `phiT`; the local `PhiAt`, `omPhi`, `E1at`, `XiAt`; `joinCol`, `PsiAt` |
| same | 1047–1065 | `ChIdx.Ok.psiSupp`, `psiInv`, `xiSupp`, `xiInv`, `psiSuppX`, `psiInvX` |
| same | 1108–1138 | `Sall`, `cAof`, `cBof`, `XiEntry`, `XiCpl1` |
| `Formalism/LocalToGlobal/IndefiniteReal/LocalNewformFunction.lean` | 28–37; 239–264; 270–279 | `symplO`, `heisO`; `IsSBHalf`, `IsPlaceModel`, `IsThetaAt`; the actual `localNewformFunction` |

Fix one nonterminal edge \(0\leq i\leq m-2\), ranks

\[
 a=N(i),\qquad b=N(i+1),\qquad n=ab,
 \tag{DO29.1}
\]

and one allowed source and target decoration, local index, and frame.
Write \(\Xi\) for the resulting scalar `TwDat.xi`, before or after a
specified nonzero chart scalar. The scalar is retained in every formula.
Let \(\mathcal S=\mathrm{Sall}\) be its actual finite half-place set.
The source's selected-place and prime hypotheses are retained; in
particular this is a set of relative split places with no conjugate
pair selected twice.

At a \(T\)-place \(P\), the factor is supported on

\[
 \operatorname{Hom}_{\mathcal O_{E,P}}(N_P,N'_P)
 \tag{DO29.2}
\]

and is constant modulo \(P\operatorname{Hom}(N_P,N'_P)\). In residue
frames it is exactly

\[
 I_{v,u}(X)=1_{\{vX=u\}},\qquad u\ne0,\quad v\ne0.
 \tag{DO29.3}
\]

This includes matrix integrality. The assertion follows directly from
the localized lattice condition in `phiT` and the residue-linearity in
`Deco.Ok`; the exact incidence description and its rank-one Fourier
span are carried THETA3-A13.

At a place \(P\in\mathrm{rowSG}\), let \(f_P,f'_P\) be the specified
source and target frames and put

\[
 L_P^{\rm fr}=f'_P M_{b\times a}(\mathcal O_{E,P})f_P^{-1}.
 \tag{DO29.4}
\]

For an `XiEntry` branch, the literal `xiSupp` and `xiInv` fields give
support in \(q_P^{-A}L_P^{\rm fr}\) and period lattice
\(q_P^B L_P^{\rm fr}\). For an `XiCpl1` branch, the literal
`psiSuppX` and `psiInvX` fields give the same bounds in the matrix
variable, with the actual fixed representative of the extra column
retained. Here \(q_P=\mathrm{qOf}(P)\), and the exponents mean scalar
multiplication exactly as in the source. No assumption that an
arbitrary function `LocCst.psi` is continuous outside its prescribed
depth is needed. These are already hypotheses of the actual
`ChIdx.Ok` record.

The first edge of every allowed chain is one of these branches, since
the source has \(m\geq2\). The present assertion does **not** silently
extend these nonterminal fields to `xiLast`. That branch has the
additional variable additive character in `ftY`; its stated depth and
terminal representative conditions must be used separately.

## 2. The explicit extension and finite transform

Use the actual mixed finite symplectic space from AM-DO-022:

\[
 E'=\mathbf Q(\zeta_{28}),\quad
 X=eW_f,\quad Y=\bar eW_f,\quad
 L=e\widehat\Lambda,
 \tag{DO29.5}
\]

where \(\Lambda=M_{b\times a}(\mathcal O_{E'})\), and \(e\) is the
selected finite half idempotent for \(\mathcal S\). The mixed scalar
trace coefficient is \(\xi'=\xi/2\); the product lattice and the
dyadic basis index remain exactly those of AM-DO-022. Write \(B\) for
the effective alternating pairing with the actual fixed additive
character \(\psi_f\). Thus \(W_xW_y=\psi_f(B(x,y)/2)W_{x+y}\).
This notation incorporates the source's standard-character sign,
rather than changing it in a Fourier formula.

Let \(L^+\supseteq L\supseteq L^-\) be compact open lattices in \(X\)
such that the local bounds of §1 imply

\[
 \operatorname{supp}\Phi\subseteq L^+,
 \qquad \Phi(t+v)=\Phi(t)\quad(v\in L^-).
 \tag{DO29.6}
\]

They can be chosen without an unspecified enlargement. At each
\(T\)-place take the sum of the standard lattice and (DO29.2) for
\(L_P^+\), and intersect the standard lattice with \(P\) times
(DO29.2) for \(L_P^-\). At each other selected place take

\[
 L_P^+=L_P+q_P^{-A}L_P^{\rm fr},\qquad
 L_P^-=L_P\cap q_P^B L_P^{\rm fr}.
 \tag{DO29.7}
\]

Products give \(L^+,L^-\). Smith normal forms of the displayed local
frame matrices give their exact elementary divisors and indices.
Thus no frame index is suppressed. Define

\[
 R=[L^+:L],\qquad N=[L:L^-],\qquad
 C=L^+/L,\quad U=L/L^-.
 \tag{DO29.8}
\]

Choose representatives \(a\in L^+\) of \(C\), and representatives

\[
 y\in (L^-)^\perp/L^\perp\subset Y/L^\perp
 \tag{DO29.9}
\]

of the characters of \(U\), where annihilators use
\(\psi_f\circ B\). This is a perfect finite pairing; in local
coordinates it is the ordinary duality between a lattice quotient
and its inverse-different dual. Its order is \(N\).

There is a unique locally constant function \(\Phi\) on \(X\),
extended by zero off \(X\), satisfying

\[
 \Phi(e\gamma)=\Xi(\gamma)\quad
     (\gamma\in M_{b\times a}(E')).
 \tag{DO29.10}
\]

**Proof of existence and uniqueness.** At the finitely many selected
places, use the factors of §1. The support and period statements make
their product constant on every coset of \(L^-\) and zero off \(L^+\).
Every required finite congruence class has a rational matrix
representative by additive weak approximation, or equivalently the
Chinese remainder theorem after clearing denominators. Its value is
independent of the representative by the period statements. This
defines the function and proves (DO29.10). Conversely rational
matrices meet every open coset of \(L^-\), so no other locally
constant extension with these periods is possible. Choose a positive
integer \(k\) with \(kL\subseteq L^-\) and \(kL^+\subseteq L\);
the local elementary divisors give one explicitly. Then (DO29.6)
is exactly the support and period part of `IsSBHalf`, and support on
\(X=eW_f\) is its remaining clause. \(\square\)

The exact Fourier coefficients are

\[
 c_{a,y}=\frac1N\sum_{u\in U}
                 \Phi(a+u)\psi_f(-B(u,y)).
 \tag{DO29.11}
\]

Finite character orthogonality gives the literal identity

\[
 \Phi(t)=\sum_{a\in C,y\in\widehat U}
 c_{a,y}\,\psi_f(B(t-a,y))1_L(t-a).
 \tag{DO29.12}
\]

Let \(T\) be any normalized `IsPlaceModel`, so that

\[
 T1_L=f_0,\quad T\Phi(\cdot+x)=W_xT\Phi,
 \quad T(\psi_f(B(\cdot,y))\Phi)=W_yT\Phi.
 \tag{DO29.13}
\]

Then the required finite vector is **exactly**

\[
 \boxed{f_\Xi=\sum_{a,y}c_{a,y}W_{-a}W_yf_0
   =\sum_{a,y}c_{a,y}\psi_f(-B(a,y)/2)W_{y-a}f_0.}
 \tag{DO29.14}
\]

Indeed apply modulation and then translation to \(1_L\) in
(DO29.12), and use the displayed Weyl law. Every normalized model
gives the same vector. This is precisely the carried A12 construction
and the literal theorem `thetaAt_eq_sum_heis_translates`, now with
the coefficients of the **actual** array rather than freely chosen
ones. The theorem `exists_isThetaAt_of_vac`, lines124–132 of
`Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsIsThetaAtOfVac.lean`,
supplies existence in the original source wrapper; the actual mixed
Schrödinger model supplies existence on the mixed host. Section5
states their precise finite comparison.

Equations (DO29.6), (DO29.10), and (DO29.14) verify all three
mathematical clauses of `IsRatDatum`. They also specify the exact
finite list and coefficients for `IsFinComb`; every parameter has
zero infinite component. They do not assert that an unchanged
elliptic `D7` wrapper has been instantiated for the new CM type.

## 3. Exact norm, denominators, and local newform examples

Normalize the finite Haar measure by \(\operatorname{vol}(L)=1\)
and the finite vacuum by \(\|f_0\|=1\). Then

\[
 \boxed{\|f_\Xi\|^2
   =\sum_{a,y}|c_{a,y}|^2
   =\frac1N\sum_{a\in C,u\in U}|\Phi(a+u)|^2.}
 \tag{DO29.15}
\]

**Proof.** The functions
\(\psi_f(B(t-a,y))1_L(t-a)\) have disjoint supports for different
\(a\), and character orthogonality on \(L/L^-\) gives orthogonality
for different \(y\) with the same \(a\). Each has norm1. The same
orthogonality holds for their images \(W_{-a}W_yf_0\): lattice
modulations distinguish different position cosets, lattice
translations distinguish different characters, and these operators
are unitary. The vacuum norm fixes the norm of every image at1.
Consequently (DO29.14) is an orthonormal expansion. Finite Parseval
gives the second equality. This proves the normalization even though
the bare predicate `IsPlaceModel` does not separately include an
isometry axiom. \(\square\)

If \(H_\Xi=\max_{a,u}|\Phi(a+u)|\), then

\[
 \|f_\Xi\|\leq\sqrt R\,H_\Xi,
 \qquad \sum_{a,y}|c_{a,y}|
       \leq\sqrt{RN}\,\|f_\Xi\|
       \leq R\sqrt N\,H_\Xi.
 \tag{DO29.16}
\]

These follow respectively from the \(RN\) summands in (DO29.15)
and Cauchy–Schwarz. They are bounds, whereas (DO29.15) is exact.

Let \(K_\Xi\) contain all actual table values and all character
values in (DO29.11)–(DO29.14). The latter are roots of unity. If
\(\delta\Phi(a+u)\) is integral over \(\mathcal O_{K_\Xi}\), then

\[
 \delta N c_{a,y}\in\mathcal O_{K_\Xi}.
 \tag{DO29.17}
\]

Equivalently, at a finite valuation \(v\),

\[
 v(c_{a,y})\geq
       \min_{a,u}v(\Phi(a+u))-v(N).
 \tag{DO29.18}
\]

The central phase in (DO29.14) is a unit and adds no valuation.
The values of the actual array still contain its `volN` factors,
finite sums, specified characters and chart scalar; their valuation
is **not** replaced by0. If the finite level and lattice changes
are prime to11, the actual theta-group isomorphisms also preserve
the integral11-adic theta lattice. Thus (DO29.17) is then a bound
for the geometric coefficient realization after the common period
has been removed. This assertion makes no claim at an auxiliary
place of residue characteristic11.

For standard frames, at a degree-one selected \(T\)-prime the local
indices are \(R_T=1,N_T=q^n\). At a selected degree-one row prime
they are \(R_P=q^{An},N_P=q^{Bn}\). Thus, when all these frames are
integral units, one may use

\[
 R=\prod_{P\in\mathrm{rowSG}}q_P^{An},\qquad
 N=T(u)^{[F':\mathbf Q]n}
           \prod_{P\in\mathrm{rowSG}}q_P^{Bn}.
 \tag{DO29.19}
\]

Repeated rational primes in the product are intentional: each
selected half place contributes its matrix quotient. For other
frames or residue degrees, (DO29.7)–(DO29.8), rather than this
simplified formula, give the exact indices.

### 3.1 The actual incidence factor

At a \(T\)-place with residue field \(\kappa\) of order \(q\),
choose the residue additive character induced by the actual
pairing. For nonzero \(u,v\) as in (DO29.3),

\[
 1_{M_{b\times a}(\mathcal O)}(t)I_{v,u}(\bar t)
   =q^{-a}\sum_{\eta\in\kappa^a}
       \psi_\kappa(-\eta\cdot u)
       \psi_\kappa(\eta\cdot v\bar t)1_L(t).
 \tag{DO29.20}
\]

This follows by summing a character of the \(a\)-dimensional
additive group \(\kappa^a\): the sum is \(q^a\) when
\(v\bar t=u\), and0 otherwise. Let \(y_{v,\eta}\in P^{-1}L^\perp/L^\perp\)
be the exact dual vector for the character
\(t\mapsto\psi_\kappa(\eta\cdot v\bar t)\), including the
coefficient of the actual trace pairing. Therefore

\[
 f_{v,u}=q^{-a}\sum_{\eta\in\kappa^a}
                 \psi_\kappa(-\eta\cdot u)W_{y_{v,\eta}}f_0,
 \quad \|f_{v,u}\|^2=q^{-a},
 \quad \sum|c_\eta|=1.
 \tag{DO29.21}
\]

The map \(\eta\mapsto y_{v,\eta}\) is injective because \(v\ne0\).
Thus the norm also follows directly from \(q^a\) orthogonal terms
of coefficient absolute value \(q^{-a}\). Its denominator is exactly
\(q^a\) in this expansion. The frequencies are the matrices
\(v^t\eta\), of rank at most1; this is the source incidence
restriction, not a full matrix-delta projector.

### 3.2 The literal `localNewformFunction`

Let the local field have residue order \(q\), uniformizer \(\varpi\),
and let \(P\subset\mathrm{GL}_r(\mathcal O)\) be a compact open
subgroup. Assume the specified finite characters are continuous and
unitary, as in the actual compact type. The source function is

\[
 F\binom{A}{B}=
 \begin{cases}
 \lambda(A)\mu(\det A)^{-1},
       &A\in P,\ B\in\varpi M_{t\times r}(\mathcal O),\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{DO29.22}
\]

This is the literal definition at the locator in §1; it includes
both its unit block and its lower-block divisibility. Choose
\(s\geq1\) such that \(K_r(\varpi^s)\subset P\) and the product
character \(\lambda\mu^{-1}\circ\det\) is trivial there. Then
(DO29.11) with \(R=1,N=q^{s(r+t)r}\) is an explicit finite
Heisenberg expression for this function. More sharply its norm is

\[
 \boxed{\|F\|^2
  =q^{-tr}\,
     \frac{\prod_{j=1}^{r}(1-q^{-j})}
          {[\mathrm{GL}_r(\mathcal O):P]}.}
 \tag{DO29.23}
\]

To prove the period assertion, changing \(A\) by
\(\varpi^sZ\) multiplies it on the right by an element of
\(K_r(\varpi^s)\) whenever \(A\in\mathrm{GL}_r(\mathcal O)\).
It therefore preserves both support and value; changes in \(B\)
by \(\varpi^s\) preserve its divisibility. For the norm, its
absolute value on its support is1. Additive matrix measure gives
\(M_r(\mathcal O)\) volume1 and
\(\mathrm{GL}_r(\mathcal O)\) volume
\(\prod_j(1-q^{-j})\). Multiplication by any integral unit matrix
preserves this additive measure, so \(P\) has exactly the displayed
index fraction of this volume. The lower block has volume
\(q^{-tr}\). Multiplication gives (DO29.23). This proves every
factor and does not identify a group probability measure with
additive matrix measure.

The actual `PhiG`, `PhiGS`, `PhiQ`, `E1at` and their specified
frame operations are retained inside the table (DO29.11). In
particular a finite auxiliary sum is not replaced by just the
local function (DO29.22). Equation (DO29.15) computes its exact
norm after that sum, including cancellation.

## 4. A nonzero actual Xi cannot be a 29-only input

Let \(\mathcal V_{29}\) be the span of all finite Heisenberg
translates of the actual vacuum whose parameters are supported
at places over29. This includes the actual permitted half-orbit
used in AM-K022 and AM-R-012, and is deliberately larger than
that half-orbit. At all other places every vector in
\(\mathcal V_{29}\) has its fixed vacuum factor.

For an actual valid prime and decoration datum, suppose
\(\Xi\not\equiv0\) is a nonterminal `xiAt`. Then

\[
 \boxed{f_\Xi\notin\mathcal V_{29}.}
 \tag{DO29.24}
\]

Here equality is tested in one common finite model, enlarging the
selected half set by the29 half places if necessary. The assertion
is unchanged by a nonzero scalar multiplying \(\Xi\).

**Proof.** The prime axioms give three distinct rational primes
\(T(u),g_0,g_1\). This is literal `Primes.Ok.g_ne` and
`T_ne_g`, lines200–239 of
`Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean`.
There is at least one selected place above each: their stated
cardinality is \([F':\mathbf Q]>0\).

If \(T(u)\ne29\), choose a \(T\)-place \(P\nmid29\).
Its factor (DO29.3) vanishes at0 because \(u\ne0\), and on an
open neighborhood of0 by its period lattice. If \(T(u)=29\),
choose a \(G\)-place \(P\nmid29\). Carried THETA3-A13 proves
locally that nonvanishing of this factor forces the underlying
matrix \(x:E'^a\to E'^b\) to be injective. In its `XiEntry`
proof, each enlarged summand has rank at most
\(\operatorname{rank}x+c_i\) but requires a unit minor of size
\(a+c_i\); in the penultimate branch `joinCol` gives the same
inequality with \(c_i=1\). Thus its local value at \(x=0\) is0,
and the actual `xiInv` or `psiInvX` gives an open neighborhood
on which it remains0. In all cases there is a mandatory factor
at some \(P\nmid29\) that vanishes near0.

In a common half model, a vector in \(\mathcal V_{29}\) has
function

\[
 G(t)=G_{29}(t_{29})
              \prod_{Q\in\mathcal S,\ Q\nmid29}1_{L_Q}(t_Q).
 \tag{DO29.25}
\]

This follows by applying only29-local operators to the tensor
vacuum. The29 operators need not be pure position translations;
their action is all contained in \(G_{29}\). If this function
equalled the nonzero \(\Phi\) of (DO29.10), choose a point where
the common value is nonzero. All its coordinates away from29
are in their \(L_Q\). Replace just its \(P\)-coordinate by0.
Formula (DO29.25) leaves its nonzero value unchanged, whereas
the mandatory source factor makes \(\Phi\) zero there. This
is a contradiction. The same argument can be made entirely
on rational samples: use a sufficiently small open coset at
each selected place and additive weak approximation. The
finite-model map is injective on the window by (DO29.15), so
different functions cannot represent the same vector. \(\square\)

This obstruction is to the **29-only span**, not to the oscillator
representation, not to arbitrary finite inputs, and not to a
changed valid global tuple. Equation (DO29.14) gives the required
nonzero vector with the other local factors included.

## 5. What the mixed finite comparison proves

At every selected good relative split place away from2 and7,
both the source trace coefficient and the mixed coefficient
\(\xi'\) are local units. Express the two effective symplectic
forms using the same fixed additive character. On \(X_P\oplus Y_P\)
their pairing coefficients differ by a unit \(r_P\) of the real
local field. The linear map

\[
 C_P(x+y)=x+r_Py,
 \qquad B_{\rm mixed}(C_Pz,C_Pw)=B_{\rm source}(z,w)
 \tag{DO29.26}
\]

is the explicit symplectic transport; \(r_P\) is by definition
the ratio of the source coefficient to the mixed coefficient.
It fixes the position variable and preserves both integral
half lattices. It therefore fixes \(1_{L_P}\), transports every
character in (DO29.11) to its actual dual vector, and preserves
the finite measure normalization. It also commutes with
\(X\mapsto hXg^{-1}\), since it is scalar on the dual half.
The split-place determinant-root normalization from AM-DO-020
is retained. There is no extra unidentified phase in this
normalized finite Heisenberg map.

Consequently the **same** raw table \(\Xi(\gamma)\) determines
the mixed vector (DO29.14), with its exact finite norm and
denominators. On the actual mixed theta family, AM-DO-026 gives
its all-polynomial reading:

\[
 \vartheta_{r_P f_\Xi}(g,h)
 =C^{2ab}\epsilon_\chi(g,h)
   \left[P(\partial)\sum_{a,y}
     c_{a,y}\psi_f(-B(a,y)/2)
       \mathcal U_{A_{g,h}(y-a)}F_{N,N'}\right]_{0}.
 \tag{DO29.27}
\]

Every finite phase, chart scalar, and common period \(C^{2ab}\)
is displayed or defined in the checked transported operator.
This comparison constructs the finite part of a **new mixed
datum**. It does not identify the old elliptic `VacIn` seed with
the primitive mixed-CM seed, and does not assert a new `D7`
instance without changing that wrapper. If a chosen auxiliary
place is bad for (DO29.26), its actual lattice indices and
dual pairing must be used instead; the abstract finite formula
still holds but the unit-lattice simplification is unavailable.

## 6. Consequences for the selected first edge and MainX

The identity \(\Xi(0)=0\), already settled in THETA3-A13, does
**not** assert \(\vartheta_{r_Pf_\Xi}(1,1)=0\). The first is
one value of a finite position function. The second is the
weighted theta/jet sum (DO29.27). They are different linear
functionals. In particular a nonintegral position translate
from R012 itself can have finite value0 at the origin and a
nonzero selected theta jet.

R012 proves nonvanishing of its selected jet on some member
of the actual29 half-orbit. Equation (DO29.24) prevents using
that statement to identify its finite vector directly with
the nonzero prescribed \(f_\Xi\). Conversely (DO29.14)
removes any merely existential finite-vector obstacle: the
prescribed raw array is now an explicit admissible finite
Heisenberg combination on the mixed host.

The remaining first-edge question is the concrete finite
functional

\[
 \sum_{a,y}c_{a,y}\psi_f(-B(a,y)/2)
       [P(\partial)\mathcal U_{y-a}F_{00}]_0
             \stackrel{?}{\ne}0,
 \tag{DO29.28}
\]

or its actual matrix version over all allowed indices and
decorations. A general nonzero theta vector or a nonzero term
of this sum does not prove (DO29.28). The exact criterion in
carried A15 remains applicable with the selected higher jet
substituted for its first derivative. Its actual local
incidence and rank restrictions remain inside the coefficients.

The next result treats a fixed nonzero auxiliary operator at
primes disjoint from29 and11, acting on the **actual** K022
half-orbit. It will prove a quantitative selected-jet detector
using simultaneous torsion-point interpolation. Even that
result does not silently make a translated29 vacuum into the
fixed `Q`-factor at29 of an already prescribed \(\Xi\); that
is a separate image or admissible-parameter equation.

### Check status

Author whole-proof review and independent review are recorded in
`definite_oscillator_CHECK_EVENTS.tsv` when actually performed.
All new equations are finite-model or elementary lattice/measure
arguments proved above. No Lean build or full MainX constructor
is claimed.
