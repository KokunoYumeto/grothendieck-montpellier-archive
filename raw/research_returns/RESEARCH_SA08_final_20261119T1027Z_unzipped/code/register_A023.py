"""Record the numerical-tail pairing theorem and its actual checks."""
from pathlib import Path
import csv
r=Path(__file__).resolve().parents[1]
with (r/'notes/A_additional_results.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages','notes'])
 w.writerow(['A-023','All filtration-preserving numerical-tail bilinear pairings; no multiplicative numerical-tail deformation','Proved; specified bridge refuted','sections/A_numerical_tails.tex','A-003;A-015','Lead L2; A.4','Full classification for J_N,J_M,J_L; finite torus and weight-four modulo-four certificate; no universal enhanced nonexistence claim.'])
with (r/'notes/A_additional_CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome'])
 w.writerow(['A-023','2026-11-19','GPT-6 Astra (OpenAI), /root','independent re-proof','Complete classification by rational localization and convergent integer evaluations; finite torus cup obstruction.'])
 w.writerow(['A-023','2026-11-19','GPT-6 Astra (OpenAI), /root/shadows_coalgebras','targeted proof check','Independent audit passed localization, degree bound, integer-sequence argument, and target vanishing obstruction.'])
 w.writerow(['A-023','2026-11-19','GPT-6 Astra (OpenAI), /root','computation or formal certificate','A_numerical_tail_pairings.py:25 exact assertions; all4 residue candidates fail; complete output in logs.'])
