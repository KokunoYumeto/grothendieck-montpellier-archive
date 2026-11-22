# ALP-LIFT-12 — an actual second definite lift of every repaired first-image vector

Author: /root/lift_accounting, GPT-6 Astra Pro, ALP_MACHINE,
21 November 2026 UTC.

This result proves nonvanishing for an actual second classical theta
correspondence. Its second Schwartz function is allowed to vary through
the full oscillator representation. It does not identify that function
with a prescribed source moved kernel, and it supplies no second-output
integral content or DP44 height bound.

## 1. Statement and integral conventions

Set
\[
 E=\mathbf Q(\zeta_7),\qquad F=E^+,\qquad
 T=U(1),\quad G=U(I_2),\quad H=U(I_4).
 \tag{S1}
\]
The positive Hermitian forms and the corresponding skew forms use
the Hom convention already fixed in ALP-LIFT-09 and AM-DO-023.
In particular both groups in (S1) are compact at every real place.
Use the actual rationally compatible first oscillator and the
globally unitary splitting characters of ALP-LIFT-09.

Let \(F_1\ne0\) be any finite sum of the actual first theta vectors
constructed there, allowing finite Schwartz translations and finitely
many holomorphic Fock polynomials as in ALP-LIFT-10. Equivalently,
one may start with a finite sum of first theta lifts of unitary
automorphic characters of \(T\) using these polynomial Fock vectors.
The source torus input may be the finite projector of ALP-LIFT-10:
its finite character decomposition is included in this definition.

Use the one fixed global character of ALP-LIFT-11,
\[
 \gamma=\gamma_{(2,2,1)},\qquad
 F_1^+(g)=\gamma(\det g)F_1(g).
 \tag{S2}
\]
This is an actual first theta vector for the repaired first splitting.
It has the same identity value and the same scalar automorphic norm.
At a real place with original polynomial degree \(d_i\), its compact
type has highest weight
\[
 (d_i+2,2),\qquad
 (\pi_i^+)^\vee=\det^{-2}\operatorname{Sym}^{d_i}(\mathbf C^2)^*.
 \tag{S3}
\]
These assertions are ALP-LIFT-11, (R23)–(R26), not new character
or real-weight claims in this note.

For the second edge take the actual standard oscillator for
\(G\times H\), with both splitting characters equal to \(1\).
The assertion is:

**Theorem.** There is a genuine global Schwartz function \(\psi\)
in this second oscillator representation for which
\[
 \Theta^{\mathrm{bil}}_{2,\psi}(F_1^+)(h)
   :=\int_{G(F)\backslash G(\mathbf A_F)}
                \vartheta_{2,\psi}(g,h)F_1^+(g)\,dg
 \quad\text{is not identically zero.}
 \tag{S4}
\]
This holds for each specific nonzero vector \(F_1^+\), including a
nonzero sum across automorphic multiplicity spaces. A target translate
of \(\psi\) can make the resulting value at \(h=1\) nonzero.

Formula (S4) is bilinear, as is the literal source liftT_apply.
Gan–Qiu–Takeda use the conjugated-input convention
\(\int\vartheta(g,h)\overline{f(g)}\,dg\).
We therefore apply their formula to \(f=\overline{F_1^+}\), in the
contragredient representation. This change is necessary; applying
their compact-type criterion directly to \(F_1^+\) would reverse
the relevant source type.

## 2. Temperedness of the actual first constituents

First fix one unitary torus character contributing to \(F_1\) and
one irreducible automorphic constituent of its first image.
Projection to this constituent is an equivariant map from the
actual first oscillator. Localizing that map shows that each local
constituent occurs as a quotient in the corresponding local theta
correspondence. This is the usual local equivariance of the theta
integral: right translation in one local group can be moved onto
the same local Schwartz factor, while integration in the source
torus supplies its local character. No assertion about a formal
free thetaG parameter is involved.

