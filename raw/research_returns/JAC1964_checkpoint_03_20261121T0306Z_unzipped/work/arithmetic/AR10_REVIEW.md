# Independent review of AR-10

Run JAC1964-20261121. Reviewer /root/arithmetic_sign; GPT-6 Astra Pro; effort setting not exposed. Whole-read of work/root/AR10_adelic.tex, recorded 2026-11-21.

I checked the complete proof against Gu's primary v2, Theorem 1.3 (p.2), Proposition 5.3 (pp.12–13), Corollary 1.6 (p.3), and §2.2 (p.5). The following steps agree:

- A middle codimension-m grade-one class in dimension 2m−1 is its normalized generalized Ceresa class.
- Its dimension is m−1; the intersection exponent is 2m−1, and the Lefschetz factorial is 0!.
- The signed height is already normalized, while the arithmetic degree retains division by [K:Q].
- Factor-exchange symmetry permits the bilinear formula by polarization.
- Products of representative components have dimension 2m−2, so the displayed Deligne pairing has the correct number of arguments.
- Finite base change and representative-independent degree are stated correctly. No canonical isometry between all representatives is asserted.
- The diagonal and anti-diagonal restrictions of Q are respectively 2L and −2L, so no nefness or sign follows formally.

One minor category clarification was sent to the author: the constructed object is an integrable adelic rational line. Clearing rational powers does not itself turn every adelic metric into a hermitian lattice in the literal category of Bost 2001. Use the adelic rank-one slope inequality directly, or state a justified model approximation. The adelic argument is elementary: give the image line the induced metrics, sum the inequalities furnished by the local operator norms, and bound the degree of the image line by the maximal slope of the target. This does not alter the sign or create a new positivity theorem.

No mathematical error was found in the identity or construction. This is an independent written proof check against the specified statements, not a formal proof-assistant certificate.
