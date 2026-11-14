import sys,re,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
key='ps_134-3_087';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A\hat{}',r'A^{\hand{\wedge}}').replace(r'\times',r'\mathrm{x}')
 new=new.replace(r'A_{/C}',r'A_{\hand{/}C}').replace(r'A_{/i^*(C)}',r'A_{\hand{/}i^{\hand{*}}(C)}')
 if new!=line:edits.append([line,new,'The presheaf carets and category-of-elements slashes are penned; the star in the second denominator is penned. The product signs are literal typed x characters.'])
edits += [
 [r'\hand{$\begin{tikzcd}[row sep=-10pt,column sep=small] \{0\} \ar[dr] & \\ & \{0,1\} \\ \{1\} \ar[ur] & \end{tikzcd}$}',r'\diagram{\begin{tikzcd}[row sep=-10pt,column sep=small] \{0\} \ar[dr] & \\ & \{0,1\} \\ \{1\} \ar[ur] & \end{tikzcd}}','The entire small barycentric diagram is handwritten. Use the diagram wrapper without nested math delimiters; the two arrows still point into the two-element subset.'],
 [r'\xout{deducexthatxi$_A$xinducesxanx}',r'\xout{deduce that $i_A$ induces an}','The underlying words and subscript A are readable beneath the machine x strikes.'],
 [r'\inserted{$i_Ai^*$}(11)',r'\inserted{$i_Ai^*$} (11)','The inserted functor and the following reference are separate items.'],
 [r'\unsure{identify|identity}','identify','The first occurrence visibly ends f-y; comparison with the clear identity below confirms the different typed letter.'],
 [r'i^*(\unsure{C})',r'i^*(\unsure{\over[typed]{A}{C}})','The argument has overlapping typed impressions. C is the plausible later reading, with an A-like lower layer; the layered reading remains uncertain.'],
 [r'\deleted{moreover}\inserted{(besides A being a \deleted{weak} test category),}',r'\deleted{moreover} \inserted{(besides A being a \deleted{weak} test category)}','The word weak is struck within the hand insertion. The long terminal curve places the insertion and is not an additional comma.'],
 [r'\xout{categoriesx}\inserted[typed]{any C in (Cat)}',r'\xout{categories} \inserted[typed]{any C in (Cat)}','Categories is the recoverable cancelled word; the trailing x is a strike in a blank cell, and the typed insertion needs a word boundary.'],
 [r'\xout{\illegible{1}}',r'\xout{however}','The old h-o-w-e-v-e-r is recoverable beneath the x row.'],
 [r'e_{\hand{A^{\hand{\wedge}}}}',r'e_{A^{\hand{\wedge}}}','The subscript A is typed; the hat is penned. The insertion curve crosses below it without making the A a handwritten letter.'],
 [r'aspheric\inserted{(which',r'aspheric \inserted{(which','The parenthetical insertion is separated from the preceding typed word.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3016:['identify','The f before y has the upper hook absent from the lower identity on the same half-page. Diplomatic retains identify; the explicit master slip variant records identity.','settle source and record one-off slip'],
 3020:['in contrast to a','Contrast is clearly typed; the arXiv contract is not the source reading.'],
 3022:[r'\deleted{moreover}','The word moreover is crossed by pen and replaced by the note above.'],
 3023:[r'\inserted{(besides A being a \deleted{weak} test category)}','The hand insertion is present, including its inner deletion. Its terminal curve is a placing stroke, not a comma.','correct transcription']
 },'unsure':[
 [r'\unsure{-}','The right edge cuts the line after prac; no hyphen is visible, so the uncertainty remains.'],
 ['identify','The first occurrence is identify, distinct from the clear identity later on this page.'],
 [r'\unsure{a}','The single cancelled letter at the clipped edge cannot be recovered securely.'],
 [r'\unsure{\over[typed]{A}{C}}','The two overlapping type layers plausibly read A corrected to C, but their order and full lower glyph are not secure.'],
 [r'\unsure{ll}','The hand amendment in appellation is crowded against the typed letters. The two-l reading remains plausible but not fully separable.']
 ],'illegible':[['however','The original letters are visible under the machine deletion.']],
 'notes':[
 'The missing right edge prevents confirmation of the hyphen after prac.',
 'The exclamation mark is drawn in pen under i.',
 'The upper word reads identify; the lower identity gives an immediate same-page comparison. A recorded master variant applies the one-letter slip correction only in corrected forms.',
 'The cancelled letter after usu is partly beyond the supplied image and remains doubtful.',
 'The argument has typed overprinting, plausibly A to C; its uncertainty is retained.',
 'The pen letters in appellation remain crowded and are retained as doubtful ll.',
 'The cancelled word before there- reads however.',
 'The A is a typed subscript crossed by a placing curve; the separate hat is handwritten.'
 ],'extra_records':[{'source_id':'OBS:ps_134-3_087:slip','before':'the identify\nfunctor','after':'the identity\nfunctor','line':17,'decision':'master slip variant','reason':'The one-off f for t is settled by the same expression identity functor later on this very page, as well as the mathematical context. Diplomatic preserves identify.'}],
 'evidence':'Both original halves, the six-detail panel and a further paired identity comparison inspected. The first word is identify with a hooked f, whereas the later identity has a plain t; this is preserved diplomatically and corrected only by a recorded slip variant. The right-edge prac and usu cancellations remain unresolved. The argument of i* has overlapping A-like and C-like type; it remains doubtful. The handwritten ll in appellation remains crowded. Deduce that i_A induces an and however are recovered under x strikes. The beside-note ends in a placement curve, not a comma. The subscript A near the final parenthetical insertion is typed, its hat penned. The barycentric two-arrow diagram is wholly handwritten, and the displayed product uses a typed x.'})
