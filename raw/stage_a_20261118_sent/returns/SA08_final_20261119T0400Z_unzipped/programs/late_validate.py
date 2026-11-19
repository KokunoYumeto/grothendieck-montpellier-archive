"""Final referential, literal-source and coverage checks for the late dossiers.

This validator checks serialization and audit records. It does not assign
mathematical verdicts and is not itself a theorem or novelty test.
"""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

B=Path('/workspace/scratch/7feb9690b71f/SA08_work')
P=B/'work/late'
errors=[]
checks=[]
def check(condition,label,detail=None):
    checks.append({'check':label,'passed':bool(condition)})
    if not condition:
        errors.append({'check':label,'detail':detail})
def js(name):
    return json.loads((P/name).read_text())
def tsv(name):
    with (P/name).open() as f:
        return list(csv.DictReader(f,delimiter='\t'))
items=js('items.json'); claims=js('claims.json'); problems=js('problems.json')
refs=js('reference_verification.json'); audit=js('quotation_audit.json')
entries=tsv('entries.tsv'); readings=tsv('readings.tsv')
links=tsv('links.tsv'); projects=tsv('project_links.tsv')
events=tsv('CHECK_EVENTS.tsv'); searches=tsv('search_log.tsv')
queries=tsv('search_queries.tsv')
I={x['id']:x for x in items}; C={x['id']:x for x in claims}
R={x['key']:x for x in refs}; A={x['id']:x for x in audit}
for name,rows,key,expected in [
    ('items',items,'id',122),('claims',claims,'id',90),
    ('problems',problems,'id',30),('references',refs,'key',38),
    ('entries',entries,'entry_id',163),('readings',readings,None,73),
    ('links',links,'link_id',55),('project links',projects,'project_link_id',14),
    ('search families',searches,'search_id',20),('query records',queries,None,169)]:
    check(len(rows)==expected,name+' count',len(rows))
    if key:
        check(len({x[key] for x in rows})==len(rows),name+' unique identifiers')
check(set(C)=={f'SA08-C{n}' for n in range(201,291)},'complete claim identifier interval')
check({p['id'] for p in problems}=={f'MP-SA08-{n}' for n in range(60,90)},'complete problem interval')
expected_entries={f'MPL_136_235-281#{n}' for n in range(1,76)}|{f'MPL_136_282-327#{n}' for n in range(1,89)}
check({e['entry_id'] for e in entries}==expected_entries,'both note packets covered exactly')
source_entries=[]
for f in P.glob('*entries_source.json'):
    source_entries.extend(json.loads(f.read_text()))
check({e['entry_id'] for e in source_entries}==expected_entries,'retained source entry coverage')
for e in entries:
    check(e['item_id'] in I,'entry target '+e['entry_id'])
    if e['item_id'] in I:
        check(e['entry_id'] in I[e['item_id']]['sources'],'entry/item backreference '+e['entry_id'])
entry_map={e['entry_id']:e for e in entries}
for i in items:
    for source in i['sources']:
        check(source in entry_map and entry_map[source]['item_id']==i['id'],'item/entry forward reference '+i['id']+' '+source)

search_ids={s['search_id'] for s in searches}
for c in claims:
    check(bool(c['items']) and set(c['items'])<=set(I),'claim items '+c['id'])
    check(bool(c['refs']) and set(c['refs'])<=set(R),'claim bibliography '+c['id'])
    check(bool(c['searches']) and set(c['searches'])<=search_ids,'claim fate search '+c['id'])
    check(c['id'] in A and bool(c.get('quotation_lines')),'claim literal quotation audit '+c['id'])
    check(c['class'] in 'ABCDEF','claim classification '+c['id'])
    for sid in c['searches']:
        family=next(s for s in searches if s['search_id']==sid)
        check(c['id'] in family['claims'].split(';'),'search/claim reciprocal '+c['id']+' '+sid)
for p in problems:
    check(set(p['claims'])<=set(C),'problem claims '+p['id'])
    check(set(p['items'])<=set(I),'problem items '+p['id'])
    check(set(p['refs'])<=set(R),'problem references '+p['id'])
    check(len(p['refs'])==len(set(p['refs'])),'problem unique reference list '+p['id'])
    check({o['claim'] for o in p['occurrences']}==set(p['claims']),'problem occurrence completeness '+p['id'])
    for o in p['occurrences']:
        c=C.get(o['claim'],{})
        for key in ['cote','scans','lines','his_statement','quotation_lines','quotation_scope']:
            check(o.get(key)==c.get(key),'problem inherited '+key+' '+p['id']+' '+o['claim'])

source_cache={}
scan_cache={}
def source(fn):
    if fn not in source_cache:
        s=(B/'sources/texts'/fn).read_text().splitlines()
        source_cache[fn]=s
        page=None; pages=[]
        for line in s:
            m=re.search(r'\\scanpage\{(\d+)\}',line)
            if m:page=int(m.group(1))
            pages.append(page)
        scan_cache[fn]=pages
    return source_cache[fn]
for a in audit:
    check(len(a['literal_fragments'])==len(a['quotation_lines']),'quote fragment/locator count '+a['id'])
    rec=C.get(a['id'],I.get(a['id'],{}))
    for fragment,loc in zip(a['literal_fragments'],a['quotation_lines']):
        m=re.fullmatch(r'(\d+)(?:[–-](\d+))?',loc['lines'])
        check(m is not None,'quote locator format '+a['id'],loc)
        if not m:continue
        lo=int(m[1]);hi=int(m[2] or m[1]); s=source(loc['file'])
        check(1<=lo<=hi<=len(s),'quote range '+a['id'],loc)
        check(fragment in '\n'.join(s[lo-1:hi]),'literal source exact '+a['id'],loc)
        pages={x for x in scan_cache[loc['file']][lo-1:hi] if x is not None}
        check(pages<=set(rec.get('scans',[])),'quote scan provenance '+a['id'],{'pages':sorted(pages),'record_scans':rec.get('scans')})
