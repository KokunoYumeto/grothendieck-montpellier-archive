# Complete odd-C3 normal-core exclusion

The complete new proof is `csp6_section.tex`, D-C3-01–03. Its independently reviewed mathematical SHA-256 is `3aec637863bd7c2e7773af72805b518b3f909ab64d1235b9aeeed2a09f5116eb`; the canonical file subsequently changes only this audit-status paragraph. The author, parent and independent peer have read the entire proof and all invoked new arguments; mathematical checks pass. New statements are not being treated as published results.

**Conclusion.** An irreducibly acting normal central product of quasisimple groups with simple quotients PSp6(q), for arbitrary odd q≥3, cannot occur in an inducing block giving a rank-nine sixfold Weil period map. The theorem allows mixed field sizes, all compatible outer automorphisms, scalars and tensor-factor permutations, and arbitrary inducing character fields. It requires neither selfduality nor a fixed determinant.

## Proof content

The complete CSp6 table gives a quarter-character bound and nonlinear degree at least q³−1 for every odd q≥5. Clifford theory only supplies a Sp6 constituent of dimension one-half or all of that degree; the proof does not assume irreducible restriction. A new elementary multiplier-centralizer argument shows that semisimple Sp6 classes are stable under similitude conjugation, transferring the character ratio without loss on those classes.

For prime q≥5, prime-order Fourier inversion in the possible doubled representation gives projective support at least one-fifth. For composite q≥25, the published unipotent estimate and the commutator inequality give support at least3/16 for every compatible normalizer. At q9 the explicit projective semilinear-involution descent and all81 row weights give the stronger2/9. The q3 complete cover/outer spectra give one-quarter. Thus3/16 is uniform, with every factor degree at least13. The actual intermediate Hurwitz factorization forces total dimension at most24. Two factors have dimension at least169, a single q≥5 factor at least62, and the sharper q3 bound excludes the remaining single factor.

## Exact artifacts and actual runs

| Artifact | Checked content | Observed result |
|---|---|---|
| `explore_generic.py` | Safe extraction of all100×90 original generic cells, degrees and class data | Complete extraction, q≥5 coefficient lead |
| `check_generic.py` | Exact re-extraction agreement with immutable original; all99×89 inequalities after q=5+x; degree floor q³−1 and class lengths | PASS8811 inequalities,0.8115s |
| `export_small.g` | All original cover/outer rows, full row orthogonality, all power maps and every selected spectrum | PASS228rows31428spectra |
| `check_small.py` | Separate rational cyclotomic Fourier; independent restriction-norm row selection; fusion/order/power/normal-class checks | PASS228rows31428spectra,0.827577s |
| `check_f9.py` | All5760GL2(F9) matrices;240 projective involution cocycles;5760 fixed symplectic bases;19440 vector descent identities;6561 dual weight pairs | PASS0.49587s |

The F9 matrix certificate is a finite **dimension-two witness**. It is not advertised as a verification of every six-dimensional semilinear matrix. The all-dimensional descent and the actual rank-two row subgroup in Sp6 are proved in the text.

The two endpoint tables have140 and88 selected rows. Their nonscalar spectrum counts are19460 and11968; minimum degrees13 and78; minimum support ratios2/7 and8/21. All original values are in `small_inputs.json`, SHA-256 `055640d09bc5b5f2d7518d5227b65cfd22879ce3d7dd0b4b50877e1bd1bc59d2`. The complete generic input is in `generic_inputs.json`, SHA-256 `64a51195068f24ea2d495c9280c9bc0899afe418f8cfdc5f81e7a13530c0c811`.

The initial exploratory dimension assertion expected89 columns and stopped before any coefficient analysis; the complete source has90 columns, one central and89 noncentral. This assertion was corrected. The initial GAP export emitted a harmless unbound-global warning for its table variable; the variable is now initialized and the fresh complete run is clean. Neither event was a failed mathematical inequality. The final generic checker additionally re-extracts every retained mathematical object from the frozen original, rather than trusting its JSON source tag alone.

## Reproduction and limits

Run the three Python scripts from this directory. They use the retained mathematical inputs and explicitly imported rational-arithmetic helpers in the parent directory. The generic source is never executed. The GAP exporter runs from the workspace root with the retained GAP4.16.1/CTblLib1.3.11 environment; it rebuilds both original input tables and all spectra. `generic_certificate.json`, `generic_run.json`, `small_scan.json`, `small_checked.json`, and `f9_checked.json` retain the actual output.

The parent independently reran the original generic certificate, full small certificate and F9 witness, with all PASS; it then reviewed and reran the final source-to-input strengthening, PASS2.484827s. The parent reviewed the proof, all code and exact primary-source passages. The independent peer `/root/imprimitive` separately reconstructed all8811 generic inequalities,228rows31428spectra and every auxiliary F9 witness without importing the author arithmetic; its full report and code are in `agents/imprimitive/audit_odd_c3/`. The peer also freshly read the invoked original passages and official table semantics. These checks are recorded distinctly from a newly constructed character table. No independent reconstruction of Lübeck's whole character-table construction, no new proof of the ATLAS tables, and no TeX compilation are claimed.

Record time:2026-11-21 19:18:55UTC from the clock tool. Author/reviewer identity:/root/g34_eightfolds, GPT-6AstraPro, effort inherited/unexposed, HODGE_DIVISION.
