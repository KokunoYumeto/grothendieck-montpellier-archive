#!/usr/bin/env python3
"""Audit links, source-page coverage and required visual-review samples.

Rendering does not mark a page as visually inspected. Reviewers must append an
observation to VISUAL_QA.tsv with the exact PDF hash after looking at each image.
"""
from __future__ import annotations
import argparse,collections,csv,hashlib,json,pathlib,re
import fitz
from PIL import Image,ImageDraw,ImageFont
from edition_core import macros,replace_ranges,strip_comments
from build_edition import read_tsv,write_tsv,load_json,input_snapshot
from pdf_links import external_link_groups
from probe_rendering import current_probe_verification
from compile_readers import measurement_code_snapshot

def audit_dependency_snapshot(root):
    """Hashes of every audit-only input, using publication-relative names."""
    names=['VISUAL_QA.tsv','BUILD_HISTORY.jsonl','PDF_CHECKS.json','BUILD_INPUTS.json','ORIGINAL_BUILD_BASELINE.json','records/GEOMETRY_REPAIR_HISTORY.json','records/RENDERING_PROBE.json','scripts/pdf_final_audit.py','scripts/pdf_links.py','scripts/probe_rendering.py','scripts/build_edition.py','scripts/edition_core.py','scripts/compile_readers.py','scripts/bootstrap_tex.py']
    return {name:hashlib.sha256((root/name).read_bytes()).hexdigest() if (root/name).exists() else None for name in names}

def unescape_url(s):return s.replace(r'\#','#').replace(r'\%','%').replace(r'\&','&')

def source_projection(source):
    diplomatic=bool(re.search(r'^\\diplomatictrue$',source,re.M));reading=bool(re.search(r'^\\readingtrue$',source,re.M))
    scans={m.arguments[0]:{'url':unescape_url(m.arguments[1]),'key':m.arguments[2]} for m in macros(source,{'DeclareScan'}) if m.arguments[0]!='#1'}
    variants={m.arguments[0]:m.arguments[1] for m in macros(source,{'DeclareVariant'}) if m.arguments[0]!='#1'}
    pages=[(m[1],m[2]) for m in re.finditer(r'% BEGIN PAGE (\S+)\n(.*?)\n\\finishscan\n% END PAGE \1',source,re.S)]
    events=[];app=[];scan_keys=[];deferred=[]
    def walk(text,current='',apparatus=False):
        for m in macros(text):
            a=m.arguments;n=m.name
            if n=='scanpage':
                info=scans[a[0]];current=info['url'];scan_keys.append(info['key']);events.append({'kind':'scan mark','uri':current,'source_key':info['key']})
            elif n in ('unsure','illegible'):
                events.append({'kind':'doubt mark','uri':current});
                if n=='unsure':walk(a[0],current,apparatus)
            elif n=='href':
                uri=current if a[0]==r'\CurrentScanURL' else unescape_url(a[0]);events.append({'kind':'explicit link','uri':uri});walk(a[1],current,apparatus)
            elif n=='scancontext':walk(a[1],unescape_url(a[0]),apparatus)
            elif n=='var':
                if diplomatic and not apparatus:walk(a[0],current,apparatus)
                else:
                    walk(a[1],current,apparatus)
                    if not reading and not apparatus:
                        app.append({'id':a[3],'class':'wording variant'});deferred.append((variants[a[3]],current))
            elif n=='frapparatus':
                if not reading:
                    app.append({'id':a[0],'class':'French source apparatus'});deferred.append((variants[a[0]],current))
            elif n=='tnote':
                if not reading:
                    app.append({'id':a[0],'class':'translator note'});deferred.append((a[1],current))
            elif n=='copytwo':
                if not diplomatic and not reading:
                    app.append({'id':a[0],'class':'copy 2 annotation'});deferred.append((a[1],current))
            elif n=='sourceglyph':pass
            elif n=='notecall':walk(a[2],current,apparatus)
            elif n=='notedef':walk(a[1],current,apparatus)
            elif n in ('DeclareVariant','DeclareScan'):pass
            else:
                for content in a:walk(content,current,apparatus)
        return current
    if pages:
        for key,body in pages:
            if key.startswith('esq119_') and not diplomatic:continue
            walk(body)
            while deferred:
                content,url=deferred.pop(0);walk(content,url,True)
    else:
        body=source.split(r'\begin{document}',1)[1].split(r'\end{document}',1)[0]
        walk(body)
        while deferred:
            content,url=deferred.pop(0);walk(content,url,True)
    return {'diplomatic':diplomatic,'reading':reading,'source_keys':scan_keys,'events':events,'apparatus':app}

