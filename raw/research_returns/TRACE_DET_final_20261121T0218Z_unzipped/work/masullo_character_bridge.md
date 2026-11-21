# MAS-11 — the actual quotient determinant for a fixed character

## Finding and exact scope

The sectorial Green argument of MAS-10 extends to a fixed primitive Dirichlet character and, more generally, a fixed unitary Hecke character of a number field. Its only deep draft dependency is Masullo's full spectral-annihilator theorem, Theorem 10.2.2.1, page 446, including full interior jets, finite independence and norm density in the continuous Hilbert dual. Neither GRH nor Theorem 10.3.2.1 on nuclearity is needed.

There are two necessary changes from the zeta statement. First, the entire central generalized eigenspace must be removed if the completed function vanishes at 1/2. Second, a non-self-dual character has a functional-equation partner. Its full single-sector inverse-square determinant equals the normalized even product of the two completed functions. The even summand of the paired quotient gives the same product, while the whole paired quotient gives its square. An internal half-spectrum determinant is available for a globally self-dual character.

The statement below fixes center 1/2 and uses a strip half-width α>1/2, with any fixed weight parameter ν>1. This ensures that all completed zeros lie strictly inside the strip using only the closed-strip consequence of the Euler product and functional equation. The same result holds at α=1/2 when the classical nonvanishing theorem on the full line Re(s)=1 is included. No boundary theorem is silently attributed to DLMF 25.15.9, which asserts only nonvanishing at the point s=1 for a nonprincipal Dirichlet character.

The integration-ready version is in work/paper_masullo_characters.tex. This note supplies its conventions, proof and source audit. No master deliverable was changed.

## 1. Completed functions, poles and normalization

Let χ be a unitary character of the idele class group C_F, and let χ∨=χ⁻¹ be its functional-equation partner. Write

\[
Q_\chi=|d_F|N\mathfrak f_\chi,
\qquad \Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),
\qquad \Gamma_{\mathbb C}(s)=2(2\pi)^{-s}\Gamma(s).
\]

Use normalized local absolute values. Thus at a real place

\[
\chi_v(x)=\operatorname{sgn}(x)^{\kappa_v}|x|^{it_v},
\quad \kappa_v\in\{0,1\},
\]

and at a complex place

\[
\chi_v(z)=(z/|z|)^{m_v}|z|_v^{it_v},
\quad m_v\in\mathbb Z,\quad |z|_v=|z|^2.
\]

Our completion is

\[
\Lambda_\chi(s)=Q_\chi^{s/2}
\prod_{v\ {
m real}}\Gamma_{\mathbb R}(s+\kappa_v+it_v)
\prod_{v\ {
m complex}}\Gamma_{\mathbb C}(s+|m_v|/2+it_v)
L_f(s,\chi).
\tag{1}
\]

The finite Euler factor is (1−χ_v(ϖ_v)q_v⁻ˢ)⁻¹ at an unramified place, and 1 at a ramified place. The Tate functional equation, after the conductor is included as in (1), has the form

\[
\Lambda_\chi(s)=\epsilon_\chi\Lambda_{\chi^\vee}(1-s),
\qquad |\epsilon_\chi|=1.
\tag{2}
\]

Primary sources for the local definitions and global functional equation are Poonen, §4.7 and Theorem 5.22, and Rajan, §1, with exact locators in §7 below. The factor 2 at each complex place is a convention; dropping all such factors multiplies the completion by a constant, which cancels from the final ratios. Dropping the conductor power is more consequential: it introduces an exponential in s. We retain it explicitly.

If χ is not a pure imaginary norm power, Λχ is entire. If χ=|·|ⁱᵗᵃᵘ, its simple poles are at −iτ and 1−iτ. Set

\[
p_\chi(s)=
\begin{cases}
(s+i\tau)(s-1+i\tau),&\chi=|\cdot|^{i\tau},\\
1,&\text{otherwise},
\end{cases}
\qquad
\mathcal F_\chi(s)=p_\chi(s)\Lambda_\chi(s).
\tag{3}
\]

Then 𝓕χ is entire of order one. Rajan states this for normalized unitary characters. For an arbitrary unitary character, write χ=χ₀|·|ⁱᵗᵃᵘ with χ₀ normalized. The conductor is unchanged and direct substitution in (1) gives

