from pathlib import Path
import subprocess, json, hashlib, time
R=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
pdf=R/'sources/category_bourbaki_r187_1.pdf'
images=R/'sources/category_bourbaki_r187_pages';images.mkdir(exist_ok=True)
notes=R/'notes/category_bourbaki_r187_pages';notes.mkdir(exist_ok=True)
def call(cmd,timeout=45):
    s=time.monotonic();p=subprocess.run(cmd,capture_output=True,timeout=timeout)
    print(json.dumps({'command':cmd,'status':p.returncode,'stdout':p.stdout.decode(errors='replace'),'stderr':p.stderr.decode(errors='replace'),'seconds':time.monotonic()-s}),flush=True)
call(['pdfinfo',str(pdf)])
call(['pdftotext','-layout',str(pdf),str(R/'notes/category_bourbaki_r187_native.txt')])
for page in range(1,8):
    path=images/f'page_{page:02d}'
    call(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','2400','-png',str(pdf),str(path)])
    call(['tesseract',str(path.with_suffix('.png')),str(notes/f'page_{page:02d}'),'-l','fra+eng'])
full='\n'.join(f'\n=== PHYSICAL PAGE {p} ===\n'+(notes/f'page_{p:02d}.txt').read_text() for p in range(1,8))
(R/'notes/category_bourbaki_r187_full.txt').write_text(full)
