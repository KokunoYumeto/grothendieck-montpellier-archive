# ALP-LIFT-16 — fixed spherical tests, 29-supported single translates, and exact level masses

Author: GPT-6 Astra Pro, ALP_MACHINE /root/lift_accounting, 21 November 2026 UTC. Inherited reasoning effort is not separately exposed.

This result sharpens ALP-LIFT-15 in the actual common \(E'=\mathbf Q(\zeta_{28})\) host. The later finite inputs can all be single norm-one Heisenberg translates supported only at29. The proof includes an exact split-place spherical-vacuum calculation valid in residue characteristic2. The translation depths remain unbounded, and the prescribed raw Xi and prior-image arithmetic lattice are not identified.

The additional quantitative output is an explicit sufficient principal level and its class mass. Its 11-adic valuation is independent of the unknown 29-depth. This does not compute a later gain: the arithmetic entries and their cancellations are separate.

## 1. The split-place vacuum coefficient, with the actual measure

Let \(F\) be any nonarchimedean local field of characteristic zero, with residue cardinality \(q\), uniformizer \(\varpi\), and ring \(\mathcal O\). Put
\[
 G=\operatorname{GL}_a(F),\quad K=\operatorname{GL}_a(\mathcal O),
                    \qquad b>a.
 \tag{S1}
\]
Normalize Haar measure on \(G\) by \(\operatorname{vol}(K)=1\).
At a split place of the common unitary host, AM-DO-020/022 identifies
the actual normalized finite vacuum with
\(\phi_0=\mathbf1_{M_{b,a}(\mathcal O)}\) after the unitary measure
change determined by its lattice. Its \(L^2\) norm is one.
The source action, without its determinant-root character, is
\[
       \omega(g)\phi(X)=|\det g|^{b/2}\phi(Xg).
 \tag{S2}
\]
For a general lattice measure, the normalized characteristic vector
is \(\operatorname{vol}(L)^{-1/2}\mathbf1_L\); its matrix coefficient
is unchanged by the corresponding unitary identification. Thus no
additive-lattice volume is lost in the normalization used here.

Write \(a_\lambda=\operatorname{diag}(\varpi^{\lambda_1},\ldots,
\varpi^{\lambda_a})\), with
\(\lambda_1\ge\cdots\ge\lambda_a\).
A direct intersection-of-lattices calculation gives
\[
 A_b(g):=\langle\omega(g)\phi_0,\phi_0\rangle
       =q^{-b\sum_i|\lambda_i|/2}
                  \quad(g\in Ka_\lambda K).
 \tag{S3}
\]
Indeed the \(i\)-th column lies in
\(\mathcal O^b\cap\varpi^{-\lambda_i}\mathcal O^b\),
of volume \(q^{-b\max(-\lambda_i,0)}\), while the determinant
factor is \(q^{-b\sum_i\lambda_i/2}\).
The formula holds at2 as well as at odd residue characteristic.
It uses the actual split Schrödinger action, not an assumed
integral diagonal/antidiagonal basis for a doubled space.

## 2. A matrix-disintegration proof of the exact spherical transform

Let \(\pi\) be an irreducible unramified unitary representation of
\(G\), let \(m_\pi(g)\) be its normalized spherical matrix coefficient,
and let \(\alpha_1,\ldots,\alpha_a\) be its standard normalized
Satake parameters. Define
\[
 C_{a,b}(q)=\prod_{i=0}^{a-1}(1-q^{i-b}),\qquad
                           s_*=(b-a+1)/2.
 \tag{S4}
\]
We will prove, in the convergence range specified below,
\[
 \boxed{\int_G A_b(g)m_\pi(g)\,dg
        =C_{a,b}(q)L(s_*,\pi)L(s_*,\pi^\vee).}
 \tag{S5}
\]
For a unitary representation the two \(L\)-values at a real point
are complex conjugates. Thus the right side is strictly positive
whenever the factors are finite and nonzero.

### 2.1 Exact full-rank matrix disintegration

For an integer \(B\ge a\), put
\[
             f_B(h)=\mathbf1_{M_a(\mathcal O)}(h)
                                           |\det h|^{B/2}.
\]
Let \(X_0=\binom{I_a}{0}\in M_{B,a}(F)\).
Every full-rank matrix can be written \(kX_0h\), with
\(k\in\operatorname{GL}_B(\mathcal O)\), \(h\in G\).
To see this, intersect its column space with \(\mathcal O^B\).
This intersection is a saturated rank-\(a\) direct summand over
the DVR, so an integral basis extends to a basis of \(\mathcal O^B\);
its change-of-basis matrix is the required \(k\).

With probability Haar measure \(dk\) on
\(\operatorname{GL}_B(\mathcal O)\), matrix Lebesgue measure satisfies
\[
 \int_{M_{B,a}(F)}F(X)\,dX
  =C_{a,B}(q)\int_{\operatorname{GL}_B(\mathcal O)}
        \int_G F(kX_0h)|\det h|^B\,dh\,dk.
 \tag{S6}
\]
The rank-deficient set has measure zero, as follows by induction
and Fubini from the vanishing of a nonzero matrix minor.
Both sides on the full-rank orbit are left compact-invariant
and transform under right multiplication by \(h_0\in G\)
with the same Jacobian \(|\det h_0|^{-B}\).
Uniqueness of a relatively invariant measure on this transitive
homogeneous space makes them proportional. The proportionality
constant is fixed by the open set of matrices whose reduction
has rank \(a\): in the right-hand coordinates this is exactly
\(h\in K\), so the integral without the constant is one.
Its additive measure is
\[
 \frac{\prod_{i=0}^{a-1}(q^B-q^i)}{q^{Ba}}
                 =\prod_{i=0}^{a-1}(1-q^{i-B}).
\]
This proves (S6), including its constant. The homogeneous-space
measure assertion can equivalently be checked in a local minor
chart; the same Jacobian and normalization give (S6).

Using (S6) on the product of two characteristic functions gives
\[
       A_B(g)=C_{a,B}(q)\int_G f_B(hg)f_B(h)\,dh
             =C_{a,B}(q)(\check f_B*f_B)(g),
              \qquad\check f_B(h)=f_B(h^{-1}).
 \tag{S7}
\]
The inverse-argument operator
\(|\det g|^{-B/2}\phi(Xg^{-1})=\omega(g^{-1})\phi(X)\)
has the same vacuum coefficient, since
\(A_B(g^{-1})=A_B(g)\) by (S3). It is not the left action in(S2).

### 2.2 The one-sided spherical zeta integral

With the normalization in (S1), the elementary unramified
Godement–Jacquet calculation is
\[
 \int_G\mathbf1_{M_a(\mathcal O)}(h)|\det h|^z
                     m_\pi(h)\,dh
       =\prod_{i=1}^a
            (1-\alpha_i q^{-z+(a-1)/2})^{-1}.
 \tag{S8}
\]
Replacing \(m_\pi(h)\) by \(m_\pi(h^{-1})\) replaces the
\(\alpha_i\) by their inverses. The product of the two formulas
is therefore independent of this convention.

For an explicit normalization check, use normalized induction from
unramified characters \(\chi_i\), with
\(\chi_i(\varpi)=\alpha_i\), and its spherical vector \(v^\circ\)
satisfying
\(v^\circ(nak)=\delta_B(a)^{1/2}\prod_i\chi_i(a_i)\).
Averaging \(v^\circ(kh)\) over \(K\) gives the normalized spherical
function. Since the matrix indicator and determinant power are
left \(K\)-invariant, that averaging disappears from the integral.
In the Iwasawa integral \(h=nak\), integrality requires
\(a_i\in\mathcal O\) and
\(n_{ij}\in a_j^{-1}\mathcal O\). Integrating these upper
off-diagonal entries contributes
\(\prod_j|a_j|^{-(j-1)}\).
The remaining exponent of each \(|a_i|\) is
\[
          z-\frac{a+1-2i}{2}-(i-1)=z-(a-1)/2.
\]
The \(a\) geometric series give (S8). This calculation is initially
in a half-plane of absolute convergence. The normalized spherical
function is determined by its Satake character, so it applies
also at reducible principal-series parameters, by the usual
spherical-function identity or its continuous specialization.
It is not restricted to generic irreducible representations.

A primary independent locator for precisely this normalization is
Macdonald (1995), ChapterV, section4, equations(4.4)–(4.5),
printed p.301, with the convergence statement immediately following;
his section3 records the inverse convention for the spherical
transform. Thus (S8) is a known formula used with its constant
checked here.

For \(B\) sufficiently large, \(f_B\in L^1(G)\); the spherical
transform is multiplicative on \(K\)-bi-invariant convolution.
Equations(S7)–(S8) give
\[
 \int_G A_B(g)m_\pi(g)\,dg
  =C_{a,B}(q)
     L((B-a+1)/2,\pi)L((B-a+1)/2,\pi^\vee).
 \tag{S9}
\]

### 2.3 Extension and absolute convergence at the actual rank

Put \(r(\lambda)=\sum_i|\lambda_i|\), and introduce an independent
complex variable \(T\). The Cartan sum
\[
 J_\pi(T)=\sum_{\lambda_1\ge\cdots\ge\lambda_a}
   \operatorname{vol}(Ka_\lambda K)m_\pi(a_\lambda)
                                                    T^{r(\lambda)}
 \tag{S10}
\]
is a power series convergent near zero. For all sufficiently large
integers \(B\), (S9) identifies its value at \(T=q^{-B/2}\) with
\[
 R_\pi(T)=
 \frac{\prod_{i=0}^{a-1}(1-q^iT^2)}
      {\prod_{i=1}^{a}
       (1-q^{(a-1)/2}T\alpha_i)
       (1-q^{(a-1)/2}T\alpha_i^{-1})}.
 \tag{S11}
\]
These values accumulate at zero, where both functions are analytic.
The identity theorem therefore proves equality of their power
series near zero, and hence equality wherever the series converges
and the rational function has no pole. This step does not assume
that an identity at infinitely many large real dimensions alone
determines a meromorphic function of the dimension.

For completeness, suppose
\[
                    |\alpha_i|,\ |\alpha_i^{-1}|\le q^s
                        \qquad(1\le i\le a).
 \tag{S12}
\]
Macdonald's explicit spherical formula and double-coset volume
formula give constants \(C,A\), depending on this representation,
such that
\[
 \begin{split}
 |m_\pi(a_\lambda)|
  &\le C(1+r(\lambda))^A q^{-\langle\rho,\lambda\rangle}
                         q^{s r(\lambda)},\\
 \operatorname{vol}(Ka_\lambda K)
  &\le C q^{2\langle\rho,\lambda\rangle},
 \qquad
 \rho=((a-1)/2,(a-3)/2,\ldots,(1-a)/2).
 \end{split}
 \tag{S13}
\]
These estimates follow directly from Macdonald (1995),
ChapterV, (2.9) and (3.4), printed pp.298–299.
For distinct Satake parameters the finite Weyl sum gives the first
bound without the polynomial factor. If parameters coincide,
the apparent denominators cancel; taking the finite-order limits
differentiates monomials \(\alpha^{w\lambda}\), adding only a
polynomial in the integer entries of \(\lambda\). There are finitely
many Weyl terms and finitely many possible coincidences, so a fixed
\(A\) suffices. This explains the bound also at repeated parameters.
The same formula holds after a central shift of \(\lambda\);
the displayed bound uses both inverse and direct parameters.

Since
\(\langle\rho,\lambda\rangle\le(a-1)r(\lambda)/2\),
(S13) proves absolute convergence of (S10) when
\[
                       |T|q^{(a-1)/2+s}<1.
 \tag{S14}
\]
Only polynomially many dominant integer tuples have a given
\(r(\lambda)\), so the geometric decay suffices.

In the actual selected chain let \(a=N_j\), \(b=a+d\), \(j\ge1\).
Formula(E13) of ALP-LIFT-14 and the initial bound(E18) imply
\[
                |\alpha_i|,\ |\alpha_i^{-1}|
                        \le q^{(d-1)/2}.
 \tag{S15}
\]
Indeed the initial rank is \(k<d\), all inserted blocks have
length \(d\), and the finite character values on uniformizers
have absolute value one. Unitarity gives the same bound for
the inverse multiset. A further unramified unitary determinant
twist preserves the bound.

At \(T=q^{-b/2}\), (S14) holds with
\[
                |T|q^{(a-1)/2+(d-1)/2}=q^{-1}.
 \tag{S16}
\]
Thus the actual integral in (S5) is absolutely convergent. Every
denominator in (S11) has its nonconstant term of modulus at most
\(q^{-1}<1\); the numerator is positive since \(b>a-1\).
Substitution gives (S5), with a strictly positive value for unitary
\(\pi\). This proof includes residue characteristic2.

## 3. The actual split Rallis test, including the character ratio

At a split place write the source common character as
\(\mu=(\eta,\eta^{-1})\). Outside29 it is unramified and unitary.
The actual Hom source operator contributes
\(\eta(\det g)^{-1}\), by AM-DO-020/022. AM-DO-028 transports
GQT's conjugated-input convention and dual-source group back to
the literal bilinear integral. Its local matrix coefficient is
therefore that of
\[
                         \widetilde\pi=\pi\otimes\eta^{-1}.
\]
The doubled evaluation identity
\(\delta(\phi_0\otimes\overline{\phi_0})(0)
 =\|\phi_0\|^2=1\)
shows that the section at \((g,1)\) is exactly the actual vacuum
coefficient (S3) with this determinant-root factor. No choice of
integral doubled coordinates is needed for this identity.

Consequently the actual local zeta value is
\[
 Z_v(s_0;\phi_0,\phi_0,v^\circ,v^\circ)
  =C_{a,b}(q)
       L(s_*,\pi\eta^{-1})L(s_*,\pi^\vee\eta),
 \qquad s_0=d/2.
 \tag{S17}
\]
These two factors are exactly the split local standard factor in
the source convention fixed by AM-DO-028. The normalized value is
\[
                            Z_v^*(s_0)=C_{a,b}(q)>0.
 \tag{S18}
\]
If the chosen local group Haar measure gives \(K\) volume \(v_K\)
instead of one, both (S17) and (S18) are multiplied by \(v_K\).
This measure factor is retained. The formula is valid at the
dyadic split places of the actual host; it closes the test-vector
point explicitly left open at the end of ALP-LIFT-15.

## 4. Fixed tests at all other places outside29

At an odd nonsplit finite place, every stage character is trivial
and the actual model is the integral unramified model, as checked
in ALP-LIFT-14 section3. Liu (2021), Lemma6.1, identifies the
doubled lattice characteristic vector with his unramified standard
section. His Proposition5.6 with sign \(+\) gives
\[
 Z_v(s_0)=\frac{L_v(s_*,\pi)}{b_a(s_0)},\qquad
 b_a(s)=\prod_{i=1}^a(1-(-1)^i q^{-2s-i})^{-1}.
 \tag{S19}
\]
The odd residue characteristic makes the diagonal/antidiagonal
lattice change integral, so the doubled product of the actual
unit lattice vacua is this lattice characteristic vector.
The normalization at the identity is one on both sides.
The additive-character rescaling needed at a ramified base-field
place was already carried out in LIFT14 without changing the
composite symplectic character or normalized vacuum.
Therefore the normalized local value is exactly
\[
             b_a(s_0)^{-1}
             =\prod_{i=1}^a(1-(-1)^i q^{-d-i})>0,
 \tag{S20}
\]
again multiplied by \(v_K\) for a different group Haar normalization.

Thus at every finite place outside29 the **actual fixed vacuum**
and the unique spherical source line give a nonzero normalized
local test. All exceptional dyadic places are split and were
treated directly in section3. Almost everywhere these are the
standard factors in GQT equation(11.3), so their global normalized
product converges and is nonzero. At the real places the selected
Schur test remains the exact positive
\(\operatorname{vol}(U(a))/\dim\rho_{j,\tau}\)
of LIFT14(E24). At29 arbitrary finite Schwartz functions remain
available, and GQT Proposition11.6(i) supplies the local tests there.

## 5. Restricting the global nonzero family to29

Let \(\pi\) be any actual cuspidal embedding arising in LIFT14.
At each finite place outside29, \(\pi_v^{K_v}\) is one-dimensional.
The Rallis argument, with the fixed tests of sections3–4,
therefore gives a nonzero lift using spherical source vectors
outside29 and the vacuum there, while varying the Schwartz
function only at29 and in the selected real component.

This yields every-vector nonvanishing on the away-from29 spherical
space, not only one representation-level occurrence. Here are the
multiplicity and cancellation details.

For one global irreducible isomorphism type, its spherical space
away from29 is
\[
   \mathcal M_\pi\otimes\pi_{29}\otimes\rho_j
             \otimes\bigotimes_{v\nmid29,\ v<\infty}\pi_v^{K_v},
 \tag{S21}
\]
where \(\mathcal M_\pi\) is its finite-dimensional actual automorphic
multiplicity space. The remaining \(\pi_{29}\otimes\rho_j\) is
irreducible for \(G(F'_{29})\times G_\infty\), with the product over
the six29 places understood. The joint kernel of the theta family
with all other finite inputs fixed is invariant under this group.
In a finite sum of copies of an irreducible smooth module, a
submodule is of the form \(\mathcal M'\otimes
(\pi_{29}\otimes\rho_j)\). If it were nonzero, a nonzero line in
\(\mathcal M'\) would define an actual global cuspidal embedding
on which all the fixed-away-from29 theta maps vanish.
The Rallis argument of the preceding paragraph applies to that
embedding, giving a contradiction. Hence this joint kernel is zero.

Different global source isomorphism types cannot cancel their
theta images. All target constituents of one source have the
unique local small-theta target. At a nonsplit place outside29
the source is spherical and its Satake multiset is recovered
by subtracting the fixed inserted block in (E12).
At a split place the reciprocal uniqueness in Mínguez's Howe
correspondence gives the same injectivity, including at29.
Thus two inequivalent global sources, whose real types are
already fixed, give inequivalent global targets. Their automorphic
isotypic subspaces are orthogonal. A nonzero image of one source
component therefore cannot be canceled by the others.

Every smooth current vector has a finite spectral decomposition
at its finite level and real type. The preceding two paragraphs
show that every nonzero current vector fixed by the standard
compacts outside29 survives a test varying only at29.
The output is again fixed by those target compacts because the
actual vacuum is fixed by them. Hence this property iterates
from the first vector of AM-R-012.

Now apply the local version of ALP-LIFT-15 to the29-component.
For some finite \(e_j\ge1\), it lies in the depth-\(29^{e_j}\)
window. One basis vector detects the nonzero map. We obtain
\[
 F_{j+1}=
  \Theta_{W_{x_j}\phi_{0,j},\,\phi_{\infty,j}}(F_j)\ne0,
 \quad
 x_j\in29^{-e_j}\Lambda_{29,j}/\Lambda_{29,j},
 \quad
 x_{j,v}=0\ (v\nmid29),
 \quad
 \|W_{x_j}\phi_{0,j}\|_{2,f}=1.
 \tag{S22}
\]
Its infinite translation component is zero. The real vector stays
in the exact selected Schur component. This is a full Heisenberg
orbit, not the prescribed isotropic half-orbit.

## 6. An explicit sufficient level and its exact index

Put \(M=29^e\), and let \(x\in M^{-1}\Lambda_{29}\).
If \(g\) and \(h\) are principal-congruence elements modulo \(M^2\)
in the source and target integral unitary groups, then
\[
                 (g,h)x-x\in M\Lambda_{29}.
 \tag{S23}
\]
This follows from the Hom action \(X\mapsto hXg^{-1}\).
All four position/momentum matrix blocks satisfy the same
integral congruence. Let the displacement be \(\delta\).
The Weyl phase \(B(x,\delta)/2\) is integral because
\(x\in M^{-1}\Lambda_{29}\), \(\delta\in M\Lambda_{29}\),
the pairing is integral on the lattice, and29 is odd.
The trace-one character of \(\delta\) is one at29.
Thus \(W_{x+\delta}\phi_0=W_x\phi_0\) exactly.
The common splitting character has conductor dividing29 and
is one on the same principal subgroups. Covariance therefore
shows that the whole translated finite vacuum is fixed by
these source and target levels.

For rank \(n\), let \(K_n(M^2)\) be principal congruence modulo
\(29^{2e}\) at all six split29 places and the standard compact
elsewhere. Its exact index is
\[
 \begin{split}
 I_n(M^2)&=[K_{n,0}:K_n(M^2)]\\
 &=29^{6n^2(2e-1)}
                  |\operatorname{GL}_n(\mathbf F_{29})|^6\\
 &=29^{12en^2}\prod_{i=1}^n(1-29^{-i})^6.
 \end{split}
 \tag{S24}
\]
Therefore (S22) has an explicit sufficient target level of this
form. The exponent \(e_j\) has not been bounded in terms of the
selected degree.

Every rational class stabilizer at \(K_n(M^2)\) is trivial.
Indeed it is finite, because it preserves the corresponding
finite lattice and is compact at infinity. At one29 place it
embeds into a conjugate of
\(1+29M_n(\mathbf Z_{29})\), which is torsion free by the
binomial valuation argument in AM-R-012. A conjugate has the
same property. Consequently, with
\(\operatorname{vol}(G_\infty)=1\) and
\(\operatorname{vol}(K_{n,0})=1\), **every** finite class has
mass exactly \(I_n(M^2)^{-1}\), not merely the identity class.

## 7. The 11-adic and archimedean mass accounting

The order of29 modulo11 is10, and
\[
                           v_{11}(29^{10}-1)=1.
\]
If \(10\nmid i\), \(v_{11}(29^i-1)=0\).
If \(i=10\ell\), the elementary lifting-the-exponent identity
gives
\(v_{11}(29^i-1)=1+v_{11}(\ell)\).
Hence, with \(r=\lfloor n/10\rfloor\),
\[
 \boxed{v_{11}(I_n(M^2))
          =6\sum_{\ell=1}^{r}(1+v_{11}(\ell))
          =6\bigl(r+v_{11}(r!)\bigr).}
 \tag{S25}
\]
It is independent of \(e\). The residue check can be made
without a large integer: \(29^{10}\equiv89\pmod{121}\),
so its difference from one has valuation exactly one.
The standard lifting argument follows by expanding
\((1+11u)^\ell-1\), first for \(\ell\) prime to11 and then
iterating the 11th power. This proves the valuation formula.

For example the value in (S25) is0 at rank6,12 at rank20,
18 at rank34, and24 at rank48. Thus the unknown translation
depth does not introduce an increasing 11-adic denominator
through these class masses. This assertion concerns these
Haar factors only.

The archimedean size of the index does depend on depth:
\[
 \frac12\log I_n(M^2)
       =6en^2\log29+
                     3\sum_{i=1}^n\log(1-29^{-i}).
 \tag{S26}
\]
For clarity, this is a class-coordinate normalization, not a
claim that the already produced input can be replaced by an
arbitrary class delta. If a scalar automorphic function of
compact type \(\rho\) is fixed by this finite level, choose
unitary bases and write its class restrictions as
\(F_c(k)=\operatorname{tr}(A_c\rho(k))\).
Since all stabilizers are trivial, Schur orthogonality gives
\[
 \|F\|_2^2=
  \frac{1}{I_n(M^2)\dim\rho}
                  \sum_c\|A_c\|_{\rm HS}^2.
 \tag{S27}
\]
Consequently each matrix entry of \(A_c\), in the chosen unitary
bases, is at most
\(\sqrt{I_n(M^2)\dim\rho}\,\|F\|_2\).
Comparison with the source's primitive Schur coefficient
lattice remains the separate normalization already studied
in AM-R-011. Formula(S27) does not identify the arithmetic row.

## 8. Remaining gate and exact scope

The new construction controls the finite support and norm:
all later inputs are one actual29-supported Heisenberg translate,
with coefficient one and finite \(L^2\) norm one. It supplies an
explicit sufficient principal level and exact class masses.
The later selected real norms, the input-vector norms, and
the output content are not set to one.

The depths \(e_j\) are not bounded. More fundamentally, these
full-orbit inputs need not equal the source's specified raw Xi
or lie in its DP59 half-orbit. AM-DO-029 records the actual
finite expansion of that raw function and its separate local
support conditions. Neither (S22) nor the mass formula proves
that the prescribed row kernel acts nontrivially on the previous
image lattice, or that its integral image is saturated.

No later \(g_j\), source \(e_j\)-error, complete \(H\), six
comparison identities, or DP44 shortening is deduced from this
result. The value of (S25) is useful concrete accounting data;
it is not itself a row gain.

## Primary locators and carried inputs

- Macdonald, I. G. (1995). Symmetric functions and Hall polynomials
  (2nd ed.). Oxford University Press. ChapterV, (2.9), p.298;
  (3.4), p.299; (4.4)–(4.5), p.301, including its convergence
  statement. https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf.
  The formula was read directly; the matrix-disintegration
  normalization and the application at the actual rank are
  given in full above.
- Liu, Y. (2021). Theta correspondence for almost unramified
  representations of unitary groups. arXiv:2105.14223v1.
  Notation5.5 and equation(5.1), p.15; Proposition5.6, p.16,
  sign \(+\); Lemma6.1, p.20; Theorem6.2, pp.21–22.
  These are the actual lattice-vector and normalized local
  integral statements used in section4.
- Gan, W. T., Qiu, Y., & Takeda, S. (2014). The regularized
  Siegel–Weil formula (the second term identity) and the Rallis
  inner product formula. arXiv:1207.4709v3, sections11.3–11.8,
  especially the doubled evaluation on p.52, equation(11.3),
  Theorem11.4 and Proposition11.6.
- Mínguez, A. (2008). Correspondance de Howe explicite:
  paires duales de type II. Annales Scientifiques de l'École
  Normale Supérieure, 41(5), 717–741. Theorem1, p.718,
  including the multiplicity-one/reciprocal uniqueness and
  all-residue-characteristic assertion.
- Actual host and phases: AM-DO-020/022; exact source-to-doubling
  convention: AM-DO-028. Actual nonzero chain and Satake blocks:
  ALP-LIFT-14. Full finite Heisenberg basis: ALP-LIFT-15.
  First input and torsion-free principal-level proof:
  AM-R-012. These retain their separate check histories.

