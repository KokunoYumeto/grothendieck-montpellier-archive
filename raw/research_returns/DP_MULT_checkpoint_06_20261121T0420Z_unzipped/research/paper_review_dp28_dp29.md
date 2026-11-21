# Independent review of integrated DP28 and DP29

Date: 2026-11-21 UTC. Reviewer: /root/formal_bound, inherited GPT-6 Astra Pro; effort setting not exposed. This is an independent reread of the root's integrated text, by the agent who developed the underlying kernel proofs. It is not an independent-model check, a Lean compilation, or a computational formal proof.

## Result

**PASS.** The statements and complete proofs of DP28 and DP29 in DP_MULT.tex agree with the established arguments. No mathematical correction is required. The review includes their preceding logarithm construction and definitions (H1)–(H4).

Two minor editorial observations were sent to the root:

- The source locator “Statement.lean, lines 43–94” should be 39–94 if intended to include the definitions of the two torus characters and the torus substitution, which begin at lines 39 and 41.
- The local paragraph broadening \(K\) may explicitly say “a valued extension of \(\mathbf Q_p\), with \(v(p)=1\).” The paper's global conventions already supply the \(p\)-adic setting, so this is a clarity issue rather than a counterexample to the stated mathematics.

## Exact reviewed blocks

The snapshot was captured at 2026-11-21 01:06:19.914719 UTC and both saved blocks were reread in full at 01:06:34 UTC (observed clock).

| Block | Source lines at capture | SHA-256 of exact block, without appended final LF |
|---|---:|---|
| DP28, proposition through end of proof | 434–464 | a75b8a5046b1666b86658724545e26eb2c2659b24a3400eb34eef53cc4e8a5d7 |
| DP29, proposition through end of proof | 468–508 | f4888e81c635d7c81ebeccef040877a9b76fdf2190b20c6f928087fef874a8f5 |
| Preceding kernel subsection and hypotheses | subsection start through DP28 | 9dc1f77b59946d08e8a3912d0168d0b121ac527046a8ee993e176b752c4afd90 |

Whole-file hash at capture: 90691253b1c578610e707a9d8984b69821d1f98c1539eb230e5dfac574b0179a.

Machine-readable metadata, including the snapshot files' own hashes with their appended terminal LF, is saved in paper_review_dp28_dp29_metadata.json. The exact saved texts are DP28_integrated_review_snapshot.tex, DP29_integrated_review_snapshot.tex, and DP28_29_setup_snapshot.tex.

## DP28: challenges checked

1. **Known Honda integrality.** Hazewinkel, Astérisque 63 (1979), Functional Equation Lemma 2.3 and formula (2.5), p.74, applies with \(B=\mathbf Z_p\), \(L=\mathbf Q_p\), ideal \(pB\), \(\sigma=\mathrm{id}\), \(q=p^h\), \(s_1=1/p\), and all other \(s_i=0\). The required identity is \(L_h(T)-p^{-1}L_h(T^q)=T\), and \(b^q\equiv b\pmod p\) holds for \(b\in\mathbf Z_p\). The cited theorem is used as a known result; no priority claim is made.
2. **Height and inverse scaling.** The first nonlinear \(p\)-series coefficient is \(1-p^{q-1}\), a unit. Scaling by \(\pi^{q-1}=p\) gives logarithm \(Z+Z^q\) modulo \(\pi\), with inverse \(\sum_{r\ge0}(-1)^rZ^{q^r}\). Thus the coefficient equalities used later are justified.
3. **All four adopted hypotheses.** The witness has rational \(p\)-adic coefficients; the roots of unity act through the declared characters \(1,-p\); all monomials have positive bidegrees and degree at least \(p+1\); and the two integral-unit ratios give precisely the two required exponential coboundaries.
4. **Unique coefficient contribution.** With \(k=p^{h-1}<q\), terms with \(m<k\) cannot contribute \(Y^k\), because their next possible \(Y\)-degree is at least \(m+q-1\ge q\); terms with \(m>k\) have larger initial \(Y\)-degree. The exact sign and denominator are therefore correct.
5. **Strict inequality and scope.** The inequality is strict exactly as used for \(h\ge3\). The result refutes the intermediate weighted estimate, and the integrated statement correctly does not refute a final derivative estimate.

## DP29: challenges checked

