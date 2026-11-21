# Independent review: genuine Kohnen projection discriminator

**Verdict: PASS.** Statement `KT-KOHNEN-THETA-NONCONGRUENCE` disproves the proposed uniform scalar congruence by the explicit case p=31. It does not prove the nonexistence of a simultaneous-unit field, and it supplies no new K-group vanishing.

## Reviewed scope

The entire new proof and standalone Python certificate were read. A copied full certificate was executed successfully and its JSON is byte-identical to the author report. The final proof text has SHA-256 `cc310dfe238d66dcac820d3ba896f9feb90ea7b1e5500ed9391c8068991988e9`; the certificate source has SHA-256 `22af36f1497f66f52b6c15a498ab8071950c3d09c21d8d52ce3395196969f20d`; both report copies have SHA-256 `969ecad4f50f1ad1201e449c6e9d4a4795b13642c219c872754517451e063d81`.

Matsusaka's 2019 thesis, printed pages 27–28 (PDF pages 36–37), was read for the precise slash operation, plus-projection formula, phase, and Remark 2.3.2. The compatible lift has phase exp(pi i/4), without a weight multiplier in that exponent. The statement that this operator maps to the plus space is imported from that primary source. The corresponding Bruinier–Jenkins–Ono author text, printed pages 14–15, formula (3.12), was checked to distinguish its idempotent normalization and its printed extra-phase problem. No whole-thesis or whole-paper proof review is claimed.

## Mathematical checks

All four cusp transformations were checked, including the matrix factorizations, the theta multiplier i at the matrix (3,1;8,3), the odd-square Poisson identity for (1,0;2,1), and the inversion formula. Fixing square-root branches at tau=iy gives the stated signs. For n congruent to 3 modulo 4, the first and third transforms contribute s sqrt(2) r_m(n), the fourth is supported at multiples of 4, and the odd theta power starts in degree m. Thus the normalized projection coefficient really is r_m(n) for 0<n<m in that residue class. The harmless scale relative to the idempotent projector is nonzero modulo 31.

At m=35, the two coefficients n=3,7 reduce to (1,2). The two Cohen Eisenstein coefficients reduce to (26,16). Their determinant is 26 modulo 31, so no common scalar exists. The exact normalized generalized Bernoulli values are −252470402/3 and −99245951007872. The code evaluates these by exact Fraction arithmetic and independently reconciles them with conductor 31d character sums modulo 31², d=3,7. Exact integer convolution supplies the theta coefficients 52360 and 864089600 and checks the mod-31 Frobenius comparison to theta^4.

The certificate's role is the finite arithmetic calculation. The plus-projection coefficient identity is justified by the accompanying proof, not inferred from a numerical transformation experiment.

## Provenance

The final formatting repair replaced two malformed carriage-return escapes with `\mathrm{odd}` and stated p congruent to 3 modulo 4 in the opening. The final text was reread after this repair. Full file hashes, actual check date, and copied replay status are in `kohnen_theta_review_manifest.json`; the replay is under `kohnen_theta_replay/`.
