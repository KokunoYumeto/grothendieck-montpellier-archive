# ALP-LIFT-20: the actual raw first G factor and its exact Steinberg component

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/lift_accounting`.
Date: 21–22 November 2026 UTC. Inherited reasoning effort is not exposed.

This result concerns the actual source functions `PhiG`, `PhiGS`,
`PsiAt`, and `XiCpl1` when `m=2`. It identifies a particular allowed
first coupled G factor exactly, rather than replacing that factor
by a freely chosen Schwartz function. Its Steinberg component is
nonzero, with a fully computed scalar and norm. Compact integration
against the initial Steinberg input extracts this component while
leaving the prescribed raw factor in the kernel.

The local theorem is independent of the global CM field and holds
at every degree-one relative split G place satisfying the source
coordinate conventions. The global corollary uses a separately
established actual mixed theta family, a selected polynomial, and
a valid common stage character. It does not instantiate the whole
`ChIdx.Ok`, identify other raw T/Q factors, handle `PhiTop`, or
prove a later restricted-image statement.

## 1. Exact source specialization

All source locations below refer to the recovered pinned commit
`7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`. The principal file is
`Formalism/LocalToGlobal/Columns/FiniteSumNonzeroLargeDepth.lean`,
abbreviated FS. No Lean execution is claimed.

Take `m=2`, put `a=k`, `b=k+t+1`, and specialize the first coupled
kernel to `m2=0`. The actual rank definitions give

\[
 r=a+1,\quad r_S=0,\quad N_0=a,\quad N_1=b,
 \quad c_0=1,\quad c_1=0.
 \tag{RG1}
\]

Here `cOf R j = R.m-1-j` (FS815), and `rS=m/2-1` is in
`Formalism/LocalRingCardinality/Params.lean`. The formula is valid
for every admissible source rank; no small-rank numerical test is
being substituted for those rank constraints.

Fix a degree-one G place with uniformizer the rational prime
`q`, residue field `kappa=F_q`, and integral coordinate lattice.
Write `O` for the local valuation ring. Fix the exact additive
character `psi_0` in the source, and let

\[
 G_q=\operatorname{GL}_a(\kappa),\qquad
 U_q=\{u\in G_q:u\text{ is upper unitriangular}\},
 \qquad
 \psi_U(u)=\psi_0\!\left(\sum_{i=0}^{a-2}u_{i,i+1}\right).
 \tag{RG2}
\]

The character is the actual initial nondegenerate column
character. Its inverse is the adelic source-input character:
`Columns/RecLevel.lean`50–52 defines `levTyp=levChr^(-1)`.

In `PsiAt` the second frame is literally one (FS984–986).
The first frame is also one at this stage: `ChIdx.Ok.zero_h`
states `L.h 0 b P=1` for every initial index (FS1019–1023).
Thus this specialization does not impose a new choice of initial
frame beyond the source's own condition. In arbitrary global
lattice frames, the following calculation is made after applying
the exact `inFr` and target inverse frame in `XiCpl1`.

Choose the allowed target residue class

\[
                       y\equiv q^{-1}e_a\pmod{O^b}.
 \tag{RG3}
\]

The subscript is zero-based: `e_a` is the first coordinate
immediately after the first `a` target coordinates. This class
belongs to `q^(-1)O^b/O^b`, exactly the G component in `ybSet`
(FS1125–1133). The assertion is independent of the representative
chosen by `repY`.

Let `X` be a `b by a` matrix. The definition `joinCol X y`
is the `b by (a+1)` matrix `[X,y]` here (FS981–983). Both
index permutations `fIdx` in `entB` are the identity in (RG1).
The source last-column scaling exponent is one, all its other
exponents are zero, and every target exponent is zero. Hence

\[
             \operatorname{entB}(\operatorname{joinCol}(X,y))
                           =[X,qy].
 \tag{RG4}
\]

This follows directly from FS684–694; it is not a change of
Schwartz normalization. Since both group arguments of `omPhi`
are one, all determinant, valuation, and splitting factors in
`Loc.om` are one (FS553–561, 940–945).

### The raw-factor identity

Put `X_0=[I_a;0]` and define

\[
 f_U(X)=
 \begin{cases}
   \psi_U(u),&X\in M_{b,a}(O),\quad\bar X=X_0u,\ u\in U_q,\\
   0,&\text{otherwise}.
 \end{cases}
 \tag{RG5}
\]

Then, for either value of the source `sharp` flag,

\[
 \boxed{\ \operatorname{PsiAt}(0,P,1,X,y)=f_U(X)\ }
                  \qquad\text{whenever (RG3) holds.}
 \tag{RG6}
\]

Here is the complete predicate check. In both `PhiG` and
`PhiGS`, the internal variable called `a` is now `r=a+1`,
since the stage parameter is `j=1`. The first integrality
condition requires all entries in `[X,qy]` to be integral.
The condition on rows at least `a+1` makes their first `a+1`
entries zero modulo `q`. In the first `a+1` rows and columns,
the first `a+1` diagonal entries are one and the entries below
the diagonal are zero. The last column is already `e_a`
modulo `q` by (RG3). Consequently the first `a` columns have
upper unitriangular top `a by a` block and every subsequent
row is zero. This is precisely the support in (RG5).

For `PhiGS`, `symIdx a 0` is the identity
(`Columns/LevGSym.lean`11–13). Its extra zero condition in
column `a` is already imposed by `qy=e_a` modulo `q`.
Its other off-diagonal conditions are exactly the same lower
zeros just used. There are no determinant-block conditions,
since their column range starts at `r` and ends strictly
before `r`.

On the support, the leading `(a+1) by (a+1)` matrix is
`diag(u,1)` modulo `q`, so its determinant is one. The inverse
`chi_0` determinant factor therefore equals one, even though
the common splitting character itself can be ramified. In
`lamGvS`, the second additive sum has length `r-a-1=0`.
The first sum is exactly the exponent in (RG2). In
`lamGv`, the only additional simple-root entry is the entry
in row `a-1`, column `a`; it is zero by (RG3). Thus both
functions give `psi_U(u)`. Off the stated support one of
the displayed source predicates fails. This proves (RG6)
using the literal definitions FS780–810 and FS927–931.

Adding an integral vector to `y` changes `qy` by a multiple
of `q`, so the same proof also establishes representative
independence directly; no unproved `ChIdx.Ok.psiInv` is used
to obtain (RG6).

At finitely many G places the classes (RG3) can be imposed
simultaneously, including after the actual target frames.
Indeed the additive Chinese remainder theorem for the
localized fractional lattice gives an element of the global
target vector space with those finitely many prescribed
classes and with the required integral classes at the other
finite places in `rowSG`. Its class is an element of the
source `ybSet`; every representative of that class has the
same local factors. This is only an existence statement for
that allowed class. No archimedean height bound for a chosen
rational representative is asserted.

## 2. Finite Fourier coefficients and exact raw norm

Give `M_{b,a}(O)` additive volume one, as in the actual split
Schrödinger model. Each residue cell has volume `q^(-ab)`.
Set

\[
            n_U=a(a-1)/2,\qquad d_q=q^{n_U}=|U_q|.
 \tag{RG7}
\]

Every nonzero value of `f_U` is a root of unity, its value
at `X_0` is one, and

\[
                         \|f_U\|^2=q^{-ab}d_q.
 \tag{RG8}
\]

This is its exact Schwartz norm, not a normalized finite
group-counting norm. Its finite value lattice is primitive
at every prime at which the character values are units.
In particular it is primitive at11 when `q` is prime to11.

There is an especially simple actual Heisenberg expansion.
Let `V=M_{b,a}(kappa)` and let `W` be the linear subspace
of matrices whose only possible nonzero entries are in the
strictly upper triangular part of their top `a by a` block.
Then `dim W=n_U`, the support of `f_U` is the affine space
`X_0+W`, and its character there is
`ell(w)=sum_i w_(i,i+1)`. Use the perfect finite pairing
`B` and actual Fourier phase of DO29.11–13; identify `ell`
with the corresponding character of `W`. For the actual
finite vacuum `phi_0` one has

\[
 f_U=\sum_y b_y W_y\phi_0,\qquad
 b_y=
 \begin{cases}
 q^{n_U-ab}\psi_0(-B(X_0,y)),&B(w,y)=\ell(w)\ \forall w\in W,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{RG9}
\]

If the finite pairing is expressed as characters rather
than scalar-valued forms, the condition means equality of
the two characters on `W`; this is invariant under the
coordinate choice. To prove the formula, insert
`X=X_0+w` into the finite Fourier formula
`q^(-ab) sum_X f_U(X) psi_0(-B(X,y))`. The sum over `W`
is `q^(n_U)` when its character is trivial and zero
otherwise. Perfectness of the pairing gives exactly
`q^(ab-n_U)` nonzero coefficients. Therefore

\[
 \#\{y:b_y\ne0\}=q^{ab-n_U},\qquad
 \sum_y|b_y|=1,\qquad
 \sum_y|b_y|^2=q^{n_U-ab}.
 \tag{RG10}
\]

These are the actual phase-correct Heisenberg operators,
not just abstract coordinate translations. They are unitary,
so the operator in (RG9) has norm at most one. Its exact
value-lattice and Fourier-coefficient lattices should not be
confused: the latter have explicit `q`-power denominators
`q^(ab-n_U)`. These denominators are units at11 but must
be retained at the auxiliary prime and in any global
coefficient-height accounting.

## 3. Exact Steinberg projection in the actual split action

Let `eta` be the local selected-half common splitting
character. In the literal source character pin,
`bar eta=chi_0^(-1)`. The genuine left source action is

\[
 \omega(g)f(X)=\eta(\det g)^{-1}
                    |\det g|^{b/2}f(Xg).
 \tag{RG11}
\]

This is the corrected DO33.5/LIFT16(S2) convention. On the
integral compact it factors on the present functions through
`G_q` with its displayed determinant correction. In particular
`f_U` has right-source `psi_U` type under `U_q`; the determinant
factor is trivial there.

Use the actual finite Steinberg representation `St_q` and
the unit generic vector `u_0` constructed in DO33.2–4.
Its dimension is `d_q`; the `psi_U` eigenspace is one
dimensional. These facts are the published finite Steinberg
theorems (Steinberg, 1957, Theorems1–2; Geck, 2015,
Theorem2.1) and the already checked normalization DO033.
With the Hermitian form conjugate-linear in its first
argument put

\[
 m(g)=\langle u_0,\operatorname{St}_q(g)u_0\rangle,
 \qquad
 f_{\rm St}(X_0g)=\eta(\det g)m(g),
 \tag{RG12}
\]

and extend `f_St` to residue cells, zero off the full-rank
orbit `X_0G_q`. This is exactly DO33.6 with `v'=u_0`.
It has pure source `St_q` type, value one at `X_0`, and

