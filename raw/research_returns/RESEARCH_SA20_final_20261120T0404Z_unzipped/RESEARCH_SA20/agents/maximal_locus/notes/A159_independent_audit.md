# A.159 independent authored-text audit

Auditor: `/root/maximal_locus2`, GPT-6 Astra, OpenAI.
Date: 20 November 2026, after checkpoint 19 recovery.
Audited source: `agents/higher_comparison/A159_all_field_higher_surjectivity.tex`.
Extent: all 490 lines / 22,116 characters, including the concluding `end{proof}`.
SHA256: `21e58ae75591f1787ffac6cb51e43191be076edada9a5b108c9b2490ae02c1e6`.
Verdict: **FULL AUTHORED MATHEMATICAL PASS**.

## Scope of the verdict

This is a full independent audit of the actual recovered A.159 source, not just an argument outline. It establishes higher PL-to-definable surjectivity over every fixed o-minimal real closed field, together with its stated standard-bound single-family and common-data pair criteria. It does not establish higher injectivity by itself. A.154, A.157, and A.158 are treated as separately proved dependencies; their specific interfaces used here are checked against the stated construction. The marked Mnëv modification is the same finite modification previously audited against the original source, not a claim that the unmodified source literally states the marked result.

## Checked steps

1. **Standard model.** Finite abstract realizations and finite PL link/chart descriptors suffice for the real-algebraic auxiliary model by real-closed-field completeness. This is finite certificate transfer, not parameterized PL homotopy invariance. The barycentre-to-characteristic-vector cubical map is genuinely PL, preserves every marked subcomplex, and has standard numerical Lipschitz bounds.

2. **Contraction over the field.** The residual-minimum argument is valid by definable compactness: a positive minimum m of |T(t)-t| contradicts r(T(t)) <= c m < m. Uniqueness and the displayed perturbation bound follow directly. Definable uniform continuity on the compact input cube gives local uniform variation with parameters. No ordinary completeness or infinite iteration is used.

3. **Hudson data.** Standard integer forward bounds and fixed real-algebraic target data allow an ordinary finite number of rises with cL < 1. The fixed-point equations have the stated initial and endpoint behavior. Formula (159.4) verifies the inverse. At v=1 the only moving bands are [2j,2j+1] for 0 <= j < R-1; the final index contributes the terminal plateau. The support-label monotonicity uses the bands met by each actual box intersection, as required.

4. **Finite target and marked split.** The source-dependent input is not used to select an infinitesimal mesh. The finite support poset and target configuration certificates are fixed first. Proposition 36's conic-star and incidence statements, together with a locally flat marked seam, give the ball/equatorial-disk pair used in the split. The source explicitly labels this as an inference. Intersecting nested balls with fixed global halves/seams preserves the required incidences. The exact inverse-image identities (159.5) preserve prismaticity. Equality outside support balls and continuity also fix their boundary inverse images.

5. **Prism straightening.** The source and target prisms are literal spatial-cell products with closed parameter simplices. All total product boundary faces have already been assigned in the increasing total-dimension induction. Coning corresponding boundary maps from centers with the same parameter coordinate preserves projection and is PL after finite compatible subdivisions. Relative Hauptvermutung supplies the one ambient map making all finitely many source cells PL. Its cellwise isotopy preserves the marked restrictions.

6. **Relative definable homotopy.** Radial extension of the prescribed spatial boundary family gives R_p. Dividing the prescribed full-ball boundary maps by R_p produces boundary-fixed Q_p. The explicit Alexander formula (159.6), including its displacement bound 2r, extends these data continuously at the parameter center over an arbitrary real closed field. The argument only asks this extension to be definable, not jointly PL.

7. **Pair equality.** Common Hudson data make the fixed-point systems equal on the bottom and parameter boundary. Common configuration data give one terminal target coloring. Source cells coincide on the marked subcomplex E. A common PL endpoint and then a common homotopy are constructed on E before their separate extensions. Quotients therefore stay based and bottom-fixed at every stage.

8. **Producing standard bounds.** All evolving vector coordinates remain in a standard bounded cube. Ordinary finite monotonicity counts give ordinary finite variation and mixed-coordinate bounds. Fixed real-algebraic PL changes preserve standard boundedness. In the maximum norm, tags 0 and 3 prevent cross-tag nearest matches and make tagged Hausdorff distance the maximum of the two distances. A.158's finite integer-tagged source, the appended constant boundary copy, and the finite labelled join all have standard coordinate and Lipschitz bounds.

9. **Boundary clock and graph-to-forward estimate.** The boundary section of w is literally affine. Any coordinate line lying in a boundary face has variation c t, so its normalized clock is the identity; endpoint coordinates remain fixed as well. Thus the clock preserves the whole parameter boundary. Definable compactness supplies nearest graph matches, and the uniform spatial Lipschitz bound gives (159.10) without any inverse bound. The final convex homotopy from id to g is relative to the boundary.

10. **Limits of the theorem.** The concluding nonconstant prescribed-boundary distinction is accurate: an arbitrary nonreal PL boundary may have a nonstandard parameter bound. A.159 alone therefore does not infer the relative injectivity theorem.

## Minor exposition suggestion

An explicit global sentence that the cubical and tagged graph estimates use the maximum norm would make the tag-diameter assertion unambiguous. The equations already use this norm. This is not a mathematical gap: all required conclusions hold with that convention, and any finite-dimensional change of norm costs a standard factor.

## Original-source provenance retained from the prior marked audit

Mnëv, arXiv:0708.4039: Proposition 4 p.21; equation (11) and Proposition 5 pp.22-23; Lemma 3 proof Steps 2-3 pp.24-25; Propositions 35-36 pp.61-63; Lemma 6 pp.63-65; Lemma 8 pp.67-68; Proposition 57 pp.88-90. The marked split is an explicitly proved adaptation.

Shiota, arXiv:1002.1508v3, Theorem 2.1, printed p.5: finite compatible o-minimal Hauptvermutung over the given real closed field.
