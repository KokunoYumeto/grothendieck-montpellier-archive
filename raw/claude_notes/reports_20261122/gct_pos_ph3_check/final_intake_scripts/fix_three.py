import pathlib

B = pathlib.Path('<local>/Documents/field_experts/intake_20261121/intakes')
NL, TAB = chr(10), chr(9)
DAY = 'Corrected 22 Nov 2026'
pending = {}


def text(rel):
    if rel not in pending:
        pending[rel] = (B / rel).read_text(encoding='utf-8')
    return pending[rel]


def sub(rel, old, new):
    s = text(rel)
    assert s.count(old) == 1, (rel, old[:60], s.count(old))
    pending[rel] = s.replace(old, new)


def event(rel, sid, newtype=None, newout=None, add=''):
    L = text(rel).rstrip(NL).split(NL)
    hit = [i for i, l in enumerate(L) if l.split(TAB)[0] == sid]
    assert len(hit) == 1, (rel, sid, hit)
    c = L[hit[0]].split(TAB)
    c[3] = newtype or c[3]
    c[4] = (newout or c[4]) + add
    L[hit[0]] = TAB.join(c)
    pending[rel] = NL.join(L) + NL


# 1. GCT_PLETH part 4: what was read before the evaluators were run
P4 = 'GCT_PLETH/INTAKE_GCT_PLETH_20261121_part4.md'
sub(P4,
"""- **Checked by computation.** I ran the run's own evaluators, after reading them and confirming they only compute and
  read their JSON data, with no writes. I compared them with my independent character computation: power-sum
  plethysm with Murnaghan-Nakayama characters of S_m (`chk/g036.py`, `chk/g037.py`).
""",
"""- **Checked by computation.** I ran the run's own evaluators without having read them, and compared their values with
  my independent character computation: power-sum plethysm with Murnaghan-Nakayama characters of S_m (`chk/g036.py`,
  `chk/g037.py`). What was done before running them:
  - G-037, `stable_hook_positive.py` (one file, standard-library imports only): I read lines 89-155, saw the list of
    its definitions and a grep of its imports and file calls, and ran a copy from my scratchpad.
  - G-036, `outer_five_positive.py`: I read lines 1-10 and imported it in place. Its import closure has 20 module
    names. I had grep output for 8 of them, for a few patterns, and had read none of the 8. The other 12, among them
    `generic_twist_lower_positive.py`, ran with no scan whose output I saw: my one broad grep was cut at 20 lines, and
    the targeted grep reported that file as not found.
  - After the fact, 22 Nov: a static scan by the main session (Claude Opus 5.5 at effort max) found 26 modules in the
    import closure (same-named copies included), three write_text calls, all inside main() or build() behind __main__
    guards, and no network, subprocess, exec or eval in the closure. My own scan (`chk/gctpos/depscan.py`) found the
    same three calls. Neither scan is a reading of the code, and neither was done before the run.
  - *""" + DAY + """. The old wording was: "I ran the run's own evaluators, after reading them and confirming they only
    compute and read their JSON data, with no writes." It was false.*
""")
P4T = 'GCT_PLETH/INTAKE_GCT_PLETH_20261121_part4_CHECK_EVENTS.tsv'
event(P4T, 'G-036', add=' [' + DAY + ': the evaluator and its imports were not read before running (8 of 20 modules grepped, 12 not scanned); '
      'the intake had said "after reading them and confirming they only compute and read their JSON data, with no writes"; static scans of 22 Nov are after the fact]')
event(P4T, 'G-037', add=' [' + DAY + ': the evaluator was read only in part (lines 89-155) before running; '
      'the intake had said "after reading them and confirming they only compute and read their JSON data, with no writes"]')

# 2. ALPOGE_GCT part 4: sizes are not contents
A4 = 'ALPOGE_GCT/INTAKE_ALPOGE_GCT_20261121_part4.md'
sub(A4,
"""- **Unchanged since part 2:** P-F31 and all its inputs (P-F23, P-F24, P-F26, P-F27, P-F28, P-F30), P-F19, P-F14 and
  P-F15. No check event after 03:30 UTC touches them, and the file sizes are byte-identical to checkpoint 05
  (`positivity_actual_cubic_pole.tex` 8,921 bytes, and so on). Nothing from parts 1-3 is withdrawn.
""",
"""- **No sign of change since part 2:** P-F31 and its inputs (P-F23, P-F24, P-F26, P-F27, P-F28, P-F30), P-F19, P-F14
  and P-F15. At the time of this part I saw no check event after 03:30 UTC on them, and their files had the byte counts
  I had listed at checkpoint 05 (`positivity_actual_cubic_pole.tex` 8,921 bytes, and so on). I compared no contents.
  Nothing from parts 1-3 is withdrawn.
  - After the fact, 22 Nov, by content, against my stored outputs of the earlier reads (`chk/gctpos/seg_compare.py`,
    `seg_more.py`): P-F31, P-F23 and P-F30 are the same as at checkpoint 05 (whole files); P-F14 and P-F15 the same as
    at checkpoint 03 (whole file); P-F26 the same as at checkpoint 05 in lines 1-40 of 229, the range compared.
    P-F24, P-F27 and P-F28 have not been compared. P-F19 has not been compared with checkpoint 05; against checkpoint
    03 it differs in two passages on scope.
  - *""" + DAY + """. The old wording was: "Unchanged since part 2: [the same list]. No check event after 03:30 UTC
    touches them, and the file sizes are byte-identical to checkpoint 05." Only sizes had been compared.*
""")
event('ALPOGE_GCT/INTAKE_ALPOGE_GCT_20261121_part4_CHECK_EVENTS.tsv', 'P-F31', 'carried as background without fault found',
      'used as input to P-F56, not reread in part 4; same file sizes as checkpoint 05 and no check event seen after 03:30Z. '
      'Content of P-F31, P-F23, P-F30 found the same as checkpoint 05 on 22 Nov, after the fact. [' + DAY +
      ': type was "used and rechecked in this run"; outcome was "unchanged in final return (no new check events after 03:30Z; '
      'byte-identical sources); used as input to P-F56"; only sizes had been compared]')

