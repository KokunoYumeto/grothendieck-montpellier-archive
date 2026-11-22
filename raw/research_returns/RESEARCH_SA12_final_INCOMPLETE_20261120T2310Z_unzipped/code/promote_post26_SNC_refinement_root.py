"""Promote the exact four-audited SNC candidate by status changes only."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
rel = 'parts/D/post26_research/D_controlled_SNC_refinement_root.tex'
p = root / rel
candidate = p.read_bytes()
candidate_sha = hashlib.sha256(candidate).hexdigest()
assert candidate_sha == '58890bfe636388f2ade972484a6703277eef67ccbc781ab9afbdb8c233322d57'
records = {
    'root': 'parts/D/post26_research/audit_controlled_SNC_refinement_root.json',
    'B': 'parts/B/post26_research/audit_root_controlled_SNC_refinement_B.json',
    'C': 'parts/C/post26_research/audit_root_controlled_SNC_refinement_C.json',
    'D': 'parts/D/post26_research/audit_controlled_SNC_refinement_D.json',
}
audits = {}
for actor, record in records.items():
    a = json.loads((root / record).read_text())
    assert a['sha256'] == candidate_sha, actor
    assert a['verdict'] == 'PASS', actor
    audits[actor] = dict(record=record, scope='Complete actual saved statements, all proof paragraphs and scope remark, with all written primary proofs of Stacks 0AGQ/0AGR/0AGS read. Explicit source omission and recursively cited background remain Known.')
snapshot = 'parts/D/post26_research/D_controlled_SNC_refinement_root_audited.source.txt'
assert not (root / snapshot).exists()
(root / snapshot).write_bytes(candidate)
old_comment = '% Separate post-CP26 candidate. Root construction with B/D preliminary scrutiny; no main-gate movement.'
new_comment = '% Post-CP26 proved auxiliary refinement. Four full actual-file/source audits; no independent main-gate movement.'
text = candidate.decode()
assert text.startswith(old_comment) and text.count('[Candidate:') == 2
promoted = text.replace(old_comment, new_comment, 1).replace('[Candidate:', '[Proved:')
assert promoted.replace(new_comment, old_comment, 1).replace('[Proved:', '[Candidate:') == text
p.write_text(promoted)
bib = 'parts/D/post26_research/references_SNC_refinement_root.bib'
m = dict(
    recorded_utc=datetime.now(timezone.utc).isoformat(), path=rel,
    sha256=hashlib.sha256(p.read_bytes()).hexdigest(), bytes=p.stat().st_size,
    audited_candidate_sha256=candidate_sha, audited_candidate_snapshot=snapshot,
    labels=['D:linear-SNC-refinement-centres', 'D:SNC-refinement-inherited-cycles'],
    status='Proved', bibliography=bib,
    bibliography_sha256=hashlib.sha256((root / bib).read_bytes()).hexdigest(),
    new_bibliography_keys=['StacksSNCRefinementRoot'], audit_scope=audits,
    promotion_changes='Leading comment and two Candidate-to-Proved heading prefixes only; exact reversal verified.',
    exact_status_reversal_verified=True,
    scope='Every reduced proper curve on the stated regular excellent surface admits SNC refinement in at most 2delta+7G<=9G+2v-2c point blowups. Applied to the actual cover model this gives O_R(t) centres, components, nodes and normalization genus. Pullback of the old full Cartier cycles preserves all specified scalar/cohomological/ordinary-family budgets; the controlled centres also give the stated Jacobian inequality.',
    limitations='No unsigned adjacent-multiplicity product bound, uniformly controlled twisted anchor, hereditary projective count, canonical-fullness assertion after pullback, or arbitrary nonflat coefficient comparison.',
    movement='Auxiliary geometric clarification only. It is not an additional independent main-gate movement.',
    certificate=None, assembly_status='Ready for root integration.'
)
out = root / 'parts/D/post26_research/integration_manifest_controlled_SNC_refinement_root.json'
assert not out.exists()
out.write_text(json.dumps(m, indent=2) + '\n')
print(json.dumps(dict(manifest=str(out.relative_to(root)), sha256=m['sha256'], status='Proved')))
