# A.115 / A.115R complete root audit

Actual audit: 2026-11-20 01:13:14 UTC.
Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), root.
Type: used and rechecked in this run; full targeted proof audit.
Outcome: PASS.

We read the complete archived A.115 proof in parts/parametric_concordance.tex, recovered from checkpoint14. We also read all three literal parts of the fresh 11,721-character A.115R reconstruction. The archived proof is preserved unchanged. A.115R is supplementary independent reconstruction documentation.

The source, target, and parameter complexes form the allowed one-way simultaneous subdivision chain. Refinement of fixed product cells is retained separately on source and target. The matching-vertex maps cover the same base map beta on every simplex, since all relevant restrictions are affine; vertex equalities therefore imply the full projection identities.

After correcting the common base map, the source and target maps preserve each product cell. They agree on the bottom and parameter boundary; they need not individually be identity there. Total-product coning first extends the common data and then the remaining cells. The coning map is jointly PL and preserves both parameter and isotopy time exactly. Conjugation through a face-preserving PL isotopy of beta removes the parameter change.

The fresh proof's equivalent factorization uses k=R_t R_s^{-1}, which is pointwise identity on the fixed subcomplex E, and a=(id x beta)^{-1} R_s. Its identity H_F=k B a H a^{-1} B^{-1} checks exactly. Contracting k rel E and a through cell-preserving families, then beta, retains every mark and every based condition.

For injectivity, a finite actual PL filling format gives a first-order existence statement over F, with exact equality to the prescribed F-PL boundary graph. Real closed field elementarity descends the filling. No boundary triangulation needs to have all its vertices over F in the original K-realization. No path in an arbitrary coefficient cell is asserted to be PL.

Original source reopened: Shiota, arXiv:1002.1508, Lemma1.1 p.2 and Lemma1.2 pp.3–5. The archived proof additionally records opened Rourke–Sanderson Theorems2.14–2.15 pp.17–19. The parameter-preserving coning and finite first-order descent are supplied explicitly in our proof.

This establishes the required normalization of any PL homotopy class to real-algebraic coefficients on a rational finite PL model. It does not by itself prove the definable-to-PL comparison.

