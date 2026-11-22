"""Record named-family completion and the auxiliary swap certificate before review15."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,csv
root=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
mp='parts/B/post22_research/integration_manifest_B_exceptional_automorphism_crowns.json'
m=json.loads((root/mp).read_text());assert hashlib.sha256((root/m['path']).read_bytes()).hexdigest()==m['sha256']
p=root/'code/output/review15_main_assessment.json';a=json.loads(p.read_text())
assert m['path'] not in {x['path'] for x in a['verified_files']}
a['verified_files'].append({'path':m['path'],'sha256':m['sha256'],'audit_manifest':mp})
a['assessment_staged_utc']=now
a['strict_main_gate_reductions'][1]+=' The bounded-index normal-subgroup refinement and fully checked classical/exceptional recognition now include all defining-characteristic finite simple Lie families (with fixed small derived exceptions absorbed), within the same one-curve radially tame outer-quotient scope.'
a['remaining_strongest_gates'][3]=a['remaining_strongest_gates'][3].replace('The named classical defining-characteristic families are now verified','All named defining-characteristic finite simple Lie families, classical and exceptional including Suzuki/Ree, are now verified')
a['auxiliary_not_movement'].append('The symmetric-square wild cyclic cover is an alternative all-genus construction of an already known failure of automatic radial tameness. Its exact wild-image order2, generator bound2g+2, and9350-assertion local certificate are auxiliary, not another main-gate reduction.')
a['report_summary']=a['report_summary'].replace('Classical-family recognition','Complete defining-characteristic Lie-family recognition')
p.write_text(json.dumps(a,indent=2)+'\n')
p=root/'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f:events=list(csv.DictReader(f,delimiter='\t'))
assert not any(e['statement_id']=='D:one-curve-wild-swap-cover' and e['type']=='computation or formal certificate' for e in events)
c=json.loads((root/'code/output/wild_swap_local_certificate_root.json').read_text())
events.append({'statement_id':'D:one-curve-wild-swap-cover','date':c['utc'],'who':c['actor'],'type':c['type'],'outcome':'PASS9350 exact assertions. '+c['scope']+' Excluded: '+c['excluded_scope']+' Independent C execution recorded at parts/C/post22_research/audit_wild_swap_certificate_C.json; same certificate, no extra movement.'})
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
p=root/'code/assemble.py';s=p.read_text();marker="report=['INCOMPLETE','','# Research report: SA12'"
addition="recognition_labels='D:exceptional-defining-characteristic-crowns; D:one-curve-wild-swap-cover; D:wild-swap-exact-image'\noutcomes=[(item,state+'; all classical and exceptional defining-characteristic Lie families satisfy the stated one-curve crown theorem with radially tame outer quotient',locator+'; '+recognition_labels) if item in ('D.1','D.2(ii)','L8') else (item,state,locator) for item,state,locator in outcomes]\n"
assert marker in s and 'recognition_labels=' not in s;s=s.replace(marker,addition+marker,1)
marker="'','## Files and continuation','',"
para='All ten exceptional defining-characteristic Lie series, including Suzuki/Ree, now satisfy the same one-curve radially tame outer-quotient crown theorem. The original Steinberg1960 article and original Yale notes supply precisely located known automorphism inputs; written proof sketches and omitted calculations are explicitly identified. This recognition is part of the same unbounded-field crown enlargement. An alternative symmetric-square construction in characteristic2 gives a fierce cyclic cover for every genusg≥2, with ramification index1 and inseparable residue degree2. It extends the previously recorded genus-two failure of automatic radial tameness. The upstairs formal retraction proves that one wild-inertia image has order exactly2 and d(pi1(U))≤2g+2. Its normal closure is not identified. These two units are auxiliary, and their9350-assertion certificate verifies only the stated finite polynomial/intersection calculations.'
s=s.replace(marker,repr(para)+',\n'+marker,1);p.write_text(s)
p=root/'parts/D/unresolved_D.tex'
with p.open('a') as f:f.write(r'''

\paragraph{Named Lie families and the tame hypothesis.}
Corollary~\ref{D:exceptional-defining-characteristic-crowns}
completes the defining-characteristic Lie-family recognition,
including Suzuki and Ree. This is part of the same one-curve
radially tame crown reduction. Example
\ref{D:one-curve-wild-swap-cover} gives an alternative construction,
for every genus at least two, of the failure already exhibited in
\ref{D:wild-genus2-single-curve}. Corollary
\ref{D:wild-swap-exact-image} gives its exact wild-image order two
and its finite-generation bound. These do not remove the radial
tameness hypothesis from the general crown theorem.
''')
print(json.dumps({'utc':now,'review15_strict_reductions':2,'new_computation_events':1,'archive_created':False}))
