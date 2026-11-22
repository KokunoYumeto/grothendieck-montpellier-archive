from pathlib import Path
import subprocess,json
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
pages=(r/'notes/category_bourbaki_r230_bki_inventory.txt').read_text().split('\f')
page=next(i+1 for i,s in enumerate(pages) if 'COTE IECN : 230' in s)
cmd=['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','2400','-png',str(r/'sources/category_bourbaki_r230_bki_inventory.pdf'),str(r/'sources/category_bourbaki_r230_bki_inventory_p61')]
p=subprocess.run(cmd,capture_output=True,timeout=40)
print(json.dumps({'physical_page':page,'printed_page':61,'command':cmd,'status':p.returncode,'stdout':p.stdout.decode(errors='replace'),'stderr':p.stderr.decode(errors='replace')}),flush=True)
