# AM-DO-032: the actual terminal Y-family, exact Fourier Gram, and its projection denominator

Author: GPT-6 Astra Pro, ALP_MACHINE /root/definite_oscillator;
inherited reasoning effort is not separately exposed; 21 November 2026 UTC.

This is a further calculation on the literal xiLast of AM-DO-031.
It varies only the Y-parameter already present in the recovered
source. It identifies its finite Fourier family, the exact Gram
matrix, and the denominator of its orthogonal projector. Its
arithmetic denominator is for this specified finite family; it
does not identify the global MainX terminal detector lattice.

## 1. The literal finite parameter set

Retain the notation and all source hypotheses of AM-DO-031:
\[
 a=N(m-1),\quad b=N(m),\quad r=k+m-1,\quad
 \mathsf M=\mathrm{cst.M},\quad
 q_P=|\mathcal O_E/P|,\quad d_P=v_P(q_P).
 \tag{DO32.1}
\]
In particular the T-places and rowSG are disjoint, and
G denotes the G branch while Q denotes its complement
inside rowSG. For the actual standard TwDat base points,
the local frame lattices are standard.

The source definitions are:

| Source | Locator |
|---|---|
| Formalism/LocalToGlobal/Columns/FiniteSumNonzeroLargeDepth.lean | ybSet and repY,1123–1131; ftY,1150–1156 |
| Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/XiAtPenultimateEqXiCpl1.lean | actual terminal point and representative,124–130; xiOver/xiLast,146–157 |
| Development/AbelianVarietyTheory/Definitions/GlobalTwisting/IntegralGLSuccEmbeddingMemParahoricTimesPrincipa.lean | locTop,391–393; representative bound,531–547 |

For fixed source decoration, ybSet is the set of cosets
of the product-local period module in the product-local
support module. Therefore it is canonically the finite set
\[
 \mathcal Y=
 \prod_{P\in G}(q_P^{-1}\mathcal O_P^a/\mathcal O_P^a)
 \ \times
 \prod_{P\in Q}
     (q_P^{-\mathsf M}\mathcal O_P^a/
                      q_P^{\mathsf M}\mathcal O_P^a).
 \tag{DO32.2}
\]
This statement concerns cosets, not the particular epsilon
representative chosen by repY. To prove it, send a rational
coset to its local residue classes. Injectivity is exactly
the definition of its period module as the intersection
of the local conditions. Surjectivity follows by CRT
after clearing the finitely many denominators, as in
AM-DO-031 Section5. The prescribed frames identify the
localized source lattice with each standard local lattice.
Thus every tuple in (DO32.2) is an actual allowed Y.

Changing repY within its coset changes its local component
by \(\mathcal O_P^a\) at G and by
\(q_P^{\mathsf M}\mathcal O_P^a\) at Q.
On the supports of ftY, the resulting character argument
is integral. LocCst.Ok.psi_int therefore proves that
the local finite function is unchanged. No representative
phase is suppressed.

## 2. The exact local Fourier calculation

