from pathlib import Path
import subprocess, json, hashlib
root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
source=root/'notes/category_nachbin_1956_bibliography1994.pdf'
for page in [7,8,9]:
    prefix=root/f'notes/category_nachbin_1956_bibliography_page{page:03d}'
    command=['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','2600','-png',str(source),str(prefix)]
    result=subprocess.run(command,capture_output=True,timeout=40)
    image=prefix.with_suffix('.png')
    print(json.dumps({'page':page,'command':command,'status':result.returncode,'stderr':result.stderr.decode(errors='replace'),'sha256':hashlib.sha256(image.read_bytes()).hexdigest() if image.exists() else None}),flush=True)