At a nonsplit finite place, the source is a unitary character of
the compact group \(U(1)\). Its one-dimensional Langlands parameter
has bounded Weil image. Gan and Ichino, Theorem 4.4(i)(a),
(ii)(b), printed p. 14, give the parameter of any nonzero
almost equal rank lift:
\[
 \phi_{\mathrm{first}}
       =(\phi_T\otimes\chi_V^{-1}\chi_W)\oplus\chi_W .
 \tag{S5}
\]
Every character in (S5) is unitary. Hence this parameter is
tempered, and so is its local representation. The two cases of
that theorem cover both the presence and the absence of the
distinguished character in \(\phi_T\); only an already nonzero
first image is being considered. Theorem 4.4(iii) also says that
the nonzero big theta lift of this tempered source is irreducible.
The bounded-parameter/tempered-representation equivalence is
the same paper's section 2.

At a split finite place the pair is of type
\(\mathrm{GL}_1\times\mathrm{GL}_2\).
Mínguez (2008), Theorem 1(2), printed p. 718, says that the
small lift has parameter
\[
                  \phi_T^\vee\oplus 1
 \tag{S6}
\]
in the standard type-II normalization. Changing the honest
splitting or the source convention only introduces unitary
characters and, where appropriate, a contragredient. Thus (S6)
is again bounded. The uniqueness assertion in Theorem 1(1)
ensures that an irreducible quotient arising from the actual
global first theta integral has this small-theta parameter.
This argument includes split dyadic places.

The twist in (S2) is unitary at every place. Taking a
contragredient also preserves temperedness. Consequently every
finite local constituent of the conjugated input for (S4) is
tempered. At real places the group is compact, so its irreducible
unitary representations are tempered. We have proved:
\[
 \text{Every irreducible constituent of }\overline{F_1^+}
       \text{ is tempered at every place.}
 \tag{S7}
\]
For a sum of torus characters, apply the same argument to each
summand before decomposing into irreducible target constituents.
It does not require that the original projector be one character.

## 3. Every finite local constituent occurs on the second edge

### 3.1. The four-dimensional target form is hyperbolic locally

At a nonsplit unramified finite place, the norm map on units of
the unramified quadratic extension is surjective. In particular
\(-1=N(z)\) for a unit \(z\), and \((1,z)\) is isotropic in
\(I_2\). Thus \(I_2\) is hyperbolic and \(I_4\) is the sum of two
hyperbolic planes.

For \(E/F\) in (S1), the only relative ramified finite place is
above \(7\). At that place choose \(b\in\mathbf Q_7\) with
\(b^2=-5\) and \(b\equiv3\pmod7\); Hensel's lemma applies because
\(3^2+5\equiv0\pmod7\) and the derivative \(6\) is a unit.
In \(I_4\) the two vectors
\[
                 u=(1,2,b,0),\qquad v=(0,-b,2,1)
 \tag{S8}
\]
are linearly independent and have zero self-pairing and zero
mutual pairing. They span a two-dimensional isotropic subspace.
Since \(I_4\) is nondegenerate, it is hyperbolic.
This proves the required target assertion at every nonsplit
finite place without an integral classification assertion.
At a split place the second pair is simply
\(\mathrm{GL}_2\times\mathrm{GL}_4\).

### 3.2. A direct quotient at nonsplit places

Let \(k=F_v\), \(L=E_v\) be a nonsplit finite extension, and
write the hyperbolic target as \(X\oplus X^*\), with
\(\dim_LX=2\). The second Schrödinger model is
\[
                    \mathcal S(X\otimes_L W)
                       \simeq\mathcal S(M_2(L)),
 \tag{S9}
\]
where \(W\) is the two-dimensional source space.
The source group preserves this position space. Its action is
right or inverse-right change of variables, depending on the
matrix identification, times a smooth unitary character.
The absolute determinant multiplier is one on \(U(W)\).
Either right-action convention gives the following same
quotient conclusion after inversion.

