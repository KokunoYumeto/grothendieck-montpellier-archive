"""Mechanical index of explicit earlier-run pointers; not a verdict engine."""
from pathlib import Path
import json,re,csv
B=Path(__file__).resolve().parents[1]
entries=json.loads((B.parents[1]/'source_audit/MPL_43_094-142_entries.json').read_text())
targets={
 'WG2 §1.1 #3':r'WG2\s*§\s*1\.1\s*#3',
 'WG2 §2.3 #12':r'WG2\s*§\s*2\.3\s*#12',
 'WG H1':r'WG\s+H1\b','WG H9':r'WG\s+H9\b',
 'FLAGGED_149 B5':r'FLAGGED_149\s+B5\b','FLAGGED_149 B9':r'FLAGGED_149\s+B9\b',
 'FLAGGED_149 Z142g':r'FLAGGED_149\s+Z142g\b','FLAGGED_149 A9':r'FLAGGED_149\s+A9\b',
 'FLAGGED_149 F8a':r'FLAGGED_149\s+F8a\b',
 'LM6 F.35':r'LM6\s+F\.35\b','LM6 F.43':r'LM6\s+F\.43\b',
 'LM6 B.22':r'LM6\s+B\.22\b','LM6 B.27':r'LM6\s+B\.27\b','LM6 A.50':r'LM6\s+A\.50\b',
 'CYCLOTOMIC_KERNEL C1':r'CYCLOTOMIC_KERNEL\s+C1\b',
 'INTAKE 20261114 §4.4':r'INTAKE\s+20261114\s*§\s*4\.4',
 'MPL_136_095-141 §1.5':r'MPL_136_095-141\s+(?:§\s*)?1\.5',
 'MPL_136_189-234 R008':r'MPL_136_189-234\s+R008',
 'MPL_136_235-281 N16':r'MPL_136_235-281\s+N16',
 'README bridge B11':r'(?:bridge|arithmetic bridge)\s+B11\b',
 '149 Théorème 3':r'149\s+Théorème\s+3',
 '142 Proposition 2':r'142\s+Proposition\s+2',
 '149/85':r'149\s*/\s*85|149\s+scan\s+85',
}
rows=[]
for e in entries:
 text=e['entry_text'].replace('**','').replace('`','')
 for target,pattern in targets.items():
  hits=list(re.finditer(pattern,text))
  if hits:
   m=hits[0]
   a=text.rfind('\n',0,m.start())+1
   z=text.find('\n',m.end())
   if z<0:z=len(text)
   rows.append(dict(entry_id=e['entry_id'],target=target,occurrences_in_entry=len(hits),
                    source_context=text[a:z].strip(),
                    verification='UNVERIFIED TARGET: cited external package/source not supplied; this records a pointer, not its truth or review status.'))
with (B/'external_pointer_index.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['entry_id','target','occurrences_in_entry','source_context','verification'],delimiter='\t');w.writeheader();w.writerows(rows)
print(f'{len(rows)} entry/target pairs; {len({r["target"] for r in rows})} distinct named targets; {len({r["entry_id"] for r in rows})} citing entries')
print('Target counts:')
for target in targets:
 matches=[r['entry_id'] for r in rows if r['target']==target]
 print(target+': '+(';'.join(matches) if matches else 'none in individually indexed entries'))
print('The final SF/title register entry also carries context-table pointers; they are included from its full source text. No target-file verification is claimed.')
