import json,re,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT

def commit(c):
 (OUT/'review_notes'/f"{c['key']}.json").write_text(json.dumps(c,ensure_ascii=False,indent=2))
 save_review(c)

key='ps_134-3_041'
s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for n,l in enumerate(s.splitlines(),1):
 a=re.sub(r'(?<!\\hand\{)\\(longrightarrow|to|in|neq|setminus|big\|)(?![A-Za-z])',lambda m:r'\hand{'+m[0]+'}',l)
 a=a.replace(r'\times',r'\mathrm{x}').replace(r'A^\wedge',r'A^{\hand{\wedge}}').replace(r'\xrightarrow{h}',r'\overset{h}{\hand{\longrightarrow}}')
 if a!=l:edits.append([l,a,f'At source line {n}, the arrows, restriction/complement signs and other specified mathematical signs are penned. The products are literal typewriter x characters, and the small presheaf carets are pen additions.'])
edits += [
 [r'f\big|C_u',r'f\hand{\big|}C_u','The second restriction bar in the first condition display is also a pen stroke, matching the first.'],
 [r'\over{\unsure{a}}{t}',r'\over{a}{t}','The old round a is visible below the correcting t in the.'],
 [r'\xout{\unsure{the}}',r'\xout{the}','The crossed letters are plainly the.'],
 [r'\xout{xxxxxxx}',r'\xout{where}','The first five underlying letters read where; the last two x strokes extend the cancellation beyond the old word and are not further text.'],
 [r'\over{\unsure{j}}{h}',r'\over{\unsure{n}}{h}','The base letter under the correcting h is one-humped and more plausibly n than j, but the overlapping lower stroke prevents certainty.'],
 [r'\over{\unsure{,}}{;}',r'\over{\unsure{,}}{:}','The live pen punctuation after checked consists of two vertically aligned dots, a colon; the older mark remains doubtful.'],
 [r'th\over{\unsure{a}}{e}n',r'th\over{a}{e}n','The lower loop of the old a is visible beneath the correcting e.'],
 [r'I\over{\unsure{d}}{n}deed',r'I\over{n}{n}deed','The typed letter is n, with a second pen n below it, rather than an old d.'],
 [r'\inserted{in A}',r'\inserted[typed]{in A}','The interlinear in A has typewriter letterforms; its curved placement mark is handwritten.'],
 [r'\over{\unsure{a}}{s}uch',r'\over{\unsure{f}}{s}uch','The underlying tall character looks f-like rather than a; it remains doubtful beneath the live s.'],
 [r'\over{\unsure{a}}{I}',r'\over{a}{I}','The original a has a visible round body and right stem beneath the capital I.'],
 [r'ce\over{\unsure{a}}{d}',r'ce\over{a}{d}','The old a remains distinguishable below the ascender added for d.'],
 [r'for any b in \over{\unsure{a}}{A}',r'for any b in \over{a}{A}','The old lowercase a is legible under the capital A correction.']
]
commit(dict(key=key,edits=edits,diffs={
2169:[r'[or ``sieve'']','The interlinear handwriting has actual square brackets and quotation marks.'],
2172:['y in C minus C_u','The word in is typed, not a membership symbol.'],
2176:['easily checked: for the left triangle','The enlarged live punctuation is two pen dots, i.e. a colon. The original transcription read it as a semicolon.','correct transcription'],
2182:[r'\inserted[typed]{in A}','The insertion is typed and its positioning curve is penned.','correct layer attribution'],
2183:['the element','The complete word element is typed.'],
2186:['replaced by I, a','The word ends d, not s.'],
2187:[r'A_{/a\mathrm{x}b}','The slice has slash, a, typed x and b; it is not the witness index x-times-b.'],
2189:[r'we are through\hand{!}','The final pen exclamation mark is retained at the right edge.']
},unsure=[
['a','The original a is visible underneath the live t.'],
[r'\unsure{;}','The compact dark punctuation after e_B remains too blotted to settle as a semicolon.'],
['the','The three cancelled letters are legible.'],
[r'\unsure{o}','The lower shape under the pen i could be o or another overtyped character; no secure base reading.'],
[r'\unsure{n}','The older body is n-like, but its lower overlap remains uncertain.'],
[r'\unsure{,}','The underlying comma-like stroke remains uncertain; the live replacement is a colon.'],
['a','The old a loop is visible beneath e.'],
[r'\unsure{,}','The mark after Fxe_i is entangled with the insertion stroke and may be a cancelled comma; do not settle its textual function.'],
['n','The printed n and the lower pen n are separable.'],
[r'\unsure{.}','The heavy punctuation before We is dot-like with a small tail; retain its uncertainty.'],
[r'\unsure{f}','The tall old character looks f-like but remains overlapped.'],
['a','The lowercase a under I is visible.'],
['a','The a under d is visible in ced.'],
[r'\unsure{a}','The character under the e correction in checking remains indistinct.'],
[r'\unsure{a}','The heavy A of the slice conceals the underlying letter.'],
['a','The lowercase a under the final capital A is legible.'],
[r'\unsure{1}','The old digit under the heavy 2 is not separable from its strokes.']
],illegible=[],notes=[
'The s of constant is overtyped but still s; no other live reading is justified.',
'The mark after Fxe_i remains entangled with the placement stroke and possibly cancelled; the doubt is retained.',
'The final ts of amounts are overtyped/retraced but both letters are legible; no word change.',
'The old a in the, then, I, ced and final A is legible; Indeed has typed n. The older in, The, such, checking, slice-A and T2 characters remain doubtful as documented separately.'
],evidence='Both halves inspected with an eighteen-detail sheet covering each doubtful overwritten character, punctuation mark and cancelled group. The construction extends f on the sieve C_u and uses the constant e_B functor on its complement. The restriction bars, backslash/complement marks and arrows are pen strokes, while every product x is typed. The cancelled group after arrows left reads where under the overstrike. The live punctuation after checked is a colon. The final argument visibly has A_/axb and condition T2, and retains the source slip asperic. Several old letters can be recovered; the unresolved base letters and the blotted punctuation remain marked rather than inferred from the proof.'))

