# Paper II: verification and source scope

## Result

The main theorem assumes only an S5 Galois extension with complex conjugation of type (12)(34). The local condition at five is removed by the published Pilloni–Stroh modularity input, through the complete Calegari dependency audit in Section 3.1. This is a literature-backed scope upgrade, not a new modularity theorem.

The main analytic hypothesis is absence of common real zeros off one half of the two entire quadratic Hecke functions B=zeta_H/zeta_F and C=zeta_J'/zeta_J. Section 3.3 proves that every comparison pole in the open strip has order at most the zero order of each function. Arbitrary common central multiplicity is allowed. The conclusion is equality of standard local L-factors at every place, including gamma factors, and entire automorphy of every nontrivial irreducible S5 factor. Separate B or C nonvanishing is a corollary.

Section 9 proves unconditional examples of quintic discriminants 8249, 60061, 30301, and 48976 by unchanged finite explicit-formula certificates. Each B has no real zero anywhere in (0,1), including at the center. All four also satisfy the original Frobenius-at-five condition.

The canonical-removal theorem and Appendix C prove method obstructions at arbitrary multiplicity and a sufficient rigidity theorem under a finite-progression description of the entire divisor. Appendix D proves the exact tensor identities and two conditional transfer equivalences. Neither appendix supplies additional absence of common zeros or a smaller numerical off-central interval.

## Proof checks

- **Real pole and sign.** The exceptional Euler quotient has nonnegative coefficients, and its negative logarithmic derivative has coefficients 4 log(p) at odd prime powers. A pole contributes a positive residue to the negative logarithmic derivative. The nonvanishing condition places any positive abscissa pole at 1/2.
- **Topology.** Positive definiteness is on the discrete additive group of real numbers. Ordinary continuity of the divisor coefficient function is neither asserted nor needed. The ordinary local finiteness condition is retained separately for the discrete coset-ring reduction.
- **Cosets.** Cohen's theorem gives abstract coset-ring level sets. Kolountzakis's discrete-coset theorem is the substantive step that removes dense subgroups before classifying discrete subgroups of the real line as cyclic.
- **Divisor reconstruction.** All zeros and poles lie on the central line under the hypothesis. The progression product has exactly this divisor, so the quotient is entire, zero-free, and of order at most one. Hadamard factorization therefore leaves only an exponential of a linear function.
- **Gamma factors.** The gamma-shift identity eliminates both the rational isolated-divisor term and any integer gamma mismatch. Real-place base change independently gives the same gamma equality.
- **Prime support.** A frequency lattice can meet prime-power logarithms for at most one distinct prime. Bounded local inverse roots give a fixed coefficient bound in that lattice, whereas a progression divisor gives an exponential factor times a finite phase sum. Cesaro mean squares rule out nonzero exponential decay of that phase sum.
- **Finite exceptions.** Calegari's published Lemma 4.10 supplies the final standard-factor comparison at every place. Full ramified Weil–Deligne equality is not inferred from standard factors alone.
- **Booker.** Theorems 1.6 and 1.7 were checked with the correct normalization. Booker's positivity is finiteness of the negative divisor support. The two summability criteria involve different coefficient sequences. Nonnegative Euler coefficients do not establish positivity.
- **Off-central attack.** Without the real-zero hypothesis, any infinite exceptional set must have abscissa in (1/2,1). Boundary positive definiteness remains valid, but an unknown interior divisor prevents Hadamard reconstruction. The central prime measure is not tempered, and the Abel measures lose mass at infinity. No unconditional removal of the remaining real-zero condition is claimed.

## Sources actually inspected