1. **Hypothesis economy and range.** The argument uses (H2)–(H4), odd \(p\), and \(h\ge2\), and does not silently need the unramified coefficient condition (H1).
2. **Minimum degree and weight choice.** The torus argument gives \(\operatorname{ord}\beta\ge p+1\), and \(r_0=p/(p^2-1)\) satisfies both \(r_0\ge\rho_h\) and \((p+1)r_0=s+1\).
3. **Formal substitution and logarithm.** Every substitution has zero constant term, so only finitely many terms contribute to a fixed coefficient. The logarithm estimate follows from \(m(s+1)-v_p(m)\ge s+1\); no analytic convergence is presumed.
4. **Binomial extraction.** The non-\(p\)-power and \(p\)-power cases both furnish an interior binomial coefficient of valuation at most one. At least one bidegree is at least two. No cancellation between different coefficients can affect the selected split monomial.
5. **The final exponential.** Integral linear substitutions, a unit \(\epsilon\), and \(\sigma/2\) preserve the exponent's weight; odd \(p\) is essential for the last assertion. Legendre's formula gives exactly \(\rho_2|\kappa|-\sum_i s_p(\kappa_i)/(p-1)\). The restriction \(n\ge1\) is applied only to the logarithmic digit bound; the constant coefficient is handled separately.
6. **Nonzero example.** For odd \(p\), \(\binom{1/2}{m}\in\mathbf Z_p\) by continuity of the fixed binomial polynomial on \(\mathbf Z_p\). After scaling, its correction factor is \(1\) modulo \(\pi\), so it cannot cancel the unit coefficient of the scaled inverse logarithm at \(q^r\). The exact valuation \(c_h(q^r-1)\), including \(r=0\), follows. The explicit construction uses an integral-unit correction and correctly makes no claim of a theta realization.

## Exact primary reference for distinct-slope Hom vanishing

**Reference to use:** Nicholas M. Katz, “Slope filtration of F-crystals,” Astérisque 63 (1979), 113–163, §1.3, pp.119–120, especially the **first paragraph of p.120**.

Katz states the Dieudonné semisimplicity theorem: over an algebraically closed perfect field, the isogeny category is semisimple and its simple representatives are indexed by the rational slopes \(\lambda\) as \(E(\lambda)\). This is an unnumbered theorem statement, immediately before the displayed decomposition; **do not label it Theorem 1.3.1**, which is the later statement about slope multiplicities.

The needed known consequence is
\[
 \operatorname{Hom}_{F\text{-isoc}}(M_\lambda,N_\mu)=0
 \quad\text{if }\lambda\ne\mu,
\]
since the two objects have disjoint simple constituents. A perfect field is handled by faithful extension to its algebraic closure. The faithful Dieudonné description and torsionfreeness of Hom between the integral free modules then give the corresponding zero Hom for the \(p\)-divisible groups. This is a direct application of the cited standard theorem, not a new classification proof.

For DP31 the two slopes are \(1/h\) and \((h-1)/h\), unequal when \(h>2\).

Primary PDF:
https://www.numdam.org/item/AST_1979__63__113_0.pdf

The published p.120 was rendered and visually inspected as katz_slope_p120.png. PDF page index: 8 (ninth physical PDF page).

Suggested bibliography entry:

Nicholas M. Katz, *Slope filtration of F-crystals*, Astérisque **63** (1979), 113–163.

The paper's own original classification reference is Ju. I. Manin, *The theory of commutative formal groups over fields of finite characteristic*, Russian Mathematical Surveys **18** (1963), 1–83; no claim is made that this agent independently recovered a theorem number from that original.

## Recovery and check events

| Event | Observed UTC time | Check |
|---|---|---|
| DP28/DP29 initial integrated read | 2026-11-21 01:04:09 | Read full setup and both proposition/proof blocks |
| Hazewinkel primary-source check | 2026-11-21 01:05:45 | Read Lemma 2.3, (2.2), (2.4), (2.5) and the Lubin–Tate specialization in the public PDF |
| Katz PDF download completed | 2026-11-21 01:05:45.473009 | 3,395,507 bytes; SHA-256 dccaa89efa4a65410d9d8d54e45dbd7d72b2f68d7fb86f5f9b834b6f363ebcf5 |
| Exact integrated blocks captured | 2026-11-21 01:06:19.914719 | Saved snapshots and metadata |
| Snapshot reread and Katz p.120 visual check | 2026-11-21 01:06:34 | Both proofs passed; exact unnumbered primary theorem locator verified |

All review events were performed by the inherited GPT-6 Astra Pro agent named above, with effort not exposed. No theorem prover, numerical coefficient test, or external RH audit was run.
