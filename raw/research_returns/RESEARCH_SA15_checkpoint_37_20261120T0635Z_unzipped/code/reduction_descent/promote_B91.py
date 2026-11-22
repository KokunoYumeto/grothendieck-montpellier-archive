from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, difflib

own=Path(__file__).resolve().parents[1]
work=own.parents[1]
stem='B_residual_wild_high_quotient'
expected='a4cdbaf120302a26842df27c6eef3f428ff81cef454c573a314d3a476410c065'
sha=lambda b:hashlib.sha256(b).hexdigest()
candidate=own/(stem+'_candidate.tex')
raw=candidate.read_bytes()
assert sha(raw)==expected
root=json.loads((work/'outputs/root_B91_audit.json').read_text())
mono=json.loads((own.parent/'monodromy/outputs/independent_B91_residual_wild_high_quotient_audit.json').read_text())
assert 'PASS' in root['status'] and root['candidate_sha256']==expected
assert 'PASS' in mono['status'] and mono['candidate_sha256']==expected
pre=own/('notes/'+stem+'.prepromotion.tex')
assert not pre.exists()
pre.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion audits passed.}',raw.decode())
s=s.replace(s.splitlines()[0],'% Proved after complete root and monodromy audits; exact candidate retained.',1)
paragraph=(
    '\n\\smallskip\n\\noindent\\emph{Independent audits.}\n'
    'The complete root and monodromy proof and exact-code audits passed.\n'
    'Their literal author-output-preserving reruns took\n'
    f"\\({root['independent_runtime_seconds']}\\) and\n"
    f"\\({mono['program_runtime_seconds']}\\) seconds, respectively.\n"
    'Both reread the complete invoked B60, B69, B82, B84 and B86\n'
    'dependency proofs. No additional original-source opening is claimed.\n'
    'The exact audited candidate, pre-promotion copy, programs, outputs,\n'
    'two full audit records and promotion diff remain retained.\n'
)
assert s.count(r'\end{remark}')==1
s=s.replace(r'\end{remark}',paragraph+r'\end{remark}')
canonical=own/(stem+'.tex')
assert not canonical.exists()
canonical.write_text(s)
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert labels==root['labels']==mono['labels'] and len(labels)==5
now=datetime.now(timezone.utc).isoformat()
scope=('Residual-wild actual p^3 comparison at e=p(p-1): both Newton parameters are p-divisible. '
       'At p5/e20 crossing rows only (5,45)/(15,95); both-large original parameters force '
       'layer shapes (3,4)/(4,4), hence actual wild orders5^8/5^9. No crossing realization, '
       'full residual-wild exclusion, irreducible-residual change or least-index closure.')
record={
    'status':'PROVED','promotion_utc':now,'canonical':str(canonical),
    'canonical_sha256':sha(canonical.read_bytes()),'audited_candidate_sha256':expected,
    'preserved_candidate':str(pre),'labels':labels,'scope':scope,
    'root_audit':'../../outputs/root_B91_audit.json','root_audit_utc':root['actual_utc'],
    'root_runtime_seconds':root['independent_runtime_seconds'],
    'companion_audit':'../monodromy/outputs/independent_B91_residual_wild_high_quotient_audit.json',
    'companion_audit_utc':mono['actual_utc'],'companion_runtime_seconds':mono['program_runtime_seconds'],
    'author_runtime_seconds':root['author_runtime_seconds'],
    'canonical_change_scope':'Status, leading provenance comment and exact independent-audit paragraph only; mathematical candidate unchanged.',
    'checkpoint_scope':'CP33 input; immutable CP32 untouched. Shared wiring is a separate coordinated action.',
    'executed_failures':[]
}
(own/'outputs/B91_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
(own/'notes/B91_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),s.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join((now,label,'PROVED_FULL_AUDITS',scope,stem+'.tex;outputs/B91_promotion.json','Complete root and monodromy proof/code audits; exact author bytes preserved'))+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:
    f.write(f'\n## {now} — B91 promoted\n\n{scope}\n')
print(json.dumps(record,indent=2))
