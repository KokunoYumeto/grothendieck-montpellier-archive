# F50: complete independent proof and primary-source review

Reviewer: /root/grothendieck_dictionary, GPT-6 Astra Pro; effort not exposed.
Date: 2026-11-21 UTC.
Target: agent_gaussian_sign_wrapper.md.
Final reviewed SHA256: 13f67e1c418422629606752238ca1352c8f74a604d86535150f984a3e95b9bc6.
Outcome: **PASS**. The full report, all new proofs, and the additions described below were read and independently reconstructed.

## 1. Review history and exact source scope

The first entire report read was 0786d41e295650793de2a103dc7c62e7a7a0a1b1256f7436f2031a0163d0f014. I requested the explicit Newton-identities justification of algebraicity and conjugate spectra. The next version added it and the characteristic-five bad-length example. Independently of the parent, I also requested the exact integer-target/common-embedding qualification in §8: sharp real thresholds must not be treated as an application of F03/F17 with arbitrary real a, and width zero separately at each embedding need not give one common weight. The final version incorporates this as G23a, and also states the operator-insertion limitation explicitly. All additions were read and checked.

The original published scan Deligne_SGA4half_original.pdf, SHA256 fb2939521f4c0ea0cdd55a90bec2e618e32fb433c78b194e705c6d989f4e42a6, was used directly. Printed pp196--197 were visually inspected in the saved original-page images. The full Proposition4.2, Proposition4.3, their proof and Remark4.4 were read. The scan's final absolute-value shorthand is erroneous; the report correctly uses only the preceding pairing and product identity. The proof uses curve vanishing and Euler characteristic/Swan conductor, not the sought weight estimate.

Original pp178--179, Remarks1.18(b)--(d), were read from the scan's extracted text. The rank-one local monodromy argument needs only the H_c^0 and H_c^2 vanishing consequences, not the adjacent Theorem1.17 weight theorem.

Milne's original author PDF v2.21 was reopened, reference turn718799677view1, and the local exact contexts of Theorem17.10 p116, Proposition18.4 pp121--122, Theorem22.1 p135, Remarks22.3(b),(d) p136, and Proposition22.5 pp136--137 were reread. Proper base change plus compactification gives the !-stalk formula. The same compactification and j_! procedure gives the needed compact-support projection formula from the displayed ordinary projection formula. The compact-support Kunneth extension is explicitly stated in Remark22.3. These are cited formalism inputs, not independently re-proved general theorems.

## 2. Gaussian line, signs, and perfect pairing

For the square map, the invariant summand of the pushforward is constant and its anti-invariant summand is the quadratic Kummer sheaf extended by zero at the origin. The nontrivial linear Artin--Schreier sheaf has zero compact cohomology: its Lang-cover realization is a nontrivial character summand of the cohomology of A1, on which the translation deck group acts trivially. Projection formula therefore reduces the quadratic Gaussian cohomology exactly to the nontrivial-Kummer case of Proposition4.2.

It is consequently a line in degree one, and the trace sum is minus the nth power of its Frobenius eigenvalue. The involution x to -x acts by -1 on this line. Square-root descent of a varying nonzero quadratic coefficient therefore gives the stated quadratic Kummer monodromy. The dual Gaussian line has the perfect pairing into E(-1) from Remark4.4. Because the quadratic character equals its inverse, the paired additive character is precisely psi inverse. Hence gamma_psi gamma_(psi inverse)=q, with no extra sign.

The completing-square Fourier formula is exact in odd characteristic and involves no estimate.

## 3. Determinant, good lengths, and actual middle cohomology

The tridiagonal determinant recurrence, consecutive coprimality at every nonzero root, and rank-drop-one conclusion are correct. For even k the leading coefficient is (-1)^(k/2)/2^k. The Chebyshev recurrence proves the squarefree sufficient condition p not dividing k+1: the distinct roots of unity pair under inversion, and no root of U_k is zero when k is even. Thus k=2pr gives an unbounded set of good even lengths for every odd characteristic. The report correctly does not claim that this condition is necessary.

On the complement of the determinant zeros, local diagonalization and square-root trivialization identify a single rank-one compact-cohomology sheaf in degree k. At a root, the leading (k-1)-block is invertible and the Schur complement is d_k/d_(k-1). The final free affine line contributes E(-1)[-2], so the fiber cohomology is only in degree k+1. Stalk base change gives precisely the two sheaves in G8; zero boundary stalks identify the first with extension by zero.

A simple zero of the Schur complement gives nontrivial quadratic local monodromy. The nearby rank-one system is geometrically nonconstant. On the connected nonproper base curve its H_c^0 vanishes; duality and nontrivial monodromy make its H_c^2 vanish. The only compact Leray terms are therefore (1,k) and (0,k+1), both of total degree k+1. No other cohomological degree can survive.

