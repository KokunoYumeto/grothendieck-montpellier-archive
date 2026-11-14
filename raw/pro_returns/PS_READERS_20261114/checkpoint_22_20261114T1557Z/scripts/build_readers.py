"""Build mode-switched standalone readers from the reviewed page files.

The default is a clearly labelled partial working edition until all 706 sources
exist. No missing source page is silently filled from the unchecked drafts.
"""
from pathlib import Path
from dataclasses import dataclass
import argparse, csv, hashlib, json, re

PROJECT=Path(__file__).resolve().parents[1]
WORKSPACE=PROJECT.parent
INPUT=WORKSPACE/'inputs/text'
MACROS={'hand':1,'over':2,'inserted':1,'margin':1,'deleted':1,'xout':1,'uline':1,'uuline':1,'underline':1,'unsure':1,'illegible':1,'diagram':1,'mspage':1,'scanpage':1}
EDIT={'over','inserted','margin','deleted','xout'}
MATHENV={'tikzcd','array','aligned','cases','equation','equation*','align','align*','gather','gather*'}
TEXTARG={'text','textrm','textsf','texttt','textnormal','mbox','hbox'}

def group(s,i,opening='{',closing='}'):
    if i>=len(s) or s[i]!=opening: raise ValueError(('argument expected',i,s[max(0,i-30):i+60]))
    j=i+1;depth=1
    while j<len(s):
        if s[j]=='%':
            e=s.find('\n',j);j=len(s) if e<0 else e+1;continue
        if s[j]=='\\':j+=2;continue
        if s[j]==opening:depth+=1
        elif s[j]==closing:
            depth-=1
            if not depth:return s[i+1:j],j+1
        j+=1
    raise ValueError(('unclosed group',i,s[max(0,i-20):i+70]))

def command(s,i):
    m=re.match(r'\\([A-Za-z]+|.)',s[i:],re.S)
    return (m[1],i+len(m[0])) if m else ('',i+1)

def skipspace(s,i):
    while i<len(s) and s[i].isspace():i+=1
    return i

def read_call(s,i,name,end):
    j=skipspace(s,end);opt=''
    if name in {'inserted','over'} and j<len(s) and s[j]=='[':
        opt,j=group(s,j,'[',']');j=skipspace(s,j)
    args=[];starts=[]
    for _ in range(MACROS[name]):
        starts.append(j+1);a,j=group(s,j);args.append(a);j=skipspace(s,j) if len(args)<MACROS[name] else j
    return opt,args,starts,j

def normalize(s,key,fixes,base=0,in_math=False,math_fixed=False,whole=None):
    """Remove nested math delimiters only when a surrounding math group supplies them."""
    whole=s if whole is None else whole
    out=[];i=0;math=in_math;fixed=math_fixed;delimiter=None;stack=[]
    def fix(pos,what,action):
        fixes.append({'reader':'all','page_key':key,'source_line':whole.count('\n',0,base+pos)+1,'what_was_wrong':what,'what_was_done':action})
    while i<len(s):
        ch=s[i]
        if ch=='%':
            e=s.find('\n',i);e=len(s) if e<0 else e+1;out.append(s[i:e]);i=e;continue
        if ch=='$':
            if math and fixed:
                d='$$' if s.startswith('$$',i) else '$'
                fix(i,'Dollar delimiter nested inside an existing math argument','Removed redundant nested delimiter; mathematical content is unchanged.')
            elif math:
                d='$$' if delimiter=='$$' and s.startswith('$$',i) else '$'
                out.append(d);math=False;delimiter=None
            else:
                d='$$' if s.startswith('$$',i) else '$'
                out.append(d);math=True;delimiter=d
            i+=len(d);continue
        if ch=='\\':
            name,j=command(s,i)
            if name in {'[','('}:out.append(s[i:j]);stack.append((math,fixed,delimiter));math=True;fixed=True;delimiter=None;i=j;continue
            if name in {']',')'}:out.append(s[i:j]);math,fixed,delimiter=stack.pop() if stack else (False,False,None);i=j;continue
            if name in {'begin','end'}:
                p=skipspace(s,j)
                if p<len(s) and s[p]=='{':
                    env,q=group(s,p);out.append(s[i:q]);i=q
                    if env in MATHENV:
                        if name=='begin':stack.append((math,fixed,delimiter));math=True;fixed=True;delimiter=None
                        else:math,fixed,delimiter=stack.pop() if stack else (False,False,None)
                    continue
            if name in TEXTARG:
                p=skipspace(s,j)
                if p<len(s) and s[p]=='{':
                    a,q=group(s,p);out.append(s[i:p+1]+normalize(a,key,fixes,base+p+1,False,False,whole)+'}');i=q;continue
            out.append(s[i:j]);i=j;continue
        if ch=='{':
            a,j=group(s,i);out.append('{'+normalize(a,key,fixes,base+i+1,math,math,whole)+'}');i=j;continue
        out.append(ch);i+=1
    return ''.join(out)

