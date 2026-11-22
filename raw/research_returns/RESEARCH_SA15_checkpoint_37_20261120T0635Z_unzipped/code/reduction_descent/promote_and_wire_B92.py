from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, difflib

own=Path(__file__).resolve().parents[1]
work=own.parents[1]
stem='B_residual_wild_crossing'
expected='54786c9ec226ed8855471c5c4eacaa5efd2927ec3aefee76aa9762bd5c221453'
sha=lambda b:hashlib.sha256(b).hexdigest()
candidate=own/(stem+'_candidate.tex')
raw=candidate.read_bytes()
assert sha(raw)==expected
root=json.loads((work/'outputs/root_B92_audit.json').read_text())
mono_path=own.parent/'monodromy/outputs/independent_B92_residual_wild_crossing_audit.json'
mono=json.loads(mono_path.read_text())
assert 'PASS' in root['status'] and root['candidate_sha256']==expected
assert 'PASS' in mono['status'] and mono['candidate_sha256']==expected
pre=own/('notes/'+stem+'.prepromotion.tex')
canonical=own/(stem+'.tex')
record_path=own/'outputs/B92_promotion.json'
assert not pre.exists() and not canonical.exists() and not record_path.exists()
pre.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion audits passed.}',raw.decode())
s=s.replace(s.splitlines()[0],'% Proved after complete root and monodromy audits; exact candidate retained.',1)
paragraph=(
    '\n\\smallskip\n\\noindent\\emph{Independent audits.}\n'
    'The complete root and monodromy proof and exact-code audits passed.\n'
    'Their literal author-output-preserving reruns took\n'
    f"\\({root['independent_runtime_seconds']}\\) and\n"
    f"\\({mono['program_runtime_seconds']}\\) seconds, respectively.\n"
    'Both reread the full actual B87 and B88 coefficient and point-field\n'
    'proofs and verified that precisely their actual 25-level statements\n'
    'are used here. The invoked earlier quotient and fixed-coefficient\n'
    'arguments were also rechecked. No fresh external original-source\n'
    'opening is claimed. The exact candidate, pre-promotion copy,\n'
    'programs, outputs, full audit records and promotion diff are retained.\n'
)
assert s.count(r'\end{remark}')==1
s=s.replace(r'\end{remark}',paragraph+r'\end{remark}')
canonical.write_text(s)
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert labels==root['labels']==mono['labels'] and len(labels)==5
now=datetime.now(timezone.utc).isoformat()
scope=('The actual quotient25 comparison has full first image and four coordinate cyclic breaks; '
       'both residual-wild crossings have full parahoric order5^8. The actual diagonal field excludes '
       '(15,95), leaving (5,45). Both-large and irreducible residual sectors are unchanged; '
       'no surviving-row realization or unrestricted least-index closure.')
record={'status':'PROVED','promotion_utc':now,'canonical':str(canonical),
    'canonical_sha256':sha(canonical.read_bytes()),'audited_candidate_sha256':expected,
    'preserved_candidate':str(pre),'labels':labels,'scope':scope,
    'root_audit':'../../outputs/root_B92_audit.json','root_audit_utc':root['actual_utc'],
    'root_runtime_seconds':root['independent_runtime_seconds'],
    'companion_audit':str(mono_path),'companion_audit_utc':mono['actual_utc'],
    'companion_runtime_seconds':mono['program_runtime_seconds'],
    'author_runtime_seconds':root['author_runtime_seconds'],
    'canonical_change_scope':'Status, leading provenance comment and independent-audit paragraph only; mathematics unchanged.',
    'executed_failures':[]}
record_path.write_text(json.dumps(record,indent=2)+'\n')
(own/'notes/B92_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),s.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join((now,label,'PROVED_FULL_AUDITS',scope,stem+'.tex;outputs/B92_promotion.json','Complete root and monodromy proof/code audits; exact author bytes preserved'))+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:
    f.write(f'\n## {now} — B92 promoted\n\n{scope}\n')

history=own/'notes/CP33_before_B92_wiring'
history.mkdir(exist_ok=False)
conso=work/'code/consolidate.py'
config=work/'notes/checkpoint33_promoted_inputs.json'
before=conso.read_text()
needle="                    'B_residual_wild_high_quotient.tex']:"
assert before.count(needle)==1 and "'B_residual_wild_crossing.tex'" not in before
after=before.replace(needle,"                    'B_residual_wild_high_quotient.tex',\n                    'B_residual_wild_crossing.tex']:")
changes=[]
for path,old,new in [(conso,before,after)]:
    (history/path.name).write_text(old)
    path.write_text(new)
    (history/(path.name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=str(path)+':before',tofile=str(path)+':after')))
    changes.append({'path':str(path),'before_sha256':sha(old.encode()),'after_sha256':sha(path.read_bytes())})
old=config.read_text()
items=json.loads(old)
new_path='agents/reduction_descent/B_residual_wild_crossing.tex'
assert new_path not in items
items.append(new_path)
new=json.dumps(items,indent=2)+'\n'
(history/config.name).write_text(old)
config.write_text(new)
(history/(config.name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=str(config)+':before',tofile=str(config)+':after')))
changes.append({'path':str(config),'before_sha256':sha(old.encode()),'after_sha256':sha(config.read_bytes())})
compile(conso.read_text(),str(conso),'exec')
wiring={'status':'WIRED','actual_utc':datetime.now(timezone.utc).isoformat(),'canonical':str(canonical),'canonical_sha256':sha(canonical.read_bytes()),'changes':changes,'scope':'One late-B include and one CP33 required path, preserving B91 and all A4 additions; no build, bibliography, report or immutable checkpoint change.','history':str(history)}
(own/'outputs/B92_CP33_wiring.json').write_text(json.dumps(wiring,indent=2)+'\n')
print(json.dumps({'promotion':record,'wiring':wiring},indent=2))
