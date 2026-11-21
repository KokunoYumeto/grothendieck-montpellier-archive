# MAS-11: independent full-proof check

Date: 2026-11-21. Checker: GPT-6 Astra Pro; effort not exposed; TRACE_DET_20261121 /root/masullo_bridge_check.

## Result and exact scope

**PASS for the substantive theorem and proof.** I read the complete initial character-extension TeX and then the complete enlarged final version, including its already-centered gauge, completed-zero interpretation and Grothendieck-framework paragraph. I independently reconstructed the analytic and operator arguments below. At the parent's subsequent request, I applied only the two local-parameter and central-wording clarifications listed below to the section file, then reread the entire current section again. No master file was edited. The post-edit full read covered 166 lines / 15,055 bytes, SHA256 0794769f1dff7fcfac864d2afbd8db6b0ccf5bf9562588c4ebdd9706b31e57f1; it also verified the explicit convention that zeros are distinct and multiplicities are carried by \(N_\rho\).

The remaining mathematical hypothesis is exactly the stated full spectral-annihilator description of the actual Masullo quotient. The argument does not prove that draft theorem, does not assume its separate nuclearity theorem, and does not use GRH. Classical continuation, functional equation, pole and order facts for fixed Hecke characters remain classical analytic inputs with the sources identified below.

Three small precision points were sent to the parent; the first two were then applied at the parent's request:

