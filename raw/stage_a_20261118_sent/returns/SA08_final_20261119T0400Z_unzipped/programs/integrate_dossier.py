"""Serialize the manually adjudicated cross-packet consolidation.

This is bookkeeping, not an entry-reading or literature-classification algorithm.
The explicit merge lists below were chosen by root after reading the records and
the passages; an independent early-packet reviewer checked the main overlaps.
All original authored records remain in work/, and aliases retain their IDs.
"""
from pathlib import Path
import collections, copy, csv, datetime, json, re

R=Path(__file__).resolve().parents[1]
O=R/'outputs'; O.mkdir(exist_ok=True)
PARTS=['early','middle','late','root']
WHO='GPT-6 Astra Pro; effort not exposed by runtime; SA08/root integration'
DATE='2026-11-19'
def readj(p): return json.loads(p.read_text())
def writej(name,data): (O/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def readt(p):
    return list(csv.DictReader(p.open(newline=''),delimiter='\t')) if p.exists() else []
def writet(name,fields,rows):
    with (O/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore'); w.writeheader();w.writerows(rows)
def uniq(xs):
    out=[]; seen=set()
    for x in xs:
        h=json.dumps(x,sort_keys=True,ensure_ascii=False)
        if h not in seen: out.append(x);seen.add(h)
    return out
def sid(n):return f'SA08-{n}'
def cid(n):return f'SA08-C{n:03}'
def pid(n):return f'MP-SA08-{n:02}'

# Same semantic objects or assertions, with occurrence-specific scope retained.
ITEM_GROUPS={
 23:[235,492],111:[230,409],16:[232,471],13:[264],3:[271,470],
 37:[239,472],50:[423],44:[419],53:[420],52:[431],79:[475],
 96:[206],107:[275,236],108:[284],455:[279],456:[280],
 457:[281],458:[282],276:[452],278:[313],277:[306],305:[453],
}
CLAIM_GROUPS={
 14:[30],32:[215],31:[212],33:[216],35:[222],11:[166],12:[173],
 13:[284],48:[241],148:[210],154:[209],161:[916],168:[908],
 247:[923],259:[903],
}
CLAIM_CLASS_OVERRIDES={11:'B',148:'C',154:'C',259:'C'}
CONFIDENCE_OVERRIDES={194:'medium',196:'low',197:'high',198:'high',199:'high',501:'high',502:'high'}
PROBLEM_GROUPS={4:[68],10:[37],16:[64],17:[66],18:[67],20:[38],
                23:[99],50:[94],51:[118],78:[91],49:[103]}
MERGE_REASONS={
 'item':'Same object, assertion, question or exact literature comparison at distinct supplied occurrences; scope differences are retained in the merged record.',
 'claim':'Same assertion or its equivalent categorical presentation; all loci, page statuses, proof limits and literature qualifications are retained.',
 'problem':'The same authorial question reappears in another packet; distinct hypotheses and stages of the question are retained.'}
aliases={'item':{},'claim':{},'problem':{}}
for kind,groups,make in [('item',ITEM_GROUPS,sid),('claim',CLAIM_GROUPS,cid),('problem',PROBLEM_GROUPS,pid)]:
    for dst,srcs in groups.items():
        for src in srcs:aliases[kind][make(src)]=make(dst)

refpath=R/'work/integration/reference_aliases.json'
REFS=readj(refpath) if refpath.exists() else {}
if isinstance(REFS,dict) and 'aliases' in REFS:REFS=REFS['aliases']
def ref(r):
    v=REFS.get(r,r)
    return v.get('canonical',r) if isinstance(v,dict) else v
def rid(s):
    for a in aliases.values():
        if s in a:return a[s]
    return ref(s)

LOC={'A':'MPL_136_002-046','B':'MPL_136_047-094','P':'MPL_136_095-141',
     'Q':'MPL_136_189-234','D':'MPL_136_235-281','E':'MPL_136_282-327'}
def line_records(value):
    if isinstance(value,list):
        out=[]
        for d in value:
            if isinstance(d,dict):
                d=copy.deepcopy(d)
                if 'file' in d and '/' not in d['file']:
                    d['file']=('codex/' if d['file'].startswith('K136-') else 'pro/')+d['file']
                out.append(d)
            else:out.extend(line_records(d))
        return out
    if not value:return []
    value=str(value)
    ms=list(re.finditer(r'(?:(pro|codex)/)?((?:MPL_136_\d+-\d+|K136-\d+)_transcription\.tex):\s*([^;]+)',value))
    if ms:return [{'file':(m.group(1) or ('codex' if m.group(2).startswith('K') else 'pro'))+'/'+m.group(2),'lines':m.group(3).strip()} for m in ms]
    markers=list(re.finditer(r'\b([ABPQDE])\s*(?=\d|notes)',value))
    if markers:
        out=[]
        for i,m in enumerate(markers):
            part=value[m.end():markers[i+1].start() if i+1<len(markers) else len(value)].strip(' ;')
            notes=part.startswith('notes')
            out.append({'file':('notes/pro/' if notes else 'pro/')+LOC[m.group(1)]+('_notes.md' if notes else '_transcription.tex'),'lines':part.removeprefix('notes').strip()})
        return out
    return [{'locator':value,'scope':'context or composite locator; use the preserved original record'}]

original={}
for typ in ['items','claims','problems']:
    original[typ]=[]
    for part in PARTS:
        p=R/'work'/part/(typ+'.json')
        if p.exists():
            for x in readj(p):
                x=copy.deepcopy(x);x['_packet_owner']=part;original[typ].append(x)

# Exact brief source quotations were manually audited separately from the claims.
quote_path=R/'work/root/quote_overrides.json'
if quote_path.exists():
    q=readj(quote_path)
    for c in original['claims']:
        if c['id'] in q:
            c['his_statement']=q[c['id']]['his_statement']
            c['_quotation_lines']=q[c['id']].get('quotation_lines','')
            if 'lines' in q[c['id']]:c['lines']=q[c['id']]['lines']
rootlinks=R/'work/root/claim_item_links.json'
if rootlinks.exists():
    cl=readj(rootlinks)
    for c in original['claims']:c['items']=uniq(c['items']+cl.get(c['id'],[]))

def paragraphs(records,key):
    vals=[]
    for x in records:
        v=x.get(key,'')
        if not v:continue
        if isinstance(v,(list,dict)):v=json.dumps(v,ensure_ascii=False)
        vals.append((x['id'],v))
    if len(vals)==1:return vals[0][1]
    return '\n\n'.join(f"[{k}] {v}" for k,v in vals)
def group_records(typ,kind):
    groups={}
    for x in original[typ]:groups.setdefault(aliases[kind].get(x['id'],x['id']),[]).append(x)
    for ident,g in groups.items():g.sort(key=lambda x:(x['id']!=ident,x['id']))
    return groups

items=[]; itemgroups=group_records('items','item')
for ident,g in itemgroups.items():
    b=copy.deepcopy(g[0]);b['id']=ident
    b['sources']=uniq(s for x in g for s in x['sources'])
    b['scans']=sorted(set(s for x in g for s in x['scans']))
    b['lines']=uniq(z for x in g for z in line_records(x['lines']))
    b['cote']=136
    for k in ['his_words','statement','reconstruction','check_reason']:b[k]=paragraphs(g,k)
    checks=uniq(x['check'] for x in g)
    if len(checks)>1:
        # This only reports already-authored assessments; it does not read a note.
        b['check']=next((x for x in ['misreads','not on the page','overstates','understates','agrees'] if x in checks),checks[0])
        b['check_reason']+='\n\nOccurrence checks: '+', '.join(x['id']+'='+x['check'] for x in g)+'.'
    fields=['id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason']
    items.append({k:b[k] for k in fields})
items.sort(key=lambda x:int(x['id'].split('-')[-1]))

claims=[]; claimgroups=group_records('claims','claim')
for ident,g in claimgroups.items():
    b=copy.deepcopy(g[0]);b['id']=ident;b['cote']=136
    b['items']=uniq(aliases['item'].get(s,s) for x in g for s in x['items'])
    b['scans']=sorted(set(s for x in g for s in x['scans']))
    b['lines']=uniq(z for x in g for z in line_records(x['lines']))
    for k in ['his_statement','statement','status_on_pages','computation','fate','present_status']:b[k]=paragraphs(g,k)
    if len(g)>1:b['fate_date']={x['id']:x['fate_date'] for x in g}
    n=int(ident.split('C')[-1]);b['class']=CLAIM_CLASS_OVERRIDES.get(n,b['class'])
    b['confidence']=CONFIDENCE_OVERRIDES.get(n,b['confidence'])
    b['refs']=uniq(ref(r) for x in g for r in x['refs'])
    if not str(b['present_status']).startswith('As of'):b['present_status']='As of November 2026: '+b['present_status']
    fields=['id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence']
    claims.append({k:b[k] for k in fields})
claims.sort(key=lambda x:int(x['id'].split('C')[-1]))
claimmap={c['id']:c for c in claims}

def occurrence(o):
    o=copy.deepcopy(o)
    if quote_path.exists() and o.get('claim') in q:
        v=q[o['claim']]
        if 'lines' in v:o['lines']=v['lines']
        if 'his_words' in o:o['his_words']=v['his_statement']
    if 'claim' in o:o['claim']=aliases['claim'].get(o['claim'],o['claim'])
    if 'lines' in o:o['lines']=line_records(o['lines'])
    if 'cote' in o:o['cote']=136
    return o
problems=[]; problemgroups=group_records('problems','problem')
for ident,g in problemgroups.items():
    if ident=='MP-SA08-65':continue  # compound occurrence distributed below
    b=copy.deepcopy(g[0]);b['id']=ident
    b['occurrences']=uniq(occurrence(z) for x in g for z in x['occurrences'])
    for k in ['as_he_states','plausible_today','state_of_art','why_open','worth']:
        if len(g)>1:b[k]=paragraphs(g,k)
    b['refs']=uniq(ref(r) for x in g for r in x['refs'])
    fields=['id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs']
    problems.append({k:b[k] for k in fields})
pmap={p['id']:p for p in problems}
# MP65 was a compound positive/negative/derived summary, not a new question.
p65=next(p for p in original['problems'] if p['id']=='MP-SA08-65')
split65={
 'MP-SA08-15':(['SA08-C215'],'The later tail calculation again asks for all-coefficient binomial rigidity. Its nonnegative answer is the weighted-family theorem.'),
 'MP-SA08-16':(['SA08-C215','SA08-C230'],'The later coefficient presentation is an explicit left adjoint, distinct from the right section functor. The unit is asserted in the nonnegative range.'),
 'MP-SA08-18':(['SA08-C286'],'The coefficient left adjoint L is exact by prime-local cofinal rows, supplying the injective-preservation step for the special finite-tail theorem.'),
 'MP-SA08-19':(['SA08-C239','SA08-C286'],'The negative presentation represents Q and therefore gives Hom_Z(Q,M), not M tensor Q. Coherent roots are stronger than merely infinite height.'),
}
for ident,(cs,description) in split65.items():
    p=pmap[ident]
    newocc=[]
    for o in p65['occurrences']:
        if o.get('claim') not in cs:continue
        o=copy.deepcopy(o)
        if o.get('claim')=='SA08-C286':
            if ident=='MP-SA08-18':o.update(scans=[277],lines=[{'file':'pro/MPL_136_235-281_transcription.tex','lines':'1695–1705'}])
            elif ident=='MP-SA08-19':o.update(scans=[299],lines=[{'file':'pro/MPL_136_282-327_transcription.tex','lines':'688–707'}])
        newocc.append(occurrence(o))
    p['occurrences']=uniq(p['occurrences']+newocc)
    p['plausible_today']+='\n\n[Distributed later occurrence MP-SA08-65] '+description
    p['state_of_art']=paragraphs([{'id':ident,'state_of_art':p['state_of_art']},{'id':'MP-SA08-65','state_of_art':description+' See the linked claims for exact proof and search scope.'}],'state_of_art')
    p['refs']=uniq(p['refs']+[ref(r) for r in p65['refs']])
problems.sort(key=lambda x:int(x['id'].split('-')[-1]))

entries=[]
for part in PARTS:
    for e in readt(R/'work'/part/'entries.tsv'):
        old=e['item_id'];new=aliases['item'].get(old,old);e['item_id']=new
        if e['verdict'].startswith('merged'):e['verdict']='merged into '+new
        if old!=new:
            e['reason']+=' Cross-packet consolidation: '+old+' is merged into '+new+'; its local correction or scope is retained.'
            if e['verdict']=='kept':e['verdict']='merged into '+new
        entries.append(e)
source_order={r['entry_id']:i for i,r in enumerate(readt(R/'sources/notes/NOTES_INDEX.tsv'))}
entries.sort(key=lambda x:source_order.get(x['entry_id'],99999))

readings=[]; links=[]; projects=[]; events=[]
for part in PARTS:
    readings+=readt(R/'work'/part/'readings.tsv')
    for x in readt(R/'work'/part/'links.tsv'):
        (projects if x['kind']=='our projects' else links).append(x)
    for x in readt(R/'work'/part/'CHECK_EVENTS.tsv'):
        # Agents use the required five columns, with one historical spelling.
        x={('who' if k.startswith('who') else k):v for k,v in x.items()}
        old=x.get('statement_id','');new=rid(old);x['statement_id']=new
        if old!=new:x['outcome']='[Original record '+old+'; canonical '+new+'] '+x.get('outcome','')
        if x.get('type','').startswith('refuted'):x['type']='refuted, with refined statement '+new+'.statement'
        events.append(x)
for f in [R/'work/integration/REFERENCE_CHECK_EVENTS.tsv',R/'work/integration/PROSE_CHECK_EVENTS.tsv',R/'work/root/quotation_CHECK_EVENTS.tsv',R/'work/root/peer_CHECK_EVENTS.tsv',R/'work/root/item_CHECK_EVENTS.tsv']:
    for x in readt(f):
        old=x.get('statement_id','');x['statement_id']=rid(old);events.append(x)
for kind,a in aliases.items():
    for old,new in a.items():events.append(dict(statement_id=new,date=DATE,who=WHO,type='used and rechecked in this run',outcome='Cross-packet semantic comparison with '+old+': '+MERGE_REASONS[kind]+' This consolidation is not an independent proof of the entire mathematical assertion.'))
for ident in split65:
    events.append(dict(statement_id=ident,date=DATE,who=WHO,type='used and rechecked in this run',outcome='The compound MP-SA08-65 occurrence was distributed to the separately scoped positive, adjunction, derived, and negative questions; source formulations remain in work/late/problems.json.'))

if (R/'work/integration/project_access_audit.json').exists():
    for ident in ['SA08-2','SA08-238','SA08-283','SA08-303','SA08-401']:
        events.append(dict(statement_id=ident,date=DATE,who='GPT-6 Astra Pro; effort not exposed by runtime; SA08/early bounded access check',type='used and rechecked in this run',outcome='Exact named external context targets were not resolved by five read-only available-file searches (21 target queries). Bounded ranked continuations were not exhausted. No target passage, cross-project mathematical implication or novelty claim was verified; see project_access_audit.md.'))

# Dedicated provenance tables may contain additional context rows not in links.tsv.
extra_project_files=[]
for part in PARTS:
    for n in ['project_links.tsv','external_project_links.tsv','project_context_provenance.tsv']:
        p=R/'work'/part/n
        if p.exists():
            rows=readt(p)
            extra_project_files.append({'path':str(p.relative_to(R)),'records':rows})
            for row in rows:
                if 'kind' in row:projects.append(row)
                elif 'project_link_id' in row:
                    notes=row['source_entries']
                    notes=re.sub(r'\bD#',LOC['D']+'#',notes)
                    notes=re.sub(r'\bE#',LOC['E']+'#',notes)
                    projects.append({'kind':'our projects','from':'cote136 scans '+row['local_locator'],
                         'to':row['reported_external_locator']+'; reported runs: '+row['reported_runs'],
                         'what':row['reported_relation'],'evidence':row['verification'],
                         'note_ids':notes})
writej('SA08_project_provenance.json',extra_project_files)

writej('SA08_items.json',items);writej('SA08_claims.json',claims);writej('SA08_problems.json',problems)
writet('SA08_entries.tsv',['entry_id','item_id','verdict','reason'],entries)
writet('SA08_readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],uniq(readings))
writet('SA08_links.tsv',['kind','from','to','what','evidence','note_ids'],uniq(links))
writet('SA08_project_links.tsv',['kind','from','to','what','evidence','note_ids'],uniq(projects))
writet('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],uniq(events))

merge_rows=[dict(entity=k,original_id=a,canonical_id=b,reason=MERGE_REASONS[k]) for k,m in aliases.items() for a,b in m.items()]
merge_rows.append(dict(entity='problem',original_id='MP-SA08-65',canonical_id=';'.join(split65),reason='Compound summary split among the already-existing positive, adjunction, derived and negative questions, without dropping an occurrence.'))
writet('SA08_id_aliases.tsv',['entity','original_id','canonical_id','reason'],merge_rows)
primary={e['entry_id']:e['item_id'] for e in entries}
expansion=[dict(entry_id=s,item_id=x['id'],role='primary verdict item' if primary[s]==x['id'] else 'additional semantic facet of composite entry') for x in items for s in x['sources']]
writet('SA08_entry_item_expansion.tsv',['entry_id','item_id','role'],expansion)

audits=[]; searches=[]
for ident,g in claimgroups.items():
    audit={'id':ident,'components':[]}
    for c in g:
        extra={k:v for k,v in c.items() if k not in ['items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence']}
        extra.update({'source_id':c['id'],'lines':c['lines'],'class_before_consolidation':c['class']})
        extra['confidence_scope']=c['confidence']
        audit['components'].append(extra)
        records=c.get('search_logs') or c.get('search_record') or c.get('searches')
        if not records:
            records=(c['fate'].split('Search:',1)[1] if 'Search:' in c['fate'] else c['fate'])
        searches.append(dict(claim_id=ident,original_id=c['id'],search_record=json.dumps(records,ensure_ascii=False),primary_reference_keys=';'.join(ref(r) for r in c['refs']),scope='Exact source hypotheses and negative-search limits are in fate; a nearby theorem is not treated as an identical result.'))
    audits.append(audit)
writej('SA08_claim_audit.json',audits)
writet('SA08_claim_searches.tsv',['claim_id','original_id','search_record','primary_reference_keys','scope'],searches)

def status_bin(c):
    # A display-only reporting bin. Full source-authored statuses are preserved.
    s=c['status_on_pages'].lower()
    if any(w in s for w in ['our refined','our completed','our replacement']):return 'explicit reconstruction record'
    if 'false' in s or 'refuted' in s:return 'false or defective as stated/transcribed'
    if any(w in s for w in ['withdrawn','corrected by himself','cancelled','retracted']):return 'withdrawn or corrected by him'
    if any(w in s for w in ['open','question','incomplete','conjectur','left to the reader','left unchecked']):return 'open, questioned or deferred on the pages'
    if any(w in s for w in ['proved there','proved on pages','proved by','definition','formal consequence']):return 'proved or formal on the pages'
    if any(w in s for w in ['sketch','calculation','computation','direct construction','with explanation','verification']):return 'construction, computation or proof sketched'
    return 'stated, cited or reproduced'
inventory=[]
for f in sorted((R/'sources/texts').rglob('*_transcription.tex')):
    scans=list(map(int,re.findall(r'\\scanpage\{(\d+)\}',f.read_text())))
    inventory.append({'file':str(f.relative_to(R/'sources/texts')),'scan_count':len(scans),'scans':scans,'missing_inside_span':sorted(set(range(min(scans),max(scans)+1))-set(scans))})
stats=dict(entries=len(entries),items=len(items),claims=len(claims),problems=len(problems),readings=len(uniq(readings)),links=len(uniq(links)),project_leads=len(uniq(projects)),check_events=len(uniq(events)),
           verdicts=dict(collections.Counter('merged' if e['verdict'].startswith('merged') else e['verdict'] for e in entries)),item_kinds=dict(collections.Counter(x['kind'] for x in items)),claims_by_class=dict(collections.Counter(x['class'] for x in claims)),claims_by_status=dict(collections.Counter(status_bin(x) for x in claims)),source_scans=sum(x['scan_count'] for x in inventory),source_files=inventory,
           original_record_counts={k:len(v) for k,v in original.items()},indexed_source_items=sum(bool(i['sources']) for i in items),codex_lead_items=sum(not i['sources'] and any(isinstance(z,dict) and z.get('file','').startswith('codex/') for z in i['lines']) for i in items),additional_pro_text_items=sum(not i['sources'] and not any(isinstance(z,dict) and z.get('file','').startswith('codex/') for z in i['lines']) for i in items),aliases=len(merge_rows),reference_aliases_loaded=bool(REFS),root_quotation_audit_loaded=quote_path.exists())
writej('SA08_statistics.json',stats)
print(json.dumps({k:v for k,v in stats.items() if k!='source_files'},ensure_ascii=False,indent=2))
