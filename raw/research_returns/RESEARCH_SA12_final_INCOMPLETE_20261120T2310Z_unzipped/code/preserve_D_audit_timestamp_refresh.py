"""Preserve a metadata refresh and restore exact original audit creation records."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json

root=Path(__file__).resolve().parents[1]
last=json.loads((root/'code/output/root_review21_last_research_scope.json').read_text())
expected={x['path']:x['sha256'] for x in last['two_end_exact_audit_records']}
paths=[
    'parts/D/post29_research/audit_C_two_end_pair_coefficient_gerbe_D.json',
    'parts/D/post29_research/weighted_SNC_source_and_author_scope_D.json'
]
changes=[]
for rel in paths:
    p=root/rel
    refreshed=p.read_bytes()
    a=json.loads(refreshed)
    original_utc=a.pop('executor_wall_utc_at_record_creation')
    reported_scope=a.pop('timestamp_scope')
    refresh_utc=a['utc']
    a['utc']=original_utc
    original=(json.dumps(a,indent=2)+'\n').encode()
    original_sha=hashlib.sha256(original).hexdigest()
    if rel in expected:
        assert original_sha==expected[rel], 'Original exact audit bytes do not reconstruct.'
    snapshot=p.with_name(p.stem+'_timestamp_refresh_230407.source.txt')
    assert not snapshot.exists()
    snapshot.write_bytes(refreshed)
    p.write_bytes(original)
    changes.append(dict(path=rel,refresh_snapshot=str(snapshot.relative_to(root)),
                        refreshed_sha256=hashlib.sha256(refreshed).hexdigest(),
                        restored_original_sha256=original_sha,original_creation_utc=original_utc,
                        refresh_utc=refresh_utc,reported_timestamp_scope=reported_scope,
                        known_prior_hash_verified=rel in expected,
                        proof_and_verdict_unchanged=True))
record={
    'utc':datetime.now(timezone.utc).isoformat(),'actor':'root',
    'kind':'Exact preservation and reconciliation of audit timestamp metadata',
    'changes':changes,
    'observed_clock':dict(clock_tool='2026-11-20 23:04:53 UTC',executor_utc='2026-11-20T23:04:53.772549+00:00'),
    'reason':'The root clock and executor reading agreed in the same tool call. Original creation times and a later refresh time alone do not establish clock skew. The refreshed records are preserved verbatim, and original creation-time records are restored without changing any proof, source scope or verdict. The C-note audit reconstructs to the exact hash already recorded by root.',
    'timing_scope':'No formal review, scheduled archive, manuscript or check-event timestamp is changed.',
    'movement':False
}
out=root/'code/output/D_audit_timestamp_refresh_reconciliation.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'record':str(out.relative_to(root)),'restored_records':len(changes),'known_prior_C_audit_hash':'PASS','movement':False}))
