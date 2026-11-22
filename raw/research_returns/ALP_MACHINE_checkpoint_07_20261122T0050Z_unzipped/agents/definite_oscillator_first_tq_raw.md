# AM-DO-035: all first coupled raw factors, their compact filters, and the remaining 29-place gate

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`.
22 November 2026 UTC. Inherited reasoning effort is not separately exposed.

This completes the local G/T/Q compatibility calculation for the first
coupled kernel when `m=2`. It uses the actual `ybSet` class, the actual
common splitting character, and an initial source input satisfying the
prescribed G, T and Q conditions. In particular, the Q determinant
character cancels; it is not an obstruction to `zero_Q`. A nontrivial
T diamond character gives the initial ramification condition and an
explicit nonzero compact filter.

Combined with ALP-LIFT-20 and AM-DO-030/034, this gives a nonzero first
lift with **all raw G/T/Q factors retained**, after one allowed auxiliary
29-place Heisenberg translate and a source level refinement there. It
does not identify that translated kernel or refined input with the
literal unmodified `XiCpl1`/`MfV`. Section 8 states the remaining equation
and proves the precise limitation of absorbing it by lattice moves.

The local identities hold for every source-admissible T prime and
twisting tuple. The global corollary assumes fixed such data, with
all its auxiliary primes away11 and29. This file does not certify
an explicit T prime or instantiate the complete `Primes.Ok` record.

## 1. Source locations and conventions

All source paths below are in the recovered original commit
`7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`. Abbreviate
`Formalism/LocalToGlobal/Columns/FiniteSumNonzeroLargeDepth.lean`
by FS. These are source readings, not a Lean execution.

| Source locator | Clause used |
|---|---|
| FS594–598, 600–608, 636–641 | `homAt`, the two scaled modules, and the actual `kerOf` sum |
| FS646–655 | `phiT` and the chosen lattice/residue frames `liftFr` |
| FS684–694, 714–719 | `entB` and the raw Q factor `PhiQ` |
| FS780–810, 981–986 | raw G/GS factors, `joinCol`, and `PsiAt` |
| FS999–1010 | actual uniformizer and residue tying of the common character |
| FS1019–1023 | initial index, `hal=1`, prescribed G type and full trivial Q level |
| FS1038–1061 | depths, support and representative-period conditions |
| FS1103–1138 | actual frames, `Sall`, `cAof`, `cBof`, `ybSet`, `repY`, and `XiCpl1` |
| FS1246–1259 | inverse source and direct target determinant characters |
| `Columns/Adelic.lean`139–145 | mirabolic source level at T |
| `Columns/RecLevel.lean`50–52 | the adelic source character is the inverse column character |
| `Columns/ScaledRamifiedLattice.lean`81–94, 160–169 | diamond operators, their sum `NmG`, and `MramV` |
| `Development/AbelianVarietyTheory/Definitions/LatticeFrames/LevChiEqOne.lean`61, 100, 114–117 | actual common label `mu0_j * xi(a)`, raw datum and scalar tie |
| `Columns/AbelianHostFieldConditions.lean`314–334 | reference characters unramified away G, and their actual tying |
| `Formalism/LocalToGlobal/Divisibility/Tuples.lean`, `GoodPl`, `tupGrp`, `Qprime`, `resChar` | twist ramification, tame residue characters and degree-one Q places |

Put

\[
 m=2,\qquad a=k,\qquad b=k+t+1,\qquad m_2=0,
 \qquad r=a+1,\quad r_S=0,\quad c_0=1,\quad c_1=0.
 \tag{DO35.1}
\]

Take the base decorated lattices at the first two ranks. Their underlying
lattices are the standard integral lattices. Their T functionals are
nonzero residue covectors; the base choice is the last-coordinate
functional. Their Q frames are the identity. At G the selected
`liftFr` need not literally be the identity, but preserves the integral
lattice and induces the prescribed identity residue frame. Therefore
all residue formulas below remain valid in those exact frames.

At a relative split degree-one place write `O` for the local ring,
`q` for its rational uniformizer and residue cardinality, and
`kappa=F_q`. Additive matrix Haar gives `M_(b,a)(O)` volume one.
The genuine source action, with the actual common splitting character
having local component `eta`, is

\[
 [\omega(g)f](X)
   =\eta(\det g)^{-1}|\det g|^{b/2}f(Xg).
 \tag{DO35.2}
\]

This is the split formula checked in AM-DO-020/024 and ALP-LIFT-20.
On a compact subgroup the absolute-value factor is one. The formula
uses a genuine left representation; replacing `Xg` by `Xg^(-1)` without
changing the other conventions would reverse the calculation below.

Let `xi` denote the finite-order twisting tuple and `mu_0` the first
reference character. The actual character in (DO35.2) is

\[
                          \eta=\mu_0\xi.
 \tag{DO35.3}
\]

This is exactly `TwDat.Is.chr` and `PinX.mv` in the cited source.
At G the tuple is unramified and the reference character is prescribed.
At T both factors are unramified. At Q the reference factor is
unramified, whereas `xi` has its nontrivial tame residue character.
The Q set belongs to the tuple, not to the reference character.

## 2. One admissible global target class for all G and Q places

Write `m_c=cst.M` to distinguish this fixed positive integer from the
auxiliary isogeny degree `M=29^e`. At every selected G place prescribe

\[
             y_P\equiv q^{-1}e_a\pmod{O^b};
 \tag{DO35.4}
\]

at every Q place prescribe

\[
             y_P\equiv e_a\pmod{q^{m_c}O^b}.
 \tag{DO35.5}
\]

Here `e_a` is zero-indexed: it is the first coordinate immediately
following the first `a` target coordinates. These prescriptions are
made in the target frames in FS1103–1106. They are compatible with
the base frames described above.

**Claim.** A single rational target vector `y` defines an actual class
`Y` in `ybSet` satisfying every prescription (DO35.4)–(DO35.5).

**Proof.** The selected G and Q prime ideals are pairwise distinct;
the Q set is disjoint from G and T by the tuple's good-place condition.
Multiply by `D_aux=g_0 g_1`. At each G prime the required congruence on
`D_aux y` is integral modulo that prime; at each Q prime it is an
integral congruence modulo its `m_c`-th power, since `D_aux` is a unit
there. The Chinese remainder theorem in `O_K`, coordinate by
coordinate, gives an integral vector satisfying all these
congruences. Divide it by `D_aux`. This gives a rational vector with
the stated local conditions. In the actual selected G frames the
same proof uses their integral coordinate maps; their reductions
are the specified residue frames. In particular the congruence
`q y=e_a mod q` is unchanged by a frame congruent to the identity.

The vector is in the module defining `ybSet`: its G valuation is
at least `-1`, and its Q valuation is at least zero, hence at least
`-m_c`. Set

\[
 Y=y+\operatorname{locLat}
       \bigl(N_1;\ e_G=0,\ e_Q=m_c\bigr).
 \tag{DO35.6}
\]

This is the literal set in FS1128–1130. Every representative of
`Y`, including `repY Y`, has the same prescribed residues. At G
ALP-LIFT-20 proves the exact representative invariance; at Q it
follows from the determinant and divisibility conditions below
(or from the actual `psiInv` clause). No independent local `y`
is being substituted for the one global class. ∎

T imposes no condition on `y`: its factor is `phiT(X)`. Its distinct
prime support makes its incidence conditions compatible with this
same G/Q class. For example, one may choose a rational `X` with
`X=X_0 mod G`, the Q block residues in Section 3, and the T last
row condition in Section 4, again by the Chinese remainder theorem.
Thus the combined finite raw function is nonzero before any theta
or compact averaging assertion is made.

## 3. The exact Q factor and cancellation of its compact character

Let

\[
 X=\begin{pmatrix}A\\ r\\ B\end{pmatrix},
 \quad A\in M_a(K_P),\ r\in M_{1,a}(K_P),\
 B\in M_{t,a}(K_P),
 \qquad \chi=\operatorname{resChar}(\xi,P).
 \tag{DO35.7}
\]

At Q the exponents in `entB` are all zero. Both group arguments in
`PsiAt` are one, by `zero_h` and its definition. For the class
(DO35.5), the top `(a+1)` square block of `[X,y]` has last column
`e_a` modulo `q`, and the lower `t` rows of that column vanish
modulo `q`. Consequently the actual source definition gives

\[
 f_Q(X)=
 \chi(\det\bar A)\,
 1_{\{A\in\operatorname{GL}_a(O),\ r\in O^a,
                   \ B\in qM_{t,a}(O)\}}.
 \tag{DO35.8}
\]

The determinant character is extended by zero on nonunits, exactly
as `unitV` in FS. This proves (DO35.8) also when the top block is
singular. A change `y -> y+q^(m_c)z`, with integral `z` and
`m_c>=1`, changes neither reduction nor lower-row divisibility.

For every `g in GL_a(O)` the support is preserved and

\[
                     f_Q(Xg)=\chi(\det\bar g)f_Q(X).
 \tag{DO35.9}
\]

But the actual label (DO35.3) has exactly the residue character
`chi` at Q. Substituting (DO35.9) into (DO35.2) proves

\[
                  \boxed{\omega(g)f_Q=f_Q\quad(g\in\operatorname{GL}_a(O)).}
 \tag{DO35.10}
\]

Thus the raw Q factor is fixed by the full source compact. This
is precisely the initial condition `zero_Q=LevQFam.top`, whose
definition is `H=top, lam=1` (FS409). Using only the reference
label `mu_0` in (DO35.2) would incorrectly leave an extra character.
The inverse source residue character `rhoS=chi^(-1)` in
FS1246–1248 confirms the same cancellation independently.

Its exact additive norm is

\[
 \|f_Q\|^2
  =q^{-ta}\prod_{i=1}^{a}(1-q^{-i})=:\Gamma_Q.
 \tag{DO35.11}
\]

Indeed `A` has invertible reduction with the displayed probability,
`r` is arbitrary integral, and `B` has `ta` entries divisible by `q`.
Every nonzero value has modulus one. The value at `[I_a;0;0]` is one.

The function is supported on integral matrices and periodic modulo
`q`. Its finite Fourier expansion in the Heisenberg vacuum basis
is therefore an actual finite combination at P. All denominators
divide a power of `q`; at a coefficient place over11 with `q!=11`,
at least one Fourier coefficient is a unit. This last assertion
does not require a Gauss-sum estimate: Fourier inversion over a
finite group of order prime to11 is an integral automorphism,
and (DO35.8) has the unit value one. The free row `r` forces the
corresponding dual row to vanish, so its Fourier support has size
at most `q^(a(b-1))`. Parseval gives exactly (DO35.11).

## 4. The T factor, source level and initial ramification condition

Let `u in kappa^a` and `v in kappa^b` be the nonzero source and
target residue covectors. In the base decorations they are the
last-coordinate covectors. The exact factor `phiT` is

\[
 f_{T,u}(X)
  =1_{M_{b,a}(O)}(X)\,1_{\{v\bar X=u\}}.
 \tag{DO35.12}
\]

Its norm is `q^(-a)` because these are `a` independent residue
conditions. Put

\[
 H_u=\{g\in\operatorname{GL}_a(\kappa):ug=u\},\qquad
 P_u=\{g:ug=s(g)u\text{ for some }s(g)\in\kappa^\times\}.
 \tag{DO35.13}
\]

The quotient `P_u/H_u` is `kappa^times`, and

\[
 d_T=[\operatorname{GL}_a(\kappa):P_u]
       =\frac{q^a-1}{q-1}.
 \tag{DO35.14}
\]

Choose any nontrivial unitary residue character `nu` of
`kappa^times`. The rational T prime is odd in the source, so such
a character exists. Work over a coefficient extension containing
its values. Define

\[
 f_{T,\nu}=\sum_{s\in\kappa^\times}\nu(s)^{-1}f_{T,su}.
 \tag{DO35.15}
\]

The supports are disjoint, so this is nonzero and

\[
                    \|f_{T,\nu}\|^2=(q-1)q^{-a}.
 \tag{DO35.16}
\]

At T the character (DO35.3) is unramified. Equation (DO35.2)
therefore gives, for a lift of `g in P_u`,

\[
 \omega(g)f_{T,u}=f_{T,s(g)^{-1}u}.
 \tag{DO35.17}
\]

With maximal-compact Haar of volume one, extend `nu(s(g))` by
zero from the inverse image of `P_u`. Equal-size fibres of
`s:P_u -> kappa^times` prove the exact compact filter

\[
 \boxed{\int_{K_T}1_{P_u}(g)\nu(s(g))\,
                  \omega(g)f_{T,u}\,dg
       =\frac{f_{T,\nu}}{d_T(q-1)}
       =\frac{f_{T,\nu}}{q^a-1}.}
 \tag{DO35.18}
\]

The scalar function in this integral has absolute value one on
`P_u`, zero outside, norm squared `1/d_T`, and is right `H_u`
invariant. This matches the literal T mirabolic level in
`Adelic.lean`139–145. Right multiplication by a lift with
`s(g)=c` multiplies it by `nu(c)`. Since `nu` is nontrivial,

\[
                    \sum_{c\in\kappa^\times}\nu(c)=0.
 \tag{DO35.19}
\]

Thus its T diamond sum vanishes. This is exactly the defining
local condition in `NmG` and `ColRamV`, not a cuspidality claim.
The source diamond operation multiplies the decorated covector
by `c` (`StdLatUnimodular.lean`113–116); changing the identification
of right translation with that operation replaces `nu` by its
inverse, and leaves (DO35.19) unchanged. Its scalar action on the
algebraic coefficient is the identity in `diamondOperatorOnForms'`.

