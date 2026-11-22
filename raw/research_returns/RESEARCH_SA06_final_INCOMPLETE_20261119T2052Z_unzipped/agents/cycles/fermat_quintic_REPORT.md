# C.3au: the rational top quotient of the complex Fermat quintic cone

**Proved in the stated restricted scope. No main-gate reset.**

Let V be the specified Fermat quintic surface over C, L=O_V(1), and X the puncture of the strict henselization of its affine cone at the vertex. Let Z be the regular cone resolution. For ordinary algebraic equivalence using actual fixed products, B²(Z)_Q is Q by degree on the exceptional surface, and B²(X)_Q is zero.

The result goes beyond the vanishing of relative differentials: although q(V)=0, the first infinitesimal neighbourhood has the nonzero absolute coefficient group H²(V,L) tensor Omega¹_C/Q. This group is not declared zero. A specified degree-five morphism from a blow-up of a product of two plane quintic curves supplies enough actual Picard products to generate it after proper pushforward.

The proof constructs any chosen Picard first jet as an actual line bundle, using formal existence followed by Popescu descent and smooth lifting over the henselian pair. A degree-fifteen curve map produces a finite fibre whose differential evaluations span the required cohomology. All complex coefficients are absorbed into actual Picard deformation parameters. The proper trace is checked by contracting the absolute Hodge class with minus a field derivation, wedging with a global simple-pole form, and taking residue and Serre trace. This proves the first-conormal trace formula with its exact sign and branch multiplicities. Finite K0 detection then eliminates the relative class, and localization gives the puncture statement.

The source line bundle is explicitly not assumed ample. The proof uses actual families on a fixed proper curve and does not algebraize an arbitrary formal K0 class, replace a pro-isomorphism by a fixed-level statement, or infer a theorem for an arbitrary complex quintic or isolated singularity. It gives no integral finiteness result.

## Artifacts

- `fermat_quintic_top.tex`: final complete proof; its historical draft is a comment-only pointer.
- `fermat_quintic_SOURCE_AUDIT.md` and `fermat_quintic_references.bib`: exact opened primary statements and normalization audit.
- `code/check_fermat_quintic_top.py`, `output/check_fermat_quintic_top.json` and `.out`: exact finite certificate, with actual runtime.
- `code/fetch_fermat_quintic_sources.py` and its JSON/stdout: full primary scans, SHA256 values and download runtimes.
- `code/compile_fermat_quintic_top.py`, `output/C3au_check.pdf` and compile JSON/stdout: reproducible standalone build.
- `fermat_quintic_results.csv` and `fermat_quintic_CHECK_EVENTS.tsv`: scoped row and actual checks.

The author's complete proof/source audit and the independent root audit passed. Root's full certification receipt is 2026-11-19T11:27:59.592062UTC, recorded in `notes/ROOT_C3au_FERMAT_AUDIT.md`. No novelty or independent-model claim is made.

Final registration: 2026-11-19T11:32:10.709394+00:00; one row and eleven actual events. Final renamed standalone build completed 2026-11-19T11:30:55.609918+00:00 in 2.8770777600002475 seconds, with no diagnostics.
