# Independent review: C.1q and C.2k

Reviewer: `/root/frobenius`. Review date: 2026-11-19. Both complete typed fragments passed independent proof and source checks. This review does not claim any closure beyond their stated scopes.

## C.1q: blow-up positivity

Reviewed `agents/cycles/blowup_positivity.tex` in full.

With the projective bundle of lines in the normal bundle and ξ=c1(O(1)), the exceptional normal line is O(-1). Consequently j*E=−ξ and the excess bundle is p*N/O(-1). Its top Chern class is the stated positive-sign polynomial in ξ. The resulting top exceptional relation is therefore

f_c(z)=π*i*z−Σ_{k=1}^{c−1}f_{c−k}(c_k(N)z).

The ambient term vanishes under the actual G^{m+1}(M)=0 hypothesis. The coefficient equations for multiplication by L/b give the stated downward recurrence. The final coefficient is the negative of q_N(−u)z, which has exactly the asserted zero locus; no sign correction is needed in the kernel statement. Extraction of the last exceptional coefficient and reconstruction are inverse, including negative controlling degrees.

The controlling degree m−c+1=(dim Z−c+2)/2 is at or below the middle of the center. Thus merely importing an above-middle Griffiths class cannot yield the claimed primitive middle radical. The proof does not overstate this limitation as a vanishing theorem for arbitrary centers.

For a smooth transverse pencil base cut out by two sections of H, the blow-up is the closed graph in M×P1. The line bundle 2π*H−E is the restriction of H⊠O(1), hence ample. Its exceptional polynomial vanishes, and weak Lefschetz supplies the stated vanishing of H^{2m−3}(Z) if the ambient cohomology is Tate.

For V×P^r inside P4×P^{r+c−1}, the normal bundle and dimensions are correct. G^2(V) is the only possible rational Griffiths group, and multiplication by H annihilates it because G^3(V)=0. The coefficient calculation reduces exactly to (1−β/b)^{c−1}. A line in the second factor through the linear center and not contained in it has strict-transform degree β−b, so ampleness imposes strict positivity. The exponent e+c−1 remains within the projective-bundle range whenever e≥0. Hence the injectivity argument is valid; no kernel on the nonample boundary is counted as a counterexample.

Primary source reopened: Jiang, Q. (2023), *On the Chow theory of projectivizations*, Journal of the Institute of Mathematics of Jussieu, 22(3), 1465–1508, https://doi.org/10.1017/S1474748021000451. Full publisher HTML and the exact Equation (2.2), Theorem 2.8(3), and normal-bundle convention immediately preceding them were read. Opened references: turn245158868view1; turn447706531view2–3; turn936821012view0.

## C.2k: classical low-degree numerical–homological equality

Reviewed `agents/cycles/low_degree_standard_D.tex` in full.

The numerical-triviality argument in codimension two uses only an algebraic divisor d obtained by hard Lefschetz and the rational Lefschetz (1,1) theorem. The displayed equation for d has consistent cohomological degrees. Pairing against divisors kills d by the divisor Hodge index form. The resulting degree-four class is primitive, and its self-pairing vanishes by numerical triviality; primitive Hodge–Riemann positivity then kills it. No codimension-two Hodge conjecture is used.

The same construction gives the algebraic primitive decomposition of A_H^2. Its two summands are orthogonal and have nondegenerate forms, so the restriction Q2 is nondegenerate. Finite-dimensional rational linear algebra therefore gives the exact displayed decomposition of A_H^{n−2}. The residual summand is exactly the homological classes of numerically trivial codimension-(n−2) cycles. Thus its vanishing is equivalent both to the stated algebraic-class Lefschetz surjectivity and to D in that codimension. The first uncovered pair is correctly (n,r)=(5,3). The final warning about the universal quantifier over source varieties in C.1n is necessary and correct.

Primary source reopened: Kleiman, S. L. (1968), *Algebraic cycles and the Weil conjectures*, in *Dix exposés sur la cohomologie des schémas*, pp. 359–386. Working complete PDF: https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf . Remarks 3.4 and 3.10, printed pp. 379–380, were read with Propositions 3.6–3.9 in the surrounding text. Opened references: turn245158868view0; turn447706531view0–1; turn936821012view1.

No changes to the owner fragments were required or made.
