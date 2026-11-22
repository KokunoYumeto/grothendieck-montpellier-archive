"""Promote the original-boundary global count only after four exact audits."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys

root = Path(__file__).resolve().parents[1]
directory = root / 'parts/D/post23_research'
path = directory / 'D_global_original_boundary_projective_growth_root.tex'
source = path.read_text()
candidate_hash = '18f24d92f0c5a1370077bf0917b93f5351680a3754dca044ca7441602f7c0ecb'
assert hashlib.sha256(source.encode()).hexdigest() == candidate_hash
assert len(sys.argv) == 4, 'Supply B, C and D audit paths in that order.'
audits = dict(root='parts/D/post23_research/audit_global_original_boundary_projective_growth_root.json',
              B=sys.argv[1], C=sys.argv[2], D=sys.argv[3])
for actor, audit_path in audits.items():
    audit = json.loads((root / audit_path).read_text())
    assert audit.get('sha256', audit.get('candidate_sha256')) == candidate_hash, (actor, audit)
    assert audit.get('verdict', audit.get('status')) == 'PASS', (actor, audit)

local_path = directory / 'D_local_divisorial_tame_projective_growth.tex'
assert '[Proved: quadratic projective growth for an original local tame pair]' in local_path.read_text()
snapshot = directory / 'global_original_boundary_audited.source.txt'
assert not snapshot.exists()
snapshot.write_text(source)
old_comment = '% Candidate: requires four complete audits and the promoted local-pair count.'
new_comment = '% Proved: four complete actual-file audits; local-pair input separately promoted.'
assert source.count('[Candidate:') == 3 and source.startswith(old_comment)
promoted = source.replace('[Candidate:', '[Proved:').replace(old_comment, new_comment)
assert promoted.replace('[Proved:', '[Candidate:').replace(new_comment, old_comment) == source
path.write_text(promoted)
now = datetime.now(timezone.utc).isoformat()
manifest = dict(
    recorded_utc=now, path=str(path.relative_to(root)),
    sha256=hashlib.sha256(promoted.encode()).hexdigest(),
    audited_candidate_sha256=candidate_hash, candidate_snapshot=str(snapshot.relative_to(root)),
    status='Proved',
    labels=['D:tame-detecting-curve-local-pairs', 'D:global-original-boundary-projective-growth', 'D:global-tame-projective-controlled-closure'],
    bibliography=None,
    audit_scope={actor:dict(record=record, scope='Complete actual candidate proof audited at the recorded SHA; exact original-source reading scope is in the audit. Promotion changes status/comment only.') for actor,record in audits.items()},
    promotion_changes='Three status headings and leading comment only; exact reversal verified.',
    scope=[
        'Fixed normal proper surfaces in characteristic p with arbitrary original closed boundary; tameness imposed only on its original codimension-one components.',
        'All q=p^f and ranks, unrestricted geometric Brauer period and exceptional wild images; fixed-pair constants only.',
        'Normal proper higher-dimensional pairs with finite boundary or the stated controlled-exceptional-centre modification; every defining-characteristic Lie simple-product quotient in this scope.'
    ],
    movement_classification='Enlargement of the same one global projective-gate reduction from finite punctures to arbitrary original surface boundary. Prerequisites and consequences are not counted separately.',
    open_scope='General D.1, general D.2(ii), residual L8, arbitrary-cover degree-linear hereditary constants, unrestricted alternating and uncovered cross-characteristic multiplicities, general nonabelian crowns, and higher-dimensional boundaries outside the proved reductions.',
    literature_scope='Known original inputs are cited with the exact opened locators and reading scopes recorded by the four auditors. No novelty or priority claim.')
out = directory / 'integration_manifest_root_global_original_boundary.json'
assert not out.exists()
out.write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps(dict(utc=now, manifest=str(out.relative_to(root)), sha256=manifest['sha256'], labels=manifest['labels']), indent=2))