| Source | Material inspected | Use and limit |
|---|---|---|
| Calegari (2013), author-hosted publisher PDF | Theorems 1.1–1.2 and 4.7; Lemmas 4.8–4.10; Section 5 and Theorem 5.3 | Automorphic construction, exact Euler quotient, final local standard factors, published numerical example |
| Green and Sanders (2008), primary Annals PDF | Theorem 1.1 and surrounding classical statement | Primary modern statement of Cohen's idempotent theorem |
| Cohen (1960), primary journal record | Bibliographic metadata | Original attribution; theorem statement checked in Green and Sanders, original proof not re-audited |
| Kolountzakis (2000), arXiv math/9904065 | Theorem 3 and its proof in Section 3.2 | Ordinary discrete elements of the abstract coset ring reduce to discrete cosets |
| Booker (2015), arXiv 1308.3067 and supplied source | Definition 1.3, Examples 1.4, Theorems 1.6–1.7; proof of 1.6 and degree-zero portion of 1.7 | Correct positivity and coefficient normalization; full low-degree classification imported |
| Ramakrishnan (2002), author manuscript | Proposition 4.1 and its comparison argument | Scope of local L- and epsilon-factor conclusion |
| Booker (2006), published primary PDF | Section 3, equation (3–1), printed p.391 | Explicit-formula normalization; the following RH-dependent optimization is not imported |
| Miller (2002), primary author manuscript | Lemma 3.1 and proof, manuscript pp.8–9 | Division by cosh gives nonnegative real part on the full strip; direct proof supplied for the triangular test |
| GNU MPFR 4.2.2 manual | Sections 4.4 and 5.7 | Directed rounding and correctly rounded transcendental operations and constants |
| Dwyer (2014), publisher record | Abstract and bibliographic metadata | Correct author and computational approach; full PDF inaccessible through the available link, so individual certificates and exact local assumptions are not asserted |
| Baker, Harman, and Pintz (2001), primary PDF | Printed p.562, final displayed lower bound | The stated short-interval prime bound only; the larger-interval deduction and prime selection are proved in the manuscript |
| Körner (2008), original course notes | Theorems 10.6, 12.3, 13.3 and Lemma 14.2 | Fourier uniqueness, LCA Bochner theorem and duality; theorem statements inspected, not a full audit of every course proof |
| Dikranjan (2018), author-hosted original notes | Section 12.5, Lemma 12.5.2 and adjacent duality statements | Double-annihilator theorem, including the density argument used in the manuscript |
| NIST DLMF, official §§25.4 and 25.15 | Zeta and primitive Dirichlet functional equations and Euler factors | Classical input for the scaled reflected quotient; its Gauss sum and coefficient failures are computed directly |

## Exact computation

`field_checks.gp` ran with PARI/GP 2.19.1. The output `field_checks.txt` records exact discriminants, real-root counts by Sturm's method, finite-field factorizations, and Galois-group labels. Independent finite-field witnesses prove the S5 labels through primitivity and a transposition.

The three candidate discriminants are 30301, 60061, and 48976. All three quintics have one real root, and their modulo-five factorization degrees are 1,2,2. The algebraic calculations alone do not certify a real-zero hypothesis. The separate finite certificates now establish the analytic hypothesis for discriminants 8249 and 60061. The positive autocorrelation certificate additionally settles 30301, and the wild-prime analysis with a triangular test settles 48976. All four explicit fields have finite real-zero certificates.

The published discriminant-1609 example is irreducible modulo five. Its Frobenius at five is a 5-cycle, and Calegari's separate two-adic modularity construction is needed. The published analytic certificate is cited, not reproduced.

## Finite real-zero certificates

