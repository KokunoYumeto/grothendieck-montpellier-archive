"""Read-only bookkeeping audit of assembled SA21 and current part inputs.
Writes only within parts/final_audit. No mathematical verdict is inferred.
"""
from pathlib import Path
import csv,json,re,hashlib,collections,ast
P=Path(__file__).parent;R=P.parents[1]
def jr(p):return json.loads(p.read_text())
def tr(p):return list(csv.DictReader(p.open(newline=''),delimiter='\t'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
partnames=['root','cotes_3_5','cotes_6_7','cotes_8_9','cotes_9_09_13','cotes_9_14_18','project_links']
eventnames=['check_events.tsv','extra_check_events.tsv','additional_reference_events.tsv','supplemental_check_events.tsv']
refs={};events=[];claims=[];problems=[];links=[];hashes=[]
for name in partnames:
    p=R/'parts'/name
    for f in ['claims.json','problems.json','links.tsv','references.bib']+eventnames:
        q=p/f
        if q.exists():hashes.append({'path':str(q.relative_to(R)),'sha256':sha(q)})
    for fn,target in [('claims.json',claims),('problems.json',problems)]:
        if (p/fn).exists():
            target.extend(dict(x,audit_source=name) for x in jr(p/fn))
    for fn in eventnames:
        if (p/fn).exists():events.extend(dict(e,audit_source=name) for e in tr(p/fn))
    if (p/'links.tsv').exists():links.extend(dict(x,audit_source=name) for x in tr(p/'links.tsv'))
    if (p/'references.bib').exists():
        for block in re.split(r'(?=^@)',(p/'references.bib').read_text(),flags=re.M):
            m=re.match(r'@\w+\s*\{\s*([^,]+)',block)
            if m:refs.setdefault(m.group(1).strip(),[]).append({'part':name,'entry':block.strip()})
eventids=collections.Counter(e['statement_id'] for e in events)
used=collections.defaultdict(list)
for x in claims+problems:
    for key in x.get('refs',[]):used[key].append(x['id'])
alias={'Esquisse1997':'Esquisse1984','CSG2026':'CSGUnpublished','SGA4I1972':'SGA4II','MontpellierCatalogue':'MontpellierArchive','MontpellierSA21':'MontpellierArchive'}
def evcount(k):
    target=alias.get(k,k)
    return sum(n for eid,n in eventids.items() if alias.get(eid,eid)==target)
noevents=[{'key':k,'used_by':used[k],'source_parts':[v['part'] for v in vals],
           'entry':vals[0]['entry']} for k,vals in refs.items() if not evcount(k)]
unresolved=[]
phrases=['target absent','cannot be checked','explicitly unresolved','not a proved identification',
 'not identified/opened','unresolved reference-reading alarm','unresolved forward reference']
assembly_source=(R/'code/assemble.py').read_text()
for line in assembly_source.splitlines():
    if "elif any(t in x['evidence'].lower()" in line:
        phrases=ast.literal_eval(re.search(r'for t in (\[.*\])\)',line).group(1))
other_flags=['unverified','not verified','not read','not opened','not supplied','absent','missing',
 'unresolved','uncertain','candidate','pending','not checked','unavailable','not inspected','no exact','probable']
for n,x in enumerate(links):
    if x['kind']=='our projects':continue
    ev=x['evidence'].lower()
    suspicious=[s for s in other_flags if s in (x['to']+' '+x['what']+' '+x['evidence']).lower()]
    if suspicious:
        unresolved.append({'ordinal_in_inputs':n+1,'would_be_verified_by_assembler':not any(s in ev for s in phrases),
                            'flags':suspicious,**x})
master={}
for name in ['SA21_claims.json','SA21_problems.json','SA21_items.json','SA21_links.tsv','SA21_references.bib','CHECK_EVENTS.tsv']:
    q=R/name
    if q.exists():master[name]={'sha256':sha(q),'bytes':q.stat().st_size}
mc=jr(R/'SA21_claims.json') if (R/'SA21_claims.json').exists() else []
mi=jr(R/'SA21_items.json') if (R/'SA21_items.json').exists() else []
mb=set(re.findall(r'@\w+\s*\{\s*([^,]+)',(R/'SA21_references.bib').read_text()))
mid={x['id'] for x in mi}
bad_items=[(x['id'],i) for x in mc for i in x.get('items',[]) if i not in mid]
bad_refs=[(x['id'],k) for x in mc for k in x.get('refs',[]) if k not in mb]
mp=jr(R/'SA21_problems.json') if (R/'SA21_problems.json').exists() else []
bad_problem_refs=[(x['id'],k) for x in mp for k in x.get('refs',[]) if k not in mb]
ml=tr(R/'SA21_links.tsv') if (R/'SA21_links.tsv').exists() else []
typed_link_ids=[{'from':x['from'],'to':x['to'],'note_ids':x['note_ids']} for x in ml
                if any(t in x.get('note_ids','') for t in ['C-SA21-','MP-SA21-'])]
directions=jr(R/'audit/directions.json') if (R/'audit/directions.json').exists() else []
valid_by_field={'items':mid,'claims':{x['id'] for x in mc},'problems':{x['id'] for x in mp}}
bad_directions=[{'rank':x['rank'],'field':field,'id':i} for x in directions
                for field,valid in valid_by_field.items() for i in x.get(field,[]) if i not in valid]
partids={x['id'] for x in claims};masterids={x['id'] for x in mc}
rep={'part_claim_count':len(claims),'master_claim_count':len(mc),
     'claims_missing_from_master':sorted(partids-masterids),'claims_extra_in_master':sorted(masterids-partids),
     'duplicate_part_claim_ids':[k for k,n in collections.Counter(x['id'] for x in claims).items() if n>1],
     'part_bib_keys':len(refs),'keys_without_direct_check_event':noevents,
     'bad_master_item_pointers':bad_items,'bad_master_ref_keys':bad_refs,
     'bad_master_problem_ref_keys':bad_problem_refs,'claim_or_problem_ids_in_link_note_ids':typed_link_ids,
     'direction_count_inspected':len(directions),'bad_direction_pointers':bad_directions,
     'link_candidates_for_manual_review':unresolved,'master_snapshot':master,'input_hashes':hashes}
(P/'snapshot.json').write_text(json.dumps(rep,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in rep.items() if k not in ['link_candidates_for_manual_review','master_snapshot','input_hashes']},ensure_ascii=False,indent=2))
