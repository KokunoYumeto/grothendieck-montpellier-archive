# Natural symplectic and orthogonal scalar covers

Fresh author-primary source audit by `/root/part_d`, 2026-11-20 10:04--10:10 UTC.

Primary source: D. E. Taylor, *The Geometry of the Classical Groups* (1992), author-maintained PDF with April 2021 corrections: <https://mail.maths.usyd.edu.au/u/don/papers/gcg.pdf>. The preserved PDF/text is owned by B at `parts/B/sources/post09_reconstruction/TaylorClassical1992.pdf` and `.txt`. We reuse the unique key `Taylor1992ClassicalB` in B's `references_classical_B.bib`; no duplicate entry is introduced.

We read the following complete relevant passages in the preserved primary text, and independently opened the author PDF (web ref `turn548644102view0`):

- pp.69--70: the natural symplectic matrices, scalar kernel {+I,-I}, and full counting of ordered symplectic bases giving the order formula.
- Theorems8.7--8.8, pp.72--74: the perfectness proof and simplicity conclusion, including exactly Sp(2,2), Sp(2,3), Sp(4,2) as exceptions.
- pp.136--137: orthogonal definitions, Omega=O', and the scalar-square-one calculation.
- Theorem11.9, pp.143--144: the full odd-dimensional even-characteristic identification with the symplectic group.
- Theorems11.45--11.48, pp.160--162: the actual stated nondegenerate-polar-form scope and simplicity proof; the four-dimensional plus type and Omega(3,3) are excluded. We do not apply this theorem to odd-dimensional polar-degenerate forms in characteristic two.
- Theorem11.51 and proof, pp.164--165, plus the entire order discussion pp.165--166: the spinor index, scalar condition, and exact projective order formulas.
- For B's unitary corollary, p.118 and complete Theorem10.20 proof pp.127--128 were separately read: the natural scalar order is gcd(r,q+1), with exactly the listed three nonsimple exceptions.

Cameron's author course PDFs were also opened for cross-checking definitions/formulas: chapter4 <https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/ch4.pdf>, chapter6 <https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/ch6.pdf>. Their PDF text extraction has symbol errors, so Taylor's clean preserved primary text controls the statement. No page-image visual inspection is claimed in this pass.

The lower bound |S| >= q^(r^2/8) in the new corollary is proved symbolically from these exact formulas. It is not an empirical finite-group computation. No new counterexample or numerical certificate is introduced.

The new result is `D:symplectic-orthogonal-simple-product` in `D_symplectic_orthogonal_scalar_lifts.tex`, initially Candidate pending independent actual-file audit. Its finite-group inputs and complete internal deduction have been checked by D. It depends on B's generic scalar-cover proposition `D:bounded-scalar-projective-growth`.

## Independent checks and promotion

Root, B and C each read the complete actual corollary and passed it. B/C reused the fresh Taylor source audit without claiming their own complete orthogonal-source reopening. Root independently reread all listed Sp/Omega primary statements and proofs, including the full spinor-index and order derivations, and authorized promotion at approximately10:14UTC. The heading is now Proved. This is recognition under the generic bounded-scalar criterion and is not counted as a separate main-gate movement after review08.
