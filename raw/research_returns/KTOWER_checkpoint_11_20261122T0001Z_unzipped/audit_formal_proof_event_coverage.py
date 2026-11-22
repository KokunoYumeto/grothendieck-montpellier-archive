"""Index formal finding IDs against recorded events; do not assert a proof replay."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import sys

B = Path(__file__).resolve().parent
paper = (B / 'KTOWER.tex').read_text()
events = list(csv.DictReader((B / 'CHECK_EVENTS.tsv').open(), delimiter='\t'))
entries = []
for match in re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary)\}\[([^\]]+)\]', paper):
    for statement in re.findall(r'KT-[A-Z0-9-]+', match.group(2)):
        pattern = re.compile(r'(?<![A-Z0-9-])' + re.escape(statement) + r'(?![A-Z0-9-])')
        found = [r for r in events if pattern.search(r['statement_id'])]
        direct = [r for r in found if r['type'] in ('targeted proof check', 'independent re-proof')]
        entries.append({'id': statement, 'environment': match.group(1),
                        'line': paper[:match.start()].count('\n') + 1,
                        'event_count': len(found), 'direct_proof_event_count': len(direct)})
missing = [r['id'] for r in entries if not r['direct_proof_event_count']]
report = {'date_utc': datetime.now(timezone.utc).isoformat(),
          'tex_sha256': hashlib.sha256((B / 'KTOWER.tex').read_bytes()).hexdigest(),
          'formal_statement_count': len(entries), 'event_count': len(events),
          'missing_direct_proof_events': missing, 'statements': entries,
          'scope': 'Record-index coverage only. The actual content, exact artifact and reading scope are in the named events and reviews. This script does not read proofs or verify mathematics.'}
out = Path(sys.argv[1])
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: report[k] for k in ('formal_statement_count', 'event_count', 'missing_direct_proof_events')}))
if missing:
    raise SystemExit(1)
