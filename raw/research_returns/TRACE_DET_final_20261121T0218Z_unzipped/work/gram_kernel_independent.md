# Independent check of the actual signed Gram kernel and projection formula

Date: 2026-11-21. Checker: GPT-6 Astra Pro, effort not exposed, `/root/step1_history_route/gram_kernel_check`.

## Result and scope

Both proposed claims are correct. The conditional-negative-type obstruction is exactly **8 sinh⁴(a)**. All proposed conjugations in the projection formula are correct in the source's **linear-first** convention. Two wording corrections are necessary: write `U = im(E) + im(F)` for the sum of subspaces, and call `U⊥ ∩ x⊥` positive definite; the full ambient `x⊥` need not be positive when `r > 0`.

This note supplies complete independent finite-dimensional proofs. It is not a Lean build, an audit of all imported lemmas, or a proof that the proposed projection formula has already been formalized in the repository.

## Source read and exact assumptions

I read the complete supplied `work/paper_actual_determinants.tex` and the complete actual `work/external_lean/lean/src/Formalism/FormalDegreeBessel/StatementG.lean` (174 lines). In the latter:

| Object | Locator | Checked content |
|---|---|---|
| Hermitian convention and unitary group | Lines 9–12, `herm`, `UH` | `h(v,w) = w* H v`, and `g* H g = H` |
| Ambient form and support | Lines 14–31, `Hpk`, `inWb`, `Tz` | Dimension `2r+k+1`; signature `(r+k,r+1)`; middle support; `T = −Re h(z,z)` |
| Pairing matrix and minors | Lines 61–71, `fvec`, `Zhat`, `Dmin` | Left frame `[E,z]`, right frame `[gE,gz′]`; ordinary leading determinants |
| Scalar and full Gram matrix | Lines 85–99, `Gf`, `gramVec`, `gramM` | `Gf = |D_(r+1)|² − TT′ |D_r|²` and `gramM = X* H X` |
| Actual propositions | Lines 165–172, `GGram`, `GNonneg` | Signed Gram identity; nonnegativity for middle-supported `z,z′`, `T,T′ > 0`, and `g* H g = H` |

A targeted text search additionally located `FinalG.lean:21–22`, `ReverseCauchySchwarzHolds.lean:179`, and `GNonneg.lean:302`. In this independent check I located those declarations but did not read their theorem bodies or dependencies. Definitions of propositions alone were not counted as proofs.

Throughout, `*` denotes conjugate transpose, not a scalar conjugation unless the object is scalar. The explicit form is an orthogonal sum of `r` hyperbolic matrices `[[0,1],[1,0]]` and `diag(1^k,−1)`, after reordering coordinates. Thus its signature is `(r+k,r+1)` directly from the definition, without invoking an unverified source theorem.

## DET-12: full proof of the two kernel obstructions

Set `r = 0`, `k = 2`, `g = I`, and `H = diag(1,1,−1)`. The support condition is vacuous. On the domain of negative unit vectors `h(z,z) = −1`, the actual source scalar is

