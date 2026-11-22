from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib

own=Path(__file__).resolve().parents[1];work=own.parents[1]
candidate=own/'B_first_wild_swapped_quotients_candidate.tex';raw=candidate.read_bytes()
expected='453ca8011e454fcb1360ccf27195d7b8a5db633d6383cd3048a9bae8d9b83d40'
assert hashlib.sha256(raw).hexdigest()==expected
root=json.loads((work/'outputs/root_B83_audit.json').read_text())
oc=json.loads((own.parent/'obstructions_crystals/B83_independent_audit.json').read_text())
assert root['candidate_sha256']==oc['candidate_sha256']==expected
assert all('PASS' in a['status'] for a in (root,oc))
pre=own/'notes/B_first_wild_swapped_quotients.prepromotion.tex'
assert not pre.exists();pre.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion proof and exact-code audits passed.}',raw.decode())
s=s.replace('% Separate post-CP29 candidate; no exact first-wild least-index claim.',
            '% Proved after CP29 archive; no exact first-wild least-index claim.')
needle='These finite checks establish no formal-group\nexistence and do not replace the uniform proofs.'
assert s.count(needle)==1
s=s.replace(needle,needle+r'''
The complete independent root and companion proof and code
audits both passed. Their author-output-preserving reruns
took \(0.3534236279956531\) and
\(0.3482199970021611\) seconds, respectively. Both
auditors checked the actual quotient lattice direction,
the common point fields, and the same original first
congruence layer before applying its tame weight
projectors. Their exact read scopes, all prior proof
versions and the complete outputs remain retained.''')
canonical=own/'B_first_wild_swapped_quotients.tex';assert not canonical.exists()
canonical.write_text(s)
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert labels==root['labels']==oc['labels'] and len(labels)==5
assert r'\status{Candidate' not in s
now=datetime.now(timezone.utc).isoformat()
scope=('At first wild e=p(p-1), actual exchanged-high quotients force both opposite original W1 entries. '
       'For p=1 mod4, nonsquare determinant separates tame weights and actual commutators force wild order>=p^5. '
       'Together with B81/B82, every p5,e20,125-torsion failure has wild image at least3125; larger images and full index{2,3} remain open.')
record={'status':'PROVED','promotion_utc':now,'canonical':str(canonical),
        'canonical_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest(),
        'audited_candidate_sha256':expected,'preserved_candidate':str(pre),'labels':labels,
        'root_audit':'../../outputs/root_B83_audit.json','root_audit_utc':root['actual_utc'],
        'root_runtime_seconds':root['independent_runtime_seconds'],
        'companion_audit':'../obstructions_crystals/B83_independent_audit.json',
        'companion_audit_utc':oc['actual_utc'],'companion_runtime_seconds':oc['independent_runtime_seconds'],
        'author_runtime_seconds':0.3601258019916713,'scope':scope,
        'source_scope':'Exact internal B69 quotient/point-field proof freshly reread; other dependencies as specified in the two audits. No new original-source read.',
        'checkpoint_scope':'Post-CP29 canonical for CP30; immutable CP29 unchanged.',
        'executed_failures':[]}
(own/'outputs/B83_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
(own/'notes/B83_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),s.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',scope,
                          'B_first_wild_swapped_quotients.tex;outputs/B83_promotion.json',
                          'Full root+OC proof/code audits; candidate and exact promotion diff retained'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:
    f.write('\n## '+now+' — B83 promoted: actual opposite quotients\n\n'+scope+'\n')
print(json.dumps(record,indent=2))
