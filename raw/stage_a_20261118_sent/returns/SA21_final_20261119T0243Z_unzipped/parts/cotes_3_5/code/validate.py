"""Final mechanical integrity audit; not a mathematical proof checker."""
from pathlib import Path
import json,csv,re,collections,datetime
R=Path(__file__).resolve().parents[1]
C=json.loads((R/'claims.json').read_text());P=json.loads((R/'problems.json').read_text())
required={'id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'}
bib=set(re.findall(r'@\w+\{([^,]+),',(R/'references.bib').read_text()))
assert len(C)==99 and len(P)==36
assert len({c['id'] for c in C})==99
for c in C:
 assert required<=set(c),c['id'];assert c['class'] in 'ABCDEF',c['id'];assert 'PENDING' not in str(c),c['id']
 assert c['refs'] and set(c['refs'])<=bib,(c['id'],set(c['refs'])-bib)
def table(name):
 with (R/name).open() as f:return list(csv.DictReader(f,delimiter='\t'))
coverage=table('coverage.tsv');readings=table('readings.tsv');links=table('links.tsv');search=table('search_log.tsv');events=table('check_events.tsv')
assert len(coverage)==22 and len(readings)==31 and len(links)==35
searched=set()
for row in search:searched.update(row['claim_ids'].split(';'))
assert {c['id'] for c in C}<=searched,{c['id'] for c in C}-searched
assert {c['id'] for c in C}<={e['statement_id'] for e in events}
proof_text=(R/'proof_checks.md').read_text()
refutation_rows=[e for e in events if e['type'].startswith('refuted')]
for e in refutation_rows:
 rid=e['outcome'].split(';',1)[0]
 assert rid.startswith(('C-SA21-','R-SA21-')),(e['statement_id'],rid)
 assert rid in proof_text,(e['statement_id'],rid)
 assert 'refinement/hypothesis restriction in this claim' not in e['outcome']
 if '#' in e['statement_id']:assert e['statement_id'] in proof_text
assert not any(e['statement_id'] in {'C-SA21-4-035','C-SA21-4-039','C-SA21-5-026','C-SA21-3-020','C-SA21-3-024'} for e in refutation_rows)
named_refinements={e['statement_id'] for e in events if e['statement_id'].startswith('R-SA21-')}
assert len(named_refinements)==8
out={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'validation':'passed','claims':len(C),'classes':dict(collections.Counter(c['class'] for c in C)),'problems':len(P),'folders':len(coverage),'scans':sum(len(x['scan_markers'].split(',')) for x in coverage),'readings':len(readings),'links':len(links),'search_groups':len(search),'check_events':len(events),'unsearched_claims':[],'meaning':'Schema, coverage and searched-fate/event mappings only; independent proofs and finite certificates are separate.'}
(R/'outputs/validation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
with (R/'progress.log').open('a') as f:f.write(out['at']+'\tFinal integrity audit passed; II→III link added; III–V artifacts stable.\n')
