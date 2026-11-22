from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, difflib

own=Path(__file__).resolve().parents[1]
work=own.parents[1]
stem='B_residual_wild_last_crossing'
expected='50a83a2885ff0a8fb79dfce8abdca45e142b4d1fb2224993830e8086f57bea04'
sha=lambda b:hashlib.sha256(b).hexdigest()
candidate=own/(stem+'_candidate.tex')
raw=candidate.read_bytes()
assert sha(raw)==expected
root_path=work/'outputs/root_B93_audit.json'
companion_path=own.parent/'obstructions_crystals/B93_independent_audit.json'
root=json.loads(root_path.read_text())
companion=json.loads(companion_path.read_text())
for audit in (root,companion):
    assert 'PASS' in audit['status'] and audit['candidate_sha256']==expected
    assert audit['author_bytes_unchanged'] and audit['all_mathematical_output_identical']
pre=own/('notes/'+stem+'.prepromotion.tex')
canonical=own/(stem+'.tex')
record_path=own/'outputs/B93_promotion.json'
assert not pre.exists() and not canonical.exists() and not record_path.exists()
pre.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion audits passed.}',raw.decode())
s=s.replace(s.splitlines()[0],'% Proved after complete root and companion audits; exact candidate retained.',1)
paragraph=(
    '\n\\smallskip\n\\noindent\\emph{Independent audits.}\n'
    'The complete root and companion proof and exact-code audits passed.\n'
    'Their literal author-output-preserving reruns took\n'
    f"\\({root['independent_runtime_seconds']}\\) and\n"
    f"\\({companion['independent_runtime_seconds']}\\) seconds, respectively.\n"
    'Both rederived the actual field stabilizers, all conductor restrictions\n'
    'and the degree-five normal-closure argument, after rereading the\n'
    'complete invoked internal proofs. The companion also freshly opened\n'
    'and read the full Cohen theorem and proof, and checked the original\n'
    'Colmez different, Herbrand and conductor proofs with the exact\n'
    'locators retained in its audit record. The root reused its prior\n'
    'full primary-source readings and claims no additional opening.\n'
    'The exact candidate, pre-promotion copy, full audit records, all\n'
    'programs and outputs, exploratory provenance and diff are retained.\n'
)
assert s.count(r'\end{remark}')==1
s=s.replace(r'\end{remark}',paragraph+r'\end{remark}')
canonical.write_text(s)
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert labels==root['labels']==companion['labels'] and len(labels)==5
now=datetime.now(timezone.utc).isoformat()
scope=('Actual original residual-wild crossing(5,45) is excluded by the same terminal determinant character: '
       'upper bounds275496/70296 contradict its lower391896. Together with B92 this removes all crossing rows. '
       'Remaining residual-wild cases have both parameters above20 and layer shapes(3,4)/(4,4); '
       'irreducible residual cases and unrestricted index{2,3} remain open.')
record={'status':'PROVED','promotion_utc':now,'canonical':str(canonical),
    'canonical_sha256':sha(canonical.read_bytes()),'audited_candidate_sha256':expected,
    'preserved_candidate':str(pre),'labels':labels,'scope':scope,
    'root_audit':str(root_path),'root_audit_utc':root['actual_utc'],
    'root_runtime_seconds':root['independent_runtime_seconds'],
    'companion_audit':str(companion_path),'companion_audit_utc':companion['actual_utc'],
    'companion_runtime_seconds':companion['independent_runtime_seconds'],
    'author_runtime_seconds':root['author_runtime_seconds'],
    'canonical_change_scope':'Status, leading provenance comment and exact independent-audit paragraph only; audited mathematics unchanged.',
    'source_scope':'Root prior full source readings reused; companion fresh Stacks032A full proof and exact original Colmez passages recorded in its complete audit. No author fresh original opening is claimed.',
    'checkpoint_scope':'Owned canonical promotion for CP34; shared include/config wiring waits OC release.',
    'executed_failures':[]}
record_path.write_text(json.dumps(record,indent=2)+'\n')
(own/'notes/B93_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),s.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join((now,label,'PROVED_FULL_AUDITS',scope,stem+'.tex;outputs/B93_promotion.json','Complete root and companion proof/code audits; exact author bytes preserved; source scopes separately recorded'))+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:
    f.write(f'\n## {now} — B93 promoted\n\n{scope}\n')
print(json.dumps(record,indent=2))
