"""Record the independently rechecked literal rational specialization."""
from pathlib import Path
import csv
r=Path(__file__).resolve().parents[1]
with (r/'notes/A_specialization_results.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages','notes'])
 w.writerow(['A-025','Literal T=1 specialization is Sullivan polynomial forms for all rings and simplicial sets; global finite weights fail on infinite X','Proved; graded variant refuted','sections/A_rational_specialization.tex','A-001;B-05;Kan homotopy lifting','136:12','Rechecks R2 and S3-136-002-141-CE008; infinite discrete counterexample has no finite certificate requirement.'])
with (r/'notes/A_specialization_CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome'])
 for ident in ['A-025','S3-136-002-141-CE008']:
  w.writerow([ident,'2026-11-19','GPT-6 Astra (OpenAI), /root','independent re-proof','Exact quotient, horizontal acyclicity and actual-section lifting proved; finite-weight counterexample has unbounded denominators.'])
  w.writerow([ident,'2026-11-19','GPT-6 Astra (OpenAI), /root/automorphisms','targeted proof check','Independent audit passed torsion, quotient algebra, Kan lifting, kernel and infinite-discrete counterexample.'])
