#!/usr/bin/env python3
"""Structural utilities for the Esquisse edition. No lexical normalization."""
from __future__ import annotations
import dataclasses, hashlib, json, pathlib, re

@dataclasses.dataclass
class Macro:
    name: str
    start: int
    end: int
    arguments: list[str]
    optional: str | None = None
    line: int = 0

ARITIES={'DeclareVariant':2,'DeclareScan':4,'DeclareNoteReturns':2,'frapparatus':1,'scancontext':2,'href':2,'hyperlink':2,'sourceglyph':1,'scanpage':1,'mspage':1,'hand':1,'handcircle':1,'over':2,'inserted':1,'margin':1,'deleted':1,'xout':1,'uline':1,'uuline':1,'unsure':1,'illegible':1,'diagram':1,'var':4,'tnote':2,'copytwo':2,'authornote':1,'notecall':3,'notedef':2}
ARITIES['margincluster']=1
ARITIES['authorstar']=2

STAR_PATTERN=re.compile(r'\(\s*(\*\s*(?:\*\s*)?)\)')

def anchor_author_stars(text,key):
    """Wrap source star marks in invisible PDF destinations; retain literal ink."""
    protected=[(m.start,m.end) for m in macros(text,{'tnote','copytwo'},recursive=True)]
    offset=0
    for line in text.splitlines(keepends=True):
        cut=next((i for i,c in enumerate(line) if c=='%' and not escaped(line,i)),None)
        if cut is not None:protected.append((offset+cut,offset+len(line)))
        offset+=len(line)
    replacements=[];events=[]
    for match in STAR_PATTERN.finditer(text):
        if any(a<=match.start()<b for a,b in protected):continue
        ident=f'{key}-star-{len(events)+1}'
        value=r'\authorstar{'+ident+'}{'+match.group()+'}'
        replacements.append((match.start(),match.end(),value))
        events.append({'id':ident,'literal_mark':match.group(),'before':match.group(),'after':value,'operation':'invisible named destination for the source star mark'})
    result=replace_ranges(text,replacements)
    recovered=replace_ranges(result,[(m.start,m.end,m.arguments[1]) for m in macros(result,{'authorstar'},recursive=True)])
    if recovered!=text:raise ValueError('Star-anchor wrapping changed the source body: '+key)
    return result,events

def escaped(s: str,i: int)->bool:
    n=0;i-=1
    while i>=0 and s[i]=='\\':n+=1;i-=1
    return n%2==1

def group(s: str,i: int,opening='{',closing='}'):
    while i<len(s) and s[i].isspace():i+=1
    if i>=len(s) or s[i]!=opening: raise ValueError(f'Expected {opening} at character {i}')
    begin=i;i+=1;depth=1
    while i<len(s):
        c=s[i]
        if c=='%' and not escaped(s,i):
            e=s.find('\n',i);i=len(s) if e<0 else e+1;continue
        if not escaped(s,i):
            if c==opening:depth+=1
            elif c==closing:
                depth-=1
                if not depth:return s[begin+1:i],i+1
        i+=1
    raise ValueError(f'Unclosed {opening} at character {begin}')

def macros(s: str,names=None,recursive=False):
    names=set(ARITIES if names is None else names);i=0
    while i<len(s):
        if s[i]=='%' and not escaped(s,i):
            e=s.find('\n',i);i=len(s) if e<0 else e+1;continue
        if s[i]=='\\' and not escaped(s,i):
            m=re.match(r'\\([A-Za-z]+)',s[i:])
            if m and m[1] in names:
                name=m[1];j=i+len(m[0]);opt=None
                if name=='inserted':
                    k=j
                    while k<len(s) and s[k].isspace():k+=1
                    if k<len(s) and s[k]=='[': opt,j=group(s,k,'[',']')
                args=[]
                try:
                    for _ in range(ARITIES[name]):arg,j=group(s,j);args.append(arg)
                except ValueError:
                    i+=len(m[0]);continue
                yield Macro(name,i,j,args,opt,s.count('\n',0,i)+1)
                if recursive:
                    for child in macros(s[i+len(m[0]):j],names,recursive=True):
                        child.start+=i+len(m[0]);child.end+=i+len(m[0]);child.line=s.count('\n',0,child.start)+1;yield child
                i=j;continue
        i+=1

def replace_ranges(text,replacements):
    for a,b,value in sorted(replacements,reverse=True):text=text[:a]+value+text[b:]
    return text

def strip_comments(s):
    out=[]
    for line in s.splitlines(keepends=True):
        cut=next((i for i,c in enumerate(line) if c=='%' and not escaped(line,i)),None)
        if cut is None:out.append(line)
        else:out.append(line[:cut])
    return ''.join(out)

def ends_in_comment(s):
    line=s.rsplit('\n',1)[-1]
    return any(c=='%' and not escaped(line,i) for i,c in enumerate(line))

