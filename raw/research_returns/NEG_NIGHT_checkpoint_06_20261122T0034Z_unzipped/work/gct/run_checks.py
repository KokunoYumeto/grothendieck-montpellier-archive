"""Run actual computational checks and append their provenance events."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import csv,os,subprocess,json,hashlib,sys,time
R=Path('work/gct'); fpath=R/'CHECK_EVENTS.tsv'
fields=['statement_id','date_utc','who_model','effort','run','type','outcome','evidence']
rows=[]
if len(sys.argv)!=2:raise SystemExit('Supply clock__curr_time UTC timestamp as sole argument; host clock has a different offset.')
clock_start=datetime.strptime(sys.argv[1],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
elapsed_start=time.monotonic()
jobs=[('NN-G011','verify_dimension_7276.py','computation or formal certificate','Independent integer-Laurent table; all 1000 associativity triples and 132 positions.'),('NN-G012','verify_signpoint_matrix_block.py','computation or formal certificate','Independent corrected-basis products and rescaled M2 images; 16 products.'),('NN-G012;E4-section6b','check_signpoint_Hecke_trace.py','used and rechecked in this run','Reuses supplied exact tensor-Hecke arithmetic; checks 5 trace values.'),('NN-G001;NN-G003','check_elementary_claims.py','computation or formal certificate','D5 prime-field point counts for 14 primes through43; strict-index formula for 99 values L=2..100. Finite supplements only.')]
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
for ids,script,kind,scope in jobs:
    start=(clock_start+timedelta(seconds=time.monotonic()-elapsed_start)).isoformat(timespec='seconds')
    out=subprocess.run(['python','-B',str(R/script)],capture_output=True,text=True,env=env)
    log=R/(script.removesuffix('.py')+'.check.log');log.write_text(out.stdout+out.stderr)
    rows.append([ids,start,'GPT-6 Astra Pro (inherited)','not exposed by runtime','/root/gct',kind,('PASS: ' if out.returncode==0 else 'FAIL: ')+scope,str(log)])
    print(script,'PASS' if out.returncode==0 else 'FAIL')
with fpath.open('a') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    if fpath.stat().st_size==0:w.writerow(fields)
    w.writerows(rows)
assert all('PASS:' in r[6] for r in rows)
