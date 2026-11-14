from review_root import review
from pathlib import Path
import json
k='ps_134-2_043'
join=r'\hand{\tikz[baseline=-.4ex]{\draw (0,0) .. controls (.06,-.01) and (.13,.02) .. (.22,.09);}}'
review(k,changes=[
(r'\mspage{28}',r'\mspage{\hand{28}}','The centered folio is handwritten.'),
(r"\hand{\unsure{d'}}",r"\hand{d'}",'The replacement d and its apostrophe are legible beside the cancellation.'),
(r'n-c atégories',r'n-c'+join+r'atégories','The pen curve joins the two typed parts across the gap; its graphic was omitted.'),
(r'n-c atégorie',r'n-c'+join+r'atégorie','A second pen joining curve is visible in the later singular occurrence.'),
(r't\unsure{\xout{u}}itre',r't\over[typed]{u}{i}tre','The enlargement shows i typed over u in one cell, not a separate u removed by x cancellation.'),
(r'accouplements\inserted{de composition}',r'accouplements \inserted[typed]{de composition}','The phrase is typed interlinearly, with a pen insertion curve; the word boundary is explicit.'),
(r'n-catégorie\inserted{$C_n(K.)$}',r'n-catégorie \inserted{$C_n(K.)$}','The handwritten object name follows a word boundary.'),
(r"\xout{une}\inserted{les O-objets d'une}",r"\xout{une}\inserted[typed]{les O-objets d'une}",'The replacement phrase is typed above the cancelled une; its curved pen anchor is not a deletion of the live baseline words.'),
(r'\unsure{N|n}',r'N','The visible letter is a capital N, despite a locally doubled impression.'),
(r'$1\leq i\leq n$',r'$1\hand{\leq} i\hand{\leq} n$','Both inequality signs are handwritten.'),
(r'\hand{$\pi_i$}(C,x)',r'\hand{$\pi_{\unsure{i|2}}$}(C,x)','The subscript is heavily retraced and retains a 2-like loop below an i-like dot. Its exact reading cannot be settled from the image.'),
(r'$O\leq i\leq n$',r'$O\hand{\leq} i\hand{\leq} n$','The two comparison signs are penned.'),
(r'$x \to x$',r'$x \hand{\to} x$','The endomorphism arrow is handwritten.'),
(r'des\inserted{classes mod équivalence des}',r'des \inserted[typed]{classes mod équivalence des}','The inserted phrase is typed interlinearly and separated from the preceding word.'),
(r'$1_x \to 1_x$',r'$1_x \hand{\to} 1_x$','The arrow between identity 1-flèches is penned.'),
(r'$1_{1_x} \longrightarrow 1_{1_x}$',r'$1_{1_x} \hand{\longrightarrow} 1_{1_x}$','The next higher endomorphism arrow is also penned.'),
(r'habituel,\inserted{les $\pi_i(C,x)$}',r'habituel, \inserted[typed]{les $\hand{\pi}_i(C,x)$}','Les and the argument are typed in the interlinear insertion, while pi is handwritten. The curve anchors the insertion without cancelling ne dépendent.'),
(r'$0\leq i\leq n$',r'$0\hand{\leq} i\hand{\leq} n$','The lower comparison pair is handwritten.'),
(r'\margin{43}',r'\margin{\hand{43}}','The lower-left archive number is in pencil.')
],doubts={'unsure':[
(r'\xout{\unsure{entre}}','doubt retained','The cancelled word plausibly reads entre but its opening and ending are heavily covered; no certain full recovery is claimed.'),
(r"\hand{d'}",'doubt resolved','The replacement d and apostrophe are legible.'),
(r'\unsure{déscription}','doubt retained','Several letters are overtyped on an older word; the exact layered reading remains uncertain.'),
(r'\over[typed]{u}{i}','doubt resolved','The u and the correcting i occupy one typewriter cell; no cancelling x is visible.'),
('N','doubt resolved','The capital N has two tall stems and a diagonal; no lower-case live n is present.'),
(r'form\unsure{e}','doubt retained','The terminal letter is clipped at the right edge and cannot be fully recovered.')
],'illegible':[
(r'\over{\illegible{1}}{i}','illegible retained','The corrected i is visible, but the heavily inked preceding layer remains unreadable.')
]},notes=[
'The replacement d\' is clear and penned; the cancelled entre remains uncertain under heavy impressions.',
'Déscription is densely overtyped and remains doubtful. Its following pen separator is retained and applied as a space by a master variant.',
'Both n-c atégorie(s) occurrences have visible pen joining curves, now restored and applied by explicit variants. The gap in loc aux has no visible joining curve; its correction is instead an explicit one-off typing-space variant supported by locaux later on this same page.',
'Titre has a same-cell typed u-to-i correction, rather than a separate struck u.',
'The arcs anchor the insertions and do not cancel sont des, n-catégorie, 2-flèches, or ne dépendent. The phrases de composition, les O-objets d\'une, and classes mod équivalence des are typed interlinearly; les pi_i(C,x) has mixed typed and handwritten provenance.',
'The disputed baseline letter is a capital N.',
'The pi subscript is heavily retraced, with an i-like dot and 2-like lower loop. A new explicit doubt prevents an unsupported clean reading.',
'The terminal e of forme is clipped and remains doubtful. The source line endings s\'in and isomor have no added hyphen.',
'The lower-left 43 is archive numbering in pencil.'
],summary='Both scan halves and eight enlarged details inspected. Restored two author joining curves, corrected four interlinear provenance assignments and word boundaries, resolved d\', capital N and typed u-to-i overprinting in titre, marked pen arrows and inequalities, and added a genuine doubt at the overworked pi subscript. Kept the uncertain cancelled entre, overtyped déscription, clipped final e and illegible older letter. The source functor formula has balanced object arguments and the full pi0 explanatory clause absent from the witness.',differences={
639:(r"classes d'équivalence \xout{\unsure{entre}}\hand{d'}homotopies",'our transcription corrected','The live d\' is clear; the cancelled entre remains doubtful. The witness de does not reproduce this correction layer.'),
640:(r"données d'associativité\hand{"+'"}', 'the typescript reads as our transcription','The handwritten closing quote is present and retained.'),
641:(r"fil d'\hand{A}riane",'the typescript reads as our transcription','The source name is Ariane, without the witness d.'),
644:(r"$C_n(K.)\hand{$\to$}C_n(K'.)$",'the typescript reads as our transcription','The arrow connects two completed C_n object expressions; the witness brackets it inside one malformed expression.'),
646:("l'appliquant à des ensembles",'the typescript reads as our transcription','The word is the participle appliquant, not the noun application.'),
648:('N','our transcription corrected','The image resolves the letter as capital N; the witness silently lowers it.'),
650:('et x un O-objet de C','the typescript reads as our transcription','The source object variable is lower-case x.'),
653:("(c'est un vulgaire ensemble), l'ensemble des classes à équivalence près",'the typescript reads as our transcription','The full explanation of pi0 and transition to pi1 is present; the witness omission loses their distinction.'),
659:('systèmes loc aux','the typescript reads as our transcription','The source contains a typed gap without a pen joining stroke. A one-off-space master variant joins the word, supported by locaux later on this checked page.'),
663:('application semi-simpliciale','the typescript reads as our transcription','The feminine final e is present.')
})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json';v=json.loads(p.read_text())
ids=['JOIN:043:1','JOIN:043:2','SPACE:043:1','DIFF:659','SPACE:044:1'];v=[x for x in v if x.get('source_id') not in ids]
for n,b,a in [(1,'n-c'+join+'atégories','n-catégories'),(2,'n-c'+join+'atégorie i.e.','n-catégorie i.e.')]:
 v.append(dict(key=k,before=b,after=a,kind='author joining cue',reason='Apply the curved pen mark joining the separated parts of the typed word; retain its graphic diplomatically.',source_id=f'JOIN:043:{n}'))
