#!/usr/bin/env python3
"""Measure the supplied, unchecked combined sources as a syntax/layout baseline.

The diagnostic PDFs are temporary and are never publication deliverables or
sources of readings. This script changes only the scan macro to log page keys.
"""
import argparse,concurrent.futures,json,pathlib,re,subprocess,sys
from bootstrap_tex import tex_env
from compile_readers import parse_log,sanitized

def run_one(source,edition,runtime,temporary):
    name=source.parent.name;folder=temporary/('original_'+name);folder.mkdir(parents=True,exist_ok=True)
    text=source.read_text();macro=r'\newcommand{\scanpage}[1]{'
    key='esq119_119_' if name.endswith('copy2') else 'esq_119_'
    text=text.replace(macro,macro+r'\typeout{ORIGINAL-SCAN: #1; PDFPAGE: \thepage}',1)
    path=folder/'original.tex';path.write_text(text)
    env=tex_env(runtime);env['max_print_line']='10000'
    r=subprocess.run(['lualatex','-interaction=nonstopmode','-file-line-error','original.tex'],cwd=folder,env=env,capture_output=True,text=True,timeout=180)
    log=(folder/'original.log').read_text(errors='replace');parsed=parse_log(log,text)
    for box in parsed['overfull']:
        line=box['source_line']
        if line:
            prefix='\n'.join(text.splitlines()[:line]);scans=list(re.finditer(r'\\scanpage\{119/(\d+)\}',prefix))
            if scans:box['page_key']=key+f'{int(scans[-1][1]):03d}'
    parsed['source']=source.relative_to(source.parents[2]).as_posix();parsed['status']='unchecked supplied-source diagnostic; not a reader';parsed['exit_code']=r.returncode
    logs=edition/'build_logs';logs.mkdir(exist_ok=True)
    (logs/('ORIGINAL_'+name+'.log')).write_text(sanitized(log,edition,runtime))
    (logs/('ORIGINAL_'+name+'.json')).write_text(json.dumps(parsed,ensure_ascii=False,indent=2)+'\n')
    return {'source':name,'errors':len(parsed['errors']),'overfull':len(parsed['overfull']),'over_2pt':sum(b['points']>2 for b in parsed['overfull']),'widest':max((b['points'] for b in parsed['overfull']),default=0),'locations':parsed['overfull']}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source',type=pathlib.Path);p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);a=p.parse_args();root=a.root.resolve();runtime=root.parent/'tex-runtime';tmp=root.parent/'build'
    sources=sorted(a.source.glob('transcription/*/*_combined.tex'))
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        results=list(pool.map(lambda s:run_one(s.resolve(),root,runtime,tmp),sources))
    (root/'ORIGINAL_BUILD_BASELINE.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    for item in results:print(json.dumps(item,ensure_ascii=False),flush=True)
