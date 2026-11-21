# F31 proposal: primitive Grassmannian objects for equal rectangles and two-row outputs

Author: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed. Date: 21 November 2026. The Kronecker difference formula and hard Lefschetz are cited known theorems. The contribution here is the precise finite-field/motivic realization, explicit projector, and scope comparison; no historical novelty is claimed for this classical geometric interpretation.

## 1. Exact known coefficient formula

Let `n,d>=1`, put `N=nd`, and let `0<=r<=floor(N/2)`. Write `p_r(n,d)` for the number of partitions of r inside the rectangle with n rows and d columns, and set `p_{-1}=0`. The known two-coefficients identity is

\[
g((N-r,r),(d^n),(d^n))=p_r(n,d)-p_{r-1}(n,d).
\tag{GP1}
\]

The zero second row is omitted when r=0. A precise primary locator for `r>=1` is Igor Pak and Greta Panova, *Bounds on certain classes of Kronecker and q-binomial coefficients*, author manuscript dated 13 October 2016, **Lemma 1.3 (Two Coefficients Lemma), p.2**, <https://www.math.ucla.edu/~pak/papers/QBC23.pdf>. The statement itself attributes earlier general proofs to Vallejo §7 and their preceding paper; we do not claim that Pak–Panova first discovered every case. Their *Unimodality via Kronecker products*, author PDF <https://www.math.ucla.edu/~pak/papers/Unimodality11.pdf>, gives the general difference in **Lemma3.1, p.4**, and identifies the rectangle counts in **Corollary4.1 and its proof, p.5**. These are manuscript page numbers, not guessed published pagination.

A recent primary restatement covering the present notation is Pak–Panova–Swanson, *A combinatorial interpretation for certain plethysm and Kronecker coefficients*, 4 November 2025, arXiv:2511.02312, **Lemma1.3, equation(2), p.2**, <https://www.math.ucla.edu/~pak/papers/plethysm-Kronecker-trees.pdf>. We invoke GP1, and do not re-prove it as a new result. The r=0 assertion is also immediate from the trivial representation occurring once in the tensor square of a Specht representation.

## 2. The actual pure Weil object and an explicit primitive projector

**Proposition GP-A.** Let `X=Gr(n,n+d)` be the split Grassmannian over `F_q`, and let `ell` be a prime different from the characteristic. Let `L=c_1(O_X(1))` be the Plücker class, in `H^2(X_bar,Q_l(1))`. Then

\[
C_r=\operatorname{coker}\bigl(
L:H^{2r-2}(X_{\overline{\mathbf F}_q},\mathbf Q_\ell)(-1)
\longrightarrow H^{2r}(X_{\overline{\mathbf F}_q},\mathbf Q_\ell)
\bigr)
\tag{GP2}
\]

is an actual finite-dimensional Weil module. For r=0 the source is zero. It has the exact form

\[
C_r\simeq\mathbf Q_\ell(-r)^{\oplus g((N-r,r),(d^n),(d^n))}.
\tag{GP3}
\]

In particular it is pure of weight `2r`, its geometric Frobenius is the scalar `q^r`, and at extension degree a its trace is `g((N-r,r),(d^n),(d^n)) q^{ar}`.

The quotient is canonically isomorphic to the primitive kernel

\[
P^{2r}=\ker\bigl(
L^{N-2r+1}:H^{2r}(X_{\bar{\mathbf F}_q},\mathbf Q_\ell)
\longrightarrow H^{2N-2r+2}(X_{\bar{\mathbf F}_q},\mathbf Q_\ell)(N-2r+1)
\bigr).
\tag{GP4}
\]

For a concrete projector, normalize all weights by putting `V_j=H^{2j}(X_bar,Q_l)(j)`. Cup product with L is a Frobenius-equivariant map `L:V_{j-1}->V_j`. For `1<=r<=floor(N/2)` set

\[
A_r=L^{N-2r+1}:V_r\longrightarrow V_{N-r+1},\qquad
B_r=L^{N-2r+2}:V_{r-1}\longrightarrow V_{N-r+1}.
\]

Then B_r is invertible, and

\[
E_r=\operatorname{id}_{V_r}-L B_r^{-1}A_r
\tag{GP5}
\]

is the Frobenius-equivariant idempotent with image `ker A_r` and kernel `L V_{r-1}`. For r=0 take `E_0=id`.

