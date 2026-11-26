# Building this paper

The project is standalone. `main.tex` contains the principal text, definitions and references and inputs `action_colimits.tex`, `action_colimits_statement.tex`, `canonical_ideal_core.tex`, `canonical_ideal_limits.tex`, `canonical_ideal_projectives.tex`, `canonical_ideal_statement.tex`, `decision_obstruction.tex`, `entire_support_projectives.tex`, `entire_support_statement.tex`, `exchange_lifting.tex`, `exchange_lifting_statement.tex`, `finite_coefficient_models.tex`, `finite_coefficient_statement.tex`, `finite_frame_ideal.tex`, `finite_frame_statement.tex`, `finite_group_projectives.tex`, `finite_group_statement.tex`, `finite_lattice_projectives.tex`, `finite_lattice_statement.tex`, `finite_semiring_projectives.tex`, `finite_semiring_statement.tex`, `further_foundations.tex`, `general_ringoid.tex`, `integral_support_reduction.tex`, `integral_support_statement.tex`, `local_unit_projectives.tex`, `local_unit_statement.tex`, `tensor_picard.tex`, `uniform_coefficient_category.tex`, `uniform_coefficient_statement.tex`, `upper_idempotent_quotient.tex`, `upper_idempotent_statement.tex`, `upper_jacobson_quotient.tex`, `upper_jacobson_statement.tex`, `upper_levitzki_quotient.tex`, `upper_levitzki_statement.tex`, `upper_semiperfect_amplitudes.tex`, `upper_semiperfect_statement.tex`, `upper_transition_radical.tex`, `upper_unit_quotient.tex`, `upper_unit_statement.tex`. All 42 TeX files must remain in the same directory. There are no local figures.

Engine: pdfLaTeX (tested with pdfTeX 1.40.26, LaTeX 2024-11-01). Standard packages: `amsart`, `amsmath`, `amssymb`, `amsthm`, `mathtools`, `geometry`, `lmodern`, `microtype`, `xcolor`, `hyperref`, and `xurl`.

From a fresh copy of this directory, run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The output is `main.pdf`. The checked build has 71 pages, no undefined references or citations, and no overfull boxes. The execution host required a local TeX format repair; no nonstandard package or project-specific format is required on a normal TeX Live installation.

The accompanying program collection is called **Finite inverse-semiring checks** in the paper. The independent finite checks run from the workbench root with:

```sh
python3 programs/paper1_exhaustive.py --output checks/paper1_certificate.json
```

Expected principal counts: 3, 41, and 1,399 idempotent matrices among all matrices of sizes 1, 2, and 3 over `(F_2)_0`; all tested images satisfy the predicted distributive-lattice and fiber-dimension conditions. Congruences of `(Z/n)_0` for `1 <= n <= 7` number `2, 4, 4, 6, 4, 8, 4`. All ideals are checked for `1 <= n <= 12`. These finite computations supplement, and do not replace, the proofs.

The intrinsic repeated-adjunction classification is checked independently by:

```sh
python3 programs/paper1_iterated.py --output checks/paper1_iterated_certificate.json
```

Expected counts: over the three-element max–min chain, ranks 1, 2, 3 give 3, 46, 1,929 idempotent matrices; over the four-element chain, ranks 1, 2 give 4, 130. Over `(F_2)^[2]`, ranks 1, 2, 3 give 4, 123, 11,933 idempotents. Every finite image is checked for the required positive-colour truncations, top-colour group labels, additive dimension formula and injective transports.

The two-idempotent square-zero reduction has a separate exhaustive check:

```sh
python3 programs/paper1_two_level.py
```

It writes `checks/paper1_two_level_certificate.json`. For R=A=Z/4 and f(a)=2a, ranks 1 and 2 give 3 and 231 idempotent matrices upstairs and 3 and 119 after replacing A by its image ideal. Every quotient idempotent is lifted by the explicit correction polynomial; explicit rectangular intertwiners identify all lifts of the same idempotent. The injective-case fibers are verified as inverse images of their reduced flags, with bottom group IP.

