from pathlib import Path
import hashlib,json,subprocess
root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
destination=root/'sources/category_bourbaki_nbr082_pages';destination.mkdir(exist_ok=True)
files=list((root/'notes/category_bourbaki_nbr082_pages').glob('*.png'))
files.extend(root.glob('notes/category_bourbaki_*.png'))
rows=[]
for source in files:
 target=destination/source.name if source.parent.name=='category_bourbaki_nbr082_pages' else root/'sources'/source.name
 if target.exists(): raise FileExistsError(target)
 data=source.read_bytes();sha=hashlib.sha256(data).hexdigest();source.rename(target)
 assert hashlib.sha256(target.read_bytes()).hexdigest()==sha
 rows.append({'old_path':str(source.relative_to(root)),'new_path':str(target.relative_to(root)),'sha256':sha,'bytes':len(data)})
(root/'notes/category_bourbaki_image_relocations.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps({'relocations':rows,'reason':'Raw reproducible source images moved to retrievable cache; notes retain authored audit and OCR/command/hash records'}),flush=True)
command=['pdftoppm','-f','2','-l','2','-singlefile','-r','300','-x','0','-y','0','-W','900','-H','800','-png',str(root/'sources/category_bourbaki_nbr082.pdf'),str(destination/'page_02_margin')]
result=subprocess.run(command,capture_output=True,timeout=40)
print(json.dumps({'command':command,'status':result.returncode,'stderr':result.stderr.decode(errors='replace')}),flush=True)
