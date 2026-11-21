# A51 weighted Weil example: author whole-proof audit

Date: 2026-11-21.

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Source: `A51_WEIGHTED_WEIL_SUPPLEMENT.tex`, SHA256 `e0e7a37754305e69955f2faa4210867fe6da814544aa20a7369ead855a31aff0`.

Bibliography: `A51_WEIGHTED_WEIL_BIB.tex`, SHA256 `cfcc93a76be4434e24e0c233c3a6128abf998d1c49b86fb1349faa3dd835d46f`.

**Verdict: PASS, author complete-proof and scope read.** I read the complete proof, its initial statement, the comparison with the A47 threshold, and both bibliography entries after writing them. The final title was narrowed to “do not force a small exponent,” because the Weil bounds of course still give dimension-dependent upper bounds.

## Mathematics checked

For every Q=q^f, trace one satisfies the ordinary case of Waterhouse's elliptic classification. The resulting elliptic curve has exactly Q rational points. Since this is a nonzero p-group and the ordinary elliptic curve has only p geometric p-torsion points, its rational p-group is cyclic. This proves the exact exponent, not just an order bound.

Weil restriction has the stated rational-point functor, geometric product decomposition, dimension, and ordinary rank. Its induced Frobenius polynomial substitutes T^f in the elliptic numerator. The canonical origin polarization is principal and descends as the product polarization. Thus the constructed object is an actual ordinary principally polarized abelian variety over the fixed field F_q.

The direct root check confirms all roots of the monic Frobenius polynomial have absolute value sqrt(q). Integrality and reciprocity hold, the reduced numerator has the expected cyclic shape, and H(1)=q^f has valuation ef. Its rational p-primary group has one generator and exponent q^f. Setting f=phi(ell^r) gives exponentially large exponents compared with the A47 threshold.

The proof expressly does not produce a C_n deck action, an integral cyclotomic endomorphism action, proper-conductor norm maps, cover point-count congruences, a primitive Jacobian factor, or one compatible tower over a fixed curve. The elliptic curves may vary with f. Hence it disproves only an inference from the listed weights/polarization/polynomial/generator constraints alone. It is not a counterexample to the sought bound for genuine curve towers and is not claimed to close the main witness gate.

## Primary reading actually completed

- Waterhouse, *Abelian varieties over finite fields*, Theorem4.1, printed pp.536–538: complete theorem statement and displayed proof read, including its split-prime ordinary case. Corollary4.4 and its complete displayed proof on p.540 were also read. The earlier Honda–Tate classification and other external inputs used there were not independently reproved. Primary PDF URL and reference IDs are in the source manifest.
- Diem's 2001 dissertation, Proposition1.21 on p.26: the entire statement and proof of the induced representation/formula were read. Section1.3.4 and Proposition1.22 on pp.27–28 were read completely, including the geometric product polarization, kernel statement and descent argument. This is a bounded reading of those source passages, not the complete 135-page dissertation.

Both original PDFs and extracted text are retained under `weighted_weil_sources/`. PDF text extraction reported one malformed-number warning while processing the scanned Waterhouse file; the relevant statements and proofs had also been read through the primary web PDF extraction. No mathematical claim relies on the warning-producing PDF metadata.

No explicit elliptic equation was computed, no curve-point enumeration was run, and no independent arithmetic implementation is claimed. The construction is an existence argument using the exact primary classification theorem, followed by the checked group and Weil-restriction deductions.
