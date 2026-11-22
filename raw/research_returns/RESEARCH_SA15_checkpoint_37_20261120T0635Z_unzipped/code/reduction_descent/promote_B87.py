from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib

own=Path(__file__).resolve().parents[1];work=own.parents[1]
stem='B_p5_tame_full_first_layer'
expected='ec7c365f216d6f8d5d44f86dab22bee217f6a7eac6ca96cba03a36b999361bf5'
candidate=own/(stem+'_candidate.tex');raw=candidate.read_bytes()
sha=lambda data:hashlib.sha256(data).hexdigest()
assert sha(raw)==expected
root=json.loads((work/'outputs/root_B87_audit.json').read_text())
oc=json.loads((own.parent/'obstructions_crystals/B87_independent_audit.json').read_text())
assert root['candidate_sha256']==oc['candidate_sha256']==expected
assert all('PASS' in a['status'] for a in (root,oc))
pre=own/('notes/'+stem+'.prepromotion.tex');assert not pre.exists();pre.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion audits passed.}',raw.decode())
s=s.replace(s.splitlines()[0],'% Proved after complete root and companion audits; exact candidate retained.',1)
para=('\n\\smallskip\n\\noindent\\emph{Independent audits.}\n'
      'The complete root and companion proof, source and code audits passed.\n'
      'Their literal author-output-preserving reruns took\n'
      f"\\({root['independent_runtime_seconds']}\\) and\n"
      f"\\({oc['independent_runtime_seconds']}\\) seconds, respectively.\n"
      'The exact audited candidate, per-auditor read scopes,\n'
      'all code and outputs, and the promotion diff are retained.\n')
assert s.count(r'\end{remark}')==1;s=s.replace(r'\end{remark}',para+r'\end{remark}')
canonical=own/(stem+'.tex');assert not canonical.exists();canonical.write_text(s)
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert labels==root['labels']==oc['labels'] and len(labels)==5
assert r'\status{Candidate' not in s
now=datetime.now(timezone.utc).isoformat()
scope=('At p5,e20, any different-special-character actual125 comparison with tame reducible residual '
       'inertia requires W1=W2=M2(F5), the full principal congruence image of order5^8, and mu25 notinK. '
       'The necessary B25/75,A/B pattern remains; no actual full-image realization/exclusion or other-sector conclusion.')
record={'status':'PROVED','promotion_utc':now,'canonical':str(canonical),
        'canonical_sha256':sha(canonical.read_bytes()),'audited_candidate_sha256':expected,
        'preserved_candidate':str(pre),'labels':labels,
        'root_audit':'../../outputs/root_B87_audit.json','root_audit_utc':root['actual_utc'],
        'root_runtime_seconds':root['independent_runtime_seconds'],
        'companion_audit':'../obstructions_crystals/B87_independent_audit.json',
        'companion_audit_utc':oc['actual_utc'],'companion_runtime_seconds':oc['independent_runtime_seconds'],
        'author_runtime_seconds':root['author_runtime_seconds'],'scope':scope,
        'source_scope':'Complete actual B84/B85/B60/B81 dependencies; exact per-auditor Serre/Colmez reading scopes retained without inflation.',
        'checkpoint_scope':'New canonical for CP31; immutable CP30 unchanged.','executed_failures':[]}
(own/'outputs/B87_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
(own/'notes/B87_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),s.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:
  f.write('\t'.join((now,label,'PROVED_FULL_AUDITS',scope,stem+'.tex;outputs/B87_promotion.json','Full root+OC proof/source/code scopes retained; no other-sector claim'))+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:f.write(f'\n## {now} — B87 promoted\n\n{scope}\n')

path=work/'code/consolidate.py';before=path.read_bytes();text=before.decode()
old="'B_first_wild_cyclotomic_quotient.tex']:"
new="'B_first_wild_cyclotomic_quotient.tex',\n                    'B_p5_tame_full_first_layer.tex']:"
assert text.count(old)==1
after=text.replace(old,new)
assert 'principal_theta_Cartier_bridge.tex' in after
history=own/'notes/CP31_before_B87_wiring';history.mkdir(exist_ok=False)
(history/path.name).write_bytes(before)
(history/(path.name+'.diff')).write_text(''.join(difflib.unified_diff(text.splitlines(True),after.splitlines(True),fromfile='consolidate.before',tofile='consolidate.after')))
path.write_text(after)
wiring={'status':'CONSOLIDATE_WIRED_NOT_BUILT','actual_utc':datetime.now(timezone.utc).isoformat(),
        'path':'code/consolidate.py','before_sha256':sha(before),'after_sha256':sha(path.read_bytes()),
        'prior_versions':str(history),'change':'B87 canonical after B86; all existing A includes preserved.',
        'workflow_scope':'No prepare/update workflow edited; parent owns CP31 requirements.'}
(own/'outputs/B87_CP31_wiring.json').write_text(json.dumps(wiring,indent=2)+'\n')
print(json.dumps({'promotion':record,'wiring':wiring},indent=2))