# 3. ALPOGE_GCT part 2: P-F35 was a computation; and the same part's claim that P-F19 and others were unchanged
A2 = 'ALPOGE_GCT/INTAKE_ALPOGE_GCT_20261121_part2.md'
sub(A2,
"""at a root of order 8 coexists with small indices. This calibrates PL-Q46: large poles do not by themselves give large
indices.
""",
"""at a root of order 8 coexists with small indices. This calibrates PL-Q46: large poles do not by themselves give large
indices.
*""" + DAY + """. This check is a computation from the cited series, and I read only the statement of P-F35. The old
check-event type was "independent re-proof", which was false.*
""")
sub(A2,
"""**P-F19 (from checkpoint 03).** Unchanged. The "corrected discriminant source reading" in the ledger concerns P-F36,
not P-F19. **P-F14, P-F15, PLE-F8, P-F1, P-F2, P-F11, P-F12** are unchanged; no finding of part 1 or of the addendum is
withdrawn.
""",
"""**P-F19 (from checkpoint 03).** Its text changed. The "corrected discriminant source reading" in the ledger concerns
P-F36, not P-F19. No finding of part 1 or of the addendum is withdrawn. When this part was written I had not compared
P-F19, **P-F14, P-F15, PLE-F8, P-F1, P-F2, P-F11 or P-F12** by content. Compared on 22 Nov with my stored outputs of
checkpoints 01 and 03, against the surviving checkpoint 09:
- P-F19 differs in two passages on scope, one inside the statement and one after the proof: both now point to P-F31 as
  closing the existence clause. The rest, the proof included, is the same.
- P-F14, P-F15, P-F11, P-F12 are the same (whole files); P-F1 and P-F2 the same (statement and proof; their file
  changed elsewhere); PLE-F8 the same in lines 1-150 of 214, the range that was stored.

*""" + DAY + """. The old wording was: "P-F19 (from checkpoint 03). Unchanged. [...] P-F14, P-F15, PLE-F8, P-F1, P-F2,
P-F11, P-F12 are unchanged". For P-F19 that was false; for the others it had not been checked.*
""")
A2T = 'ALPOGE_GCT/INTAKE_ALPOGE_GCT_20261121_part2_CHECK_EVENTS.tsv'
event(A2T, 'P-F35', 'computation or formal certificate',
      add=' [' + DAY + ': type was "independent re-proof"; only the statement was read and the indices were computed]')
event(A2T, 'P-F19', 'carried as background without fault found',
      'not reread at checkpoint 05. Content compared 22 Nov (checkpoint 03 against 09): two passages on scope changed, '
      'proof the same. [' + DAY + ': type was "used and rechecked in this run"; outcome was "unchanged in checkpoint 05 '
      '(source correction in ledger concerns P-F36)", which was false]')

for rel, s in pending.items():
    if rel.endswith('.tsv'):
        assert {len(l.split(TAB)) for l in s.rstrip(NL).split(NL)} == {5}, rel
for rel, s in pending.items():
    (B / rel).write_text(s, encoding='utf-8', newline=NL)
    print('corrected', rel)

NOTE = """- Part 1 of the 22 Nov task DONE: three corrections in md + TSV (GCT_PLETH p4, ALPOGE_GCT p4, ALPOGE_GCT p2).
  Two faults more, found while doing it, corrected in the same files:
  (a) ALPOGE p2 said P-F19 "Unchanged": false, two scope passages changed cp03 -> cp09 (proof same);
  (b) my report said "one imported module ran unscanned": 12 of the 20 in the G-036 closure did.
  Content evidence for retired checkpoints = my stored tool outputs (seg_compare.py, seg_more.py, seg_f1.py in chk/gctpos).
"""
with open('<local>/Documents/agent_notes/a0805369bae2ebddc_NOTES.md', 'a', encoding='utf-8', newline=NL) as fh:
    fh.write(NOTE)
