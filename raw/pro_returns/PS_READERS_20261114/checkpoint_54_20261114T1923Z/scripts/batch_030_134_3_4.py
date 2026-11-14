import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT,occurrences
key='ps_134-3_030';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();u=occurrences(s,'unsure');edits=[]
def e(a,b,r):edits.append([a,b,r])
e(u[0][0],r'f\over{la}{la}rring','The enlarged crop shows two distinct typed r characters after the retouched la; the actual spelling is flarring. The la is retraced by hand.')
e(u[1][0],'26','The handwritten figure has a continuous upper curve and a lower loop: section26, replacing the cancelled page27 reference.')
e(r'\deleted{\unsure{of $\mathrm{id}_{(\mathrm{Hot})}$}}',r'\deleted{\hand{of $\mathrm{id}_{(\mathrm{Hot})}$}}','The enlarged crossed group resolves of id with parenthesized Hot below; the entire deleted phrase is handwritten.')
e(r'$W \subset \mathrm{Fl}(M)$',r'$W \hand{\subset} \mathrm{F}\over{l}{l}(M)$','The inclusion is a rounded handwritten subset sign, not a typed less-than; the l in Fl is retraced by a long pen stroke.')
conf=dict(key=key,edits=edits,diffs={
1944:['28.','The left margin contains only the handwritten section number; the witness title is not on this typescript page.'],
1947:[r'f\over{la}{la}rring','The scan has two r characters, with la retouched by hand.','correct transcription'],
1948:[r'\deleted{(p.27)}\inserted{(section 26)}','The enlarged handwritten numeral is26; the old p.27 is struck.','correct transcription'],
1950:['“weak equivalences”','The typed quotation is plural, ending ces before the closing quote.'],
1953:[r'\xrightarrow{\approx}','The arrow has two wavy strokes above it, not the single-wave equivalence form of the witness.'],
1955:['such kind of things','The noun kind is singular in the typed line.'],
1959:['a localization functor','The underlined functor is singular.'],
1960:['word “model category”','The typed word is word, with a clear final d, rather than the witness work.']},
unsure=[[r'f\over{la}{la}rring','The enlarged crop settles the two-r spelling and handwritten retracing of la.'],['26','The figure has the curved upper stroke and loop of6; the rewritten reference is to section26.'],[u[2][0],'The small area after -1 is obscured by the beginning of the handwritten deletion; a separate period cannot be established.'],[r'of $\mathrm{id}_{(\mathrm{Hot})}$','The enlarged crossing leaves readable of, id, and a parenthesized Hot subscript.']],
illegible=[],notes=[
'The geometric realization and autoequivalence words are legible despite overtyping; flarring has two r letters and retouched la, now specified; facts remains legible.',
'The enlarged correction reads section26, replacing p.27.',
'The enlarged deleted phrase reads of id_(Hot); its handwriting and deletion are retained, while the preceding possible period remains doubtful.',
'The first parenthesized asterisk is machine-cancelled before the live repetition; the tiny isolated left mark supplies no legible text.',
'The underlines beneath the localization reformulation are hand-drawn lines with varying pressure.',
'The inclusion is a rounded handwritten subset sign; the l of Fl has a handwritten retracing, now marked.',
'The small traces near The, means and rephrased are isolated overwriting/ink marks rather than recoverable additional words; the legible words remain.'],
evidence='Both complete halves opened. Upper: section28 has no descriptive title; the plural weak equivalences and source isnt are clear. Enlarged flarring shows two r characters and hand-retouched la. The overwritten cross-reference resolves to section26 over deleted p.27. The inserted of in the assumption is handwritten. Lower: the autoequivalence arrow bears two waves, the phrases such kind, a localization functor and word model category match the page against witness errors. The crossed handwritten phrase after -1 reads of id_(Hot); the uncertain intervening punctuation remains. The W comparison uses a rounded pen subset sign and a retraced l. The first (*) is machine-cancelled and repeated, and the long underlines belong to the manuscript. Isolated little marks around legible words remain interpreted as overwriting traces, not invented text.')
(OUT/'review_notes'/f'{key}.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2));save_review(conf)
