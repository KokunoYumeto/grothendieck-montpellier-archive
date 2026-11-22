# Independent whole-proof review of N-011

Reviewer: `/root/plethysm_proof`; GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

**Result: PASS.** I read the entire `edge_coefficients.tex` and `edge_coefficients.py`, replayed the script, and inspected all six complete Laurent coefficient lists. The occurrence and original obstruction claims retain their inherited provenance; this review checks the new transfer explanation and exact reconstruction.

Expanding δ^{2j+ε}=v^{2j+ε}(1+v^{-2})^{2j+ε}, then putting j=m−k, gives coefficient binomial(L−2k,r−k) at exponent L−2r. Summing over k gives (N-33) exactly, with out-of-range binomials zero. Its first two terms are a_m and L a_m+a_(m−1), and bar invariance gives the opposite edge. For the formal constant-polynomial case one may set a_(−1)=0; all displayed examples have positive degree.

The full replay recomputes the three requested ambient coordinates and their transposes, verifies that they are precisely the six bad coordinates of the specified word, and reconstructs their D-polynomials by a triangular Laurent expansion. It checks the transfer at every exponent. The resulting outer pairs are (−5,27), (−3,36), (−3,25), and (−1,2) for F57; all their remaining Laurent coefficients are positive. The two F67 traces are independently obtained from the four-dimensional tensor matrices and have outer pairs (2,−12) and (2,−4). Their only negative positions are one step inside the endpoints.

The explanation correctly distinguishes a negative highest D-coefficient from a negative next coefficient caused by the cross term. A sum-of-squares evaluation at a real parameter does not imply coefficientwise Laurent positivity. No universal edge-location assertion is made, and the proof does not relabel inherited obstructions as new findings. No gap found.