- **BD-S12 (8249).** Exact discriminant 73·113; signature (1,2); S5 from irreducibility at 2 and a (2,3) factorization at 13; Frobenius 5 has type (1,2,2). Tame transposition inertia gives conductor 8249³, gamma shifts 0,0,0,0,1,1, and ramified denominators 1−T³ at 73 and (1−T)²(1+T) at 113.
- **BD-S13 (analytic criterion).** The transform of `(1−|x|/8)_+/cosh(x/2)` has nonnegative real part throughout the full strip by the boundary identity and the harmonic minimum principle. Its uniform quadratic decay makes the zero sum absolutely convergent. The sign +1 Hecke functional equation forces even central order. Any real zero therefore contributes at least twice the transform at zero. The explicit formula and the gamma tail were independently rederived by the root worker.
- **MPFR certificate (8249).** The finite sum has 465 prime powers. Exact polynomial arithmetic and Sturm chains are implemented with integers and fractions; every transcendental endpoint uses 160-bit MPFR directed rounding. 1024 cells and the explicit tail give S₈<811/100<224/25<2H₈(0). All traces agree with a separate PARI factorization calculation.
- **Separate Arb check (8249).** A newly written Sympy/Arb program factors every relevant finite-field polynomial and counts permutation traces directly on points and pairs. At 192 bits and 2048 cells it proves S₈<17/2 and 2H₈(0)>89/10. This is separate same-model implementation, not a statement-only reproof or human review.
- **BD-S14 (60061).** Exact discriminant 17·3533, signature (1,2), irreducibility at 3 and (2,3) factorization at 19, and the literal five-adic condition pass. The ramified invariant degrees are (1,2) and (1,1,1). Both the MPFR and independent Arb calculations prove S₈<89/10<224/25<2H₈(0), with 465 prime powers and 2048 cells. The conductor includes 3533 even though that prime is beyond the finite sum cutoff.
- **Scope.** Neither result asserts GRH or priority for these field examples. Dwyer's full field list was not accessible. The discriminant-30301 triangular test with A=8 fails its sufficient inequality, but the larger positive autocorrelation test below proves real nonvanishing.

## Third finite certificate: discriminant 30301

The polynomial x^5−2x^3+2x^2+1 has squarefree discriminant 157·193 and the required local types. Its ramified invariant residual degrees are (3) and (1,2), giving conductor 30301³ and the same gamma factors. The 32 positive rational step weights define a normalized autocorrelation h, with C0=19457050 and minimum consecutive autocorrelation difference 93025. Thus h is nonnegative and decreasing, and its Fourier transform is nonnegative. Division by cosh gives full-strip positivity by the already proved harmonic argument.

The separate MPFR program was written without reading the root Arb source. Its nonsingular gamma integrand uses L_h(x)=(1−h(x))/x; L_h is monotone on each half-unit segment, so endpoint interval enclosures are rigorous. At 160 bits and 16384 cells it proves S<11<111/10<2H(0), with gap >1/10. The interval output is S in [10.979093271802581,10.985420668170939], threshold in [11.173701370408187,11.177607620408189]. The displayed rational assertions, not binary64 previews, certify the theorem.

A newly written PARI script regenerated every one of the 595877 prime-power traces using fixed points, two-cycles, and parity. Its entire CSV agrees byte for byte with both the earlier PARI stream and the independent FLINT stream. The root Arb certificate at 192 bits and 32768 cells independently proves the same sufficient inequalities. The manuscript gives the exact weights, autocorrelation formula, admissibility argument, local factors, gamma tail, and finite-bound mechanism. No priority claim is made for this field.

## Fourth finite certificate: discriminant 48976

The polynomial x^5−2x^3+x+2 has discriminant 2^4·3061. A coprime Hensel factorization of f(x+1) into a linear factor and an Eisenstein quartic proves maximality at two directly. The squarefree odd discriminant part proves global index one. The quadratic sign field has discriminant 3061 and Frobenius sign −1 at two. The inertia argument forces lower groups A4, V4, 1, and the invariant dimensions of R are 1 and 3. Thus a2(R)=6 and the wild Euler denominator is 1+T. The odd ramified denominator is (1−T)(1−T²), giving Q=2^6·3061^3.

The MPFR certificate at 160 bits and 2048 cells proves S<61/10<224/25<2H(0), with gap >14/5. The separate root Sympy/Arb implementation independently checks the maximal order, enumerates all transitive A4 subgroups, computes invariant dimensions and Frobenius traces on permutations, and factors every relevant prime. At 192 bits and 4096 cells it proves the same inequalities. Every one of the 465 traces agrees with both the MPFR exact arithmetic and a fresh PARI stream. An optional degree-ten resultant/maximal-order calculation also recovers both ramified factors and the conductor; its integral bases and `nfcertify` output are retained.

Serre's primary book was opened for the Eisenstein integral-closure theorem (Chapter I, Section 6, Proposition 17/corollary) and the Artin conductor and conductor-discriminant formulas (Chapter VI, Section 2, Proposition 2 Corollary 1′ and Proposition 4/corollary; Section 3, Proposition 6 Corollary 1). The root worker read the full mathematical note and MPFR source; the S5 worker then read the complete independent Arb source and checked its trace list. This is same-model checking, not human review.

