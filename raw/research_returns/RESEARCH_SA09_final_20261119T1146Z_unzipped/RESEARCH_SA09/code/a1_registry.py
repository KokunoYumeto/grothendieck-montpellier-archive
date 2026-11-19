"""Write the A.1 statement registry, proof events, and correction record."""
from pathlib import Path
import csv, json, datetime
ROOT=Path(__file__).resolve().parents[1]
date='2026-11-19'
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); effort not exposed; run /root SA09-20261119'
rows=[
 ('A1.1','Roby homogeneous-law representability, base change and exponential decomposition over arbitrary rings','Known','Roby III.3-4 and IV.1','137:78-85','Universal divided powers, not invariant tensors on nonflat modules'),
 ('A1.2','Full strict polynomial category of globally bounded polynomial laws with explicit mixed substitution','Proved','A1.1','137:75-86','All commutative rings and arbitrary modules; degrees zero and one included'),
 ('A1.3','L1 identification with Gamma^d P is false; correct relation is polynomial enrichment of Hom followed by linear representation','Refuted','A1.1;A1.2;Krause Section 2;Friedlander-Suslin Definition 2.1','137:83,86','Finite F2 counterexample has morphism cardinalities 4 versus 8'),
 ('A1.4','f maps to Gamma^p(f) is a canonical natural degree-p polynomial law for arbitrary modules','Proved','A1.1','137:86','No unjustified Hom base-change assumption'),
 ('A1.5','The isomorphism unit to Gamma^q(unit) is independent of the other bare axioms','Proved','Exterior partition construction in characteristic 2','137:82-83','Finite witness Lambda^2(F2)=0; all homogeneous associativity identities proved'),
 ('A1.6','Bare tensor/divided-power axioms do not imply the printed structured equivalence','Refuted','A1.2;scalar cocycle identity','137:82-84','F3 scalar twist; requires preserving specified exponential and unit comparisons'),
 ('A1.7','Exact all-degree repair by finite substitution comonad, multigrading and mixed representability coherences','Proved','A1.2;explicit finite diagrams','137:79-84','Necessary and sufficient; no minimality or redundancy claim for coherence list'),
 ('A1.8','Bare abstract tensor/divided-power data need not admit natural strict polynomial enrichment','Refuted','Split exponential retract construction;finite F4 calculation','137:85-86','Does not deny separate basis-dependent laws on individual Hom spaces'),
 ('A1.9','Scalar-weight eigenspaces, exact gcd ambiguity and integral all-base-change separation','Proved','Integer valuation and coefficient calculations','137:76-77','Prime inversion sufficient but not necessary; degree zero separately distinguished'),
]
with (ROOT/'notes'/'A1_results.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages','notes'])
 for ident,statement,status,deps,pages,notes in rows:
  w.writerow([ident,statement,status,'sections/A1.tex, '+ident,deps,pages,notes])
events=[]
for ident,statement,status,deps,pages,notes in rows:
 events.append([ident,date,who,'used and rechecked in this run' if status=='Known' else 'targeted proof check',statement+'; '+notes])
for ident in ['A1.3','A1.5','A1.6','A1.8','A1.9']:
 events.append([ident,date,who,'computation or formal certificate','code/a1_checks.py; exact bounded scope and output in logs/a1_checks.json'])
events += [
 ['SA09-6 (137:75)',date,who,'used and rechecked in this run','Target-side addition and source id_X typing verified; transcribed id_Y does not type-check'],
 ['SA09-6 (137:76-77)',date,who,'refuted, with the refined statement\'s id','Necessity of prime inversion is false for torsion-free groups; exact corrected statement A1.9'],
 ['SA09-6 (137:83)',date,who,'independent re-proof','Unit-axiom independence given a complete exterior-power model in A1.5'],
 ['SA09-6 (137:84)',date,who,'refuted, with the refined statement\'s id','Printed full equivalence refuted by A1.6; exact corrected coherent-data equivalence A1.7'],
 ['L1',date,who,'refuted, with the refined statement\'s id','Typed identification false by A1.3; positive module Hom-law is A1.4, abstract nonautomaticity A1.8'],
]
with (ROOT/'notes'/'A1_CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)
corrections=[
 {'file':'RESEARCH_SA09_study/study/readings/SA09_137-138.md','lines':'229-233','correction':'Prime inversion is sufficient, not necessary: all torsion-free coefficient groups already separate weights; exact annihilator and degree-zero clauses are A1.9.'},
 {'file':'RESEARCH_SA09_study/study/readings/SA09_137-138.md','lines':'241-246','correction':'Unit independence now has an explicit full model A1.5; homogeneous-only verification does not establish full equivalence, which A1.6 refutes for the listed data.'},
 {'file':'RESEARCH_SA09_study/study/readings/SA09_137-138.md','lines':'753-759','correction':'L1 confuses Hom(Gamma^d V,W) with Gamma^d Hom(V,W); A1.3 supplies exact relation and finite counterexample.'},
 {'file':'RESEARCH_SA09_transcriptions/transcriptions/MPL_137_045-086_transcription.tex','lines':'1038','correction':'For f:X→Y the precomposition is f∘(n id_X), not id_Y. No ink reading is asserted.'},
 {'file':'RESEARCH_SA09_transcriptions/transcriptions/MPL_137_045-086_transcription.tex','lines':'1221-1223','correction':'Typed associativity is G^p(alpha_qr) alpha_p,qr = alpha_p,q^{G^r} alpha_pq,r; resolve any differing superscript by sources and targets.'},
 {'file':'RESEARCH_SA09_transcriptions/transcriptions/MPL_137_045-086_transcription.tex','lines':'1278-1281','correction':'The full equivalence needs the explicit mixed coherence and representability requirements in A1.7; A1.6 refutes the printed bare assertion.'},
 {'file':'RESEARCH_SA09_transcriptions/transcriptions/MPL_137_045-086_transcription.tex','lines':'1308-1310','correction':'The degree-p target must be Hom(Gamma^pX,Gamma^pY), not the doubtful r alternative. Standard module answer A1.4; abstract natural enrichment counterexample A1.8.'},
]
(ROOT/'notes'/'A1_corrections.json').write_text(json.dumps(corrections,indent=2,ensure_ascii=False))
print(json.dumps({'statements':len(rows),'check_events':len(events),'corrections':len(corrections)}))
