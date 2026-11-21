# Ordinary rank-two exclusion: independent whole-proof and exact source audit

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed.
Date: 21 November 2026. This is a mathematical and source-text audit;
no Lean kernel build was run.

## Verdict and scope

The complete proof of `KT-ORDINARY-RANK2-UNIT-EXCLUSION` and its
restriction/twist variant in
`../unitary_audit/reducible_comparison/ordinary_rank2_exclusion.tex`
passes. The final actual-source corollary
`KT-AUXILIARY-UNIT-NO-TYPEII` also passes a complete independent read.
The reviewed version and source hashes, including the earlier draft hash,
are recorded in `ordinary_rank2_review_manifest.json`.

The hypotheses are substantive: a continuous absolutely irreducible
two-dimensional representation over a finite extension of Q_p; residual
semisimplification `1 + eta omega^a`; an ordinary stable line with
unramified rank-one quotient; and unramified restriction to the quadratic
field away from p. Here p>3, p does not divide the fundamental negative
discriminant, and a is positive even and nonzero modulo p−1. No upper
bound on a and no splitting assumption at p are needed.

The Bernoulli unit contradicts a nonzero class in the precise residual
strict group already proved zero in
`KT-AUXILIARY-UNIT-SELMER-BRIDGE`. This does not assert that all bare
`Adm2A` representations satisfy the residual and determinant conditions,
and it does not exclude generic irreducible rank-three sources.

## Whole new-proof checks

Urban's Theorem 1.1 is applied with the two ordered scalar blocks
`1, eta epsilon^a`. Compactness supplies an integral stable lattice;
the residual characters are distinct already on inertia at p. The
auxiliary nonzero fractional module is finite over a DVR and contained
in its fraction field, so it is free of rank one. The no-quotient
condition yields a nonsplit residual extension
`0 -> k -> Lbar -> k(eta omega^a) -> 0`.

The ordinary line intersects this lattice in a saturated rank-one
submodule. Its reduced quotient is unramified, so it must be the residual
character 1, while the line has character `eta omega^a`. It therefore
splits the opposite extension on the whole decomposition group at p.
This argument uses the nontrivial residual inertia character, not a
Fontaine–Laffaille range.

At every other rational prime, inertia acts through a quotient of order
at most two because the representation is unramified after restriction
to the quadratic field. Averaging is valid in characteristic p>2,
including primes dividing the quadratic discriminant. Thus every away
inertia restriction of the extension class vanishes.

All coefficient character values lie in F_p. Extending the strict
cohomology group from F_p to the finite residue field is just taking a
finite direct sum, with identical local maps. This is a finite-coefficient
argument throughout; no unjustified finite/divisible identification is
inserted. The auxiliary-unit bridge supplies the already audited zero
group.

For the restriction variant, the two characters on G_E are distinct
and invariant under conjugation by G_Q. Semisimplification therefore
splits into two G_Q characters; their extensions differ only by eta.
The determinant determines the opposite eta exponents. Twisting by eta
preserves the ordinary unramified quotient because p is unramified in E.

Urban's exact statement and complete printed proof on author pages 6–10
of arXiv math/9803171v1 were read in the preceding independent audit
`REDUCIBLE_COMPARISON_REVIEW.md`; that accepted source input is reused
here, rather than represented as a fresh kernel or full-library check.

## Exact actual-point source match

Source root below is the pinned tree under
`source/src/Development/AutomorphicArithmetic/AutomorphicVarieties/`.

1. `UnitaryThreeGroups/RhoKApply.lean:76–83` defines `Dat.IsPt`.
   Its `int` and `red` clauses hold for every global matrix entry;
   `red` is closeness to `r0 eta PsiQ`, not just a Frobenius condition.
   `IsPtOf.lean:124–166` proves `isPt_push` from an actual local
   coefficient-ring point. That complete proof was read.

2. `UnitaryThreeGroups/BaseRepGL3NormalisedOfPsiEqOne.lean:28–34`
   defines the corner, `TypeII`, and `Wfun`. The last is the corner
   multiplied on the right by `diag(-1,1)` when eta is −1, and is the
   corner itself when eta is 1. Meanwhile
   `UnitaryThreeReflectionRight.lean:291–301` defines `r0` with left
   matrix `tor Psi = diag(Psi,1,Psi^{-1})`.

