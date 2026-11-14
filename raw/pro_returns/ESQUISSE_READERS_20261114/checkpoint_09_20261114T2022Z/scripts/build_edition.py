#!/usr/bin/env python3
"""Generate standalone LuaLaTeX readers from one annotated master per language."""
from __future__ import annotations
import argparse,csv,fcntl,hashlib,json,pathlib,re,sys
from collections import Counter
from edition_core import *

FRENCH_RIGHTS="Les droits sur l'œuvre originale appartiennent à son auteur, à ses représentants ou à ses ayants droit. Dans la mesure où nous détenons des droits sur la transcription, la traduction, les corrections et la composition produites par l'IA, nous les consacrons au domaine public sous CC0 1.0. Cette édition est publiée à des fins éducatives et non lucratives, et nous ne revendiquons aucun droit que nous ne détenons pas. Si vous détenez des droits sur cette œuvre et vous opposez à sa publication ici, veuillez ouvrir une issue GitHub et nous la retirerons."
PREFACES={
'FR_diplomatique':"Ce volume donne intégralement la copie 1 puis la copie 2. Chaque page porte son lien vers le fac-similé de la cote 119. Le bleu marque l’écriture manuscrite ; le texte biffé, les insertions, les surcharges et les notes marginales conservent leur distinction. Les mots soulignés restent soulignés. Les lectures incertaines restent signalées par des crochets et un point d’interrogation, avec un lien vers le scan. Les numéros de page du document et les marques d’archive sont conservés. Les notes (1) à (7) restent à la fin, avec des liens de retour.",
'FR_corrige_apparat':"Le texte suit la dactylographie de la copie 1, avec les corrections de l’auteur. Les suppressions, insertions et surcharges sont enregistrées dans l’apparat ; chaque correction éditoriale d’une coquille porte sa justification. L’apparat indique séparément les annotations de la copie 2. Une annotation propre à cette copie entre dans le texte seulement lorsqu’elle corrige une coquille commune, avec mention explicite. Les graphies et les usages récurrents de l’auteur sont maintenus. Les lectures encore incertaines restent marquées et reliées au scan. Les notes (1) à (7) conservent leur place finale.",
'FR_texte_de_lecture':"Ce texte de lecture est produit à partir du même texte corrigé que la forme avec apparat. Il omet les commentaires éditoriaux, les variantes et les marques de correction ; les notes de l’auteur et les lectures incertaines sont conservées. Les marques de scan et les numéros de page figurent uniquement dans la marge. Les notes (1) à (7) restent à la fin, avec des liens aller et retour. Les graphies et usages récurrents conservés sont recensés ci-dessous. @RETAINED_USAGE@",
'EN_corrected_translator_notes':"This English translation follows the corrected French text of copy 1. Authorial changes and justified corrections of isolated typing slips are recorded in the apparatus. Copy 2 annotations are identified separately. Translator’s notes explain words, wordplay, abbreviations and notation at the place where an explanation is needed. Unresolved readings remain marked and linked to their scans. The author’s notes (1)–(7) remain at the end, with links in both directions. The formulas retain the exact French source strings; terminology follows the supplied unified English glossary.",
'EN_reading':"This reading text is generated from the same English annotated master as the form with translator’s notes. The editorial apparatus, translator’s notes and correction markers are omitted. The author’s notes and unresolved readings remain. Scan marks and source page numbers appear only in the margin. The author’s notes (1)–(7) remain at the end with links in both directions. The formulas retain the exact French source strings."
}
FORMS={
'FR_diplomatique':('FR','ESQUISSE_FR_diplomatique','Texte diplomatique — les deux copies',True,False),
'FR_corrige_apparat':('FR','ESQUISSE_FR_corrige_apparat','Texte corrigé avec apparat',False,False),
'FR_texte_de_lecture':('FR','ESQUISSE_FR_texte_de_lecture','Texte de lecture',False,True),
'EN_corrected_translator_notes':('EN','ESQUISSE_EN_corrected_translator_notes','Corrected text with translator’s notes',False,False),
'EN_reading':('EN','ESQUISSE_EN_reading','Reading text',False,True)
}