The finite distributive support classification has a separate matrix-image check:

```sh
python3 programs/paper1_finite_lattice_projectives.py
```

It writes `checks/paper1_finite_lattice_certificate.json`. The program exhausts ranks 1 and 2 over six support posets (empty, one point, two incomparable points, the two three-point forks, and the four-point diamond), with coefficient rings zero, F_2 and F_3. All 19,152 matrices are enumerated; 6,402 are idempotent. The recovered images satisfy the color truncations, admissible-ideal condition, quotient-label dimension formula, and injective transitions, with zero failures. There are 1,038 nonprincipal nonzero-label occurrences, including 22 empty-poset ordinary-ring boundary cases. The image and fiber data are computed directly from matrices rather than constructed from the classification.

Historical checkpoint 14 source/PDF: fresh two-pass build `build/paper1_fresh_0026`, copied from exactly the twenty-nine required TeX sources into an otherwise empty directory. All 56 pages were rendered and inspected in seven contact sheets; new statement page 9, proof/example pages 31–32 and the rewritten open-problem discussion page 53 were displayed individually. Theorem 1.14 and §7.8 give detection at upper multiplicative idempotents (SZ1-089–091), its n+1 fixed-matrix-fiber bound and finite-projective-class invariance. Example 7.16 proves strictness over the earlier upper-unit quotient and explicitly separates global nonnilpotence from fixed-fiber nilpotence. Theorem 1.13 remains the earlier unrestricted quotient; Theorems 1.15–1.16 retain the integral and local specializations. No warning, overfull box or unresolved reference/citation occurs. Source/PDF and metadata synchronized at approximately 00:29 UTC on November 25; current hashes are in `checks/paper1_build.json`. That historical revision required twenty-eight local inputs; the current complete input list is at the top of this file.

The finite-group classification has a separately replayed finite check:

```sh
python3 programs/paper1_finite_group_projectives.py
python3 programs/root_finite_group_pair_replay.py
```

For `(F_2)_0[C_2]`, ranks1 and2 exhaust9 and6,561 matrices and give5 and235 idempotents. Their fixed birth quotients number2 and146, with1 and91 nonzero. Each satisfies `2 rank(g−1)=dimension`, the projectivity criterion over `F_2[C_2]`. Nonfixed birth points number4 and416. The author program enumerates actual semimodule images; the separate root implementation uses Boolean support matrices, binary amplitude column spaces and quotient ranks. The initial root replay preceded reading the author code. Complete image-size histograms also agree, with their later comparison chronology recorded in `checks/root_finite_group_replay_comparison.json`. These finite ranks and this coefficient ring are supporting checks, not substitutes for the theorem. No numerical counts were inserted into the frozen manuscript.


## Checkpoint 15 revision, 25 November 2026

Fresh directory `build/paper1_fresh_0049` began with the 31 required TeX sources. Two unchanged-source pdfLaTeX passes produced 58 pages, with no warnings, undefined references or citations, or overfull boxes. All 58 pages were rendered and visually inspected in eight contact sheets; pages 9 and 32–34 were additionally inspected individually. No layout defect was found. The live source files were compared byte-for-byte with the fresh-build sources before copying the PDF. The new material is Theorem 1.15 and its full proof: the compatible locally nilpotent quotient and finite-matrix compatibility (SZ1-092–095).


## Checkpoint 16 revision, 25 November 2026

Fresh directory `build/paper1_fresh_0119` began with the 32 required TeX files. Two unchanged-source pdfLaTeX passes produced 60 pages without warnings, undefined references or citations, or overfull boxes. All 60 pages were inspected in eight rendered contact sheets; the title/abstract page1, new proposition/proof pages34–35, and remaining-open page56 were also inspected individually. The source files byte-match the build copies. Proposition7.18 includes SZ1-096/097. The title now names Faul, Goswami, Joubert and Manuell; the abstract has234words. Olson–Jenkins global-semiring radical conventions are explicitly distinguished in Section7.9.