Integrating h first gives zero off P_k=0 and E(-1)[-2] on that closed locus. Closed-open localization and base change identify the resulting complex with the closed pushforward of that constant complex; projection formula then gives G9. The degree k+1 concentration becomes exactly degree k-1 on H_k. This remains valid at the singular vertex and does not use an unjustified dimension-to-sign inference.

## 4. Effective spectrum and all-embedding hypotheses

The smooth projective double cover of a squarefree even-degree polynomial has the indicated two-point infinity fiber, with anti-invariant quadratic line determined by its leading coefficient. The affine point count and the trace formula with H0=E and H2=E(-1) give G13 with the correct minus signs. At determinant roots the Schur-complement sum is Q chi(d_(k-1)) g_n^(k-1). Since k is even, the generic term uses positive gamma^(kn) and the rank-drop term uses negative gamma^((k-1)n). Their sum is exactly minus the trace of the effective space G10, of dimension2k-1.

The rank-k finite-etale object W_k properly includes nonrational determinant roots. On each Frobenius cycle its full-cycle scalar is plus or minus one; its characteristic polynomial is a product of polynomials T^d minus a sign. This verifies both its finite order and the embedding invariance of its spectrum. The eta line is likewise quadratic.

The added Newton argument is valid and avoids a hidden use of a Weil weight or integrality theorem. The integer power traces of H1(C_k), obtained from point counts, determine a rational characteristic polynomial. Its eigenvalues are algebraic and its multiset is embedding stable. Gamma is minus a finite cyclotomic sum. These facts verify the conjugate-spectrum conditions by replacing psi with its conjugate character.

At k=2 the union-of-axes computation gives Q(2g_n-1), exactly as in G14. At p=5,k=4, d4=(h²-1)² and d3(plus or minus1)=3. The generic sum has Q-2 terms of character one; the singular terms have character (-1)^n. This gives the stated sequence 5^(3n)-2*5^(2n)-2*(-5 gamma³)^n. Here gamma²=5 by the pairing and the square-scaling identity at -1. Its positive top root125 cannot be the negative of an effective spectrum. This confirms the necessary restriction to good lengths.

The cohomological equality of Frobenius characters does not imply a canonical direct-sum splitting or arithmetic semisimplicity, and neither is claimed.

## 5. The noncircular Gaussian size test

The unnormalized quadratic trace function has absolute value one. Its input sign is negative and every good even path length has a negative effective output, exactly satisfying F03 with a=0,d=1. Applying that theorem to psi and its inverse gives both upper bounds. The perfect product q then forces equality.

The curve H1 eigenvalues enter only as an effective finite spectrum and their sizes are not used. Thus this is a valid test of the sign theorem that does not assume a curve Riemann hypothesis. The report correctly treats the resulting Gaussian bound as classical, not as a new GCT weight theorem.

## 6. Normalization, exact Hom, and actions

The definition J(C)=L_psi(x²) tensor p*(C tensor G^vee)[1] has the required shift. Since compact cohomology of the rank-one factor is G[-1], its compact cohomology is naturally C in degree zero. Its pointwise trace has the extra minus sign from [1], and summing it cancels the Gaussian scalar exactly.

For an even k-fold external product, the shift is [k]. The already proved degree k-1 cohomology therefore becomes degree -1. Tensoring by C^tensor k and G^vee tensor k preserves an actual effective coefficient space. With the extra Tate twist supplying Q, the output is exactly G19, with zero error.

The degree-zero Hom assertion is correct in either the perverse heart or the constructible derived Weil category: equal shifts cancel, the common invertible lisse line cancels, and morphisms between constant geometric sheaves on connected A1 are linear maps. Weil descent imposes precisely Frobenius commutation. Exactness follows from exact constant pullback/tensoring and the lisse[1] perverse normalization. This gives the stated actual End/Hom realization of F46, including its arithmetic Jordan block and both actions. No claim about higher Ext is made.

J is not monoidal; its unit image and tensor-product formula explicitly show the mismatch. It is a module functor for constant coefficient spaces, which is exactly enough to transport the specified graded-kernel matrix construction and its ordered word compositions. Equalities in graded K0 are not upgraded to unconstructed coherent relation isomorphisms.

The added operator-insertion warning is essential and correct. Retaining T as a morphism does not make Tr(TF^n) an effective object trace. The all-word sign claim uses the actual positive graded coefficient objects, and is explicitly separate from such arbitrary insertions.

