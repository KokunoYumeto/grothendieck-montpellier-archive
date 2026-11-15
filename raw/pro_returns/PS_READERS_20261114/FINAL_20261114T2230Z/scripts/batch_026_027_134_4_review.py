import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
variants=[]
key='ps_134-4_026';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'F\ell',r'F\over{l}{l}').replace(r'\overline{W}',r'\overset{\hand{\rule{0.6em}{0.4pt}}}{W}').replace(r'\subset',r'\hand{\subset}').replace(r'\hand{$\to$}',r'\hand{\ensuremath{\to}}').replace(r'\hand{$\longrightarrow$}',r'\hand{\ensuremath{\longrightarrow}}')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The l of Fl is a typed l retraced in pen; the saturation bars and inclusion signs are penned. Nested math delimiters in handwritten arrows are repaired without changing the signs.'])
edits += [
 [r'containing $W_h$\deleted{)}',r'containing $\over{W}{W}_h$\deleted{)}','The W has a distinct pen retracing over typed W. The following parenthesis is independently pen-cancelled.'],
 [r'localise\over{\illegible{1}}{d}',r'localise\over[typed]{\illegible{1}}{d}','The new d has typewriter serifs and a repeated machine impression; the covered old cell remains unreadable.'],
 [r'\xout{\unsure{elements}}',r'\xout{elements}','The old word elements is recoverable from its surviving stems and bowls beneath the machine strikes.'],
 [r'\xout{\unsure{isomorphic}}',r'\xout{isomorphic}','The letters of isomorphic remain readable below the line of x strikes.'],
 [r'\hand{\uline{organigram.}}\hand{$\lceil$}',r'\uline{organigram.}\diagram{\begin{tikzpicture}[baseline=-0.4ex,x=1em,y=1ex]\draw (0,0)--(0.4,0)--(0.4,1.6)--(1.8,1.6);\end{tikzpicture}}','Organigram is typed and underlined by pen. The following mark is a continuous stepped paragraph instruction, not a mathematical ceiling sign.'],
 [r'\over{T}{t}he natural',r'\over{T}{t}\over[typed]{H}{h}e natural','The first letter is corrected to t by pen; the next cell separately shows typed h over capital H.'],
 [r'$W_h$\hand{$^{-1}M$,}',r'$\over{W}{W}_h$\hand{$^{-1}M$,}','The W in the formula is itself pen-retraced, in addition to the new superscript, M and comma.'],
 [r'\xout{\unsure{of taking}}',r'\xout{of taking}','The old o/f and taking contours are readable under the machine cancellation.'],
 [r'\[ Hom_1(M),\ Hom_2(M) \]',r'\[ Ho\over[typed]{M}{m}_1(M),\ Hom_2(M) \]','The first Hom has a lowercase m typed over visible upper bars of capital M.'],
 [r'\xout{\unsure{notions resp.}}',r'\xout{\unsure{notions resp.}}','The old word notions and following resp are plausible, but the last punctuation is covered by an x; retain the complete doubtful reading.'],
 [r'\arrow[r, shift left, "\hand{$r_{21}$}"]',r'\arrow[r, shift left, color=blue, "\hand{$r_{21}$}"]','The upper arrow is drawn in pen; its typed source and target remain plain.'],
 [r'\arrow[l, shift left, "\hand{$r_{12}$}"]',r'\arrow[l, shift left, color=blue, "\hand{$r_{12}$}"]','The lower arrow is also penned; retain its direction and label.']
]
edits.append([r'\diagram{\begin{tikzcd} Hom_1', '% Hand-drawn arrows are marked blue; typed objects remain plain.\n'+r'\diagram{\begin{tikzcd} Hom_1','Add the agreed provenance comment for the mixed diagram.'])
save_review({'key':key,'edits':edits,'diffs':{
 3600:['on M. New paragraph: When M admits','A full blank line and indentation visibly separate the paragraphs.'],
 3604:['organigram.','The word is typed, with pen underlining and a following paragraph mark; it is not a numbered reference.'],
 3609:[r'\uline{or $W_h$}','A continuous pen underline runs under or and W_h.'],
 3612:['W_h^{-1}M,','The large handwritten M is unambiguous after the superscript; the witness omits it.'],
 3613:['described in A),','The typed reference is A), ending with a comma rather than a period.'],
 3616:['resp. of all homotopism notions','The typed all is visibly present after of.'],
 3618:[r'see correction in \S 51!','The handwritten final numeral has the angular form of 1; retain 51 despite the witness replacement by 52.'],
 3619:['Hom_2(M)','The target of the two-arrow diagram has both parentheses.'],
 3626:['it gives rise','The word rise is clearly typed at the right edge; the following to is cancelled.']
 },'unsure':[
 [r'\unsure{satura}','The x cancellation covers the first and last cells; satura remains a reasonable but not fully secure reading.'],
 [r'\unsure{assum}','The old fragment reaches the clipped right edge; its middle contours support assum without settling all letters.'],
 ['elements','The e/l and terminal t/s survive below and above the x strikes.'],
 ['isomorphic','The complete sequence can be followed beneath the cancelling x line.'],
 [r'\unsure{ri}','The pen ir obscures the old pair. There are surviving typed strokes, but they do not independently settle their order.'],
 ['of taking','The o/f and the ascenders and descender in taking are recoverable.'],
 [r'\unsure{notions resp.}','The final punctuation and some internal cells remain hidden under the x row.']
 ],'illegible':[
 [r'\illegible{1}','The new typed d is legible, but the previous letter is not separately recoverable.'],
 [r'\illegible{1}','The handwritten forming covers residual typed letters; no complete older word is secure.'],
 [r'\illegible{1}','Beneath dwell only an initial d-like curve and a final upright survive; a complete older word cannot be read.'],
 [r'\illegible{1}','The looped pen l covers an older rounded typed cell, without enough shape to name it.'],
 [r'\illegible{1}','The new rela covers several older typed strokes whose exact sequence is unreadable.']
 ],'notes':[
 'The W is pen-retraced. The following typed closing parenthesis has a separate dense pen cancellation, and a new parenthesis appears after too.',
 'The new d is typed; the final l and rela are penned. Each obscured lower layer remains explicitly unreadable.',
 'Elements, isomorphic and of taking are resolved from visible letter contours. Satura, assum, the old ri pair and notions resp. retain uncertainty.',
 'The note visibly ends in section 51, with a clear angular 1. The alternative 52 is the witness reading, not the scan reading.',
 'The lower-left 26 is handwritten. The two diagram arrows and their labels are penned, while Hom labels are typed.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_026:assumption','before':'assuption too','after':'assumption too','line':13,'decision':'master slip variant','reason':'The missing m is an isolated typing slip; assumption is correctly typed in the first two lines of this same page.'},
 {'source_id':'OBS:ps_134-4_026:paragraph','before':r'\uline{organigram.}\diagram{\begin{tikzpicture}[baseline=-0.4ex,x=1em,y=1ex]\draw (0,0)--(0.4,0)--(0.4,1.6)--(1.8,1.6);\end{tikzpicture}}', 'after':r'\uline{organigram.}\par', 'line':22,'decision':'master author instruction','reason':'The stepped pen sign instructs a new paragraph before We\'ll now. Its actual graphic is retained diplomatically.'}
 ],'evidence':'Both original scan halves and seventeen enlarged panels inspected. The source clearly preserves a blank paragraph before When M admits and a stepped paragraph sign after typed, pen-underlined organigram. W is pen-retraced at containing and at the later localisation formula; its bars and the Fl letter retracings are likewise penned. The closing parenthesis after containing W_h is independently struck and reinserted after too. The new d of localised is a typewriter impression, while l of equal and rela are penned; their old layers remain unreadable. Elements, isomorphic and of taking resolve; satura, assum, the old third-letter pair and notions resp. remain doubtful. The two Hom arrows and labels are handwritten. The margin unequivocally denies r21 and cites section 51, which must not be silently replaced by the witness section 52. The ending has rise and a cancelled to.'})
