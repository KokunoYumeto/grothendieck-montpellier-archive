"""Verify the final research package's cross-file consistency before archiving.

This is a release-record audit, not a mathematical proof or PDF visual review.
The explicit visual inspection is recorded separately in PDF_QA_APPROVED.json.
"""
from pathlib import Path
from datetime import datetime, timezone
import collections, csv, hashlib, json, re, time

start = time.perf_counter()
root = Path(__file__).resolve().parents[1]
canonical = lambda s: re.sub(r'[^A-Za-z0-9]', '', s).upper()
report = (root/'RESEARCH_SA08_report.md').read_text()
rows = list(csv.DictReader((root/'RESEARCH_SA08_results.csv').open()))
events = list(csv.DictReader((root/'CHECK_EVENTS.tsv').open(), delimiter='\t'))
qa = json.loads((root/'logs/PDF_QA_APPROVED.json').read_text())
review = json.loads((root/'logs/PROGRESS_REVIEW_03.json').read_text())
register = json.loads((root/'logs/register_audit.json').read_text())
checks = {}
checks['incomplete_first_line'] = report.startswith('INCOMPLETE\n')
checks['final_report_heading'] = '# RESEARCH_SA08 final report — incomplete' in report
checks['binding_stop_recorded'] = review['stop_required'] and review['consecutive_no_movement'] == 2
expected = {f'A.{i}' for i in range(1,6)} | {f'B.{i}' for i in range(1,9)} | {f'C.{i}' for i in range(1,4)} | {f'L{i}' for i in range(1,9)}
table = [line.split('|')[1].strip() for line in report.splitlines() if line.startswith('| ') and line.split('|')[1].strip() in expected]
checks['all_24_requested_outcomes_once'] = set(table) == expected and len(table) == len(expected)
checks['numbered_statement_register'] = register['result_rows'] == register['numbered_statement_labels'] == len(rows) and not any(register[k] for k in ('duplicate_result_ids','duplicate_labels','paper_labels_without_rows','result_rows_without_paper_labels'))
checked = {canonical(e['statement_id']) for e in events}
uncovered = [r['id'] for r in rows if canonical(r['id']) not in checked]
checks['every_statement_has_check_event'] = not uncovered
allowed_types={'targeted proof check','independent re-proof',
 'computation or formal certificate','used and rechecked in this run',
 'carried as background without fault found',"refuted, with the refined statement's id"}
checks['check_event_types_use_requested_vocabulary'] = all(e['type'] in allowed_types for e in events)
checks['pdf_matches_visual_approval'] = hashlib.sha256((root/'RESEARCH_SA08_paper.pdf').read_bytes()).hexdigest() == qa['pdf_sha256']
changed_sources = [rel for rel,sha in qa['source_sha256'].items() if hashlib.sha256((root/rel).read_bytes()).hexdigest() != sha]
checks['all_approved_sources_unchanged'] = not changed_sources
checks['all_rendered_pages_explicitly_reviewed'] = qa['rendered_pages'] == qa['visually_inspected_pages'] and qa['visual_review'].startswith('Passed explicit image inspection:')
build = (root/qa['build_log']).read_text()
checks['clean_final_build'] = qa['overfull_after'] == 0 and not re.search(r'Overfull|undefined|Fatal error|duplicate destination|Package hyperref Warning', build)
entries = re.split(r'(?m)^@', (root/'RESEARCH_SA08_references.bib').read_text())[1:]
unmarked_bib = [e.split('{',1)[1].split(',',1)[0] for e in entries if not re.search(r'(?i)(opened|not opened)',e)]
checks['all_bibliography_access_states_marked'] = not unmarked_bib
programs = sorted(p.name for p in (root/'code').iterdir() if p.is_file())
unlisted_programs = [p for p in programs if p not in report]
checks['every_saved_program_named_in_report'] = not unlisted_programs
result = {
 'utc': datetime.now(timezone.utc).isoformat(),
 'scope': 'Final cross-file delivery audit; does not replace mathematical or visual checks.',
 'all_checks_passed': all(checks.values()), 'checks': checks,
 'statement_rows': len(rows), 'check_events': len(events),
 'event_types': dict(collections.Counter(e['type'] for e in events)),
 'requested_outcome_rows': len(table), 'bibliography_entries': len(entries),
 'code_files': len(programs), 'pdf_pages': qa['pages'],
 'visually_inspected_pages': qa['rendered_page_count'],
 'approved_source_files': len(qa['source_sha256']),
 'uncovered_statements': uncovered, 'changed_sources': changed_sources,
 'unmarked_bibliography_entries': unmarked_bib,
 'unlisted_programs': unlisted_programs,
 'seconds': time.perf_counter()-start,
}
(root/'logs/FINAL_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
if not result['all_checks_passed']:
    raise SystemExit('Final consistency audit failed; inspect FINAL_AUDIT.json.')