For completeness, the finite Fourier coefficients can also be
computed exactly. Fix a nontrivial residue additive character
`psi`. The coefficient indexed by `ell in kappa^a` on the
rank-one matrix frequency `v^t ell` is

\[
 b_\ell=q^{-a}\sum_{s\ne0}\nu(s)^{-1}\psi(-s\,\ell u^t).
 \tag{DO35.20}
\]

It vanishes when `ell u^t=0`; otherwise it is a nonzero Gauss
sum divided by `q^a`, of complex modulus `q^(1/2-a)`. To see
nonvanishing and the norm without importing a formula, put
`G(c)=sum_(s!=0) nu(s)^(-1) psi(cs)`. For `c!=0`, substitution
`s -> c^(-1)s` shows all `|G(c)|` agree. Orthogonality of `psi`
gives `sum_c |G(c)|^2=q(q-1)` while `G(0)=0`, hence
`|G(c)|^2=q`. The product of the Gauss sum and its conjugate
is `q`, so these coefficients are units at every place over11
when `q!=11`. Their number is exactly

\[
                      s_T=(q-1)q^{a-1}.
 \tag{DO35.21}
\]

Parseval recovers (DO35.16). Their total complex absolute value
is `(q-1)/sqrt(q)`. No division by `q-1` has been made in the
auxiliary vector (DO35.15); the division belongs to the actual
compact filter (DO35.18) and must be charged there.

