"""Integrate fully written and whole-reviewed HOS07--10 and ALT06a/b."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
paths={'HOS5':'agents/g34_eightfolds/bireflection/higher_odd_symplectic_five_section.tex','ALT87':'research/ordinary_alternating_87_section.tex'}
frozen={'HOS5':'3fb15463d75bfa8da6167a57e2905b76f6e42a46ec7f7148b641b611d0a47a67','ALT87':'5ab4d6447f1b04c0d5c3b52afc5dbaf1a5450cd1d388034d51e3cd68f251cd79'}
for k,p in paths.items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==frozen[k]
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert all(r['id'] not in ('Q2bo','Q2bp') for r in rows)
(R/'research/gates_before_hos5_alt87.json').write_text(json.dumps({r['id']:r for r in rows if r['id']=='Q2i'},indent=2)+'\n')
p=R/paths['HOS5'];s=p.read_text();p.write_text(change(s,'This is a complete new elementary proof, currently awaiting independent\nwhole-proof review. Its character-theoretic construction is the explicit','This complete new elementary proof has passed independent whole-proof\nreviews by /root and /root/imprimitive. Both also read the full author\nchecker; the peer separately reconstructed the exact finite arithmetic.\nIts character-theoretic construction is the explicit'))
p=R/paths['ALT87'];s=p.read_text();p.write_text(change(s,'New root derivation, awaiting independent whole-proof review.','New root derivation, whole-read by the author and independently\nreviewed in full by /root/imprimitive. Both mathematical reviews pass;\nindependent exact rational and Young-diagram checks also pass.'))
p=R/'research/root_bibitems.tex';s=p.read_text();p.write_text(change(s,'1(3) (2019), 295--323, doi:10.2140/tunis.2019.1.295.','1(3) (2019), 295--320, doi:10.2140/tunis.2019.1.295.'))
p=R/'HODGE_DIVISION.tex';s=p.read_text()
for anchor,addition in [('agents/g34_eightfolds/bireflection/higher_odd_symplectic_section.tex',paths['HOS5']),('research/ordinary_alternating_long_row_obstruction.tex',paths['ALT87']),('agents/imprimitive/orthogonal_levels/orthogonal_level_bibitems.tex','agents/g34_eightfolds/bireflection/higher_odd_symplectic_five_bibitems.tex')]:
 a=r'\input{'+anchor+'}';s=change(s,a,a+'\n'+r'\input{'+addition+'}')
s=change(s,'Only $q=3,5$ remain in this higher odd-symplectic family.',r'''D-HOS-07--10 now excludes all higher $q=5$ cores, with arbitrary
mixed ranks, full compatible normalizers and tensor permutations.
Opposite radicals give a trivial-isotypic proportion at most one half;
the exact Heisenberg carrier argument includes defining-characteristic
order. The resulting normalizer support is $31e/250$. Every ordinary
core factor is self-dual, so the original imaginary character field
forces a nontrivial form multiplier. Two such inertias and the other
ten force $e\le25<250$, the elementary factor-degree floor.
Thus only $q=3$ remains among the single-field higher odd-symplectic
cases. No additional arbitrary mixture of $q=5$ with the previous
nonselfdual higher-field cases is asserted here.''')
s=change(s,'at least $250$. The scalar single-factor',r'''at least $250$. HD-ALT-06a/b keeps the exact first-row square-content
contribution and strengthens the remaining row or column bound to
$87n/100$. Its quantitative necessary inequality is
$\delta(n,k)\le1/10+3/(5e)$ for the explicitly given tail function.
The excluded annulus gives $e<2000$ for $n\ge30$, against the
precise cubic degree floor, and $e<54$ at the fifteen smaller endpoints.
The scalar single-factor''');p.write_text(s)
hos=('D-HOS-07--10 excludes arbitrary mixed-rank higherSp(q5) cores with all compatible normalizers: opposite-radical and defining-characteristic carrier arguments give support31/250, every ordinary factor is selfdual, and the actual nontrivial multiplier budget gives e<=25<250. Onlyq3 remains among single-field higher odd-symplectic cases; no extra mixture ofq5 with nonselfdual higher-field cases is asserted. ')
alt=('HD-ALT06a/b strengthens this to a row/column>87n/100 by retaining the exact first-row square-content term. The explicit necessary support inequality is delta(n,k)<=1/10+3/(5e). The excluded annulus gives e<2000 for n>=30 against the cubic degree floor, and e<54 for15<=n<=29 against minimum90. ')
for r in rows:
 if r['id']=='Q2i':
  t=change(r['finding_ids_or_current_gate'],'onlyq3/q5 remain in that family. ',hos)
  r['finding_ids_or_current_gate']=change(t,'The all-degree scalar single-factor standard,',alt+'The all-degree scalar single-factor standard,')
newrows=[['Q2bo','Prompt target2; higher ordinary symplectic cores overF5','Can higher symplectic q5 factors supply the actual period-rank-nine inducing block after compatible normalizers, scalar phases or tensor mixing?','refuted',hos+'Whole author/root/peer mathematical audits and independent exact arithmetic PASS; no character-table premise.'],['Q2bp','Prompt target2; sharper ordinary alternating tail','Can a surviving transitive ordinary alternating factor have maximal row/column at most87n/100?','refuted',alt+'Whole root/peer mathematical readings PASS; all15 exact endpoints and877 supplemental Young diagrams checked independently. Longer shapes remain open.']]
rows.extend(dict(zip(fields,x)) for x in newrows)
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[
 ('D-HOS-07--10','targeted proof check','Root read entire frozen proof in bounded untruncated chunks, all206 lines of author checker and full author JSON. PASS radical generation, fixed-space half bound, exact Fourier bound including defining characteristic, all q5 normalizer cases, tensor support and actual multiplier/Hurwitz obstruction. Status-only canonical change.',paths['HOS5']),
 ('D-HOS-07--10 independent audit','independent re-proof','Imprimitive whole-proof/source/author-code audit PASS20:34:28UTC at3fb15463; root read full report SHAa38f2efff88c74cc9d0b32332382f451419c87ae9865cc86bcb181ef9029960a. Independent0.468551252s:480GSp2 matrices/19200commutators,4992nonsquare selfadjoint cases,496fullquadratic carriers, parity and constants. Root does not claim whole peer-code reading.','agents/imprimitive/audit_symplectic_five/PEER_AUDIT.md'),
 ('D-HOS-10 factorization source','used and rechecked in this run','Root freshly opened full19-page Vinroot authorPDF and read Th1p1, char-not2 hypothesis, and similitude conventionp2. Published LMA52(2004)385-403 DOI10.1080/03081080412331316079. Cited published Wonenburger factorization; original Wonenburger proof not freshly read. Prior LiXia14/HHM35/4 retained, peer rechecked.','agents/g34_eightfolds/bireflection/higher_odd_symplectic_five_bibitems.tex; https://www.math.wm.edu/~vinroot/gspfactor.pdf'),
 ('HD-ALT-06a/b','targeted proof check','Root whole mathematical reading PASS and entire repaired final proof reread at5ab4d644. First-row squares, monotonicities, full normalizer, actual multiplier, strict ceilings, all endpoints and unsplit Rasala degree checked. Earlier display/control-character repairs retained; no theorem repair.',paths['ALT87']),
 ('HD-ALT-06a/b author arithmetic','computation or formal certificate','Actual exact checker PASS0.067912614s, universal rational identities and15endpoints. Initial SymPy structural-equality assertion retained and corrected by expanding difference. No group exhaustion.','research/check_alternating_87.py; research/alternating_87_checked.json; research/alternating_87_attempts.json'),
 ('HD-ALT-06a/b independent audit','independent re-proof','Imprimitive full proof/source/author-code audit PASS20:37:32UTC. Root read full report SHA396557e069f4668ed1a229a087c457d5f6b4b6c3a1eb4016f32cedc63ca51adb. Independent sparse-Fraction reconstruction PASS0.034737581s, identities,15endpoints,877Young diagrams n15-40. No root arithmetic imported; root does not claim whole peer-code reading.','agents/imprimitive/audit_alternating_87/PEER_AUDIT.md'),
 ('HD:GKT2019 citation precision','used and rechecked in this run','Peer publisher metadata/PDF confirm295-320; corrected bibliography from295-323. Root reopened MSPPDF, reread exactp312degree consequence and requestedp320render. Root landingXHTML fetch failed unsupported content type, not claimed retrieved. Mathematical input unchanged; no semisimple-regular hypothesis imported.','research/root_bibitems.tex; https://msp.org/tunis/2019/1-3/tunis-v1-n3-p01-p.pdf')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Higher symplectic q5 exclusion and87-percent alternating gate\n\n'+now+' — Q2bo and Q2bp refuted; Q2i strictly reduced. '+hos+alt+'These proved restrictions occur after review08. Rechecks and bibliography correction are not separate movement. No hourly review is performed here.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Remaining q3 symplectic cases and longer alternating labels\n\n'+hos+alt+'These are necessary restrictions on actual condition-A curve suppliers, with original imaginary-field inclusion and actual polarized Shapiro/period factorization. No missing cycle supplier or existence conclusion follows. EGA/SGA, lambda-ring, K-theory and realizations retain their common-framework placement. Condition-I division, Cayley-Hamilton inversion, motivic/L-function scope and conditional Markman/Severn/032 status are unchanged.\n')
out={'date_utc':now,'integrated':['D-HOS-07--10','HD-ALT-06a/b'],'frozen_reviewed_sha256':frozen,'canonical_sha256':{k:hashlib.sha256((R/v).read_bytes()).hexdigest() for k,v in paths.items()},'new_rows':{'Q2bo':'refuted','Q2bp':'refuted'},'strictly_reduced_main_gates':['Q2i']}
(R/'research/hos5_alt87_integration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
