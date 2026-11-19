"""Validate authored record structure and evidence links; never infer verdicts."""
import csv, json
from pathlib import Path

B = Path('SA05/work/cote12c')
def table(name):
    return list(csv.DictReader((B / name).open(), delimiter='\t'))
items = json.loads((B / 'items.json').read_text())
claims = json.loads((B / 'claims.json').read_text())
problems = json.loads((B / 'problems.json').read_text())
entries, searches, refs, events = map(table, ['entries.tsv','search_log.tsv','reference_ledger.tsv','CHECK_EVENTS.tsv'])
required = {
    'items': 'id sources kind cote scans lines his_words statement reconstruction check check_reason'.split(),
    'claims': 'id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split(),
    'problems': 'id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split(),
}
for name, rows in [('items',items),('claims',claims),('problems',problems)]:
    assert len({r['id'] for r in rows}) == len(rows), (name,'duplicate id')
    for r in rows:
        assert set(required[name]) <= r.keys(), (name,r['id'],'missing field')
        assert all(r[k] is not None for k in required[name]), (name,r['id'],'null field')
expected = {f'MPL_12_099-149#{n}' for n in range(1,104)}
assert {r['entry_id'] for r in entries} == expected
assert len(entries) == 103
item_ids = {r['id'] for r in items}
ref_ids = {r['key'] for r in refs}
search_by_id = {r['search_id']:r for r in searches}
event_ids = {r['statement_id'] for r in events}
for r in entries:
    assert r['item_id'] in item_ids and r['reason'].strip()
for r in claims:
    assert set(r['items']) <= item_ids
    assert set(r['refs']) <= ref_ids
    assert r['id'] in event_ids
    linked = [search_by_id[s] for s in r['search_ids']]
    assert any(any(k in json.loads(s['query']) for k in ['system1_search_query','system2_search_query']) for s in linked), (r['id'],'no actual query')
    assert any(s['opened_urls'] for s in linked), (r['id'],'no retrieval links')
for r in problems:
    assert r['refs'] and set(r['refs']) <= ref_ids
assert item_ids <= event_ids and ref_ids <= event_ids
assert len(refs) == len(ref_ids)
assert {r['key'] for r in json.loads((B/'reference_records.json').read_text())} == ref_ids
report = {'result':'passed','scope_entries':103,'items':len(items),'claims':len(claims),'problems':len(problems),'references':len(refs),'search_batches':len(searches),'check_events':len(events),'checks':['all requested JSON fields','unique scope entry IDs','all ID/ref joins','every claim linked to a real search-query batch','every claim has retrieved evidence links','item/claim/reference check-event coverage','consistent bibliography ledger'],'boundary':'This program validates bookkeeping only. It does not assign verdicts or prove source fidelity.'}
(B/'outputs'/'scope_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