At a G-place, \(d_P=1\), and the source limited-depth
character induces a nontrivial additive character on
\(q^{-1}\mathcal O_P/\mathcal O_P\). Since q is the
rational prime and the residue degree is1, its pairing
with \(\mathcal O_P/q\mathcal O_P\) is perfect.
The last-row functions are exactly
\[
 \varphi_y(\eta)=1_{\mathcal O_P^a}(\eta)
                       \psi_P(-\eta y),
 \qquad y\in q^{-1}\mathcal O_P^a/\mathcal O_P^a.
 \tag{DO32.3}
\]
With additive measure giving \(\mathcal O_P^a\)
volume1, they are an orthonormal basis of the
functions supported there and constant modulo
\(q\mathcal O_P^a\):
\[
 \langle\varphi_y,\varphi_{y'}\rangle
          =1_{\{y=y'\}}.
 \tag{DO32.4}
\]
Indeed the integral of a nontrivial character on
a compact additive group is0: translation by an
element at which it is not1 multiplies that integral
by a nontrivial scalar. For a trivial character
the integral is the group's volume1.

At a Q-place the source character is only required
on \(q^{-D_P}\mathcal O_P\), where
\(D_P\ge2\mathsf M\). Its annihilator of the local
ring within this domain is an \(\mathcal O_P\)-module:
\[
 \mathfrak a_{\psi,P}
 =\{z\in q^{-D_P}\mathcal O_P:
                  \psi_P(z\mathcal O_P)=1\}
 =P^{c_P},
 \qquad -d_P<c_P\le0.
 \tag{DO32.5}
\]
Here and below P denotes its maximal ideal in the
completion. To justify every part of (DO32.5),
the set is closed under addition and multiplication
by \(\mathcal O_P\), contains \(\mathcal O_P\),
and lies in a fixed fractional ideal. Hence it is
a fractional ideal \(P^{c_P}\). The source condition
\(\psi_P(q^{-1})\ne1\) excludes \(q^{-1}\) from it,
so \(c_P>-d_P\), while its inclusion of the ring
gives \(c_P\le0\). The same conductor ideal is
therefore already determined on the smaller
argument range needed for ftY. This reasoning
uses only the finite additive quotient and
does not extend the source character arbitrarily.

The actual Q functions, including the source scalar, are
\[
 \varphi_y(\eta)=q^{-\mathsf M a}
 1_{q^{-\mathsf M}\mathcal O_P^a}(\eta)
                      \psi_P(-\eta y),
 \qquad
 y\in H_P:=
 q^{-\mathsf M}\mathcal O_P^a/
                       q^{\mathsf M}\mathcal O_P^a.
 \tag{DO32.6}
\]
The pairing radical is
\[
 R_P=
 q^{\mathsf M}P^{c_P}\mathcal O_P^a/
                       q^{\mathsf M}\mathcal O_P^a,
 \qquad |R_P|=q^{-c_Pa}.
 \tag{DO32.7}
\]
The notational product \(P^{c_P}\mathcal O_P^a\)
means componentwise multiplication by that fractional
ideal. The bounds in (DO32.5) imply that its numerator
is inside the support module. Two allowed y's give
exactly the same function if their difference is
in \(R_P\). Otherwise their inner product is0.
More precisely,
\[
 \boxed{\quad
 \langle\varphi_y,\varphi_{y'}\rangle
 =q^{(d_P-2)\mathsf M a}
                1_{\{y-y'\in R_P\}}.
 \quad}
 \tag{DO32.8}
\]

To prove (DO32.8), the character integral is nonzero
precisely when
\((y-y')q^{-\mathsf M}\mathcal O_P\subset P^{c_P}\),
coordinate by coordinate. This is exactly (DO32.7).
Its nonzero value before the amplitude is the
volume \(q^{d_P\mathsf M a}\); the squared amplitude
is \(q^{-2\mathsf M a}\). Their product gives
the displayed factor. If the character is trivial
on the full support, the two functions agree
pointwise, not just up to a scalar, since their
value at \(\eta=0\) is the same nonzero number.

After removing the duplicate parameters, the number
of Q functions is
\[
 |H_P/R_P|=q^{(2d_P\mathsf M+c_P)a}.
 \tag{DO32.9}
\]
They span exactly the functions supported on
\(q^{-\mathsf M}\mathcal O_P^a\) and constant
modulo \(q^{\mathsf M}P^{c_P}\mathcal O_P^a\).
This follows from finite Fourier inversion for
the resulting perfect quotient pairing.

In the degree-one case \(d_P=1\), (DO32.5)
forces \(c_P=0\). There are no duplicates,
the common norm square is \(q^{-\mathsf M a}\),
and the matrix of values
\[
 q^{-\mathsf M a}\psi_P(-\eta y),
 \qquad \eta,y\in H_P,
 \tag{DO32.10}
\]
is unitary for counting measure: \(|H_P|=q^{2\mathsf M a}\).
This explains the literal scalar in ftY without
replacing it by a guessed Haar normalization.

## 3. Gram matrix of the prescribed terminal family

Let \(f_Y\) be the actual finite Heisenberg realization
of xiLast for Y, using AM-DO-031. All upper-matrix
and T-incidence factors are fixed as Y varies.
The local positions at distinct selected places
are independent. Consequently the preceding
last-row inner products tensor with the fixed
nonzero upper and T factors.

Let
\[
 \overline{\mathcal Y}=
 \prod_{P\in G}
        (q_P^{-1}\mathcal O_P^a/\mathcal O_P^a)
 \times\prod_{P\in Q} H_P/R_P,
 \qquad n_Y=|\overline{\mathcal Y}|.
 \tag{DO32.11}
\]
Choose one representative for each reduced class.
The remaining choices give identical finite vectors.
Then
\[
 \boxed{\quad
 \langle f_Y,f_{Y'}\rangle_f
                =\kappa\,1_{\{Y=Y'\}},
 \qquad
 \det\operatorname{Gram}(f_Y)=\kappa^{n_Y},
 \quad}
 \tag{DO32.12}
\]
where the nonzero rational number \(\kappa\)
is exactly the unscaled finite norm square
computed in AM-DO-031:
\[
\begin{split}
 \kappa={}&
 \prod_{P\in T}q_P^{-a}
 \prod_{P\in G}
    \left[
     q_P^{-C_G}
       \prod_{i=1}^{t}(1-q_P^{-i})^{m-1}
    \right]\\
 &{}\cdot
 \prod_{P\in Q}
    \left[
     q_P^{(d_P-2)\mathsf M a-d_P r(b-1-r)}
       \prod_{i=1}^{r}(1-q_P^{-i})
    \right],\\
 C_G={}&r(r+1)/2+k+mrt+m(m-1)t^2/2.
\end{split}
\tag{DO32.13}
\]
The scalar is unchanged by the actual Y-representative.
A prescribed common chart scalar w multiplies
the Gram by \(w\overline w\); it must be retained.
Nonstandard lattice frames retain their actual
Jacobian as in AM-DO-031.

Thus this is a source-defined orthogonal family,
not a new arbitrary choice of finite inputs.
It is a basis of its actual finite span. The
identity (DO32.12) is a finite oscillator
pairing, not an automorphic Petersson pairing.

## 4. Integral saturation versus the exact pairing denominator

Assume all selected residue characteristics differ
from11, and work over a coefficient valuation ring
containing the finite character values. Conjugate
coefficient lattices are paired when the chosen
11-place is not fixed by the coefficient involution.
Every root of unity remains an11-adic unit.

The lattice generated by the distinct \(f_Y\) is
saturated in the finite function module on its
ambient support/period window, intersected with
its characteristic-zero span. Here is a direct
argument. Finite Fourier inversion uses only
orders of finite p-groups with \(p\ne11\);
its denominators are units. The invariant
submodule under the radicals in (DO32.7) is
split by the corresponding averaging idempotent,
whose denominator is again a unit. Finally the
fixed upper/T factor has a unit-valued coordinate:
use the local identity and incidence matrices
of AM-DO-031 Section5. Evaluation at that
coordinate splits tensor multiplication by
that fixed factor, after multiplying by its
unit inverse. This proves saturation.

Nevertheless the pairing on this saturated
lattice need not be unimodular. From (DO32.13),
\[
 \boxed{\quad
 v_{11}(\kappa)
 =\sum_{P\in G}(m-1)
                  \sum_{i=1}^{t}v_{11}(q_P^i-1)
   +\sum_{P\in Q}\sum_{i=1}^{r}
                         v_{11}(q_P^i-1).
 \quad}
 \tag{DO32.14}
\]
All powers of q are units at11, so this formula
holds for the general-Q calculation as well.
For \(o_P=\operatorname{ord}_{11}(q_P)\mid10\)
and \(h_L=\lfloor L/o_P\rfloor\), the exact
elementary lifting-the-exponent formula gives
\[
 \sum_{i=1}^{L}v_{11}(q_P^i-1)
   =h_L\,v_{11}(q_P^{o_P}-1)+v_{11}(h_L!).
 \tag{DO32.15}
\]
Indeed the terms vanish unless \(o_P\mid i\);
for \(i=o_Pj\) their valuation is
\(v_{11}(q_P^{o_P}-1)+v_{11}(j)\).

In the actual rank range, \(t\ge13\).
Thus every G-place away from11 contributes
at least \(m-1>0\) to (DO32.14), because
\(o_P\le10\). This is compatible with the
coefficient primitivity of every \(f_Y\):
coefficient primitivity and a unimodular
restricted pairing are different conditions.

Apply the already proved detector calculation
AM-R-002 to this specified finite lattice.
For an individual basis vector \(f_Y\), its
pairing ideal against this same lattice is
exactly \(\kappa R\). Its dual vector within
this span is \(\kappa^{-1}f_Y\), with exact
denominator valuation \(v_{11}(\kappa)\)
and complex norm \(\kappa^{-1/2}\).
With the Hermitian pairing linear in its first argument,
the orthogonal projector onto the whole span is
\[
 \Pi_{\mathrm{term}}
 =\kappa^{-1}\sum_{Y\in\overline{\mathcal Y}}
                  f_Y\langle\,\cdot\,,f_Y\rangle_f.
 \tag{DO32.16}
\]
It has that exact denominator on the ambient
finite function lattice, with its volume
normalizations retained. To see that the
upper bound is attained, factor the space into
the fixed upper/T vector and its full last-row
Fourier subspace. A unit-valued coordinate
of the fixed factor gives a unit numerator
in its rank-one projector. The last-row
projection has unit denominators at11.
Its diagonal at an allowed last-row position
is a p-power unit. Hence no smaller11-power
can clear the displayed projector.

This is a restriction on a detector required
to remain in this terminal finite span or
on its orthogonal projector. It is not a
denominator lower bound for every detector
in the entire finite oscillator. Since the
span is saturated, an integral functional
on it can extend to the ambient coefficient
module; that extended functional need not
be represented by an integral vector in
this same orthogonal subspace. Nor is
the global MainX detector lattice already
identified with this finite span.

## 5. Exact effect of applying a theta operator

Let T denote any fixed actual selected theta
operator out of this finite input space, with
the other archimedean and automorphic inputs
fixed and their actual measures retained. Use the source
Hermitian convention, linear in the first argument.
Equations (DO32.12) and (DO32.16) give the
genuine adjoint identity
\[
 T\Pi_{\mathrm{term}}T^\dagger
 =\kappa^{-1}
    \sum_{Y\in\overline{\mathcal Y}}
          (Tf_Y)\langle\,\cdot\,,Tf_Y\rangle.
 \tag{DO32.17}
\]
Restrict the target to the finite-dimensional image of the
finite input window, so every linear scalar detector has
a Riesz adjoint. For any such detector \(\ell\), this says
\[
 \sum_Y|\ell(Tf_Y)|^2
 =\kappa\,
   \|\Pi_{\mathrm{term}}T^\dagger\ell^\dagger\|^2.
 \tag{DO32.18}
\]
This is exact positivity and finite Plancherel,
including its scalar. It proves nonvanishing
of one actual allowed Y precisely when the
displayed projected adjoint is nonzero.

The new calculation fixes the projection,
its rank, Gram and arithmetic denominator.
It does not assert that a prescribed prior
theta image has nonzero projection to this
finite span. A zero projected adjoint is
still possible; the source's local types
and arithmetic row must decide it.
Likewise the actual terminal mass equation
uses class stabilizers, branching maps and
the specified row pairing. Substituting
the finite Gram scalar for that global
identity would be unjustified.

The calculation therefore removes a concrete
finite Fourier and normalization ambiguity,
and supplies a computable factor for a future
matching proof. It does not replace the
remaining selected-image or terminal-mass
equation by the mere fact that xiLast is
a nonzero function.

## Review status

Author whole-proof review: PASS, 2026-11-21T23:28:15.931357+00:00.
The complete saved proof was read; source-linear-first
Hermitian rank-one operator notation was corrected during
that review. Exact quotient/radical, Gram, saturation,
projector denominator and theta-adjoint scope checked.
Independent review remains separate; no Lean build claimed.