v.extend([
dict(key=k,before=r'\unsure{déscription}\hand{/}des',after=r'\unsure{déscription} des',kind='author spacing cue',reason='The pen separator instructs a word space before des; the overtyped preceding word remains doubtful.',source_id='SPACE:043:1'),
dict(key=k,before='loc aux',after='locaux',kind='slip corrected',reason='One-off internal typing space; locaux is correctly typed in the later systems-local sentence on this same checked page.',source_id='DIFF:659')])

k='ps_134-2_044'
review(k,changes=[
(r'\mspage{29}',r'\mspage{\hand{29}}','The centered folio is handwritten.'),
(r'\over{N}{n}',r'\over[typed]{N}{n}','The lower-case n has typewriter serifs and is typed over a capital N; it is not handwritten.'),
(r'\inserted{espérer}',r'\inserted[typed]{espérer}','Espérer is typed interlinearly, with a pen anchor that does not cancel pouvoir.'),
(r'\unsure{\hand{+1)}}',r'\hand{+1)}','The handwritten plus sign, numeral 1 and closing parenthesis are all clear. The following baseline full stop is retained.'),
(r'\xout{\illegible{2}}',r'\xout{telles quelles}','The cancelled phrase is recoverable as telles quelles, with the feminine endings visible beneath the typed x impressions.'),
(r'\xout{\unsure{équivalence}}',r'\xout{équivalence}','The whole word is legible beneath the cancellation, including the accented initial letter.'),
(r'\inserted{équivalente à}',r'\inserted[typed]{équivalente à}','The inserted phrase is typed above the line; the pen curve only gives its anchor.'),
(r'ensemble\hand{s}',r'ensemble\inserted[typed]{s}','The added s is typed above the line, rather than drawn in pen.'),
(r'yoga\inserted{général}',r'yoga \inserted[typed]{général}','Général is typed interlinearly and separated from yoga.'),
(r'\margin{44}',r'\margin{\hand{44}}','The archive number is handwritten in pencil.')
],doubts={'unsure':[
(r'\hand{+1)}','doubt resolved','All three pen characters are legible.'),
('équivalence','doubt resolved','The word remains readable through the typed x cancellation.')
],'illegible':[
(r'\over{\illegible{1}}{ca}','illegible retained','The ca correction is clear, but the densely inked old letters cannot be completely recovered.'),
('telles quelles','illegible resolved','The two cancelled words are legible, including their feminine endings, before the live replacement tels quels.')
]},notes=[
'The author folio 29 is penned and the lower-left archive 44 is in pencil.',
'The guide curves insert de plus and typed espérer. Neither un homomorphisme nor pouvoir is cancelled.',
'A typed lower-case n is superposed on N; the provenance is corrected accordingly.',
'The oblique stroke before qui is a word-spacing instruction; its graphic remains diplomatic and an explicit master variant applies a space.',
'The older letters under ca remain illegible.',
'The pen sequence +1) is fully legible; the following dot is a distinct baseline full stop and remains.',
'The cancellations read telles quelles and équivalence. Both are recovered rather than silently dropped.',
'The pi, inequality and infinity signs remain marked as handwritten. The interlinear words espérer, équivalente à, général and the added final s are typed.'
],summary='Both scan halves and six enlarged details inspected. Recovered the cancelled telles quelles and équivalence, resolved +1), corrected the typed N-to-n overprint and four interlinear provenance assignments, and retained the illegible undertext of ca. The spacing stroke before qui has an explicit applied variant. Clipped right-edge line ends remain as supplied; no hidden letters are invented.',differences={
668:(r"i=\over[typed]{N}{n}+1''",'the typescript reads as our transcription','The closing quotation after the formula is visible and omitted from the witness.'),
670:('0 <= i <= n with closing quotation','the typescript reads as our transcription','The source explicitly closes the quotation after n.'),
674:(r"n\hand{+1)}.s'interprète",'our transcription corrected','The image settles +1) as pen writing. Its following full stop is distinct and is not removed to match the witness.'),
675:('dans le langage','the typescript reads as our transcription','The typed article is le.'),
680:(r'\hand{\infty}-équivalence','the typescript reads as our transcription','The source separator is a hyphen, not the witness full stop.')
})
v.append(dict(key=k,before=r'flèches\hand{\textbackslash}``qui',after=r'flèches ``qui',kind='author spacing cue',reason='Apply the oblique pen stroke as the missing word space before the opening quotation; retain the graphic diplomatically.',source_id='SPACE:044:1'))
p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
