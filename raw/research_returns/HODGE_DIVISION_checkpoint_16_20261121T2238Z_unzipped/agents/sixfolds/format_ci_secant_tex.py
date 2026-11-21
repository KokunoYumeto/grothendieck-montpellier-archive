#!/usr/bin/env python3
"""Convert the independently root-reviewed SF-E809--E810 proof unabridged."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

root=Path(__file__).resolve().parent
source=(root/'ci_secant_obstruction_draft.md').read_text()
(root/'ci_secant_obstruction_proofs.md').write_text(source)
tex=subprocess.check_output(
    ['pandoc','-f','markdown+tex_math_single_backslash','-t','latex'],
    input=source.encode()).decode().replace('\\tightlist\n','')
for n in (809,810):
    tex=re.sub(r'(\\subsection\{SF-E'+str(n)+r'\.[\s\S]*?\})\\label\{[^}]*\}',
               lambda m:m[1]+'\\label{SF-E'+str(n)+'}',tex,count=1)
assert tex.count('\\(')==tex.count('\\)')
assert tex.count('\\[')==tex.count('\\]')
assert not any(ord(x)<32 and x not in '\n\r\t' for x in tex)
assert '$' not in tex
assert sorted(re.findall(r'\\begin\{([^}]+)\}',tex))==sorted(re.findall(r'\\end\{([^}]+)\}',tex))
path=root/'ci_secant_obstruction_section.tex'
path.write_text(tex)
out={'file':path.name,'lines':len(tex.splitlines()),
     'sha256':hashlib.sha256(tex.encode()).hexdigest(),
     'inline_pairs':tex.count('\\('),'display_pairs':tex.count('\\['),
     'PDF_compilation_claimed':False}
(root/'ci_secant_conversion_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