\[
\Lambda_\chi(s)=Q_\chi^{-i\tau/2}\Lambda_{\chi_0}(s+i\tau).
\]

Thus both the order-one assertion and the pole prescription extend by vertical translation. Pole cancellation does not add a zero: the poles are simple with nonzero residues. Also pχ(s)=pχ∨(1−s), so 𝓕χ satisfies (2) with the same root number. The Euler product excludes completed zeros in Re(s)>1; the completed functional equation excludes them in Re(s)<0. This suffices for the strip choice in this note.

For a primitive Dirichlet character modulo q, use the equivalent customary completion

\[
\Lambda_\chi(s)=(q/\pi)^{(s+\kappa)/2}
\Gamma((s+\kappa)/2)L(s,\chi),
\quad \kappa=(1-\chi(-1))/2,
\tag{4}
\]

\[
\epsilon_\chi=\frac{\tau(\chi)}{i^\kappa\sqrt q},
\quad \tau(\chi)=\sum_{a\bmod q}\chi(a)e^{2\pi ia/q}.
\tag{5}
\]

It differs from (1) by the constant q^{κ/2}. For q>1, primitivity implies that χ is nonprincipal and pχ=1. For q=1, pχ=s(s−1), recovering the usual entire zeta completion up to the harmless factor 1/2. Equations (4)–(5) are checked against the exact primitive functional equation in DLMF 25.15.5–6 and Kedlaya's equations 6.1.4 and 6.2.2.

## 2. The actual sector and the unitary gauge

Fix center a=1/2, half-width α>1/2 and ν>1, and set

\[
H_\alpha=L^2(\mathbb R,w_\alpha(u)\,du),
\qquad w_\alpha(u)=e^{2\alpha|u|}(1+u^2)^{\nu/2}.
\tag{6}
\]

Masullo's Notation 10.2.2.1 permits a unitary base point χ in each compact-character component. Normalize compact Haar measure to have mass one. Name Eχ the quotient sector whose dual is indexed by χ. In the already centered ambient realization, the primal sector is represented by

\[
f(g)=\overline{\chi(g)}h(\log|g|).
\tag{7}
\]

Since χ is unitary, (7) is an isometry onto (6); the centered theta-image becomes a closed space Vχ, and Eχ=Hα/Vχ. The a=1/2 centering is already incorporated in Vχ, in accordance with the source's equations (10.2.2.1)–(10.2.2.2). Labeling by the dual character avoids an ambiguity about conjugates in the source's isotype notation.

The precise conditional input is that the full continuous annihilator of Vχ is the norm closure of the independent jets

\[
\ell_{\rho,j}(h)=\int_{\mathbb R}h(u)e^{z_\rho u}u^j\,du,
\qquad z_\rho=\rho-\tfrac12,
\qquad 0\le j<N_\rho,
\tag{8}
\]

Throughout every sum and product, ρ ranges over the distinct zeros of 𝓕χ and Nρ denotes its multiplicity. Equivalently the jet span is norm dense in Eχ′. The jets are continuous because |Re zρ|≤1/2<α. All multiplicities are interior multiplicities, so the draft's boundary jet cap never enters. The fixed-sector statement follows by compact-character averaging from the source's full Hilbert-dual density; this is a bounded projection and selects exactly the indicated character block.

An imaginary norm twist must not be discarded. In (7), the pure translation h(u)↦h(u−v) corresponds to original radial translation multiplied by the inverse of the unitary scalar χ on the chosen radial section. Thus the ensuing Green operator measures the spectral parameter relative to this actual base point χ. When χ and χ∨ have the same restriction to C_F¹ but are different global characters, the paired construction uses labeled copies with their respective gauges. Equality of compact restrictions is not the self-duality condition.

## 3. Trace class from the actual quotient metric

Put B₀=α+ν/4 and choose μ>B₀. On Hα take the Green convolution

\[
g_\mu(v)=\frac{e^{-\mu|v|}}{2\mu},
\qquad K_\mu h=\int_{\mathbb R}g_\mu(v)h(\,\cdot-v)\,dv.
\tag{9}
\]

