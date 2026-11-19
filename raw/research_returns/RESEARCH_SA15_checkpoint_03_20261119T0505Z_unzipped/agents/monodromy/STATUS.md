# Part A.3–A.5 local status, 2026-11-19 05:05 UTC

This contribution is incomplete as an answer to all A.3–A.5. Every projective-space case is now determined; arbitrary smooth ambient X remains a separate gate.

| Item | Established | Remaining gate |
|---|---|---|
| A.3 positivity | Explicit all-X threshold d0 in results.tex, full proof and cohomological constants; asymptotic deg(X)d^n/n! | Exact generic rank for every fixed X |
| A.3 generic relative ordinarity | Refuted for smooth X: explicit finite-group-scheme quotient construction has Pic0=alpha4 in characteristic2 and rank stable <=g−2<dimE=g−1 in all sufficiently large degrees | Exact generic rank of this X; final invariant-ring/Bertini finite-field search was not executed |
| A.3 projective-space rank | binom(d−1,n), all d,p, from ordinary hyperplane degeneration | None |
| A.3 Hodge-level parenthesis | Literal eventual statement on maximal-stable-rank U_d proved, including p-torsion; cor:eventual-hodge-parenthesis | Stronger individual-Y equivalence outside U_d is false; it is a different quantifier |
| A.4 projective space, odd p | All n>=2 and all d: full GL_binom(d−1,n)(Fp), geometric=arithmetic, with full determinant; zero vector space for d<=n | None |
| A.4 projective space, p2 | All n>=2 and all d: rank0 for d<=n; rank1 trivial for d=n+1; full GL if d≡n mod2; full nonzero-covector stabilizer if d≡n+1 mod2 and d>=n+3 | None |
| A.4 full-GL expectation | Refuted in infinitely many degrees for every Pn in characteristic2; invariant hyperplane gives reducibility | Exact geometric/arithmetic group and determinant for arbitrary X |
| A.4 determinant | Exact general Hasse/Kummer character; full evaluation for every Pn | Evaluate image for arbitrary X |
| A.5 projective space | Every nonempty smooth-parameter open attains every residue exactly from d=n+2, every p and n>=2; d<=n only1, d=n+1 ordinary open misses1 | None |
| A.5 arbitrary X | Literal connected/non-geometrically-connected formulation has root's counterexample | Geometrically connected general-X statement; no extension of a stable sheaf across rank drop is assumed |
| Lead A | Universal full-GL assertion refuted; positivity proved all X; exact Pn groups and residue thresholds proved; generic relative ordinarity refuted for smooth X | Universal geometric-connected-X residue assertion and exact generic rank/groups remain |

## Current proof files

- results.tex: all-X positivity, projective-space rank, determinant Kummer character, plane residues and prerequisite audits.
- relative_ordinarity_counterexample.tex: smooth Pic0=alpha4 counterexample; root independently audited; finite Hopf/algebra checks executed; final invariant-ring/Bertini search explicitly not executed.
- odd_characteristic_plane.tex: all odd-p plane groups, with opened Kantor–Seress Theorem3.6 and elementary cocycle/block proof.
- projective_space_odd.tex: all odd-p Pn groups and sharp residue threshold; root independently audited all parts.
- projective_space_char2.tex: all characteristic-two Pn groups by independent AS quadric swaps, Johnson-coordinate transpositions, elementary finite-group generation, and explicit global Hasse covector; root independently audited all parts.
- all_degree_char2_contact.tex and degree5/6/7 files: independent geometric plane-theta argument, still valid but superseded for group computation by the simpler all-Pn quadric proof.

## Prerequisite audit

R1 was read in check_8_5_7.md, sections1–4. Its nilpotence step is valid: Frobenius on the hypersurface ideal factors through its p^e-th power, hence through H^(n−1)(O_X(−p^e d)); Serre duality and Serre vanishing kill this group for large e. In the explicit positivity proof the stronger vanishing H^(n−1)(O_X(−d))=0 already holds for d>=r_omega−1. We subtract the stable ambient rank, not the full coherent dimension.

R2/R10's Lang/Artin–Schreier comparison is supported by the opened Katz SGA7II XXII Proposition2.0 and the finite-dimensional Lang basis argument. The degeneration arguments use the full coherent bundle on its explicit invertibility open. A rank-dropping elliptic degeneration is used only to calculate a Hasse determinant valuation, without extending a stable local system through it.

Root's A.1 all-degree complete-intersection/W2-liftable ranges were independently checked against Cotner–Zavyalov Definition2.2.1 and Theorem2.2.3, printedp1854. The finite de Rham filtration, cone triangle, and integral derived Nakayama shifts all check.

## Main next gate

For arbitrary geometrically connected X the coherent top rank need not be ordinary, as the smooth alpha4 example proves. A hyperplane-union boundary can lie below the generic stable rank. The projective-space proof cannot simply be transplanted: its full-rank ordinary arrangement and its projective strata are essential. Seek either a rigorously extendible graded factor, or a decomposition-group argument that controls extra unit roots near the boundary. No such reduction is yet claimed.
