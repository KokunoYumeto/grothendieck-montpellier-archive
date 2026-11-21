# A064 — independent review of the two-column unit family

Reviewed by GPT-6 Astra Pro, effort setting not exposed, run `/root/archive_audit`, on 2026-11-21 UTC. The complete report `work/rectangular/two_column_tail_unit_family.md`, UT.1–UT.19, was read and its proofs checked. **PASS.** This event is a mathematical proof review; it does not claim a new replay of the author's numerical sweeps.

## 1. Exterior kernel and the unique invariant

The map UT.3 is the literal raising operator on the two summands in the exterior algebra of \(W\otimes\mathbf Q^2\). With all first-copy wedge factors placed before second-copy factors, moving the \(l\)-th second-copy vector to the first copy gives exactly the sign \((-1)^{l-1}\) in the report. In skew Cauchy, the source weight \((j,j)\) occurs in the \(\mathrm{GL}_2\)-factor of shape \((2j-k,k)\), with raising scalar \(j-k\). It vanishes exactly at \(k=j\). Thus the kernel is the actual embedded \(S_{(2^j)}W\), including the endpoint \(j=\dim W\), where the target exterior power vanishes.

For \(W=\mathfrak h_a\), the hook identification is explicit. The ordered-singleton tabloid map to \(e_{i_1}\wedge\cdots\wedge e_{i_q}\) sends the column antisymmetrizer to

\[
q!\,(e_{i_1}-e_{i_0})\wedge\cdots\wedge(e_{i_q}-e_{i_0}).
\]

Fixing \(i_0=a\) gives a spanning set of \(\Lambda^q\mathfrak h_a\). Its dimension is \(\binom{a-1}{q}\), so this is the stated hook Specht isomorphism, with its scalar and all ranks checked. The hooks in \(\Lambda^{j+1}\mathfrak h_a\) and \(\Lambda^{j-1}\mathfrak h_a\) differ; their tensor product has no invariant. The determinant inner products identify each exterior power with its dual. Consequently the source of UT.3 has a one-dimensional invariant line, and its invariant line lies in the kernel. This proves the claimed one-dimensional invariant space in \(S_{(2^j)}\mathfrak h_a\).

The inverse Gram tensor \(\Omega_j\) is nonzero and realizes this line. The tensor \(J=(P\otimes P)\sum_i e_i\otimes e_i\), with \(P=1-a^{-1}\mathbf1\mathbf1^t\), is the ordinary coevaluation tensor of \(\mathfrak h_a\). Applying the two exterior maps to \(J^{\otimes j}\) produces \(j!\Omega_j\): the ordered choices of a fixed increasing index set contribute precisely \(j!\). This verifies the matching, Gram, and invariant constructions as actual maps, not only dimension equalities.

## 2. The balanced flag morphism

The displayed minors \(v_{j+1,I}\) have row weight one and right weight \((a-j,1^j)\). On \(u\ne0\), they are the components of

\[
u\,\mathbf1\wedge\bar w_2\wedge\cdots\wedge\bar w_{j+1}.
\]

The map \(\Lambda^j\mathfrak h_a\to\Lambda^{j+1}\mathbf Q^a\), \(z\mapsto\mathbf1\wedge z\), is injective; on its image its inverse is contraction by \(\mathbf1/a\). Hence the smaller flag coordinates used by the report have the claimed ordinary permutation action. The smaller flag relations follow by evaluating on the centered column matrix.

The map on \(S_{(2^j)}\mathfrak h_a\) is multiplication by \(u^{n-2}\) after substitution of these minors. It has the stated balanced row weight and highest weight \((an-2j,2^j)\). Its injectivity has a concrete dense inverse: prescribe nonzero \(u_0\), select the first coordinates with product \(u_0\), and choose subsequent columns by dividing the first centered column by \(u_0\). This realizes arbitrary smaller flag matrices on the open chart.

Surjectivity follows because the shape has exactly two columns of height greater than one. Replacing those two ordinary minors by their balanced expressions leaves exactly \(u^{n-2}\); all remaining first-column factors cancel by row balance. The exponent is nonnegative for every \(n\ge2\), including \(n=2\). This proves the exact balanced-module isomorphism and its \(S_a\)-equivariance, with no unaccounted determinant sign. It transfers the unique Gram invariant to a nonzero vector and proves UT.1/UT.17 for every stated \(a,n,j\).

## 3. Canonical-image and rectangular consequences

The stated canonical rank-one ranges follow from the already audited second-row-two specialization of R034. Both the full band restriction and its finite-base hypotheses are satisfied.

For UT.18–UT.19 I independently opened the primary Ikenmeyer–Panova PDF, *Rectangular Kronecker coefficients and plethysms in geometric complexity theory*, arXiv:1512.03798v2, and read Theorem 2.1 on printed p.5, the definitions and complete Proposition 2.5–2.6 proofs on p.6, and Lemma 2.7 plus the complete Proposition 2.8 proof on p.7:

<https://arxiv.org/pdf/1512.03798>.

The source's padding map preserves the evaluation pairing and shifts only the first highest-weight part. Its full-rank evaluation matrix proves injection of highest-weight multiplicity spaces. The uniform determinant bound is \(M=n\binom{n+n^2-1}{n}\); the resulting inclusion of the padded-form variety in the determinant orbit closure gives the stated coordinate restriction. The Peter–Weyl comparison bounds the latter multiplicity by the rectangular Kronecker coefficient. Finally Theorem 2.1 makes this coefficient constant for both rectangle heights \(M,n\ge2j\), while keeping the width \(a\) fixed. The source imposes no exclusion at \(a=2\); there is no need to require \(a\ge2j\). Thus the finite chain proves the claimed rectangular lower bound on the exact stated range.

The complete R014 finite-chain explanation was also reread during this check. The use here is its specialization to \(\rho=(2^j)\), with unchanged maps. All averaging, exterior, Gram, and flag maps are rational, so the report's characteristic-zero scalar-extension statement follows.
