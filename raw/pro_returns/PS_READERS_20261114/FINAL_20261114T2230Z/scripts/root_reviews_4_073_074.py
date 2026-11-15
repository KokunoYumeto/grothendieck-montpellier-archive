from review_root import review
from pathlib import Path

src=(Path(__file__).resolve().parents[2]/'inputs/text/transcription/ps_pages/ps_134-4_073.tex').read_text()
changes=[
 (r'aspheric\unsure{,|.}',r'aspheric\hand{,}','The dark mark has a visible descending tail: it is a pen comma.'),
 (r'mode\over{h}{l}izing',r'mode\over[typed]{h}{l}izing','The superposed l has regular typewriter serifs; the correction is typed over h.'),
 (r'\xout{xxxxxxxx followed xf}',r'\xout{\illegible{1} followed \unsure{of}}','The first cancelled word is not eight literal x letters: the x impressions obscure its base. Followed is legible; the last old word is only tentatively of.'),
 (r'\unsure{mathe}',r'\unsure{name}','The cancelled pen word has initial humps, an a-like loop and a terminal loop supporting name; an independent reading agrees. The crossed middle remains uncertain, so this is a revised doubtful reading.'),
 ('it does cor-',r'it do\over[typed]{e}{e}s cor-','The e of does has two regular superposed typewriter impressions.'),
 ('THere is',r'T\over[typed]{h}{H}ere is','A regular capital H is superposed on the lower h; both layers remain visible.'),
 (r'\inserted{f:}',r'\inserted[typed]{f:}','The interlinear f and colon have regular typewriter shapes, with a pen placement curve.'),
 ('Indeed,',r'I\unsure{\ensuremath{\underset{\hand{\wedge}}{\overset{\hand{\wedge\prime}}{\mathrm n}}}}deed,','Preserve the small upper pen marks and lower chevron at n. Their function is unclear, so the graphic remains doubtful rather than omitted.'),
 ('means that for any',r'means that f\unsure{\over[typed]{or}{or}} any','The two letter cells after f contain regular overprints; their old and final impressions cannot be securely separated.'),
 (r'ret\xout{mu}rning',r'ret\unsure{\over[typed]{mu}{ur}}ning','The crowded letters occupy two overprinted cells, not a deleted two-letter run followed by a separate r. The proposed mu-to-ur correction remains doubtful.'),
 (r'F\!\unsure{l}',r'F\!\over{l}{\ell}','The typed l is visible beneath a separate diagonal pen stroke, as in the adjacent uses of Fl.')
]
for line in src.splitlines():
 if any(x in line for x in [r'\longrightarrow',r'\to']):
  after=line.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\to',r'\hand{\to}')
  if line.startswith('a map '):
   after=after.replace(r'\inserted{f:}',r'\inserted[typed]{f:}').replace('$A ',r'$\over{A}{A} ')
   line=line.replace(r'\inserted{f:}',r'\inserted[typed]{f:}')
  if r'\overset' in line:after=after.replace(r'{A}{}',r'{\over{A}{A}}{}')
  changes.append((line,after,'The map arrows are hand-drawn. The two dark A letters in the category-to-topos comparison also retrace typed A.'))
review('ps_134-4_073',owner='134_4_tail',changes=changes,doubts={'unsure':[
 (r'\hand{,}','doubt resolved','The lower tail clearly distinguishes a comma from a period.'),
 (r'\unsure{name}','doubt revised','Name is the best reading, independently supported, but the cancelling stroke crosses its middle and prevents a secure resolution.'),
 (r'\over{l}{\ell}','doubt resolved','A typed l and an added diagonal pen stroke can be separately identified.')
 ]},notes=[
 'The mark after aspheric is a pen comma with a visible tail.',
 'The final l in modelizing has regular typewriter serifs over the old h; its provenance is corrected to typed.',
 'The cancelled run contains an unreadable first word, then legible followed and doubtful of. Literal cancellation x marks are no longer represented as the first word.',
 'The complete handwritten insertion is crossed out. Its middle word remains doubtful; no conjectural replacement is adopted as settled.',
 'The e of it does is regularly overtyped, now represented.',
 'The small marks above and below n in Indeed are now preserved as an explicitly doubtful graphic.',
 'For has regular crowded overprints whose individual layers remain doubtful. The r of or is clearly handwritten over a typed f.',
 'Returning contains two overprinted cells. The old draft incorrectly represented an extra cancelled mu followed by r; the possible mu-to-ur layering is now explicitly doubtful.',
 'The l of Fl is clear under the added diagonal pen stroke.',
 'The lower-left 73 is handwritten archive foliation.'
 ],summary='Both halves and sixteen enlarged details inspected. The absolute-versus-relative asphericity warning and the distinction between universal and weak W-asphericity are complete. Corrected typed insertions/overprints, marked the pen arrows and A retracings, resolved comma and Fl, restored the omitted marks at Indeed, and replaced literal x cancellation characters by an explicitly unreadable old word. The crowded returning and for overprints remain doubtful. All source formulas, the lowercase slice indices, and the cancelled bottom-line continuation are retained.',differences={
 4482:('the notion of a W-aspheric map','the typescript reads as our transcription','The article a is present between of and W-aspheric.'),
 4484:('(and same thing if','the typescript reads as our transcription','The scan has no article the before same.'),
 4494:(r'the correspon-% \deleted{ding map A/b}','the typescript reads as our transcription','The next-line continuation ding map A/b is visibly crossed out by pen. A fresh continuation begins on the next source page; the witness merges the continuation without recording this deleted attempt.')
 })

