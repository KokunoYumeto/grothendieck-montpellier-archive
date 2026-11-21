# Geometry and tower findings for KTOWER

## Completed results

1. **KT-FF-SEC refutes finite-field section surjectivity.** Every profinite extension of the finite-field Galois group splits. The explicit proper genus-two curve
   
   \[
   y^2+y=1+\frac{x^2+x}{x^3+x+1}
   \]
   
   over F₂ has no rational point. Its full arithmetic fundamental sequence and the sequence retaining the full arithmetic quotient with maximal prime-to-two geometric quotient both admit sections. Properness removes tangential/cuspidal exceptions. This does not contradict the accepted A05 injectivity theorem. Full proof: `finite_field_sections.tex`. Root and author whole-proof checks passed.

2. **KT-POLY-FAIL refutes general higher-dimensional point separation for the maximal geometric prime-to-p quotient.** The surface obtained by twisting the genus-two Artin–Schreier curve `y²+y=x⁵` by its hyperelliptic involution along a connected étale double cover of a hyperbolic base has all of its geometric fibre group killed in every odd finite quotient. Two distinct rational points in a split fibre therefore induce the same arithmetic section class. Full proof: `polycurve_counterexample.tex`. Root and author whole-proof checks passed. The interpretation of the quotient is essential: the result concerns completion of the whole geometric group, not a fibrewise quotient retaining the full geometric base.

3. **KT-ARTIN-FAIL gives an affine elementary-fibration example.** Replace the fibre by `y²+y=x+1/x+1/(x+1)` and remove one fixed branch point. The result is a smooth affine surface in an elementary hyperbolic tower. The finite odd quotient proof uses prime-to-two Künneth after product trivialization, never a full affine wild homotopy sequence. Full proof: `artin_tower_counterexample.tex`. Root and author whole-proof checks passed; the root-requested clarification was incorporated.

4. **KT-PRODUCT-SEP gives a positive higher-dimensional conclusion.** If finitely many maps from X to hyperbolic curves jointly separate X(k), A05 implies that the prime-to-p point-section map separates X(k). Hence varieties embedding in a product of hyperbolic curves, including strongly hyperbolic Artin neighborhoods in the Schmidt–Stix sense, satisfy point separation. The extra embedding condition cannot be dropped. Full proof: `product_separation.tex`. Root and author whole-proof checks passed, conditional only on carried A05.

## Reviewed rather than newly proved

5. **F149 marked/unmarked recognition survives the requested full read.** The supplied generic-to-global, marked recognition, bare-extension and unmarked-curve proofs were read completely. No fault was found under their stated hypotheses. The positive result keeps the full generic Galois marking; the negative result permits the base profinite group to move and uses a nonintegral profinite slope. Neither asserts section surjectivity. Literature comparison and exact check scope: `f149_review.tex`.

6. **AG-C149-NORMAL is an explicit instance of F149-RELATIVE.** The torsion-line-bundle family verifies the fibre homotopy injection assumed in the relative theorem. The normal line is L and its conormal is L-dual, accounting for the sign. Sectionwise arithmetic splitting does not assert a global splitting over π₁(S). Whole supplied proofs of NORMAL, FULLLIFT and RELATIVE were read. Comparison: `f149_normalizer_comparison.tex`.

## Remaining gates

7. **Ihara: no new arithmetic Triple-NV theorem.** Accepted Greenberg, Vandiver and cubic reductions are retained. The exact remaining cubic incidence condition is CU.1 for the actual companion errors. A completed all-weight K-group vanishing theorem would imply the all-prime kernel conclusion through the carried Kurihara/Vandiver bridge. This workstream supplies neither that theorem nor a new prime. Status: `ihara_gate.tex`.

8. **Route 2: exact theta-orbit reformulation, no all-curves existence theorem.** Over Fbar₂, any cover can be pointed over any prescribed geometric point, so the point parameter imposes no geometric existence restriction. For a genus-two curve and an odd-order line bundle L, the primitive factor has two-rank zero exactly when every multiplication-by-two orbit on primitive characters meets the Raynaud theta divisor. The proof uses one-dimensional character cohomology and the stable Frobenius rank. The O₅ Rosati-fixed restriction remains unused in forcing this incidence. No universal exponent/index bound or curve for which all odd cyclic covers fail was obtained. Full proof and limitations: `route2_gate.tex`. Root and author whole-proof checks passed.

## Review and integration notes

- The LaTeX files are section fragments for root integration. They use ordinary theorem/proposition/lemma/proof environments and the accepted result identifiers. They are not standalone documents.
- `SOURCE_LOCATORS.md` gives exact published, author and input locators. `CHECK_EVENTS.tsv` records what was read, what was carried, and independent root reviews.
- Every new proof above has both an author whole-proof read and a root targeted whole-proof review, except the short newly assembled F149 comparison, which has an author whole-proof read and relies on the fully read supplied proofs.
- No claim of exhaustive literature priority is made. The elementary splitting fact, Raynaud machinery, tangent functors and anabelian reconstruction are established inputs. The new contribution in this bundle is the explicit counterexamples, careful quotient scope, direct product-separation corollary, and the precise assembly/review of the supplied statements.


## Follow-up: finite Frobenius data cannot force fixed-support incidence

**KT-RM-FROB-AVOID** strengthens the carried A37 avoidance method to any prescribed finite symplectic Frobenius class, even at the same primes whose theta torsion is to be excluded. The proof in `rm_frobenius_avoidance.tex` freezes determinant valuations of suitable deeper ell-adic lifts, then applies carried joint monodromy, specialization, and A19. It excludes all powers and products of a prescribed finite prime support and works in any nonempty ordinary O5 open. It leaves exact field size and Weil polynomial free.

**KT-RM-FROB-NONDETERMINATION**, the positive/negative comparison at every finite4159-adic precision uses the actual A13 positive curve and defines the common class from that curve. It does not assert positive incidence for arbitrary Frobenius data. Thus a criterion based only on finite Frobenius/RM information cannot force a theta witness from a fixed finite prime support. The universal question permitting curve-dependent primes remains unresolved.

The author and lean-chain independent whole-proof checks passed. The peer requested characteristic two be explicit in the HB-locus statement; this wording is now included. Root independently whole-read both new results and complete A19/A37 and reported PASS. `ROUTE2_EXPLORATION.md` records the separate mixed-difference experiments that found no further RM exclusion and the capped/failed runs. Those experiments are not used in the proof.
