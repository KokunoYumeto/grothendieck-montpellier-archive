from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re,difflib
own=Path(__file__).resolve().parents[1]; work=own.parents[1]
source=own/'B_wild_CM_layer_candidate.tex'
expected='9f40d83044089c669d36982ab2760e06d59c8baecf6a4115c78ce5905e9e7fa7'
raw=source.read_bytes(); assert hashlib.sha256(raw).hexdigest()==expected
root=json.loads((work/'outputs/root_B78_audit.json').read_text())
comp=json.loads((own.parent/'obstructions_crystals/B78_independent_audit.json').read_text())
for audit in (root,comp): assert audit['candidate_sha256']==expected and 'PASS' in audit['status']
saved=own/'notes/B_wild_CM_layer.prepromotion.tex'; assert not saved.exists(); saved.write_bytes(raw)
t=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; complete independent root and companion proof, primary-source and exact-code audits passed.}',raw.decode())
t=t.replace('% Post-CP27 candidate. Potential CM means finite-extension endomorphisms.','% Proved after full independent audits. Potential CM means finite-extension endomorphisms.')
needle='all-prime proof above.'
assert t.count(needle)==1
t=t.replace(needle,needle+r'''
The independent root and companion audits read every proof and
the entire corrected program; unchanged-program reruns passed in
\(0.21194225999352057\) and \(0.22546726299333386\) seconds.
Both freshly read the original Lubin--Tate proofs on
pp.~381--384 and the complete Stacks Tag~032A proof, retaining
the finite-residue limitation of the original Lubin--Tate source.
The exact audited candidate and every executed earlier output
remain preserved.''')
canonical=own/'B_wild_CM_layer.tex'; assert not canonical.exists(); canonical.write_text(t)
labels=re.findall(r'\\label\{([^}]+)\}',t); assert len(labels)==5 and r'\status{Candidate' not in t
now=datetime.now(timezone.utc).isoformat()
record=dict(status='PROVED',promotion_utc=now,canonical=str(canonical),canonical_sha256=hashlib.sha256(canonical.read_bytes()).hexdigest(),audited_candidate_sha256=expected,preserved_candidate=str(saved),labels=labels,root_audit='../../outputs/root_B78_audit.json',root_audit_utc=root['actual_utc'],root_runtime_seconds=root['independent_runtime_seconds'],companion_audit='../obstructions_crystals/B78_independent_audit.json',companion_audit_utc=comp['actual_utc'],companion_runtime_seconds=comp['independent_runtime_seconds'],author_runtime_seconds=0.21962125301070046,scope='At arbitrary e, nonsquare potential-CM height2 characters recover from actual p^n for n>=v_p(e)+2. At e=p(p-1), exact least manuscript index2 within the potentially CM, potentially supersingular subclass, with explicit actual mod-p2 lower pair. Full p5/e20 index remains2..3 and remaining125 failure has a non-CM member.',source_scope='Fresh original LT Lemma1/Theorems1/2 proofs pp381-384 and Stacks032A proof; prior HG/Tate through complete B52 proof reread. Explicit extension of finite-residue LT argument by Eisenstein polynomials.',correction_history='notes/B78_terminal_index_correction/correction.json',checkpoint_scope='Post-CP27 canonical wired for CP28, no build executed.')
(own/'outputs/B78_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',record['scope'],'B_wild_CM_layer.tex;outputs/B78_promotion.json','Root and OC complete proof/source/code PASS; corrected and prior outputs retained'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:f.write('\n## '+now+' — B78 promoted: terminal CM layer\n\n'+record['scope']+'\n')
history=own/'notes/CP28_before_B78_wiring'; assert not history.exists(); history.mkdir()
wiring=[]
for rel,old,new in [('code/consolidate.py',"'B_first_wild_finite_patterns.tex']:","'B_first_wild_finite_patterns.tex',\n                    'B_wild_CM_layer.tex']:"),('code/prepare_checkpoint28.py',"'agents/reduction_descent/B_first_wild_finite_patterns.tex'","'agents/reduction_descent/B_first_wild_finite_patterns.tex','agents/reduction_descent/B_wild_CM_layer.tex'")]:
 p=work/rel; before=p.read_bytes(); s=before.decode(); assert s.count(old)==1,rel
 after=s.replace(old,new); (history/p.name).write_bytes(before)
 (history/(p.name+'.diff')).write_text(''.join(difflib.unified_diff(s.splitlines(True),after.splitlines(True),fromfile=rel+'.before',tofile=rel)))
 p.write_text(after); wiring.append(dict(path=rel,before_sha256=hashlib.sha256(before).hexdigest(),after_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
wrecord=dict(status='WIRED_NOT_BUILT',actual_utc=datetime.now(timezone.utc).isoformat(),files=wiring,prior_versions=str(history),global_build_executed=False)
(own/'outputs/B78_CP28_wiring.json').write_text(json.dumps(wrecord,indent=2)+'\n')
print(json.dumps({'promotion':record,'wiring':wrecord},indent=2))