def source_page_spans(check,pdf_pages):
    starts=check.get('scan_pages',[]);spans={}
    for i,item in enumerate(starts):
        stop=starts[i+1]['pdf_page'] if i+1<len(starts) else pdf_pages+1
        spans[item['key']]=list(range(item['pdf_page'],stop))
    return spans

def visible_page_bodies(source,projection):
    """Project running source content, keeping its note-call macros intact."""
    def running(text):
        replacements=[]
        for m in macros(text,{'var','tnote','copytwo','frapparatus'}):
            value=running(m.arguments[0 if projection['diplomatic'] else 1]) if m.name=='var' else ''
            replacements.append((m.start,m.end,value))
        return strip_comments(replace_ranges(text,replacements))
    return {m[1]:running(m[2]) for m in re.finditer(r'% BEGIN PAGE (\S+)\n(.*?)\n\\finishscan\n% END PAGE \1',source,re.S) if not m[1].startswith('esq119_') or projection['diplomatic']}

def author_footnote_placements(doc,bodies,spans):
    """Locate only the anchored source marks, separately from apparatus quotes."""
    pattern=re.compile(r'\(\s*(\*\s*(?:\*\s*)?)\)');out=[];names=doc.resolve_names()
    for key,body in bodies.items():
        counts=collections.Counter(re.sub(r'\s','',m[1]) for m in pattern.finditer(body))
        anchored=list(macros(body,{'authorstar'},recursive=True));circled=list(macros(body,{'handcircle'},recursive=True))
        for mark,count in counts.items():
            if count<2:continue # The sommaire mentions (*) once, without a local note.
            found=[];pages=collections.Counter();raw_pages={};problems=[]
            for m in anchored:
                if re.sub(r'\s','',m.arguments[1])!='('+mark+')':continue
                destination='star-'+m.arguments[0];target=names.get(destination);page=target['page']+1 if target else None
                if page is not None:pages[page]+=1
                found.append({'id':m.arguments[0],'destination':destination,'literal_mark':m.arguments[1],'pdf_page':page,'position':list(target['to']) if target else None,'inside_source_span':page in spans.get(key,[]),'inside_handcircle':any(c.start<=m.start and m.end<=c.end for c in circled)})
                if target is None:problems.append('Source star destination absent: '+destination)
                elif page not in spans.get(key,[]):problems.append('Source star destination outside its source-page span: '+destination)
            if len(found)!=count:problems.append('The source literal count differs from its anchored star count.')
            for n in spans.get(key,[]):
                total=sum(1 for m in pattern.finditer(doc[n-1].get_text()) if re.sub(r'\s','',m[1])==mark)
                if total:raw_pages[n]=total
            if len(pages)!=1:problems.append('Source call and starred note occupy different physical pages or are absent.')
            out.append({'source_key':key,'marker':'('+mark+')','expected_instances':count,'pdf_page_instances':dict(pages),'pdf_text_mark_instances_including_apparatus':raw_pages,'source_anchors':found,'problems':problems,'same_physical_page':not problems and len(pages)==1 and sum(pages.values())==count})
    return out

