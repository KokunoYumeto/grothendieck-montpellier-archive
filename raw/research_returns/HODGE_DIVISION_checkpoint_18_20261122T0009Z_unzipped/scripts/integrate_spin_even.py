"""Integrate the completely reviewed genuine even-natural Spin extension."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, io, json, re

R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
p='agents/sixfolds/spin_lifting/spin_even_extension_section.tex'
peer='agents/g34_eightfolds/bireflection/SPIN_EVEN_EXTENSION_PEER_AUDIT.md'
assert hashlib.sha256((R/p).read_bytes()).hexdigest()=='875c5067c0a2e6c399098eb878bcc00b0f9bdb5551ef178cd840a4a42e4a01f2'
assert hashlib.sha256((R/peer).read_bytes()).hexdigest()=='6df27d68330ae2bcb05c35512f73d82c5c52d511681a76f6299423d847502737'
s=before=(R/p).read_text()
a='New author derivation, D-OL19--21. Independent and root whole-proof reviews are pending.'
b='New author derivation, D-OL19--21. The complete root canonical proof/code reading and the independent /root/g34\\_eightfolds whole-proof/source audit have passed; distinct exact Clifford implementations are retained.'
assert s.count(a)==1;s=s.replace(a,b)
assert re.findall(r'\\\[(.*?)\\\]',before,re.S)==re.findall(r'\\\[(.*?)\\\]',s,re.S)
(R/p).write_text(s)
main=(R/'HODGE_DIVISION.tex').read_text()
anchor=r'\input{agents/imprimitive/orthogonal_lowlevels/orthogonal_even_odd_section.tex}'
assert main.count(anchor)==1;main=main.replace(anchor,anchor+'\n'+r'\input{'+p+'}')
a='Genuine spin characters retain their separate earlier bounds.'
b='''D-OL-19--21 now removes the genuine-Spin boundary in odd
characteristic and even natural dimension: every nontrivial
irreducible module of every represented Spin central quotient
is covered, giving $d\\le1134$ in this parity as well.
The even-Clifford lift and its odd bimodule prove actual
kernel preservation, while unique odd-primary radical lifts
retain all multiplicities and normalizer actions. Odd natural
genuine-Spin modules remain a separate pending extension.'''
assert main.count(a)==1;main=main.replace(a,b)
anchor=r'\input{agents/imprimitive/orthogonal_lowlevels/orthogonal_support_bibitems.tex}'
assert main.count(anchor)==1
main=main.replace(anchor,anchor+'\n'+r'\input{agents/sixfolds/spin_lifting/spin_even_extension_bibitems.tex}')
(R/'HODGE_DIVISION.tex').write_text(main)
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert not any(x['id']=='Q2cj' for x in rows)
finding=('D-OL19--21 excludes every actual rank-nine source with represented odd-characteristic Spin factors of EVEN natural dimension d>=1136, allowing every nontrivial irreducible complex module and arbitrary compatible represented central kernel. '
 'The natural even-Clifford automorphism plus odd bimodule proves actual quotient compatibility; unique odd-p radical lifts and full inverse-image Levi retain every support/multiplicity estimate. '
 'Nonzero radical weights give a>360 without ordinary descent. Low-support q3 inertia consists only of projective reflections; exactly12 one-factor bad branches contradict actual generation. '
 'Thus transitive genuine-Spin even natural dimension is necessarily d<=1134, strictly replacing the earlier huge spin bound in this parity. '
 'Odd natural genuine Spin and characteristic2 are not newly asserted here; the separate ordinary even-field theorem remains unchanged. ')
row=next(x for x in rows if x['id']=='Q2i');old=dict(row);row['finding_ids_or_current_gate']+=' '+finding
rows.append(dict(zip(fields,['Q2cj','Prompt target2; genuine even-natural Spin central quotients and full normalizers',
 'Can genuine odd-characteristic even-natural Spin factors d>=1136 provide the actual rank-nine source?', 'refuted',finding+'Root and independent whole-proof/source/code audits PASS; finite models supplement universal proofs.'])))
out=io.StringIO();w=csv.DictWriter(out,fields,delimiter='\t');w.writeheader();w.writerows(rows);q.write_text(out.getvalue())
(R/'research/gate_before_spin_even.json').write_text(json.dumps(old,indent=2)+'\n')
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 w.writerow(['D-OL19--21 independent audit read and integration',now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION','targeted proof check',
  'Root read entire peer6df27d68 after complete canonical215-line proof, every author checker line/output/source/status/bibitem. Peer complete frozen Markdown and canonical TeX/source audit PASS; independent F9 8x8 Fock matrices passed4096 products4096 trace pairs576 semilinearity128 composition512 scaling66 covariance at23:16:07UTC in0.183001543s. Root has not whole-read peer code. Status only changed, all18 displays identical. Q2cj refuted and Q2i strictly reduced; no new cycle or compilation claim.',peer])
 w.writerow(['D-OL22--24 root contributor complete proof/checker reading',now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION','targeted proof check',
  'PASS complete frozen a5b4c580 proof, every340-line checker, full127-line output and complete source/status record. Initial combined proof output clipped154 tokens at the lift interface; separate complete1--92 reading supplied all missing text. Root contributed the order4 strategy, so this is contributor verification rather than independent origin. All central sectors, multiplicities, SO cosets, higher2-powers, exact support thresholds, degree bound and actual source contradiction checked. Author first-run0.904313123s; root did not rerun. Independent G34 peer pending; not promoted by this event.','agents/imprimitive/spin_odd/spin_odd_extension_section.tex'])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Genuine even-natural Spin closure\n\n'+now+' — Q2cj refuted; Q2i strictly reduced afterreview10. '+finding+' No formalreview or checkpoint in this integration.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Genuine Spin and actual central quotients\n\n'+finding+' This is a restriction on actual finite-cover local systems, their representation lambda-rings and induced K-theoretic classes, hence on condition-A suppliers (cote16scan050;SIGN_NEXT SN-C03/C04). It produces no condition-I algebraic cycle. The existing schemes-over-Z, exact EGA/SGA/FGA and motivic frame, and conditional Markman/Severn/032 statuses, remain.\n')
rec={'date_utc':now,'new_row':'Q2cj','main_gate_strictly_reduced':'Q2i','proof_sha256':hashlib.sha256(s.encode()).hexdigest(),'frozen_canonical_sha256':'875c5067c0a2e6c399098eb878bcc00b0f9bdb5551ef178cd840a4a42e4a01f2','peer':peer,'display_changes':False,'odd_spin_status':'root/contributor whole proof and code PASS; independent peer pending'}
(R/'research/spin_even_integration.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2))
