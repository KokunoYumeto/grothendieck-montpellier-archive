"""Read-only source-log audit; recommendations do not modify historical logs."""
from pathlib import Path
import csv
import collections
import datetime
import json
import re
import time

started = time.perf_counter()
base = Path(__file__).resolve().parents[1]
agents = base.parent
rows = []
for path in sorted(agents.glob('*/*CHECK_EVENTS.tsv')):
    with path.open(newline='') as source:
        for line, record in enumerate(csv.DictReader(source, delimiter='\t'), 2):
            rows.append({'path': str(path.relative_to(agents.parent)),
                         'line': line, **record})

recommendations = []
for record in rows:
    kind = record.get('type', '')
    outcome = record.get('outcome', '')
    action = category = rationale = ''
    if kind in {'Independent review requested', 'Boutot ChapterV access',
                'Alternate source access', 'recovery verification',
                'typographical_correction',
                'independent proof/source check received',
                'independent root check received'}:
        action = 'retain in auxiliary administrative/access log'
        category = 'no mathematical canonical category assigned'
        rationale = {
            'Independent review requested': 'A request is not a completed review.',
            'Boutot ChapterV access': 'Only metadata was obtained; the full chapter was inaccessible.',
            'Alternate source access': 'This row records failed Quillen access and points to a separate Skalit certification; it does not itself check the inaccessible proposition.',
            'recovery verification': 'Reconstruction/fidelity provenance alone; actual rerun and proof-reread events are separate.',
            'typographical_correction': 'Only a literal comma was reported and corrected; no new proof check.',
            'independent proof/source check received': 'Author receipt duplicates the separately preserved reviewer event; do not count receipt as a new independent re-proof.',
            'independent root check received': 'Author receipt duplicates the separately preserved root event; do not count receipt as a new independent re-proof.',
        }[kind]
    elif kind in {'source retrieval', 'source-access record',
                  'primary source recovery', 'retrieval and OCR audit'}:
        action = 'canonicalize with nonmathematical scope'
        category = 'computation or formal certificate'
        rationale = 'Successful retrieval/hash/text/OCR work only; preserve failures and exact output scope. This event does not establish a fresh mathematical source reading. Any explicitly reported visual source reading remains a separate source audit.'
    elif kind in {'restoration-compare', 'fresh recovery fidelity audit',
                  'full recovery fidelity and proof audit'}:
        action = 'canonicalize actual renewed mathematical reread'
        category = 'targeted proof check'
        rationale = 'Outcome explicitly says the restored complete proof was reread and mathematics verified. Preserve distinction from historical certification; do not label independent re-proof merely from fidelity.'
    elif kind in {'fresh recovery certificate', 'fresh recovery document verification'}:
        action = 'canonicalize actual fresh program/build run'
        category = 'computation or formal certificate'
        rationale = 'Use the fresh retained runtime/output; document compilation certifies typesetting only, not mathematics.'
    elif kind == 'source-locator-correction':
        action = 'canonicalize actual source comparison'
        category = 'used and rechecked in this run'
        rationale = 'The primary text was actually checked to repair the equation locator; do not treat this as a new proof.'
    elif kind in {'correction', 'correction found and verified',
                  'targeted scope correction', 'failed route and correction'}:
        action = 'canonicalize mathematical sign/scope/typing check'
        category = 'targeted proof check'
        rationale = 'This is substantive mathematical convention/scope checking, not merely administrative. Retain any withdrawal or failed-route outcome exactly.'
    elif re.search(r'typeset|compil|document validation', kind, re.I):
        action = 'canonicalize document-only verification'
        category = 'computation or formal certificate'
        rationale = 'Compilation/layout validation only; retain this explicit limitation in the outcome.'
    if action:
        recommendations.append({**record, 'recommended_action': action,
                                'recommended_category': category,
                                'rationale': rationale})

aliases = collections.defaultdict(list)
missing_effort = collections.defaultdict(list)
for record in rows:
    who = record.get('who', record.get('who_model_effort_run', ''))
    location = {'path': record['path'], 'line': record['line'],
                'statement_id': record.get('statement_id', '')}
    if 'GPT' not in who or ('/root' not in who and 'RESEARCH_SA06' not in who):
        aliases[who].append(location)
    if not re.search(r'effort|reasoning', who, re.I):
        missing_effort[who].append(location)

out = base / 'output'
out.mkdir(exist_ok=True)
fields = ['path', 'line', 'statement_id', 'date', 'who_original',
          'type_original', 'recommended_action', 'recommended_category',
          'rationale', 'outcome_original']
with (out / 'event_metadata_recommendations.tsv').open('w', newline='') as target:
    writer = csv.DictWriter(target, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    for record in recommendations:
        writer.writerow({
            'path': record['path'], 'line': record['line'],
            'statement_id': record.get('statement_id', ''),
            'date': record.get('date', ''),
            'who_original': record.get('who', record.get('who_model_effort_run', '')),
            'type_original': record.get('type', ''),
            'recommended_action': record['recommended_action'],
            'recommended_category': record['recommended_category'],
            'rationale': record['rationale'],
            'outcome_original': record.get('outcome', '')})

result = {
    'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_files': len({r['path'] for r in rows}),
    'source_rows': len(rows),
    'recommendation_rows': len(recommendations),
    'recommended_action_counts': dict(collections.Counter(
        r['recommended_action'] for r in recommendations)),
    'alias_rows': dict(aliases),
    'missing_effort_rows': dict(missing_effort),
    'type_counts': dict(collections.Counter(r.get('type', '') for r in rows)),
    'runtime_seconds': time.perf_counter() - started,
    'scope': 'Read-only snapshot and conservative row-level recommendations; no source event modified, no new mathematical check or main-gate movement.'
}
(out / 'event_metadata_audit.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items()
                  if k not in {'alias_rows', 'missing_effort_rows', 'type_counts'}}, indent=2))
