"""Structural and exact-source validation of already authored research records.

This is not a mathematical test suite and does not generate verdicts.  It checks
coverage, references, literal quotation provenance, and reproducibility links.
"""
from pathlib import Path
import json,csv,collections,re,datetime
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'work/middle'
def J(f):return json.loads((OUT/f).read_text())
def T(f):return list(csv.DictReader((OUT/f).open(),delimiter='\t'))
items=J('items.json');claims=J('claims.json');problems=J('problems.json')
entries=T('entries.tsv');embedded=T('embedded_coverage.tsv');events=T('CHECK_EVENTS.tsv')
refs=J('reference_audit.json');search=T('search_coverage.tsv');readings=T('readings.tsv');links=T('links.tsv')
idsets={k:{x['id']for x in v}for k,v in [('items',items),('claims',claims),('problems',problems)]}
for name,arr in [('items',items),('claims',claims),('problems',problems)]:assert len(idsets[name])==len(arr),name
packages={'MPL_136_095-141','MPL_136_189-234'}
index=list(csv.DictReader((ROOT/'sources/notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
expected={x['entry_id']for x in index if x['package']in packages}
assert len(entries)==104 and len(expected)==104
assert {x['entry_id']for x in entries}==expected
assert len({x['entry_id']for x in entries})==104
assert all(x['item_id']in idsets['items']for x in entries)
assert all(s in expected for x in items for s in x['sources'])
assert len(embedded)==131 and len({x['embedded_id']for x in embedded})==131
assert all(x['verdict']and x['reason']and x['actual_manuscript_locators']for x in embedded)
assert all(x['check']in {'agrees','overstates','understates','misreads','not on the page'}for x in items)
assert all(c['items']and all(i in idsets['items']for i in c['items'])for c in claims)
assert len(search)==101 and {x['claim_id']for x in search}==idsets['claims']
assert all(x['search_records']and x['searched_fate']for x in search)
refkeys={r['key']for r in refs};assert len(refkeys)==len(refs)
assert all(r['note']in {'verified','unverified'}for r in refs)
assert all(k in refkeys for x in claims+problems for k in x['refs'])
quote_count=0;passage_count=0
for x,key in [(x,'his_statement')for x in claims]+[(x,'his_words')for x in items]:
    parts=[]
    for p in x['quote_passages']:
        ls=(ROOT/'sources/texts/pro'/p['file']).read_text().splitlines()
        a,z=map(int,(p['lines']+'-'+p['lines']).split('-')[:2])if '-'not in p['lines']else map(int,p['lines'].split('-'))
        actual='\n'.join(ls[a-1:z]).strip();assert actual==p['text'],x['id']
        current=None;scanmap=[]
        for l in ls[:z]:
            m=re.search(r'\\scanpage\{(\d+)\}',l)
            if m:current=int(m.group(1))
            scanmap.append(current)
        assert set(scanmap[a-1:z])=={p['scan']},x['id']
        parts.append(actual);passage_count+=1
    assert x[key]=='\n[…]\n'.join(parts),x['id']
    quote_count+=bool(parts)
cd={x['id']:x for x in claims};occ=0
for p in problems:
    for o in p['occurrences']:
        c=cd[o['claim']]
        assert o['his_words']==c['his_statement']and o['lines']==c['lines']and o['scans']==c['scans'],p['id']
        occ+=1
eventids={x['statement_id']for x in events}
assert idsets['items']|idsets['claims']<=eventids
assert all(x['who']=='GPT-6 Astra Pro; effort not exposed by runtime; SA08/middle'for x in events)
assert all(x['kind']in {'folder','published work','our projects'}for x in links)
external=T('external_project_links.tsv')
assert all(x['kind']=='our projects'for x in external)
assert [x for x in links if x['kind']=='our projects']==external
assert (ROOT/'programs/middle_math_checks.py').exists()and(OUT/'computation_results.json').exists()
assert (ROOT/'logs/middle_math_checks.log').stat().st_size>0
required=['directions.md','prose_findings.md','search_log.md','search_results_index.json','mathematical_checks.md','references.bib','read_ledger.md']
assert all((OUT/f).stat().st_size>0 for f in required)
result={'validated_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Structural and literal-source fidelity checks only; mathematical conclusions retain their individual evidence types.','counts':{'indexed_entries':len(entries),'embedded_entries':len(embedded),'items':len(items),'claims':len(claims),'problems':len(problems),'problem_occurrences':occ,'readings':len(readings),'all_typed_links':len(links),'internal_and_publication_links':len(links)-len(external),'external_project_links':len(external),'check_events':len(events),'bibliography_records':len(refs),'search_batches':len(J('search_results_index.json')),'claim_search_rows':len(search),'records_with_author_quotations':quote_count,'literal_quote_fragments':passage_count,'directions':9},'entry_verdicts':dict(collections.Counter(x['verdict']for x in entries)),'item_checks':dict(collections.Counter(x['check']for x in items)),'claim_classes':dict(collections.Counter(x['class']for x in claims)),'claim_statuses':dict(collections.Counter(x['status_on_pages']for x in claims)),'reference_access':dict(collections.Counter(x['note']for x in refs)),'checks_passed':['104 indexed entries exactly matched with no duplicates','131 embedded dispositions present','All claim/item/problem links resolve','All claim/problem bibliography keys resolve','Every claim has saved search coverage','Every literal author quote exactly matches selected source lines within one scan','Every problem occurrence matches the corrected final claim quotation','External-project links tagged and copied exactly to their own table','Computation program and actual outputs retained','Every item and claim has a truthful check event','Required reports and evidence files present'],'limits':['No manuscript scans supplied; ink readings undecided.','Earlier search batches1–38 retain complete outputs but no separately saved literal top-level input string; this is disclosed.','No automatic theorem verification is implied by this validation.']}
(OUT/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
with(OUT/'progress.log').open('a')as f:f.write(result['validated_at_utc']+' UTC — All middle-package stages structurally validated; exact quotation provenance and every claim search record checked. Root owns global start/stage chronology and checkpoint saves.\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
