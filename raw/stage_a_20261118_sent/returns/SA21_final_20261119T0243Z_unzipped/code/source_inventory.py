"""Mechanical source/locator inventory; editorial full-read decisions are external."""
from pathlib import Path
import csv,hashlib,json,re,collections
R=Path(__file__).resolve().parents[1];W=R.parent;S=W/'sources/texts'
expected=set(re.findall(r'J156-\d+-\d+',(S/'TOPIC.md').read_text()))
actual={p.stem.replace('_transcription','') for p in (S/'codex').glob('*_transcription.tex')}
assert actual==expected and len(actual)==82
records=[];scans={}
for p in sorted(S.rglob('*transcription.tex')):
 text=p.read_text();lines=text.splitlines();cote=None;marks=[]
 if p.parent.name=='codex':cote=int(re.match(r'J156-(\d+)-',p.name).group(1))
 for no,line in enumerate(lines,1):
  m=re.search(r'\\cotefile\{156-(\d+)\}',line)
  if m:cote=int(m.group(1))
  m=re.search(r'\\scanpage\{(\d+)\}',line)
  if m:
   scan=int(m.group(1));marks.append({'cote':f'156-{cote}','scan':scan,'line':no});scans.setdefault(cote,[]).append({'scan':scan,'file':str(p.relative_to(S)),'line':no})
 folder=p.stem.replace('_transcription','')
 if p.parent.name=='pro':owner='/root';note=W/'sources/notes/pro'/f'{folder}_notes.md'
 else:
  c=int(re.match(r'J156-(\d+)-',folder).group(1));f=int(folder.rsplit('-',1)[1]);note=W/'sources/notes/codex'/f'{folder}_notes.md'
  owner='/root/cotes_156_3_5' if c in [3,4,5] or c==9 and 9<=f<=13 else '/root/cotes_156_6_7' if c in [6,7] or c==9 and f>=14 else '/root/cotes_156_8_9'
 assert note.exists(),note
 records.append({'folder':folder,'transcription':str(p.relative_to(S)),'transcription_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'physical_lines':len(lines),'scan_markers':len(marks),'scan_range':';'.join(f'{x["cote"]}:{x["scan"]}' for x in marks),'notes':str(note.relative_to(W/'sources/notes')),'notes_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'reader':owner,'read_status':'full transcription and corresponding notes read; individual decisions in items/claims and owner logs'})
with (R/'SA21_coverage.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(records[0]),delimiter='\t');w.writeheader();w.writerows(records)
(R/'audit/scan_inventory.json').write_text(json.dumps(scans,ensure_ascii=False,indent=2)+'\n')
catalog={1:26,2:18,3:40,4:88,5:48,6:93,7:113,8:126,9:139}
summary=[]
for c,rows in sorted(scans.items()):
 nums=[r['scan'] for r in rows];assert len(nums)==len(set(nums))
 summary.append({'cote':f'156-{c}','catalogue_pages':catalog[c],'supplied_markers':len(nums),'supplied_manuscript_markers':len([n for n in nums if n>=2]),'missing_catalogue_scan_numbers':sorted(set(range(2,catalog[c]+2))-set(nums)),'cover_marker':1 in nums})
result={'folders':len(records),'Codex_folders':len(actual),'Pro_packages':1,'supplied_total_scan_markers':sum(len(v) for v in scans.values()),'supplied_manuscript_scan_markers':sum(x['supplied_manuscript_markers'] for x in summary),'catalogue_total':sum(catalog.values()),'by_cote':summary,'TOPIC_count_corrections':'VII numeric Codex column says56 but105 scans are supplied; VIII/IX say0 but126/138 are supplied. The explicit folder lists are complete and are used as the coverage authority.','cover_note':'The Pro package includes two institutional cover/logo pages as scan1; they are not extra mathematical manuscript pages.'}
(R/'audit/coverage_summary.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
