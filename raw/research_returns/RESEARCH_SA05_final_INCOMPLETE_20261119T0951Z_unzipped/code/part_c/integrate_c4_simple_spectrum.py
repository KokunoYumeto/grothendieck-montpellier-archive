"""Insert the independently audited conditional C4 proposition exactly once."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

root=Path(__file__).resolve().parents[2]
section=root/'sections/part_c.tex'
fragment=root/'part_c/c4_simple_spectrum_positivity.tex'
text=section.read_text()
payload=fragment.read_text()
label='\\label{c:threefold-simple-spectrum}'
anchor='\\begin{lemma}[A finite exterior-power test for monodromy purity]'
if anchor not in text:
    positions=[line for line in text.splitlines() if 'exterior' in line and '\\begin' in line]
    raise RuntimeError('Expected exact exterior criterion anchor absent: '+repr(positions))
assert label not in text, 'Refuse a repeated integration and repeated audit events.'
section.write_text(text.replace(anchor,payload+'\n\n'+anchor,1))
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
rows=[
 ['c:threefold-simple-spectrum','A globally squarefree primitive target Frobenius spectrum plus mixed numerical-equals-homological equivalence implies the threefold primitive restriction-image pairing is nondegenerate','Proved sufficient condition; universal C4 remains open','sections/part_c.tex, label c:threefold-simple-spectrum','Algebraic cohomological kernel projector; two target right ideals; rational Frobenius trace Gram matrix; adjoint-fixed field-factor idempotents','12:118-120; C.4','All components and ample classes are defined over the fixed finite residue field before imposing squarefreeness. No D(SxS), source semisimplicity, or Chow-idempotent lift used. Actual im(f) intersection P obtained, not im(pf).'],
 ['c:threefold-simple-spectrum-scope','The simple-spectrum sufficient condition retains mixed D and cannot be made universal by an unproved field-extension or alteration step','Proved scope clarification; no universal movement','sections/part_c.tex, label c:threefold-simple-spectrum-scope','c:threefold-simple-spectrum','12:118-120; C.4','Squarefreeness is global across the disjoint union and can fail after taking Frobenius powers. No transfer removes either retained hypothesis.']
]
with (root/'part_c/results.csv').open('a',newline='') as out:
    csv.writer(out).writerows(rows)
events=[]
for statement in ['c:threefold-simple-spectrum','c:threefold-simple-spectrum-scope']:
    events += [
      [statement,now,'GPT-6 Astra (OpenAI), /root/part_c','targeted proof check','Full written proof checked: explicit Tate target, mixed trace-test projection, first ideal/kernel projector, actual primitive intersection, rational trace Gram inversion, adjoint-fixed idempotents, second ideal, and finite averaging. Sufficient subcase only.'],
      [statement,now,'GPT-6 Astra (OpenAI), /root','independent re-proof','Recorded after root read the complete actual fragment at09:16UTC and passed every step. Scope retains mixed D and squarefreeness of the full primitive disjoint-union spectrum. No qualifying universal movement.'],
      [statement,now,'GPT-6 Astra (OpenAI), /root/part_d','independent re-proof','Recorded after D read the complete actual fragment and passed both statements. Fixed-field split-component condition and no unsafe Frobenius-power passage checked. Written mathematical audit; no new independent Katz-Messing opening claimed.']
    ]
with (root/'part_c/CHECK_EVENTS.tsv').open('a',newline='') as out:
    csv.writer(out,delimiter='\t').writerows(events)
result={'recorded_utc':datetime.now(timezone.utc).isoformat(),'section':str(section.relative_to(root)),'fragment':str(fragment.relative_to(root)),'labels':[r[0] for r in rows],'new_check_events':len(events),'scope':'Conditional sufficient subcase; no universal gate movement.','run_history':'The first invocation stopped at the guarded anchor check before making any changes: the existing title uses test rather than criterion. The anchor was corrected and the subsequent invocation succeeded.'}
Path(__file__).with_name('integrate_c4_simple_spectrum_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
