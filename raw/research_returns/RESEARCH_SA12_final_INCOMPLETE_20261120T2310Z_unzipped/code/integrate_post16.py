"""Integrate audited post-checkpoint16 statements without creating an archive."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
paths = ['parts/C/post16_research/D_integral_antinef_energy_cycle.tex']
pattern = re.compile(r'\\begin\{(proposition|corollary|lemma|example|theorem)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
rows = []
for rel in paths:
    s = (root / rel).read_text()
    for match in pattern.finditer(s):
        assert match[2].startswith(('Proved:', 'Refuted:')), (rel, match[2])
        rows.append(dict(
            id=match[3], statement=match[2].split(':', 1)[1].strip(),
            status=match[2].split(':', 1)[0],
            where_proved=rel + ': label ' + match[3],
            depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}', s)))),
            manuscript_pages='29/061,066',
            notes='Post-checkpoint16 auxiliary result with complete root/B/C/D actual-file proof audits. No effective object atlas, factorial cover count or general finite-generation conclusion follows. Not main-gate movement.'
        ))
p = root / 'parts/D/results_D.csv'
with p.open() as f:
    previous = list(csv.DictReader(f))
known = {row['id'] for row in previous}
new = [row for row in rows if row['id'] not in known]
with p.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'statement', 'status', 'where_proved', 'depends_on', 'manuscript_pages', 'notes'])
    writer.writeheader()
    writer.writerows(previous + new)
p = root / 'parts/D/paper_D.tex'
s = p.read_text()
for rel in paths:
    line = '\\input{' + rel + '}'
    if line not in s:
        s += '\n' + line + '\n'
p.write_text(s)
p = root / 'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f:
    events = list(csv.DictReader(f, delimiter='\t'))
added = {row['id'] for row in new}
with (root / 'parts/C/post16_research/CHECK_EVENTS_C_post16.tsv').open() as f:
    for event in csv.DictReader(f, delimiter='\t'):
        if event['label'] not in added:
            continue
        actor = event['auditor'].rsplit('; ', 1)[1]
        events.append(dict(
            statement_id=event['label'], date=now,
            who='GPT-6 Astra Pro; ' + actor + '; SA12 run1; effort setting not independently exposed',
            type=event['type'], outcome=event['result'] + ' Consolidated after the immutable checkpoint16; the author manifest records subsequent status and fraction-only typography changes, with no mathematical change.'
        ))
with p.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['statement_id', 'date', 'who', 'type', 'outcome'], delimiter='\t')
    writer.writeheader()
    writer.writerows(events)
p = root / 'parts/D/unresolved_D.tex'
s = p.read_text()
marker = '% Post-checkpoint16 integral cycle budget'
if marker not in s:
    s += '\n\n' + marker + r'''
\paragraph{An integral cycle without denominator loss.}
Lemma~\ref{D:integral-antinef-energy-cycle} constructs an integral
anti-nef exceptional cycle by global lattice minimization and zero-cost
repairs on the zero-canonical components. Its energy is linear in cover
degree, and it has strictly positive conormal degree on the nonrational
core. Corollary~\ref{D:punctured-cover-antinef-cycle} bounds cohomology on
every fixed multiple of the full cycle, including its nilpotent layers.
These statements remove a numerical denominator loss. They do not prove
formal determination, boundary-framed compatibility, or the required
object-presentation bound, and are not new main-gate movement.
'''
    p.write_text(s)
p = root / 'code/assemble.py'
s = p.read_text()
paragraph = 'Two post-checkpoint16 auxiliary units construct an integral anti-nef exceptional cycle with linear energy and linear full-cycle cohomology, avoiding denominator loss. All four actual-file proof checks passed. Strict conormal positivity holds on the positive-canonical core; entire zero-canonical components are separately treated by the RDP fundamental cycle. Formal determination, boundary-framed compatibility and an effective object atlas remain unproved. This is not movement after review10.'
if paragraph not in s:
    s = s.replace("'','## Files and continuation','',", repr(paragraph) + ",\n'','## Files and continuation','',")
    p.write_text(s)
record = dict(utc=now, labels=[row['id'] for row in rows], added_rows=len(new),
              files=[dict(path=rel, sha256=hashlib.sha256((root / rel).read_bytes()).hexdigest()) for rel in paths],
              main_movement=False, archive_created=False,
              requested_open=['general D.1', 'general D.2(ii)', 'residual L8'])
(root / 'code/output/integrate_post16.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
