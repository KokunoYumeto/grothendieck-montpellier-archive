"""Repair mechanical word-spacing in authored English prose, preserving source quotes and IDs."""
import csv,json,pathlib,re
R=pathlib.Path('SA05/work/cote11a')
def polish(s):
 if not isinstance(s,str):return s
 s=re.sub(r'\b(Theorem|Lemma|Proposition|Corollary|Remark|Definition|Chapter|Section|Exposé|printed|published|scan|cote|lines|line|characteristic|dimension|degree|fall|June|submitted|version)(?=[0-9])',r'\1 ',s)
 s=re.sub(r'\b(As of)(?=[0-9])',r'\1 ',s)
 s=re.sub(r'\b(in|for|to|of|from|on|over|with|under|by|and|all|every|the|an|if|when|while|since|assume|assumes|has|is|as|at|but|hence|then|satisfies|requires|contains|gives|proves|named|both|its|into|allows)(?=[A-Z0-9ℓδ])',r'\1 ',s)
 s=re.sub(r'(?<=[a-zé])(?=Poincaré|Künneth|Frobenius|Noetherian|Cartier|Weil|Kock|Hua|Murayama|Stacks|EGA|SGA|GIT|Codex|Lean|Chow|Tate|Dieudonné)',r' ',s)
 s=s.replace('all8','all 8').replace('current64','current 64').replace('the64','the 64').replace('the8','the 8').replace('forstringsm','for strings m').replace('printedp','printed p').replace('printedpp','printed pp').replace('date2026','date 2026').replace('section11','section 11').replace('forf,','for f,')
 return s
fields={
 'items.json':['statement','reconstruction','check_reason'],
 'claims.json':['statement','fate','fate_date','present_status','attribution'],
 'problems.json':['title','as_he_states','plausible_today','state_of_art','why_open','worth','attribution']}
for name,ks in fields.items():
 data=json.loads((R/name).read_text())
 for obj in data:
  for k in ks:
   if k in obj:obj[k]=polish(obj[k])
  if isinstance(obj.get('computation'),dict):obj['computation']['check']=polish(obj['computation']['check'])
 (R/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
for name,ks in [('entries.tsv',['reason']),('CHECK_EVENTS.tsv',['outcome']),('search_log.tsv',['outcome','verification_extent']),('readings.tsv',['alternative','evidence']),('links.tsv',['what','evidence']),('reference_checks.tsv',['extent','limitations'])]:
 with (R/name).open() as f:rd=csv.DictReader(f,delimiter='\t');rows=list(rd);header=rd.fieldnames
 for row in rows:
  for k in ks:row[k]=polish(row[k])
 with (R/name).open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=header,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('Mechanical prose spacing repaired; source quotations, identifiers, formulas and source files preserved.')