## 5. The complete auxiliary vector and exact fixed costs

At each G place use the Steinberg vector `f_St` of AM-DO-033,
with its determinant factor for the actual reference label.
ALP-LIFT-20 proves, for the actual raw factor `f_U`,

\[
 \int_{K_G}\overline{m_G(g)}\omega(g)f_U\,dg
          =\frac{\alpha_G}{d_G}f_{St},
 \quad d_G=q^{a(a-1)/2},\quad
 \alpha_G=\frac{d_G^2}{|\operatorname{GL}_a(\kappa)|}.
 \tag{DO35.22}
\]

Here `m_G` is the matrix coefficient of a unit generic vector in
the finite Steinberg representation. Its inverse-unipotent source
type is the literal initial `colLev_0` character. The raw factor
remains in the kernel on the left of (DO35.22).

Form the actual finite auxiliary vector

\[
 \phi_{\rm aux}
   =\bigotimes_{P\in G}f_{St,P}
       \otimes\bigotimes_{P\in T}f_{T,\nu_P}
       \otimes\bigotimes_{P\in Q}f_{Q,P}
       \otimes\bigotimes_{P\notin G\cup T\cup Q}\phi_{0,P}.
 \tag{DO35.23}
\]

Its finite norm squared is the exact product

\[
 \Gamma_{\rm aux}
  =\prod_{P\in G}\left(q_P^{-ab}\frac{|\operatorname{GL}_a(\kappa_P)|}{d_{G,P}}\right)
    \prod_{P\in T}(q_P-1)q_P^{-a}
    \prod_{P\in Q}\Gamma_{Q,P}.
 \tag{DO35.24}
\]