def repair_diagram_separators(s,key,fixes):
    def repair(m):
        old=m[0];new=re.sub(r'(?<!\\)&',r'\\&',old)
        if new!=old:
            fixes.append({'reader':'all','page_key':key,'source_line':s.count('\n',0,m.start())+1,'what_was_wrong':'TikZ matrix alignment characters were tokenized inside a macro argument.','what_was_done':'Use the explicit \\& cell separator and the matching TikZ ampersand replacement setting; objects and arrows are unchanged.'})
        return new
    return re.sub(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',repair,s,flags=re.S)

def repair_macro_layout(s,key,fixes):
    out=[];cursor=0
    pattern=re.compile(r'\\(diagram|xout)\s*\{')
    while True:
        m=pattern.search(s,cursor)
        if not m:out.append(s[cursor:]);break
        a,end=group(s,m.end()-1);changed=a
        if m[1]=='diagram':
            def tag(mm):
                return r'\quad\textnormal{('+mm[1]+')}'
            changed=re.sub(r'\\tag\{([^{}]+)\}',tag,a)
            action='Set the existing parenthesized label beside its diagram as explicit text; amsmath tag requires an equation environment.'
        elif len(a)>24 and 'x' in a:
            chars=[];i=0
            while i<len(a):
                if a[i]=='\\':
                    _,j=command(a,i);chars.append(a[i:j]);i=j;continue
                chars.append(a[i])
                if a[i]=='x' and (a.count('x')>=5 or (i>0 and a[i-1]=='x') or (i+1<len(a) and a[i+1]=='x')):chars.append(r'\allowbreak{}')
                i+=1
            changed=''.join(chars)
            action='Permit zero-width line breaks after visible x-overstrike characters in the long cancelled run; no printed character is removed or added.'
        else:action=''
        out.append(s[cursor:m.end()]+changed+'}')
        if changed!=a:
            fixes.append({'reader':'all','page_key':key,'source_line':s.count('\n',0,m.start())+1,'what_was_wrong':'Diagram label outside an equation.' if m[1]=='diagram' else 'Unbreakable long run of visible typewriter cancellation characters.','what_was_done':action})
        cursor=end
    return ''.join(out)

def preserve_front_lineation(s,key,fixes):
    if not key.startswith('ps_134-2_') or int(key.rsplit('_',1)[1])>13:return s
    out=[];depth=0;math=False;env=0
    for lineno,line in enumerate(s.splitlines(True),1):
        visible=re.split(r'(?<!\\)%',line,1)[0]
        i=0
        while i<len(visible):
            if visible[i]=='\\':
                name,j=command(visible,i)
                if name in {'[','('}:math=True
                elif name in {']',')'}:math=False
                elif name in {'begin','end'}:
                    mm=re.match(r'\{(tikzcd|tikzpicture|array|tabular)\}',visible[j:])
                    if mm:env+=1 if name=='begin' else -1
                i=j;continue
            if visible[i]=='{':depth+=1
            elif visible[i]=='}':depth-=1
            elif visible[i]=='$':math=not math
            i+=1
        if visible.strip() and depth==0 and not math and env==0 and not visible.lstrip().startswith((r'\scanpage',r'\mspage',r'\end{')):
            end=len(visible.rstrip('\r\n'))
            line=line[:end]+r'\par'+line[end:]
            fixes.append({'reader':'all','page_key':key,'source_line':lineno,'what_was_wrong':'Separate contents/dedication lines flowed into one paragraph.','what_was_done':'Retained the source line boundary as a paragraph boundary, without changing words or symbols.'})
        out.append(line)
    return ''.join(out)

def local_layout_repairs(s,key,fixes):
    p=PROJECT/'records/TYPESETTING_PATCHES.json'
    for r in json.loads(p.read_text()) if p.exists() else []:
        if r['key']!=key:continue
        before,after=r['before'],r['after']
        if s.count(before)==1:
            line=s.count('\n',0,s.index(before))+1;s=s.replace(before,after,1)
        elif s.count(after)==1:
            line=s.count('\n',0,s.index(after))+1
        else:raise ValueError(('local layout patch not unique',key,r['id'],s.count(before),s.count(after)))
        fixes.append({'reader':'all','page_key':key,'source_line':line,'what_was_wrong':r['problem'],'what_was_done':r['action']+' ['+r['id']+']'})
    return s

def explicit_transform(s,key,variants,overrides):
    ranges=[]
    for o in overrides:
        before=repair_diagram_separators(normalize(o['before'],key,[]),key,[])
        after=repair_diagram_separators(normalize(o['after'],key,[]),key,[])
        if s.count(before)!=1:raise ValueError(('explicit variant must locate uniquely',key,o['source_id'],s.count(before)))
        pos=s.index(before);ranges.append((pos,pos+len(before),before,after,o))
    ranges.sort();out=[];cursor=0
    for start,end,before,after,o in ranges:
        if start<cursor:raise ValueError(('overlapping explicit variants',key))
        out.append(transform(s[cursor:start],key,variants,base=cursor,whole=s))
        corrected=transform(after,key,[],'corrected')
        v=Variant(key,len(variants)+1,s.count('\n',0,start)+1,before,corrected,o['kind'],o['reason'],o['source_id'],o.get('in_math',False))
        variants.append(v);out.append(r'\var{'+before+'}{'+corrected+'}{'+v.kind+'}{'+v.id+'}')
        cursor=end
    out.append(transform(s[cursor:],key,variants,base=cursor,whole=s))
    return ''.join(out)

@dataclass
class Variant:
    key:str
    number:int
    line:int
    before:str
    after:str
    kind:str
    reason:str
    source_id:str
    in_math:bool
    @property
    def id(self):return f'{self.key}-v{self.number:04d}'

def reason_for(name,opt):
    return {
      'deleted':('deletion','The author cancels this material by hand; it leaves the corrected running text.'),
      'xout':('typewriter deletion','The typewriter strikes out this material; it leaves the corrected running text.'),
      'over':('typewriter overwriting' if opt=='typed' else 'writing over','The superposed '+('typed' if opt=='typed' else 'handwritten')+' reading replaces the underlying reading.'),
      'inserted':('typed insertion' if opt=='typed' else 'insertion','The '+('typed' if opt=='typed' else 'handwritten')+' insertion is incorporated at its indicated position; insertion brackets leave the running text.'),
      'margin':('marginal note revised','The author\'s internal cancellations and replacements in this marginal note are applied at its source-line call.')
    }[name]

def transform(s,key,variants,mode='annotate',base=0,in_math=False,whole=None):
    """Maximal editorial operations are single variants; nested layers remain in their readings."""
    whole=s if whole is None else whole
    out=[];i=0;math=in_math;delimiter=None;stack=[]
    while i<len(s):
        if s[i]=='%':
            e=s.find('\n',i);e=len(s) if e<0 else e+1;out.append(s[i:e]);i=e;continue
        if s[i]=='$':
            if math:
                d='$$' if delimiter=='$$' and s.startswith('$$',i) else '$';math=False;delimiter=None
            else:
                d='$$' if s.startswith('$$',i) else '$';math=True;delimiter=d
            out.append(d);i+=len(d);continue
        if s[i]=='\\':
            name,j=command(s,i)
            if name in {'[','('}:stack.append((math,delimiter));math=True;delimiter=None;out.append(s[i:j]);i=j;continue
            if name in {']',')'}:math,delimiter=stack.pop() if stack else (False,None);out.append(s[i:j]);i=j;continue
            if name in {'begin','end'}:
                p=skipspace(s,j)
                if p<len(s) and s[p]=='{':
                    env,q=group(s,p);out.append(s[i:q]);i=q
                    if env in MATHENV:
                        if name=='begin':stack.append((math,delimiter));math=True;delimiter=None
                        else:math,delimiter=stack.pop() if stack else (False,None)
                    continue
            if name in TEXTARG:
                p=skipspace(s,j)
                if p<len(s) and s[p]=='{':
                    a,q=group(s,p);out.append(s[i:p+1]+transform(a,key,variants,mode,base+p+1,False,whole)+'}');i=q;continue
            if name in MACROS:
                opt,args,starts,q=read_call(s,i,name,j)
                if name in EDIT:
                    original=s[i:q]
                    rendered=[transform(a,key,[], 'corrected',base+p,math,whole) for a,p in zip(args,starts)]
                    if name in {'deleted','xout'}:corrected=''
                    elif name=='over':corrected=rendered[1] if opt=='typed' else r'\hand{'+rendered[1]+'}'
                    elif name=='inserted':corrected=rendered[0] if opt=='typed' else r'\hand{'+rendered[0]+'}'
                    else:corrected=r'\margin{'+rendered[0]+'}'
                    if original==corrected:out.append(original)
                    elif mode=='corrected':out.append(corrected)
                    elif mode=='diplomatic':out.append(original)
                    else:
                        kind,reason=reason_for(name,opt)
                        v=Variant(key,len(variants)+1,whole.count('\n',0,base+i)+1,original,corrected,kind,reason,f'PAGE:{key}:L{whole.count(chr(10),0,base+i)+1}',math)
                        variants.append(v)
                        out.append(r'\var{'+original+'}{'+corrected+'}{'+kind+'}{'+v.id+'}')
                    i=q;continue
                prefix='\\'+name+('['+opt+']' if opt else '')
                out.append(prefix+''.join('{'+transform(a,key,variants,mode,base+p,math,whole)+'}' for a,p in zip(args,starts)))
                i=q;continue
            out.append(s[i:j]);i=j;continue
        if s[i]=='{':
            a,j=group(s,i);out.append('{'+transform(a,key,variants,mode,base+i+1,math,whole)+'}');i=j;continue
        out.append(s[i]);i+=1
    return ''.join(out)

def texescape(s):
    return ''.join({'&':r'\&','%':r'\%','_':r'\_','#':r'\#','{':r'\{','}':r'\}','\\':r'\textbackslash{}'}.get(c,c) for c in str(s))

def link_marks(s):
    s=re.sub(r'(?m)(?<!\\)%.*$','',s)
    return {name:len(re.findall(r'\\'+name+r'\s*\{',s)) for name in ['scanpage','unsure','illegible']}

def tsv(path,fields,rows):
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)