**Proof.** First, the split Grassmannian has a Tate motive, with p_j(n,d) summands of degree2j. We make this arithmetic statement precise rather than infer arithmetic semisimplicity from purity alone. Let the split multiplicative group act on the ambient `(n+d)`-dimensional space with distinct weights `1,2,...,n+d`. A fixed n-plane is a sum of weight lines, hence is a coordinate plane indexed by `I={i_1<...<i_n}`; these are rational points over F_q. Its tangent space is `Hom(U_I,k^{n+d}/U_I)`, with weights `j-i` for `i in I`, `j not in I`. The dimension of the positive weight space is

\[
a_I=\sum_{s=1}^n\bigl(d+s-i_s\bigr).
\]

The numbers `lambda_s=d+s-i_s` form a partition with `d>=lambda_1>=...>=lambda_n>=0`, and every such partition arises uniquely. Thus a_I=j occurs p_j(n,d) times. Brosnan's motivic Białynicki–Birula theorem, **Theorems3.3 and3.5, author PDF pp.5–6**, gives a direct sum of Tate motives over the original field, with exactly these multiplicities. In Brosnan's homological notation this is `M(X)=direct_sum_j Z(j)^{p_j}`. In the cohomological convention used here, each such Lefschetz summand realizes to Q_l(-j) in degree2j. Hence

\[
H^{2j}(X_{\bar{\mathbf F}_q},\mathbf Q_\ell)
\simeq \mathbf Q_\ell(-j)^{\oplus p_j(n,d)},
\qquad H^{2j+1}(X_{\bar{\mathbf F}_q},\mathbf Q_\ell)=0,
\tag{GP6}
\]

with scalar geometric Frobenius q^j. This is also the familiar split Schubert-cell computation. The motivic theorem supplies the actual arithmetic direct sum; a merely filtered collection of equal eigenvalues would not by itself exclude Jordan extensions.

The scheme X is smooth projective of dimension N, and the Plücker line bundle is ample and defined over F_q. Thus hard Lefschetz applies to its constant intersection complex `Q_l[N]`. A precise primary weight-theoretic locator is **BBD Theorem5.4.10, p.144**, applied to `X->Spec F_q` and the pure perverse sheaf `Q_l[N]`. It makes B_r an isomorphism. Since `A_r L=B_r`, the map `L:V_{r-1}->V_r` is injective, and direct calculation gives

\[
E_r^2=E_r,\quad A_rE_r=0,\quad E_rL=0,
\quad E_r|_{\ker A_r}=\operatorname{id}.
\]

More explicitly, `(L B_r^{-1}A_r)^2=L B_r^{-1}(A_rL)B_r^{-1}A_r=L B_r^{-1}A_r`. This proves the direct sum

\[
V_r=L V_{r-1}\oplus\ker A_r.
\]

The quotient therefore has dimension p_r-p_{r-1}, and the restriction of the quotient map to the primitive kernel is an isomorphism. It is canonical after the Plücker class has been fixed. Every V_j has scalar Frobenius1 by GP6, so the quotient and kernel do as well. Untwisting by (-r) proves GP2–GP4, and GP1 identifies their rank with the required Kronecker coefficient. All cup products, inverse maps, and projectors are Frobenius-equivariant in the displayed twisted spaces. ∎

**Why the Tate twist in GP2 matters.** A rationally defined divisor gives an invariant class in `H^2(1)`, so its equivariant untwisted-target map is `H^{2r-2}(-1)->H^{2r}`. The common informal quotient `H^{2r}/L H^{2r-2}` specifies the underlying vector-space image, but omits the twist needed to make the source-to-target map a morphism of Weil modules. In GP5 all spaces were twisted to weight zero precisely to remove that ambiguity.

## 3. An actual rational Chow-motive summand, without the standard conjectures

The same projector is algebraic in this particular cellular case. Write `mathbb L` for the Lefschetz motive, whose cohomological realization is Q_l(-1) in degree2. Over F_q, the cited motivic decomposition gives

\[
h(X)\simeq\bigoplus_{j=0}^{N}(\mathbb L^j)^{\oplus p_j(n,d)}.
\]

Use rational coefficients. Between sums of a fixed Tate motive every morphism is a rational matrix, and `End(mathbb L^j)=Q`; between distinct Tate degrees the degree-zero Hom vanishes. After normalizing the degree pieces by their Tate powers, the Plücker maps in GP5 are rational matrices. Equivalently, take Schubert cycle bases, in which multiplication by the Plücker class has integral entries. B_r has nonzero determinant by hard Lefschetz, so its inverse is a rational matrix and therefore an actual morphism in this Tate subcategory. The matrix E_r is an actual algebraic idempotent; taking its image gives a rational Chow motive

