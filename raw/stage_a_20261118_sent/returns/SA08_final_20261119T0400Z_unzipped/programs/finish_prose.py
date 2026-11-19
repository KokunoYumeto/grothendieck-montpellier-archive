"""Update table counts and canonical citations; apply modest prose spacing.
This edits exposition only, never source quotations or diplomatic transcriptions.
"""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];O=R/'outputs'
a=json.loads((R/'work/integration/reference_aliases.json').read_text())
stats=json.loads((O/'SA08_statistics.json').read_text())
bib=(O/'SA08_references.bib').read_text()
notes=re.findall(r'\bnote\s*=\s*\{(verified|unverified)\}',bib)
dirs=len(re.findall(r'^## \d+\.',(O/'SA08_directions.md').read_text(),re.M))
rows=[('Indexed entries / verdict rows',stats['entries']),('Consolidated items',stats['items']),
 ('Items with indexed source entries',stats['indexed_source_items']),('Direct Codex lead/metadata items',stats['codex_lead_items']),('Additional Pro full-text item without an indexed note',stats['additional_pro_text_items']),
 ('Claim records, including three labelled reconstructions',stats['claims']),('Consolidated historical problems',stats['problems']),('Readings to check against scans',stats['readings']),
 ('Checked local/publication link records',stats['links']),('Separate external-project provenance leads',stats['project_leads']),('Ranked directions',dirs),('Check-event rows',stats['check_events']),
 ('Bibliography works',len(notes)),('References with an opened URL/DOI',notes.count('verified')),('Original-access leads marked unverified',notes.count('unverified'))]
text='| Measure | Count |\n|---|---:|\n'+'\n'.join(f'|{k}|{v}|' for k,v in rows)+'\n\n'
text+='**Indexed-entry verdicts:** '+', '.join(f"{k}: {v}" for k,v in stats['verdicts'].items())+'. No source entry is silently dropped; withdrawal on the manuscript is recorded in item kind and page status rather than deleting an accurate note about that withdrawal.\n\n'
text+='| Item kind | Count |\n|---|---:|\n'+'\n'.join(f'|{k}|{v}|' for k,v in stats['item_kinds'].items())+'\n\n'
defs={'A':'Own-publication match, with donor chronology distinguished','B':'Developed by others into an established result','C':'Partial development or a precise remaining scope gap','D':'No exact later development located in the recorded bounded search','E':'Known antecedent or classical result','F':'Intended claim not identifiable with complete hypotheses'}
text+='| Claim class | Meaning in this dossier | Count |\n|---|---|---:|\n'+'\n'.join(f'|{k}|{defs[k]}|{stats["claims_by_class"].get(k,0)}|' for k in 'ABCDEF')+'\n\n'
text+='| Page-status reporting bin | Count |\n|---|---:|\n'+'\n'.join(f'|{k}|{v}|' for k,v in stats['claims_by_status'].items())+'\n'
dp=O/'SA08_dossier.md';s=dp.read_text();s=re.sub(r'(?s)(<!-- STATISTICS_START -->).*?(<!-- STATISTICS_END -->)',lambda m:m.group(1)+'\n'+text+'\n'+m.group(2),s);dp.write_text(s)
changes={}
for n in ['SA08_dossier.md','SA08_directions.md','README.md']:
 p=O/n;s=p.read_text();before=s
 s=s.replace('SA 08','SA08')
 s=re.sub(r'@([A-Za-z][A-Za-z0-9_]*)',lambda m:'@'+a.get(m.group(1),m.group(1)),s)
 # Clear references to retired members inside numerical ranges.
 s=s.replace('SA08-C217–SA08-C226','SA08-C217–SA08-C221, SA08-C223–SA08-C226')
 s=s.replace('SA08-C220–SA08-C225','SA08-C220–SA08-C221, SA08-C223–SA08-C225')
 s=s.replace('SA08-305–SA08-307','SA08-305, SA08-307')
 # Shield identifiers, citation keys, inline code, and mathematical content.
 saved=[]
 def hide(m):saved.append(m.group(0));return '\x00'+str(len(saved)-1)+'\x00'
 s=re.sub(r'`[^`]*`|\\\(.*?\\\)|\\\[.*?\\\]|@[A-Za-z][A-Za-z0-9_]*|(?:MP-)?SA08-[A-Z]?\d+|\bSA08\b|MPL_136_\d+-\d+|K136-\d+',hide,s,flags=re.S)
 s=re.sub(r'(?<=[A-Za-z])(?=\d)', ' ',s)
 s=re.sub(r'(?<=\d)(?=[A-Za-z])', ' ',s)
 s=re.sub(r'\bClass([A-F])\b',r'Class \1',s)
 s=re.sub(r'([,;:])(?=[A-Za-z0-9])',r'\1 ',s)
 s=re.sub(r'(?i)\b(the|all|its|in|of|at|on|over|from|by|and|with|through|between|than|scan|scans|cote|degree|degrees|weight|weights|arity|index|indices|part|section|theorem|theorems|proposition|propositions|corollary|lemma|remark|paragraph|chapter)(?=\d)',r'\1 ',s)
 s=re.sub(r'(?<=\d)(January|February|March|April|May|June|July|August|September|October|November|December)',r' \1',s)
 s=re.sub(r'(January|February|March|April|May|June|July|August|September|October|November|December)(?=\d)',r'\1 ',s)
 s=re.sub(r'\bpp\s*(?=\d)',r'pp. ',s);s=re.sub(r'\bp\s*(?=\d)',r'p. ',s)
 s=re.sub(r'\b(printed|published)(?=pp?\.)',r'\1 ',s)
 s=re.sub(r'(§\d+)(?=Theorem|Proposition|Lemma|Remark)',r'\1 ',s)
 s=re.sub(r'(?<=[A-Za-z])(?=\x00\d+\x00)', ' ',s)
 s=re.sub(r'(?<=\x00)(?=[A-Za-z])',' ',s)
 s=re.sub(r'\x00(\d+)\x00',lambda m:saved[int(m.group(1))],s)
 p.write_text(s)
 changes[n]={'changed':s!=before,'words':len(s.split()),'citation_occurrences':len(re.findall(r'@[A-Za-z][A-Za-z0-9_]*',s))}
print(json.dumps({'statistics_written':rows,'prose':changes},ensure_ascii=False,indent=2))
