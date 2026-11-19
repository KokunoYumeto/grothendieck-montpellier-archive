from pathlib import Path
import urllib.request,concurrent.futures,subprocess,json
P=Path('SA23_work/external/forms');P.mkdir(exist_ok=True)
urls={
'Szymik2014':'https://arxiv.org/pdf/1211.3239',
'QuillenK1973':'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Quillen-Higher-I.pdf',
'Schlichting2002':'https://www.maths.ed.ac.uk/~v1ranick/papers/schlk.pdf',
'Segal1974':'https://ncatlab.org/nlab/files/SegalCategoriesAndCohomologyTheories.pdf',
'HopkinsSinger2005':'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hopksing.pdf',
'May1972':'https://www.math.uchicago.edu/~may/BOOKS/geom_iter.pdf',
'GaitsgoryAlgebroids':'https://people.mpim-bonn.mpg.de/gaitsgde/Book/algebroids.pdf',
'Hatcher':'https://pi.math.cornell.edu/~hatcher/AT/AT.pdf',
'HopfAlgebroids2023':'https://mat.uab.cat/pubmat/fitxers/download/FileType:abstract/FolderName:v67(1)/FileName:A6712301.pdf'
}
def get(k,u):
 try:
  p=P/(k+'.pdf')
  if not p.exists():p.write_bytes(urllib.request.urlopen(u,timeout=50).read())
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True,check=True)
  return dict(key=k,url=u,size=p.stat().st_size,outcome='downloaded and text extracted')
 except Exception as e:return dict(key=k,url=u,outcome=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:r=list(ex.map(lambda x:get(*x),urls.items()))
(P/'download_more_log.json').write_text(json.dumps(r,indent=2))
print(json.dumps(r,indent=2))
