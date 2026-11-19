"""Reproduce all worker-authored ledgers and exact mathematical checks.
Original source files and Python/SymPy are required; no network retrieval is needed.
"""
from pathlib import Path
import subprocess,sys,json,datetime
W=Path(__file__).resolve().parents[1]
records=[]
for name in ['build_review','build_claims','build_annotations','finalize_support','clean_typography','computations','check_ledger','build_project_audit']:
    r=subprocess.run([sys.executable,str(W/'programs'/f'{name}.py')],capture_output=True,text=True)
    (W/'outputs'/f'{name}.txt').write_text(r.stdout+r.stderr)
    records.append({'program':name+'.py','exit_code':r.returncode,'output':'outputs/'+name+'.txt'})
    if r.returncode:raise RuntimeError(records[-1])
(W/'outputs/run_all.json').write_text(json.dumps(records,indent=2)+'\n')
import csv
validation=json.loads((W/'outputs/validation.json').read_text())
validation['check_events_after_project_audit']=len(list(csv.DictReader((W/'CHECK_EVENTS.tsv').open(),delimiter='\t')))
validation['verified_project_correspondences']=len(list(csv.DictReader((W/'verified_project_links.tsv').open(),delimiter='\t')))
validation['additional_folder_links']=1
(W/'outputs/validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
with(W/'progress.log').open('a') as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+' All six dossier stages complete; all eight serializer/check programs rerun successfully, including the targeted project endpoint audit; outputs persisted.\n')
print(json.dumps(records,indent=2))
