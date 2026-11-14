"""Add explicit TeX spaces at reviewed whole-word insertion boundaries.

This repairs rendering only.  Prefixes, suffixes and note calls are excluded.
Run after the page-review batches; each repair is appended to its page evidence.
"""
import re,json,sys
from pathlib import Path
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review
out=Path('PS_READERS_WORK')
joined={'co','Hot-','``','ly','ly small in any case.)',r'\hand{-}test','to','0-',',','I=','en','h'}
changed=[]
for p in sorted((out/'checked_pages').glob('ps_134-[34]_*.tex')):
 q=out/'review_notes'/f'{p.stem}.json'
 if not q.exists():continue
 c=json.loads(q.read_text());s=p.read_text();added=[]
 while True:
  fix=None
  for m in re.finditer(r'\\inserted(?:\[[^\]]*\])?\{',s):
   j=m.end();level=1
   while level:
    if s[j]=='{' and s[j-1]!='\\':level+=1
    elif s[j]=='}' and s[j-1]!='\\':level-=1
    j+=1
   body=s[m.end():j-1]
   if body in joined or re.fullmatch(r'\(\d+\)',body):continue
   before=s[m.start()-1] if m.start() else ' ';after=s[j] if j<len(s) else ' '
   left=before.isalpha();right=after.isalpha()
   if not(left or right):continue
   a=max(0,m.start()-1);b=min(len(s),j+1)
   while s.count(s[a:b])!=1:a=max(0,a-20);b=min(len(s),b+20)
   old=s[a:b];new=s[a:m.start()]+(' ' if left else '')+s[m.start():j]+(' ' if right else '')+s[j:b]
   fix=[old,new,'Mechanical spacing: preserve a literal word boundary around this whole-word insertion so the applied reading cannot concatenate adjacent words. No source wording or layer changed.'];break
  if fix is None:break
  added.append(fix);s=s.replace(fix[0],fix[1],1)
 extras={
 'ps_134-3_035':[(r'\xout{quasi}\inserted[typed]{weak}',r'\xout{quasi} \inserted[typed]{weak}')],
 'ps_134-3_068':[(r'\inserted{$\mathcal{A}$}\hand{/}such',r'\inserted{$\mathcal{A}$} \hand{/} such'),(r'\inserted[typed]{a}\hand{/}locally',r'\inserted[typed]{a} \hand{/} locally')]
 }
 for old,new in extras.get(p.stem,[]):
  if old in s:
   assert s.count(old)==1;s=s.replace(old,new);added.append([old,new,'Mechanical spacing: separate the inserted whole word from the neighbouring deleted word or pen placement slash; preserve the source content.'])
 if added:
  c['edits'].extend(added);c['evidence']+=' A later mechanical pass added explicit spaces at '+str(len(added))+' whole-word insertion boundary/placement spans; prefixes, suffixes and note calls remain joined.'
  save_review(c);changed.append((p.stem,len(added)))
print('spacing repairs',sum(n for _,n in changed),'on',len(changed),'pages')
