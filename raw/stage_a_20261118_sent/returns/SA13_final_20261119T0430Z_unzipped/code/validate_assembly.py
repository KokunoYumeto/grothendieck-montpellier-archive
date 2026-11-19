"""Structural audit of the authored dossier. This is not a mathematical proof."""
from pathlib import Path
from collections import Counter
import json,csv,re
R=Path(__file__).resolve().parents[2];D=R/'deliverable'
def J(n):return json.loads((D/n).read_text())
def T(n):return list(csv.DictReader((D/n).open(),delimiter='\t'))
items=J('SA13_items.json');claims=J('SA13_claims.json');problems=J('SA13_problems.json');entries=T('SA13_entries.tsv')
required={
 'item':'id sources kind cote scans lines his_words statement reconstruction check check_reason'.split(),
 'claim':'id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split(),
 'problem':'id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split()}
issues=[];warnings=[]
I={x['id'] for x in items};C={x['id'] for x in claims};P={x['id'] for x in problems}
aliases={x['alias']:x['canonical'] for x in T('SA13_aliases.tsv')}
def canonical(s):
 while s in aliases:s=aliases[s]
 return s
for kind,rs in [('item',items),('claim',claims),('problem',problems)]:
 for x in rs:
  missing=set(required[kind])-set(x)
  if missing:issues.append({'kind':'missing_fields','id':x['id'],'fields':sorted(missing)})
  for f in required[kind]:
   if f in x and x[f] is None:issues.append({'kind':'null_field','id':x['id'],'field':f})
for e in entries:
 if e['item_id'] not in I:issues.append({'kind':'entry_missing_item','entry':e})
for c in claims:
 for i in c['items']:
  if i not in I:issues.append({'kind':'claim_missing_item','id':c['id'],'item':i})
 if not c.get('search_ids'):issues.append({'kind':'claim_no_search','id':c['id']})
 if c['class'] not in list('ABCDEF'):issues.append({'kind':'claim_class','id':c['id'],'value':c['class']})
for p in problems:
 for key,ids in [('items',I),('claims',C),('claim_ids',C)]:
  for v in p.get(key,[]):
   if canonical(v) not in ids:issues.append({'kind':'problem_bad_link','id':p['id'],'field':key,'target':v})
 if not p['refs']:issues.append({'kind':'problem_without_source','id':p['id']})
source_index=list(csv.DictReader((R/'sources/notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
ids={r.get('entry_id') or r.get('id') for r in source_index}
actual=Counter(x['entry_id'] for x in entries)
if len(entries)!=379 or set(actual)!=ids or set(actual.values())!={1}:issues.append({'kind':'entry_coverage','total':len(entries),'missing':sorted(ids-set(actual)),'extra':sorted(set(actual)-ids)})
owners={}
for i in items:
 for s in i['sources']:
  if s in ids:owners.setdefault(s,[]).append(i['id'])
for e in entries:
 if owners.get(e['entry_id'])!=[e['item_id']]:issues.append({'kind':'source_provenance_mismatch','entry':e['entry_id'],'verdict_item':e['item_id'],'item_sources':owners.get(e['entry_id'])})
pages=json.loads((R/'work/pages.json').read_text());pageidx={(p['file'],int(p['cote']),int(p['scan'])):p for p in pages}
locators_checked=0
for kind,rs,field in [('item',items,'lines'),('claim',claims,'lines'),('problem',problems,'occurrences')]:
 for x in rs:
  for loc in x[field]:
   if not isinstance(loc,dict):issues.append({'kind':'locator_type','id':x['id'],'value':loc});continue
   if not all(k in loc for k in ['file','cote','scan','start','end']):
    warnings.append({'kind':'nonline_occurrence','id':x['id'],'value':loc});continue
   key=(loc['file'],int(loc['cote']),int(loc['scan']));p=pageidx.get(key)
   if not p:issues.append({'kind':'locator_page_missing','id':x['id'],'value':loc});continue
   locators_checked+=1
   if not (p['start']<=loc['start']<=loc['end']<=p['end']):issues.append({'kind':'locator_outside_scan','id':x['id'],'locator':loc,'page':[p['start'],p['end']]})
bib=(D/'SA13_references.bib').read_text();keys=set(re.findall(r'^@\w+\{([^,]+),',bib,re.M))
for x in claims+problems:
 for ref in x['refs']:
  if ref not in keys:issues.append({'kind':'missing_reference','id':x['id'],'ref':ref})
searches=set()
for path in (D/'shards').rglob('*search_log.tsv'):
 for r in csv.DictReader(path.open(),delimiter='\t'):
  if r.get('search_id'):searches.add(r['search_id'])
for c in claims:
 for s in c.get('search_ids',[]):
  if s not in searches:issues.append({'kind':'missing_search_row','id':c['id'],'search':s})
for c in claims:
 co=c['computation']
 if isinstance(co,dict):
  for key in ['proof','code','output']:
   if key in co:
    path=str(co[key]).split('#')[0]
    if not (D/path).is_file():issues.append({'kind':'missing_computation_file','id':c['id'],'field':key,'path':path})
events=T('CHECK_EVENTS.tsv');eventids={x['statement_id'] for x in events}
for x in items+claims:
 if x['id'] not in eventids:issues.append({'kind':'missing_check_event','id':x['id']})
for ref in sorted({r for x in claims+problems for r in x['refs']}):
 if ref not in eventids:warnings.append({'kind':'reference_without_separate_event','ref':ref})
allowedchecks={'agrees','overstates','understates','misreads','not on the page'}
for x in items:
 if x['check'] not in allowedchecks:issues.append({'kind':'item_check_enum','id':x['id'],'value':x['check']})
for e in events:
 if not e['outcome'].strip():issues.append({'kind':'empty_event','id':e['statement_id']})
report={'entries':len(entries),'items':len(items),'claims':len(claims),'problems':len(problems),'locators_checked':locators_checked,'reference_keys':len(keys),'search_groups':len(searches),'check_events':len(events),'issues':issues,'warnings':warnings,'issue_counts':dict(Counter(x['kind'] for x in issues)),'warning_counts':dict(Counter(x['kind'] for x in warnings)),'passed':not issues}
(D/'outputs/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['issues','warnings']},indent=2))
if issues:raise SystemExit(1)
