#!/usr/bin/env python3
from pathlib import Path
import csv,datetime,json
ROOT=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode; inherited effort not separately exposed; run part_c_algebra)'
schema=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
a2=[
 ['A2b-regularity','Analytic family of canonical seams and cap maps, with one-sided metric derivatives','Proved','sections/part_a2b_secondary.tex, A2b-regularity','Mondello grafting theorem;AhlforsBers1960A2b','67/061-070','Beltrami parameter dependence with normalized deck-group conjugacy; C1,1 interface'],
 ['A2b-energy','The logarithmic cap radius Jacobian in squared boundary lengths is symmetric positive definite; cap-radius map is injective','Proved','sections/part_a2b_secondary.tex, A2b-energy','A2b-regularity','67/068-069','Exact Green identity including fixed cusp ends; no assumed Liouville convexity'],
 ['A2b-recession','Uniform cap collapse bound and Strebel support recession of the cap potential','Proved','sections/part_a2b_secondary.tex, A2b-recession','A2-strebel-deficit;collar lemma;Solynin1999A2b','67/068-070','Zero-weight recession directions handled by coordinate upper bounds'],
 ['A2b-image','Exact radius image is exp of the strict nonnegative-weight Strebel half-space intersection','Proved','sections/part_a2b_secondary.tex, A2b-image','A2b-energy;A2b-recession','67/068-069','Complete coercivity and boundary-minimum exclusion proof; unique canonical representative of each feasible analytic-disc radius vector'],
]
a1=[
 ['A1-graph-range','Unbordered surgery on each stable graph is a real-analytic diffeomorphism onto its exact proper open log-convex tensor range; tangent and fundamental-group isomorphisms','Proved under stated hypotheses','sections/part_a1_range.tex, A1-graph-range','A2b-energy;A2b-image;A2b-recession;A1-tensor;A1-retained-discs','67/074-082','Actual toric S1 phases; self-loops included; fixed full external cap domains excluded'],
 ['A1-small-ranges','Exact one-node tensor ranges are 0<|q|<16 for separating(0,4) and 0<|q|<1 for irreducible(1,1)','Proved','sections/part_a1_range.tex, A1-small-ranges','A1-graph-range;A2-explicit-limits;A2-nonbox','67/074-082','Specified projective tangent frames; every phase; unique length'],
]
events=[
 ['A2b-regularity',now,who,'primary-source check and derivation','Ahlfors–Bers1960 section5.7 Theorems10–11 pp402–403 opened; normalized conjugacy and elliptic bootstrap detailed'],
 ['A2b-energy',now,who,'independent re-proof','Moving seam sign and two Green identities checked independently by root; cusp estimates and strict zero-energy implication supplied'],
 ['A2b-image',now,who,'targeted proof check','Strict support inequalities, nonnegative recession directions, bounded sublevels and exclusion of every finite boundary minimum checked'],
 ['Solynin1999A2b',now,who,'primary-source check and derivation','Original Russian eq1.2 p9, eq2.2 p23, Theorem2.1 eq2.27 p32 read; square-root weight specialization and zero-weight approximation verified'],
 ['A2b-energy',now,who,'computation or formal certificate','Numerical diagnostic only:1209 positive normalized pants Hessians;600 positive monotonicity pairings; analytic proof does not rely on sampling'],
 ['A2-strebel-deficit',now,who,'independent re-proof','Reviewed root area comparison: peripheral loop lower bound, annular Cauchy–Schwarz, reduced-area signs and fixed cusp contribution'],
 ['A2-cap-limit',now,who,'independent re-proof','Reviewed root zero-weight limit argument and positive-weight compactness; no gap found'],
 ['A2-explicit-limits',now,who,'independent re-proof','Koebe pullback exactly−du²/u²; orange uniformization has derivative modulus3sqrt3/4; third graph arc clarified to root'],
]
a1events=[
 ['A1-graph-range',now,who,'targeted proof check','Incidence pullback Hessian positive definite; loop branches counted twice; recession proof and equivariant common radial retract supplied'],
 ['A1-small-ranges',now,who,'independent re-proof','Supports compute log16 for two one-active pants and0 for the self-node two-active pant'],
 ['A1-graph-range',now,who,'scope check','S1 seam phases distinguished from real fully marked twists; no inference for fixed external disc domains'],
]
for prefix,rows,ev in [('part_a2b',a2,events),('part_a1_range',a1,a1events)]:
 with (ROOT/'checks'/f'{prefix}_results.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(schema);w.writerows(rows)
 with (ROOT/'checks'/f'{prefix}_events.tsv').open('w',newline='') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(ev)
 print(prefix,len(rows),'statement rows',len(ev),'events',now)
rec={'date':now,'a2b_rows':len(a2),'a1_range_rows':len(a1),'a2b_events':len(events),'a1_range_events':len(a1events)}
(ROOT/'code'/'part_a2b_make_metadata_output.json').write_text(json.dumps(rec,indent=2)+'\n')
