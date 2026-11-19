"""Narrow primary-document retrieval requested by root; all outputs retained."""
from pathlib import Path
import urllib.request,urllib.parse,json,re,subprocess,sys
P=Path(__file__).parent/'primary'
P.mkdir(exist_ok=True)
targets={
 'sga4_index':'https://fabrice.orgogozo.perso.math.cnrs.fr/SGA4/index.html',
 'sga4_old':'https://www.normalesup.org/~forgogozo/SGA4/',
 'EsquisseFr':'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseFr.pdf',
}
if len(sys.argv)>1:
    targets={sys.argv[1]:sys.argv[2]}
for name,url in targets.items():
    rec={'name':name,'url':url}
    try:
        with urllib.request.urlopen(url,timeout=25) as r:
            data=r.read();rec.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'),bytes=len(data))
        ext='.pdf' if data.startswith(b'%PDF') else '.html'
        path=P/(name+ext);path.write_bytes(data);rec['local']=str(path)
        if ext=='.html':
            links=[urllib.parse.urljoin(url,x) for x in re.findall(r'href\s*=\s*[\"\']([^\"\']+)',data.decode('utf-8','replace'),re.I)]
            rec['links']=links
        else:
            txt=P/(name+'.txt')
            sub=subprocess.run(['pdftotext','-layout',str(path),str(txt)],capture_output=True,text=True)
            rec['pdftotext_returncode']=sub.returncode;rec['pdftotext_stderr']=sub.stderr
    except Exception as e:rec['error']=repr(e)
    (P/(name+'_retrieval.json')).write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(rec,ensure_ascii=False,indent=2))
