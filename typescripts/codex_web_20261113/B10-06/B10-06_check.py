#!/usr/bin/env python3
"""Static delimiter/environment check; deliberately does not invoke TeX."""
from pathlib import Path
import re
import sys

SCANS = [77, 78, 79, 80, 81, 82, 83, 84, 86, 87]
ROOT = Path(__file__).resolve().parent

def check(p):
    s=p.read_text(encoding='utf-8')
    braces=[];envs=[];math=[];dollars=0;groups=0;begins=0;displays=0
    i=0;line=1;errors=[]
    while i<len(s):
        c=s[i]
        if c=='\n':line+=1;i+=1;continue
        if c=='%':
            j=s.find('\n',i);i=len(s) if j<0 else j;continue
        if c=='\\':
            m=re.match(r'\\([A-Za-z]+|.)',s[i:])
            if not m:errors.append(f'line {line}: trailing backslash');break
            cmd=m[1];i+=len(m[0])
            if cmd in ['[','(']:
                math.append((cmd,line))
                if cmd=='[':displays+=1
            elif cmd in [']',')']:
                expected='[' if cmd==']' else '('
                if not math or math[-1][0]!=expected:errors.append(f'line {line}: unmatched math delimiter \\{cmd}')
                else:math.pop()
            elif cmd in ['begin','end']:
                e=re.match(r'\{([^{}]+)\}',s[i:])
                if not e:errors.append(f'line {line}: missing environment name')
                else:
                    name=e[1]
                    if cmd=='begin':envs.append((name,line));begins+=1
                    elif not envs or envs[-1][0]!=name:errors.append(f'line {line}: unmatched end {name}')
                    else:envs.pop()
            continue
        if c=='{':braces.append(line);groups+=1
        elif c=='}':
            if not braces:errors.append(f'line {line}: unmatched closing brace')
            else:braces.pop()
        elif c=='$':dollars+=1
        i+=1
    if braces:errors.append('unclosed braces from lines '+str(braces))
    if envs:errors.append('unclosed environments '+str(envs))
    if math:errors.append('unclosed math delimiters '+str(math))
    if dollars%2:errors.append(f'odd dollar-sign count {dollars}')
    return errors,dict(brace_pairs=groups,display_pairs=displays,dollar_pairs=dollars//2,environments=begins)

def main():
    files=[ROOT/'pages'/f'B10-06_10_scan{n:03}.tex' for n in SCANS]
    files += [ROOT/'B10-06_transcription.tex',ROOT/'B10-06_standalone.tex']
    failed=False
    for p in files:
        errors,counts=check(p)
        print(('FAIL' if errors else 'PASS')+' '+p.name+' '+', '.join(f'{k}={v}' for k,v in counts.items()))
        for e in errors:print('  '+e)
        failed=failed or bool(errors)
    fragment=(ROOT/'B10-06_transcription.tex').read_text()
    joined=''.join((ROOT/'pages'/f'B10-06_10_scan{n:03}.tex').read_text() for n in SCANS)
    structural={
      'fragment is exact page-file concatenation':fragment==joined,
      'one cotefile marker at start':fragment.startswith('\\cotefile{10}\n') and fragment.count('\\cotefile{')==1,
      'scan markers in requested order':[int(x) for x in re.findall(r'\\scanpage\{(\d+)\}',fragment)]==SCANS,
      'no notation definitions':not re.search(r'\\(?:newcommand|renewcommand|def|DeclareMathOperator)\b',fragment),
      'no embedded scan images':'\\includegraphics' not in fragment,
      'word join 079/080 preserved':'équi%\n% archive sheet number: 78\n\\scanpage{80}%\nvalente' in fragment,
    }
    for label,ok in structural.items():
        print(('PASS ' if ok else 'FAIL ')+label);failed=failed or not ok
    print('Compilation: not attempted.')
    return 1 if failed else 0

if __name__=='__main__':sys.exit(main())
