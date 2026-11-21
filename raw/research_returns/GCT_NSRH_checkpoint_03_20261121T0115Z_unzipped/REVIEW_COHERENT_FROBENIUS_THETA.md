# Fresh full review of F36: coherent Frobenius on the actual branch module

Reviewer: /root/rectangular_and_theta, GPT-6 Astra Pro. Date: 2026-11-21 UTC.

## Snapshot and verdict

The complete agent_coherent_frobenius_gate.md was read, including all eight sections, every displayed formula and the scope qualifications. Reviewed SHA-256:

0505059c15c9cafe19372b2f6c6dd5205a951617ac961d5c403fa11b16bb2fd0.

**PASS. No mathematical blocker found.** The center pullback and the parameter pullback are correctly distinguished. The actual branch multiplicities, both branch orientations in the torsion formulas, derived periodicity, relative Frobenius, Morita base change and right-row conjugation formulas all check. The underlying F19/F21 algebra and tensor-lattice calculations were independently reviewed earlier in REVIEW_R3_THETA.md and REVIEW_R3_TENSOR_THETA.md.

This is a fresh algebraic proof review of the report, not a certification of a later paper fragment or of an arithmetic Weil realization. No formal proof kernel was used.

## 1. Good characteristic and the ring maps

With \(R=\mathbf F_q[[t]]\), \(\Delta=t^m u(t)\ne0\), and \(C=R[x]/(x(x-\Delta))\), C is free over R with basis 1,x. The corresponding basis 1,x-\Delta is also valid. The actual center has m=2: in the previously checked formula the leading coefficient of \(\Delta\) is \(3/4\), a unit for p>3. The regular F19/F21 denominators and determinant units at v=1 involve only the excluded primes 2 and 3, so the stated good-characteristic restriction is appropriate for this reduction.

The report uses absolute p-Frobenius, which is semilinear on the coefficient field when q is a nontrivial p-power. Its iterate is q-Frobenius. This is not geometric Frobenius on an l-adic realization. The entrywise matrix map is a ring homomorphism because its coefficient ring is commutative of characteristic p; it is correctly distinguished from taking the noncommutative matrix pth power.

## 2. Underived center pullback and the opposite-branch kernels

For \(f_1=x\), \(f_2=x-\Delta\) and \(d=\Delta^{p-1}\), the identities
\[
f_1^p=d f_1,\qquad f_2^p=d f_2
\]
are correct. For the second, the characteristic-p binomial identity gives
\(x^p-\Delta^p=d(x-\Delta)\), including the sign.

Frobenius base change of the cyclic quotient gives
\[
F_C^*L_i=C/(f_i^p)=C/(d f_i).
\]
The ideal \((d f_i)\) is exactly the R-submodule \(R d f_i\), since multiplication by the other basis coordinate only multiplies \(f_i\) by a scalar in R. Thus the stated underlying R-module is
\(R\oplus R/(d)\), and its torsion length is m(p-1).

The natural reduction to \(L_i=C/(f_i)\) is the linearization of the branchwise semilinear p-power map and is surjective. Its kernel is
\[
(f_i)/(d f_i)\simeq C/(f_j,d)=L_j/dL_j,\qquad j\ne i,
\]
because \(\operatorname{ann}(f_i)=(f_j)\). In particular the underived kernel is on the *opposite* branch. The report states this correctly and does not incorrectly claim a split C-module decomposition. Torsion versus R-freeness excludes every candidate C-linear unit isomorphism, not just the displayed surjection.

The iterated-power substitution replaces d by \(\Delta^{p^e-1}\), so the q-version has the claimed length m(q-1).

## 3. Derived pullback and exact Tor orientation

The resolution of \(L_1=C/(f_1)\) has
\[
d_1=f_1,\quad d_2=f_2,\quad d_3=f_1,\ldots.
\]
Cancellation in the domain \(R[X]\) proves the annihilator equalities used for its exactness. After Frobenius, its differentials become \(d f_1,d f_2,\ldots\). Multiplication by d on C is injective, since C is free over the domain R.

Thus in homological degree one,
\[
H_1=(f_2)/(d f_2)\simeq L_1/dL_1,
\]
while in degree two,
\[
H_2=(f_1)/(d f_1)\simeq L_2/dL_2.
\]
Periodicity gives precisely the report's odd/even formulas; for \(L_2\) they interchange. The degree-one Tor is therefore on the *same* branch, whereas the underived-surjection kernel is on the opposite branch. I checked this distinction directly rather than inferring the labels from symmetry.

All these groups are nonzero and have R-length m(p-1). Consequently the derived pullback of the same branch module is unbounded to the left. Replacing its representative by another resolution cannot make the derived object bounded. The scope rightly leaves genuinely different objects or unbounded categories open.

## 4. Actual Morita action and the counts 20 versus 40