\[
\mathsf P_r\simeq (\mathbb L^r)^{\oplus g((N-r,r),(d^n),(d^n))},
\]

whose realization is C_r. One may construct its correspondence using the Schubert cycles and their dual cycles, so all data remain defined over F_q.

This argument does **not** assert the algebraicity of the Lefschetz inverse for an arbitrary smooth projective variety. It uses the full matrix Hom spaces of this explicitly Tate motive. Rational coefficients are essential to the specified projector in general; no integral hard-Lefschetz splitting is claimed. Brosnan §2, pp.3–4, gives the category of correspondences, idempotent completion, and integral-to-rational convention; Theorem3.5 supplies the required decomposition.

## 4. Exact integral and basis limitations: Gr(2,4)

Take n=d=r=2, so N=4. Let `sigma_2,sigma_11` be the degree-four Schubert basis, and `sigma_1` the Plücker class. The ordinary Schubert/Pieri products are

\[
L\sigma_1=\sigma_2+\sigma_{11},\qquad
L\sigma_2=L\sigma_{11}=\sigma_{21}.
\]

Thus `p_2-p_1=2-1=1`, and the primitive line is spanned by `sigma_2-sigma_11`. In the ordered basis `(sigma_2,sigma_11)`, GP5 is

\[
E_2=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\tag{GP7}
\]

Its negative entries and denominators are visible, despite its image being an actual pure Tate line. In the integral Schubert lattice,

\[
L H^2_{\mathbf Z}=\mathbf Z(\sigma_2+\sigma_{11}),\qquad
P^4_{\mathbf Z}=\mathbf Z(\sigma_2-\sigma_{11}),
\]

and their sum has index2 in `H^4_Z`. Here H_Z may be read as the integral Chow/cycle lattice, or the integral cohomology of the complex Grassmannian; the same obstruction is visible over Z_2. Consequently the **specified primitive-versus-Lefschetz decomposition** does not split that integral lattice.

This is not an obstruction to every integral projector onto the primitive line. For example `[[1,0],[-1,0]]` is an integral idempotent with that image and a different kernel. The obstruction concerns the prescribed kernel `L H^2`, and GP7 concerns its Schubert-matrix entries. In particular, one must not infer nonnegative canonical-basis matrices from the purity or motivic existence of the image.

The two displayed Pieri products are the ordinary add-one-box rule; a primary general statement already checked in this run is Alex Postnikov's 2014 MIT18.315 lecture notes, scribed by Carl Lian, Theorem7.10, p.16, together with the standard Schubert interpretation. The Grassmannian geometry and integral Schubert basis are also treated in Brion, *Lectures on the geometry of flag varieties*, §1.1 and §1.3; his author PDF is over C, whereas the finite-field assertion above uses Brosnan's arbitrary-field theorem.

## 5. Scope relative to Ikenmeyer–Panova and the nonstandard gate

The two equal rectangular factors have arbitrary height n and width d, so this is a family beyond merely imposing height at most two on all tensor factors. Its limitation is the third partition: `(nd-r,r)` has at most two rows, equivalently the padded tail has at most one part.

By contrast, the supplied Ikenmeyer–Panova manuscript allows a general tail `bar(lambda)` subject to `|bar(lambda)|<=md` and `length(lambda)<=m^2` in its relevant padded-permanent range, and its Kronecker positivity theorem also assumes `d>3m^3`, `n>3m^4` outside its finite exceptional set. Exact supplied-source locators are `main.tex`, theorem labels `thm:kadishlandsberg` and `thm:secondmain`, lines397–420. GP-A realizes the single-part-tail subfamily whenever `r<=min(md,floor(nd/2))`; it does not supply a primitive-Grassmannian formula for arbitrary multipart tails. Its own construction needs no IP size threshold.

The finite-dimensional pure Tate object and explicit rational primitive projector are genuine geometric data. They do not identify VIII's nonstandard canonical bases, their transition or multiplication coefficients, or the geometric path counts required by the sign-only criterion. The purity here uses classical hard Lefschetz and the split Grassmannian motive; it is not obtained anew by the path argument. Nor does dimension equality choose a canonical isomorphism with the Satake multiplicity space of F20. Their normalizations have different Tate weights: in the GL_n times GL_n construction for the two rectangles `(d^n)`, F20's natural coefficient has weight `2nd(n-1)`, while this Grassmannian coefficient has weight `2r`. A suitable Tate twist aligns weights but does not select a basis or an action comparison.

