# Independent complete audit of D-BI-21a–c and the A1-core exclusion

**Outcome: PASS.** Reviewer `/root/imprimitive`, GPT-6 Astra Pro, inherited reasoning effort not exposed, HODGE_DIVISION, 2026-11-21. This is an independent whole-proof review and a fresh computational reconstruction. The published character tables remain explicit mathematical inputs; this audit does not reconstruct those tables from group presentations.

The proof reviewed is `agents/g34_eightfolds/bireflection/a1_core_section.tex`, SHA-256 `5e1cc5935fd781a3959c8cc4f1713bf6564a59e912b02c8a531970e57fd5a56f`. The complete character input has SHA-256 `5ed905449e1f6f64f3eb18b27a213fc5c72e0731dbd591670166e8763ad7fc88`.

## Whole-proof review

I read the entire proof and both original programs, `a1/export_and_scan.g` and `check_a1_spectra.py`. I checked the following issues in full.

1. The inventory covers all cyclic outer subgroups, including the proper order-two subgroup at q=16 and all three subgroups at q=27. There are fourteen retained core tables and nineteen extension tables. This agrees with my separately exported CTblLib inventory, including its source strings and actual core fusions.
2. The mixed diagonal-field obstruction at q=p² is valid: for the displayed matrices, α²=inn(u) and α(u)=−u. An intertwiner whose square is a scalar multiple of ρ(u) cannot conjugate ρ(u) to its negative. On the universal cover 6.A6 the unique lift and the central element z have the asserted properties; z³ is the central involution. This correctly forces invariant characters to factor through 3.A6 or L2(25), respectively, before the corresponding actual extension table is used.
3. Every actual finite linear normalizer is covered. Perfectness removes central automorphisms, Schur's lemma removes the linear centralizer, and rescaling an intertwiner makes its power equal to the prescribed inner element in an actual cyclic extension. This handles arbitrary scalar phases and nonsplit extensions without assuming all characters are invariant. The inner adjustment does not lose the original matrix: it remains an element of that represented extension.
4. The exceptional degree-five A6 rows are precisely the two deleted six-letter characters, related by an outer automorphism. Their full linear normalizer is scalar times the corresponding S6 image. Thus the exceptional case falls under the already reviewed scalar deleted-standard theorem, rather than being discarded by a character-ratio estimate.
5. The tensor argument uses the correct nonscalar eigenspace codimension. A factorwise action inherits the one-fifth bound; a nontrivial factor cycle has the stronger one-quarter bound by the previously reviewed weighted word-orbit argument. The actual Hurwitz identity gives 12 ceil(e/5) ≤ 2e+6. A degree-five exceptional tensor factor with at least two factors has e≥25, so it is impossible. With no exceptional factor, the one-quarter inequality excludes every e≥5. The large-field part uses the already reviewed D-BI-20 only after its degree hypothesis is checked.

No nonsplitness is needed for the small-field e≥6 exclusion. The last e=5 step uses the nonsplit target hypothesis through the scalar deleted-standard theorem. This distinction is retained correctly.

## Fresh finite reconstruction

The new file `independent_check.py` imports no GAP calculation, no original selected-row list and no G34 arithmetic implementation. It reuses my earlier independently authored exact cyclotomic-polynomial arithmetic, selects every extension row by pointwise equality of its complete restriction with a complete core irreducible character row, and computes the entire Fourier spectrum of every nonscalar entry in an exact cyclotomic quotient ring. This is a different selection and Fourier implementation from the author's restriction-norm and Ramanujan-trace checker.

The actual run completed in **3.041 seconds**, with output `independent_check.json`:

- all 33 tables and all 654 selected rows;
- all 18,922 nonscalar spectra, with integral nonnegative multiplicities and correct degree sums;
- minimum codimension ratio exactly 1/5;
- exactly the four quarter-bound exceptions in table 6.A6.2_1, rows 3,4,5,6 and classes 20,20,21,21;
- their core restrictions are rows 2,2,3,3 of 6.A6 and kill its center;
- no one-fifth failure.

The exception spectra, starting with eigenvalue 1, are respectively (4,1), (1,4), (4,0,1,0), (1,0,4,0). The program also matches the complete table inventory and fusion data against my separately exported primary metadata. All output was inspected after the run; no computation is merely proposed.

## Primary-source review and limits

I freshly read White's published paper *Character degrees of extensions of PSL₂(q)*, publisher PDF DOI `10.1515/jgt-2012-0026`, especially the full automorphism description in §§2–3 and the complete statements and proofs of Lemmas 4.4–4.6 on numbered pp. 9–10. These give the diagonal/field actions used in the degree-five exceptional normalizer argument. I had independently exported and inspected CTblLib's exact construction labels: at q=9 the first outer class is field/S6 and the second is diagonal/PGL, whereas at q=25 these first two labels are reversed. The third is mixed in both cases. The universal-cover exceptions are explicit published inputs, not inferred from spectral checks.

The primary character-table provenance and full fusion inventory are retained; complete coverage does not rest on a sample of class representatives or a degree cutoff. I do not claim a fresh proof of the classification of universal covers or of the published character tables.
