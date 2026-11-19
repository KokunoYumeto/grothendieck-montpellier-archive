"""Correct the bibliographic chapter locator after checking the primary OCR.
Does not edit manuscript sources or historical web-query output.
"""
from pathlib import Path
import json
P=Path(__file__).parent
files=['curated_zz_assessment.py','curated_zzz_completion.py','references.bib','narrative.md','proof_audits.md','finalize_records.py']
changes=[]
for name in files:
    f=P/name;s=f.read_text();t=s
    if name=='finalize_records.py':
        # Preserve the literal historical query strings; correct the assessment.
        t=t.replace("'Birkhoff1948':'Opened scanned primary book; chV§5", "'Birkhoff1948':'Opened scanned primary book; chIV§5")
    else:
        t=t.replace('Birkhoff1948 Chapter V','Birkhoff1948 Chapter IV')
        t=t.replace('Birkhoff1948, Chapter V','Birkhoff1948, Chapter IV')
        t=t.replace('Birkhoff1948 V§','Birkhoff1948 IV§')
        t=t.replace('Birkhoff1948 chV','Birkhoff1948 chIV')
        t=t.replace('Chapter V sections 5--6','Chapter IV sections 5--6')
        t=t.replace('chapter V §5','chapter IV §5')
    if t!=s:
        f.write_text(t);changes.append(name)
print(json.dumps({'corrected_files':changes,
 'evidence':'parts/cotes_3_5/outputs/birkhoff1948.txt:3855–3857 (Chapter IV Complete Lattices),4234–4389 (§§5–6),4886–4887 (Chapter V Modular Lattices)',
 'unchanged':'Theorem9+Corollary pp54–56; Theorem10 p56; mathematical claims and source manuscript unchanged.',
 'historic_query_note':'S05/S09 record the earlier mistaken chapter query wording; the corrected result locator and new check event control.'},indent=2))
