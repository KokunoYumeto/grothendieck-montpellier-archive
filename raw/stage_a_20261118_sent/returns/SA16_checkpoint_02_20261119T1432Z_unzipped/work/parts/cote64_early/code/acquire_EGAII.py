"""Reproduce primary-source acquisition without redistributing its full text.

The live download was initiated through urllib.request.urlretrieve and completed
on 2026-11-19, before this small reproducibility wrapper was saved. Source files
belong outside work in the excluded external_cache directory.
"""
import hashlib,json,subprocess,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
cache=ROOT.parents[2]/'external_cache'/'cote64_early'
cache.mkdir(parents=True,exist_ok=True)
url='https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EGA/EGAII.pdf'
pdf=cache/'EGAII.pdf'
if not pdf.exists(): urllib.request.urlretrieve(url,pdf)
txt=pdf.with_suffix('.txt')
if not txt.exists(): subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],check=True)
result={'url':url,'retrieval_date':'2026-11-19','bytes':pdf.stat().st_size,
 'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
 'extraction_command':['pdftotext','-layout','EGAII.pdf','EGAII.txt'],
 'read_locators':'Printed pp.72–76: Propositions4.1.6 and4.2.3, Theorem4.2.4, sections4.2.8–10.',
 'own_result_note':'The canonical quotient is invertible and universal; its functoriality fixes the projective convention used in the independent tangent-line derivation.',
 'external_full_text':'Excluded from deliverables; cache only.'}
(ROOT/'outputs'/'EGAII_source.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
