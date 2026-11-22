"""Register C.3ah after the root proof pass; retain actual checks."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

started=time.perf_counter()
base=Path(__file__).resolve().parents[1]
columns=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
row=['C.3ah',
     'For every r>=1, a specified regular source of dimension N=r+2 has zero CH^r and a principal regular puncture with non-torsion ordinary J^r; combined ordinary J2 surjectivity is universal exactly when N<=3 over C',
     'Refuted, with an explicit counterexample',
     'regular_ambient_calabi_yau.tex, paragraph C.3ah',
     'C.3e strict-local cone injection; C.3s generic-point non-support; Skalit2017 Corollary6.4(i); C.3r/C.3ae/C.3ag for the full J2 dimension corollary',
     '14:107-112',
     'R is the strict henselization of the regular affine (r+2)-space local ring; f is the Fermat form of degree r+2. The target class is the specified geometric generic point minus a specified algebraic point on the Calabi-Yau base. Actual fixed-product curve families prove ordinary algebraic triviality. No claim that all higher-r dimensions are settled.']
with (base/'regular_ambient_results.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(columns);w.writerow(row)
who='GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root/cycles'
root='GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root'
real='GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root/real_weil'
events=[
 (root,'targeted proof check','Identified the missing N4 case by combining the already proved C3s(m=0) target with the C3r regular-ambient Gersten vanishing; proposed the uniform N=r+2 construction.'),
 (who,'used and rechecked in this run','Read the full C3s proof and exact C3r Gersten paragraph. Verified strict henselization/quotient compatibility, ordinary family pullback and all dimensions for the explicit Fermat cone.'),
 (who,'primary-source verification','Freshly opened Skalit arXiv1710.00303 full29-page primary and exact Corollary6.4(i), authorp27, with its proof from Theorem4.5 and Lemma2.18. Zero-dimensional base C gives integral positive-codimension Chow vanishing.'),
 (who,'targeted proof check','Reproved non-support for the specified geometric generic point: finite-data descent and norm yield a diagonal decomposition; the two support types kill H^(r,0), while adjunction gives K_T trivial. This proves non-torsion modulo H CH^(r-1), not merely existence of an unnamed class.'),
 (real,'independent targeted proof check','Independent preaudit of C3s(m=0) and C3r passed before the typed draft: regular source CH vanishes and the ordinary non-torsion target survives C3e. Final typed audit recorded separately when received.'),
 (real,'independent targeted proof check','Full typed proof and combined J2 iff N<=3 table passed at09:18:25UTC, with fresh opening of Skalit Corollary6.4(i) p27 and proof. Independent review/events are agents/real_weil/C3ah_regular_ambient_independent_REVIEW.md and matching CHECK_EVENTS.tsv; no correction requested.'),
 (root,'independent targeted proof check','Root read the entire typed regular_ambient_calabi_yau.tex and passed the generic-point/norm/support argument, actual ordinary family, exact Skalit scope and complete J2 dimension corollary. Integration authorized at the09:18-stage.'),
 (who,'computation or formal certificate','Twelve exact SymPy cases r=1 through12 verify the Fermat gradients, both specified point equations, fixed hyperplane membership, trivial-canonical adjunction exponent and local dimensions. Runtime0.22352465400035726 seconds; complete code/JSON/stdout retained. No non-torsion statement inferred from the grid.'),
 (who,'typesetting verification','Initial wrapper found an alignment-environment typo, repaired from split to aligned. Full four-pass standalone LuaLaTeX/BibTeX then passed with no diagnostics at09:17:51UTC, runtime2.479470054000558 seconds; failed and successful logs both retained.')]
with (base/'regular_ambient_CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who_model_effort_run','type','outcome'])
    for actor,kind,outcome in events:w.writerow(['C.3ah','2026-11-19',actor,kind,outcome])
record={'utc':datetime.now(timezone.utc).isoformat(),'rows':1,'events':len(events),'runtime_seconds':time.perf_counter()-started}
(base/'output/register_regular_ambient.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
