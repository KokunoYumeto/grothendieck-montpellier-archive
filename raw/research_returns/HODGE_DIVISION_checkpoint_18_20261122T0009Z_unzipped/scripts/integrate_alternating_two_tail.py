"""Promote whole-proof reviewed D-ATT01--03, preserving the frozen math."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
proof='agents/g34_eightfolds/bireflection/alternating_two_tail_section.tex'
report='agents/imprimitive/audit_alternating_two_tail/PEER_AUDIT.md'
frozen='663aea29319e2ce97288077ba58195eaa6946f1bd5eda3033589c5b95b84ec3b'
reporthash='52e5c87cdd650a5d08573ea365d7c515dae9de0ef3977da06e0f251b69050b37'
assert hashlib.sha256((R/proof).read_bytes()).hexdigest()==frozen
assert hashlib.sha256((R/report).read_bytes()).hexdigest()==reporthash
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
p=R/proof;before=s=p.read_text()
s=change(s,'This is a new complete author derivation, submitted for independent\nwhole-proof review.',
 'This complete new author derivation has passed whole-proof readings\nby the root and independent /root/imprimitive reviewer, with separate\nexact computational supplements.')
assert re.findall(r'\\\[(.*?)\\\]',s,re.S)==re.findall(r'\\\[(.*?)\\\]',before,re.S)
p.write_text(s)
finding=('D-ATT01--03 treats ordinary two-box-tail tensor cores UP=(n-2,2) andEX=(n-2,1,1), allt>=2, full compatible scalar/outer/permutation normalizers. '
 'Exact minimum projective supports are n-3 andn-2; all-power traces are bounded below by-1 and-floor((n-1)/2). '
 'The unique actual scalar coordinate, KsubsetFsubsetQ(zetaM), and two conductor-marked inertia entries exclude BOTH labels for15<=n<=39 over every non-EisensteinK. '
 'If8dividesdiscK, EXn40 is excluded too. Ifoddp>=7dividesdiscK,h=p-1, UP is excluded throughn=10h-1 andEX throughn=10h. '
 'Remaining UP lower cutoffs40,40,60,100,180,420,660,1620 andEX40,41,61,101,181,421,661,1621 correspond respectively toK=-1,-2,-7,-11,-19,-43,-67,-163. '
 'Atn39t2 both labels satisfy ALT07beta36/703<.1 but fail the new Gaussian obstruction, proving strictness. '
 'Larger tensor parameters and other labels remain open; no actual source or cycle is asserted. ')
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0]);assert 'Q2cd' not in {r['id'] for r in rows}
old=next(r for r in rows if r['id']=='Q2i');(R/'research/gate_before_alternating_two_tail.json').write_text(json.dumps(old,indent=2)+'\n')
old['finding_ids_or_current_gate']=change(old['finding_ids_or_current_gate'],'Longer unexcluded tensor cases remain. ',finding+'Longer unexcluded tensor cases remain. ')
rows.append(dict(zip(fields,['Q2cd','Prompt target2; two-box-tail tensor cores',
 'Can ordinary UP/EX tensor cores in the stated conductor-dependent degree ranges supply an actual rank-nine source?',
 'refuted',finding+'Complete root and independent imprimitive proof/source/code audits PASS; independent pair-orbit and author eigenvalue spectra retained.'])))
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
p=R/'HODGE_DIVISION.tex';s=p.read_text();anchor=r'\input{research/ordinary_alternating_conductor_section.tex}'
s=change(s,anchor,anchor+'\n'+r'\input{'+proof+'}')
anchor='unchanged by this conductor argument.'
s=change(s,anchor,anchor+r'''
D-ATT-01--03 gives stronger exact support and trace estimates for both
two-box-tail cores. For every tensor count at least two, both labels
are excluded through $n=39$ over every non-Eisenstein field. The
conductor-eight exterior case also excludes $n=40$; for an odd
discriminant prime $p\ge7$, the unordered-pair and exterior ranges
extend respectively through $10(p-1)-1$ and $10(p-1)$.
The degree-$39$ profiles pass the preceding shape gate, giving a
separate strict reduction. Larger unexcluded tensor ranges remain.''')
p.write_text(s)
events=[('D-ATT01--03 root full proof and dependencies','targeted proof check',
 'Root whole frozen proof663aea29, every line of author checker and full correct output read; all support/trace/scalar/conductor/Hurwitz endpoints PASS. Root freshly reread complete D-UP01--03 and D-EX01--03 proof files. Wrong output filename lookup corrected without mathematical execution. Author actual certificate22:29:53.938488UTC0.969025051s:11224partitions777780spectral entries672tensor/swapcases8950trace and8950phasechecks. Root did not rerun author program.',proof),
 ('D-ATT01--03 independent peer audit','targeted proof check',
 'Root entire report52e5c87c read. Imprimitive complete independent whole-proof/source/code PASS, including fresh complete Milne ChVpp157--159. Its independently authored actual signed/unsigned pair-orbit certificate PASS22:32:22.399542UTC1.778241281s:11224partitions583996pairorbits777780spectralentries5958arithmeticcases. No repair requested. Root has not whole-read peer code.',report),
 ('D-ATT01--03 integrated restriction','targeted proof check',
 'Status-only canonical promotion; all displayed mathematics unchanged. Q2cd refuted and Q2i strictly smaller. Current t2 all-n research is an unreviewed separate future draft and is not counted. No TeX compilation or positive cycle claim.','scripts/integrate_alternating_two_tail.py')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,t,o,e in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',t,o,e])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Two-box-tail alternating tensor restrictions\n\n'+now+' — Q2cd refuted; Q2i strictly reduced. '+finding+'Complete root and independent peer readings PASS. No formal review or checkpoint occurred in this integration.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Exact small-tail supports refine the finite supplier gate\n\n'+finding+'This constrains weight-one local systems and possible condition-A cycle suppliers, not positivity/condition-I cycle creation (cote16scan050, cote44Th4, SIGN_NEXT SN-C03/C04 and SN-14). The scalar line is cyclotomic and restriction of scalars gives its rational representation/K-theory class. The common schemes-over-Z, EGA/SGA/FGA, lambda-ring, projector and motivic/L-function frame is unchanged; no new Markman, Severn or032 premise.\n')
out={'date_utc':now,'proof':proof,'frozen_sha256':frozen,'canonical_sha256':hashlib.sha256((R/proof).read_bytes()).hexdigest(),'whole_read_peer_report':report,'peer_sha256':reporthash,'new_row':'Q2cd','strictly_reduced_main_gate':'Q2i'}
(R/'research/alternating_two_tail_integration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
