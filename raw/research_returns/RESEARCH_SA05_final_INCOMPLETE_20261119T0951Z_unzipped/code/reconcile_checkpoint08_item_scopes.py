"""Reconcile proved additions without promoting any universal open item."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

root=Path(__file__).resolve().parents[1]
path=root/'ITEM_STATUS.tsv'
with path.open(newline='') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
by={r['item']:r for r in rows}
def labels(item, additions):
    by[item]['statement_ids']=';'.join(dict.fromkeys(by[item]['statement_ids'].split(';')+additions))
labels('B.1',['prop:B-limit-diagnostics'])
labels('B.5',['prop:B-finite-field-coefficient-gate'])
labels('C.4',['c:threefold-target-positivity'])
labels('C.6',['c:local-global-motive-approximation','c:bgv-pure-local-boundary'])
extra={
 'B.1':' The new limit diagnostics refute two shortcuts involving continuous-cohomology colimits and completed Frobenius modules; they do not prove the required uniform ramification control.',
 'B.5':' For the specified rational Weil extension of all Chow-heart coefficients, perfect duality is equivalent to Beilinson plus Parshin and is already detected on P1 with constant coefficients. This stronger coefficient scope is distinguished from homogeneous pure summands; it does not resolve arithmetic f-admissibility.',
 'C.4':' Positivity on the surface-square target together with homological=numerical equivalence on the mixed threefold-surface product is a proved sufficient package. Its unresolved product hypotheses do not prove the residual pairing.',
 'C.6':' Finite-prime local/global approximation proves equivalence of the universal number-field and p-adic pure-motive formulations. A finite-field cycle still lacks the pure local realization needed for the attempted converse; occurrence among semistable strata is insufficient.'
}
for item,text in extra.items():
    if text.strip() not in by[item]['scope_or_gate']:
        by[item]['scope_or_gate']+=text
additions={
 'B.1':['prop:B-limit-diagnostics'],
 'B.5':['prop:B-finite-field-coefficient-gate'],
 'C.4':['c:threefold-target-positivity'],
 'C.6':['c:local-global-motive-approximation','c:bgv-pure-local-boundary']
}
(root/'ITEM_SCOPE_ADDITIONS.json').write_text(json.dumps(
    {item:dict(statement_ids=additions[item],scope_append=text) for item,text in extra.items()},
    indent=2,ensure_ascii=False)+'\n')
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['item','status','statement_ids','scope_or_gate'],delimiter='\t')
    writer.writeheader();writer.writerows(rows)
out=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),all_items=len(rows),
         updated_items=list(extra),scope='All eight universal mathematical rows remain open; no status promotion.')
(root/'code/reconcile_checkpoint08_item_scopes_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
