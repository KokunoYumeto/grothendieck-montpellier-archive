from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

own = Path(__file__).resolve().parents[1]
work = own.parents[1]
source = own/'B_rational_high_line_candidate.tex'
expected = '5709f274bd7c897ade3b817505570dec37a8a6cfe3c1acdeb368087e2bfad040'
raw = source.read_bytes()
assert hashlib.sha256(raw).hexdigest() == expected
root = json.loads((work/'outputs/root_B73_audit.json').read_text())
comp = json.loads((own.parent/'obstructions_crystals/B73_independent_audit.json').read_text())
for audit in (root, comp):
    assert audit['candidate_sha256'] == expected and 'PASS' in audit['status']
preserved = own/'notes/B_rational_high_line.prepromotion.tex'
assert not preserved.exists()
preserved.write_bytes(raw)
text = re.sub(r'\\status\{Candidate[^}]*\}', lambda _:r'\status{Proved; complete independent root and companion proof and exact-code audits passed.}', raw.decode())
text = text.replace('% Isolated post-CP26 candidate. Full proofs precede the finite supplement.', '% Proved after full independent root and companion audits; exact candidate preserved.')
needle = 'mixed-threshold dependencies indicated above.'
assert needle in text
text = text.replace(needle, needle+r'''
The independent root and companion audits passed for all six
assertions and the complete program. Their author-output-preserving
reruns took \(9.449625776003813\) and \(9.306663159004529\)
seconds, respectively. Exact prepromotion bytes, audit scopes,
the superseded weaker outline, and all executed code/output
remain retained.''')
canonical = own/'B_rational_high_line.tex'
assert not canonical.exists()
canonical.write_text(text)
labels = re.findall(r'\\label\{([^}]+)\}', text)
assert len(labels) == 6 and r'\status{Candidate' not in text

# Root explicitly authorized these two integration edits.
backup = own/'notes/CP27_before_B73_wiring'
assert not backup.exists()
backup.mkdir()
consolidate = work/'code/consolidate.py'
previous = consolidate.read_text()
(backup/'consolidate.py').write_text(previous)
old = "                    'B_first_level_mixed_boundary.tex']:"
new = "                    'B_first_level_mixed_boundary.tex',\n                    'B_rational_high_line.tex']:"
assert previous.count(old) == 1
consolidate.write_text(previous.replace(old,new))
prepare = work/'code/prepare_checkpoint27.py'
previous = prepare.read_text()
(backup/'prepare_checkpoint27.py').write_text(previous)
old = "required=['agents/reduction_descent/B_first_level_mixed_boundary.tex']"
new = "required=['agents/reduction_descent/B_first_level_mixed_boundary.tex',\n          'agents/reduction_descent/B_rational_high_line.tex']"
assert previous.count(old) == 1
prepare.write_text(previous.replace(old,new))

now = datetime.now(timezone.utc).isoformat()
record = {
    'status':'PROVED', 'promotion_utc':now,
    'canonical':str(canonical),
    'canonical_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest(),
    'audited_candidate_sha256':expected,
    'preserved_candidate':str(preserved), 'labels':labels,
    'root_audit':'../../outputs/root_B73_audit.json',
    'root_audit_utc':root['actual_utc'],
    'root_runtime_seconds':root['independent_runtime_seconds'],
    'companion_audit':'../obstructions_crystals/B73_independent_audit.json',
    'companion_audit_utc':comp['actual_utc'],
    'companion_runtime_seconds':comp['elapsed_seconds'],
    'author_runtime_seconds':9.558507562003797,
    'scope':'Exact full B4 height-two index nu_min(p,e,2)=2 iff p<e<p^3, for p>=5, mu_p in K, p not dividing e, perfect residue. e=p-1 has index1; permitted e>p^3 has index at least3. No exact higher-index or wild absolute-ramification claim.',
    'literature_search':'outputs/B73_literature_search.json',
    'source_search_limit':'Fresh bounded primary queries and explicit read scopes; no completeness or priority conclusion.',
    'wiring_changes':['code/consolidate.py','code/prepare_checkpoint27.py'],
    'wiring_preservation':str(backup),
    'checkpoint_scope':'Canonical promoted for CP27; no CP26 archive or frozen PDF mutation.',
    'executed_failures':[]
}
(own/'outputs/B73_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',record['scope'],'B_rational_high_line.tex;outputs/B73_promotion.json','Root and OC full independent proof/code PASS; exact candidate, all runtimes and targeted source-search limits retained'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:
    f.write('\n## '+now+' — B73 promoted after full audits\n\n'+record['scope']+' The actual high-branch point fields identify high lines even in scalar residual modules. The final actual comparison is only p-torsion and uses the genuine tame/wild distinction. CP27 wiring authorized by root is complete; no build or global report was run here.\n')
print(json.dumps(record,indent=2))
