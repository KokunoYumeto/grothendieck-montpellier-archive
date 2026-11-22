# Contributor reading of the final HD-AST07–09 proof

Reviewer/contributor: `/root/imprimitive`, GPT-6 Astra Pro, inherited reasoning effort not exposed, project HODGE_DIVISION, 2026-11-21.

**Result: contributor verification PASS.** This is not an independent-origin peer audit of a jointly derived proof. I independently supplied the Cauchy estimate, verified the root's remaining scalar cases, and then read the entire final written proof and every line of its exact checker. The separately assigned `/root/g34_eightfolds` review supplies the independent whole-proof role.

The root proof is `research/alternating_standard_two_factor_section.tex`. My initial whole reading bound hash `495d06546718236a158131b740c330a62cd1ec02a1c7cf9714d50af10d110520`. I caught one formatting-only error in the condition in (AST2.7): a TeX font escape had become a newline followed by the literal text `m even`. Root replaced it by explicit `\text{even}`. I reread the complete repaired proof at SHA-256 `32b5cc512a130b41b5d6f3d8e0d4f2d5fa02e3714ce9d6ba6d6b89d5a4163108`. No mathematical repair was needed.

The proof correctly treats every target eigenvalue. The Cauchy estimate uses the full permutation spectrum, subtracts exactly one occurrence of the eigenvalue one, and retains the resulting `−2c+1` term in the squared multiplicity sum. It gives the needed uniform baseline when the total index is at least `n`. For smaller total index the root's rational conjugate-pair estimate covers nonreal targets; its fixed-point/grid estimate covers target one; and its odd-cycle count covers target minus one, including cycle-count minima one and two. These are exhaustive cases, not an estimate valid only at target one.

I checked the exact weighted-swap formula, including repeated eigenvalues and identity cycle product. The scalar extraction is an actual homomorphism because the rational wreath image intersects the scalars trivially. This gives a genuine transitive action on `2n` letters and hence an actual connected quotient cover. The Riemann–Hurwitz index sum retains coefficient-cover scalar marks even though their permutation indices vanish.

The all-field source proof is sound. Transitivity and product one force a positive even number of swaps. Four swaps plus eight other genuine marks exceed the moving-rank budget, so there are exactly two. No scalar-conductor marking is used or needed. The final exact lower bound is `D >= 2e+a+5 > 2e+6`. The source reduction uses the actual intermediate-cover variation and does not assert sufficiency of a dimension inequality.

I read every line of `research/check_standard_two_factor.py`. It constructs full grid spectra directly from pairs of cycle lengths, subtracts the two full letter spectra and adds the trivial line at eigenvalue one. Its exact target comparisons, phase denominators, weighted swaps and actual `2n` indices agree with the proof. Root's execution remains attributed to root; I do not relabel it as my independent rerun.

My separate exact spectral-convolution programs and their unchanged outputs are already retained here. Both the initial conjectured coefficient pair and the stronger final bound passed all **478,097** unordered partition pairs for `15 <= n <= 20`; the stronger test completed at **22:46:01.231212 UTC** in **12.020758151 seconds**. Those tests use no root grid implementation. Their finite scope does not establish the universal theorem, whose full proof is separately verified above.

Known inputs were reread in the complete D-AST01–03 and HD-AST04–06 arguments during this run. The exact original-field/inducing-field distinction is preserved, but this particular new two-factor conclusion imposes no arithmetic field restriction. The source interface makes no new classification, cycle-supply, positivity or motivic claim.

The earlier contribution note `CAUCHY_AND_PHASE_DERIVATION.md` preserves the development history and the alternate composite-order edge check. The final canonical theorem uses the shorter Cauchy argument. The font-escape correction was an actual detected source-format error, not a failed mathematical assertion.