This is a strong vector integral. Since |(log√wα)′|≤B₀ almost everywhere, translations have norm at most e^{B₀|v|}; the kernel is integrable against this weight. The translation identity

\[
\ell_{\rho,j}(T_vh)=e^{z_\rho v}
\sum_{k=0}^j\binom jk v^{j-k}\ell_{\rho,k}(h)
\]

and the complete annihilator show that Vχ is invariant. Consequently (9) induces a bounded quotient operator Kχ.

The weak-domain calculation of MAS-10 depends only on the real Lipschitz function log√w, not on the triviality of the character. Under U=√wα, let D=∂−b with b=(log√wα)′. For y=Kμh, the weighted convolution bounds give y,y′,y″ in Hα and (μ²−∂²)y=h. Integration by parts after applying U yields the same sector estimate

\[
\Re\langle K_\mu h,h\rangle\ge0,
\qquad
|\Im\langle K_\mu h,h\rangle|
\le c\Re\langle K_\mu h,h\rangle,
\quad c=\frac{B_0}{\sqrt{\mu^2-B_0^2}}.
\tag{10}
\]

Compression to Vχ⊥ preserves (10), and so does taking adjoints. The complete jet action is the Taylor multiplier

\[
F_\mu(z)=\frac1{\mu^2-z^2},
\qquad
K_\chi'\ell_{\rho,j}=
\sum_{k=0}^j\binom jkF_\mu^{(j-k)}(z_\rho)\ell_{\rho,k}.
\tag{11}
\]

If zρ=b+it, then μ²−b²+t²>0, so

\[
\Re\lambda_\rho>0,
\qquad |lambda_\rho|\le
\frac1{\mu^2-1/4+t^2},
\quad\lambda_\rho=F_\mu(z_\rho).
\tag{12}
\]

Entire order one implies

\[
\sum_{\rho\ne1/2}N_\rho|z_\rho|^{-2}<\infty.
\tag{13}
\]

For completeness, divide 𝓕χ(1/2+z) by its central zero first. Jensen's formula bounds its zero count by Oη(R^{1+η}) for every η>0. The dyadic sum of |zρ|⁻² converges on choosing η<1. Since |Re zρ|≤1/2, (12) and (13) give ∑Nρ|λρ|<∞, including the finitely many central jets. Rajan's sharper local zero-count estimate also implies this, but is not needed.

List the independent jets in finite blocks and increasing jet order. Their Riesz representatives have Kχ* invariant finite-prefix spans. Gram–Schmidt therefore gives an orthonormal triangular basis with diagonal entries conjugate to λρ, each repeated Nρ times. The sum of the diagonal of Re Kχ* is finite.

Here is the exact singular-value step, to avoid an inference from eigenvalues alone. If a bounded T satisfies (10), write A=Re T and Q=Im T. A≥0 with finite sum of its orthonormal diagonal implies A^{1/2} is Hilbert–Schmidt. The quadratic-form bounds −cA≤Q≤cA give Q=A^{1/2}CA^{1/2}, with C bounded selfadjoint and ‖C‖≤c. Hence

\[
T=A^{1/2}(I+iC)A^{1/2}\in\mathcal S_1,
\qquad \|T\|_1\le\sqrt{1+c^2}\operatorname{Tr}A.
\]

Applying this to Kχ* proves Kχ is trace class in the actual quotient norm, with

\[
\|K_\chi\|_1\le\frac{\mu}{\sqrt{\mu^2-B_0^2}}
\sum_\rho N_\rho\Re\frac1{\mu^2-z_\rho^2}.
\tag{14}
\]

Compactness now follows. The compact triangular argument from MAS-10 identifies the exact nonzero spectrum and algebraic multiplicities: tail compressions tend to zero in norm, so every fixed nonzero spectral value is contained in a finite triangular prefix. Thus no extra nonzero spectral values or algebraic dimensions can be concealed in a tail. This establishes (14) before any use of an eigenvalue trace formula or Fredholm determinant product.

## 4. Central zeros require the full Riesz projection

Let m=ord_{s=1/2}𝓕χ(s). If m>0, μ⁻² is an eigenvalue of Kχ and I−μ²Kχ is not invertible. Let Pχ,0 be the finite-rank Riesz projection for μ⁻², and set it to zero if m=0. By (11), its transpose is identity on all m central jets and zero on every noncentral jet block. Dense dual jets give

