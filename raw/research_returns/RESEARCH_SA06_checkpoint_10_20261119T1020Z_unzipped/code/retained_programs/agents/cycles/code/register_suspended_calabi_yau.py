"""Record the audited low-dimensional suspended Calabi–Yau theorem."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

started=time.perf_counter()
base=Path(__file__).resolve().parents[1]
row=['C.3ai',
 'For every r>=1 and r+2<=N<=2r+1, a specified regular ambient strict local source has zero CH^r while its regular principal puncture has a non-torsion ordinary algebraically trivial class',
 'Refuted, with an explicit counterexample',
 'suspended_calabi_yau.tex, paragraph C.3ai',
 'C.3e strict-local cone injection; C.3s finite-data descent; C.3r transverse join construction; C.2b affine vanishing and Poincare duality; Skalit2017 Corollary6.4(i)',
 '14:107-112',
 'Fermat degree d+2 with d=2r-N+2 and k=N-r-2 paired suspensions. Integral transverse correspondence identity gives a cohomological left inverse. The specified generic-point class cannot lie in H CH^(r-1), by its exact Hodge shift below the middle. Actual fixed-product curve families are retained.']
with (base/'suspended_calabi_yau_results.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']);w.writerow(row)
who='GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root/cycles'
root='GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root'
frob='GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root/frobenius'
events=[
 (root,'targeted proof check','Proposed suspension by paired Fermat variables to fill the interval between the Calabi-Yau top-cycle construction and the odd cubic boundary.'),
 (who,'targeted proof check','Reproved the integral identity transposeGamma1 composedGamma0=DeltaT: pair equations force the common smooth base, both vertices are avoided, and tangent subspaces are complementary with multiplicity one.'),
 (who,'targeted proof check','Finite-data descent, finite-extension norm and closure give bGamma0=H B+b(T timesGamma0[o])+vertical. Explicitly retained the constant correspondence term; it and the vertical term kill H^(d,0).'),
 (who,'targeted proof check','Checked B has codimension r-1 and shifts H^(d,0) to type(d+k-1,k-1), total degree n-2. For k0 the second index is negative; otherwise affine-complement vanishing and Poincare duality give weak Lefschetz below the middle, where only diagonal types occur.'),
 (who,'used and rechecked in this run','Reused freshly opened exact Skalit Corollary6.4(i), p27, with baseC; checked positive integral source Chow vanishing, local quotient compatibility, normal Fermat cone and actual ordinary curve-family pullback.'),
 (root,'independent targeted proof check','Root read the complete typed C3ai and passed all codimensions, transverse composition, finite-data and constant-term spread, Hodge shift and Skalit/cone scope; integration approved subject to clean finite certificate and wrapper.'),
 (frob,'independent targeted proof check','Full typed C3ai independently passed: triple-product diagonal composition with multiplicity1, k0 convention, constant-term norm/closure, exact type(d+k-1,k-1) in degree n-2, and strict-local target/source scope. Freshly reopened Skalit Corollary6.4(i), authorp27, and checked the geometrically regular C to R and henselian hypotheses.'),
 (who,'computation or formal certificate','Exact certificate checks210 pairs(r,N) with r<=20,20 Fermat degrees, both pair substitutions, tangent determinant eta(1-zeta), incidence/composite codimensions and Hodge shifts. Runtime0.10279798600095091 seconds; code/JSON/fullstdout retained. The proof, not this grid, covers every dimension.'),
 (who,'typesetting verification','Repaired prose and filename overflows exposed by the wrapper; the final four-pass LuaLaTeX/BibTeX build has no diagnostics at09:22:51UTC, runtime2.953216986999905 seconds. All initial and final logs retained.')]
with (base/'suspended_calabi_yau_CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who_model_effort_run','type','outcome'])
 for actor,kind,outcome in events:w.writerow(['C.3ai','2026-11-19',actor,kind,outcome])
record={'utc':datetime.now(timezone.utc).isoformat(),'rows':1,'events':len(events),'runtime_seconds':time.perf_counter()-started}
(base/'output/register_suspended_calabi_yau.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
