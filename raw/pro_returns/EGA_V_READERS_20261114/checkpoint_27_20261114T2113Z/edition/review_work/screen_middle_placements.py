"""Compare recorded visual changes with their declared source-line locations.

Creates review candidates only; does not alter checked pages or attest a review.
"""
import json,difflib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
out=Path(__file__).parent/'placement_candidates'
out.mkdir(exist_ok=True)
report=[]
for site in range(55,125):
 key=f'ega25_25_{site:03}'
 rec=json.loads((root/'review_work'/(key+'.json')).read_text())
 s=(root.parent/'source/transcription/ega_v_cote25/pages'/(key+'.tex')).read_text()
 origins=[i for i,l in enumerate(s.splitlines(keepends=True),1) for _ in l]
 touched=[False]*len(s)
 applied=[]
 for d in rec['decisions']:
  if d.get('category') not in ('reading_change','encoding_adjustment'):continue
  before,after,line=d['before'],d['image'],int(d['line'])
  starts=[];start=0
  while True:
   at=s.find(before,start)
   if at<0:break
   starts.append(at);start=at+1
  if not starts:
   report.append(f'{key}: missing {d["id"]} {before!r}')
   continue
  at=min(starts,key=lambda x:(abs(origins[x]-line),sum(touched[x:x+len(before)]),x))
  applied.append((d['id'],line,origins[at],before))
  s=s[:at]+after+s[at+len(before):]
  origins[at:at+len(before)]=[origins[at]]*len(after)
  touched[at:at+len(before)]=[True]*len(after)
 s=s.replace('not yet checked by eye.','checked against both supplied scan parts; see CHECK_DECISIONS.tsv.')
 cur=(root/'checked_pages'/(key+'.tex')).read_text()
 if s!=cur:
  (out/(key+'.tex')).write_text(s)
  diff=''.join(difflib.unified_diff(cur.splitlines(True),s.splitlines(True),fromfile=key+' checked',tofile=key+' line-targeted'))
  (out/(key+'.diff')).write_text(diff)
  report.append(f'{key}: candidate differs, {len(diff.splitlines())} diff lines')
 for did,want,got,before in applied:
  if want!=got:report.append(f'{key}: {did} declared{want} selected{got}: {before!r}')
(out/'report.txt').write_text('\n'.join(report)+'\n')
print('\n'.join(report))
