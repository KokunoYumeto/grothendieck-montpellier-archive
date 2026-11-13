#!/usr/bin/env python3
"""Static delimiter/structure checks only. Does not compile or alter LaTeX."""
from pathlib import Path
import re,json,csv,hashlib
ROOT=Path(__file__).resolve().parent
SCANS=[43,63,65,72,73,74,75,80]

def uncomment(text):
    return re.sub(r'(?<!\\)%[^\n]*','',text)

def check(path):
    source=path.read_text();s=uncomment(source)
    depth=0;math=None;stack=[];counts={'brace_pairs':0,'display_pairs':0,'dollar_pairs':0,'environment_pairs':0}
    errors=[];i=0
    while i<len(s):
        if s[i]=='\\':
            m=re.match(r'\\(begin|end)\{([^{}]+)\}',s[i:])
            if m:
                op,env=m.groups()
                if op=='begin':stack.append(env)
                elif not stack or stack.pop()!=env:errors.append('Environment mismatch at '+str(i))
                else:counts['environment_pairs']+=1
                # The environment-name braces are balanced and counted here.
                counts['brace_pairs']+=1
                i+=len(m.group());continue
            if i+1<len(s) and s[i+1] in '[]':
                if s[i+1]=='[':
                    if math is not None:errors.append('Display opened inside math at '+str(i))
                    math='display'
                else:
                    if math!='display':errors.append('Unmatched display end at '+str(i))
                    math=None;counts['display_pairs']+=1
                i+=2;continue
            # Escaped punctuation, including braces and dollar signs, is literal.
            if i+1<len(s) and not s[i+1].isalpha():i+=2;continue
            m=re.match(r'\\[A-Za-z]+',s[i:])
            if m:i+=len(m.group());continue
        c=s[i]
        if c=='{':depth+=1
        elif c=='}':
            depth-=1;counts['brace_pairs']+=1
            if depth<0:errors.append('Unmatched closing brace at '+str(i))
        elif c=='$':
            if math=='display':errors.append('Dollar inside display at '+str(i))
            elif math=='inline':math=None;counts['dollar_pairs']+=1
            else:math='inline'
        i+=1
    if depth:errors.append('Final brace depth '+str(depth))
    if math:errors.append('Unclosed '+math+' math')
    if stack:errors.append('Unclosed environments '+repr(stack))
    return dict(file=str(path.relative_to(ROOT)),passed=not errors,counts=counts,errors=errors)

def run():
    files=[ROOT/'pages'/f'C45-01_45_scan{n:03}.tex' for n in SCANS]
    files+=[ROOT/'C45-01_transcription.tex',ROOT/'C45-01_standalone.tex']
    results=[check(p) for p in files]
    assembled=(ROOT/'C45-01_transcription.tex').read_text()
    expected='\n\n'.join((ROOT/'pages'/f'C45-01_45_scan{n:03}.tex').read_text().rstrip() for n in SCANS)+'\n'
    assert assembled==expected,'Assembly differs from concatenated page files'
    assert assembled.startswith('\\cotefile{45}\n\\scanpage{43}')
    assert len(re.findall(r'\\cotefile\{',assembled))==1
    assert [int(n) for n in re.findall(r'\\scanpage\{(\d+)\}',assembled)]==SCANS
    assert not re.search(r'\\(?:newcommand|renewcommand|def|documentclass|includegraphics)\b',assembled)
    rows=list(csv.DictReader((ROOT/'C45-01_inventory.csv').open()))
    assert rows and all(r['transcribed']=='yes' for r in rows)
    assert sorted({int(r['scan']) for r in rows})==SCANS
    assert len({r['element'] for r in rows})==len(rows)
    assert all(r['kind'] in ['text','letter part','display','diagram','drawing','margin note','insertion','deletion','handwritten'] for r in rows)
    assert all(r['hand'] in ['typed','Grothendieck','other hand','unknown'] for r in rows)
    counts={name:len(re.findall(r'\\'+name+r'\{',assembled)) for name in ['unsure','illegible','deleted']}
    # Tables should remain actual Markdown tables after per-page additions.
    for name in ['C45-01_doubts.md','C45-01_notes.md']:
        expected_cols=None
        for line in (ROOT/name).read_text().splitlines():
            if not line.startswith('|'):expected_cols=None;continue
            cols=len(re.findall(r'(?<!\\)\|',line))
            if expected_cols is None:expected_cols=cols
            assert cols==expected_cols,('Inconsistent Markdown table row',name,line)
    assert all(r['passed'] for r in results),results
    return dict(status='PASS',compiled=False,results=results,marks_in_assembled_fragment=counts,inventory_rows=len(rows),unfinished_pages=[])

if __name__=='__main__':
    report=run()
    print(json.dumps(report,ensure_ascii=False,indent=2))
