from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib

own=Path(__file__).resolve().parents[1];work=own.parents[1]
candidate=own/'B_first_wild_reducible_terminal_candidate.tex';raw=candidate.read_bytes()
expected='594f019abab5cd378c489671f7ff021c7e0e446ac53166f696dafa035f0f761b'
assert hashlib.sha256(raw).hexdigest()==expected
root=json.loads((work/'outputs/root_B82_audit.json').read_text())
oc=json.loads((own.parent/'obstructions_crystals/B82_independent_audit.json').read_text())
delta=json.loads((own.parent/'obstructions_crystals/B82_determinant_delta_audit.json').read_text())
assert root['candidate_sha256']==delta['candidate_sha256']==expected
assert oc['candidate_sha256']==delta['prior_candidate_sha256']
assert all('PASS' in a['status'] for a in (root,oc,delta))
pre=own/'notes/B_first_wild_reducible_terminal.prepromotion.tex'
assert not pre.exists();pre.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion proof and exact-code audits passed.}',raw.decode())
s=s.replace('% Separate post-CP29-build candidate; no change to the frozen current gate.',
            '% Proved after CP29 archive release; exact audited candidates retained.')
needle='were reread. No new original-source read is claimed.'
assert s.count(needle)==1
s=s.replace(needle,needle+r'''
The complete independent root and companion audits passed;
their author-output-preserving reruns took
\(0.3949265940027544\) and \(0.39488881299621426\) seconds,
respectively. Both auditors also checked the exact final
determinant simplification, which removes an unnecessary
square-character case split and finite twist without changing
the statement or certificate. Both source versions, the exact
diff, and all audit records remain retained. No additional
source reading or redundant rerun is claimed for that delta.''')
canonical=own/'B_first_wild_reducible_terminal.tex';assert not canonical.exists()
canonical.write_text(s)
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert labels==root['labels']==oc['labels'] and len(labels)==5
assert r'\status{Candidate' not in s
now=datetime.now(timezone.utc).isoformat()
scope=('At first wild e=p(p-1), actual p3 comparison with two slopes, wild order p4 and one B=pb '
       'with p not dividing b recovers the high line and finite character. A different-character '
       'comparison with nontrivial residual wild inertia must have wild order p^r,5<=r<=9. '
       'Residual-tame exchanged high lines and larger images remain open; full index stays{2,3}.')
record={'status':'PROVED','promotion_utc':now,'canonical':str(canonical),
        'canonical_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest(),
        'audited_candidate_sha256':expected,'preserved_candidate':str(pre),'labels':labels,
        'root_audit':'../../outputs/root_B82_audit.json','root_audit_utc':root['actual_utc'],
        'root_runtime_seconds':root['independent_runtime_seconds'],
        'companion_audit':'../obstructions_crystals/B82_independent_audit.json',
        'companion_audit_utc':oc['actual_utc'],'companion_runtime_seconds':oc['independent_runtime_seconds'],
        'companion_delta_audit':'../obstructions_crystals/B82_determinant_delta_audit.json',
        'companion_delta_utc':delta['actual_utc'],
        'author_runtime_seconds':0.42271842100308277,'scope':scope,
        'source_scope':'Complete internal B49/B60/B69 coefficient, break and line-character arguments; no fresh original-source claim.',
        'checkpoint_scope':'Post-CP29 canonical for CP30; immutable CP29 unchanged.',
        'executed_failures':[]}
(own/'outputs/B82_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',scope,
                          'B_first_wild_reducible_terminal.tex;outputs/B82_promotion.json',
                          'Full root+OC proof/code audits and exact determinant delta; all versions retained'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:
    f.write('\n## '+now+' — B82 promoted: residual-wild terminal matrices\n\n'+scope+'\n')
history=own/'notes/CP30_before_B82_wiring';assert not history.exists();history.mkdir()
path=work/'code/consolidate.py';before=path.read_bytes();text=before.decode()
old="'B_first_wild_Cartan_exclusion.tex']:"
new="'B_first_wild_Cartan_exclusion.tex',\n                    'B_first_wild_reducible_terminal.tex']:"
assert text.count(old)==1;after=text.replace(old,new)
(history/path.name).write_bytes(before)
(history/(path.name+'.diff')).write_text(''.join(difflib.unified_diff(
    text.splitlines(True),after.splitlines(True),fromfile='consolidate.before',tofile='consolidate.after')))
path.write_text(after)
wiring={'status':'CONSOLIDATE_WIRED_NOT_BUILT','actual_utc':datetime.now(timezone.utc).isoformat(),
        'path':'code/consolidate.py','before_sha256':hashlib.sha256(before).hexdigest(),
        'after_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'prior_versions':str(history),'prepare30':'Coordinate required canonical with OC; not changed here.'}
(own/'outputs/B82_CP30_wiring.json').write_text(json.dumps(wiring,indent=2)+'\n')
print(json.dumps({'promotion':record,'wiring':wiring},indent=2))
