"""Supersede early arrow-provenance judgments after cross-page image comparison.

Run after the original Brown review scripts. This is an explicit second visual
review, not an automatic classifier. The old decisions remain in the ledger,
labelled as withdrawn; the changes below record every revised rendering.
"""
from pathlib import Path
import csv
from review_root import FIELDS,macro_occurrences
P=Path(__file__).resolve().parents[1]
changes={
'brown_134-2_119':[(r'\hand{\longrightarrow}',r'\longrightarrow','The compact repeated arrow-key head matches the small typed arrows, unlike the large freehand equivalences on site 118.')],
'brown_134-2_123':[
 (r'\underset{\hand{\longrightarrow}}{\ell im}',r'\underset{\unsure{\longrightarrow|\hand{\longrightarrow}}}{\ell im}','The arrow is probably a typed head with an underline shaft, but the enlarged image and independent inspection do not securely exclude pen retouch. Retain explicit provenance alternatives.'),
 (r'\underset{\hand{\longleftarrow}}{\ell im}',r'\underset{\unsure{\longleftarrow|\hand{\longleftarrow}}}{\ell im}','The second limit arrow has the same residual provenance uncertainty; its direction is clear.'),
 (r'\hand{\xrightarrow{\ \textcolor{black}{\phi}\ }}',r'\xrightarrow{\ \phi\ }','The small repeated head matches the typewriter arrow glyph, with a separate straight shaft; no positive pen correction is visible.'),
 (r'\hand{\longrightarrow} \tau_1',r'\longrightarrow \tau_1','The regular compact arrowhead matches the typed arrows elsewhere in this copy.'),
 (r'u \hand{\longmapsto}',r'u \longmapsto','The bar, straight shaft and compact arrow-key head match the assembled typewriter mapsto on site 136; the earlier hand claim is withdrawn.'),
 (r'T \hand{\longmapsto}',r'T \longmapsto','The small mapsto has the same regular typewriter construction; no handwritten replacement is established.')],
'brown_134-2_124':[
 (r'\hand{\xrightarrow{\ \textcolor{black}{F}\ }}',r'\xrightarrow{\ F\ }','Independent enlarged comparison finds the same compact key-like arrowhead as the typed arrows on sites 130 and 133.'),
 (r'\mathbb{C}(\Gamma_X F) \hand{\longrightarrow}',r'\mathbb{C}(\Gamma_X F) \longrightarrow','The final comparison uses the same small regular arrow glyph and underline-like shaft.')],
'brown_134-2_125':[
 (r'C_{n+1} \hand{\xrightarrow{\textcolor{black}{F}}}',r'C_{n+1} \xrightarrow{F}','The first F-labelled arrow has a compact typewriter head, independently confirmed against the comparison crop.'),
 (r'C \hand{\xrightarrow{\textcolor{black}{F}}}',r'C \xrightarrow{F}','The second F-labelled arrow has the same regular construction and is restored to plain typing.')],
'brown_134-2_126':[
 (r'C_{n+1} \hand{\longrightarrow} D_{n+1}',r'C_{n+1} \longrightarrow D_{n+1}','The compact arrow-key head matches the other small typed arrows.'),
 (r'C_n \hand{\longrightarrow} D_n',r'C_n \longrightarrow D_n','The second arrow has the same repeated head and separate underline-like shaft.'),
 (r'((n-1)\text{-Cat})) \hand{\longrightarrow} \mathit{Hom}',r'((n-1)\text{-Cat})) \longrightarrow \mathit{Hom}','The short Hom comparison uses the same small typewriter arrow form.'),
 (r'D_{n+1} \hand{\longrightarrow} (n\text{-Cat})',r'D_{n+1} \longrightarrow (n\text{-Cat})','The local-system arrow likewise has the compact repeated typed head.')],
'brown_134-2_130':[
 (r'L_1 \mathrel{\overset{d}{\hand{\longrightarrow}}} L_0',r'L_1 \xrightarrow{\ d\ } L_0','Cross-page comparison and independent inspection establish a typed short arrowhead joined to a separate underline shaft; the earlier hand classification was too strong.'),
 (r'L_0 \hand{\longrightarrow} \mathrm{Aut}',r'L_0 \longrightarrow \mathrm{Aut}','The second arrow has the same tiny typed head and stepped join as the first and as the limit arrows on site 133.')]
}
old=r'''\begin{tikzcd}
\mathit{Hom}(e_n^{D_{n+1}}, F) \arrow[r,color=blue] \arrow[d, equal, "\text{def.}",color=blue] & \mathit{Hom}(e_n^{C_{n+1}}, f^{*}_{n+1} F) \arrow[d, equal, "\text{def.}",color=blue] \\
\Gamma_{D_{n+1}}(F) & \Gamma_{C_{n+1}}(F)
\end{tikzcd}'''
new=r'''\begin{tikzcd}[row sep=small]
\mathit{Hom}(e_n^{D_{n+1}}, F) \arrow[r,phantom,"{\unsure{\longrightarrow|\hand{\longrightarrow}}}" description] & \mathit{Hom}(e_n^{C_{n+1}}, f^{*}_{n+1} F) \\
\unsure{\Vert|\hand{\Vert}}\;\text{def.} & \unsure{\Vert|\hand{\Vert}}\;\text{def.} \\
\Gamma_{D_{n+1}}(F) & \Gamma_{C_{n+1}}(F)
\end{tikzcd}'''
changes['brown_134-2_126'].append((old,new,'The long arrow shaft and the two vertical equalities cannot be securely assigned to pen or assembled typing. Independent inspection favors typing but does not settle the provenance. Keep all three as explicit typed/hand alternatives; the labels, objects, arrow direction, and vertical equalities are unchanged.'))
ledger=P/'records/CHECK_DECISIONS_134_2.tsv';rows=list(csv.DictReader(ledger.open(),delimiter='\t'))
newrows=[]
for key,items in changes.items():
 p=P/'checked_pages'/f'{key}.tex';s=p.read_text()
 for i,(before,after,reason) in enumerate(items,1):
  sid=f'RECHECK:{key}:arrow:{i}'
  if any(r['source_id']==sid for r in rows):continue
  assert s.count(before)==1,(key,i,s.count(before))
  line=s.count('\n',0,s.find(before))+1;s=s.replace(before,after,1)
  for r in rows:
   if r['key']==key and r['image_reading']==before and r['decision']=='our transcription corrected':
    r['decision']='superseded visual judgment';r['reason']='Withdrawn by '+sid+'. Earlier judgment: '+r['reason']
  newrows.append(dict(key=key,cote='134-2',site=key[-3:].lstrip('0'),line=line,transcription_reading=before,image_reading=after,arxiv_reading='',decision='provenance reassessed',reason=reason,source_id=sid))
 p.write_text(s)
 note=P/'review_notes'/f'{key}.txt';text=note.read_text();text+='\nPROVENANCE REASSESSMENT (supersedes earlier arrow statements):\n'+'\n'.join(r['source_id']+': '+r['reason'] for r in newrows if r['key']==key)+'\n';note.write_text(text)
with ledger.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=FIELDS,delimiter='\t');w.writeheader();w.writerows(rows+newrows)
p=P/'records/PAGE_REVIEW_134_2.tsv';r=list(csv.DictReader(p.open(),delimiter='\t'))
for row in r:
 if row['key'] in changes:
  s=(P/'checked_pages'/(row['key']+'.tex')).read_text();row['issues_remaining']=sum(len(macro_occurrences(s,m)) for m in ['unsure','illegible'])
  if 'PROVENANCE REASSESSMENT' not in row['notes']:row['notes']+=' PROVENANCE REASSESSMENT supersedes the earlier confident hand-arrow statements; see RECHECK rows and the comparison crops.'
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=r[0].keys(),delimiter='\t');w.writeheader();w.writerows(r)
print({'revised_arrow_decisions':len(newrows)})
