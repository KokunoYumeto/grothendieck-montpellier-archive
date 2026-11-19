"""Validate user-required table coverage, references and retained evidence files."""
from pathlib import Path
from collections import Counter
import csv,json,re
R=Path(__file__).resolve().parents[1];O=R/'work/early'
req={
 'items.json':'id sources kind cote scans lines his_words statement reconstruction check check_reason'.split(),
 'claims.json':'id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split(),
 'problems.json':'id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split()}
data={f:json.loads((O/f).read_text()) for f in req}
errors=[]
for f,fields in req.items():
 seen=set()
 for row in data[f]:
  if row['id'] in seen:errors.append(f'duplicate {f} {row["id"]}')
  seen.add(row['id'])
  for key in fields:
   if key not in row:errors.append(f'missing {key}: {row["id"]}')
items={x['id'] for x in data['items.json']}
claims={x['id'] for x in data['claims.json']}
refs=set(re.findall(r'@\w+\{([^,]+),',(O/'references.bib').read_text()))
allowed_status={'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages'}
for c in data['claims.json']:
 for i in c['items']:
  if i not in items:errors.append(f'{c["id"]} absent item {i}')
 if c['status_on_pages'] not in allowed_status:errors.append(f'invalid status {c["id"]}')
 for r in c['refs']:
  if r not in refs:errors.append(f'{c["id"]} absent ref {r}')
 if not c.get('search_logs'):errors.append(f'{c["id"]} no searched fate')
 for s in c.get('search_logs',[]):
  if not (R/s).is_file():errors.append(f'{c["id"]} absent log {s}')
for p in data['problems.json']:
 for r in p['refs']:
  if r not in refs:errors.append(f'{p["id"]} absent ref {r}')
entries=list(csv.DictReader((O/'entries.tsv').open(),delimiter='\t'))
index=list(csv.DictReader((R/'sources/notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
indexed=[x for x in index if any(str(v).startswith(('MPL_136_002-046','MPL_136_047-094')) for v in x.values())]
actual=Counter(x['entry_id'] for x in entries)
# User's exact index ID field is checked without inferring note verdicts.
index_ids={str(x.get('entry_id',x.get('id',''))) for x in indexed}
if not index_ids or '' in index_ids:
 # Earlier coverage file records original exact-ID matching; display headers for review.
 errors.append('unrecognized original index identifier field: '+repr(list(index[0])))
if set(actual)!=index_ids:errors.append('entry index mismatch: missing='+repr(sorted(index_ids-set(actual)))+' extra='+repr(sorted(set(actual)-index_ids)))
if any(v!=1 for v in actual.values()):errors.append('nonunique verdict entry')
for e in entries:
 if e['item_id'] not in items:errors.append('entry target missing '+e['entry_id'])
for name in ['readings.tsv','links.tsv','project_links.tsv','CHECK_EVENTS.tsv']:
 rows=list(csv.DictReader((O/name).open(),delimiter='\t'))
 if not rows:errors.append(name+' empty')
 if name in ['links.tsv','project_links.tsv']:
  for row in rows:
   for nid in row['note_ids'].split('; '):
    if nid not in actual:errors.append(name+' unknown note '+nid)
summary={'entries':len(entries),'items':len(items),'claims':len(claims),'problems':len(data['problems.json']),
 'verdicts':dict(Counter(e['verdict'] if not e['verdict'].startswith('merged') else 'merged' for e in entries)),
 'item_checks':dict(Counter(x['check'] for x in data['items.json'])),
 'item_kinds':dict(Counter(x['kind'] for x in data['items.json'])),
 'claims_by_class':dict(Counter(x['class'] for x in data['claims.json'])),
 'claims_by_status':dict(Counter(x['status_on_pages'] for x in data['claims.json'])),
 'bibliography_keys':len(refs),'search_logs':len([p for p in (R/'logs').glob('early_search_*.json') if p.name!='early_search_index_output.json']),'errors':errors}
for name in ['readings.tsv','links.tsv','project_links.tsv','CHECK_EVENTS.tsv']:
 summary[name]=len(list(csv.DictReader((O/name).open(),delimiter='\t')))
(O/'validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
