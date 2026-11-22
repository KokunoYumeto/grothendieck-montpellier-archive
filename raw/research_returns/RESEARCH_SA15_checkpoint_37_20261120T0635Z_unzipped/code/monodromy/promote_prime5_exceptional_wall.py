"""Owned-file promotion only; parent explicitly reserved shared integration."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, difflib, re

agent=Path(__file__).resolve().parents[1]
root=agent.parents[1]
candidate=agent/'post_CP36_prime5_exceptional_wall_candidate.tex'
canonical=agent/'prime5_exceptional_wall.tex'
expected='5d949110f65325c83cbf986fd0b29ae017eebf64eff9bc79d305b4cb861e22ef'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate)==expected and not canonical.exists()
root_audit=root/'outputs/root_prime5_exceptional_wall_audit.json'
oc_audit=root/'agents/obstructions_crystals/prime5_exceptional_wall_independent_audit.json'
ra=json.loads(root_audit.read_text()); oa=json.loads(oc_audit.read_text())
assert 'PASS' in ra['status'] and 'PASS' in oa['status']
assert ra['input_sha256'][str(candidate.relative_to(root))]==expected
assert oa['candidate_sha256']==expected
before=candidate.read_text()
after,count=re.subn(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; independent audits passed.}',before)
assert count==3
after=after.replace('% Isolated post-freeze diagnostic candidate; no canonical assertion yet.',
                    '% Promoted abstract scope guard after full independent proof/code audits.')
after=after.replace('The current checkpoint inputs are\nunchanged and this note is unpromoted.',
    'The complete independent parent audit passed at 05:58:07.826322 UTC,\n'
    'with an unchanged isolated checker run of \\(0.0048347230040235445\\)\n'
    'seconds. The complete independent obstruction/crystal audit passed at\n'
    '05:56:06.345318 UTC, with an unchanged isolated run of\n'
    '\\(0.004974707000656053\\) seconds. Both reruns preserved the author\n'
    'artifacts and reproduced every mathematical output field. Promotion\n'
    'records only this abstract obstruction; it supplies no new geometric\n'
    'monodromy case.')
history=agent/'notes/CP37_prime5_exceptional_wall_promotion'
history.mkdir(exist_ok=False)
(history/'candidate.tex').write_text(before)
(history/'promotion.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
canonical.write_text(after)
now=datetime.now(timezone.utc).isoformat()
labels=re.findall(r'\\label\{([^}]+)\}',before)
scope='Abstract prime-five Heisenberg exceptional ratios t^5=1 have both generic ranks four and a birational radical but empty common maximal-rank Euler wall. No actual Cartier realization or full-monodromy consequence is inferred.'
record={'status':'PROMOTED_OWNED_FILES_ONLY','actual_utc':now,'candidate':str(candidate.relative_to(root)),'candidate_sha256':expected,'canonical':str(canonical.relative_to(root)),'canonical_sha256':sha(canonical),'labels':labels,'audits':[str(root_audit.relative_to(root)),str(oc_audit.relative_to(root))],'scope':scope,'shared_files_modified':False,'new_computation_at_promotion':False}
(agent/'outputs/prime5_exceptional_wall_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (agent/'CHECK_EVENTS_post_CP16.tsv').open('a') as f:
    for label in labels:f.write('\t'.join([label,now,'/root/monodromy','PROMOTED-ROOT-OC-FULL-PROOF-CODE-PASS',scope])+'\n')
assert sha(candidate)==expected
print(json.dumps(record,indent=2))