\[
\operatorname{rank}P_{\chi,0}=m
\]

and make Pχ,0 independent of μ. This uses the entire generalized eigenspace. Because Fμ is even, its first derivative at zero vanishes, but its higher even derivatives need not vanish; the central block may contain higher generalized vectors which an eigenvector-only removal would miss.

Define the closed invariant complement and its restricted Green operator by

\[
E_\chi^\circ=(I-P_{\chi,0})E_\chi,
\qquad K_\chi^\circ=K_\chi|_{E_\chi^\circ}.
\]

The complement is not presumed orthogonal. Restriction to a closed invariant Hilbert subspace preserves trace class, and the exact compact spectrum now excludes μ⁻². Therefore

\[
R_\chi=K_\chi^\circ(I-\mu^2K_\chi^\circ)^{-1}
\in\mathcal S_1(E_\chi^\circ).
\tag{15}
\]

On every retained finite jet block, rational composition gives

\[
\frac{F_\mu(z)}{1-\mu^2F_\mu(z)}=-\frac1{z^2},
\]

including every derivative up to the zero multiplicity. This proves independence of μ by dual density. Equivalently, extend Rχ by zero on the removed block; the extended bounded operator has the same full dual action for every μ. Its retained nonzero eigenvalues are −zρ⁻² with full algebraic multiplicity, added if different zeros have the same square.

A norm twist provides a concrete reason not to assume central nonvanishing: if χ=|·|ⁱᵗᵃᵘ, a zero of the base completed Dedekind zeta function at 1/2+iτ becomes central for χ. The original zeta value at 1/2 being nonzero does not exclude this case for arbitrary χ.

## 5. The exact determinant, including genus constants

Set

\[
C_\chi(z)=\mathcal F_\chi(1/2+z),\quad
f_\chi(z)=C_\chi(z)/z^m,\quad
a_\chi=f_\chi(0)=\mathcal F_\chi^{(m)}(1/2)/m!\ne0.
\tag{16}
\]

The partner has the same central order. Dividing the functional equation by z^m and comparing the nonzero constant terms yields

\[
\frac{f_\chi(-z)}{a_\chi}
=\frac{f_{\chi^\vee}(z)}{a_{\chi^\vee}}.
\tag{17}
\]

Thus

\[
\mathcal H_\chi(z)=
\frac{f_\chi(z)f_{\chi^\vee}(z)}{a_\chi a_{\chi^\vee}}
=\frac{f_\chi(z)f_\chi(-z)}{a_\chi^2}
\tag{18}
\]

is even and entire of order at most one, with value 1 at zero. Under (1) and (3), conjugation gives aχ∨=overline(aχ), so its first denominator is |aχ|². Define

\[
G_\chi(w)=\mathcal H_\chi(i\sqrt w)
\tag{19}
\]

by the even power series; it is entire of order at most 1/2 and does not require a branch choice.

Hadamard factorization retains an a priori linear exponential:

\[
\frac{f_\chi(z)}{a_\chi}
=e^{b_\chi z}\prod_{\rho\ne1/2}
\bigl[(1-z/z_\rho)e^{z/z_\rho}\bigr]^{N_\rho}.
\]

Multiplication by the same formula at −z cancels both e^{bχz} and every genus-one convergence factor. By (13) the resulting product converges absolutely and locally uniformly:

\[
\mathcal H_\chi(z)=
\prod_{\rho\ne1/2}(1-z^2/z_\rho^2)^{N_\rho}.
\tag{20}
\]

The ordinary trace-class determinant theorem now applies to the actual operator (15), with its algebraic multiplicities already established:

\[
\boxed{\det_{E_\chi^\circ}(I-wR_\chi)=
\prod_{\rho\ne1/2}(1+w/z_\rho^2)^{N_\rho}
=G_\chi(w).}
\tag{21}
\]

This proves the normalization and excludes a hidden exponential factor. It is more than matching a zero set. No central polynomial is encoded by the determinant: it was explicitly removed in (16), and must be restored separately if one wants the original completed function.

## 6. Paired parity and internal self-dual parity

