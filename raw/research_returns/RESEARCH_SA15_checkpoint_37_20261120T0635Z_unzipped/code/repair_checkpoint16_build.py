"""Retain the failed first build and repair only the two-pencil display alignment."""
from pathlib import Path
import shutil, subprocess, sys, json, datetime
w = Path(__file__).resolve().parents[1]
dest = w/'outputs/failed_checkpoint16_build'
assert not dest.exists()
dest.mkdir()
for rel in ['RESEARCH_SA15_paper.tex','RESEARCH_SA15_paper.log',
            'sections/A_monodromy.tex','outputs/build_console.txt','outputs/build_failure.json',
            'agents/obstructions_crystals/A3_mixed_thin_strip_residues.tex']:
    shutil.copy2(w/rel, dest/Path(rel).name)
p = w/'agents/obstructions_crystals/A3_mixed_thin_strip_residues.tex'
old = p.read_text()
needle = 'H^0(H)\\oplus H^0(HB)&\\longrightarrow H^0(H^2),\n & (x,y)&\\longmapsto a_0x+\\mu b_2y,'
replacement = 'H^0(H)\\oplus H^0(HB)&\\longrightarrow H^0(H^2),\\\\\n (x,y)&\\longmapsto a_0x+\\mu b_2y,'
assert old.count(needle) == 1
p.write_text(old.replace(needle, replacement))
record = {'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'failure':'Extra alignment tab in a split display; no mathematical change.',
          'failed_runtime_seconds':json.loads((dest/'build_failure.json').read_text())['seconds']}
(dest/'repair_record.json').write_text(json.dumps(record, indent=2)+'\n')
subprocess.run([sys.executable,str(w/'code/prepare_checkpoint16.py')],check=True,cwd=w)
print(json.dumps(record, indent=2))
