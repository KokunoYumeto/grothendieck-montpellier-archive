from review_root import review
from pathlib import Path
import json
k='ps_134-2_035'
review(k,changes=[
(r'\mspage{27}',r'\mspage{\hand{21}}','The centered handwritten folio is 21, not 27.'),
(r'(such as hh: $f\to g$',r'\hand{(}such as hh: $f\hand{\to} g$','The opening parenthesis and arrow are penned; the two baseline h letters are separately typed.'),
(r'\deleted{as} as',r'\deleted{as} \hand{as}','The second live as is handwritten, after the cancelled typed as.'),
(r'\xout{\illegible{1}} Thus',r'\xout{Such} Thus','Such is legible under the typewriter x impressions.'),
(r'inde-% \margin{(13!) false, see PS}',r'inde-%','This marginal-note command was hidden after the TeX comment sign; it is restored at its visible body call by the next recorded change.'),
(r'amalgamation.\hand{(13)}',r'amalgamation.\hand{(13!)}\margin{\unsure{(13!) false, see PS}}','The call includes an exclamation mark. The full visible marginal note is restored here; its wording is clear, while its light crossing hatching leaves cancellation status uncertain.'),
(r'\margin{(14!), false, see below}',r'\margin{\unsure{(19!), false, see below}}','The digit is 9, independently confirmed from the closed loop and descender. The broad pencil hatching leaves the status of the otherwise readable note uncertain.'),
(r'\hand{(14)})',r'\hand{(19!)})','The corresponding body call also reads 19 followed by an exclamation, independently confirmed.'),
(r'\xout{\unsure{and the $F_i$}}',r'\xout{and the $F_i$}','The cancelled phrase and the F_i is legible; the capital is F, not R.'),
(r'$i\geq 1$',r'$i\hand{\geq} 1$','The inequality sign in this range is penned.'),
(r'$(\underline{F}_i)_{i\in\underline{N}}$ and of the maps $(\underline{s}^i_1)_{i\geq 1}$ and $(\underline{t}^i_1)_{i\geq 1}$',r'$(\underline{F}_i)_{i\hand{\in}\underline{N}}$ and of the maps $(\underline{s}^i_1)_{i\hand{\geq} 1}$ and $(\underline{t}^i_1)_{i\hand{\geq} 1}$','The membership sign and the two inequality signs are hand drawn; letters and indices are typed.'),
(r'primiti\deleted{\unsure{y}}\inserted{ve}',r'primiti\deleted{y}\inserted[typed]{ve}','The old letter is y, clearly cancelled; its replacement ve is typed above the line, with a pen insertion curve.'),
(r'\deleted{amalgamation}\inserted{fiber products}',r'\deleted{amalgamation}\inserted[typed]{fiber products}','This later replacement fiber products is typed interlinear text, unlike the earlier handwritten replacement at the page top.'),
(r'\margin{(25.2.) (20!) this may give however \uline{two} large a subcategory $\underline{C}_{n+1}$}',r'\margin{\unsure{(25.2.) (20!) this may give however \uline{two} large a subcategory $\underline{C}_{n+1}$}}','The literal underlined word is two, not too. The wording is clear, but crossing hatching leaves the note cancellation status uncertain.'),
(r'$h\colon K\to \underline{F}_i$ $(i\geq 1)$',r'$h\colon K\hand{\to} \underline{F}_i$ $(i\hand{\geq} 1)$','The arrow and range inequality are handwritten.'),
(r'fibered products.\hand{(20)}',r'fibered products.\hand{(20!)}','The body call after products includes the separate exclamation mark.'),
(r'an\inserted{intrinsic}',r'an \inserted[typed]{intrinsic}','Intrinsic is typed above the line and constitutes a separate word after an.'),
(r'\inserted{(nor even automorphisms)}',r'\margin{\deleted{nor even automorphisms}}\inserted{(nor even automorphisms)}','The cancelled marginal version is restored at the live interlinear repetition; it was previously lost inside a TeX comment.'),
(r'tha\xout{\unsure{q}}t',r'th\over[typed]{q}{a}t','The a is typed over q in the same cell. There is no separately spaced extra q to delete.'),
(r'induc-% \margin{\deleted{nor even automorphisms}}',r'induc-%','Removed the now-restored note command from the TeX comment, where it could never print.'),
(r'$h\colon f\to g$',r'$h\colon f\hand{\to} g$','The homotopy arrow is handwritten.'),
(r'$h\colon \underline{F}_i\to \underline{F}_i$',r'$h\colon \underline{F}_i\hand{\to} \underline{F}_i$','The endomorphism arrow is handwritten; the subsequent source conditions literally use f and are preserved.')
],doubts={'unsure':[
(r'\xout{\unsure{m}}','doubt retained','The cancellation in recomvered obscures its underletter; m is plausible but not independently secure.'),
(r'\xout{and the $F_i$}','doubt resolved','All words and the F are readable beneath the x impressions.'),
(r'\deleted{y}','doubt resolved','The old y beneath the typed ve is legible.'),
(r'\over[typed]{q}{a}','doubt resolved','The old q and superposed a share one typed cell; the correction mechanism was misrepresented as deletion of a separate letter.')
],'illegible':[
(r'\xout{Such}','illegible resolved','The cancelled word before Thus reads Such.'),
(r'\deleted{\illegible{1}}','illegible retained','The dense black blob following the handwritten products does not yield secure undertext.')
]},notes=[
'The opening parenthesis is pen. Two separate h letters are typed before the colon; the arrow is pen. The doubled h is retained diplomatically and separately recorded as a one-off correction.',
'The earlier as is cancelled and the later as is handwritten.',
'The cancelled word before Thus is Such.',
'The blot following handwritten products remains illegible. The cancelled letter in recomvered remains uncertain as m.',
'The cancelled phrase is and the F_i; the capital is F.',
'The membership sign and the range inequalities are handwritten, with typed variables and indices.',
'The old y is readable. The inserted ve is typed, not handwritten.',
'The marginal note explicitly underlines two. Its hatching status remains uncertain, and its wording is not paraphrased to the witness footnote.',
'The small tick above structure is present but does not yield an additional letter. In that, a is typed over q in one cell, rather than q being a separate cancelled character.',
'The lower-left 35 is the archive number and remains marginal.'
],summary='Both scan halves and enlarged details inspected; marginal and body call 19 independently checked. Recovered Such, and the F_i, and the old y; corrected typed insertion provenance and same-cell q-to-a overwriting. Restored two marginal notes hidden inside TeX comments. Uncertain hatching status is marked for the three otherwise legible objections. Section 13 continues onto site 36.',differences={
451:('hh:','the typescript reads as our transcription','Two h letters are separately typed. The corrected forms remove this doubled variable only by an explicit one-off-slip variant supported by the single h used for the same homotopy on this page.'),
453:(r'amalgamation.\hand{(13!)}; (13!) false, see PS','our transcription corrected','The body call is after amalgamation, not after products. Its exclamation mark is restored and the commented-out source marginal note is restored to a live anchor.'),
455:(r'\hand{(19!)}; (19!), false, see below','our transcription corrected','Both calls read 19!, confirmed by a second reader. The source wording is retained, rather than the witness expanded This is false, as seen below.'),
458:(r'$\underline{F}_{i+1}$','the typescript reads as our transcription','The visible index is i+1. Its mismatch with the preceding pair F_i and F_{i-1} is discussed in the guide, not corrected in the readers.'),
460:('the system of the objects','the typescript reads as our transcription','The second the is visibly typed; the witness omits it.'),
462:(r'primiti\deleted{y}\inserted[typed]{ve}','our transcription corrected','The replacement is typed interlinear text and the old y is readable.'),
464:(r'\deleted{amalgamation}\inserted[typed]{fiber products}','our transcription corrected','The inserted phrase has typewriter forms and is not handwritten.'),
465:(r'$t^i_1 h$','the typescript reads as our transcription','No underline appears beneath this t, although the preceding s is underlined. No notation is silently harmonized.'),
466:(r'\hand{(20!)}; (25.2.) (20!) this may give however \uline{two} large a subcategory $\underline{C}_{n+1}$','our transcription corrected','The call includes an exclamation mark; the dated marginal wording and literal two are preserved with uncertain hatching status.'),
467:(r'an \inserted[typed]{intrinsic}','our transcription corrected','The word is typed interlinear text. A word boundary after an is restored.'),
469:('auomorphisms','the typescript reads as our transcription','The source omits the t. The same word automorphisms is clear elsewhere on this page; an explicit one-off-slip variant supplies t only in the corrected forms.'),
472:(r'\margin{\deleted{nor even automorphisms}}\inserted{(nor even automorphisms)}','our transcription corrected','The live repetition begins with lower-case nor. The cancelled marginal precursor is restored from the hidden TeX comment and retained diplomatically.')
})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json';v=json.loads(p.read_text())
v=[x for x in v if x.get('source_id') not in ['DIFF:451','DIFF:469']]
v.extend([
dict(key=k,before='such as hh:',after='such as h:',kind='slip corrected',reason='One-off doubled variable before the homotopy colon; the same homotopy is denoted by a single h later on this checked page.',source_id='DIFF:451'),
dict(key=k,before='auomorphisms',after='automorphisms',kind='slip corrected',reason='One-off omitted t; the complete word is clearly typed several times on this same checked page.',source_id='DIFF:469')])
p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
