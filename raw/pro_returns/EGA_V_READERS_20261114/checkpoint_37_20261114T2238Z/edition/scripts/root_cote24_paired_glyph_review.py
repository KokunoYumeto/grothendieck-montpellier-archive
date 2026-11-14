"""Supersede initial Greek-baseline judgments after actual paired enlarged views.
Run after root_audit24_004_005, _006_007 and _008_010 if reproducing the audit.
The saved page records are the source of record; this is a documented amendment.
"""
from pathlib import Path
import csv,json
from audit_record import save,aggregate
from root_review_support import ReviewedPage
ROOT=Path(__file__).resolve().parents[1]
ledger=ROOT/'records/VISUAL_DECISION_SUPERSESSIONS.tsv'
rows=list(csv.DictReader(ledger.open(),delimiter='\t')) if ledger.exists() else []
for n in (4,5,6,7,9,10):
 key=f'ega24_24_{n:03}';j=ROOT/'review_work'/f'{key}.json';o=json.loads(j.read_text())
 if any(d.get('category')=='paired-glyph-review' for d in o['decisions']):continue
 p=ReviewedPage((ROOT/'checked_pages'/f'{key}.tex').read_text())
 eligible=[]
 for d in o['decisions']:
  if d.get('category')=='reading-change' and ('\\xi' in d['before'] or '\\eta' in d['before']) and ('_\\' in d['before'] or '_{' in d['before']) and d['image']==d['before'].replace('_{\\xi}',r'\xi').replace('_{\\eta}',r'\eta').replace('_\\xi',r'\xi').replace('_\\eta',r'\eta'):
   eligible.append(d)
 pairs=[]
 for d in eligible:
  pair=(d['image'],d['before'])
  if pair not in pairs:pairs.append(pair)
 for before,after in pairs:
  p.change(before,after,'Paired magnified views compare the attached Greek glyph with its standalone form on the same page or adjacent repeated typewriting. The attached form is visibly lowered despite retaining full character size. This supersedes the initial full-page baseline interpretation.','index-placement-restored')
 if n==5:
  p.change(r'H$\xi$',r'H$_{\xi}$','The enlarged same-line pair formation of Hxi from xi shows the attached xi lower than the standalone xi. Its full size alone had obscured this displacement in the draft.','index-placement-corrected')
  for d in o['decisions']:
   if d['line']=='NOTES item3':
    d['decision']='superseded-after-enlargement'
    d['reason']='The -1 observation remains; the xi placement statement is superseded by the paired-glyph review appended below.'
 for d in eligible:
  d['decision']='superseded-after-enlargement'
  d['reason']+=' Subsequent paired enlarged inspection showed a real downward displacement. See the appended paired-glyph-review decision; this initial judgment is not the final reading.'
 for d in o['decisions']:
  if n==9 and d['line']=='NOTES item2':
   d['image']='Eta, xi and phi are regular typed glyphs. Paired magnified views establish a lower level for attached eta/xi; the original subscripts are restored.'
   d['reason']='Paired magnification supersedes the initial placement interpretation; the typing-layer judgment is unchanged.'
 new=[]
 for d in p.decisions:d['category']='paired-glyph-review';new.append(d)
 p.note('paired enlarged comparison','Full-size Greek letters interpreted as baseline','Attached xi or eta is lower than the standalone glyph; full character size and vertical placement were assessed separately.','review-revised','The full pages were already read. This targeted second inspection corrects the stated placement judgments without changing any letter, word, query or mathematical sign.','paired-glyph-review')
 new=p.decisions
 old=[{k:v for k,v in d.items() if k!='id'} for d in o['decisions']]
 saved=save(key,p.text,old+new,0,o['visual_notes']+' Follow-up: paired enlarged Greek glyphs establish the actual lowered attachments; initial contrary decisions are explicitly superseded.')
 for d in eligible:
  matches=[nd for nd in saved['decisions'][len(old):] if nd['before']==d['image'] and nd['image']==d['before']]
  match=next((nd for nd in matches if nd['line']==d['line']),matches[0] if matches else None)
  rows.append(dict(key=key,superseded_decision=d['id'],final_decision=match['id'] if match else saved['decisions'][-1]['id'],reason='Paired enlarged Greek glyph comparison establishes a real lower placement.'))
with ledger.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['key','superseded_decision','final_decision','reason'],delimiter='\t');w.writeheader();w.writerows(rows)
print(aggregate())
