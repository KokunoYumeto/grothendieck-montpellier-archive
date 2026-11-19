"""Read-only assembly-prefix and record-update regression checks.

The finalizer is evaluated only before its first output write. The only file
written by this script is its own integration validation report.
"""
from pathlib import Path
import ast,copy,hashlib,json,collections

W=Path(__file__).resolve().parents[1]
program=W/'programs/finalize_dossier.py'

def canonical_snapshot():
    files=list(W.glob('SA23_*'))+[W/'CHECK_EVENTS.tsv',W/'outputs/final_counts.json']
    return {str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in files if p.is_file()}

before=canonical_snapshot()
tree=ast.parse(program.read_text());prefix=[]
for node in tree.body:
    if not isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):
        calls=[n for n in ast.walk(node)if isinstance(n,ast.Call)]
        if any(isinstance(n.func,ast.Name)and n.func.id in {'dump','write_tsv'}for n in calls):break
        for call in calls:
            if isinstance(call.func,ast.Attribute):
                assert call.func.attr not in {'write_text','write_bytes','unlink','rename','replace'},ast.unparse(call)
    prefix.append(node)
ns={'__file__':str(program),'__name__':'read_only_integration_validation'}
exec(compile(ast.Module(body=prefix,type_ignores=[]),str(program),'exec'),ns)
data=ns['data'];original=ns['original'];plan=ns['PLAN'];resolve=ns['resolve'];patch=ns['apply_record_update']
errors=[];tests=[]
def require(ok,name,detail=None):
    tests.append({'check':name,'passed':bool(ok),'detail':detail})
    if not ok:errors.append({'check':name,'detail':detail})

# A repeated append must retain the exact first snapshot and both audit entries.
sample={'id':'SA23-999999','cote':'161-3','lines':['owner-range'],
        'source_records':[{'id':'SA23-999998','his_words':'literal witness'}]}
initial=copy.deepcopy(sample)
first={'kind':'items','id':sample['id'],'append_fields':{'cote':['161-2'],'lines':['owner-range','review-range']},'reason':'First append'}
second={'kind':'items','id':sample['id'],'append_fields':{'lines':['review-range','later-range'],'source_occurrences':[{'cote':'161-2','claim_ids':['C-SA23-groupes-031']}]},'reason':'Second append'}
patch(sample,first);patch(sample,second)
require(sample['integration_record_before_update']==initial,'first pre-update snapshot survives repeated updates')
require(sample['source_records']==initial['source_records'],'appends preserve source witnesses')
require(sample['cote']==['161-3','161-2']and sample['lines']==['owner-range','review-range','later-range'],'scalar-to-list append and stable deduplication')
require(sample['integration_updates']==[first,second]and sample['integration_update_reasons']==['First append','Second append'],'all update records and rationales retained')
first['append_fields']['lines'].append('mutated external plan object')
require('mutated external plan object'not in sample['lines']and 'mutated external plan object'not in sample['integration_updates'][0]['append_fields']['lines'],'patch data copied without aliasing the plan')
protected=False
try:patch(sample,{'id':sample['id'],'set_fields':{'source_records':[]},'reason':'Invalid replacement'})
except AssertionError:protected=True
require(protected,'source_records cannot be overwritten by scope updates')
null_sample={'id':'SA23-999997','lines':None}
patch(null_sample,{'id':null_sample['id'],'append_fields':{'lines':['range']},'reason':'Append to absent value'})
require(null_sample['lines']==['range'],'append does not create null array members')
require(ns['rewrite'](sample)['integration_updates']==sample['integration_updates'],'update history remains an original-ID audit record')

# Every consolidated witness is the current owner's entire unmodified record.
witness_count=0
for kind,rows in data.items():
    originals={r['id']:r for r in original[kind]}
    for r in rows:
        for witness in r.get('source_records',[]):
            witness_count+=1
            if witness!=originals.get(witness['id']):errors.append({'check':'original witness retained','kind':kind,'target':r['id'],'source':witness['id']})
