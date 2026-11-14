"""Record complete root visual review of cote24 sites8--10."""
from pathlib import Path
import csv
from audit_record import source_path,save,aggregate
from root_review_support import ReviewedPage
ROOT=Path(__file__).resolve().parents[1]
notes={r['key']:r['notes'].split(' | ') for r in csv.DictReader((ROOT.parent/'source/transcription/ega_v_cote24_blass/NOTES.tsv').open(),delimiter='\t')}
for n in (8,9,10):
 key=f'ega24_24_{n:03}';p=ReviewedPage(source_path(key).read_text())
 if n==8:
  p.change(r'P^{V}',r'PV','All three V characters are full-height on the line with P; the small vertical difference follows the capital letterform, with no raised index line.','notation-placement-corrected')
  observations=[
   'The lowered S/s was additionally viewed in a large crop. The worn small curved glyph does not securely establish its case; both S and s remain marked.',
   'The point before xi is visibly typed and remains in the text.',
   'Eta and xi have the regular repeated type-element outlines; no pen stroke is visible in either.',
   'The upper-left dots and faint lower mark contain no readable letter or notation; the whole lower blank area was viewed.',
   'No handwritten text or correction is visible.',
   'No long handwritten passage is present.'
  ]
  p.note('7--24','Complete final part of Section1','Every line, symbol, numeral1, punctuation mark and blank region agrees with the scan, with the V placement corrected.','confirmed','Both full images and the S/s crop were read; the dot before xi and the literal case of P in image in P are retained.','full-text')
  p.note('13,19--24','X and Y; Y a hyperplane section','The English omits the xi attached to Y in the corresponding geometric-property and terminological passages at cote25/sites7--8.','comparison-recorded','This is an observed difference in written notation; the English letters remain as typed.','cote24-comparison')
 elif n==9:
  for letter in ('H','Y','G','Z'):
   for greek in ('eta','xi'):
    before=letter+'_{\\'+greek+'}'
    if before in p.text:p.change(before,letter+'\\'+greek,'Each attached Greek letter has the same full-size type-element shape and baseline as the standalone eta or xi on this page. The draft had introduced a reduced mathematical subscript.','notation-placement-corrected')
  p.change(r'\underline{Y}_{\eta}',r'\underline{Y}\eta','The typed eta after the underlined Y is full-size on the line; only Y is underlined.','notation-placement-corrected',count=1)
  observations=[
   'Only P in the first PV is underlined; the later PV on that line is unadorned. The original underline scope is correct.',
   'Eta, xi and phi are repeated regular typed glyphs. Attached eta/xi letters sit on the main line and have been restored from artificial reduced subscripts.',
   'Every body line, heading, underline and query is typed; no handwritten addition appears.',
   'No long handwritten passage is present.'
  ]
  p.note('7--33','Complete Section2 opening and Propositions2.1--2.2','All text and formulas were read against both images, including underlined ???, the literal bracketed illegible ask AG query, the overline on Y and the final typed phi.','confirmed','The final equality uses the Greek phi type character; no empty-set glyph is substituted.','full-text')
  p.note('23--24','X??? [illegible ask AG]','French counterpart: cote25/site8, the insertion En tous cas overline Y est irréductible after the dominance assertion. The English retains its three question marks and bracketed query before overline Y is irreducible.','cross-reference','The checked French identifies the queried insertion; the English gap is not filled.','cote24-crossreference')
  p.note('15','Spec k(eta)','Blass explicitly types k(eta). The checked French cote25/site8 has Spec(eta), without k in that occurrence.','comparison-recorded','The mathematical notation is reported as written in each witness.','cote24-comparison')
  p.note('22','underlined Y eta','The Y of the English Proposition2.1 is underlined; the corresponding French Y eta at cote25/site8 is not underlined.','comparison-recorded','The underline is visible and is retained in the English.','cote24-comparison')
 else:
  p.change(r'\underline{P}^{V}',r'\underline{P}V','Both V characters are full-size baseline capitals next to the underlined P; no half-line raising or size reduction appears.','notation-placement-corrected')
  for letter in ('Y','Z'):
   p.change(letter+'_{\\eta}',letter+r'\eta','Each eta has the full-size type-element shape, x-height and descender of the body Greek character, with no separate lowered index position.','notation-placement-corrected')
  observations=[
   'The space after indeed X and before underlined P-H is genuinely blank; no faint arrow or inclusion is visible.',
   'The wide space after f:X in Corollary2.3 contains no arrow or handwritten addition.',
   'Both V characters have full cap size on the same main line as P. The draft superscript interpretation is corrected; only P remains underlined.',
   'The folio10 is printed in a regular serif face, without a visible pen layer.',
   'The bottom star and the two-line query are handwritten. The star beside the heading has the regular small typed asterisk form and remains typed.',
   'The handwritten question is a short two-line note, read in full.'
  ]
  p.note('7--35','Complete proof outline, Corollary2.3 and marginal query','Every line, formula, underline and punctuation cluster was read, including the double comma, angle signs around the dimension comparison, and both lines of the handwritten question.','confirmed','Both whole halves were inspected; neither blank symbol position is filled.','full-text')
  p.note('18','indeed X [blank] underlined P-H','French counterpart: cote25/site8, X subset P-H in the affine/projective argument.','cross-reference','The checked French locates the absent English inclusion; the blank remains in Blass.','cote24-crossreference')
  p.note('28','f:X [wide blank] underlined P','French counterpart: cote25/site9, Corollaire2.3, f:X with a handwritten arrow to P.','cross-reference','The absent arrow is recorded as an English gap and not supplied.','cote24-crossreference')
  p.note('34--35','Ask Grothendieck: what is the meaning and role of underlined capital letters?','The question accompanies the proof of2.2, corresponding to cote25/sites8--9, which repeatedly distinguishes the visibly underlined Y and H forms.','cross-reference','The query is preserved in full and linked to its source context, without an editorial answer in the text.','cote24-crossreference')
  p.note('14--15',"[French: il faut one must]",'This typed translator gloss refers to the inserted le il faut at cote25/site8.','cross-reference','The literal translator gloss is retained.','cote24-crossreference')
  p.note('13','Z eta = phi','The English proof types Z eta. The checked French cote25/site8 corrects X by hand to Y at the corresponding equality.','comparison-recorded','The differing leading letter is reported in the guide; neither witness is changed to match the other.','cote24-comparison')
 assert len(observations)==len(notes[key]),(key,len(observations),len(notes[key]))
 for i,(before,seen) in enumerate(zip(notes[key],observations),1):p.note(f'NOTES item{i}',before,seen,'checked','This listed concern was independently checked in the full scan comparison.','NOTES')
 text,decisions=p.finish();save(key,text,decisions,0,'Every line in both full scan halves was visually compared; site8 index crop and site10 handwritten question were read closely.')
print(aggregate())
