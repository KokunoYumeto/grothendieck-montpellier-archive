"""Actual due-time review followed by the immutable CP20 archive."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
assert datetime.datetime.now(datetime.timezone.utc)>=datetime.datetime.fromisoformat('2026-11-19T17:50:40+00:00')
log=w/'outputs/review13_recording_stdout.txt';assert not log.exists()
with log.open('w') as f:
    subprocess.run([sys.executable,str(w/'code/record_review.py'),'13',str(w/'notes/review13_assessment.json')],cwd=w,stdout=f,stderr=subprocess.STDOUT,check=True)
report=w/'RESEARCH_SA15_report.md'
if 'RainsSam2019LateLead' not in report.read_text():
    with report.open('a') as f:f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
review=json.loads((w/'notes/progress_review_13.json').read_text())
print(json.dumps({'actual_review_utc':review['actual_utc'],'movement_count':len(review['movement']),
                  'no_movement_streak':review['no_movement_streak'],'disposition':review['disposition']},indent=2),flush=True)
subprocess.run([sys.executable,str(w/'code/archive_checkpoint20.py')],cwd=w,check=True)
