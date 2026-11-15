from review_root import review
from pathlib import Path
import json

P=Path(__file__).resolve().parents[1]
src=(P.parent/'inputs/text/transcription/ps_pages/ps_134-4_079.tex').read_text()
oldmargin=r"\margin{c'est vrai -- pour tout \unsure{localisateur} \unsure{fonda-mental} \unsure{(i.e.} \unsure{un} \underline{W} \unsure{qui satisf.} \unsure{L1, L3, L4)} \unsure{d'après} \unsure{qui vérifie} \unsure{L5, L4.} \illegible{1}}"
newmargin=r"\margin{c'est vrai -- pour tout localisateur fonda-mental (i.e. un $\underline{W}$ qui \unsure{vérifie} les L1, L3, L4) ainsi que les \unsure{duals|duales} des \unsure{L5, L4'}.}"
changes=[
 (oldmargin,newmargin,'The two scan halves were rejoined at their measured overlap, then the whole note was rotated and independently inspected. The final clause reads ainsi que les duals des L5,L4-prime, not the draft d-apres/qui-verifie repetition. The overlapped verifie, duals spelling and final axiom labels remain doubtful.'),
 (r'fact\xout{\illegible{1}}',r'fact\deleted{\illegible{1}}','The old mark after fact is cancelled by irregular diagonal pen strokes, not regular typewriter x impressions.'),
 ('b) The functor',r'b) T\over{h}{h}e functor','The h is retraced by a long irregular pen stem over its typed base.'),
 ('The following property',r'T\over[typed]{h}{\unsure{H|h}}e following property','The h has a regular H-like raised overprint; its final H/h status remains uncertain.'),
 ('The property c)',r'T\over{h}{h}e property c)','The h has the same long pen retracing as in the first line.'),
 ('The argument in',r'T\over[typed]{h}{\unsure{H|h}}e argument in','The regular raised H-like overprint is restored with its final-letter uncertainty.'),
 ('condition that the cartesian',r'condition th\over[typed]{\unsure{d}}{a}t the c\over[typed]{\unsure{u}}{a}rtesian','The a cells contain regular overprints. Their old tall d-like and rounded u-like bases remain doubtful.'),
 ('eventually, relative to',r'eventually, \over[typed]{\unsure{n}}{r}elative to','The initial r has a regular overlapping n-like old impression, now retained as doubtful.'),
 ('However this ``strong',r'Howe\over{b}{v}er this ``strong','A pen v is written over a typed b with its tall stem still visible.'),
 ('the property we have',r'the propert\over[typed]{\unsure{p}}{y} we have','The final y cell contains an older p-like stem/descender impression; retain that uncertain base.'),
 (r'\begin{tikzcd}[column sep=small]',r'\begin{tikzcd}[column sep=small,every arrow/.append style={draw=blue!65!black}]','All three triangle arrows are hand-drawn; their typed labels remain black.')
]
for before,after,_ in changes:src=src.replace(before,after,1)
for line in src.splitlines():
 if r'\to' in line:
  changes.append((line,line.replace(r'\to',r'\hand{\to}'),'The source arrows have continuous pen shafts and irregular pen arrowheads.'))
