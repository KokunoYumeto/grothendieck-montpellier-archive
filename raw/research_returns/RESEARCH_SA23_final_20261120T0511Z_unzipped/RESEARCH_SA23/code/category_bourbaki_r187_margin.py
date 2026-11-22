from pathlib import Path
import subprocess,json,time
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
commands=[['pdftoppm','-f','2','-l','2','-singlefile','-r','250','-x','0','-y','0','-W','1400','-H','800','-png',str(r/'sources/category_bourbaki_r187_1.pdf'),str(r/'sources/category_bourbaki_r187_pages/page_02_margin')],['pdftoppm','-f','12','-l','12','-singlefile','-scale-to','2400','-png',str(r/'notes/category_bourbaki_delsarte_list.pdf'),str(r/'sources/category_bourbaki_delsarte_page012')]]
for cmd in commands:
    p=subprocess.run(cmd,capture_output=True,timeout=40)
    print(json.dumps({'command':cmd,'status':p.returncode,'stdout':p.stdout.decode(errors='replace'),'stderr':p.stderr.decode(errors='replace')}),flush=True)