## Checkpoint 17 revision, 2026-11-25T02:13:48.335233+00:00

The checked final build uses the same 32 required TeX files, freshly copied to `build/paper1_fresh_0216`, and three unchanged-source pdfLaTeX passes. It produces 60 pages with no warning, undefined reference/citation, or overfull box. Theorem 1.10 now covers finite support semirings with semiperfect upper coefficient rings; Section 7.14 supplies the full proof and Example 7.19. The finite-total-semiring result remains a specialization.

All 60 pages were rendered and inspected in eight contact sheets of the first complete revision; pages 1, 6, 7, 38, 39, 40, and 57 were also inspected individually. A wording correction clarified that additive coefficient groups are abelian while coefficient rings may be noncommutative. The final build was fully rerendered: 59 page images byte-match those already inspected, and the sole changed page 7 was inspected again. No layout defect remains. Live sources byte-match every build input. The abstract contains 238 words.

PDF SHA256: `1ee98c0f901a464f8a3bc17460778114f575e4db30269ceaf0065131792a3f50`. Main source SHA256: `ac013a6cb4fd9a95bfba30be25f75d4f7bb368f4d12c17224fd61d619b14a641`.


## Checkpoint 18 revision, 2026-11-25T02:50:21.189438+00:00

Fresh directory `build/paper1_fresh_0248` contains all 36 required TeX sources, copied before three unchanged-source pdfLaTeX passes. The output has 64 pages and 786926 bytes, with no warnings, unresolved references/citations or overfull boxes. Live inputs byte-match all build copies. All 64 pages were rendered and inspected in eight contact sheets. Pages 1, 11, 12, 36, 37, 43, 44 were also inspected individually. No layout defect was found.

Theorem 1.18 and Section 7.16 classify amplitudes over arbitrary supports with semiperfect upper coefficient rings; the local specialization, diagonal alternative and polynomial action-ring boundary are included. Theorem 1.19 and Section 7.11 establish the compatible Jacobson quotient, its unconditional isomorphism-lifting scope, exact-support object lifting under semiperfect upper coefficients, and the ordinary semilocal-domain obstruction. Exact primary source distinctions separate this coefficient construction from global Jacobson–Bourne and simple-semimodule radicals. The abstract has 240 words.

PDF SHA256: `75a608831afc781c09f11c56bf906d77bd2c3b167fffc682286b74e009a9960e`. Main source SHA256: `0577804209b10fc9d271ababc85076f212421291f014854be5eefe17a8f1ac36`.


## Checkpoint 18 final synchronized revision, 2026-11-25T03:03:31.074174+00:00

Fresh build `build/paper1_fresh_0300` contains all 38 required TeX sources. Three unchanged-source pdfLaTeX passes produce 66 pages, 794947 bytes, no warnings, unresolved citations/references or overfull boxes. Every live source byte-matches its build input. All 66 pages were rendered and inspected through nine contact sheets; new theorem/proof/convention pages 12, 31, 32, 39, 45 were individually inspected. The preceding 64-page revision also received full-page and detailed new-page review. No layout defect remains.

Theorem 1.20 and Section 7.7 add the unrestricted exact finite coefficient-model theorem (SZ1-107), including the one-sided annihilator, the a² projector lift and every mixed-corner morphism. Theorem 1.18's proof is simplified to use these exact corners, without changing its upper-semiperfect hypothesis. Example 7.21 adds the independently checked distinction between the compatible Jacobson coefficient family, global Jacobson–Bourne radical and simple-semimodule radical (SZ1-106). The remaining 100–105 results and their scope limits are retained. The abstract is 259 words.

PDF SHA256: `a400cb452e8e388aa320f83967a01be87d5e95a0ed72ce7a8bcc052a10995d58`. Main source SHA256: `fd2587cda9925f8f9e923869f2d7980ff2323dcdc0faeb9d970cc77444e066d9`.


