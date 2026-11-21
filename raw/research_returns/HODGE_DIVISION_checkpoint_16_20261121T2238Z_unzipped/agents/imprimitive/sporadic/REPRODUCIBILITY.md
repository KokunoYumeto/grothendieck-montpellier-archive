# Sporadic normal-core certificate and provenance

## Mathematical result and review

`sporadic_core_section.tex` contains D-SPOR-01–03 in full. Every nonlinear irreducible representation of every universal sporadic cover, and every irreducible outer extension whose restriction is irreducible and nonlinear, has largest nonscalar eigenspace of dimension at most three quarters of its degree. The proof extends this bound to arbitrary scalar normalizers and normal central products with factor permutations. The actual Hurwitz rank factorization then excludes such an irreducible normal core in a dominant Weil sixfold source. The inducing field need not equal the original quadratic field, and the conclusion does not require nonsplitness.

The parent independently read the complete proof and programs and reran the standalone verifier: PASS, 3,035 selected rows and 473,972 nonscalar entries, 12 Fourier fallbacks, 0.464 seconds. The sibling `/root/g34_eightfolds` independently read the whole proof and sources and reconstructed the entire calculation using integer-list cyclotomic arithmetic, restriction inner products computed by normalized traces, and Ramanujan-sum Fourier multiplicities: PASS with the same counts in 0.8 seconds. Its report and executable are retained in `agents/g34_eightfolds/bireflection/SPORADIC_CORE_PEER_AUDIT.md` and `audit_sporadic_input.py/.json`. These are independent mathematical and computational checks; no proof assistant was used.

## Complete retained mathematical inputs

- `character_inputs.json`: every character, class size/order, stored prime power map, source string, and relevant subgroup fusion for all 38 tables. SHA-256 `c2268f05043ed29a9048d5fe7d55b1a096e5c8615fa049b3438cca088f703edb`, 2,472,924 bytes.
- `coverage.json`: all 26 simple sporadic groups, their multiplier and outer-group metadata, universal covers, and the 12 needed outer extensions.
- `alternating_cover_inputs.json`: separate complete tables for 2.A6 and 2.A8–11, including power2 maps and source strings. SHA-256 `d41d9bcb33344ce8d655dd83aa90f4a58ffc4f00a5cd22271c72895c22e7d26c`, 24,596 bytes. This supports the parent's separately scoped essentially self-dual spin result; it is not needed for D-SPOR-01–03.

Character values are exact integers or pairs `[n, coefficients]` representing an integer polynomial in the primitive nth root of unity. Complete table data are retained rather than only selected successful inequalities. All 38 sporadic tables identify their origin as the published *ATLAS of Finite Groups*. The stored ambiguity in the third-power map for 3.McL is documented by the source; no Fourier fallback uses that table, so this ambiguity does not affect the proof.

The table identification, Schur multipliers and outer automorphism groups are published mathematical inputs. Exact row orthogonality is a consistency check and does not by itself establish those identifications. No new reconstruction of the sporadic groups or their complete character tables is claimed.

## Executable certificates

The scripts use paths relative to the workspace root unless noted otherwise.

1. `scan_quarter_bound.g` performs the full GAP scan. The successful corrected run took 4.445 seconds. Its exact norm bound uses GAP's canonical cyclotomic basis and requires 24 Fourier fallbacks, all in 2.J2.
2. `export_inputs.g` exports the complete inputs and verifies exact full row orthogonality and the degree-square sum for every table. The successful run took 4.381 seconds.
3. `verify_quarter_bound.py` reads only the retained JSON, independently selects the relevant outer rows, and verifies the bound in integer polynomial quotient rings using SymPy and python-flint. It runs without GAP. The author's separate arithmetic run passed in 0.513 seconds. Its different cyclotomic basis needs only 12 Fourier fallbacks, also all in 2.J2. This differing count is expected; the underlying exact inequalities and complete coverage agree.
4. `small_spectra.g` records all exact eigenmultiplicities in the selected minimal examples, including degrees 24 for 2.Co1, 28 for 2.Ru, 18 for 3.J3, 12 for 6.Suz, and 6 for 2.J2. These examples illustrate the full bound and are not its coverage argument. The minimum degree of 2.Suz itself is 143; the degree-12 example belongs to 6.Suz.
5. `export_alternating_inputs.g` supplies the separate complete spin inputs, verifies their full orthogonality, and computes the degree-24 indicators directly from the square map. The two degree-24 rows of 2.A8 are nonreal conjugates with indicator zero; there is no faithful degree-24 row in 2.A9–11.

Example standalone command from any working directory:

```bash
python /workspace/scratch/796f50e61a8b/HODGE_DIVISION_work/agents/imprimitive/sporadic/verify_quarter_bound.py
```

The successful environment used Python 3.12.14, SymPy 1.14.0 and python-flint 0.9.0. The local GAP executable is `cache/gap-4.16.1/gap`; use flags `-q -A -T`, from the workspace root, to run the GAP scripts. The independent sibling arithmetic uses neither GAP nor this verifier's implementation.

## Retrieval and build

`retrieval_manifest.json` retains official URLs, downloaded byte counts and SHA-256 hashes for GAP 4.16.1, CTblLib 1.3.11 and the required supporting packages. The GAP core hash was checked against the official release metadata. The CTblLib archive hash was calculated locally and is not described as a publisher-supplied checksum. GAP was configured with `--with-readline=no` and compiled with `make -j4`; both completed successfully.

The full third-party runtime and archives are temporary dependencies in the directory named `cache` and are excluded from the deliverable. Complete compact mathematical tables, authored scripts, outputs, retrieval hashes and proof files are retained outside that directory.

## Honest execution notes

The first local GAP startup failed because mandatory supporting packages were absent; official packages were installed and the successful runs used the unmodified package machinery. The first arithmetic scan passed but GAP's default pretty-printing inserted line continuations in the JSON output; output formatting was disabled and the full scan was rerun to produce valid JSON. The first table export stopped on a reserved global name; that author-program identifier was renamed and the export rerun with abort-on-error. These preparation errors are not counted as successful checks.

## Primary source locators

- Conway, Curtis, Norton, Parker and Wilson, *ATLAS of Finite Groups*, Oxford University Press, 1985: named sporadic tables and their Schur covers and outer extensions, with exact electronic identifiers retained in the JSON.
- Author-maintained CTblLib archive and manual: <https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/>. Manual Section 3.7-3 explains `ExtensionInfoCharacterTable`, including multiplier and outer-group metadata and universal-cover identifiers; Section 3.7-6 explains the ATLAS provenance marker. The parent also checked Section 3.7-5. The complete table source strings are retained.
- GAP official release: <https://github.com/gap-system/gap/releases/tag/v4.16.1>. `EigenvaluesChar` implements the cyclic Fourier multiplicity identity; that identity is proved explicitly in D-SPOR-01 and separately implemented in both independent verifiers.
