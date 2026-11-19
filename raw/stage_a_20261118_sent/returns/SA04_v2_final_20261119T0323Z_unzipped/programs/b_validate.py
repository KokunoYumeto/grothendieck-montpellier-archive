"""Structural validation only. This program does not make mathematical verdicts."""
from pathlib import Path
import csv,json,re,collections
R=Path(__file__).resolve().parents[1];O=R/'parts/b'
def tsv(n):return list(csv.DictReader((O/n).open(),delimiter='\t'))
E=tsv('entries.tsv');I=json.loads((O/'items.json').read_text());C=json.loads((O/'claims.json').read_text());P=json.loads((O/'problems.json').read_text())
assert {e['entry_id'] for e in E}=={f'MPL_93_047-091#{i}' for i in range(161,326)}
assert len(E)==165
ii={x['id'] for x in I};cc={x['id'] for x in C}
assert len(ii)==len(I) and len(cc)==len(C)
assert all(e['item_id'] in ii for e in E)
assert sorted(s for x in I for s in x['sources'])==sorted(e['entry_id'] for e in E)
assert all(set(x['items'])<=ii for x in C)
assert all(x['class'] in 'ABCDEF' for x in C)
assert all(x['confidence'] in ['high','medium','low'] for x in C)
assert all(x['fate'] and x['present_status'] and x['computation'] for x in C)
bib=(O/'references.bib').read_text();keys=set(re.findall(r'@\w+\{([^,]+),',bib))
assert {r for x in C for r in x['refs']}<=keys
assert {r for x in P for r in x['refs']}<=keys
search=tsv('search_log.tsv');covered={x['claims'] for x in search if x['query_id'].startswith('FATE-')}
assert cc<=covered
events=tsv('CHECK_EVENTS.tsv');ee={x['statement_id'] for x in events}
assert ii|cc|keys<=ee
links=tsv('links.tsv')
with (O/'project_leads.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['kind','from','to','what','evidence','note_ids'],delimiter='\t');w.writeheader();w.writerows(x for x in links if x['kind']=='our projects')
stats={'entries':len(E),'items':len(I),'claims':len(C),'problems':len(P),'readings':len(tsv('readings.tsv')),'links':len(links),'project_leads':len(tsv('project_leads.tsv')),'references':len(keys),'check_events':len(events),'verdicts':dict(collections.Counter(e['verdict'].split(' into')[0] for e in E)),'claims_by_class':dict(collections.Counter(x['class'] for x in C)),'schema_and_coverage_checks':'passed; this is not a mathematical certification'}
(R/'outputs/b_validation.json').write_text(json.dumps(stats,indent=2)+'\n')
print(json.dumps(stats,indent=2))
