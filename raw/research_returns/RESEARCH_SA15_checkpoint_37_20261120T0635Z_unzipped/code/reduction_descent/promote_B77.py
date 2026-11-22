from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, difflib

own = Path(__file__).resolve().parents[1]
work = own.parents[1]
source = own/'B_first_wild_finite_patterns_candidate.tex'
expected = '4ba07b6ebed9e8d72c8a9520e68b1a070c7df4446d8fc9de078b9a5fba43824a'
raw = source.read_bytes()
assert hashlib.sha256(raw).hexdigest() == expected
root = json.loads((work/'outputs/root_B77_audit.json').read_text())
comp = json.loads((own.parent/'obstructions_crystals/B77_independent_audit.json').read_text())
for audit in (root, comp):
    assert audit['candidate_sha256'] == expected and 'PASS' in audit['status']
saved = own/'notes/B_first_wild_finite_patterns.prepromotion.tex'
assert not saved.exists()
saved.write_bytes(raw)
t = re.sub(r'\\status\{Candidate[^}]*\}', lambda _: r'\status{Proved; complete independent root and companion proof and exact-code audits passed.}', raw.decode())
t = t.replace('% Separate post-CP27 candidate. The nonsquare whole-formal branch remains open.', '% Proved after full root and companion audits; the nonsquare whole-formal branch remains open.')
needle = 'proof are retained; no executed computation failed.'
assert t.count(needle) == 1
t = t.replace(needle, needle + r'''
The complete independent root and companion proof/code audits
passed, with unchanged-program reruns taking
\(0.7250874890014529\) and \(0.630934568005614\) seconds,
respectively. The author output and exact audited candidate
were preserved. The audits reread the full internal B64 and B50
proofs; they reused the previously audited original Bondarko
and Tate passages without claiming a fresh external-source read.''')
canonical = own/'B_first_wild_finite_patterns.tex'
assert not canonical.exists()
canonical.write_text(t)
labels = re.findall(r'\\label\{([^}]+)\}', t)
assert len(labels) == 4 and r'\status{Candidate' not in t
now = datetime.now(timezone.utc).isoformat()
record = dict(status='PROVED', promotion_utc=now, canonical=str(canonical),
    canonical_sha256=hashlib.sha256(canonical.read_bytes()).hexdigest(),
    audited_candidate_sha256=expected, preserved_candidate=str(saved), labels=labels,
    root_audit='../../outputs/root_B77_audit.json', root_audit_utc=root['actual_utc'],
    root_runtime_seconds=root['independent_runtime_seconds'],
    companion_audit='../obstructions_crystals/B77_independent_audit.json', companion_audit_utc=comp['actual_utc'],
    companion_runtime_seconds=comp['elapsed_seconds'], author_runtime_seconds=0.6461968240037095,
    scope='p>=5, e=p(p-1), height2, mu_p in K, perfect residue: least full B4 index is bounded2..3. Actual p^3 failure requires two whole potentially supersingular groups and nonsquare finite determinant. Atp5/e20 only normalized AB/AC finite-character patterns, joint24, remain. No existence or exact wild index claim.',
    source_scope='Fresh full internal B64/B50 reads; previously audited original Bondarko/Tate passages reused without a fresh external-source-read claim.',
    checkpoint_scope='Post-CP27 canonical wired for CP28 under explicit parent authorization; no build run.',
    executed_failures=[])
(own/'outputs/B77_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',record['scope'],'B_first_wild_finite_patterns.tex;outputs/B77_promotion.json','Root and OC full proof/dependency/code PASS; exact candidate/output preserved'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:
    f.write('\n## '+now+' — B77 promoted: first wild finite patterns\n\n'+record['scope']+'\n')

history=own/'notes/CP28_before_B77_wiring'
assert not history.exists()
history.mkdir()
wiring=[]
for rel,old,new in [
    ('code/consolidate.py',"'B_wild_cyclic_point.tex']:","'B_wild_cyclic_point.tex',\n                    'B_first_wild_finite_patterns.tex']:"),
    ('code/prepare_checkpoint28.py',"'agents/reduction_descent/B_wild_cyclic_point.tex']","'agents/reduction_descent/B_wild_cyclic_point.tex','agents/reduction_descent/B_first_wild_finite_patterns.tex']")]:
    path=work/rel; before=path.read_bytes(); text=before.decode()
    assert text.count(old)==1,rel
    after=text.replace(old,new)
    (history/path.name).write_bytes(before)
    (history/(path.name+'.diff')).write_text(''.join(difflib.unified_diff(text.splitlines(True),after.splitlines(True),fromfile=rel+'.before',tofile=rel)))
    path.write_text(after)
    wiring.append(dict(path=rel,before_sha256=hashlib.sha256(before).hexdigest(),after_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
wrecord=dict(status='WIRED_NOT_BUILT',actual_utc=datetime.now(timezone.utc).isoformat(),files=wiring,prior_versions=str(history),global_build_executed=False)
(own/'outputs/B77_CP28_wiring.json').write_text(json.dumps(wrecord,indent=2)+'\n')
print(json.dumps({'promotion':record,'wiring':wrecord},indent=2))
