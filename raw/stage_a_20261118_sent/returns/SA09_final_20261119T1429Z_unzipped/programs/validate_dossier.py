#!/usr/bin/env python3
"""Structural, provenance and reproducibility checks for the finished dossier.

This validator does not infer any semantic verdict, truth value or fate class.
The authored source reviews and proof audits are the evidence for those.
"""
import csv,hashlib,json,re,sys
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path

R=Path(__file__).resolve().parents[1]
S=R.parent/'source'
failures=[];warnings=[];checks=[]
def check(condition,label,detail=None):
 checks.append({'check':label,'passed':bool(condition)})
 if not condition:failures.append({'check':label,'detail':detail})
def js(name):return json.loads((R/name).read_text())
def tsv(name):return list(csv.DictReader((R/name).open(),delimiter='\t'))

required=['SA09_dossier.md','SA09_entries.tsv','SA09_items.json','SA09_claims.json',
 'SA09_problems.json','SA09_readings.tsv','SA09_links.tsv','SA09_directions.md',
 'SA09_references.bib','CHECK_EVENTS.tsv','progress.log']
check(all((R/n).is_file() and (R/n).stat().st_size>0 for n in required),'All requested deliverables exist')
E=tsv('SA09_entries.tsv');I=js('SA09_items.json');C=js('SA09_claims.json');P=js('SA09_problems.json')
index=list(csv.DictReader((S/'SA09_notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
expected=Counter(r['entry_id'] for r in index)
check(len(E)==380 and Counter(e['entry_id'] for e in E)==expected,'Exactly the 380 indexed entries, each once')
check(Counter(s for i in I for s in i['sources'])==expected,'Item sources partition the complete index')
IDs={x['id']:x for x in I};CIDs={x['id']:x for x in C};PIDs={x['id']:x for x in P}
check(len(IDs)==len(I)==252 and len(CIDs)==len(C)==216 and len(PIDs)==len(P)==73,'Unique canonical item, claim and problem IDs')
fields={
 'SA09_items.json':'id sources kind cote scans lines his_words statement reconstruction check check_reason'.split(),
 'SA09_claims.json':'id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split(),
 'SA09_problems.json':'id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split()}
for name,names in fields.items():
 bad=[x['id'] for x in js(name) if set(x)!=set(names)]
 check(not bad,'Exact requested schema: '+name,bad)
check(all(e['item_id'] in IDs and e['entry_id'] in IDs[e['item_id']]['sources'] and e['reason'] for e in E),'Every verdict resolves to its item and has a reason')
check(set(e['verdict'] for e in E)<=set(['kept','merged','corrected','withdrawn','rests on a misreading']),'Canonical verdict vocabulary')
check(all(set(c['items'])<=set(IDs) for c in C),'Claim-to-item references resolve')
check(all(c['class'] in 'ABCDEF' and c['confidence'] in ['high','medium','low'] for c in C),'Fate classes and confidence use requested vocabulary')
check(all(all(c[k] for k in fields['SA09_claims.json'] if k!='items') for c in C),'Every claim has statement, page status, computation record, searched fate, date and references')
empty_items=[c['id'] for c in C if not c['items']]
check(all(c.startswith('CL-SA09-137-') for c in empty_items),'Claims without indexed items are confined to the unindexed source packet/provenance record',empty_items)
check(all(all(p[k] for k in fields['SA09_problems.json']) for p in P),'Every problem has all requested substantive fields')

# Bibliographic entries are deliberately parsed only at entry/field boundaries;
# no citation is treated as verified merely because a DOI-shaped string exists.
bibtext=(R/'SA09_references.bib').read_text()
bib={}
for part in re.split(r'(?m)(?=^@)',bibtext):
 m=re.match(r'@\w+\{([^,]+),',part)
 if m:
  check(m.group(1) not in bib,'Unique bibliography key '+m.group(1))
  bib[m.group(1)]=part
used={r.split(':',1)[0].strip() for c in C for r in c['refs']}|{r.split(':',1)[0].strip() for p in P for r in p['refs']}
check(used<=set(bib),'Every claim/problem reference exists in the bibliography',sorted(used-set(bib)))
check(all(re.search(r'\bnote\s*=\s*\{(?:verified|unverified)\}',part) for part in bib.values()),'Every reference has the required verified/unverified note')
check(all(re.search(r'\b(?:url|doi)\s*=',part) for part in bib.values()),'Every bibliography record has an opened/attempted locator')

events=tsv('CHECK_EVENTS.tsv');event_ids={r['statement id'] for r in events}
check(set(IDs)|set(CIDs)|set(bib)<=event_ids,'Every item, claim and reference has a check event',sorted((set(IDs)|set(CIDs)|set(bib))-event_ids))
check(all(all(r.values()) for r in events),'Every event records statement, date, actor, type and outcome')
event_types=['targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found']
check(all(r['type'] in event_types or r['type'].startswith('refuted, with') for r in events),'Event types describe the actual allowed check categories')

coverage=tsv('SA09_claim_search_coverage.tsv')
check(set(r['claim_id'] for r in coverage)==set(CIDs),'Every canonical claim has recorded literature searches')
for worker in ['cote137','cote138_early','cote138_middle','cote138_late']:
 d=R/'workers'/worker
 cs=json.loads((d/'claims.json').read_text())
 if worker=='cote137':
  searches=list(csv.DictReader((d/'search_log.tsv').open(),delimiter='\t'))
  ok=all(any(c['id'] in r['claim_ids'].split(';') and r['query'] and r['result'] for r in searches) for c in cs)
 elif worker=='cote138_middle':
  searches=json.loads((d/'search_log.json').read_text())
  ok=all(any(c['id'] in r['claim_ids'] and r['queries'] and r['outcome'] and r['services'] for r in searches) for c in cs)
 else:
  searches=list(csv.DictReader((d/'search_log.tsv').open(),delimiter='\t'))
  search_ids={r['claim_id'] for r in searches}
  ok={c['id'] for c in cs}<=search_ids and all(r.get('queries') and (r.get('outcome') or r.get('exact_result')) for r in searches)
 check(ok,'Nonempty actual claim-level search records: '+worker)
check(all((R/r['record_file']).is_file() and r['search_records'] for r in coverage),'Search coverage pointers resolve to saved records')

# Source integrity and named line bounds, independent of the mathematical
# correctness of any proposed alternative reading.
manifest=tsv('source_manifest.tsv')
hash_bad=[];source_cache={}
for row in manifest:
 p=S/row['path']
 if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:hash_bad.append(row['path'])
 if p.name.endswith('_transcription.tex'):
  lines=p.read_text().splitlines();at={};scan=None
  for no,line in enumerate(lines,1):
   m=re.search(r'\\scanpage\{(\d+)\}',line)
   if m:scan=int(m.group(1))
   at[no]=scan
  source_cache[p.name]=(lines,at)
check(not hash_bad,'Every supplied source file matches its initial SHA-256',hash_bad)
locpat=re.compile(r'(MPL_\d{3}_\d{3}-\d{3}_transcription\.tex):(\d+(?:[–-]\d+)?(?:\s*,\s*\d+(?:[–-]\d+)?)*)')
loc_checks=0;loc_fail=[];scan_notes=[]
def checkloc(text,owner,declared=None):
 global loc_checks
 for match in locpat.finditer(text):
  name,ns=match.groups()
  if name not in source_cache:loc_fail.append([owner,name,'unknown file']);continue
  lines,at=source_cache[name]
  actual=set()
  for part in ns.split(','):
   parts=re.split('[–-]',part.strip());a=int(parts[0]);z=int(parts[-1]);loc_checks+=1
   if not 1<=a<=z<=len(lines):loc_fail.append([owner,match.group(),len(lines)])
   else:actual.update(at[n] for n in range(a,z+1) if at[n] is not None)
  if declared is not None:
   declared=set(map(int,declared))
   if actual-declared:scan_notes.append({'owner':owner,'locator':match.group(),'additional_scans_in_range':sorted(actual-declared)})
for obj in I+C:
 for loc in obj['lines']:checkloc(loc,obj['id'],obj['scans'])
 if obj in C:check(bool(locpat.search(' '.join(obj['lines']))),'Named manuscript locator: '+obj['id'])
for p in P:checkloc(json.dumps(p['occurrences'],ensure_ascii=False),p['id'])
readings=tsv('SA09_readings.tsv')
for n,r in enumerate(readings,1):checkloc(r['line'],'reading-'+str(n))
check(not loc_fail,'All named manuscript line ranges lie inside unchanged sources',loc_fail)
check(not scan_notes,'Scan lists cover all scan markers crossed by named item/claim line ranges',scan_notes)
check(len(readings)==173 and all(all(r.values()) for r in readings),'All 173 reading alarms have evidence and qualified alternatives')

# Complete explicit identifiers in authored records must resolve. Compact
# displayed ranges are supplemented by the complete JSON/TSV identity maps.
aliases={r['from_id']:r['to_id'] for r in tsv('SA09_id_aliases.tsv')}
allids=set(IDs)|set(CIDs)|set(PIDs)
idpat=re.compile(r'(?<![A-Za-z0-9_-])(?:CL-SA09-(?:137|138[EML])-\d{3}|MP-SA09-\d+|SA09-\d+)(?![A-Za-z0-9_-])')
dangling=[]
for name in ['SA09_items.json','SA09_claims.json','SA09_problems.json','SA09_directions.md']:
 for found in set(idpat.findall((R/name).read_text())):
  if aliases.get(found,found) not in allids:dangling.append([name,found])
check(not dangling,'Every explicit item/claim/problem cross-reference resolves',dangling)
directions=(R/'SA09_directions.md').read_text()
parts=re.split(r'(?m)^## (?=D\d+\.)',directions)[1:]
check(len(parts)==12,'Twelve ranked global research directions')
check(all(re.search(r'(?<![-A-Za-z])SA09-\d+',p) and 'CL-SA09-' in p and 'MP-SA09-' in p for p in parts),'Every direction cites item, claim and problem IDs')

groups=tsv('claim_status_groups.tsv')
check(Counter(r['claim_id'] for r in groups)==Counter(CIDs.keys()),'Counts-only status map covers canonical claims exactly once')
check(all(r['grouping_reason'] and r['original_status'] for r in groups),'Status grouping retains its authored qualifications and reasons')

links=tsv('SA09_links.tsv');leads=tsv('SA09_project_leads.tsv')
check(all(set(r)=={'kind','from','to','what','evidence','note_ids'} and all(r.values()) for r in links+leads),'Link and original-lead rows have the requested complete schema')
check(all(r['kind'] in ['folder','published work','our projects'] for r in links+leads),'Link kinds are canonical')
check(all(r['kind']=='our projects' for r in tsv('SA09_project_links.tsv')),'Checked external-project correspondences have their separate table')

computed=js('workers/cote138_middle/outputs/computations.json')
needed={'dihedral','cubic','odd_power','conic_models','groupoid_corollary_counterexample','bipyramid_product','tame_spherical_signatures','kummer_basechange','unit_vs_cyclic_action_n5','reversal','orientation_ranks'}
check(needed<=set(computed),'Corrected middle computation-key pointers exist')
program_outputs={
 'workers/cote137/programs/recompute.py':'workers/cote137/outputs/recompute.json',
 'workers/cote138_early/programs/computations.py':'workers/cote138_early/outputs/computations.json',
 'workers/cote138_middle/programs/compute_middle.py':'workers/cote138_middle/outputs/computations.json',
 'workers/cote138_late/programs/exact_arithmetic.py':'workers/cote138_late/outputs/exact_arithmetic.json',
 'workers/cote138_late/programs/finite_maps.py':'workers/cote138_late/outputs/finite_maps_all.json',
 'workers/cote138_late/programs/catalogue_checks.py':'workers/cote138_late/outputs/catalogue_checks.json'}
for program,out in program_outputs.items():
 check((R/program).is_file() and (R/out).is_file(),'Retained computation and output: '+program)
 js(out)
counts=js('counts.json')
check(sum(counts['verdicts'].values())==380 and sum(counts['item_kinds'].values())==252 and sum(counts['claim_classes'].values())==216,'Summary counts reconcile exactly')
text=(R/'SA09_dossier.md').read_text()
check('{{COUNT_TABLES}}' not in text and '{{' not in text,'Final dossier has no unfilled placeholders')
check('claim_status_groups.tsv' in text,'Overview explains qualified page-status counts')

report={'validated_utc':datetime.now(timezone.utc).isoformat(),'passed':not failures,
 'scope':'Structural and provenance validation only; semantic judgments were individually authored from source reading and proof/literature checks.',
 'counts':{k:counts[k] for k in ['entries','items','claims','problems','readings','links','reported_project_leads','references','check_events','directions']},
 'source_files_unchanged':len(manifest) if not hash_bad else False,'named_line_ranges_checked':loc_checks,
 'source_range_scan_notes':scan_notes,'claims_without_indexed_note_items':empty_items,
 'checks_passed':sum(r['passed'] for r in checks),'checks_total':len(checks),'failures':failures,'warnings':warnings,
 'checks':checks,'runtime':{'python':sys.version}}
(R/'VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['checks','claims_without_indexed_note_items']},ensure_ascii=False,indent=2))
raise SystemExit(0 if not failures else 1)
