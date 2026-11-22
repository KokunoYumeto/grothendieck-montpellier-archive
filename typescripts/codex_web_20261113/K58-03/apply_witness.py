#!/usr/bin/env python3
"""Render the recorded witness decisions and prove every unmarked span is unchanged.

By default this command verifies the final files. Pass --apply to reconstruct
the final files from the separately stored frozen text and the decisions.
"""
from collections import Counter
from pathlib import Path
import csv,hashlib,argparse,re
from tex_elements import arguments
root=Path(__file__).resolve().parent
def tsv(path):
 with path.open() as f:return list(csv.DictReader(f,delimiter='\t'))
def esc(s):return s.replace('|',r'\|').replace('\n',' ')
def code(s):return chr(96)+esc(s)+chr(96)
def run(apply):
 rows=tsv(root/'audit/witness_places.tsv')
 seen=set();frozen=tsv(root/'audit/frozen_places.tsv')
 assert [r['id'] for r in rows]==[r['id'] for r in frozen]
 checksums={p:h for h,p in (line.split('  ',1) for line in (root/'audit/frozen.sha256').read_text().splitlines())}
 oldfiles=[];finalfiles=[];unchangedbytes=0
 for path in sorted((root/'pages').glob('*.tex')):
  old=(root/'audit/frozen_pages'/path.name).read_bytes()
  assert hashlib.sha256(old).hexdigest()==checksums['pages/'+path.name],path
  oldfiles.append(old);t=old.decode();marks=list(arguments(t,{'unsure','illegible'}))
  rr=[r for r in rows if int(r['scan'])==int(path.stem[-3:])]
  assert len(marks)==len(rr)
  pos=0;parts=[]
  for (a,b,typ,val),r in zip(marks,rr):
   assert r['frozen reading']==val and r['id'] not in seen
   seen.add(r['id']);result=r['result'];replacement=r['replacement or new alternatives']
   if result=='changed':new=replacement
   elif result=='alternative added':new='\\unsure{'+val+'|'+replacement+'}'
   elif result in {'unchanged','uncovered'}:new=t[a:b]
   else:raise ValueError(result)
   unchangedbytes+=len(t[pos:a].encode())
   parts.extend([t[pos:a],new]);pos=b
  parts.append(t[pos:]);unchangedbytes+=len(t[pos:].encode())
  with_changes=''.join(parts).encode();finalfiles.append(with_changes)
  if apply:path.write_bytes(with_changes)
  else:assert path.read_bytes()==with_changes,path
 assert hashlib.sha256(b''.join(oldfiles)).hexdigest()==checksums['K58-03_transcription.tex']
 assert seen=={r['id'] for r in rows}
 if not apply:assert (root/'K58-03_transcription.tex').read_bytes()==b''.join(finalfiles)
 if apply:
  p=root/'K58-03_doubts.md'
  pre=p.read_text().split('\n## Witness check')[0].rstrip()
  # Update the reference to the best tight crop in each local entry.
  lines=pre.splitlines()
  byid={r['id']:r for r in rows}
  for i,line in enumerate(lines):
   m=re.match(r'^\| (\d+\.\d+[a-z]?) \|',line)
   if m:
    row=byid[m[1]];lines[i]=re.sub(r'\x60\d{3}_[A-Za-z0-9_]+\.png\x60',lambda _:code(row['comparison crop']),line,count=1)
  pre='\n'.join(lines)
  report=['','## Witness check','',
   'The manuscript scan is one greater than the archival page cited by Hua. Thus Lemme 4 on scan 21 is page 20 of batch-01, and the two-row diagram on scan 35 is page 34 of batch-02. The cover (scan 28) appears as a section heading for archival page 27. Batch-02 skips the typed archival pages 21, 23 and 25. Of these leaves only scan 22 has a frozen doubt. The other typed leaves have no eligible place. An illegible placeholder or an omitted cancellation in Hua supplies no candidate.',
   '',
   'Each row compares one pre-existing mark. The evidence column names the enhanced crop used for the final comparison. A retained candidate may agree with Hua and still remain doubtful on the page. When an abbreviation is legible, the transcription keeps its written form. The unchanged-scope check rebuilds each page from the frozen bytes plus the listed substitutions.',
   '',
   '| Scan / place | Location | Frozen reading | Witness | Ink on the comparison crop | Result |',
   '|---|---|---|---|---|---|']
  for r in rows:
   outcome=r['result'];addition=r['replacement or new alternatives']
   if addition:outcome+=' → '+code(addition)
   witness=('Hua '+r['witness file']+' reads '+r['witness account'] if r['result']!='uncovered' else 'Hua '+r['witness file']+' states that '+r['witness account'])
   report.append('| '+' | '.join([r['id'],esc(r['location']),code(r['frozen reading']),esc(witness),code(r['comparison crop'])+'. '+esc(r['ink on reinspection']),outcome])+' |')
  p.write_text(pre+'\n'+'\n'.join(report)+'\n')
 counts=Counter(r['result'] for r in rows)
 print(f"{len(rows)} frozen places; {len(seen)-counts['uncovered']} covered; {counts['changed']} changed; {counts['alternative added']} places with alternatives added; {counts['unchanged']} unchanged on comparison; {counts['uncovered']} on an uncovered page.")
 print('New alternative candidates:',sum(len(r['replacement or new alternatives'].split('|')) for r in rows if r['result']=='alternative added'))
 print(f'All {unchangedbytes} bytes outside frozen marks match across the 15 pages.')
if __name__=='__main__':
 parser=argparse.ArgumentParser()
 parser.add_argument('--apply',action='store_true');run(parser.parse_args().apply)
