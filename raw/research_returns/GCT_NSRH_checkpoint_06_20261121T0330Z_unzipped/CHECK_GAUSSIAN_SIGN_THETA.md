# F50 author check record

Date: 2026-11-21 UTC. Checker: /root/rectangular_and_theta.

## Exact code and source inputs

- Script: check_gaussian_sign_wrapper.py.
- Script SHA256: ef2303607a0b6274da20438d21868d3cc2989e89ad168d5028b9208b117eadc5.
- Current proof report after review clarifications: agent_gaussian_sign_wrapper.md, SHA256 13f67e1c418422629606752238ca1352c8f74a604d86535150f984a3e95b9bc6.
- Original SGA4 1/2 PDF: primary_sources/Deligne_SGA4half_original.pdf, SHA256 fb2939521f4c0ea0cdd55a90bec2e618e32fb433c78b194e705c6d989f4e42a6.

The original Gaussian statements and full proofs on printed pages196--197 were read in extracted text and rendered images. They are PDF pages235--236. Their correct perfect pairing into E(-1), not the misprinted absolute-value shorthand, is the source input. Milne's complete statements of Theorem17.10, Proposition18.4, Theorem22.1, Remarks22.3(b),(d), and Proposition22.5 were read in the downloaded original author PDF and local extracted text. These are source applicability checks, not independent reproofs of the general etale formalism.

## Exact executable results

The script exited successfully with the following results:

    Tridiagonal determinants and consecutive coprimality: k=2..10 PASS
    Sufficient squarefree condition: p=3,5,7,11,13 and even k<=30 PASS
    Exact cyclotomic G12 and graph zero-count: p=3, k=2 PASS
    Exact cyclotomic G12 and graph zero-count: p=3, k=4 PASS
    Exact cyclotomic G12 and graph zero-count: p=3, k=6 PASS
    Exact cyclotomic G12 and graph zero-count: p=5, k=2 PASS
    Exact cyclotomic G12 and graph zero-count: p=5, k=4 PASS
    Exact cyclotomic G12 and graph zero-count: p=5, k=6 PASS
    Exact cyclotomic G12 and graph zero-count: p=7, k=2 PASS
    Exact cyclotomic G12 and graph zero-count: p=7, k=4 PASS
    Exact cyclotomic G12 and graph zero-count: p=11, k=2 PASS
    Exact cyclotomic G12 and graph zero-count: p=11, k=4 PASS
    Excluded p=5,k=4: d4=(h^2-1)^2 and d3(+-1)=3 mod5 PASS

The exponential-sum check enumerates the finite prime-field tuples, records their additive-character exponents, and compares polynomials exactly modulo the prime cyclotomic polynomial. No floating-point evaluation is used. The bad p=5,k=4 case checks the general rank-dependent sum G12; it is not incorrectly counted as a good squarefree path length.

## Scope

These computations check signs, minor conventions and finite examples. The proof for every good even path length and all finite extensions is the determinant/monodromy/Leray proof in the report, not an extrapolation from these examples.

The parent independently reconstructed the complete original report and requested the explicit integer-weight precision. The independent source/proof reviewer requested the Newton-identity algebraicity check and the common-weight condition across embeddings. Both are incorporated in the displayed report hash. Their independent review records are separate from this author's source/computation record.
