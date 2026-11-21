# Even Sp4/Sp6 source and verification record

Author `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed,
HODGE_DIVISION, 21 November 2026. Complete proof D-ESC-01–03 is in
`even_symplectic_section.tex`; independent whole-proof review is requested
separately. The scope includes all ordinary irreducibles, not only Weil
or unipotent characters.

## Complete mathematical inputs

- Official GenericCharacterTables `Sp4.0` and `Sp6.0`, frozen commit
  `87231738271ed548f62e7f1c98ff2bbfc1ed30d3`. Every original mathematical
  entry was retained and parsed. The source URL/hash manifest is
  `even_symplectic_retrieval.json`. Complete upstream files are in
  `cache`; only mathematical inputs and authored code belong in the
  final deliverable.
- The official table inventory
  <https://oscar-system.github.io/GenericCharacterTables.jl/stable/tables_list/>
  explicitly identifies **complete** `Sp4.0` and `Sp6.0`. It records
  that Enomoto's Sp4 printed table contains misprints and that F.Lübeck
  recomputed the implemented table with Deligne–Lusztig theory. The
  proof uses this corrected official table, not a purported exact
  copy of all original printed entries. The same inventory explicitly
  says the odd-Sp4 entry is only unipotent/incomplete; it is not used.
- Enomoto, *The characters of the finite symplectic group Sp(4,q),
  q=2^f*, Osaka J.Math.9(1972),75–94. Original published PDF opened at
  <https://ir.library.osaka-u.ac.jp/repo/ouka/all/8596/ojm09_01_07.pdf>.
  Complete-character purpose is on p.75, construction is §4 pp.80–85,
  final completeness assertion p.85, group tables IV-1/IV-2 pp.92–94.
  I checked the coverage assertion and exact locators; this is not
  labelled a fresh independent reproof of the printed character
  classification or its correction history.
- Lübeck, *Charaktertafeln für die Gruppen CSp6(q) mit ungeradem q
  und Sp6(q) mit geradem q*, Heidelberg dissertation1993. Full author
  PDF retrieved from
  <https://www.math.rwth-aachen.de/~Frank.Luebeck/preprints/CharTabCSp6.pdf>,
  794539bytes, SHA-256
  `5d336441c90390b3f2072ed7ceaaacdfb83776549954d9d830dbabe4967af070`.
  I read Introduction pp.3–4, construction overview §2.2 pp.18–21,
  and the generic-file/verification paragraphs of §9 pp.78–79.
  They explicitly state complete ordinary-character coverage,
  include all Lusztig-series and nonuniform pieces, and state that
  the full values are supplied as CHEVIE files. The printed appendix
  contains only some explicit subtables; the proof does not confuse
  those with the complete file. This is a dissertation and official
  mathematical data source, not mislabelled a refereed journal paper.
- The complete small numerical inputs are the official CTblLib ATLAS
  records `S4(4)`, `S4(4).2`, `S4(4).4`, `2.S6(2)`. All source strings,
  class data, prime power maps, indicators and actual core fusions are
  retained. `S4(4).4` additionally identifies itself as `Aut(S4(4))`.
  Simple-group metadata give `(multiplier,outer)=('',4)` and `(2,'')`.
  The full exceptional-multiplier list is HHM2015, Chapter5/Table1,
  p.35, read previously and checked against these families. These
  classification and table identities are explicit mathematical inputs,
  not inferred merely from numerical orthogonality.

## Executed exact checks

1. Safe original-input extraction and coefficient proof: **83 rows /
   4549 nonidentity cells**. All shifted coefficient inequalities pass.
   The threshold8 Sp4 bound is1/4/minimum degree196; threshold4 Sp6
   bound is17/63/minimum degree378. Offline reparse plus Fraction
   verification passed in0.587s.
2. Fresh GAP full-row orthogonality and exact eigenvalue scan, followed
   by separate integer-polynomial Fourier reconstruction:
   **104 selected rows /3442 spectra**, PASS0.145s. All normal fusions,
   prime power maps and cyclic outer quotients are checked. The only
   quarter failures are degrees7,21,27, with ratios1/7,5/21,2/9.
   The unique degree7 indicator is recomputed as+1 directly.
3. All three mathematical input/coefficient files were regenerated a
   second time, including a fresh GAP export, and their hashes were
   unchanged. Timings occur only in run summaries, not deterministic
   mathematical certificates.

| File | Bytes | SHA-256 |
|---|---:|---|
| `even_symplectic_generic_inputs.json` |436290|`49ecbe27ad97b8cfe0204f96ef463ef1e8e0626ce6987bcccb0d8b33041e4fa0`|
| `even_symplectic_polynomials.json` |87938|`92e32ae7b01d49469f31464472ae044b320b59a6400fedaec5003fde2760a3b3`|
| `even_symplectic_small_inputs.json` |19056|`b51fae6eaa904bb5a1bdcac2f6aa85a940c9968ddba912bf115faa750e772fe2`|

## Failed probes and exact boundary

The stronger generic quarter-character estimate at threshold4 failed
for six Sp4 cells and three Sp6 cells. All failures are retained in
`even_symplectic_exploration.json`; the theorem uses the corrected
ranges/ratios, without claiming the failed bound. An initial inventory
query asked `ExtensionInfoCharacterTable` on an outer extension, where
the library has no method. Restricting that metadata call to the simple
groups fixed the inventory query; no mathematical table changed.
The first GAP exporter produced only harmless unbound-global parser
warnings, then completed every check; initializing those globals removed
the warnings on the deterministic second execution.

The theorem with arbitrary original field leaves exactly the single
degree7 Sp6(2) case. It removes that case only by the **previously
proved eight-field, non-Eisenstein, nonsplit** D-BI-17 theorem. Neither
its existence nor a new all-fields degree7 exclusion is asserted.
