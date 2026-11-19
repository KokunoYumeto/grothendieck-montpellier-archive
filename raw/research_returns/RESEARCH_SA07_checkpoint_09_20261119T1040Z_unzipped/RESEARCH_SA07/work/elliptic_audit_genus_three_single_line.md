# Independent audit of F.3.29: a single normalizer line in genus three

Audit date: 2026-11-19. Auditor: OpenAI GPT-6 Astra, inherited effort, agent `elliptic_splitting`. This is AI-produced work. The parent and the triangle agent own integration.

## 1. Verdict and exact scope

**PASS.** I independently read the final work proof `LM6_A22_genus_three_single_line.tex`, the complete certificate `check_genus_three_single_line.py`, and the primary-source passages listed below. I reran the final revised certificate after its additional paired-conjugator checks were added.

The proved linear statement is

\[
q_6\{D\in U_{3,6}:D(a)\in[\mathbb L_6(V),a]\}=0
\]

for every nonzero vector in the original six-dimensional symplectic space. The arithmetic consequence applies to the original once-punctured genus-three curve with a rational puncture, every prime, and every finite number-field base extension in the statement. It requires neither a CM decomposition nor any second tangent line.

The separately proved balanced tangency lemma applies in every genus at least three. It does not prove the all-genus analogue of the displayed universal-quotient statement. That further detector calculation remains unproved here. The main elliptic algebraic-splitting question is unaffected by this audit.

## 2. Actual image maps and the R transfer

The dependencies retained from F.3.24 are the actual boundary-fixed geometric image and its strict weight-graded action:

\[
J_6\subset U_{3,6},\quad q_6(J_6)=0,\quad [U_{3,6},J_1]\subset J_7.
\]

I reread the work proof of F.3.24, including the punctured Malcev action, Hain's strictness step, and removal of the lower-degree boundary-inner term inside the geometric algebraic image. These maps retain the actual geometric Johnson image. The proof does not replace it by a formal ideal.

The formula for the first Johnson derivation is consistent with the tensor convention used in the code. Its twenty triples of distinct basis vectors span the full exterior cube, so the mixed bracket equations test every element of the first Johnson image.

I read MSS2026v1 Proposition 4.1 and its immediately preceding characterization, printed pages 10–11. The five displayed terms of R match the code exactly, including the final uncontracted ninth letter. The source states vanishing on the Johnson image; its proof is a sketch. The forty checks on literal iterated Johnson brackets test implementation and signs. They do not independently establish universal vanishing, which remains an imported primary-source theorem.

The final proof now supplies the required genus transfer. Embed a boundary surface of genus three in a sufficiently large boundary surface, fixing a path from the large boundary basepoint to the small subsurface. Extend a small-surface mapping class by the identity on the complement. With the corresponding free-group generators, the induced derivation is unchanged on the six original generators and zero on the added generators. The Johnson homomorphism therefore takes the extended class to this extended derivation. If i denotes the symplectic inclusion of homology, its tensor is precisely the image under the ninth tensor power of i. Since every contraction in R uses the unchanged symplectic pairing and leaves the ninth letter, the exact identity is

\[
R_G(i^{\otimes9}T)=iR_3(T).
\]

The left side vanishes on the extended actual Johnson class in the source's stable range. Injectivity of i gives vanishing in genus three. No stable multiplicity formula is evaluated directly at genus three. The Enomoto–Satoh transfer is the corresponding map already proved in F.3.24, with the left inverse on cyclic tensors given by killing added letters.

Only the coefficient of c in R applied to the bracket with the abc first Johnson vector is imposed in the final certificate. No assertion about the separate S map or its exterior-cube quotient is needed.

## 3. Complete parameterization and exact computation

For a balanced degree-six derivation, its associated tensor has four symplectic pairs. The fifteen multiplicity blocks in the proof account for every possible support. The coefficient of D(a) is parameterized by the full degree-six free Lie space through the commutator with a. Every other image, including D(b), is parameterized by the full required degree-seven free Lie space. Thus the initial 180-dimensional kernel is a single-line space.

