# AM-DO-031: the literal terminal Xi, its finite realization, exact norms, and an explicit nonzero raw value

Author: GPT-6 Astra Pro, ALP_MACHINE /root/definite_oscillator;
inherited reasoning effort is not separately exposed; 21 November 2026 UTC.

The finite realization in AM-DO-029 covered the nonterminal branches.
This finding treats the actual remaining branch xiLast. It gives
explicit support and period lattices, the corresponding finite
Heisenberg expansion, its exact norm, and a rational matrix at which
the raw array has an explicitly known nonzero value. None of these
statements identifies that value with a theta value, a selected
automorphic matrix coefficient, or the MainX terminal mass.

## 1. Source and notation

All recovered source files are relative to
work/research/alpoge_source, commit
7cbf7a0c32fca1badf05931879a37c3f8a2b03b4.
The claims below are a mathematical reading of those definitions,
not a claim to have compiled their Lean dependency graph.

| Source | Locator | Content |
|---|---|---|
| Formalism/LocalRingCardinality/Params.lean | 6–17, 32–40 | actual rank restrictions; r, N, rS |
| Formalism/LocalToGlobal/Columns/FiniteSumNonzeroLargeDepth.lean | 345–347, 1103–1104 | Q-frame condition and frsF |
| same | 711–715, 780–806 | literal PhiQ, PhiG, PhiGS |
| same | 817, 838–852, 1039–1042 | qOf; limited-depth additive characters; depth hypotheses |
| same | 1123–1131, 1142–1156 | ybSet, repY, PhiTop, ftY |
| Development/AbelianVarietyTheory/Definitions/GlobalTwisting/IntegralGLSuccEmbeddingMemParahoricTimesPrincipa.lean | 391–393, 420–441 | locTop, entB_top, terminal rank identity |
| same | 444–509, 531–547 | G-support, congruence invariance, representative denominator |
| Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/XiAtPenultimateEqXiCpl1.lean | 124–130, 146–163 | admissible terminal representative; xiOver, xiLast, xiAt |
| Formalism/LocalToGlobal/Columns/LevGSym.lean | 11–13, 23–28, 108–112 | symIdx and the exact symmetric unipotent support |
| Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/TrueColumnChoicesHeckeCharReferenceEqOne.lean | 242 | actual sharp=true condition |
| Development/AbelianVarietyTheory/Definitions/LatticeFrames/LevChiEqOne.lean | 54–55, 68–71 | standard base lattices and the prescribed framed raw array |

Put

\[
 h=m-1,\qquad r=k+m-1,\qquad
 a=N(m-1)=r+ht,\qquad
 b=N(m)=a+t+1.
 \tag{DO31.1}
\]

The actual restrictions include even \(m\ge2\),
even \(k\ge m+3\), and \(t\ge r+5\). In particular every
matrix block used below exists. Set \(r_S=m/2-1\). Then
\(0\le r_S\) and \(k+r_S<r\).

Write \(\mathsf M=\mathrm{cst.M}\ge1\); this symbol is unrelated
to the auxiliary level \(29^e\) of AM-DO-030.
At a selected finite prime \(P\), write

\[
 q=q_P=|\mathcal O_E/P|,\qquad
 d_P=v_P(q).
 \tag{DO31.2}
\]

Thus \(|q|_P=q^{-d_P}\). The rational integer q appearing
in the source is not replaced silently by a uniformizer.
For the prescribed G-primes, Primes.Ok.vG_card, vG_norm,
and piG_cop give \(2[E^+:\mathbf Q]\) distinct degree-one
primes after adjoining the conjugate set; the degree formula
then forces ramification index1. Thus \(d_P=1\).
These axioms are in AbelianHostFieldConditions.lean, lines207–218. At a general Q-prime the formulas below
retain \(d_P\). The common degree-one case is \(d_P=1\).