vpath=OUT/'records/MASTER_VARIANTS_134_3_4.json';variants=json.loads(vpath.read_text());sid='OBS:ps_134-3_087:slip'
variants=[v for v in variants if v['source_id']!=sid]+[{'key':key,'before':'the identify\nfunctor','after':'the identity\nfunctor','kind':'slip corrected','reason':'The wrong f for t is settled by the same phrase identity functor later on this page.','source_id':sid}];vpath.write_text(json.dumps(variants,ensure_ascii=False,indent=2)+'\n')

key='ps_134-3_088';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',lambda m:r'\hand{\ensuremath{'+m.group(1)+'}}',line)
 new=new.replace(r'A\^{}',r'A\hand{\ensuremath{^{\wedge}}}').replace(r'\Delta}\^{}',r'\Delta}\hand{\ensuremath{^{\wedge}}}').replace(r'\Delta}}\^{}',r'\Delta}}\hand{\ensuremath{^{\wedge}}}')
 new=new.replace(r'A^{\wedge}',r'A^{\hand{\wedge}}').replace(r'\hand{\^{}}',r'\hand{\ensuremath{^{\wedge}}}')
 if new!=line:edits.append([line,new,'The hats are pen additions. Replace empty accents and nested math delimiters with the corresponding visible handwritten symbols.'])
