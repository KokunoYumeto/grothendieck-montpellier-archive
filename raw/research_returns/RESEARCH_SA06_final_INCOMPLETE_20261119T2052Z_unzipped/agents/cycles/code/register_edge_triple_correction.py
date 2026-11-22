"""Register the fully audited restricted C.3bq theorem without changing master files."""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import csv
import json

tic = perf_counter()
base = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
build = json.loads((base/'output/compile_edge_triple_correction.json').read_text())
cert = json.loads((base/'output/edge_triple_correction_certificate.json').read_text())
assert not build['diagnostics']
assert len(build['runs']) == 4 and all(x['returncode'] == 0 for x in build['runs'])
assert cert['checks_failed'] == 0

columns = ['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
row = ['C.3bq',
       'For exceptional SNC surfaces with a negative ample combination, the kernel of component CH0 restriction lies in the actual proper perfect-family relation subgroup if H2 of the rational dual complex vanishes, or if all signed triple-point Pic0 periods vanish rationally',
       'Proved in the stated scope',
       'SNC_edge_triple_correction.tex, ET.1-ET.12',
       'C.3bm/EP; C.3bo; GH2011 A/C; TT8.1; actual proper-symbol EL lemma; Quillen Gersten/localization; Levine1994 p258 Adams operations; Weibel II/III',
       '14:106-109 (restricted rational top-quotient criterion)',
       'Algebraically closed characteristic p>0 and actual proper-curve fixed-product relations. With zero component rational Albanese kernels, ordinary top B2_Q vanishes. No universal Picard-period vanishing or unrestricted component-kernel result; no automatic main-gate movement.']
with (base/'SNC_edge_triple_results.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(columns);w.writerow(row)

event_file=base/'SNC_edge_triple_CHECK_EVENTS.tsv'
event_columns=['statement_id','date','who_model_effort_run','type','outcome']
who='GPT-6 Astra Pro (OpenAI); /root/cycles; RESEARCH_SA06; effort inherited and not separately exposed'
events=[
 ['C.3bq',stamp,who,'targeted proof check',
  'Author full final re-proof: coherent two-stage totalization; every vertex K2 ambiguity represented by a proper symbol family; actual component degree-unit subtraction retaining Pic0; explicit (psi2-2)/2 intermediate lift; period-annihilator cochain correction; conditional component-Albanese-kernel corollary. Root and both independent peer full receipts read.'],
 ['C.3bq',stamp,who,'primary source check',
  'Fresh GH2011 nonconnective convention/A/C pp29-30 and full displayed TheoremC proof pp47-48; Quillen Section7 Prop3.2 eq3.3 and Th5.11 reopening; complete Levine1994 arbitrary-scheme/iterated-fibre/delooping paragraph p258; WeibelIII6.1 p48 theorem statement only. Full original Matsumoto proof not claimed. Earlier TT/WeibelII/EL dependencies reused with precise separate peer/root source receipts.'],
 ['C.3bq',cert['completed_at_utc'],who,'code/experiment',
  f"Retained check_edge_triple_correction.py: {cert['checks_passed']} bounded exact checks, runtime {cert['runtime_seconds']:.12f}s; four complexes including repeated triple points, exact annihilator/correction, Adams polynomial and one-triple weighted energy identity. Full JSON/stdout retained; does not certify geometry or universal period vanishing."],
 ['C.3bq',build['utc'],who,'typesetting verification',
  f"Final four-stage standalone LuaLaTeX/BibTeX build passed all commands with no overfull/undefined/error diagnostics, runtime {build['runtime_seconds']:.12f}s. Five-page final PDF rendered and all pages visually inspected after build; display closures, source links, labels and margins correct. Earlier overfull drafts retained in prior stdout."],
]
old=[]
if event_file.exists():
    with event_file.open(newline='') as f: old=list(csv.reader(f,delimiter='\t'))[1:]
with event_file.open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(event_columns);w.writerows(old)
    w.writerows([e for e in events if e not in old])
report={'completed_at_utc':stamp,'runtime_seconds':perf_counter()-tic,
        'row':'C.3bq','event_rows_added':len([e for e in events if e not in old]),
        'final_proof':str(base/'SNC_edge_triple_correction.tex')}
(base/'output/register_edge_triple_correction.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