review('ps_134-4_079',owner='134_4_tail',changes=changes,doubts={'unsure':[
 ('localisateur','doubt resolved','The connected pen letters of localisateur are legible after rotation.'),
 ('fonda-mental','doubt resolved','The word is split fonda-/mental over two handwritten lines.'),
 ('(i.e.','doubt resolved','The opening parenthesis and abbreviation i.e. are visible.'),
 ('un','doubt resolved','The two connected pen letters before W read un.'),
 (r'qui \unsure{vérifie}','doubt narrowed with corrected reading','Qui is clear; verifie is the best reading across pale body type, not satisf., but remains doubtful.'),
 ('les L1, L3, L4)','doubt resolved','The three axiom labels and closing parenthesis are visible.'),
 ('ainsi que les','doubt resolved with corrected reading','The lower line reads ainsi que les, not d-apres.'),
 (r'\unsure{duals|duales}','doubt revised','Independent inspection identifies a d-initial word with a tall l and s-like end, best read duals or duales, not a repeated qui-verifie clause.'),
 (r"\unsure{L5, L4'}",'doubt retained','L5 and L4 are legible, but the small terminal raised stroke is partly obscured and remains uncertain.')
 ],'illegible':[
 (r'\deleted{\illegible{1}}','doubt retained','The old glyph after fact is blackened by pen cancellation and remains unreadable.'),
 ('des','doubt resolved','The short lower-left word before the last axiom labels reads des in the rejoined and rotated image.')
 ]},notes=[
 'The entire French margin was rejoined from both halves, rotated and independently read. It refers to a localisateur fonda-mental satisfying L1,L3,L4 and to the duals of L5,L4-prime. Three local doubts remain where writing crosses body type or a small terminal stroke is unclear.',
 'The lower-left 79 is handwritten archive foliation.',
 'The blackened old glyph after fact remains unreadable; its cancellation is by pen rather than typewriter.',
 'So si is unequivocally typed, with the two letters reversed. The final readings in the other listed words remain legible; visible old bases in that, cartesian, relative and property are now marked as doubtful overprints, and However has a clear pen v over typed b. The dark in impression does not expose an independently readable different old letter.',
 'The old f,g W implies run has both regular x impressions and a pen strike; both cancellation layers are retained.',
 'The C-is-W-aspheric insertion is typed, while both surrounding parentheses are handwritten.'
 ],summary='Both halves, nine enlarged details and the fully rejoined/rotated French margin inspected, with an independent reading of the latter. Corrected the margin substantially while preserving doubts at verifie, duals and the final label. Restored several visible pen/typed overprints and the pen cancellation after fact; all arrows are marked. The source says basic modelizer and for any A in C, both preserved as source slips for the guide. So si is a clear letter transposition and receives an explicit corrected-form variant supported by correctly typed so is on p163.',differences={
 4597:('so si','the arXiv text corrects','The scan clearly types so si. The adjacent standard construction and correctly typed so is on p163 establish this one-off transposition; the corrected forms use so is with an explicit slip variant.'),
 4598:(r"$f^{o}$: $C^{o}\hand{\to} C'^{o}$",'the typescript reads as our transcription','The scan uses small superscript o and an unparenthesized primed target, as transcribed.'),
 4599:(newmargin,'our transcription corrected','The complete note was rotated and independently reread. Its final clause concerns duals of axioms, not the draft repeated qui-verifie phrase; the witness omits the note.'),
 4600:('are concerned','the typescript reads as our transcription','The typed verb is plural are.'),
 4602:('basic modelizer','the typescript reads as our transcription','The source noun is modelizer; the witness changes it to localizer. The conceptual slip is discussed only in the guide.'),
 4608:('(cf proposition on page','the typescript reads as our transcription','The abbreviation is cf, not of.'),
 4611:(r'\margin{$\times$}','the typescript reads as our transcription','A handwritten cross is present beside the fibration-axiom sentence.')
 })

vp=P/'records/MASTER_VARIANTS_134_4_tail.json';vv=json.loads(vp.read_text())
vv=[v for v in vv if v['source_id']!='DIFF:4597']
vv.append(dict(key='ps_134-4_079',before='so si',after='so is',kind='slip corrected',reason='The two letters of is are transposed in this isolated occurrence. The clause and the correctly typed so is on p163 settle the correction; no consistent author usage is standardized.',source_id='DIFF:4597'))
vp.write_text(json.dumps(vv,indent=2)+'\n')

