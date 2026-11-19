"""Reproduce all generated p3 tables from the human-authored records.
Narrative Markdown and manually curated bibliography are source documents and are not overwritten.
"""
from pathlib import Path
import subprocess,sys
S=Path(__file__).resolve().parents[1]
steps=['build_p3.py','polish_records.py','problem_prose_finish.py','search_records.py','event_records.py','supplementary_events.py','link_records.py','validate_p3.py']
for name in steps:
 result=subprocess.run([sys.executable,str(S/'code'/name)],text=True,capture_output=True,check=True)
 (S/'outputs'/(Path(name).stem+'.txt')).write_text(result.stdout+result.stderr)
 print(name+': '+result.stdout.strip())
