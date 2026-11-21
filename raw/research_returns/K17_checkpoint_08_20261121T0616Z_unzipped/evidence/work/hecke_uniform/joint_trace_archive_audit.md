# Independent whole-proof audit of the joint residual trace criterion

Reviewer: `/root/archive_kummer`, GPT-6 Astra Pro. Date: 21 November 2026.

**Verdict: PASS under the section's retained stipulated arithmetic-source inputs.** Entire final TeX reviewed: `work/hecke_uniform/joint_trace_section.tex`, SHA256 `aafd45cd09be9003b923e4db3c3e6cb871d3e8ff7bf481b98ea7063f775564fb`. This is a mathematical/source-content audit. No new Lean compilation, proof-assistant verification, or numerical Hecke execution is claimed.

## Primary source actually read in full

All seven files in `joint_trace_manifest.json` were freshly read from beginning to end in this audit, not merely their exported statements:

- `SmallClassNumbers/CorGKOf.lean`, 29 lines;
- `ModularityArgument/ThresholdArguments/DenseThresholdCases/FOneCharU.lean`, 96 lines;
- `SmallClassNumbers/OnePoint.lean`, 41 lines;
- `UnitaryThreeGroups/IsPtOf.lean`, 166 lines;
- `TheoremsMuLinked/GaloisRepresentationTypes/OneChar.lean`, 216 lines;
- `HeightAndVanishing/CoefIndep.lean`, 77 lines;
- `UnitaryThreeGroups/ModelUpper.lean`, 250 lines.

The complete newly saved `UnitaryThreeGroups/PtShape.lean` and `DatFacts.lean` were additionally read. These confirm the torus-orbit/isomorphism comparison, the exact multiplier kernel, and the residual character facts used in the trace translation. The manifest's pinned-commit URLs and hashes remain the source provenance; reading these proofs does not re-certify every imported external arithmetic contract. That boundary is stated explicitly in the theorem.

## K17-S17-JOINT: reconstruction

The complete unramified construction in `FOneCharU.lean` chooses D, the marked g1, U, S and M before introducing the test-element-specific trace identity. Its strengthened `hadm` assertion is exactly the union of `Adm3U_s` and `Adm2A` written in the new section. The assertion uses the source's Type-I and Type-II outputs and retains the extra hypotheses; it is not replaced by the weaker older admissibility predicates in `OnePoint.lean`.

The no-point contradiction is valid. The identity has eta=1. If there is no TwoPt point, the trace nonvanishing premise of `model_upper` is vacuous even though the identity trace difference itself is zero. The theorem supplies a finite model length before converting normalized zero to actual zero. Its covering set consists of TwoPt points and is therefore empty. With ramification index1, M.len=0; `vlen_le` then contradicts nonzero Vlen. This is the full argument in `OnePoint.lean`, using the stronger admissibility fact available from the other proof.

For a chosen point f, the same representation works for **every** Galois element. In the actual proof of `isPt_push`, `S.r.red` identifies the residue of each entry, and `diagonal_rep_map_entries` identifies the corresponding base entry. Their difference is therefore in the maximal ideal of S.R. The local-point condition sends it to norm strictly less than1. The separate `ipo_le_one` proof also establishes integrality of every pushed entry. Restriction to G_K uses D.eta's exact kernel; the matrix representation is D.rhoK. The exact base trace is Psi+1+Psi^{-1}, as proved by `trace_reducible_three_dim`. The ultrametric inequality applied to the three diagonal differences gives the simultaneous residual trace congruence, with no change of f as the element varies.

Coefficient descent uses precisely both conclusions of `coefIndep`: equality of normalized lengths and equivalence of their being infinite. This avoids the possible error that ENat.toNat sends infinity to0. If the unramified length were0, the original length would first be finite, then have normalized value0, hence itself be0 because its ramification index is finite and positive. Thus nonzero length persists under the unramified coefficient replacement. `exists_unram` and `gd_chHom` preserve the actual character values and the complete datum. The admissibility predicates do not depend on that coefficient-ring choice. The single global congruence therefore descends exactly as stated.

The contrapositive needs no cardinality bound: each representation may have its own detecting element. It is enough that this difference is a unit for each representation; the theorem does not need a single preselected group element to work for all of them.

## K17-S17-GROUP-RING: reconstruction

The full `ModelUpper.lean` proof was checked past the initial trace element, through the final normalized inequality. The only properties of its chosen homogeneous element used are membership in degree0, zero base value, and nonzero evaluation at every two-signed point. Each trace element a_j has these first two properties; a finite Z_l-linear combination preserves them. Its evaluation is the corresponding linear combination of trace differences because the coefficient algebra maps fix Z_l.

For the third property, `M.pts` sends a model point, after the grading torus action, to a local point f. Degree0 makes the chosen element invariant under that torus action. `hadm` and the assumed nonvanishing of d_b then give M5. `LemmaM` applies to this actual homogeneous element. The proof's finite-cover construction, irredundant torus-orbit reduction, push-map comparison and final valuation sum use no further property specific to one group element. The finite representative set may depend on the new element; the final wording correctly says its **selection argument** is unchanged, not that its entries are unchanged.

The isomorphism-injectivity proof `hinj` in `FOneCharU.lean` uses only the point shape and normalized torus uniqueness. It is independent of the testing function, so the finite set of admissible representations has no isomorphic repetitions. The factor2 and the ramification normalization match the source theorem exactly. Coefficient descent preserves the same Z_l coefficients and the exact t(s_j), and uses the same finiteness/normalized-length conclusions as above.

## Joint operator corollary and final scope

Under the stated simultaneous coverage assumption, one global representation gives a simultaneous characteristic-zero eigenvector on one of the integral Hecke lattices. A finite coefficient extension contains the finitely many eigenvalues and that eigenvector. Scaling it to be integral and primitive gives a nonzero vector after reduction. Every scaled trace difference is in the maximal ideal because the scaling factors are units. It is therefore a common residual kernel vector. An invertible linear combination or a unit full-size minor of the vertically stacked matrices excludes it. This proof uses finite free lattices, as in the concrete finite matrix models; no semisimplicity modulo ell is required.

The proof properly insists on simultaneous coverage of a single global representation. Independent characteristic polynomials, with no common module/eigensystem identification, would not justify the criterion.

The finite hyperplane argument is also correct for values in the algebraic residue field: each nonzero F_ell-linear functional has a proper kernel in F_ell^r, of cardinality at most ell^{r-1}. Fewer than ell such kernels cannot cover that space. The stronger point theorem removes this family-size restriction.

Finally, Vlen is defined over Q and is independent of the chosen auxiliary imaginary quadratic datum. Hence nonzero length forces a residual Eisenstein admissible eigensystem for every datum satisfying GD. The section asserts only this direction; it does not infer a Selmer class from an automorphic congruence. No numerical vanishing, Greenberg conclusion or full-kernel equality is certified by this source strengthening alone.

No mathematical correction was requested. The only optional terminology clarification sent to the author was that the integral modules in the joint-operator corollary are the finite free lattices used in its primitive-vector argument; the existing matrix context already supplies that interpretation.
