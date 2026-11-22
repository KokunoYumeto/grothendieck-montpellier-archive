"""Integrate the wholly checked E836 and its explicit scalar-inference boundary."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
path='agents/sixfolds/rm_ci_point_quantization_obstruction_section.tex';p=R/path
frozen='9485999671e40a440ccf9fd96bd0a749307c17d69fa75dbb5cc771ab8095b048';assert hashlib.sha256(p.read_bytes()).hexdigest()==frozen
boundary='research/ci_integrable_cross_minor_boundary.tex'
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
before=p.read_text();s=change(before,r'''\textbf{Status:} complete new proof submitted for independent
whole-proof review.''',r'''\textbf{Status:} complete new proof checked in full by the author,
/root and /root/imprimitive. The root has also read the entire canonical
conversion; the peer audit concerns the complete frozen draft.
All twenty-one display blocks are unchanged by conversion.''');assert re.findall(r'\\\[(.*?)\\\]',s,re.S)==re.findall(r'\\\[(.*?)\\\]',before,re.S);p.write_text(s)
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0]);assert not {'Q5aj','Q5boundary1'}&{r['id'] for r in rows}
(R/'research/gates_before_ci_point.json').write_text(json.dumps({r['id']:r for r in rows if r['id']=='Q5i'},indent=2)+'\n')
p=R/'HODGE_DIVISION.tex';s=p.read_text()
for anchor,extras in [('agents/sixfolds/rm_semistable_reflexive_reduction_section.tex',[path,boundary]),('agents/sixfolds/rm_reflexive_bibitems.tex',['agents/sixfolds/rm_ci_point_quantization_bibitems.tex'])]:
 a=r'\input{'+anchor+'}';s=change(s,a,a+'\n'+'\n'.join(r'\input{'+e+'}' for e in extras))
anchor='from weak equivariant semiregularity, without an equivariant choice\nof stable-factor filtration.'
s=change(s,anchor,anchor+r'''
SF-E836 independently restricts the actual point-torsion/point-cokernel
class: if both defects are free over one common finite complete
intersection admitting a commuting generator triple for either
complementary bivector, the two first-order deformations are impossible.
Both orders of the actual companion-matrix equations yield the scalar
cross-minor identities; the commuting triple then contradicts the
published Jacobian-socle theorem. This includes every such complete
intersection of embedding dimension at most three, and all coordinate
power ideals. HD-CI-B1 records an actual length-sixteen integrable
counterexample to extending the scalar inference without that hypothesis.
It does not solve the stronger matrix equations or produce a supplier.''')
p.write_text(s)
gate=('SF-E836 excludes every nontrivial actual point modification with common Artin complete-intersection defect modules T=A^n,Q=A^m, where a regular four-generator presentation has three generators commuting moduloI under either complementary constant bivector. Supertrace forcesm=n; both companion orders Cpi Bij=Ppiij I=Bij Cpi imply scalar cross minors; the commuting triple kills the mixed wedge, contradicting the published nonzero Jacobian socle. It covers every such CI of embeddingdimension<=3 via formal mixed-plane elimination and all coordinate power ideals. Actual coherent rank32 balanced examples with Extdimension6m²length(A) exist but admit no weakly semiregular action in the stated E819 scope. No all-CI or arbitrary-module claim. ')
for r in rows:
 if r['id']=='Q5i':r['finding_ids_or_current_gate']+=' '+gate
rows.append(dict(zip(fields,['Q5aj','Prompt target5; E819 actual local quantization and published CI socle','Can a common complete-intersection point defect with a commuting generator triple evade the balanced weak-semiregularity obstruction?','refuted',gate+'Whole author/root/peer proof checks and exact published-source reading PASS.'])))
rows.append(dict(zip(fields,['Q5boundary1','SF-E836 inference boundary; explicit root construction','Do the scalar cross-minor equations alone force the Jacobian to vanish for every integrable complete intersection?','refuted','HD-CI-B1: I=(ell1²,ell2²,ell3²,ell4²) with the displayed rational invertible matrix gives all36 scalar cross minors zero but Jacobian=-64/5 times the nonzero top socle. Both root and separate peer full-proof/code checks PASS. This boundary is not main-gate movement and is not a companion-matrix solution or module deformation.'])))
with q.open('w',newline='') as f:w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[('SF-E836','targeted proof check','Root whole243-line frozen draft e63e9b1c and complete460-line canonical94859996 read; author checker,fullJSON,bibliography,conversionJSON read. All21displays byte-identical. PASS both companion orders, formal generator covariance, mixed-plane elimination, global bridge and actual examples. Root has not read conversion diff, but both complete endpoints were read.',path),('SF-E836 socle and prior interfaces','used and rechecked in this run','Root fresh original EisenbudUlrich2019 Th7.1 statementp210 and complete invoked AppA1/A3/A5 statements/proofspp222-225 read; no full following Th7.1 proof reading or rendered-page visual claim. Root reread invoked E819 map-lifting and characteristic-map ranges and E815 balanced actual bundle; earlier BF/S21 input reviews retained.','agents/sixfolds/rm_ci_point_quantization_bibitems.tex'),('SF-E836 peer audit','targeted proof check','Root entire imprimitive report SHA69e57364e74d8882554e00a1db78c9ba1afe039c9b98b1eee09e582dab29a096 read. Full frozen draft, author code, primary socle proof and E819 interface PASS; independent free-associative/integer polynomial check0.001669476s21:48:14UTC. Peer did not claim canonical conversion reread; root has not whole-read peer code.','agents/imprimitive/audit_ci_point/PEER_AUDIT.md'),('HD-CI-B1','targeted proof check','Root whole original proof and complete newly typeset canonical proof read. Actual rational invertible gradient construction, length16 algebra, all scalar minors, nonzero Jacobian and generator-covariance boundary PASS. Separate peer whole-proof/code audit also read completely; no module solution inferred.',boundary),('HD-CI-B1 exact supplement','computation or formal certificate','Actual root computation2026-11-21T21:43:07.590990+00:00 PASS0.079846188s;36 ordered minors, actual gradient and nonzero socle. ScriptSHA1aff0c56df19e2fd1b1b889e1530c2741c6c2a1526521c8cda22082d1aa5f6bc. This records the completed run, not a rerun now.','research/ci_integrable_cross_minor_boundary_checked.json'),('HD-CI-B1 peer audit','targeted proof check','Root entire sixfolds report SHA2fd505b0e3b11b5926a7644902dab1b16cd3e7768e9782e858cec73b78c2395c read. Whole original proof/code PASS; separate Fraction/bitmask/polynomial reconstruction0.001124912s at21:46:34UTC. Root has not whole-read peer code. No main-gate movement.','agents/sixfolds/INTEGRABLE_CI_BOUNDARY_PEER_AUDIT.md')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Common complete-intersection point-defect restriction\n\n'+now+' — Q5aj refuted; Q5i strictly reduced. '+gate+'HD-CI-B1/Q5boundary1 separately refutes an overbroad scalar inference but is explicitly not main-gate movement. No formal review is performed here.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Actual common-CI local deformation restriction\n\n'+gate+'HD-CI-B1 prevents promoting scalar compatibility to an unrestricted CI theorem. This concerns actual coherent sheaves and their local perfect resolutions/K-theory on Artin subschemes; finite jets descend to the algebraic scheme without asserting algebraicity of a formal logarithm. The condition-A supplier boundary is cote16 scan050 (SIGN_NEXT SN-C03/C04), with condition I scan049/cote44 Th4 and resultant inversion scans048-049 unchanged. The common realization/weight/motive/L-function framework supplies no new detector. No new Markman/Severn/032 premise is introduced.\n')
out={'date_utc':now,'integrated':['SF-E836','HD-CI-B1'],'E836_frozen_sha256':frozen,'canonical_sha256':{path:hashlib.sha256((R/path).read_bytes()).hexdigest(),boundary:hashlib.sha256((R/boundary).read_bytes()).hexdigest()},'new_rows':{'Q5aj':'refuted','Q5boundary1':'refuted; explicit boundary only'},'strictly_reduced_main_gates':['Q5i'],'excluded_from_movement':['HD-CI-B1','Q5boundary1']}
(R/'research/ci_point_integration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
