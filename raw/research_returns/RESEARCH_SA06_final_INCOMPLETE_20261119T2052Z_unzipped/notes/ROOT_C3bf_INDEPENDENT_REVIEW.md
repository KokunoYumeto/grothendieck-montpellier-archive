# Root independent review of C.3bf

We read the entire first typed proof at13:48:13UTC and the revised direct-family proof during the scheduled review beginning13:50:08UTC. The proof is approved in its exact scope: k is the algebraic closure of F5, N≥4, and the nonzero ordinary integral Picard restriction kernel contains (Z/5)^3. It asserts no rational failure or higher Chow nonvanishing.

## Geometry and formal groups

The specified deformation F+t ell H of the Segre model retains the smooth Fermat plane quartic in characteristic five. The characteristic-zero geometric construction uses only the indicated nonzero partial derivatives and proper Segre contraction, so its normal strict-local model and regular punctures have the same verified properties here. The maximal ideal pulls back to the ideal of the single exceptional divisor because the Segre coordinates t x_i z_j generate that ideal. On ell=0 the deformation vanishes identically, giving the required split target neighborhood.

The coherent calculation gives H¹(V,L)=k^(m+1), H²(V,L)=0, and H¹(V,L^n)=H²(V,L^n)=0 for n≥2. Thus the whole subsequent formal Picard group is determined by its first neighborhood, rather than only its tangent space. The unit transition maps are surjective at later stages, so compatible trivializations of endpoint classes exist. On the target the exact divisor sequence gives the quotient by U=ell H¹(C,O_C), with U the three-dimensional span of x0,x1,x2; all later H¹ and the required H² groups vanish.

The three degree-five Jacobian monomials are a basis in characteristic five, and the actual Poincare obstruction identifies the Picard extension class with the rank-three contraction map. The Hasse–Witt matrix is2I3 over F5. The ordinary Verschiebung v therefore has etale kernel (Z/5)^3, and v* kills H¹(O). The Hom–Ext sequence then identifies its three independent additive characters with the three independent extension classes. This proves that the lifted J^(5) is embedded in the source extension and that its target restriction has exactly the displayed kernel.

## Actual fixed-product families

We specifically rejected reliance on an unproved universal family over the whole abelian variety. For each kernel point choose a smooth proper curve P through it and zero. The initial Poincare bundle on V×P lifts to V2×P because its only possible obstruction is the mixed contraction tensor and v* kills its H¹(J,O) factor. The lifted Picard map differs from the prescribed map by a morphism from the proper curve to the affine vector kernel, hence by a constant. Normalization at zero removes that constant. This is also the source-minimal derivation of the initially formulated representative-gerbe argument; it requires no separate general gerbe-classification input.

For n≥2, H²(V×P,L^n)=0; H¹(V×P,L^n) need not vanish, but uniqueness of entire families is unnecessary. Their individual endpoint classes are unique. Proper formal existence produces a completed actual family. Popescu descent and smooth lifting over the henselian pair (R,m²) preserve its whole first jet on the fixed product. The source point cannot be killed by an exceptional divisor because a nonzero multiple of the ample conormal has nonzero Neron–Severi class. On the target, formal endpoint triviality and the actual puncture Picard comparison give zero. Tensor differences and endpoint uniqueness prove that the resulting map on all125 kernel points is a group injection.

## Source and finite-check scope

We freshly opened Brion's *Commutative algebraic groups up to isogeny. II*, author PDF at https://www-fourier.univ-grenoble-alpes.fr/~mbrion/isogeny_II_rev.pdf, Section3.2.3, equation(3.8), authorp23. The bifunctorial Ext¹(A,Ga)=H¹(A,O) statement and its next characteristic-p paragraph precede the explicit subsequent restriction to characteristic zero. No fresh reading of Oort's original cited there is claimed. Frobenius independently opened Brion's separate course, pp47–48 and Remark5.3.3(i), with the same characteristic qualification.

The owner freshly opened Hacon–Patakfalvi arXiv1310.2996v2, Lemma2.3.1 and Proposition2.3.2 with proof on authorp12, for the ordinary/Verschiebung criterion, and Brion1204.2628v2 Theorem1.1 for the exterior algebra of coherent cohomology. The root's direct arXiv opening of Hacon–Patakfalvi failed, so we do not attribute that opening to the root. The complete Illusie, formal-existence, Popescu, henselian lifting, and Elkik inputs are the exact previously audited ones in C.3m/p/w/az.

At13:52:48UTC we inspected the complete finite-certificate program and output:41 checks passed, none failed; run started13:51:48.836254, runtime0.07533210799738299seconds. We independently checked the Hasse–Witt matrix, Jacobian reductions, universal Segre identity, and split-target substitution. We did not rerun and overwrite the owner's timing. Finite m/n samples and the abstract125-point enumeration are explicitly not substituted for the all-dimension geometric proof or actual algebraic equivalence.

This is a genuine negative result for the main integral degree-one restriction question. The remaining rational and higher-degree gates are unchanged. No priority claim is made.
