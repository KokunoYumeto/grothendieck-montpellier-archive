"""Integrate the independently reviewed odd-natural genuine Spin source proof."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, io, json, re
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
p='agents/imprimitive/spin_odd/spin_odd_extension_section.tex'
peer='agents/g34_eightfolds/bireflection/SPIN_ODD_EXTENSION_PEER_AUDIT.md'
assert hashlib.sha256((R/p).read_bytes()).hexdigest()=='a5b4c58088ddd71709ff7067670bd9d2ce71f25a02a0710cdfb557db79ca9e44'
assert hashlib.sha256((R/peer).read_bytes()).hexdigest()=='f7e3234f30ba22502cf52ad7f2ddcbea46361adcc0ac684589b09bfc23d63b7c'
s=before=(R/p).read_text()
a='Independent whole-proof reviews are pending.'
b='The complete root contributor reading and the separate\n/root/g34\\_eightfolds whole-proof/source/code audit have passed.\nRoot supplied the order-four strategy; independent origin is not claimed\nfor that contribution. Distinct exact carrier reconstructions are retained.'
assert s.count(a)==1;s=s.replace(a,b)
assert re.findall(r'\\\[(.*?)\\\]',before,re.S)==re.findall(r'\\\[(.*?)\\\]',s,re.S)
(R/p).write_text(s)
main=(R/'HODGE_DIVISION.tex').read_text()
anchor=r'\input{agents/sixfolds/spin_lifting/spin_even_extension_section.tex}'
assert main.count(anchor)==1;main=main.replace(anchor,anchor+'\n'+r'\input{'+p+'}')
a='Odd natural\ngenuine-Spin modules remain a separate pending extension.'
b='''D-OL-22--24 supplies the separate odd-dimensional genuine-Spin
argument. Its order-four Heisenberg carrier covers both natural
$SO$ cosets, while higher two-power roots are handled by their
squares and the published restricted-support estimate. Thus
every odd-characteristic transitive Spin factor, with arbitrary
represented central kernel and any nontrivial complex irreducible
module, satisfies $d\\le1133$ in odd dimension and $d\\le1134$
in even dimension. The same source contradiction excludes mixed
large-dimensional factors of both parities.'''
assert main.count(a)==1;main=main.replace(a,b);(R/'HODGE_DIVISION.tex').write_text(main)
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0]);assert not any(x['id']=='Q2cm' for x in rows)
finding=('D-OL22--24 excludes all actual rank-nine sources with arbitrary represented odd-characteristic Spin factors of ODD natural dimension d>=1135, with every nontrivial complex irreducible module and all compatible scalars/outers/factor permutations. '
 'The new q3 order4 carrier for g^2=-reflection covers BOTH SO cosets; quotient fixed dimensions N-1,2N-2,N-1 yield7a/32 after every linear and nonlinear multiplicity sector. '
 'Higher2-powers are excluded by applying LST to the square in Omega. Only projective negative reflections remain below delta; exactly12 actual one-factor generators contradict perfectness on their common perpendicular. '
 'With D-OL21 this covers mixed odd-characteristic Spin factors of both parities: transitive d<=1133 odd andd<=1134 even, without ordinary descent. '
 'These strictly replace the earlier huge genuine-Spin odd-dimensional gate; no source or cycle is asserted at surviving dimensions. ')
row=next(x for x in rows if x['id']=='Q2i');old=dict(row);row['finding_ids_or_current_gate']+=' '+finding
rows.append(dict(zip(fields,['Q2cm','Prompt target2; odd-natural genuine Spin and all-order normalizers',
 'Can arbitrary genuine odd-natural Spin factors d>=1135 provide the actual rank-nine source?', 'refuted',finding+'Whole author/root-contributor and independent peer proofs/code/interfaces PASS.'])))
out=io.StringIO();w=csv.DictWriter(out,fields,delimiter='\t');w.writeheader();w.writerows(rows);q.write_text(out.getvalue())
(R/'research/gate_before_spin_odd.json').write_text(json.dumps(old,indent=2)+'\n')
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['D-OL22--24 independent report and integration',now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION','targeted proof check',
 'Root read entire peerf7e3234f after complete contributor proof/code/output/source reading. Peer independent whole frozen proof and every author-code line PASS; own59778dual maps729actualWeyl matrices59778trace and59778square-kernel coefficient checks, exact characteristic-zero carrier spectra with independent modular kernel ranks. FirstPASS1.192861824s23:19:31UTC; added explicit characteristic-zero bridge then finalPASS0.467313632s23:19:59UTC. No failed assertion. Root did notwhole-readpeer code. All21mathdisplaysunchanged bystatuspromotion. Q2cmrefuted,Q2istrictlyreduced; no compilationclaim.',peer])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Genuine odd-natural Spin closure\n\n'+now+' — Q2cm refuted; Q2i strictly reduced afterreview10. '+finding+' No formalreview or checkpoint in this integration.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## The odd-dimensional central-cover boundary\n\n'+finding+' This acts on finite-cover local systems and their representation lambda-rings/K-theory, hence shrinks condition-A suppliers (cote16scan050;SIGN_NEXT SN-C03/C04). It supplies no positive detecting cycle; the condition-I, schemes-over-Z, EGA/SGA/FGA, projector and motivic framework remains as previously located. Markman, Severn and032 retain their conditional status.\n')
rec={'date_utc':now,'new_row':'Q2cm','strictly_reduced_main_gate':'Q2i','canonical_sha256':hashlib.sha256(s.encode()).hexdigest(),'frozen_sha256':'a5b4c58088ddd71709ff7067670bd9d2ce71f25a02a0710cdfb557db79ca9e44','peer':peer,'display_changes':False}
(R/'research/spin_odd_integration.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2))