## Optional external narrowing of the remaining pole

Liu (2026), Hexagon 2611.00421v2, primary record and original PDF were opened. The main Theorem 1.2 (printed p.3) and finite-order Theorem 8.29 (pp.78–80) give the stronger endpoint B* = 0.873345856106718576801184796065…; equations (42) and (44) define the degree-nine constant. The statement applies to B as a nontrivial quadratic Hecke function over the sextic field F. The weaker one-stage Theorem 1.1 gives 3493459/4000000 and is retained only as an intermediate bound.

The exact program `../../programs/liu_boundary_exact.py` checks the defining substitution, isolates the unique root between 8733458561067185768/10^19 and 8733458561067185769/10^19 by Sturm counts, and certifies irreducibility modulo 11. This finite algebraic certificate and the check of the theorem's applicability do not independently re-prove Liu's full 101-page analytic argument. Its zero-free theorem remains a named external input. The four finite real-zero certificates, the central-zero theorem, and the boundary-removal results do not use it. Source PDF SHA256: `077ccd27e19ee8dcc1f34c1b356290c09ad0d4a8a5a89f29fcced5d132b727fa`.

## Independent reconstruction of the new boundary results

The complete author argument is in `../../reviews/s5_offcentral_new_reductions.md`. Root checked the full simple and arbitrary-multiplicity proofs, including annihilator inclusions, Haar-density normalization, mutual singularity, nontriviality, and the bounded-prime versus exponential-coefficient contradiction. It also checked the global rigidity proof and all three countermodels. These are targeted same-model proof checks.

A fresh instance then received only the statements in `../../reviews/s5_offcentral_statement_targets.md`. It did not open the author's note or this manuscript before recording `../../reviews/s5_offcentral_blind_reconstruction.md`. It independently reconstructed every target A–F, including a different Gaussian/Følner proof of positivity and a Laplace-density proof of global rigidity. The S5 author worker read the entire completed reconstruction and compared it with the author argument; no mathematical gap was found. Two local notation errors in the independent record were corrected by its author without changing the proofs. Final independent-record SHA256: `58fafc3fecfe22c1a5b8acdadabea205c4792f52feb927e888acfb55321fe352`.

The child used the BHP short-interval bound as a granted target input and disclosed that its separate PDF fetch timed out. The author worker separately read the published p.562 bound. Thus independent derivation of the construction is distinguished from independent audit of that external input. The isolated reconstruction is a same-model reproof, not human review, different-model validation, or a formal proof-assistant certificate.

## Published scope and common-zero checks

Pilloni–Stroh Théorème 0.3, Khare–La Rosa–Wiese Theorem 1.2/4.4 and §4.2, and the entirety of published Calegari §§3–4 were read in the stated applicability audit. Root independently inspected the same primary input and the downstream dependencies, giving a targeted PASS. Because root had accidentally seen a few author-reconstruction lines, that audit is not labelled blind. A separate same-model agent then reconstructed the scope targets from their statement and primary sources before opening the author proof or changed manuscript. Its complete record is `../../reviews/s5_scope_upgrade_cubic_analytic_blind.md`, SHA256 `e4054da5e311651f56ba196ff2d14174a36b1b3961af7962d5862b0e917c02c7`. The prior central-pole exclusion theorem was explicitly granted; its use is not counted as a fresh reproof. Both root and the author read the entire completed reconstruction and found no discrepancy.

The common-zero statement packet preceded the author's proof. Root independently reconstructed its two targets using the packet, Belt Theorem 6.2 read in full local context, and explicitly granted earlier comparison/central-rigidity inputs. Root had supplied the elementary C identification and had seen the high-level spectrum/target messages; no author proof was opened before that reconstruction. Its record SHA256 is `3dfc196e0f2ae4ed384f254310ad7aaa120c26038a2090295c97fbf63c7ab090`. The author then read the entire root reconstruction and found no discrepancy. Root subsequently read the full author proof, including finite corrections, arbitrary orders and the pair-field zeta consequences, and gave a targeted PASS. These are same-model checks with the stated exposure boundaries.

