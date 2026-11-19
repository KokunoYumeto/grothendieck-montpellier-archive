from pathlib import Path
import csv, json, time

started = time.perf_counter()
root = Path('/workspace/scratch/6215ed17d0f0/RESEARCH_SA05_work')
path = root / 'part_c/results.csv'
with path.open(newline='') as handle:
    reader = csv.DictReader(handle)
    fields = reader.fieldnames
    rows = list(reader)
new_rows = [
    ('c:local-dimension', 'Inherited local dimension function, including the punctured-trait test', 'Proved', 'Definition', 'Dimension formula; Pilloni-Stroh 1.1.1 and 1.2.2', '12:120', 'Not the Krull dimension of a nonproper localized source.'),
    ('c:proper-level', 'Proper cohomology generated with t>=max(0,a-d) and r+2t<=a', 'Proved', 'Lemma', 'de Jong 7.3/7.4; Deligne Weil II 4.1.1; abstract blowup sequence', '12:113-120', 'Galois-quotient alteration and dimension induction preserve simultaneous bounds.'),
    ('c:general-level-bound', 'Corrected weight envelope and level bounds, including the margin condition', 'Proved under stated finite-type and dimension-normalized hypotheses', 'Theorem', 'c:proper-level; de Jong 4.1/8.2; Riou 3.1.2/3.1.4 and trace; Deligne1968 2.4', '12:118-120; R6', 'Level min(i,2n-i)+j; margin/open-boundary level min(i,2n-1-i)+j; weight <=2min(i,n)+2j.'),
    ('c:level-optimality', 'All level bounds are attained; constant-coefficient weights are attained and 2j is necessary', 'Proved in stated senses', 'Proposition', 'Ordinary elliptic slopes; cone Gysin sequence; Legendre Tate monodromy', '12:118-120', 'For j>0 the weight envelope is attained in interior degrees; endpoint improvement retains a local-invariant-cycle gate.'),
]
by_id = {row['id']: row for row in rows}
by_id['c:level-special-cases']['notes'] = 'Universal replacement and margin now proved in c:general-level-bound under its explicit scope.'
for ident, statement, status, kind, dependencies, pages, notes in new_rows:
    by_id[ident] = dict(zip(fields, [ident, statement, status, 'sections/part_c.tex, ' + kind + ' label ' + ident, dependencies, pages, notes]))
with path.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(by_id.values())

events_path = root / 'part_c/CHECK_EVENTS.tsv'
with events_path.open(newline='') as handle:
    reader = csv.DictReader(handle, delimiter='\t')
    event_fields = reader.fieldnames
    events = list(reader)
events_to_add = [(r[0], 'targeted proof check', r[2] + ': ' + r[-1]) for r in new_rows]
events_to_add += [
    ('c:proper-level', 'independent re-proof', 'GPT-6 Astra /root/part_b independently checked quotient alteration, abstract-blowup induction and the E-dimension drop.'),
    ('c:general-level-bound', 'independent re-proof', 'GPT-6 Astra /root/part_b independently checked boundary dimensions using the corrected inherited dimension function; /root caught and repaired the ordinary-Krull-dimension misidentification.'),
    ('c:general-level-bound', 'computation or formal certificate', '35681 exact finite optimization checks pass; check_c4_bounds_output.json, parameters n<=15 and i<=30.'),
    ('c:level-optimality', 'computation or formal certificate', 'Legendre discriminant/c4, split node over F5, symmetric-power N ranks j=0..30 and Frobenius compatibility all pass; check_c4_bounds_output.json.'),
    ('R6', 'used and rechecked in this run', 'Re-read 12:111-113 and 120: dimension clause is an uncertain insertion; level is geometric generation with simultaneous weight restrictions; proper correction and margin proved in explicit convention.'),
]
for ident, kind, outcome in events_to_add:
    event = dict(zip(event_fields, [ident, '2026-11-19', 'GPT-6 Astra (OpenAI), /root/part_c', kind, outcome]))
    if event not in events:
        events.append(event)
with events_path.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=event_fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(events)

report = {'result_rows': len(by_id), 'check_events': len(events), 'added_labels': [r[0] for r in new_rows], 'runtime_seconds': round(time.perf_counter()-started, 6)}
(root / 'code/part_c/update_c4_records_output.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
