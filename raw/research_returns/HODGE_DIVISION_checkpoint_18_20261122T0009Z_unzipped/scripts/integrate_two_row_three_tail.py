"""Promote the reviewed all-count ordinary (n-3,3) source exclusion."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,io,json,re
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
p='research/alternating_two_row_three_tail_section.tex'
peer='agents/g34_eightfolds/bireflection/THREE_BOX_TWO_ROW_PEER_AUDIT.md'
assert hashlib.sha256((R/p).read_bytes()).hexdigest()=='2f78ba157ecd0a5d671b682622ecc812e82086b048b6fb91bf7265fae3396096'
assert hashlib.sha256((R/peer).read_bytes()).hexdigest()=='bfb4047442ebce9b5a24a385ec38e882e307cb7c6bfb1e7f483def600b348b50'
s=before=(R/p).read_text();a='Independent review remains pending.'
b='The complete separate /root/g34\\_eightfolds proof/source/code\naudit and its distinct actual-subset reconstruction have also passed.\nShared preceding weighted-cycle authorship is explicitly disclosed.'
assert s.count(a)==1;s=s.replace(a,b)
assert re.findall(r'\\\[(.*?)\\\]',before,re.S)==re.findall(r'\\\[(.*?)\\\]',s,re.S)
(R/p).write_text(s)
main=(R/'HODGE_DIVISION.tex').read_text();anchor=r'\input{research/alternating_remaining_integer_cutoffs_section.tex}'
assert main.count(anchor)==1;main=main.replace(anchor,anchor+'\n'+r'\input{'+p+'}')
anchor=r'\input{research/alternating_standard_conductor_bibitems.tex}'
assert main.count(anchor)==1;main=main.replace(anchor,anchor+'\n'+r'\input{research/alternating_two_row_three_tail_bibitems.tex}')
anchor='main non-Eisenstein problem has at least three boxes off its long\nrow or column and satisfies the exact ALT07/ALT08 shape bounds.'
replacement=anchor+'''
HD-AT301--03 further removes the entire two-row label $(n-3,3)$,
for $n\\ge15$: a single factor is excluded over every original
field, and every transitive tensor count over non-Eisenstein fields.
Its new all-eigenvalue character-defect estimate has a full positive
constant term, so the actual natural quotient Riemann--Hurwitz
identity exceeds the permitted moving-rank budget.'''
assert main.count(anchor)==1;main=main.replace(anchor,replacement);(R/'HODGE_DIVISION.tex').write_text(main)
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0]);assert not any(x['id']=='Q2cn' for x in rows)
finding=('HD-AT301--03 excludes the ordinary two-row three-box-tail label(n-3,3) forALLn>=15: singlefactor overEVERYoriginalK, andALLtransitive tensorcounts overNON-EISENSTEINoriginalK. '
 'The new universal character-average estimate isnu(Wx)>=A ind(x)+B withA=(n^2-8n+3)/6,B=n(n-5)/6, valid forEVERYtargeteigenvalue, usingchi>=-n/2. '
 'Singlefactor actualn-letter RH givesD-2a>=n^2-8n-1>6. Two scalar marks and actualnt-letter RH plus the exactweightedcycleerror giveD-2e>B*a^(t-1)>6 for everyt>=2. '
 'The n100 label(97,3) passed earlier necessaryshape/finitegates and is now removed; no actualsourceexistencewasasserted. Otherthree-box andlargertailsremain. ')
row=next(x for x in rows if x['id']=='Q2i');old=dict(row);row['finding_ids_or_current_gate']+=' '+finding
rows.append(dict(zip(fields,['Q2cn','Prompt target2; ordinary two-row three-box-tail alternating source',
 'Can the ordinary(n-3,3)label, in any transitive tensor count andn>=15, supply the actual nonEisenstein rank-nine source?', 'refuted',finding+'Complete root and peer audits PASS; knownJames-LiebeckTh29.13 cited and entire invoked proof read.'])))
out=io.StringIO();w=csv.DictWriter(out,fields,delimiter='\t');w.writeheader();w.writerows(rows);q.write_text(out.getvalue())
(R/'research/gate_before_two_row_three_tail.json').write_text(json.dumps(old,indent=2)+'\n')
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t').writerow(['HD-AT301--03 independent audit and integration',now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION','targeted proof check',
 'Root read entire peerbfb40474 after complete author proof/code/output readings. Peer complete frozenproof/source/codePASS; own11224classes23636509actualsubsetpoints3508661orbits86216spectra PASS10.785513520s23:25:06UTC. Two auditor-only symbolic normalization/equality failures retained; no author mathrepair. Shared weighted-framework authorship disclosed. Root has not whole-readpeer code. Onlystatuschanged,15displaysidentical. Q2cnrefuted,Q2istrictlyreduced. No newcycleorcompilationclaim.',peer])
with (R/'LEDGER.md').open('a') as f:f.write('\n## All-count two-row three-box-tail exclusion\n\n'+now+' — Q2cn refuted; Q2i strictly reduced afterreview10. '+finding+' No formalreview or checkpoint in this integration.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## A three-box-tail supplier family removed\n\n'+finding+' This is an actual finite-cover/local-system obstruction in the representation lambda-ring and induced K-theory, shrinking condition-A suppliers(cote16scan050;SIGN_NEXT SN-C03/C04). It supplies no condition-I positive cycle and adds no Markman,Severn or032 premise. The existing schemes-over-Z, EGA/SGA/FGA and motivic/projector frame remains.\n')
rec={'date_utc':now,'new_row':'Q2cn','strictly_reduced_main_gate':'Q2i','canonical_sha256':hashlib.sha256(s.encode()).hexdigest(),'frozen_sha256':'2f78ba157ecd0a5d671b682622ecc812e82086b048b6fb91bf7265fae3396096','peer':peer,'display_changes':False}
(R/'research/two_row_three_tail_integration.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2))
