import sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review

def hmarks(tail='e'):
 return r'T$\overset{\hand{\scriptscriptstyle\perp\perp}}{\underset{\hand{\scriptscriptstyle,\frown}}{\mathrm h}}$'+tail
key='ps_134-4_036'
edits=[
 [r'\xout{defin}',r'\xout{\unsure{defin}}','The old end-of-line letters are struck by typewriter x impressions and clipped at the right edge; defin is plausible but not wholly secure.'],
 ['that with respect',r'that \over{wi}{wi}th respect','The w and i are retraced in pen, while th remain ordinary type.'],
 ['M as a product',r'M \over{a}{a}\over{\unsure{s}}{s} a product','As is retraced in pen; the lower s-like impression is obscured by the heavier stroke and remains doubtful.'],
 [r'product\inserted{category}',r'product \inserted{category}','Restore the visible space before the whole-word insertion category.'],
 [r'\unsure{c|e}',r'c','The typed letter is an open c, without the cross-stroke of e.'],
 [r'\inserted[typed]{locally connected}topological',r'\inserted[typed]{locally connected} topological','The typed interlinear insertion has a placing curve; topological remains live and is separated by a word space.'],
 ['\n3.4.\n','\n'+r'\hand{3.4.}'+'\n','The date is written in pen.'],
 ['\n52. Before','\n'+r'\hand{52.} Before','The section numeral and its period are handwritten.'],
 ['accuracies !).',r'accuracies \hand{!}).','The exclamation stroke and its point are penned; the adjacent parenthesis and final period are typed.'],
 [r'M \longrightarrow M\'',r'M \hand{\longrightarrow} M\'','The arrow between the typed categories is drawn in pen.'],
 [r'\underline{Hom}(M\',C) \longrightarrow \underline{Hom}(M,C)',r'\underline{Hom}(M\',C) \hand{\longrightarrow} \underline{Hom}(M,C)','The Hom comparison arrow is handwritten.']
]
# Apostrophes are literal TeX punctuation, not backslash escapes.
edits=[[(v.replace("\\'","'") if isinstance(v,str) else v) for v in e] for e in edits]
save_review({'key':key,'edits':edits,'diffs':{
 3796:['As for c),','The visibly typed c refers to the decomposition assumption; the witness substitutes e.'],
 3798:['by still defining','Still defining is typed above machine-cancelled interpreting and is placed by a pen hook.'],
 3799:['locally connected topological space','Locally connected is typed interlinearly; the long curve places it before topological and does not separately cancel that word.'],
 3800:['52. Before pursuing ...','Only the section numeral is present; the witness title Inaccuracies rectified is absent.'],
 3801:['I would like first to correct','First is clearly typed between like and to.']
 },'unsure':[
 ['c','The open right side and absence of a central bar settle the c/e reading.'],
 [r'\unsure{f}','A short upper horizontal old stroke survives beneath the penned n, but the complete lower letter cannot be recovered confidently.']
 ],'illegible':[[r'\illegible{1}','The penned flew covers the earlier word too densely to recover it; no witness reading is substituted.']],
 'notes':[
 'The letter in As for c) is a clear typed c, now resolved.',
 'To is pen-cancelled, and the following old word has machine x overprinting and a clipped right edge; defin remains explicitly doubtful. Definition and of are penned replacements.',
 'Locally connected is typed, and the line underneath is continuous with its placing hooks. Topological remains live.',
 'Still defining is typed above the cancelled interpreting.',
 'Flew is clear handwriting; its earlier typed word remains unreadable.',
 'The first o of looking is reinforced in pen, as encoded.',
 'The w and i of with have pen retracing, now marked; th remain typed.',
 'The bottom-left 36 is handwritten; the new date and section number are also in pen.'
 ],'evidence':'Both original scan halves, seven enlarged detail panels and an additional on crop inspected. The typed c in As for c) resolves the principal witness disagreement. The raised still defining and locally connected are typed; the latter has a continuous placing curve and leaves topological live. Definition, of, category, As usual, the, was and while are pen additions. Came from is penned and then cancelled. The initial defin is clipped and x-overprinted, while the word under flew is unrecoverable. With has penned wi, as has pen retracing with a doubtful lower s, and the old cell beneath the n in on remains doubtful. The date 3.4, section 52, exclamation point and both displayed arrows are handwritten. The two whole-word insertion boundaries receive actual spaces.'})

