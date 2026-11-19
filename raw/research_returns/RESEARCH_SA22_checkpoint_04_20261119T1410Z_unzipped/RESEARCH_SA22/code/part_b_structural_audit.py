#!/usr/bin/env python3
"""Check owned Part B citations, labels and result-ledger coverage."""
from pathlib import Path
import re, csv, json
root=Path(__file__).resolve().parents[1]
tex=(root/'sections/part_b.tex').read_text()
bib=(root/'sources/part_b.bib').read_text()
keys=set(re.findall(r'@\w+\{([^,]+),',bib));used=set()
for block in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',tex):
    used.update(block.split(','))
labels=re.findall(r'\\label\{([^}]+)\}',tex)
rows=list(csv.DictReader((root/'checks/part_b_results.csv').open()))
mapped={i.strip() for r in rows for i in r['where_proved'].split(';')}
result={
 'missing_bib_keys':sorted(used-keys),
 'duplicate_labels':[x for x in set(labels) if labels.count(x)>1],
 'unmapped_statement_labels':[x for x in labels if x.startswith(('thm:','lem:','prop:')) and x not in mapped],
 'referenced_missing_local_labels':sorted(set(re.findall(r'\\ref\{([^}]+)\}',tex))-set(labels)),
 'bib_entries':len(keys),
 'statements':len([x for x in labels if x.startswith(('thm:','lem:','prop:'))]),
 'ledger_rows':len(rows),
}
for key in ['missing_bib_keys','duplicate_labels','unmapped_statement_labels','referenced_missing_local_labels']:
    assert not result[key],(key,result[key])
(root/'code/part_b_structural_audit_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
