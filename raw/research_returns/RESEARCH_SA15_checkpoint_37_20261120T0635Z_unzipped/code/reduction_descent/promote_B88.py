from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib
own=Path(__file__).resolve().parents[1];work=own.parents[1]
stem='B_p5_full_image_ramification'
expected='59e1f80c1b6a5b1b269859c2b5bd7ab488771a008409d4c9760931cdf9293fab'
sha=lambda b:hashlib.sha256(b).hexdigest()
candidate=own/(stem+'_candidate.tex');raw=candidate.read_bytes();assert sha(raw)==expected
root=json.loads((work/'outputs/root_B88_audit.json').read_text())
oc=json.loads((own.parent/'obstructions_crystals/B88_independent_audit.json').read_text())
assert all('PASS' in r['status'] and r['candidate_sha256']==expected for r in (root,oc))
pre=own/('notes/'+stem+'.prepromotion.tex');assert not pre.exists();pre.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion audits passed.}',raw.decode())
s=s.replace(s.splitlines()[0],'% Proved necessary profile after complete root and companion audits; no realization or exclusion claim.',1)
para=('\n\\smallskip\n\\noindent\\emph{Independent audits.}\n'
      'The complete root and companion proof, source and code audits passed.\n'
      'Their literal author-output-preserving reruns took\n'
      f"\\({root['independent_runtime_seconds']}\\) and\n"
      f"\\({oc['independent_runtime_seconds']}\\) seconds, respectively.\n"
      'The exact audited candidate, full read scopes, code,\n'
      'outputs and promotion diff are retained.\n')
assert s.count(r'\end{remark}')==1;s=s.replace(r'\end{remark}',para+r'\end{remark}')
canonical=own/(stem+'.tex');assert not canonical.exists();canonical.write_text(s)
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert labels==root['labels']==oc['labels'] and len(labels)==3
now=datetime.now(timezone.utc).isoformat()
scope=('Necessary actual p5/e20 tame full-image profile: E1 lower(6,336), E2(24,234); '
       'full second-field upper6,24,66,72 and lower6,96,1146,1896; actual cyclotomic quotient breaks72overL,3overK. '
       'No impossibility or realization of the full image or a BT comparison is inferred.')
record={'status':'PROVED','promotion_utc':now,'canonical':str(canonical),
 'canonical_sha256':sha(canonical.read_bytes()),'audited_candidate_sha256':expected,
 'preserved_candidate':str(pre),'labels':labels,
 'root_audit':'../../outputs/root_B88_audit.json','root_audit_utc':root['actual_utc'],
 'root_runtime_seconds':root['independent_runtime_seconds'],
 'companion_audit':'../obstructions_crystals/B88_independent_audit.json',
 'companion_audit_utc':oc['actual_utc'],'companion_runtime_seconds':oc['independent_runtime_seconds'],
 'author_runtime_seconds':root['author_runtime_seconds'],'scope':scope,
 'source_scope':'Complete B87 actual point-field/coefficient proof; complete original Colmez2.12/3.7-3.10 and exact per-auditor scopes retained.',
 'checkpoint_scope':'CP31 canonical; prior checkpoints unchanged.','executed_failures':[]}
(own/'outputs/B88_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
(own/'notes/B88_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),s.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:f.write('\t'.join((now,label,'PROVED_FULL_AUDITS',scope,stem+'.tex;outputs/B88_promotion.json','Full root+OC proof/source/code audits; necessary profile only'))+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:f.write(f'\n## {now} — B88 promoted\n\n{scope}\n')
path=work/'code/consolidate.py';before=path.read_bytes();text=before.decode()
old="'B_p5_tame_full_first_layer.tex']:";new="'B_p5_tame_full_first_layer.tex',\n                    'B_p5_full_image_ramification.tex']:"
assert text.count(old)==1;after=text.replace(old,new)
for token in ('principal_theta_Cartier_bridge.tex','ppav_twisted_Cartier_Moore.tex','A4_common_Cartier_incidence.tex','ROOT_SEARCH_LOG_31.md'):assert token in after
history=own/'notes/CP31_before_B88_wiring';history.mkdir(exist_ok=False)
(history/path.name).write_bytes(before)
(history/(path.name+'.diff')).write_text(''.join(difflib.unified_diff(text.splitlines(True),after.splitlines(True),fromfile='consolidate.before',tofile='consolidate.after')))
path.write_text(after)
wiring={'status':'CONSOLIDATE_WIRED_NOT_BUILT','actual_utc':datetime.now(timezone.utc).isoformat(),
 'path':'code/consolidate.py','before_sha256':sha(before),'after_sha256':sha(path.read_bytes()),
 'prior_versions':str(history),'change':'B88 afterB87; all preceding A includes and LOG31 preserved.',
 'workflow_scope':'Parent owns CP31 prepare/update; no workflow edited.'}
(own/'outputs/B88_CP31_wiring.json').write_text(json.dumps(wiring,indent=2)+'\n')
print(json.dumps({'promotion':record,'wiring':wiring},indent=2))
