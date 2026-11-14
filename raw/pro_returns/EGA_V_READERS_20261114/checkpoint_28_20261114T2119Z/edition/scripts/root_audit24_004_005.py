"""Record root's complete visual comparison of cote24 sites4--5."""
from pathlib import Path
import csv
from audit_record import source_path,save,aggregate
from root_review_support import ReviewedPage
ROOT=Path(__file__).resolve().parents[1]
notes={r['key']:r['notes'].split(' | ') for r in csv.DictReader((ROOT.parent/'source/transcription/ega_v_cote24_blass/NOTES.tsv').open(),delimiter='\t')}
for n in (4,5):
 key=f'ega24_24_{n:03}';p=ReviewedPage(source_path(key).read_text())
 if n==4:
  p.change(r'^{\vee}',r'V','Enlarged EV and full-line comparison show full-height baseline capital V; the draft had supplied a superscript wedge. All such V occurrences on this page were separately checked.','notation-placement-corrected')
  p.change(r'p$^{*}$',r'p*','The enlarged crop shows an ordinary typed asterisk at its usual character position after p, with no superscript-sized or half-line shift.','notation-placement-corrected',count=1)
  p.change(r'H$_{\xi}$',r'H$\xi$','The typed xi begins at the H cap level and has its normal descender; it is not reduced or lowered as an index.','notation-placement-corrected')
  p.change('% NOTE: a white strip covers the next typed line (only faint traces show through); nothing else is typed below it on the page',r'\illegible{?}'+'\n% NOTE: an opaque horizontal white strip occupies the next line position; underlying text cannot be recovered or counted from the supplied image.','The visible white strip is recorded as an occluded place with unknown extent, not as a reconstructed line or a known number of words.','gap-marked',count=1)
  observations=[
   'The first EP in the pairing is full-height typing. The following P after EV is lower. EP is retained exactly.',
   'Both -1 groups after L_P and the final L-1 are on the baseline; no exponent is supplied.',
   'The underline below the subscript P of (EV)_P is visible. Other short underlines are retained as encoded; their worn end points do not securely justify extending them.',
   'The opaque horizontal strip is visible below the final xi. No underlying word is securely readable and no word count can be established; an unknown-extent illegibility mark now links this place.',
   'No long handwritten passage is present; the body is typed.'
  ]
  p.note('11--35','Complete opening of Section1','All words, formula constituents, punctuation, underlines, baseline -1 strings and page numeral were read against both full halves.','confirmed','The display continues through the overlap; the blank lower region and the strip were also inspected.','full-text')
  p.note('occluded final line','White strip after the final xi','French context is cote25/site4 final paragraph, correspondence entre xi (i.e. L...), continuing on cote25/site5 with ou encore L inverse subset E.','cross-reference','The French identifies the passage only; it does not supply an English reading under the strip.','cote24-crossreference')
  p.note('24','O_P(1) after the equality in (**)','Blass types O_P(1). The checked French cote25/site4 types D_P(1), followed by the statement about a section of L_P(1).','comparison-recorded','Both printed letters are preserved; this notation discrepancy belongs in the guide, without a correction based on the other witness.','cote24-comparison')
  p.note('30','E = p superscript star (O_P(1))','Blass has a full-size ordinary typed p*; an enlarged crop resolves the draft superscript interpretation. The checked French cote25/site4 has p with a handwritten subscript star.','comparison-recorded','The location of the star differs visibly between the witnesses and is not standardized.','cote24-comparison')
 else:
  p.change(r'Symm$^{k}$',r'Symm$k$','The enlarged crop shows a full-height k with its foot on the m baseline; the draft had supplied an exponent.','notation-placement-corrected',count=1)
  p.change(r'\hand{\unsure{$\subset$|$\in$}}',r'\hand{$\subset$}','An enlarged crop shows the two-arm open inclusion curve with no medial membership stroke. The pen layer is confirmed.','doubt-resolved',count=1)
  observations=[
   'The enlarged inclusion crop shows a handwritten subset sign, without a middle arm. The alternative membership reading is removed.',
   'The separate small circle has an even printed ring and no pen irregularity; it remains typed, at its own line position.',
   'The -1 groups and xi after H remain at the text baseline, as the image shows; no mathematical index shift is supplied.',
   'PV in the functor line is the literal baseline typing. No check accent is substituted.',
   'The upper numeral5 has regular serif printed contours; it is retained without a pen macro.',
   'There is one short handwritten sign, not a long handwritten passage.'
  ]
  p.note('7--38','Complete text, both paragraphs and Remarks','Every word, typed query, formula, isolated circle, baseline string and trailing point agrees with the image apart from the resolved inclusion doubt.','confirmed','Both complete scan halves and the enlarged inclusion were read. The wording determined of and the five terminal dots are retained.','full-text')
  p.note('16','[Ask AG par 17 of what?]','The exact typed query follows the sentence about a smooth projective fibration; its French counterpart is cote25/site5, au par.17 qu’un fibré projectif est lisse.','cross-reference','The historical query is retained and its source passage identified without an editorial answer.','cote24-crossreference')
  p.note('21--24','[Ask AG about next symbol] and isolated circle','French counterpart: cote25/site5, the functor domain (Sch) with a superscript circle and subscript /S. Blass prints the circle on a separate line.','cross-reference','The French locates the queried mark; the English layout and query remain.','cote24-crossreference')
  p.note('37--38','P(Symm superscript k(E)); P identifies with an open and closed subscheme','Blass has E without the dual mark and a final underlined P without the dual mark; French cote25/site5 has a dual mark over E in Symm and over that final P.','comparison-recorded','Both typographic departures are visible. No mathematical repair is made in the Blass text.','cote24-comparison')
 assert len(observations)==len(notes[key]),(key,len(observations),len(notes[key]))
 for i,(before,seen) in enumerate(zip(notes[key],observations),1):p.note(f'NOTES item{i}',before,seen,'checked','Each listed concern was individually compared with the supplied scan.','NOTES')
 text,decisions=p.finish();save(key,text,decisions,0,'Every line in both full scan halves was visually compared; site5 inclusion additionally inspected in a magnified crop.')
print(aggregate())
