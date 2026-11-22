# Independent whole-proof audit of HD-SPIN-01a/b

**Outcome: PASS.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro, inherited/unexposed effort, run HODGE_DIVISION, 2026-11-21 approximately16:27–16:32 UTC. Entire root-owned `research/spin_core_obstruction.tex` read without editing it. Audited SHA256: `e0180456a1372b455672b31a13d045e52c92604f010da5f3d223a07e7deebcc7`.

The exact published primary input was reopened at https://ems.press/content/serial-article-files/31824?nt=1: Guralnick–Tiep, JEMS14(2012),605–657, DOI10.4171/JEMS/313. I read the complete Lemma2.23 proof on p621 and the complete first spin paragraph of Proposition3.4's proof on p626. The latter page was also visually checked to confirm the minimum-degree exponent floor(n/2)−1. The argument uses the unrestricted local2.A6 character-ratio fact and the general spin-degree lower bound explicitly stated within those proofs; it does not import Proposition3.4's extra age hypotheses.

## Universal proof

The scalar centralizer and perfectness identify every normalizing element's projective action with an automorphism of A_n. For n≥8 this is a permutation. A nonidentity permutation fails to centralize some3-cycle, and the resulting commutator projects to a nonidentity even permutation on at most6 letters. Its lift lies in the natural2.A6 subgroup and is noncentral. The central involution acts as−1 in the faithful spin representation, so every irreducible restriction constituent is faithful. The published local trace estimate therefore sums to |trace(h)|≤a/2. Rotating a maximal eigenvalue gives nu(h)≥a/4; the exact rank inequality for a commutator, after scalar adjustment, gives nu(g)≥a/8. All statements also hold for finite order up to scalars.

The factor-algebra normalizer and weighted tensor-cycle argument are the already fully checked D-SPOR03 argument and apply independently of sporadic type. Factorwise elements retain the one-eighth bound; factor permutations satisfy the stronger quarter bound. Actual scalar inertia has full moving rank. Two nontrivial bilinear multipliers move at least ceil(e/2), and the other ten genuine inertias move at least ceil(e/8). The continuous inequality forces e≤24, while D-BI09 applies with all its primitive, nonsplit and larger-field hypotheses and gives e≥24. Thus e24 is the only possible endpoint. Two spin factors already have degree at least64, and the general minimum excludes n≥12.

The multiplier restricts trivially to the perfect remaining core, so its irreducible representation must be self-dual. The only actual degree24 rows among2.A8–11 are the nonreal pair in2.A8; this is a contradiction. The proof appropriately leaves nonselfdual spin cores, ordinary alternating cores and n<8 outside its scope.

## Independent exact finite check

`audit_spin_inputs.py` reads the full five-table export with SHA256 d41d9bcb33344ce8d655dd83aa90f4a58ffc4f00a5cd22271c72895c22e7d26c. It uses this reviewer's independent integer-polynomial and Ramanujan-trace arithmetic from `audit_sporadic_input.py`, not GAP or the author's check implementation. It identifies each central involution from class order and class size, independently selects the center-negative rows, and verifies the full faithful-degree lists.

All66 noncentral entries of the6 faithful2.A6 rows satisfy the exact trace-half inequality. The2.A8 degree24 rows are16 and17, with nonreal values on classes16–19. The checker recomputes their Frobenius–Schur indicators from the square map and obtains0, verifies that every value lies in Q(b7), and checks b7²+b7+2=0 exactly. A nonreal entry proves that this field is precisely Q(sqrt(-7)). There are no degree24 faithful rows in2.A9,2.A10 or2.A11.

The exact ceiling budget on9≤e≤24 admits14,15,16,24; after D-BI09 it leaves only24. My first implementation contained an incorrect hand-entered expected list for this auxiliary check and stopped at that assertion after all character checks had passed. I corrected the expected list and reran the complete checker successfully. This was a reviewer certificate assertion error, not a defect in the written proof, which uses the valid continuous bound followed by D-BI09. The failed check is retained in the event log.

Full exact output is `audit_spin_inputs.json`. Published character tables and their identification with the named groups remain explicit inputs; the review does not reprove these tables or the general minimum spin-degree theorem.


## HD-SPIN-02a/b complete strengthening

**Whole-proof outcome: PASS**, 2026-11-21 about16:36–16:39 UTC. I read every line of the128-line `research/spin_quarter_obstruction.tex`, SHA256 `66a78151ba633fd7d494704e7847de9f43315e4f2a759b4927800442014e6a8e`. The proof correctly strengthens the normalizer bound to one quarter and removes the self-duality and nonsplit-polarization hypotheses.

My fresh `audit_spin_half.py` reconstructs every cyclic multiplicity on all66 noncentral entries of the6 faithful2.A6 rows, using the independent Ramanujan-trace implementation. In every row the smallest ratio nu/degree is exactly1/2. I separately compared every entry of the displayed SPINQ.2 maximum-multiplicity table with my output, all66 matching exactly. The full certificate is `audit_spin_half.json`.

For a fixed eigenvalue, multiplicities add across a reducible restriction. Thus the local half-dimensional eigenspace estimate is valid on the entire restriction, with no need to align eigenvalues or use a character triangle inequality. The support-six commutator gives nu(g)≥a/4. The already audited factor-normalizer and weighted tensor-cycle argument extends this to all nonscalar elements of an irreducibly acting normal central product of spin factors. Every genuine scalar inertia has full moving rank. Since every factor degree is at least8, the intermediate-cover genus argument and twelve-branch necessary condition give3e≤2e+6 with e≥8, a contradiction.

The statement is correctly scoped to the actual six-dimensional multiplicity variation of a Weil sixfold source. It handles all compatible outer automorphisms, factor permutations and larger inducing fields; no primitive, ESD or determinant hypothesis is used beyond the stated normal irreducible spin-core assumption. It still leaves ordinary alternating cores and exceptional covers with alternating degree below8 open. No issue found.
