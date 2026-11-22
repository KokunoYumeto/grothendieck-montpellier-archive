"""Integrate whole-proof reviewed D-OL16--18, ordinary scope only."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
p='agents/imprimitive/orthogonal_lowlevels/orthogonal_even_odd_section.tex'
sha='897ea4b9995e0668b4487cefeacd366645e67fe4509afe0a23b692c33418892a'
report='agents/sixfolds/audit_orthogonal_even_odd/PEER_AUDIT.md';rsha='30a7395e5b43d8764ed31367266ce7ab0c982b67d791785f023ff3eb2dfd6c68'
assert hashlib.sha256((R/p).read_bytes()).hexdigest()==sha
assert hashlib.sha256((R/report).read_bytes()).hexdigest()==rsha
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
before=s=(R/p).read_text()
s=change(s,'The full written proof\nand exact supplement pass the author check; independent review\nis pending and the result is not promoted.',
 'The complete author, root and independent /root/sixfolds\nproof, source and code readings have passed, with distinct exact\nsupplements. The result is promoted only in its stated ordinary scope.')
assert re.findall(r'\\\[(.*?)\\\]',before,re.S)==re.findall(r'\\\[(.*?)\\\]',s,re.S)
(R/p).write_text(s)
finding=('D-OL16--18 excludes every nonempty central product of ordinary odd-field orthogonal factors with even naturald>=1136, including mixedfields/dimensions, representedcentralquotients, allscalars and compatiblefactorpermutations. '
 'The nonsquare projective-involution case constructs an invariant isotropic2plane via a symmetric/Hermitian extension-field form; the actual Heisenberg radical, full Levi rank2-orbits and multiplicity-aware Weyl trace give7a/32. '
 'All other prime normalizers are treated by field descent, line radicals, or the exact LSTmu2support567 bound. Atq3 the only low-support all-order maps are projectivereflections; even-dimensional determinant parity rules out higher2power roots. '
 'The actual Hurwitz budget forces exactly12 one-factor reflections, whose commonnatural fixedspace contradicts perfectness and actual generation. '
 'Combined withOL09--15, every surviving ORDINARY transitive orthogonal factor has naturald<=1134, and oddd<=1133. Genuine spin representations remain outside this theorem and retain their earlier gate. ')
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0]);assert 'Q2cg' not in {r['id'] for r in rows}
main=next(r for r in rows if r['id']=='Q2i');(R/'research/gate_before_orthogonal_even_odd.json').write_text(json.dumps(main,indent=2)+'\n');main['finding_ids_or_current_gate']+=' '+finding
rows.append(dict(zip(fields,['Q2cg','Prompt target2; ordinary even-natural orthogonal cores over oddfields','Can the stated large ordinary orthogonal factors supply an actual rank-nine source when all nonsquare, skew, field and scalar normalizers are retained?','refuted',finding+'Whole root and independent sixfolds audits PASS; ordinary/faithful-spin distinction remains explicit.'])))
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
paper=R/'HODGE_DIVISION.tex';s=paper.read_text();anchor=r'\input{agents/imprimitive/orthogonal_lowlevels/orthogonal_three_odd_section.tex}'
s=change(s,anchor,anchor+'\n'+r'\input{'+p+'}')
s=change(s,'satisfy $d\\le1133$. Odd-field even-natural ordinary characters and\ngenuine spin characters retain their earlier bounds.',r'''satisfy $d\le1133$. D-OL-16--18 closes the remaining ordinary
even-natural odd-field case at $d\ge1136$. The nonsquare normalizer
uses an invariant isotropic two-plane and its full Heisenberg radical;
the square and field cases retain all compatible normalizers. At
$q=3$, a determinant argument leaves only projective reflections,
and twelve such actual generators contradict perfectness on their
common natural fixed space. Consequently every surviving ordinary
transitive factor has $d\le1134$, with $d\le1133$ in odd dimension.
Genuine spin characters retain their separate earlier bounds.''')
paper.write_text(s)
events=[('D-OL16--18 root complete proof/certificate','targeted proof check','Root read entire frozen897ea4b9 proof, every checker line, full correct output and source record. All extension-field forms, radical matrices/generation, fixed dual rank2orbits, Weyl carrier multiplicities, square/skew/field normalizers and exact12reflection source contradiction PASS. Author final0.184052911s22:36:42UTC recorded; root did not rerun. Existing source interfaces retained with exact locators; no fresh full upstream source reading claimed by root.',p),
 ('D-OL16--18 complete independent peer report','targeted proof check','Root entire peer30a7395e read. Full source/proof/code audit PASS; fresh complete Taylor/LST/GLT invoked passages and Li-Xia author-version scope explicit, publisher403 retained. Independent F5/F7 nondiagonal matrix/carrier supplement0.3245319s22:49:08UTC:6048rank2fixedmaps400group-laws27234Weyl identities126exactbounds. Root has not whole-read peer code.',report),
 ('D-OL16--18 integrated ordinary closure','targeted proof check','Status-only promotion; all22displays unchanged. Q2cg refuted andQ2i strictly reduced. Ordinary d<=1134, oddd<=1133. Spin extension research not promoted. No source existence or TeX compilation claim.','scripts/integrate_orthogonal_even_odd.py')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,t,o,e in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',t,o,e])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Completion of the large ordinary orthogonal exclusion\n\n'+now+' — Q2cg refuted; Q2i strictly reduced after review10. '+finding+'No formal review or checkpoint in this integration.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Ordinary orthogonal supplier rank becomes bounded\n\n'+finding+'This restricts actual l-adic/complex finite local systems and condition-A suppliers (cote16scan050;SIGN_NEXT SN-C03/C04), while preserving ordinary descent through the natural group. Heisenberg carriers are actual representations and tensor/convolution operations are in their lambda-ring/K-theory; no condition-I positivity step supplies a cycle. The common schemes-over-Z, EGA/SGA/FGA and motivic/L-function frame is unchanged; no new Markman, Severn or032 premise.\n')
out={'date_utc':now,'proof':p,'reviewed_sha256':sha,'canonical_sha256':hashlib.sha256((R/p).read_bytes()).hexdigest(),'whole_read_peer_report':report,'peer_sha256':rsha,'new_row':'Q2cg','strictly_reduced_main_gate':'Q2i'}
(R/'research/orthogonal_even_odd_integration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