The orbit of the identity matrix is \(U(W)(k)\), and it is
closed in \(M_2(L)\). Indeed it is cut out by the equation
\(g^*Jg=J\) for a nonsingular matrix \(J\); that equation
already forces \(g\) to be invertible. Restriction therefore
gives an equivariant surjection
\[
 \mathcal S(M_2(L))\longrightarrow C_c^\infty(U(W)(k)),
 \tag{S10}
\]
with the same character twist.

Here is the surjectivity detail. If \(C\) is a compact open
subset of the closed orbit, its complement in the orbit is
closed in the ambient space. Each point of \(C\) has a compact
open ambient neighborhood avoiding that complement. Finitely
many such neighborhoods cover \(C\); their union intersects the
orbit in exactly \(C\). A compactly supported locally constant
function on the orbit has a finite partition into such sets.
Extending their characteristic functions, and disjointifying
the finitely many ambient neighborhoods, extends that function
to an element of the ambient Schwartz space.

Every irreducible smooth representation \(\pi_v\) is a quotient
of the right regular representation \(C_c^\infty(U(W)(k))\).
For a nonzero smooth vector \(a\in\pi_v\), the map
\[
 f\longmapsto\int_{U(W)(k)} f(g)\pi_v(g^{-1})a\,dg
 \tag{S11}
\]
is equivariant for right translation. Taking the normalized
indicator of a compact open subgroup fixing \(a\) shows that
the map is nonzero. Irreducibility makes it surjective.
The group is unimodular, so the substitution in this
equivariance calculation introduces no modular character.
A character twist of the regular representation has the same
quotient property.

Equations (S10) and (S11) prove
\[
                  \operatorname{Hom}_{G(k)}
                          (\omega_{2,v},\pi_v)\ne0
 \tag{S12}
\]
for every irreducible smooth \(\pi_v\), in particular every
constituent in (S7). This is a quotient argument, not an
inference from a subquotient of an open-orbit submodule.

### 3.3. Split places

At a split place use Mínguez, Theorem 1(2), with \(n=2,m=4\).
It states directly that
\(\operatorname{Hom}_{\mathrm{GL}_2}(\omega_{2,4},\pi_v)\ne0\)
for every irreducible smooth \(\pi_v\), over a nonarchimedean
field of any residue characteristic. Unitary splitting
characters or a group automorphism do not change this
all-representations assertion.

The nonsplit closed-orbit proof must not be copied verbatim
here: the full-rank \(\mathrm{GL}_2\) orbit is not closed in
the whole matrix space. Its regular quotient from an open
submodule alone would not establish a quotient of the full
oscillator. The cited type-II theorem closes precisely that
point.

## 4. The real local doubling factor is explicitly nonzero

By (S3), each real component of the conjugated input has type
\[
 \pi_i=\det^{-2}\operatorname{Sym}^{d_i}(\mathbf C^2)^*,
                     \qquad \dim\pi_i=d_i+1.
 \tag{S13}
\]
AM-DO-023 and ALP-LIFT-11 show that this exact type occurs in
the second positive Hom oscillator with trivial splitting
characters. Choose an isometric \(U(2)\)-equivariant embedding
\(\iota:\pi_i\hookrightarrow\omega_{2,i}\), a unit vector \(a\),
and \(\phi=\iota(a)\). Such a vector is a polynomial times a
Gaussian and is an actual Schwartz vector.