## Checkpoint 19 synchronized revision, 2026-11-25T03:38:09.761881+00:00

Fresh directory `build/paper1_fresh_0336` contains all 38 required TeX sources. Three unchanged-source pdfLaTeX passes produce 68 pages and 806393 bytes, with no warnings, unresolved references/citations or overfull boxes. Every live source byte-matches its build input. All 68 pages were rendered and visually inspected through nine contact sheets; new example/proof pages 32–33 and transition-test pages 40–41 were also inspected individually. No layout defect was found.

Corollary 7.22 adds the independently checked upward and two-by-two ordinary-ring tests for the compatible Jacobson ideal (SZ1-108), retaining noncommutative order and nonzero bottom coefficient fibers. Example 7.16 adds the independently checked fixed-finite-object restriction obstruction (SZ1-109). Its bicyclic construction has semisimple upper coefficient rings and pairwise nonisomorphic cyclic projectives on the same free support. It does not exclude every possible universal ordinary-ring construction. The abstract and principal theorems are unchanged.

PDF SHA256: `bb3c84a07141c7739001aa6814053aa0e5ca4d00b10df3b23d8305a1eea1ac98`. Main source SHA256: `fd2587cda9925f8f9e923869f2d7980ff2323dcdc0faeb9d970cc77444e066d9`.


## Checkpoint 20 synchronized revision, 2026-11-25T04:24:48.263794+00:00

Fresh directory `build/paper1_fresh_0430` contains all 40 required TeX sources. Three unchanged-source pdfLaTeX passes produce 69 pages and 816852 bytes, with no warnings, unresolved references/citations or overfull boxes. Every live source byte-matches its build input. All 69 pages were rendered. Nine contact sheets of the preceding same-layout revision were visually inspected, with pages1,13and42also inspected individually; a complete PNG-hash comparison proves that final pages2–69are pixel-identical. Final page1was separately inspected after the precise kernel wording correction, and final pages12,41and68were also individually reviewed. No layout defect was found. The comparison certificate is `checks/paper1_cp20_visual_comparison.json`.

Theorem1.21 (SZ1-110/111) lifts finite projective objects through every compatible coefficient quotient when all upper coefficient rings are exchange. Its full proof uses the finite-Peirce ordinary exchange criterion, the exact image ideal in a unital coefficient enlargement, and a one-square correction inside the prescribed nonunital matrix fiber. The compatible Jacobson quotient therefore preserves V and K0 under this broader hypothesis. The semiperfect multiplicity classification remains unchanged. The 267-word abstract and deposit abstract agree.

PDF SHA256: `b00163835d921802d215f92d122b94fe08ee79af7fccd542784334fa9b6c2520`. Main source SHA256: `752ac11a7b3d819416f293d0280001c83735a622136e1b56f169fab54218b6f4`.


## Uniform coefficient-category revision, 2026-11-25T05:33:24.080755+00:00

Fresh directory `build/paper1_fresh_0534` contains all 42 recursively required TeX sources. Three unchanged-source pdfLaTeX passes produce 71 pages and 830553 bytes, with no warnings, unresolved references/citations or overfull boxes. Every live source byte-matches its build input. All 71 pages were rendered and all nine contact sheets were visually inspected; pages1,13,15,34,35,36and67were also viewed individually. No layout defect was found.

Theorem1.22 (SZ1-112), stated on page13 and proved in Section7.8 on pages34–36, gives one coefficient category and explicit ideal for the entire fixed-support amplitude category. The proof preserves the covariant/opposite convention and repeated categorical objects. The abstract and proof overview explain the mechanism; Section15states that the classification of supports and ordinary ideal-generated projectives remains open. The 272-word abstract and deposit abstract agree.

PDF SHA256: `a79e379ad8769f991c116e84198f8aa3564fbb45992f54ddb5d19408b2f2428f`. Main source SHA256: `8476ab2e8bbf47d36b59e45cb2e73a2c009cef4f3548e68e0b3183da9cc31df0`.
