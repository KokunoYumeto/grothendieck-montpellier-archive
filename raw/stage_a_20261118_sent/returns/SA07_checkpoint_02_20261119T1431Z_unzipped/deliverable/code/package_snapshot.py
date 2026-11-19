"""Package current work, excluding supplied inputs and third-party source bodies.

Raw retrievals remain in scratch. Their exact requests, URL/ref metadata and
SHA-256 hashes are preserved, alongside every authored result and computation.
The checkpoint includes incomplete agent work; final packaging uses integrated
deliverables only. Existing ZIPs are never overwritten or nested.
"""
import argparse,hashlib,json,re,zipfile
from pathlib import Path
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parents[2]
D=BASE/'deliverable'

def web_metadata(p):
    obj=json.loads(p.read_text())
    req={k:obj[k] for k in ('request','query','params','queries','input') if isinstance(obj,dict) and k in obj}
    strings=[]
    def walk(v):
        if isinstance(v,dict):
            for k,x in v.items():
                if k=='text' and isinstance(x,str):strings.append(x)
                elif isinstance(x,(list,dict)):walk(x)
        elif isinstance(v,list):
            for x in v:walk(x)
        elif isinstance(v,str):strings.append(v)
    walk(obj)
    pages=[]
    for txt in strings:
        for m in re.finditer(r'^([^\n]{0,350})\n(【[^\n]+】[^\n]*)',txt,re.M):
            pages.append({'source_heading':m.group(1),'retrieval_metadata':m.group(2)})
    if not pages:
        for txt in strings:
            for url in sorted(set(re.findall(r'https?://[^\s\)\]>"}]+',txt))):pages.append({'url':url})
    return {'raw_file':str(p.relative_to(BASE)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'requests':req,'source_metadata':pages,'note':'Third-party source body omitted; requests, source metadata, exact locators and our own assessments are retained.'}

def main():
    a=argparse.ArgumentParser();a.add_argument('name');a.add_argument('--final',action='store_true');args=a.parse_args()
    dest=BASE/args.name
    if dest.exists():raise SystemExit('Refusing to overwrite existing ZIP')
    candidates=list(D.rglob('*'))
    if not args.final:candidates+=list((BASE/'agents').rglob('*'))
    manifest=[];payload=[]
    for p in sorted(set(candidates)):
        if not p.is_file() or '__pycache__' in p.parts:continue
        rel=p.relative_to(BASE)
        if p.suffix in ('.pdf','.png','.jpg','.jpeg','.zip') or p.name.endswith('_transcription.tex'):continue
        if p.name in ('entries_source.json','source_entries.json'):continue
        if '_transcription.tex.' in p.name or '_notes.md.' in p.name or '_doubts.md.' in p.name:continue
        if p.name.startswith('tex_') or p.name in ('navigation_output.txt','source_index.txt'):continue
        if p.suffix=='.txt' and not any(s in p.name.lower() for s in ('output','command','log','fetch','error')):continue
        arc=str(rel if not args.final else p.relative_to(D))
        data=p.read_bytes()
        if re.match(r'web_?(?:root_)?\d+.*\.json$',p.name) and not any(s in p.name for s in ('request','ledger','metadata')):
            data=(json.dumps(web_metadata(p),ensure_ascii=False,indent=2)+'\n').encode()
            arc=arc.removesuffix('.json')+'_retrieval_metadata.json'
        payload.append((arc,data));manifest.append({'path':arc,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    stamp=datetime.now(timezone.utc).isoformat()
    with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for arc,data in payload:z.writestr(arc,data)
        z.writestr('SNAPSHOT_MANIFEST.json',json.dumps({'created_utc':stamp,'final':args.final,'members':manifest,'inputs':'Use the original supplied ZIP and PROMPT; attachments and earlier checkpoints are intentionally not embedded.','source_body_policy':'Downloaded third-party books/articles and their full tool excerpts are not redistributed; retrieval request/URL metadata, hashes, citations, locators, authored analysis and computation outputs are included.'},indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'path':str(dest),'bytes':dest.stat().st_size,'members':len(payload)+1,'created_utc':stamp},indent=2))

if __name__=='__main__':main()
