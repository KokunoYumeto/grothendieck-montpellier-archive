#!/usr/bin/env python3
"""Rebuild authored root records and execute the saved exact calculations."""
import json,subprocess,sys,datetime
from pathlib import Path
P=Path(__file__).resolve().parent;root=P.parents[2]
programs=[P/'author_items.py',P/'author_middle.py',(P/'repair_codex_locators.py','items'),P/'author_entries.py',P/'author_literature.py',P/'author_claims.py',P/'author_problems.py',P/'author_tables.py',(P/'repair_codex_locators.py','tables'),root/'SA05/programs/root_certificates.py',P/'author_evidence.py']
out=P/'outputs';out.mkdir(exist_ok=True)
records=[]
for entry in programs:
 pr,args=(entry[0],list(entry[1:])) if isinstance(entry,tuple) else (entry,[])
 proc=subprocess.run([sys.executable,str(pr),*args],cwd=root,text=True,capture_output=True)
 output=out/(pr.stem+('_'+'_'.join(args) if args else '')+'_run.txt')
 output.write_text(proc.stdout+proc.stderr)
 records.append({'program':str(pr.relative_to(root)),'arguments':args,'exit_code':proc.returncode,'output':str(output.relative_to(root))})
 if proc.returncode:raise RuntimeError(pr.name+' failed: '+proc.stderr)
summary={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'programs':records,'all_passed':True}
(out/'build_log.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
