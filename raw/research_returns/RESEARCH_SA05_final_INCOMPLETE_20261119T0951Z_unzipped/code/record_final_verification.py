"""Record final verification after the actual fifth review and visual QA."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import time

root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
review=json.loads((root/'progress/review_05.json').read_text())
assert review['stop_rule_triggered'] and not review['movement']
assert review['consecutive_reviews_without_movement']==2
qa=json.loads((root/'code/pdf_qa_output.json').read_text())
index=json.loads((root/'code/consolidate_records_output.json').read_text())
coverage=json.loads((root/'code/audit_check_coverage_output.json').read_text())
table=json.loads((root/'code/update_report_output.json').read_text())
assert qa['visual_inspection_passed'] and not qa['overfull_boxes']
assert not index['index_warnings'] and not index['literature_annotation_gaps']
assert not coverage['unmatched_numbered_labels']
assert not table['missing_compiled_labels'] and table['items']==44
log=(root/'build/RESEARCH_SA05_paper.log').read_text(errors='replace')
assert not re.search(r'(?:Citation|Reference).*undefined|There were undefined|multiply defined|Overfull',log)
assert not re.search(r'(?:LaTeX|Package [^\n]+) Warning',log)
blg=(root/'build/RESEARCH_SA05_paper.blg').read_text(errors='replace')
assert 'Warning--' not in blg
paper=(root/'RESEARCH_SA05_paper.tex').read_text()
assert '\\textbf{INCOMPLETE.}' in paper
report=root/'RESEARCH_SA05_report.md'
assert report.read_text().startswith('INCOMPLETE')
pdf=root/'RESEARCH_SA05_paper.pdf'
out={
    'verified_utc':datetime.now(timezone.utc).isoformat(),
    'final_status':'INCOMPLETE',
    'review_05_stop_rule_triggered':True,
    'pdf_pages':qa['pages'],
    'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'rendered_and_actually_inspected_pages':qa['rendered_pages'],
    'final_overfull_boxes':0,'final_latex_bibtex_warnings':0,
    'numbered_statements':index['numbered_statements'],
    'check_event_records':index['check_events'],
    'explicit_cross_reference_records':index['explicit_cross_reference_records'],
    'bibliography_entries':index['bibliography_entries'],
    'literature_records':index['literature_records'],
    'all_item_rows':table['items'],
    'open_mathematical_rows':len(review['open_mathematical_rows']),
    'scope':'Final consistency and visual verification; no assertion that the unresolved mathematics is proved.'}
heading='## Final verification of the INCOMPLETE deliverables'
assert heading not in report.read_text()
entry=f'''

{heading}

After the stopping review, the final paper was rebuilt from the retained
LuaLaTeX/BibTeX sources. It has {qa['pages']} pages and
{index['numbered_statements']} numbered statements. The final build has zero
overfull boxes and zero LaTeX/BibTeX warnings. The checkpoint-09 initial
bibliography-path failure and its repair remain recorded above; no failed
build is represented as a successful final build. The final pages
{', '.join(map(str,qa['rendered_pages']))} were rendered and actually viewed.
The first page explicitly states INCOMPLETE. No clipping, overlapping
formulae or margin defects were found in the inspected sample.

The final statement-to-event index resolves every numbered label. It has
{index['check_events']} check-event records, including
{index['explicit_cross_reference_records']} explicit cross-reference records;
cross-references link existing checks and are not additional independent
proof checks. The bibliography has {index['bibliography_entries']} canonical
entries with opening annotations, and the literature ledger has
{index['literature_records']} work records. The outcome table resolves all
44 item rows to compiled statement numbers or the named index files.
The eight mathematical rows identified by the stopping review remain
unresolved in their stated universal scopes.

The last source-reconciliation repair changed the Saito publication-list
annotation from an access statement to the explicit word Opened, preserving
its metadata-only scope. No mathematical assertion changed. An optional
sentence in the elliptic-completion note extending the illustration to every
odd coefficient prime was removed: the retained prime-three case has a fully
explicit torsion point and already proves the required distinction. That
omission is a scope choice, not a claim that the broader standard statement
is false. No other post-checkpoint09 proof passage was discarded.

The final file list records hashes and identifies the successful checkpoint
holding each unchanged supplementary file omitted from this ZIP. Current
deliverables, notes and programs are included. New or changed computation
outputs are included; earlier raw third-party sources, supplied attachments,
ordinary rendered page images and earlier ZIPs are excluded as requested.
All retained results are AI-produced research records; no priority or
completed solution of the unresolved questions is claimed.
'''
report.write_text(report.read_text()+entry)
ledger=root/'PROGRESS_LEDGER.md'
ledger.write_text(ledger.read_text()+f'''\n\n## Final verification after stopping\n\nThe final {qa['pages']}-page PDF and all 44 item rows were verified at {out['verified_utc']}. The mathematical stopping decision remains unchanged: two consecutive no-movement reviews, eight unresolved mathematical rows, status INCOMPLETE. Only verification and packaging followed review05. The final report records the actual rendered-page sample, source/check indices and file-manifest scope.\n''')
out['record_seconds']=round(time.perf_counter()-started,6)
(root/'code/final_verification_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
