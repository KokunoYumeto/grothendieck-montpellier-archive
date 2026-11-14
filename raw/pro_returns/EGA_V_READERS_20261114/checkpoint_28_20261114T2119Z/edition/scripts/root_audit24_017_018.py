"""Record complete visual review of cote24 sites17--18."""
from pathlib import Path
import csv
from audit_record import source_path,save,aggregate
from root_review_support import ReviewedPage
ROOT=Path(__file__).resolve().parents[1]
notes={r['key']:r['notes'].split(' | ') for r in csv.DictReader((ROOT.parent/'source/transcription/ega_v_cote24_blass/NOTES.tsv').open(),delimiter='\t')}
for n in (17,18):
 key=f'ega24_24_{n:03}';p=ReviewedPage(source_path(key).read_text())
 if n==17:
  observations=[
   'The folio17 is regular serif printing; the mspage content is correct.',
   'The penned note reads * Ask Grothendieck with no final point. Two typed6* occurrences share its asterisk, so the draft statement that nothing refers to it is too strong. No further pointer selects just one of them; both reference contexts are recorded.',
   'Every eta has regular repeated type-element contours. No eta on this page is handwritten; their attached placements are lower than their standalone forms in k(eta).',
   'The handwritten question is short; no long handwritten passage appears.'
  ]
  p.note('7--35','Complete end of2.14, Corollary2.15, editorial paragraph, and start of2.16','All words, formula characters, indices, references and the handwritten question were read in both full images.','confirmed','The literal k(y), capital K(eta), and absence of geometrically before the first normal are preserved.','full-text')
  p.note('8','first par.6*','French counterpart: cote25/site13, compte tenu du par.6 in the proof of2.14.','cross-reference','The first starred reference is recorded separately; the handwritten Ask Grothendieck query remains.','cote24-crossreference')
  p.note('14','reference par.6*','French counterpart: cote25/site14, par raison de platitude (réf par.6).','cross-reference','The second starred reference has its own French location; no answer is supplied.','cote24-crossreference')
  p.note('7','k(y) in the equivalence','French cote25/site13 has k(eta) in the handwritten equivalence. The English letter inside these parentheses is a clear Latin y.','comparison-recorded','Both explicit formulas remain as written.','cote24-comparison')
  p.note('12','K(eta)','French cote25/site14 has lowercase k(eta) here; Blass types capital K.','comparison-recorded','The case difference is recorded without alteration.','cote24-comparison')
  p.note('21','is not normal over k','French cote25/site14 has a typed insertion géom before normal in the hypothesis list. The English hypothesis omits it, although its conclusion says geometrically normal.','comparison-recorded','The observed missing qualification is reported in the guide, not supplied in the text.','cote24-comparison')
  p.note('Theorem2.14 across16--17','No introductory unramified/characteristic-zero qualification','The French margin at cote25/site13 reads doubtful un ramifié|non ramifié ou k de car0 beside2.14. No corresponding marginal hypothesis occurs in the English statement on16 or its continuation on17.','comparison-recorded','Both complete English pages and the checked French marginal reading were compared; the French doubt remains unresolved.','cote24-comparison')
 else:
  observations=[
   'The small upper-left dots are isolated marks without readable lettering; the margins and blank lower region were viewed.',
   'Eta and the Greek arguments in k(eta) have regular type-element outlines. Their attached lower placement is retained, with no handwriting macro.',
   'There is no long handwritten passage and no handwritten body text on this page.'
  ]
  p.note('7--35','Complete continuation of2.16, Corollary2.17 and Remark2.18','Every line, two distinct PB queries, typed stars, indices, hyphenation, reference and underline was read against both full halves.','confirmed','The phrases not be immersed and devissage (unscrewing), and the two endpoint conjunctions and in2.18, remain Blass’s actual words.','full-text')
  p.note('7--8','[PB incomprehensible].*','French counterpart: cote25/site14, pour que Z_i soit non immergé, il f et s que Z_i le soit. The checked French also repeats Z_i in this sentence.','cross-reference','The comparison does not invent an eta index or repair the translator’s question.','cote24-crossreference')
  p.note('16--17','[PB: incomprehensible].*','French counterpart: cote25/site14, se réduire au cas k alg clos, followed by the typed insertion alors X est séparable sur k.','cross-reference','The English clause orders separability and reduction differently and remains as typed with the query.','cote24-crossreference')
  p.note('23','k (reference)','French counterpart: cote25/site15, F n’est pas séparable sur k (réf) in2.17.','cross-reference','The placeholder reference remains incomplete.','cote24-crossreference')
  p.note('10','multiplicity...at Z_i at k...at Z_i relative to k(eta)','The English has Z_i in both multiplicity positions, as does the checked French cote25/site14.','comparison-recorded','No extra eta is inferred from mathematical expectation.','cote24-comparison')
  p.note('29--35','2.13 and2.17;2.12 and2.17','French cote25/site15 uses the ranges2.13 à2.17 and2.12 à2.17. Blass types and between the endpoints in both places.','comparison-recorded','The English conjunctions are retained; the range difference is described in the guide.','cote24-comparison')
 assert len(observations)==len(notes[key]),(key,len(observations),len(notes[key]))
 for i,(before,seen) in enumerate(zip(notes[key],observations),1):p.note(f'NOTES item{i}',before,seen,'checked','This concern was independently checked against the full page images.','NOTES')
 text,decisions=p.finish();save(key,text,decisions,0,'Every line in both full scan halves was read, including every reference/query, formula, index and the handwritten question on17.')
print(aggregate())
