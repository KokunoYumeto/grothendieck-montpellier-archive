from pathlib import Path
import subprocess
import hashlib
root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
source = root / 'sources/mast_nachbin_inventory1997.pdf'
for page in [26, 27, 28, 30, 31, 32, 33, 34, 44]:
    prefix = root / f'notes/category_nachbin_inventory_{page:03d}'
    command = ['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','1800','-png',str(source),str(prefix)]
    result = subprocess.run(command, capture_output=True, text=True, timeout=60)
    print('COMMAND',repr(command),'STATUS',result.returncode,'STDOUT',repr(result.stdout),'STDERR',repr(result.stderr),flush=True)
    if result.returncode == 0:
        path = prefix.with_suffix('.png')
        print('IMAGE',str(path),'BYTES',path.stat().st_size,'SHA256',hashlib.sha256(path.read_bytes()).hexdigest(),flush=True)
