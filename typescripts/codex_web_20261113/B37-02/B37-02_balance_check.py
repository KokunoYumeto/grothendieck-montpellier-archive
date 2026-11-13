"""Non-compiling checks for the B37-02 diplomatic transcription.

Run from any directory: python B37-02_balance_check.py
This checks source delimiters, not TeX expansion, typography or mathematical truth.
"""
from pathlib import Path
import re, csv, json, hashlib

BASE=Path(__file__).resolve().parent
SCANS=[18,23,24,25,27,30,31,34,35]

def escaped(s,i):
    j=i-1;n=0
    while j>=0 and s[j]=='\\':n+=1;j-=1
    return bool(n%2)

def without_comments(s):
    lines=[]
    for line in s.splitlines():
        for i,c in enumerate(line):
            if c=='%' and not escaped(line,i):
                line=line[:i];break
        lines.append(line)
    return '\n'.join(lines)

def check(path):
    raw=path.read_text();s=without_comments(raw);issues=[];depth=0
    for i,c in enumerate(s):
        if c in '{}' and not escaped(s,i):
            depth+=1 if c=='{' else -1
            if depth<0:issues.append('closing brace before opening at offset '+str(i))
    if depth:issues.append('brace depth '+str(depth))
    state=None;dollars=0;displays=[0,0];parens=[0,0]
    for m in re.finditer(r'\\\[|\\\]|\\\(|\\\)|\$',s):
        tok=m.group();i=m.start()
        if escaped(s,i):continue
        if tok=='$':
            dollars+=1
            if state=='$':state=None
            elif state is None:state='$'
            else:issues.append('dollar inside explicit math at offset '+str(i))
        elif tok in [r'\[',r'\(']:
            (displays if tok==r'\[' else parens)[0]+=1
            if state is not None:issues.append('nested math opener at offset '+str(i))
            state=tok
        else:
            (displays if tok==r'\]' else parens)[1]+=1
            want=r'\[' if tok==r'\]' else r'\('
            if state!=want:issues.append('unmatched math close at offset '+str(i))
            state=None
    if state:issues.append('unclosed math '+state)
    if dollars%2:issues.append('odd dollar count')
    stack=[];envs={}
    for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',s):
        if escaped(s,m.start()):continue
        action,name=m.groups()
        if action=='begin':stack.append(name);envs[name]=envs.get(name,0)+1
        elif not stack or stack.pop()!=name:issues.append('environment mismatch '+name)
    if stack:issues.append('unclosed environments '+repr(stack))
    return {'file':str(path.relative_to(BASE)),'passed':not issues,'issues':issues,'dollar_tokens':dollars,'display_open_close':displays,'paren_math_open_close':parens,'environments':envs}

def main():
    pages=[BASE/'pages'/f'B37-02_37_scan{n:03}.tex' for n in SCANS]
    targets=pages+[BASE/'B37-02_transcription.tex',BASE/'B37-02_standalone.tex']
    result=[check(p) for p in targets]
    expected=''.join(p.read_text() for p in pages)
    assembled=(BASE/'B37-02_transcription.tex').read_text()
    assertions={
        'page_order':re.findall(r'\\scanpage\{(\d+)\}',assembled)==list(map(str,SCANS)),
        'exact_concatenation':assembled==expected,
        'one_cotefile_at_start':assembled.startswith(r'\cotefile{37}') and assembled.count(r'\cotefile{')==1,
        'no_page_macro_definitions':not re.search(r'\\(?:def|newcommand|renewcommand)\b',assembled),
        'no_embedded_images':not re.search(r'\\(?:includegraphics|includepdf)\b',assembled),
        'no_document_preamble_in_fragment':not re.search(r'\\documentclass|\\begin\{document\}',assembled),
        'tikzcd_escaped_ampersands':all(r'ampersand replacement=\&' in x for x in re.findall(r'\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}',assembled,re.S)),
    }
    with (BASE/'B37-02_inventory.csv').open(newline='') as f:
        reader=csv.DictReader(f);header=reader.fieldnames;rows=list(reader)
    assertions['inventory_columns']=header==['cote','scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
    assertions['all_inventory_yes']=all(r['transcribed']=='yes' for r in rows)
    assertions['all_scans_in_inventory']=set(int(r['scan']) for r in rows)==set(SCANS)
    assertions['unique_inventory_ids']=len(set(r['element'] for r in rows))==len(rows)
    assertions['inventory_order']=list(map(int,(r['scan'] for r in rows)))==sorted(int(r['scan']) for r in rows)
    assertions['valid_sheet_kind']=all(r['sheet_kind'] in ['text','letter','reused_typed','cancelled_draft','cover'] for r in rows)
    assertions['valid_hand']=all(r['hand'] in ['typed','Grothendieck','other hand','unknown'] for r in rows)
    assertions['valid_element_kind']=all(r['kind'] in ['text','letter part','display','diagram','drawing','margin note','insertion','deletion','handwritten'] for r in rows)
    counts={k:len(re.findall(r'\\'+k+r'\{',without_comments(assembled))) for k in ['unsure','illegible','deleted']}
    by_page={str(n):{k:len(re.findall(r'\\'+k+r'\{',without_comments(p.read_text()))) for k in counts} for n,p in zip(SCANS,pages)}
    payload={'compilation_attempted':False,'checks':result,'assertions':assertions,'macro_occurrences_in_page_text_only':counts,'per_page_counts':by_page,'inventory_rows':len(rows),'passed':all(x['passed'] for x in result) and all(assertions.values())}
    print(json.dumps(payload,ensure_ascii=False,indent=2))
    return 0 if payload['passed'] else 1

if __name__=='__main__':raise SystemExit(main())
