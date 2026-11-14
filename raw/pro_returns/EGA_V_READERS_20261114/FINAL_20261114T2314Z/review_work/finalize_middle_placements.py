"""Commit individually inspected line-placement and encoding amendments.

The candidate diffs and affected scan locations were reviewed before this file
was run. This script adds decision records and does not aggregate team records.
"""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_record import save
root=Path(__file__).resolve().parents[1]

def commit(site,text,extra,note):
 key=f'ega25_25_{site:03}'
 rec=json.loads((root/'review_work'/(key+'.json')).read_text())
 rows=[{k:v for k,v in d.items() if k!='id'} for d in rec['decisions']]
 rows.extend(extra)
 for d in rows:
  if d['before']==d['image'] and d['decision']=='corrected_from_scan':
   d['decision']='confirmed';d['category']='visual_check'
   d['reason']='The encoded reading itself remains unchanged. '+d['reason']
 return save(key,text,rows,rec['lines_read'],rec['visual_notes']+' '+note)

reasons={
64:'Reopened lower scan confirms the two distinct handwritten isomorphism signs and the dual mark on the following P line. The earlier replacement selected an already edited occurrence; this amendment restores the source-line target stated in the original decision.',
66:'Reopened lower scan and enlarged second connector confirm a handwritten arrow in each display. The earlier replacement nested the second hand tag at the first arrow; this amendment restores the declared second-display target.',
68:'Reopened lower scan confirms the three separate handwritten less-or-equal signs. The earlier replacements nested their hand tags on the first sign; this amendment distributes them to the source lines recorded in the original decisions.',
76:'Reopened upper scan confirms the additional w-like impression in the live quasi-projectif on source line13. The cancelled occurrence on line12 does not receive this reading; this amendment restores the recorded line target.',
107:'Reopened both scan parts confirms typed cancellation after rela on source line11 and a pen-plus-typewriter cancellation after sous-foncteur on source line27. This amendment restores the distinction and the original recorded target.'}
for site,reason in reasons.items():
 key=f'ega25_25_{site:03}'
 old=(root/'checked_pages'/(key+'.tex')).read_text()
 new=(root/'review_work/placement_candidates'/(key+'.tex')).read_text()
 if old==new:continue
 a,b=old.splitlines(),new.splitlines()
 assert len(a)==len(b)
 rows=[dict(line=i,before=x,image=y,decision='corrected_placement',reason=reason,category='placement_correction') for i,(x,y) in enumerate(zip(a,b),1) if x!=y]
 commit(site,new,rows,'Recorded line-target placements rechecked against the scans and corrected; see placement_correction decisions.')

for site,old_fragment,new_fragment,line in [(114,r'l\textquotesingle exempl',"l'exempl",19),(120,r'l\textquotesingle ensemble',"l'ensemble",8)]:
 key=f'ega25_25_{site:03}'
 old=(root/'checked_pages'/(key+'.tex')).read_text()
 if old_fragment not in old:continue
 rows=[dict(line=line,before=old_fragment,image=new_fragment,decision='encoding_adjusted',reason='Use a literal apostrophe for the same scanned character sequence; this is an encoding change and adds no letter or word space.',category='encoding_adjustment')]
 commit(site,old.replace(old_fragment,new_fragment),rows,'The apostrophe is encoded literally, with no change of reading.')

site=98;key='ega25_25_098'
old=(root/'checked_pages'/(key+'.tex')).read_text()
before=r'\margin{98}';after=r'\margin{\unsure{$\backslash$|1}}\margin{98}'
if after not in old:
 rows=[dict(line=43,before=before,image=after,decision='corrected_from_scan',reason='A reopened enlargement of the full lower edge shows a separate short curved descending pen stroke below the arrow terminal. Backslash-like mark and numeral1 remain possible; its graphic presence is now explicit without assigning a function.',category='reading_change')]
 commit(site,old.replace(before,after),rows,'The separate short lower pen mark was re-enlarged and recorded explicitly with uncertainty.')
print('Committed inspected placement amendments and encoding cleanup.')
