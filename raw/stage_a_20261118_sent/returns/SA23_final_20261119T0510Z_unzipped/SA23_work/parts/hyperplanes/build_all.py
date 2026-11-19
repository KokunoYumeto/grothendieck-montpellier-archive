#!/usr/bin/env python3
"""Rebuild the authored cote25 registers in their dependency order, saving output."""
import json, subprocess, sys
from pathlib import Path

P=Path(__file__).resolve().parent
W=P.parents[1]
ROOT=W.parent
steps=[
 ('build_registers.py','registers_output.json'),
 ('build_references.py','references_output.json'),
 ('build_problems.py','problems_output.json'),
 ('build_readings.py','readings_output.json'),
 ('build_links_directions.py','links_directions_output.json'),
 ('build_search_log.py','search_log_output.json'),
 ('validate.py','validation_run_output.json'),
]
results=[]
for program,output in steps:
 r=subprocess.run([sys.executable,str(P/program)],cwd=ROOT,text=True,capture_output=True)
 (P/output).write_text(r.stdout)
 if r.stderr:(P/(output+'.stderr')).write_text(r.stderr)
 results.append(dict(program=program,output=output,returncode=r.returncode))
 if r.returncode:
  print(r.stderr)
  raise SystemExit(r.returncode)
(P/'build_all_output.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results))