require(not any(e['check']=='original witness retained'for e in errors),'all merged source_records retain current owner records',{'witness_records_checked':witness_count})

ids={kind:{r['id']for r in rows}for kind,rows in data.items()}
for kind,rows in data.items():
    require(len(ids[kind])==len(rows),'unique canonical '+kind+' IDs')
for c in data['claims']:
    for sid in c['items']:
        if sid not in ids['items']:errors.append({'check':'canonical claim item','claim':c['id'],'item':sid})
for p in data['problems']:
    for sid in p.get('claims',[]):
        if sid not in ids['claims']:errors.append({'check':'canonical problem claim','problem':p['id'],'claim':sid})
require(not any(e['check'].startswith('canonical ')for e in errors),'canonical item and claim references resolve')

entries=[row for owner in ns['P']for row in ns['read_tsv'](owner/'entries.tsv')]
require(len(entries)==326 and all(len(resolve(row['item_id']))==1 for row in entries),'326 indexed entries have single canonical targets')

# These source-owner additions were made after the duplicate-review snapshot.
final_claims={r['id']:r for r in data['claims']}
original_claims={r['id']:r for r in original['claims']}
locator_checks=[]
for sid in ['C-SA23-groupes-014','C-SA23-groupes-019']:
    source=ns['seq'](original_claims[sid]['lines']);retained=ns['seq'](final_claims[sid]['lines'])
    row={'id':sid,'owner_locators':source,'assembled_locators':retained,'all_retained':all(v in retained for v in source)}
    locator_checks.append(row)
    require(row['all_retained'],'recent owner locator additions preserved',row)

for kind in ['item','claim','problem']:
    edges=[(r['target'],s)for r in plan.get(kind+'_merges',[])for s in r['sources']]
    require(len(edges)==len(set(edges)),'unique '+kind+' merge edges')
require(not json.loads((W/'integration/plan_builder_validation.json').read_text())['errors'],'plan builder reports no conflicting updates')

updates=[r for rows in data.values()for r in rows if r.get('integration_updates')]
require(sum(len(r['integration_updates'])for r in updates)==len(plan['record_updates']),'every accepted scope update has an audit-history entry')
require(all('integration_updates'not in r['integration_record_before_update'] for r in updates),'pre-update snapshots are not recursively nested')

editorial={r['original_id']:r['id']for r in ns['original_editorial']if r.get('original_id')}
editorial_alias_checks=[]
for sid in ['MP-SA23-hyp-66']:
    if sid in editorial:
        ok=resolve(sid)==[editorial[sid]]and sid not in ids['problems']
        editorial_alias_checks.append({'source':sid,'editorial':editorial[sid],'resolved':resolve(sid),'passed':ok})
        require(ok,'hyperplanes editorial removal uses the existing alias path',editorial_alias_checks[-1])

after=canonical_snapshot()
require(before==after,'no canonical top-level register or final-count file was written')
report={'date':'2026-11-19','scope':__doc__.strip(),
        'plan_sha256':hashlib.sha256((W/'integration/consolidation_plan.json').read_bytes()).hexdigest(),
        'finalizer_sha256':hashlib.sha256(program.read_bytes()).hexdigest(),
        'counts_in_memory':{kind:len(rows)for kind,rows in data.items()},
        'tests':tests,'errors':errors,'passed':not errors,
        'owner_locator_checks':locator_checks,'editorial_alias_checks':editorial_alias_checks,
        'canonical_snapshot_unchanged':before==after,'finalizer_output_files_written':False}
(W/'integration/consolidation_update_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'tests':len(tests),'errors':errors,'counts_in_memory':report['counts_in_memory'],'canonical_files_unchanged':before==after,'passed':not errors},ensure_ascii=False))
raise SystemExit(bool(errors))
