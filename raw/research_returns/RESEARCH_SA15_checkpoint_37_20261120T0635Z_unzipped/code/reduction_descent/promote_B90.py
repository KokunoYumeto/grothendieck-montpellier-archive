from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib
own=Path(__file__).resolve().parents[1];work=own.parents[1]
stem='B_p5_third_point_ramification'
expected='915d0471127a83c19d45fdefcd7696c92fedc5571e5785d3734e85fafaa732bd'
sha=lambda b:hashlib.sha256(b).hexdigest()
candidate=own/(stem+'_candidate.tex');raw=candidate.read_bytes();assert sha(raw)==expected
root=json.loads((work/'outputs/root_B90_audit.json').read_text())
mono=json.loads((own.parent/'monodromy/outputs/independent_B90_third_point_ramification_audit.json').read_text())
assert root['status']=='PASS' and root['candidate_sha256']==expected
assert 'PASS' in mono['status'] and mono['source_sha256']==expected
pre=own/('notes/'+stem+'.prepromotion.tex');assert not pre.exists();pre.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion audits passed.}',raw.decode())
s=s.replace(s.splitlines()[0],'% Proved after full root and companion audits; exact actual-field candidate retained.',1)
old=r'\cite[Propositions 3.7--3.10, pp.~14--16]'
new=r'\cite[Proposition 3.7, Theorem 3.10 and Proposition 3.13(ii), full proofs, pp.~14--16]'
assert s.count(old)==1;s=s.replace(old,new)
paragraph=('\n\\smallskip\n\\noindent\\emph{Independent audits.}\n'
 'The complete root and monodromy proof and exact-code audits passed.\n'
 'Their literal author-output-preserving reruns took\n'
 f"\\({root['independent_runtime_seconds']}\\) and\n"
 f"\\({mono['exact_program_runtime_seconds']}\\) seconds, respectively.\n"
 'The root subsequently reread the original Colmez proofs through\n'
 'Proposition 3.13 and retained a separate source addendum. The canonical\n'
 'citation names Proposition 3.7, Theorem 3.10 and Proposition 3.13(ii)\n'
 'precisely; this corrects only the candidate\'s bibliographic labels.\n'
 'The exact candidate, source scopes, code, outputs and promotion diff\n'
 'remain retained.\n')
assert s.count(r'\end{remark}')==1;s=s.replace(r'\end{remark}',paragraph+r'\end{remark}')
canonical=own/(stem+'.tex');assert not canonical.exists();canonical.write_text(s)
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert labels==root['labels']==[a['label']for a in mono['assertions']] and len(labels)==4
now=datetime.now(timezone.utc).isoformat()
scope=('Actual third-level point fields exclude the whole tame reducible residual '
       'different-special-character125 comparison at p5/e20. Exact determinant coset '
       'average1896/5 is impossible. Irreducible-residual and nontrivial-residual-wild '
       'sectors remain open; unrestricted least-index interval stays{2,3}.')
record={'status':'PROVED','promotion_utc':now,'canonical':str(canonical),
 'canonical_sha256':sha(canonical.read_bytes()),'audited_candidate_sha256':expected,
 'preserved_candidate':str(pre),'labels':labels,'scope':scope,
 'root_audit':'../../outputs/root_B90_audit.json','root_audit_utc':root['actual_utc'],
 'root_runtime_seconds':root['independent_runtime_seconds'],
 'companion_audit':'../monodromy/outputs/independent_B90_third_point_ramification_audit.json',
 'companion_audit_utc':mono['actual_utc'],'companion_runtime_seconds':mono['exact_program_runtime_seconds'],
 'author_runtime_seconds':root['author_runtime_seconds'],
 'source_addendum':'../../outputs/root_B90_source_addendum.json',
 'canonical_only_correction':'Bibliographic labels: Proposition3.7, Theorem3.10, Proposition3.13(ii); no mathematical change.',
 'checkpoint_scope':'CP32 input; immutable CP31 unchanged.','executed_failures':[]}
(own/'outputs/B90_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
(own/'notes/B90_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),s.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
with(own/'CHECK_EVENTS.tsv').open('a')as f:
 for label in labels:f.write('\t'.join((now,label,'PROVED_FULL_AUDITS',scope,stem+'.tex;outputs/B90_promotion.json','Full root+mono audits; canonical citation correction only'))+'\n')
with(own/'STATUS_CURRENT.md').open('a')as f:f.write(f'\n## {now} — B90 promoted\n\n{scope}\n')
path=work/'code/consolidate.py';before=path.read_bytes();text=before.decode()
old="'B_p5_cyclotomic_break_three_example.tex']:"
new="'B_p5_cyclotomic_break_three_example.tex',\n                    'B_p5_third_point_ramification.tex']:"
assert text.count(old)==1;after=text.replace(old,new)
history=own/'notes/CP32_before_B90_wiring';history.mkdir(exist_ok=False)
(history/path.name).write_bytes(before)
(history/(path.name+'.diff')).write_text(''.join(difflib.unified_diff(text.splitlines(True),after.splitlines(True),fromfile='consolidate.before',tofile='consolidate.after')))
path.write_text(after)
wiring={'status':'CONSOLIDATE_WIRED_NOT_BUILT','actual_utc':datetime.now(timezone.utc).isoformat(),
 'path':'code/consolidate.py','before_sha256':sha(before),'after_sha256':sha(path.read_bytes()),
 'prior_versions':str(history),'change':'One B90 include immediately after B89; no other content changed.',
 'workflow_scope':'Parent owns CP32 prepare/update; no workflow or bibliography edited.'}
(own/'outputs/B90_CP32_wiring.json').write_text(json.dumps(wiring,indent=2)+'\n')
print(json.dumps({'promotion':record,'wiring':wiring},indent=2))