src=(Path(__file__).resolve().parents[2]/'inputs/text/transcription/ps_pages/ps_134-4_074.tex').read_text()
changes=[
 (r'\inserted{last}',r'\inserted[typed]{last}','The interlinear last is regular typing, attached by a handwritten placement curve.'),
 (r'\uline{Prop\unsure{s|o}sition}',r'\uline{Prop\over[typed]{o}{\unsure{s|o}}sition}','The disputed cell contains both the rounded old o and a regular s-shaped overprint. The final s/o reading remains uncertain.'),
 (r'I\hand{\unsure{*}}',r'I\unsure{\ensuremath{^{\mathrm I|1}}}','The small raised mark has a regular stem and horizontal serifs, unlike an asterisk. Preserve its uncertain I/1 form without asserting handwriting.'),
 (r'revie\over{\unsure{e}}{w}',r'revi\over[typed]{\unsure{e}}{e}w','The crowded impression is in the e cell, while the final w is plain and separate. The older e-like base remains doubtful.'),
 ('very strong notion',r'very stron\over[typed]{k}{g} notion','The tall k stem is visible beneath the final regularly typed g.'),
 ('FOr this map',r'F\raisebox{-0.25ex}{\unsure{o|O}}r this map','The rounded letter is lowered relative to F and r. Its case is not secure at this impression, so it remains explicit rather than silently made a capital.')
]
for line in src.splitlines():
 if any(x in line for x in [r'\longrightarrow',r'\to']):
  after=line.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\to',r'\hand{\to}')
  changes.append((line,after,'All map arrows on this page have continuous hand-drawn shafts and uneven pen arrowheads.'))
review('ps_134-4_074',owner='134_4_tail',changes=changes,doubts={'unsure':[
 (r'\unsure{ms}','doubt retained','The pen cancellation obscures the first typed letter; ms remains a possible reading, not an established one.'),
 (r'\unsure{except}','doubt retained','The outer e and terminal pt are clear, but the cancelling stroke obscures the middle letters.'),
 (r'\unsure{c}','doubt retained','The heavy loop of the new g hides most of the old letter; a c-like arc is visible but not conclusive.'),
 (r'\over[typed]{o}{\unsure{s|o}}','doubt retained with layering restored','Both rounded o and regular s-shaped impressions are visible in the same cell; the final reading remains uncertain.'),
 (r'\unsure{h}','doubt retained','The raised dark mark over h does not securely distinguish a handwritten retracing from the recurring H-like regular overprint.'),
 (r'\unsure{\ensuremath{^{\mathrm I|1}}}','doubt revised','The raised glyph has a vertical stem and top/bottom bars; it is not securely an asterisk, and I versus 1 remains uncertain.'),
 (r'\over[typed]{\unsure{e}}{e}w','doubt retained with location corrected','The overprint lies on the penultimate e, not on the final w; the old e-like impression remains doubtful.')
 ],'illegible':[(r'\deleted{\illegible{1}}','doubt retained','The small blackened cancelled mark before We has no securely separable letter sequence.')]},notes=[
 'The crossed-out interlinear word is plausibly except, but its middle strokes are obscured; the uncertainty remains.',
 'The pen sms at the right edge is legible. The cancelled old run at the next line remains doubtful ms.',
 'The rounded letter after F is visibly lowered, but its case is not secure; this is now marked. The right edge ends at tha, and no clipped t is invented.',
 'The disputed letter of Proposition contains a regular o/s overprint. Its layering is recorded and the final-letter doubt remains.',
 'The mark over h may be a pen retracing or the recurring regular H-like overprint; the existing doubt is retained.',
 'The mark after I is raised and has serifs, not the radiating form of an asterisk. Its uncertain I/1 form is retained.',
 'The old k stem beneath the final g in strong is visible; the typewriter overprint is restored.',
 'The cancelled blackened sign before We remains unreadable.',
 'The lower-left 74 is handwritten archive foliation.'
 ],summary='Both halves and fifteen enlarged details inspected. Preserved the weak-asphericity proposition, its explicit condition f), and the distinction from universal asphericity. Corrected the typed last insertion, the Proposition and strong overprints, the raised mark after I and the location/provenance of the review overprint. All eight source doubts remain either explicitly doubtful or revised as marked alternatives; the unreadable cancellation is retained. Source slice slashes and lowercase representable a are clear and differ materially from the witness.',differences={
 4499:(r'A_{/F}\hand{\longrightarrow}A_{/G}','the typescript reads as our transcription','Both subscript slashes are printed and visible; the witness drops them.'),
 4501:(r"G'=a\hand{\longrightarrow}G",'the typescript reads as our transcription','The representable object is a lowercase a, consistent with the following with a in A; the witness capitalizes it.'),
 4505:('all time','the typescript reads as our transcription','The scan has no the between all and time.'),
 4506:(r'W_{(\mathrm{Cat})}','the typescript reads as our transcription','The displayed source class is W indexed by (Cat), not just (Cat).'),
 4507:('a map in (Cat) which is weakly','the typescript reads as our transcription','The relative pronoun is which, not the witness that.')
 })
