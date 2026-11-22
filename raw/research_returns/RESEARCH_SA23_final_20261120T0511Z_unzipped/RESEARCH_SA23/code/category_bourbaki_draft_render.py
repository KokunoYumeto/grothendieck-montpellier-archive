from pathlib import Path
import subprocess, concurrent.futures, hashlib, json, os
root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
source=root/'notes/category_bourbaki_nbr082.pdf'
out=root/'notes/category_bourbaki_nbr082_pages';out.mkdir(exist_ok=True)
def process(page):
 prefix=out/f'page_{page:02d}'
 command=['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','2200','-png',str(source),str(prefix)]
 result=subprocess.run(command,capture_output=True,timeout=40)
 image=prefix.with_suffix('.png')
 env=os.environ.copy();env['OMP_THREAD_LIMIT']='1'
 ocr_command=['tesseract',str(image),'stdout','-l','eng','--psm','3']
 ocr=subprocess.run(ocr_command,capture_output=True,timeout=40,env=env)
 prefix.with_suffix('.txt').write_bytes(ocr.stdout)
 record={'page':page,'render_command':command,'render_status':result.returncode,'render_stderr':result.stderr.decode(errors='replace'),'image_sha256':hashlib.sha256(image.read_bytes()).hexdigest(),'ocr_command':ocr_command,'ocr_status':ocr.returncode,'ocr_stderr':ocr.stderr.decode(errors='replace'),'text_bytes':len(ocr.stdout),'text_sha256':hashlib.sha256(ocr.stdout).hexdigest()}
 prefix.with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
 return record
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for record in pool.map(process,range(1,10)): print(json.dumps(record),flush=True)
full=''.join(f'\n===== PHYSICAL PDF PAGE {page} =====\n'+(out/f'page_{page:02d}.txt').read_text() for page in range(1,10))
(root/'notes/category_bourbaki_nbr082_full.txt').write_text(full)
print(json.dumps({'complete':True,'characters':len(full),'ocr_is_finding_aid':True}),flush=True)
