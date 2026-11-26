"""Integrate manually reviewed records; this script makes no scientific verdicts.

Cross-source equivalences are explicit decisions documented in the two agent16
merge reviews and research/integration_decisions.md. Owner records are retained.
"""
from pathlib import Path
from collections import Counter, defaultdict
from copy import deepcopy
import csv, json, re, hashlib

B = Path(__file__).resolve().parents[1]
OWNERS = {'root':'', 'agent16':'SA18_', 'agent45':'', 'agent46':''}
ITEM_ALIASES = {
    'SA18-11001':'SA18-16024',
    'SA18-11057':'SA18-16069',
    'SA18-45002':'SA18-16050',
    'SA18-45003':'SA18-16050',
    'SA18-45004':'SA18-16069',
    'SA18-46003':'SA18-16050',
    'SA18-11078':'SA18-45045',
}
PARTIAL_ENTRIES = {'MPL_46_002-048#42': 'SA18-16069'}
CLAIM_ALIASES = {
    'CL-SA18-45049':'CL-SA18-11078',
    'CL-SA18-11085':'CL-SA18-45121',
}
CLAIM_SPLITS = {'CL-SA18-11079':['CL-SA18-45117','CL-SA18-45118']}
PROBLEM_ALIASES = {'MP-SA18-11031':'MP-SA18-45021'}
ALIASES = {**ITEM_ALIASES, **CLAIM_ALIASES, **PROBLEM_ALIASES}

