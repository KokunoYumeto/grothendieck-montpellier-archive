"""Integrate the completely reviewed rank-five common-CI obstruction."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
proof=R/'agents/sixfolds/rm_rank_five_jet_obstruction_section.tex'
peer=R/'agents/g34_eightfolds/bireflection/RANK_FIVE_JET_PEER_AUDIT.md'
frozen='9c1e72ec497ea28629e65169427ddc82e1a122904b2f11d2bfaf770eb00229ee'
assert hashlib.sha256(proof.read_bytes()).hexdigest()==frozen
assert hashlib.sha256(peer.read_bytes()).hexdigest()=='38deb8801727394099c52e1496508da5e1edf8700e6d7a30abcf616b30f7031b'
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
before=s=proof.read_text()
s=change(s,'new complete refinement submitted for independent\nwhole-proof review.',
         'complete new refinement checked in full by the author, /root\nand /root/g34\\_eightfolds. The root also read the entire canonical\nconversion and both exact certificate reports.')
s=change(s,'Its dimension is at most \\((k-a)+ea\\le ek\\).',
         'The hypothesis forces \\(e\\ge1\\): if \\(e=0\\), nilpotence gives\n\\(\\mathfrak n=\\mathfrak n^2=0\\) and hence \\(W=0\\), contrary to\n\\(\\rho>e\\). Its dimension is at most \\((k-a)+ea\\le ek\\).')
assert re.findall(r'\\\[(.*?)\\\]',s,re.S)==re.findall(r'\\\[(.*?)\\\]',before,re.S)
proof.write_text(s)
gate=('SF-E839 strengthens the regular-quadratic common-CI gate: every leading bracket pencil must have rank<=4. '
      'A square matrix cokernel annihilated by rho independent leading quadratic classes is zero whenever rho exceeds the embedding dimension; '
      'the actual companion pencil then contradicts independent Jacobian-socle bracket tuples. '
      'The intrinsic residual locus is cut out on each Gr(4,10) chart by at most216 coefficients of the36five-minors, each degree<=14. '
      'An explicit nonsquare length16 algebra has generic and both pure ranks5, identically zero E838 determinant pencil, '
      'and no commuting-triple presentation; it and every higher formal perturbation are excluded in all positive multiplicities. '
      'Thus the rank<=4 gate strictly improves E838 as well as E836/E837. Equalityrho=e fails for the abstract matrix lemma and is retained as a boundary only. '
      'No sufficiency, codimension or actual semiregular object on the residual locus is claimed. ')
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert 'Q5am' not in {r['id'] for r in rows}
(R/'research/gate_before_rank_five_jets.json').write_text(json.dumps(next(r for r in rows if r['id']=='Q5i'),indent=2)+'\n')
for r in rows:
 if r['id']=='Q5i':r['finding_ids_or_current_gate']+=' '+gate
rows.append(dict(zip(fields,['Q5am','Prompt target5; actual companion equations and rank-five leading jets',
 'Can common quadratic-CI point defects with any rank-five bracket pencil survive the weaker determinant-zero necessary condition?',
 'refuted',gate+'Whole author/root/G34 proof and code/output reviews PASS; separate exact quotient-ring supplement retained.'])))
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
p=R/'HODGE_DIVISION.tex';s=p.read_text();a=r'\input{agents/sixfolds/rm_quadratic_jet_obstruction_section.tex}'
s=change(s,a,a+'\n'+r'\input{agents/sixfolds/rm_rank_five_jet_obstruction_section.tex}')
a='It asserts no module deformation on the residual locus.'
s=change(s,a,a+r'''
SF-E839 strengthens that locus to rank at most four for every pencil.
Five independent quadratic annihilators already contradict the same
filtered image bound. Its thirty-six five-minors yield at most 216
coefficient equations, each of degree at most fourteen on a normalized
Grassmannian chart. An explicit nonsquare rank-five example has an
identically zero determinant pencil and no commuting-triple presentation,
proving strictness relative to all three preceding criteria. The equality
case for the abstract matrix lemma is explicitly false, with its own
small algebraic boundary example. No residual-locus existence follows.''')
p.write_text(s)
events=[('SF-E839 root whole canonical proof and certificate','targeted proof check',
 'Root all302canonical lines9c1e72ec, every author checker line and full19-check JSON, conversion certificate and whole G34 report read. Universal rho>e lemma, companion inverse,216degree14equations, rank5 nonsquare/no-commuting-triple strictness and actual global scope PASS. Author0.448135348s22:15:52UTC read, not rerun. No whole draft or conversion-diff reading by root claimed.',str(proof.relative_to(R))),
 ('SF-E839 peer audit','targeted proof check',
 'Root whole report38deb880 read. G34 full170-line frozen draft, author code/output, E838/E836 and fresh full E-U primary proof scopes PASS. Separate actual16basis quotient,256products,4096associativitytriples,36minors and socle supplement PASS0.274954087s22:18:11UTC. Root has not whole-read peer code.',str(peer.relative_to(R))),
 ('SF-E839 integration and e0 clarification','targeted proof check',
 'Status updated and trivial e>=1 inference made explicit in abstract lemma: e0 gives nilpotent n=n²=0 and W0, contradictingrho>e. G34 agreed in message; main quadratic application e4 unchanged. All14displays unchanged. Q5am refuted and Q5i strictly reduced. Existing citations reused, no TeX compilation.', 'scripts/integrate_rank_five_jets.py')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Five-leading-bracket refinement\n\n'+now+' — Q5am refuted and Q5i strictly reduced. '+gate+'No formal review or off-schedule checkpoint.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Stricter Artin-scheme quadratic residual locus\n\n'+gate+'This is an actual coherent/perfect-resolution obstruction to condition-A suppliers (cote16 scan050; SIGN_NEXT SN-C03/C04). The common scheme, lambda/K-theory, EGA/SGA/FGA and motivic-realization frame remains. Condition I and the Cayley-Hamilton division step do not supply the missing object.\n')
out={'date_utc':now,'finding':'SF-E839','reviewed_canonical_sha256':frozen,
     'canonical_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'display_blocks_unchanged':14,
     'new_row':'Q5am','strictly_reduced_main_gate':'Q5i'}
(R/'research/rank_five_jets_integration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