It is nonzero. Each factor is an actual finite Heisenberg
combination of the local vacuum; their product is one such
combination with pairwise distinct translated classes after
like terms are combined. The previous arguments and DO033
show that the coefficient array is primitive at11. A valid
bound for its number of terms is

\[
 s\le
  \prod_{P\in G}q_P^{ab}
  \prod_{P\in T}(q_P-1)q_P^{a-1}
  \prod_{P\in Q}q_P^{a(b-1)}.
 \tag{DO35.25}
\]

Every auxiliary rational prime here is assumed different from
11 and29. This is the exact hypothesis needed for the integral
prime-to-11 translated-line comparisons in DO030. The empty
Q set, supplied by the reference tuple, is explicitly allowed.

The raw finite vector with the unprojected G and T factors has
norm squared

\[
 \Gamma_{\rm raw}
  =\prod_{P\in G}q_P^{-ab}d_{G,P}
    \prod_{P\in T}q_P^{-a}
    \prod_{P\in Q}\Gamma_{Q,P}.
 \tag{DO35.26}
\]

Unlike the selected G vector, the raw G norm has no GL-order
denominator. If Q is empty, its finite norm has zero11 valuation.
For nonempty Q the explicit factor (DO35.11) retains its possible
11 valuation. One must not equate primitive coefficients with
unit Hilbert norm.

