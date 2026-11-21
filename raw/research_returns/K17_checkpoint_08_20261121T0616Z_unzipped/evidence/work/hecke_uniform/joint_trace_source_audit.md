# K17 joint residual trace deduction: source and author audit

Date: 2026-11-21. Author/checker: `/root/vandiver_k`, GPT-6 Astra Pro.
Effort: not exposed. Run: K17.

Status: complete proof written and read back by its author; independent
whole-proof audit requested from the parent and archive agent. All statements
retain the stipulated arithmetic source inputs. No new Lean compilation or
unconditional conjecture resolution is asserted.

The complete deliverable is `joint_trace_section.tex`. Its substantive IDs are
K17-S17-JOINT and K17-S17-GROUP-RING. The first statement is stronger for
vanishing: a nonzero source Selmer group forces a **single** actual admissible
representation with the Eisenstein residual trace at **every** Galois element.
Thus detecting elements may depend on the representation. The second statement
retains the source's quantitative inequality for finite linear combinations of
trace differences with coefficients in `Z_l`.

## Exact primary source locators

All source references are to pinned commit
`7cbf7a0c32fca1badf05931879a37c3f8a2b03b4` of the recovered Lean mirror.
The path prefix is
`src/Development/AutomorphicArithmetic/AutomorphicVarieties/`.
`joint_trace_manifest.json` records exact local paths, URLs, and hashes.

1. `SmallClassNumbers/CorGKOf.lean`, entire file, especially lines 10–18
   (`corGK_of`) and 20–25 (`litN`, `corGK`). The same closed inputs are
   explicitly passed to the stronger `oneCharU_of_katoTwoW_rig_admI_automorphy`.
   This is the existing stipulated-source boundary, not a newly verified
   external literature chain.
2. `ModularityArgument/ThresholdArguments/DenseThresholdCases/FOneCharU.lean`,
   entire file. Lines 19–74 are the complete `oneChar_unramU` proof; the model
   construction is lines 32–37, the trace identity `htr` lines 42–47, and the
   strengthened `hadm` assertion lines 48–54. Lines 55–58 give the exact
   `PtHyp` call and `vlen_le`. Lines 59–74 pass from points to representations
   without isomorphic repetitions. Lines 75–96 remove coefficient
   ramification. The datum/model and `hadm` do not depend on the test element.
3. `SmallClassNumbers/OnePoint.lean`, entire file. Lines 27–35 contain the
   complete empty-`TwoPt` contradiction. At the identity test element the
   nonvanishing condition is vacuous if no points exist. The covering set is
   empty, so the finite model length vanishes. Its older admissibility
   predicates are replaced here by the exact stronger `hadm` assertion in
   item 2, using the same construction and stronger available inputs.
4. `UnitaryThreeGroups/IsPtOf.lean`, entire file and proof. The theorem
   `isPt_push` begins at line 124. Lines 136–145 prove the entrywise residual
   congruence directly: `S.r.red` and `diagonal_rep_map_entries` show that the
   difference is in the maximal ideal of the deformation ring, and the local
   point maps it to norm strictly less than one. `ipo_le_one` also proves
   entrywise integrality; the full preceding continuity argument was read.
5. `TheoremsMuLinked/GaloisRepresentationTypes/OneChar.lean`, entire file.
   `trace_reducible_three_dim` computes the base trace as `Psi+1+Psi^-1`.
   `exists_unram` uses the prime-to-l character order; `gd_chHom` preserves
   the full source datum; the coefficient-change identities preserve the
   actual character values, not merely their residues.
6. `HeightAndVanishing/CoefIndep.lean`, entire file. The exported `coefIndep`
   begins at line 68 and proves equivalence of infinite lengths **and**
   equality of normalized lengths. It does not claim literal equality of
   unnormalized lengths. Together with finite positive ramification indices,
   this proves equivalence of vanishing, including the case in which the
   original length might initially be infinite.
7. `UnitaryThreeGroups/ModelUpper.lean`, entire file. The theorem starts at
   line 103. Lines 133–148 construct a degree-zero trace element `a`, with
   evaluation identity `hqa` and zero base value `hxa`. Lines 149–158 prove
   `M5`; lines 159–160 apply `LemmaM`. The complete rest of the proof through
   the final normalized inequality uses only those properties of `a`, not
   its being the trace of one group element. Replacing it by a finite
   coefficient-linear combination is therefore valid. The finite covering
   set may change with `a`; the argument constructing it is unchanged.

## Complete proof checks

The author freshly read every file listed above in full and reconstructed:

- the identity-test empty-point argument, with finiteness retained before
  converting normalized length zero into actual length zero;
- the stronger Type-I and Type-II admissibility assertions with the exact
  source predicates;
- entrywise residue compatibility and the ultrametric passage to trace;
- the quantifiers: one chosen point works for every group element;
- coefficient descent using both conclusions of `coefIndep`;
- homogeneous degree, base point, and torus-invariance for arbitrary finite
  `Z_l` combinations;
- the complete unchanged orbit-cover and isomorphism-injectivity arguments;
- the factor 2 and ramification normalization in the bound;
- the integral primitive-vector argument converting simultaneous Hecke
  coverage into a common residual kernel, and the determinant/stacked-minor
  sufficient tests;
- the finite hyperplane counting argument and its strict condition `n<l`;
- the final one-way uniform reduction, with no converse from automorphic
  congruences to nonzero Selmer groups asserted.

The full TeX was read back after writing. A wording refinement distinguishes
the unchanged representative-selection **argument** from an assertion that
the selected finite set itself is unchanged. No mathematical gap was found
in this author audit. Independent audit remains a distinct event.

## Numerical boundary

No new K-group vanishing follows merely from this source strengthening.
The parent has found common residual kernels for the current full U3
operators at 7 and 13, so those particular pairs of tests do not yet remove
the higher4 residual supports. Those numerical reports have not been
independently audited in this note. The stronger theorem is useful because
it identifies the precise joint congruence obstruction rather than requiring
one Frobenius element to separate all forms at once.

## Same-basis check for the existing full U3 matrices

`work/hecke_general/harmonic_hecke_certificate.py`, lines 235–285, was freshly
read. The harmonic basis `H`, swap signs, and evaluation matrix are stored
once per degree, outside the prime loop. Both prime records use that basis.
The rational-form basis change uses only the fixed swap signs, so the saved
`rational_real_form_operator` matrices for 7 and 13 are expressed in the same
basis and may be combined. This check is independent of whether the resulting
joint determinant is a unit.
