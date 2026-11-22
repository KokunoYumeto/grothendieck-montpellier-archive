"""Preserve and amend CP31 inputs/status after further complete promotions."""
from pathlib import Path
import ast,datetime,difflib,hashlib,json
w=Path(__file__).resolve().parents[1]
folder=w/'notes/CP31_scope_amendment';assert not folder.exists();folder.mkdir()
changes=[]
def amend(rel,new,reason):
 p=w/rel;old=p.read_text();assert old!=new
 name=rel.replace('/','__')
 (folder/name).write_text(old)
 (folder/(name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='before',tofile='after')))
 if p.suffix=='.py':ast.parse(new,filename=rel)
 p.write_text(new)
 changes.append({'path':rel,'before':str((folder/name).relative_to(w)),
 'before_sha256':hashlib.sha256(old.encode()).hexdigest(),
 'after_sha256':hashlib.sha256(new.encode()).hexdigest(),'reason':reason})
p=w/'code/prepare_checkpoint31.py';t=p.read_text()
old="for optional in ['agents/reduction_descent/B_p5_tame_full_first_layer.tex']:"
new="for optional in ['agents/reduction_descent/B_p5_tame_full_first_layer.tex', 'agents/reduction_descent/B_p5_full_image_ramification.tex', 'agents/obstructions_crystals/A4_common_Cartier_incidence.tex', 'agents/monodromy/Cartier_kernel_wall_inertia.tex']:"
assert t.count(old)==1
amend('code/prepare_checkpoint31.py',t.replace(old,new),'Add only actual canonical later promotions to the build/QA input list; candidate files are excluded by the existing status guard.')
p=w/'code/update_current31.py';t=p.read_text()
marker="(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\\n')"
assert t.count(marker)==1
addition='''for row in rows:
 if row['item']=='A.4' and proved('agents/obstructions_crystals/A4_common_Cartier_incidence.tex'):
  row['where']+='; lem:DE-common-incidence-multiplication; prop:DE-common-Cartier-incidence; cor:DE-odd-principal-cube-kernel-birational'
  row['gate']+=(' The subsequent common-incidence proof closes the gap between separate generic ranks: the other contraction is literally the same Moore pencil, and the degree-one symmetrizer identifies the actual trivial left kernel linearly with the same section variable. All multiplication and dual determinant opens meet, with bijective relative Frobenius on a smooth connected pullback curve. Consequently the actual left-kernel map is separably dominant and birational in every fixed odd principal-cube degree. The remaining local gate is a nonempty corank-one Hasse wall inside this common open, followed by global full-radical generation; no new exact-group degree is asserted from birationality alone.')
 if row['item']=='A.4' and proved('agents/monodromy/Cartier_kernel_wall_inertia.tex'):
  row['where']+='; lem:maximal-kernel-variation-stable-loss; prop:birational-Cartier-kernel-wall-inertia'
  row['gate']+=(' The conditional wall theorem now proves that any nonempty Hasse wall inside the common maximal-rank open is smooth with simple determinant order, stable loss exactlyone, and full hyperplane-radical inertia. Maximal kernel variation excludes a further nilpotent step. Nonemptiness of that wall and the required global generation remain unproved; separate nonzero ambient determinants do not prove nonvanishing on the degree-one Hasse cubic.')
 if row['item']=='B.4' and proved('agents/reduction_descent/B_p5_full_image_ramification.tex'):
  row['where']+='; prop:B-RD88-point-fields; cor:B-RD88-cyclotomic'
  row['gate']+=(' B88 gives a further necessary actual profile for the survivingp5 full first layer: the two degree25 point fields have lower breaks(6,336) and(24,234); the common second division field has upper breaks6,24,66,72 and lower breaks6,96,1146,1896. Its actual cyclotomic quotient requires break72 overL and3 overK. The two diagonal quotient fields are distinct in this four-dimensional case. This profile is not an exclusion or realization of the full-image comparison; no impossibility of cyclotomic break3 is inferred.')
'''
amend('code/update_current31.py',t.replace(marker,addition+marker),'Record the proved common incidence and only canonically promoted conditional wall/profile consequences, preserving open group and realization gates.')
p=w/'sections/A_route_limitations_29.tex';t=p.read_text()
old='''These elementary statements are conditional tools. Their higher-degree
geometric hypotheses remain unproved; no additional monodromy group is
determined by this subsection.'''
new='''These elementary statements are conditional tools. Their later
higher-degree application is developed in
Corollary~\\ref{cor:DE-odd-principal-cube-kernel-birational}.
No additional monodromy group follows from these tools alone.'''
assert t.count(old)==1;t=t.replace(old,new)
old='''For higher degree, the typed
identification of the relevant kernel map with the map above, its
maximal differential rank on an actual corank-one wall, and the
required global radical generation remain unproved.'''
new='''For higher degree, the subsequent common-incidence theorem now
proves birationality of the actual left-kernel map in every fixed odd
principal-cube degree. Maximal differential rank on a nonempty actual
corank-one wall and the required global radical generation remain the
additional geometric conditions; the present generic-rank conclusion
does not supply their nonemptiness or generation.'''
assert t.count(old)==1;t=t.replace(old,new)
amend('sections/A_route_limitations_29.tex',t,'Update the old open-scope prose to cite the later proved common-incidence/birational theorem; all four original mathematical statements and their proofs remain unchanged.')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'status':'PASS','actual_utc':now,'changes':changes,
 'scope':'Integration and scope amendments only. No mathematical execution, actual review, build, finalization or archive is performed by this script.'}
(w/'outputs/checkpoint31_scope_amendment.json').write_text(json.dumps(record,indent=2)+'\n')
with(w/'notes/checkpoint31_changes.md').open('a')as f:
 f.write('\n## Integration and retained recording failure\n\nThe earlier conditional-kernel section has an explicit scope update referring to the later common-incidence theorem. Its four statements and proofs are unchanged; prior prose and exact diffs are retained in notes/CP31_scope_amendment. CP31 build/QA inputs now include only actually canonical later additions. The root local-wall audit recorder initially failed at Python parse time because of an apostrophe in a prose string. No instruction or numerical test executed in that failed attempt. The exact failed source and stderr were retained, and the corrected recorder succeeded at01:54:07.610775 UTC; this recording failure is not concealed or counted as a failed mathematical proof.\n')
print(json.dumps(record,indent=2))
