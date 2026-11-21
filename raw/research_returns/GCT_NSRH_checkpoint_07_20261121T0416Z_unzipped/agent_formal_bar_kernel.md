# F56 supplement: a formal bar compatible with the actual rank-three action

Author: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed. Run `GCT_NSRH_20261121`. Date: 2026-11-21 UTC.

This is a separate supplement to the fully reviewed F56 report. It distinguishes an entrywise graded duality from the transpose-dual adjoints discussed there. It proves formal bar compatibility for the constructed category and its action, with the actual F43 bar after decategorification. It does not identify VIII's designated integral forms or canonical basis, and does not change the established Karoubi or adjoint conclusions.

## 1. Statement and conventions

Let `V` be finite-dimensional Z-graded vector spaces over a characteristic-zero field `k`, with degree-preserving maps and ordinary tensor symmetry, without Koszul signs. For a graded space define

\[
 (U^*)_d=\operatorname{Hom}_k(U_{-d},k).
\]

Use F56's finite-state matrix-kernel category, with

\[
 (K\star L)_{ij}=\bigoplus_h K_{ih}\otimes L_{hj}.
\]

**Proposition B1.** The entrywise rule

\[
 \mathsf B(K)_{ij}=K_{ij}^*,\qquad
 \mathsf B(f)_{ij}=f_{ij}^*
 \tag{B1}
\]

is a contravariant strong monoidal functor preserving the order of kernel multiplication. Its canonical double-dual map is a coherent monoidal involution. It restricts to F56's positive word categories `P64` and `P6`, reverses grading shifts, and fixes the two named kernel objects up to specified symmetric self-duality maps.

On split K0 it sends an actual Laurent matrix to its entrywise substitution `v -> v^-1`. Under F56's identification with the actual word algebra, this is the actual F43 bar: the named generators are fixed. The corresponding duality on the row action fixes the64 state classes and gives the actual semilinear tensor bar in the F43 basis after the already proved localization.

The explicit quadratic and degree-five relation maps, their coefficient permutations, and their ordered overlap comparisons are carried to their inverse maps under these self-dual identifications. This bar is not the transpose-dual adjoint and does not make the named generators self-adjoint.

## 2. The contravariant monoidal structure

For every pair of entries use the degree-preserving pairing map

\[
 K_{ih}^*\otimes L_{hj}^*
   \longrightarrow (K_{ih}\otimes L_{hj})^*,
 \qquad
 \phi\otimes\psi\longmapsto
       [u\otimes w\mapsto\phi(u)\psi(w)].
\]

Taking the finite direct sum over `h` gives an isomorphism

\[
 \mu_{K,L}:\mathsf B K\star\mathsf B L
       \xrightarrow{\sim}\mathsf B(K\star L).
 \tag{B2}
\]

The finite-dimensional and finite-state hypotheses make duals commute with these finite direct sums. There is no transpose of `i,j`, and the kernel order remains `K,L`. The usual convention identifying `(U tensor V)^*` with `V^* tensor U^*` gives the same map after ordinary coefficient symmetry; it does not reverse matrix multiplication.

The unit map is the identity `k -> k^*` given by evaluation against scalar multiplication on each diagonal entry. For entrywise maps `f:K -> K'` and `g:L -> L'`, the naturality identity is

\[
 \mathsf B(f\star g)\mu_{K',L'}
   =\mu_{K,L}(\mathsf Bf\star\mathsf Bg).
 \tag{B3}
\]

Both sides pair with an input tensor by applying `f,g` to its two factors. For a triple kernel product, both monoidal coherence routes give the functional

\[
 u\otimes w\otimes z\longmapsto
       \phi(u)\psi(w)\chi(z)
\]

in the same flattened intermediate-state summand. This proves the associativity coherence; the unit coherence is scalar multiplication by1. Iterated products are treated by the same ordered path expression. This is a direct proof of strong monoidality as a functor from the opposite category with the same object multiplication.

Let

\[
 \eta_K:K\longrightarrow\mathsf B^2K,
 \qquad \eta_K(u)(\phi)=\phi(u)
 \tag{B4}
\]

entrywise. It is natural. The tensorator on `B^2` is

\[
 \mu^{(2)}_{K,L}
  =\mathsf B(\mu_{K,L})^{-1}
       \circ\mu_{\mathsf B K,\mathsf B L}.
\]

Direct evaluation on pure tensors gives