## 7. Sharp pointwise thresholds and the common integer weight

The pointwise absolute value is exactly q^(-n/2) times the absolute trace of C. Sufficiency of G21 follows by summing eigenvalue moduli with B=dim C. Necessity follows from F02 after grouping equal eigenvalues, whose multiplicities are positive. Jordan off-diagonal terms make no contribution to traces of powers.

The reciprocal coefficient C^vee(-1) has maximum radius q/min|alpha|. Its sharp real exponent is 1-b_min, whereas the first sharp real exponent is b_max-1. Their discrepancy is exactly b_max-b_min.

The corrected G23a is the right formal F03/F17 application: choose one integer w, set a=w-1, and require b_max,sigma<=w<=b_min,sigma for every embedding. This is equivalent to the desired common all-conjugate modulus. Zero width at separate embeddings by itself is not enough. The proof correctly retains this distinction.

When C is already pure of integer weight w, the unshifted lisse factor has weight w-1 and [1] makes the perverse complex pure of weight w in BBD's convention. This does not force semisimplicity of arithmetic Frobenius.

## 8. Actual word spaces and the graph-error lower bound

For F45's total effective word space, both endpoint coefficients are nonzero. Thus b_max=2L and b_min=-2L. The pointwise exponents 2L-1 and 2L+1 and the required dual exponent1-2L give the exact gap4L. For each genuine homogeneous piece the opposite two exponents match and recover only its already known degreewise weight. Odd edge degrees can use a genuine rank-one Weil line with eigenvalue sqrt(q); no integral Tate-motive claim is made for it.

For point-supported positive input, Q times the kth path sum is an effective nonempty Tate power sum. It cannot equal a negative effective power sum, by the finite-spectrum lemma. The report correctly does not turn this example into a prohibition on every F04 error budget.

For the normalized constant affine padding, grouping odd/even path variables gives a nondegenerate bilinear form with triangular invertible block matrix. Its zero count is exactly Q^(kd-1)+Q^(kd/2)-Q^(kd/2-1). Multiplying the constant coefficient trace gives G27. The top root q^(kL) retains positive coefficient, doubled only in the kd=2 case. Adding any effective output spectrum cannot cancel it. F02 forces the error rate to be at least q^(kL), and comparison with the stipulated exponent gives eta_k>=kd/2. The argument survives full extension progressions because the top positive Tate root stays visible.

## 9. Conclusion and remaining review scope

All new assertions in the final report pass. The normalized construction supplies actual curve sheaves, exact identity traces, actual Hom comparisons, and proved opposite-sign cohomology. It does not supply an independent weaker pointwise bound for an unknown coefficient space: the explicit bound is equivalent to that coefficient's upper radius, and the reciprocal bound gives precisely the lower radius. The remaining GCT basis, arbitrary-insertion and coherent-operation gates are preserved.

This is a complete independent mathematical report review with exact local primary-source checks. I did not run the author's finite-field script, and do not claim its execution as my own check. The author's finite computations are ancillary to the complete proofs. A generated F50 LaTeX fragment still needs a separate direct whole-text match.

## 10. Complete generated fragment and final corrected hashes

The entire 599-line generated fragment was read from the saved snapshot agent_F50_fragment_snapshot.tex at SHA256 1baea8ce4b1f12edaf7f7fc59517ecb78ef9cc0e5b80175353c58626b7b49faf. Every proof and qualification matches the reviewed report, including the actual middle-degree argument, bad-length example, Newton algebraicity, fixed integer/common-embedding target, Hom and module-functor scope, operator-insertion distinction, word dual gap and graph-error lower bound. The separate Grothendieck paragraph correctly distinguishes the proved geometric sign comparison from the remaining independent pointwise bound.

Two small precisions were requested and corrected. First, a line with eigenvalue q^(1/2) has integer weight one; the fragment now correctly calls odd-degree lines ones of odd integer weight, while retaining the absence of an integral Tate-motive assertion. Second, the W_k embedding-stability argument now explicitly uses its signed-permutation cycle polynomials T^d-epsilon with epsilon equal to plus or minus one. This gives a rational characteristic polynomial; finite order alone would not have implied embedding stability.

The exact textual diff from the fully read snapshot to the corrected fragment was inspected and contains only these two changes. Final fragment SHA256 b2107d7d72737a7dd0d6ed7494e4c72b9a70d39645e448b03d264aae751c483d: **PASS**. The matching signed-permutation clarification in the report was also read; final report SHA256 cf6ca3f1ed8f48f8bc8a28b234855a488330cc849e40a9dcc974737ff5a5ebde: **PASS**. No source proof, arithmetic convention or action scope was weakened by the corrections.