### Known positive formulas for this family

The 2025 Pak–Panova–Swanson paper goes further on the combinatorial side: **Theorem1.1, p.1 / Theorem4.5, p.9**, gives a positive marked-KOH-tree formula for GP1; **Theorem1.2, p.1 / Theorem5.2, p.10**, gives a marked-GOH-tree formula for two-row-output plethysm, with the reduction of general inner shapes in **Lemma2.1, pp.4–5**. These are literature results, not consequences of GP-A and not results proved by this investigation. Definition4.4, p.9, specifies the marks; §2.2, p.5, discusses computation via polynomial expansions in numerical parameters. That discussion does not by itself provide the succinct bit-length PH1/Ehrhart apparatus of GCT VI. No blanket claim that this two-row family's positive combinatorial interpretation is open should remain.

The statement of Lemma4.2 uses the correct cumulative mark `k_i` in its upper bound. Its short proof appears to print `k_t` in the final substitution where `k_{t-1}` is required; no argument here relies on that typo. I checked the cited statements and exact locators, not a complete independent re-proof of the whole tree paper.

## 6. Grothendieck-framework dictionary and primary source audit

- **Schemes over Z and FGA.** The integral Grassmannian is the parameter scheme of rank-d locally free quotients of `O_Z^{n+d}` (equivalently rank-n subbundles). It is a special projective Quot scheme with its universal exact sequence and Plücker line. The framework locator is FGA, Exposé221, §3, Theorems3.1–3.2, pp.259–260, whose primary statements were checked earlier. This is actual projective geometry, not an assumed geometric model of a noncommutative bialgebra.
- **SGA3 and group actions.** The split group scheme GL_{n+d,Z} acts, and the cocharacter `t->diag(t,t^2,...,t^{n+d})` gives the G_m-action used above. SGA3, ExposéI, 4.7.1–4.7.3 supplies the already checked representation/comodule and diagonalizable-grading language.
- **Étale weights and Lefschetz.** GP2 is a cokernel in actual finite-dimensional Weil modules, GP5 an equivariant projector, and GP3 states the exact weights and Frobenius eigenvalues. BBD Theorem5.4.10, p.144, supplies hard Lefschetz under its full projective/ample/pure-perverse hypotheses. The split Tate statement comes from Brosnan, not from an invalid implication that purity alone forces semisimplicity.
- **Motives and K0.** The image of GP5 in the rational Tate category is an effective motive with class `g [mathbb L^r]`; its positive cone is the cone of actual Tate direct sums. The inherited Schubert-matrix entries need not be nonnegative, as GP7 proves.
- **Archive anchor.** Cote16, visually checked manuscript scans35,37,39 (PDF pages36,38,40), contains Lefschetz/primitive-projector language. It is a framework anchor for GP4–GP5, not evidence that this Kronecker identity or this proof is present in the manuscript. Reused backs34,36,38,40 must not be cited as those handwritten computations.

Primary web retrieval refs available to the root (open them before citing in a final response):

- Pak–Panova QBC23 original author PDF: `turn569762011view0`, `turn610383394view0`, `turn788456201view1`; exact Lemma1.3, p.2.
- Pak–Panova Unimodality11 author PDF: `turn569762011view1`, `turn788456201view2`; Lemma3.1, p.4 / Corollary4.1, p.5.
- Pak–Panova–Swanson author PDF: `turn431925467view0`, `turn569762011view4`, `turn788456201view3`; exact pages/locators above.
- Brosnan original author PDF: <https://math.umd.edu/~pbrosnan/Papers/bb.pdf>, refs `turn177112527view0`, `turn866228929view0`, `turn866228929view1`, `turn788456201view0`. §2 and Theorems3.2–3.5 read. Theorem3.5 is author PDF p.6; Theorem3.3 p.5. Publication is Inventiones Mathematicae161(2005),91–111, but no published page conversion is asserted here.
- Brion author PDF: <https://www-fourier.univ-grenoble-alpes.fr/~mbrion/lecturesrev.pdf>, refs `turn481026880view0`, `turn177112527view1`, `turn866228929view3`. Used only for conventional Schubert geometry, not as an arbitrary-field theorem.
- BBD original numdam PDF/local `primary_sources/BBD.pdf`, Theorem5.4.10 p.144, reread in this check. General theorem invoked, not reproved.

All new algebraic steps in GP-A, GP5, the rational Tate-projector argument, and the index-two example have complete proofs above. A fresh independent review remains to be recorded before insertion into a final package.
