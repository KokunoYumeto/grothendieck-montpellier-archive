"""Promote the fully audited seven-label twisted Cartier/Moore assembly."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, difflib, csv

agent = Path(__file__).resolve().parents[1]
work = agent.parents[1]
candidate = agent / 'ppav_twisted_Cartier_Moore_candidate.tex'
canonical = agent / 'ppav_twisted_Cartier_Moore.tex'
expected = '80db90e54c403914d3aa26626a829ec31c1f85eecb078833e675af5441ada65b'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate) == expected
assert not canonical.exists()
root_audit = work / 'outputs/root_twisted_Cartier_Moore_audit.json'
oc_audit = work / 'agents/obstructions_crystals/twisted_Cartier_Moore_bridge_independent_audit.json'
for path in (root_audit, oc_audit):
    data = json.loads(path.read_text())
    assert 'PASS' in data['status'] and data['candidate_sha256'] == expected

before = candidate.read_text()
text, count = re.subn(r'\\status\{Candidate[^}]*\}',
                     lambda _: r'\status{Proved; independent audits passed.}', before)
assert count == 7
old = ('The complete linear system \\(|3\\Theta_A|\\) is a closed immersion,\n'
       'as in the previously proved cubic-theta jet results.')
new = ('The complete linear system \\(|3\\Theta_A|\\) is a closed immersion.\n'
       'For an indecomposable polarization this follows from\n'
       'Theorem~\\ref{thm:ppav-three-theta-jets}; for a product polarization,\n'
       'the degree-three embeddings of the two elliptic factors followed\n'
       'by the Segre embedding give the same assertion.')
assert old in text
text = text.replace(old, new)
old = ('This whole subsection\n'
       'remains a candidate pending complete independent proof audits.')
new = ('The complete independent obstruction/crystal proof and source audit\n'
       'passed at 01:35:24.622429 UTC on 20 November 2026, and the complete\n'
       'parent proof and source audit passed at 01:37:50.135808 UTC.\n'
       'Both checked all seven assertions, the exact theta lifts, every\n'
       'Frobenius target, the fixed-point argument, and the outgoing\n'
       'isogeny construction.  No new numerical experiment was needed\n'
       'for these geometric deductions.  The exact candidate and both\n'
       'audit records remain retained.')
assert old in text
text = text.replace(old, new)
canonical.write_text(text)
proof_diff = agent / 'history/ppav_twisted_Cartier_Moore_promotion.diff'
assert not proof_diff.exists()
proof_diff.write_text(''.join(difflib.unified_diff(
    before.splitlines(True), text.splitlines(True),
    fromfile=str(candidate.relative_to(work)),
    tofile=str(canonical.relative_to(work)))))

changes = []
def save_change(path, after, reason):
    prior = path.read_text()
    assert prior != after
    stem = 'pre_ppav_twisted_Cartier_Moore_' + str(path.relative_to(work)).replace('/', '__')
    saved = agent / 'history' / stem
    assert not saved.exists()
    saved.write_text(prior)
    diff = saved.with_name(saved.name + '.diff')
    diff.write_text(''.join(difflib.unified_diff(
        prior.splitlines(True), after.splitlines(True),
        fromfile=str(saved.relative_to(work)), tofile=str(path.relative_to(work)))))
    path.write_text(after)
    changes.append({'path': str(path.relative_to(work)),
                    'before': str(saved.relative_to(work)),
                    'diff': str(diff.relative_to(work)), 'reason': reason})

consolidate = work / 'code/consolidate.py'
prior = consolidate.read_text()
anchor = "   out.write('\\n\\\\input{sections/A_nonordinary_ppav_covectors}\\n')"
assert prior.count(anchor) == 1
assert "moore_parameters=a/'obstructions_crystals/A4_Moore_singular_parameters.tex'" in prior
addition = ("   twisted_cartier=a/'monodromy/ppav_twisted_Cartier_Moore.tex'\n"
            "   if twisted_cartier.exists() and '\\\\status{Candidate' not in twisted_cartier.read_text():\n"
            "    out.write('\\n'+twisted_cartier.read_text()+'\\n')\n")
save_change(consolidate, prior.replace(anchor, addition + anchor),
            'Insert the audited typed Cartier/Moore assembly immediately after its principal-bridge and Moore-classification dependencies; preserve all B87 and other current includes.')

bib = agent / 'references.bib'
prior = bib.read_text()
key = 'EdixhovenVanDerGeerMoonenAV'
start = prior.index('{' + key + ',')
end = prior.index('\n}', start)
segment = prior[start:end]
pos = segment.index('note={') + len('note={')
depth, i = 1, pos
while depth:
    if segment[i] == '{': depth += 1
    elif segment[i] == '}': depth -= 1
    i += 1
sentence = (' For the typed cubic Cartier--Moore bridge on 20 November 2026, '
            'the parent and obstruction/crystal audits freshly read the complete '
            'original Theorem2.7 and Corollary2.8 pp19--20, Lemma8.24 p121, '
            'Theorem8.28 pp122--123, and normalized-symmetry Definition11.44 p178. '
            'The adjacent Lemma11.45 has an unwritten proof and is not imported; '
            'the required symmetry identities are proved from rigidification and proper global units. '
            'The earlier complete isotropic-descent and principal-bridge source reads are reused explicitly. '
            'No new image inspection or numerical computation is asserted by this access note.')
after = prior[:start] + segment[:i-1] + sentence + segment[i-1:] + prior[end:]
save_change(bib, after, 'Append the exact completed TCM primary-source access and explicit scope of the unwritten adjacent proof; retain all earlier notes.')

now = datetime.now(timezone.utc).isoformat()
labels = re.findall(r'\\label\{([^}]+)\}', candidate.read_text())
record = {'status': 'PROMOTED', 'actual_utc': now,
          'candidate': str(candidate.relative_to(work)), 'candidate_sha256': expected,
          'canonical': str(canonical.relative_to(work)), 'canonical_sha256': sha(canonical),
          'labels': labels, 'root_audit': str(root_audit.relative_to(work)),
          'oc_audit': str(oc_audit.relative_to(work)),
          'proof_diff': str(proof_diff.relative_to(work)), 'changes': changes,
          'scope': 'Exact twisted Cartier/Moore coefficients and maximal dual alternating rank for every fixed odd principal-cube degree. No new full monodromy degree or generic-curve rank theorem is inferred.'}
(agent / 'outputs/ppav_twisted_Cartier_Moore_promotion.json').write_text(json.dumps(record, indent=2) + '\n')
(agent / 'outputs/checkpoint31_required_twisted_Cartier_Moore.json').write_text(json.dumps({
    'required': str(canonical.relative_to(work)), 'canonical_sha256': sha(canonical),
    'note': 'Parent owns the CP31 preparer; this promotion edits only the current consolidation include.'}, indent=2) + '\n')
with (agent / 'CHECK_EVENTS_post_CP16.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for label in labels:
        writer.writerow([label, now, '/root/monodromy', 'PROMOTED-root-OC-full-proof-source-PASS', record['scope']])
with (agent / 'post_CP16_notes.md').open('a') as f:
    f.write('\n## ' + now + ' — Twisted Cartier/Moore assembly promoted\n\n' + record['scope'] +
            ' The exact candidate is retained unchanged; the canonical replaces only status/audit wording and makes the already-audited cubic embedding reference explicit. All prior consolidation and bibliography bytes and exact diffs are retained. No proof passage or executed program was removed.\n')
assert sha(candidate) == expected
print(json.dumps(record, indent=2))