\[
                 \|f_{\rm St}\|^2=
                          q^{-ab}|G_q|/d_q.
 \tag{RG13}
\]

Let `P_St` be the orthogonal projection onto the full
`St_q` isotypic subspace for the actual action (RG11),
including all its multiplicity copies in the residue
Schwartz space. Then

\[
 \boxed{\ P_{\rm St}f_U=\alpha_q f_{\rm St},\qquad
                  \alpha_q=\frac{d_q^2}{|G_q|}>0.\ }
 \tag{RG14}
\]

Here is a proof that controls the whole isotypic projection,
not only its nonzero inner product. On the free orbit
`X_0G_q`, tensoring functions by `eta(det g)` identifies
the actual right-source action with the ordinary right
regular representation. It leaves `f_U` unchanged, since
every point in its support has determinant one. The
Steinberg matrix coefficients span the full Steinberg
isotypic space in this regular representation. For any
`v,w in St_q`, their inner products with `f_U` are

\[
 \begin{split}
 &q^{-ab}\sum_{u\in U_q}
       \overline{\langle w,\operatorname{St}_q(u)v\rangle}
                                         \psi_U(u)\\
 &\hspace{12mm}=q^{-ab}d_q\,
       \overline{\langle w,u_0\rangle\langle u_0,v\rangle}.
 \end{split}
 \tag{RG15}
\]