\[
 \eta_{K\star L}
       =\mu^{(2)}_{K,L}(\eta_K\star\eta_L),\qquad
 \mathsf B(\eta_K)\circ\eta_{\mathsf B K}
       =\operatorname{id}_{\mathsf B K}.
 \tag{B5}
\]

For the second identity, its value on `phi` at `u` is `eta_K(u)(phi)=phi(u)`. The unit has the same identity. These are the monoidal double-dual and involutive coherence conditions, rather than only an objectwise claim that a space is isomorphic to its double dual.

## 3. Specified self-dual coefficient spaces

For `r=1,2`, give `A_r=k<-r> direct-sum k<r>` the ordered homogeneous basis `e_{r,-},e_{r,+}` and the symmetric degree-zero form

\[
 b_r(e_{r,-},e_{r,+})=b_r(e_{r,+},e_{r,-})=1,
 \qquad b_r(e_{r,-},e_{r,-})=b_r(e_{r,+},e_{r,+})=0.
 \tag{B6}
\]

It is nondegenerate. Define `theta_r:A_r -> A_r^*` by `theta_r(x)(y)=b_r(x,y)`. In particular it exchanges the opposite-degree dual basis labels. Symmetry is precisely

\[
 \mathsf B(\theta_r)\eta_{A_r}=\theta_r.
 \tag{B7}
\]

On `D=A1 tensor A1`, use the product form

\[
 b_D(x_1\otimes x_2,y_1\otimes y_2)
      =b_1(x_1,y_1)b_1(x_2,y_2).
\]

Its self-duality map is `theta_D=mu_(A1,A1)(theta_1 tensor theta_1)`. It pairs the two distinct degree-zero labels with one another, and pairs the degree minus-two label with the degree two label. Thus those degree-zero labels are retained, not collapsed to their common degree.

Apply these maps entrywise to each `K_i`: its nonzero entries are exactly `D` or the branch's `A1,A2`, with scalar-plus `D` and scalar-minus zero. This gives `theta_i:K_i -> B K_i`. The unit has the ordinary scalar form. Tensor products use product forms, and direct sums use orthogonal sums. The monoidal structure gives a specified self-duality of every unshifted word by retaining its state path and the ordered coefficient pairings. Its symmetry follows from the symmetry of the product form on each path summand.

There is a natural identification

\[
 \mathsf B(K\langle d\rangle)
       \simeq (\mathsf B K)\langle-d\rangle.
 \tag{B8}
\]

Therefore duality sends every finite sum of shifted word objects to an object of the same positive word category. It also sends their morphisms to morphisms because that category is full in the matrix-kernel category. Closure under isomorphism handles any alternate presentation of such an object. No choice of a presentation is used to define the functor `B` itself.

## 4. Relation maps and their inverses

Give the two sides of each F56 relation their product and orthogonal-sum forms just specified. Every flattened associator preserves its path and product pairing. Every ordinary coefficient permutation is an isometry of these forms: multiplication of the scalar pairings is commutative, and there is no Koszul sign.

For the quadratic map, the right-coefficient version is path identification; the left-coefficient version only interchanges the initial edge and the extracted `D`. Each is an isometry. The two triple-reduction outputs differ by the transposition of the two separately labeled loop coefficients, which is also an isometry, with its actual nontrivial action retained.

For the degree-five relation, recall `U=A1^2`, `V=A2^2`. On the first branch the map is the summand permutation `(1 2)(3 4)` with identity coefficient maps. On the second branch it sends summands `1,2,3,4` to `3,4,1,2` and interchanges `U,V` on the two mixed summands. These are all isometries for the product forms. The scalar-plus terms are identities and the minus terms are zero. Thus the complete natural relation map is an isometry, not merely a map between spaces of equal dimension.

In detail, for any such map `r:C -> C'` the isometry equation is