For the doubled oscillator, Gan–Qiu–Takeda, section 11.3,
printed p. 52, give the equivariant map \(\delta\) normalized
by evaluation at zero:
\[
              \delta(\phi_1\otimes\overline{\phi_2})(0)
                         =\langle\phi_1,\phi_2\rangle .
 \tag{S14}
\]
Their possible determinant character is trivial here because
the second target splitting character is \(1\).
Consequently its Siegel–Weil section at \(s_0=1\) satisfies
\[
 \Phi_\delta(g,1;1)
       =\langle\omega_{2,i}(g)\phi,\phi\rangle
       =\langle\pi_i(g)a,a\rangle .
 \tag{S15}
\]
Their local zeta integral in section 11.6, printed p. 54,
uses the complex conjugate of the input matrix coefficient.
The bars in these two formulas have been checked on rendered
PDF pages; the plain-text extraction drops them.
Thus Schur orthogonality gives the exact value
\[
 \begin{split}
 Z_i(1,\Phi_\delta,a,a)
    &=\int_{U(2)}
          |\langle\pi_i(g)a,a\rangle|^2\,dg\\
    &=\frac{\operatorname{vol}(U(2))}{d_i+1}>0.
 \end{split}
 \tag{S16}
\]
In the GQT normalization this yields
\[
 Z_i^*(1,\Phi_\delta,a,a)
   =\frac{\operatorname{vol}(U(2))}
      {(d_i+1)L_i(3/2,\pi_i)}\ne0 .
 \tag{S17}
\]
The standard local factor of a tempered representation is
holomorphic and nonzero in \(\operatorname{Re}s>0\); the precise
doubling-factor version is Lapid–Rallis, Proposition 5,
also invoked in Gan–Ichino, section 6.7, printed p. 27.
For these compact real groups the factors are the usual
nonvanishing gamma factors.

This direct compact calculation is needed. GQT Theorem 11.7's
general converse does not cover arbitrary definite real unitary
groups at \(m=2n\). We are not applying that converse without
its extra hypotheses; (S16) proves its required local
nonvanishing in the present actual compact types.

## 5. The global \(L\)-value and the Rallis hypotheses

Let \(\pi\) be an actual irreducible cuspidal subrepresentation
of the space generated by \(\overline{F_1^+}\), with its actual
embedding in automorphic functions. By (S7), its unramified
Satake parameters have absolute value one. Hence the partial
standard Euler product at \(s=3/2\) is absolutely convergent
and nonzero: the logarithms are bounded by a fixed-degree
multiple of
\[
       \sum_{\mathfrak p}\sum_{r\ge1}
              \frac{N\mathfrak p^{-3r/2}}r<\infty.
 \tag{S18}
\]
At a split place this can be viewed as the product over the
two primes of \(E\). Enlarging the finite exceptional set
has no effect on this conclusion. The finitely many remaining
standard local factors are holomorphic and nonzero at \(3/2\)
by the same tempered doubling-factor property used in (S17).
Thus the completed factor in GQT is
\[
                           L(3/2,\pi)\ne0 .
 \tag{S19}
\]
There is no central-value nonvanishing conjecture in (S19).
In particular one must not substitute \(L(1/2,\pi)\) for this
evaluation point.

For clarity, one can avoid any ramified local-LLC factor
identification in the last paragraph. GQT Theorem 11.4(ii)
itself gives holomorphy of the completed factor once all local
theta lifts are nonzero, which has been proved in sections
3–4. Its local factors have no zeros; its partial unramified
product is nonzero by (S18). These facts also give (S19).
The tempered local-factor property is a direct stronger check.

The target \(I_4\) is positive definite at every real place,
so it is anisotropic over \(F\). Its global Witt index is
\(r=0\), even though its finite local Witt indices are two.
The parameters of GQT Theorem 11.4 are exactly
\[
 \epsilon_0=0,\quad n=2,\quad m=4,\quad d(n)=2,\quad
 r=0,\quad s_{m,n}=(m-n)/2=1.
 \tag{S20}
\]
Thus \(d(n)<m\le2d(n)\), \(r\le n\), and
\(0<s_{m,n}\le d(n)/2\). The lower-tower vanishing assumption
for \(j<r\) is empty. Both automorphic quotients are compact;
all their automorphic forms are cuspidal because the groups
have no proper rational parabolic subgroups.

At every finite place, (S12) and the split theorem give local
theta occurrence. GQT Proposition 11.6(i), printed p. 55,
then gives the nonzero normalized local zeta functional.
At every real place the same conclusion follows from (S17).
GQT Theorem 11.4(ii), printed p. 54, and (S19) therefore imply
that the second global theta lift of this actual cuspidal
embedding of \(\pi\) is nonzero.

