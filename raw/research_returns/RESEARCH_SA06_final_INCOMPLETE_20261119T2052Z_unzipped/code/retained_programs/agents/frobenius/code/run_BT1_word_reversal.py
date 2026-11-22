"""One instrumented replay of the exact previously untimed word-reversal program."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,subprocess,sys,time
root=Path(__file__).resolve().parents[3]
base=root/'agents/frobenius'
program=base/'code/check_BT1_word_reversal.py'
started=datetime.now(timezone.utc).isoformat()
tick=time.perf_counter()
proc=subprocess.run([sys.executable,str(program)],cwd=root,text=True,capture_output=True)
elapsed=time.perf_counter()-tick
finished=datetime.now(timezone.utc).isoformat()
(base/'output/BT1_word_reversal_instrumented.out').write_text(proc.stdout)
(base/'output/BT1_word_reversal_instrumented.err').write_text(proc.stderr)
original=(base/'output/BT1_word_reversal_original_untimed.out').read_text()
record={'started_utc':started,'finished_utc':finished,'runtime_seconds':elapsed,'exit_code':proc.returncode,'program':'agents/frobenius/code/check_BT1_word_reversal.py','program_sha256':sha256(program.read_bytes()).hexdigest(),'input_manifest':'agents/frobenius/output/BT1_word_reversal_input.json','stdout_file':'agents/frobenius/output/BT1_word_reversal_instrumented.out','stderr_file':'agents/frobenius/output/BT1_word_reversal_instrumented.err','stdout':proc.stdout,'stderr':proc.stderr,'matches_original_stdout':proc.stdout==original,'original_process_timing_recorded':False,'status':'PASS' if proc.returncode==0 and proc.stdout==original else 'FAIL','scope':'Exact finite stdout replay and reversal labels only; no geometry or infinite theorem certified.'}
(base/'output/BT1_word_reversal_instrumented.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
raise SystemExit(proc.returncode or (0 if proc.stdout==original else 1))
