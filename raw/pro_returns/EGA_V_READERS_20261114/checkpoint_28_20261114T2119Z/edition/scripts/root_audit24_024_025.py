"""Save root's complete cote24 sites24--25 visual comparison."""
from pathlib import Path
import csv
from audit_record import source_path,save,aggregate
from root_review_support import ReviewedPage
ROOT=Path(__file__).resolve().parents[1]
notes={r['key']:r['notes'].split(' | ') for r in csv.DictReader((ROOT.parent/'source/transcription/ega_v_cote24_blass/NOTES.tsv').open(),delimiter='\t')}
for n in (24,25):
 key=f'ega24_24_{n:03}';p=ReviewedPage(source_path(key).read_text())
 if n==24:
  observations=[
   'Each underlined P is followed by a main-baseline lowercase v. The typed letter is retained without replacing it by a dual mark.',
   'The R subscript is a lowered lowercase k, visibly shorter than the capital K later on the same line.',
   'Both complete halves show no handwritten material. The isolated top-left speck has no readable character form.',
   'No long handwritten passage occurs.'
  ]
  p.note('7--41','Proposition4.3, proof and Corollary4.4 opening','Every word, property label, hypothesis, index, bar, relation, arrow, underline and punctuation was compared with both complete image halves.','confirmed','The literal and in the hypothesis, lowercase k in R_k, typed x in the product, and unclosed quotation are retained.','full-text')
  p.note('22--24','(v) geometrically integral; (vi) geometrically irreducible','French cote25/site20 lists irreducible above integral, with overwritten v/vi labels and a pen relocation mark. Blass prints the integral item first and the irreducible item second.','comparison-recorded','The clear English order does not remove the remaining French label uncertainties.','cote24-comparison')
  p.note('28--29','characteristic zero and ... unramified','French cote25/site20 joins the characteristic and morphism clauses with ou, and the inserted morphism description remains doubtful un ramifie/non ramifie. English has and and unramified.','comparison-recorded','The connective difference is reported without repairing the hypothesis.','cote24-comparison')
  p.note('36','cases(i) to(v)','French cote25/site20 has a doubtful final label with a crossed i before v. The English prints an unambiguous(v).','comparison-recorded','The English label is preserved without settling the French hand.','cote24-comparison')
  p.note('41','Z x_K bar K','French cote25/site20 writes a tensor-product sign in Z tensor_K bar K; the English has the ordinary lowercase x.','comparison-recorded','The typescript product letter is retained literally.','cote24-comparison')
 else:
  observations=[
   'The page number25 has regular serif numeral shapes distinct from the monospaced body. No pen layer is established; the production method remains unspecified.',
   'Only P is underlined, and the v is on the main baseline.',
   'The xi shapes are regular typed Greek elements. Attached xi sits lower than standalone xi on the same lines, and the subscripts are retained.',
   'There are exactly six typed question marks after A Q T. The later PB query has exactly three, followed by two ordinary stars.',
   'Both starred notes are handwritten and were read in full, including the second line in Corollary4.4 and the final point after AG.',
   'The two short notes do not form a long handwritten passage.'
  ]
  p.note('7--40','Corollary4.4 continuation, commentary, Section5 opening and both pen notes','Every line, formula, index, question mark, star, heading, underline and handwritten word was read against both complete image halves.','confirmed','The missing i inside f(X), capital K(xi), E_xi, extra x, not valid ... if, and both translator queries remain literal.','full-text')
  p.note('9--13','K(xi); dim bar f(X)>=2; E_xi; final underlined P','French cote25/site20 has lowercase k(xi) and f(X_i) with i inside the argument. E_xi and the final P without a dual are present in both witnesses.','comparison-recorded','The genuine differences are separated from readings already shared by the French; nothing is repaired.','cote24-comparison')
  p.note('15--16,38--39','A Q T ??????; Par.9,*; handwritten What is AQT? Where is par9?','French counterpart: cote25/site21 opening, La constructibilite se fait par AQT and oubli au par.9.','cross-reference','The typed and handwritten questions are preserved; the abbreviation is not supplied from an external edition.','cote24-crossreference')
  p.note('21--27','not valid as such if f is quasi-finite; sufficient to consider','French cote25/site21 says nest valable tel quel que si f est quasi-fini and il faut regarder the dimensions of the images. English prints not valid ... if and sufficient.','comparison-recorded','These changes in the qualifying sentence are reported without altering either text.','cote24-comparison')
  p.note('36,40','PB ???**; handwritten illegible - ask AG.','French counterpart: cote25/site21 canceled paragraph4.5, si xi designe limage de y dans P with a dual mark; the paragraph is directed to5.1 and its cancellation is expressly rescinded on French22.','cross-reference','Blasss query remains; the cross-reference includes the authors relocation instruction.','cote24-crossreference')
 assert len(observations)==len(notes[key]),(key,len(observations),len(notes[key]))
 for i,(before,seen) in enumerate(zip(notes[key],observations),1):p.note(f'NOTES item{i}',before,seen,'checked','This listed issue was individually examined in the complete scan comparison.','NOTES')
 text,ds=p.finish();save(key,text,ds,0,'All lines in both complete image halves read, including both complete handwritten notes on25 and all query punctuation.')
print(aggregate())