In the radial gauges, J h(u)=h(−u) is unitary from the χ ambient space to the χ∨ ambient space. Equation (2) pairs a χ zero ρ with the χ∨ zero 1−ρ, with equal multiplicity, and direct substitution gives

\[
\ell_{\chi^\vee,1-\rho,j}(Jh)=(-1)^j\ell_{\chi,\rho,j}(h).
\]

The full annihilator descriptions therefore imply JVχ=Vχ∨. J descends to the actual quotients; evenness of the Green kernel implies JKχ=Kχ∨J. Riesz functional calculus gives the same intertwining for the central projections, and hence J is unitary between the central complements and intertwines Rχ and Rχ∨.

On the labeled direct sum Eχ°⊕Eχ∨°, let

\[
\mathcal J(x,y)=(Jy,Jx).
\]

The even summand is the graph {(x,Jx)/√2:x∈Eχ°}. This graph map is unitary, and conjugates the restricted direct-sum R operator to Rχ. The odd graph has the same property. Therefore

| Actual operator space | Ordinary determinant |
| --- | --- |
| Full single character, with central block removed | Gχ(w) |
| Even summand of the paired direct sum | Gχ(w) |
| Odd summand of the paired direct sum | Gχ(w) |
| Whole paired direct sum | Gχ(w)² |

The table remains valid when the compact restrictions coincide, provided labeled copies and their gauges are kept. “Half” here means half of the labeled partner pair. It does not mean discarding half the zeros of a non-self-dual character itself.

If χ=χ∨ globally, J is an internal unitary involution of Eχ°. The functional equation implies εχ=(−1)^m and fχ even. Every noncentral pair {z,−z} contributes Nρ independent even jets and Nρ odd jets. Projection of the dense jet span onto each parity summand proves completeness there. Consequently

\[
\boxed{\det_{E_{\chi,+}^\circ}(I-wR_{\chi,+})
=\frac{f_\chi(i\sqrt w)}{a_\chi}.}
\tag{22}
\]

Both sides are entire and 1 at zero. Their squares agree by (21), proving equality near zero and then everywhere. The full single-sector determinant is the square of (22). The same noncentral determinant holds on the odd internal summand.

Before removal, central jet j has parity (−1)^j, giving central dimensions ceiling(m/2) and floor(m/2). A self-dual functional equation with root number −1 would force odd m; this is a parity implication, not an assertion that such a root number occurs for the fixed primitive GL(1) characters under discussion. Every central generalized vector is removed before either parity determinant is formed.

The result is for fixed characters. No estimate uniform in conductor or infinity type is asserted. It establishes ordinary Fredholm determinants in the actual quotient metric, but not positivity, selfadjointness or a bounded metric equivalence to the designated positive diagonal model. Those are different claims and are not needed here.

## 7. Exact source locators and verification limits

### Masullo, supplied draft

The supplied extraction work/masullo_full.txt was reread at the following printed locations:

- Page 445, equations (10.2.2.1)–(10.2.2.2): the actual Hilbert quotient and its compact-character sectors.
- Page 445, Notation 10.2.2.1: selection of a unitary base point in each component.
- Page 446, Theorem 10.2.2.1 and equations (10.2.2.4)–(10.2.2.6): spectral jets, full interior multiplicities, independence and the asserted Markushevich basis.
- Pages 440–441, Remark 10.2.1.2: Hilbert-dual density used in the quotient argument.

These are conditional source claims. This note proves the character determinant consequence from them; it does not certify the source theorem's proof. The nuclearity theorem is unused.

The meaning of “completed zeros” was checked directly, not inferred from the title of Theorem 10.2.2.1. Definition 3.2.1.2, page 123, calls the product (3.2.1.2), including archimedean factors (3.2.1.3)–(3.2.1.5), L(s,χ). Definition 3.2.1.4 separately defines the finite Lf. Thus our Λχ is 2^{r₂}Qχ^{s/2} times the source's completed function. This is nowhere-zero multiplication. For χ=|·|ⁱᵗᵃᵘ, Proposition 3.2.1.3(2), page 123, gives exactly the poles −iτ and 1−iτ with nonzero residues. The statement of Theorem 7.1.4.2(1), page 326, uses the ideal generated by (s+iτ)(1−s−iτ)L(s,χ), which equals −pχ(s)L(s,χ). This confirms that pole clearing adds no zeros and that the source's spectral jets have exactly the zero multiplicities of 𝓕χ. The draft's product display (7.1.4.9), including its zero-pairing convention, is not used for either growth or normalization; equations (18)–(21) are independently derived from the classical order-one theorem and Hadamard factorization.

