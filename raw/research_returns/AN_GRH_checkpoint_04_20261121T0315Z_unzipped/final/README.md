# AN_GRH final package

The main deliverable is the standalone **AN_GRH.tex**, accompanied by a compiled PDF. It contains the complete checked A1 reconstruction, explicit theta obstructions, prime-power and composite primitive-factor sufficient conditions, exact examples of degrees 13, 15 and 4159, a Lang–Weil test and its limitation, a conditional Hooley–Lenstra family of candidate orders, generic avoidance at every odd order, finite-field avoidance for any fixed finite prime support, an all-extension obstruction to the older quotient test, finite GT certificate proofs, effective Galois bounds, source audit, exact references, and a separate part for unchecked inputs and remaining gates.

## Result status

- **A1:** proved without number-field GRH, by the recovered cuspidal/configuration argument.
- **Requested proof through Hooley:** not established. A06 refutes the universal primitive-root theta bridge. A11 weakens the sufficient condition to an odd prime power n with an exact-order-n theta point and <2,-1> = (Z/n)^×. A15 and A18 allow any odd conductor for a geometric primitive-rank-zero cover, in every genus at least two in characteristic two. For genus two this is equivalent to theta meeting every primitive doubling orbit of the same cyclic torsion subgroup, and A18 removes the elliptic-double-quotient exception. This universal finite-field incidence or orbit-coverage question remains open. Under M, A17 supplies candidate orders 3q for a family of primes of density Artin constant/2; it does not supply theta incidence.
- **Positive-rank progress:** A07 refutes prime-order incidence for generic curves over finitely generated fields, with transcendental moduli. A08 proves that no fixed finite prime list works for all finite-field curves of rank one or two; the ordinary case excludes any fixed finite list of odd degrees. A09 gives an exact order-13 theta point and a pointed degree-13 cover on a rank-one curve. A10 excludes order three on every nonordinary genus-two base. These statements keep their different quantifiers and ground fields.
- **Further concrete tests:** A12 gives an unconditional Lang–Weil lower bound for theta points in a prescribed rational subgroup. A13 certifies at least four exact-order-4159 theta points on an ordinary curve over F128. A14 proves that the sufficient numerical test eventually fails at any one fixed odd prime; it does not prove absence of theta torsion. A16 gives an exact order-15 rank-one example whose primitive factor has rank zero while the proper-conductor factors have positive rank. A15 still separates points in that example.
- **Finite search at fixed prime support:** A19 proves that all geometric theta points supported on a fixed finite set S of odd primes lie in F_(Q^d), where Frobenius^d fixes J[ell] for every ell in S. Thus every exponent can be covered by a terminating finite computation. A20 applies this to the A09 curve and proves that it has no nonzero theta point of any order 3^a, although it has the exact order-13 witness. The remaining family of possible prime supports is unbounded. A21 proves generic avoidance of all nonzero odd torsion in both positive-rank strata. A22 proves that every fixed finite pool of odd primes fails uniformly over finite fields, even allowing all powers and products; such avoidance examples occur in every nonempty moduli open.
- **All-extension numerical obstruction:** A23 proves that the ordinary A13 curve viewed overF4 defeats the older B.3 prime-quotient size inequality over every constant extension and for every prime divisor. Its existing theta witness persists. Thus strengthening prime-distribution input cannot universally force that particular sufficient test.
- **Frobenius and pairing restrictions:** A24 excludes every inert eligible prime power for the ordinary A13 curve; its surviving split-prime candidates still have the separately proved positive density under M. A25 shows that successful large-prime A12 tests have rational r-torsion rank at most two, with explicit cutoffs and a necessary Q^(3/4) prime scale. These restrictions concern the stated curve or numerical tests, and leave universal incidence open.
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

The A13 checks use the standard library, with independently computed recurrence and Sylvester-determinant group orders. The A15 unit-group checks also use the standard library:

```sh
cd certificates/A13
python lang_weil_4159_certificate.py
python verify_ordinary_4159_independent.py
```

```sh
cd certificates/A15
python check_A15_units.py
```

The A16 Taylor producer and finite search use the standard library. The independent norm verifier uses SymPy and imports no producer arithmetic:

```sh
cd certificates/A16
python construct_theta15.py
python verify_theta15_symbolic.py
python search_theta15_F8.py
```

The finite search records the specified models and points tested; it is not a classification up to isomorphism or a universal existence proof.

For A20, the producer uses a four-dimensional integer companion matrix, the independent verifier uses a polynomial resultant, and a separately written check uses Newton power sums:

```sh
cd certificates/A20
python check_three_primary.py
python verify_three_primary.py
python A20_recurrence_check.py
```

Only the second command requires SymPy. A19 supplies the geometric finite-support reduction used with these exact computations.

The optional A23 recurrence cross-check uses the standard library:

```sh
cd certificates/A23
python verify_A23_recurrence.py
```

Its finite range is an arithmetic cross-check. The paper proves the all-extension inequality symbolically.

The optional A24 and A25 checks use the standard library:

```sh
python certificates/A24/check_A24_orbits.py
python certificates/A25/verify_lang_pairing_cutoffs.py
```

A24 proves the inert-prime-power obstruction uniformly without relying on its small-prime consistency checks; A25 proves the entire cutoff ranges after the exact anchor comparisons.

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
