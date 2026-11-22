from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib
own=Path(__file__).resolve().parents[1];work=own.parents[1]
candidate=own/'B_tame_residual_one_prime_recovery_candidate.tex';raw=candidate.read_bytes()
expected='f08414cd26b408769ae16b0fcead57b758ea5e14df2569d396f077834f2950e9'
assert hashlib.sha256(raw).hexdigest()==expected
root=json.loads((work/'outputs/root_B84_audit.json').read_text())
oc=json.loads((own.parent/'obstructions_crystals/B84_independent_audit.json').read_text())
assert root['candidate_sha256']==oc['candidate_sha256']==expected
assert all('PASS' in a['status'] for a in (root,oc))
pre=own/'notes/B_tame_residual_one_prime_recovery.prepromotion.tex'
assert not pre.exists();pre.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion proof and exact-code audits passed.}',raw.decode())
s=s.replace('% Separate post-CP29 candidate; no unrestricted first-wild least-index claim.',
            '% Proved after CP29; no unrestricted first-wild least-index claim.')
needle='claimed.\n\\end{remark}'
assert s.count(needle)==1
s=s.replace(needle,r'''claimed.
The complete independent root and companion proof and code
audits passed; their author-output-preserving reruns took
\(0.11858891700103413\) and
\(0.11411567399045452\) seconds, respectively.
Both exact audit records and the prior candidate remain
retained. The earlier exploratory parameter rows are
preserved as superseded research, without a retroactive
claim that the current argument had already been known.
\end{remark}''')
canonical=own/'B_tame_residual_one_prime_recovery.tex';assert not canonical.exists()
canonical.write_text(s)
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert labels==root['labels']==oc['labels'] and len(labels)==3
assert r'\status{Candidate' not in s
now=datetime.now(timezone.utc).isoformat()
scope=('For arbitrary e and L-rational first-level modules, actual p2 comparison recovers both high lines, '
       'Newton parameters and finite characters whenever at least one b is prime to p. At p5,e20, '
       'the residual-tame necessary pattern at every image size is B25/75,A/B up to common quadratic twist. '
       'No pair existence or exact first-wild index is claimed.')
record={'status':'PROVED','promotion_utc':now,'canonical':str(canonical),
        'canonical_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest(),
        'audited_candidate_sha256':expected,'preserved_candidate':str(pre),'labels':labels,
        'root_audit':'../../outputs/root_B84_audit.json','root_audit_utc':root['actual_utc'],
        'root_runtime_seconds':root['independent_runtime_seconds'],
        'companion_audit':'../obstructions_crystals/B84_independent_audit.json',
        'companion_audit_utc':oc['actual_utc'],'companion_runtime_seconds':oc['independent_runtime_seconds'],
        'author_runtime_seconds':0.12348706599732395,'scope':scope,
        'source_scope':'Complete internal inverse-polygon, fixed-coefficient and finite determinant bridges as specified in both audit records; no new original-source read.',
        'checkpoint_scope':'Post-review20 canonical for CP30; immutable CP29 unchanged.',
        'executed_failures':[]}
(own/'outputs/B84_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
(own/'notes/B84_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),s.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',scope,
                          'B_tame_residual_one_prime_recovery.tex;outputs/B84_promotion.json',
                          'Full root+OC proof/code audits; exact candidate and promotion diff retained'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:
    f.write('\n## '+now+' — B84 promoted: one-prime point-field recovery\n\n'+scope+'\n')
history=own/'notes/CP30_before_B84_wiring';assert not history.exists();history.mkdir()
path=work/'code/consolidate.py';before=path.read_bytes();text=before.decode()
old="'B_first_wild_swapped_quotients.tex']:"
new="'B_first_wild_swapped_quotients.tex',\n                    'B_tame_residual_one_prime_recovery.tex']:"
assert text.count(old)==1;after=text.replace(old,new)
oldlog=r'\\path{notes/ROOT_SEARCH_LOG_28.md}'
newlog=oldlog+'\n'+r'\\path{notes/ROOT_SEARCH_LOG_29.md}'+'\n'+r'\\path{notes/ROOT_SEARCH_LOG_30.md}'
assert after.count(oldlog)==1
assert (work/'notes/ROOT_SEARCH_LOG_29.md').exists() and (work/'notes/ROOT_SEARCH_LOG_30.md').exists()
after=after.replace(oldlog,newlog)
(history/path.name).write_bytes(before)
(history/(path.name+'.diff')).write_text(''.join(difflib.unified_diff(text.splitlines(True),after.splitlines(True),fromfile='consolidate.before',tofile='consolidate.after')))
path.write_text(after)
wiring={'status':'CONSOLIDATE_WIRED_NOT_BUILT','actual_utc':datetime.now(timezone.utc).isoformat(),
        'path':'code/consolidate.py','before_sha256':hashlib.sha256(before).hexdigest(),
        'after_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'prior_versions':str(history),'changes':['B84 canonical after B83','F.2 search logs29 and30 appended after28'],
        'workflow_scope':'Parent owns prepare/update workflows; neither edited.'}
(own/'outputs/B84_CP30_wiring.json').write_text(json.dumps(wiring,indent=2)+'\n')
print(json.dumps({'promotion':record,'wiring':wiring},indent=2))