1. Take the local parameters explicitly as \(\kappa_v\in\{0,1\}\), \(m_v\in\mathbb Z\), \(t_v\in\mathbb R\). The real gamma factor requires the chosen parity representative 0 or 1, not an arbitrary exponent representing the same sign character.
2. Replace “Removing only eigenvectors would not suffice at a multiple central zero” by “need not suffice.” At central multiplicity two the Green block is scalar, since \(F_\mu'(0)=0\); at multiplicity at least three genuine higher generalized vectors can occur. The actual construction correctly removes the whole Riesz block in every case.
3. The fetched online rendering of Kedlaya (6.1.4) appears to have a \(\pi^{-s}\) on its right side where its surrounding derivation requires \(\pi^{-s/2}\). The formula in MAS-11 is independently supported by DLMF and the adjacent derivation. This observation concerns the retrieved display; no claim about an independently inspected printed edition is made.

The parent's earlier request to clarify that the radial gauge acts in an already-centered ambient space is incorporated in the final version I read.

## 1. Classical completion and source conventions

Primary sources inspected directly:

- [Poonen, Tate's thesis notes](https://math.mit.edu/~poonen/786/notes.pdf), §4.7, Theorem 4.18, Theorem 5.16 and Theorem 5.22. The local factors, two possible norm-character poles, and global functional equation match the conventions used here.
- [Rajan, Distribution of values of Hecke characters of infinite order](https://www.researchgate.net/publication/266311380_Distribution_of_values_of_Hecke_characters_of_infinite_order), author-uploaded full text, §1, printed pp. 281–283. This states the conductor normalization and order-one assertion for normalized unitary characters.
- [DLMF §25.15](https://dlmf.nist.gov/25.15), formulas (25.15.5)–(25.15.6), and [Kedlaya, Chapter 6](https://kskedlaya.org/ant/chap-funceq2.html), the even/odd functional-equation derivations. The Dirichlet specialization, partner character, parity and Gauss-sum normalization were checked; the minor display issue noted above is not imported.

For the stated unitary local characters, conversion to Tate's local parameter gives

\[
L_v(s,\chi_v)=
\begin{cases}
\Gamma_{\mathbb R}(s+\kappa_v+it_v),&v\text{ real},\\
\Gamma_{\mathbb C}(s+|m_v|/2+it_v),&v\text{ complex}.
\end{cases}
\]

At a complex place the norm is \(|z|_v=|z|^2\). This is why the angular shift is \(|m_v|/2\) while the imaginary norm shift is \(it_v\). The factors of 2 in \(\Gamma_{\mathbb C}\) are constant per complex place; they do not affect zero sets or any normalization \(f_\chi/a_\chi\).

The finite Euler factors use the actual local character conductor, so the expression is primitive, even when one begins with a character describable using a larger modulus. With \(Q_\chi=|d_F|N\mathfrak f_\chi\), the factor \(Q_\chi^{s/2}\) absorbs the s-dependent conductor part of the epsilon factor. Its remaining epsilon constant has modulus one. Inversion preserves conductor and sends the local parameters to \(\kappa_v,-m_v,-t_v\). Thus the chosen completions satisfy both

\[
\Lambda_\chi(s)=\epsilon_\chi\Lambda_{\chi^\vee}(1-s),
\qquad
\Lambda_{\chi^\vee}(s)=\overline{\Lambda_\chi(\overline s)}.
\]

For a primitive Dirichlet character, the customary completion differs from this one only by the positive constant \(q^{\kappa/2}\). The stated root number \(\tau(\chi)/(i^\kappa\sqrt q)\) is correct. The primitive principal case has conductor one and is treated separately.

### Imaginary norm twists and poles

If \(\chi=\chi_0|\cdot|^{i\tau}\), the finite Euler factors and every archimedean argument are shifted by \(i\tau\), while the conductor is unchanged. Direct substitution gives

\[
\Lambda_\chi(s)=Q_\chi^{-i\tau/2}\Lambda_{\chi_0}(s+i\tau).
\]

An arbitrary unitary character can be normalized by subtracting the weighted mean of its archimedean imaginary norm parameters. Hence it is such an imaginary norm twist of a normalized unitary character. Vertical translation and multiplication by a nonzero constant preserve entire order.

Only a pure norm character \(\chi=|\cdot|^{i\tau}\) gives poles, at \(-i\tau\) and \(1-i\tau\). They are simple with nonzero residues. Therefore

\[
p_\chi(s)=(s+i\tau)(s-1+i\tau)
\]

removes both poles and gives nonzero values at the removed singularities. It creates no new zeros. In all other cases \(p_\chi=1\). The direct calculation

\[
p_{\chi^\vee}(1-s)
=(1-s-i\tau)(-s-i\tau)
=(s+i\tau)(s-1+i\tau)
\]

checks the sign and preserves the same functional equation for \(\mathcal F_\chi=p_\chi\Lambda_\chi\). Conjugation likewise carries \(p_\chi\) to \(p_{\chi^\vee}\). Thus \(\mathcal F_\chi\) is entire of order one, with the completed zero divisor.

For \(\Re s>1\), the finite Euler product is nonzero, the gamma factors are finite and nonzero, and the conductor factor never vanishes. Reflection by the functional equation excludes zeros for \(\Re s<0\). The pole-clearing values are nonzero. Consequently the elementary closed-strip statement \(0\le\Re\rho\le1\) suffices. No boundary nonvanishing theorem is silently used.

## 2. Exact meaning of the draft's zeros

I directly reread the relevant passages in work/masullo_full.txt and work/masullo_pages_444_457.txt:

- Definition 3.2.1.2 and (3.2.1.2)–(3.2.1.5), printed p. 123.
- Proposition 3.2.1.3(2), on the two simple poles.
- Theorem 7.1.4.2(1), printed p. 326, including its pole-cleared ideal.
- Notation 10.2.2.1, printed p. 445, allowing a unitary base point for each compact-character component.
- Theorem 10.2.2.1 and (10.2.2.4)–(10.2.2.6), printed p. 446.

The draft's \(L(s,\chi)\) already includes the archimedean factors. Its finite \(L_f\) is separately named in Definition 3.2.1.4. Thus enlarging the Hilbert strip does not introduce the trivial zeros of the finite Euler product as extra jets.

The draft's completion differs from the completion here by \(2^{r_2}Q_\chi^{s/2}\), a nowhere-zero function. In the norm-character case, Theorem 7.1.4.2(1) uses

\[
(s+i\tau)(1-s-i\tau)L(s,\chi)=-p_\chi(s)L(s,\chi).
\]

The sign is harmless and the zero divisor is exactly the one claimed. The later product formula (7.1.4.9), and the proof surrounding it, are not used. This is a notation/pole interpretation check; the full spectral-annihilator theorem itself remains a conditional draft input.

## 3. The gauge, centering and sector restriction

Let the centered ambient quotient have \(a=1/2\), half-width \(\alpha>1/2\), and weight exponent \(\nu>1\):

\[
w_\alpha(u)=e^{2\alpha|u|}(1+u^2)^{\nu/2}.
\]

The factor \(|g|^{1/2}\) belongs to the definition of the centered theta-image, not to an additional factor in the gauge. In that already-centered ambient space, write

\[
f(g)=\overline{\chi(g)}h(\log|g|).
\]

Because \(\chi\) is unitary and the compact Haar factor has mass one, this map is isometric from the radial weighted \(L^2\) space onto the primal sector labeled by the dual base point \(\chi\).

The source's bilinear dual pairing with
\(\chi(g)|g|^{\rho-1/2}(\log|g|)^j\)
then becomes exactly

\[
\ell_{\rho,j}(h)=\int_{\mathbb R}h(u)e^{(\rho-1/2)u}u^j\,du.
\]

There is no extra conjugation, imaginary shift or additional half-center. If \(s(v)\) is the chosen radial section of norm \(e^v\), the original translation \(f(g)\mapsto f(s(v)^{-1}g)\) becomes

\[
h(u)\mapsto \chi(s(v))h(u-v).
\]

Multiplication by the inverse unitary scalar gives the pure translation \(T_vh(u)=h(u-v)\). This explicitly verifies the assertion about arbitrary imaginary norm twists.

Compact-character averaging is bounded because the compact action is unitary and preserves the theta-image. Applying the relevant dual projection to the global dense jet span gives the dense span in the fixed sector. Labeling by the dual character avoids an isotype-inverse convention error.

Every completed zero satisfies \(|\Re(\rho-1/2)|\le1/2<\alpha\). Therefore

\[
\int_{\mathbb R}
\frac{e^{2\Re(\rho-1/2)u}|u|^{2j}}{w_\alpha(u)}\,du<\infty
\]

for every finite j. All multiplicity jets are continuous and are interior jets; none is subject to the source's boundary truncation.

## 4. Independent verification of the Green transfer

Put \(B_0=\alpha+\nu/4\). Almost everywhere,

\[
b(u)=\frac{(\log w_\alpha)'(u)}2
=\alpha\operatorname{sgn}u+\frac{\nu u}{2(1+u^2)},
\qquad |b|\le B_0.
\]

Thus \(\|T_v\|\le e^{B_0|v|}\), and the translations are strongly continuous. For \(\mu>B_0\), both \(g_\mu=e^{-\mu|v|}/(2\mu)\) and its weak first derivative are integrable with this exponential weight. Their weighted \(L^1\) norms are respectively \(1/[\mu(\mu-B_0)]\) and \(1/(\mu-B_0)\). The strong vectorwise convolution is bounded.

The binomial translation formula sends each jet to lower jets at the same zero. Full annihilator totality therefore makes the theta subspace invariant under translations and Green convolution. The quotient operator is a compression of the ambient operator to the orthogonal complement of the theta subspace.

For \(y=K_\mu f\), distributional differentiation gives
\(y''=\mu^2y-f\), with \(y,y',y''\) in the weighted space. Under multiplication by \(\sqrt{w_\alpha}\), set \(h=\sqrt{w_\alpha}y\), \(D=\partial-b\). Then \(h,Dh\in H^1\), \(D^2h=\sqrt{w_\alpha}y''\). The same direct integration by parts as in MAS-10 gives

\[
\Re\langle(\mu^2-D^2)h,h\rangle
\ge\|h'\|^2+(\mu^2-B_0^2)\|h\|^2
\]

and imaginary part bounded by
\(2B_0\|h'\|\|h\|\).
No derivative of the cusp coefficient b is needed. Hence the symmetric numerical sector has constant

\[
c=\frac{B_0}{\sqrt{\mu^2-B_0^2}}.
\]

It passes to the quotient by compression and to the adjoint by complex conjugation.

The full dual multiplier is \(F_\mu(z)=(\mu^2-z^2)^{-1}\). For \(z=b+it\), \(|b|\le1/2\), let \(A=\mu^2-b^2+t^2>0\). Then

\[
\Re\frac1{\mu^2-z^2}=\frac{A}{A^2+4b^2t^2}>0,
\qquad
\left|\frac1{\mu^2-z^2}\right|
\le\frac1{\mu^2-1/4+t^2}.
\]

Entire order one is enough for the required summability. After removing the finite central order, Jensen's formula gives \(n(R)=O_\eta(R^{1+\eta})\) for every \(\eta>0\). Dyadic summation with \(0<\eta<1\) gives
\(\sum_{\rho\ne1/2}N_\rho|z_\rho|^{-2}<\infty\).
The displayed bound then implies absolute summability of all Green eigenvalues; the central contribution is finite.

Enumerate complete jet blocks in increasing derivative order. Their Riesz representatives are total and finitely independent, and their finite prefixes are invariant under \(K_\chi^*\). Gram–Schmidt preserves those prefixes. In the global conjugate-first convention the adjoint diagonal is \(\overline{\lambda_\rho}\), so the real-part diagonal sum is \(\sum_\rho N_\rho\Re\lambda_\rho\).

For completeness, the trace-ideal step uses positivity of \(A_K=(K+K^*)/2\), not a general assertion that summable eigenvalues imply trace class. The finite positive diagonal sum makes \(A_K^{1/2}\) Hilbert–Schmidt. The sector bound gives
\(-cA_K\le (K-K^*)/(2i)\le cA_K\);
bounded form factorization yields
\(K=A_K^{1/2}(I+iC)A_K^{1/2}\), with \(C=C^*\), \(\|C\|\le c\).
Thus K is trace class, with precisely the norm estimate in the TeX.

Only now use compactness. Finite invariant orthonormal flags give a triangular block decomposition whose tail norm tends to zero. For a nonzero value absent from the diagonal, a sufficiently small tail and an invertible finite block give an inverse. For a displayed eigenvalue, its generalized eigenspace lies in a finite prefix once the tail norm is smaller than its modulus. Thus the spectrum and algebraic multiplicities are exact. Collisions occur only for \(z_\rho=\pm z_{\rho'}\), so there are finitely many occurrences of each nonzero Green eigenvalue.

This verifies the whole MAS-10 transfer, with no extra nuclearity, GRH or uniform-conductor hypothesis.

## 5. Central Riesz removal and the reciprocal square

Let \(m=\operatorname{ord}_{1/2}\mathcal F_\chi\). The value \(\mu^{-2}\) occurs in the Green spectrum exactly when \(z_\rho=0\), and its total algebraic multiplicity is m.

The transpose of the Riesz projection for \(\mu^{-2}\) is identity on the entire central jet block and zero on every noncentral block: this follows by restricting the resolvent to each finite invariant jet block and integrating around the isolated spectral value. Since the jet span is norm dense, its range is exactly the m-dimensional central span. Therefore the primal projection has rank m. Its action on all jets does not depend on \(\mu\), so density also proves independence of the projection from \(\mu\).

The range \(E_\chi^\circ=(I-P_{\chi,0})E_\chi=\ker P_{\chi,0}\) is closed and invariant. It carries the inherited Hilbert norm even when the projection is not orthogonal. If \(i:E_\chi^\circ\to E_\chi\) is inclusion and \(Q\) is the orthogonal projection onto this closed subspace, then the restricted Green operator is \(QK_\chi i\); this proves trace-class restriction directly by the ideal property.

The value \(\mu^{-2}\) is absent from the restricted spectrum, so \(I-\mu^2K_\chi^\circ\) is boundedly invertible. Hence its product defining \(R_\chi\) is trace class. On each noncentral jet block, rational functional calculus gives the identity of truncated Taylor series

\[
\frac{F_\mu(z)}{1-\mu^2F_\mu(z)}=-\frac1{z^2}.
\]

The denominator is nonzero at every noncentral zero. Restricted noncentral jets remain total: restriction of the full dual to the closed complement is surjective, all central jets vanish there, and all noncentral jets survive. Therefore the full-jet identity proves independence of \(R_\chi\) from \(\mu\).

The compact spectral description, or the same finite-flag proof on the complement, gives exactly the eigenvalues \(-z_\rho^{-2}\), with additive full algebraic multiplicities at coincident values.

The central caution deserves precision. At zero,

\[
F_\mu(z)=\mu^{-2}+\mu^{-4}z^2+\mu^{-6}z^4+\cdots.
\]

Thus \(K'\ell_0=\mu^{-2}\ell_0\) and \(K'\ell_1=\mu^{-2}\ell_1\), while
\(K'\ell_2=\mu^{-2}\ell_2+2\mu^{-4}\ell_0\).
This explains both why generalized removal is necessary in general and why “need not suffice” is the exact wording for removal of ordinary eigenvectors.

## 6. Partner normalization and genus-one cancellation

Write \(C_\chi(z)=\mathcal F_\chi(1/2+z)=z^mf_\chi(z)\), with \(a_\chi=f_\chi(0)\ne0\). The functional equation gives the same central order for the inverse character and

\[
f_\chi(z)=\epsilon_\chi(-1)^mf_{\chi^\vee}(-z),
\qquad
a_\chi=\epsilon_\chi(-1)^ma_{\chi^\vee}.
\]

Dividing these equations proves

\[
\frac{f_\chi(-z)}{a_\chi}
=\frac{f_{\chi^\vee}(z)}{a_{\chi^\vee}}.
\]

The conjugation identity also gives \(a_{\chi^\vee}=\overline{a_\chi}\). These conclusions require no central nonvanishing; division is performed only after the exact central factor has been removed.

Therefore

\[
\mathcal H_\chi(z)=
\frac{f_\chi(z)f_{\chi^\vee}(z)}{a_\chi a_{\chi^\vee}}
=\frac{f_\chi(z)f_\chi(-z)}{a_\chi^2}
\]

is even, entire, of order at most one and normalized to one at zero. Substituting \(z=i\sqrt w\) through its even power series gives an entire \(G_\chi\), with order at most one half. There is no branch choice.

Hadamard factorization of \(f_\chi/a_\chi\), whose value at zero is one, is

\[
\frac{f_\chi(z)}{a_\chi}
=e^{b_\chi z}\prod_{\rho\ne1/2}
\left((1-z/z_\rho)e^{z/z_\rho}\right)^{N_\rho}.
\]

Multiply the finite partial products at z and -z and then pass to locally uniform limits. The two linear exponentials cancel, as do the convergence factors in every matched term. The resulting product

\[
\mathcal H_\chi(z)=
\prod_{\rho\ne1/2}(1-z^2/z_\rho^2)^{N_\rho}
\]

is absolutely locally uniformly convergent by reciprocal-square summability. This cancellation is essential: no evenness of \(f_\chi\) itself was assumed in the non-self-dual case.

The ordinary trace-class determinant theorem now gives

\[
\det_{E_\chi^\circ}(I-wR_\chi)
=\prod_{\rho\ne1/2}(1+w/z_\rho^2)^{N_\rho}
=\mathcal H_\chi(i\sqrt w)=G_\chi(w).
\]

If both z and -z already occur among the zeros for the single character, their factors are both present and their multiplicities add. Thus this formula also handles accidental squared-parameter collisions correctly.

## 7. Labeled exchange and self-dual half determinant

On the centered idelic ambient space, inversion takes

\[
\overline{\chi(g)}h(\log|g|)
\quad\text{to}\quad
\overline{\chi^\vee(g)}h(-\log|g|).
\]

It is therefore exactly \(Jh(u)=h(-u)\) between the two radial gauges. The radial weight is even, so J is unitary. A substitution gives

\[
\ell_{\chi^\vee,1-\rho,j}(Jh)=(-1)^j\ell_{\chi,\rho,j}(h).
\]

The functional equation matches the zero blocks with their multiplicities. Totality of the annihilators then proves \(JV_\chi=V_{\chi^\vee}\), so J descends to the actual quotient. The Green kernel is even; consequently J intertwines both Green operators, their central Riesz projections, and their reciprocal squares. In particular it maps the closed central complements unitarily.

On two labeled copies the exchange involution
\(\mathcal J(x,y)=(Jy,Jx)\)
has even subspace unitarily parametrized by \(x\mapsto(x,Jx)/\sqrt2\). The direct-sum operator restricted to this graph is unitarily equivalent to \(R_\chi\). Its determinant is \(G_\chi\); the full direct sum has determinant \(G_\chi^2\). The labels are necessary even when the compact restrictions coincide, because different norm twists give different radial gauges. No assertion that equal compact types imply global self-duality is used.

If the global character actually satisfies \(\chi=\chi^\vee\), the coefficient of the first nonzero central Taylor term forces \(\epsilon_\chi=(-1)^m\). It follows that \(f_\chi\) is even. Reflection now acts inside the single quotient and preserves the central complement.

For every unordered pair of noncentral zeros \(\{z,-z\}\), it exchanges two independent jet spaces with signs \((-1)^j\). The even subspace has dimension \(N_\rho\), and projection of the total dual jet span is total in the even dual. Thus the determinant of the even restriction has one factor \(1+w/z_\rho^2\) per pair, with multiplicity \(N_\rho\). Its square is the full single-sector determinant \(G_\chi\).

The function \(f_\chi(i\sqrt w)/a_\chi\) is entire because \(f_\chi\) is even, is normalized to one, and has the same square. The two square roots agree near zero and hence everywhere by analytic continuation. This proves the claimed self-dual half determinant.

There are two distinct involutions here: exchange of two labeled character copies, and internal reflection in a self-dual single sector. Their determinant multiplicities differ exactly as stated. Before central removal, reflection has eigenvalues \((-1)^j\) on the m central jets; its even and odd dimensions are therefore \(\lceil m/2\rceil\) and \(\lfloor m/2\rfloor\).

## Final disposition

The entire final proof checks out, including arbitrary unitary norm twists, all completed multiplicities, the nonorthogonal central complement, independence from the auxiliary Green parameter, genus-one cancellation, normalized partner product, and both parity constructions. There is no missing operator bound or hidden central-nonvanishing assumption.

The enlargement \(\alpha>1/2\) correctly avoids needing a boundary nonvanishing theorem. The optional \(\alpha=1/2\) version explicitly requires that extra classical fact. The conclusion is for fixed characters; no uniform conductor or infinity-type estimate is claimed.

The new framework paragraph accurately describes an analytic trace-class realization conditional on the draft spectral theorem. It supplies no arithmetic cohomology, Frobenius operator, motive, positivity or selfadjointness. Those boundaries are retained rather than inferred from the determinant identity.