def endnote_links(doc,bodies,spans):
    names=doc.resolve_names();calls=[];definitions={};checks=[]
    for key,body in bodies.items():
        for m in macros(body,{'notecall','notedef'},recursive=True):
            if m.name=='notecall':calls.append({'note':m.arguments[0],'anchor':m.arguments[1],'source_key':key})
            else:definitions[m.arguments[0]]=key
    for call in calls:
        dest='note-'+call['note'];origin=names.get(call['anchor']);target=names.get(dest);definition=definitions.get(call['note']);problems=[]
        if origin is None:problems.append('call anchor absent from PDF destinations')
        if target is None:problems.append('note anchor absent from PDF destinations')
        if definition is None:problems.append('note definition absent from generated source')
        if origin and origin['page']+1 not in spans.get(call['source_key'],[]):problems.append('call anchor resolves outside its source-page span')
        if target and target['page']+1 not in spans.get(definition,[]):problems.append('note anchor resolves outside its source-page span')
        forward=sum(l.get('nameddest')==dest for l in doc[origin['page']].get_links()) if origin else 0
        backward=sum(l.get('nameddest')==call['anchor'] for l in doc[target['page']].get_links()) if target else 0
        if forward!=1:problems.append('expected exactly one forward named link from this call page')
        if backward!=1:problems.append('expected exactly one return named link from this note page')
        checks.append({**call,'definition_source_key':definition,'call_pdf_page':origin['page']+1 if origin else None,'note_pdf_page':target['page']+1 if target else None,'forward_links':forward,'return_links':backward,'problems':problems})
    return {'calls':len(calls),'definitions':len(definitions),'checks':checks,'problems':sum(bool(c['problems']) for c in checks)}

def marginal_note_audit(doc,placements):
    text='\n'.join(p.get_text() for p in doc);labels=len(re.findall(r'(?:Marginal note|Note marginale)\s*:',text));problems=[]
    blocks=sum(p['placement']=='block' for p in placements)
    for i,p in enumerate(placements,1):
        if p['placement']=='margin' and (p['lines']>3 or p.get('within_three_line_height') is not True):problems.append({'occurrence':i,'source_key':p['key'],'problem':'Margin placement lacks a passing actual line-count and height measurement.'})
        if p['placement']=='block' and p.get('labelled_block') is not True:problems.append({'occurrence':i,'source_key':p['key'],'problem':'Block placement lacks its emitted label confirmation.'})
    if labels!=blocks:problems.append({'problem':'Printed marginal-note labels differ from block placements.','expected':blocks,'printed':labels})
    return {'placements':len(placements),'in_margin':len(placements)-blocks,'in_labelled_blocks':blocks,'printed_block_labels':labels,'problems':problems}

def sample_pages(n,count=40):
    if n<=count:return list(range(1,n+1))
    return sorted(set(1+round(i*(n-1)/(count-1)) for i in range(count)))