for i in items:
    if i['his_words']:
        check(i['id'] in A and bool(i.get('quotation_lines')),'source-bearing item exact quotation '+i['id'])
    else:
        check(i['kind'] in ['idea of the earlier run','other','title, date or page count'],'blank quote is provenance or earlier-run '+i['id'],i['kind'])
for n in [285,286,287]:
    check('No separate authorial assertion' in C[f'SA08-C{n}']['quotation_scope'],'reconstruction is not attributed as authorial '+str(n))
check(C['SA08-C284']['scans']==[273] and 'D1571' in C['SA08-C284']['lines'] and '#74' in C['SA08-C284']['lines'],'C284 final provenance')
check(C['SA08-C205']['class']=='C' and 'not an ordinary K(k,p)' in C['SA08-C205']['statement'],'C205 derived nonlinear correction')
check(C['SA08-C288']['scans']==[262],'C288 exact donor page')

allowed_types={'used and rechecked in this run','carried as background without fault found','independent re-proof','targeted proof check','computation or formal certificate',"refuted, with the refined statement's id"}
event_ids={e['statement_id'] for e in events}
check(set(I)|set(C)|set(R)<=event_ids,'check events cover every item claim and reference')
check({e['type'] for e in events}<=allowed_types,'honest event type vocabulary')
check(all(e['who'].startswith('GPT-6 Astra Pro; effort not exposed by runtime; SA08/') for e in events),'event identity and effort disclosure')
for e in events:
    if e['refined_statement_id']:
        check(e['refined_statement_id'] in C,'refinement target '+e['statement_id'])
    if e['statement_id'] in R and R[e['statement_id']]['note']!='verified':
        check(e['type']=='carried as background without fault found','unverified source not elevated '+e['statement_id'])

all_ids=set(I)|set(C)|{p['id'] for p in problems}
for f in (B/'work').glob('*/*.json'):
    if f.name in ['items.json','claims.json','problems.json']:
        for row in json.loads(f.read_text()):all_ids.add(row['id'])
for link in links:
    check(set(filter(None,link['statement_ids'].split(';')))<=all_ids,'link identifiers '+link['link_id'])
    check(set(filter(None,link['reference_keys'].split(';')))<=set(R),'link references '+link['link_id'])
for p in projects:
    check('unverified lead' in p['verification'],'external project isolation '+p['project_link_id'])
bibkeys=set(re.findall(r'^@\w+\{([^,]+),',(P/'references.bib').read_text(),re.M))
check(bibkeys==set(R),'bibliography/verification exact keys')
for s in searches:
    check(set(filter(None,s['claims'].split(';')))<=set(C),'search claim identifiers '+s['search_id'])
    for fn in s['raw_logs'].split(';'):
        check((B/fn).exists(),'retained family raw log '+s['search_id']+' '+fn)
raw_files=sorted((B/'research').glob('late_web_*.json'))
check(len(raw_files)==32,'all 32 substantive raw web outputs retained',len(raw_files))
for f in raw_files:
    data=json.loads(f.read_text())
    check('args' in data and 'result' in data,'raw query/results record '+f.name)
for q in queries:
    check((B/q['raw_log']).exists(),'retained query output '+q['raw_log'])
for fn in ['programs/late_computations.py','logs/late_computations_output.json','programs/late_quadratic_normalization.py','logs/late_quadratic_normalization.json']:
    check((B/fn).exists(),'computation artifact '+fn)
check('The55 checked links' in (P/'findings.md').read_text(),'prose/link count consistency')
for fn in ['findings.md','directions.md','source_checks.md','proofs.md','search_log.md','root_peer_review.md']:
    check((P/fn).stat().st_size>500,'substantive prose artifact '+fn)

result={
    'validation':'PASS' if not errors else 'FAIL',
    'scope':'Referential integrity, note coverage, literal-source copying, provenance and retained evidence. This is not a mathematical proof or novelty test.',
    'counts':{'items':len(items),'entries':len(entries),'claims':len(claims),'problems':len(problems),'readings':len(readings),'references':len(refs),'links':len(links),'isolated_project_leads':len(projects),'search_families':len(searches),'query_records':len(queries),'raw_search_outputs':len(raw_files),'check_events':len(events),'literal_claims':sum(c['id'] in A for c in claims),'literal_items':sum(i['id'] in A for i in items),'source_fidelity_events':len(tsv('quotation_CHECK_EVENTS.tsv'))},
    'entry_verdicts':dict(Counter(e['verdict'] for e in entries)),
    'claim_classes':dict(Counter(c['class'] for c in claims)),
    'event_types':dict(Counter(e['type'] for e in events)),
    'checks_run':len(checks),'errors':errors,
    'source_hashes':{fn:hashlib.sha256((B/'sources/texts'/fn).read_bytes()).hexdigest() for fn in source_cache},
    'limitations':['No manuscript scans or second-pass files supplied. Diplomatic uncertainty remains unresolved.','External project endpoints remain isolated unverified leads.','Reading a source is not recorded as an independent proof.','Negative searches do not establish novelty.']}
(B/'logs/late_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(1 if errors else 0)
