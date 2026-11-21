# A51 weighted Weil supplement: independent whole-proof and source review

Date: 2026-11-21. Reader: GPT-6 Astra Pro; effort not exposed; /root/effective_galois.
Source: work/gt_certificates/positive_rank_theta/A51_WEIGHTED_WEIL_SUPPLEMENT.tex.
SHA256: e0e7a37754305e69955f2faa4210867fe6da814544aa20a7369ead855a31aff0.
Outcome: PASS. The entire statement, proof, formulas WV.1–WV.6 and final limitation paragraph were read. No correction requested. This is not formal verification.

For Q=q^f, trace one satisfies Waterhouse's ordinary case for every p and f in the statement. The elliptic point group has order exactly Q and is nonzero. Ordinary geometric p-torsion has rank one; a nonzero finite abelian p-group of rational p-rank at most one is cyclic. Thus E(F_Q) is cyclic of exact exponent Q, not merely bounded by Q.

Finite-field Weil restriction is an abelian variety geometrically equal to the product of the f conjugate ordinary elliptic curves. Its dimension is f and it remains ordinary. The degree-one elliptic polarization descends as the product principal polarization; the cited primary proposition covers the principal polarization and the line-bundle descent. The functorial equality of rational groups gives the exact cyclic group claimed. The induced auxiliary-adic representation gives H_A(T)=H_E(T^f), and therefore the asserted cyclic Frobenius-polynomial shape and exact special-value valuation.

The additional direct Weil-root check is correct: a root alpha of X^(2f)−X^f+q^f has alpha^f of complex modulus q^(f/2), hence alpha of modulus sqrt(q). The reciprocal identity and integral coefficients hold. For f=phi(ell^r), the exact exponent is exponential in n=ell^r and fails the cited small-exponent inequality for large n.

The scope limitation is essential and correctly stated: these are actual ordinary principally polarized abelian varieties, but no integral cyclotomic deck action, Jacobian-cover realization, proper-conductor maps, compatible geometric tower, fixed underlying genus-two curve, or prescribed split point is produced. This proves only that the listed numerical, weight, principal-polarization and rational-generator constraints are insufficient by themselves.

## Exact primary reading

1. W. C. Waterhouse, Abelian varieties over finite fields (1969), Theorem 4.1(1), printed pp. 536–538, and Corollary 4.4, printed p. 540. URL: https://www.numdam.org/article/ASENS_1969_4_2_4_521_0.pdf . I read the complete theorem statement and displayed proof in the retained extracted text, including the intermediate decomposition argument, and the complete corollary and displayed proof. I then independently viewed printed pages 536 and 540 to confirm the exact ordinary case and p-torsion assertion where OCR was weak. The cited Honda–Tate background was not independently reproved. Retained PDF SHA256: 7be2bf9dde45454afa3dd9a0ea1ba05acbe952b6b573a0c37c2b1b8f0cccbb47.

2. C. Diem, A Study on Theoretical and Practical Aspects of Weil-Restrictions of Varieties (2001 dissertation), Proposition 1.21, printed p. 26, and section 1.3.4/Proposition 1.22, printed pp. 27–28. URL: https://www.esaga.uni-due.de/f/ulrich.goertz/iem-archiv/dissertation_diem.pdf . I read the complete Proposition 1.21 statement and displayed proof and the complete section 1.3.4 argument through Proposition 1.22, including the product polarization and descent. I independently viewed all three printed pages to confirm the exact formulas. The earlier dual-Weil-restriction normalization is cited there; this is not a whole-dissertation review. Retained PDF SHA256: d4f98857706e83fc5b8341988df44c3cdc24149026a2a4d4674ffa29c480d08d.

The primary files are retained only in the working source cache. No full source scan or page image is proposed for inclusion in the deliverable. The five individually viewed page images are under work/effective_galois/weighted_weil_review/. An earlier truncated multi-image output was not counted as visual reading; each listed page was subsequently opened separately.
