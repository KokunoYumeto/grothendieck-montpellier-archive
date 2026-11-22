# F59 scalar-complex amendment: the singular factor and the pure coefficient

Author: /root/grothendieck_dictionary, GPT-6 Astra Pro; inherited effort is not exposed. Date: 2026-11-21 UTC.

This is an amendment separate from the frozen scalar-complex report and fragment. It uses their checked generic support theorem SC-A. It gives two further exclusions, neither of which proves an unconditional theorem for every bounded nonfactorable complex with nonflat cohomology.

## 1. No scalar coefficient repairs a scalar multiple of the invariant correspondence

Let k have characteristic zero. Put

\[
 A=k[x,y,z_1,\ldots,z_m],\qquad
 \tau(x,y,z)=(-x,-y,z),\qquad S=A^\tau,
 \qquad T=A\otimes_S A.
 \tag{SA1}
\]

All variables have positive even internal degree, with x,y of degree two as before. Let U be a bounded complex of finite graded scalar k-spaces with nonzero cohomology, that is, a nonzero derived object. Regard

\[
                         X=U\otimes_k T
 \tag{SA2}
\]

as a derived A-bimodule. It need not already lie in the ordinary Soergel homotopy category.

### Proposition SA-A

For no bounded scalar complex C is there an isomorphism

\[
                  X\otimes_A^{\mathbf L}X\simeq C\otimes_k X.
 \tag{SA3}
\]

In particular the natural invariant-correspondence candidate remains excluded after changing the scalar coefficient complex. The statement does not need the Euler condition on C or X.

**Proof.** Generically T has one identity graph and one tau graph. This follows directly from the quadratic Galois extension of fraction fields associated with the involution, or from the explicit two-graph calculation in the checked invariant-correspondence supplement. Let

\[
 u(t)=\sum_i\dim_kH^i(U)t^i,\qquad
 d(t)=\sum_i\dim_kH^i(C)t^i.
\]

We forget the internal grading. Generic Kunneth applied to (SA3) gives

\[
 2u(t)^2(e+\tau)=d(t)u(t)(e+\tau).
\]

Since u is nonzero, the Laurent polynomial domain gives d=2u. Let a be the highest cohomological degree of U and r=dim H^a(U)>0. Then C also has highest degree a and dim H^a(C)=2r.

The ordinary module T is concentrated in degree zero. Its derived square has highest degree zero, with H^0 equal to the ordinary tensor T tensor_A T. This module is nonzero, as its generic rank is four. Scalar Kunneth and the top-degree truncation therefore turn degree 2a of (SA3) into an actual A-bimodule isomorphism, after forgetting internal grading,

\[
       (T\otimes_A T)^{\oplus r^2}
             \simeq T^{\oplus 2r^2}.
 \tag{SA4}
\]

Only top degrees are used. No vanishing of the possible lower Tor groups of T is assumed.

At the origin of the left A-space,

\[
 B=k\otimes_A T
   =k[x,y]/(x^2,xy,y^2),\qquad \dim_kB=3.
 \tag{SA5}
\]

The fixed z variables are also killed. Every positive invariant acts as zero on this B. Hence

\[
 \begin{aligned}
 k\otimes_A(T\otimes_A T)
   &=B\otimes_S A\\
   &=B\otimes_k(k\otimes_S A)
     =B\otimes_kB,
 \end{aligned}
 \tag{SA6}
\]

which has dimension nine. Applying the ordinary left-origin fiber to the actual module isomorphism (SA4) gives 9r squared equal to 6r squared, impossible. This use of ordinary fiber preserves an actual isomorphism; it is not an assertion that ordinary fiber is exact on an arbitrary derived triangle. QED.

This strengthens the earlier fixed-coefficient origin-fiber test. It does not assert that every possible coupled complex must factor as U tensor T. A genuinely nonfactorable complex with nonflat cohomology is outside SA-A.

## 2. Pure point coefficients are incompatible with the generic multiplicity condition

Return to the actual ambient generator class and scalar quadratic of SC1-SC3. SC-A proved that every cohomological multiplicity of C, with the internal grading forgotten, is even. For the arithmetic clause, take the characteristic-zero scalar field k to be a finite ell-adic coefficient field E with ell not dividing q, enlarged when needed. More generally the same argument applies after a specified scalar extension preserving the displayed dimensions and relation; no comparison from an arbitrary characteristic-zero field is implicit.

### Proposition SA-B

Suppose, in addition, that the underlying scalar complex C is equipped with an arithmetic Weil structure over a finite field, is a bounded pure complex of one integer weight, and its Euler traces at every sufficiently large extension degree have the form

\[
 \operatorname{Tr}_{\rm Eul}(F^n;C)
   =\epsilon\,\beta^n\bigl(q^{sn}+2+q^{-sn}\bigr),
 \qquad s\in\mathbb Z\setminus\{0\},\quad\epsilon\in\{1,-1\}.
 \tag{SA7}
\]

Here beta is a nonzero pure algebraic eigenvalue of an integer weight t. Then no X satisfying the actual scalar quadratic exists, whether or not its cohomology is flat.

