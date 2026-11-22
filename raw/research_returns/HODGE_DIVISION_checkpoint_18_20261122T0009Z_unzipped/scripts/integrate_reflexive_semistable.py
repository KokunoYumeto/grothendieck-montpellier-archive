"""Integrate whole-reviewed stable-reflexive and semistable sheaf results."""
from pathlib import Path
from datetime import datetime, timezone
import csv,hashlib,json,re
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
paths={
 'E834':'agents/sixfolds/rm_reflexive_mixed_curvature_section.tex',
 'E835':'agents/sixfolds/rm_semistable_reflexive_reduction_section.tex'}
frozen={
 'E834':'1ac992d7aab89a788ae2e2658d3e2f9877a6bfe60c088810619c544a5f8104ae',
 'E835':'3bfeb04e0c430bc48c34cf5fd42073141370383e8bbe2961636a6cf636d09876'}
for k,p in paths.items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==frozen[k],k
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
def displays(s):return re.findall(r'\\\[(.*?)\\\]',s,re.S)
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert all(r['id'] not in ('Q5ah','Q5ai') for r in rows)
(R/'research/gates_before_reflexive_semistable.json').write_text(json.dumps({r['id']:r for r in rows if r['id']=='Q5i'},indent=2)+'\n')
p=R/paths['E834'];before=p.read_text()
s=change(before,'\\textbf{Status:} complete new proof, submitted for independent\nwhole-proof review. This repairs the two specific unresolved steps',
 r'''\textbf{Status:} complete new proof, whole-read by the author and
independently checked in full by /root and /root/g34\_eightfolds.
The invoked published analytic statements and the new arguments pass;
their exact reading scopes are recorded separately. This repairs the
two specific unresolved steps''')
assert displays(s)==displays(before);p.write_text(s)
p=R/paths['E835'];before=p.read_text()
s=change(before,r'''\textbf{Status:} complete new proof, submitted for independent
whole-proof review. Its new analytic premise is SF-E834, which is
separately frozen and under review. This section does not promote that
premise before its review. The remaining steps are algebraic and are
proved in full below.''',r'''\textbf{Status:} complete new proof, whole-read by the author and
independently checked in full by /root and /root/g34\_eightfolds.
Its analytic premise SF-E834 has separately passed both whole-proof
reviews. The remaining algebraic steps are proved in full below.''')
s=change(s,'escape, once E834 is established.','escape, by the separately checked E834.')
s=change(s,'The new analytic premise E834 is explicitly separate and must pass its\nown whole-proof reviews.','The analytic premise E834 remains a separate theorem and has passed its\nown whole-proof reviews.')
assert displays(s)==displays(before);p.write_text(s)
p=R/'HODGE_DIVISION.tex';s=p.read_text()
for anchor,extra in [
 ('agents/sixfolds/rm_mixed_star_cubic_obstruction_section.tex',list(paths.values())),
 ('agents/sixfolds/rm_positive_defect_bibitems.tex',['agents/sixfolds/rm_reflexive_bibitems.tex'])]:
 a=r'\input{'+anchor+'}';s=change(s,a,a+'\n'+'\n'.join(r'\input{'+x+'}' for x in extra))
s=change(s,'and gives trace-kernel dimension at least $1+3s$, for $s$ support orbits.',r'''and gives trace-kernel dimension at least $1+3s$, for $s$ support orbits.
SF-E834 now extends mixed discriminant nonnegativity and its equality
characterization to stable reflexive sheaves. Translation averaging
over complete-intersection surfaces supplies precisely the required
Chern--Weil pairings. Equality removes mixed curvature; Bianchi and
compact transverse slices bound both pure blocks across the entire
singular set. A smooth determinant normalization and the published
Biswas extension theorem make the sheaf locally free, after which
SF-E811 gives projective flatness. Thus no stable reflexive sheaf has
the positive balanced normalized character.
SF-E835 applies this to the reflexive hulls of all stable factors of
an arbitrary semistable torsion-free sheaf. The exact discriminant
variance and effective support cycles remove surface defects; the
normalized cubic character removes curve defects. Actual extension
classes lift across the remaining finite set by local cohomology in
dimension four. Consequently the actual reflexive hull has the precise
locally free stable-factor filtration required by SF-E818.
Every semistable torsion-free balanced sheaf is therefore excluded
from weak equivariant semiregularity, without an equivariant choice
of stable-factor filtration.''')
s=change(s,'include unstable locally free objects, singular stable factors or\nreflexive hulls, the nonreduced equal-length modifications just described,',
 'include unstable torsion-free objects, the nonreduced equal-length\nmodifications just described,')
p.write_text(s)
stable=('SF-E834 proves mixed discriminant nonnegativity for every slope-stable reflexive sheaf on the genuine polarized RM fourfold, with equality exactly for locally free projectively flat sheaves. Translated smooth surfaces and absolute Fubini give the divisor-pair ChernWeil identities; Bianchi plus clean transverse slices gives bounded tracefree curvature across curves and points; determinant normalization and published BiswasTh3.2 give the actual bundle extension. The positive balanced normalized character is impossible. ')
semi=('SF-E835 excludes every slope-semistable torsion-free balanced sheaf from weak equivariant semiregularity in E818 finite-action scope. Stable-factor reflexive hulls are stable; the mixed variance identity, E834 and strict effective-surface positivity eliminate surface defects, and the cubic character eliminates curve defects. Local cohomology below4 vanishes at the remaining finite set, so actual Ext1 classes lift and the actual hull is locally free with stable projectively flat same-slope quotients. E818 then applies; no equivariant stable filtration is assumed. ')
for r in rows:
 if r['id']=='Q5i':
  t=change(r['finding_ids_or_current_gate'],'Remaining: unstable bundles, singular stable factors/reflexive hulls,',stable+semi+'Remaining: unstable torsion-free sheaves,')
  r['finding_ids_or_current_gate']=t