def load_json(path,default):return json.loads(path.read_text()) if path.exists() else default

def read_tsv(path):
    if not path.exists():return []
    with path.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))

def write_tsv(path,rows,fields):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)

def tex_text(s):
    return s.replace('\\',r'\textbackslash{}').replace('&',r'\&').replace('%',r'\%').replace('_',r'\_').replace('#',r'\#')

def input_snapshot(root):
    patterns=['checked_pages/*.tex','translated_pages/*.tex','guide_fragments/*.tex','templates/*.tex']
    paths={p.relative_to(root).as_posix():p for pattern in patterns for p in root.glob(pattern)}
    for name in ['editorial_variants.json','copy2_annotations.json','RELEASE_STATUS.json','records/PAGE_MAP.tsv','scripts/build_edition.py','scripts/edition_core.py']:
        paths[name]=root/name
    return {name:hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None for name,p in sorted(paths.items())}

def check_master_forms(root,generated):
    reports={}
    def payload(path):
        text=path.read_text();pages=re.findall(r'% BEGIN PAGE \S+\n.*?\n% END PAGE \S+',text,re.S)
        declarations=[text[m.start:m.end] for m in macros(text,{'DeclareScan','DeclareVariant','DeclareNoteReturns'}) if m.arguments[0]!='#1']
        return '\n'.join(declarations+pages)
    for lang in ['FR','EN']:
        paths=[root/p for p in generated if p.startswith(lang+'/')];master=root/lang/('ESQUISSE_'+lang+'_master_annotated.tex');reference=payload(master)
        reports[lang]={'master':master.relative_to(root).as_posix(),'shared_body_and_declarations_sha256':sha256(reference),'forms':[]}
        for path in paths:
            match=payload(path)==reference
            reports[lang]['forms'].append({'source':path.relative_to(root).as_posix(),'same_body_and_declarations':match})
            if not match:raise ValueError('A generated form differs from its annotated master body: '+path.name)
    (root/'MASTER_FORM_EQUIVALENCE.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n')

def get_metadata(root):
    source=root.parent/'source/records/PAGES_ESQUISSE.tsv'
    derived=root/'records/PAGE_MAP.tsv'
    rows=read_tsv(source if source.exists() else derived)
    if not rows:raise FileNotFoundError('The supplied page coordinates or derived PAGE_MAP.tsv are required.')
    fields=['key','cote','site','pdf_page','ts_page','viewer']
    write_tsv(derived,rows,fields)
    return {r['key']:r for r in rows}

