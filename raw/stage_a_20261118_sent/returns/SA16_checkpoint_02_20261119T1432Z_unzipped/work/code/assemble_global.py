#!/usr/bin/env python3
"""Serialize manually adjudicated cross-package consolidation; no text verdicts inferred.

Run after the part authors' builders. All merge decisions are in the explicitly
reviewed proposal JSONs. Unmerged part records are retained under work/parts/.
"""
from pathlib import Path
import json,csv,re,copy,collections,hashlib,datetime

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'deliverables';OUT.mkdir(exist_ok=True)
PARTS=['cote62','cote63','cote64_early','cote64_late']
def readj(p,default=None):return json.loads(p.read_text()) if p.exists() else default
def tsv(p):return list(csv.DictReader(p.open(),delimiter='\t')) if p.exists() else []
def dump(name,x):(OUT/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def writet(name,rows,fields):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
def unique(xs):
    seen=set();out=[]
    for x in xs:
        k=json.dumps(x,ensure_ascii=False,sort_keys=True)
        if k not in seen:seen.add(k);out.append(x)
    return out
def sortid(s):return int(s.rsplit('-',1)[-1])
data={p:{k:readj(ROOT/'work/parts'/p/(k+'.json'),[]) for k in ['items','claims','problems']} for p in PARTS}
supp=ROOT/'work/parts/cote63_supplement'
if (supp/'claims.json').exists():
    data['cote63_supplement']={k:readj(supp/(k+'.json'),[]) for k in ['items','claims','problems']}
allparts=list(data)
itemmerge=readj(ROOT/'work/outputs/cross_merge_proposals.json')
itemaliases={s:m['keep_id'] for m in itemmerge['recommended_merges'] for s in m['item_ids'] if s!=m['keep_id']}
claimaliases={'C-SA16-512':'C-SA16-293','C-SA16-503':'C-SA16-298'}
aliases={**itemaliases,**claimaliases}
def cid(s):return aliases.get(s,s)
def replaceids(s):
    return re.sub(r'(?<![A-Za-z0-9-])(?:C-)?SA16-\d+(?!\d)',lambda m:cid(m.group()),s) if isinstance(s,str) else s
def refobj(obj):
    if isinstance(obj,str):return replaceids(obj)
    if isinstance(obj,list):return [refobj(a) for a in obj]
    if isinstance(obj,dict):return {k:refobj(v) for k,v in obj.items()}
    return obj
items={a['id']:copy.deepcopy(a) for p in allparts for a in data[p]['items']}
claims={a['id']:copy.deepcopy(a) for p in allparts for a in data[p]['claims']}
problems=[copy.deepcopy(a) for p in allparts for a in data[p]['problems']]
origin={a['id']:p for p in allparts for k in ['items','claims','problems'] for a in data[p][k]}
for a in list(items.values())+list(claims.values())+problems:
    a['audit_package']='work/parts/'+origin[a['id']]
    a['as_of']='2026-11-19'

merge_events=[]
for m in itemmerge['recommended_merges']:
    rs=[items[x] for x in m['item_ids']];a=items[m['keep_id']]
    a['occurrence_history']=[{k:r.get(k) for k in ['id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason','audit_package']} for r in rs]
    a['sources']=unique([s for r in rs for s in r['sources']]);a['scans']=sorted(set(x for r in rs for x in r['scans']),key=lambda x:int(x))
    cotes=sorted(set(int(x) for r in rs for x in (r['cote'] if isinstance(r['cote'],list) else [r['cote']])))
    a['cote']=cotes[0] if len(cotes)==1 else cotes
    a['lines']=[{'occurrence_id':r['id'],'cote':r['cote'],'locators':r['lines']}for r in rs]
    a['his_words']=' | '.join(unique(r['his_words']for r in rs))
    a['statement']=m['recommended_statement'];a['reconstruction']=m['provenance_and_status']
    a['check_reason']='Cross-package consolidation: '+m['rationale']+' Individual comparisons are preserved in occurrence_history.'
    a['aliases']=[x for x in m['item_ids']if x!=m['keep_id']]
    a['merge_review']=m['proposal_id']
    for x in a['aliases']:del items[x]
    merge_events.append({'statement_id':a['id'],'date':'2026-11-19','who':'GPT-6 Astra Pro; inherited effort; root consolidation and cote64-early review','type':'used and rechecked in this run','outcome':m['rationale'],'artifact':'work/outputs/cross_merge_proposals.json','scope':'Source-passage identity comparison; independent mathematical statuses remain separate.'})

claim_merge_specs=[
('C-SA16-293','C-SA16-512','B','The same branch-data/tangent-square-root groupoid equivalence over arbitrary bases with 2 invertible. The modern Legendre atlas and effective descent match its exact relative scope; early proof_supplement §9 proves the local functor and automorphism-sheaf comparison, independently reviewed in late64. The special symmetric mu4 scalar normalization is excluded.'),
('C-SA16-298','C-SA16-503','E','The same elementary Isom torsor for two square roots with fixed orientation: a mu2 torsor, not two guaranteed global sections. The stronger varying-orientation mu4 extension and its normalization retain separate claims.')]
for keep,old,klass,reason in claim_merge_specs:
    rs=[claims[keep],claims[old]];a=claims[keep]
    a['occurrence_history']=[{k:r.get(k) for k in ['id','items','cote','scans','lines','his_statement','statement','status_on_pages','class','computation','fate','refs','audit_package']}for r in rs]
    a['items']=unique(cid(x)for r in rs for x in r['items']);a['scans']=sorted(set(x for r in rs for x in r['scans']),key=int)
    a['lines']=[{'occurrence_id':r['id'],'locators':r['lines']}for r in rs]
    a['his_statement']=' | '.join(unique(r['his_statement']for r in rs))
    a['status_on_pages']='; '.join(r['id']+': '+r['status_on_pages']for r in rs)
    a['computation']=[{'occurrence_id':r['id'],'audit_package':r['audit_package'],'detail':r['computation']}for r in rs]
    a['refs']=unique(x for r in rs for x in r['refs']);a['class']=klass
    a['fate']=reason+' Historical first formulation is not assigned without a dated manuscript.'
    a['present_status']='As of 2026-11-19: established in the stated scope. '+reason
    a['aliases']=[old];a['consolidation_reason']=reason;del claims[old]
    merge_events.append({'statement_id':keep,'date':'2026-11-19','who':'GPT-6 Astra Pro; inherited effort; root and cote64-early review','type':'used and rechecked in this run','outcome':reason,'artifact':'work/outputs/cross_problem_merge_proposals.json','scope':'Exact-claim identity and class adjudication; original source statuses retained.'})
for c in claims.values():c['items']=unique(cid(x)for x in c['items'])
for p in problems:
    for k in ['items','claims','occurrences']: 
        if k in p:p[k]=refobj(p[k])

entryrows=[]
for p in PARTS:
    for r in tsv(ROOT/'work/parts'/p/'entries.tsv'):
        # Normalize only the already-authored verdict vocabulary, not its decision.
        for label in ['kept','merged','corrected','withdrawn','rests on a misreading']:
            if r['verdict'].startswith(label):r['verdict']=label;break
        if r['item_id'] in itemaliases:
            old=r['item_id'];v=r['verdict'];r['item_id']=cid(old);r['verdict']='merged'
            r['reason']=f'Cross-package merge of {old} into {r["item_id"]}; prior verdict {v}: '+r['reason']
        entryrows.append(r)
index=tsv(ROOT/'sources/SA16_notes/NOTES_INDEX.tsv')
indexids=[r.get('entry_id',r.get('id'))for r in index]
if not any(indexids):raise RuntimeError('Read index field names')
positions={s:i for i,s in enumerate(indexids)}
entryrows.sort(key=lambda r:positions[r['entry_id']])
writet('SA16_entries.tsv',entryrows,['entry_id','item_id','verdict','reason'])

# A small balanced BibTeX parser preserves authored field text; it never decides verification.
def balanced(s,i):
    start=i+1;depth=1;i+=1
    while i<len(s):
        if s[i]=='\\':i+=2;continue
        if s[i]=='{':depth+=1
        if s[i]=='}':
            depth-=1
            if depth==0:return s[start:i],i+1
        i+=1
    raise ValueError('Unclosed braced value')
def parsebib(path):
    s=path.read_text();out=[];i=0
    while (m:=re.search(r'@(\w+)\s*\{',s[i:])):
        typ=m.group(1);body,i=balanced(s,i+m.end()-1);key,body=body.split(',',1);r={'key':key.strip(),'type':typ};j=0
        while j<len(body):
            m=re.match(r'[\s,]*(\w+)\s*=\s*',body[j:])
            if not m:
                assert not body[j:].strip(' \t\r\n,');break
            k=m.group(1);j+=m.end()
            if body[j]=='{':v,j=balanced(body,j)
            elif body[j]=='"':
                end=j+1
                while body[end]!='"' or body[end-1]=='\\':end+=1
                v,j=body[j+1:end],end+1
            else:
                end=body.find(',',j);end=len(body)if end<0 else end;v,j=body[j:end].strip(),end
            r[k]=v
        out.append(r)
    return out
bibproposal=readj(ROOT/'work/outputs/bib_alias_proposals.json')
bibaliases={m['key']:g['canonical_key']for g in bibproposal['exact_alias_groups']for m in g['members']if m['key']!=g['canonical_key']}
bibparts=allparts+['cote62/supplement_katz'];grouped=collections.defaultdict(list)
for p in bibparts:
    path=ROOT/'work/parts'/p/'references.bib'
    if path.exists():
        for r in parsebib(path):r['source_part']=p;grouped[bibaliases.get(r['key'],r['key'])].append(r)
refs=[]
for key,rs in grouped.items():
    a=copy.deepcopy(rs[0]);a['key']=key
    for r in rs[1:]:
        for k,v in r.items():
            if k not in a:a[k]=v
    a['note']='verified' if any(r.get('note')=='verified'for r in rs)else'unverified'
    a['verification_scopes']=[{'part':r['source_part'],'key':r['key'],'note':r.get('note'),'scope':r.get('verification_scope',r.get('annote','See source metadata/reference audit and claim events.')),'locators':r.get('locators',''),'url':r.get('url','')}for r in rs]
    a['verification_scope']=' || '.join(f"[{r['part']}; {r['key']}; {r['note']}] {r['scope']}"for r in a['verification_scopes'])
    a['locators']=' || '.join(unique(r.get('locators','')for r in rs if r.get('locators')))
    a['original_records']=rs
    for g in bibproposal['exact_alias_groups']:
        if g['canonical_key']==key:
            a.update({k:v for k,v in g['canonical_metadata_proposal'].items()if v is not None});a['verification_scope']+=' Scope guard: '+g['required_scope_preservation']
    refs.append(a)
refkeys={r['key']for r in refs}
for c in claims.values():c['refs']=unique(bibaliases.get(x,x)for x in c['refs'])
for p in problems:p['refs']=unique(bibaliases.get(x,x)for x in p['refs'])
refs.sort(key=lambda r:r['key'].lower())
def bibescape(v):return str(v).replace('{','(').replace('}',')')
with (OUT/'SA16_references.bib').open('w') as f:
    f.write('% note=verified means a source URL opened; verification_scope says exactly what was verified.\n% Historical attribution and proof checking are separate from access.\n\n')
    for r in refs:
        f.write('@'+r.get('type','misc')+'{'+r['key']+',\n')
        fields={k:v for k,v in r.items()if k not in ['key','type','source_part','original_records','verification_scopes'] and not isinstance(v,(list,dict))}
        f.write(',\n'.join('  '+k+' = {'+bibescape(v)+'}'for k,v in fields.items())+'\n}\n\n')
dump('SA16_reference_audit.json',refs)
writet('SA16_id_aliases.tsv',[{'kind':'item','old_id':k,'canonical_id':v}for k,v in itemaliases.items()]+[{'kind':'claim','old_id':k,'canonical_id':v}for k,v in claimaliases.items()]+[{'kind':'reference','old_id':k,'canonical_id':v}for k,v in bibaliases.items()],['kind','old_id','canonical_id'])

readings=[];links=[];events=[]
eventparts=allparts+['cote62/supplement_katz']
for p in allparts:
    readings+=tsv(ROOT/'work/parts'/p/'readings.tsv')
    for r in tsv(ROOT/'work/parts'/p/'links.tsv'):
        r['source_part']=p
        for k in ['from','to','note_ids']:r[k]=replaceids(r[k])
        links.append(r)
for p in eventparts:
    for r in tsv(ROOT/'work/parts'/p/'check_events.tsv'):
        old=r['statement_id'];r['original_statement_id']=old;r['statement_id']=cid(bibaliases.get(old,old));r['source_part']=p
        if r.get('refined_statement_id'):r['refined_statement_id']=cid(r['refined_statement_id'])
        a=r.get('artifact','')
        if a and not a.startswith(('work/','sources/')):r['artifact']='work/parts/'+p+'/'+a
        events.append(r)
for r in tsv(ROOT/'work/outputs/cross_merge_check_events.tsv'):
    r['original_statement_id']=r['statement_id'];r['statement_id']=cid(r['statement_id']);r['source_part']='cross_merge_review';events.append(r)
events+=merge_events
for r in tsv(ROOT/'work/outputs/cross_consolidation_check_events.tsv'):
    r['original_statement_id']=r['statement_id'];r['statement_id']=cid(r['statement_id']);r['source_part']='cross_problem_claim_review';events.append(r)
for m in itemmerge['links_not_merges']:
    ids=unique(cid(x)for x in m['item_ids']);passages=m['passages_read']
    links.append({'kind':'folder','from':ids[0]+' '+json.dumps(passages[0],ensure_ascii=False),'to':';'.join(ids[1:])+' '+json.dumps(passages[1:],ensure_ascii=False),'what':m['rationale'],'evidence':'Both endpoints read; '+m['decision_id']+' in work/outputs/cross_merge_proposals.json','note_ids':';'.join(unique(s for x in ids for s in items[x]['sources'])),'source_part':'global cross-merge review','verification':'both endpoints read; link, not identity'})
writet('SA16_readings.tsv',readings,['cote','scan','line','reading','alternative','evidence','weight','confidence'])
writet('SA16_links.tsv',links,['kind','from','to','what','evidence','note_ids'])
writet('SA16_our_projects.tsv',[r for r in links if r['kind']=='our projects'],['kind','from','to','what','evidence','note_ids'])
writet('SA16_link_audit.tsv',links,['kind','from','to','what','evidence','note_ids','source_part','verification','endpoint_status'])
writet('CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome','artifact','scope','refined_statement_id','original_statement_id','source_part'])
dump('SA16_items.json',sorted(items.values(),key=lambda x:sortid(x['id'])))
dump('SA16_claims.json',sorted(claims.values(),key=lambda x:sortid(x['id'])))
dump('SA16_problems.json',sorted(problems,key=lambda x:sortid(x['id'])))

