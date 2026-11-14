from review_root import review
from pathlib import Path
import json
k='ps_134-2_047'
review(k,changes=[
(r'\unsure{\hand{qui}|qui}',r'\hand{qui}','The dark, irregular letters are penned over the baseline; the live word qui is legible.'),
(r"géom\unsure{\over{e}{é}|é}trie",r"géo\'{m}étrie",'The enlarged word has three typed acute accents: over the first e, over m, and over the second e. Preserve the extra accent over m and resolve the second e as typed é.'),
(r'\margin{47}',r'\margin{\hand{47}}','The archive number is in pencil.')
],doubts={'unsure':[
(r'\hand{qui}','doubt resolved','The live word is handwritten and all three letters are readable; no separate older word is securely recoverable.'),
(r"géo\'{m}étrie",'doubt resolved','The second e has a typed acute matching the other typed accent impressions. An additional typed acute above m was omitted and is restored.')
],'illegible':[]},notes=[
'The folio reads 32 in pen. Its final digit is retraced, but no different earlier digit can be separately identified.',
'Qui is a legible handwritten word over the line, without a separately recoverable older word.',
'The terminal t of forment is penned. The following long stroke is a word-separation instruction, retained graphically and applied as a space in the corrected forms.',
'There are three typed acute accents in the word: the extra one above m is now represented literally, and the second é is resolved as typed.',
'Corps, ne and rait remain readable despite overtyping; no independently recoverable older word is invented.',
'The lower-left 47 is the handwritten archive number.'
],summary='Both scan halves and enlarged qui and accent details inspected. Resolved handwritten qui, restored the extra typed acute over m in géométrie, and resolved the second e accent as typed. The terminal t and following pen spacing stroke are preserved, with a separate applied space variant. The signature A.G. is present; the lower half is otherwise blank.',differences={
743:(r'groupe topologique\deleted{,}\inserted{etc)} \hand{qui}','our transcription corrected','The live qui is plainly handwritten; the cancellation and insertion remain as represented.'),
744:(r'formen\hand{t}\hand{/}guère','the typescript reads as our transcription','The t and spacing stroke are handwritten; a master variant applies the indicated space without retaining a slash as prose.'),
746:(r'\hand{A.G.}','the typescript reads as our transcription','The handwritten closing initials are visible and omitted from the witness.')
})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json';v=json.loads(p.read_text());v=[x for x in v if x.get('source_id') not in ['SPACE:047:1','SPACE:048:1','SPACE:048:2']]
v.append(dict(key=k,before=r'formen\hand{t}\hand{/}guère',after=r'formen\hand{t} guère',kind='author spacing cue',reason='The long pen stroke separates forment from guère; apply a space while retaining the graphic diplomatically.',source_id='SPACE:047:1'))

k='ps_134-2_048'
review(k,changes=[
(r'\mspage{33}',r'\mspage{\hand{33}}','The centered folio is handwritten.'),
(r'\unsure{App.6|Appr.6}',r'App.6','The label contains A and two p letters followed by the dot and 6; there is no extra r.'),
(r'\xout{xxxxxxxxxx}',r'\xout{pro-\illegible{1}}','The cancellation covers a typed word beginning pro-. The surviving prefix is clear, but the rest cannot be recovered without supplying hidden letters; the old transcription had represented only the cancelling x impressions.'),
(r"\hand{\unsure{''}}",r'\hand{\unsure{*}»}','The right double-angle quotation mark is clear. The preceding dark star-like mark remains uncertain in identity and function.'),
(r'cas \unsure{F} non',r'cas \hand{F} non','The letter F is clearly visible and reinforced in pen; it is not cancelled.'),
(r'f: X $\longrightarrow$ Y',r'f: X $\hand{\longrightarrow}$ Y','The arrow is drawn in pen.'),
(r'\xrightarrow{\hand{$\sim$}}',r'\hand{\xrightarrow{\sim}}','Both the arrow and its tilde are handwritten, not only the tilde.'),
(r'\hand{$\mathcal{F}$}(Y) $\longrightarrow$\hand{$\mathcal{F}$}(X)',r'\hand{$\mathcal{F}$}(Y) $\hand{\longrightarrow}$\hand{$\mathcal{F}$}(X)','The comparison arrow between section categories is handwritten.'),
(r'\hand{$\mathcal{F}$}(Y) $\longrightarrow$ f',r'\hand{$\mathcal{F}$}(Y) $\hand{\longrightarrow}$ f','The arrow in condition A is handwritten.'),
(r'\hand{$\mathcal{F}$}$\longrightarrow$ f',r'\hand{$\mathcal{F}$}$\hand{\longrightarrow}$ f','The arrow in condition B is handwritten.'),
(r'\margin{48}',r'\margin{\hand{48}}','The lower-left archive number is written in pencil.')
],doubts={'unsure':[
('App.6','doubt resolved','The section label is legible as App.6, without an additional r.'),
(r'\hand{\unsure{*}»}','doubt narrowed','The closing double-angle quote is clear; its preceding star-like dark mark remains doubtful.'),
(r'\hand{F}','doubt resolved','The F is legible and live; the dark strokes reinforce it rather than cancel it.')
],'illegible':[]},notes=[
'The inequalities, tilde and arrows are handwritten. Arrow provenance is now explicitly marked where the original source had marked only the tilde or endpoints.',
'The closing mark is a right double-angle quotation mark preceded by an uncertain star-like blot; the latter remains marked.',
'The bold F is live and penned/retouched, not struck out.',
'The marginal call reads App.6; there is no extra r.',
'The two separation strokes after son and une remain diplomatic, with explicit master variants applying spaces before the quoted phrases.',
'The à following ou encore is typed and slightly high; it is not a handwritten insertion.',
'Both the centered 33 and the archive 48 are handwritten; their distinct foliation roles are preserved.'
],summary='Both scan halves and enlarged label, F, quotation and cancellation details inspected. Resolved App.6 and live penned F, narrowed the closing-quote doubt, recovered the prefix pro- beneath the long typewriter cancellation without inventing its unreadable remainder, and marked all omitted pen arrows. The source salutation is Cher Larry, and condition A says localement constant. All mathematical indices and the calligraphic F symbols are preserved.',differences={
747:('Cher Larry,','the typescript reads as our transcription','Larry is clearly typed; the witness changes the addressee form to Breen.'),
749:('no descriptive heading','the typescript reads as our transcription','The image has a numbered handwritten call only; the witness supplies a descriptive heading.'),
750:(r'\margin{(App.6)}','our transcription corrected','The call is resolved as App.6 and retained in marginal form.'),
757:(r'cas \hand{F} non commutatif','our transcription corrected','The F is present and not cancelled, contrary to its omission from the witness.'),
758:(r'\hand{$\mathcal{F}$}','the typescript reads as our transcription','The n-gerbe symbol is a large calligraphic handwritten F, distinguished from the preceding ordinary coefficient-sheaf F.'),
763:('localement constant','the typescript reads as our transcription','The word contains s; the witness contant is unsupported.'),
764:('est une n-équivalence with no semicolon','the typescript reads as our transcription','The end of condition A has no typed semicolon.')
})
for n,b,a in [(1,r'son\hand{|}``type',r'son ``type'),(2,r'une\hand{|}``équivalence',r'une ``équivalence')]:
 v.append(dict(key=k,before=b,after=a,kind='author spacing cue',reason='Apply the pen separator as a space before the quotation, preserving the graphic in the diplomatic form.',source_id=f'SPACE:048:{n}'))
p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
