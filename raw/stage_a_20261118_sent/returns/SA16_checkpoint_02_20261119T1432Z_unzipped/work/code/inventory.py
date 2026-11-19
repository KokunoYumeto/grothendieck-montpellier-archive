#!/usr/bin/env python3
"""Inventory the attached transcriptions; no mathematical verdicts are generated."""
from pathlib import Path
import re, json
root=Path(__file__).resolve().parents[2]
rows=[]
for path in sorted((root/'sources/SA16_texts').glob('*/*transcription.tex')):
    text=path.read_text()
    rows.append({'file':str(path.relative_to(root/'sources')),'lines':len(text.splitlines()),
                 'cote':re.findall(r'\\cotefile\{([^}]+)\}',text),
                 'scans':re.findall(r'\\scanpage\{([^}]+)\}',text)})
out=json.dumps(rows,ensure_ascii=False,indent=2)+'\n'
(root/'work/outputs/source_inventory.json').write_text(out)
print(out)