def audit_one(tex,root,checks,history,visual):
    pdf=tex.with_suffix('.pdf');name=tex.stem;source=tex.read_text();projection=source_projection(source);doc=fitz.open(pdf)
    expected=collections.Counter(e['uri'] for e in projection['events']);link_groups=external_link_groups(doc)
    actual=collections.Counter(l['uri'] for l in link_groups['logical_links']);rectangles=collections.Counter(l['uri'] for l in link_groups['annotation_rectangles'])
    check=checks.get(name,{});spans=source_page_spans(check,len(doc));old_keys=set();bodies=visible_page_bodies(source,projection)
    footnotes=author_footnote_placements(doc,bodies,spans);notes=endnote_links(doc,bodies,spans);marginal=marginal_note_audit(doc,check.get('marginal_note_placements',[]))
    expected_entries=collections.Counter(a['id'] for a in projection['apparatus']);printed_entries=collections.Counter(a['id'] for a in check.get('printed_apparatus_entries',[]))
    apparatus_mismatches=[{'id':ident,'source':expected_entries[ident],'printed':printed_entries[ident]} for ident in sorted(set(expected_entries)|set(printed_entries)) if expected_entries[ident]!=printed_entries[ident]]
    for run in history:
        if run.get('name')==name:
            old_keys.update(b['page_key'] for b in run.get('overfull',[]) if b.get('page_key'))
            old_spans=source_page_spans(run,run.get('pdf_pages',0))
            for violation in run.get('ink_outside_type_area',[])+run.get('ink_outside_sheet',[]):
                old_keys.update(key for key,ns in old_spans.items() if violation['pdf_page'] in ns)
            for page in run.get('landscape_pages',[]):old_keys.update(key for key,ns in old_spans.items() if page in ns)
    for run in load_json(root/'records/GEOMETRY_REPAIR_HISTORY.json',[]):
        if run['reader']==name:old_keys.update(run['source_keys'])
    for old in load_json(root/'ORIGINAL_BUILD_BASELINE.json',[]):old_keys.update(b['page_key'] for b in old.get('locations',[]) if b.get('page_key'))
    mandatory=set(check.get('landscape_pages',[]))
    if check.get('scan_pages'):mandatory.update(range(1,min(x['pdf_page'] for x in check['scan_pages'])))
    for key in old_keys:mandatory.update(spans.get(key,[]))
    # The source-glyph and font-slot repairs also receive explicit visual checks.
    for key in ['esq_119_002','esq_119_011','esq_119_013','esq_119_016','esq_119_026','esq_119_042','esq_119_043','esq_119_044','esq_119_051','esq_119_058','esq119_119_078','esq119_119_087','esq119_119_092','esq119_119_095','esq119_119_118','esq119_119_119','esq119_119_120','esq119_119_127','esq119_119_134']:mandatory.update(spans.get(key,[]))
    required=set(sample_pages(len(doc)))|mandatory;digest=hashlib.sha256(pdf.read_bytes()).hexdigest();seen={int(r['pdf_page']) for r in visual if r['reader']==name and r['pdf_sha256']==digest and r['status']=='visually inspected'}
    mismatches=[{'uri':uri,'expected_logical_links':expected[uri],'pdf_logical_links':actual[uri],'pdf_annotation_rectangles':rectangles[uri]} for uri in sorted(set(expected)|set(actual)) if expected[uri]!=actual[uri]]
    actual_by_id={item['id']:item for item in link_groups['logical_links']}
    sequence_mismatches=[]
    for i,event in enumerate(projection['events'],1):
        ident='edlink-'+str(i);found=actual_by_id.get(ident)
        if found is None or found['uri']!=event['uri']:sequence_mismatches.append({'id':ident,'source_event':event,'pdf_uri':found['uri'] if found else None})
    for ident in actual_by_id:
        if not re.fullmatch(r'edlink-[1-9][0-9]*',ident) or int(ident.split('-')[1])>len(projection['events']):sequence_mismatches.append({'id':ident,'problem':'PDF logical link has no projected source event.'})
    recorded_inputs=load_json(root/'BUILD_INPUTS.json',{}).get('input_sha256',{});current_inputs=input_snapshot(root)
    input_mismatches=[p for p in sorted(set(recorded_inputs)|set(current_inputs)) if recorded_inputs.get(p)!=current_inputs.get(p)]
    return {'reader':name,'status':check.get('status','unrecorded build'),'pdf_sha256':digest,'source_sha256':hashlib.sha256(tex.read_bytes()).hexdigest(),'compiled_source_matches':check.get('source_sha256')==hashlib.sha256(tex.read_bytes()).hexdigest(),'compiled_pdf_matches':check.get('pdf_sha256')==digest and check.get('pdf_compilation_succeeded') is True,'measurement_code_matches':check.get('measurement_code_sha256')==measurement_code_snapshot(root) and check.get('measurement_code_unchanged_during_run') is True,'measurement_code_sha256':check.get('measurement_code_sha256',{}),'upstream_input_mismatches':input_mismatches,'source_pages':len(projection['source_keys']),'source_keys':projection['source_keys'],'pdf_pages':len(doc),'expected_link_count':sum(expected.values()),'pdf_external_link_annotations':sum(rectangles.values()),'pdf_external_logical_links':sum(actual.values()),'executed_external_link_count':check.get('executed_external_link_count'),'logical_link_tracking_issues':link_groups['issues'],'logical_link_sequence_mismatches':sequence_mismatches,'logical_link_source_events':projection['events'],'logical_link_rectangles':link_groups['logical_links'],'link_count_mismatches':mismatches,'expected_archive_pages':sorted(set(e['uri'] for e in projection['events'] if 'grothendieck.umontpellier.fr/web/viewer.html?' in e['uri'])),'source_apparatus_entries':len(projection['apparatus']),'apparatus_by_class':dict(collections.Counter(a['class'] for a in projection['apparatus'])),'executed_apparatus_entries':check.get('executed_apparatus_entries'),'printed_apparatus_entries':len(check.get('printed_apparatus_entries',[])),'apparatus_entry_mismatches':apparatus_mismatches,'author_footnote_placements':footnotes,'endnote_link_audit':notes,'marginal_note_placements':check.get('marginal_note_placements',[]),'marginal_note_audit':marginal,'required_visual_pages':sorted(required),'mandatory_visual_pages':sorted(mandatory),'visually_inspected_pages':sorted(seen),'uninspected_required_pages':sorted(required-seen),'errors':check.get('errors',[]),'warnings':check.get('warnings',[]),'overfull':check.get('overfull',[]),'missing_characters':check.get('missing_characters',[]),'ink_outside_sheet':check.get('ink_outside_sheet',[]),'ink_outside_type_area':check.get('ink_outside_type_area',[]),'justified_geometry_exclusions':check.get('justified_geometry_exclusions',[]),'permitted_single_glyph_overhangs':len(check.get('single_glyph_overhangs',[]))}

