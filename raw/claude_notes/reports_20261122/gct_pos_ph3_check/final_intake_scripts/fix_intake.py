import pathlib, collections

B = pathlib.Path('<local>/Documents/field_experts/intake_20261121/intakes/GCT_POS')
M = B / 'INTAKE_GCT_POS_20261121_kronecker.md'
T = B / 'INTAKE_GCT_POS_20261121_kronecker_CHECK_EVENTS.tsv'
NL = chr(10)
TAB = chr(9)
BS = chr(92)
s = M.read_text(encoding='utf-8')


def between(a, b, new):
    global s
    assert s.count(a) == 1, ('start', a)
    i = s.index(a)
    j = s.index(b, i + len(a))
    s = s[:i] + new + s[j:]


def cell(key, idx, new):
    global s
    L = s.split(NL)
    hit = [i for i, l in enumerate(L) if l.startswith('| ' + key + ' |')]
    assert len(hit) == 1, ('cell', key, hit)
    c = L[hit[0]].split(' | ')
    c[idx] = new + (' |' if idx == 3 else '')
    L[hit[0]] = ' | '.join(c)
    s = NL.join(L)


between('## 0. Return read and scope', '- **Read in full, with the proof:**',
"""> **Update and corrections, 22 Nov 2026, about 08:30 UTC (same agent).**
> - **This intake is of checkpoint 03 and is superseded in part.** `GCT_POS_final_20261122T0219Z_unzipped` is now the
>   return, and the checkpoint-03 folder has been retired. Its FINAL_STATUS.md says the programme ended INCOMPLETE, and
>   claims that **the existence clause of numerical PH3 is refuted for triple-rectangular Kronecker coefficients**
>   (K023, R-NEW004, K024, PNEW013: a pole of order 2^(n-1)·3^r, some r ≥ 0, for every n ≥ 2). I have not read or
>   checked that proof. Where this file calls that question open, or advises waiting for the final, it describes
>   checkpoint 03.
> - **Section 1a is filled in:** all 5,214 rows of R-NEW-001 agree.
> - **Corrections to what I first wrote and reported:**
>   - the number confirmed was 15 findings, not 18 (16 with R-NEW-001), plus the n = 4 value table;
>   - 17 findings are carried, not about 15, and 2 are background, not 3;
>   - K-018 is confirmed at n = 9 only: I read the first 70 of 147 lines of its file;
>   - several "read in full" entries were partial, and are now listed as such;
>   - four check events typed "independent re-proof" were computations, and are retyped.

## 0. Return read and scope

- **Return:** `research_returns""" + BS + """GCT_POS_checkpoint_03_20261121T2215Z_unzipped`, the snapshot of 22:16 UTC on 21 Nov,
  taken about 2 h 15 min into the run. It is a checkpoint, not the final return.
""")

between('- **Read in full, with the proof:**', '- **Read at statement level, with the source text of the statement:**',
"""- **Read, with the proof** (line counts are those of the files in the final):
  - K-001 to K-008 (`branches/kronecker/KRONECKER_FINDINGS.tex`, lines 1-520 of 537); the chart ideals of K-003/K-004
    and the commutator kernel of K-004 were not recomputed;
  - K-009 (`branches/root/lift_bound.tex`, whole);
  - R-NEW-003 (`branches/root/h4_finite_rational.tex`, lines 1-90 of 115: the denominator and degree argument);
  - K-014 (`N5_POLE.tex`, lines 1-60 of 132);
  - K-018 (`AMPLIFYING_GADGET.tex`, lines 1-70 of 147);
  - the PNEW-005 assembly (`plethysm/quantitative_refinement.tex`, lines 329-420 of 429).
""")

cell('K-003, K-004', 2, 'targeted proof check of the arguments; chart ideals and commutator kernel not recomputed')
cell('K-018', 3, '**confirmed at n = 9**, which refutes the universal 2^{n−1} bound; the all-n formula is at statement level (proof read in part)')
cell('R-NEW-003', 3, '**confirmed for the denominator and degree argument** (end of the proof not read; numerator not expanded)')
cell('PNEW-006', 3, '**confirmed, given the exterior identity**, whose proof is not read')
cell('R-NEW-001', 2, 'independent computation of every row (`o6b.py`, `o6c.py`): 0 mismatches')
cell('R-NEW-001', 3, '**confirmed**, on the copy in the final (see 1a)')

between('**Counts.**', '### 1a.',
"""**Counts** (35 findings: K-001 to K-020, R-NEW-001 to 003, PNEW-001 to 012).
- 16 confirmed, at the scope stated in the tables: K-001 to K-009, K-014 (given K-011), K-018 (n = 9 only),
  R-NEW-001, R-NEW-003, PNEW-001, PNEW-005 (given PNEW-002 to 004), PNEW-006 (given the exterior identity).
  The n = 4 value table is also confirmed, for s ≤ 4.
- 2 background, correct: R-NEW-002, PNEW-011.
- 17 carried at statement level: K-010 to K-013, K-015 to K-017, K-019, K-020, PNEW-002 to 004, PNEW-007 to 010,
  PNEW-012.
- 0 refuted. No gap found in what was read.

""")