def annotate_all(root):
    ed=load_json(root/'editorial_variants.json',[]);metadata=get_metadata(root)
    decisions=read_tsv(root/'CHECK_DECISIONS.tsv');variants=[];cleanup=load_json(root/'MECHANICAL_CLEANUP.json',[])+load_json(root/'REVIEW_STAGE_CLEANUP.json',[]);coverage=[];annotated={}
    out=root/'annotated_pages';out.mkdir(exist_ok=True)
    for p in sorted((root/'checked_pages').glob('*.tex'),key=lambda p:(p.stem.startswith('esq119'),int(p.stem.rsplit('_',1)[-1]))):
        key=p.stem;s=p.read_text();clean,events=clean_latex(s)
        # This function never changes checked pages. A nonempty event list blocks final source equivalence until applied and logged.
        for event in events:cleanup.append({'key':key,**event,'source_id':'pending mechanical integration','status':'applied in generated body; checked page integration required'})
        if key.startswith('esq_'):
            marked,vs=annotate(clean,key,ed)
            for v in vs:
                candidates=[d for d in decisions if d['key']==key and d.get('image_reading')==v['page_reading']]
                if candidates and v['source_id']==v['id']:v['source_id']=','.join(d['source_item_id'] for d in candidates)
            variants.extend(vs)
        else:marked=clean;vs=[]
        (out/p.name).write_text(marked)
        annotated[key]=marked
        coverage.append({'key':key,'checked_sha256':sha256(s),'cleaned_sha256':sha256(clean),'annotated_sha256':sha256(marked),'diplomatic_recovery_equal':str(resolve_variants(marked,False)==clean).lower(),'variants':len(vs),'pending_cleanup':len(events)})
    # Delimiter repairs already integrated into scan-based reclassifications are recorded without repeating the reading change.
    for d in decisions:
        before=d.get('transcription_reading','');after=d.get('image_reading','')
        if d.get('source_item_id','').startswith('L-') and r'\hand{$' in before and before!=after:
            cleaned,ev=clean_nested_math(before)
            if ev:
                for event in ev:cleanup.append({'key':d['key'],'line':d['line'],'before':event['before'],'after':event['after'],'operation':'nested delimiter repair integrated with scan correction','reason':'Redundant nested dollar delimiters disappeared when the scan decision reclassified the enclosed character. The reading change itself is recorded separately in CHECK_DECISIONS.tsv.','source_id':d['source_item_id'],'status':'mechanical component integrated in the recorded scan correction'})
    (root/'VARIANTS.json').write_text(json.dumps(variants,ensure_ascii=False,indent=2)+'\n')
    write_tsv(root/'CLEANUP_LOG.tsv',cleanup,['key','line','before','after','operation','reason','source_id','status'])
    write_tsv(root/'SOURCE_COVERAGE.tsv',coverage,['key','checked_sha256','cleaned_sha256','annotated_sha256','diplomatic_recovery_equal','variants','pending_cleanup'])
    glyph_rows=[]
    for key,text in annotated.items():
        doubts=list(macros(text,{'unsure'},recursive=True))
        for glyph in macros(text,{'sourceglyph'},recursive=True):
            glyph_rows.append({'key':key,'glyph_id':glyph.arguments[0],'line':glyph.line,'uncertainty_marked':str(any(d.start<=glyph.start and glyph.end<=d.end for d in doubts)).lower(),'viewer':metadata[key]['viewer']})
    write_tsv(root/'records/SOURCE_GLYPH_USAGE.tsv',glyph_rows,['key','glyph_id','line','uncertainty_marked','viewer'])
    changes=[]
    for v in variants:
        m=metadata[v['key']]
        changes.append({'variant_id':v['id'],'cote':m['cote'],'site':m['site'],'place':v['line'],'page_reading':v['page_reading'],'corrected_reading':v['corrected_reading'],'kind':v['kind'],'reason':v['reason_fr'],'source_id':v['source_id']})
    write_tsv(root/'CHANGES.tsv',changes,['variant_id','cote','site','place','page_reading','corrected_reading','kind','reason','source_id'])
    return metadata,annotated,variants

NOTE_PATTERNS=[re.compile(r'\(\$(?:\{\})?\^\{?([1-7])\}?\$\)'),re.compile(r'\\hand\{\$\^\{\(([1-7])\)\}\$\}'),re.compile(r'\(\\textsuperscript\{([1-7])\}\)'),re.compile(r'\$\^\{\(([1-7])\)\}\$')]

def link_notes(pages,metadata):
    """Wrap the source's existing marks; the original mark remains intact."""
    matches={};calls={};defs={}
    for key,text in pages.items():
        site=int(metadata[key]['site']);copy='copy2' if site>=78 else 'copy1';ts=metadata[key]['ts_page']
        used=[]
        for pat in NOTE_PATTERNS:
            for m in pat.finditer(text):
                if any(a<=m.start()<b for a,b in used):continue
                used.append((m.start(),m.end()));n=m[1]
                if not ts:continue
                if int(ts)>=52:
                    ident=f'{copy}-{n}';defs[ident]=(key,m.group(),m.start());kind='definition';anchor=ident
                else:
                    ident=f'{copy}-{n}';anchor=f'call-{key}-{n}-{len(calls.get(ident,[]))+1}';kind='call';calls.setdefault(ident,[]).append((anchor,ts))
                matches.setdefault(key,[]).append((m.start(),m.end(),m.group(),kind,ident,anchor))
    new={}
    for key,text in pages.items():
        repl=[]
        for a,b,mark,kind,ident,anchor in matches.get(key,[]):
            replacement='\\notedef{'+ident+'}{'+mark+'}' if kind=='definition' else '\\notecall{'+ident+'}{'+anchor+'}{'+mark+'}'
            repl.append((a,b,replacement))
        new[key]=replace_ranges(text,repl)
    decl=[]
    for ident in defs:
        targets=calls.get(ident,[])
        links=[r'\hyperlink{'+a+'}{p.\\,'+p+'}' for a,p in targets]
        decl.append(r'\DeclareNoteReturns{'+ident+'}{'+', '.join(links)+'}')
    return new,'\n'.join(decl),{'calls':calls,'definitions':defs,'unresolved_calls':sorted(set(calls)-set(defs))}