The standard Lyndon bracketing routine chooses the longest proper Lyndon suffix. Its triangular leading-word property makes restriction to the Lyndon-word coefficient rows injective on each free Lie block. I checked the specialness signs: D([x,y]) equals [D(x),y]+[x,D(y)]. The code also verifies each lifted kernel derivation directly in the full associative word algebra, independently of the row restriction.

The degree-six commutator with a is injective. In the free associative algebra, an element commuting with a has only words in a, by comparison of the first and last letters and induction. Its intersection with the free Lie algebra is the span of a. The degree-six homogeneous part of this span is zero.

For each block, reduction modulo 101 supplies a rank lower bound. The matching integer kernel lifts are independent modulo 101 and are checked in the original integer matrix. This supplies the rational rank upper bound, with matching values in every block. These are rational rank proofs, not guesses of a rational kernel from a modular kernel.

On the resulting 180 vectors the mixed ES equations and the one R coordinate give 7,977 nonzero coordinate rows. The code obtains rank 48, selects 48 independent rows modulo 101, row-reduces those rows over the rationals, and checks all 132 independent cleared-denominator kernel vectors against every original integer row. This proves the full rational kernel dimension 132.

The arithmetic in the integer matrices is protected by explicit fixed-width product bounds. The modular elimination keeps entries within the int16 range; the relevant products are at most products of residues below 101. Integer matrix multiplications are bounded before execution. The final contraction identities use Python integers after extraction.

## 4. Actual geometric brackets and invariant extension

Both sixfold right-nested brackets Z1 and Z2 are formed from actual first Johnson derivations. Their membership in J6 follows by the graded geometric Lie bracket, before any numerical calculation.

For every integer kernel vector the program checks all 105 complete contraction coordinates against the span of the contractions of Z1 and Z2. The two selected coordinate rows form the matrix

\[
\begin{pmatrix}-104&-288\\32&192\end{pmatrix}
\]

with determinant -10752. Clearing that determinant gives exact integer identities in every coordinate, for all 132 kernel vectors. The determinant is used only as a nonzero rational scalar; no assertion about integral division at primes dividing it occurs.

The quotient is symplectic-trivial. Complete reducibility over the characteristic-zero field extends a scalar component of q6 from the universal image to the full special derivation representation and then to the eighth tensor power. MSS2015v2 Proposition 2.1 gives surjectivity of the contraction description in every genus; injectivity in the stable range is unnecessary. Thus the extended functional is a linear combination of the 105 contractions. Its values on Z1 and Z2 are zero by their actual membership in J6. The exact contraction-span calculation therefore proves its vanishing on the actual balanced single-line kernel. The same reasoning would work componentwise; it does not rely on an accidental choice of a quotient coordinate.

## 5. Torus projection after the actual-image constraints

Nakamura's original page 117 states that the actual geometric and universal graded images are stable under GSp and gives the equivariant exact quotient map. The quotient has character t cubed in degree six.

The chosen diagonal torus preserves tangency to a: it scales a and conjugates a commutator with a into another such commutator. Hence the weight projector onto t cubed preserves both the actual universal image and the full single-line tangent space. A generic torus element separates the finitely many occurring characters; its Lagrange polynomial realizes the projector over the coefficient field. The quotient value is unchanged.

The selected individual R-coordinate equation need not itself define a torus-stable space. This causes no gap: the projected vector still belongs to the actual universal image, so all mixed geometric equations, including this R coordinate, hold afresh. The argument does not promote a projected derivation to an individual Galois element.

## 6. Original genus-three arithmetic consequence

The finite-cover detector from F.3.21 is used only to produce a nonzero homology class for the same procyclic generator. Its construction uses a finite ell-group quotient in which the generator survives, the preimage of its cyclic subgroup, and arithmetic descent of that finite geometric cover. The pro-ell subgroup is the corresponding geometric pro-ell fundamental group, and its abelianization is torsion-free. Intersecting the original normalizer with the arithmetic covering group gives finite index and therefore open arithmetic image.

The normalizer exponent acts by the same character on the original first nonzero Magnus term and on the detected homology class. Its geometric kernel acts trivially on the original leading term, so the character factors through the open Galois image. If the detected class maps nontrivially to proper homology, the exact Frobenius weights give degree one for the original leading term.

