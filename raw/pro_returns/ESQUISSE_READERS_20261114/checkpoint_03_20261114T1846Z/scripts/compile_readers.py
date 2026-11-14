#!/usr/bin/env python3
"""Compile standalone sources and record measured PDF/log properties.

Visual inspection is recorded separately; automated geometry never substitutes
for looking at a rendered page.
"""
from __future__ import annotations
import argparse,collections,csv,datetime,json,os,pathlib,re,shutil,subprocess,sys
from bootstrap_tex import tex_env

def sanitized(text,edition,runtime):
    for p,label in [(str(edition),'EDITION'),(str(runtime),'TEX-RUNTIME'),('/usr/share/texlive/texmf-dist','TEXLIVE'),('/usr/share/texmf','TEXMF')]:
        text=text.replace(p,label)
    # TeX wraps paths at max_print_line. Raw logs remain outside deliverables.
    text=re.sub(r'/workspace/[^\s()<>]+','[workspace-file]',text)
    text=re.sub(r'/home/[^\s()<>]+','[runtime-file]',text)
    return text

def parse_log(log,source):
    over=[]
    for m in re.finditer(r'Overfull \\([hv])box \(([0-9.]+)pt too (wide|high)\)([^\n]*)',log):
        tail=m[4];line=re.search(r'(?:at lines?|in paragraph at lines?) (\d+)(?:--(\d+))?',tail)
        lineno=int(line[1]) if line else None
        key=None
        if lineno:
            prefix='\n'.join(source.splitlines()[:lineno]);hits=re.findall(r'% BEGIN PAGE ([^\n]+)',prefix)
            if hits:key=hits[-1]
        over.append({'kind':m[1],'points':float(m[2]),'direction':m[3],'source_line':lineno,'page_key':key,'context':tail.strip()})
    missing=re.findall(r'Missing character:[^\n]*',log)
    errors=re.findall(r'^!.*$',log,re.M)
    warnings=re.findall(r'^(?:LaTeX|Package [^\n]+|Class [^\n]+|Font [^\n]+).*Warning[^\n]*',log,re.M)
    scans=[{'key':m[1],'pdf_page':int(m[2])} for m in re.finditer(r'EDITION-SCAN: ([^;]+); PDFPAGE: (\d+)',log)]
    return {'errors':errors,'warnings':warnings,'overfull':over,'missing_characters':missing,'scan_pages':scans}

def inspect_pdf(pdf):
    import fitz
    doc=fitz.open(pdf);uris=[];outside_sheet=[];outside_type=[];landscape=[];text_counts=[]
    for i,p in enumerate(doc):
        w,h=p.rect.width,p.rect.height
        if w>h:landscape.append(i+1)
        # Main text, running folios, and the expressly reserved marginal-note lane.
        allowed=fitz.Rect(22/25.4*72-1,20/25.4*72-1,w-5/25.4*72+1,h-18/25.4*72+1)
        for kind,box,*rest in p.get_bboxlog():
            if kind not in ('fill-text','stroke-text','fill-path','stroke-path','fill-image'):continue
            r=fitz.Rect(box)
            if not p.rect.contains(r):outside_sheet.append({'pdf_page':i+1,'kind':kind,'bbox':list(box)})
            if not allowed.contains(r):outside_type.append({'pdf_page':i+1,'kind':kind,'bbox':list(box)})
        for link in p.get_links():
            if link.get('uri'):uris.append({'pdf_page':i+1,'uri':link['uri']})
        text_counts.append(len(p.get_text()))
    # Examine individual characters in extracted lines to distinguish the expressly
    # permitted overhang of one letter from an actual text-area violation.
    conservative_candidates=outside_type;outside_type=[];single_overhang=[]
    for i,p in enumerate(doc):
        mainleft=22/25.4*72;mainright=p.rect.width-34/25.4*72
        marginleft=mainright+5/25.4*72;marginright=marginleft+23/25.4*72
        for block in p.get_text('rawdict')['blocks']:
            for line in block.get('lines',[]):
                chars=[c for sp in line['spans'] for c in sp['chars'] if c['c'].strip()]
                if not chars:continue
                chars.sort(key=lambda c:c['bbox'][0]);left=min(c['bbox'][0] for c in chars)
                lo,hi=(marginleft,marginright) if left>=marginleft-2 else (mainleft,mainright)
                leftbad=[j for j,c in enumerate(chars) if c['bbox'][0]<lo-.15]
                rightbad=[j for j,c in enumerate(chars) if c['bbox'][2]>hi+.15]
                vertical=[j for j,c in enumerate(chars) if c['bbox'][1]<20/25.4*72-1 or c['bbox'][3]>p.rect.height-18/25.4*72+1]
                oneleft=not leftbad or leftbad==[0];oneright=not rightbad or rightbad==[len(chars)-1]
                if vertical or not oneleft or not oneright:
                    outside_type.append({'pdf_page':i+1,'kind':'text line','bbox':list(line['bbox']),'text':''.join(c['c'] for c in chars),'left_offending_characters':len(leftbad),'right_offending_characters':len(rightbad),'vertical_offending_characters':len(vertical)})
                elif leftbad or rightbad:
                    single_overhang.append({'pdf_page':i+1,'line':''.join(c['c'] for c in chars),'left':chars[0]['c'] if leftbad else '', 'right':chars[-1]['c'] if rightbad else ''})
    external=len(uris);archive=[u for u in uris if 'grothendieck.umontpellier.fr/web/viewer.html?' in u['uri']]
    targets=collections.defaultdict(set)
    for item in archive:
        m=re.search(r'file=\.\./(\d+)\.pdf#page=(\d+)',item['uri'])
        if m:targets[m[1]].add(int(m[2]))
    internal=sum(1 for p in doc for l in p.get_links() if not l.get('uri'))
    return {'pdf_pages':len(doc),'external_link_annotations':external,'archive_link_annotations':len(archive),'internal_link_annotations':internal,'archive_distinct_pdf_pages':{c:sorted(ns) for c,ns in targets.items()},'ink_outside_sheet':outside_sheet,'ink_outside_type_area':outside_type,'single_glyph_overhangs':single_overhang,'conservative_bbox_candidates':conservative_candidates,'landscape_pages':landscape,'characters_by_pdf_page':text_counts}

