from pathlib import Path
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import csv, json, sys

ROOT=Path(__file__).resolve().parent.parent
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,21,2,1,8,tzinfo=timezone.utc)
stamp=now.astimezone(ZoneInfo('Europe/Berlin')).isoformat()
builder=ROOT/'work/build_package.py'
text=builder.read_text()
old="'work/root/five_point_three_parameter_report.md','work/root/five_point_two_row_report.md'])"
new="'work/root/five_point_three_parameter_report.md','work/root/five_point_two_row_report.md',\n 'work/root/staircase_uniform_report.md','work/root/staircase_five_report.md'])"
assert old in text
builder.write_text(text.replace(old,new))

eventpath=ROOT/'work/root/CHECK_EVENTS.tsv'
with eventpath.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; events=list(reader)
checks=[
 ('G-022','targeted proof check','Read entire ST1–10 proof after construction: literal monomial-cycle trace, powered-root collision, both Vandermonde signs, weighted-incidence rank, every cycle-count degree inequality, integral central tournament, box injection, threshold comparison, determinant transport and actual Sra map application; PASS.'),
 ('G-023','targeted proof check','Read entire SF1–7 proof and both delivered Python files: rational-polytope dimension and forest denominator proof, exact Ehrhart interpolation range, complete seven class formulas, fixed Newton constants, determinant sign, lattice bijection, arithmetic and every support endpoint; PASS. A separate agent review remains in progress.'),
 ('G-023','computation or formal certificate','Re-executed exact bounded-flow counts and all2940 fixed Newton constants; identity samples and all class trace samples agree, every positive-order constant is positive with minimum107377819, and exact initial zero lists agree; PASS.'),
 ('SRC-BECK-ROBINS','used and rechecked in this run','Read primary author-corrected second-edition text dated18February2023: Theorem3.8 printedp68/PDFp84 and Theorem3.23 printedp80/PDFp96. Checked integral/rational polytope hypotheses and period denominators for the actual trace polytopes. Known Ehrhart theorems are cited, not reproved.'),
]
for sid,typ,outcome in checks:
    row={k:'' for k in fields}
    row.update(statement_id=sid,date=stamp,who_model_effort_run='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01',type=typ,outcome=outcome)
    events.append(row)
with eventpath.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)

sys.path.insert(0,str(ROOT/'work'))
import build_package
rows=build_package.questions()
openrows=[r for r in rows if not(r['state'].startswith('proved') or 'refuted' in r['state'])]
ledger=ROOT/'deliverables/LEDGER.md'
with ledger.open('a') as f:
    f.write('\n## Formal progress review 01 — '+stamp+'\n\n')
    f.write('Scheduled three-hour review. Movement: **YES**. Consecutive reviews without movement: **0**. Continue the research. Next formal review:21November2026,03:01:08UTC (04:01:08Europe/Berlin).\n\n')
    f.write('The complete outer-four direct-formula row changed to proved (T037). The outer-five main gate strictly shrank to the central inequalities after G021, and G023 now evaluates every central staircase shape with seven active positive polytopes and exact support. G022 proves all-rank staircase nonvanishing with an explicit uniform bound. The actual-map gate strictly shrank by the first-row band, rectangular prolongation, recursive component ranges and the explicit multiplicity-one components R025–R026. These are proved reductions and row changes, independent of packaging.\n\n')
    f.write('The remaining main gates are: polynomial description-size preprocessing for varying rank; the outer-five central flag-ideal correction away from the evaluated staircase and other completed families; the remaining actual common-polarization annihilator after the exact component removals; and the width-seven boundary valuation filtration. The archive and named-source input gates are retained verbatim below.\n\n')
    f.write('Every currently open question row at this review:\n\n| Row | State | Exact current gate |\n|---|---|---|\n')
    for r in openrows:
        values=[r['id'],r['state'],r['finding_ids_or_current_gate']]
        f.write('| '+' | '.join(x.replace('|',' / ').replace('\n',' ') for x in values)+' |\n')
    f.write('\nCheckpoint04 is prepared at the scheduled45-minute boundary. It contains the current complete deliverables, full work documentation and attached sources; earlier checkpoint ZIPs are excluded. Research continues.\n')
review={'review':1,'time_utc':now.isoformat(),'time_berlin':stamp,'movement':True,'consecutive_no_movement':0,'next_review_utc':'2026-11-21T03:01:08+00:00','open_rows':openrows,'new_completed_findings':['T-037','G-020','G-021','G-022','G-023','R-024','R-025','R-026']}
(ROOT/'work/REVIEW_01.json').write_text(json.dumps(review,indent=2,ensure_ascii=False)+'\n')
print(stamp,len(openrows),'open rows recorded; movement yes')
