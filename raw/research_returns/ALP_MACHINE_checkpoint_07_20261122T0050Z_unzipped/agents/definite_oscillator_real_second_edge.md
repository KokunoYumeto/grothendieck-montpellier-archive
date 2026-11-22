# AM-DO-023: exact honest-splitting weights and a specified second-edge vanishing

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`;
inherited reasoning effort not separately exposed; 21 November 2026 UTC.

The first theta lift in ALP-LIFT-09 is nonzero. The assertion below is
that its displayed archimedean type does not survive one **specified**
next positive-definite Hom theta edge with trivial splitting characters.
It does not assert vanishing for every second edge, for an arbitrarily
changed conjugation or polarization, for a changed character, or for a
doubled Gram kernel. This calculation is over the original host
\(E=\mathbf Q(\zeta_7)\), as is ALP-LIFT-09. AM-DO-022 instead
uses \(E'=\mathbf Q(\zeta_{28})\); the two are not combined into one
tower without an additional extension-of-field comparison.

## 1. Conventions and the exact local formula

At a real CM place put \(S=\mathbf C^a\), \(T=\mathbf C^b\),
with their positive identity Hermitian forms. Let \(\kappa>0\).
The symplectic space is \(\operatorname{Hom}_{\mathbf C}(S,T)\),
with form

\[
 b(X,Y)=-2\operatorname{Re}
          (i\kappa\operatorname{tr}(Y^*X))
       =2\kappa\operatorname{Im}\operatorname{tr}(Y^*X),
 \tag{DO23.1}
\]

and group action \(A(g,h)X=hXg^{-1}\). Use
\(\psi(t)=e^{2\pi it}\) and the covariance

\[
 \omega(g,h)\rho(X)\omega(g,h)^{-1}=\rho(hXg^{-1}).
 \tag{DO23.2}
\]

Use the source convention for the honest unitary splitting: a change
of the two character labels acts by
\(\nu_{\Delta\chi_T}(\det g)^{-1}
  \nu_{\Delta\chi_S}(\det h)\), where
\(\nu_\chi(z/\bar z)=\chi(z)\).
This is the convention in `LocalNewformFunction.splitFacO`, line 51,
and AM-DO-022. Write its character labels as

\[
 \chi_S(z)=(z/\bar z)^{m/2},\quad m\equiv a\pmod2,
 \qquad
 \chi_T(z)=(z/\bar z)^{m'/2},\quad m'\equiv b\pmod2.
 \tag{DO23.3}
\]

Let \(\mathcal F=\operatorname{Sym}(T\otimes S^*)\) be the
positive holomorphic Fock space, including its Gaussian vacuum. Then
the **actual honest-splitting action** is

\[
 \boxed{\mathcal F\big|_{U(S)\times U(T)}
   =\det_S^{(-m'-b)/2}\boxtimes\det_T^{(m+a)/2}
                       \otimes\operatorname{Sym}(T\otimes S^*).}
 \tag{DO23.4}
\]

Here the integer powers are legitimate precisely because of the parity
conditions in (DO23.3). The exponent \(m/2\) in the character on
\(\mathbf C^\times\) must not be confused with a determinant power
on \(U(b)\): the latter includes the additional \(a/2\) vacuum
shift. For instance an odd-dimensional opposite space requires an
honest splitting of the metaplectic circle extension, while the bare
oscillator by itself only acts on the determinant double cover.

### Primary-source identification

Konno and Konno (2007), §3.1, printed pp.43–44, use a Hermitian space
\(V\) linear in the second variable and a skew-Hermitian space
\(W\) linear in the first variable, with symplectic form

\[
 \operatorname{Re}((v,v')\overline{\langle w,w'\rangle}).
 \tag{DO23.5}
\]

Take their \(V\) to be the positive target of rank \(b\), and
their \(W\) to have coefficient \(-2i\kappa I_a\), hence
signature \((p',q')=(0,a)\). Formula (DO23.5) becomes (DO23.1)
entry by entry: \(\operatorname{Re}(2i\kappa\bar X Y)
 =2\kappa\operatorname{Im}(X\bar Y)\).
Their matrix right action, equation (3.1), is
\(X.\iota(h,g)=h^{-1}Xg\). Their Schrödinger representation
satisfies covariance with the inverse of this right action. This can
be checked directly from their §2.1 formula
\(\omega(a)\phi(x)=|\det a|^{1/2}\phi(xa)\): conjugation sends
translation by \(y\) to translation by \(ya^{-1}\).
Thus their group arguments \((h,g)\), without inverting either
group argument, give exactly (DO23.2).

There is a necessary character-label conversion. Konno and Konno's
pair is
\[
                       (\xi,\xi')=(\chi_S,\chi_T^{-1}).
\tag{DO23.5a}
\]
Their source splitting changes by \(\nu_{\Delta\xi'}(\det g)\),
whereas the source convention fixed above changes by its inverse.
This can be read directly from the character factor
\(\xi'(\det a)\) in the doubled source formula (3.10), printed
p.48; the same positive determinant convention is stated for the
zero-dimensional opposite member immediately above Lemma 3.1.
Thus §4.1's source exponent is \(-m'\), not \(m'\).
This is a conversion of splitting labels; no inversion of the group
argument or change of the already verified Heisenberg action is made.
Since \(d\psi=2\pi i\), one has \(d\psi\cdot i<0\).
Proposition 4.4(ii), printed pp.68–69, gives on the positive target
block the scalar \((m+q'-p')/2=(m+a)/2\), together with the
standard creation action. On the negative source block it gives the
scalar \((-m'+q-p)/2=(-m'-b)/2\), together with the dual creation
action. Lemma 5.2(i), printed p.73, exponentiates these formulas to
the compact groups. This proves (DO23.4) with the fixed standard
Harris–Kudla–Sweet splitting, rather than merely determining it up to
a determinant character.

As a direct sign check, in one normalized real coordinate the operators
\(D_A=-2\pi ix\), \(D_B=-\partial_x\) implement the Heisenberg
action used in (DO18.5). The rotation generator for multiplication by
\(e^{i\theta}\) is
\(L=-i\partial_x^2/(4\pi)+i\pi x^2\); it has vacuum eigenvalue
\(i/2\) on \(e^{-\pi x^2}\). The creation operator has commutator
\([L,r]=ir\). This confirms the positive target polynomial sign;
the exact determinant-character shift is supplied by the preceding
primary formula, not inferred from this sign check alone.

## 2. The first lift's exact target types

Use the actual Jacobian \(J\), its CM type \(\Phi=\{1,2,3\}\),
and the splitting chosen in ALP-LIFT-09. At each of the three selected
embeddings the element
\(\xi=(\zeta_7-\zeta_7^{-1})/7\) is a positive multiple of \(i\).
Thus its negative skew coefficient has the sign in (DO23.1) at every
selected place. The character \(\chi_S=\mu_E\) has exponents

\[
                             (m_1,m_2,m_3)=(-1,-1,+1).
 \tag{DO23.6}
\]

Indeed \(\mu_E=\mu_-\circ N_{E/\mathbf Q(\sqrt{-7})}\), and
\(\mu_{-,\infty}(z)=|z|/z\). The embeddings 1 and 2 restrict to
the chosen imaginary-quadratic embedding, whereas 3 restricts to its
conjugate; the latter reverses the exponent. This is also immediate
from the quadratic residues \(\{1,2,4\}\pmod7\).

For the first edge \(a=1,b=2\), (DO23.4) gives the target vacuum
characters

\[
                         1,\qquad1,\qquad\det_{U(2)}.
 \tag{DO23.7}
\]

ALP-LIFT-09's explicit nonzero vector applies \(\partial_1\partial_3\)
in each of the two ordinary Jacobian factors. Therefore its total
Fock degrees at the three selected CM places are \((2,0,2)\).
In a rank-one source oscillator, the degree-\(d\) target polynomial
space is \(\operatorname{Sym}^d\mathbf C^2\), an irreducible
\(U(2)\)-module. The monomial with one creation in each of the two
coordinates is a nonzero vector in \(\operatorname{Sym}^2\), even
though it is not a highest-weight vector. Hence the target compact
module containing the first lift is exactly

\[
  \operatorname{Sym}^2\mathbf C^2\ \boxtimes\ \mathbf1\
       \boxtimes\left(\det\otimes\operatorname{Sym}^2\mathbf C^2\right),
 \tag{DO23.8}
\]

with dominant highest weights

\[
                              (2,0),\qquad(0,0),\qquad(3,1).
 \tag{DO23.9}
\]

The actual theta map is equivariant for right translation on target
automorphic functions: \(R_h\vartheta_\phi=\vartheta_{\omega(h)\phi}\).
The source torus integral preserves this equivariance because the two
unitary actions commute. It is nonzero on the displayed irreducible
compact module, by the exact identity value in ALP-LIFT-09. Its kernel
is an invariant submodule, hence is zero on that module. Thus
(DO23.8) is a type of the actual nonzero automorphic first image, not
merely a formal polynomial type before taking theta.

ALP-LIFT-09 labels its tensor source torus by direct multiplication
\(t\). Identifying it with the Hom source can use \(g=t^{-1}\).
This changes the source eigencharacter \(\beta\) by inversion. It
does not change the target group, the opposite skew form, \(\mu_E\),
or (DO23.7)–(DO23.9). The first-lift statement defined \(\beta\)
by its actual action, so it is unaffected by this relabeling.

## 3. Vanishing for the unchanged positive Hom second edge

Now fix a second edge with source the positive \(U(2)\), target
the positive \(U(4)\), the same positive-complex Hom convention
(DO23.1)–(DO23.2), and \(\chi_S=\chi_T=1\). Formula (DO23.4)
restricts its source Fock representation to

\[
           \det_{U(2)}^{-2}\otimes
                    \operatorname{Sym}(\mathbf C^4\otimes(\mathbf C^2)^*).
 \tag{DO23.10}
\]

Every irreducible source type is of the form
\(\det^{-2}\otimes S_\lambda((\mathbf C^2)^*)\), where
\(\lambda=(\lambda_1\ge\lambda_2\ge0)\). Its dominant highest
weight is

\[
                         (-2-\lambda_2,-2-\lambda_1).
 \tag{DO23.11}
\]

For completeness, this follows by decomposing each homogeneous
polynomial degree under the compact group, or by the polynomial
Schur decomposition. Dualization reverses and negates the two dominant
weights; twisting by \(\det^{-2}\) subtracts 2 from each. In
particular both entries in (DO23.11) are at most \(-2\).
None of the weights in (DO23.9) occurs; the second selected CM place
alone already excludes the trivial \((0,0)\) type.

This proves that the actual first compact module (DO23.8) has zero
local theta image under this specified second oscillator. It also
proves the global theta integral is zero for every Schwartz input at
that second edge, using the convention
\(\int\vartheta(g,h)\overline{f(g)}\,dg\).
One elementary global justification is to average first over the
compact real source group. Its Haar average is the orthogonal
projection onto matching compact types. The theta kernel's source
types lie in (DO23.11), and \(f\)'s type is (DO23.9), so that
projection is zero. The compact averaging can be inserted by right
invariance of Haar measure. The definite automorphic quotient is
compact, so no regularization or exchange of divergent integrals is
involved.

The conclusion remains true for the contragredient of (DO23.8) at
this unchanged edge: the second selected place is still trivial,
which is absent from (DO23.10). Changing the source splitting
character, changing the sign/polarization of the edge, or using a
different coefficient module changes the displayed spectrum and must
be analyzed separately. In particular a Gram composition with the
adjoint theta operator is a different construction; it can detect the
first image and is not ruled out by this calculation.

The recovered source uses the bilinear convention
\(\int\vartheta(g,h)f(g)\,dg\) for `liftT`, as stated in
`Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/WittSmallGroupEmbeddingMemPointwiseStabilizerIso.lean`,
`liftT_apply`, lines 160–167. It therefore tests the contragredient
of the input type against the source oscillator. The preceding
trivial-place argument also proves vanishing for this exact source
convention at the specified unchanged edge. It must be used when
comparing a general chain's nontrivial characters and coefficients;
one cannot transfer the conjugated-input matching rule unchanged.

## 4. A quantitative necessary shift, without asserting a global repair

If the second edge keeps its Hom geometry but has target character
\(\chi_T(z)=(z/\bar z)^{m'/2}\), in the source character convention,
its source vacuum exponent is \(c=(-m'-4)/2\). Its source dominant weights are
\((c-\lambda_2,c-\lambda_1)\). A given dominant weight
\((r,s)\), \(r\ge s\), occurs in this polynomial model if and
only if \(c\ge r\): choose \(\lambda=(c-s,c-r)\).
Thus the types (DO23.9) require respectively

\[
                             m'_1\le-8,\qquad
                             m'_2\le-4,\qquad
                             m'_3\le-10.
 \tag{DO23.12}
\]

These are exact local occurrence conditions for this source module.
They are not a construction of a global automorphic splitting character
with those infinity types, and do not prove finite occurrence or
global nonvanishing for the repaired second lift. A global character
would also have to satisfy rational-unit and finite-level compatibility.
The unchanged even-rank trivial characters have \(m'_i=0\) and fail
all three inequalities.

**Correction record.** An earlier version identified Konno's
\(\xi'\) with the source label \(\chi_T\), overlooking the
inverse in `splitFacO`. It consequently had \((m'-b)/2\) in
(DO23.4) and the reversed conditions in (DO23.12). Equations
(DO23.4), (DO23.5a), and (DO23.12) now use the source convention
consistently. The actual first target types and the unchanged
\(\chi_T=1\) second-edge vanishing were unaffected by that error.

## Primary reference

Konno, T., & Konno, K. (2007). On doubling construction for real unitary
dual pairs. *Kyushu Journal of Mathematics, 61*(1), 35–82.
https://doi.org/10.2206/kyushujm.61.35
Primary PDF: https://www.jstage.jst.go.jp/article/kyushujm/61/1/61_1_35/_pdf
Exact locators: §2.1, printed pp.37–38, Heisenberg and covariance
convention; §3.1, pp.43–44, forms and equation (3.1); §3.3, pp.47–48,
honest splittings; §4.1, p.49, character exponents; Proposition 4.4(ii),
pp.68–69, exact Fock operators; Lemma 5.2(i), p.73, compact action.
The paper's displayed last page is 82; an external metadata entry
listing 85 is not used for the page range.

Carried first-lift construction: ALP-LIFT-09, especially (V7)–(V11),
(V18)–(V26), and (V32), with the independent whole-proof check already
recorded in `definite_oscillator_CHECK_EVENTS.tsv`.
