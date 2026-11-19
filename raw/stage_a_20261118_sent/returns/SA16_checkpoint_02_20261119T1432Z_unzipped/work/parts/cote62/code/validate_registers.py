"""Structural validation only: this script never infers a mathematical verdict."""
from pathlib import Path
import csv,json,re,collections
P=Path(__file__).resolve().parents[1];root=P.parents[2]
def j(n):return json.loads((P/n).read_text())
def t(n):return list(csv.DictReader((P/n).open(),delimiter='\t'))
items=j('items.json');claims=j('claims.json');problems=j('problems.json');entries=t('entries.tsv');readings=t('readings.tsv');links=t('links.tsv');refs=j('reference_registry.json');search=t('search_log.tsv')
itemids={i['id'] for i in items};claimids={c['id'] for c in claims};refkeys={r['key'] for r in refs};searchids={s['search_id'] for s in search}
expected={r['entry_id'] for r in csv.DictReader((root/'sources/SA16_notes/NOTES_INDEX.tsv').open(),delimiter='\t') if r['package']=='MPL_62_002-050'}
assert len(entries)==len(expected)==103
assert {r['entry_id'] for r in entries}==expected
assert len({r['entry_id'] for r in entries})==len(entries)
assert {s for i in items for s in i['sources']}==expected
for r in entries:assert r['item_id'] in itemids
for r in claims+problems:
    for key in r['refs']:assert key in refkeys,(r['id'],key)
    for sid in r['search_ids']:assert sid in searchids,(r['id'],sid)
    for iid in r['items']:assert iid in itemids,(r['id'],iid)
for r in problems:
    for cid in r['claims']:assert cid in claimids,(r['id'],cid)
assert len(itemids)==len(items) and len(claimids)==len(claims)
for c in claims:
    assert c['search_ids'] and c['refs']
    if c['status_on_pages']=='false as stated':assert c['refined_statement']['id']==c['id']+'.R'
texts={p.name:p for p in (root/'sources/SA16_texts').rglob('*transcription.tex')}
warnings=[]
for r in readings:
    name,loc=r['line'].split(':',1);ls=texts[name].read_text().splitlines();n=int(re.match(r'\d+',loc)[0]);assert 1<=n<=len(ls)
    scan=None
    for line in ls[:n]:
        m=re.search(r'\\scanpage\{(\d+)\}',line)
        if m:scan=int(m[1])
    if scan!=int(r['scan']):warnings.append(dict(id=r['id'],declared=r['scan'],scan_at_start=scan,line=r['line'],text=ls[n-1]))
report=dict(items=len(items),entries=len(entries),claims=len(claims),problems=len(problems),readings=len(readings),links=len(links),references=len(refs),search_batches=len(search),entry_verdict_counts=dict(collections.Counter(r['verdict'] for r in entries)),claim_status_counts=dict(collections.Counter(c['status_on_pages'] for c in claims)),claim_class_counts=dict(collections.Counter(c['class'] for c in claims)),link_endpoint_counts=dict(collections.Counter(r['endpoint_status'] for r in links)),reading_scan_warnings=warnings)
(P/'outputs/structural_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
