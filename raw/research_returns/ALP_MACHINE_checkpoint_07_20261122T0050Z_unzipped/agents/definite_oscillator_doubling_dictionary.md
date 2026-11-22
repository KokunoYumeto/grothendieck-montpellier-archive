# AM-DO-028: the even-rank Hom/tensor and doubling-character dictionary

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`;
inherited reasoning effort not separately exposed; 21 November 2026 UTC.

This result fixes the character ratio in the Rallis factor for the
literal bilinear source theta operator. It uses the actual
Hom action and the determinant-root convention of AM-DO-022--026.
It applies to even-rank edges with splitting characters trivial
on the base-field ideles. It does not claim a new general local
theta theorem, a full global chain, or an arithmetic estimate for
the Schwartz functions obtained by nonvanishing theorems.

## 1. The tensor model includes a dual source space

Write \(E/F\) for the CM extension, including the common host
\(E'=\mathbf Q(\zeta_{28})\) when that host is used. Let
\(S=E^a,T=E^b\) have their identity Hermitian forms, with both
\(a,b\) even. Use the actual trace-zero coefficient \(\xi\)
of the symplectic form; on the common host this is \(\xi'=\xi_J/2\).
The underlying symplectic action and form are
\[
 X\longmapsto hXg^{-1},\qquad
 B(X,Y)=-\operatorname{Tr}_{E/F}
                   (\xi\operatorname{tr}(Y^*X)).
 \tag{DO28.1}
\]
Composition with \(\operatorname{Tr}_{F/\mathbf Q}\) gives
the rational form used previously. The additive character and
self-dual measures are transported with this form.

Put \(V=T\) and let \(U=S^\vee\) have the skew-Hermitian
form \(-\xi\) times the dual identity Hermitian form, linear
in the first variable. The map
\[
 V\otimes_EU\longrightarrow\operatorname{Hom}_E(S,T),
                  v\otimes\ell\longmapsto v\ell
 \tag{DO28.2}
\]
is a symplectic isomorphism. Indeed, on pure tensors the product
of the two forms is
\(-\xi(v'^*v)(\ell'^*\ell)\), whose trace is exactly
(DO28.1) after expanding the matrix trace. The source group
identification is
\[
 \alpha:U(S)\longrightarrow U(U),\qquad
                            \alpha(g)=g^{-t}.
 \tag{DO28.3}
\]
Thus the tensor action \(h\otimes\alpha(g)\) is exactly
the Hom action. This is an actual representation isomorphism,
with the same Heisenberg form, rather than an identification of
two abstract groups followed by an unspecified oscillator twist.

For a character \(\chi\) trivial on \(\mathbb A_F^\times\),
write
\[
 \nu_\chi(z/\bar z)=\chi(z).
 \tag{DO28.4}
\]
The standard tensor splitting changes on \(U(U)\) by
\(\nu_{\Delta\chi_V}(\det g_U)\) and on \(U(V)\) by
\(\nu_{\Delta\chi_U}(\det h)\). This is the usual
Kudla/Harris--Kudla--Sweet character-change convention. GQT
equation (2.2), printed p.13, fixes the positive source sign
already in the zero-dimensional opposite-member case. Gan
(2022), section2.5, printed pp.14--15, states the two character
changes explicitly with the Hilbert-90 inverse.

Since \(\det\alpha(g)=\det(g)^{-1}\), pulling back this
splitting through (DO28.3) gives the source convention
\[
 \nu_{\Delta\chi_T}(\det g)^{-1}
                         \nu_{\Delta\chi_S}(\det h)
 \tag{DO28.5}
\]
when and only when the tensor labels are
\[
                     \boxed{\chi_U=\chi_S,\qquad\chi_V=\chi_T.}
 \tag{DO28.6}
\]
The determinant roots, rather than the determinants themselves,
are evaluated in (DO28.4). Functorial transport of the fixed
standard splitting through the symplectic isomorphism fixes the
baseline as well as the character changes; no free character
is added. In the common-host construction the baseline is also
the explicitly checked trivial-character model of DO022.

This does not contradict the corrected Konno--Konno dictionary
in DO023. Their matrix source argument there was kept as \(g\),
not replaced by \(g^{-t}\); its character label is therefore
\(\chi_T^{-1}\). Changing that label while omitting (DO28.3)
changes the representation.

## 2. The input is conjugated and transported

Let \(F\) be an actual automorphic vector in a unitary
representation \(\sigma\) of \(U(S)(\mathbb A_F)\).
The source operator is
\[
        T_\phi F(h)=\int_{[U(S)]}\theta_\phi(g,h)F(g)\,dg.
 \tag{DO28.7}
\]
GQT section11.2, printed pp.51--52, uses the integral against
the conjugated input. The bar was checked in the rendered PDF,
since text extraction omits it. Define the input in tensor
coordinates by
\[
         f(u)=\overline{F(\alpha^{-1}u)},\qquad
         \pi=\overline\sigma\circ\alpha^{-1}.
 \tag{DO28.8}
\]
With Haar measure pushed forward under the group isomorphism,
the GQT theta integral of \(f\) is exactly (DO28.7), for the
transported actual Schwartz vector. There is no unspecified
volume scalar. For Tamagawa measures the same conclusion
follows from invariance under the rational group isomorphism.

At the level of standard base-change parameters, contragredience
from complex conjugation and contragredience from (DO28.3)
cancel. More precisely, at an unramified place the automorphism
\(g\mapsto g^{-t}\) sends the Satake matrix to its inverse
transpose, while \(\overline\sigma=\sigma^\vee\) for the
unitary representation. Hence
\[
                         \phi_\pi=\phi_\sigma.
 \tag{DO28.9}
\]
The same statement holds whenever the usual local Langlands
parameter is available and its contragredient functoriality is
used. The unramified statement suffices to identify the partial
global standard Euler product. At a compact real place the
two operations likewise return the original highest weight.

This is why the actual selected input in DO025 retains its old
parameter block under a same-character lift. Its Hom oscillator
component is the dual of the input; the tensor source component
is the input after the simultaneous change (DO28.3), (DO28.8).

## 3. An exact doubling-integral twist identity

This part can be checked directly in GQT, without guessing the
meaning of a printed multiplication sign in an \(L\)-factor.
Let \(\chi\) be a unitary character of
\(E^\times\backslash\mathbb A_E^\times\), trivial on
\(\mathbb A_F^\times\). On the doubled unitary group
\(G(U\oplus U^-)\), define
\[
                         d_\chi=\nu_\chi\circ\det.
 \tag{DO28.10}
\]
For its Siegel Levi element \(m(A)\), the unitary determinant
is \(\det A/\overline{\det A}\). Therefore
\[
                       d_\chi(m(A))=\chi(\det A).
 \tag{DO28.11}
\]
Multiplication by \(d_\chi\) gives an exact isomorphism
between the normalized induced representations
\[
 I(s,1)\longrightarrow I(s,\chi),\qquad
                        \Phi\longmapsto\Phi_\chi=d_\chi\Phi.
 \tag{DO28.12}
\]
The normalization by the parabolic modulus is unchanged, and
the multiplier is independent of \(s\). Standard, holomorphic,
and good sections are transported accordingly. For good
sections defined using the standard intertwiner, this also
follows directly: \(d_\chi\) is trivial on the unipotent
radical, so the intertwiner changes only by its fixed nonzero
value at the chosen Weyl representative. No zero or pole in
\(s\) is introduced.

On the embedded pair \((g,1)\), the multiplier is
\(\nu_\chi(\det g)\). In GQT section11.6, printed p.54,
the local zeta integral is the integral of this section against
the **conjugated** matrix coefficient of \(\pi\). That bar
was also checked in the rendered PDF. Consequently
\[
 \begin{split}
 Z_\chi(s,\Phi_\chi,f_1,f_2;\pi)
 &=\int\Phi(g,1)\nu_\chi(\det g)
                    \overline{\langle\pi(g)f_1,f_2\rangle}\,dg\\
 &=Z_1(s,\Phi,f_1,f_2;
                       \pi\otimes(\nu_\chi\circ\det)^{-1}).
 \end{split}
 \tag{DO28.13}
\]
This holds first in the common region of absolute convergence,
and elsewhere by meromorphic continuation. It is an equality
of the actual local integrals with unchanged Haar measure.
The same identity holds for the global doubling integral: the
automorphic character \(d_\chi\) is trivial on rational
points, so it factors through the Eisenstein sum, and its two
group factors cancel against the corresponding input twists.
Here there is a necessary distinction between \(\chi\) and
\(\nu_\chi\): for \(t\bar t=1\),
\(\chi(t)=\nu_\chi(t)^2\), since \(t/\bar t=t^2\).
Thus the actual factor in GQT's global integral on printed
p.53 is
\[
 d_\chi(g_1)d_\chi(g_2)\chi(\det g_2)^{-1}
              =d_\chi(g_1)d_\chi(g_2)^{-1}.
 \tag{DO28.13a}
\]
Its product with \(\overline{f_1(g_1)}f_2(g_2)\) is
\(\overline{(f_1d_\chi^{-1})(g_1)}
       (f_2d_\chi^{-1})(g_2)\), exactly as required for
the representation in (DO28.14). This also checks the
determinant-root normalization in the global identity.

GQT defines its local standard factor from these doubling
integrals and cites the normalized GCD statement of Yamana
in section11.6. Thus, in the even-character case here, its
factor is the untwisted standard factor of
\[
                   \pi_0=\pi\otimes(\nu_\chi\circ\det)^{-1}.
 \tag{DO28.14}
\]
At nonarchimedean places the equality of good-section ideals in
(DO28.13) gives the same normalized reciprocal polynomial
factor; its constant-term-one normalization removes a Laurent
unit ambiguity. The archimedean standard gamma-factor
interpretation gives the same twist when expressed through
the standard parameter. In particular, at every unramified
place its standard Euler parameter is
\[
                              \phi_\pi\otimes\chi^{-1}.
 \tag{DO28.15}
\]
No claim that an arbitrary nonstandard \(L\)-factor convention
uses the same printed symbol is necessary. Equations
(DO28.12)--(DO28.15) fix the convention by the actual integrals.

## 4. The factor in the source's labels

Apply section3 with \(\chi=\chi_V=\chi_T\), and use
(DO28.9). The Rallis factor for (DO28.7), expressed in standard
base-change notation, is
\[
 \boxed{L_E(s,\phi_\sigma\otimes\chi_T^{-1})
        =L_E(s,\phi_\sigma^\vee\otimes\chi_T).}
 \tag{DO28.16}
\]
The equality follows from conjugation of \(E/F\): the
standard parameter is conjugate self-dual, and
\(\chi_T^c=\chi_T^{-1}\) because its restriction to the
base field is trivial. Conjugating all places of \(E\)
permutes the Euler factors. At a split place of \(F\), this
permutes its two \(E\)-places, so the assertion is for the
paired local standard factor, not for a single arbitrarily
chosen component in isolation.

There is a useful check directly in the source model. Replacing
\(\chi_T\) by \(\chi_T\delta\) multiplies the source
kernel by \(\nu_\delta(\det g)^{-1}\). Replacing the input
by \(F(g)\nu_\delta(\det g)\) makes the integrand unchanged.
The parameter in (DO28.16) is invariant under this simultaneous
change. A proposed parameter \(\phi_\sigma^\vee\chi_T^{-1}\)
would fail this exact identity and is therefore incorrect for
the fixed source convention.

For an already established standard parameter block
\(\mu_r\otimes S_d\) in an input to edge \(j\), the
corresponding character in (DO28.16) is
\[
                              \mu_r\mu_j^{-1},
 \tag{DO28.17}
\]
or its inverse after the simultaneous conjugation used in the
right side of (DO28.16). Here \(S_d\) denotes the actual
length-\(d\) segment with whichever standard/Arthur parameter
description has been proved for that local lift. This calculation
does not supply that local theta theorem. When the segment
has the usual unramified exponents
\((d-1)/2,(d-3)/2,\ldots,-(d-1)/2\), evaluating at
\(s=(d+1)/2\) gives the Hecke factors at
\(1,2,\ldots,d\), with the character (DO28.17).

For the selected DO025 exponents, \(\mu_j/\mu_r\) has
infinity exponent \(-e_j+e_r\). If \(j>r\), the proved
strict increase \(e_j-e_r\ge(j-r)(d+2)>0\) shows that this
is a nontrivial angular character. This verifies the sign and
nontriviality needed when applying a separate Hecke
\(L(1)\)-nonvanishing theorem. It is not a proof of that
theorem or a quantitative lower bound for its value.

## 5. Exact scope and sources

The evenness restriction is essential to the simple global
character \(d_\chi\) in (DO28.10): this argument assumes
\(\chi|\mathbb A_F^\times=1\). It does not silently
extend to an odd opposite rank, where a fixed reference
character must first be divided out. It preserves the actual
host, polarization, additive character, determinant roots,
Haar measures, and bilinear input convention. A Rallis
nonvanishing theorem still requires its local occurrence,
global range, and cuspidality hypotheses. It provides no
selected arithmetic row or bound on the later finite Schwartz
input.

Primary locators used here:

- Gan, W. T., Qiu, Y., & Takeda, S. (2014). *The regularized
  Siegel--Weil formula (the second term identity) and the Rallis
  inner product formula*. Inventiones Mathematicae, 198,
  739--831. The supplied arXiv version1207.4709, section2.8
  and equation(2.2), printed pp.12--13; section11.2,
  pp.51--52; section11.5 and section11.6, pp.53--54;
  Theorem11.4, pp.54--55. The PDF was inspected for the bars
  omitted by its text extraction.
- Gan, W. T. (2022). *Automorphic forms and the theta
  correspondence*. Arizona Winter School lecture notes,
  section2.5, pp.14--15, character changes; sections2.6 and3.8,
  pp.15--16 and26, input/quotient convention; Theorem2.6,
  p.18, and Theorem3.3, p.27, the rank-one inverse-character
  factor. https://swc-math.github.io/aws/2022/2022GanNotes.pdf
- AM-DO-022, DO023 as corrected, DO025, and DO026 for the
  actual Hom splitting and source integral. GQT's published
  results are used at their stated hypotheses, not re-proved.

The full source-to-doubling twist calculation above is new work
in this run; its whole-proof check is recorded separately.
