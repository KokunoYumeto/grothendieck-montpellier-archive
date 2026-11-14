import sys,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-3_085';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'^{\wedge}',r'^{\hand{\wedge}}')
 if new!=line:edits.append([line,new,'The presheaf carets are pen additions throughout, including within the cancelled remark.'])
edits += [
 [r"\unsure{''|*}",r"\unsure{''}",'The dark closing mark has no visible asterisk arms. A filled double-quote is the plausible reading, retained as doubtful because its two strokes cannot be separated.'],
 [r'\inserted[typed]{aspheric\hand{,}}',r'\inserted[typed]{aspheric}','The curve after aspheric is the continuous placing stroke; there is no independent comma.'],
 [r'\hand{\geq}',r'\mathrel{\underset{\hand{-}}{>}}','The greater-than sign is typed; only the lower equality stroke is penned.'],
 [r'\unsure{not}','not','The cancelled n-o-t is clearly readable below the x strokes.'],
 [r'W_{(\mathrm{Cat})}{}^{-1}',r'W_{(\mathrm{Cat})}\overset{-1}{\xout{-1}}','A lower typed minus-one is crossed out, with the replacement typed above it. Both layers are visible.'],
 [r'\quad F \hand{\longmapsto}',r'\quad \over{F}{F} \hand{\longmapsto}','The capital F is retraced in pen over an older typed F, matching the same form on page 79.'],
 ['The basic example',r'T\over[typed]{H}{h}e basic example','The H and h occupy a shared overtyped cell.'],
 ['can be just translated',r'\over[typed]{c}{c}an be just translated','The c has two displaced rounded type impressions.'],
 [r'\xout{\illegible{1}}',r'\xout{or}','The cancelled word at the right edge reads or beneath the x row.'],
 [r'equivalent\xout{\unsure{es}}',r'equivalen\unsure{\over{tes}{ces}}','The final letters are penned or retraced, not machine-deleted. A c-like curve appears against the typed t, but the full correction tes to ces remains uncertain; preserve the doubtful layered reading.'],
 [r'saw\inserted{before}',r'saw \inserted{before}','Before is a separate inserted word and needs an explicit boundary after saw.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2979:[r'\inserted[typed]{aspheric} object','The apparent comma is the curved insertion line, continuous with its right-hand hook. Retain aspheric without an invented comma.','reject false punctuation'],
 2981:['any object','The word object is singular.'],
 2989:[r'A_{/i^{\hand{*}}(C)}','The slash is visible and the exponent star is penned.'],
 2992:[r'equivalen\unsure{\over{tes}{ces}}','The pen-overwritten ending remains doubtful. It is neither a clean typed equivalences nor a machine-cancelled es.','retain doubtful revision'],
 2993:['equivalence (or, what is enough','The source has the noun equivalence and the word what.'],
 2994:[r'as we saw \inserted{before}','The typed verb is saw, and before is a hand insertion.'],
 2996:[r'i(a) = A_{/a}','The argument a is lowercase on both sides.']
 },'unsure':[
 [r"\unsure{''}",'The closing ink blob plausibly represents a double quote, but its individual strokes remain obscured.'],
 [r'\unsure{x}','The cancelled remark label has crowded overprinting; its final x-like character remains uncertain.'],
 ['not','The old word is readable.'],
 [r'\unsure{rs}','The last cells are overwritten and partly clipped at the right edge, so the ending remains doubtful.'],
 [r'\unsure{\over{tes}{ces}}','The final pen strokes should not be deleted. The proposed correction of the full ending remains uncertain; an independent review of the same crop agreed on retaining this doubt.']
 ],'illegible':[['or','Both lower letters remain distinguishable beneath their x strikes.']],
 'notes':[
 'The closing mark is a filled quote-like blob, without the radiating strokes of an asterisk. It remains doubtful.',
 'The sign has a typed greater-than component and a separate pen lower stroke; the mixed provenance is represented.',
 'The entire Remark is boxed and diagonally cancelled. Its crowded item label remains doubtful. All three formula arrows were left blank and remain blank.',
 'The final parenthesis in (10) is penned; the modelizers ending remains overprinted and clipped.',
 'Very is readable under its x row. The last ending after equivalen is a pen revision over tes, not a typewriter deletion; the possible final ces remains explicitly doubtful.'
 ],'evidence':'Both original halves, twelve enlarged details and a comparison crop of the capital F with page 79 inspected. The aspheric insertion has no separate comma; the apparent mark is its placing curve. The greater-than sign is typed and gains a pen lower stroke. The large Remark is fully cancelled with its unfilled arrow spaces preserved. Not, very and the right-edge or are recoverable. A misplaced lower minus-one is machine-cancelled beneath its typed replacement. The F is a pen retracing over type. The ending after equivalen has live pen strokes and a possible c correction over t; it remains doubtful rather than being deleted or silently normalized. The final saw, lowercase i(a), and hand before are confirmed.'})