## 6. Global compact extraction on the actual degree-seven host

Use the genuine host and selected highest polynomial of AM-DO-034,
with the actual rank and stage characters supplied in AM-K031.
In particular `f=42`, `a=42`, `b=1802` is its `m=2,t=1759`
example. Keep the standard-lattice coefficient
`xi_K=xi_0 pi_B^(-6)` and its actual eigen-coordinate scalar.
Let `D` be the total selected degree and `B_nu` the factorial
valuation bound in DO034. Let

\[
 M=29^e\ge3s(D+1)-1.
 \tag{DO35.27}
\]

The simultaneous jet theorem DO030, in the proved host form
DO034, applied to the nonzero primitive vector (DO35.23), gives
one actual permitted half-orbit translate `W_(x_lambda)` with

\[
 \theta_{P_\nu\otimes W_{x_\lambda}\phi_{\rm aux}}(1,1)
      =\mathcal P\,a_\lambda\ne0,\qquad
 v_{11}(a_\lambda)\le B_\nu,
 \quad \mathcal P=C^{14ab}.
 \tag{DO35.28}
\]

All gauges, the ordinary product line and the fixed root-of-unity
translation phases are those already proved in DO030/034. The
factor `C` is the same analytic period, not a newly normalized
value of the raw T or Q function.

Define `K^e` to be the maximal source compact outside29 and the
rational principal congruence subgroup of level `29^e` at the
six F places above29. Its exact index in the maximal compact is

\[
 I_a^K(M)=M^{42a^2}\prod_{i=1}^{a}(1-29^{-i})^6.
 \tag{DO35.29}
\]

The ramification index is seven and there are six residue places;
these must not be replaced by forty-two unramified residue factors.
DO034 proves that the finite rational stabilizer of this compact
is trivial. The congruence fixes every relevant half-orbit vector;
the other auxiliary places are disjoint from29.

On the identity finite class define the actual automorphic source
function by

\[
 F(g_\infty,k)=
   \overline{m_\infty(g_\infty)}
   \prod_{P\in G}\overline{m_{G,P}(k_P)}
   \prod_{P\in T}1_{P_u}(k_P)\nu_P(s(k_P)),
 \quad k\in K^e,
 \tag{DO35.30}
\]

and set it to zero off that class. Here `m_infty` is the unit
highest source matrix coefficient used in DO034, and `d_rho` is
the dimension of that compact real representation. Triviality of
the rational stabilizer proves this definition is well defined
on the automorphic quotient, rather than only on a local chart.
It is smooth at finite places, compact-finite at infinity, and
square-integrable because the source unitary quotient is compact.

