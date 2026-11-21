# F63: independent whole-proof and primary-source review

Reviewer: `/root/rectangular_and_theta`, GPT-6 Astra Pro; reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

## Frozen targets and verdict

**PASS. No mathematical correction is required.** I read the complete report and exact script, reconstructed the algebraic proofs independently, read the original primary-source contexts listed below, visually inspected the original matrix pages, and reran the exact symbolic certificate. This is a full review of the stated deductions and their source applicability. It is not an independent proof of every theorem in Blasiak's paper.

- Report: `agent_iterated_chebyshev_gate.md`, SHA256 `8ee2ba3448005df2ed9a4e39df8103e4d86d80ddad852227b30766cb7edbb224`.
- Script: `verify_iterated_chebyshev_gate.py`, SHA256 `d453a92697f09bc243be984f2355d595a344a2c0c5deb8a6972057cbb3774935`.
- Author's saved output: `verify_iterated_chebyshev_gate_output.txt`, SHA256 `1c625a69c22d431af3679dcbe2852e124e94797e2e4f60819db53ccaf7052f01`.
- Original primary PDF: `primary_sources/Blasiak_1010_0421v2.pdf`, SHA256 `1970dbbe63dcf8b4f32b00d6b637b7b9425f743f21f91d7d9565ad10a1a82387`.
- Original extracted text: `primary_sources/Blasiak_1010_0421v2.txt`, SHA256 `c7a0f02d417f8f7d4f89a9431b58772e4cb58b84ddd9911109395cfa74b054a3`.

Primary work: Jonah Blasiak, *Nonstandard braid relations and Chebyshev polynomials*, arXiv:1010.0421v2, 16 May 2014, https://arxiv.org/pdf/1010.0421.

## 1. Parameter, normalization and source checks

The report correctly fixes strand rank three and lets `k` count tensor factors. This is a different parameter from the strand-rank-four binary example F57. Write delta=v+v^-1, D=delta^2. The source uses u in place of v and f in place of D.

I read Proposition 2.3, Definition 2.5 and equations (8)--(11), printed pp. 4--7. The Hopf algebra here is the localized rank-one parabolic H2. Definition 2.5 constructs the iterated algebra inside H3 tensor-power k; it does not give the entire ordinary H3 a Hopf structure. Equation (11) gives the actual restriction map used by the report:

`P_i^(k_l+k_r) -> P_i^(k_l) tensor P_i^(k_r) + Q_i^(k_l) tensor Q_i^(k_r)`.

I read equation (13), equation (14), Proposition 3.1 and its matrix proof, printed pp. 8--10. I also visually inspected original p. 8. The source explicitly acts on the **left on column vectors**, and its two matrices are `[[delta^k,c],[0,0]]` and `[[0,0],[1,delta^k]]`. Their product has trace c. Absolute irreducibility holds precisely when c is neither 0 nor delta^(2k). These are exactly the conventions used in the report and certificate.

I read equation (24), Theorem 3.4 and its occurrence induction (25)--(26), Corollary 3.5, and Theorem 3.7, printed pp. 11--14. They supply, over Q(v), the two scalar simples and the k two-dimensional simples with

`c_(k,j)=delta^(2(k-j)) A_j^2`, where `A_j=delta^j T_j(1/delta)`.

Corollary 3.5 supplies split semisimplicity at the generic parameter, not at v=1. The report does not confuse those fibers. Theorem 3.7 supplies the stated quadratic and degree-(2k+1) braid relation; the script checks the complete k=4 presentation on the displayed actual restriction.

I read Definition 5.1, equations (44)--(48), Proposition 5.3, Proposition 5.5 and Proposition 5.8, printed pp. 20--24; I visually inspected original p. 22. Cellularity has no effective coefficient cone. Proposition 5.3 requires the sigma constants to be invertible, together with the earlier incomparable-label difference condition in the choice of poset. Equation (48) has the balanced sigma entries. For the fourth label this sigma is A4, which has mixed signs. Thus the report correctly distinguishes this known cellular basis from a hypothetical strictly effective Laurent basis. Inverting A4 in a cellular localization does not turn the trace into a positive Laurent polynomial, nor does the report claim the source's cellular theorem fails.

## 2. Independent reconstruction of the trace obstruction

From the scaled recurrence I get A1=1, A2=2-D, A3=4-3D, A4=D^2-8D+8. Substituting D=(v+v^-1)^2 gives

`A4=v^4-4v^2-2-4v^-2+v^-4`.

I expanded its square independently:

`A4^2=v^8-8v^6+12v^4+8v^2+38+8v^-2+12v^-4-8v^-6+v^-8`.

This is the actual trace of P1 P2 on the specified generic simple. A simultaneous conjugation cannot change it. A product of matrices over Q_{≥0}[v^{±1}] has an effective Laurent trace, so no simultaneous effective Laurent matrix model exists on that simple.

For every k>=4, the j=4 simple has trace delta^(2(k-4)) A4^2. The positive-real zero argument is sound: D(v) is strictly increasing for v>1 with image (4,infinity), and D=4+2sqrt(2) is a zero of A4. The resulting Laurent polynomial is nonzero, vanishes at a positive real v, and is positive at v=1. It cannot have all coefficients nonnegative or all nonpositive. This uses only a Laurent polynomial identity of a generic module; irreducibility at the zero is neither needed nor claimed.

