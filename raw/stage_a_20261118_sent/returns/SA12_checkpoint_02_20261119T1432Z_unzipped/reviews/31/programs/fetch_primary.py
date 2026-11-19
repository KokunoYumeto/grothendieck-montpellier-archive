from pathlib import Path
import urllib.request,subprocess,json,concurrent.futures
out=Path('/workspace/scratch/a77a578fa7d4/SA12_work/reviews/31'); dest=out/'external'; dest.mkdir(exist_ok=True)
urls={'sga4iii':'https://www.normalesup.org/~forgogozo/SGA4/tomes/tome3.pdf','sga4v':'https://www.cmls.polytechnique.fr/perso/orgogozo/SGA4/05/05.pdf','sga3ix':'https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp9-8nov09.pdf','sga3x':'https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo10-8nov09.pdf','sga2':'https://www.cmls.polytechnique.fr/perso/laszlo/sga2/sga2-smf.pdf','ega3ii':'https://wstein.org/sga/circle/EGAIII.2.pdf'}
def get(kv):
 k,u=kv
 try:
  r=urllib.request.urlopen(u,timeout=30); data=r.read(); p=dest/(k+'.pdf'); p.write_bytes(data); x=subprocess.run(['pdftotext','-layout',str(p),str(dest/(k+'.txt'))],capture_output=True,text=True)
  return {'key':k,'url':u,'status':r.status,'bytes':len(data),'pdftotext':x.returncode}
 except Exception as e:return {'key':k,'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:r=list(ex.map(get,urls.items()))
s=json.dumps(r,indent=2); (out/'outputs/fetch_primary.json').write_text(s);print(s)
