"""Record actual review23 only after due time and only from audited canonical proofs."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
due=datetime.datetime.fromisoformat('2026-11-20T03:50:40+00:00')
assert datetime.datetime.now(datetime.timezone.utc)>=due
canonical=[
 'sections/A_full_radical_image_structure.tex',
 'agents/obstructions_crystals/A4_Lang_polar_irreducibility.tex',
 'agents/obstructions_crystals/A4_Lang_main_orbit.tex',
 'agents/obstructions_crystals/A4_Lang_deck_slice_bound.tex',
 'agents/reduction_descent/B_residual_wild_high_quotient.tex',
 'agents/reduction_descent/B_residual_wild_crossing.tex']
for rel in canonical:
 p=w/rel
 assert p.exists() and '\\status{Candidate' not in p.read_text() and '\\textup{[Candidate' not in p.read_text(),rel
audits=[
 'outputs/root_Lang_polar_irreducibility_audit.json',
 'outputs/root_Lang_main_orbit_audit.json',
 'outputs/root_Lang_deck_slice_bound_audit.json',
 'agents/monodromy/outputs/independent_Lang_deck_slice_bound_audit.json',
 'outputs/root_B91_audit.json',
 'agents/monodromy/outputs/independent_B91_residual_wild_high_quotient_audit.json',
 'outputs/root_B92_audit.json',
 'agents/monodromy/outputs/independent_B92_residual_wild_crossing_audit.json']
for rel in audits:
 r=json.loads((w/rel).read_text())
 assert 'PASS' in r.get('status',r.get('result','')),rel
assessment={
 'due_utc':due.isoformat(),
 'next_checkpoint_due_utc':'2026-11-20T04:20:40+00:00',
 'movement':[
  'A.4: the actual reduced Lang polar is now proved irreducible for every odd principal-cube system on a fixed nonordinary principal surface, without any height-three assumption. Its maximal-dual-rank component is identified with the unique large orbit V minus K_d. The central cubic deck slice further proves dim(V/K_d)>=8. Hence the former polar-irreducibility/local-to-main-component obligation is closed, and the structural full-image gate reduces to excluding nonzero exceptional K_d, now of dimension at most r-8, whose nonzero Lang components are wholly in lower dual-rank strata. No new exact full-image degree is claimed.',
  'B.4: B91 forces both original residual-wild parameters to be p-divisible at first wild ramification and reduces the p5/e20 crossing branch to (5,45),(15,95); its both-large branch reduces to layer shapes(3,4),(4,4), of wild orders5^8,5^9. B92 then excludes crossing(15,95) through the incompatible actual degree25 diagonal-quotient breaks72 and336. Only crossing(5,45), the two both-large shapes and the unchanged irreducible-residual sector remain within the stated actual125 comparison gate.'
 ],
 'unresolved_refinements':[
  'Every open row is reviewed in the accompanying current-state table: general A.3; general exact whole-image and effective all-large-degree A.4; higher-dimensional B.3; and general B.4. Their general status remains OPEN. A.5 remains fully closed in every-X, every-residue, every-open scope with its proved explicit bound.',
  'A.3 primitive mixed positive-index ranks and arbitrary-X ranks have not advanced. The fixed f0 first undecided exact-group odd degree remains17; the fixed f1 first odd/even gaps remain5 and8. The new quotient bound and main component do not determine K_d or H_d and do not close the all-X question.',
  'The full first-wild least manuscript index remains in{2,3}. The last-crossing B93 candidate is not yet fully audited or canonical and is excluded from this review. No actual comparison realizing any surviving pattern is known here.',
  'The abstract Pfaffian height-two countermodel, the full-radical block-group restatement by itself, parity calculations, failed routes, source searches, layout convergence corrections and checkpoint production are not counted as movement.',
  'The arbitrary odd-source block theorem and compatible-intermediate full-image criterion are still candidate work at the review cutoff; no movement is credited to them. No unproved assumption that a dense open meets a special slice is used.'
 ]}
p=w/'notes/review23_assessment.json';assert not p.exists()
p.write_text(json.dumps(assessment,indent=2)+'\n')
subprocess.run([sys.executable,str(w/'code/update_current34.py')],cwd=w,check=True)
subprocess.run([sys.executable,str(w/'code/record_review_markdown_safe.py'),'23',str(p)],cwd=w,check=True)
r=json.loads((w/'notes/progress_review_23.json').read_text())
assert r['no_movement_streak']==0 and len(r['movement'])==2
assert {x['item'] for x in r['open_rows']}=={'A.3','A.4','B.3','B.4'}
message=('\n### Actual hourly review23\n\n'
 f"Review23 occurred at {r['actual_utc']}, against actual review22 at {r['baseline_actual_utc']}. "
 'The reduced polar and main-component identification close the corresponding structural A.4 obligations, and the deck slice bounds the exceptional module by dimension r-8. B91 narrows the actual residual-wild parameter/layer alternatives, and B92 excludes crossing(15,95). '
 'The four general open rows A.3,A.4,B.3,B.4 stay open; A.5 stays completely closed. The unaudited B93 candidate is not counted. Consecutive no-movement count: zero; disposition: Continue. '
 'Checkpoint34 is due04:20:40UTC; next actual review24 is due04:50:40UTC on20November2026.\n')
for rel in ['notes/checkpoint34_changes.md','RESEARCH_SA15_report.md']:
 with (w/rel).open('a') as f:f.write(message)
print(message)