def render_samples(tex,result,destination):
    doc=fitz.open(tex.with_suffix('.pdf'));folder=destination/tex.stem;folder.mkdir(parents=True,exist_ok=True);pages=result['required_visual_pages'];paths=[]
    for n in pages:
        p=folder/f'page_{n:03d}.png';doc[n-1].get_pixmap(matrix=fitz.Matrix(1.25,1.25)).save(p);paths.append((n,p))
    # Each page retains roughly 72-dpi full-sheet resolution on the contact sheet;
    # individual 90-dpi renderings remain available for closer inspection.
    sheetpaths=[]
    for start in range(0,len(paths),4):
        group=paths[start:start+4];width=596;height=868;sheet=Image.new('RGB',(width*2,height*2),'#e3e6e9');draw=ImageDraw.Draw(sheet)
        for j,(n,p) in enumerate(group):
            im=Image.open(p).convert('RGB');im.thumbnail((width,height-26));x=(j%2)*width;y=(j//2)*height;draw.text((x+8,y+5),f'{tex.stem} — PDF page {n}',fill='black');sheet.paste(im,(x+(width-im.width)//2,y+25))
        sp=folder/f'sheet_{start//4+1:02d}.png';sheet.save(sp);sheetpaths.append(sp.name)
    index={'reader':tex.stem,'pdf_sha256':result['pdf_sha256'],'source_sha256':result['source_sha256'],'pages':pages,'sheets':sheetpaths,'page_render_dpi':90,'sheet_layout':'two columns, two rows','renderings':'Reproducible intermediate images; page and sheet filenames are relative to this reader rendering directory.'}
    encoded=json.dumps(index,indent=2)+'\n';(folder/'RENDER_INDEX.json').write_text(encoded)
    retained=tex.parent.parent/'records/render_indices';retained.mkdir(parents=True,exist_ok=True);(retained/(tex.stem+'.json')).write_text(encoded)
    return {'reader':tex.stem,'pages':len(pages),'sheets':len(sheetpaths)}

def report(root,results,visual):
    lines=['# Typesetting report','', 'This report gives measured results for the current PDFs. A partial working edition is identified explicitly. Rendered pages are counted as inspected only when a reviewer has recorded an observation against the exact PDF hash.','', '## Current build measurements','', '| PDF | Source pages | PDF pages | LaTeX errors | Overfull boxes | Widest (pt) | Missing characters | External links | Inspected / required |','|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for r in results:
        lines.append('| '+r['reader']+' | '+str(r['source_pages'])+' | '+str(r['pdf_pages'])+' | '+str(len(r['errors']))+' | '+str(len(r['overfull']))+' | '+str(max((b['points'] for b in r['overfull']),default=0))+' | '+str(len(r['missing_characters']))+' | '+str(r['pdf_external_link_annotations'])+' | '+str(len(set(r['visually_inspected_pages'])&set(r['required_visual_pages'])))+' / '+str(len(r['required_visual_pages']))+' |')
    lines+=['','## Baseline and repair history','']
    for b in load_json(root/'ORIGINAL_BUILD_BASELINE.json',[]):lines.append(f"- The supplied unchecked {b['source']} combined source, run as a diagnostic with LuaLaTeX, produced {b['errors']} errors and {b['overfull']} overfull boxes, widest {b['widest']} pt. Its diagnostic PDF is excluded from the readers. The supplied earlier pdfLaTeX record reported 35 errors; the engine and run are distinguished here.")
    lines+=['','The first partial French build exposed three missing Γ characters inside a math-roman command. The fontspec no-math setting preserves the required math-font slots. Breakable underlining repairs the initial unbreakable prose boxes without changing their text. Individual repairs and page keys are recorded in TYPESETTING_FIXES.tsv; syntax repairs are recorded in CLEANUP_LOG.tsv.','', '## Per-PDF findings','']
    for r in results:
        lines+=['### '+r['reader'],'',r['status']+'.','',f"The current source and compiled-source hash {'agree' if r['compiled_source_matches'] else 'DO NOT AGREE; this PDF requires rebuilding'}. Expected logical external links: {r['expected_link_count']}; identified PDF logical links: {r.get('pdf_external_logical_links','not yet tracked')}; PDF external-link annotation rectangles: {r['pdf_external_link_annotations']}. Distinct archive pages linked: {len(r['expected_archive_pages'])}.",f"Apparatus entries in the projected source: {r['source_apparatus_entries']}; executed counter in the build log: {r['executed_apparatus_entries']}. Classes: "+', '.join(f'{k}: {v}' for k,v in r['apparatus_by_class'].items())+'.',f"Ink outside the sheet: {len(r['ink_outside_sheet'])} candidates; text-area violations: {len(r['ink_outside_type_area'])}; permitted isolated glyph overhangs: {r['permitted_single_glyph_overhangs']}."]
        lines+=[f"Printed nonempty apparatus bodies: {r.get('printed_apparatus_entries','not yet logged')}; per-ID projection/print differences: {len(r.get('apparatus_entry_mismatches',[]))}. Every printed body is guarded against an undefined or empty declaration."]
        lines+=[f"Current PDF hash matches the successful compilation record: {r.get('compiled_pdf_matches',False)}. Upstream inputs changed since generation: {len(r.get('upstream_input_mismatches',[]))}."]
        lines+=[f"Measurement code matches the recorded build: {r.get('measurement_code_matches',False)}. Per-link source/PDF sequence differences: {len(r.get('logical_link_sequence_mismatches',[]))}."]
        footnotes=r.get('author_footnote_placements',[]);badfootnotes=[x for x in footnotes if not x['same_physical_page']];endnotes=r.get('endnote_link_audit',{})
        lines+=[f"Source starred-footnote pairs checked: {len(footnotes)}; pairs split across physical pages or with mismatched marker counts: {len(badfootnotes)}. Endnote calls: {endnotes.get('calls','not yet checked')}; definitions: {endnotes.get('definitions','not yet checked')}; forward/return-link problems: {endnotes.get('problems','not yet checked')}."]
        if footnotes:lines+=['','Starred-footnote placements:']+[f"- {x['source_key']} {x['marker']}: "+', '.join(f'PDF page {p} has {n} marks' for p,n in x['pdf_page_instances'].items())+('.' if x['same_physical_page'] else '; requires repair or an explicit source-page continuation mark.') for x in footnotes]
        margins=r.get('marginal_note_placements',[])
        if margins:lines+=['',f"Marginal-note placements: {sum(x['placement']=='margin' for x in margins)} in the margin, {sum(x['placement']=='block' for x in margins)} labelled in the text block. The LuaLaTeX renderer counts actual line boxes at footnote size; it also enforces a height of at most three footnote-size baselines for a marginal placement."]
        exclusions=r.get('justified_geometry_exclusions',[])
        if exclusions:lines+=['',f"Geometric exclusions, each retaining its measured box in the JSON audit: {len(exclusions)}. These are ink inside the reserved marginal-note frame, printed page numbers in the narrow footer frame, or conservative stroke boxes whose exact butt-capped rule endpoints remain inside the main frame. Paths and images are otherwise checked against the declared main and margin frames; the footer allowance applies only to the printed folio."]
        if r.get('apparatus_entry_mismatches'):lines+=['','Apparatus discrepancies requiring repair:']+[f"- {x['id']}: projected {x['source']}, printed {x['printed']}." for x in r['apparatus_entry_mismatches']]
        if r['link_count_mismatches']:lines+=['','Logical link-count differences require repair. Each PDF rectangle retains a logical-link identifier; wrapped rectangles are grouped before counting.']+[f"- {m['uri']}: source {m['expected_logical_links']}, PDF logical links {m.get('pdf_logical_links','not yet tracked')}, rectangles {m['pdf_annotation_rectangles']}." for m in r['link_count_mismatches']]
        if r['ink_outside_type_area']:lines+=['','Text-area candidates:']+[f"- PDF page {v['pdf_page']}: {v.get('text',v.get('kind','ink'))}." for v in r['ink_outside_type_area']]
        lines+=['','Required rendered sample and repair pages: '+', '.join(map(str,r['required_visual_pages']))+'.','Inspected pages for this exact PDF: '+(', '.join(map(str,r['visually_inspected_pages'])) or 'none')+'.','Remaining required pages: '+(', '.join(map(str,r['uninspected_required_pages'])) or 'none')+'.','']
        observed=[v for v in visual if v['reader']==r['reader'] and v['pdf_sha256']==r['pdf_sha256'] and v['status']=='visually inspected']
        for v in observed:lines.append(f"- PDF page {v['pdf_page']}: {v['observation']}")
        lines.append('')
    lines+=['## Reproducible intermediates excluded from publication','', 'Raw runtime logs, font caches, downloaded support packages, temporary diagnostic PDFs and duplicate intermediate renderings are excluded. Sanitized build logs, exact source hashes, measured results, render indices and visual observations are retained. No source reading is taken from a diagnostic PDF.','']
    (root/'TYPESETTING_REPORT.md').write_text('\n'.join(lines))

def main():
    p=argparse.ArgumentParser();p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);p.add_argument('--render',action='store_true');p.add_argument('--names',nargs='*');a=p.parse_args();root=a.root.resolve();dependency_hashes=audit_dependency_snapshot(root);probe_check=current_probe_verification(root);checks=load_json(root/'PDF_CHECKS.json',{});history=[json.loads(l) for l in (root/'BUILD_HISTORY.jsonl').read_text().splitlines()] if (root/'BUILD_HISTORY.jsonl').exists() else [];visual=read_tsv(root/'VISUAL_QA.tsv');paths=sorted(p for d in ['FR','EN','GUIDE'] for p in (root/d).glob('*.tex') if p.with_suffix('.pdf').exists())
    if a.names:paths=[p for p in paths if p.stem in a.names]
    results=[]
    for tex in paths:
        r=audit_one(tex,root,checks,history,visual);results.append(r)
        if a.render:print(json.dumps(render_samples(tex,r,root.parent/'qa/final')),flush=True)
    dependency_after=audit_dependency_snapshot(root)
    changed=[name for name in dependency_hashes if dependency_hashes[name]!=dependency_after[name]]
    for r in results:r.update(audit_input_sha256=dependency_hashes,audit_inputs_unchanged_during_run=not changed,audit_inputs_changed_during_run=changed,rendering_probe_verification=probe_check)
    prior=load_json(root/'FINAL_PDF_AUDIT.json',{});prior.update({r['reader']:r for r in results});(root/'FINAL_PDF_AUDIT.json').write_text(json.dumps(prior,ensure_ascii=False,indent=2)+'\n');report(root,list(prior.values()),visual)
    for r in results:print(json.dumps({'reader':r['reader'],'source_pages':r['source_pages'],'expected_links':r['expected_link_count'],'actual_links':r['pdf_external_link_annotations'],'mismatched_targets':len(r['link_count_mismatches']),'required_visual_pages':len(r['required_visual_pages']),'uninspected':len(r['uninspected_required_pages'])}),flush=True)

if __name__=='__main__':main()
