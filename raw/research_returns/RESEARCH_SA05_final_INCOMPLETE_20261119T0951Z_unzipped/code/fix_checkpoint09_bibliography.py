"""Repair literal file paths in two new bibliography annotations."""
from pathlib import Path
from datetime import datetime, timezone
import json
import subprocess
import time

root=Path(__file__).resolve().parents[1]
start=time.perf_counter()
failed=root/'build/build_step_03.txt'
capture=root/'code/checkpoint09_initial_build_failure.txt'
if failed.exists() and not capture.exists():capture.write_bytes(failed.read_bytes())
p=root/'part_c/references.bib';s=p.read_text();repairs=[]
for name in ['fetch_taylor_yoshida_source_output.json','fetch_vial_base_extension_source_output.json']:
    old='in code/part_c/'+name+'.'
    new='in \\path{code/part_c/'+name+'}.'
    if old in s:s=s.replace(old,new);repairs.append(name)
p.write_text(s)
# The status macro supplies terminal punctuation itself.
cosmetic=[]
for rel in ['sections/part_c.tex','part_c/c4_simple_spectrum_positivity.tex',
            'sections/b1_milnor_divisibility.tex']:
    p=root/rel;s=p.read_text();old=s
    for value in [
      'Proved sufficient condition; the universal threefold gate remains open.',
      'Proved scope clarification; no unconditional reduction of the universal gate.',
      'Proved intermediate statement; the universal B.1 gate is unchanged.',
      'Proved intermediate structural consequence; no new universal gate.']:
        s=s.replace('\\status{'+value+'}','\\status{'+value[:-1]+'}')
    if s!=old:p.write_text(s);cosmetic.append(rel)
subprocess.run(['python','code/consolidate_records.py'],cwd=root,check=True,capture_output=True,text=True)
p=subprocess.run(['bibtex','build/RESEARCH_SA05_paper'],cwd=root,capture_output=True,text=True)
(root/'code/checkpoint09_bibtex_repair_output.txt').write_text(p.stdout+'\n'+p.stderr)
out=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),
    initial_failure='Unescaped underscores in literal code paths in two new bibliography notes; first fatal error was Taylor–Yoshida path.',
    repaired_paths=repairs,cosmetic_status_punctuation=cosmetic,
    bibtex_exit=p.returncode,seconds=round(time.perf_counter()-start,6),
    mathematical_changes=False)
(root/'code/fix_checkpoint09_bibliography_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
if p.returncode:raise SystemExit(p.returncode)