variants += [
 {'key':key,'before':'assuption too','after':'assumption too','kind':'slip corrected','reason':'An isolated missing m, settled by correctly typed assumption twice on the same page.','source_id':'OBS:ps_134-4_026:assumption'},
 {'key':key,'before':r'\uline{organigram.}\diagram{\begin{tikzpicture}[baseline=-0.4ex,x=1em,y=1ex]\draw (0,0)--(0.4,0)--(0.4,1.6)--(1.8,1.6);\end{tikzpicture}}','after':r'\uline{organigram.}\par','kind':'author paragraph instruction','reason':'The author draws a step between organigram and We\'ll now to begin a new paragraph.','source_id':'OBS:ps_134-4_026:paragraph'}]

key='ps_134-4_027';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\to',r'\hand{\to}').replace(r'\in ',r'\hand{\in} ')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The arrows and membership signs on this line are drawn in pen; the adjacent objects and variables are typed.'])
edits += [
 [r'\unsure{comrresponding|corresponding}',r'co\unsure{\over[typed]{m}{r}}responding','The dark first r cell has overlapping type impressions; the live spelling appears corresponding, but the proposed older m is uncertain.'],
 ['or, equivalently, faithful.',r'or, equiv\over{\unsure{alent}}{alent}ly, faithful.','Alent is retraced in pen, including the tall loop of l. Its exact lower typed sequence remains uncertain.'],
 [r'\deleted{\unsure{and}}',r'\deleted{\xout{\unsure{and}}}','The old word has machine x impressions and a separate long pen cancellation; the possible extra initial cell is not secure.'],
 [r'\xout{\unsure{(C}}',r'\deleted{\xout{\unsure{(C}}}','The cancelled label has both machine x marks and a separate looped pen strike; its old text remains doubtful.'],
 [r'\unsure{g}',r'\over{g}{g}','The live letter has the upper bowl and lower loop of g; it is pen-retraced over a typed g.'],
 ['The condition C$_{12}$ is not autodual',r'T\over[typed]{H}{h}e condition C$_{12}$ is not autodual','The h is typed over a capital H, whose upper bar survives.'],
 ['The condition C$_{12}$ above',r'T\over[typed]{H}{h}e condition C$_{12}$ above','The next The has a separate repeated H/h typewriter correction.'],
 [r'same \xout{xxxxxx} objects',r'same \xout{arrows} objects','The cancelled word arrows is legible beneath the x row.'],
 ['is that this functor commute',r'is that th\over[typed]{\illegible{1}}{i}s functor commute','The i in this is retyped over a covered older cell; its exact earlier letter cannot be named securely.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3628:['M to W_h^{-1}M to M_h','The middle term includes the typed M after the exponent -1; both arrows are handwritten.'],
 3631:['a rather evident','The source clearly types evident, not direct.'],
 3635:['as far as the main emphasis','The vowel in far is a, so the witness for is not the page reading.'],
 3637:['having same objects','No the occurs before same; the intervening deleted word is arrows.']
 },'unsure':[
 [r'co\unsure{\over[typed]{m}{r}}responding','The intended upper spelling is corresponding, but overlapping type strokes leave the exact older first-r cell uncertain.'],
 [r'\unsure{and}','The final n/d are plausible under cancellation; the possible extra leading cell prevents a confident complete reading.'],
 [r'\unsure{proof}','The heavily retraced handwritten word has a p-like opening and f-like ending, but its internal strokes remain ambiguous.'],
 [r'\unsure{(C}','Dense pen and machine cancellation leaves only a few arcs; the complete former label is uncertain.'],
 [r'\over{g}{g}','The pen shape resolves as g from its upper bowl and lower loop over the typed g.'],
 [r'\unsure{$\cdot$}','The small brown irregular mark could be a stain rather than a deliberate dot; retain its doubtful graphic status.']
 ],'notes':[
 'The first r has overlapping type impressions; the possible older m is retained as a doubtful lower layer instead of printing an invented extra letter.',
 'The cancelled word after evident remains doubtful. Both machine x impressions and a horizontal pen stroke are visible.',
 'The former condition label remains unreadable beyond the tentative (C. The live g is a legible pen retracing over typed g.',
 'The margin clearly gives 3.4. and section 52. The word after for a remains doubtful proof because its middle is heavily retraced.',
 'Equivalently has pen retracing of alent, not merely machine retyping. The i in this has a distinct machine overprint with an unreadable lower cell.',
 'The brown irregular dot lacks an independent pen stroke or clear punctuation form; it remains marked doubtful.',
 'The lower-left 27 is handwritten.',
 'The two long underlines beneath the cartesian-product statement are continuous pen strokes.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_027:variables','before':'f,g; f_o=hs_o, f_1=hs_1','after':'f,g; f_o=hs_o, f_1=hs_1','line':21,'decision':'retain author notation','reason':'The condition begins with f,g but the displayed equalities use f_o,f_1. Both are clearly visible and are preserved; the guide explains the evident pairing without rewriting the source.'}
 ],'evidence':'Both original halves and eleven enlarged panels inspected. The initial to, is handwritten. Every arrow and the two membership signs are pen strokes, with typed object names. The first r of corresponding has a covered older type layer, retained as uncertain. Equivalently contains a pen-retraced alent with uncertain earlier letters. The old word after evident and the initial condition label remain doubtful under both machine and pen cancellation. The live g is a clear pen-over-typed g. The marginal note clearly cites section 52 and calls the statement rash; its heavily retraced proof remains doubtful. The underlined product claim and weak addition are handwritten. The small brown margin dot is possibly a stain, retained as doubtful. The cancelled word arrows is recovered. The two The forms have H/h type overprinting, and the i of this covers an unreadable old cell. The source uses f,g before a display written with f_o,f_1; that notation is preserved.'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