def compile_one(tex,edition,runtime,buildroot,passes):
    name=tex.stem;build=buildroot/name;build.mkdir(parents=True,exist_ok=True);target=build/tex.name
    shutil.copy2(tex,target);env=tex_env(runtime);env['max_print_line']='10000'
    runs=[]
    for n in range(passes):
        r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',target.name],cwd=build,env=env,capture_output=True,text=True)
        runs.append({'pass':n+1,'exit_code':r.returncode})
        (build/f'console-{n+1}.txt').write_text(r.stdout+r.stderr)
        if r.returncode:break
    log=(build/(name+'.log')).read_text(errors='replace') if (build/(name+'.log')).exists() else r.stdout+r.stderr
    source_text=target.read_text()
    parsed=parse_log(log,source_text);parsed.update(status=(re.search(r'% EDITION STATUS: (\w+); source units ([0-9/]+)',source_text).group(0) if '% EDITION STATUS:' in source_text else 'partial development build'),source_sha256=__import__('hashlib').sha256(target.read_bytes()).hexdigest(),name=name,runs=runs,source=tex.relative_to(edition).as_posix(),compiled_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
    logs=edition/'build_logs';logs.mkdir(exist_ok=True)
    (logs/(name+'.log')).write_text(sanitized(log,edition,runtime))
    pdf=build/(name+'.pdf')
    if pdf.exists() and r.returncode==0:
        shutil.copy2(pdf,tex.with_suffix('.pdf'));parsed.update(inspect_pdf(pdf))
    (logs/(name+'.json')).write_text(json.dumps(parsed,ensure_ascii=False,indent=2)+'\n')
    with (edition/'BUILD_HISTORY.jsonl').open('a') as f:f.write(json.dumps(parsed,ensure_ascii=False)+'\n')
    return parsed

def main():
    p=argparse.ArgumentParser();p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);p.add_argument('--runtime',type=pathlib.Path);p.add_argument('--build-root',type=pathlib.Path);p.add_argument('--names',nargs='*');p.add_argument('--passes',type=int,default=3);a=p.parse_args();edition=a.root.resolve();runtime=(a.runtime or edition.parent/'tex-runtime').resolve();buildroot=(a.build_root or edition.parent/'build').resolve()
    paths=sorted(p for d in ['FR','EN','GUIDE'] for p in (edition/d).glob('*.tex'))
    if a.names:paths=[p for p in paths if p.stem in a.names]
    summaries=[]
    for tex in paths:
        r=compile_one(tex,edition,runtime,buildroot,a.passes);summaries.append(r)
        print(json.dumps({'reader':r['name'],'exit_code':r['runs'][-1]['exit_code'],'pages':r.get('pdf_pages'),'overfull_count':len(r['overfull']),'widest':max([b['points'] for b in r['overfull']],default=0),'missing':len(r['missing_characters']),'outside_sheet':len(r.get('ink_outside_sheet',[]))}),flush=True)
    checks={}
    if (edition/'PDF_CHECKS.json').exists():checks=json.loads((edition/'PDF_CHECKS.json').read_text())
    checks.update({r['name']:r for r in summaries});(edition/'PDF_CHECKS.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':main()
