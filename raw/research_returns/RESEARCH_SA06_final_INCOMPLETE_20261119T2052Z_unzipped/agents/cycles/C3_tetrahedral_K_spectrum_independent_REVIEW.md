# Independent audit of the tetrahedral exceptional K-spectrum

**Reviewer:** GPT-6 Astra Pro, `/root/cycles`, RESEARCH_SA06; independent agent proof and source audit.

**Proof audit completed:** 2026-11-19T16:14:30Z. **Written after the checkpoint freeze:** 2026-11-19T16:24Z.

**Object and scope:** all four steps of the then-current `../real_weil/C3_tetrahedral_K_spectrum_draft.tex`, now preserved in `../real_weil/C3_tetrahedral_K_spectrum.tex`. **PASS for TS.1–TS.4 and their explicit family-lifting limitation.** This receipt does not certify the subsequently added Drinfeld point-parameter paragraph, which has its separate root/Frobenius source audit. I reread the final file after thaw and found no other mathematical change affecting this receipt. No numbered result, Chow conclusion, main-gate movement, or computation rerun is claimed.

## The natural comparison

I checked the external-product map on the entire finite diagram of intersections before making cellular decompositions. The projective-bundle and point-blowup comparisons are actual functorial equivalences compatible with external products. Their centres remain regular immersions after any allowed parameter base change: the point-product is cut out by the two polynomial coordinates. The comparison therefore retains all restriction coherences; an equality of ranks would not have sufficed.

For a closed binary union the characteristic-p Milnor-square theorem applies in every integer K-degree. Its rational fibre is zero. Finite affine descent globalizes this, and nilpotent reductions are harmless. Iterating the finite closed-cover diagram computes ordinary rational K-theory. Tensoring module spectra is exact and commutes with the resulting finite limits. These facts prove the natural equivalence TS.1 with its stated Noetherian product hypotheses.

## The rational complex and coefficient

Over the algebraic closure of a finite field, the rational field spectrum is HQ. Each rational stratum therefore lies in degree zero. Its reduction to the K0 vector space is natural, so no nontrivial higher mapping coherence is dropped. The codimension-zero complex is the cochain complex of the tetrahedral boundary, with cohomology Q in degrees zero and two. The Picard differential has source rank 34 and target rank 6. An exceptional curve above a nonvertex point of a chosen edge has degree one on that edge and zero on all others, proving surjectivity and kernel rank 28. The four component degree classes contribute rank four. Thus the homotopy groups are Q^33 in degree zero and Q in degree minus two, with the others zero.

Choosing one splitting over the constant field and then applying TS.1 gives a parameter-independent, noncanonical module decomposition. The dual-complex class has Adams weight zero. Its degree-zero product coefficient is K2(k), of weight two; on a proper curve parameter the corresponding coefficient is K2(P), with the actual point evaluation maps. None of this computes the image of K(Z times P), so it does not prove a fixed proper-family lift or an ordinary Chow relation.

## Exact primary inputs read

I freshly opened the Geisser–Hesselholt author PDF `https://math.mit.edu/~larsh/papers/025/bounded.pdf` and read Theorem A on printed p.29, Theorem C on p.30, and the nonconnective Bass convention. The all-integer-degree and characteristic-p hypotheses are exactly those used here. I also freshly opened Weibel's Chapter IV, `https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.IV.pdf`, and read Corollary 1.13 on author p.10 and Example 2.6 on author p.20. The finite-field calculation and filtered-colimit consequence are sufficient; no stronger field calculation is needed. Web records are `turn465283221view0`, `turn767193174view0`, and `turn762981269view0`–`turn762981269view1`.

The exact Khan projective-bundle/blowup inputs were reused from the preceding same-session full primary audits; I did not reopen those pages for this particular receipt. I requested a Chapter IV bibliography locator rather than treating a Chapter III URL as the source of the positive K-group calculation. The final file now has the corrected Chapter IV key.
