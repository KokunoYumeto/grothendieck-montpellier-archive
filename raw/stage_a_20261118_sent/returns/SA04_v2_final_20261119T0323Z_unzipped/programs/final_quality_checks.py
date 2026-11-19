"""Read-only checks of the finished SA04 registers, plus validation-report output.

These checks do not assign source verdicts or infer mathematical truth. They
compare authored identifiers, schemas, source manifests and saved audit evidence.
"""
from pathlib import Path
import json,csv,re,hashlib,collections,datetime
W=Path(__file__).resolve().parents[1];F=W/'final';ROOT=W.parent
errors=[]
def require(condition,message):
 if not condition:errors.append(message)
def j(path):return json.loads(path.read_text())
def ts(path):return list(csv.DictReader(path.open(),delimiter='\t'))
required=['SA04_dossier.md','SA04_entries.tsv','SA04_items.json','SA04_claims.json','SA04_problems.json','SA04_readings.tsv','SA04_links.tsv','SA04_directions.md','SA04_references.bib','CHECK_EVENTS.tsv']
for name in required:require((F/name).is_file() and (F/name).stat().st_size>0,'missing required file '+name)
items=j(F/'SA04_items.json');claims=j(F/'SA04_claims.json');problems=j(F/'SA04_problems.json')
entries=ts(F/'SA04_entries.tsv');events=ts(F/'CHECK_EVENTS.tsv');readings=ts(F/'SA04_readings.tsv');links=ts(F/'SA04_links.tsv')
bib=(F/'SA04_references.bib').read_text();refs=set(re.findall(r'^@\w+\{([^,]+),',bib,re.M))
active={x['id'] for x in items+claims+problems}|refs
aliases={x['old_id']:x['canonical_id'] for x in ts(F/'ID_ALIASES.tsv') if ' -> ' not in x['old_id']}
assembly=j(W/'outputs/assembly_validation.json');require(assembly['passed'],'assembly validation failed')
require(len(entries)==432,'entry count differs from432')
index=ts(ROOT/'source/SA04_notes/NOTES_INDEX.tsv')
require(collections.Counter(x['entry_id'] for x in entries)==collections.Counter(x['entry_id'] for x in index),'index entry bijection failed')
required_events={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
for e in events:
 require(e['type'] in required_events,'noncanonical event type '+e['type'])
 require(e['statement_id'] in active,'orphan event '+e['statement_id'])
 require(bool(e['date']) and bool(e['who']) and bool(e['outcome']),'empty event field')
 if e['type'].startswith('refuted'):
  targets=re.findall(r'(?<![A-Za-z0-9-])(?:C-)?SA04-\d+',e['outcome'])
  require(bool(targets),'refutation has no explicit refined statement/item ID: '+e['statement_id'])
  for target in targets:require(target in active or target in aliases,'refutation target missing '+target)
coverage={e['statement_id'] for e in events}
for identifier in {x['id'] for x in items+claims}|refs:require(identifier in coverage,'no check event '+identifier)
# Claim-fate search coverage is separate from the event ledger.
search_paths=['parts/a/search_log.tsv','parts/b/search_log.tsv','parts/c/search_log.tsv','parts/root/claim_fate_audit.tsv','parts/b/root_supplement_search_log.tsv']
searched=set();search_rows={}
for relative in search_paths:
 rows=ts(W/relative);search_rows[relative]=len(rows)
 for row in rows:
  field=row.get('claim_ids',row.get('claims',row.get('claim_id','')))
  searched.update(re.findall(r'C-SA04-\d+',field))
searched={aliases.get(x,x) for x in searched}
missing_fates=sorted({x['id'] for x in claims}-searched)
require(not missing_fates,'claims without a searched-fate record '+str(missing_fates))
# Consume the independent exact-locator audit, which must describe these files.
audit=j(W/'outputs/c_final_register_audit.json')
for name,h in audit['hashes'].items():require(hashlib.sha256((F/name).read_bytes()).hexdigest()==h,'independent audit stale for '+name)
for key in ['orphan_event_ids','schema_identifier_errors','noncanonical_event_types','bad_source_intervals','unparsed_locators','empty_source_intervals','incomplete_target_locators','changed_during_read']:
 require(not audit[key],'independent audit issue: '+key)
for kind,missing in audit['missing_event_coverage'].items():require(not missing,'independent missing-event '+kind)
require(not any(x['missing'] for x in audit['scan_field_discrepancies']),'declared source scan not found in its cited ranges')
# Every reading has an actual numeric locator; prose alternatives remain undecided.
for r in readings:
 require(bool(re.search(r'\d',r['line'])),'reading lacks numeric locator '+str(r))
 for field in ['cote','scan','line','reading','alternative','evidence','weight','confidence']:require(bool(r[field]),'empty reading field '+field)
project=ts(F/'SA04_project_leads.tsv')
require(project==[x for x in links if x['kind']=='our projects'],'separate project-lead view differs from main link table')
# Main prose references are keyed to the delivered bibliography.
dossier=(F/'SA04_dossier.md').read_text();directions=(F/'SA04_directions.md').read_text()
require(len(dossier.split())>=5000,'overview unexpectedly short')
require(len(re.findall(r'^## \d+\.',directions,re.M))==30,'direction count differs from30')
unknown_citations=[]
for bracket in re.findall(r'\[([^\[\]]+)\]',dossier):
 for token in re.findall(r'\b[A-Za-z][A-Za-z0-9]*(?:19\d\d|20\d\d|XVII|IV4|III1|III2|AV|01ZR|0620|0A1J|03NP|00VZ|056U)\b',bracket):
  if token not in refs:unknown_citations.append(token)
require(not unknown_citations,'unknown overview citation keys '+str(unknown_citations))
for name,body in [('dossier',dossier),('directions',directions)]:
 for identifier in re.findall(r'(?<![A-Za-z0-9-])(?:C-|MP-)?SA04-\d+',body):
  require(identifier in active or identifier in aliases,'unknown '+name+' ID '+identifier)
 for path in re.findall(r'(?:parts|programs|outputs)/[A-Za-z0-9_/.-]+\.(?:json|md|py|txt|tsv|bib)',body):require((W/path).exists(),'broken '+name+' artifact path '+path)
 require(not any(ord(c)<32 and c not in '\n\t\r' for c in body),'control character in '+name)
require('D\\circ v=\\Delta\\circ d_E' in dossier,'typed Manin equation missing')
require('## 10. Final register counts' in dossier,'count section missing')
# All input hashes still match the source manifest; no diplomatic input changed.
manifest=j(F/'SOURCE_MANIFEST.json');bad_input=[]
for row in manifest:
 path=ROOT/row['file'] if row['file'].startswith('upload/') else ROOT/'source'/row['file']
 if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=row['sha256']:bad_input.append(row['file'])
 if row['file'].endswith('PREAMBLE.tex'):require(not row.get('scan_markers'),'preamble macro example treated as archive scan')
require(not bad_input,'source input hash changed '+str(bad_input))
require(len(ts(F/'SOURCE_SCOPE.tsv'))==30,'catalogue inventory not30')
# Saved outputs for every substantive computation entry point.
calculations={'a_computations.py':'a_computations.txt','b_computations.py':'b_computations.json','b_supplement_computations.py':'b_supplement_computations.json','c_computations.py':'c_computations.txt','c_manin_check.py':'c_manin_check.json','c_review_genus2.py':'c_review_genus2.json','root_computations.py':'root_computations.json','root_git_computation.py':'root_git_computation.json','root_weierstrass_supplement.py':'root_weierstrass_supplement.json','b_tits_check.py':'b_tits_check.json'}
for program,output in calculations.items():
 require((W/'programs'/program).is_file(),'missing calculation program '+program)
 require((W/'outputs'/output).is_file() and (W/'outputs'/output).stat().st_size>0,'missing calculation output '+output)
hardcoded=[p.name for p in sorted((W/'programs').glob('*.py')) if '/workspace/scratch/594d1dc856a9' in p.read_text() and p.name!=Path(__file__).name]
# Date-stamped receipt consistency, without creating an extra checkpoint.
checkpoints=ts(W/'CHECKPOINTS.tsv')
for cp in checkpoints:
 p=ROOT/cp['checkpoint'];require(p.is_file(),'missing local checkpoint '+p.name)
 if p.is_file():require(hashlib.sha256(p.read_bytes()).hexdigest()==cp['sha256'],'checkpoint modified '+p.name)
 require(cp['persistent_file_id'].startswith('libfile_'),'checkpoint has no persistent receipt '+p.name)
report={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':not errors,'counts':assembly['counts'],'directions':30,'overview_words':len(dossier.split()),'all_claims_have_searched_fates':not missing_fates,'claim_search_rows':search_rows,'source_inputs_unchanged':not bad_input,'exact_event_types':dict(collections.Counter(e['type'] for e in events)),'calculation_program_outputs':calculations,'programs_requiring_workspace_prefix_relocation':hardcoded,'checkpoints_saved':len(checkpoints),'source_scan_context_envelopes':len(audit['scan_field_discrepancies']),'errors':errors}
(F/'FINAL_VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(W/'outputs/final_quality_checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(0 if not errors else 1)
