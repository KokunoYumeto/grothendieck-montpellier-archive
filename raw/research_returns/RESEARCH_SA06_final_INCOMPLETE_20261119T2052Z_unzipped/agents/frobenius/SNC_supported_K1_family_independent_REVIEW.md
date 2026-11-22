# Complete independent review of the supported K1 construction

Reviewer: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode, `/root/frobenius_continuation`; inherited effort.  
Completed: 2026-11-19T19:13:37.274055+00:00.  
Verdict: **PASS for HK.1–HK.3 in the displayed auxiliary scope.** No main-gate movement, ordinary K0-family statement, valuation specialization theorem, or final quotient vanishing follows from this receipt.

The complete proof file `agents/cycles/SNC_supported_K1_family_RESEARCH.tex` was read and independently reconstructed; current SHA-256 is `c5d4cb38a4f07db5e877e8a9be8f591f4970263cfbbfba8281370b86ba0166da`. Its complete companion research/source note was also read. No program or compilation was rerun.

## Detailed proof check

1. Moving a component representative away from the double boundary and placing its finite support on a high smooth connected proper curve A_i are the same precise moving/Bertini steps already audited in C.3br. Transversality to every edge and avoidance of all finitely many triple points are compatible open jet conditions. A degree-zero divisor on A_i gives L_i∈Pic0(A_i), and its line-bundle K0 difference pushes to the exact specified point-cycle class by the Cartier-divisor exact sequences. Denominator clearing occurs before this construction.
2. VE applies to these A_i as its input curves and marks all A_i/edge intersections. It gives one actual proper parameter P, with literal zero restrictions in K1(P) at every marking. Its two endpoint values are the asserted zero and u([L_i]−1).
3. The pushforward A_i×P→E_i×P is a regular closed immersion into the smooth component product and is therefore a permitted perfect proper pushforward. The proof does not push A_i directly into the singular E. The union W can acquire additional isolated points on E_i from neighboring curves; enlarging support from A_i to W_i is permitted and does not affect the construction.
4. Transversality gives Tor-independent squares with each incident double curve. The supported base-change homotopy identifies the restriction with the sum of point pushforwards of the exact zero marked K1 classes. Thus the edge restriction vanishes in the actual supported group, not merely after forgetting support.
5. Applying the established rational closed-union descent to the ambient product and to the open complement, then taking their homotopy fibre, gives supported descent with its actual coherent nullhomotopies. W misses every triple point, so the entire third column has zero support spectrum. The resulting two-column fibre sequence HK.3 is exact at the needed K1 component tuple and provides an actual supported lift.
6. Forgetting support and using supported endpoint base change plus the projection formula gives the two component endpoint tuples separately. An arbitrary kernel ambiguity in the global lift has no component effect. No Adams decomposition of K1 or claim about a selected global K0 lift is needed.

The negative-exceptional hypothesis is indeed unnecessary for this auxiliary construction. Characteristic p>0 is used for the singular rational descent. The marked construction itself remains integral on the regular products.

## Exact primary-source reading

Freshly opened the primary Thomason–Trobaugh published PDF https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Thomason-Trobaugh.pdf . Read complete Section3.16, printedpp319–320; Proposition3.17 with its full proof, pp320–321; Proposition3.18 with its complete proof through the explicit supported analogue, pp321–322. Exact retrieval references: `turn190960836view0`, `turn190960836view1`, `turn521408174view0`. The complete raw-support localization proof of Theorem7.4 was freshly read earlier in this same continuation, as recorded in the PL note. Previously completed exact source proofs for VE, the SNC descent and prescribed-point Bertini are reused; no new reading of their entire original literature is claimed here.

The theorem is ready to be retained as an audited auxiliary result. Its proposed valuation desuspension remains a separate research gate. The node obstruction and the distinction between abstract Picard tensors and exterior products have been checked and are real limitations of the proposed shortcut, not objections to HK itself.

Typography-only closing recheck at 2026-11-19T19:15:27.900324+00:00: the shortened heading and the displayed component tuple at the start were freshly read. They change no mathematical assertion or proof. Current HK SHA-256 is `7b9b1db9ccae381156ea243ef524912f388ad4d455e1582a2127d4be9a99de0c`. PASS is retained.