The equality is the finite `psi_U` projector and the
one-dimensionality of its image. Thus the projection is
a multiple of the single coefficient `m`, including in
the multiplicity direction. By finite Schur orthogonality
the squared norm of `m` on `G_q` is `|G_q|/d_q`.
Its inner product with `f_U` is `d_q`. The scalar is
therefore exactly `d_q^2/|G_q|`, proving (RG14).
All other residue orbits are invariant under the source
compact and have zero restriction of `f_U`, so they do
not add any component to this projection.

Consequently

\[
 \|P_{\rm St}f_U\|^2
       =q^{-ab}\frac{d_q^3}{|G_q|},\qquad
 \frac{\|P_{\rm St}f_U\|^2}{\|f_U\|^2}
       =\frac{d_q^2}{|G_q|}=\alpha_q.
 \tag{RG16}
\]

The same calculation gives the more precise compact filter
actually used in a theta lift:

\[
 \boxed{\ \int_{\operatorname{GL}_a(O)}
       \overline{m(\bar g)}\,\omega(g)f_U\,dg
              =\frac{\alpha_q}{d_q}f_{\rm St}.\ }
 \tag{RG17}
\]

The compact has measure one. Finite Schur orthogonality
makes this filter `d_q^(-1)` times the projection onto
`u_0` on each Steinberg copy and zero on other irreducible
types. Equation(RG14) then proves (RG17). This also verifies
the sign: the kernel has `psi_U` covariance and the source
matrix coefficient is its complex conjugate, with covariance
`psi_U^(-1)` as required by the literal bilinear lift.

