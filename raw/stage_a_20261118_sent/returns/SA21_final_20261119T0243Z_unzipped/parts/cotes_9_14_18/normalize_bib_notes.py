"""Normalize only verification-marker fields, preserving full details in annote.
Run: python normalize_bib_notes.py > bib_normalization_output.txt
"""
from pathlib import Path
import re
p=Path(__file__).with_name('references_new.bib')
s=p.read_text()
def change(m):
    return 'note={'+m.group(1)+'},\n annote={'+m.group(2)+'}'
s,n=re.subn(r'note=\{(verified|unverified); ([^\n]+)\}',change,s)
p.write_text(s)
print(f'Normalized{n} note fields; full former detail retained in annote. Idempotent on rerun.')
