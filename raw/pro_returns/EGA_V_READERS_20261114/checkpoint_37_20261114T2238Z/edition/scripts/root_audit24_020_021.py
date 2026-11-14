"""Save root's complete cote24 sites20--21 visual comparison."""
from pathlib import Path
import csv
from audit_record import source_path,save,aggregate
from root_review_support import ReviewedPage
ROOT=Path(__file__).resolve().parents[1]
notes={r['key']:r['notes'].split(' | ') for r in csv.DictReader((ROOT.parent/'source/transcription/ega_v_cote24_blass/NOTES.tsv').open(),delimiter='\t')}
for n in (20,21):
 key=f'ega24_24_{n:03}';p=ReviewedPage(source_path(key).read_text())
 if n==20:
  p.change(r'k^1',r'k1','Each full-size1 sits on the main baseline next to k, as on the preceding page. A raised exponent is not visible.','notation-placement-corrected')
  p.change(r't_n{}^{-1}',r't_n{-1}','The n is lowered, but the following -1 is full-size at the main baseline. The two occurrences were compared separately.','notation-placement-corrected')
  p.change(r'\sum_{I}^{M}',r'\sum\limits_{I}^{M}','The typed capital M is directly above Sigma and the capital I directly below it. Explicit limits encode this visible vertical arrangement in the inline formula.','layout-encoding-corrected',count=1)
  observations=[
   'Both numerals2 are clear regular serif forms, unlike the monospaced body digits. Their lettering is secure, and no irregular pen stroke establishes a handwritten layer; plain2 is retained without claiming the production method.',
   'The bar over f(X) is a straight even rule matching the typed overlines elsewhere; no handwritten correction is visible.',
   'The limits are capital M above and capital I below Sigma, on separate lines. Explicit limits now keep that observed placement.',
   'The isolated second period after primary extension of k1 is plainly typed and retained.',
   'No long handwritten passage occurs.'
  ]
  p.note('7--31','Complete function-field continuation, Zariski lemma and3.2 opening','All words, indices, signs, limits, punctuation, bars and numeral forms were read in both full halves.','confirmed','The coefficient a_i before S1, missing leading minus in a_i=t_i t_n-1, baseline k1 and -1, and capital I/M limits remain literal.','full-text')
  p.note('8--9','a_i S1; a_i=t_i t_n-1','French cote25/site16 has a_1 S1 and a_i=-t_i t_n inverse. The English coefficient index is i and its coefficient formula has no leading minus.','comparison-recorded','Both differences are visible and are reported without a mathematical correction.','cote24-comparison')
  p.note('19--21','lemma refers to L without a definition L=K(S1,...,Sm)','The checked French cote25/site17 explicitly introduces L=K(S1,...,Sm) before k prime. The English moves directly from the transcendence-degree condition to k1.','comparison-recorded','The omitted defining phrase is recorded; the Blass reader does not interpolate it.','cote24-comparison')
  p.note('21','sum from capital I to capital M','French cote25/site17 has lower limit numeral1 and upper lowercase m. Blass types I and M.','comparison-recorded','The printed capital letters are retained and not converted from their mathematical context.','cote24-comparison')
 else:
  observations=[
   'The bar spans f(X), with a clear X inside the parentheses. It is not moved to the Z mentioned in the prose.',
   'K in the corollary conclusion is capital; later instances in the proof are lowercase k. All are retained.',
   'Eta, sigma, not-in, not-equal and the empty-set glyph have regular type-element shapes. No pen layer is visible in these symbols.',
   'The bottom note is penned and reads * ASK A.G., including the final point. Its star corresponds to the typed star at par.6; the enlarged note was also read.',
   'The handwritten note is short, not a long passage.'
  ]
  p.note('7--37','Complete3.2 ending,3.3 and Section4 opening','Every line, letter case, index, bar, Greek symbol, typed reference and both heading underlines was read against both full images.','confirmed','The literal X0 and X prime phrase, f(X) in the definition of sigma, capital K, and the finite-presentation opening are retained.','full-text')
  p.note('18,37','par.6*; ASK A.G.','French counterpart: cote25/site17, par.6 avec le th. de Hartshorme in the proof of3.3.','cross-reference','The translator query remains; the spelling in each witness is preserved.','cote24-crossreference')
  p.note('13','sigma; dim bar f(X)=0','French cote25/site17 retains doubt between script G/S for the family and between Z/X inside f. Blass has a clear typed sigma and clear X.','comparison-recorded','The English does not resolve the French image uncertainty; each reading remains in its own witness.','cote24-comparison')
  p.note('15','connected over K(eta)','French cote25/site17 has lowercase k(eta); the English conclusion prints capital K.','comparison-recorded','The letter case is not standardized.','cote24-comparison')
  p.note('21','X0 and X prime,...,X_n=X double prime','French cote25/site17 has X_o=X prime at the start of the chain. Blass types and instead of that equality and a numeral0 in X0.','comparison-recorded','The wording and index form are retained literally.','cote24-comparison')
 assert len(observations)==len(notes[key]),(key,len(observations),len(notes[key]))
 for i,(before,seen) in enumerate(zip(notes[key],observations),1):p.note(f'NOTES item{i}',before,seen,'checked','This listed concern was individually examined in the complete scan comparison.','NOTES')
 text,ds=p.finish();save(key,text,ds,0,'All lines and formulas in both complete scan halves read, including limit positions and letter cases; site21 handwritten query additionally magnified.')
print(aggregate())
