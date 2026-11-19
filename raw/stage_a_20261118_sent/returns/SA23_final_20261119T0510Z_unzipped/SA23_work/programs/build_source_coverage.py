#!/usr/bin/env python3
"""Inventory exact supplied files; owner assignments are explicit, not inferred verdicts."""
import json,csv,re,hashlib,collections
from pathlib import Path
W=Path(__file__).resolve().parents[1];S=Path('sources')
def owner(name):
 if name.startswith('MPL_22+23'):return 'ega'
 if name.startswith('MPL_2_'):return 'root'
 if name.startswith('MPL_68_'):return 'misc'
 if name.startswith('MPL_93_'):return 'bt'
 if name.startswith(('HC1-','K1-','K21-')):return 'analysis_curves'
 if name.startswith(('K22-','K23-','H26-')):return 'ega'
 if name.startswith(('K161-1-','K161-2-')):return 'groupes'
 if name.startswith(('K161-3-','K161-4-')):return 'spaces'
 if name.startswith('K161-5-'):return 'bt'
 if name.startswith('K161-6-'):return 'misc'
 if name.startswith(('K162-5-','tapis_de_quillen_162-5','ega_v_cote24')):return 'forms'
 if name.startswith('ega_v_cote25'):return 'hyperplanes'
 raise ValueError('No authored ownership assignment for '+name)
rows=[];leaves=collections.defaultdict(set)
for category,pattern in [('transcription','texts/**/*.tex'),('lead notes','notes/codex/*_notes.md'),('indexed notes','notes/pro/*_notes.md'),('doubts','notes/pro/*_doubts.md')]:
 for f in sorted(S.glob(pattern)):
  if f.name=='PREAMBLE.tex':continue
  o=owner(f.name);t=f.read_text();cote='';loc=[]
  for m in re.finditer(r'\\(cotefile|scanpage)\{([^{}]+)\}',t):
   typ,val=m.groups()
   if typ=='cotefile':cote=val
   else:
    if'/'in val:c,n=val.split('/',1)
    else:c,n=cote,val
    n=n.strip();loc.append((c,n));leaves[c].add(n)
  rows.append(dict(file=str(f),category=category,owner=o,lines=len(t.splitlines()),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),scan_markers=len(loc),cotes=sorted({c for c,_ in loc}),leaf_labels=[c+'/'+n for c,n in loc],reading_evidence=f'parts/{o}/coverage.md and the individually authored reading ledgers; the owner read the complete supplied text, including cancellations and duplicates.'))
(W/'outputs'/'source_coverage.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with(W/'SA23_source_coverage.tsv').open('w')as h:
 fs=['file','category','owner','lines','bytes','sha256','scan_markers','cotes','reading_evidence'];wr=csv.DictWriter(h,fieldnames=fs,delimiter='\t');wr.writeheader()
 for r in rows:wr.writerow({k:','.join(r[k])if isinstance(r[k],list)else r[k]for k in fs})
report={'files':len(rows),'transcriptions':sum(r['category']=='transcription'for r in rows),'indexed_notes':sum(r['category']=='indexed notes'for r in rows),'doubts':sum(r['category']=='doubts'for r in rows),'codex_notes':sum(r['category']=='lead notes'for r in rows),'transcription_lines':sum(r['lines']for r in rows if r['category']=='transcription'),'retained_scan_labels_by_cote':{k:len(v)for k,v in leaves.items()},'expected_catalogue_only_without_supplied_text':['162-1','162-6'],'extra_cotes_in_supplied_indexed_packages':['68','93'],'caution':'TOPIC model/page columns are catalogue packaging metadata, not proof of supplied text. Scan labels are retained transcription markers, not a new collation to manuscript images.'}
assert report['transcriptions']==45,report
assert report['codex_notes']==38,report
assert '162-1'not in leaves and'162-6'not in leaves,report
(W/'outputs'/'source_coverage_summary.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
