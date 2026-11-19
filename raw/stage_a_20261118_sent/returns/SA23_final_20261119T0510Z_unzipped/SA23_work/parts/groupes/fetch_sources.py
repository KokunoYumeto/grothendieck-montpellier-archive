"""Retrieve publicly available primary sources; raw texts stay outside deliverables."""
import concurrent.futures, hashlib, json, pathlib, subprocess, urllib.request

BASE = pathlib.Path(__file__).resolve().parent
EXT = BASE / 'external'
EXT.mkdir(exist_ok=True)
SOURCES = {
    'riehl-context-current': 'https://emilyriehl.github.io/files/context.pdf',
    'ziegler-1111.1981': 'https://arxiv.org/pdf/1111.1981',
    'kelly-tac10': 'https://tac.mta.ca/tac/reprints/articles/10/tr10.pdf',
    'batanin-kock-weber-1510.08934': 'https://arxiv.org/pdf/1510.08934',
    'karazeris-flatness': 'https://www.tac.mta.ca/tac/volumes/12/5/12-05.pdf',
}

def retrieve(pair):
    key,url = pair
    path = EXT / (key+'.pdf')
    try:
        if not path.exists():
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
            path.write_bytes(urllib.request.urlopen(req,timeout=45).read())
        if not path.read_bytes().startswith(b'%PDF'):
            raise ValueError('Response is not PDF')
        txt=EXT / (key+'.txt')
        subprocess.run(['pdftotext','-layout',str(path),str(txt)],check=True)
        return {'key':key,'url':url,'status':'downloaded and text extracted; not itself proof of reading',
                'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    except Exception as exc:
        return {'key':key,'url':url,'status':'failed','error':str(exc)}

if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        results=list(pool.map(retrieve,SOURCES.items()))
    (BASE/'retrieval_audit.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))