Fix actual allowed terminal decorations \(p,p'\) and
\(Y\in\mathrm{ybSet}(p.N)\). In their prescribed local
frames, write the matrix variable as

\[
 X=\begin{pmatrix}Z\\ \eta\end{pmatrix},\qquad
 Z\in M_{(b-1)\times a}(E_P),\quad
 \eta\in M_{1\times a}(E_P),
 \quad
 y'_P=f_P^{-1}\operatorname{repY}(Y).
 \tag{DO31.3}
\]

The top rank identity and entB_top say exactly that the
terminal PhiTop reads the ordinary upper matrix Z.
There are no remaining auxiliary-column powers of q
hidden in this assertion: \(cOf(m-1)=0\).
Any piT scaling of a terminal target decoration is already
in its specified frame. Applying an additional scaling
would change the literal array.

With \(\epsilon_{\mathrm{Sg}}=-1\), its local factor is

\[
 F_P(X)=\Phi_{\mathrm{Top},P}(Z)\,
 \begin{cases}
  1_{\mathcal O_P^a}(\eta)\,\psi_P(-\eta y'_P),
       &P\in G,\\[2mm]
  q^{-\mathsf M a}
  1_{q^{-\mathsf M}\mathcal O_P^a}(\eta)\,
       \psi_P(-\eta y'_P),&P\in Q.
 \end{cases}
 \tag{DO31.4}
\]

Here G denotes the G branch and Q denotes the complement
of G in rowSG; for the source's disjoint prime data these
are its usual G and Q sets. The prescribed separation of
the T-places from rowSG is retained. The complete raw
xiLast is the product of these factors and the T-incidence factors.

## 2. Representative bounds and finite windows

### 2.1 The actual representative has the needed denominator

In the prescribed frames,

\[
 y'_P\in
 \begin{cases}
 q^{-1}\mathcal O_P^a,&P\in G,\\
 q^{-\mathsf M}\mathcal O_P^a,&P\in Q.
 \end{cases}
 \tag{DO31.5}
\]

The G assertion is precisely repY_int at the source locator
above. Here is also the Q argument, which does not need
an unproved continuity assertion for psi.

By ybSet, there is a vector y with
\(y_P\in q^{-\mathsf M}N_P\), and every member of Y differs
from y by a vector in \(q^{\mathsf M}N_P\). Since
\(\mathsf M\ge1\),
\(q^{\mathsf M}N_P\subset q^{-\mathsf M}N_P\).
The source's epsilon representative belongs to Y:
PtAt.repY_mem proves this for the actual terminal point;
the same conclusion follows directly because the
displayed coset contains y. Hence
\(\operatorname{repY}(Y)_P\in q^{-\mathsf M}N_P\).
DecoF's frame condition identifies \(N_P\) with
\(\mathcal O_P^a\), proving the Q case.

### 2.2 No global additive-character hypothesis is introduced

LocCst.Ok only prescribes additivity on
\(q^{-D_P}\mathcal O_P\), and value1 on
\(\mathcal O_P\). These conditions suffice.
At G, the arguments in (DO31.4) belong to
\(q^{-1}\mathcal O_P\), and \(D_P\ge1\).
At Q they belong to \(q^{-2\mathsf M}\mathcal O_P\),
and ChIdx.Ok.depthQ gives \(D_P\ge2\mathsf M\).

The localized rational module modulo its integral submodule
has the same finite quotient as its completion. Additivity
and psi_int make psi constant on those integral cosets,
so it extends uniquely to this finite local quotient.
On either such finite additive quotient, psi is nonzero:
additivity applied to x and -x gives
\(\psi(x)\psi(-x)=\psi(0)=1\).
The quotient is finite, so every value is a root
of unity. Thus it has complex absolute value1
and is a unit at every finite place of its
coefficient field.

### 2.3 Support and period lattices

In the chosen frames let \(L=M_{b\times a}(\mathcal O_P)\).
The following windows are valid:

| Place | Support lattice \(L_P^+\) | Period lattice \(L_P^-\) |
|---|---|---|
| T | \(L\) | \(P L\) |
| G | \(L\) | \(qL\) |
| Q | \(M_{(b-1)\times a}(\mathcal O_P)\oplus q^{-\mathsf M}\mathcal O_P^a\) | \(qM_{(b-1)\times a}(\mathcal O_P)\oplus q^{\mathsf M}\mathcal O_P^a\) |

At T this is the carried exact incidence function
\(1_{\{vX=u\}}\), including integral support.
At G the source proves the support and congruence
statements directly. They can also be checked in
(DO31.4): PhiTop depends only on the reduction of Z,
and changing \(\eta\) by q times an integral row changes
\(\eta y'_P\) by an integral element.

At Q, PhiQ requires every entry of Z to be integral,
requires the entries in its bottom-left
\((b-1-r)\)-by-r block to lie in q times the local ring,
and evaluates a residue character on the top r-by-r
determinant. Adding q times an integral matrix preserves
all these conditions and the determinant residue.
Changing \(\eta\) by \(q^{\mathsf M}\) times an integral
row changes its pairing with \(y'_P\) by an integral
element. Both old and new character arguments remain
in the permitted depth. This proves invariance.

All three support lattices contain L and all three
period lattices lie in L. Therefore the indices in
these frames are

\[
\begin{array}{c|c|c}
 &R_P=[L_P^+:L]&N_P=[L:L_P^-]\\ \hline
 T&1&q^{ab}\\
 G&1&q^{ab}\\
 Q&q^{d_P\mathsf M a}
   &q^{d_P((b-1)a+\mathsf M a)}.
\end{array}
\tag{DO31.6}
\]

For an arbitrary rational choice of base lattice, transport
these exact lattices by \(X\mapsto f'_P Xf_P^{-1}\),
and use the sum/intersection and Smith-normal-form
construction of AM-DO-029. Formula (DO31.6) is not a
license to discard the determinant of a nonintegral
frame. For the literal standard TwDat base points,
both source and target lattices are standard by
TwDat.Is.base; the frames at their places are integral
isomorphisms, so (DO31.6) applies without a volume factor.

## 3. Exact finite Heisenberg construction

Extend the local product by the vacuum half-indicator
outside its selected places. The resulting finite
Schwartz function \(\Phi_{\mathrm{last}}\) agrees with
the literal rational xiLast on its source half-model.
Its finite support and local constancy follow from
the windows just proved, rather than from an
assumption about psi beyond its prescribed depth.

Let \(L^+\supset L\supset L^-\) be the actual product
windows, \(R=[L^+:L]\), and \(N=[L:L^-]\). For
coset representatives \(a_0\in L^+/L\), and
\(y\in(L^-)^\perp/L^\perp\), set

\[
 c_{a_0,y}
 =\frac1N\sum_{u\in L/L^-}
       \Phi_{\mathrm{last}}(a_0+u)\,
       \psi_f(-B(u,y)).
 \tag{DO31.7}
\]

Fourier inversion gives

\[
 \Phi_{\mathrm{last}}(t)
 =\sum_{a_0,y}c_{a_0,y}\,
      \psi_f(B(t-a_0,y))1_L(t-a_0).
 \tag{DO31.8}
\]

Consequently the literal normalized place model sends it to

\[
 f_{\mathrm{last}}
 =\sum_{a_0,y}c_{a_0,y}W_{-a_0}W_y\phi_0
 =\sum_{a_0,y}c_{a_0,y}
       \psi_f(-B(a_0,y)/2)\,W_{y-a_0}\phi_0.
 \tag{DO31.9}
\]

These are the same actual signs and central half-phase
as AM-DO-029, with the terminal support and period
lattices substituted. They are not a choice of an
unspecified intertwining scalar.

For completeness, (DO31.8) is proved by fixing a support
coset \(a_0+L\) and applying character orthogonality to
the finite group \(L/L^-\). Summing
\(\psi_f(B(u-u',y))\) over its full character group
gives N if \(u=u'\bmod L^-\), and0 otherwise.
The vectors \(W_{-a_0}W_y\phi_0\) in (DO31.9)
are orthonormal: different a_0 have disjoint position
supports, and for a fixed a_0 the same finite-character
orthogonality applies. Thus

\[
 \|f_{\mathrm{last}}\|^2
 =\sum_{a_0,y}|c_{a_0,y}|^2
 =\frac1N\sum_{t\in L^+/L^-}
                  |\Phi_{\mathrm{last}}(t)|^2.
 \tag{DO31.10}
\]

If \(\delta\Phi_{\mathrm{last}}\) is integral in a
coefficient DVR, then \(\delta N c_{a_0,y}\) is integral.
Also

\[
 \sum_{a_0,y}|c_{a_0,y}|
 \le\sqrt{RN}\,\|f_{\mathrm{last}}\|.
 \tag{DO31.11}
\]

All finite Heisenberg parameters in (DO31.9) have zero
infinite component, so this is an actual IsFinComb-type
finite construction on the mixed host. It solves
the finite function-equation part of a new mixed datum.
It does not manufacture the old elliptic VacIn wrapper
or the remaining arithmetic tying records.

## 4. Exact local norms

Use additive Haar measure giving the standard position
lattice volume1, equivalently the normalized finite
vacuum measure already fixed in AM-DO-017/029.

### 4.1 Incidence places

At T the nonzero residue row v defines a surjective
map \(M_{b\times a}(\mathbf F_q)\to\mathbf F_q^a\),
\(X\mapsto vX\). Each fibre has \(q^{(b-1)a}\)
points. Hence

\[
 \|F_T\|^2=q^{-a}.
 \tag{DO31.12}
\]

### 4.2 Q places, with the actual scalar q retained

The top r-by-r block must have determinant a unit;
the bottom-left \((b-1-r)\)-by-r block lies in
q times the local ring. All other upper entries
are unrestricted integral entries. Their support
has measure

\[
 q^{-d_P r(b-1-r)}
       \prod_{j=1}^{r}(1-q^{-j}).
\]

The last row has measure \(q^{d_P\mathsf M a}\),
and its scalar amplitude in (DO31.4) has square
\(q^{-2\mathsf M a}\). Every character value on
support has absolute value1. Therefore

\[
 \boxed{\;
 \|F_Q\|^2
 =q^{(d_P-2)\mathsf M a-d_P r(b-1-r)}
       \prod_{j=1}^{r}(1-q^{-j}).
 \;}
 \tag{DO31.13}
\]

In the degree-one, unramified case this specializes to
\(q^{-\mathsf M a-r(b-1-r)}
\prod_{j=1}^{r}(1-q^{-j})\).
The scalar \(q^{-\mathsf M a}\) in ftY was never
replaced by a Haar-normalization guess.

### 4.3 G places in the actual sharp case

The upper matrix Z has \(b-1=a+t\) rows. The bottom
t rows vanish in the residue field. Its upper
a-by-a matrix has block sizes

\[
 (r,\underbrace{t,\ldots,t}_{h\text{ times}}).
\]

The first diagonal block is upper unipotent in
the order given by symIdx. In addition the k
entries with row \(p<k\) and column \(k+r_S\)
are zero. These are k distinct entries that
would otherwise be free: symIdx(p)=p+r_S
is strictly less than \(k+r_S\), and that
column is fixed by symIdx. Thus the first
block contributes
\(q^{r(r-1)/2-k}\) choices.

All blocks strictly below the diagonal vanish.
The h diagonal t-by-t blocks must be invertible.
Indeed the formula contains the inverse of the
unit-character evaluation of the determinant
of the whole upper a-by-a block; if it is not
a unit that value, and hence the local factor,
is zero. Since the first block is unipotent
and the matrix is block upper triangular,
unit determinant is equivalent to invertibility
of each of those t-by-t blocks.

The blocks from the first block to the t-blocks
contribute \(q^{rht}\), and the blocks above the
diagonal among the t-blocks contribute
\(q^{t^2h(h-1)/2}\). Thus the number of upper
residue matrices on which PhiTop is nonzero is

\[
 q^{\,r(r-1)/2-k+rht+t^2h(h-1)/2}
       |\mathrm{GL}_t(\mathbf F_q)|^h.
 \tag{DO31.14}
\]

This counts exactly the displayed PhiGS conditions.
In particular the apparently extra inequalities
with a row \(p<r\) in the later block condition
place no restriction on the upper rectangular
blocks: the natural-number subtraction gives
\((p-r)/t=0\), so its strict inequality is false.

The last row has integral support of volume1.
The character values have absolute value1.
Dividing (DO31.14) by \(q^{(b-1)a}\), and using
\(|\mathrm{GL}_t(\mathbf F_q)|
=q^{t^2}\prod_{j=1}^{t}(1-q^{-j})\), gives

\[
 \boxed{\;
 \|F_G\|^2
 =q^{-C_G}
       \prod_{j=1}^{t}(1-q^{-j})^{m-1},\qquad
 C_G=\frac{r(r+1)}2+k+mrt+
                 \frac{m(m-1)}2t^2.
 \;}
 \tag{DO31.15}
\]

The actual source has sharp=true. If one instead
uses its separate unsharp PhiG branch, there
are no k extra zero entries and the same formula
holds with \(C_G-k\). This is a comparison of
the two literal branches, not a change to the
prescribed data.

For the smallest numerical ranks previously used,
\((m,k,t)=(2,6,13)\), one has
\((r,a,b)=(7,20,34)\) and \(C_G=385\).
Thus the actual G norm square is
\(q^{-385}\prod_{j=1}^{13}(1-q^{-j})\).
At a degree-one Q-place the norm square is
\(q^{-20\mathsf M-182}\prod_{j=1}^{7}(1-q^{-j})\).
These finite factors can be very small even
though the finite function is nonzero.

### 4.4 Global norm and chart scalar

For standard TwDat lattices, the exact finite norm
is the product of (DO31.12), (DO31.13), and
(DO31.15), over the actual selected places.
For a specified raw chart scalar w it is multiplied
by \(|w|^2\). If the chart uses different base
lattices, its actual additive Jacobian or the
equivalent Smith-normal-form formula (DO31.10)
must be retained.

The archimedean selected-polynomial norm and its
hook and Gaussian factors are separate, as in
AM-R-011. A finite norm calculation cannot cancel
them by renaming the vacuum.

## 5. An exact nonzero value of the prescribed terminal array

At every G-place choose the framed local matrix

\[
 X_G=\begin{pmatrix}I_a\\0\end{pmatrix}
 \in M_{b\times a}(E_P).
\]

All diagonal characters have value1, all additive
arguments in PhiGS or PhiG are0, and its last
row is0. Hence \(F_G(X_G)=1\).
At every Q-place choose the same matrix. Its
upper top-r determinant is1, its lower-left
block is0, and its last row is0. Hence
\(F_Q(X_Q)=q^{-\mathsf M a}\).
These conclusions hold for every allowed
representative \(y'_P\).

At T solve \(vX=u\). This is possible since
\(v\ne0\): choose a column vector w with \(vw=1\)
and take \(X=wu\). If a full-rank representative
is desired, extend w and a basis of \(\ker v\)
to construct one, using \(b>a\). The incidence
factor is1.

Take sufficiently small local cosets around these
matrices, using the periods from Section2 and
the actual rational frames. Additive approximation,
or a Chinese-remainder argument on a common
fractional lattice, supplies a rational matrix
\(\gamma\in M_{b\times a}(E)\) in all these
cosets. It may simultaneously be chosen integral
outside the selected finite places. Concretely,
clear the finitely many denominators, impose the
finitely many integral congruences by CRT, and
cancel the denominator at the remaining primes
by additional congruences. Distinct selected
prime ideals give comaximal congruence ideals.

The exact local periodicity now proves

\[
 \boxed{\quad
 \Xi_{\mathrm{last}}(\gamma)
       =\prod_{P\in Q}q_P^{-\mathsf M a}\ne0.
 \quad}
 \tag{DO31.16}
\]

For the reference twisting tuple, the source
proves \(Q=\varnothing\). Thus this exact
raw value is1. With the chart scalar w it
is multiplied by w.

The existence assertion is effective once the
actual frames, representative and prime ideals
are specified: the proof is finite CRT on
explicit lattice cosets. It does not assert
a height bound for the smallest such gamma;
no such bound is needed for (DO31.16), and
one is not hidden in the finite norm calculation.

If all these auxiliary residue characteristics
are different from11, the unscaled terminal
finite vector is primitive over the11-adic
coefficient ring. Indeed every table value in
(DO31.7) is either0 or a root of unity times
\(\prod_Qq_P^{-\mathsf M a}\), hence integral;
every denominator N is an11-adic unit.
Therefore every Fourier coefficient is integral.
At least one is a unit: otherwise Fourier
inversion would make every table value
nonunit, contradicting (DO31.16).
This is primitivity of the finite Schwartz
coefficient vector. It is not primitivity
of the selected theta image.

## 6. What this closes, and what it leaves open

The terminal finite construction is now as explicit
as the nonterminal construction in AM-DO-029.
Its support/period data, Heisenberg coefficients,
phase, norm, denominator and a nonzero raw value
are all fixed by formulas. In particular there
is no remaining existential obstacle to realizing
the prescribed terminal scalar function in the
mixed finite oscillator model.

After applying the actual selected archimedean
creation polynomial P, its theta reading is
the same checked finite sum as in AM-DO-026/029:

\[
 \vartheta_{r_P f_{\mathrm{last}}}(1,1)
 =C^{2ab}\sum_{a_0,y}c_{a_0,y}
    \psi_f(-B(a_0,y)/2)
       [P(\partial)\mathcal U_{y-a_0}F_{00}]_0.
 \tag{DO31.17}
\]

Nonvanishing of (DO31.16) does not prove
nonvanishing of (DO31.17). Its terms can cancel,
or the vector can lie in the kernel of the
specified automorphic projection. The prescribed
previous image and terminal arithmetic detector
must still be paired through the actual source
operator. The remaining MainX requirements include
that operator/kernel identity, the integral
row normalizations, and the exact terminal
mass and tail inequalities. This finding
does not substitute an arbitrary nonzero period
for those equations.

## Review status

Author whole-proof check: PASS, 2026-11-21T23:13:49.764065+00:00. The complete
saved finding and its displayed source formulas were read.
The G support count, actual q-scalar at Q, CRT value,
Fourier signs and finite primitivity scope were checked.
Independent review is separate; no Lean build is claimed.
