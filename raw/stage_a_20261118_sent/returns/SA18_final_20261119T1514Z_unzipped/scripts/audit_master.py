"""Structural/source-coordinate checks after the scientific review; no verdict inference."""
from pathlib import Path
from collections import Counter,defaultdict
import csv,json,re,argparse

B=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--strict',action='store_true');args=parser.parse_args()
def load(name):return json.loads((B/name).read_text())
def tsv(name):
    with (B/name).open(newline='')as f:return list(csv.DictReader(f,delimiter='\t'))
items=load('SA18_items.json');claims=load('SA18_claims.json');problems=load('SA18_problems.json')
entries=tsv('SA18_entries.tsv');events=tsv('CHECK_EVENTS.tsv');search=tsv('SA18_literature_search.tsv')
aliases=load('SA18_aliases.json');bib=(B/'SA18_references.bib').read_text()
keys=re.findall(r'@\w+\{([^,]+),',bib)
item_ids={x['id']for x in items};claim_ids={x['id']for x in claims};problem_ids={x['id']for x in problems}
original=tsv('../sources/SA18_notes/NOTES_INDEX.tsv');original_ids={x['entry_id']for x in original}
errors=[];notes=[];results={}
def check(label,condition,detail=None):
    results[label]={'pass':bool(condition)}
    if detail is not None:results[label]['detail']=detail
    if not condition:errors.append(label)

check('exactly335originalentries',len(entries)==335 and {x['entry_id']for x in entries}==original_ids)
check('uniqueentryverdict',len(entries)==len({x['entry_id']for x in entries}))
check('uniqueitemclaimproblemIDs',len(item_ids)==len(items)and len(claim_ids)==len(claims)and len(problem_ids)==len(problems))
check('everyentryhasverdictandreason',all(x.get('verdict')and x.get('reason')for x in entries))
check('allentrytargetsvalid',all(x['item_id']in item_ids for x in entries))
inverse=defaultdict(list)
for item in items:
    for eid in item['sources']:inverse[eid].append(item['id'])
