from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

own=Path(__file__).resolve().parents[1]
work=own.parents[1]
source=own/'B_iterated_high_quotient_candidate.tex'
expected='30538d9b2588452cd20be474b5e9860994d37b91ba7cf257b8a2b389dfa32990'
raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()==expected
root=json.loads((work/'outputs/root_B74_audit.json').read_text())
comp=json.loads((own.parent/'obstructions_crystals/B74_independent_audit.json').read_text())
for audit in (root,comp):
    assert audit['candidate_sha256']==expected and 'PASS' in audit['status']
preserved=own/'notes/B_iterated_high_quotient.prepromotion.tex'
assert not preserved.exists()
preserved.write_bytes(raw)
t=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; complete independent root and companion proof and exact-code audits passed.}',raw.decode())
t=t.replace('% Separate post-B73 candidate; no promotion from the finite supplement.','% Proved after full independent root and companion audits; exact candidate preserved.')
needle='literature search.'
assert t.count(needle)==1
t=t.replace(needle,needle+r'''
The complete independent root and companion proof/code audits
passed. Their author-output-preserving exact reruns took
\(0.8197192030056613\) and \(0.8659103850077372\) seconds,
respectively. All five assertions, exact candidate bytes,
executed versions, and audit records are retained.''')
canonical=own/'B_iterated_high_quotient.tex'
assert not canonical.exists()
canonical.write_text(t)
labels=re.findall(r'\\label\{([^}]+)\}',t)
assert len(labels)==5 and r'\status{Candidate' not in t
now=datetime.now(timezone.utc).isoformat()
record={
    'status':'PROVED','promotion_utc':now,
    'canonical':str(canonical),
    'canonical_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest(),
    'audited_candidate_sha256':expected,
    'preserved_candidate':str(preserved),'labels':labels,
    'root_audit':'../../outputs/root_B74_audit.json',
    'root_audit_utc':root['actual_utc'],
    'root_runtime_seconds':root['independent_runtime_seconds'],
    'companion_audit':'../obstructions_crystals/B74_independent_audit.json',
    'companion_audit_utc':comp['actual_utc'],
    'companion_runtime_seconds':comp['elapsed_seconds'],
    'author_runtime_seconds':0.863016332994448,
    'scope':'Full B4 height-two upper nu_min<=n-1 for n>=3 and e<p^n, when p>=5, mu_p in K, perfect residue and p not dividing e. Exact nu_min=3 for p^3<e<p^4. The interval p^4<e<p^5 retains only bounds3..4; no wild absolute-index or higher-height claim.',
    'source_scope':'Previously fully audited B69/B71/B73/B63 source chain; no new external main-proof read claimed.',
    'checkpoint_scope':'Canonical ready for CP27. Global wiring is recorded separately to avoid a race with root build preparation.',
    'wiring_changes':[],
    'executed_failures':[],
    'successful_prior_checker':'code/verify_iterated_high_quotient.initial.py and .initial.output.json preserved; integer inequality rewritten without changing mathematical outputs.'
}
(own/'outputs/B74_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',record['scope'],'B_iterated_high_quotient.tex;outputs/B74_promotion.json','Root and OC complete independent proof/code PASS; exact level count and actual quotient construction; all versions/runtimes retained'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:
    f.write('\n## '+now+' — B74 promoted: iterated high quotients\n\n'+record['scope']+' For p=5, every permitted multiple of4 from128 through624 has exact index3; e628 is bounded3..4 and remains unresolved here. All quotient comparisons have the explicitly retained truncation level, with only p-torsion at the final stage.\n')
print(json.dumps(record,indent=2))