3. `UnitaryThreeGroups/CoboundaryLemmaNoColumn.lean:135–141`
   is `typeII_facts`. Its complete proof and the complete helper
   `W_facts` were read. For an actual Type-II point it constructs a
   continuous W, irreducible over the algebraic coefficient closure,
   with every matrix exactly `Wfun r g`, and determinant exactly eta.
   Consequently its canonical integral reduction is globally
   `diag(eta barPsi, barPsi^{-1})`. For psi=1, the twist
   `R = epsilon^e W` has residual semisimplification
   `eta omega^{2e} + 1` and determinant `eta epsilon^{2e}`.
   The canonical W does not require an additional eta twist.

4. `UnitaryThreeGroups/AdmissibleOfTypeII.lean:142–195` constructs
   the full rational decomposition-group flag of W. The high line has
   inertia character `epsilon^e psi`; the quotient has
   `epsilon^{-e} psi^{-1}`. For psi=1, twisting by epsilon^e leaves
   an unramified quotient. The proof extends the inertia eigenline
   to the complete decomposition group, so it applies when p is inert
   as well as when it splits. The entire file and the corresponding
   dense-threshold proof were read, not merely this statement.

5. `UnitaryThreeGroups/PtInertiaAway.lean:54–58` gives the precise
   away-inertia conjugacy for `I_q intersect ker eta`. With psi=1,
   epsilon is trivial on I_q for q≠p, so the comparison diagonal is
   the identity. Hence r, its corner W, and the epsilon^e twist are
   unramified on G_E away from p. The complete proof was read.

6. Finite coefficients need not be inferred from automorphy.
   `UnitaryThreeGroups/TanDet.lean:150–152` specifies `IsCO c.O R`;
   private `pow_le` at 182–210 and private `fin_quot` at 212–216 prove
   `R/(ker f)^2` finite over c.O for any `IsLocPt f`.
   Its quotient `R/ker f`, identified with the image of f, is therefore
   finite as well. The fraction field of this image is a finite
   extension of Q_p, and all pushed representation entries and all
   `Wfun` entries lie in it. Enlarging this field finitely to contain
   the finitely many entries of the local flag basis is permitted.
   The complete `fin_gen`, `pow_le`, and `fin_quot` proofs were read;
   their imported completion/Nakayama background remains an accepted
   source input, not a newly verified kernel theorem.

Thus the ordinary rank-two theorem applies with a=2e to actual Type-II
points with psi=1 and GD, subject to the already accepted `CohInp`
source convention. A unit of `B_{1,eta omega^{2e}}` excludes these
points directly. No modular attachment is needed for this particular
deduction.

## Bare admissibility is weaker

`../unitary_audit/source/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/AutomorphyLifting/AutomorphyDescent/AutNewformW.lean:14–20`
defines `Adm2A`. It asserts the existence of an irreducible W, a weight
2e+1 newform attachment after its specified twist, `WitAQ`,
`Level(e,-e)`, a weight-zero determinant, and an isomorphism of the
three-dimensional system to `W|G_E` plus a trivial middle summand.
It does not itself assert the residual pair or determinant eta.
The stronger source conclusion above belongs to the actual Type-II
point construction, not to every member of this larger ambient
admissibility class.

## Final appended corollary check

The final corollary includes every source restriction audited above: an
actual IsLocPt specialization, GD, N=2, psi=1, and the accepted CohInp
source convention. It explicitly retains the odd discriminant required
by this actual N=2 source. In particular it cannot be applied directly
to the even-discriminant D-plus/D-minus family without a separate source
construction. The generic rank-two exclusion itself permits those even
discriminants whenever its independent representation hypotheses hold.
The added finite-image/socle argument justifies semisimple restriction
in the restriction variant. All final proofs pass; no new kernel claim.

Final reviewed TeX SHA-256: `dbf0385112c0ad125e3372b1ac10bb45051fd6c1a7e2d40f0925cd3a745d7d0d`.