### Primary classical sources

**B. Poonen, 18.786: Number Theory II, MIT lecture notes.** [Author PDF](https://math.mit.edu/~poonen/786/notes.pdf). Section 4.7, printed pages 19–22, defines the finite factors and ΓR, ΓC and derives the shifted real/complex factors. Theorem 5.16, printed pages 34–37, supplies global continuation and poles. Definition 5.20 and Theorem 5.22, printed pages 38–39, give the global Euler product and functional equation. Local conductor and Gauss-sum calculations are in §4.8, printed pages 21–24. These verify the factor/pole convention in (1)–(3).

**C. S. Rajan, “Distribution of values of Hecke characters of infinite order,” Acta Arithmetica 85 (1998), 279–291, DOI 10.4064/aa-85-3-279-291.** [Publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/85/3/110150/distribution-of-values-of-hecke-characters-of-infinite-order); [author-upload full text](https://www.researchgate.net/publication/266311380_Distribution_of_values_of_Hecke_characters_of_infinite_order). Section 1, printed pages 281–282, gives the unitary completion, contragredient functional equation and conductor. Page 282 states the entire-order-one assertion for the pole-cleared completion of normalized characters and the genus-one Hadamard product. Equation (2), pages 282–283, gives a local zero count Oχ(log(|t|+2)) for fixed χ. The norm-twist extension and the weaker summability deduction (13) were proved above. The publisher's PDF returned HTTP403; the full text was read from the explicitly author-uploaded copy, not from a citation in a third-party paper.

**NIST DLMF, §25.15.** [Official page](https://dlmf.nist.gov/25.15). Equations (25.15.5)–(25.15.6) specify the primitive Dirichlet functional equation and Gauss sum. The distinction between principal and nonprincipal analytic continuation appears before (25.15.2). Equation (25.15.9) gives L(1,χ)≠0 for nonprincipal χ; it was not used as a source for the whole vertical line.

**K. S. Kedlaya, Notes on analytic number theory, Chapter 6.** [Author chapter](https://kskedlaya.org/ant/chap-funceq2.html). Equations (6.1.4) and (6.2.2) give the even and odd primitive functional equations, checking the i^κ and q/π constants in (4)–(5).

The working draft's complex gamma convention omits the factor 2 and its raw completed L may omit the conductor power. This note uses the explicit completion (1) before taking normalized products. Its zeros, multiplicities and central order coincide with the source's completed zero data. Primitive finite Euler factors are retained throughout; an imprimitive L-function has extra Euler-factor zeros and is not silently substituted.

## 8. Relation to Grothendieck's framework

MAS-11 gives analytic trace-class realizations of completed rank-one Hecke L-functions on the specified adelic Hilbert quotients. The new work establishes the singular-value condition that allows the ordinary Fredholm machinery in cote 1 to apply. Its exterior-power coefficients and trace-logarithm formula then govern the character operators and their parity restrictions.

Rank one refers to the local character representations defining the Euler factors. The construction does not supply a constructible ℓ-adic complex on Spec O_F, an arithmetic cohomology with Frobenius or an arithmetic correspondence whose determinant has been identified with (21), or a motive identified with the Hilbert quotient. The geometric comparison retains that precise missing identification. The analytic character determinant step is closed conditional on the spectral-annihilator theorem; a geometric realization is not a consequence of its determinant identity.

## 9. Check result

The entire proof was read through after writing. Checks covered the unitary norm-twist gauge, dual sector convention, strict inclusion of all completed zeros in the chosen strip, real-part sector bound, trace-ideal factorization, compact triangular multiplicities, full central Riesz removal, independence of μ, the residual Hadamard exponential, partner parity, internal self-dual parity, and coincident compact restrictions. No generalized similarity theorem was attempted. The parent should independently verify the integration-ready TeX before folding MAS-11 into the master.
