"""Record full root visual comparison of cote24 sites14--16."""
from pathlib import Path
import csv
from audit_record import source_path,save,aggregate
from root_review_support import ReviewedPage
ROOT=Path(__file__).resolve().parents[1]
notes={r['key']:r['notes'].split(' | ') for r in csv.DictReader((ROOT.parent/'source/transcription/ega_v_cote24_blass/NOTES.tsv').open(),delimiter='\t')}
for n in (14,15,16):
 key=f'ega24_24_{n:03}';p=ReviewedPage(source_path(key).read_text())
 if n==14:
  observations=[
   'The first overbar is directly over dim, with f(Z) outside it. The later overbar in2.11 is over f(Z). Both distinct spans are retained.',
   'Only the Y in the opening y-in-Yeta phrase of2.11 is underlined there, as encoded.',
   'The folio14 has regular serif printed contours and no pen stroke.',
   'The upper-left dots have no readable character or textual function.',
   'No handwriting or long handwritten passage occurs.'
  ]
  p.note('7--35','Complete Corollaries2.9--2.11','All words, indices, bars, underlines, reference placeholders and punctuation were read against both full halves.','confirmed','The literal h(Z), the bar over dim, and the statement about already knowing constructibility are retained.','full-text')
  p.note('25','R_k (reference)','French counterpart: cote25/site12, R_k (réf) in Corollaire2.11.','cross-reference','The reference remains incomplete in both witnesses.','cote24-crossreference')
  p.note('33--35','give the different references assuring that Z is closed','French counterpart: cote25/site12, Il faut donner les diverses références assurant que Z est fermé.','cross-reference','The request for references is retained and its source identified.','cote24-crossreference')
  p.note('12','bar over dim, then f(Z)=0','French cote25/site11 places the bar over f(Z), after dim; Blass places it over dim.','comparison-recorded','The bar is not moved on mathematical grounds.','cote24-comparison')
  p.note('14','h(Z)','French cote25/site11 has doubtful h with an inverse-image exponent -1, followed by (Z); Blass has h(Z), with no exponent.','comparison-recorded','The visible missing exponent is reported without adding it.','cote24-comparison')
  p.note('34--35','we already know that it is constructible by applying2.3','French cote25/site12 says that one must know constructibility in order to apply2.3.','comparison-recorded','The different wording of the logical dependency is recorded; the English sentence is kept as typed.','cote24-comparison')
 elif n==15:
  observations=[
   'The v after the underlined P is visibly a baseline lowercase letter. It is retained literally.',
   'The infinity sign is on the ordinary symbol line after H, without a separate lower placement; H infinity is retained as encoded.',
   'There is an actual blank inside k( ); the1 after Omega is at baseline and the u/k group is below. The word illegible and its star are typed after the formula.',
   'The folio15 is regular serif printing.',
   'The footnote is penned and reads * Ask A.G., with the points after A and G. It corresponds by its star to the typed illegible query.',
   'The handwritten material is the one short query; no long passage occurs.'
  ]
  p.note('7--36','Complete opening and Theorem2.12 proof','Every word, formula, index, underline, blank, parenthesis and footnote was read against both full halves.','confirmed','The doubled to, ncessary, lowercase y before the arrow, baseline v and1, and the extra closing parenthesis in the differential expression remain literal.','full-text')
  p.note('19','regular at x (reference)','French counterpart: cote25/site12, X est régulier en x (réf).','cross-reference','The placeholder reference is retained.','cote24-crossreference')
  p.note('20','perfect (reference)','French counterpart: cote25/site12, k est alg clos donc parfait (réf).','cross-reference','The second distinct reference placeholder is retained.','cote24-crossreference')
  p.note('33','blank k( ); [illegible]*; Ask A.G.','French counterpart: cote25/site13, (underlined Omega superscript1 subscript U/k) tensor_k k( ) suivantes. The French parentheses also contain a blank.','cross-reference','The query is preserved; comparison does not fill an English gap from an absent French argument.','cote24-crossreference')
  p.note('28--29','H infinity [at infinity]','The typed English gloss accompanies H infinity; French cote25/site12 has H subscript infinity without this gloss.','comparison-recorded','The translator gloss is part of the English witness and remains.','cote24-comparison')
  p.note('29','lowercase y arrow U_k(eta)','French cote25/site12 has capital Y and a handwritten hooked arrow. Blass types lowercase y and an ordinary arrow.','comparison-recorded','The case and arrow shape are not repaired from the French.','cote24-comparison')
 else:
  p.change('% NOTE: a white rectangle covers the rest of this line after "Y_eta = (empty set)", and another white rectangle covers the beginning of the next line; any text under them is hidden.',r'\illegible{?}'+'\n'+r'\par\illegible{?}'+'\n% NOTE: two separate opaque white rectangles follow the empty-set equality: one at the line end and one at the next line start. Underlying content and word counts cannot be recovered.','Both separate occluded places are visible. Each now has an unknown-extent linked mark; no hidden word is reconstructed.','gaps-marked',count=1)
  observations=[
   'Both white rectangles are visible, one at the last proof-line end and one at the next line start. No underlying letter is securely readable; two unknown-extent marks record the separate masks.',
   'Omega is followed by a baseline1 in both expressions; u/s and u/k are lowered and lowercase, as typed.',
   'The bound1<=i<=n lies on a separate line below the summation sign in the quotient expression. It remains attached there in the English transcription.',
   'The first scalar-field index has lowercase k; Corollary2.13 prints capital K(eta). Both cases are retained.',
   'The upper-left dots contain no readable text.',
   'No handwritten body material is visible.',
   'No long handwritten passage occurs.'
  ]
  p.note('7--34','Complete proof ending, Corollary2.13 and Theorem2.14 opening','All words, indices, case distinctions, sum bounds, inequalities, punctuation and four list entries were read against both full images.','confirmed','The two masks were inspected separately and remain unreadable. The literal p<=n and subsequent p=n are preserved.','full-text')
  for loc in ('end of proof line','next line start'):
   p.note(loc,'Opaque white rectangle','French context: cote25/site13, the proof ends with Y eta = empty set, followed by Corollaire2.13.','cross-reference','The comparison identifies the position only; no particular English words beneath this separate mask are asserted.','cote24-crossreference')
  p.note('11','quotient sum with lower bound1<=i<=n','French cote25/site13 places1<=i<=n after the inserted generators a_i, while the quotient sum has no such explicit bound there. Blass places the bound under the quotient sum and omits a_i in the following family-of-generators phrase.','comparison-recorded','The changed location of the bound is visible; no mathematical correction is applied.','cote24-comparison')
  p.note('19','K(eta)','French cote25/site13 has lowercase k(eta) in Corollaire2.13; Blass types a capital K.','comparison-recorded','The letter case is retained.','cote24-comparison')
 assert len(observations)==len(notes[key]),(key,len(observations),len(notes[key]))
 for i,(before,seen) in enumerate(zip(notes[key],observations),1):p.note(f'NOTES item{i}',before,seen,'checked','This listed concern was individually examined against the complete supplied images.','NOTES')
 text,decisions=p.finish();save(key,text,decisions,0,'Every line in both full scan halves read against the source, including all formulas and indices, the handwritten question on15, and both opaque masks on16.')
print(aggregate())
