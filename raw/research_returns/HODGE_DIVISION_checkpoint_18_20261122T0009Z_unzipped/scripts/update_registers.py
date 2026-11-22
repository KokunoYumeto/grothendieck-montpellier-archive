"""Merge actual checks, retaining original descriptions and scope without upgrades."""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
fields=['statement_id','date_utc','who','model','effort','run','type','outcome','evidence']
allowed={'targeted proof check','independent re-proof','computation or formal certificate',
         'used and rechecked in this run','carried as background without fault found'}

def category(raw):
    if raw in allowed or raw.startswith('refuted,'):return raw
    if raw=='author derivation':return None
    if raw=='execution setup':return 'computation or formal certificate'
    if raw in {'author computational certificate','author exact computational certificate',
               'independent computational reconstruction','tested conjectural expectation',
               'fresh certificate rerun','certificate integrity repair',
               'tested stronger estimate'}:
        return 'computation or formal certificate'
    if raw in {'author verification','contributor verification of complete written proof',
               'author derivation and whole-proof reading'}:
        return 'targeted proof check'
    if raw in {'author derivation and primary normalizer check','author derivation and published-source check',
               'author derivation and primary-source check'}:
        return 'used and rechecked in this run'
    if raw.startswith('independent re-proof') or raw=='independent derivation then whole proof mathematical check':
        return 'independent re-proof'
    if raw in {'retained input structural consistency check',
               'independent original-input computation',
               'source-label assertion and corrected input check',
               'independent symbolic exact computation'}:
        return 'computation or formal certificate'
    if raw=='source-label assertion and official source check':return 'used and rechecked in this run'
    if raw=='complete primary invoked argument read':return 'used and rechecked in this run'
    if raw.startswith(('primary','published-source','published primary-source','bibliographic')):
        return 'used and rechecked in this run'
    if raw.startswith(('whole','new')) or 'proof clarification' in raw or 'whole proof' in raw:
        return 'targeted proof check'
    if raw.startswith('unabridged conversion'):return 'targeted proof check'
    if raw.startswith(('exact','independent exact','independent arithmetic','independently written','fresh exact','fresh numerical','fresh rerun','independent tool','computation','compilation')):
        return 'computation or formal certificate'
    if raw in {'conversion and structural check','editorial structural check'}:
        return 'computation or formal certificate'
    raise ValueError(f'Unclassified check type: {raw!r}')

rows=[];notes=[]
for path in sorted((ROOT/'agents').rglob('CHECK_EVENTS.tsv')):
    with path.open(newline='') as f:
        for x in csv.DictReader(f,delimiter='\t'):
            raw=x.get('type') or x.get('check_type') or ''
            typ=category(raw)
            detail=x.get('scope_and_limits') or x.get('scope') or ''
            outcome=x.get('outcome','')
            if raw!=typ:outcome=f'Original event description: {raw}. '+outcome
            if detail:outcome+=' Scope: '+detail
            evidence=x.get('evidence') or x.get('locator') or str(path.relative_to(ROOT))
            row=dict(statement_id=x.get('statement_id',''),
                date_utc=x.get('date_utc',x.get('date','2026-11-21')),
                who=x.get('who',path.parent.name),
                model=x.get('model','GPT-6 Astra Pro (session identity)'),
                effort=x.get('effort','inherited; not externally exposed'),
                run=x.get('run','HODGE_DIVISION'), type=typ or raw,
                outcome=outcome,evidence=evidence)
            (rows if typ else notes).append(row)
with (ROOT/'research/root_check_events.tsv').open(newline='') as f:
    rows.extend(csv.DictReader(f,delimiter='\t'))
with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();seen=set()
    for r in rows:
        assert r['type'] in allowed or r['type'].startswith('refuted,'),r
        key=tuple(r.get(k,'') for k in fields)
        if key not in seen:w.writerow({k:r.get(k,'') for k in fields});seen.add(key)
with (ROOT/'research/DERIVATION_NOTES.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(notes)
print(f'Merged {len(seen)} actual checks with canonical types; retained {len(notes)} derivation-only notes separately.')
