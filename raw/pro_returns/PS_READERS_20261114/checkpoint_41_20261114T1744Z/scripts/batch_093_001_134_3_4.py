import sys,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-3_093'
edits=[
 ['Pursuing Stacks (presumably',r'Pursuing \over{S}{S}tacks (presumably','The initial S of Stacks is reinforced in pen over a typed S.'],
 [r'\unsure{not|no,}',r'no\over{\unsure{t}}{t}','The final live pen character is t. Its lower typed cell is too obscured to confirm, so that lower layer remains doubtful.'],
 [r'(\hand{\Delta}_{/a})\hat{}\,\approx\hand{\Delta}\hat{}_{/a}',r'(\hand{\Delta}_{/a})^{\hand{\wedge}}\,\hand{\approx}\hand{\Delta}^{\hand{\wedge}}_{/a}','Both hats and the equivalence sign in the deleted formula are handwritten.'],
 [r'\xout{xxxxi}',r'\xout{\unsure{fini}}','The old right-edge fragment appears to start fini, but its ending is clipped and the lower letters remain uncertain.'],
 [r'H\hand{o}t',r'H\over[typed]{o}{o}t','The o has two vertically displaced regular type impressions, not a handwritten replacement.'],
 [r'\unsure{XIII|VIII}',r'\over[typed]{\unsure{V}}{X}III','The live numeral is XIII, with a crossing X in the first cell. An older V-like typed impression remains uncertain beneath it.'],
 [r'3 in \xout{\unsure{pagexl}}',r'3 \over{o}{i}\over{n}{n} \xout{page \unsure{1}}','In has pen i over typed o and pen n retracing. The cancelled word page is recoverable; the final narrow numeral-like cell remains doubtful as 1.'],
 [r'\inserted{(section 39),}',r'\inserted{(section 39)}','The apparent comma belongs to the long curved insertion hook, not to the parenthetical words.'],
 [r'\xout{was}\inserted[typed]{is}',r'\xout{was} \inserted[typed]{is}','The typed replacement is is a separate word after the cancellation.'],
 [r'\mspage{93}',r'\mspage{\hand{93}}','The lower-left foliation is handwritten.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3123:['I am going to come back upon this ... compare remarks in section 35.','The complete opening continuation is present above note 33 and remains live.'],
 3124:[r"($^{33}$) We'll see later it \uline{is} stronger.",'The short note is present, with is underlined.'],
 3128:[r'(\hand{!}$^{35}$)','The exclamation mark is penned beside the typed note number.'],
 3137:['see section 44 .','The final punctuation is a typed period; there is no closing parenthesis after 44.']
 },'unsure':[
 [r'no\over{\unsure{t}}{t}','The final t is handwritten and clear, while its older cell remains obscured.'],
 [r'\over[typed]{\unsure{V}}{X}III','The corrected first letter is X; the older V-like layer is not fully separable.'],
 [r'page \unsure{1}','The letters page are readable, but the final slender cell cannot be distinguished conclusively from a 1/l form.']
 ],'notes':[
 'The deleted section 38 corollary insertion precedes that. The new Cf. end of section 39 note is placed after indeed by its pen curve, and has no closing parenthesis in its wording.',
 'The word ends in a live handwritten t inside the entirely cancelled example. All Delta symbols, the hats and the equivalence sign are penned.',
 'Hot has repeated typed o impressions. The exclamation signs before 35 and after story are handwritten.',
 'The final numeral reads XIII, with an uncertain older V-like type layer in its first cell.',
 'In is corrected in pen over o/n. The cancelled page is readable; its final numeral-like cell remains uncertain.',
 'The lower-left 93 is handwritten.'
 ],'extra_records':[{'source_id':'OBS:ps_134-3_093:1','before':'finite products and arbitrary sums','after':'finite products and arbitrary sums','line':22,'decision':'retain authorial mathematical limitation; discuss in guide','reason':'The source restricts ordinary products to finite ones while retracting a more general limit claim. Arbitrary products also exist in the homotopy category, represented by products of Kan complexes; the source wording is preserved.'}],
 'evidence':'Both original halves and enlarged details of not, XIII, Hot, the cancelled limit fragment, in, page and the section-39 insertion inspected. The whole example in note 34 is diagonally cancelled, including its handwritten mathematics. The new section-39 reference has the visible placement specified in the source. Not ends in a clear pen t; XIII has a clear X over an uncertain older V. Hot has two typed o impressions. In has pen o-to-i and n retracing, and the old page letters are recovered. The comma assigned to the section-39 insertion is actually its placing hook. Note 35 retains its strong source wording about finite products and arbitrary sums, with the limitation discussed separately in the guide.'})

key='ps_134-4_001';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A\hat{}',r'A^{\hand{\wedge}}')
 if new!=line:edits.append([line,new,'The presheaf carets are added in pen, not empty type accents.'])