key='ps_134-4_037'
quote=r'\unsure{\diagram{\begin{tikzpicture}[baseline=(q.base)]\node[inner sep=0pt] (q) {``};\draw[color=blue,line width=.6pt] (q.west) ++(.015,.02) -- ++(-.02,.11) -- ++(.04,.09) -- ++(.02,.06);\end{tikzpicture}}}'
edits=[
 [r'O\unsure{ne}',r'O$\overset{\hand{\scriptscriptstyle\perp\perp}}{\mathrm n}$e','The letters ne are legible. Two small upper pen strokes mark n; they are not an unreadable replacement word.'],
 [r'\xout{\unsure{compositi}}',r'\xout{compositi}','The old compositi letters remain readable under the typewriter x row.'],
 [r'T\unsure{h}e other',hmarks()+' other','The h is legible, with paired upper and lower pen marks rather than an unresolved letter.'],
 [r'\uline{The characteristic',r'\uline{'+hmarks()+' characteristic','The same upper/lower pen marks surround the h of The characteristic.'],
 [r'\over{\unsure{w}}{W}e',r'\over{W}{W}e','The old impression has capital-W upper serifs, and a capital W is retraced over it in pen.'],
 [r'\xout{the\unsure{xxxx}}',r'\xout{the\illegible{1}}','The old the is legible, but the remaining cancelled run cannot be read; literal x placeholders are replaced by an illegibility mark.'],
 ['\nThe set of homotopy','\n'+hmarks()+' set of homotopy','The last paragraph also carries paired upper and lower h marks.'],
 [r'\unsure{\xout{``}}',quote,'The irregular ink over the left quote does not establish cancellation of the whole opening quotation mark. Retain the doubtful quote and superposed pen stroke graphically.'],
 [r"$M\to M'$,",r"$M\hand{\to} M'$\,$\overset{\hand{-}}{,}$",'The inline arrow is penned, and a separate raised horizontal pen bar stands above the following comma.'],
 [r'M \longrightarrow M\'',r'M \hand{\longrightarrow} M\'','The displayed basic-functor arrow is drawn in pen.'],
 [r'M \longrightarrow M/R',r'M \hand{\longrightarrow} M/R','The quotient arrow is drawn in pen.'],
 [r'M \longrightarrow W^{-1}M',r'M \hand{\longrightarrow} W^{-1}M','The localization arrow is drawn in pen.'],
 [r'\mathrm{Hom}_1(M) \longleftrightarrow \mathrm{Hom}_2(M)',r'\mathrm{Hom}_1(M) \hand{\longleftrightarrow} \mathrm{Hom}_2(M)','The correspondence has a single pen line with two arrowheads.']
]
edits=[[(v.replace("\\'","'") if isinstance(v,str) else v) for v in e] for e in edits]
save_review({'key':key,'edits':edits,'diffs':{
 3809:["thus M' corresponds","The typed M' is explicit, not the pronoun it."],
 3810:["between those M'","The word is those with an o, not these."],
 3811:['saturated subsets W of Fl(M)','The typed W occurs between subsets and of.'],
 3814:['with same objects','There is no article between with and same.'],
 3815:['when we got an','The typed verb is got; the underlining does not change its vowel.'],
 3816:['than the converse','The typed comparison begins than, not then.']
 },'unsure':[
 ['ne with upper pen marks on n','Both letters are legible; the small added marks are retained graphically.'],
 ['compositi','The surviving p descender and the following ositi sequence identify the cancelled text.'],
 ['h with upper and lower pen marks','The typed h remains legible beneath nontextual marks.'],
 [r'\unsure{f}','The old f is plausible from its crossbar, but the pencilled n crosses it and prevents a wholly secure lower-layer reading.'],
 ['W','The old upper serifs and width show a capital W.'],
 [r'\illegible{1}','The old run after the is hidden by the machine x row.'],
 [quote,'The irregular dark ink crosses the left quote without securely cancelling the entire opening quotation mark; independent review agrees.']
 ],'notes':[
 'The word One is legible. The n has a pair of small upper pen strokes, preserved graphically.',
 'The other, The characteristic and the final The set have legible h letters with small upper and lower pen marks.',
 'The ell strokes in Fl are handwritten, unlike the typed F and parentheses.',
 'Compositi resolves beneath its x row. The remains readable before an unrecoverable cancelled run, now marked illegible.',
 'Canonical, localization and sur are typed interlinear additions with pen placing marks. The prefix sur joins the surviving jective.',
 'The dark ink across the left opening quote does not justify cancelling the whole quotation mark. A separate horizontal pen bar is preserved above the comma after the last M-prime.',
 'The archive folio 37 is handwritten.'
 ],'evidence':'Both original scan halves and nine enlarged panels inspected. The first One resolves as ordinary typed letters with small upper marks on n. Three The forms have the recurring upper/lower marks around a legible h. Compositi resolves under machine strikes; the cancelled run after the remains unreadable. The old W is capital, while the old f under the penned n remains doubtful. The scan retains thus M-prime, those, the W after subsets, with same objects, got and than against the witness. Canonical, localization and sur are typed above the line. All four displayed arrows and the final inline arrow are pen-drawn. The opening quote bears irregular ink without a secure full cancellation; independent inspection supports preserving its uncertainty. The separate raised bar after the last M-prime is retained graphically.'})
