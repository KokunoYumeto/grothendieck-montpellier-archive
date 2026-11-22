"""Record the user's scheduled substantive progress review, not packaging progress."""
from pathlib import Path
import csv,json,datetime,re,sys
root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1]);now=datetime.datetime.now(datetime.timezone.utc)
rows=list(csv.DictReader((root/'RESEARCH_SA14_SA19_results.csv').open()))
by={r['id']:r for r in rows}
terms=['undec','unsettled','unresolved','undetermined','pending','delegated','needs exact']
openrows=[r for r in rows if any(s in r['status'].lower() for s in terms)]
if number==1:
 movements=[
  {'id':'A3','from':'Undecided','to':'Proved','evidence':'sections/A.tex, a:very-ample-example; code/certify_A3_output.json; explicit smooth surface and very ample L with h1(L^-1)=1.'},
  {'id':'A4','from':'Undecided','to':'Proved exact obstruction description','evidence':'sections/A.tex, finite multiplicative cohomology sequence and bounded-exponent proof.'},
  {'id':'A1','from':'All dimensions n>=4','to':'Dimension four suffices','evidence':'sections/A.tex, dimension reduction with typed restriction maps; universal fourfold gate remains.'},
  {'id':'B1,B2,C1,C2,C3,C4','from':'Undecided','to':'Scoped proofs/refutations recorded','evidence':'sections/B.tex and C.tex; complete divisorial counterexamples, exact family obstruction, henselian comparison.'},
  {'id':'D1,D2,D3,D4-versal','from':'Undecided','to':'Proved constructions and full modular families','evidence':'sections/D.tex; ordinary and supersingular hulls, all-Artinian Pic-tau flatness, distinct Picvar counterexample.'},
  {'id':'E1,E2,E3 and E4 subrows','from':'Undecided','to':'Many literal claims proved or refuted','evidence':'sections/E.tex; E4.H and E4.Q explicit counterexamples. Parent E4 retains precise remaining gates.'},
  {'id':'G1,G2,G3','from':'Undecided','to':'Proved complete section criterion and signs','evidence':'sections/G.tex; quadratic refinement monodromy and determinant comparison.'},
  {'id':'H-Ga,H-all,SA19-H4','from':'Undecided','to':'Higher Ext proved; overbroad comparisons/refuted local projectivity separated','evidence':'sections/H.tex; exact categories and explicit local Artin-Schreier obstruction.'},
  {'id':'I-2d,I8','from':'Undecided','to':'Surface presentation proved and every-dimensional open-left-ideal presentation proved','evidence':'sections/I.tex; universal Cousin-complex extension proof and three targeted audits. General-topology gate retained.'},
  {'id':'J1-Th4,J1-Th5,J1-Th7,J2-isomorphism,J2-positivity','from':'Undecided','to':'Refuted with specified counterexamples','evidence':'sections/J.tex; raw-sign, quadric-pencil, Ceresa and characteristic-five Jacobian counterexamples.'},
  {'id':'SA14-H1,H2,H5,H6,H7,H8,H9,H10,H11,H12,H13','from':'Undecided','to':'Scoped proofs/refutations in result register','evidence':'Individual typed statements and check events; no promotion of A2 or higher all-regular representability.'}
 ]
 previous_stagnant=0
else:
 prev=json.loads((root/'code'/f'formal_review_{number-1:02d}.json').read_text())
 previous_stagnant=prev['consecutive_reviews_without_movement']
 # Later reviews require a separately written, explicit list of proved changes.
 movements=json.loads((root/'code'/f'formal_review_{number:02d}_movements.json').read_text())
movement=bool(movements);stagnant=0 if movement else previous_stagnant+1
result={'review':number,'time_utc':now.isoformat(),'baseline':'initial dated ledger' if number==1 else f'formal_review_{number-1:02d}.json','movement':movement,'consecutive_reviews_without_movement':stagnant,'stop_rule_triggered':stagnant>=2,'movements':movements,'open_rows':openrows,'next_review_target_utc':(datetime.datetime(2026,11,20,17,2,47,tzinfo=datetime.timezone.utc)+datetime.timedelta(hours=number)).isoformat(),'all_rows_snapshot':rows}
p=root/'code'/f'formal_review_{number:02d}.json'
if p.exists():raise SystemExit('Refusing to overwrite a formal review')
p.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
 f.write(f'\n## Formal progress review {number:02d} — {now.isoformat()}\n\n')
 f.write('Comparison baseline: '+result['baseline']+'. Movement is counted only for a proved status change or a strictly smaller proved main gate. Packaging, source search alone, and restatement are not counted.\n\n')
 f.write(f'**Movement: {"YES" if movement else "NO"}. Consecutive reviews without movement: {stagnant}. Stop rule triggered: {"YES" if stagnant>=2 else "NO"}.**\n\n')
 f.write('| Item | Previous state | Proved change | Evidence |\n|---|---|---|---|\n')
 for x in movements:f.write('| '+' | '.join(str(x[k]).replace('|','\\|') for k in ['id','from','to','evidence'])+' |\n')
 f.write('\n### Every current unresolved row\n\n| Row | Status | Strongest current gate |\n|---|---|---|\n')
 for r in openrows:f.write('| '+' | '.join(r[k].replace('|','\\|') for k in ['id','status','notes'])+' |\n')
 f.write('\nNext formal review target: '+result['next_review_target_utc']+'. Main A1/A2 retain priority; the broad-topology I gate, wild surface group, remaining Picard structure questions, and precise programme-equivalence gates continue in parallel.\n')
print(json.dumps({k:result[k] for k in ['review','time_utc','movement','consecutive_reviews_without_movement','stop_rule_triggered','next_review_target_utc']},indent=2))
