# Standalone build and verification

## Current artifact

**Sharp residues and hypersurface monodromy, after Grothendieck and Katz** has **49 pages**. The fresh source-only build completed at 2026-11-23T12:26:16.834841+00:00. The PDF has 613,491 bytes, no overfull boxes and no undefined references or citations.

| File | SHA256 |
| --- | --- |
| `auxiliary_lemmas.tex` | `166dea8f85d5725374cf5f26345762912eb663bacd6f1d706b9d8aae3b172a03` |
| `characteristic_three.tex` | `710fe27061bbe0e58864776e6444d57c4c125cce96de478d40521ea32b64efd6` |
| `characteristic_three_higher.tex` | `c48850765ac911c606e7443e8a328b7d111c7099a98300ce5cd321b410d14fc5` |
| `characteristic_two_higher.tex` | `64aeb5af58964be15b6503d72b36602f9a3aa26aac95a010267f8d291479320c` |
| `higher_monodromy.tex` | `f545e159e378e8bc3224fc56eacdb77ff1e9dd0429ca68dd8be3fce9cd2d185b` |
| `main.tex` | `230f2ee4aea1f60d0651d2181181819642c0adca7f9501191834daf637595018` |
| `main.pdf` | `959384204f4380c5d270b01f36622fa63767ef810a396325def1f1679b29e894` |

## Standard TeX build

Keep the six TeX source files in the table together. The bibliography is embedded in `main.tex`; no image, bibliography database or third-party source file is required. A standard TeX installation with the packages in the preamble suffices. From this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The recorded build copied only these source inputs into an empty directory before running three passes. Exact evidence is `audit/paper17_auxiliary_public/build_final03.json`. Environment-specific format repair is an audit detail, unnecessary on a normal TeX installation.

## Full readings and pages

Two cumulative complete readings passed. The CP13 mathematical text has its previously completed expert and newcomer readings; byte comparison confirms that all four proof fragments are unchanged and that main.tex changes only its method note, appendix inclusion and three references. The entire new appendix, changed closing text and references received expert and newcomer readings. The latter found the need to define the indexed ordinary opens, local systems and images; that clarification and the diagonal sign subgroup were reread in the final source and render. No claim is made of two fresh end-to-end readings of all 49 pages.

All 49 final03 page images were viewed on 13 numbered contacts and passed. Root separately read the full appendix, both clarity changes and the complete main.tex diff; it viewed all final02 pages and all changed final03 pages, with exact image identity for pages 1–45. Exact scope, continuity, individual image hashes and the final root record are in `audit/paper17_auxiliary_public/final_readings_and_QA.json`. There are no overfull boxes or undefined citations/references.

## Computational supplements

Python 3 and its standard library suffice. From the workbench root:

```sh
python papers/paper17/projective_frobenius_formula_checks.py
python programs/hypersurface_higher_monodromy_checks.py
python programs/small_characteristic_hypersurface_checks.py
```

The original formula program covers point counts, semilinear iteration, the characteristic-two covector, Deuring-polynomial gcds and first-degree coefficient positions. Its prior successful output has 280 point-count and 280 iteration comparisons, 188 covector comparisons, 25 polynomial gcds and 15 distinct-entry checks; the unchanged program SHA256 is `76e02f8980211a0dfea8f9c29b9e1b42a12c8ee6534e06b267a0fa046bf994a9`.

The higher-prime/seed program covers 30 exterior cases, 666 overlap instances, 10 characteristic-three seed dimensions, 8,245 minor entries and 44,989 high-high monomial pairs. Its unchanged SHA256 is `facb8dc48ef35c1e015e9490074bff791f0ad424dd165dd23b9159b3d7aa1f06`; its exact earlier record is `audit/paper17_higher/program_record.json`.

The small-characteristic program SHA256 is `dd7cb886be106dfc1887098329001b99cab86cbab75749f18060d16bab4647fd`. Its successful combined output verifies 104 elliptic coefficient cases, 7,305 characteristic-two cochain identities, local stabilizer orders 24 and 1,344, the first higher group order 20,160, 94 characteristic-three norm lifts, 6,930 signed clique centres and 322 elementary words. Exact output SHA and limits are `audit/paper17_small_characteristics/program_record.json`. All these calculations are finite corroborations; universal conclusions follow from the written proofs.

The separate quartic program `programs/plane_quartic_schreier_checks.py` uses orbit-stabilizer lengths 26, 24, and 9 and determinant-one enumeration, agreeing with the author's full-matrix enumeration at order 5,616. Its distinct-method credit is restricted to that finite calculation.

## Mathematical check scope

The residue theorem, independent cubic-boundary image, determinant consequence, plane groups, higher p>=5 groups and characteristic-three first-degree seed retain their completed separate same-model reconstructions and full comparisons. The new higher characteristic-three proof has a 351-line statement-led reconstruction and separate 233-line root derivation, fully compared. The new higher characteristic-two proof has 234-line author, 244-line root and 793-line further-worker reconstructions, all fully compared. Exact admitted inputs and related prior exposure are disclosed; no globally pristine or different-model independence is claimed.

The finite projective-hypersurface images are now determined for every prime, n >= 2, d >= 1 over every perfect ground field. The sixteen original auxiliaries in the recorded inventory now have complete targeted comparisons at their named published/common-geometry inputs. Seven have new full public appendix proofs, seven public conclusions were already covered, and two are classical Peel statements. These categories add no independent-main credit, and a public consequence does not certify its original geometric route. Other original source statements remain subject to their own exact records. No human checked the mathematics. New text and original code are CC0 1.0. No external publication or deposit occurred.

Recorded: 2026-11-23T12:31:32.861553+00:00.
