"""Promote the three global PGL units after four exact-file audits."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
directory = root / 'parts/D/post23_research'
path = directory / 'D_global_finite_puncture_projective_growth_root.tex'
candidate = path.read_text()
candidate_hash = 'a4dc93accb491adf249ef68706ca295a3914c28c5be3635b8130582ec857454a'
assert hashlib.sha256(candidate.encode()).hexdigest() == candidate_hash
audits = {
    'root': 'parts/D/post23_research/audit_global_finite_puncture_projective_growth_root.json',
    'B': 'parts/B/post23_research/audit_root_global_finite_puncture_projective_B.json',
    'C': 'parts/C/post23_research/audit_root_global_finite_puncture_projective_C.json',
    'D': 'parts/D/post23_research/audit_global_finite_puncture_projective_growth_D.json'
}
for actor, audit_path in audits.items():
    audit = json.loads((root / audit_path).read_text())
    assert audit['sha256'] == candidate_hash
    assert audit.get('verdict', audit.get('status')) == 'PASS'

snapshot = directory / 'global_finite_puncture_audited.source.txt'
assert not snapshot.exists()
snapshot.write_text(candidate)
old = 'They are proper normal curves or points; if $d_i$ generators\ngenerate their fundamental groups, their representation counts'
new = ('They are proper normal curves or points; their fundamental groups\n'
       'are finitely generated\n'
       '\\citep[Expose~X, Theorem~2.6, pp.~272--273]{C_SGA1}.\n'
       'If $d_i$ generators generate those groups, their representation counts')
assert candidate.count(old) == 1
promoted = candidate.replace(old, new)
assert promoted.count('[Candidate:') == 3
promoted = promoted.replace('[Candidate:', '[Proved:')
promoted = promoted.replace('% Candidate: pending four complete actual-file audits.',
                            '% Proved: four complete actual-file audits; one explicit known-input citation added.')
reverse = promoted.replace('[Proved:', '[Candidate:')
reverse = reverse.replace('% Proved: four complete actual-file audits; one explicit known-input citation added.',
                          '% Candidate: pending four complete actual-file audits.')
reverse = reverse.replace(new, old)
assert reverse == candidate
path.write_text(promoted)
now = datetime.now(timezone.utc).isoformat()
manifest = {
    'recorded_utc': now, 'path': str(path.relative_to(root)),
    'sha256': hashlib.sha256(promoted.encode()).hexdigest(),
    'audited_candidate_sha256': candidate_hash,
    'candidate_snapshot': str(snapshot.relative_to(root)),
    'status': 'Proved',
    'labels': ['D:global-finite-puncture-projective-growth',
               'D:global-projective-finite-puncture-closure',
               'D:global-unrestricted-projective-simple-products'],
    'bibliography': None,
    'reused_bibliography_keys': ['C_SGA1', 'LucchiniMarionTracey2020D'],
    'audit_scope': {
        actor: {'record': audit_path,
                'scope': 'Full mathematical candidate audited at the recorded SHA. Exact primary scope is in this record; final changes are status/comment and the explicit SGA1 X2.6 citation only.'}
        for actor, audit_path in audits.items()
    },
    'promotion_changes': 'Three Candidate-to-Proved headings, leading comment, and one explicit citation for the already-used proper-curve generator theorem. Exact reversal to the fully audited bytes verified.',
    'citation_refresh': {
        'actor': 'root',
        'source': 'parts/C/sources/sga1/smf_doc-math_3_01.tex',
        'locator': 'Expose X Theorem2.6 and preceding complete written argument, pp272--273',
        'scope': 'Fresh full statement and proof read. C explicitly approved this exact added locator in its audit. No mathematical assertion or constant changed.'
    },
    'scope': [
        'Fixed normal proper surfaces in characteristic p minus finitely many points; all q=p^f and ranks, unrestricted geometric Brauer period.',
        'Proper schemes in every dimension with finite punctures of componentwise codimension at least two, and the stated controlled-exceptional-centre codimension-two closure. Nonnormal and nonreduced schemes allowed via finite normalization.',
        'Selected simple-product quotients with the projective size comparison, including every defining-characteristic Lie family. No unrestricted alternating or crown conclusion.'
    ],
    'movement_classification': 'One strict global finite-puncture PGL gate reduction, including its detecting-curve/count prerequisites and dimensional, normalization and simple-family consequences. To be counted once at formal review16.',
    'literature_scope': 'Scoped queries recorded in root_global_and_local_quotient_literature_search.json; known inputs cited with exact opened locators. No novelty or priority claim.'
}
out = directory / 'integration_manifest_root_global_finite_puncture.json'
assert not out.exists()
out.write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'utc': now, 'path': manifest['path'], 'sha256': manifest['sha256'], 'labels': manifest['labels'], 'manifest': str(out.relative_to(root))}, indent=2))