\[
 \mathsf B(r)\,\theta_{C'}\,r=\theta_C.
\]

Since `r` is invertible, this is exactly

\[
 \theta_C^{-1}\,\mathsf B(r)\,\theta_{C'}=r^{-1}.
 \tag{B9}
\]

The same argument covers the ordered overlap comparisons and unshifted word contexts equipped with the displayed self-dual product forms. Hence these actual named maps dualize to their inverses. For arbitrary shifted or summed contexts `H,J`, the dual of `id_H star r star id_J` instead identifies, by monoidality and the self-duality of the two relation objects only, with `id_(B H) star r^-1 star id_(B J)`. This is the inverse relation map on the corresponding dual contexts; their grading shifts reverse. It is not a claim that every shifted object is self-dual. No unspecified additional higher relation is supplied by this observation.

## 5. Actual bar on the algebra and its state module

Entrywise graded duality has character

\[
 \operatorname{ch}(\mathsf B K)_{ij}(v)
       =\operatorname{ch}(K)_{ij}(v^{-1}).
 \tag{B10}
\]

Its monoidality and additivity therefore give the semilinear ring involution on split K0 with `v -> v^-1` and the two classes `[K_i]` fixed. Under F56's exact character embedding, it is the actual coefficientwise bar on `A_Lambda^act`, not an anti-automorphism reversing words.

On the row category `V^I`, set `(B_I X)_i=X_i^*`. The same pairing gives a natural comparison

\[
 T_{\mathsf B K}(\mathsf B_I X)
       \xrightarrow{\sim}\mathsf B_I(T_K X).
 \tag{B11}
\]

Its unit and action-associativity diagrams agree on the same state-path pure tensors, and its double-dual compatibility follows from(B5). On the Grothendieck module this is coefficientwise `v -> v^-1`, with each degree-zero state class fixed.

F43 proved that the actual tensor bar fixes every vector of the chosen64-state basis and that its right generator matrices are the displayed Laurent matrices. Identifying the state classes with that basis therefore identifies(B10)--(B11) with the actual semilinear bar and its actual action compatibility on the full-rank lattice spanned by those vectors. The already proved localization is bar stable and makes this the actual entire tensor lattice there. This is an equality of the resulting decategorified bar maps; it is not an assertion that graded vector-space duality is literally the original semilinear map on quantum tensor vectors before this comparison.

## 6. Adjoints, arithmetic transport, and remaining limits

The ambient action adjoint is the transpose graded dual

\[
 (K^\dagger)_{ij}=(K_{ji})^*.
\]

It is different from(B1). Its state transpose changes the supports of the reset kernels. The F56 positive-word argument proving `K_i^dagger` absent from the word category remains valid. The existence of the entrywise bar does not produce adjunction evaluations, identify `K_i` with its adjoint, or make the category closed under arbitrary summands. The previously computed Karoubi normalization and collision loss are unchanged. The symmetric bilinear forms used for these coefficient identifications are not positive Hermitian polarizations.

Under F56's fixed-q coefficient functor, `B` sends the arithmetic line of degree `d` to the line of degree `-d`. Entrywise F53 transport gives the corresponding internal coefficient duality on the perverse image. It is not asserted to be the ambient Verdier dual: F53 distinguishes the internal dual, the Gaussian/Verdier dual and the reciprocal weight dual. No new pointwise estimate or single weight for a mixed total is obtained.

The construction closes a formal bar comparison for these rank-three kernels. It still does not identify VIII's designated global and local lattices, its simple labels, canonical bases, or compatible graded kernels through all tensor degrees. In particular the intrinsic global-form obstruction of F49 is not removed by formal bar compatibility alone.

## 7. Separate Grothendieck dictionary

Finite graded coefficient spaces are representations of a split one-dimensional torus. Their linear dual reverses the character lattice; evaluation into the double dual and the product pairing supply the exact functorial structures proved above. This is the finite locally free representation language of the already audited SGA3 I4.7.2--3/cote90 scan17 framework. On the coefficient Grothendieck ring it gives the involution `v -> v^-1`; SGA6 V sections2--3/cote133 scan18 is the existing representation/lambda/sigma vocabulary, not a claimed lambda-ring structure on the noncommutative matrix-word algebra.

The actual action and its localized lattice are affine module data in the established EGA I Theorem1.3.7, Corollary1.3.8 and Theorem1.4.1 dictionary. The full monoidal and inverse-map proofs are given here and are not attributed to an unpublished manuscript. The duality is entrywise and contravariant; it is neither the transpose action adjoint nor an unproved identification with Verdier duality or VIII's designated global basis.

## 8. Author proof check

The author reconstructed the variance and tensorator directions, naturality, both double-dual coherence equations, the symmetric coefficient forms including the two distinct zero-degree loop labels, both degree-five branch maps and their isometry equations, the row action, and the exact F43 bar comparison. No numerical test is needed for these tensor identities. A fresh independent whole-proof check is requested before integration. The reviewed F56 report and fragment are unchanged by this separate supplement.
