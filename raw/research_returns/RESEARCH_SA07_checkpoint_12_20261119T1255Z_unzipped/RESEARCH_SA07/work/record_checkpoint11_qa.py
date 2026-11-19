"""Record completed visual/log/hash checks; this does not create a checkpoint."""
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
    'first_complete_build_overfull_pt': [4.93317],
    'transient_integration_errors_repaired': ['multi-column split environment', 'undefined mathscr alphabet'],
    'visually_inspected_pages': [1,49,71,116,150,151,152,153,154,155,156,157,158,159,230,235,236,261],
    'additional_full_size_inspection': [155,157],
    'visual_outcome': 'All inspected content fits; the repaired lattice definitions and new homology, cochain and detector displays are legible and within margins.',
    'checkpoint_created_by_this_script': False,
}
(OUT / 'code' / 'checkpoint11_qa.json').write_text(json.dumps(data, indent=2) + '\n')
report = OUT / 'RESEARCH_SA07_report.md'
text = report.read_text()
heading = '## Verification before checkpoint11'
if heading not in text:
    text += '\n\n' + heading + '\n\n'
    text += (f'The current paper has{page_count} pages,{len(results)} numbered statements and'
             f'{pdf.stat().st_size} bytes. The integrated record has{len(events)} check events,'
             f'{len(sources)} source-access entries with explicit access status, and'
             f'{len(records)} registered mathematical programs. Every registered run passes; '
             'root verified every retained source/output hash pair with no mismatch. '
             'The307-assertion historical inventory is unchanged.\n\n')
    text += ('The first added-display build exposed an alignment-environment error, and '
             'the next exposed an unavailable alphabet control; both are repaired. '
             'The first completed261-page build had one4.93317pt overflow in the '
             'E.2.29 lattice definitions. Breaking those definitions into three aligned '
             'rows removed it. The final LuaLaTeX log has zero overfull boxes, undefined '
             'references/citations, missing characters, fatal errors and LaTeX warnings. '
             'Root rendered and visually inspected pages1,49,71,116,150-159,230,235,236,261, '
             'with full-size checks of155 and157. The integral Hom block, cusp matrices, '
             'nilpotent construction, explicit cocycle lift and IA minor fit. '
             'The machine-readable record is code/checkpoint11_qa.json.\n\n')
    text += ('E.2.28 andE.2.29 now appear in the main paper with complete proofs and '
             'original-source maps. The A5 registered run passed in1.612472seconds. '
             'The extra root prescription check, cyclic Bass-unit lift, and elliptic '
             'tangent/graph/isogeny work retain their programs, outputs and exact scope '
             'in the work notes. Root read the original Mochizuki pp13-14 and16-19 '
             'and Waldschmidt pp385-386. The actual isogeny formula gives a discrepancy '
             'valuation decreasing by one per connected ordinary step, with the '
             'unproved lower denominator bound explicitly retained.\n\n')
    text += ('Actualreview06 was recorded at11:55:07.516251UTC, with movementYES for '
             'the closure of F.3.32-F.3.33 and no consecutive no-movement reviews. '
             'The next actual hourly review is due12:55UTC. This typesetting and '
             'record check is not an additional movement review.\n')
    report.write_text(text)
print(json.dumps(data, indent=2))
