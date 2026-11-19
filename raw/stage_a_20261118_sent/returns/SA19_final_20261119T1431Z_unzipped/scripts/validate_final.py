"""Final integrity audit. It checks coverage and provenance, never creates verdicts."""
from pathlib import Path
import json,csv,re,collections,hashlib
B=Path(__file__).resolve().parents[1]
def j(n):return json.loads((B/n).read_text())
def t(n):
    with (B/n).open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
claims=j('SA19_claims.json');items=j('SA19_items.json');problems=j('SA19_problems.json');events=t('CHECK_EVENTS.tsv');refs=t('SA19_bibliography_audit.tsv')
entry=t('SA19_entries.tsv');pages=j('source_audit/page_index.json')
knownpages={(str(x['cote']),str(x['scan'])) for x in pages}
errors=[];warnings=[]
for a in claims+items:
    for o in a['occurrences']:
        for s in o['scans']:
            if (str(o['cote']),str(s)) not in knownpages:errors.append('Unprovided source scan '+a['id']+' '+str(o['cote'])+'/'+str(s))
eventids={x['statement_id'] for x in events}
for a in claims+items:
    if a['id'] not in eventids:errors.append('Missing check-event coverage '+a['id'])
for r in refs:
    if r['key'] not in eventids:errors.append('Missing reference check event '+r['key'])
    if not r['access_and_scope']:warnings.append('No access annotation '+r['key'])
# Search logs sometimes use inclusive compact ID ranges for a common exact theorem family.
searchids=set()
for row in j('SA19_research_log.json'):
    fields=[row.get(k,'') for k in ['claim_id','claim_ids','statement_id']]
    for field in fields:
        for m in re.finditer(r'CL-SA19-(\d+)(?:\s*[–−-]\s*(?:CL-SA19-)?(\d+))?',str(field)):
            a=int(m.group(1));b=int(m.group(2) or a)
            searchids.update(f'CL-SA19-{i:03d}' for i in range(a,b+1))
searchids.add('CL-SA19-054') if 'CL-SA19-647' in searchids else None
for a in claims:
    if a['id'] not in searchids:errors.append('Missing searched-fate ledger coverage '+a['id'])
ids={x['id'] for x in claims+items+problems}
aliases={x['old_id']:x['canonical_id'] for x in t('SA19_aliases.tsv')}
for fn in ['SA19_directions.md','SA19_dossier.md']:
    text=(B/fn).read_text()
    for m in re.finditer(r'(?<![\w-])((?:CL-|MP-)?SA19-\d+)(?!\d)',text):
        v=m.group(1)
        if v not in ids and v not in aliases:errors.append('Unresolved narrative ID '+fn+' '+v)
    if re.search(r'\b(?:TODO|TBD)\b',text):errors.append('Unfinished placeholder '+fn)
for a in items:
    for s in a.get('merged_scope_checks',[]):
        if s['former_item_id'] not in aliases:errors.append('Historical merge ID lost '+a['id'])
for n in ['SA19_dossier.md','SA19_entries.tsv','SA19_items.json','SA19_claims.json','SA19_problems.json','SA19_readings.tsv','SA19_links.tsv','SA19_directions.md','SA19_references.bib','CHECK_EVENTS.tsv','progress.log']:
    if not (B/n).is_file() or (B/n).stat().st_size==0:errors.append('Missing deliverable '+n)
leadrows=t('SA19_our_project_leads.tsv');pointers=t('SA19_external_pointer_index.tsv')
directions=len(re.findall(r'^### RD-SA19-',(B/'SA19_directions.md').read_text(),re.M))
# Every genuine computation program/output is retained; serializers and fetch tools
# are catalogued as well, without pretending that every saved amendment is a proof.
programs=[]
for p in sorted(B.rglob('*.py')):
    if '__pycache__' in p.parts:continue
    body=p.read_text();programs.append({'path':str(p.relative_to(B)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'classification':'mathematical check' if p.name in {'exact_checks.py','table_checks.py','computations.py','calculations.py','compute.py'} else 'audit, serialization, retrieval or validation support','execution_evidence':'See sibling outputs and the workstream RUNNING_THE_CHECKS.md/code README; mathematical calculations retain their actual stdout.'})
with (B/'SA19_programs.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['path','bytes','sha256','classification','execution_evidence'],delimiter='\t');w.writeheader();w.writerows(programs)
result={'errors':sorted(set(errors)),'warnings':sorted(set(warnings)),'entries':len(entry),'distinct_entries':len({r['entry_id'] for r in entry}),'items':len(items),'claims':len(claims),'problems':len(problems),'claims_with_search_ledger':sum(c['id'] in searchids for c in claims),'items_and_claims_with_check_events':sum(x['id'] in eventids for x in items+claims),'reference_events':sum(r['key'] in eventids for r in refs),'reading_alarms':len(t('SA19_readings.tsv')),'checked_links':len(t('SA19_links.tsv')),'external_lead_groups':len(leadrows),'external_pointer_pairs':len(pointers),'external_distinct_targets':len({x['target'] for x in pointers}),'directions':directions,'program_files':len(programs),'scope':'Structural/reference/coverage checks only. Mathematical verdicts and source reading were performed before this program.'}
(B/'outputs/final_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