between('### 1a.', '## 2. What is new',
"""### 1a. The outer-six table (R-NEW-001)

- **Result: all 5,214 rows agree with both of the run's columns** (11, 121, 847 and 4,235 rows for n = 0, 1, 2, 3).
  The rows are exactly all pairs (μ ⊢ 6, λ ⊢ 6n), with none missing, extra or repeated (`o6c.py`).
- **Method:** h_n and p_r[h_n] expanded in power sums, paired with Schur functions by my own Murnaghan-Nakayama code,
  in exact rationals. It is the same classical method as the run's first column, in independent code.
- **Which file:** checkpoint 03 was retired before this check finished, so the file checked is
  `certificates/outer_six_n_le_3.tsv` of the final, sha256
  0d660744557c219cd1665692ca4edc38f0d63851e9aa521cd7660722b9b07c7a, as in the final's manifest. It has the row
  count of checkpoint 03's file. I could not compare the bytes of the two copies.
- **Failed attempts:** two earlier runs by weight expansion (`o6.py`) gave no result; the second, on a reduced sample,
  ran out of memory. Neither is evidence.

""")

s = s.replace("`o6.py`: the outer-six table against my power-sum computation",
              "`o6b.py`, `o6c.py`: every row of the outer-six table against my power-sum computation")
s = s.replace("is the first density theorem in the direction of SH(b)",
              "is a density theorem in the direction of SH(b) (no literature search made)")

L = [l.split(TAB) for l in T.read_text(encoding='utf-8').splitlines()]
assert not any(r[0] == 'R-NEW-001' for r in L)
extra = {
    'K-003': '; chart-ideal computations not rerun',
    'K-004': '; chart-ideal and commutator-kernel computations not rerun',
    'K-018': '; all-n formula not checked (proof read in part)',
    'R-NEW-003': '; end of the proof, after the degree argument, not read',
    'PNEW-006': '; given the exterior identity, whose proof was not read',
}
for r in L[1:]:
    if r[3] == 'independent re-proof':
        assert r[0] in ('K-005', 'K-014', 'K-018', 'PNEW-001'), r
        r[3] = 'computation or formal certificate'
    r[4] += extra.get(r[0], '')
L.append(['R-NEW-001', '2026-11-22', L[1][2], 'computation or formal certificate',
          'confirmed: all 5214 rows (every mu|-6, lambda|-6n, n<=3) recomputed, 0 mismatches against both columns '
          '(o6b.py, o6c.py); file = copy in the final return, sha256 0d660744557c219c..., checkpoint 03 having been retired'])

# both files are written only after every assertion above has passed
M.write_text(s, encoding='utf-8')
T.write_text(NL.join(TAB.join(r) for r in L) + NL, encoding='utf-8')

ids = collections.defaultdict(set)
for r in L[1:]:
    ids['carried' if r[3].startswith('carried') else 'confirmed'].add(r[0])
print('events', len(L) - 1, {k: len(v) for k, v in ids.items()})
print('confirmed', sorted(ids['confirmed']))
print('carried or background', sorted(ids['carried']))

NOTE = """- 22 Nov ~08:30 UTC: R-NEW-001 DONE: 5214/5214 rows agree (o6b.py, o6c.py; copy in the final return). Intake 1a + event filled.
  Corrected: 15 (not 18) findings confirmed before this, 16 now + n=4 value table; 17 carried; 2 background; K-018 n=9 only;
  partial readings marked; 4 events retyped from re-proof to computation.
  cp03 is retired. GCT_POS final (22 Nov 02:19Z) claims numerical PH3 refuted for Kronecker (K023/R-NEW004/K024/PNEW013): NOT checked.
  Errors in my earlier intakes, NOT yet edited there:
  (1) GCT_PLETH part 4 says I read the evaluators and confirmed no writes before running. I had read stable_hook_positive.py in
      part and only grepped some direct imports; generic_twist_lower_positive.py was not found by that grep and ran unscanned.
      Rescanned 22 Nov (depscan.py, 20 modules): three write_text calls, all in main()/build() behind __main__ guards,
      not reached on import; newest mtime in that return is its unpacking (11:36 local, 21 Nov). No harm found.
  (2) ALPOGE_GCT part 4 + its TSV call the P-F31 sources "byte-identical": only file sizes were compared.
  (3) ALPOGE_GCT part 2 TSV types P-F35 as "independent re-proof": it was a computation.
"""
D = pathlib.Path('<local>/Documents/agent_notes')
main = D / 'a0805369bae2ebddc_NOTES.md'
with main.open('a', encoding='utf-8', newline=NL) as fh:
    fh.write(NOTE)
(D / '20261121_intake_GCT_PLETH_ALPOGE_GCT_NOTES.md').write_bytes(main.read_bytes())
print('notes updated')
