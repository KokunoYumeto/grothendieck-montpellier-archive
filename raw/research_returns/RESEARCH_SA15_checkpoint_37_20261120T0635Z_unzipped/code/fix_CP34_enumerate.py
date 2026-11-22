"""Repair the actual CP34 first-build list terminator; mathematical text unchanged."""
from pathlib import Path
import csv,datetime,difflib,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
p=w/'agents/obstructions_crystals/A4_general_odd_source_Cartier.tex'
before=p.read_text();assert hashlib.sha256(p.read_bytes()).hexdigest()=='bebb8eeda592394683fad55ce97b4c21c4d9045a196498a96a52a88cc35bf29d'
needle='\\tag{DE-GOS2}\n\\]\nBoth are square matrices'
assert before.count(needle)==1
after=before.replace(needle,'\\tag{DE-GOS2}\n\\]\n\\end{enumerate}\nBoth are square matrices')
folder=w/'notes/CP34_enumerate_repair';assert not folder.exists();folder.mkdir()
shutil.copy2(p,folder/p.name)
p.write_text(after)
(folder/'repair.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='after')))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
r={'status':'LATEX-ENVIRONMENT-REPAIR','actual_utc':now,'file':str(p.relative_to(w)),
 'before_sha256':'bebb8eeda592394683fad55ce97b4c21c4d9045a196498a96a52a88cc35bf29d',
 'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'actual_failure':'CP34 attempt01 stopped because the two-item enumerate in the source lemma was not closed before end lemma.',
 'change':'Inserted exactly one end-enumerate after the second displayed item. No mathematical statement, map, hypothesis or proof text changed.',
 'retained_failed_build':'outputs/checkpoint34_build_attempt01',
 'retained_candidate':'agents/obstructions_crystals/post_CP33_general_odd_source_Cartier_candidate.tex',
 'rerun':'Will execute prepare_checkpoint34.py as attempt02; no future success claimed.'}
(folder/'record.json').write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t').writerow(['CP34-LATEX-LIST-REPAIR',now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root','artifact verification','Actual first compilation failed on an unclosed enumerate. One closing command inserted; all mathematical text unchanged, candidate and failed actual inputs/logs preserved.'])
with (w/'notes/checkpoint34_changes.md').open('a') as f:
 f.write('\n## Actual compilation failure and repair\n\nCheckpoint34 attempt01 failed after12.2 seconds because the two-item list in the arbitrary-source lemma lacked its closing enumerate command. The full failed input snapshot and actual log are retained. Exactly one closing command was inserted after the second displayed item; no mathematical content changed. The original audited candidate and the pre-repair canonical file are preserved, together with the one-line diff. The next compilation is a separate recorded attempt.\n')
print(json.dumps(r,indent=2))
