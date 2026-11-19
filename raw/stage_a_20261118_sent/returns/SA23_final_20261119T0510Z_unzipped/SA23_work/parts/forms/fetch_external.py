from pathlib import Path
import urllib.request,concurrent.futures,fitz,json
P=Path('SA23_work/external/forms')
files={
'Rinehart1963':'https://www.ams.org/journals/tran/1963-108-02/S0002-9947-1963-0154906-3/S0002-9947-1963-0154906-3.pdf',
'Quillen1968etale':'https://math.univ-cotedazur.fr/~cazanave/Gdt/ImJ/Quillenetale.pdf',
'Quillen1971Adams':'https://math.univ-cotedazur.fr/~cazanave/Gdt/ImJ/Quillen.pdf',
'Friedlander1973':'https://www.numdam.org/article/PMIHES_1973__42__5_0.pdf',
'Thom1954':'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/thomcob.pdf',
'Milnor1958':'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Milnor-A.pdf',
'Thomason1980':'https://www.numdam.org/item/CTGDC_1980__21_3_305_0.pdf',
'Benoist2011':'https://www.numdam.org/item/BSMF_2011__139_4_555_0.pdf',
'PoonenSlavov2020':'https://math.mit.edu/~poonen/papers/bertini_locus.pdf'
}
def get(pair):
 k,u=pair
 try:
  b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=55).read();(P/(k+'.pdf')).write_bytes(b)
  d=fitz.open(stream=b,filetype='pdf');s='\n'.join('PDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d));(P/(k+'.txt')).write_text(s)
  r={'key':k,'url':u,'bytes':len(b),'pages':len(d),'textchars':len(s),'status':'downloaded, not automatically read'}
 except Exception as e:r={'key':k,'url':u,'status':str(e)}
 print(json.dumps(r),flush=True);return r
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:r=list(e.map(get,files.items()))
(P/'download_log.json').write_text(json.dumps(r,indent=2)+'\n')
