"""Structural audit of manually prepared SA21 VI–VII files, not proof checking."""
from pathlib import Path
import json,csv,re
from collections import Counter
P=Path(__file__).parent
claims=json.loads((P/'claims.json').read_text())
problems=json.loads((P/'problems.json').read_text())
cf={'id','items','cote','scans','lines','his_statement','statement','status_on_pages','status_category','computation','class','fate','fate_date','present_status','refs','confidence'}
pf={'id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs'}
assert all(set(c)==cf for c in claims)
assert all(set(x)==pf for x in problems)
assert len({c['id'] for c in claims})==len(claims)==96
assert len({p['id'] for p in problems})==len(problems)==25
bib=(P/'references.bib').read_text()
keys=set(re.findall(r'@\w+\{([^,]+),',bib))
assert all(set(x['refs'])<=keys for x in claims+problems)
def read_tsv(n):
    with (P/n).open() as f:return list(csv.DictReader(f,delimiter='\t'))
coverage=read_tsv('coverage.tsv'); readings=read_tsv('readings.tsv'); links=read_tsv('links.tsv'); events=read_tsv('check_events.tsv')
assert len(coverage)==26 and all(c['claims'] for c in coverage)
assert all(c['lines'] and c['scans'] and c['fate'] for c in claims)
assert all(c['id'] in {e['statement_id'] for e in events} for c in claims)
assert all('No scan inspected' in r['evidence'] for r in readings)
cert=json.loads((P/'finite_checks_output.json').read_text())
assert all(cert['path_graph_local_support_counterexample']['all_axioms_exhaustively_checked'].values())
assert cert['path_graph_local_support_counterexample']['left_S_A_minus_B']!=cert['path_graph_local_support_counterexample']['right_S_A_intersection_cosupp_S_B']
unresolved=[l for l in links if 'unresolved' in l['evidence'] or 'absent' in l['evidence']]
result={'structural_audit':'passed','claims':len(claims),'problems':len(problems),'folders':len(coverage),
        'readings':len(readings),'links':len(links),'explicit_unresolved_link_rows':len(unresolved),
        'check_events':len(events),'reference_keys':len(keys),
        'P4_axiom_checks':len(cert['path_graph_local_support_counterexample']['all_axioms_exhaustively_checked']),
        'class_counts':dict(Counter(c['class'] for c in claims)),
        'status_category_counts':dict(Counter(c['status_category'] for c in claims)),
        'limits':'This validates schema, IDs, bibliography keys and saved finite results; it does not independently prove manuscript statements.'}
(P/'validation_output.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
