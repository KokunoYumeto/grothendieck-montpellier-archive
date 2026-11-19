"""Structural audit only; no mathematical verdict is inferred by this program."""
import csv,json,re,hashlib
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parents[1]
ROOT=P.parents[2]
SRC=ROOT/'sources'
MASTER=json.loads((ROOT/'SA14_work/research/entries_source.json').read_text())
PACKS={'MPL_57_271-315','MPL_58_020-067'}
expected={k for k in MASTER if k.split('#')[0] in PACKS}
def table(name):
    with (P/name).open() as f:return list(csv.DictReader(f,delimiter='\t'))
def data(name):return json.loads((P/name).read_text())
E=table('entries.tsv');I=data('items.json');C=data('claims.json');M=data('problems.json')
R=table('readings.tsv');L=table('links.tsv');S=table('search_log.tsv');V=table('CHECK_EVENTS.tsv')
errors=[]
def test(cond,description):
    if not cond:errors.append(description)
test(len(E)==146,'Expected146 entry rows')
test({x['entry_id'] for x in E}==expected,'Source-entry coverage differs from exact master package IDs')
test(len({x['entry_id'] for x in E})==len(E),'Duplicate source-entry verdict')
test(Counter(k.split('#')[0] for k in expected)=={'MPL_57_271-315':61,'MPL_58_020-067':85},'Package entry counts differ')
fields={
'items':{'id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'},
'claims':{'id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'},
'problems':{'id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs'}}
for name,records in [('items',I),('claims',C),('problems',M)]:
    test(len({x['id'] for x in records})==len(records),name+' duplicate IDs')
    for x in records:
        test(fields[name]<=x.keys(),x['id']+' missing fields')
        test(all(x.get(k) not in ['',None,[]] for k in fields[name]),x['id']+' blank required field')
        test(201<=int(x['id'].split('-')[-1])<=399,x['id']+' outside allocated range')
iset={x['id'] for x in I};cset={x['id'] for x in C};mset={x['id'] for x in M}
for x in E:test(x['item_id'] in iset,x['entry_id']+' missing target item')
source_map={s:x['id'] for x in I for s in x['sources']}
test(len(source_map)==sum(len(x['sources']) for x in I),'Source entry occurs in multiple items')
test(set(source_map)==expected,'Item source coverage differs')
for x in E:test(source_map.get(x['entry_id'])==x['item_id'],'Verdict/item source mapping mismatch '+x['entry_id'])
bib=(P/'references.bib').read_text()
bkeys=re.findall(r'@\w+\{([^,]+),',bib)
test(len(bkeys)==len(set(bkeys)),'Duplicate bibliography keys')
for x in C+M:
    test(set(x['refs'])<=set(bkeys),x['id']+' unresolved reference')
    test(len(x['refs'])==len(set(x['refs'])),x['id']+' duplicate reference')
for x in C:
    test(set(x['items'])<=iset,x['id']+' unresolved item')
    test(x['class'] in 'ABCDEF',x['id']+' invalid class')
    test(set(x['search_events'])<={s['event_id'] for s in S},x['id']+' missing search event')
    excerpts=[]
    for loc in x['lines']:
        file,ranges=loc.split(': ',1)
        raw=(SRC/'SA14_texts/pro'/file).read_text().splitlines()
        for a,b in re.findall(r'(\d+)[–-](\d+)',ranges):
            a,b=int(a),int(b);test(1<=a<=b<=len(raw),x['id']+' invalid line range')
            excerpts.append(f'{file}: {a}–{b}\n'+'\n'.join(raw[a-1:b]))
    test(x['his_statement']=='\n\n'.join(excerpts),x['id']+' diplomatic excerpt mismatch')
    file='MPL_57_271-315_transcription.tex' if x['cote']==57 else 'MPL_58_020-067_transcription.tex'
    raw=(SRC/'SA14_texts/pro'/file).read_text()
    scans={int(n) for n in re.findall(r'\\scanpage\{(\d+)\}',raw)}
    test(set(x['scans'])<=scans,x['id']+' nonexistent supplied scan locator')
for x in M:
    for o in x['occurrences']:
        test(o['claim'] in cset,x['id']+' missing claim occurrence')
        test(set(o['items'])<=iset,x['id']+' missing occurrence item')
vids={v['statement_id'] for v in V}
test(iset|cset|mset|set(bkeys)<=vids,'Missing check event for an item, claim, problem or reference')
test(all('effort not exposed' in v['who'] for v in V),'Check-event signature does not follow protocol')
test(all('Text concordance, not mathematical proof.' in v['outcome'] or v['statement_id'].startswith('MP-') for v in V if v['type']=='used and rechecked in this run'),'Documentary event lacks scope label')
for x in L:
    test(x['kind'] in {'folder','published work','our projects'},'Invalid link kind')
    if x['note_ids']:
        test(set(x['note_ids'].split(';'))<=expected,'Link has source note outside owned packets: '+x['note_ids'])
test(not list(P.rglob('*.pdf')),'External PDF remains in part deliverables')
test(not list(P.rglob('*.png')),'External page image remains in part deliverables')
calc=data('outputs/calculations.json')
test(len(calc)==16,'Calculation section count differs')
proof=(P/'outputs/proof_checks.md').read_text()
test(len(re.findall(r'^## P\d+\.',proof,re.M))==32,'Proof-check section count differs')
test(len(re.findall(r'^\| \d+ \|', (P/'directions.md').read_text(),re.M))==12,'Direction count differs')
report=dict(result='PASS' if not errors else 'FAIL',scope='Structural consistency only. Entry verdicts and theorem identifications were authored after reading, not generated by validation.',errors=errors,counts=dict(entries=len(E),items=len(I),claims=len(C),problems=len(M),readings=len(R),links=len(L),quarantined_links=sum(x['kind']=='our projects' for x in L),directions=12,search_rows=len(S),check_events=len(V),reading_records=len(table('read_log.tsv')),references=len(bkeys),proof_checks=32,calculation_sections=len(calc)),verdicts=dict(Counter(x['verdict'] for x in E)),classes=dict(Counter(x['class'] for x in C)),statuses=dict(Counter(x['status_on_pages'] for x in C)),files={str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(P.rglob('*')) if f.is_file() and f.name!='validation.json'})
(P/'outputs/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='files'},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
