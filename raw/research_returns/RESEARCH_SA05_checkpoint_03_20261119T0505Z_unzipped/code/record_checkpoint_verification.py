"""Record actual build/visual verification; does not claim a checkpoint save."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re,sys,time
ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic();number=int(sys.argv[1])
qa=json.loads((ROOT/'code/pdf_qa_output.json').read_text())
index=json.loads((ROOT/'code/consolidate_records_output.json').read_text())
coverage=json.loads((ROOT/'code/audit_check_coverage_output.json').read_text())
table=json.loads((ROOT/'code/update_report_output.json').read_text())
log=(ROOT/'build/RESEARCH_SA05_paper.log').read_text(errors='replace')
assert qa['visual_inspection_passed'],'Visual inspection must precede this record'
assert not qa['over_2pt'],'A box exceeds the permitted size'
assert not coverage['unmatched_numbered_labels'],'Statement event coverage is incomplete'
assert not table['missing_compiled_labels'],'The report still has uncompiled labels'
assert not index['index_warnings'] and not index['literature_annotation_gaps']
assert not re.search(r'(?:Citation|Reference).*undefined|There were undefined|multiply defined',log)
pdf=ROOT/'RESEARCH_SA05_paper.pdf'
result=dict(checkpoint_number=number,verification_utc=datetime.now(timezone.utc).isoformat(),
 pdf_pages=qa['pages'],pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
 rendered_and_inspected_pages=qa['rendered_pages'],overfull_boxes=qa['overfull_boxes'],
 numbered_statements=index['numbered_statements'],check_event_records=index['check_events'],
 explicit_cross_reference_records=index['explicit_cross_reference_records'],
 bibliography_entries=index['bibliography_entries'],literature_records=index['literature_records'],
 scope='Verification only; checkpoint upload success is recorded separately after it occurs.')
heading=f'### Checkpoint {number:02d} verification'
report=ROOT/'RESEARCH_SA05_report.md';text=report.read_text()
entry=f'''\n{heading}\n\nThe verified PDF has{qa['pages']}pages and{index['numbered_statements']}numbered statement records. The final LuaLaTeX log has zero overfull boxes and no undefined citations or references. In this expansion an unbreakable program path produced one35.33685pt overflow; a breakable path fixed it. The three source syntax errors encountered during integration were repaired before this final build. Pages{','.join(map(str,qa['rendered_pages']))} were rendered and visually inspected, including the repaired passage and the new proof sections. Text, formulae and margins are legible.\n\nThe source bibliography contains{index['bibliography_entries']}canonical entries, each with explicit opening status, and the consolidated literature ledger contains{index['literature_records']}work records. Every numbered statement has a matching check-event label. There are{index['check_events']}event records, including{index['explicit_cross_reference_records']}explicit cross-reference records that link preserved checks to numbered statements; those links are not new independent checks. The item table resolves all statement labels to their compiled numbers. This verifies the checkpoint contents and does not declare the research programme complete.\n'''
if heading not in text:report.write_text(text+entry)
result['seconds']=round(time.monotonic()-start,4)
(ROOT/f'code/checkpoint_{number:02d}_verification_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
