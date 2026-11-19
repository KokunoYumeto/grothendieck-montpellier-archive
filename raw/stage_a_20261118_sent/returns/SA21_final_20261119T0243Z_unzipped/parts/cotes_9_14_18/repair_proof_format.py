"""Repair inline-math delimiters lost in the initial JS patch transport.
No mathematical wording or verdict is altered.
Run: python repair_proof_format.py > proof_format_output.txt
"""
from pathlib import Path
import re
p=Path(__file__).with_name('formalism_and_checks.md')
s=p.read_text()
marker='<!-- inline math normalized -->'
if marker in s:
    print('Already normalized; unchanged.')
else:
    s=s.replace('\x0barphi',r'\varphi').replace('gamma^',r'\gamma^')
    out=[]; display=False; count=0
    for line in s.splitlines():
        if line.strip()==r'\[':display=True
        if display:
            out.append(line)
            if line.strip()==r'\]':display=False
            continue
        result=[];i=0
        while i<len(line):
            if line[i]!='(':
                result.append(line[i]);i+=1;continue
            start=i+1;depth=1;i+=1
            while i<len(line) and depth:
                if line[i]=='(':depth+=1
                if line[i]==')':depth-=1
                i+=1
            assert depth==0,line
            body=line[start:i-1]
            body=re.sub(r"(?<![A-Za-z_^\\])\{([A-Za-z0-9,']+)\}",lambda m:r'\{'+m.group(1)+r'\}',body)
            body=re.sub(r"\\\{([A-Za-z0-9,']+)\}",lambda m:r'\{'+m.group(1)+r'\}',body)
            result.extend(('$',body,'$'));count+=1
        out.append(''.join(result))
    out.append(marker)
    p.write_text('\n'.join(out)+'\n')
    assert not any(ord(c)<32 and c not in '\n\t\r' for c in p.read_text())
    print(f'Normalized {count} inline mathematical expressions; display math preserved. No control characters remain.')
