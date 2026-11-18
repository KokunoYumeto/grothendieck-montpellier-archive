"""Lexical LaTeX balance check only; this does not run a TeX compiler."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
TOKEN = re.compile(r'\\(begin|end)\{([^{}]+)\}|\\[\[\]()]|\\[{}%$]|\\\\|\\[A-Za-z@]+|\\.|[$ {}]', re.X)

def uncomment(source):
    out=[]
    for line in source.splitlines():
        for i,c in enumerate(line):
            if c=='%':
                k=i-1; n=0
                while k>=0 and line[k]=='\\': n+=1; k-=1
                if n%2==0: line=line[:i]; break
        out.append(line)
    return '\n'.join(out)

def check(path):
    source=uncomment(path.read_text())
    braces=[]; envs=[]; math=[]; errors=[]; dollars=0
    for m in TOKEN.finditer(source):
        t=m.group(); line=source[:m.start()].count('\n')+1
        if m.group(1)=='begin':envs.append((m.group(2),line))
        elif m.group(1)=='end':
            name=m.group(2)
            if not envs or envs[-1][0]!=name:errors.append(f'{line}: unmatched end {name}')
            else:envs.pop()
        elif t=='{':braces.append(line)
        elif t=='}':
            if not braces:errors.append(f'{line}: unmatched closing brace')
            else:braces.pop()
        elif t in (r'\[',r'\('):
            if math:errors.append(f'{line}: nested math delimiter {t}')
            math.append((t,line))
        elif t in (r'\]',r'\)'):
            expected={r'\]':r'\[',r'\)':r'\('}[t]
            if not math or math[-1][0]!=expected:errors.append(f'{line}: unmatched math delimiter {t}')
            else:math.pop()
        elif t=='$':
            dollars+=1
            if math and math[-1][0]=='$':math.pop()
            elif math:errors.append(f'{line}: dollar delimiter inside another math delimiter')
            else:math.append(('$',line))
    if braces:errors.append(f'Unclosed braces at lines {braces}')
    if envs:errors.append(f'Unclosed environments: {envs}')
    if math:errors.append(f'Unclosed math delimiters: {math}')
    if dollars%2:errors.append('Odd dollar delimiter count')
    return errors

def main():
    files=sorted((ROOT/'pages').glob('*.tex'))+[ROOT/'CTRL-145_transcription.tex',ROOT/'CTRL-145_standalone.tex']
    failed=False
    for path in files:
        errors=check(path)
        failed |= bool(errors)
        print(('FAIL' if errors else 'PASS')+' '+path.relative_to(ROOT).as_posix())
        for error in errors:print('  '+error)
    print('No compilation attempted. This checks lexical balance, not mathematical correctness or rendered layout.')
    return int(failed)

if __name__=='__main__':sys.exit(main())
