# DP60 — independent complete proof and integrated-version review

**PASS.** Checker `/root/archive_binomial`, GPT-6 Astra Pro; reasoning effort not exposed. Date2026-11-21 UTC. At03:57:22 I read the entire ten-section memo and the entire intended LaTeX theorem, proof and scope paragraphs. The targeted source and contraction-profile challenge closed at03:58:07. No proof correction was requested.

Memo SHA256: `e654214e03dbf299af2759c8643f5dd01633515608134bf33555e526c808e5d2`.

Fragment SHA256: `d1ceda8a9196ec35b6da24df6e60e33077154d89da985389f61ca31e752bfcff`.

## Mathematical challenge

### Constant precision and all product errors

At an ordinary witness m=(p^k+1)p^r, the digit sum is exactly two. An error prefactor divisible byp has derivative valuation at least `1+cm−2/(p−1)`, whereas the pure value has valuation `cm−1/(p−1)`. The gap is `1−1/(p−1)>0` for every oddp, includingp=3. Terms of original group-coordinate order exceedingn remain of that order after substitution by the normalized inverse logarithm, so they cannot affect any selected derivative of degree at mostn.

For the two-copy harmonic expression the product error is divisible byp in the entire product-coordinate power-series ring. It need not remain a separated product; the full polydisc integrality proof only requires an arbitrary integral function in the product coordinates. Every supported monomial of the harmonic differential polynomial has its coefficient times its multi-factorial equal, up to sign, to a!b!. Thus the same strictly positive valuation gap holds for the complete error sum. There is no hidden growth of the required coefficient precision withn.

I re-read DP46's weighted inverse-logarithm and full primitive-logarithm argument, and DP51's complete full-polydisc extension. They justify precisely the integral-prefactor claims used here. The argument does not improperly extend a one-variable assertion to the entire product ring.

### Fixed algebraic generators and representatives

DP56 supplies the projective coordinates over the localized number-field ring R0, with a unit cotangent minor. The finitely many residue-class exponents b_l ensure that every sufficiently large tensor exponent has the form b_l+aq with q≥n. Only finitely many auxiliary sections are chosen, so their norms can be bounded independently of the moving tensor level.

Localization base change gives the chosen generators as fractions of sections over A0=OE[1/14]. Their finitely many denominators can be cleared by algebraic integers outside the selected prime. Such multipliers are local units; a common one for the h_i preserves all coordinate ratios. Clearing can add zeroes elsewhere, but creates no new finite-prime denominator. This does not require that the original completed formal frame have algebraic coefficients.

At11, the residue of zeta7 has degree three and the set `c0+c1 zeta7+c2 zeta7^2`, with each c_i between0 and10, is a genuine complete residue system for F_(11^3). It consists of algebraic integers and has absolute value at most30 at every complex embedding. The CRT explanation of reduction from OE through localization and completion is correct; no local residue class is omitted.

The interpolating polynomial is taken only modulo11. Its coefficients therefore belong to this fixed finite set, even when the target formal unit U is defined only over the completion. Homogenization with h0 and the residue-class generator eta_l makes every term a global section of exactly L^kappa, with nonnegative exponents sinceq≥n. The congruence in integral t-coordinates is equivalent to the claimed congruence in z-coordinates. Its constant term is a unit, so the global section is nonzero.

### Norms, primes and tensor level

There are binom(n+3,3) monomials. Each term is a product ofq fixed h-sections and one fixed eta-section, so tensor-compatible metrics give the exact bound `30 binom(n+3,3) H^(q+1)`. Sinceq≤kappa/a, its logarithm is O(kappa+log(n+1)). This estimate remains valid at all finitely many complex embeddings simultaneously.

At every good-model nonarchimedean place the sections are integral and have model sup norm at most one. At the finitely many remaining places, proper analytification and continuity bound the same fixed generator set; the ultrametric inequality removes the monomial-count factor. The resulting specified adelic positive-log sup-size has the claimed order bound.

The least square above an+b0, adjusted by at most one in its square root to avoid11, has kappa=an+O(sqrt n). Every such exponent is a unit at11, and the pure-kernel calculation is uniform over unit exponents. The source factor M^(−m) is a unit. Thus the exact values and the linear tensor/logarithmic-norm bounds hold simultaneously for every explicit witness of degree at most the interpolation order.

Fixed continuous Hermitian metric changes cost O(kappa) in logarithm by compactness. A fixed honest holomorphic frame or a fixed holomorphic gauge on a relatively compact chart also costs O(kappa). The statement correctly excludes an unidentified p-adic display frame or level-dependent source metric from this comparison.

## Sources and integrated preservation

Stacks Project Lemma30.5.2(2), Tag02KH, was opened and its exact statement read: flat base change for a quasi-coherent sheaf on a quasi-compact, quasi-separated morphism. The localization A0→R0 and the proper Jacobian satisfy all hypotheses. The projective-coordinate and ample-power inputs from Tags01VT and01Q3 were already checked in the complete DP56 review; they are cited rather than re-proved here.

The entire intended fragment retains all new proof components: strict constant-precision error estimate, complete harmonic product errors, finite residue-class generators, global denominator clearing, bounded coefficient representatives, explicit section formula, all norm estimates, square-level choice and metric limits. Snapshots, complete theorem/proof hash and actual main preservation counts are in `late_proof_snapshots/DP60_archive_review_metadata.json`.

## Exact scope

The theorem constructs actual number-field sections in the full global section space, integral away from2 and7, with exact finite local values and linear tensor/logarithmic norm bounds. It does not identify these particular sections with the prescribed translate span or theta image, align an externally prescribed row-degree sequence with the explicit ray, compare the constants with a net global budget, or prove existence or impossibility of a shorter complete lift chain. No machine formalization, numerical experiment or Lean execution is claimed.

At record time the exact intended fragment occurs 0 time(s) in the main paper, and the complete theorem/proof block occurs 0 time(s). Complete block SHA256: `5cc7cf847e68a780215864cba8abb38e42056210bf1e5278646af4e3af5875de`.

At04:01:59 UTC the unchanged reviewed fragment was verified to occur exactly once in the main paper. This later event is byte preservation only; it does not duplicate the actual complete reading recorded above.