The checked actual algebra is
\(A=R\times R\times M_2(C)\), and the actual module is the sum of scalar ranks 20 and 4 with 16 and 4 copies of the standard row modules on the two branches. Entrywise Frobenius fixes all matrix units. Therefore extension of scalars along this algebra map commutes with the usual matrix Morita equivalence.

For right modules the source is \(M\otimes_{A,\phi_A}A\). On a branch row module this replaces its multiplicity module \(L_i\) by \(F_C^*L_i\); the commutativity of C identifies the left/right center tensor descriptions. The trivial finite projective bundle E justifies the displayed Hom base change without any flatness assumption on center Frobenius.

There are 20 branch multiplicity copies, giving 20 torsion factors at the multiplicity-sheaf level. Each standard row has rank two over the branch, so the actual tensor module has 40 factors. The scalar sectors remain free. Therefore
\[
F_A^*M\simeq R^{64}\oplus(R/(d))^{40}
\]
as R-modules, exactly as stated. Its torsion length is \(40m(p-1)\), hence \(80(p-1)\) for the actual collision.

The natural semilinear map linearizes to a surjection: the images of the standard basis elements, followed by the target algebra action, generate the target. Morita equivalence identifies its kernel with the branch kernels above. In every positive derived Tor degree there are likewise 40 copies of \(R/(d)\), with the stated alternating branch orientations before forgetting to R. The scalar sectors have no higher Tor because they are free over their scalar algebra factors.

## 5. Relative Frobenius and its geometric meaning

Parameter base change gives
\[
C^{(p)}=R[X]/(X(X-\Delta^p)).
\]
The relative map sends \(X\) to \(x^p=d x\), fixing the target R. Its matrix in the specified free bases is \(\operatorname{diag}(1,d)\), so it is injective and its cokernel has length m(p-1).

Under the two-branch normalization maps, the source consists of pairs congruent modulo \(\Delta^p\), and the target of pairs congruent modulo \(\Delta\). The relative Frobenius map is the inclusion of those subrings: evaluation at the target branches 0 and \(\Delta\) after \(X\mapsto d x\) gives the source branch evaluations 0 and \(\Delta^p\). The report's order-mp versus order-m statement is therefore correct, including units.

This inclusion is finite, induces the identity on the two generic branches and the single closed residue point, and is a universal homeomorphism. This agrees with the earlier F22 model while retaining the distinct coherent rings. Factorization through parameter pullback followed by this extension of scalars identifies exactly where the torsion appears; ordinary etale topological invariance cannot remove the coherent defect.

## 6. The different parameter-base unit structure

In the adapted basis the branch evaluation maps commute with Frobenius. Hence entrywise p-powers satisfy
\[
\tau_{\rm ad}(ma)=\tau_{\rm ad}(m)\phi_A(a).
\]
The linearization over R alone maps each free basis vector \(1\otimes e_j\) to \(e_j\), giving an isomorphism \(R\otimes_{F_R,R}M\to M\). This does not assert an isomorphism from the larger algebra/center pullback. The report consistently distinguishes those tensor products.

In old right-row coordinates, \(r_{\rm old}=r_{\rm ad}B\) and
\(\rho_{\rm ad}=B\rho_{\rm old}B^{-1}\). Transport gives
\[
\tau_{\rm old}(r)
=r^{[p]}(B^{[p]})^{-1}B=r^{[p]}U.
\]
The order of these factors is correct. Since B is regular invertible, so is \(B^{[p]}\), and U is an R-unit matrix.

Solving the corresponding representation identity gives
\[
\rho_{\rm old}(\phi_A(a))
=B^{-1}B^{[p]}\rho_{\rm old}(a)^{[p]}
              (B^{[p]})^{-1}B
=U^{-1}\rho_{\rm old}(a)^{[p]}U.
\]
It follows directly that
\[
\tau_{\rm old}(r\rho_{\rm old}(a))
=\tau_{\rm old}(r)\rho_{\rm old}(\phi_A(a)).
\]
This verifies the exact actual action compatibility. Dropping U would be an unjustified assertion about the original embedded algebra, and the report explicitly avoids doing so. Iteration is consistent as well: the conjugating products telescope to \((B^{[p^e]})^{-1}B\).

## 7. Scope and check event

The conclusion is an explicit obstruction to unit Frobenius pullback of the same actual branch object over the singular center, together with a constructive unit semilinear structure over the distinct parameter base. It is not an obstruction to every possible coherent or constructible realization. It supplies neither arithmetic purity nor the required path-output sign, and it does not identify quantum grading with Frobenius weight.

Suggested event: F36-COHERENT-FROBENIUS-THETA-FRESH.

Full report read and all displayed algebraic claims independently checked. Verdict: PASS. The final generated-fragment match remains a separate event.