key='ps_134-3_042'
commit(dict(key=key,edits=[
 [r'\inserted{gave to this notion}',r'\inserted[typed]{gave to this notion}','The upper replacement consists of monospaced typewriter letters; its pen curve places it before last week.'],
 [r'\deleted{\unsure{topos}}',r'\deleted{\xout{topos}}','The letters t-o-p-o-s are visible under machine x-overstrikes and an additional horizontal pen deletion.'],
 [r'$A^{\wedge}$',r'$A^{\hand{\wedge}}$','The small caret on A at the end of item 4 is handwritten.'],
 [r'F\over{\unsure{1}}{l}(M)',r'F\over{l}{l}(M)','The base character is a typed l with its top and bottom serifs; a diagonal pen stroke retraces it.'],
 [r'\inserted{general}',r'\inserted[typed]{general}','The word general above understanding is typed, with a handwritten insertion curve.'],
 [r'\xout{the notion}',r'\deleted{\xout{the notion}}','The machine-cancelled phrase is also crossed by a continuous pen line.']
],diffs={
2192:[r'\inserted[typed]{gave to this notion}','The replacement phrase is typed; its curve is an insertion mark and does not cancel last.','correct layer attribution'],
2196:['which categories M associated to','The capital M is plainly typed, not A with a hat.'],
2200:[r'\inserted[typed]{general}','The interlinear word general is typed.','correct layer attribution']
},unsure=[
[r'\unsure{;}','The punctuation after sense is densely overstruck; semicolon remains tentative.'],
['topos','The five letters are readable beneath both machine and pen cancellation.'],
[r'\unsure{\hand{ch}}','The handwritten completion reaches the clipped right edge; ch is plausible, but the h is not fully available.'],
['l','The typewriter base has the serif shape of lowercase l; the pen diagonal is a retracing.'],
[r'\unsure{n}','The older character under h in That remains overlapped.'],
[r'\unsure{of}','The densely crossed two-letter group after constructing is compatible with of, but neither letter is securely separated.']
],illegible=[],notes=[
'The right ones wording survives an overprint near the s/closing quote; no additional live character can be established.',
'The punctuation after sense remains doubtful. Gave to this notion is typed above the cancellation; its placing stroke passes above last and leaves last week live.',
'The cancelled word is topos, with both typewriter x marks and an additional pen line.',
'The edge completion looks ch but is clipped, so its doubt remains.',
'The subset sign is handwritten, and the following letter is a typed l retraced in pen.',
'The pen-cancelled two-letter group after constructing remains doubtful as of.',
'The last line of that paragraph ends at namel and continues with a hand dash before ly; retained literally.',
'The right edge truncates the specified lines. No missing letters or hyphens have been invented.'
],evidence='Both halves inspected with enlarged details of sense punctuation, topos, the right-edge which, Fl, That and the cancelled of. The page and section numbers and the date 15.3 are typed. The six-item planning passage retains comes, the comma after used so far, and the literal M in item 5. Topos is recoverable under dual cancellation. Gave to this notion and general are typed interlinear revisions, whereas ways of and the displaced of are cursive. The final the notion has both x-overstrikes and a pen line. The right-edge word completions and the old letters that remain obscured stay doubtful.'))