coverage=[]
for p in allparts:
    rows=tsv(ROOT/'work/parts'/p/'claim_search_coverage.tsv');byid={r.get('claim_id'):r for r in rows}
    for c in data[p]['claims']:
        row=byid.get(c['id'],{});ids=c.get('search_ids',row.get('search_ids',row.get('search_groups',c.get('search_groups',c.get('literature_search_group',[])))))
        coverage.append({'claim_id':cid(c['id']),'original_claim_id':c['id'],'source_part':p,'search_ids_or_groups':json.dumps(ids,ensure_ascii=False),'search_record':'work/parts/'+p+'/search_log.tsv','exact_fate':c['fate'],'refs':';'.join(bibaliases.get(x,x)for x in c['refs']),'mapping_detail':json.dumps(row,ensure_ascii=False)})
writet('SA16_claim_search_coverage.tsv',coverage,['claim_id','original_claim_id','source_part','search_ids_or_groups','search_record','exact_fate','refs','mapping_detail'])
inv=readj(ROOT/'work/outputs/source_inventory.json');folderrows=[]
for r in inv:
    f=ROOT/'sources'/r['file'];name=f.stem.replace('_transcription','')
    part='cote63'if '63-'in name else'cote62'if'62' in name else'cote64_early'if name in ['MPL_64_002-039','MPL_64_040-077']else'cote64_late'
    folderrows.append({'folder':name,'cote':','.join(r['cote']),'source_file':r['file'],'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'physical_lines':r['lines'],'scan_labels':';'.join(r['scans']),'read_scope':'complete supplied transcription and associated notes; see source read logs','review_part':'work/parts/'+part,'original_scans':'not supplied; no ink adjudication'})
writet('SA16_folder_coverage.tsv',folderrows,list(folderrows[0]))
missingrefs=sorted(set(x for c in list(claims.values())+problems for x in c['refs'])-refkeys)
missingitems=sorted(set(x for c in claims.values()for x in c['items'])-set(items))
counts={'source_entries':len(indexids),'entry_verdicts':len(entryrows),'verdicts':dict(collections.Counter(r['verdict']for r in entryrows)),'items':len(items),'items_by_kind':dict(collections.Counter(x['kind']for x in items.values())),'claims':len(claims),'claims_by_class':dict(sorted(collections.Counter(x['class']for x in claims.values()).items())),'claims_by_status_on_pages':dict(collections.Counter(x['status_on_pages']for x in claims.values())),'problems':len(problems),'readings':len(readings),'links':len(links),'links_by_kind':dict(collections.Counter(r['kind']for r in links)),'references':len(refs),'references_by_note':dict(collections.Counter(r['note']for r in refs)),'check_events':len(events),'transcription_files':len(inv),'claim_source_occurrences_searched':len(coverage),'source_parts':allparts}
assert len(indexids)==len(set(indexids))==366
assert set(indexids)==set(r['entry_id']for r in entryrows) and len(entryrows)==366
assert not missingrefs,missingrefs
assert not missingitems,missingitems
assert set(r['item_id']for r in entryrows)==set(items)
assert all(r['verdict'] in ['kept','merged','corrected','withdrawn','rests on a misreading']for r in entryrows)
assert all(r['note']in ['verified','unverified']for r in refs)
assert all(r['kind']in ['folder','published work','our projects']for r in links)
dump('SA16_counts.json',counts)
dump('SA16_structural_validation.json',{'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'entry_coverage':'366/366 unique, exact NOTES_INDEX match','item_source_coverage':len(items),'missing_references':missingrefs,'missing_claim_item_links':missingitems,'bibliography_alias_groups':len(bibproposal['exact_alias_groups']),'item_merges':len(itemaliases),'claim_merges':len(claimaliases),'supplement_received':(supp/'claims.json').exists(),'counts':counts})
print(json.dumps(counts,ensure_ascii=False,indent=2))
