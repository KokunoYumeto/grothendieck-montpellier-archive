"""Authorized owned-file promotion after CP34 release; shared wiring deferred."""
from pathlib import Path
from datetime import datetime,timezone
import difflib,hashlib,json,re

root=Path(__file__).resolve().parents[3]
own=root/'agents/obstructions_crystals'
src=own/'post_CP34_Lang_wedge_pole_theta_bound_candidate.tex'
dst=own/'A4_Lang_wedge_pole_theta_bound.tex'
expected='cf64119de3fe23e9e93f3e07face711ccf1f8f0e2fd9acea2e3a16b8fdf6fd5b'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src)==expected and not dst.exists()
audits=['outputs/root_Lang_wedge_pole_theta_bound_audit.json',
        'agents/monodromy/outputs/independent_Lang_wedge_pole_theta_bound_audit.json']
for name in audits:
 r=json.loads((root/name).read_text())
 assert 'PASS' in r['status'] and r['candidate_sha256']==expected
before=src.read_text()
labels=re.findall(r'\\label\{([^}]+)\}',before)
assert len(labels)==5
after=re.sub(r'\\status\{Candidate[^}]*\}',r'\\status{Proved; full independent proof and source audits passed.}',before)
after=re.sub(r'\A%[^\n]*','% Promoted after CP34 release and two complete independent audits; exact candidate retained.',after)
assert after.count('\\status{Proved')==5
h=own/'notes/CP35_Lang_wedge_pole_promotion'
h.mkdir(exist_ok=False)
(h/'candidate.tex').write_bytes(src.read_bytes())
(h/'promotion.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='candidate',tofile='proved')))
with dst.open('x') as f:f.write(after)
now=datetime.now(timezone.utc).isoformat()
record={'status':'PROMOTED AFTER TWO COMPLETE INDEPENDENT PROOF/SOURCE AUDITS',
 'actual_utc':now,'candidate':str(src.relative_to(root)),'candidate_sha256':expected,
 'canonical':str(dst.relative_to(root)),'canonical_sha256':sha(dst),'labels':labels,
 'audits':audits,'history':str(h.relative_to(root)),
 'shared_wiring':'DEFERRED: root holds consolidate/config for CP35 setup; no shared file changed.',
 'scope':'Invariant determinant-wedge poles are bounded by the remaining Euler determinant divisor. The theta degree forces quotient dimension at least d2; cyclic type(3,3ell) gives3ell and fixed principal systems give max(8,3d). Full image follows only if the good-wall union has the entire determinant degree; no universal K=0 claim.',
 'source_scope':'Full retained original AV8.19/8.20 proofs independently read by author, root and companion; no numerical program needed.'}
out=own/'Lang_wedge_pole_theta_bound_promotion.json'
with out.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:
  f.write('\t'.join([now,label,'promotion_after_full_independent_audits',record['canonical'],record['scope'],
                     'PROVED; stronger bound, no general vanishing',str(out.relative_to(root))])+'\n')
with (own/'D_results.md').open('a') as f:
 f.write('\n\n## Determinant wedge and theta-degree bound — '+now+'\n\n')
 f.write('`A4_Lang_wedge_pole_theta_bound.tex` proves a new quantitative restriction on the canonical residual module. The actual invariant wedge is regular at every full-radical common wall; its poles elsewhere are bounded by the full determinant orders. The theta commutator forces the nonempty regular-wall union to have degree at least the larger polarization elementary divisor. Exterior-Euler vanishing then gives the stated quotient bounds. All extra-wall poles remain allowed; no complete A.4 claim is inferred.\n')
assert sha(src)==expected
print(json.dumps({'status':record['status'],'actual_utc':now,'canonical':record['canonical'],
                  'canonical_sha256':record['canonical_sha256'],'record':str(out.relative_to(root)),
                  'shared_files_changed':False}))
