from review_root import review
from pathlib import Path
import json

k='ps_134-2_029'
cue=r'\margin{\diagram{\begin{tikzpicture}\draw (0,0)--(.32,0)--(.32,.27)--(.68,.27);\end{tikzpicture}}}'
review(k,changes=[
    (r"\mspage{\unsure{\#5|8'}}",r'\mspage{\hand{\unsure{1|\#}5}}','The final 5 is clear; the heavily retraced first mark could be 1 or a hash-like overprint. The old alternative 8-prime is unsupported.'),
    (r'deduce\unsure{s|d}',r'deduce\over{s}{d}','A pen d corrects the typed final s.'),
    (r'$h: K \to F_i$',r'$h: K \hand{\to} F_i$','The arrow is drawn by hand. The literal index i is retained despite the preceding page i+1.'),
    (r'\inserted{the bunch of}',r'\inserted[typed]{the bunch of}','The interlinear words have typewriter forms; the surrounding insertion curve is pen.'),
    (r'\margin{this has to be corrected -- amalgamated sums exist in \unsure{$C_\infty$} only, and these sho\unsure{uld} be respected}',r'\margin{\unsure{this has to be corrected -- amalgamated sums exist in $\underline{C}_o$ only, and \uline{\unsure{those|these}} \unsure{sh\textsuperscript{d}|sh\textsuperscript{ld}} be respected}}','The subscript is one round o beneath an underlined C, independently confirmed by a second reader. The underlined demonstrative and abbreviated sh with raised ending remain uncertain. The outer doubt records the uncertain status of the pencil hatching.'),
    (r'\inserted{(14)}',r'\inserted{(14!)}','The call is 14 followed by an exclamation mark.'),
    (r'\xout{xxxxxxx}',r'\xout{\unsure{version}}','The cancelled seven-letter word appears to be version; overlapping x strokes prevent a certain reading.'),
    (r'associat\unsure{i}ng',r'associating','The dotted i is visible and the word is secure.'),
    (r'\inserted{finite}',r'\inserted[typed]{finite}','Finite is a typed interlinear addition.'),
    (r'\xout{xxxxxxxxxxx}',r'\xout{an isomorphism}','The cancelled wording beneath the typed a homotopy is legibly an isomorphism.'),
    (r'\varinjlim',r'\mathop{\mathrm{lim}}\limits_{\hand{\longrightarrow}}','The letters lim are typed; the rightward arrow underneath is penned.'),
    (r'\inserted{implicit} \unsure{fact}',r'\inserted[typed]{implicit} fact','Implicit is typed above the line. The apparent strike on fact belongs to the insertion curve; fact remains live.'),
    (r'mute to these\inserted{(13)}.',r'mute to these\inserted{(13!)}.','The first call to 13 includes an exclamation mark.'),
    (r'fiberproducts\over{,}{)}\inserted{(13)},',r'fiberproducts\over{,}{)}\inserted{(13!)},','The second call to 13 also includes an exclamation mark.'),
    (r'\hand{$\ulcorner$}',cue,'The source has a stepped paragraph cue, rather than the mathematical corner symbol supplied by the initial transcription.'),
    (r'\deleted{\unsure{assuming}}',r'\deleted{assuming}','Assuming is clearly legible under the pen cancellation.'),
    (r'e\over{\illegible{1}}{q}uivalent',r'e\over[typed]{\illegible{1}}{q}uivalent','The replacement q is a typewriter overprint; its underlying character remains illegible.')
],doubts={'unsure':[
    (r'\mspage{\hand{\unsure{1|\#}5}}','doubt narrowed','Only the heavily retraced first mark remains uncertain. The second digit is 5; 8-prime is not supported.'),
    (r'deduce\over{s}{d}','doubt resolved','The pen d and typed s can be distinguished.'),
    (r'$\underline{C}_o$','doubt resolved','The subscript is a single round o, not an infinity sign; the capital has a visible underline.'),
    (r'\unsure{sh\textsuperscript{d}|sh\textsuperscript{ld}}','doubt retained','The source abbreviates the word after sh with a raised ending. No complete baseline ould is visible, so expansion to should is not certified.'),
    ('associating','doubt resolved','The i is legible.'),
    ('fact','doubt resolved','Fact is live; the crossing line belongs to the insertion mark for implicit.'),
    (r'\deleted{assuming}','doubt resolved','The cancelled typed word is assuming.')
],'illegible':[
    (r'\deleted{\illegible{1}}','illegible retained','The blot before the inserted references conceals the old text.'),
    (r'\over{\illegible{1}}{A}','illegible retained','The heavy handwritten A conceals its underlying character.'),
    (r'\deleted{\illegible{1}}','illegible retained','The cancellation after products of arrows is not securely recoverable.'),
    (r'\over{\illegible{1}}{two}','illegible retained','The underlying text below the first handwritten two remains obscured within the cancelled phrase.'),
    (r'\deleted{\illegible{1}}','illegible retained','The short deletion after family cannot be read securely; no contextual word is supplied.'),
    (r'\over{\illegible{1}}{h}','illegible retained','The old letter under the pen h of technical is too overworked to identify.'),
    (r'\deleted{\illegible{1}}','illegible retained','The small cancellation at the end of the belongs clause is not recoverable.'),
    (r'\over[typed]{\illegible{1}}{q}','illegible retained','The old letter beneath the typed q remains obscured.')
]},notes=[
    'The final digit of the centered handwritten folio is 5. Its first heavily retraced mark remains 1-or-hash-like; sequence alone is not used to certify 15.',
    'The first line changes typed deduces to deduced by a handwritten d.',
    'The earlier matter beneath the blot and handwritten A remains illegible, while both inserted references (1),(2) are retained.',
    'Both the cancelled and live versions of two ways of remain. The typed undertext beneath the first two is still illegible; associating is secure.',
    'The marginal subscript is a single o under an underlined C. The demonstrative remains those-or-these and the following abbreviation sh with raised d-or-ld remains unexpanded. The hatching status is separately marked uncertain.',
    'Implicit is typed interlinear text and fact is not cancelled.',
    'The small vertical pen stroke after C_n\'s is clearly present; its function is not inferred.',
    'All three calls include exclamation marks: (14!), (13!), and (13!).',
    'The source approximates membership with typewriter strokes in both displayed inline relations; the mathematical encoding as membership is retained.'
],summary='Both supplied halves and enlarged details inspected. Corrected d-over-s, typed interlinear provenance, the marginal C_o, all three exclamation-mark calls, and the stepped paragraph cue. Recovered the cancelled an isomorphism and assuming; retained the abbreviated marginal word and other unresolved undertext. A second reader independently checked the marginal C_o, demonstrative and abbreviation.',differences={
    303:(r'\inserted[typed]{the bunch of}','our transcription corrected','The words are present but are typed above the line, not handwritten.'),
    304:(r'\inserted{(1),(2)}','the typescript reads as our transcription','Both numbered relations are visible; the witness cites only the second.'),
    306:(r'\inserted{(14!)}','our transcription corrected','The source has the handwritten call (14!), not the expanded witness footnote.'),
    308:(r'$\underline{C}_o$; \unsure{those|these}; \unsure{sh\textsuperscript{d}|sh\textsuperscript{ld}}','our transcription corrected','The scan names C_o. The demonstrative and abbreviated raised ending remain doubtful; should is not supplied as certain text. The source note is retained at its anchor.'),
    309:(r'\deleted{can}\inserted{may}','the typescript reads as our transcription','Can is struck out and replaced by handwritten may; the witness retains can.'),
    313:(r"\hand{``}standar\over{t}{d}\hand{''}",'the typescript reads as our transcription','The author adds quotation marks around standard; the witness drops them.'),
    316:('at all a sense','the typescript reads as our transcription','The article a is visibly typed and omitted in the witness.'),
    321:(r'\inserted{(13!)}','our transcription corrected','The call includes an exclamation mark and is absent from the witness text.'),
    323:('having same objects','the typescript reads as our transcription','There is no the in this phrase.'),
    324:(r"\over{,}{(}and ``same'' fiberproducts\over{,}{)}",'the typescript reads as our transcription','The author replaces commas by parentheses but does not insert the before same.'),
    327:(r'\inserted{(13!)}','our transcription corrected','The second call after fiberproducts includes an exclamation mark.'),
    328:(r'sequence $(C_n)$','the typescript reads as our transcription','The C in this specific sequence is not underlined on the scan.'),
    331:(cue,'our transcription corrected','The stepped pen cue requests a paragraph boundary. It is drawn in the diplomatic reader and applied in the corrected readers.'),
    335:(r'e\over[typed]{\illegible{1}}{q}uivalent','our transcription corrected','The q is a typewriter overprint; the old character remains illegible.')
})

variant_path=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json'
variants=json.loads(variant_path.read_text()) if variant_path.exists() else []
variants=[v for v in variants if v.get('source_id')!='DIFF:331']
variants.append(dict(key=k,before=cue+'It is fairly obvious',after='\n\nIt is fairly obvious',kind='author paragraph break',reason='The stepped pen cue at this boundary instructs a new paragraph; the diplomatic text retains its graphic.',source_id='DIFF:331'))
variant_path.write_text(json.dumps(variants,ensure_ascii=False,indent=2)+'\n')