\[
K(z,z')=G_f(2,0,z,z',I)=|h(z',z)|^2-1,
\]

because the empty minor is `D_0 = 1` and `D_1 = h(z′,z)`. Hermitian symmetry makes the order inside the modulus immaterial. In particular `K(z,z) = 0`.

Take

\[
z(t)=(\sinh t,0,\cosh t)^T,\qquad t\in\mathbb R.
\]

Then

\[
h(z(t),z(s))=\sinh s\sinh t-\cosh s\cosh t=-\cosh(t-s),
\]

and therefore

\[
K(z(s),z(t))=\sinh^2(t-s).
\]

For `s ≠ t`, this is strictly positive. A positive semidefinite kernel with zero diagonal has every entry zero: its two-point matrix has determinant `−|K(s,t)|²`, which must be nonnegative. Equivalently, any Hilbert feature map with `K(s,t) = ⟨Φ(s),Φ(t)⟩` would have `‖Φ(t)‖² = 0` for every `t`. Thus this actual rank-zero scalar does not form a positive semidefinite Hilbert Gram kernel on the stated domain.

For conditional negative type, choose points `−a, 0, a` with `a > 0` and real coefficients `(1,−2,1)`, whose sum is zero. Writing `u = sinh²(a)`, `v = sinh²(2a)`, the double sum is

\[
\sum_{i,j=1}^3 c_i c_j K(z(t_i),z(t_j))
=2v-8u
=2\cdot4u(1+u)-8u
=8u^2=8\sinh^4(a)>0.
\]

The required inequality for a conditionally negative kernel is `≤ 0`, so it fails. In particular `K` cannot be a squared Hilbert distance either. Both obstructions already occur inside the real curve above; complex phases and completion questions play no role. The conclusion is an obstruction to these specified kernel interpretations, not to every possible transform or unrelated operator. For `k = 0`, the rank-zero kernel is identically zero, so the nontrivial counterexample explicitly uses a positive direction.

## Projection formula on `D_r ≠ 0`: complete independent proof

Assume exactly the `GNonneg` hypotheses. Set

\[
E=[e_0,\ldots,e_{r-1}],\quad F=gE,\quad y=gz',\qquad
C=E^*HF,\quad b=E^*Hy,\quad c=z^*HF,\quad d=z^*Hy.
\]

Here `b` is a column and `c` is a row. Middle support, isotropy of `E`, and the unitary equation imply

\[
E^*HE=F^*HF=0,\qquad E^*Hz=F^*Hy=0,\qquad
z^*Hz=-T,\quad y^*Hy=-T'.
\]

The actual source pairing matrix is precisely

\[
\widehat Z=\begin{pmatrix}C&b\\c&d\end{pmatrix},
\qquad D_r=\det C.
\]

Suppose `D_r ≠ 0`. The frame `[E,F]` has Gram matrix

\[
\begin{pmatrix}0&C\\C^*&0\end{pmatrix}.
\]

It is nonsingular, so this frame is independent and spans a nondegenerate subspace `U = im(E) + im(F)`. Replacing `F` by `FC⁻¹` gives Gram matrix `[[0,I],[I,0]]`, of signature `(r,r)`. Subtracting these indices from those of `H` shows that `U⊥` has signature `(k,1)`.

Define

\[
\alpha=(C^*)^{-1}c^*,\qquad\beta=C^{-1}b,\qquad
x=z-E\alpha,\quad y_0=y-F\beta.
\]

Then

\[
E^*Hx=0,\quad F^*Hx=c^*-C^*\alpha=0,
\qquad E^*Hy_0=b-C\beta=0,\quad F^*Hy_0=0.
\]

Thus `x,y₀ ∈ U⊥`, and they are the `H`-orthogonal projections of `z,y` onto `U⊥`. Their norms remain unchanged, since each removed vector is isotropic and orthogonal to the original vector:

\[
x^*Hx=-T,\qquad y_0^*Hy_0=-T'.
\]

Since `α* = c C⁻¹`, direct expansion gives

\[
\begin{aligned}
x^*Hy_0
&=d-c\beta-\alpha^*b+\alpha^*C\beta\\
&=d-cC^{-1}b=:s.
\end{aligned}
\]

In the **source's linear-first convention**, this equation is `h(y₀,x) = s`; its conjugate is `h(x,y₀) = s̄`. Consequently the proposed vector

\[
p=y_0+\frac{h(y_0,x)}{T}x=y_0+\frac{s}{T}x
\]

has `h(p,x)=s+(s/T)(−T)=0`. It lies in `U⊥ ∩ x⊥`. Since `x` is negative and `U⊥` has signature `(k,1)`, this latter space is positive definite, with dimension `k`. Expanding the norm yields

\[
h(p,p)=-T'+\frac{|s|^2}{T}\ge0.
\]

The Schur determinant identity gives

\[
D_{r+1}=\det C\,(d-cC^{-1}b)=\det C\,s.
\]

Substitution into the actual definition now proves exactly

\[
\boxed{G_f=|\det C|^2\bigl(|s|^2-TT'\bigr)
=|\det C|^2\,T\,h(p,p)\ge0.}
\]

All conjugations and the plus sign in `p` are therefore correct. In a conjugate-linear-first convention the coefficient must instead be written `⟨x,y₀⟩/T`. On this chart, equality holds precisely when `p = 0`. The positive space and projection depend on the input configuration, so this identity by itself does not supply a fixed positive semidefinite kernel in two inputs; DET-12 rules out that particular interpretation already in rank zero.

## Boundary cases and singular charts

- **`r = 0`:** Interpret the empty matrix `C` as the unique invertible endomorphism of the zero-dimensional space, with determinant `1`. Then `U = 0`, `x = z`, `y₀ = gz′`, and the formula reduces to the usual reverse-Cauchy–Schwarz decomposition in signature `(k,1)`. There is no missing empty determinant factor.
- **`k = 0` and `D_r ≠ 0`:** The space `U⊥` is a negative line. Its orthogonal complement to `x` is zero, so `p = 0` and `Gf = 0`.
- **`D_r = 0`:** The displayed projections are undefined and need not have finite limits. No limiting argument is necessary for nonnegativity: the original polynomial definition gives `Gf = |D_(r+1)|² ≥ 0` immediately. Therefore the chart proof plus this case supplies a complete independent proof of the full source nonnegativity assertion.
- **`T = 0`:** The projection onto `x⊥` used here is not defined by this formula. This is outside the source's strict `T > 0` hypotheses and should not be included without a separate argument. The proof actually does not need `T′ > 0`, but retaining the stated source hypotheses is harmless.

For completeness, `k = 0` also forces `Gf = 0` on the singular chart. The following independent block identity verifies this without an appeal to density. With `m = r+1`, `A = diag(0^r,−T)`, `B = diag(0^r,−T′)`, and `Z = Zhat`, the full Gram matrix is

\[
M=\begin{pmatrix}A&Z\\Z^*&B\end{pmatrix}.
\]

Expanding its determinant in the two possible nonzero entries of `A,B`, the term using neither is `(-1)^m |det Z|²`; a term using just one is zero because the remaining off-diagonal pairing blocks have unequal sizes; and the term using both is `TT′(-1)^r |det C|²`. Hence

\[
\det M=(-1)^{r+1}\bigl(|D_{r+1}|^2-TT'|D_r|^2\bigr)=(-1)^{r+1}G_f.
\]

This independently checks the source's signed Gram identity, including the empty-minor case. If `k = 0`, the `2r+2` Gram vectors lie in dimension `2r+1`, so `det M = 0` and consequently `Gf = 0` everywhere, including `D_r = 0`.
