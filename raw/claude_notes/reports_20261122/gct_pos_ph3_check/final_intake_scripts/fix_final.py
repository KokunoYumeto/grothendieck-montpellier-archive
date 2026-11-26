"""Exact corrections of my own final intake before delivery.  Touches only that intake, its events and my notes."""
import pathlib
D = pathlib.Path('<local>/Documents')
G = D / 'field_experts/intake_20261121/intakes/GCT_POS'
MD, TS = G / 'INTAKE_GCT_POS_20261122_final.md', G / 'INTAKE_GCT_POS_20261122_final_CHECK_EVENTS.tsv'
NL, TAB = chr(10), chr(9)
s = MD.read_text(encoding='utf-8')


def sub(old, new):
    global s
    assert s.count(old) == 1, (old[:70], s.count(old))
    s = s.replace(old, new)


sub("""  only. They are in the scratchpad of session e0d20ada, folder `chk\\gctpos\\`, each with its output saved beside it:
""", """  only. They are in the scratchpad of session e0d20ada, a temporary folder that a reboot or cleanup can clear:
  `<local>/AppData\\Local\\Temp\\claude\\f2c80a22394db22f\\e0d20ada-e036-40ad-83b1-31e9a63b69bc\\scratchpad\\chk\\gctpos`.
""")
sub("""  - `final_aux.py`: hashes, and the N-diff.
- **Read:** FINAL_STATUS.md (lines 1-90); for each finding, what its row says in §1.
""", """  - `final_aux.py`: hashes, and the N-diff;
  - `final_verify.py`: the exact tests for K-022 and PNEW-016, the hashes again, and the search for the two proofs.
- **Read:** FINAL_STATUS.md (lines 1-98); for each finding, what its row says in §1.
- **The main session's events** are copied under its name, with two changes of form: ids in the run's hyphenated form,
  and its type "computation" written as "computation or formal certificate".
""")
sub('"Carried" means: statement read, no fault seen, proof not checked.',
    '"Carried" means: statement read to the extent given, no fault seen, proof not checked.')
sub("numerator zero to order 2, series regular;",
    "numerator zero to order exactly 2 (exact cyclotomic arithmetic), series regular;")
sub("computation, n = 4 only: total minus chain residue is divisible by 3",
    "hand arithmetic on the n = 4 residues: total minus chain is divisible by 3")
sub("| K-010 | first 25 lines", "| K-010's table | first 25 lines")
sub("| plethysm LEDGER; SOURCE_AUDIT | whole file; lines 1-60 |",
    "| plethysm LEDGER; SOURCE_AUDIT | all 111 lines, cut at 900 bytes; lines 1-60 |")
sub("Lines were cut at 170 to 900 bytes in some stored outputs;",
    "\"Same\" holds only up to the stored width: lines were cut at 200 to 1,500 bytes in some stored outputs;")

sub("""| 128-142 | poles only at n = 4, 5; orders at most those of K-018 | the result at the top; K-025 gives odd factors too |
| 159-174 | PH3 for Kronecker open; attack through K-020's component | refuted; the r = 0, PH2 and SH(a) gates are in §6. The K-020 attack is not needed for PH3 |
| 183-187 | H02 waits for the run's final; "two independent computations of the witness" | §3. The witness has the run's computation and mine, and rests on an exterior identity I did not read |
| 209-212 | H02 "Tests 1, 2 and 4 pass" |""",
"""| 128-134, in part | poles known only at n = 4, 5 | the all-n pole, up to a power of 3. The facts at n = 4, 5 stand |
| 145-146, 186-187 | the witness "checked here exactly"; "two independent computations"; H02 waits for the final | §3. I recomputed the wave once, to 60 digits; the f₉(6) = 1 side rests on an exterior identity whose proof I did not read |
| 159-170 | PH3 for Kronecker open; attack through K-020's component | refuted; that attack is not needed for PH3. Its line 164 gave two-part orders only: K-025 gives odd factors too |
| 172-174 | PH2, SH(a): "No wave estimate yet" | still open, with an amplitude (PNEW-015) and a dichotomy (PNEW-016); §6 |
| 210-212 | H02 "Tests 1, 2 and 4 pass" |""")
sub("| 226-229, 235-240 | successor questions | §6 |", "| 226-229, 235-240 | successor questions | §8 |")
sub("Lines 189-196 (H20, H21) and 218-221 (the K-018 candidate and its Kravtsov gate) stand.",
    "Lines 189-196 (H20, H21) and 230-234 stand. So do 218-221 (the K-018 candidate and its Kravtsov gate), with n = 9,\n16, 23, 30 now checked where 219 says n = 9.")

sub("""- `IMPLICATIONS.md`, line 5, does the same, "as fixed in the prompt".
""", """- `IMPLICATIONS.md`, line 5, does the same, "as fixed in the prompt".
- `QUESTIONS.tsv`, row Q1ph3 (line 4), gives 1.6.7 as the question's locator.
""")
sub("""  corollary uses is already the one of §3.4.
- The cause is partly ours:""", """  corollary uses is already the one of §3.4 (the run's SOURCE_AUDIT §10 says so too).
- The run does cite 3.3.4 for P-F14, and its 1.6.7 citations for the plethysm family are right.
- The cause is partly ours:""")
sub("coefficients under that name.\n\n**Faults in the dependent",
    "coefficients under that name; it named 3.3.1-3.3.4 only as \"general-form versions\".\n\n**Faults in the dependent")