There is no claim that `P_St` is an integral projector.
For a fixed place above11 with `q` prime to11,

\[
 v_{11}(\alpha_q)=-v_{11}(|G_q|)
             =-\sum_{i=1}^{a}v_{11}(q^i-1).
 \tag{RG18}
\]

The explicit denominators are part of the compact averaging
cost. The raw factor (RG5) itself remains primitive.

## 4. A first global lift retaining the raw G factors

This section is a corollary of the local theorem and the
already established actual-family/jet/extraction inputs,
not an assertion of new global theta-family existence.
Use DO033 on the actual `J^2` host, or its separately
verified degree-seven host version DO034 once that version
and its rank/character hypotheses are in place. Keep a
selected primitive polynomial `P`, its actual period scalar
`mathcal P`, and its content upper bound `B_P`. In DO033,
`mathcal P=C^(2ab)`; on a different host its own period
formula must be used. Fix any further nonzero auxiliary
finite factor for which the actual simultaneous-jet theorem
has been established. It is retained in all its norms and
coefficient bounds. For clarity, the displayed formulas
below take that additional factor to be the normalized
vacuum; its known scalar factors can be multiplied back.

At each selected G place take the exact raw factor (RG5),
arising from the allowed class (RG3). Write

\[
 d_G=\prod_vd_{q_v},\quad
 A_G=\prod_v\alpha_{q_v},\quad
 \Gamma_U=\prod_vq_v^{-ab}d_{q_v},\quad
 \Gamma_{\rm St}=\prod_vq_v^{-ab}|G_{q_v}|/d_{q_v}.
 \tag{RG19}
\]

Then `Gamma_U=A_G Gamma_St`. The exact raw G Schwartz
norm is `sqrt(Gamma_U)`, and its tensor Heisenberg expansion
has coefficient absolute sum one and
`prod_v q_v^(ab-n_U)` nonzero terms. The Steinberg projection
is `A_G` times the tensor of the DO033 vectors.

Apply the actual simultaneous-jet theorem to that tensor of
the nonzero `f_St` vectors, not merely to an abstract finite
representation. With its Fourier support size `s_St`, one
can take a single permitted29 half-translate at

\[
                   M=29^e\ge3s_{\rm St}(D+1)-1,
 \qquad s_{\rm St}\le\prod_vq_v^{ab}.
 \tag{RG20}
\]

It gives an actual selected coefficient `a_lambda` with
`a_lambda != 0` and `v_11(a_lambda)<=B_P`, after the same
period removal and coordinate hypotheses as in DO033/034.
The29 operator and the real selected differential commute
with the G-compact action because they act at other places.
Thus the same individual permitted translate works before
the compact filtering of the raw factor; no replacement
of `f_U` by `f_St` in the prescribed kernel is necessary.

Let `I=vol(K*)^(-1)` be the exact source compact index for
the selected29 level, with full integral compacts at G,
and let `d_rho` be the selected real source dimension.
The identity class has trivial rational stabilizer at the
levels in DO033/034. Use their actual class-supported source
function
`F=conj(m_infty product_v m_v)`, zero on other classes.
It has initial literal `psi_U^(-1)` type at every G place.
Successive application of (RG17) and real Schur orthogonality
gives the exact raw-kernel value

\[
 \boxed{\ \Theta_{\rm raw}^{\rm bil}(F)(1)
       =\frac{A_G\,\mathcal P\,a_\lambda}{I d_\rho d_G}
       \ne0,\qquad
 \|F\|_2^2=\frac1{I d_\rho d_G},\quad\|F\|_\infty=1.\ }
 \tag{RG21}
\]

The proof performs the compact integral on the raw theta
kernel, replacing its G factor by the right-hand side of
(RG17) inside that integral. Absolute convergence of the
definite theta integral and the finite compact average
justify this operation. It is exactly the source's bilinear
convention, not a silently conjugated-input theta map.

After making the raw finite input and source input unit
norm, the value becomes

\[
 \Theta_{\rm raw,unit}^{\rm bil}(F_{\rm unit})(1)
       =\frac{A_G\,\mathcal P\,a_\lambda}
                    {\sqrt{\Gamma_U}\sqrt{I d_\rho d_G}}.
 \tag{RG22}
\]

