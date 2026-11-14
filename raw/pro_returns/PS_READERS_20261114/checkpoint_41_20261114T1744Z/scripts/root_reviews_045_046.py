from review_root import review
from pathlib import Path
import json
k='ps_134-2_045'
space45=r'\margin{\(\uparrow\) espace \(\downarrow\)}'
review(k,changes=[
(r'Je \xout{\illegible{1}}',r'Je \xout{\unsure{vois}}','The last three letters ois are recoverable, and the leading cancelled character plausibly reads v; retain uncertainty about the complete word.'),
(r'\margin{espace}',space45,'The spacing instruction has both an upward and a downward arrow spanning the section boundary; restore both graphics.'),
(r"d'image directe\inserted{$Lf_*(K.)$,}",r"d'image directe \inserted[typed]{$Lf\hand{_*}(K.)$,}",'The interlinear expression is typed, with its subscript star added by hand; add the visible word boundary.'),
(r'P\over{\unsure{q}}{o}stnikoff',r'P\over[typed]{\unsure{q|g}}{o}stnikoff','The live o is typed. A descender from the old letter is visible, but it does not securely distinguish q from g.'),
(r'\xout{\unsure{en termes de n-champs}}',r'\xout{en termes de n-champs}','The full phrase is recoverable beneath the typed x impressions.'),
(r'\margin{45}',r'\margin{\hand{45}}','The lower-left archive number is in pencil.')
],doubts={'unsure':[
(r'\xout{\unsure{-1}}','doubt retained','The numeral-like final stroke is present, but the first cancelled sign remains too covered to settle the whole -1 reading.'),
(r'\xout{\unsure{e}}','doubt retained','The cancelled terminal character is heavily covered by x impressions.'),
(r'\unsure{fordu|tordu}','doubt retained','The first pen letter has a long descending stem and cross-stroke compatible with either the transcribed f or the intended t; the image alone does not settle it.'),
(r'\xout{\unsure{e}}','doubt retained','The cancelled letter after un remains obscured. Its grammatical awkwardness is not repaired.'),
(r'\over{\unsure{p}}{p}','doubt retained','The live penned p is clear but the older letter is substantially covered.'),
(r'\over[typed]{\unsure{q|g}}{o}','doubt retained','The old descender could belong to q or g; the typed live o is clear.'),
('en termes de n-champs','doubt resolved','The full cancelled phrase is readable under the typewriter x pattern.')
],'illegible':[
(r'\xout{\unsure{vois}}','illegible narrowed','The ending ois is visible and the leading character plausibly v, but it remains marked because cancellation covers its identifying strokes.'),
(r'\xout{\illegible{1}}','illegible retained','The word between évidente and correspond is mostly covered by cancelling impressions; no complete reading is secure.'),
(r'\xout{\illegible{1}}','illegible retained','The short cancelled word after inversement is too heavily overtyped to recover.')
]},notes=[
'Both 30 and 45 are handwritten; the former is author foliation and the latter archive numbering.',
'The cancelled -1 after n remains doubtful under its x cancellation.',
'The cancelled word after Je is tentatively recoverable as vois; the first letter remains uncertain.',
'The final e of origine is overtyped but legible; no different live letter is visible.',
'The interlinear (n+1) is typed and cancelled, and belongs above the product expression. It remains separately recorded from the live pen correction of n-fibré to (n+1)-fibré.',
'The first letter of fordu/tordu remains uncertain. The stroke beneath liée is the lower bend of the marginal spacing arrow, not an underline of the word.',
'The cancelled phrase before doivent clearly reads en termes de n-champs.',
'The tiny isolated mark above naive has no securely identifiable lexical content; no letter or punctuation is invented from it.'
],summary='Both scan halves and nine enlarged details inspected. Narrowed the cancelled word after Je to doubtful vois, recovered en termes de n-champs, distinguished typed Lf(K.) from its hand-added star, retained the old descender uncertainty in Postnikoff, and restored the spacing arrows. The source inverse-image sentence and its full account of simplicial sheaves differ substantively from the witness. Both original uncertain cancelled e characters remain, including the awkward un certaine mesure.',differences={
688:(r"C $\hand{\to}$C'",'the typescript reads as our transcription','The source category letter is capital C, not the witness lower-case c.'),
695:(r'\hand{(App.\,4)}','the typescript reads as our transcription','The source has only the numbered handwritten call, not the witness descriptive heading.'),
696:(space45,'our transcription corrected','The source contains espace and two opposed arrows. The original transcription omitted the arrows; a master variant applies their spacing instruction.'),
698:('construite en termes de la notion de faisceau semi-simplicial sur X','the typescript reads as our transcription','The full phrase specifies the simplicial-sheaf side of the relative comparison and is absent from the witness.'),
701:(r"correspond à la notion \over{\unsure{p}}{p}lus subtile d'image inverse de n-champs; et inversement",'the typescript reads as our transcription','The source compares inverse image of simplicial sheaves with inverse image of n-stacks. The witness substitutes direct image and reverses the stated comparison.'),
703:(r"d'image directe \inserted[typed]{$Lf\hand{_*}(K.)$,}",'our transcription corrected','The inserted expression is predominantly typed; the subscript star is handwritten. Its comma is visible.'),
704:('sans doute','the typescript reads as our transcription','There is no extra a after sans.'),
712:('devrait être noté','the typescript reads as our transcription','The final e bears its visible acute accent.')
})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json';v=json.loads(p.read_text());v=[x for x in v if x.get('source_id') not in ['SPACE:045:1','SPACE:046:1']]
v.append(dict(key=k,before=space45,after=r'\par\medskip',kind='author spacing cue',reason='Apply the opposed arrows and espace instruction as additional separation before App.4, preserving the drawing diplomatically.',source_id='SPACE:045:1'))

