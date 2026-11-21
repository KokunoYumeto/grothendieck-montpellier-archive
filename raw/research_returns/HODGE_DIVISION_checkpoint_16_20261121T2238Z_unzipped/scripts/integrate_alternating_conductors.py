"""Integrate independently reviewed actual-field alternating restrictions."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
proofs={'HD-AST04--06':('research/alternating_standard_conductor_section.tex','051bdda5eccbb84c61c2e197aaec3588f8cd42427f34029736a1694bd0896777'),
        'HD-ALT08':('research/ordinary_alternating_conductor_section.tex','53a5c7f3433579520265800de4a44ee706f5a9e573c54936818beff02fadb2b8')}
reports={'HD-AST04--06':('agents/sixfolds/audit_alternating_conductor/PEER_AUDIT.md','9328b1230d22a11e518648ed81ca95191da57ecb89fd5cb2fe9433483433dfcc'),
         'HD-ALT08':('agents/sixfolds/audit_alternating_conductor/ALT08_PEER_AUDIT.md','a11ee1e30869f131f1fb1bb1b9f1c7e5bc49e0a2dd2f3370f057c84365b8f0c4')}
for path,sha in list(proofs.values())+list(reports.values()):assert hashlib.sha256((R/path).read_bytes()).hexdigest()==sha,path
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
p=R/proofs['HD-AST04--06'][0];s=p.read_text()
s=change(s,'This is a new root derivation, submitted for independent whole-proof\nreview.',
 'This new root derivation has passed the complete root and independent\n/root/sixfolds proof, source and code reviews, with separate exact\nsupplements.');p.write_text(s)
p=R/proofs['HD-ALT08'][0];before=s=p.read_text()
s=change(s,'This complete new root derivation is submitted for independent whole-proof\nreview.',
 'This complete new root derivation has passed the full root and\nindependent /root/sixfolds proof and code reviews, with separate exact\nsupplements. The cyclotomic scalar-line footer precision is incorporated.')
assert re.findall(r'\\\[(.*?)\\\]',s,re.S)==re.findall(r'\\\[(.*?)\\\]',before,re.S);p.write_text(s)
p=R/'research/alternating_standard_conductor_bibitems.tex';s=p.read_text();s=change(s,'6 August 2020. Chapter V','6 August 2020, author course notes. Chapter V');p.write_text(s)
standard=('HD-AST04--06 proves the unique actual scalar character of the rational standard tensor-wreath normalizer. '
 'Only KsubsetFsubsetQ(zetaM) is used; quadratic conductors force >=2scalar phases with the required order. '
 'Rational eigenspace multiplicities and the fourth-root all-power trace bound exclude standard tensors witht>=2 for15<=n<=19 over every non-Eisenstein originalK, '
 'throughn20 if8dividesdiscK, and throughn=5(p-1) ifoddp>=7dividesdiscK. '
 'The class-number-one remaining lower cutoffs are20,21,31,51,91,211,331,811 forK=-1,-2,-7,-11,-19,-43,-67,-163 respectively. '
 'The n15t2 profile satisfies prior numerical gates and is excluded here; no source existence is implied. ')
general=('HD-ALT08 applies the verified scalar-field argument to ALL remaining ordinary long Specht tensor labels. '
 'The exact necessary inequality is beta(n,k)<=1/(5h)+3/(5e), withh4if8dividesdiscK orh=p-1foroddp>=5dividingdiscK. '
 'It forces maxrow/column>((1+sqrt(1-4/(5h)))/2)n for alln>=15 after the separate singleStd exclusion. '
 'For the seven non-Gaussian/non-Eisenstein class-number-one fields h=4,6,10,18,42,66,162; the first threshold0.9472135955n and the other six are stronger. '
 'The n100label(94,6),degree1116764880,beta31/539 passes ALT07 but fails the h4 inequality, proving strictness outside standard/tail2 cases. '
 'The Gaussian general-shape gate stays at ALT07; larger unexcluded labels, scalar orders and tensor multiplicities are not enumerated or bounded by these inequalities. ')
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0]);assert not {'Q2cc','Q2ce'}&{r['id'] for r in rows}
(R/'research/gate_before_alternating_conductors.json').write_text(json.dumps(next(r for r in rows if r['id']=='Q2i'),indent=2)+'\n')
for r in rows:
 if r['id']=='Q2i':r['finding_ids_or_current_gate']=change(r['finding_ids_or_current_gate'],'Long-shape tensor cases for n>=15 remain. ',standard+general+'Longer unexcluded tensor cases remain. ')
rows.extend([dict(zip(fields,['Q2cc','Prompt target2; actual scalar conductors for standard tensor cores',
 'Can the stated standard tensor parameters survive when the actual original quadratic field is retained in the scalar cyclotomic field?',
 'refuted',standard+'Whole root/sixfolds proofs/source/code PASS; distinct t2/t3 and scalar tuple supplements retained.'])),
 dict(zip(fields,['Q2ce','Prompt target2; field-sensitive full long-Specht shape gate',
 'Can labels between the old ALT07 boundary and the new conductor-dependent radical boundary supply an actual rank-nine source?',
 'refuted',general+'Whole root/sixfolds proofs/dependency/code PASS; all theorem/displays unchanged by cyclotomic-line footer clarification.']))])
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
p=R/'HODGE_DIVISION.tex';s=p.read_text();anchor=r'\input{agents/imprimitive/lie_small_fields/alternating_standard_tensor_section.tex}'
s=change(s,anchor,anchor+'\n'+r'\input{'+proofs['HD-AST04--06'][0]+'}'+'\n'+r'\input{'+proofs['HD-ALT08'][0]+'}')
anchor=r'\input{research/ordinary_alternating_fixed_free_bibitems.tex}'
s=change(s,anchor,anchor+'\n'+r'\input{research/alternating_standard_conductor_bibitems.tex}')
anchor='the old finite-degree gate but fails this new one, proving strictness.'
s=change(s,anchor,anchor+r'''
HD-AST-04--06 retains the actual original field in the rational
tensor-wreath scalar coordinate. Quadratic conductors force two inertia
phases of specified orders. Rational eigenspaces and the fourth-root
trace bound exclude standard tensors through $n=19$ over every
non-Eisenstein field, through $20$ when $8$ divides the discriminant,
and through $5(p-1)$ for odd discriminant primes $p\ge7$.
HD-ALT-08 then treats all remaining long labels: the necessary tail
inequality is $\beta(n,k)\le1/(5h)+3/(5e)$, with $h=4$ in the
conductor-eight case and $h=p-1$ in the odd-prime case. The required
row or column exceeds $\tfrac12(1+\sqrt{1-4/(5h)})n$.
For $\mathbf Q(\sqrt{-2})$ this is over $0.9472135954n$;
the other six non-Gaussian/non-Eisenstein class-number-one fields
have stronger thresholds. The nonstandard label $(94,6)$ at $n=100$
shows strictness beyond ALT07. The Gaussian general-shape gate is
unchanged by this conductor argument.''')
s=change(s,'in the tensor case. Long-shape tensor constructions for $n\ge15$\nstill require separate arguments.',
 'in the tensor case. Long-shape tensor constructions outside the\nnew explicit bounds still require separate arguments.')
p.write_text(s)
events=[('HD-AST04--06 peer audit','targeted proof check',
 'Root entire sixfolds report9328b123 read. Full frozen proof051bdda5, source/code and complete D-AST01--03 dependency PASS. Independent integer group-ring t3 spectra/weighted3cycles:132eachcase,83608scalar quadruples,1436cutoffs PASS0.181133699s22:23:30UTC. Milne author-course-note status and upstream source limits explicit. Root has not whole-read peer code.',reports['HD-AST04--06'][0]),
 ('HD-ALT08 peer audit and footer precision','targeted proof check',
 'Root entire reporta11ee1e3 read. Whole initial proof1a599128 and exact final footer delta PASS, bound to53a5c7f3. Only correction: nonreal scalar line is over its cyclotomic field; restriction of scalars yields rational representation class. All theorem/displays unchanged. Independent no-SymPy polynomial/hooks supplement1068hookdimensions,252746integercomparisons PASS0.117519289s22:29:12UTC. Complete ALT03/07 dependencies reread. Root has not whole-read peer code.',reports['HD-ALT08'][0]),
 ('HD-ALT08 final-hash supplement','computation or formal certificate',
 'Root actual rerun after footer-only correction PASS22:28:58.120377UTC0.09728152099705767s, same13740exact comparisons and universal identities. Initial complete result retained in root_pending_peer JSON. No failed theorem or certificate assertion.', 'research/alternating_conductor_checked.json'),
 ('HD-AST04--06 HD-ALT08 integration','targeted proof check',
 'Root previously whole-read both proofs/checkers/outputs; both complete independent reports now read. Status-only promotion; explicit course-note metadata. Q2cc,Q2ce refuted and Q2i strictly reduced. No field equality, source existence or TeX compilation claimed.','scripts/integrate_alternating_conductors.py')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,t,o,e in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',t,o,e])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Actual quadratic conductors in the alternating supplier gate\n\n'+now+' — Q2cc and Q2ce refuted; Q2i strictly reduced. '+standard+general+'No formal review or off-schedule checkpoint.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Original-field arithmetic sharpens finite-local-system restrictions\n\n'+standard+general+'The scalar character is a line over a cyclotomic field; restriction of scalars gives a rational representation/lambda-ring class. Its conductor restricts actual weight-one local systems and condition-A suppliers (cote16 scan050; SIGN_NEXT SN-C03/C04), without creating cycles through condition I. The common EGA/SGA/FGA, schemes-over-Z, K-theory, projector and motivic/L-function frame remains; no new Markman, Severn or032 premise.\n')
out={'date_utc':now,'reviewed_proofs':proofs,'whole_read_peer_reports':reports,
     'canonical_sha256':{k:hashlib.sha256((R/v[0]).read_bytes()).hexdigest() for k,v in proofs.items()},
     'new_rows':['Q2cc','Q2ce'],'strictly_reduced_main_gate':'Q2i'}
(R/'research/alternating_conductors_integration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
