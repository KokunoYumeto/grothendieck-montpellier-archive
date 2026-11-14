import re,sys,json
from pathlib import Path
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-3_071';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'B\times_A',r'B\mathrm{x}_A')
 if new!=line:edits.append([line,new,'The fiber-product separator is a typed lowercase x on the scan; preserve that glyph instead of normalizing it to a multiplication cross.'])
up=r'\margin{\diagram{\begin{tikzpicture}\draw[->] (.6,0)--(.2,0) .. controls (0,0) and (0,.2) .. (0,.4)--(0,1.3);\end{tikzpicture}}}'
down=r'\margin{\diagram{\begin{tikzpicture}\draw[->] (.6,1.3)--(.2,1.3) .. controls (0,1.3) and (0,1.1) .. (0,.9)--(0,0);\end{tikzpicture}}}'
trans=r'\begin{tikzpicture}[baseline=(t.base)]\node[anchor=base west,inner sep=0pt] (t) at (0,0) {explicitly down};\draw[color=blue] (-.05,-.03) .. controls (-.03,-.36) and (.25,-.30) .. (.55,-.30)--(1.50,-.30) .. controls (1.75,-.30) and (1.63,.22) .. (1.99,.22) .. controls (2.10,.22) and (2.17,.12) .. (2.28,.16);\end{tikzpicture}'
edits += [
 [r'\deleted{functors}\inserted{maps}',r'\deleted{functors} \inserted{maps}','Keep the visible word boundary between the cancelled typed word and the replacing handwritten word.'],
 [r'\unsure{\hand{B}}$\hand{\to}$',r'$\over{B}{B}^{\deleted{\illegible{1}}}\hand{\to}$','The B is retraced over a typed B. A separate raised item after it is crossed densely; retain that cancelled item as unreadable instead of omitting it.'],
 [r'\unsure{\over{a}{o}}f',r'af','The scan shows an ordinary typed a with its right foot, not an o correction. Preserve the authorial af.'],
 [r'iff \deleted{\illegible{1}} for',r'iff \deleted{if} for','The cancelled fragment after iff reads if; the f ascender and i trace remain visible.'],
 [r'T\unsure{\hand{h}}e feeling',r'T\over[typed]{h}{h}e feeling','The two h impressions have typewriter serifs and are displaced vertically; this is a typed overprint.'],
 [r'categories\inserted{[in the purely categorical sense]}',r'categories \inserted{[in the purely categorical sense]}','Add the literal space required before this inserted bracketed phrase.'],
 [r'\margin{$\uparrow$ (bracket with upward arrow, beside this paragraph)}',up,'Replace the editorial description, which is not manuscript wording, by the visible upward bent-arrow graphic.'],
 [r'\margin{$\downarrow$ (bracket with downward arrow, beside this paragraph)}',down,'Replace the editorial description by the separate downward bent-arrow graphic.'],
 [r'H\unsure{\over{e}{o}}wever',r'H\over[typed]{e}{o}\over[typed]{w}{w}ever','The old e/new o and the doubled w have serif typewriter impressions; their final reading is However.'],
 [r'gene\unsure{r}al',r'gene\over[typed]{f}{r}al','The r is typed over the earlier tall f impression, which remains visible above it.'],
 [r'comment\inserted{still,}',r'comment \inserted{still,}','Keep a literal space at this whole-word insertion boundary.'],
 [r'auto\unsure{\over{h}{m}}atically',r'auto\over[typed]{h}{m}atically','The old h ascender and new m arches are distinct typewriter impressions.'],
 [r'\unsure{28}',r'28','Both handwritten numerals in the section reference are readable: 2 and 8.'],
 [r'dr\unsure{\over{a}{o}}pping',r'drapping','The word is visibly typed drapping, with an uncorrected a. Do not supply the witness’s o.'],
 [r'arrows\unsure{\hand{,}}made',r'arrows\unsure{\hand{,}} made','Retain the doubtful small punctuation stroke while adding the visible following word space.'],
 [r'wrote \hand{(}explicitly\hand{)}down',r'wrote '+trans,'The continuous pen curve passes under explicitly and rises over the beginning of down; it is a transposition mark, not two parentheses. Keep the typed order in the diplomatic text.'],
 [r'the\hand{``}assumption',r'the \hand{``}assumption','The opening hand quotation mark begins a separate quoted word after the article.'],
 [r'the\hand{``}assumpti-',r'the \hand{``}assumpti-','Keep the article separated from the repeated quoted assumption word.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2756:['universal weak equivalences','The adjective is universal, without the ly ending printed in the witness.'],
 2757:[r'\inserted{(46)}','The handwritten call after aspheric is 46.'],
 2758:[r'\margin{X awkward}','Both the pale X and the oblique word awkward are visible.'],
 2767:[r'the \hand{``}assumption\hand{\'\'}(p.30)','Both quotation marks are handwritten and are retained around the typed word.'],
 2768:[r'\over{.}{!}','The sentence-final period has a pen vertical stroke added above it to make an exclamation mark.'],
 2771:[r'\hand{\S.28}','The section reference has clear digits 28.','correct transcription'],
 2772:['drapping','The scan shows a plain typed a, with no secure overprinted o; preserve drapping as a source spelling.','correct transcription'],
 2773:['wrote '+trans,'The source types explicitly down and adds a continuous transposition curve. Diplomatic preserves this; the dedicated master variant applies down explicitly.','correct transcription']
 },'unsure':[[r'\over{B}{B}','The B is clear; a separate crossed raised item has been restored as illegible.'],['a','The letter has a typed a bowl, right stem and foot; there is no secure o layer.'],[r'\over[typed]{h}{h}','Both h impressions are typed.'],[r'\over[typed]{e}{o}','The e-to-o change is recoverable as typed overprinting.'],[r'\over[typed]{f}{r}','The old tall f and final shorter r are legible type impressions.'],[r'\over[typed]{h}{m}','The old h ascender remains above the new typed m.'],['28','Both pen numerals are clear.'],['a','The word reads drapping with an ordinary typed a.'],[r'\unsure{\hand{,}}','The isolated pen stroke below the line could be a comma, but its purpose and form remain uncertain.']],
 'illegible':[['if','The cancelled fragment is legible as if.'],[r'\illegible{1}','The small cancelled item after proved has overlapping type and pen strokes; its full underlying character sequence remains unreadable.']],
 'notes':[
 'The B is a pen retracing over B. The raised adjacent crossed item is separately preserved as illegible; it is not silently dropped.',
 'The source has literal af, while The has two displaced typed h impressions.',
 'However is typed overprinting of e by o, with a repeated w. General contains a typed r over f.',
 'The handwritten section number is securely 28.',
 'The stroke under explicitly down is a continuous transposition curve, not parentheses. The two margin marks are opposing bent arrows, reconstructed without their former editorial descriptions.'
 ],'evidence':'Both original halves and twelve local enlargements inspected. The source discusses universal weak equivalences and makes a tentative connection with fibering/cofibering functors, then returns to the role of the autoequivalence assumption and the weakening of saturation. The marginal awkward and call 46 are clear. The typed af and drapping are uncorrected source spellings; earlier transcription had conjectured o corrections. The B has a separate cancelled raised item, newly retained as unreadable. Typed overprints account for The, However, general and automatically. The number 28 is recovered. The transposition curve under explicitly down is reconstructed with typed order preserved, and a separate master variant applies the instruction. The punctuation stroke before made and the old item after proved remain uncertain.'})
