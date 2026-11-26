#!/usr/bin/env python3
"""Consolidate working inventories without upgrading historical evidence.

Run from the enclosing deliverable directory:
    python workbench/programs/consolidate_records.py
Canonical per-paper registers take precedence when available. Unreconciled
report aliases are explicitly labelled; this program is not a proof checker.
"""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[2]
REC = ROOT/'workbench/records'
FIELDS = ['id','aliases','statement','exact_statement','source_status',
          'proof_file','historical_checks','current_checks','literature_status',
          'paper','current_gate','record_kind','related_ids','register_sources','registration_note']

def read(path):
    with path.open(encoding='utf-8') as f:
        return list(csv.DictReader(f,delimiter='\t'))

def write(path, fields, rows):
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n',extrasaction='ignore')
        w.writeheader();w.writerows(rows)

def normpath(s):
    return s.removeprefix('source/')

def main():
    inventories=[REC/'paper_1/REGISTER.tsv',REC/'paper_4/REGISTER.tsv',REC/'papers_5_6/REGISTER.tsv',REC/'ROOT_REGISTER.tsv']
    combined=REC/'papers_2_3/REGISTER.tsv'
    if combined.exists():
        inventories.append(combined)
    else:
        inventories += [REC/'papers_2_3/REGISTER_THEOREM_BLOCKS.tsv', REC/'papers_2_3/REGISTER_REPORT_ROWS.tsv']
    rows=[]
    for p in inventories:
        if not p.exists():continue
        for x in read(p):
            exact=x.get('exact_statement_tex',x.get('exact_statement',x.get('statement',x.get('statement_or_gate',''))))
            stmt=x.get('statement',x.get('statement_or_gate',x.get('title','')))
            if not stmt:stmt=exact
            proof=normpath(x.get('proof_file',x.get('proof_locator','')))
            if x.get('line') and ':' not in proof:proof+=':'+x['line']
            if x.get('source_line') and ':' not in proof:proof+=':'+x['source_line']
            hist='; '.join(x[k] for k in ['run_check_events','intake_check_events','source_checks','intake_checks','check_events','historical_checks'] if x.get(k))
            note=('report/question row; alias reconciliation pending' if 'REPORT_ROWS' in p.name
                  else x.get('registration_note','reconstructed from current source; historical status is not current verification'))
            kind=x.get('record_kind','result_or_question')
            if kind=='report_result':
                note+='; report result not matched to a numbered theorem block; distinctness unresolved'
            rows.append(dict(id=x.get('id',x.get('statement_id','')),aliases=x.get('aliases',x.get('earlier_id','')),
                statement=stmt,exact_statement=exact,source_status=x.get('source_status',x.get('run_status','not supplied')),
                proof_file=proof,historical_checks=hist,
                current_checks=x.get('current_checks',x.get('current_check',x.get('current_status','see CHECK_EVENTS.tsv; not automatically verified'))),
                literature_status=x.get('literature_status','unsettled; no novelty claim'),paper=x.get('paper','unassigned'),
                current_gate=x.get('current_gate',x.get('gate','scope and current checks must be read in the per-paper records')),
                record_kind=kind,related_ids=x.get('related_ids',''),register_sources=x.get('register_sources',str(p.relative_to(ROOT))),
                registration_note=note))
    # Preserve rather than silently coalesce a collision between a report ID and
    # an independently labelled theorem until the responsible worker resolves it.
    seen=set()
    for r in rows:
        if r['id'] in seen:
            r['aliases'] += '; '+r['id'];r['id'] += ':REPORT_ALIAS_PENDING'
            r['registration_note']+='; duplicate spelling retained transparently'
        seen.add(r['id'])
    rows.sort(key=lambda r:r['id'])
    write(ROOT/'REGISTER.tsv',FIELDS,rows)
    ev=[]
    for p in sorted(REC.rglob('CHECK_EVENTS.tsv')):
        for x in read(p):
            ev.append(dict(statement_id=x.get('statement_id',x.get('id','')),
                           date=x.get('date',x.get('timestamp','2026-11-23')),
                           who=x.get('who',x.get('checker',x.get('model','not stated in this fragment'))),
                           type=x.get('type',x.get('check_type','not stated in this fragment')),
                           outcome=x.get('outcome',x.get('result','')),
                           evidence=x.get('evidence',x.get('record',str(p.relative_to(ROOT))))))
    write(ROOT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome','evidence'],ev)
    unresolved=sum('pending' in x['registration_note'] or 'distinctness unresolved' in x['registration_note'] for x in rows)
    print(f'Register: {len(rows)} rows (not a count of distinct certified theorems); current check events: {len(ev)}; unresolved report/alias rows: {unresolved}')

if __name__=='__main__':main()