def variant_declarations(variants,lang):
    lines=[]
    for v in variants:
        old=v['page_reading'];new=v['corrected_reading'];reason=v['reason_fr' if lang=='FR' else 'reason_en']
        if v.get('math'):old='$'+old+'$';new='$'+new+'$' if new else ''
        old=r'\AppReading{'+argument_text(old)+'}' if old else r'\EmptyReading{}'
        new=r'\AppReading{'+argument_text(new)+'}' if new else r'\EmptyReading{}'
        label=(KIND_LABEL_FR if lang=='FR' else KIND_LABEL_EN).get(v['kind'],v['kind'])
        if v.get('source_apparatus'):
            note=r'\textit{French source apparatus: '+label+'}. Page reading: '+old+'; corrected French: '+new+'. '+reason
        else:note=r'\textit{'+label+'}. '+old+r' \(\rightarrow\) '+new+'. '+reason
        lines.append(r'\DeclareVariant{'+v['id']+'}{'+note+'}')
    return '\n'.join(lines)

def attach_copy2(pages,annotations,lang,metadata):
    out=dict(pages)
    for a in annotations:
        if a.get('merged_into_variant'):continue
        key=a['key']
        if key not in out:continue
        text=a.get('text_fr' if lang=='FR' else 'text_en')
        if not text:raise ValueError(f"Missing {lang} apparatus text for {a['id']}")
        copy2_key=a.get('copy2_key')
        if not copy2_key:
            site=str(int(metadata[key]['site'])+76)
            copy2_key=next((k for k,m in metadata.items() if m['site']==site),None)
        if copy2_key not in metadata:raise ValueError('Missing copy2 source coordinates for '+a['id'])
        m2=metadata[copy2_key];url=m2['viewer'].replace('#',r'\#')
        label=('copie 2' if lang=='FR' else 'copy 2')+', scan '+m2['cote']+'/'+m2['site']
        linked=r'\scancontext{'+url+'}{'+r'\href{'+url+'}{['+label+']} '+text+'}'
        mark=r'\copytwo{'+a['id']+'}{'+linked+'}'
        anchor=a.get('anchor_fr' if lang=='FR' else 'anchor_en',a.get('anchor'))
        if anchor:
            pos=out[key].find(anchor)
            if pos<0:raise ValueError(f"Copy2 apparatus anchor absent for {a['id']}")
            pos+=len(anchor);out[key]=out[key][:pos]+mark+out[key][pos:]
        else:out[key]=out[key].rstrip()+'\n'+mark+'\n'
    return out

