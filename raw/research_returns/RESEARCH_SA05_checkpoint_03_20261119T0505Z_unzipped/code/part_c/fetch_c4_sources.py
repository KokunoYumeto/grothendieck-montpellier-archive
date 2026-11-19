from pathlib import Path
import urllib.request,concurrent.futures,time,json,subprocess
ROOT=Path('/workspace/scratch/6215ed17d0f0/RESEARCH_SA05_work')
entries={
'dejong1996':'https://www.numdam.org/item/PMIHES_1996__83__51_0.pdf',
'deligne1968':'https://www.numdam.org/item/PMIHES_1968__35__107_0.pdf',
'deligne_weil2':'https://www.numdam.org/item/PMIHES_1980__52__137_0.pdf',
'gabber_ilo':'https://fabrice.orgogozo.perso.math.cnrs.fr/travaux_de_Gabber/GTG/GTG.pdf',
'beauville_chow1986':'https://math.univ-cotedazur.fr/u/beauvill/pubs/Chow.pdf',
'ellenberg_logan_srinivasan2024':'https://padmask.github.io/CertifyingCeresa.pdf'}
def run(item):
 key,url=item;started=time.monotonic();p=ROOT/'part_c/sources'/f'{key}.pdf'
 try:
  data=urllib.request.urlopen(url,timeout=150).read();p.write_bytes(data)
  r=subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True,text=True)
  return {'id':key,'url':url,'bytes':len(data),'seconds':round(time.monotonic()-started,3),'text_exit':r.returncode,'stderr':r.stderr,'status':'obtained'}
 except Exception as e:return {'id':key,'url':url,'seconds':round(time.monotonic()-started,3),'status':'failed','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: out=list(pool.map(run,entries.items()))
(ROOT/'code/part_c/fetch_c4_sources_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