In that case Nakamura's finite-base-invariant quotient supplies an actual arithmetic element in degree six with nonzero q6. It is lifted through the same original normalizer. Its exponent on the procyclic generator is one because it acts identically on degree-one homology. The inner correction between that lift and the canonical special representative is handled using the full logarithm of the generator: remove the degree-one multiple of a by a rational power of the full generator, then the free Lie centralizer eliminates degrees two through five. Degree seven gives D(a)=[Z6,a]. The proved single-line statement contradicts nonzero q6.

The detected nonzero homology class therefore lies in the boundary kernel. After finite extension defining the boundary points, its character is exactly cyclotomic. This equality extends from the intersected normalizer to the full normalizer over its open arithmetic image because the remaining difference lies in the geometric kernel, where the exponent character is trivial. Nakamura1994 Definition and Theorem 2.1.1, printed page 94, apply to the full class of finite ell-groups. They give actual cusp inertia containing the nontrivial generator, and its closed procyclic subgroup follows by closure.

## 7. Separate all-genus balanced lemma

The final added code reconstructs B from the coefficient chains of words b^i w b^j in D(b). It checks [B,b]=D(b) exactly and checks the Dynkin–Specht–Wever identity Dynkin6(B)=6B. The latter places B in the degree-six free Lie algebra. All 180 basis vectors pass.

For an arbitrary-genus balanced block, the handle multiplicities sum to four. If the constrained handle has multiplicity zero, both relevant images vanish. At multiplicity one, the cyclic tensor condition determines the full tensor from its unique b-leading part; rotating to its unique a-leading part yields D(b)=[A,b] with the same A as D(a)=[A,a]. At multiplicity at least two, the block uses at most three handles and is covered by the exact six-letter calculation after relabelling. This proves the stated all-genus balanced tangent-space equality, with no all-genus q6 assertion.

## 8. Primary-source locators actually checked

- MSS, *The first Galois obstruction in the Johnson cokernel*, arXiv:2608.17673v1, 18 August 2026, full local original PDF/text. Printed pages 10–11: vanishing characterization and Proposition 4.1, including all five R terms. The stated universal vanishing is imported with the source's sketch-of-proof status retained.
- Nakamura, *Coupling of universal monodromy representations...*, original 1996 scan. I visually reread printed pages 115, 116, and 117 (`Nakamura1996_images/page18.png` through `page20.png`): degree-six rank table; finite-base invariance; Lemma 4.5 and Corollary 4.6; actual GSp stability, quotient sequence (4.7.1), curve map (4.7.2), and its surjectivity onto the arithmetic quotient.
- Nakamura1994, full local original text, printed page 94: definition of cyclotomic normalizer and Theorem 2.1.1. Its full-class and arithmetic-image hypotheses match the last step above.
- MSS2015v2, Proposition 2.1, printed page 8, and the contraction conventions on pages 7–8, independently read in the immediately preceding F.3.28 audit. The required assertion is surjectivity for every genus.
- The exact F.3.24 strictness/normalization and ES transfer proofs were reread as dependencies. This audit does not claim to replace the underlying opened Hain and Enomoto–Satoh theorems by the finite computation.

## 9. Reproducibility and distinct run records

The earlier core run started at `2026-11-19T10:28:15.722341+00:00`, exited 0, had external elapsed time 42.715731766 seconds and program-reported internal time 41.638550149 seconds. Its separate files are `elliptic_audit_single_line_run.json` and `.output.txt`. It predates the added paired-conjugator checks.

The final revised run started at `2026-11-19T10:32:30.047760+00:00`, exited 0, had external elapsed time **42.928949937 seconds** and program-reported internal time **41.742954870 seconds**. Its files are `elliptic_audit_single_line_final_run.json` and `.output.txt`.

The final program SHA256 is `9b4d226893786c0edf7fc0ddd556d497ee7f9903971e940532becf2118367c4f`. The final run reproduces dimension 180, all 180 paired-conjugator checks, matrix rank 48 and kernel dimension 132, all 132 by 105 contraction identities, the determinant -10752, and maximum integer kernel coefficient 247830.