At G it has the initial inverse generic character; at T it has
the literal mirabolic invariance and zero diamond sum from
Section 4; at Q it is fixed by the full compact. These statements
are about this actual global function. They do not follow merely
from nonzero local factors. Its only extra source level is the
displayed refinement at29. With maximal finite compact volumes
one and compact real volume one, direct orthogonality gives

\[
 \|F\|^2
   =\frac1{I_a^K(M)d_\rho d_{G,\rm all}d_{T,\rm all}},
 \quad \|F\|_\infty=1,
 \tag{DO35.31}
\]

where `d_(G,all)=product_G d_G` and
`d_(T,all)=product_T d_T`. No class-number-one assertion is used.

Now keep the **raw** G, T and Q factors in the theta kernel, and
apply the same permitted29 translate to its vacuum there. The
compact integrations (DO35.10), (DO35.18), (DO35.22) commute,
and the real integration is the selected matrix-coefficient
projection of DO034. Thus the literal bilinear lift has value

\[
 \boxed{
 \Theta_{\rm raw,G/T/Q}^{\rm bil}(F)(1)
   =\frac{A_G\,\mathcal P\,a_\lambda}
      {I_a^K(M)d_\rho d_{G,\rm all}
          \prod_{P\in T}(q_P^a-1)}\ne0,
 \qquad A_G=\prod_{P\in G}\alpha_{G,P}.}
 \tag{DO35.32}
\]

This is an equality for actual global automorphic and Schwartz
inputs. It retains the raw local functions and the common
character (DO35.3). The local G denominator and the T averaging
denominator are not suppressed in a claim of nonzero pairing.

If the source and raw finite Schwartz vector are separately
normalized to norm one, divide (DO35.32) by

\[
 \sqrt{\Gamma_{\rm raw}}\,
 \bigl(I_a^K(M)d_\rho d_{G,\rm all}d_{T,\rm all}\bigr)^{-1/2}.
 \tag{DO35.33}
\]

If the real Schwartz factor is normalized as well, divide by its
exact norm in DO034, including `det(2Y)^(-7ab)`, the hook factors,
the eigen-coordinate metrics and `|c_nu|^2`. No new real norm
formula is being inferred from compact projection.

For fixed ranks and fixed G/T/Q data, (DO35.27) can be chosen
with `M<29(3s(D+1)-1)` (except the harmless `e>=1` endpoint).
Consequently the logarithm of (DO35.29) is `O(log(D+1))`.
All G/T/Q factors in (DO35.31)–(DO35.33) are fixed constants in
that assertion. This does not remove the separate linear-degree
coordinate denominator, Fock and factorial costs in DO034.
If the T prime or the Q tuple varies with D, the displayed
products, rather than this fixed-data simplification, apply.

## 7. What is and is not coupled to `cst.M`, `cAof` and `cBof`

The first raw function at `m2=0` contains no `E1at` sum. Its G
and Q local formulas are `PsiAt` with both group arguments one.
The integer `m_c=cst.M` only controls the admitted Q target class
and its period here. The choices (DO35.4)–(DO35.5) work for every
`m_c>=1`. The first-factor support is integral in X and periodic
modulo q, so the first-factor clauses are compatible with

\[
 A\ge m_c,\quad B\ge m_c,\quad B>0,\quad
 D_G=1,\quad D_Q\ge\max(2m_c,3).
 \tag{DO35.34}
\]

For example `m_c=A=B=1,D_Q=3` satisfies these displayed bounds.
This is not an assertion that all group, character and later-row
clauses of `ChIdx.Ok` have been instantiated.

The exact integers entering the finite `kerOf` expression are

\[
 c_A=\left(\prod_{P\in G\cup Q}q_P\right)^A,
 \qquad
 c_B=T(u)\left(\prod_{P\in G\cup Q}q_P\right)^B.
 \tag{DO35.35}
\]

Their exponents count the selected prime ideals; in particular a
rational fully split G prime occurs f times. These integers are
units at29 when all actual auxiliary places avoid29. Increasing
`cst.M`, A or B cannot insert a29 component into `Sall` or into
the actual half-position idempotent.