badinverse={x['entry_id']:{'entrytarget':x['item_id'],'itemtargets':inverse.get(x['entry_id'])}for x in entries if inverse.get(x['entry_id'])!=[x['item_id']]}
check('exactentryiteminverse',not badinverse,badinverse)
check('nofabricatednoteIDs',set(inverse)==original_ids,sorted(set(inverse)-original_ids))
check('claimitemtargetsvalid',all(set(x['items'])<=item_ids for x in claims))
required={
 'item':('id sources kind cote scans lines his_words statement reconstruction check check_reason'.split(),items),
 'claim':('id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split(),claims),
 'problem':('id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split(),problems)}
for name,(fields,rows)in required.items():check(name+'requiredfields',all(set(fields)<=set(x)for x in rows))
check('claimclassesAtoF',all(x['class']in list('ABCDEF')for x in claims))
statuses={'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages'}
badstatus={x['id']:x['status_on_pages']for x in claims if x['status_on_pages']not in statuses}
check('sixcanonicalpagestatuses',not badstatus,badstatus)
check('itemcheckvocabulary',all(x['check']in {'agrees','overstates','understates','misreads','not on the page'}for x in items),dict(Counter(x['check']for x in items)))
check('claimfatecomplete',all(x['fate']and x['fate_date']and x['present_status']and x['confidence']in {'high','medium','low'}for x in claims))
check('all12topiccotesrepresented',set(range(45,57))<={int(c)for x in claims for c in x['cote']})

source_lengths={};badcoords=[]
def inspectcoords(v,record):
    if isinstance(v,list):
        for y in v:inspectcoords(y,record)
    if isinstance(v,dict):
        if 'file'in v and 'start'in v:
            p=B.parent/'sources'/v['file']
            if not p.exists():badcoords.append((record,'missing source',v));return
            if str(p)not in source_lengths:source_lengths[str(p)]=len(p.read_text().splitlines())
            a=v['start'];z=v.get('end',a)
            if not (1<=a<=z<=source_lengths[str(p)]):badcoords.append((record,'bad line span',v,source_lengths[str(p)]))
        for k,y in v.items():
            if k not in {'file','absolute_file'}and isinstance(y,(dict,list)):inspectcoords(y,record)
for group in [items,claims,problems]:
    for x in group:inspectcoords(x,x['id'])
check('allsourcelinesvalid',not badcoords,badcoords)
unindexed=[x['id']for x in claims if not x['items']]
check('unindexedclaimsretaincoordinates',all(x['cote']and x['scans']and x['lines']for x in claims if not x['items']),unindexed)

check('uniquebibliographykeys',len(keys)==len(set(keys)))
missingrefs={x['id']:sorted(set(x['refs'])-set(keys))for x in claims+problems if set(x['refs'])-set(keys)}
check('allclaimproblemreferencesresolve',not missingrefs,missingrefs)
notes_by_key={}
for m in re.finditer(r'@\w+\{([^,]+),',bib):
    tail=bib[m.end():];n=re.search(r'\bnote\s*=\s*\{([^}]+)\}',tail)
    notes_by_key[m[1]]=n[1]if n else ''
check('allreferencesmarked',all(v in {'verified','unverified'}for v in notes_by_key.values()),dict(Counter(notes_by_key.values())))
check('eachproblemhasopenedcomparator',all(any(notes_by_key.get(k)=='verified'for k in x['refs'])for x in problems),[x['id']for x in problems if not any(notes_by_key.get(k)=='verified'for k in x['refs'])])
searched={x['statement_id']for x in search if x.get('queries')and x.get('exact_match_or_limit')}
missingsearch=sorted((claim_ids|problem_ids)-searched)
check('everyclaimandproblemsearched',not missingsearch,missingsearch)

checked={x['statement_id']for x in events}
check('everyitemandclaimhascheckevent',(item_ids|claim_ids)<=checked,sorted((item_ids|claim_ids)-checked))
eventtypes={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found','refuted'}
check('eventtypesdescribeactualwork',all(x['type']in eventtypes for x in events),dict(Counter(x['type']for x in events)))
false={x['id']for x in claims if x['status_on_pages']=='false as stated'}
refuted={x['statement_id']for x in events if x['type']=='refuted'}
check('allfalseclaimswithrefutationevent',false<=refuted,sorted(false-refuted))
check('refutationeventsnamerefinedstatement',all(re.search(r'CL-SA18-\d+',x['outcome'])for x in events if x['type']=='refuted'))
known=item_ids|claim_ids|problem_ids|set(keys)|original_ids
for kind in ['item_aliases','claim_aliases','claim_splits','problem_aliases']:known.update(aliases[kind])
unknown=sorted(checked-known)
check('eventstatementIDsresolve',not unknown,unknown)

badartifacts=[]
for c in claims:
    for p in c.get('audit_artifacts',[]):
        if not(B/p).exists():badartifacts.append((c['id'],p))
    co=c['computation']
    if isinstance(co,dict):
        for k in ['code','output']:
            if k in co and not(B/co[k]).exists():badartifacts.append((c['id'],co[k]))
check('claimauditartifactsavailable',not badartifacts,badartifacts)

linkids=[]
for name in ['SA18_links.tsv','SA18_project_links.tsv']:
    for i,row in enumerate(tsv(name),2):
        found=re.findall(r'MPL_[^;\s,]+#\d+',row['note_ids'])
        for eid in found:
            if eid not in original_ids:linkids.append((name,i,eid))
check('linknoteIDsvalid',not linkids,linkids)
check('projectleadsseparate',all(x['kind']!='our projects'for x in tsv('SA18_links.tsv')))
forbidden=[str(p.relative_to(B))for p in B.rglob('*')if p.is_file()and p.suffix.lower()in {'.pdf','.png','.jpg','.jpeg','.zip'}]
check('noattachedorpublicsourcebodiesinarchive',not forbidden,forbidden)

# Structural evidence of full supplied-transcription coverage is reported; the
# owner read logs, not this aggregate count, document the scientific reading.
manifest=load('source_manifest.json');pageindex=load('research/page_index.json')
source_summary={'source_files':len(manifest),'transcription_files':len([x for x in manifest if x['path'].endswith('_transcription.tex')]),
 'scan_units':len(pageindex),'scan_units_by_cote':dict(Counter(x['cote']for x in pageindex)),
 'transcription_lines':sum(x['lines']for x in manifest if x['path'].endswith('_transcription.tex')),
 'owner_read_records':['parts/root/read_coverage.json','parts/agent16/read_log.tsv','parts/agent45/outputs/source_read_manifest.json','parts/agent46/source_review.md','parts/agent46/outputs/package_audit.json']}
check('sourcecoveragerecordspresent',all((B/p).exists()for p in source_summary['owner_read_records']))
(B/'SA18_source_coverage.json').write_text(json.dumps(source_summary,indent=2)+'\n')
report={'date':'2026-11-19','all_checks_pass':not errors,'failed_checks':errors,'checks':results,'source_coverage':source_summary,
 'scope':'Structural coverage and provenance validation. Mathematical reasoning is in the source-owner reviews and explicit proof/certificate records, not inferred by this program.'}
(B/'outputs/master_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'all_checks_pass':not errors,'failed_checks':errors,'counts':{k:len(v)for k,v in [('entries',entries),('items',items),('claims',claims),('problems',problems)]},'source_coverage':source_summary},indent=2))
if args.strict and errors:raise SystemExit('Master audit did not pass.')
