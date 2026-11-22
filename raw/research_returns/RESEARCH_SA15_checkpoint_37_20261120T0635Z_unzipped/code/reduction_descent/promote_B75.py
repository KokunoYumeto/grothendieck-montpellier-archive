from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

own = Path(__file__).resolve().parents[1]
work = own.parents[1]
source = own / 'B_terminal_frobenius_pair_candidate.tex'
expected = '5475144072763f8e9869ac63030d9b550f5eaf507428ded08cc50dc08879a4ff'
raw = source.read_bytes()
assert hashlib.sha256(raw).hexdigest() == expected
root = json.loads((work / 'outputs/root_B75_audit.json').read_text())
comp = json.loads((own.parent / 'obstructions_crystals/B75_independent_audit.json').read_text())
for audit in (root, comp):
    assert audit['candidate_sha256'] == expected and 'PASS' in audit['status']
preserved = own / 'notes/B_terminal_frobenius_pair.prepromotion.tex'
assert not preserved.exists()
preserved.write_bytes(raw)
t = re.sub(r'\\status\{Candidate[^}]*\}', lambda _: r'\status{Proved; complete independent root and companion proof and exact-code audits passed.}', raw.decode())
t = t.replace('% Isolated after the CP27 canonical freeze; not part of that frozen paper.',
              '% Promoted after CP27 archive release; exact audited candidate retained.')
needle = r'''Equal \(b_i\) give equal \(c_i\pmod N\).'''
assert t.count(needle) == 1
t = t.replace(needle, r'''The last congruence in (B-RD75.1) is exactly (B-RD69.2):
the canonical high-line character is \(\mathbf F_p\)-valued,
which gives \(c_i\equiv B_i=pb_i\pmod{p+1}\).
''' + needle)
needle = 'executed computation failed.'
assert t.count(needle) == 1
t = t.replace(needle, needle + r'''
The complete independent root and companion proof/code audits
passed; their author-output-preserving exact reruns took
\(0.07519893000426237\) and \(0.0776550739974482\) seconds,
respectively. The exact candidate, all four assertion records,
program, output and audit provenance are retained.''')
canonical = own / 'B_terminal_frobenius_pair.tex'
assert not canonical.exists()
canonical.write_text(t)
labels = re.findall(r'\\label\{([^}]+)\}', t)
assert len(labels) == 4 and r'\status{Candidate' not in t
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'PROVED', 'promotion_utc': now,
    'canonical': str(canonical),
    'canonical_sha256': hashlib.sha256(canonical.read_bytes()).hexdigest(),
    'audited_candidate_sha256': expected,
    'preserved_candidate': str(preserved), 'labels': labels,
    'root_audit': '../../outputs/root_B75_audit.json',
    'root_audit_utc': root['actual_utc'],
    'root_runtime_seconds': root['independent_runtime_seconds'],
    'companion_audit': '../obstructions_crystals/B75_independent_audit.json',
    'companion_audit_utc': comp['actual_utc'],
    'companion_runtime_seconds': comp['elapsed_seconds'],
    'author_runtime_seconds': 0.08401663199765608,
    'scope': 'p>=5, mu_p in K, perfect residue and p not dividing e. Whole formal character recovery from actual p^n for n>=3 and e<p^(n-1)(p+1). Full B4 upper nu<=n-1 only for n>=4. Exact index3 for p^3<e<p^3(p+1); p5/e128..748 prime to5. Next p5/e752 remains bounded3..4 with no comparison constructed.',
    'source_scope': 'The exact B69.2 high-line congruence and full B74 induction were reread in the root audit. No new external theorem is imported.',
    'checkpoint_scope': 'Promoted after CP27 archive release. Not part of the immutable CP27 PDF/current table; canonical ready for CP28 wiring by parent.',
    'promotion_edits': ['Candidate statuses replaced by short proved statuses.', 'Explicit B69.2 citation and derivation added as requested by root.', 'Independent audit runtimes and retained provenance appended.'],
    'executed_failures': [], 'global_wiring_changes': []
}
(own / 'outputs/B75_promotion.json').write_text(json.dumps(record, indent=2) + '\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'PROVED_FULL_AUDITS', record['scope'],
                            'B_terminal_frobenius_pair.tex;outputs/B75_promotion.json',
                            'Root and OC full independent proof/code PASS; exact candidate preserved; post-CP27 promotion']) + '\n')
with (own / 'STATUS_CURRENT.md').open('a') as f:
    f.write('\n## ' + now + ' — B75 promoted: terminal Frobenius pair\n\n' + record['scope'] + '\n')
print(json.dumps(record, indent=2))
