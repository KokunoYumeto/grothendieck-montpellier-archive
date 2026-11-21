# Mathematical transcription audit

Run JAC1964-20261121; agent /root/programme_audit. This is a mathematical audit of the supplied TeX. Original manuscript images were absent. A forced type or degree correction below is not a claim about which character Grothendieck actually wrote. Deleted text and uncertainty markers should remain visible in a diplomatic edition.

## Cote 44

- Scan1 is the modern IMAG cover. Scans3,5,7 contain other deleted algebra/root-system or letter material; they are not extra statements in the seven-theorem programme. The operative programme is scans2,4,6 and the Serre letter is scans8–9.
- Scan2 Th.3 leaves n−i versus n+1−i uncertain. The complementary index n+1−i is mathematically forced by the incidence pairing and is stated unambiguously in scan8. Report it as a mathematical disambiguation.
- Scan2 Th.4 is unqualified, but scan8 explicitly adds the marginal requirement to account for primitive decomposition. Scan9 alone is false on arbitrary parameter families, as the E^3 calculation shows. Do not remove that margin.
- Scan4 Th.5 assumes algebraic equivalence to zero on Y. Replacing this by homological equivalence is a substantive change, not notation. The height normalization and local admissibility data are not specified there.
- The sign (-1)^m in scan4 is attached to the critical case i=j=m, n=2m. The adjacent margin says the noncritical cases vanish by Lefschetz. Do not interpret m as an independently defined integer in every i+j=n case.
- The word `intègres` in the pencil hypothesis is insufficient to remove higher-codimension vertical corrections. The quadric counterexample does not justify changing it to another word without images.
- Scan4 Th.6 contains a deleted finite-kernel clause. The rational proof under B(X) does establish that clause, but an edition should continue to mark it as deleted.
- Scan6 Th.7 does not define tau. The customary saturation of algebraic equivalence is refuted in characteristic zero in JAC-P05, but proved for all abelian varieties over Fbar_p in JAC-P15 under the accepted Tate input plus Kahn. It must not silently become homological equivalence.
- Scan8 changes `anti` to symmetric. A divisor correspondence on the parameter abelian variety is symmetric even though the corresponding odd Poincaré form is alternating. Under phi_L(x)=t_x^*L tensor L^{-1}, the elliptic normalized diagonal induces minus the positive polarization; this accounts for the difference between the incidence sign (-1)^m and the primitive cup-product sign (-1)^{m−1}.

## Cote 16, no.7

The operative pages here are scans34,36,38,40,49,50. Scans35,37,39 are unrelated printed mathematical material on the reverse sides. Scan33 is needed to fix the convention: Lambda is the normalized lowering operator along a Lefschetz string, not the sl_2 lowering operator with string coefficients. The archive uses labels such as C(X) for algebraicity of this operator; modern standard-conjecture letters should not be substituted without declaring the translation.

| Location | Transcribed expression | Mathematical diagnosis |
|---|---|---|
| Scan34, first square | Bottom-right H^{2(n−1)±i}(Y), lower arrow L_Y^{n−i} | The displayed exponent of L forces target H^{2n−i}(Y). Its Gysin image then lies in H^{2n−i+2}(X), as in the upper-right corner. The right arrow's subscript must have the same source degree. |
| Scan34, last kernel display | Sum indexed j≥n of P^i(X) | Bound and summand use different indices. The intended endpoint sum is over the same index, P^j(X), n≤j≤2n. This agrees with ker(j*)=ker L_X. |
| Scan36, first displayed summand after alpha | Sum L_X^j P^j(X), indexed i,j | The primitive index must be i, as in alpha and the original bigrading. |
| Scan36, last line of projector identities | p_j^X j_*=j_* p_{j−2}^Y, with condition n+1≤i≤2n | The condition must use j, the index in the formula. |
| Scan38, first two sums | L_X^jP^j(X) | The primitive index must again be i. |
| Scan38, kernel of Lambda_Y | Sum 0≤i≤n+1 of P^i(Y) | For dim(Y)=n−1 the bottom endpoints are 0≤i≤n−1. The preceding sum on X also has that upper bound. |
| Scan38, second expression for Lambda_Y j* | (id_Y−sum p_X^j) j* Lambda_X | Projectors acting on Y must be p_Y^j; the X label is type-inconsistent. |
| Scan38, last line | p_X^i Lambda_X j*=Lambda_X j* p_Y^i | These compositions are not typed: j* goes from X to Y, whereas Lambda_X follows it. The neighboring first identity uses j_*; the compatible expression has j_* in these two places. No palaeographic correction is claimed. |
| Scan40, first underbrace | L_X Lambda_X=id_X−sum_{0≤i≤2n}p_i^X | The bound must be 0≤i≤n for this intermediate equality, as scan33 B(4) states. After multiplying by the top-endpoint complement, the final all-endpoint expression q is correct. |
| Scan40, formula with Lambda_Y^m | Second sum has index j but summand p_X^i | The summand must carry j. |
| Scan50, A' and A'' | 2i≤n−1 applied to H^i, and H^{j+2} followed by H^i(Y) | Cohomological degree and codimension indices have become inconsistent. State a corrected result with a single cohomological degree r: restriction is injective/isomorphic below the middle and Gysin is surjective/isomorphic above it. Do not publish a guessed literal repaired line. |

The boxed scan40 identity Lambda_Y=j* Lambda_X^2 j_* passes a Lefschetz-string check with the normalized convention. The identity j* Lambda_X j_*=id_Y−p_E also passes. These are the identities used in JAC-P02; the proof there reconstructs them on the relevant degree instead of relying on every transcribed auxiliary formula.

## Published source transcription cautions

The modern SGA transcription is useful for searching, but critical expressions were checked against original scans: XVIII5.3.2–5.3.5, XVIII6.2, XX4.1 and4.3, and SGA7 I IX10.4. For example, the online discussion around XX4.2 contains a dimension/degree transcription discrepancy; no explicit high-degree numerical threshold is used in JAC-P04. Only the verified existence of a sufficiently high degree is used.