With the paper's Haar and Petersson normalizations, its
identity is
\[
 \langle\Theta_{2,\psi_1}(f_1),
                    \Theta_{2,\psi_2}(f_2)\rangle
       =2\,L(3/2,\pi)
          \prod_v Z_v^*(1,\psi_{1,v}\otimes
                    \overline{\psi_{2,v}},f_{1,v},f_{2,v}).
 \tag{S21}
\]
Replacing these measures by probability measures introduces
the corresponding positive quotient-volume factors. No such
factor has been silently assigned the value one in a height
or norm budget. The archimedean factors (S16) are explicit;
the finite test functions supplied by local nonvanishing
have not been optimized or bounded arithmetically.

## 6. Why every specified first vector survives, including multiplicities

It remains to pass from constituent nonvanishing to the
assertion about each specified \(F_1^+\).
Let \(\mathcal A\) be the closed \(G(\mathbf A_F)\)-submodule
generated by the finite collection of first vectors in
question, after (S2). Define the common kernel
\[
 \mathcal N=\{F\in\mathcal A:
          \Theta^{\mathrm{bil}}_{2,\psi}(F)=0
                         \text{ for every }\psi\}.
 \tag{S22}
\]
Equivalently, intersect the kernels of the scalar functionals
\[
 F\longmapsto\int_{[G]}
                    \vartheta_{2,\psi}(g,h)F(g)\,dg
 \quad(\psi,\ h\text{ arbitrary}).
\]
They are continuous on \(L^2([G])\): the quotient is compact
and a fixed theta kernel is a smooth square-integrable
function there. Thus \(\mathcal N\) is closed.
Changing variables in the integral moves right translation
of \(F\) into the source action on \(\psi\), so \(\mathcal N\)
is \(G(\mathbf A_F)\)-invariant.

The compact anisotropic automorphic quotient has discrete
unitary spectrum, with finite multiplicities. A nonzero
closed invariant subspace of such a Hilbert direct sum
contains an irreducible automorphic subrepresentation.
This statement allows a subspace inside a multiplicity
space: it does not assume multiplicity one.
If \(\mathcal N\ne0\), choose such an irreducible copy
\(\pi^+\subset\mathcal N\). Its conjugate copy
\(\overline{\pi^+}\) is an actual cuspidal embedding to
which sections 2–5 apply.

The GQT identity applies to this particular embedding,
with its induced Petersson form. Its factorization can
always be obtained by scaling one local invariant pairing;
that nonzero positive scale cannot change the conclusion.
It gives some \(f\in\overline{\pi^+}\) and \(\psi\) for which
\(\int\vartheta_{2,\psi}(g,h)\overline{f(g)}\,dg\) is nonzero.
But \(\overline f\in\pi^+\subset\mathcal N\), a contradiction.
Therefore \(\mathcal N=0\), proving (S4) for each nonzero
specified first vector, not only for one favorable spectral
projection.

Finally, if its output is nonzero at \(h_0\), replace \(\psi\)
by its target translate \(\omega_2(h_0)\psi\). The value at
the target identity becomes that previous value at \(h_0\).
This does not compute the arithmetic height or denominators
of the translated second Schwartz function.

## 7. Precisely stated transfer to another CM host

The argument is structural over a CM extension \(K/K^+\).
It applies with the same ranks if the following inputs
have actually been supplied:

1. An actual first \(U(1)\to U(I_2)\) theta vector from
   unitary characters and polynomial Fock vectors, with
   globally unitary splitting characters.
2. A globally admissible fixed character twist making each
   real first type \(\det^2\operatorname{Sym}^{d_\tau}\),
   with the same Hom and bilinear integral conventions.
3. The positive form \(I_4\) is hyperbolic at every nonsplit
   finite place.

