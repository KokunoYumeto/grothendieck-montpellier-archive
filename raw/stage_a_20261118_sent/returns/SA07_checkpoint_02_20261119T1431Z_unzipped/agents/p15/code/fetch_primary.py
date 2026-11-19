from pathlib import Path
import urllib.request
ROOT=Path('/workspace/scratch/9c0c54a66f6c/agents/p15/evidence')
sources={
 'Grothendieck1969Hodge.pdf':'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/HodgeConj.pdf',
 'BorelHarishChandra1962.pdf':'https://www.mathi.uni-heidelberg.de/~wienhard/retreat10/references/borel_harishchandra_2.pdf',
}
for name,url in sources.items():
 try:
  data=urllib.request.urlopen(url,timeout=25).read()
  (ROOT/name).write_bytes(data)
  print(name,len(data),data[:5])
 except Exception as e: print(name,type(e).__name__,str(e))
