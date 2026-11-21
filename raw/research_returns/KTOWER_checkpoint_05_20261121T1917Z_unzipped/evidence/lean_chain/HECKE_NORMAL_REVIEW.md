# Independent review: stable Hecke localization and integral extension data

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

## Verdict

**PASS.** I read the complete `unitary_audit/hecke_normal_results.tex`, including its subsequently appended literature-scope paragraph, and the entire `hecke_normal_audit.py`. I freshly replayed the unchanged small certificate using a byte-identical copy of its current input. All six evaluated unit/Bezout certificates pass, and the resulting JSON is byte-identical to the author's report.

The conclusions are an integral identity in the indicated localized stable Hecke order, exact trace invisibility of the original strict Selmer directions, and a nonunit trace-discriminant bound for the actual split-residual adjoint lattice. They do not bound the strict Selmer length or remove the original classical rank-two branch. No stronger arithmetic vanishing follows from these lemmas.

## 1. All-prime Hecke identity and proper maximal ideal

The structural relation is valid at every split q other than ell, not just at the two computed test primes. On the Hecke-invariant complement of the constructed symmetric-square subspace, Cayley–Hamilton kills R(A7). On the constructed symmetric-square subspace, self-duality of the adjoint parameter makes the two normalized minuscule eigenvalues equal at every such q. Semisimplicity makes their difference the zero operator on that subspace. These operators commute, so the product is identically zero on the entire stable characteristic-zero space. It therefore vanishes on any common integral lattice; no integral direct-sum projector onto the two subspaces is being assumed.

The common lattice exists using the integral harmonic representation at ell greater than three, intersected with the stable rational subspace. Passing to a finite coefficient extension and restricting scalars to Z_ell, if needed, gives the same finite integral-matrix setting. Adding its image under the harmonic-variable interchange preserves stability under both Hecke directions. The already checked dual-matrix identity gives an actual conjugation involution on this order.

Although infinitely many split Hecke generators are used, their algebra is a Z_ell-submodule of a finite free matrix module, hence is finite and torsion-free. The claimed residual ideal is proper: the already proved Fretwell–Roberts/symmetric-square construction gives a cuspidal eigencharacter with all the required residual split-prime values for every prime dividing the indicated modulus. Because the quotient is generated over F_ell by those now scalar generators, the proper quotient is exactly F_ell. Thus the ideal is maximal. The evaluated gcd certificate also ensures ell is different from seven, so A7 is among the permitted generators.

The unit R(t7) modulo ell makes R(A7) a unit after this localization. Dividing the exact operator relation proves A_q equals A_q^opp for every split q. All generators are then fixed, so the conjugation involution is the identity on the localized order. Every generic complementary factor is killed because R(A7) is zero there. This argument does not assume distinct eigenvalues at seven.

For the augmented order, the added first coordinate has equal values t_q in both directions, so the same annihilating relation holds there. The first projection itself supplies the residual augmentation. It is explicitly a formal Eisenstein coordinate, not an additional compact cuspidal representation.

## 2. Trace invisibility is an exact integral statement

The checked Selmer equivalence identifies every odd weight-minus-one finite-coefficient tangent with the actual normalized lift `(1+epsilon*t(g)*(E21-E32))*r0(g)`. On G_E this is lower triangular with unchanged diagonal. Every characteristic coefficient is therefore unchanged over the square-zero coefficient ring itself. This is stronger than a statement after semisimplification, and it includes traces of every product of group matrices because those products are again group elements.

Consequently all polynomial trace coordinates have zero derivative. The torus-weight description gives the same result. An injective restriction to that trace algebra would already force the original strict Selmer module to vanish by the proved duality. The identity involution on the localized Hecke order does not supply this injectivity, nor does a pseudorepresentation algebra comparison automatically recover the off-diagonal extension modules. The section correctly retains the need for those integral extension and reducibility-pairing data.

## 3. Rank-nine lattice and discriminant at least twelve

Absolute irreducibility over the fraction field makes the span of the group algebra the full matrix algebra: after scalar extension to an algebraic closure this is the usual density/Burnside statement, and dimension descends. The O'-span of the integral matrices is a finite free full rank-nine sublattice of M3(O').

Its reduction has image in the diagonal subspace, of dimension at most three, because this is the actual split diagonal residual lattice constructed in the host-point proof. At least six inclusion elementary divisors are therefore divisible by the uniformizer. The quotient length is at least six. The full matrix algebra's trace pairing has a matrix-unit Gram matrix with determinant a unit. Changing to a basis of the smaller lattice multiplies this determinant by the square of the inclusion determinant. Thus the displayed discriminant valuation equals twice the quotient length and is at least twelve.

These are normalized uniformizer valuations over O'. No coefficient-ramification factor is missing. The result concerns this actual integral lattice; it is not the odd normal Jacobian's Fitting ideal and does not imply a nonzero Selmer group. The elementary complexes and finite-pairing examples correctly show why rational dimensions and existence of a perfect pairing cannot evaluate an integral length.

## 4. Targeted primary-source exclusion

I read the exact primary text in the saved Hida–Tilouine author manuscript (7 October 2018), printed pages 2–4: the imposed residual irreducibility on page 2; hypothesis (*) on page 3, including containment of SL2(k'); and the statements of Theorems 1.1 and 1.3. I also read Zhang arXiv:1802.08329v1, printed pages 7–8, including Definition 2.5, Condition 2.7, Remark 2.8, Proposition 2.10, and Theorem 2.11. The latter R=T theorem expressly assumes Big, Dist, and RegU; Big is the stated symmetric-power SL2 containment and implies absolute irreducibility in its setting.

The present residual rank-two semisimplification is a sum of two characters. Every residual lattice is consequently reducible, whether split or a nonsplit extension. Its symmetric powers preserve the associated monomial flag; scalar twists and restriction preserve this flag. The cited irreducibility and large-image conditions therefore fail for the present branches. This is a check of failed hypotheses, not an import or independent verification of those papers' full comparison proofs. No claim is made that all possible literature comparisons have been excluded.

## 5. Fresh finite certificate and hashes

The small script uses exact descending-order Horner evaluation modulo each composite-allowed modulus, checks the saved full evaluation and vanishing of the constructed symmetric-square factor, obtains an inverse using the ordinary composite-modulus inverse operation, and verifies the explicit integer Bezout identity. Invertibility is certified without assuming the modulus prime. The other code assertions ensure the test primes and 2,3 are coprime to the modulus.

The unchanged replay lives in `hecke_normal_replay/` below this review directory.

* Script SHA256: `2e795a0ef6bce131620392fccd1b4ab1d775d26e2dd1becea12d654592adc93a`.
* Exact polynomial input SHA256: `1cbe9d27760cb8030bac929e0385983b9892a4265de62154a87fc16234f1557d`.
* Fresh six-check report SHA256: `c65bef628a51caafc2a009799260cd4220f1ed2f854672865ec01e82edba19a3`.

The replay verifies these six finite modular evaluations and Bezout identities only. The automorphic decomposition, all-prime self-duality, actual source cotangent identification, and absolute irreducibility remain the explicitly named previously checked inputs. No Lean compilation is claimed.
