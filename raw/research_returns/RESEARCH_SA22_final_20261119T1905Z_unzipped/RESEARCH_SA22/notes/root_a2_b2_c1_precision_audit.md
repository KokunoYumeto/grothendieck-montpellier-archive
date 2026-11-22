# Root proof reread and the C.1(d) clarification

19 November 2026, after build25. These are proof checks of existing claims, not changed outcomes or smaller progress gates. No mathematical certificate was rerun.

## A.2: energy, recession and image

The root read the entire active `sections/part_a2b_secondary.tex` proof. The mixed bilinear energy identities use the cylinder integration by parts with the variation indices chosen consistently; the seam terms cancel and yield the symmetric positive Jacobian in squared-length coordinates. The genus-specific uniform radius bounds, collar extension, support supremum and recession calculation apply in their stated stable connected-surface scope. The extension to nonnegative recession directions uses the support supremum, not an unproved embedded-domain limit. The minimization proof explicitly excludes escape to infinity, a negative-infinite boundary value and every finite boundary minimum. Its last assertion identifies radius vectors, not arbitrary discs with canonical discs. Part A567 independently checked inactive factors and shifted orthants in `notes/part_a567_a1_a2_zero_face_audit.md`.

## B.2: the generic divisor-square example

The root reread the construction and proof of `thm:B2-square`, its Mumford lemma, and the entire `prop:B2-kernel` proof. The elliptic curve is explicitly given over the algebraic numbers; the two x-coordinates are required to be algebraically independent over that field. This is an exactly specified family of generic counterexamples, with every such choice satisfying the proved conclusion. For each n, auxiliary degree and rational-curve degree, the finite-type incidence parameter scheme is defined over the algebraic numbers. Its image cannot be dense because pullback of the nonzero two-form would force n times that form to vanish. Each proper closure is therefore avoided by the specified generic point. This proves nontorsion, not merely nonvanishing of one cohomological invariant. The Albanese-kernel generation and rational square-spanning argument follow from the displayed cycle identity and Abel's theorem. No finite numerical sample is substituted for the generic proof.

## C.1(d): proof precision and explicit universal tests

The root read the full revised proof, including the ordinary polynomial-ring test and the compatible truncated-polynomial-ring tests. The two corrected phrases retain the exact scalar factor lambda and identify a nonunital nilpotent subalgebra. They do not change the theorem's conclusion. The subsection now repeats that K is a commutative Q-algebra.

Naturality identifies an ordinary action with its universal value over K[t]. The image test uses uniform nilpotence and the finite polynomial logarithm, evaluated at1 and compared with t times that endomorphism. A formal action is a compatible sequence over K[t]/(t^(n+1)), with the two-variable addition identities. Its logarithms give a specified element of the inverse-limit module; membership in the image of the stated K-linear map is exactly the extension obstruction, and that map's kernel is the already stated fibre subgroup. Universal substitution includes every further base extension and imposes no quasi-coherence assumption. This supplies an explicit linear lifting criterion without assuming that an exponential already exists. The numbered result and CSV identity are unchanged.