variants=Path('PS_READERS_WORK/records/MASTER_VARIANTS_134_3_4.json')
v=json.loads(variants.read_text()) if variants.exists() else []
v=[x for x in v if x.get('source_id')!='DIFF:2773']
v.append({'key':key,'before':trans,'after':'down explicitly','kind':'authorial transposition','reason':'The continuous pen curve under explicitly and over the beginning of down exchanges their typed order. Diplomatic retains the typed order and the graphic.','source_id':'DIFF:2773'})
variants.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')

key='ps_134-3_072';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A\hand{\hat{}}',r'A\over{\unsure{?}}{{}^{\wedge}}').replace(r'\hat{}',r'^{\hand{\wedge}}')
 if new!=line:edits.append([line,new,'The raised presheaf carets are pen. In Fl(A-hat), a lower question-mark-like type impression survives beneath the added caret and remains doubtful. Repair the empty-accent macros without dropping that lower layer.'])
edits += [
 [r'\mspage{72}',r'\mspage{\hand{72}}','The folio is handwritten.'],
 [r'\margin{\unsure{$\ast$ cf th p. VIII}}',r'\margin{$\ast$ cf \unsure{th} p. \uline{VIII}}','The margin has an asterisk, cf, a short abbreviation, p. and underlined VIII. The abbreviation remains doubtful rather than expanded.'],
 [r'\hand{\unsure{(*)}}',r'\hand{(47)}','The call contains a crossed 4 and a long-stemmed 7; it is 47, not an asterisk.'],
 [r'that \inserted{the} weak',r'that \inserted[typed]{the} weak','The interlinear the in the saturation paragraph is typed above a pen placement curve.'],
 [r'\deleted{xaftar}',r'\xout{after}','The cancelled word is after; its apparent x characters are machine cancellation strokes, including one over the preceding space.'],
 [r'respect \xout{xx} to',r'respect \xout{of} to','The cancelled fragment has a readable o bowl and f ascender: of.'],
 [r'with \inserted{the} \xout{xxx} excep-',r'with \inserted[typed]{the} \xout{one} excep-','The replacement the is typed, and the cancelled old word one is readable.'],
 [r'of just \inserted{the two} \xout{xxx}, \inserted{first, that,} all',r'of just \inserted[typed]{the two} \xout{one}, \inserted[typed]{first,} \inserted{that,} all','The two and first, are typed interlinear additions; that, is pen. The old one is readable. Preserve both commas and the uncancelled all.'],
 [r'model\xout{xxxxx} preserving',r'model\xout{izing} preserving','The old suffix izing is visible beneath the machine cancellation; retain it as the cancelled ending of modelizing.'],
 [r'induce\unsure{\over{s}{d}}',r'induce\over[typed]{s}{d}','The old s lower curves and new d ascender are distinguishable typewriter impressions.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2778:[r'\hand{(47)}\hand{.}','The handwritten call is 47, followed by its separate period.','correct transcription'],
 2779:[r'\margin{$\ast$ cf \unsure{th} p. \uline{VIII}}','The reference VIII is clear and underlined. The small abbreviation remains uncertain.','correct transcription'],
 2780:[r'\inserted[typed]{the}','The interlinear article is typed.','correct transcription'],
 2787:['Namely here','No comma follows Namely on the scan.'],
 2788:[r'with \inserted[typed]{the} \xout{one}','The upper the is typed and the lower one remains readable under its machine cancellation.','correct transcription'],
 2789:[r'of just \inserted[typed]{the two} \xout{one}, \inserted[typed]{first,} \inserted{that,} all','The source retains the lower comma after one and the typed comma after first. Only that, is hand. The placement curve does not cancel all the.','correct transcription']
 },'unsure':[[r'$\ast$ cf \unsure{th} p. \uline{VIII}','The short abbreviation remains uncertain, while the other parts and the underlined Roman numeral are clear.'],['(47)','The digits are 4 and 7, not an asterisk.'],[r'\over[typed]{s}{d}','The old s and new typed d are both discernible.']],
 'illegible':[],
 'notes':[
 'The margin has star, cf, an uncertain short abbreviation, p. and underlined VIII; the numeral is secure.',
 'The call is (47), with a separate pen period.',
 'All presheaf carets and subset signs are hand. In Fl(A-hat), the lower overwritten character is still question-mark-like and is retained tentatively.',
 'The final t of Int is blotted by pen, as transcribed.',
 'The insertion curve passes above all the and descends before all; neither word is cancelled. The two first are typed, that is handwritten, and the visible commas remain.',
 'The final modeli cancellation still obscures its two old cells, which remain represented by the original cancellation notation. Induced has a typed d over a readable s.'
 ],'evidence':'Both full halves and eight enlarged details inspected. The call following strongly saturated is 47, and the marginal Roman numeral VIII is underlined; its abbreviation remains uncertain. The first added the is typed. The cancelled after, of, two occurrences of one and suffix izing are recovered. Section 42 strengthens model-preserving to reflection as well as preservation of weak equivalences. Its mixed insertion has typed the two and first, followed by handwritten that, with all the remaining live. The final d in induced is typed over s. The overwritten character beneath the caret in Fl(A-hat) remains uncertain, as do the terminal cancelled cells of modeli.'})
