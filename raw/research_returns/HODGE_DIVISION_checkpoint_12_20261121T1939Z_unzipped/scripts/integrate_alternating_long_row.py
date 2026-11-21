"""One-time integration of whole-reviewed HD-ALT05."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
R=Path(__file__).resolve().parents[1]
p=R/'research/ordinary_alternating_long_row_obstruction.tex'
reviewed='340aff36a1858f2933d511e1526c49789fe765140c25b70fc232828a09c5f619'
assert hashlib.sha256(p.read_bytes()).hexdigest()==reviewed
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert not any(x['id']=='Q2az' for x in rows)
s=p.read_text().replace('New root proof, read in full by its author and submitted for independent\nwhole-proof review.', 'New root proof, read in full by its author and independently by\n/root/g34\\_eightfolds; both whole-proof reviews PASS on 21 November\n2026. Separate exact arithmetic certificates also passed.')
p.write_text(s)
m=R/'HODGE_DIVISION.tex';s=m.read_text()
a=r'\input{research/ordinary_alternating_three_quarters.tex}'
assert a in s and 'ordinary_alternating_long_row_obstruction.tex' not in s
s=s.replace(a,a+'\n'+r'\input{research/ordinary_alternating_long_row_obstruction.tex}')
a='each factor has degree at least $125$.'
b='each factor has degree at least $125$. HD-ALT-05 then strengthens\nthis to a row or column longer than $6n/7$. Its tail-content\nestimate gives $e\\le144$, against an unsplit factor degree\nat least $250$.'
assert a in s;s=s.replace(a,b);m.write_text(s)
for x in rows:
 if x['id']=='Q2i':
  s=x['finding_ids_or_current_gate']
  a='HD-ALT04 further forces every transitive factor label to have a row/column>3n/4; its excluded range gives e<=64 against factor degree>=125.'
  b='HD-ALT04/05 further force every transitive factor label to have a row/column>6n/7; the final tail-content bound gives e<=144 against unsplit factor degree>=250 in the excluded annulus.'
  assert a in s;x['finding_ids_or_current_gate']=s.replace(a,b)
rows.append(dict(zip(fields,['Q2az','Prompt target2; remaining long ordinary alternating shapes','Can a transitive ordinary An factor have largest row/column between3n/4 and6n/7?','refuted','HD-ALT-05a/b for n>=15: exact tail-content estimates and Cauchy give all-normalizer nu>=5a/48. The nontrivial-multiplier budget forces e<=144, while the unsplit factor degree is at least250. Shape(12,3) at n15 witnesses a strictly smaller gate.'])))
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
now=datetime.now(timezone.utc).isoformat()
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in [
  ('HD-ALT-05a/b','targeted proof check','Complete author proof and independent whole peer report read. PASS tail-tableau bound, positive content sum, monotone tail substitutions, exact shifted cubic positivity, no halving on alternating restriction, actual ESD/tensor period budget and all-n contradiction. Only the status header changed after reviewedSHA'+reviewed+'.','research/ordinary_alternating_long_row_obstruction.tex; agents/g34_eightfolds/bireflection/ORDINARY_ALTERNATING_LONG_ROW_PEER_AUDIT.md'),
  ('HD-ALT-05 arithmetic','computation or formal certificate','Actually wrote and executed the complete exact arithmetic certificate:118502 tails for n15--100, all ratios/hook degrees/shifted polynomial identities PASS; inducing degree144 versus minimum250. Finite checks support the all-n written proof. Final boundary checks use Fraction, with no floating arithmetic.','research/alternating_long_row_certificate.py; alternating_long_row_certificate.json')
 ]:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Final long-row refinement after review05\n\n'+now+' — HD-ALT05 further narrows Q2i to ordinary An labels with row/column>6n/7, and Q2az is refuted. The complete tail-content proof and actual period obstruction have independent whole review and separate arithmetic reconstruction. For the next hourly movement assessment, ALT04/05 are one chain of strict shape-gate improvements, with the ultimate six-sevenths gate recorded; they are not artificial double-counting of a repeated result. Still longer shapes remain open.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\nHD-ALT05 strengthens the ordinary alternating supplier restriction to a first row or column exceeding six sevenths of n. This is an exact all-degree consequence of finite local-system character data and actual period factorization, not a finite search extrapolation. The condition A supplier interpretation and the separate condition I/Cayley--Hamilton/weights limitations are those explicitly stated in its proof.\n')
print(json.dumps({'finding':'HD-ALT05','date_utc':now,'reviewed_sha256':reviewed,'canonical_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
