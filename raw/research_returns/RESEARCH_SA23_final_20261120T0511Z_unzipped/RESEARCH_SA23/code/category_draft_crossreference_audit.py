from pathlib import Path
import subprocess
import hashlib

root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
pdf = root / 'notes/geometry_Fredholm1956.pdf'
prefix = root / 'notes/category_draft_Fredholm1956_p319'
cmd = ['pdftoppm', '-f', '2', '-l', '2', '-singlefile', '-scale-to', '1800', '-png', str(pdf), str(prefix)]
print('COMMAND', repr(cmd))
r = subprocess.run(cmd, text=True, capture_output=True)
print('RETURN', r.returncode)
print('STDOUT', r.stdout)
print('STDERR', r.stderr)
if r.returncode:
    raise SystemExit(r.returncode)
for relative in [
    'notes/geometry_Fredholm1956.pdf',
    'notes/category_draft_Fredholm1956_p319.png',
    'notes/geometry_cote1_full/page_044.jpg',
    'notes/geometry_cote1_full/page_064.jpg',
    'notes/category_compare_Fredholm1956_p348.png',
    'notes/category_memoir_followup_199.png',
    'notes/category_memoir_followup_200.png',
]:
    p = root / relative
    print('SOURCE', relative, 'BYTES', p.stat().st_size, 'SHA256', hashlib.sha256(p.read_bytes()).hexdigest())
print('This program renders and fingerprints the sources only; handwriting and publication-note comparison is a human/model visual inspection recorded in category_draft_crossreference_audit.md.')
