from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

own=Path(__file__).resolve().parents[1]
work=own.parents[1]
source=own/'B_first_level_mixed_boundary_candidate.tex'
expected='d903ca018de6ac14e0bffa767ce664f0589b04448d0135a5c63404ca2832548c'
raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()==expected
root=json.loads((work/'outputs/root_B72_audit.json').read_text())
comp=json.loads((own.parent/'obstructions_crystals/B72_independent_audit.json').read_text())
for audit in (root,comp):
 assert audit['candidate_sha256']==expected and 'PASS' in audit['status']
preserved=own/'notes/B_first_level_mixed_boundary.prepromotion.tex'
assert not preserved.exists()
preserved.write_bytes(raw)
text=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; complete independent root and companion proof and exact-code audits passed.}',raw.decode())
text=text.replace('% Isolated post-CP26 candidate. No statement is promoted by the finite supplement.','% Proved after full root and companion audits; kept outside frozen CP26 paper.')
needle='provide a formal-group existence test.'
assert needle in text
text=text.replace(needle,needle+'\nThe complete independent root and companion audits passed.\nTheir author-output-preserving exact reruns took\n\\(0.5013780940062134\\) and \\(0.5564822399901459\\) seconds,\nrespectively. The exact audited candidate and complete audit\nrecords are preserved.')
canonical=own/'B_first_level_mixed_boundary.tex'
assert not canonical.exists()
canonical.write_text(text)
labels=re.findall(r'\\label\{([^}]+)\}',text)
assert len(labels)==6 and r'\status{Candidate' not in text
now=datetime.now(timezone.utc).isoformat()
record={
 'status':'PROVED', 'promotion_utc':now,
 'canonical':str(canonical),
 'canonical_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest(),
 'audited_candidate_sha256':expected, 'preserved_candidate':str(preserved),
 'labels':labels,
 'root_audit':'../../outputs/root_B72_audit.json',
 'root_audit_utc':root['actual_utc'],
 'root_runtime_seconds':root['independent_runtime_seconds'],
 'companion_audit':'../obstructions_crystals/B72_independent_audit.json',
 'companion_audit_utc':comp['actual_utc'],
 'companion_runtime_seconds':comp['elapsed_seconds'],
 'author_runtime_seconds':0.5185015480092261,
 'scope':'Exact full B4 nu_min(p,2(p^2-1),2)=2 for p>=5; combined tame sector2<=t<=2p+2,p not dividingt. p5/e48 settled; e52 and p-divisible indices not asserted.',
 'checkpoint_scope':'Late separate promotion for CP27. Frozen CP26 PDF, consolidation and required-source list unchanged.',
 'wiring_changes':[]
}
(own/'outputs/B72_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:
  f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',record['scope'],'B_first_level_mixed_boundary.tex;outputs/B72_promotion.json','Root and OC full proof/dependency/code PASS; exact candidate and all runtimes retained; no frozen CP26 wiring change'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:
 f.write(f'\n## {now} — B72 promoted after full audits\n\n'+record['scope']+' The strict first-level mixed break is exactly the information retained by the second actual quotient. This late promotion is separate from the frozen CP26 paper and is for CP27 integration. No executed numerical check failed.\n')
print(json.dumps(record,indent=2))
