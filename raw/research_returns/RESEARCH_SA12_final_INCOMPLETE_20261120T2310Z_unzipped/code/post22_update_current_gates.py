"""Update current gates after the fully audited arbitrary-SNC and local transfer proofs."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
root=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
manifests=[
 'parts/D/post22_research/integration_manifest_SNC_general_geometry_D.json',
 'parts/D/post22_research/integration_manifest_SNC_general_count_D.json',
 'parts/D/post22_research/integration_manifest_local_projective_all_dimensions_D.json',
 'parts/B/post22_research/integration_manifest_B_classical_automorphism_crowns.json']
p=root/'code/output/review15_main_assessment.json';a=json.loads(p.read_text())
known={x['path'] for x in a['verified_files']}
for mp in manifests:
 m=json.loads((root/mp).read_text());assert hashlib.sha256((root/m['path']).read_bytes()).hexdigest()==m['sha256']
 if m['path'] not in known:a['verified_files'].append({'path':m['path'],'sha256':m['sha256'],'audit_manifest':mp})
a['assessment_staged_utc']=now
a['strict_main_gate_reductions'][0]='One strict local-projective reduction: the unrestricted geometric-period quadratic PGL count now holds for arbitrary fixed complete excellent normal local surfaces via projective SNC resolution, including graph cycles and secondary residues. Fixed slicing and finite normalization extend it to complete equicharacteristic local punctures in all dimensions, including nonnormal/nonreduced rings when every component has dimension at least two. This enlarges the same post-review14 tree reduction, rather than adding another movement.'
a['remaining_strongest_gates'][1]='Unbounded geometric Brauer period in defining-characteristic projective representations on the residual global proper surfaces. The corresponding fixed-complete-local puncture problem is now proved in every dimension with every component dimension at least two. Uniform constants linear in the degree of arbitrary finite local covers remain unproved.'
a['remaining_strongest_gates'][3]+=' The named classical defining-characteristic families are now verified in this same one-curve radially tame crown scope.'
a['auxiliary_not_movement'][0]='The tree geometry, arbitrary-SNC geometry and effective atlas, actual unit-Isom comparison, SNC resolution, fixed slicing, and finite-normalization transfers are dependencies or closures of this single local-projective reduction, not separate movements.'
a['report_summary']='Two strongest main gates are strictly smaller after review14: unrestricted-period projective counts now cover the stated complete local punctures in every dimension, and the one-curve projective crown family permits unbounded tame field-image order. Classical-family recognition belongs to that same crown enlargement. General D.1, D.2(ii) and residual L8 remain open.'
p.write_text(json.dumps(a,indent=2)+'\n')

note=json.loads((root/'parts/D/post22_research/bibliography_note_local_projective_transfer_D.json').read_text())
p=root/note['central_path'];s=p.read_text()
pattern=r'(@misc\{StacksDSurfaceResolution,[\s\S]*?\n note=\{)([^\n]*)(\}\})'
assert len(re.findall(pattern,s))==1
p.write_text(re.sub(pattern,lambda m:m[1]+note['note']+m[3],s,count=1))

p=root/'code/assemble.py';s=p.read_text()
marker="report=['INCOMPLETE','','# Research report: SA12'"
assert marker in s
addition="""general_local_scope='; unrestricted-period projective q^(C_R r²) growth now holds for arbitrary complete excellent normal local surfaces and, by fixed slicing and normalization, for every connected puncture component of complete local k-algebras whose irreducible components all have dimension at least two, including nonnormal/nonreduced rings'
general_local_labels='D:SNC-general-Brauer-geometry; D:SNC-general-residual-category; D:SNC-general-weighted-presentation; D:SNC-general-projective-quadratic-count; D:complete-local-projective-growth-all-dimensions'
outcomes=[(item,state+general_local_scope,locator+'; '+general_local_labels+'; D:normal-subgroup-projective-crowns; D:classical-defining-characteristic-crowns') if item in ('D.1','D.2(ii)','L8') else (item,state,locator) for item,state,locator in outcomes]
"""
assert 'general_local_scope=' not in s;s=s.replace(marker,addition+marker,1)
marker="'','## Files and continuation','',"
paragraph='The post-checkpoint22 arbitrary-SNC synthesis removes the exceptional-graph restriction from the fixed local projective count. Graph cycles and nonzero secondary residues are retained; mixed-order projective node blocks, marked spectral curves, actual finite presentations and their unit-class comparison give q^(C_R r²) with unrestricted geometric Brauer period. Projective SNC resolution plus the fixed detecting surface slice and finite-proper normalization descent extend this bound to complete local punctures in all dimensions, including nonnormal/nonreduced rings with every component of dimension at least two. All five new local units passed four full actual-file audits. They enlarge the same single post-review14 local reduction. The residual global Brauer-period bound and degree-linear hereditary constants are still unproved. The bounded-index normal-subgroup crown refinement and named classical-family recognition are also assembled; both belong to the same one-curve unbounded-field crown enlargement. Earlier paragraphs retain the dated route by which these results were reached; this paragraph and the formal-review assessment specify their current scope.'
assert marker in s;s=s.replace(marker,repr(paragraph)+',\n'+marker,1)
p.write_text(s)

p=root/'parts/D/unresolved_D.tex';s=p.read_text()
marker='\\section{Part D: unresolved gates and unchecked candidates}\n'
intro=r'''
\paragraph{Current scope after the arbitrary-SNC synthesis.}
Only general D.1, general D.2(ii), and their dependent residual L8
remain requested open rows. The checked local projective theorem
\ref{D:SNC-general-projective-quadratic-count} covers arbitrary SNC
exceptional graphs, including secondary residues. Corollary
\ref{D:complete-local-projective-growth-all-dimensions} removes the
graph and dimension restrictions in the stated complete local scope,
with every irreducible component of dimension at least two.
Its constant is allowed to depend on the fixed ring. The remaining
projective-period problem is global; hereditary constants linear in
arbitrary cover degree are also unproved. In the one-curve radial-tame
scope, \ref{D:tame-projective-automorphism-crowns} and
\ref{D:normal-subgroup-projective-crowns} permit unbounded field image,
and \ref{D:classical-defining-characteristic-crowns} verifies the
listed classical families. Wild outer covers, alternating
multiplicities, uncovered cross-characteristic families, other crown
geometries, and the residual global dimensional reductions remain.
The following record retains successive approaches and their later
closures; a historical intermediate gate is not a new open item.

'''
assert intro not in s;s=s.replace(marker,marker+intro,1)
old='The unbounded-field projective count in\n\\ref{D:bounded-graph-projective-crown-reduction} remains an explicit\nhypothesis.'
new='In the earlier reduction, the unbounded-field projective count in\n\\ref{D:bounded-graph-projective-crown-reduction} was an explicit\nhypothesis, discharged by \\ref{D:tame-projective-semilinear-count}.'
assert old in s;s=s.replace(old,new,1)
old='The unresolved geometric step is to extend the actual\ncoefficient gerbe coherently'
new='The geometric step that had remained was to extend the actual\ncoefficient gerbe coherently'
assert old in s;s=s.replace(old,new,1)
old='Arbitrary exceptional graphs,\nthe residual global projective problem, the unbounded-field\nsemilinear gerbe comparison and the other stated strongest gates\nremain unresolved.'
new='At that stage arbitrary graphs and the unbounded-field comparison\nwere still unresolved; both are now proved in their stated scopes.\nThe residual global projective problem and the other current\nstrongest gates remain unresolved.'
assert old in s;s=s.replace(old,new,1)
s+=r'''

\paragraph{Arbitrary SNC graphs and all complete local punctures.}
The two geometry statements
\ref{D:SNC-general-Brauer-geometry}--\ref{D:SNC-general-residual-category}
retain graph-cycle residues and the noncommuting node algebra.
The actual weighted presentation and unit comparison in
\ref{D:SNC-general-weighted-presentation} yield
\ref{D:SNC-general-projective-quadratic-count}. The new all-dimensional
closure \ref{D:complete-local-projective-growth-all-dimensions}
uses a fixed slice, projective SNC resolution and finite-proper torsor
descent, and does not assume Brauer pullback injectivity.
These results enlarge one local-projective reduction. They give
neither a global proper-surface count at unrestricted Brauer period
nor an index-linear atlas for arbitrary finite local covers.
'''
p.write_text(s)
with (root/'PROGRESS_LEDGER.md').open('a') as f:
 f.write('\n\n## Post-checkpoint22 current-gate update\n\nINCOMPLETE. '+now+'. Four arbitrary-SNC units and the complete-local all-dimensional closure now have four actual-file audits and are centrally assembled. The classical defining-characteristic crown recognition and normal-subgroup refinement are assembled. The staged review15 assessment counts exactly two strict reductions since review14, with no requested-row changes and no extra movement for dependencies, transfers, recognition or packaging. No formal review or checkpoint was performed by this update.\n')
print(json.dumps({'utc':now,'updated':'review15 assessment, current report/appendix scope, existing bibliography note','strict_reductions':2,'archive_created':False}))
