"""Record the due actual review, update the report, then archive CP12 once."""
from pathlib import Path
import json,subprocess,sys
w=Path(__file__).resolve().parents[1]
def run(name,*args):
 subprocess.run([sys.executable,str(w/'code'/name),*args],check=True,cwd=w)
run('record_review.py','7',str(w/'notes/review07_assessment.json'))
review=json.loads((w/'notes/progress_review_07.json').read_text())
note='\n## Actual hourly review07\n\n'
note+=f"The actual review was recorded at {review['actual_utc']}, against immutable review06. It found the structural A.3 extensions, the closed coherent Noetherian E.2 refinement, and the strictly smaller B.4 least-index gate described in notes/review07_assessment.json. The consecutive no-movement count is {review['no_movement_streak']}; disposition: {review['disposition']}. Post-freeze candidates, packaging and repeated calculations were excluded from this progress count. The next review is due12:50:40UTC and the next checkpoint is due12:35:40UTC.\n"
with (w/'notes/checkpoint12_changes.md').open('a') as f:f.write(note)
run('update_current12.py')
with (w/'RESEARCH_SA15_report.md').open('a') as f:
 f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
run('export_agent_programs.py')
run('checkpoint.py','12')
run('verify_checkpoint_archive.py','12')