def argument_text(s):
    """Terminate a final TeX comment before appending a generated closing brace."""
    return s+'\n' if ends_in_comment(s) else s

def cluster_margins(s):
    """Stack adjacent marginal notes without changing their contents or source."""
    marks=list(macros(s,{'margin'}));groups=[];run=[]
    for mark in marks:
        if run and strip_comments(s[run[-1].end:mark.start]).strip():
            if len(run)>1:groups.append(run)
            run=[]
        run.append(mark)
    if len(run)>1:groups.append(run)
    replacements=[];events=[]
    for run in groups:
        original=s[run[0].start:run[-1].end];wrapped=r'\margincluster{'+original+'}'
        replacements.append((run[0].start,run[-1].end,wrapped))
        events.append({'first_line':run[0].line,'notes':len(run),'original':original,'generated':wrapped})
    transformed=replace_ranges(s,replacements)
    recovered=replace_ranges(transformed,[(m.start,m.end,m.arguments[0]) for m in macros(transformed,{'margincluster'})])
    if recovered!=s:raise ValueError('Margin clustering changed source content')
    return transformed,events

def body(s):
    return '\n'.join(l for l in s.splitlines() if not l.lstrip().startswith('%')).strip()+'\n'

def sha256(s): return hashlib.sha256(s.encode()).hexdigest()

def math_spans(s):
    """Return exact delimited math spans, without changing any characters."""
    out=[];i=0;start=None;closer=None
    while i<len(s):
        if s[i]=='%' and not escaped(s,i):
            e=s.find('\n',i);i=len(s) if e<0 else e+1;continue
        if start is None:
            if s[i]=='$' and not escaped(s,i):
                delim='$$' if s.startswith('$$',i) else '$';start=i;closer=delim;i+=len(delim);continue
            if s.startswith('\\[',i) or s.startswith('\\(',i):start=i;closer='\\]' if s[i+1]=='[' else '\\)';i+=2;continue
        elif s.startswith(closer,i) and not (closer=='$' and escaped(s,i)):
            end=i+len(closer);out.append((start,end,s[start:end]));start=None;closer=None;i=end;continue
        i+=1
    if start is not None:raise ValueError('Unclosed mathematics delimiter')
    return out

def resolve_variants(s,corrected=True):
    repl=[]
    for m in macros(s,{'var'}):repl.append((m.start,m.end,resolve_variants(m.arguments[1 if corrected else 0],corrected)))
    return replace_ranges(s,repl)

def clean_nested_math(s):
    """Remove only redundant outer dollar pairs in a hand macro already in math.

    The scanner treats a balanced macro argument as one object, so its own dollar
    signs cannot accidentally toggle the surrounding mathematics state.
    """
    out=[];events=[];i=0;mode=None
    while i<len(s):
        if s[i]=='%' and not escaped(s,i):
            j=s.find('\n',i);j=len(s) if j<0 else j+1;out.append(s[i:j]);i=j;continue
        m=re.match(r'\\(hand|over|inserted|unsure|deleted|xout)\b',s[i:])
        if m:
            found=next(macros(s[i:],{m[1]}),None)
            if found and found.start==0:
                original=s[i:i+found.end];replacement=original
                if mode and found.name=='hand' and found.arguments[0].startswith('$') and found.arguments[0].endswith('$'):
                    inner=found.arguments[0][1:-1]
                    if '$' not in inner:
                        replacement='\\hand{'+inner+'}'
                        events.append({'line':s.count('\n',0,i)+1,'before':original,'after':replacement,'operation':'remove nested math delimiters','reason':'The hand macro is already inside a math span; the redundant dollar pair causes a mode error and carries no printed content.'})
                out.append(replacement);i+=found.end;continue
        if s.startswith('\\[',i) or s.startswith('\\(',i):mode=s[i:i+2];out.append(s[i:i+2]);i+=2;continue
        if s.startswith('\\]',i) or s.startswith('\\)',i):mode=None;out.append(s[i:i+2]);i+=2;continue
        if s[i]=='$' and not escaped(s,i):mode=None if mode=='$' else '$'
        out.append(s[i]);i+=1
    return ''.join(out),events

KIND_LABEL_FR={'deletion':'suppression','insertion':'insertion','writing-over':'surcharge','slip-corrected':'coquille corrigée','marginal-note-placed':'note marginale placée','copy2-handwriting':'annotation de la copie 2','copy2-typed-difference':'différence dactylographiée de la copie 2'}
KIND_LABEL_FR.update({'slip corrected':'coquille corrigée','writing over':'surcharge','marginal note placed':'note marginale placée'})
KIND_LABEL_EN={'deletion':'deletion','insertion':'insertion','writing-over':'writing over','slip-corrected':'slip corrected','marginal-note-placed':'marginal note placed','copy2-handwriting':'copy 2 handwriting','copy2-typed-difference':'copy 2 typed difference'}