review('ps_134-4_080',owner='134_4_tail',changes=[
 (r'\inserted{previous}',r'\inserted[typed]{previous}','The interlinear previous is regular typing with a handwritten placement curve.'),
 (r'\inserted{saturated}',r'\inserted[typed]{saturated}','The interlinear saturated is regular typing with a pen placement curve.'),
 (r'W\unsure{\subset} \mathrm{F}\unsure{\mathrm{l}}(M))',r'W\hand{\subset} \mathrm{F}\over{l}{\ell}(M))','The inclusion sign is a clear continuous pen stroke; the typed l has a separate diagonal pen stroke.'),
 (r'T\over{H}{h}e latter',r'T\over[typed]{h}{\unsure{H|h}}e latter','The regular raised H-like overprint does not establish the draft handwritten H-to-h order. Preserve the visible typed layering and uncertainty.'),
 (r'\xout{to specify}',r'\deleted{\xout{to specify}}','A continuous pen strike crosses the regular typewriter x cancellation of the same phrase.'),
 (r'\hand{(} for',r'\unsure{\hand{(}|\hand{\ensuremath{\leftarrow}}} for','The large curved opening mark also contains a short horizontal stroke. Preserve the uncertain parenthesis/left-arrow interpretation instead of suppressing that extra stroke.'),
 (r'\hand{65}.',r'\hand{6}\over{\unsure{2}}{5}.','The final pen 5 covers an older curved numeral with a 2-like lower diagonal; the older digit remains uncertain.'),
 ('for looking at',r'for l\over[typed]{\unsure{l|d}}{o}oking at','The first o contains an older tall stem, plausibly l or d, obscured by the final regular o.'),
 ('a landscape',r'a la\over[typed]{\unsure{d}}{n}dscape','The n cell has an older tall d-like impression; its base remains doubtful.'),
 ('wholly at ease',r'w\unsure{\over[typed]{m}{h}}olly at ease','The dense regular overprint is on h, while the following o is plain. The proposed m-to-h order remains uncertain.'),
 ('The grinding',r'T\unsure{\ensuremath{\overset{\perp\perp}{\mathrm h}}}e grinding','Preserve the two small raised marks over h as an uncertain graphic; no secure pen-versus-typing attribution is inferred from darkness alone.'),
 (r'\inserted{same}',r'\inserted[typed]{same}','The interlinear same has regular typewriter letters and a pen placement curve.'),
 (r'expect\xout{\illegible{1}}',r'expect\xout{now}','The old n, o and w remain readable under the regular x cancellation.'),
 ('(with respect',r'(\over[typed]{f}{w}ith respect','The old f stem and curved top remain visible beneath the final regular w.'),
 (r"M \longrightarrow M'",r"M \hand{\mathrel{\rule{2.5em}{.4pt}}} M'",'The scan shows a hand-drawn horizontal connector with a blunt/dotted end, without a readable arrowhead. Retain the visible line rather than supplying an arrowhead.')
 ],doubts={'unsure':[
 (r'\hand{\subset}','doubt resolved','The continuous open pen curve has an upper and lower horizontal stroke, clearly an inclusion sign.'),
 (r'\over{l}{\ell}','doubt resolved','The typed l and a diagonal pen addition are separately visible.'),
 (r'\unsure{\hand{,}}','doubt retained','A comma-like tail appears at the clipped right edge after it, but the border obscures part of the mark and its provenance.')
 ],'illegible':[
 ('now','doubt resolved','All three old letters n,o,w are visible under the x strikes.'),
 (r'\illegible{1}','doubt retained','The blackened old letter between preserv and ing remains unreadable.')
 ]},notes=[
 'The inclusion is a clear handwritten subset sign; Fl has a typed l crossed by a diagonal pen stroke. Both original doubts are resolved.',
 'To specify carries both regularly spaced x strikes and a continuous pen line; both mechanisms are now recorded.',
 'The final section digit is pen 5 over a doubtful old 2-like digit. The dark 4 in 7.4. is a pen retracing, with no distinct earlier reading exposed.',
 'Looking has an older tall stem beneath the first o; landscape has a d-like old base under n. The dense wholly overprint is at h, not its following plain o; its old/final order stays doubtful.',
 'The two raised marks above h in The grinding are now preserved graphically and remain uncertain.',
 'The letter cancelled inside preserving remains unreadable. The w of with overlies a clear typed f. The extra M before u is struck by the typewriter and remains in the diplomatic form.',
 'The lower-left 80 is handwritten archive foliation.'
 ],summary='Both halves and thirteen enlarged details inspected. The concluding terminology paragraph and dated opening of section65 are complete. Corrected three typed insertions, resolved subset and Fl, restored the dual cancellation of to specify, and added explicit doubts for the overwritten section digit and crowded word/graphic layers. Resolved the cancelled now and old f under w. The right-edge comma remains doubtful. The displayed map has a visible pen connector without a readable head and is represented as that line. The first paragraph keeps the author-specific Hot_W notation and the source extra parenthesis.',differences={
 4614:('modelizers, test functors','the typescript reads as our transcription','The list contains no and before test functors.'),
 4627:('65.','the typescript reads as our transcription','The scan has its section number and date, but no descriptive section title.'),
 4629:(r'aloof of it\unsure{\hand{,}}','the typescript reads as our transcription','The comma-like tail at the clipped right edge remains marked; the witness omits it.'),
 4635:("(with respect to (W,W')) if",'the typescript reads as our transcription','Two closing parentheses are typed, closing both the pair and with-respect parenthesis.')
 })
