#!/usr/bin/env python3
"""Compact completeness/coverage metadata checks, separate from spectra."""
from pathlib import Path
import hashlib,json
B=Path(__file__).resolve().parent
R=B.parents[2]
p=R/'research/orthogonal_small_inputs.json'
D=json.loads(p.read_text());tabs={t['name']:t for t in D['tables']}
expected={
 'O7(3)':('6','2'),'O8-(2)':('','2'),'O8+(3)':('2^2','S4'),
 'O8-(3)':('2','2^2'),'O9(3)':('2','2'),
 'O10+(2)':('','2'),'O10-(2)':('','2'),
 'O12+(2)':('','2'),'O12-(2)':('','2')}
assert {t['name']:tuple(t['extension_information']) for t in D['metadata']}==expected
assert D['gap_version']=='4.16.1' and D['ctbllib_version']=='1.3.11'
for name,(mult,outer) in expected.items():
 cover=(mult+'.' if mult else '')+name
 assert cover in tabs
 if name not in ['O8+(3)','O8-(3)','O9(3)']:
  extension=cover+'.2'
  assert extension in tabs and tabs[extension]['core']==cover
  # Nontrivial conjugation on core classes confirms a genuine outer action.
  fusion=tabs[extension]['fusion']
  assert len(set(fusion))<len(fusion)
official_classes={
 '6.O7(3)':180,'6.O7(3).2':186,'O8-(2)':39,'O8-(2).2':60,
 '2^2.O8+(3)':354,'2.O8-(3)':190,'2.O9(3)':326,
 'O10+(2)':97,'O10+(2).2':155,'O10-(2)':115,'O10-(2).2':164,
 'O12+(2)':271,'O12+(2).2':392,'O12-(2)':237,'O12-(2).2':375}
for name,n in official_classes.items():assert len(tabs[name]['characters'])==n
assert 'PossibleCharacterTablesOfTypeV4G' in tabs['2^2.O8+(3)']['information']
for name in ['2.O8-(3)','2.O9(3)']:
 assert 'April 2008' in tabs[name]['information']
for name in ['O12+(2)','O12-(2)']:
 assert 'Magma V2.23-9' in tabs[name]['information']
assert '1986' in tabs['O12+(2).2']['information']
assert '1987' in tabs['O12-(2).2']['information']
out={'status':'PASS','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'metadata':D['metadata'],'official_page_class_counts':official_classes,
     'scope':'retained official complete-table metadata and six nontrivial outer fusions; no reconstruction of original group table constructions'}
(B/'metadata_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS nine universal covers, six genuine outer actions, fifteen complete official class counts')