No torus class-number calculation enters the second-step
proof once input 1 exists. If \(K/K^+\) is unramified at
every finite nonsplit place, input 3 follows immediately
from the norm argument in section 3.1.
AM-R-009 supplies the intended inputs for
\(K=\mathbf Q(\zeta_{28})\): its fixed twist has
\(\mathbf c=(2,1,2,2,1,2)\), and its degree-eight vector
at label9 has the actual first identity value
\((9/4)C^4\). These inputs have now been independently
whole-checked in review_root_unramified_first_lift.md,
retaining the accepted DP57 and DO022 host facts.
Thus there is the concrete corollary
\[
 \exists\psi:\quad
 \Theta^{\mathrm{bil}}_{U(2)\to U(4),\psi}
       (\Theta'_P)\ne0,\qquad
 \Theta'_P(1)=\frac94C^4,
 \tag{S23}
\]
over this same \(E'\), with the actual first source input
of norm one from (R9.27). At infinity the degrees are
\(d_9=8\) and zero at the other five places, so the
unnormalized compact numerator in (S16), multiplied over
all six places, is \(\prod_{\tau}\operatorname{vol}(U(2)_\tau)/9\).
This does not normalize the finite second test functions.
The field and lattice normalizations in this corollary
are the stated \(E'\) data, not an identification of
\(E'\) with the original \(E\) in (S1).

## 8. Remaining gate and costs

This proves a genuine nonzero two-edge composition with
an unrestricted actual second Schwartz input.
For the sharp first coefficients of ALP-LIFT-10, it proves
that the same nonzero first vector is not annihilated by
every second kernel. It does not prove that its second
value has the first coefficient's valuation.

The next arithmetic gate is to choose that second kernel
inside the permitted finite moved family, prove its
integral lattice and content, and bound the actual mass
and archimedean norm of the nonzero pairing. The full
common-character pins, stage row modules, harmonic
branching maps and six terminal identities are also
absent from this two-edge result. In particular the
rank-one starting edge is still not the source's
even-rank StdPair constructor. No shorter DP44 chain
or net DP44 gain is claimed from (S4) or (S21).

## Primary references and exact locators

- Gan, W. T., Qiu, Y., & Takeda, S. (2014).
  The regularized Siegel–Weil formula (the second term identity)
  and the Rallis inner product formula. arXiv:1207.4709v3.
  Section11.2–11.3, printed pp.51–52, the conjugated-input
  integral and doubled Schwartz map; section11.6–11.7,
  printed p.54, normalized local factors and Theorem11.4;
  Proposition11.6(i), printed p.55; Theorem11.7,
  pp.56–57, the real-place caveat deliberately bypassed.
  https://arxiv.org/pdf/1207.4709v3
- Gan, W. T., & Ichino, A. (2015).
  The Gross–Prasad conjecture and local theta correspondence.
  arXiv:1409.6824v2. Section2, bounded parameters and tempered
  representations; Theorem4.4(i)(a), (ii)(b), (iii), printed
  p.14, the almost equal rank parameter and irreducibility;
  section6.7, printed p.27, the exact tempered local
  doubling-factor property of Lapid–Rallis Proposition5.
  https://arxiv.org/pdf/1409.6824
- Mínguez, A. (2008). Correspondance de Howe explicite:
  paires duales de type II. Annales scientifiques de
  l'École Normale Supérieure, 41(5), 717–741.
  Theorem1(1)–(2), printed p.718; Corollary6.3 is its
  later proved version. The theorem includes every
  nonarchimedean residue characteristic.
  https://www.numdam.org/item/ASENS_2008_4_41_5_717_0.pdf
- Lapid, E. M., & Rallis, S. (2005). On the local factors
  of representations of classical groups. In
  Automorphic representations, L-functions and applications:
  Progress and prospects (pp.309–360). De Gruyter.
  Proposition5, used in exactly the form explicitly recorded
  in Gan–Ichino section6.7. The primary Gan–Ichino passage
  was directly read; no independent full reading of the
  Lapid–Rallis chapter is claimed.
  https://doi.org/10.1515/9783110892703.309

Internal dependencies: ALP-LIFT-09, (V22)–(V38);
ALP-LIFT-10, actual finite moved family and source inputs;
ALP-LIFT-11, (R23)–(R26); AM-DO-023, corrected real
source action and the trivial-character second case.
Check events are recorded separately, only after whole
proof readings. This proof has not been formalized in Lean.