One must also avoid the converse false inference that every
rational representative x in `kerOf` is integral at29. `homAt`
in FS594 imposes conditions only at `Sall`, so representatives
may have denominators elsewhere. The finite quotient and the
congruence/additivity identities are defined using that same
localized module. Changing such a representative does not
enlarge the actual idempotent support or change `IsRatDatum`.
The obstruction in the next section is about that actual finite
input, not about the incidental denominator of a representative
chosen in the displayed finite sum.

## 8. The remaining literal datum and source-level equations

For the degree-seven host, every29 place is absolutely ramified
of index seven. A source Q place must be `GoodPl`, which includes
degree one and rational-uniformizer valuation one. Thus29 is not
an eligible Q place. The source G primes are the large degree-one
primes of K031, and the T conditions likewise require degree-one
selected places and their explicit congruences. Hence the actual
G/T/Q `Sall` used here avoids29.

The literal idempotent predicate is
`IsIdemSum(A.e,Sall)` (LevChiEqOne62), and AM-DO-030 proved from
`IsIdemAt` that it has zero29 component. The finite input fixed
by `IsRatDatum` is therefore the raw G/T/Q vector with the
standard vacuum at29. Equation (DO35.32) instead uses
`W_(x_lambda)` there, and its source function has the refined
level `K^e`. Neither difference is removed by Section 3's Q
character cancellation.

There is a precise limitation on repair by actual lattice moves.
At a relative split29 place, all source and target unitary
actions in the Hom model preserve the position polarization.
They act by an invertible linear change `X -> h^(-1)Xg`, with
a nonzero determinant-root scalar and positive Jacobian factor.
A moved vacuum is consequently a nonzero scalar times the
indicator of a linear lattice containing zero. The actual
`thMoved` family comes from those source and target lattice
moves; its root variables in `VacT` are determinant roots, not
affine translation parameters. A nontrivial permitted pure
position translate has indicator `1_L(X+x)` with `x notin L`;
its support does not contain zero. Thus

\[
 \boxed{W_x\phi_0\ne c\,\omega(g,h)\phi_0
 \quad\text{for }x\notin L,\ c\ne0,}
 \tag{DO35.36}
\]

for every individual source/target lattice or frame move at
that place. The statement includes nonintegral linear moves.
Changing the selected class, the row frame, or a determinant
root does not change this origin-support proof.

It does not exclude an equality of a single global theta
value, a finite linear combination of group translates,
nonvanishing after a compact projection, or a nonzero witness
already having `x_lambda=0`. These are different possible
routes, and none is disproved by (DO35.36).

The remaining first-row assertion at maximal29 level can be
written concretely. Let `P_(29,0)` be compact averaging on the
source29 factor, and let `L_(G/T/Q,Pnu)` be the actual theta
functional after the already computed G/T/Q and real filters.
One needs, for an actual permitted global initial input at that
level, a nonzero value of

\[
 L_{G/T/Q,P_\nu}\bigl(P_{29,0}\phi_{0,29}\bigr)
       =L_{G/T/Q,P_\nu}(\phi_{0,29}).
 \tag{DO35.37}
\]

The proved theorem supplies a nonzero value with
`W_(x_lambda) phi_(0,29)` and a smaller compact. A construction
which removes the source stabilizer by a generic T decoration
would allow a maximal29 class-supported input, but its integral
against that translated kernel contains
`P_(29,0) W_(x_lambda) phi_(0,29)`. Nonzero unaveraged value does
not imply nonzero averaged value. This is the exact projection
gate; it is not settled by the finite nonvanishing of (DO35.23).

Likewise moving the auxiliary isogeny to another split ray prime
does not alone solve (DO35.37): if that prime is outside `Sall`
the same issue recurs, while if it lies in Q its raw factor is
the prescribed (DO35.8), not a freely selectable translate.
The completed local identities provide the actual tests to use
in a future local or global nonvanishing argument.

Even after such an analytic assertion is proved, identifying the
source input with a specified integral `MfL`/`NlamC` row, or
proving the literal `PinCol`/`MainX` mass equations, requires those
actual lattice and scalar ties. The compact values and norms in
this finding do not instantiate the full arithmetic records.

## 9. Proof-check status

Author whole-proof review and the separate finite exact diagnostic
are recorded in `definite_oscillator_CHECK_EVENTS.tsv` after the
completed file has been read. No computational check is used as
a substitute for the proofs above. No Lean build is claimed.
