"""Record completed visual, log and hash checks; never create an archive."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import fitz

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / 'output' / 'RESEARCH_SA07'
log = (OUT / 'RESEARCH_SA07_paper.log').read_text()
bad = {label: len(re.findall(pattern, log)) for label, pattern in {
    'overfull_boxes': r'Overfull \\[hv]box',
    'undefined_controls': r'Undefined control sequence',
    'undefined_references_or_citations': r'undefined',
    'latex_warnings': r'LaTeX Warning',
    'missing_characters': r'Missing character',
    'fatal_errors': r'Fatal error',
}.items()}
assert not any(bad.values()), bad
records = list(csv.DictReader((OUT / 'COMPUTATION_RECORD.tsv').open(), delimiter='\t'))
failures = []
for row in records:
    for path, key in [(OUT/'code'/row['script'], 'script_sha256'),
                      (OUT/row['output'], 'output_sha256')]:
        if hashlib.sha256(path.read_bytes()).hexdigest() != row[key]:
            failures.append(str(path))
    if row['exit_code'] != '0':
        failures.append(row['script'] + ': exit=' + row['exit_code'])
assert not failures, failures
sources = list(csv.DictReader((OUT / 'LITERATURE_RECORD.tsv').open(), delimiter='\t'))
assert not any('STILL REQUIRES' in row['access_status'] for row in sources)
claims = list(csv.DictReader((OUT / 'audit_claims.csv').open()))
results = list(csv.DictReader((OUT / 'RESEARCH_SA07_results.csv').open()))
events = list(csv.DictReader((OUT / 'CHECK_EVENTS.tsv').open(), delimiter='\t'))
pdf = OUT / 'RESEARCH_SA07_paper.pdf'
page_count = len(fitz.open(pdf))
data = {
    'actual_utc': datetime.now(timezone.utc).isoformat(),
    'pdf_pages': page_count,
    'pdf_bytes': pdf.stat().st_size,
    'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'numbered_statements': len(results),
    'canonical_assertions': len(claims),
    'check_events': len(events),
    'source_access_records': len(sources),
    'registered_programs_with_verified_source_and_output': len(records),
    'log_counts': bad,
    'interrupted_build_overfull_pt': [39.89973, 198.23315],
    'first_complete_build_overfull_pt': [39.89973, 19.16591],
    'transient_integration_errors_repaired': ['unescaped underscores in a bibliography source filename'],
    'visually_inspected_pages': [1,48,49,50,51,52,53,54,55,56,57,58,74,130,168,169,170,171,172,173,174,175,240,253,254,255,281],
    'additional_full_size_inspection': [51,55,174,175,255],
    'visual_outcome': 'All inspected content fits. The repaired program names and split hash, elliptic coefficient formulas, proper-completion proof and numerical-equivalence category maps are legible and within margins.',
    'checkpoint_created_by_this_script': False,
}
(OUT / 'code' / 'checkpoint12_qa.json').write_text(json.dumps(data, indent=2) + '\n')
report = OUT / 'RESEARCH_SA07_report.md'
text = report.read_text()
heading = '## Verification before checkpoint 12'
if heading not in text:
    text += '\n\n' + heading + '\n\n'
    text += (f'The paper has {page_count} pages and {len(results)} numbered statements, '
             f'with {len(events)} integrated check events, {len(sources)} source-access '
             f'records and {len(records)} registered mathematical programs. Root verified '
             'all retained source/output hashes and zero exit codes. The 307 canonical '
             'assertion statuses are unchanged. Additional work-note checks arriving after '
             'the production merge remain in their dated work ledgers.\n\n')
    text += ('The first integration failed on unescaped underscores in a bibliography '
             'filename; those are escaped. The interrupted build exposed overflows of '
             '39.89973pt and 198.23315pt. The first complete build retained two overflows, '
             '39.89973pt and 19.16591pt. Breakable program paths in A.4.37 and an explicit '
             'two-line SHA-256 in E.2.31 remove them. The final LuaLaTeX log has zero '
             'overfull boxes, undefined references or citations, missing characters, '
             'fatal errors and LaTeX warnings. Root inspected rendered pages '
             '1, 48–58, 74, 130, 168–175, 240, 253–255 and 281, including full-size '
             'checks of 51, 55, 174, 175 and 255. The exact counts and PDF hash are in '
             'code/checkpoint12_qa.json.\n\n')
    text += ('The additions are A.4.36–A.4.40, E.2.30–E.2.31 and F.3.35–F.3.36. '
             'The exact elliptic tensor, integral tangent, isogeny, branch, period-product, '
             'degree-prime leaf and cusp-conjugator programs are retained with their '
             'registered runs. F.3.36 uses the opened original Kleiman text, including '
             'Theorem 2A11, Proposition 3.8, Corollary 3.9 and Remark 3.10; the attempted '
             'Lieberman download yielded HTML and is recorded as not obtained. These '
             'family results do not settle the remaining general numerical-equivalence '
             'question. This verification creates no checkpoint and records no movement '
             'review.\n')
    report.write_text(text)
print(json.dumps(data, indent=2))