def make_document(root,form,metadata,pages,variants,notedecls,master=False,guide=False):
    lang,name,formtitle,dipl,reading=FORMS[form]
    template=(root/'templates/preamble.tex').read_text();front=(root/'templates/frontmatter.tex').read_text()
    french=lang=='FR';title="Esquisse d'un programme" if french else 'Sketch of a Program'
    retained_path=root/'templates/retained_usages_fr.tex'
    retained=retained_path.read_text() if retained_path.exists() else 'Le relevé des usages conservés accompagne les fichiers de travail.'
    pref=PREFACES[form].replace('@RETAINED_USAGE@',retained)
    release=load_json(root/'RELEASE_STATUS.json',{'final':False})
    included=len(pages) if dipl or not french else sum(k.startswith('esq_') for k in pages)
    required=116 if dipl else 58
    if guide:
        included=len([p for p in (root/'guide_fragments').glob('*.tex') if 'preface' not in p.stem.lower()])
        required=18
    coverage=''
    if not release.get('final'):
        if guide:coverage='\\noindent\\textbf{Working checkpoint.} This guide currently contains '+str(included)+' of the 18 requested commentary units. Its scope is recorded with the checked-page coverage.\\par\\smallskip'
        elif french:coverage='\\noindent\\textbf{Édition de travail partielle.} Ce fichier contient '+str(included)+' pages sources sur les '+str(required)+' prévues pour cette forme. La collation et les contrôles finaux se poursuivent.\\par\\smallskip'
        else:coverage='\\noindent\\textbf{Partial working edition.} This file contains '+str(included)+' of the '+str(required)+' source pages required for this form. Collation and final validation remain in progress.\\par\\smallskip'
    frontmap={'COVERAGE_STATUS':coverage,'PREFACE_TITLE':'Préface' if french else 'Preface','FORM_PREFACE':pref,'TRANSLATION_CREDIT':'' if french else 'AI-translated by GPT-6 Astra (OpenAI, ChatGPT Pro mode).','RIGHTS_TITLE':'Droits et crédits' if french else 'Rights and credits','FRENCH_RIGHTS':'\n'+FRENCH_RIGHTS if french else ''}
    for k,v in frontmap.items():front=front.replace('@'+k+'@',v)
    scan_decl=[]
    for key in pages:
        m=metadata[key];scan_decl.append(r'\DeclareScan{'+m['cote']+'/'+m['site']+'}{'+m['viewer'].replace('#',r'\#')+'}{'+key+'}{'+m['site']+'}')
    parts=[]
    c1=[k for k in pages if k.startswith('esq_')];c2=[k for k in pages if k.startswith('esq119_')]
    for copy,keys in [('copy1',c1),('copy2',c2)]:
        if not keys:continue
        if copy=='copy2':parts.append(r'\ifdiplomatic')
        if french:parts.append(r'\EditionPart{'+copy+'}{'+('Copie 1' if copy=='copy1' else 'Copie 2')+'}')
        for key in sorted(keys,key=lambda k:int(metadata[k]['site'])):
            pagebody,_=cluster_margins(body(pages[key]))
            parts.extend(['% BEGIN PAGE '+key,pagebody,r'\finishscan','% END PAGE '+key])
        if copy=='copy2':parts.append(r'\fi')
    mapping={'LINK_TRACKING':(root/'templates/link_tracking.tex').read_text(),'HAND_RENDERER':(root/'templates/hand_renderer.tex').read_text(), 'SOURCE_GLYPH_DEFINITIONS':'\n'.join((root/'templates'/name).read_text() for name in ['source_glyphs.tex','source_brackets.tex'] if (root/'templates'/name).exists()), 'LANGUAGES':'english,french' if french else 'french,english','FORM_SWITCHES':('\\diplomatictrue' if dipl else '\\diplomaticfalse')+'\n'+('\\readingtrue' if reading else '\\readingfalse')+'\n'+('\\englishfalse' if french else '\\englishtrue'),'EDITION_TITLE':title,'EDITION_FORM':formtitle+(' — annotated master' if master else ''),'PDF_TITLE':title+' — '+formtitle,'SCAN_DECLARATIONS':'\n'.join(scan_decl),'VARIANT_DECLARATIONS':variant_declarations(variants,lang),'NOTE_DECLARATIONS':notedecls,'FRONT_MATTER':front,'BODY':'\n'.join(parts)}
    for k,v in mapping.items():template=template.replace('@'+k+'@',v)
    status='final' if release.get('final') else 'partial'
    return '% EDITION STATUS: '+status+'; source units '+str(included)+'/'+str(required)+'\n'+template