def jwrite(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

def tsvread(path):
    if not path.exists(): return []
    with path.open(newline='') as f: return list(csv.DictReader(f, delimiter='\t'))

def tsvwrite(path, fields, rows):
    with path.open('w', newline='') as f:
        w=csv.DictWriter(f, fieldnames=fields, delimiter='\t', extrasaction='ignore')
        w.writeheader(); w.writerows(rows)

def unique(values):
    out=[]; seen=set()
    for v in values:
        k=json.dumps(v,sort_keys=True,ensure_ascii=False)
        if k not in seen: seen.add(k);out.append(v)
    return out

def portable(x):
    if isinstance(x,str):
        x=x.replace(str(B.parent/'sources')+'/', '').replace(str(B)+'/', '')
        return x
    if isinstance(x,list): return [portable(v) for v in x]
    if isinstance(x,dict): return {k:portable(v) for k,v in x.items()}
    return x

def redirect_text(s):
    # Token boundaries prevent an alias such as ...11085 matching a suffix ID.
    for old,new in ALIASES.items():
        s=re.sub(r'(?<![A-Za-z0-9-])'+re.escape(old)+r'(?![A-Za-z0-9])',new,s)
    for old,targets in CLAIM_SPLITS.items():
        s=re.sub(r'(?<![A-Za-z0-9-])'+re.escape(old)+r'(?![A-Za-z0-9])',' and '.join(targets),s)
    return s

def redirect(x):
    if isinstance(x,str): return redirect_text(x)
    if isinstance(x,list):
        vals=[]
        for v in x:
            if isinstance(v,str) and v in CLAIM_SPLITS: vals.extend(CLAIM_SPLITS[v])
            else: vals.append(redirect(v))
        return unique(vals)
    if isinstance(x,dict): return {k:redirect(v) for k,v in x.items()}
    return x

def cotes(x):
    if x is None: return []
    if isinstance(x,list): return sorted(set(z for y in x for z in cotes(y)))
    if isinstance(x,int): return [x]
    return sorted(set(int(v) for v in re.findall(r'\d+',str(x))))

def lines(x):
    out=[]
    if not x: return out
    if not isinstance(x,list): x=[x]
    for y in x:
        if isinstance(y,dict):
            fn=portable(y.get('file',y.get('absolute_file','')))
            if 'start' in y:
                out.append({'file':fn,'start':int(y['start']),'end':int(y.get('end',y['start']))})
            elif 'absolute_1_based' in y:
                ns=y['absolute_1_based']
                for i in range(0,len(ns),2): out.append({'file':fn,'start':int(ns[i]),'end':int(ns[min(i+1,len(ns)-1)])})
            else: out.append(portable(y))
        elif isinstance(y,str):
            s=portable(y)
            m=re.match(r'(.+?\.tex):(.*)',s)
            if not m: out.append({'locator':s});continue
            for r in m[2].split(';'):
                n=re.match(r'\s*(\d+)(?:\s*[-–—]\s*(\d+))?',r)
                if n:out.append({'file':m[1],'start':int(n[1]),'end':int(n[2] or n[1])})
                elif r.strip():out.append({'file':m[1],'locator':r.strip()})
    return unique(out)

def scans(x, cs):
    if isinstance(x,dict):return {str(k):v for k,v in x.items()}
    if len(cs)==1:return {str(cs[0]):x or []}
    if not x:return {}
    return {'shared_or_unspecified':x}

def normalize(x,owner,kind):
    x=portable(deepcopy(x));x['review_owner']=owner
    if kind=='items':
        kind_names={'self-flagged step (a step he marks as unverified)':'self-flagged step','withdrawn in the same text (he corrects or retracts it later, with both places)':'withdrawn in the same text'}
        x['kind']=kind_names.get(x['kind'],x['kind'])
    if kind!='problems':
        x['cote']=cotes(x.get('cote'));x['scans']=scans(x.get('scans'),x['cote']);x['lines']=lines(x.get('lines'))
    refs=x.get('refs')
    if refs is not None:
        details=[r for r in refs if isinstance(r,dict)]
        x['refs']=unique([r['key'] if isinstance(r,dict) else r for r in refs])
        if details:x['reference_details']=details
    if kind=='claims':
        if x['status_on_pages']=='corrected by himself later (both places)':
            x['status_on_pages']='corrected by himself later'
        paths={
            'root':['research/root_proofs.md','scripts/root_certificates.py','outputs/root_certificates.json','scripts/root_extra_certificates.py','outputs/root_extra_certificates.json'],
            'agent16':['parts/agent16/source_review.md','parts/agent16/scripts/computations.py','parts/agent16/outputs/computations.json'],
            'agent45':['parts/agent45/source_review.md','parts/agent45/scripts/math_checks.py','parts/agent45/outputs/math_checks.json','parts/agent45/scripts/exterior_checks.py','parts/agent45/outputs/exterior_checks.json'],
            'agent46':['parts/agent46/proofs.md','parts/agent46/scripts/checks.py','parts/agent46/outputs/computations.json']}
        x['audit_artifacts']=paths[owner]
        if not x.get('items'):
            x['index_scope']='Transcription claim without an indexed Pro-note entry; source coordinates, not a fabricated note ID, are its provenance.'
    return x

data={k:[] for k in ['items','claims','problems']}; entries=[]; inputs=[]
for owner,prefix in OWNERS.items():
    p=B/'parts'/owner
    for kind in data:
        f=p/(prefix+kind+'.json');inputs.append(f)
        data[kind].extend(normalize(x,owner,kind) for x in json.loads(f.read_text()))
    f=p/(prefix+'entries.tsv'); inputs.append(f)
    entries.extend(portable(tsvread(f)))
by={k:{x['id']:x for x in xs}for k,xs in data.items()}

def merge_location(target,other):
    target['cote']=unique(target.get('cote',[])+other.get('cote',[]))
    for c,ss in other.get('scans',{}).items():
        target.setdefault('scans',{})[c]=unique(target.get('scans',{}).get(c,[])+ss)
    target['lines']=unique(target.get('lines',[])+other.get('lines',[]))

def occurrence(x):
    return {k:deepcopy(x[k]) for k in ['id','review_owner','origin','cote','scans','lines','his_statement','statement','status_on_pages','status_detail','computation','class','fate','fate_date','refs'] if k in x}

for old,new in ITEM_ALIASES.items():
    src=by['items'][old];dst=by['items'][new]
    if 'merged_records' not in dst:dst['merged_records']=[deepcopy(dst)]
    dst['merged_records'].append(deepcopy(src));dst['sources']=unique(dst['sources']+src['sources'])
    merge_location(dst,src)
    dst['cross_package_merge']='Same explicitly identified object/question; source-specific qualifications and readings are preserved in merged_records.'
    del by['items'][old]

for eid,new in PARTIAL_ENTRIES.items():
    row=next(r for r in entries if r['entry_id']==eid)
    old=row['item_id'];src=by['items'][old];dst=by['items'][new]
    src['sources'].remove(eid);dst['sources']=unique(dst['sources']+[eid])
    dst.setdefault('partial_source_merges',[]).append({'entry_id':eid,'from_item':old,'reason':'Only the full A[p] reconstruction question matches Oda Corollary5.11; the retained source item also covers Picard[p] and Corollary5.12, whose hypotheses differ.'})

for old,new in CLAIM_ALIASES.items():
    src=by['claims'][old];dst=by['claims'][new]
    dst.setdefault('occurrences',[occurrence(dst)]).append(occurrence(src))
    merge_location(dst,src)
    dst['items']=unique(dst.get('items',[])+src.get('items',[]));dst['refs']=unique(dst['refs']+src['refs'])
    dst['merged_claim_ids']=unique(dst.get('merged_claim_ids',[])+[old])
    dst['occurrence_status_rule']='The canonical status describes the most complete supplied occurrence; every occurrence retains its own wording, author, proof status and date.'
    if new=='CL-SA18-45121':
        dst['origin']='Grothendieck letter of22July1961 and Antoine Delzant offprint of1962; separate documentary occurrences.'
        dst['statement']='For a field F of characteristic different from2, Delzant’s rank-zero augmentation filtration J on GW(F) gives J²/J³≅I²/I³. The degree-two Stiefel–Whitney/Clifford map to H²(F,Z/2) is an isomorphism: identify I²/I³ with K₂^M(F)/2, then use the degree-two norm-residue theorem. The source asks only injectivity.'
        dst['index_scope']='Contains an unindexed letter occurrence and indexed offprint entries; both are merged in this canonical claim.'
    del by['claims'][old]

for old,targets in CLAIM_SPLITS.items():
    src=by['claims'][old]
    ranges={'CL-SA18-45117':(1804,1829),'CL-SA18-45118':(1831,1843)}
    for target in targets:
        dst=by['claims'][target];a,b=ranges[target]
        component=deepcopy(src)
        component['lines']=[{'file':'SA18_texts/pro/MPL_11_043-058+56_transcription.tex','start':a,'end':b}]
        component['statement']='The presentation proposition.' if target.endswith('117') else 'The binary-isometry criterion used for the corollary.'
        dst.setdefault('occurrences',[occurrence(dst)]).append(occurrence(component))
        merge_location(dst,component);dst['items']=unique(dst['items']+src['items']);dst['refs']=unique(dst['refs']+src['refs'])
        dst['origin']='Grothendieck letter of22July1961 and corresponding proposition/corollary in Antoine Delzant’s1962 offprint.'
        dst['status_on_pages']='proof sketched'
        dst['status_detail']='Stated without proof in the1961 letter; corresponding1962 offprint gives the compressed proposition/corollary with Witt references. Separate occurrence statuses are retained.'
        dst['merged_claim_ids']=unique(dst.get('merged_claim_ids',[])+[old])
        dst['index_scope']='The earlier composite offprint claim was split into its presentation and binary-classification components before merging with the corresponding letter statements.'
    del by['claims'][old]

# Partial identity is a link, not a licence to erase the stronger open question.
by['claims']['CL-SA18-11081']['related_claims']=[{'id':'CL-SA18-45122','relation':'Same total-class construction on fields. The offprint specifies the1958 Chern-class target ring law; the letter’s unspecified universal target remains a separate question.'}]
by['claims']['CL-SA18-45122']['related_claims']=[{'id':'CL-SA18-11081','relation':'The established field construction is shared; the literal universal-target claim is not merged into it.'}]

for old,new in PROBLEM_ALIASES.items():
    src=by['problems'][old];dst=by['problems'][new]
    dst.setdefault('merged_records',[deepcopy(dst)]).append(deepcopy(src))
    dst['occurrences']=unique(dst['occurrences']+src['occurrences']);dst['refs']=unique(dst['refs']+src['refs'])
    dst['merged_problem_ids']=unique(dst.get('merged_problem_ids',[])+[old])
    del by['problems'][old]

for row in entries:
    old=row['item_id'];new=PARTIAL_ENTRIES.get(row['entry_id'],ITEM_ALIASES.get(old,old))
    if new!=old:
        original=row['verdict'];row['item_id']=new;row['verdict']='merged into '+new
        row['reason']=f'Cross-package exact-identity merge from {old}; original source verdict: {original}. '+row['reason']
    row['reason']=redirect_text(row['reason'])

# Supplemental transcription items may cite a broad note as context. The sole
# entry verdict stays with its canonical primary item; retain the extra note
# provenance explicitly instead of silently assigning a second verdict.
entry_target={r['entry_id']:r['item_id']for r in entries}
for item in by['items'].values():
    related=[eid for eid in item['sources']if entry_target.get(eid)!=item['id']]
    if related:
        item['related_note_entries']=unique(item.get('related_note_entries',[])+related)
        item['sources']=[eid for eid in item['sources']if eid not in related]
        item['index_scope']='Supplemental transcription analysis. Related indexed notes are retained in related_note_entries; their one entry verdict remains assigned to the primary item.'

# Preserve snapshots before redirection: their original IDs are resolvable in aliases.
for kind in by:
    for x in by[kind].values():
        for key in list(x):
            if key not in {'id','merged_records','occurrences','merged_claim_ids','merged_problem_ids','partial_source_merges'}:
                x[key]=redirect(x[key])
        if kind=='problems':x['occurrences']=redirect(x['occurrences'])
    data[kind]=sorted(by[kind].values(),key=lambda x:x['id'])
    jwrite(B/('SA18_'+kind+'.json'),data[kind])
entries.sort(key=lambda r:(r['entry_id'].split('#')[0],int(r['entry_id'].split('#')[1])))
tsvwrite(B/'SA18_entries.tsv',['entry_id','item_id','verdict','reason'],entries)

tables={k:[] for k in ['readings','links','project_links']}
for owner,prefix in OWNERS.items():
    p=B/'parts'/owner
    for kind in tables:
        f=p/(prefix+kind+'.tsv')
        if not f.exists(): f=p/(kind+'.tsv')
        if f.exists():
            inputs.append(f)
            for row in tsvread(f):
                row=redirect(portable(row))
                if kind=='links' and row.get('kind')=='our projects': tables['project_links'].append(row)
                else:tables[kind].append(row)
for kind,fields in [('readings',['cote','scan','line','reading','alternative','evidence','weight','confidence']),('links',['kind','from','to','what','evidence','note_ids']),('project_links',['kind','from','to','what','evidence','note_ids'])]:
    tables[kind]=unique(tables[kind]);tsvwrite(B/('SA18_'+kind+'.tsv'),fields,tables[kind])

events=[]
for owner in OWNERS:
    p=B/'parts'/owner
    fs=[p/'CHECK_EVENTS.tsv']
    if owner=='root':fs.append(p/'claim_events.tsv')
    if owner=='agent16':fs.extend([p/'root_audit_CHECK_EVENTS.tsv',p/'cross_merge_CHECK_EVENTS.tsv',p/'additional_cross_merge_CHECK_EVENTS.tsv',p/'status_CHECK_EVENTS.tsv',p/'overview_CHECK_EVENTS.tsv',p/'ega_followup_CHECK_EVENTS.tsv'])
    for f in fs:
        if not f.exists():continue
        inputs.append(f)
        for row in tsvread(f):
            old=row['statement_id'];targets=CLAIM_SPLITS.get(old,[ALIASES.get(old,old)])
            if old=='SUPP-parent-c55':targets=['CL-SA18-11110b']
            for target in targets:
                z=redirect(portable(deepcopy(row)));z['statement_id']=target
                type_map={'refuted, with refined ID':'refuted',"refuted, with the refined statement's id":'refuted','independent proof check':'targeted proof check','reference check':'used and rechecked in this run','literature scope check':'used and rechecked in this run','cross-package identity review':'used and rechecked in this run'}
                if z['type']in type_map:
                    oldtype=z['type'];z['type']=type_map[oldtype]
                    z['outcome']='Event terminology normalized from '+oldtype+'; '+z['outcome']
                if z['type']=='refuted'and not re.search(r'CL-SA18-\d+',z['outcome']):
                    z['outcome']+=' Refined statement ID: '+target+' (modern statement and qualifications in this canonical claim record).'
                if old!=target:z['outcome']='Canonical merge of '+old+': '+z['outcome']
                if old in CLAIM_SPLITS:z['outcome']='Shared check of the original composite, applied to this component. '+z['outcome']
                events.append(z)
events=unique(events)
tsvwrite(B/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)

search=[]
for owner in OWNERS:
    f=B/'parts'/owner/'literature_search.tsv'
    if not f.exists():continue
    inputs.append(f)
    for row in tsvread(f):
        rawids=[row['statement_id']]if row.get('statement_id')else re.findall(r'(?:CL|MP)-SA18-\d+[a-z]?',row.get('claim_ids','')+';'+row.get('problem_ids',''))
        query=row.get('queries',row.get('query',row.get('query_or_request','')))
        opened=row.get('opened_references',row.get('opened_urls',row.get('opened_sources','')))
        if not opened and row.get('url'):
            opened=('Search-result leads only: 'if row.get('operation')=='search'else 'Opened source: ')+row['url']
        result=row.get('exact_match_or_limit',row.get('result',row.get('outcome','')))
        if row.get('result_scope'):result+=' Scope: '+row['result_scope']
        for old in rawids:
            targets=CLAIM_SPLITS.get(old,[ALIASES.get(old,old)])
            for target in targets:
                search.append({'statement_id':target,'review_owner':owner,'date':row.get('date','2026-11-19'),'queries':query,'opened_references':opened,'exact_match_or_limit':result,'details':json.dumps(portable(row),ensure_ascii=False)})
tsvwrite(B/'SA18_literature_search.tsv',['statement_id','review_owner','date','queries','opened_references','exact_match_or_limit','details'],unique(search))

def bibrecords(s):
    out=[]; pos=0
    while True:
        m=re.search(r'@\w+\s*\{\s*([^,]+),',s[pos:])
        if not m:break
        start=pos+m.start();key=m[1].strip();i=pos+m.end();depth=1
        while i<len(s) and depth:
            if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
            if s[i]=='}' and (i==0 or s[i-1]!='\\'):depth-=1
            i+=1
        if depth:raise ValueError('Unbalanced BibTeX '+key)
        out.append((key,s[start:i]));pos=i
    return out

bibs={};bibowners=defaultdict(list)
for owner,prefix in OWNERS.items():
    f=B/'parts'/owner/(prefix+'references.bib');inputs.append(f)
    for key,entry in bibrecords(f.read_text()):
        bibowners[key].append(owner)
        if key in bibs and key!='Oda1969':raise ValueError('Unexpected bibliography collision '+key)
        if key not in bibs:bibs[key]=entry
if 'Oda1969' in bibs:
    bibs['Oda1969']='''@article{Oda1969,
  author = {Tadao Oda},
  title = {The first de Rham cohomology group and Dieudonne modules},
  journal = {Annales scientifiques de l'Ecole Normale Superieure},
  series = {4}, volume = {2}, number = {1}, pages = {63--135}, year = {1969},
  doi = {10.24033/asens.1175},
  url = {https://www.numdam.org/item/ASENS_1969_4_2_1_63_0/},
  note = {verified},
  annote = {Primary paper opened and checked by both source owners. Corollary5.11: full finite group scheme A[p] over a perfect field. Corollary5.12: the Picard statement requires X(k) nonempty and the specified Cartier-stable subspace. These are not interchangeable. Metadata and DOI rechecked by root on Numdam.},
  addendum = {Thesis completed June1967; publication1969. No earlier circulation date inferred.}
}'''
(B/'SA18_references.bib').write_text('% Verified means the cited URL was opened; annote states whether the exact result or only metadata was checked.\n\n'+'\n\n'.join(bibs[k] for k in sorted(bibs))+'\n')

def bibfield(entry,name):
    m=re.search(r'(?im)^\s*'+re.escape(name)+r'\s*=\s*\{',entry)
    if not m:return ''
    i=m.end();start=i;depth=1
    while i<len(entry)and depth:
        if entry[i]=='{'and entry[i-1]!='\\':depth+=1
        if entry[i]=='}'and entry[i-1]!='\\':depth-=1
        i+=1
    return entry[start:i-1].strip()

index=['# Reference index','',
       'Keys in the tables and dossier resolve here and in `SA18_references.bib`. '
       '**Verified** means that the listed link was opened. The scope note distinguishes '
       'an exact theorem or proof check from a metadata-only check. An unopened historical '
       'back-reference remains **unverified** even when a later verified paper cites it.','']
for key,entry in sorted(bibs.items()):
    title=bibfield(entry,'title');url=bibfield(entry,'url');note=bibfield(entry,'note')
    index+=['## '+key,'',f"{bibfield(entry,'author')}. **{title}**. {bibfield(entry,'year')}. **{note}**.",'']
    if url:index+=['[Opened source or recorded reference]('+url+')','']
    for fld in ['annote','addendum']:
        if bibfield(entry,fld):index+=[bibfield(entry,fld),'']
(B/'SA18_reference_index.md').write_text('\n'.join(index))

aliases={'item_aliases':ITEM_ALIASES,'partial_entry_moves':PARTIAL_ENTRIES,'claim_aliases':CLAIM_ALIASES,'claim_splits':CLAIM_SPLITS,'problem_aliases':PROBLEM_ALIASES,'partial_claim_links':[['CL-SA18-11081','CL-SA18-45122']],'documentation':['parts/agent16/cross_package_merge_review.json','parts/agent16/additional_cross_package_merge_review.json','research/integration_decisions.md']}
jwrite(B/'SA18_aliases.json',aliases)
counts={'entries':len(entries),'items':len(data['items']),'claims':len(data['claims']),'problems':len(data['problems']),
        'readings':len(tables['readings']),'links':len(tables['links']),'project_links':len(tables['project_links']),
        'bibliography_records':len(bibs),'check_events':len(events),'literature_search_rows':len(unique(search)),
        'items_by_kind':dict(Counter(x['kind']for x in data['items'])),
        'claims_by_class':dict(sorted(Counter(x['class']for x in data['claims']).items())),
        'claims_by_status':dict(Counter(x['status_on_pages']for x in data['claims'])),
        'claims_without_indexed_items':sum(not x.get('items')for x in data['claims']),
        'items_without_index_entries':sum(not x.get('sources')for x in data['items']),
        'bibliography_shared_keys':{k:v for k,v in bibowners.items()if len(v)>1}}
def verdict(v):
    s=v.lower()
    if s.startswith('merged'):return 'merged'
    if 'misreading' in s:return 'rests on a misreading'
    if s.startswith('correct'):return 'corrected'
    if s.startswith('withdraw'):return 'withdrawn'
    if s.startswith('kept'):return 'kept'
    return v
counts['verdicts_by_kind']=dict(Counter(verdict(x['verdict'])for x in entries))
jwrite(B/'SA18_counts.json',counts)
jwrite(B/'outputs/integration_inputs.json',[{'path':str(p.relative_to(B)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for p in dict.fromkeys(inputs)])
print(json.dumps(counts,ensure_ascii=False,indent=2))