The exact finite programs enumerate all 120 permutations, verify the Hecke-induced and exterior-square character identities, and count every exceptional eigenvalue. A preliminary handwritten rank-six spectrum was rejected by the first exact assertion and corrected before the passing certificate and manuscript integration. The final certificates pass; the failed preliminary assertion is retained in the check-event narrative, not described as a passing run.

## Compilation and visual verification

The final source was compiled in a fresh directory containing the three required TeX files. After editorial corrections, two final sequential pdfTeX passes gave a 41-page PDF of 591862 bytes. The final log has no errors, unresolved references or citations, multiply defined labels, or overfull boxes; a mild underfull bibliography line remains. Every one of the 41 pages was freshly rendered at 75 dpi and inspected in eleven contact sheets. The full unconditional pole-order bound is displayed in Theorem 1.1 before the common-zero assumption. The new scope proof, all finite corrections, all four field certificates, complete appendices, Method disclosure and bibliography fit within the page area. Final rendered-page inspection: 2026-11-24T17:49:06Z. The earlier 35-page frozen receipt is preserved separately in `../../reviews/s5_pre_scope_version_receipt.json`; its hashes are not overwritten. The four numerical certificate sources, outputs, and trace records are hash-compared with that earlier manifest and remain unchanged. No new numerical rerun is required for this manuscript-only extension.

## Provenance

The analytic reconstruction was written from the assigned statement and published literature before the supplied proof files were opened. Subsequent authorized source audit checked the proposed explicit-formula route against the separate Abel-residue and Hadamard route used in this manuscript. The source-isolation note and timestamped events are in `../../reviews/s5_independent.md` and `../../reviews/s5_check_events.tsv`.

These are mathematical checks by agents of the same model. They are not independent human peer review or formal verification. No unchanged supplied source file is included among the manuscript deliverables.


## Current 43-page appendix update: 24 November 2026, 19:25 UTC

This entry supersedes the earlier 41-page compilation description for the current source/PDF pair, while preserving that description as a historical check event. The prior exact pair and publication metadata are retained read-only in `../../reviews/paper_II_before_symmetric_square_20261124_192143/`.

A separate same-model agent independently reconstructed the symmetric-square targets from the statement packet, two explicit prior-identity clarifications, and Takeda's primary theorem. The complete proof froze at 19:18:10 UTC before the authored symmetric-square note was read at 19:19:44 UTC. Root reported a full targeted read at 19:20 UTC and PASS. Independent integer enumeration checked all 120 permutations, the order-20 affine group, all character identities, and the exact local polynomial quotient. The resulting D bound is correct but redundant: D=L(V)L(R)zeta_F, so ord D >= ord L(R). Actual arithmetic strictness is not established and no improvement over the existing Artin-factor criterion is claimed.

The final isolated build used three sequential pdfTeX wrapper passes and produced 43 pages, 606950 bytes. Its final log has no errors, undefined references/citations, overfull boxes, LaTeX warnings or natbib warnings. Current PDF SHA256: `c53dd382cbee567ee3d096ea7f82b07b44249d65e0ee1e503be225cf2a2aaf7e`. Fresh images of pages 38--43 were personally inspected, including the citation paragraph in Proposition D.3, the complete new Proposition D.4, both finite tables, its deletion/order and redundancy proof, Remark D.5, and new reference entries. This is targeted affected-page QA, not a claim that all 43 current pages were visually reinspected. No numerical certificate was changed or rerun.

The exact new external locators were personally checked in primary PDFs: Takeda (2015 v1), Theorem 7.1 pp.49--50; Jacquet--Shalika (1981 II), Proposition 3.3 p.795, Proposition 3.6 pp.802--804, Theorem 3.7 p.804; Shahidi (1980), theorem p.462. These are statement/applicability checks, not new proofs of the full analytic papers. Detailed exposure, proof and source hashes are in the independent review receipt and `symmetric_square_build_receipt.json`. No human review is represented.