edits += [
 [r'\margin{II}',r'\margin{\diagram{\begin{tikzpicture}[rotate=25]\node[inner sep=1pt] (n) {II};\draw (-.36,.38)--(.38,.38);\draw (-.36,-.38)--(.38,-.38);\end{tikzpicture}}}','The upper-left II is accompanied by two oblique pencil rules; reconstruct them with the numeral.'],
 [r'\mspage{89}',r'\mspage{(89)}','The typed folio is enclosed in parentheses.'],
 ['test categories and test functors',r'test \over[typed]{c}{c}ategories and test functors','The first c of categories has overlapping type impressions.'],
 [r'\over{\unsure{d}}{d}uring',r'\over{a}{d}uring','The old typed a is visible below the taller pen d.'],
 [r'\deleted{ungratifying}\inserted{very}',r'\deleted{ungratifying} \inserted{very}','Very is a separate replacement word.'],
 [r'appeared \xout{\illegible{1}}',r'appeared \xout{again}','The old a-g-a-i-n is visible beneath the machine x row.'],
 [r'simple\unsure{-}minded','simple-minded','A short horizontal typed hyphen is visible between the adjacent e and m.'],
 [r'\inserted{which}',r'\inserted[typed]{which}','Which is typed above the line and placed by a pen curve.'],
 [r'T\hand{\unsure{h}}ere',r'T$\overset{\hand{\unsure{\wedge}}}{\mathrm{h}}$ere','The h is plain type. A small separate mark above it is angular but not securely identifiable, so retain a doubtful overhead mark rather than a doubtful handwritten h.'],
 ['There seem to be',r'T\over[typed]{H}{h}ere seem to be','The second There has H and h in the same typed cell.'],
 ['In all of them',r'I\over[typed]{N}{n} all of them','A typed capital N is overlapped by its lowercase replacement.'],
 ['basic ones and more',r'basic ones and \over{\unsure{m}}{m}ore','The m is retraced in pen; the lower letter is partly obscured.'],
 [r'substitu\over{\illegible{1}}{t}es',r'substitu\over{\unsure{t}}{t}\over{e}{e}\over{s}{s}','The final t-e-s are pen-retraced, with e and s recoverable underneath; the older t-cell remains doubtful.'],
 [r'\inserted{a} considerably',r'\inserted[typed]{a} considerably','The inserted a has the typewriter form and is placed by a separate slash.'],
 [r'\unsure{o}ther',r'\xout{r}\over[typed]{\unsure{a}}{o}ther','The first r is separately x-struck; the following o is live type over a partly obscured a-like cell.'],
 [r'th\over{\unsure{e}}{i}s',r'th\over{e}{i}\over{s}{s}','The typed e is visible beneath the pen i; the following s is also pen-retraced.'],
 [r'A_{/F}',r'A_{\hand{/}F}','The category-of-elements slash is drawn in pen.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3138:['45.','Only the section number precedes the body; no descriptive section title is on the scan.'],
 3141:[r'during this \deleted{ungratifying} \inserted{very} work','The source retains this before the replacement very, not the.'],
 3145:[r'T$\overset{\hand{\unsure{\wedge}}}{\mathrm{h}}$ere is','The typed word is There. The separate overhead mark does not turn h into s.','correct transcription provenance'],
 3147:['there is','The second paragraph clearly reads there is, not these is.'],
 3155:['Upper-left II with two oblique rules','The faint pencil numeral and its two rules are present and reproduced.'],
 3156:[r'\margin{1}','The bottom-left handwritten 1 is present.']
 },'unsure':[
 ['a','The old typed a is visibly distinct from the tall pen d.'],
 ['-','The short horizontal hyphen between e and m is visible.'],
 [r'\hand{\unsure{\wedge}} over typed h','The h itself is typed and clear; the small angular overhead mark is unresolved.'],
 [r'\xout{r}\over[typed]{\unsure{a}}{o}','The separately struck r and live o are visible. The lower letter under o remains doubtful.'],
 ['e','The old e bowl and crossbar remain beneath the hand i.']
 ],'illegible':[
 ['again','The letters of again survive under the x row.'],
 [r'\unsure{t}','The pen t covers most of the older cell; t is plausible but not securely recoverable.'],
 [r'\illegible{1}','The two dark cancelled cells before i_A remain unrecoverable.']
 ],'notes':[
 'The h is regular type; a separate small angular mark sits above it and remains doubtful.',
 'The hyphen is visible close to the adjacent letters; no extra deleted m is asserted.',
 'The word has a separately cancelled r followed by a live typed o over a doubtful a-like cell.',
 'The right edge does not show hyphens after struc or pressing; no absent hyphen has been supplied.',
 'During has pen d over typed a. Substitutes has penned t/e/s with a doubtful lower t-cell. This has visible typed e under pen i and retraced s.',
 'All formula arrows are drawn in pen, as are the presheaf hats and category-of-elements slash.'
 ],'evidence':'Both original halves and enlarged details of simple-minded, the first There, substitutes, the two cancelled cells before i_A, other, during and this inspected. The folio is typed (89), with a ruled II in the upper-left margin and handwritten 1 below. Again is recovered under x strikes. Which and the separate a insertion are typed, whereas have me and very are handwritten. The first There has a typed h with an unresolved small overhead mark; the second has H-to-h overprinting. The r before other is separately x-struck, and o retains an uncertain lower a-like layer. The final t/e/s of substitutes and i/s of this are pen corrections. The source still says this very work, there is, caracteristic and analoguous.'})
