# Independent local Masullo audit

Owner: GPT-6 Astra Pro; effort inherited/not externally exposed; MAS_ARTIN /root/pf26_audit. Date: 2026-11-21.

## Source and privacy

Alessandro Maria Masullo, *The Music of the Primes*, public draft, 940 PDF pages; printed/PDF page numbers agree. Current source SHA-256: `e039d3f6cf0a4b14f03c7edb85097752dd65c0a2fe543c76fe992be234f97bf5`. Source and review page images are confined to `private_sources`; they must not enter the deliverable ZIP. The delivered module contains original mathematical derivations and short formula references only.

## Findings

- **MA-LA-001:** the literal centered Poisson conclusion loses the factor p^(-k/2). Definitions checked at pp.367 and490, centered occurrence at pp.494/496, unweighted asserted answer at pp.494/495. For p2 and a bump supported(1.5,2.5) with h2=1, the two claimed values are log2/sqrt2 and log2. Independent of all nontrivial-zero statements.
- **MA-LA-002:** the printed outer multiplier S→S00 is false. The preceding Fourier cutoff does not preserve flatness even starting from a flat Schwartz input of integral zero. An annular cutoff repairs this codomain.
- **MA-LA-003:** the exact real even trace of the draft's normalized local kernel has different limits as r=Yepsilon tends to0 or infinity: A0(h) and0. Smooth finite cutoffs are rigorously trace class by a Hermite expansion.
- **MA-LA-004:** the defect persists for the draft's thin boundary smoothing rather than only fixed scaled profiles. Explicit paths X=Y=N, delta=N^-4, epsilon=N^-2 versus epsilon=N^-1/2 satisfy all divergent cutoff and thin-smoothing conditions. Sine-integral evaluation and O(delta(X+Y)) smoothing error prove the limits. Sufficient repair: lambda_prime/lambda_doubleprime→0.
- **MA-LA-005:** source p517 first uses a transposed K and then substitutes the delta for the oppositely transposed K, losing a Jacobian in the intermediate equality. In the real even sector these slips cancel; final corrected local density can be recovered directly. This finding is explicitly not promoted to another counterexample to that final density.
- **MA-LA-006:** source cyclic nuclear-trace lemma is valid and independently reproved. Mere precompact convergence does not imply trace convergence; a nuclear lift, stronger than range inclusion, is required. The local smooth annular model has such a lift; no global weighted-space lift is certified here.

## What was checked

The entire argument of the target local pages was read, exact displayed equations on pp496/514/517 were visually inspected, and each new proof was reread in full after writing. No formal proof assistant or numerical spectrum calculation was used. The actual model is GPT-6 Astra Pro; effort setting is inherited and not externally exposed.

The initial standalone LaTeX attempt found a missing pdflatex.fmt. This environment issue was subsequently resolved by initializing the installed pdfTeX format and supplying the installed scalable-font maps. The integrated MAS_ARTIN report compiles successfully; its build and rendering checks are recorded separately.

## Ongoing review

Parent/root has a new explicit theta–Möbius smooth intertwiner route in trace_global.tex. Initial independent algebra check confirms its n^-1/2 factors, zeta(s+1/2) Mellin factor, zero-moment cancellation, finite Euler removal, Möbius inverse on theta image and compact-interval tail support. The spherical finite-adic spanning statement preserves the two moments after combining summands by the product formula. Full source/proof review follows in separate events.
