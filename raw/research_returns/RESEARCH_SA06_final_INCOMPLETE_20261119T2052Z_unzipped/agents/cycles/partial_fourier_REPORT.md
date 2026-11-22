# C.4ab: a partial Fourier test for the residual surface case

**Status: proved exact reformulation and method exclusion. No main-gate movement.**

Let A be a complex abelian surface with primitive type-(1,2) polarization L, NS(A)=ZL, and scalar rational Hodge endomorphisms on H1(A) and on T(A). For an integral codimension-two correspondence Z on A^2, let t, s, n be its scalar actions on H1, T, and NS. The primitive norm-four lattice gives n-s=4k. An integral relative Fourier-Mukai K-class E_Z then produces an actual integral curve c2(E_Z)P on A x Ahat, with mixed Matsusaka scalar

    m_Z = 3(t^2-s) - (n-s)/2 = 3(t^2-s)-2k.

Its parity is t-s. Such an odd scalar, together with the already proved universal scalar2, splits A off a product of Jacobians. Conversely any actual splitting gives an integral correspondence with t=1,s=0 by pulling and pushing normalized Poincare divisors on A x C. Thus this is an exact integral criterion, not an unproved promise that a new surface supplies the desired class.

The Bastianelli-Pirola-Stoppino Galois-closure surface is the residual fibre product over a rational ruled surface. The trace-minus-diagonal formula gives t=s=-1, so its partial Fourier transform is excluded. This calculation is stronger than citing only its Albanese variety: a transformed K-class is not automatically covered by the earlier divisor-pushforward method exclusion.

The criterion does not replace ordinary Chow classes by etale Chow classes. The June2026 Kahn preprint supplies etale integral projectors and explicitly separates their algebraicity in ordinary Chow from the etale statement.

## Retained artifacts

- `partial_fourier_correspondence.tex`: full proof and exact scope.
- `partial_fourier_references.bib`: three fresh primary references; existing BPS and Voisin keys reused.
- `code/check_partial_fourier_parity.py` and `output/partial_fourier_parity.json/.out`: exact rational exterior algebra and finite checks.
- `code/fetch_partial_fourier_sources.py` and its JSON/stdout: complete primary PDFs, SHA256, bytes and actual runtimes.
- `code/compile_partial_fourier.py`, wrapper PDF and logs: final typesetting checks with actual runtime.

The main type-(1,2) splitting problem remains unresolved by this criterion.

Registration UTC: 2026-11-19T12:20:29.079164+00:00
