from pathlib import Path
import subprocess,json
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
folder=r/'sources/category_bourbaki_r230_pages';folder.mkdir(exist_ok=True)
for page in [1,2,3,156]:
    cmd=['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','2500','-png',str(r/'sources/category_bourbaki_r230_original_1.pdf'),str(folder/f'page_{page:03d}')]
    p=subprocess.run(cmd,capture_output=True,timeout=40)
    print(json.dumps({'command':cmd,'status':p.returncode,'stdout':p.stdout.decode(errors='replace'),'stderr':p.stderr.decode(errors='replace')}),flush=True)