For k<=3 the proposed b_(k,j) have effective Laurent coefficients, square to c_(k,j), and the diagonal conjugation of the source matrices gives entries delta^k and b_(k,j). This proves the stated restricted minimality for individual generic simples. It does not provide coherent intertwiners or positivity for the iterated coproduct, and that limit is explicit.

## 3. Actual tensor occurrence and regular splitting

I independently multiplied the two binary F21/F43 blocks with `a=D-2` and formed the actual delta^(2,2) restriction. The report's R1,R2 are exactly `P_i tensor P_i + Q_i tensor Q_i`. Put d=D^2 and A=2a^2-d=A4. For the four columns u+,u-,b1,b2 of B, direct multiplication gives

`R_i u+=d u+`, `R_i u-=0`,

`R1 b1=d b1`, `R1 b2=A b1`, `R2 b1=A b2`, `R2 b2=d b2`.

The determinant is

`det B=2 D a (A-d)^2=128 D(D-2)(D-1)^2`.

It is a unit in Q[v^{±1}]_(v-1), since D(1)=4. Consequently this is an actual regular-local decomposition into epsilon+, epsilon- and the displayed rank-two block, not merely a generic character computation. The generic block is irreducible because A^2 is neither zero nor d^2 as a rational function.

The occurrence claim is correctly grounded in the actual binary block already constructed in F21/F43 and the source's actual coproduct inclusion. Taking one such block from each binary tensor module supplies the four-factor tensor occurrence. For larger k, appending ordinary trivial factors scales the generators by delta; no unjustified claim about the parity of the all-standard Specht tensor power is made.

For the projector I independently checked

`E4=[d(R1+R2)-R1R2-R2R1]/(d^2-A^2)`

and `d^2-A^2=16(D-1)(D-2)^2`. It is zero on the scalar blocks and the identity on the rank-two block. Thus it is regular locally at v=1, idempotent, commuting, and has marked trace A^2. The explicit matrix after denominator cancellation agrees with the displayed formula. This is a projector in the image/commutant on this four-dimensional module. The report does not assert that it is a globally separating primitive central idempotent of the entire iterated algebra.

It follows that R1,R2,E4 cannot all have effective Laurent matrices in one basis. This does not by itself rule out an effective basis for the unmarked containing module.

## 4. Whole-module positive traces and arithmetic scope

For a nonempty word of length L with 2s cyclic changes, the rank-one matrix contraction gives the block trace `d^(L-2s) A^(2s)`. The scalar summands give d^L and zero, hence whole trace

`d^(L-2s) (d^(2s)+A^(2s))`.

I checked the positive decomposition with U=d+A=2(D-2)^2 and V=d-A=8(D-1):

`d^(2s)+A^(2s)=2^(1-2s) sum_(j even) binom(2s,j) U^(2s-j)V^j`.

Both U,V have effective Laurent coefficients; the expression is visibly rationally effective and is already integral, hence is integrally effective. The formula includes s=0. The displayed trace of R1R2 agrees with adding d^2 to A^2, including cancellation of the v^{±6} terms. Thus all the claimed unmarked word traces are positive even though the selected summand and its marked trace are not. This is a genuine boundary of the result, not a missing sign in the calculation.

The pure-point-complex consequence is explicitly tied to v=q^(n/2) or v=q^n. Every exponent in the offending polynomial is even, so under either specified assignment the forced weights have the same parity. Mixed coefficient signs violate the pure-complex Euler parity criterion. This does not exclude mixed Tate realizations, arbitrary operator-inserted traces, or unrelated variable normalizations.

## 5. Exact-check record and limits

I ran `python GCT_NSRH_work/verify_iterated_chebyshev_gate.py` on 2026-11-21 UTC. It exited 0 and printed PASS for:

- the original left-column normalization and actual k=4 tensor restriction;
- the scaled Chebyshev coefficients and full mixed Laurent trace;
- both R_i B block identities and the exact determinant;
- the projector, its regular denominator, and its marked trace;
- the whole product characteristic polynomial and positive whole trace;
- the k<=3 individual-simple effective models;
- the complete k=4 nonstandard braid relation.

The certificate corroborates, but does not replace, the written proofs and primary-source checks above. I found no numerical approximation in a proof step. No master file or shared master log was edited.

## 6. Complete final-fragment match

I subsequently read the entire generated `finding_F63.tex`, SHA256 `1af4f6d7e72bdba1eb87024e1a6357c5ca844ccc3a22f356625677ea9b9305a9`. **PASS: the complete fragment matches the reviewed report.** It retains the original left-column matrix convention, every source hypothesis and parameter distinction, the explicit local basis and determinant proof, the full projector formula and its exact scope, the all-word rank-one contraction and positive even-binomial identity, actual tensor occurrence for k=4 and trivial-factor extension for k>4, both stated arithmetic normalizations, the distinction from source cellularity, and the separate dictionary. It does not claim that effective unmarked traces produce an effective basis or that the four-dimensional projector separates all global algebra branches. No new mathematical assertion requiring correction was introduced.

Final formatting delta: the two raw Unicode section-sign occurrences were replaced by TeX `\S` commands in the source citation and dictionary. I checked those exact replacements; no mathematics or prose changed. The final fragment SHA256 is `af4fffb91778b1765a3262a90cc18c3517f34aea9e6ee4225bc824924ab8e259`. The complete match above remains PASS at this final hash.