def generate(root):
    metadata,annotated,frvars=annotate_all(root);c2=load_json(root/'copy2_annotations.json',[])
    c2printed=[a for a in c2 if not a.get('merged_into_variant')]
    for a in c2:
        if a.get('merged_into_variant') and not any(v['id']==a['merged_into_variant'] for v in frvars):raise ValueError('Merged copy2 annotation lacks its printed French variant: '+a['id'])
    frpages,frnotes,frnotestatus=link_notes(annotated,metadata);frpages=attach_copy2(frpages,c2,'FR',metadata)
    enpages={p.stem:p.read_text() for p in sorted((root/'translated_pages').glob('*.tex'))}
    envers=[];ensourcenotes=[];frbyid={v['id']:v for v in frvars}
    for key,text in list(enpages.items()):
        clean,_=clean_latex(text)
        # Explicit translated variants carry the same ids as the French master.
        for m in macros(clean,{'var'}):
            old,new,kind,vid=m.arguments
            if vid not in frbyid:raise ValueError('English variant has no French source: '+vid)
            v=dict(frbyid[vid]);v.update(page_reading=old,corrected_reading=new,kind=kind);envers.append(v)
        for m in macros(clean,{'frapparatus'}):
            vid=m.arguments[0]
            if vid not in frbyid:raise ValueError('English source-apparatus marker has no French source: '+vid)
            v=dict(frbyid[vid]);v['source_apparatus']=True;ensourcenotes.append(v)
        enpages[key]=clean
    enpages,ennotes,ennotestatus=link_notes(enpages,metadata);enpages=attach_copy2(enpages,c2,'EN',metadata)
    layouts=[]
    for lang,language_pages in [('FR',frpages),('EN',enpages)]:
        for key,text in language_pages.items():
            original=body(text);transformed,events=cluster_margins(original)
            for event in events:layouts.append({'language':lang,'key':key,**event,'source_body_sha256':sha256(original),'generated_body_sha256':sha256(transformed),'source_recovery_equal':True})
    (root/'records/TYPESETTING_LAYOUTS.json').write_text(json.dumps(layouts,ensure_ascii=False,indent=2)+'\n')
    coverage=[]
    for key,text in enpages.items():
        fr=resolve_variants(annotated.get(key,''),True);en=resolve_variants(text,True)
        for name in ['tnote','copytwo']:
            en=replace_ranges(en,[(m.start,m.end,'') for m in macros(en,{name})])
        # Links wrap existing marks without changing the source mathematics.
        for name,arg in [('notecall',2),('notedef',1)]:en=replace_ranges(en,[(m.start,m.end,m.arguments[arg]) for m in macros(en,{name})])
        fmath=math_payloads(fr);emath=math_payloads(en)
        coverage.append({'key':key,'french_math_count':len(fmath),'english_math_count':len(emath),'math_equal':str(fmath==emath).lower(),'french_sha256':sha256(fr),'english_sha256':sha256(en),'translator_notes':len(list(macros(text,{'tnote'})))})
    write_tsv(root/'TRANSLATION_COVERAGE.tsv',coverage,['key','french_math_count','english_math_count','math_equal','french_sha256','english_sha256','translator_notes'])
    (root/'NOTE_LINKS.json').write_text(json.dumps({'FR':frnotestatus,'EN':ennotestatus},ensure_ascii=False,indent=2)+'\n')
    generated=[]
    for form,(lang,name,_,_,_) in FORMS.items():
        pages,vs,notes=(frpages,frvars,frnotes) if lang=='FR' else (enpages,envers+ensourcenotes,ennotes)
        d=root/lang;d.mkdir(exist_ok=True);path=d/(name+'.tex');path.write_text(make_document(root,form,metadata,pages,vs,notes));generated.append(path.relative_to(root).as_posix())
    for lang,form in [('FR','FR_corrige_apparat'),('EN','EN_corrected_translator_notes')]:
        pages,vs,notes=(frpages,frvars,frnotes) if lang=='FR' else (enpages,envers+ensourcenotes,ennotes)
        path=root/lang/('ESQUISSE_'+lang+'_master_annotated.tex');path.write_text(make_document(root,form,metadata,pages,vs,notes,True));generated.append(path.relative_to(root).as_posix())
    # The guide uses the same credits and rights; content is owned by the guide author.
    guidefragments=sorted((root/'guide_fragments').glob('*.tex'))
    if guidefragments:
        guidebody='\n\n'.join(p.read_text() for p in guidefragments)
        document=make_document(root,'EN_corrected_translator_notes',metadata,{},[], '',guide=True)
        start=document.index('\\begin{document}');after=document.index('\\typeout{EDITION-APPARATUS-COUNT:')
        document=document[:after]+guidebody+'\n'+document[after:]
        document=document.replace(r'\newcommand{\EditionTitle}{Sketch of a Program}',r'\newcommand{\EditionTitle}{A Guide to the Esquisse}')
        document=document.replace(r'\newcommand{\EditionForm}{Corrected text with translator’s notes}',r'\newcommand{\EditionForm}{Commentary for a mathematical reader}')
        document=document.replace(PREFACES['EN_corrected_translator_notes'],'This guide follows the sommaire, sections 1–10 and notes (1)–(7) in the order of the typescript. Page references give the original typescript pagination and link to the archive. The guide is based on the checked text and collation; it does not change the text’s mathematics.')
        document=document.replace('AI-translated by GPT-6 Astra (OpenAI, ChatGPT Pro mode).','')
        (root/'GUIDE').mkdir(exist_ok=True);p=root/'GUIDE/ESQUISSE_GUIDE.tex';p.write_text(document);generated.append(p.relative_to(root).as_posix())
    check_master_forms(root,generated)
    (root/'BUILD_INPUTS.json').write_text(json.dumps({'status':'final' if load_json(root/'RELEASE_STATUS.json',{'final':False}).get('final') else 'partial','generated':generated,'checked_pages':len(annotated),'translated_pages':len(enpages),'french_variants':len(frvars),'english_variants':len(envers),'english_source_apparatus_notes':len(ensourcenotes),'copy2_annotations':len(c2printed),'copy2_annotation_records':len(c2),'copy2_annotations_merged_into_variants':len(c2)-len(c2printed),'input_sha256':input_snapshot(root)},indent=2)+'\n')
    kinds=Counter(v['kind'] for v in frvars);enkinds=Counter(v['kind'] for v in envers);notes=sum(int(r['translator_notes']) for r in coverage)
    counts=['# Apparatus counts','', '| Cote | Form | Kind | Count |','|---|---|---|---:|']
    for form,(_,_,_,dipl,reading) in FORMS.items():
        if dipl or reading:counts.append(f'| 119 | {form} | apparatus entries | 0 |');continue
        for kind,n in (kinds if form.startswith('FR') else enkinds).items():counts.append(f'| 119 | {form} | {kind} | {n} |')
        for kind,n in Counter(a['kind'] for a in c2printed).items():counts.append(f'| 119 | {form} | copy 2: {kind} | {n} |')
        if form.startswith('EN'):
            for kind,n in Counter(v['kind'] for v in ensourcenotes).items():counts.append(f'| 119 | {form} | French source apparatus: {kind} | {n} |')
            counts.append(f'| 119 | {form} | translator note | {notes} |')
    counts+=['','Counts are derived from the annotated masters. Unchanged handwriting receives no variant solely because it is handwritten.',f"Copy 2 annotation records: {len(c2)}; separately printed: {len(c2printed)}; merged into an explicitly identified correction variant: {len(c2)-len(c2printed)}. Merged records are retained but are not printed twice."]
    (root/'APPARATUS_COUNTS.md').write_text('\n'.join(counts)+'\n')
    return generated

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('command',choices=['annotate','generate']);p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);a=p.parse_args()
    with (a.root/'.audit-records.lock').open('a') as lock:
        fcntl.flock(lock.fileno(),fcntl.LOCK_EX)
        if a.command=='annotate':m,pg,v=annotate_all(a.root);print(json.dumps({'checked_pages':len(pg),'variants':len(v)}))
        else:print(json.dumps({'generated':generate(a.root)},indent=2))
