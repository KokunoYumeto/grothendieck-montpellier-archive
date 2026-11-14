"""Save the complete visual comparison of cote24 sites11--13."""
from pathlib import Path
import csv
from audit_record import source_path,save,aggregate
from root_review_support import ReviewedPage
ROOT=Path(__file__).resolve().parents[1]
notes={r['key']:r['notes'].split(' | ') for r in csv.DictReader((ROOT.parent/'source/transcription/ega_v_cote24_blass/NOTES.tsv').open(),delimiter='\t')}
for n in (11,12,13):
 key=f'ega24_24_{n:03}';p=ReviewedPage(source_path(key).read_text())
 if n==11:
  observations=[
   'All four subset signs have uneven, thick pen strokes within typed blank spaces; each inclusion reading and hand layer is confirmed.',
   'The printed string is f(Z1), with the numeral1 at full height. It is not a prime, and remains literal.',
   'The cap forms are visibly low relative to the neighboring capitals. They remain cap glyphs; no extra letter or index is inferred from the type-element placement.',
   'The folio11 is regular serif printing with no pen addition.',
   'The tiny right-margin traces are isolated specks without a securely readable character or assigned textual function; no word or symbol is invented.',
   'There is no long handwritten passage, only the four inclusion signs.'
  ]
  p.note('9--37','Complete Corollaries2.4--2.5 and proof','Every word, formula, prime, numeral1, cap, overline, underline and inclusion was read against both halves. The enlarged index crop confirms the actual lower placement of i and eta.','confirmed','No reading change is required; the literal unclosed proof parenthesis and the final dimension equality are retained.','full-text')
  p.note('15','f(Z1)','French counterpart at cote25/site9 is f(Z prime). The English numeral1 remains unchanged.','comparison-recorded','The source comparison identifies the difference without normalizing a typed1 to a prime.','cote24-comparison')
  p.note('32','non-empty subsets of underlined Y','Blass underlines Y here; the corresponding French cote25/site9 has unadorned Y.','comparison-recorded','Both visible underline scopes are preserved.','cote24-comparison')
 elif n==12:
  observations=[
   'The folio12 is regular serif printing; no handwritten addition is visible.',
   'The star after par.3 is the regular typed asterisk. The star and the complete question at the foot are penned.',
   'The short underline below Y in the conclusion of2.6 is regular typing; eta is lower than the standalone eta in k(eta), as the paired crops confirm.',
   'The three overlines above f(X_i), f(X), and f(Z_i) are straight regular typed rules, each at the indicated span.',
   'The upper-left spots contain no recoverable character or notation.',
   'The single-line handwritten footnote is short and was read in full.'
  ]
  p.note('7--38','Complete Propositions2.6--2.7 opening and footnote','All prose, indices, relations, bars and punctuation were compared, including the oddly paired brackets in slightly illegible)(Ask AG), quasi coherent without a hyphen, and the literal same or among.','confirmed','Both full images and the paired eta crops were read. The original subscript placement is supported by the magnification.','full-text')
  p.note('11','[slightly illegible)(Ask AG)]','French counterpart: cote25/site9, the handwritten alternative ou que f soit une immers. et dim overline f(X)>0 in2.6.','cross-reference','The translator’s exact query and punctuation remain; the French locates the queried insertion.','cote24-crossreference')
  p.note('25','reference needed for the last equality','French counterpart: cote25/site10, the handwritten (réf) in the dimension-equality line.','cross-reference','The English placement of the request after the last equality is preserved; the French marker lies before the equality to dim X-1.','cote24-crossreference')
  p.note('36--38','par.3*; Ask Grothendieck about this reference.','French counterpart: cote25/site10, il résulte du par.3 in the proof of2.7.','cross-reference','The typed asterisk and the complete penned query are retained.','cote24-crossreference')
  p.note('13','dim underlined Y eta','The English conclusion of2.6 underlines Y; French cote25/site9 has Y eta without an underline.','comparison-recorded','The visible underline difference is retained.','cote24-comparison')
 else:
  observations=[
   'The first Y has a clear short overline and no underline. The source encoding is retained.',
   'A separate regular typed v-shaped mark is centered above the underlined P. The check-above-P representation retains this observed placement and no pen macro is added.',
   'No handwriting appears; the small upper-left mark has no readable character.',
   'No long handwritten passage is present.'
  ]
  p.note('7--40','Complete end of2.7 and Proposition2.8','Every line, the literal (2), the two printed illegible placeholders, all five properties, the four (ref) strings, capital N, H eta, and both local-ring indices were read against both full halves.','confirmed','The visible H and capital N are retained as typed; no mathematical repair is substituted.','full-text')
  p.note('17','underlined illegible; [illegible ask AG.]','French counterpart: cote25/site10, the handwritten remarque analogue pour la doubtful dim.|dém. de2.doubtful1.','cross-reference','The checked French itself retains doubt in this phrase; no answer is inserted in the English placeholders.','cote24-crossreference')
  for where,english,french in [('25','coprof M <= N (ref)','(i) coprof M <= n (réf)'),('27','M satisfies (S_k) (ref)','(ii) M satisfait (S_k) (réf)'),('31','M is reduced (ref)','(iv) M est réduit followed by the doubtful handwritten réf|vif'),('33','M is integral (ref)','(v) M est intègre followed by the doubtful handwritten réf|vif')]:
   p.note(where,english,'French counterpart: cote25/site11, '+french+'.','cross-reference','The placeholder reference is retained; the source site identifies the precise list item.','cote24-crossreference')
  p.note('38','paragraph6*','French counterpart: cote25/site11, résultats du par.6 in the proof of2.8. No footnote answering the star appears on English site13.','cross-reference','The literal starred reference remains; no bibliographical completion is invented.','cote24-crossreference')
  p.note('25','coprof M <= N','Blass types a capital N; French cote25/site11 types a lowercase n.','comparison-recorded','The letter case is visible and is preserved in each witness.','cote24-comparison')
  p.note('35','H eta satisfies the property','Blass types H with eta. The corresponding French cote25/site11 has a doubtful E|F with eta,y indices, not an H reading.','comparison-recorded','The English H and the French uncertainty are both retained; the guide records the mismatch without supplying a mathematical correction.','cote24-comparison')
 assert len(observations)==len(notes[key]),(key,len(observations),len(notes[key]))
 for i,(before,seen) in enumerate(zip(notes[key],observations),1):p.note(f'NOTES item{i}',before,seen,'checked','This concern was individually examined during the full scan comparison.','NOTES')
 text,decisions=p.finish();save(key,text,decisions,0,'Both complete scan halves read line by line, including every index and bar, all handwritten signs/notes, and the relevant enlarged index comparisons.')
print(aggregate())
