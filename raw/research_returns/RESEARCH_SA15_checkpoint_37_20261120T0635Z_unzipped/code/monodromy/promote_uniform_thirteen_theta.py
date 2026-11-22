"""Promote the exact norm-thirteen candidate after root and OC authorization."""
from pathlib import Path
from datetime import datetime, timezone
import csv, difflib, hashlib, json, re

agent = Path(__file__).resolve().parents[1]
work = agent.parents[1]
candidate = agent / 'nonordinary_uniform_thirteen_theta_geometry_candidate.tex'
expected = '9266244ac3fb5ca57c4c9c051be22f8d1787c42c7653c054c8a0b4fd1636b5db'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate) == expected
root_audit = work / 'outputs/root_uniform_thirteen_theta_audit.json'
oc_audit = work / 'agents/obstructions_crystals/uniform_thirteen_theta_independent_audit.json'
assert root_audit.exists() and oc_audit.exists()
canonical = agent / 'nonordinary_uniform_thirteen_theta_geometry.tex'
assert not canonical.exists()
text = candidate.read_text()
text, count = re.subn(r'\\status\{Candidate[^}]*\}', lambda m: '\\status{Proved; independent audits passed.}', text)
assert count == 7, count
extra = r'''
The complete independent parent proof and code audit passed at
00:18:08.900956 UTC on 20 November 2026. Its six unchanged isolated
stage reruns and the full 34-check reconstruction passed, the latter
in 0.741939530 seconds. The complete obstruction/crystal audit passed
at 00:18:09.650432 UTC; its full reconstructive rerun took
0.714615302 seconds. Both audits read the entire geometric proof,
all exceptional-fibre arguments, all exact coefficient programs, and
the applicable internal normal-form, nodality, and monodromy-transfer
proofs. They preserved the author outputs. The exact audited candidate,
its earlier layout versions, and their literal differences are retained.
'''
position = text.rfind('\\end{remark}')
assert position >= 0
text = text[:position] + extra + text[position:]
canonical.write_text(text)
changes = []

def edit(relative, old, new, reason):
    path = work / relative
    before = path.read_text()
    assert before.count(old) == 1, (relative, before.count(old))
    saved = agent / 'history' / ('pre_uniform_thirteen_' + relative.replace('/', '__'))
    assert not saved.exists()
    saved.write_text(before)
    after = before.replace(old, new)
    path.write_text(after)
    diff = saved.with_name(saved.name + '.diff')
    diff.write_text(''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True), fromfile=str(saved.relative_to(work)), tofile=relative)))
    changes.append({'file': relative, 'prior': str(saved.relative_to(work)), 'diff': str(diff.relative_to(work)), 'reason': reason})

edit('code/consolidate.py', "'monodromy/nonordinary_uniform_eleven_theta_geometry.tex'",
     "'monodromy/nonordinary_uniform_eleven_theta_geometry.tex',\n                  'monodromy/nonordinary_uniform_thirteen_theta_geometry.tex'",
     'Include the fully audited norm-thirteen theorem after norm eleven.')
edit('code/prepare_checkpoint29.py', 'for rel in required:\n',
     "required.append('agents/monodromy/nonordinary_uniform_thirteen_theta_geometry.tex')\nfor rel in required:\n",
     'Require the proved canonical norm-thirteen input before checkpoint29 integration.')
edit('agents/monodromy/nonordinary_arbitrary_odd_neighbors.tex',
     'remaining odd degree is thirteen.',
     'remaining odd degree is seventeen after\nCorollary~\\ref{cor:f0-odd-multiples-thirteen-candidate}.',
     'Replace the superseded residual degree-thirteen gate by the now-proved forward reference and degree seventeen.')
edit('agents/monodromy/nonordinary_cubic_component_norm_transfer.tex',
     'fixed two-rank-zero odd degree is thirteen after\nCorollary~\\ref{cor:f0-odd-multiples-eleven-candidate};',
     'fixed two-rank-zero odd degree is seventeen after\nCorollary~\\ref{cor:f0-odd-multiples-thirteen-candidate};',
     'Update only the residual degree after the newly proved degree-thirteen source.')
edit('agents/monodromy/nonordinary_uniform_eleven_theta_geometry.tex',
     'has the proved full one-covector stabilizer. The first remaining odd\nfixed-surface degree in two-rank zero is $13$.',
     'has the proved full one-covector stabilizer. The degree-thirteen case\nis settled in Corollary~\\ref{cor:f0-odd-multiples-thirteen-candidate};\nthe first remaining odd fixed-surface degree is then $17$.',
     'Preserve the norm-eleven theorem while replacing its superseded open-degree sentence with an explicit forward reference.')

labels = re.findall(r'\\label\{([^}]+)\}', candidate.read_text())
now = datetime.now(timezone.utc).isoformat()
scope = ('Every fixed indecomposable two-rank-zero ppav has a nodal polarized thirteen-self-isogeny with 168 nodes. '
         'For complete |3dTheta| systems every fixed f0 odd degree divisible by 3,5,7,11,13 is full GL; all even f0 degrees were already full. '
         'First remaining f0 odd degree17; f1 degree5/even8 unchanged.')
record = {'status': 'PROMOTED', 'actual_utc': now, 'candidate': str(candidate.relative_to(work)),
          'candidate_sha256': expected, 'canonical': str(canonical.relative_to(work)),
          'canonical_sha256': sha(canonical), 'labels': labels,
          'root_audit': str(root_audit.relative_to(work)), 'oc_audit': str(oc_audit.relative_to(work)),
          'changes': changes, 'scope': scope}
(agent / 'outputs/uniform_thirteen_theta_promotion.json').write_text(json.dumps(record, indent=2) + '\n')
with (agent / 'CHECK_EVENTS_post_CP16.tsv').open('a', newline='') as handle:
    writer = csv.writer(handle, delimiter='\t')
    for label in labels:
        writer.writerow([label, now, '/root/monodromy', 'PROMOTED-root-OC-full-proof-code-PASS', scope])
with (agent / 'post_CP16_notes.md').open('a') as handle:
    handle.write('\n## ' + now + ' — Uniform norm-thirteen theorem promoted\n\n' + scope + '\n\n'
                 'The exact audited candidate remains byte-identical. Every earlier executed version, failed or timed-out calculation, four-point packet, coefficient input and exact output is retained. '
                 'The original 3+2g choice is explicitly false at the exceptional modulus and is replaced there by the independently verified three-anticommuting-unit map. '
                 'Three obsolete degree-thirteen scope sentences were replaced by forward references and the degree-seventeen residual gate; their prior bytes and exact diffs are retained. '
                 'Root and OC completed full proof and reconstructive-code audits before promotion. No sampling or unproved specialization inference is used.\n')
assert sha(candidate) == expected
print(json.dumps(record, indent=2))
