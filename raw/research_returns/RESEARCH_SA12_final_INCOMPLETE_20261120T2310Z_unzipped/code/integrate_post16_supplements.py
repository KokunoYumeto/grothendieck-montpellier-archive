"""Integrate individually audited post16 repairs and functorial transfers."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
specs = [
    ('parts/C/post16_research/integration_manifest_C_RDP_Hom_framing.json', 'C', 'auxiliary'),
    ('parts/D/post16_research/integration_manifest_Brauer_transfer_root.json', 'root', 'closure'),
]
pattern = re.compile(r'\\begin\{(proposition|corollary|lemma|example|theorem)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
cols = ['id', 'statement', 'status', 'where_proved', 'depends_on', 'manuscript_pages', 'notes']
p = root / 'parts/D/results_D.csv'
with p.open() as f:
    rows = list(csv.DictReader(f))
known = {r['id'] for r in rows}
p = root / 'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f:
    events = list(csv.DictReader(f, delimiter='\t'))
all_labels, files, added_labels = [], [], []
for manifest_rel, owner, kind in specs:
    manifest = json.loads((root / manifest_rel).read_text())
    rel = manifest.get('path', manifest.get('file'))
    source = (root / rel).read_text()
    digest = hashlib.sha256((root / rel).read_bytes()).hexdigest()
    assert digest == manifest['sha256'], (rel, digest)
    if owner == 'C':
        assert {a['auditor'] for a in manifest['audits']} >= {'/root', '/root/part_b', '/root/part_c', '/root/part_d'}
    else:
        assert set(manifest['audits']) == {'root', 'B', 'C', 'D'}
    matches = list(pattern.finditer(source))
    assert [m[3] for m in matches] == manifest['labels']
    assert all(m[2].startswith(('Proved:', 'Refuted:')) for m in matches)
    all_labels.extend(manifest['labels'])
    files.append(dict(path=rel, sha256=digest, accounting=kind))
    current_added = set()
    for m in matches:
        if m[3] in known:
            continue
        note = ('Functorial and finite-normalization closure of the one global Brauer-zero reduction. Fixed detecting-surface pullback vanishing suffices; no H2 injection. Four complete actual-file audits. Not an additional movement event.' if kind == 'closure' else
                'Auxiliary RDP Hom/framing theorem or exact refutation with two-end and finite-subscheme repairs. Four complete actual-file audits and independent finite certificate runs. Individual modules only; no arbitrary Artinian-family decomposition or hereditary object atlas. Not main-gate movement.')
        rows.append(dict(id=m[3], statement=m[2].split(':', 1)[1].strip(), status=m[2].split(':', 1)[0],
                         where_proved=rel + ': label ' + m[3],
                         depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}', source)))),
                         manuscript_pages='29/061,066', notes=note))
        known.add(m[3]); current_added.add(m[3]); added_labels.append(m[3])
    p = root / 'parts/D/paper_D.tex'
    s = p.read_text(); line = '\\input{' + rel + '}'
    if line not in s:
        p.write_text(s + '\n' + line + '\n')
    if owner == 'C':
        with (root / 'parts/C/post16_research/CHECK_EVENTS_C_post16.tsv').open() as f:
            author_events = list(csv.DictReader(f, delimiter='\t'))
        for e in author_events:
            if e['label'] not in current_added:
                continue
            actor = e['auditor'].rsplit('; ', 1)[-1]
            events.append(dict(statement_id=e['label'], date=now,
                               who='GPT-6 Astra Pro; ' + actor + '; SA12 run1; effort setting not independently exposed',
                               type=e['type'], outcome=e['result'] + ' Consolidated from the separately retained author event; this timestamp is the integration time, and no unreported source reopening is implied.'))
    else:
        for e in manifest['events']:
            if e['label'] not in current_added:
                continue
            actor = '/root' if e['actor'] == 'root' else '/root/part_' + e['actor'].lower()
            events.append(dict(statement_id=e['label'], date=e['recorded_utc'],
                               who='GPT-6 Astra Pro; ' + actor + '; SA12 run1; effort setting not independently exposed',
                               type=e['kind'], outcome=e['status'] + ': ' + e['scope']))

with (root / 'parts/D/results_D.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
with (root / 'parts/D/CHECK_EVENTS_D.tsv').open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['statement_id', 'date', 'who', 'type', 'outcome'], delimiter='\t')
    w.writeheader(); w.writerows(events)

p = root / 'parts/D/unresolved_D.tex'; s = p.read_text()
s = s.replace('Complete local punctures, nonnormal transfer of this new theorem,\nthe remaining cross-characteristic families and alternating\nmultiplicities require their separate arguments.',
              'Complete local punctures, the remaining cross-characteristic\nfamilies and alternating multiplicities require their separate arguments.\nCorollaries~\\ref{D:Brauer-zero-detecting-surface-transfer} and\n\\ref{D:Brauer-zero-normalization-transfer} now give the detecting-surface\nand finite-normalization closure of this same reduction. They require\nzero Brauer class only after each fixed surface pullback, with no\ninjection in degree-two cohomology asserted.')
marker = '% Post-checkpoint16 RDP Hom repairs'
if marker not in s:
    s += '\n\n' + marker + r'''
\paragraph{What boundary framing does and does not cost.}
Lemma~\ref{D:RDP-full-Hom-vanishing} proves unframed Hom vanishing
for full sheaves on rational double points and a finite-subscheme
bound by rank product times length. The exact standard two-end
bound on an $A$-chain is at most $2rs$, independently of its length,
by Proposition~\ref{D:A-chain-two-end-Hom-bound}. However
Example~\ref{D:A-chain-internal-framing-obstruction} has ranks one,
one transverse internal branch and framed dimension $m$ on an
$A_{3m-1}$ chain, even for fixed-characteristic Frobenius-periodic
reflexive modules. Thus attachment count alone does not suffice.
These individual-module statements do not yet provide an effective
global family atlas or the needed nonabelian count.
'''
p.write_text(s)

p = root / 'code/assemble.py'; s = p.read_text()
s = s.replace('This packet does not yet cover complete local punctures, nonnormal transfer, alternating multiplicities or general crowns, and does not close any requested row.',
              'The separately checked detecting-surface and finite-normalization corollaries give the closure of this same reduction, requiring zero Brauer class only after the fixed surface pullbacks and asserting no H2 injection. This packet does not yet cover complete local punctures, alternating multiplicities or general crowns, and does not close any requested row.')
paragraph = 'Three audited auxiliary RDP framing units give unframed Hom vanishing, the exact two-end dimension rs+r s0−r0 s≤2rs in every characteristic, and a rank-one single-internal-branch counterfamily with framed H1=m on A_(3m−1). Thus a bound using attachment count alone is refuted; the two-end and finite-subscheme bounds are proved repairs. Root, B and D independently reran the536909-assertion finite exponent certificate. The geometric proofs and individual-module scope are separate; no hereditary atlas is inferred.'
if paragraph not in s:
    s = s.replace("'','## Files and continuation','',", repr(paragraph) + ",\n'','## Files and continuation','',")
p.write_text(s)

record = dict(utc=now, labels=all_labels, added_rows=len(added_labels), files=files,
              new_main_movement=False, accounting='Auxiliary framing repairs plus formal closure of the already integrated single Brauer-zero reduction.',
              requested_status_changes=[], archive_created=False)
(root / 'code/output/integrate_post16_supplements.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
