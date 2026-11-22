"""Record the completed tree reduction once; no formal review or ZIP."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
paths=['parts/D/post21_research/integration_manifest_SNC_tree_components_D.json',
       'parts/D/post21_research/integration_manifest_SNC_tree_count_D.json']
verified=[]
for name in paths:
 m=json.loads((root/name).read_text())
 assert hashlib.sha256((root/m['path']).read_bytes()).hexdigest()==m['sha256']
 assert set(m['audits'])=={'root','B','C','D'}
 assert all(a['verdict']=='PASS' for a in m['audits'].values())
 verified.append(dict(path=m['path'],sha256=m['sha256'],audit_manifest=name,promoted_at_utc=m['promoted_at_utc']))
prior=json.loads((root/'code/output/formal_review14.json').read_text())
gates=prior['remaining_strongest_gates'][:]
gates[1]='Unbounded geometric Brauer period in defining-characteristic projective representations on residual global and complete-local surfaces outside the proved complete-local SNC-exceptional-tree case; every fixed period bound remains covered with a constant allowed to depend on that bound.'
record=dict(assessment_actor='root',assessment_staged_utc=now,formal_review_completed=False,
 movement=True,strict_main_gate_reductions=['One strict local-projective reduction: the unrestricted geometric-period quadratic PGL count now holds for every fixed complete excellent normal local surface with a regular projective SNC exceptional tree, extending the previously proved one-smooth-curve case.'],
 requested_status_changes=[],verified_files=verified,all_required_proof_audits_completed=True,
 remaining_strongest_gates=gates,requested_open=prior['requested_open'],
 auxiliary_not_movement=['The component atlas and finite-unit comparison are dependencies of this one tree reduction, not separate movements.',
 'All ordinary hereditary PGL and bounded-field crown results already included in review14 remain accounted there and cannot be counted again.',
 'Searches, audit refreshes, compilation, image inspection and checkpoint assembly are not research movement.'],
 report_summary='A complete four-audit SNC-tree local projective count is proved. General D.1, general D.2(ii), residual L8, arbitrary exceptional graphs, residual global projective counts and general crown/simple-family gates remain open.')
(root/'code/output/review15_main_assessment.json').write_text(json.dumps(record,indent=2)+'\n')

p=root/'parts/D/results_D.csv'
with p.open() as f: reader=csv.DictReader(f); cols=reader.fieldnames; rows=list(reader)
for row in rows:
 if row['id']=='D:SNC-tree-projective-quadratic-count':
  row['notes']=row['notes'].replace('Auxiliary; no main-gate movement.','One strict post-review14 local projective-gate reduction; assembly does not create a further movement event.')
 elif row['id']=='D:SNC-tree-finite-unit-comparison':
  row['notes']=row['notes'].replace('Auxiliary; no main-gate movement.','Auxiliary dependency of the same single post-review14 SNC-tree projective reduction.')
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)

p=root/'code/assemble.py';s=p.read_text()
s=s.replace('The ordinary hereditary PGL proof and bounded-field crown consequence have four actual-file audits and are retained separately pending integration; the verified407-page checkpoint21 PDF contains the preceding11 crown units.',
            'The ordinary hereditary PGL proof and bounded-field crown consequence have four actual-file audits and are now assembled; checkpoint21 had contained the preceding11 crown units.')
scope="""tree_scope='; all projective representations of a fixed complete excellent normal local surface with an SNC exceptional-tree resolution satisfy q^(C_R r²), with unrestricted geometric Brauer period'
outcomes=[(item,state+tree_scope,locator+'; D:SNC-tree-projective-quadratic-count') if item in ('D.1','D.2(ii)','L8') else (item,state,locator) for item,state,locator in outcomes]
"""
assert "report=['INCOMPLETE'" in s and 'tree_scope=' not in s
s=s.replace("report=['INCOMPLETE'",scope+"report=['INCOMPLETE'",1)
marker="'','## Files and continuation','',"
paragraph="""'Four further post-checkpoint21 statements complete one new local-projective reduction. Small marked sources and fixed partial resolutions give actual component bundles and maps over every coefficient algebra, with derived restriction and finite-projective gluing at the thick nodes. Uniform original-cycle poles and Frobenius windows give finite-presentation actual unit-Isom and open-and-closed unit classes. The component-rescaled factorial estimate then proves q^(C_R r²) projective counts for every fixed complete local surface with an SNC exceptional tree, uniformly in scalar order and geometric Brauer period. All four actual-file proof audits passed. The effectivity proof explicitly constructs an algebraic generating anchor from the cyclic splitting cover, first lifts finite-cycle data formally, and only then applies existence theory over the correct completed coefficient base. This is one strict reduction after review14, staged for review15; the component and comparison inputs are not separate movements. General exceptional graphs, residual global projective counts, hereditary tree constants, unbounded-field projective descent and full finite generation remain unresolved.',
"""
assert marker in s
p.write_text(s.replace(marker,paragraph+marker,1))

p=root/'parts/D/unresolved_D.tex'
with p.open('a') as f:f.write(r'''

\paragraph{The exceptional-tree projective gate is now closed.}
Lemmas and propositions
\ref{D:SNC-tree-small-marked-source}--\ref{D:SNC-tree-finite-unit-comparison}
now supply the missing actual component atlas, thick-node pasting and
finite unit-class comparison. Theorem
\ref{D:SNC-tree-projective-quadratic-count} proves
$q^{C_Rr^2}$ for every fixed complete excellent normal local surface
with a regular projective SNC exceptional-tree resolution, without
bounding its geometric Brauer period. This is one strict extension
beyond the one-smooth-curve case after review14. It does not give
hereditary-index constants for trees. Arbitrary exceptional graphs,
the residual global projective problem, the unbounded-field
semilinear gerbe comparison and the other stated strongest gates
remain unresolved. No full finite-generation conclusion is inferred.
''')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
 f.write('\n\n## Post-review14 completed SNC-tree reduction\n\nINCOMPLETE. '+now+'. The four audited tree component/comparison/count units were promoted at16:21:51.431743UTC and integrated at16:22:36.668567UTC. The fixed-local unrestricted-period projective count now covers SNC exceptional trees. This is one strict local-projective reduction staged for the17:10UTC formal review; the component atlas and finite-Isom proof are its dependencies, not separate movement. The last completed formal review remains review14 with counter0. All requested open rows remain unchanged. Exact source hashes and four-actor audit manifests are in code/output/review15_main_assessment.json. No checkpoint is created by this record.\n')
print(json.dumps({'utc':now,'staged_review':15,'strict_reductions':1,'formal_review_completed':False,'archive_created':False},indent=2))
