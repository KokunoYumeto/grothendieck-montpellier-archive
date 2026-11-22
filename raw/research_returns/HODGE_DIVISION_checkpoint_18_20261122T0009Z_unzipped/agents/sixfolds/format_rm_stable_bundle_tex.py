#!/usr/bin/env python3
"""Unabridged conversion of independently reviewed SF-E811--E812."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

root = Path(__file__).resolve().parent
source = (root / 'rm_stable_bundle_obstruction_draft.md').read_text()
(root / 'rm_stable_bundle_obstruction_proofs.md').write_text(source)
tex = subprocess.check_output(
    ['pandoc', '-f', 'markdown+tex_math_single_backslash', '-t', 'latex'],
    input=source.encode()).decode().replace('\\tightlist\n', '')
for name in ('SF-E811', 'SF-E811-RM', 'SF-E812'):
    tex = re.sub(r'(\\subsection\{' + name + r'\.[\s\S]*?\})\\label\{[^}]*\}',
                 lambda m: m[1] + '\\label{' + name + '}', tex, count=1)
assert tex.count('\\(') == tex.count('\\)')
assert tex.count('\\[') == tex.count('\\]')
assert not any(ord(c) < 32 and c not in '\n\r\t' for c in tex)
assert '$' not in tex
assert sorted(re.findall(r'\\begin\{([^}]+)\}', tex)) == sorted(re.findall(r'\\end\{([^}]+)\}', tex))
path = root / 'rm_stable_bundle_obstruction_section.tex'
path.write_text(tex)
out = {'file': path.name, 'lines': len(tex.splitlines()),
       'sha256': hashlib.sha256(tex.encode()).hexdigest(),
       'inline_pairs': tex.count('\\('), 'display_pairs': tex.count('\\['),
       'PDF_compilation_claimed': False}
(root / 'rm_stable_bundle_conversion_check.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