k='ps_134-2_046'
space46=r'\margin{\(\uparrow\) espacer \(\downarrow\)}'
review(k,changes=[
(r'\mspage{31}',r'\mspage{\hand{31}}','The centered folio is penned.'),
(r'Giraud$_{\unsure{x}}$',r'Giraud$_x$','The lowered typewriter x is clearly visible and is retained as a literal extra mark.'),
(r'n-groupoide\inserted{C}',r'n-groupoide \inserted{C}','The inserted C is a separate mathematical object name.'),
(r"qu'i\unsure{l}",r"qu'i\unsure{l|b}",'The final cell has a tall l-like stem together with a b-like bowl. Keep both readings under the visible overprinting.'),
(r'\margin{\unsure{(\ \ )}}',r'\margin{\hand{(\quad)}}','Both faint pencil parentheses are visible; their interior is empty and no content is supplied.'),
(r'\margin{espacer}',space46,'The pen spacing instruction includes an upward arrow and a downward arrow; restore both omitted graphics.'),
(r'\inserted{(App.5)}La',r'\inserted{(App.5)} La','The inserted section call is separated from the following word.'),
(r'\unsure{algèbtre|algèbre}',r'algèb\unsure{\over[typed]{t}{r}}e','The t/r shapes occupy one overtyped cell, not two successive characters. Their exact layer order remains uncertain.'),
(r"qu\unsure{'}on \deleted{\illegible{1}}",r"qu\deleted{\unsure{p}}'on \deleted{p}",'The apostrophe is clear. A heavily cancelled p-like character precedes it, while a second cancelled p after on is legible; preserve both cancellation sites.'),
(r"\hand{vocable}n'est",r"\hand{vocable} n'est",'The inserted vocable is a separate word; restore its following space.'),
(r'\margin{46}',r'\margin{\hand{46}}','The archive number is handwritten in pencil.')
],doubts={'unsure':[
('x','doubt resolved','The lowered character has a clear typewriter x shape.'),
(r"\over{\unsure{e}}{'}",'doubt retained','The handwritten apostrophe is clear, but the covered older character remains unresolvable.'),
(r'\unsure{l|b}','doubt retained','The overtyped terminal cell has both a tall stem and a b-like bowl; no single live letter is secure.'),
(r'\hand{(\quad)}','doubt resolved','Two faint pencil parentheses are visible, with an empty interior.'),
(r'algèb\unsure{\over[typed]{t}{r}}e','doubt narrowed','The disputed characters are superposed in one cell; the layer order remains uncertain.'),
(r'\unsure{groupoides}','doubt retained','The word is substantially overtyped and its full layered reading remains uncertain.'),
("'",'doubt resolved','The apostrophe itself is clear; the previously unrecorded cancelled character immediately before it is now separately marked as doubtful p.')
],'illegible':[
('p','illegible resolved','The cancelled letter after on has a clear stem, foot and bowl identifying p.')
]},notes=[
'The lowered mark after Giraud is a typed x, retained literally.',
'The old character beneath the apostrophe in l\'idée remains uncertain. The terminal cell of qu\'il/qu\'ib retains both l and b as alternatives.',
'The disputed t/r in algèbre occupies one overtyped cell; the source does not securely support two successive letters.',
'The dense groupoides remains doubtful. The apostrophe of qu\'on is clear; a cancelled p-like character before it is restored as doubtful, and the cancelled p after on is resolved. The small mark over notamment does not introduce an extra lexical character.',
'The faint right-edge pencil marks are empty parentheses; no hidden note is invented.',
'The centered 31 is handwritten, and the lower-left 46 is archive numbering in pencil.'
],summary='Both scan halves and six enlarged details inspected. Resolved the lowered x after Giraud, the empty pencil parentheses, the apostrophe in qu\'on and the following cancelled p; restored the previously unrecorded cancelled p-like character before that apostrophe. Narrowed the t/r overprint in algèbre and retained the l/b overprint and groupoides doubt. Restored spacing arrows and word boundaries. App.4 ends with the explicit Remords about classifying topoi; App.5 begins the proposed topological-algebra program.',differences={
715:('Giraud with lowered x','our transcription corrected','The x is clear on the image and omitted from the witness.'),
723:(r'\hand{$\pi$}$_n$ .\hand{)}','the typescript reads as our transcription','The malformed payload records punctuation order at the end of the classifying-topos parenthesis: the image has a full stop before the handwritten closing parenthesis, while the witness puts the stop after it. Pi is also handwritten. The unparsed item is thus located and settled without changing the source.'),
732:(space46,'our transcription corrected','Espacer and both opposed arrows are present; restore the omitted arrows and apply their separation through a master variant.'),
733:(r'\inserted{(App.5)}','the typescript reads as our transcription','The source gives a handwritten numbered call, without the witness descriptive heading.'),
735:('relations multiples','the typescript reads as our transcription','The source has a single enumeration and transition, without the witness repeated relations phrase.'),
736:('notamment','the typescript reads as our transcription','Both m letters are visibly typed.'),
737:('de faisceaux abéliens etc. (Les','the typescript reads as our transcription','The second etc. is present and omitted by the witness.'),
738:('envisagé...)','the typescript reads as our transcription','No extra full stop follows the closing parenthesis before C\'est.'),
741:(r'\hand{vocable}', 'the typescript reads as our transcription','The handwritten word is legible, rather than an empty placeholder.')
})
v.append(dict(key=k,before=space46,after=r'\par\medskip',kind='author spacing cue',reason='Apply espacer and its opposed arrows as additional paragraph separation before App.5; retain the drawing diplomatically.',source_id='SPACE:046:1'))
p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