KIND_LABEL_EN.update({'slip corrected':'slip corrected','writing over':'writing over','marginal note placed':'marginal note placed'})

def annotate(s,key,editorial=None):
    """Annotate authorial corrections and explicitly supplied editorial changes.

    Handwriting as such and unchanged marginal content remain in their source
    macros. Only a changed reading receives a variant.
    """
    variants=[]
    for m in macros(s,{'over','inserted','deleted','xout'}):
        kind={'over':'writing-over','inserted':'insertion','deleted':'deletion','xout':'deletion'}[m.name]
        new=m.arguments[-1] if m.name in ('over','inserted') else ''
        original=s[m.start:m.end];old=original
        vid=f'V-{key}-{kind}-{len(variants)+1:03d}'
        math=any(a<m.start<b for a,b,_ in math_spans(s))
        rf={'over':'La surcharge remplace les caractères dactylographiés.','inserted':'L’ajout est placé à l’endroit indiqué par le signe d’insertion.','deleted':'Le passage biffé est retiré du texte corrigé.','xout':'Le passage rayé à la machine est retiré du texte corrigé.'}[m.name]
        re_={'over':'The overwritten characters replace the typed characters.','inserted':'The addition is placed where its insertion mark points.','deleted':'The struck passage is removed from the corrected text.','xout':'The typewriter strike-out is removed from the corrected text.'}[m.name]
        variants.append({'id':vid,'key':key,'line':m.line,'page_reading':old,'corrected_reading':new,'kind':kind,'source_id':vid,'reason_fr':rf,'reason_en':re_,'math':math,'start':m.start,'end':m.end})
    replacements=[(v['start'],v['end'],'\\var{'+v['page_reading']+'}{'+v['corrected_reading']+'}{'+v['kind']+'}{'+v['id']+'}') for v in variants]
    result=replace_ranges(s,replacements)
    for edit in editorial or []:
        if edit['key']!=key:continue
        old=edit['old'];new=edit['new'];occ=edit.get('occurrence',1)
        pos=-1
        for _ in range(occ):pos=result.find(old,pos+1)
        if pos<0:raise ValueError(f"Editorial variant {edit['id']} target absent")
        vid=edit['id'];kind=edit.get('kind','slip-corrected')
        end=pos+len(old);printed_old=old;printed_new=new
        if ends_in_comment(old):
            if result[end:end+1]!='\n' or not ends_in_comment(new):raise ValueError('Trailing-comment variant requires the matching source newline: '+vid)
            # Absorb the source newline, so generated braces cannot be swallowed
            # by the comment and cannot introduce a space after its printed hyphen.
            printed_old+='\n';printed_new+='\n';end+=1
        result=result[:pos]+'\\var{'+printed_old+'}{'+printed_new+'}{'+kind+'}{'+vid+'}'+result[end:]
        variants.append({'id':vid,'key':key,'line':edit.get('line',s[:s.find(old)].count('\n')+1),'page_reading':old,'corrected_reading':new,'kind':kind,'source_id':edit.get('source_id',','.join(edit.get('source_ids',[])) or vid),'reason_fr':edit['reason_fr'],'reason_en':edit['reason_en'],'math':edit.get('math',False)})
    return result,[{k:v for k,v in item.items() if k not in ('start','end')} for item in variants]

def clean_diagrams(s):
    replacements=[];events=[]
    for m in macros(s,{'diagram'}):
        inner=m.arguments[0]
        marker=r'\begin{tikzcd}'
        at=inner.find(marker)
        if at<0 or 'ampersand replacement=' in inner:continue
        end=at+len(marker)
        if end<len(inner) and inner[end]=='[':
            options,stop=group(inner,end,'[',']')
            converted=inner[:end]+'['+options+r',ampersand replacement=\&]'+inner[stop:]
        else:converted=inner[:end]+r'[ampersand replacement=\&]'+inner[end:]
        converted=re.sub(r'(?<!\\)&',r'\\&',converted)
        old=s[m.start:m.end];new=r'\diagram{'+converted+'}'
        replacements.append((m.start,m.end,new))
        events.append({'line':m.line,'before':old,'after':new,'operation':'make tikz-cd alignment valid inside a macro argument','reason':'Use ampersand replacement and escaped alignment tokens. All diagram objects, indices, arrow directions and labels remain character-for-character unchanged.'})
    return replace_ranges(s,replacements),events

def clean_latex(s):
    s,first=clean_nested_math(s);s,second=clean_diagrams(s)
    return s,first+second

def math_payloads(s):
    payloads=math_spans(s)
    for m in macros(s,{'diagram'}):
        if not any(a<=m.start and m.end<=b for a,b,_ in payloads):payloads.append((m.start,m.end,s[m.start:m.end]))
    return [t for _,_,t in sorted(payloads)]