The extra Weil comparison in (SA7) is explicit additional data. Purity is not deduced from the formal Euler class alone.

**Proof.** Let w be the pure complex weight. By BBD 5.1.8, pp. 126-127, an eigenvalue of point weight a can occur only in cohomological degree a-w. In particular each fixed eigenvalue can occur in only one cohomological degree. Thus it cannot be removed from the Euler trace by an opposite-parity cancellation. Jordan blocks do not change their trace multiplicities.

Finite power-sum uniqueness, obtained by an invertible Vandermonde matrix on distinct nonzero eigenvalues, applies also to eventual equality. The only possible visible roots in (SA7) are beta q^s, beta and beta q^-s, and their Euler multiplicities are respectively epsilon, 2epsilon, epsilon. There can be no other eigenvalues: purity puts each in a unique degree, so a zero Euler multiplicity would force its ordinary multiplicity to be zero.

Their weights are t+2s, t and t-2s. Their cohomological degrees are consequently

\[
                  t+2s-w,\quad t-w,\quad t-2s-w,
\]

which are distinct because s is nonzero. The actual cohomological dimensions in those degrees are 1,2,1. The common sign epsilon only determines whether those degrees are even or odd. Thus the two outer cohomological multiplicities are odd, contrary to SC-A. QED.

No semisimplicity premise is needed for this trace argument. The nilpotent parts of Frobenius contribute their usual dimensions to the trace, while the purity condition still fixes the degree of each eigenvalue.

### Exact F61 consequence

Retain the original formal labels when using F61's pure coefficient D as a proposed scalar complex in the ordinary Hecke category. Both of its explicit candidates have Euler class delta squared:

\[
 \begin{aligned}
 C_{\rm full}
  &=E(-2)[-4]\oplus E^{\oplus2}\oplus E(2)[4],\\
 C_{\rm half}
  &=E(-1)[-2]\oplus E^{\oplus2}\oplus E(1)[2].
 \end{aligned}
 \tag{SA8}
\]

Their cohomological dimensions are 1,2,1 in degrees -4,0,4 and -2,0,2, respectively. Already this direct calculation contradicts SC-A. Equivalently, SA-B applies with s=2 and s=1, beta=1 and epsilon=1. A common pure arithmetic line, Tate twist or cohomological shift does not change the two odd outer multiplicities, whenever the changed candidate retains the stated scalar Euler premise.

These objects and their actual relation maps do work in F61's different finite-state matrix-kernel category. The present result excludes transporting the same scalar coefficient into an ordinary bounded Soergel lift of the actual ambient generator class with the required quadratic. It does not contradict F61 or exclude every pure construction in other categories.

An elementary grading-only version is also immediate: if H^j(C)_e can be nonzero only on one affine degree line j=a e+b with nonzero integral slope a, then the Euler class delta squared forces actual outer multiplicities one in two distinct degrees. No cancellation at a fixed formal e is possible along this single line. Such a C also contradicts SC-A. This argument requires the displayed grading-to-degree comparison; it is not a claim that an arbitrary graded scalar complex has that property.

## 3. Separate dictionary and remaining case

The first test concerns the actual affine singular invariant correspondence and ordinary origin fibers. EGA I, Theorem 1.3.7, p. 86, Corollary 1.3.8, p. 87, and Theorem 1.4.1, pp. 90-92, provide the affine module/sheaf framework, with no claim that all derived candidates are scalar multiples of this correspondence. The proof only uses generic localization, top cohomology and the explicit three-dimensional singular fiber. It does not apply ordinary tensor base change to unproved cohomology isomorphisms. The formal torus grading has the SGA 3, I, 4.7.2-3 action framework and cote 90, scan 17. The effective-versus-virtual coefficient distinction uses SGA 6, V, Sections 2-3, with cote 133, scan 18; no lambda-ring structure on the noncommutative word algebra is inferred.

The second test combines the effective generic multiplicities of ordinary Hecke graph cohomology with BBD's exact point-complex purity convention. The finite perfect scalar complexes use SGA 6, I, Definition 4.7, pp. 121-122, and Example 4.8, p. 122; BBD 5.1.8, pp. 126-127, is the purity source. The finite power-sum argument and the integer multiplicity contradiction are proved here. Neither a source canonical lattice nor an unpublished archival theorem supplies the additional arithmetic comparison (SA7).

After this amendment, a scalar-complex escape would have to be genuinely nonfactorable, have nonflat cohomology, and fail the particular pure arithmetic coefficient comparison just tested. These are necessary conditions, not a proof that an escape exists. General nonflat quasi-idempotents do exist: for a nonzero homogeneous f of positive degree, the central two-term Koszul complex K(f) satisfies K(f) tensor K(f) isomorphic to K(f) tensor (k direct sum k(-deg f)[1]), by replacing the second Koszul generator by its difference with the first. Its generic image is zero and its Euler rank is zero. It therefore does not supply the actual nonzero generic support 2(e+tau) required here.

Fresh independent review is requested before integrating this amendment. The previously frozen F59 scalar report and fragment are unchanged.