new=[
 ['Q5ah','Prompt target5; singular stable-reflexive RM equality','Can a stable reflexive sheaf with singular locus furnish the positive balanced normalized character?','refuted',stable+'Whole author/root/G34 proof and exact published-input reviews PASS. No 032/Markman/Severn premise or numerical certificate.'],
 ['Q5ai','Prompt target5; all semistable torsion-free balanced sheaves','Can singular stable factors or a singular reflexive hull evade the semistable weak-semiregularity obstruction?','refuted',semi+'Whole author/root/G34 proof and local-cohomology source reviews PASS. Unstable sheaves, torsion-bearing objects and arbitrary perfect complexes remain outside.']]
rows.extend(dict(zip(fields,x)) for x in new)
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[
 ('SF-E834','targeted proof check','Root whole343-line frozen draft515d1e29 and complete360-line conversion read; whole final notation diff3467ed3f read,357-line canonical1ac992d7. PASS exact averaging/Fubini, RM divisor span, curvature sign/equality, Bianchi, compact slices, determinant rescaling, bundle extension and E811 interface. All14displays unchanged by polish; status-only integration.',paths['E834']),
 ('SF-E834 published analytic inputs','used and rechecked in this run','Root complete Biswas2011 published8-page paper read, including exactTh3.2 and full proofp77, general analytic-set hypothesis and L^n curvature. BandoSiu originalp40 image visually read; full OCRpp39,40,48,49 read, including admissibility and Th3. Root does not claim completepp45-47 reading. Author/peer complete relevantpp45-49 read. Upstream HarrisTonegawa full proof not retrieved, explicitly not claimed.','agents/sixfolds/rm_reflexive_bibitems.tex; agents/sixfolds/references_cache/bando2.jpg'),
 ('SF-E834 E811 dependency','targeted proof check','Root reread complete invoked E811 bundle proof and RM specialization through line410, including rationality of actual holonomy-algebra bundles, central curvature and finite-deck argument. Genuine RM forbids rational pure-volume lines without a simplicity hypothesis. Earlier E811 whole reviews retained; no new independent re-proof claimed.','agents/sixfolds/rm_stable_bundle_obstruction_section.tex'),
 ('SF-E834 peer audit','targeted proof check','Root entire G34 report SHA1b634d9263a3cbd8cedb9f725a0ab3bcaa1b4e0cf545dbd27231932b2fb224c9 read. Whole frozen proof and exact source scopes PASS21:29:17UTC. New analytic implications independently checked; no computation or upstream existence re-proof claimed.','agents/g34_eightfolds/bireflection/REFLEXIVE_MIXED_CURVATURE_PEER_AUDIT.md'),
 ('SF-E835','targeted proof check','Root whole257-line frozen draft11b576f3, complete273-line conversion and entire notation diff0a6a1f32 read;269-line canonical3bfeb04e PASS. Actual stable filtration/hulls, variance, effective surfaces/curves, Ext1 restriction, induction by actual extensions, reflexive identification and unchanged categorical finite-action scope checked. All10displays unchanged; no numerical premise.',paths['E835']),
 ('SF-E835 algebraic sources and E818','used and rechecked in this run','Root freshly read full Stacks0G7P statement/proof; full0A39 support triangle, exact sequence and spectral sequence; full0AVZ depth statement/proof. Root whole canonical E818 reread, including Pluecker/Albanese strict surface positivity and exact Fulton leading-support scope. No new reading of entire Fulton RiemannRoch proof claimed.','https://stacks.math.columbia.edu/tag/0G7P; https://stacks.math.columbia.edu/tag/0A39; https://stacks.math.columbia.edu/tag/0AVZ; agents/sixfolds/rm_positive_defect_obstruction_section.tex'),
 ('SF-E835 peer audit','targeted proof check','Root whole G34 report SHA9841e55c3e6cd991490ad00feed81a24d1cb7729816695871ba117964875ff30 read. Full proof/source/interfaces PASS21:31:49UTC; actual extension lifting verified without assuming double-dual exactness or nonproper GAGA. No numerical computation needed.','agents/g34_eightfolds/bireflection/SEMISTABLE_REFLEXIVE_REDUCTION_PEER_AUDIT.md')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:
 f.write('\n## Stable-reflexive equality and the full semistable torsion-free gate\n\n'+now+' — Q5ah/Q5ai refuted; Q5i strictly reduced. '+stable+semi+'The singular-hull and singular-stable-factor escape is closed in this semistable scope. Unstable, nonpure and broader derived constructions remain open. These are substantive changes after review08; source maintenance and TeX polishing are not movement. No formal hourly review is performed here.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
 f.write('\n## Singularities do not evade the semistable balanced-sheaf obstruction\n\n'+stable+semi+'This narrows the actual K-theory/perfect-complex supplier route of DEG_L S-14; it does not turn a class into a cycle. The variance and actual extension steps live in coherent K0 and Ext, and local cohomology supplies an actual sheaf extension across codimension four. The same condition-A/condition-I, Cayley-Hamilton, schemes-over-Z, realizations, weights, motives and L-function limitations recorded in the common framework persist. No additional Grothendieck archive theorem or conditional Markman/Severn/032 statement is used.\n')
out={'date_utc':now,'integrated':['SF-E834','SF-E835'],'frozen_reviewed_canonical_sha256':frozen,'canonical_sha256':{k:hashlib.sha256((R/v).read_bytes()).hexdigest() for k,v in paths.items()},'new_rows':{'Q5ah':'refuted','Q5ai':'refuted'},'strictly_reduced_main_gates':['Q5i']}
(R/'research/reflexive_semistable_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
