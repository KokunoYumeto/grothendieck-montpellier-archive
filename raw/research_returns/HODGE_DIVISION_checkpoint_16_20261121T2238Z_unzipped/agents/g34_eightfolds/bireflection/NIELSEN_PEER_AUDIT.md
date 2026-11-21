# Independent whole-proof audit: D-NR-01–04

Reviewer: /root/g34_eightfolds; GPT-6 Astra Pro; effort inherited/unexposed; HODGE_DIVISION; 2026-11-21 UTC.

**Outcome: PASS in the stated scope.** I read the entire current `agents/imprimitive/nielsen_rank_algorithm.tex`, including the new exact Rouché subroutine, complete-package dovetailing, finite further field-of-definition extension, all-sheet specialization, and the Grothendieck-framework clarification. This is a whole-proof mathematical audit, not an execution of the unbounded model search.

## Exact monodromy

Each segment certificate compares a strict lower bound on the starting polynomial on disjoint root discs with an exact coefficient-derivative upper bound. The algebraic choices of centers, radii, and bounds are decidable. Compactness away from the leading-coefficient and discriminant zeros provides uniform root separation and bounded derivatives, proving termination of dyadic subdivision. Extra discriminant points are avoided but do not create new branch classes on the normalization. The deck-action convention and right-multiplication comparison correctly retain the inner Nielsen label.

## Selecting the component

All finite coefficient-field, curve, chart, action, and certification packages are dovetailed by description length. The individual field-factorization, smoothness, geometric-connectedness, degree, group-law, and branch-support tests reduce to effective exact algebra. Good spreading is followed by field norms so that every sheet is good over one nonempty base open. Irreducibility of the finite coefficient field gives connected S. Testing every algebraic point of one finite étale fibre is essential and is correctly imposed: a map of finite covers is open and closed onto one component, and the component remains irreducible after removing the bad divisor. A finite further field extension supplies the generic cover even when the group has nontrivial center. Thus a successful generic package occurs and has the correct full generic period rank.

## Published source check

I independently read the complete relevant passages of Romagny–Wewers, *Hurwitz spaces*, Séminaires et Congrès 13 (2006), 313–341: Theorem 3.1 and Propositions 3.2 and 3.4, pp.319–321; Theorem 4.3, p.323 and its full derivation in §4.4, p.327; Theorem 4.11, pp.328–331 and Remark 4.15(i), p.331. The local published PDF was already retained by imprimitive. The analytic covering, finite field of definition, algebraic comparison, and characteristic-zero finiteness claims used in the proof are supported at these locators. The proof appropriately does not silently assume a universal cover on the coarse generic point or cite an unspecified SGA field-of-definition statement.

## Full codifferential and termination

The Schur contraction sum is the invariant part of differential multiplication. The local models z=u^e give precisely invariant tangent sheaf T_P1(-B) and quadratic differentials with simple branch poles, so the entire r−3 dimensional Hurwitz tangent space is tested. Enumerating regular rational differentials terminates at the known genus, with regularity checked in torsion-free differential modules on finitely many smooth affine charts. Gaussian elimination in the finite extension of Qbar(t) gives both a lower minor and an upper row-reduction certificate. No restricted subfamily or dimension inequality is used as a substitute for the period derivative.

The induced natural-group formula sums the cyclic products over the cosets, giving exactly the trace of quadratic differentials. It retains the map X→P1 and therefore remains correct when its forgetting map is not a submersion. The finite table claim fixes all group parameters and bounds tuple length first; it does not assert an executed unbounded table.

## Independent finite example

I rebuilt the cubic example directly in a separate SymPy matrix: products indexed by (a,b) map to the coefficient vector of z^(a+b), giving a 9×25 matrix and an independently chosen identity 9-minor. The branch valuations are (1,0) and (0,1), and the infinity order is 4−a in both eigenspaces. Riemann–Hurwitz gives genus10, so the two five-form lists exhaust H0. Exact output is in `nielsen_peer_example.json`. This verifies the displayed finite example only; the generic model enumeration has not been run.