If the real Schwartz vector is also made unit, divide by
its exact norm from R011/DO034. Every factor is displayed;
in particular the Steinberg averaging factor is not omitted.
For `q_v` prime to11,

\[
 \begin{split}
 v_{11}(\Gamma_U)&=v_{11}(d_G)=0,\\
 v_{11}(A_G)&=-\sum_v\sum_{i=1}^{a}v_{11}(q_v^i-1),\\
 v_{11}\!\left(\mathcal P^{-1}
                 \Theta_{\rm raw}^{\rm bil}(F)(1)\right)
   &\le B_P-v_{11}(I d_\rho)
                  -\sum_v\sum_{i=1}^{a}v_{11}(q_v^i-1).
 \end{split}
 \tag{RG23}
\]

This is an upper content witness for one actual first
coefficient. It is neither a lower divisibility theorem
for all rows nor a comparison with the full global DP44
cost. It also does not say that the original raw theta
kernel has only Steinberg type.

For `f` selected places above each of two completely split
rational G primes `g_0,g_1`, the local factors specialize to

\[
 \begin{split}
 d_G&=(g_0g_1)^{f a(a-1)/2},\\
 \Gamma_U&=(g_0g_1)^{f(-ab+a(a-1)/2)},\\
 A_G&=(g_0g_1)^{-fa}
       \prod_{\epsilon=0}^{1}\prod_{i=1}^{a}
                                     (1-g_\epsilon^{-i})^{-f}.
 \end{split}
 \tag{RG24}
\]

These identities use `|GL_a(F_q)|=q^(a^2) product_i(1-q^(-i))`
and are field-general local counts. The source index `I`
must still be the correct one for the actual global host:
old `J^2` and repaired `J^14` have different rational29
ramification and therefore different exponents in that index.

## 5. What this closes and what remains

The local equality (RG6) closes the raw initial G-factor
identification for the displayed allowed coupled class when
`m=2`. Equations(RG14) and(RG17) prove nonzero interaction
with the actual initial Steinberg input and compute its
exact cost. The conditional global corollary proves that
this raw G factor can be retained in the actual first lift
once the cited actual-family and selected-jet hypotheses
are satisfied.

The statement does not identify a complete `XiCpl1` unless
its other actual T/Q factors and their finite family are
also supplied. It does not prove nonvanishing of `XiAt`
at later stages for `m>2`, identify the terminal `PhiTop`,
construct all six `AdmS` ties, or compute the full DP44
changed-data cost. Those are separate exact source gates.
No isotypic occurrence is being substituted for preservation
of a prescribed later arithmetic image lattice.

## 6. Sources and checks

Accepted inputs: DO033's generic vector, actual split
action, phase-correct Fourier model, simultaneous jets,
and compact class extraction; DO029/030 for the actual
Heisenberg and auxiliary multijet comparison; R012/R011
for the selected real polynomial and norm. Their proved
scope is retained. DO034 is needed separately before the
new host is used in the global corollary.

Steinberg, R. (1957). Prime power representations of finite
linear groups II. *Canadian Journal of Mathematics, 9*,
347–351. https://doi.org/10.4153/CJM-1957-041-1 .
Theorems1–2, pp.348–350: published Steinberg construction,
irreducibility, and regular restriction to the upper
unipotent. Read in the publisher PDF during this run.

Geck, M. (2015). *On the ell-modular composition factors of
the Steinberg representation*. https://arxiv.org/pdf/1504.04157 .
Theorem2.1 and Corollary2.3, pp.3–5: the integral flag
model and characteristic-zero properties used in DO033.

Author whole-proof reading was completed on 21 November 2026,
including all source predicates, the full isotypic multiplicity
argument, the compact filter, the conditional global extraction,
and every displayed norm/valuation factor. The exact diagnostic
passed 729 residue-matrix predicate comparisons, 48 full
Steinberg projections, 48 matrix-coefficient filters, and the
full 729-point Fourier transform. Its raw norm is `1/243`,
projection scalar `3/16`, and projected norm is `1/1296`.
The separate TSV records the check time and exact scope.

The exact diagnostic `raw_first_g_steinberg_certificate.py`
checks both raw predicates and the full finite Steinberg
projection/filter in `GL_2(F_3)`, with a nontrivial determinant
splitting and all residue matrices. It also checks the
explicit raw Fourier expansion and all displayed finite
norms. This diagnostic is not a proof of the general rank
statement or a verification of a full Lean datum.
