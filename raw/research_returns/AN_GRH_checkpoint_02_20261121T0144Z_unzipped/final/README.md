# AN_GRH final package

The main deliverable is the standalone **AN_GRH.tex**, accompanied by a compiled PDF. It contains the complete checked A1 reconstruction, explicit theta obstructions, a weaker prime-power sufficient condition and a degree-13 positive-rank witness, finite GT certificate proofs, effective Galois bounds, source audit, exact references, and a separate part for unchecked inputs and remaining gates.

## Result status

- **A1:** proved without number-field GRH, by the recovered cuspidal/configuration argument.
- **Requested proof through Hooley:** not established. A06 refutes the universal primitive-root theta bridge. A11 weakens the sufficient condition to an odd prime power n with an exact-order-n theta point and <2,-1> = (Z/n)^×. This finite-field incidence question remains open on the positive-rank locus.
- **Positive-rank progress:** A07 refutes prime-order incidence for generic curves over finitely generated fields, with transcendental moduli. A08 proves that no fixed finite prime list works for all finite-field curves of rank one or two; the ordinary case excludes any fixed finite list of odd degrees. A09 gives an exact order-13 theta point and a pointed degree-13 cover on a rank-one curve. A10 excludes order three on every nonordinary genus-two base. These statements keep their different quantifiers and ground fields.
- **GT certificates:** proved for every identified modulus and the stated infinite families; 53 explicit moduli and 4,825 unit words checked. T07 also gives the exact LLS criterion and the conditional large-modulus threshold exp(300).
- **Effective Galois bounds:** proved under precisely stated analytic assumptions; M-dependent results remain conditional on Masullo's draft claim. The actual LM8 factors have the explicit bound ell>964 log6+5760 over Q under M, and a separately stated unconditional adelic-index bound.
- **Exhaustive historical audit:** INCOMPLETE because two complete registers and most LM7 proof blocks were not recovered. Every supplied flag and every recovered row is represented.

## Required files

AN_GRH.tex, QUESTIONS.tsv, LEDGER.md, CHECK_EVENTS.tsv, IMPLICATIONS.md and TRANSCRIPTION_NOTES.tsv are all at the root. The additional ROW_* and GT_* tables contain the detailed evidence behind the paper. Original register status is preserved as metadata, not treated as a proof check.

The source-specific paper locators refer to retained files under `source/` and `recovered/`. Large original archives and downloaded external research PDFs are excluded. SOURCE_RECOVERY_MANIFEST.tsv identifies exact source versions by hashes. The checked section sources are retained in `proof_sources/`; the main TeX file contains them inline and needs no external section files.

## Reproduce the arithmetic

The GT and short A06 checks use Python 3 and only its standard library:

```sh
cd certificates/gt
python verify_gt_units.py
python check_unit_certificates.py
python check_lls_bound_scope.py
```

```sh
cd certificates/A06
python check_theta_obstruction.py
python verify_theta_small_independent.py
python check_a06_prime_orbit_independent.py
```

The B.23 polynomial and supplementary curve-geometry checks require `python-flint==0.9.0` (the version used in this run):

```sh
cd certificates/B23
python primitive_conductors.py
python primitive_verify.py
```

```sh
cd certificates/A06
python check_b23_geometry.py
```

Run regenerating scripts in a working copy if the delivered logs and data should remain unchanged. The supplied B.23 binary coefficient arrays and manifests are complete; the verifier checks both full Bezout identities at 191 and 229. The new A06 proof itself needs only the small arithmetic checks, not the large Bezout certificates.

The A09 direct producer and point-count checker use the standard library. Its independently written polynomial verifier also uses SymPy:

```sh
cd certificates/A09
python theta13_direct.py
python verify_theta13_norm.py
python check_base_counts.py
```

## Build the paper

With an ordinary XeLaTeX or LuaLaTeX installation containing standard AMS, longtable, fontspec, Latin Modern, microtype, hyperref and enumitem packages:

```sh
lualatex AN_GRH.tex
lualatex AN_GRH.tex
```

`python reproduce/assemble_paper.py` rebuilds the standalone source from `proof_sources/`. The initial missing-format failure was resolved by using the installed XeTeX toolchain with process-local search paths and an isolated format. `reproduce/compile_standalone_tex.py` records that environment-specific build procedure. No packages or fonts were installed, and no system configuration was changed.

The compiled paper and visual checks are recorded under `evidence/build/`; the manifest binds the checks to exact TeX and PDF hashes. Structural validation also checks included-source completeness, citation keys, finding/check-event coverage and retained-source hashes. Compilation and visual inspection are separate from mathematical proof checking.

## Verification convention

CHECK_EVENTS.tsv records what actually happened. A whole-proof reading is not a formal certificate. A replay of an earlier independently written verifier is not a new independent implementation. Source-statement inspection is not a reproof of a cited theorem. Alpöge's theorem is accepted as instructed; the Lean archive was not rebuilt. Masullo's all-field Hecke-GRH claim is conditional, and its intended final theorem heading 13.3.1.2 has no statement in the supplied draft.

Original handwritten scans were not provided. TRANSCRIPTION_NOTES.tsv distinguishes mathematically forced notation/typing corrections from possible authorial lapses, conventions and items requiring visual confirmation.
