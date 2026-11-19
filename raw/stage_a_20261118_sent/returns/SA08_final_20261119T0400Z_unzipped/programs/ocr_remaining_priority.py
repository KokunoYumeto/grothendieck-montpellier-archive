"""OCR remaining original SGA7-I pages requested for donor-page collation."""
from pathlib import Path
import subprocess,json
r=Path(__file__).resolve().parents[1]
jobs=[(453,453),(458,463),(472,479),(489,503)]
for a,b in jobs:
 p=subprocess.run(['python',str(r/'programs/ocr_reference.py'),str(r/'work/reference_pdfs/sga7-1.pdf'),str(a),str(b),'--workers','4'],capture_output=True,text=True)
 print(json.dumps({'first':a,'last':b,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}),flush=True)
