"""Preserve the late audited proof before the scheduled first review."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, time

root=Path(__file__).resolve().parents[1]
start=time.monotonic()
now=datetime.now(timezone.utc).replace(microsecond=0).isoformat()
path=root/'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as stream:
    reader=csv.DictReader(stream,delimiter='\t')
    fields=reader.fieldnames
    rows=list(reader)
identifier='draft:B3-all-bases-surface-gate'
outcome=('Root read the complete late proof in part_b/b3_all_bases_surface_gate_audited_draft.md. '
         'Independently opened and read Kelly Lemma18 and Corollaries19–20; Stacks29.47.9, '
         '29.42.10,37.44.1 and85.36.3–6. Checked the schematic graph, relative Frobenius '
         'twist and Verschiebung; rational equalizer then flat Q-to-Qell extension; '
         'eigenvalue-m divisor/Kummer identification on the total dual abelian scheme; '
         'weight−1 Cech kernel; nilpotent and finite-open descent. The equivalence with '
         'surface Tate passes for every finite-type base. The arbitrary relative-curve '
         'Brauer quotient remains a separate unresolved scope.')
if not any(row['statement_id']==identifier for row in rows):
    rows.append(dict(statement_id=identifier,date=now,who='GPT-6 Astra / root / current run',
                     type='targeted proof check',outcome=outcome))
    with path.open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t')
        writer.writeheader();writer.writerows(rows)
note=root/'part_b/b3_all_bases_surface_gate_audited_draft.md'
text=note.read_text().replace(
    'The full note still awaits their final audit.',
    'The complete note subsequently passed the independent D and root audits before the first formal review.')
marker='## Late proof after the checkpoint typesetting freeze'
text+='\n\n## Final root audit\n\n'+outcome+'\n\nAudited at '+now+'.\n'
note.write_text(text)
report=root/'RESEARCH_SA05_report.md'
if marker not in report.read_text():
    report.write_text(report.read_text()+'\n\n'+marker+'\n\n'
      'After the PDF was frozen, the complete proof in '
      'part_b/b3_all_bases_surface_gate_audited_draft.md passed B, D and root audits. '
      'It extends the surface-Tate equivalence to abelian schemes over every finite-type '
      'base. The numbered PDF and outcome-table scope for this extension await integration '
      'in the next checkpoint; the full proof and root check event are already preserved here. '
      'The formal review counts this movement now. It does not settle the arbitrary-base '
      'relative-curve Brauer quotient or prove surface Tate.\n')
result={'checked_at':now,'event':identifier,'root_events':len(rows),
        'seconds':round(time.monotonic()-start,6)}
(root/'code/record_late_cp04_audit_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
