#!/usr/bin/env python3
"""Merge explicit author check/source records without upgrading their status."""
from pathlib import Path
import csv
import re
import shutil

ROOT=Path(__file__).resolve().parent.parent
WORK=ROOT.parent.parent/'work'
if not WORK.exists(): WORK=ROOT/'work'

def entries(text):
    for part in re.split(r'(?=@\w+\s*\{)',text):
        key=re.match(r'@\w+\s*\{\s*([^,]+),',part)
        if key: yield key.group(1),part.strip()

bibpath=ROOT/'RESEARCH_SA07_references.bib'
original=bibpath.read_text()
known=dict(entries(original))
added=[]
for source in sorted(WORK.glob('*references.bib')):
    for key,entry in entries(source.read_text()):
        if key not in known:
            known[key]=entry
            added.append(entry)
if added: bibpath.write_text(original.rstrip()+'\n\n'+'\n\n'.join(added)+'\n')
print('Added bibliography entries:',len(added))

eventpath=ROOT/'CHECK_EVENTS.tsv'
with eventpath.open() as file: current=list(csv.reader(file,delimiter='\t'))
header=current[0]
rows=current[1:]
seen={tuple(r) for r in rows}
valid={'targeted proof check','independent re-proof','computation or formal certificate',
       'used and rechecked in this run','carried as background without fault found',
       "refuted, with the refined statement's id"}
sources=[WORK/'additional_source_CHECK_EVENTS.tsv',WORK/'agent_elliptic_check_events.tsv',
         WORK/'generation_check_events.tsv',WORK/'triangle_comparison_audit_CHECK_EVENTS.tsv',
         WORK/'audit_next_CHECK_EVENTS.tsv',WORK/'audit_postcheckpoint_CHECK_EVENTS.tsv',
         WORK/'audit_after04_CHECK_EVENTS.tsv',WORK/'audit_after05_CHECK_EVENTS.tsv',
         WORK/'audit_after06_CHECK_EVENTS.tsv',WORK/'audit_after07_CHECK_EVENTS.tsv',
         WORK/'audit_after08_CHECK_EVENTS.tsv',
         WORK/'audit_after09_CHECK_EVENTS.tsv',
         WORK/'audit_after10_CHECK_EVENTS.tsv',
         WORK/'audit_after10b_CHECK_EVENTS.tsv',
         WORK/'unrestricted_CHECK_EVENTS.tsv',
         WORK/'root_postcheckpoint03_CHECK_EVENTS.tsv']
for source in sources:
    if not source.exists(): continue
    with source.open() as file: incoming=list(csv.reader(file,delimiter='\t'))[1:]
    for row in incoming:
        if not row: continue
        assert len(row)==5,(source,row)
        assert row[3] in valid,(source,row)
        if tuple(row) not in seen:
            rows.append(row);seen.add(tuple(row))
with eventpath.open('w',newline='') as file:
    writer=csv.writer(file,delimiter='\t',lineterminator='\n')
    writer.writerow(header);writer.writerows(rows)
print('Check events:',len(rows))

for name in ['audit_claims.csv','audit_claims.md','audit_claims_coverage.json',
             'triangle_comparison_audit_source_checks.csv',
             'audit_postcheckpoint_source_checks.csv',
             'audit_postcheckpoint_validation.json',
             'audit_after04_source_checks.csv','audit_after04_validation.json',
             'audit_after04_computation_records.json',
             'audit_after05_source_checks.csv','audit_after05_validation.json',
             'audit_after05_computation_records.json',
             'audit_after06_source_checks.csv','audit_after06_validation.json',
             'audit_after06_computation_records.json',
             'audit_after07_source_checks.csv','audit_after07_validation.json',
             'audit_after07_computation_records.json',
             'audit_after08_source_checks.csv','audit_after08_validation.json',
             'audit_after08_computation_records.json',
             'audit_after09_source_checks.csv','audit_after09_validation.json',
             'audit_after09_computation_records.json',
             'audit_after10_source_checks.csv','audit_after10_validation.json',
             'audit_after10_computation_records.json',
             'audit_after10b_source_checks.csv','audit_after10b_validation.json',
             'audit_after10b_computation_records.json',
             'generation_after10_source_checks.csv','unrestricted_source_checks.csv']:
    source=WORK/name
    if source.exists(): shutil.copy2(source,ROOT/name)
print('Copied current assertion inventory and comparison source table.')