edits += [
 [r'condition,  \xout{\illegible{1}}',r'condition,  \xout{\unsure{then}}','The struck edge word starts th-e, with a clipped final cell that may be n. Retain the tentative word; it does not read and.'],
 [r'\inserted{Remarks.}',r'\inserted{\uline{Remarks.}}','The handwritten Remarks heading is underlined.'],
 [r'\hand{1.}I',r'\hand{1.} I','The handwritten item label and the first typed word are separate.'],
 ['condition that it induce',r'co\over[typed]{j}{n}d\unsure{it}ion that it induce','The n is retyped over a visible j. The neighbouring i/t impressions are crowded and their precise layering remains doubtful.'],
 [r'(Hot),\hand{(}',r'(Hot)\unsure{\over{,}{;}}\hand{(}','The punctuation before the added parenthesis has two heavy vertical components, plausibly a pen-altered comma; the exact final punctuation remains uncertain.'],
 [r'\inserted{weak}',r'\inserted[typed]{weak}','Weak is typewritten above the line, with a pen placing curve.'],
 [r'(Cat)\inserted{say}',r'(Cat) \inserted{say}','Say is a separate inserted word after the parenthesized category.'],
 [r'\inserted{left}',r'\inserted[typed]{left}','Left is typewritten above adjoint, with its pen placing curve.'],
 [r'\hand{3.}On',r'\hand{3.} On','The handwritten number and the following word are separated.'],
 [r'\unsure{if}','if','The cancelled i and f are legible under the x strokes.'],
 [r'category\hand{.}',r'category\over{,}{.}','The terminal dot lies over the old typed comma; both layers should be represented.'],
 [r'preserving\inserted{(and moreover A aspheric)}',r'preserving \inserted{(and moreover A aspheric)}','The inserted parenthesis is a separate item after preserving.'],
 ['More generally',r'M\overset{\hand{\smile}}{\mathrm{o}}re generally','A small curved pen mark sits above the typed o; it is not a diaeresis or an extra letter.'],
 [r'A\deleted{\^{}}',r'A\deleted{\hand{\ensuremath{^{\wedge}}}}','The blotted-out presheaf hat was itself penned.'],
 [r'\deleted{It occured to me \xout{too}',r'\deleted{It occured to me \deleted{too}','The local deletion of too is made with diagonal pen strokes, not typewriter x strikes.']
]
# The curved mark is inline math, with only the added stroke marked handwritten.
edits[-3][1]=r'M$\overset{\hand{\smile}}{\mathrm{o}}$re generally'
save_review({'key':key,'edits':edits,'diffs':{
 3029:[r'\xout{\unsure{then}} therefore','The edge word is machine-cancelled and plausibly then; there is no live and.','correct transcription; retain doubt'],
 3042:[r'test functor, \hand{even} with a strict','The added even is clearly present at the end of the line.'],
 3052:[r'(A\hand{\ensuremath{^{\wedge}}}\xout{\unsure{x}} , $W_A = W_{A^{\hand{\wedge}}}$)','The first entry has a penned presheaf hat, with a separately cancelled character following it.'],
 3053:['is model preserving, A ... is a weak test category','The typed A at the right end of the line is present and live.'],
 3055:[r'\inserted{However, if we} ... assume that','The hand replacement is legible above the deleted typed sentence.'],
 3058:[r'\hand{(}and we apply criterion (vii) (p. 80).)','The added opening parenthesis and original closing parenthesis are both visible.'],
 3064:[r"\inserted{assuming} ... \hand{$i_A$, or equivalently} \hand{$\varphi = i_A i^*$, is model-preserving too.}",'Assuming is handwritten at the left, and the ending explicitly includes is and the comma after the formula.']
 },'unsure':[
 [r"\unsure{does'nt|does(nt}",'The curved sign reaches below the normal apostrophe position and has a heavier upper stroke. The apostrophe/parenthesis ambiguity remains.'],
 [r'\unsure{x}','A cancelled type cell follows A below the pen hat. Its underlying letter cannot be separated securely.'],
 ['if','The i-f sequence is readable despite the x row.']
 ],'illegible':[
 [r'\unsure{then}','The first three letters are partly recoverable; the clipped last cell prevents certainty.'],
 [r'\illegible{1}','Dense diagonal pen hatching before i_A obliterates the older word.'],
 [r'\illegible{1}','The small dark pen deletion after too. has no securely recoverable letters.']
 ],'notes':[
 'The cancelled edge word is tentatively then, with its final cell clipped; and is not supported.',
 'The curved mark in does(nt remains ambiguous between a parenthesis and an apostrophe overprint.',
 'The n is visibly retyped over j; the adjacent i/t layering is crowded and remains marked as doubtful.',
 'The punctuation after (Hot) is heavily altered and may be a semicolon over the typed comma; the uncertainty is explicit.',
 'The cell after A remains unreadable under its x strike. More has a separate pen cup above the typed o, reconstructed without changing its spelling.',
 'The heavy hatch before i_A and the small deletion after too. are retained as illegible.',
 'The entire fourth remark is enclosed by pen cancellation lines and diagonal strokes, including its handwritten label; none is left live.'
 ],'evidence':'Both original halves and enlarged details of the opening edge, does(nt, condition, (Hot) punctuation, weak insertion, A-hat cell, cancelled if, More, and the two bottom scribbles inspected. The edge word is tentatively then, not a live and. Condition includes j-to-n type correction and unresolved adjacent i/t overlap. Weak and left are typed interlinear additions. The pen underlining of Remarks and the curved mark above More are restored. Even, A after model preserving, the hat on the first A, However if we, and the full assuming/is ending are all visible. If is recovered under machine strikes. The final two overwritten words stay illegible, and the entire fourth remark is visibly cancelled.'})
