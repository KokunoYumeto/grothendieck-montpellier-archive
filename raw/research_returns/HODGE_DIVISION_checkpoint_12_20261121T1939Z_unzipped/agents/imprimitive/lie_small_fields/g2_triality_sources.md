# G2 and triality: source and computation record

Author `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed,
HODGE_DIVISION, 21 November 2026. The complete new argument is
`g2_triality_section.tex`, D-G2T-01–03. Independent written review was
requested after the author proof and exact certificates were complete.

## Original mathematical inputs and precise access scope

1. **Official generic character-table library.**
   <https://oscar-system.github.io/GenericCharacterTables.jl/stable/tables_list/>
   and its references page were read for all eleven entries: eight
   `G2.*` tables and three `3D4.*` tables. The source was frozen at
   commit `87231738271ed548f62e7f1c98ff2bbfc1ed30d3`.
   `generic_table_retrieval.json` retains each original URL, size,
   and SHA-256. Every complete original mathematical entry was parsed;
   no downloaded Julia code was executed. The complete source files are
   in `cache` only and need not be included in the deliverable. The
   retained `generic_character_entries.json` contains only original
   mathematical entry expressions, declared degree/class-length
   expressions, conditions, and provenance.
2. **Enomoto–Yamada, 1986.** *The characters of G2(2^n)*,
   Japan. J. Math.12,325–377, DOI10.4099/math1924.12.325.
   Full published PDF retrieved from
   <https://www.jstage.jst.go.jp/article/math1924/12/2/12_2_325/_pdf/-char/en>.
   I read the introductory coverage assertion and verified the exact
   table locations: IV-1 p.364, IV-2 pp.365–370, IV-3 p.371. The
   generic input covers both signs. This log does **not** claim a fresh
   independent reproof of the paper's complete character construction.
3. **Enomoto, 1976.** *The characters of the finite Chevalley group
   G2(q), q=3^f*, Japan. J. Math.2,191–248,
   DOI10.4099/math1924.2.191. Full publisher PDF retrieved from
   <https://www.jstage.jst.go.jp/article/math1924/2/2/2_2_191/_pdf/-char/en>.
   The introduction explicitly states complete complex-character
   coverage. Exact table locations checked: VII-1 p.239, VII-2
   pp.240–247. Full table entries used in the proof are the frozen
   official mathematical implementation. No fresh reproof of the
   complete original construction is claimed.
4. **Chang–Ree, 1974.** *The characters of G2(q)*, Symposia
   Mathematica XIII,395–413. The original full article was not retrieved.
   The four complete ordinary-character tables for characteristic
   greater than three are accessed through the official mathematical
   data, which explicitly identifies this published source and its
   character/class notation. Do not mark this as a fresh full-paper
   read or invent a page-specific proof audit.
5. **Deriziotis–Michler, 1987.** *Character table and blocks of finite
   simple triality groups 3D4(q)*, Trans. AMS303,39–70,
   DOI10.1090/S0002-9947-1987-0896007-9. The AMS full PDF returned403.
   The original article's introductory text pp.39–42 was read through
   the indexed article copy and locates the complete table in §4,
   Theorem4.3 and Tables3.6/4.4. The complete mathematical tables used
   are the three official `3D4` inputs. No fresh full read of
   Theorem4.3's entire proof is claimed.
6. **Hiss–Husen–Magaard, 2015.** *Imprimitive irreducible modules for
   finite quasisimple groups*, Memoirs AMS234,no.1104. Author full text:
   <https://www.math.rwth-aachen.de/~Gerhard.Hiss/Preprints/ImIrrMod.pdf>.
   Chapter5, Table1 and its preceding paragraph, numbered p.35,
   give the complete exceptional-multiplier list; only G2(3)/G2(4)
   occur from the two families. The same page records
   G2(2)'≅U3(3), explicitly outside the present theorem.
7. **Complete small tables.** Official CTblLib1.3.11 ATLAS records
   `3.G2(3)`, `3.G2(3).2`, `2.G2(4)`, `2.G2(4).2`,
   `3D4(2)`, `3D4(2).3`. Every original row, class size/order,
   prime power map, fusion and source string is retained. Official
   extension metadata give multipliers/outers `(3,2),(2,2),(1,3)`.
   The meaning of that metadata is the previously freshly read
   CTblLib manual §3.7-3; group/table correctness is an explicit
   published input, not inferred from orthogonality.

## Exact verification events

- `build_generic_input.py` validated all eleven frozen source hashes and
  extracted the compact original mathematical data: **415124 bytes**,
  SHA-256 `66ad9b13d457d141d424084336787b3bb1f9d53818475b806f7a6cc24eb3664b`.
- `parse_generic_bounds.py` checked original degrees and class lengths,
  then all **318 nontrivial row types / 9242 nonidentity cells**.
  Every shifted coefficient inequality passed in **0.748 seconds**.
  Threshold5 is used for G2 and threshold3 for triality.
- `check_generic_polynomials.py` independently re-evaluates the retained
  coefficient inequalities with Python `Fraction`, without Flint or
  the parser. It passed all9242 inequalities in **0.207 seconds**.
  It validates the derived polynomial certificate; correspondence
  with original expressions is the separate parser check. This is
  author verification, not an independent person's review.
- The six-table GAP exporter checked full orthogonality. The compact
  numerical input SHA-256 is
  `e4a8aefbf5a4a32a5b31b217143ccae03db8b9f3753cc2e91a6169d0364b6a7c`.
- `check_g2_triality_small.py` independently selected irreducible
  restrictions and recomputed **239 rows /11502 full spectra** by
  exact cyclotomic polynomial Fourier arithmetic. It passed in
  **0.693 seconds**. All fusion and power-map consistency checks passed.
  This reuses the author's previously fully reviewed D-SPOR Fourier
  helper; it is distinct from GAP's eigenvalue routine.
- The earlier eight-table exploratory run, which additionally used
  3D4(3)/3D4(4), is preserved truthfully in
  `g2_triality_exploration_log.md`. Those two numerical tables are
  unnecessary after the uniform polynomial proof. Compacting the
  final input is not a failed calculation or a claim of broader
  finite coverage than was actually executed.

## Precise remaining review gate

The all-field theorem is fully proved from the explicit published table
inputs and the displayed exact arithmetic. The G34 sibling has now passed the complete independent whole-proof
and source audit, and separately reconstructed all11 original generic
files/9242 coefficient bounds and all239rows/11502 spectra in1.355s,
without importing the author parser or checker. Its report and output
are retained in the sibling bireflection directory. Root review is
recorded separately when received.
The separate linear-Weil audit performed by this author is recorded
in `../audit_linear_weil/PEER_AUDIT.md`; it is not a self-audit of D-G2T.

## Deterministic-certificate repair after root rerun

The first coefficient file included the runtime in seconds, so a fresh
root rerun changed its file hash while leaving every mathematical entry
unchanged. The parser now excludes timing from the retained coefficient
file and keeps it only in the run summary. The repaired certificate was
regenerated, fully rechecked, and regenerated a second time; its hash
remained exactly `568425a2cf62e62dbe24709a3372d9bd182946e0a53ae74e7fed45ba640dcd13`. The proof hash was updated accordingly.
Root reports complete mathematical/code review and actual fresh reruns
PASS; its remaining source-semantic review is recorded separately.