key='ps_134-3_086';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',lambda m:r'\hand{\ensuremath{'+m.group(1)+'}}',line)
 new=new.replace(r'A\hat{}',r'A^{\hand{\wedge}}').replace(r'A\^{}',r'A\hand{\ensuremath{^{\wedge}}}')
 if new!=line:edits.append([line,new,'Use ensuremath for the hand symbols so they remain valid inside existing math mode; represent the penned presheaf carets instead of empty accents.'])
edits += [
 [r'\xout{xxxxxxxx}',r'\xout{moreover}','The eight cancelled letters read moreover and are repeated live on the next line.'],
 [r'\unsure{in|an}',r'\unsure{\over[typed]{A}{i}}n','The first cell has an A-shaped lower impression and a possible dotted i correction. Keep uncertainty on the layered interpretation rather than assert plain in.'],
 [r'\unsure{still|stuff}','still','The hand clearly writes s-t-i-l-l, with two final l strokes.'],
 [r'\inserted{plus a little more still on i.)}',r'\inserted{plus a little more still on i.}','The long right-hand curve places the insertion and is not an additional textual parenthesis. The original typed parenthesis after aspheric remains.'],
 [r'\unsure{Then}','Then','The old T-h-e-n remains legible beneath the pen cancellation.'],
 [r'\xout{are equivalent}',r'\deleted{are equivalent}','The phrase is crossed by long pen strokes, not a row of typewriter x characters.'],
 [r'NB\xout{xxx}',r'NB\xout{not}','The old word not is recoverable and precedes the live repeated not.'],
 ['THe element',r'T\over[typed]{H}{h}e element','The H and h share one typed cell, as in the preceding page.'],
 ['i.e.  A  itself',r'i.e.  \over{A}{A}  itself','The A is reinforced with heavy pen strokes over a typed A.'],
 ['(iii)  There exists',r'(\over[typed]{i}{i}ii\over[typed]{)}{)}  There exists','The first i and closing parenthesis have vertically displaced typed impressions.'],
 [r'i_{\hand{!}}(I)\to',r'i_{\hand{!}}(I)\hand{\to}','The map from i_!(I) to Delta_1 is drawn in pen.'],
 [r'A\hand{\ensuremath{^{\wedge}}}$\to$(Cat)',r'A\hand{\ensuremath{^{\wedge}}}$\hand{\to}$(Cat)','The extension arrow is penned, like the adjacent original functor arrow.'],
 ['The conditions  (ii)',r'\margin{\diagram{\begin{tikzpicture}[x=1em,y=1ex]\draw (0,0)--(3,.35);\draw (0,1)--(3,1.4);\end{tikzpicture}}}'+'\n'+'The conditions  (ii)','Two sloping parallel pen strokes stand in the left margin beside this conclusion; reconstruct them rather than omit them.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3003:[r'aspheric)\hand{,} \inserted{plus a little more still on i.}','The added word is still. The final curving line is an insertion marker, not an extra parenthesis.','correct transcription'],
 3004:[r'aspheric)\hand{,} \inserted{plus','The original typed closing parenthesis remains uncancelled before the added comma and insertion.'],
 3007:[r'i: A\hand{\ensuremath{\to}}(Cat)\hand{;} \inserted{Moreover, A is aspheric.}','The added Moreover begins with a capital M, is written below the line, and adds the asphericity requirement.']
 },'unsure':[
 [r'\unsure{\over[typed]{A}{i}}n','The first cell clearly has overlapping impressions, but the final i interpretation remains qualified.'],
 ['still','The pen letters and two final tall l strokes are readable.'],
 ['Then','The original word survives under the crossing strokes.']
 ],'notes':[
 'The first cell has an A-shaped lower layer and a possible dotted i overprint; its reading remains doubtful.',
 'The inserted word is still, and the terminal curve is a placing mark rather than a second textual closing parenthesis.',
 'The cancelled word is Then, replaced by Consider above it.',
 'The first i and closing parenthesis of (iii) are retyped. THe has a shared H/h type cell, rather than an uncancelled capital H.'
 ],'extra_records':[{'source_id':'OBS:ps_134-3_086:1','before':r'tions\hand{:}\xout{are equivalent}:','after':r'tions\hand{:}\deleted{are equivalent}:','decision':'retain source punctuation after pen deletion','reason':'A colon is inserted after conditions, while the earlier typed colon remains visible after the crossed are equivalent. The diplomatic source preserves both; no unseen cancellation of the earlier colon is asserted.','line':32}],
 'evidence':'Both original halves and nine enlarged details inspected. The old moreover and not are recovered from x strikes. The added phrase reads plus a little more still on i.; its right sweep is placement, not another parenthesis. The original typed parenthesis after aspheric remains live. Then is recovered beneath Consider, and are equivalent is pen-deleted. Both visible colons around that deletion are preserved. THe is H-to-h type overprinting; the first i and closing parenthesis in (iii) are retyped, and the later A is pen-retraced. The formula (12) and extension arrows are penned. Two parallel sloping marginal strokes accompany the conclusion. The inserted final asphericity requirement is retained with its capital Moreover.'})