sub("""- the verifier sentence of the cp03 intake (§2c, first row);
""", """- the verifier sentence of the cp03 intake (§2c, first row), and its "generator was not rerun" for K-002, which was
  inaccurate: that verifier regenerates the coverage;
- the cp03 intake's two claims about the n = 9 witness (§2c, lines 145-146 and 186-187);
- the core of prompt 52, which I wrote, also carried the false premise "maximal order 2^(n-1)" for tensors;
""")
sub("""- **New (files not in that manifest):**
""", """- **New:** 79 files are not in that manifest (the TSV lists them). The proof files with new ids among them are:
""")

sub("""4. **Q3, Q4, Q5.** Unchanged since checkpoint 03:""", """4. **Q3, Q4, Q5.** Unchanged since checkpoint 03 in the columns compared:""")
s = s.rstrip() + """

## 7. The scope of the two proofs, and what is new

- **Neither proof is used.**
  - I searched the return's 575 text files (tex, md, tsv, txt, py, json, bib, csv) for both names, "Riemann
    hypothesis", GRH and both titles, with the run id ALPOGE_GCT removed.
  - Outside the copy of the prompt there is one hit, SOURCE_AUDIT.md line 272: the run says that Alpöge's theorem is
    not an input to any new result and that Masullo's draft is not used.
  - The statements I read involve no L-function. PDFs and compressed files were not searched.
- **New against our own results:** the 24 rows of §1. The main one extends the refutation of numerical PH3 from
  plethysm (P-F19/P-F31) to Kronecker coefficients. P-F14 had refuted 3.3.4 only for torus subgroup restriction.
- **New against the literature: not known.** No search was made, Hexagon included.

## 8. Integration, and what a successor prompt needs

Nothing below is edited here.

- **Our earlier rows:** ALPOGE_GCT P-F60's gate (the Kronecker form of PH3) closes by K-023 to PNEW-013. The register
  changes are in §3.
- **Cotes, studies and companion notes:** none was read for this intake, so no edit is proposed.
- **A successor of prompt 52 needs:**
  - Hypothesis 3.3.4 and rank(x) of §3.4 wherever Kronecker coefficients are meant, and numerical PH3 given as refuted;
  - the main questions r = 0, then PH2 and SH(a), with the obstacles and attacks of §6;
  - neither false premise (maximal order 2^(n-1); no odd lifts), and PNEW-014 as the reason a K₀ congruence alone
    cannot decide PH2 or SH(a);
  - an exhaustive literature audit (Q10 is incomplete), with Kravtsov, Franks-Reichenbach and Hexagon.
- Prompts 30-36 were not reread, so I propose no edit to them.
"""

L = [l.split(TAB) for l in TS.read_text(encoding='utf-8').rstrip(NL).split(NL)]
out = []
for c in L:
    if c[0] == 'K-027' and c[3].startswith('computation'):
        continue
    if c[0] == 'K-027':
        c[4] += '; hand arithmetic on the n=4 residues agrees with the congruence'
    if c[0] == 'K-022' and c[3].startswith('computation'):
        c[4] = c[4].replace('numerator vanishes to order 2', 'numerator vanishes to order exactly 2 (exact, final_verify.py)')
    if c[0] == 'PNEW-016' and c[3].startswith('computation'):
        c[4] = 'constant 17/240 (check_final.py); threshold inequalities at 79004, and the n^3/5 inequality at 2000 with its margin, exact (check_final.py, final_verify.py)'
    out.append(c)
assert all(len(c) == 5 for c in out)
MD.write_text(s, encoding='utf-8', newline=NL)
TS.write_text(NL.join(TAB.join(c) for c in out) + NL, encoding='utf-8', newline=NL)

N = D / 'agent_notes/a0805369bae2ebddc_NOTES.md'
with N.open('a', encoding='utf-8', newline=NL) as fh:
    fh.write("""- Final intake verified and corrected before delivery (fix_final.py): s7 scope (neither Alpoge nor Masullo used), s8 integration;
  fourth 1.6.7 place = QUESTIONS.tsv Q1ph3; K-027 arithmetic no longer typed as computation; K-022 and PNEW-016 tests now exact.
  K-008 completeness result: 307,307 + 291,704 covered triples, none outside the list; 87,720 certificates pass own checker.
""")
(D / 'agent_notes/20261121_intake_GCT_PLETH_ALPOGE_GCT_NOTES.md').write_bytes(N.read_bytes())
print('events', len(out) - 1)
print('types', sorted({c[3] for c in out[1:]}))
new = ['K-0%d' % i for i in range(21, 39)] + ['R-NEW-004', 'R-DIAG-001'] + ['PNEW-0%d' % i for i in range(13, 17)]
print('new findings without an event', [x for x in new if x not in {c[0] for c in out}])
