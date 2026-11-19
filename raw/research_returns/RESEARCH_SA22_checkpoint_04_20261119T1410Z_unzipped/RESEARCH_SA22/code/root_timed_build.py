"""Run the specified retained build driver, recording actual runtime and exit status."""
from pathlib import Path
import subprocess,time,json,sys,datetime
ROOT=Path(__file__).resolve().parents[1]
number=int(sys.argv[1]);driver=sys.argv[2]
started=time.perf_counter();timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
log=ROOT/'logs'/f'build_{number:02d}.out'
if log.exists():raise RuntimeError('Build logs are never overwritten by this wrapper')
with log.open('w') as output:
    process=subprocess.run(['bash',str(ROOT/'code'/driver)],stdout=output,stderr=subprocess.STDOUT)
result=dict(build=number,driver='code/'+driver,started_utc=timestamp,
            elapsed_seconds=time.perf_counter()-started,exit_code=process.returncode,
            log=str(log.relative_to(ROOT)))
(ROOT/'code'/f'root_timed_build_{number:02d}_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
sys.exit(process.returncode)
