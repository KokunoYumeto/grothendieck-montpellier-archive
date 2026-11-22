# Independent audit of HD-E8-01–02

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed. HODGE_DIVISION, 2026-11-21, approximately 12:51–12:54 UTC.

**PASS.** I read the complete `research/e8_source_gate.tex`, the three exact arithmetic programs it identifies, and the published Carter source at Proposition 21/Table 3, pages 22–23, and Tables 9–11, pages 50–54. The complete class classification remains a published input, not a newly verified enumeration of the 696,729,600-element group.

The independent program `audit_e8_local.py` reconstructs all 112 representative matrices from the words and the displayed Cartan matrix. It uses Sympy's rational Gaussian domain matrices and does not import the author's arithmetic helper. It obtains the determinant of 1−g on the moving space by deflating the characteristic polynomial at x=1, a method different from the author's restriction-of-operator calculation. It obtains the moving Gram determinant from independent columns of 1−g. All 224 real and imaginary-coset local computations pass. The full imaginary-coset spectra and ages are also independently matched from the reconstructed characteristic polynomials.

Exactly the six reported imaginary-coset classes have nonnorm invariant: 55,56,57,58,101,102, all of moving rank eight and Gaussian norm class three. All real classes have norm invariant. The only imaginary-coset class of moving rank four is class6, with balanced involution spectrum and norm invariant. Every other imaginary-coset class has larger moving rank. The resulting JSON retains every independently checked invariant.

The geometric deductions in HD-E8-02 are valid. A sixfold gives total moving rank22 over a genus-zero base. Higher-genus sources have insufficient dimension. Nonsplitness requires a rank-eight exceptional inertia, while the coset-product relation requires a second imaginary-coset inertia, of rank at least four. Twelve branch points therefore force exact equality: ten reflections and those two entries. Their fixed ages force the rank-eight entry's age to equal four, leaving exactly classes57 and58. Its local class is three, and all remaining local factors are norms. The exact spectra give branch orders (2^11,12).

The statement is correctly a necessary pattern. This audit does not certify a product-one generating tuple, actual period rank nine, or algebraic cycle suppliers. Those are separate tasks.
