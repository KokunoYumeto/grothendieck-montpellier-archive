import pathlib
D = pathlib.Path('<local>/Documents')
TAB, NL = chr(9), chr(10)
ME = 'Claude Opus 5.5 at effort high, agent a0805369bae2ebddc (GCT_POS final intake)'
DAY = '2026-11-22'
P, C, B = 'targeted proof check', 'computation or formal certificate', 'carried as background without fault found'
out = [('statement_id', 'date', 'who', 'type', 'outcome')]

# the main session's events, under its own name
src = D / 'reports_20261122/gct_pos_ph3_check/CHECK_EVENTS.tsv'
norm = {'GCT_POS:K023': 'K-023', 'GCT_POS:R-NEW004': 'R-NEW-004', 'GCT_POS:K024': 'K-024', 'GCT_POS:PNEW013': 'PNEW-013'}
for line in src.read_text(encoding='utf-8').splitlines()[1:]:
    c = line.split(TAB)
    out.append((norm.get(c[0], c[0]), c[1], c[2], C if c[3] == 'computation' else c[3],
                c[4] + ' [carried from reports_20261122/gct_pos_ph3_check/CHECK_EVENTS.tsv; not repeated here]'))

F = ' (check_final.py)'
mine = [
    ('K-002', C, 'certified list complete: own enumeration of every normalised covered mod-16 triple finds none outside it (k008_complete.py); covers the order-8 lifts of K-002'),
    ('K-008', C, '87,720 certificates pass own checker; 307,307 and 291,704 normalised covered triples, none outside the certified list (k008_complete.py)'),
    ('K-018', C, 'n=9,16,23,30 rebuilt from the printed gadget: positive free margin-one support, order of chi 2*256^k; other n not checked' + F),
    ('K-019', C, 'n=9: fixed dimension 1 at order 512, 4 at order 256; discrete stabilizer not checked' + F),
    ('K-020', C, 'diagonal part for k<=4 and finiteness of the stabilizer (full Lie rank mod 1000003) for k<=3; discrete part and all k not checked' + F),
    ('K-021', P, 'confirmed given K-020: proof lines 29-104 read (block collapse, fixed-space and Lie counts, divisibility step)'),
    ('K-021', C, 'dimensions 1, 358, 2773, 9304 for every l<k<=4' + F),
    ('K-022', P, 'cancellation confirmed on proof lines 26-72 of 189; ring properties read in part'),
    ('K-022', C, 'M=8..64: two weights divisible by M, numerator vanishes to order 2; at M=8 series equals standard-monomial count to degree 47' + F),
    ('K-025', P, 'confirmed: lines 18-62 read; block sum with the k=3 tensor gives order 3*2^25'),
    ('K-025', C, 'frame critical, order-three element fixes it, 2^25 summand rebuilt' + F),
    ('R-DIAG-001', P, 'confirmed: lines 1-78 of 107 read (presentation, fixed planes, free cyclic action)'),
    ('R-DIAG-001', C, 'Laurent coefficients 1/6 and 5/24 recomputed exactly' + F),
    ('K-027', C, 'necessary congruence holds at n=4 only (total minus chain residue divisible by 3); proof not read' + F),
    ('K-033', C, 'printed series equals printed coefficient polynomial to a=39; that it is the component series not checked' + F),
    ('K-037', C, 'Lemma K-037a at rho=0.5, 0.9: reduced matrices and order-three element; the theorem not checked' + F),
    ('PNEW-015', C, 'exponent 1/12-1/32=5/96 only; proposition proofs not checked' + F),
    ('PNEW-016', P, '(a),(b) confirmed on the lines read (18-22, 31-125, 141-169); (c) confirmed given PNEW-015 and K-024 (170-305); decides neither PH2 nor SH(a)'),
    ('PNEW-016', C, 'constants 17/240, the threshold inequalities at 79004 and the n^3/5 inequality at 2000 recomputed exactly' + F),
]
for sid in ('K-026', 'K-027', 'K-028', 'K-029', 'K-030', 'K-031', 'K-032', 'K-033', 'K-034', 'K-035', 'K-036', 'K-037', 'K-038',
            'PNEW-014', 'PNEW-015'):
    mine.append((sid, B, 'statement read (in part where the intake says so); proof not checked'))
out += [(s, DAY, ME, t, o) for s, t, o in mine]
dst = D / 'field_experts/intake_20261121/intakes/GCT_POS/INTAKE_GCT_POS_20261122_final_CHECK_EVENTS.tsv'
assert all(len(r) == 5 and all(TAB not in x for x in r) for r in out)
dst.write_text(NL.join(TAB.join(r) for r in out) + NL, encoding='utf-8', newline=NL)

ids = {r[0] for r in out}
new = ['K-0%d' % i for i in range(21, 39)] + ['R-NEW-004', 'R-DIAG-001'] + ['PNEW-0%d' % i for i in range(13, 17)]
print('events', len(out) - 1, '| new findings', len(new), '| without an event:', [x for x in new if x not in ids])

note = """- GCT_POS FINAL intake WRITTEN: intakes/GCT_POS/INTAKE_GCT_POS_20261122_final.md + _CHECK_EVENTS.tsv.
  24 new findings: 5 confirmed here (K-021, K-022, K-025, R-DIAG-001, PNEW-016), 4 with the main session's check, 15 carried.
  Changed: numerical PH3 Kronecker refuted; K-018 n=9,16,23,30; K-019/K-020 partly confirmed; K-002/K-008 completeness closed (k008_complete.py).
  Open: r=0, PH2, SH(a). Erratum 1.6.7 -> 3.3.4 (cause partly my core 52). No code of the return run in this intake.
"""
for n in ('a0805369bae2ebddc_NOTES.md',):
    with (D / 'agent_notes' / n).open('a', encoding='utf-8', newline=NL) as fh:
        fh.write(note)
(D / 'agent_notes/20261121_intake_GCT_PLETH_ALPOGE_GCT_NOTES.md').write_bytes((D / 'agent_notes/a0805369bae2ebddc_NOTES.md').read_bytes())
