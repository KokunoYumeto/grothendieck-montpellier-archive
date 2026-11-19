import urllib.request,tarfile,subprocess,time,hashlib
from pathlib import Path
root=Path('/workspace/scratch/6215ed17d0f0/tool_builds');root.mkdir(exist_ok=True)
u='https://pari.math.u-bordeaux.fr/pub/pari/unix/pari-2.19.1.tar.gz'
t=time.monotonic()
data=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
assert hashlib.sha256(data).hexdigest()=='419553b11ff8c3ecb8e9031b7d91d7cee003a5d721e685fcb499565c96fe2943'
p=root/'pari-2.19.1.tar.gz';p.write_bytes(data)
with tarfile.open(p) as tf:tf.extractall(root,filter='data')
build=root/'pari-2.19.1'
log=Path('/workspace/scratch/6215ed17d0f0/RESEARCH_SA05_work/part_b/pari_build.log')
with log.open('w') as f:
 f.write(f'URL: {u}\nSHA256: {hashlib.sha256(data).hexdigest()}\n')
 for cmd in [['./Configure','--without-readline'],['make','-j4','gp']]:
  f.write('COMMAND: '+repr(cmd)+'\n');f.flush()
  subprocess.run(cmd,cwd=build,stdout=f,stderr=subprocess.STDOUT,check=True)
 f.write(f'Elapsed seconds: {time.monotonic()-t:.3f}\n')
print(build/'gp');print('seconds',time.monotonic()-t)