def select_variant(s,mode):
    out=[];i=0
    while i<len(s):
        if s.startswith(r'\var{',i):
            j=i+4;args=[]
            for _ in range(4):a,j=group(s,j);args.append(a)
            out.append(select_variant(args[mode],mode));i=j
        else:out.append(s[i]);i+=1
    return ''.join(out)

def build(args):
    meta=json.loads((INPUT/'records/PAGES_PS.json').read_text())
    meta=sorted(meta,key=lambda x:(x['text']=='brown',int(x['cote'].split('-')[1]),int(x['site'])))
    meta=[m for m in meta if (PROJECT/'checked_pages'/(m['key']+'.tex')).exists() and (not args.cote or m['cote']==args.cote)]
    if args.limit:meta=meta[:args.limit]
    outdir=PROJECT/('qa/build/'+args.cote if args.cote else 'readers');outdir.mkdir(parents=True,exist_ok=True)
    partial=len(meta)!=706
    preamble=(PROJECT/'scripts/reader_preamble.tex').read_text()
    overrides=[]
    for p in (PROJECT/'records').glob('MASTER_VARIANTS_*.json'):overrides.extend(json.loads(p.read_text()))
    chunks=[];allvars=[];fixes=[];manifest=[]
    for m in meta:
        key=m['key'];raw=(PROJECT/'checked_pages'/(key+'.tex')).read_text()
        normalized=local_layout_repairs(preserve_front_lineation(repair_macro_layout(repair_diagram_separators(normalize(raw,key,fixes),key,fixes),key,fixes),key,fixes),key,fixes)
        vv=[];annotated=explicit_transform(normalized,key,vv,[o for o in overrides if o['key']==key])
        reconstructed=select_variant(annotated,0)
        if reconstructed!=normalized:raise AssertionError(('diplomatic reconstruction differs',key))
        url=f"https://grothendieck.umontpellier.fr/web/viewer.html?file=../{m['cote']}.pdf\\#page={m['pdf_page']}"
        chunks.append('\\pssource{'+key+'}{'+m['cote']+'/'+str(m['site'])+'}{'+url+'}\n')
        chunks.extend('\\psnumber{'+v.id+'}{'+str(v.number)+'}\n' for v in vv)
        chunks.append('%% BEGIN SOURCE '+key+'\n'+annotated+'\n%% END SOURCE '+key+'\n')
        if vv:
            chunks.append('\\ifnum\\EditionMode=1\n\\psapparatusstart\n')
            for v in vv:
                before=('$'+v.before+'$') if v.in_math else v.before
                after=('$'+v.after+'$') if v.in_math and v.after else v.after
                chunks.append(r'\psentry{'+v.id+'}{'+str(v.number)+'}{'+texescape(v.kind)+'}{'+before+'}{'+after+'}{'+texescape(v.reason)+'}\n')
            chunks.append('\\psapparatusend\n\\fi\n')
        allvars.extend(vv)
        diplomatic_marks=link_marks(normalized);corrected_marks=link_marks(select_variant(annotated,1));apparatus_marks=link_marks(''.join(v.before+v.after for v in vv))
        manifest.append({'key':key,'cote':m['cote'],'site':m['site'],'pdf_page':m['pdf_page'],'raw_sha256':hashlib.sha256(raw.encode()).hexdigest(),'normalized_sha256':hashlib.sha256(normalized.encode()).hexdigest(),'variants':len(vv),'diplomatic_reconstruction_equal':True,'expected_link_marks':{'diplomatic':diplomatic_marks,'reading':corrected_marks,'corrected_apparatus':{n:corrected_marks[n]+apparatus_marks[n] for n in corrected_marks}}})
    body=''.join(chunks)
    forms={'PS_EN_diplomatic':0,'PS_EN_corrected_apparatus':1,'PS_EN_reading':2,'PS_EN_master_annotated':1}
    for name,mode in forms.items():
        label={'PS_EN_diplomatic':'Diplomatic reader','PS_EN_corrected_apparatus':'Corrected reader with apparatus','PS_EN_reading':'Reading text','PS_EN_master_annotated':'Annotated master'}[name]
        top='% Generated by scripts/build_readers.py; change the reviewed sources and rebuild.\n'+f'\\def\\EditionMode{{{mode}}}\n'+f'\\def\\EditionLabel{{{label}}}\n'+f'\\def\\EditionStatus{{'+(f'WORKING EDITION: {len(meta)} of 706 source pages reviewed and included' if partial else 'Complete checked edition')+'}\n'
        (outdir/(name+'.tex')).write_text(top+preamble+'\n\\begin{document}\n\\psfrontmatter\n'+body+'\n\\end{document}\n')
    records=outdir if args.cote else PROJECT/'records'
    (records/'BUILD_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
    changes=[]
    for v in allvars:
        mm=next(m for m in meta if m['key']==v.key)
        changes.append({'cote':mm['cote'],'site':mm['site'],'place':f'{v.key}:L{v.line}','typescript_reading':v.before,'corrected_reading':v.after,'kind':v.kind,'reason':v.reason,'source_id':v.id,'evidence_id':v.source_id})
    tsv(records/'CHANGES_EN.tsv',['cote','site','place','typescript_reading','corrected_reading','kind','reason','source_id','evidence_id'],changes)
    tsv(records/'TYPESETTING_FIXES_GENERATED.tsv',['reader','page_key','source_line','what_was_wrong','what_was_done'],fixes)
    print(json.dumps({'pages':len(meta),'variants':len(allvars),'mechanical_fixes':len(fixes),'complete':not partial,'destination':str(outdir.relative_to(PROJECT))}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--cote');p.add_argument('--limit',type=int);build(p.parse_args())
