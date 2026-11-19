# All-genus completion: F.3.32

The exact polynomial calculation and the actual subgroup maps now prove the original CM common-kernel assertion of LM6 A.22. The production theorem is F.3.32 in `sections/F_audit.tex`; the complete independently audited draft is `work/F3_32_integrated_text.tex`.

## Exact finite certificate

The complete Levi-invariant single-line tangent input has twelve coordinates, with positive multiplicity dimensions 3, 3, 1, 0 and pure-complement dimension 5. Three scalar R rows and four cyclic ES rows form a 7 by 12 matrix M7(s). The five raw detector rows form K(s). For the explicit quotient matrix L from F.3.31, the displayed 3 by 7 integer-polynomial matrix N0 satisfies

`N0(s) M7(s) = 9(2s+3)(4s²+6s−1) L K(s)`.

Every one of the 36 polynomial differences is identically zero. At s=3+t the denominator is `9(9+2t)(53+30t+4t²)`, positive for t≥0. Thus there are no exceptional integers s≥3. Seven necessary rows suffice; their completeness as mixed equations is not asserted or required.

The standalone program recomputes every input and scalar row, with no stored matrix, pickle, interpolation or inverse. The final frozen code is `output/RESEARCH_SA07/code/check_all_genus_single_line.py`, SHA256 `7d11658b85e6ee10a86c18ea8c8758dd9bc4ee8eb2fc4b82195a07b14187f653`. Root registered it as mathematical program 44 and reran it successfully in 19.233908 seconds. Generation independently reran the same code in 18.531897790 seconds. Elliptic independently checked all 144 scalar entries by literal words at complement genus 2, then separately checked the polynomial identity over QQ[s].

## Actual mathematical conclusion

The Levi projector preserves the actual universal image, the one-line tangency condition and q6. The five-detector map sends the certified kernel into the span of two actual geometric Johnson brackets. Its injectivity on full symplectic invariants proves q6=0 for every tangent vector in the actual universal image in every genus≥3 and at every rational prime.

F.3.31 already supplies the full profinite counterexample-to-matrix witness, including a residual element invisible in every original maximal pro-prime quotient. Its original proper-homology detector is applied before choosing the prime. Actual finite-cover powers, arithmetic normal cores, rational cusp descent and filling preserve the nonzero proper class and open arithmetic normalizer. The new all-genus identity excludes that witness. Hence the full CM-curve subgroup is cuspidal. Finally, the actual map from cusp inertia Zhat to the maximal pro-ell group sends the ell-component alpha to the nonzero degree-two Magnus class alpha[X,Y]. The explicit UT3 quotient proves cusp inertia meets the common kernel trivially, including ell=2.

The separate extension to general affine hyperbolic number-field curves is assigned to F.3.33. It is not silently substituted for the original CM-curve scope of F.3.32.

## Source and audit status

The proof explicitly imports R-vanishing on actual J7 from the opened 18 August 2026 v1 of Morita–Sakasai–Suzuki, Proposition 4.1, whose proof is presented there as a sketch. Actual mapping-class stabilization and the natural contraction map transfer that result to all required genera. The original five-detector theorem, full-class proper-homology lemma, actual arithmetic universal quotient, and their exact locators are recorded in `audit_after11_source_checks.csv`.

There are 16 new canonical check-event rows and four source-check rows. The inventory remains 307 assertions in 154 source entries, with historical assertion statuses unchanged: 195 PROVED, 44 REFUTED, 28 OPEN, 30 READING, 9 DOCUMENTARY-GAP and 1 NAMED-CONJECTURE-IMPLICATION. The current obligations and dependencies of I.B05.01, I.B05.02 and II.MB15.02 have been updated. Earlier progress and stopping-point wording is preserved verbatim in `audit_after11_superseded_scopes.json`; the original LM6 register reading is preserved.
