import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT
def hmarks(tail='e'):
 return r'T$\overset{\hand{\scriptscriptstyle\perp\perp}}{\underset{\hand{\scriptscriptstyle,\frown}}{\mathrm h}}$'+tail
key='ps_134-4_034';edits=[
 [r'\unsure{is satisfied, the}',r'\unsure{is satisfied, we}','The final old word has two cells with w/e-like contours, rather than the three cells required for the; retain doubt beneath the x row.'],
 [r'\xout{\unsure{contractibility}}',r'\xout{the homotopy}','The cancelled text is the homotopy: the initial the and final p/y descenders are visible. The raised contractibility is the replacement.'],
 [r'\deleted{\unsure{elementary}}',r'\deleted{elementary}','The old elementary is readable beneath its pen cancellation.'],
 [r'T\hand{h}at',r'T\over{H}{h}at','The penned h covers a typed capital H whose horizontal bars survive.'],
 [r'\xout{\unsure{e}}',r'\xout{\illegible{1}}','The cancelled cell after monoid is covered by an x; an underlying e is not secure.'],
 [r'\xout{\unsure{contractible contractor}}',r'\xout{contractible contractor}','The full earlier two-word phrase remains readable under the x line.'],
 [r'e_1\hand{.}f',r'e_1\over{\illegible{1}}{\cdot}f','The pen point/mark inside the parentheses covers older typed strokes whose exact letter is unreadable.'],
 [r'\hand{\unsure{\circ|\cdot}}',r'\hand{\circ}','The symbol has a visible white centre surrounded by a closed pen ring.'],
 [r'Then $p_o$',hmarks('en')+r' $p_o$','The h in Then has the paired small upper T-like marks and lower comma/curve; preserve those graphics.'],
 ['The argument',hmarks()+' argument','The same paired upper and lower marks surround h at the beginning of this paragraph.'],
 ['The canonical',hmarks()+' canonical','The heading likewise marks h above and below; retain the pen graphics.'],
 [r'd)\quad For',r'd)\quad F$\overset{\hand{\smile}}{\underset{\hand{\frown}}{\mathrm o}}$r','For has separate curved pen marks above and below its o.'],
 ['The equivalence',r'T\over[typed]{h}{h}e equivalence','The h has a displaced lower repeated type impression.'],
 [r'gi\hand{v}e',r'gi\over{\illegible{1}}{v}e','The live pen v covers an old type cell; its exact former letter is not recoverable.'],
 [r'indeed\inserted[typed]{if I is a contractor}',r'indeed \inserted[typed]{if I is a contractor}','Insert the actual word space at this whole-phrase insertion boundary.'],
 [r'\underline{J}$\inserted',r'\underline{J}$ \inserted','Retain the visible spacing before the parenthetical insertion.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3757:['Y to underlined Hom(X,Y)','The arrow has an arrowhead but no bar at its tail.'],
 3760:['and homotopy relation','The handwritten noun is singular relation.'],
 3764:['End(X,X)','Both X arguments and their separating comma are visibly typed.'],
 3768:['e_1 circle e_1 = e_1','The handwritten sign is a closed small ring, not a solid dot.'],
 3770:['pi_o = id_{H_o}','The o is under i on the left, and under H within the right subscript; retain the source index placement.']
 },'unsure':[
 [r'\unsure{is satisfied, we}','The final two old cells suggest we; their x overprinting leaves doubt.'],
 ['the homotopy','The initial the and terminal p/y contours identify the old phrase.'],
 ['elementary','The old letters can be followed below the horizontal cancellation.'],
 [r'\illegible{1}','No secure old letter can be separated beneath the terminal x.'],
 ['contractible contractor','Both old words are recoverable beneath the x strikes.'],
 [r'\circ','A white centre distinguishes the ring from a filled dot.'],
 [r'\unsure{hence}','The pen stroke obscures the first and middle old cells; hence remains plausible but not secure.']
 ],'notes':[
 'The cancelled clause ends in a two-cell we-like word; the revised doubtful reading is is satisfied, we.',
 'The nontextual upper/lower marks in For, Then, The argument and The canonical are restored graphically. The initial The equivalence instead has a displaced typed h impression.',
 'The opening parenthesis is handwritten. The inner dot/mark covers unreadable earlier type strokes; the composition sign in the following prose is a clear ring.',
 'The live v is penned over an unreadable older type cell, now preserved as an overprint.',
 'The lower-left 34 is handwritten.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_034:retract_formula','before':'pi_o = id_{H_o}','after':'pi_o = id_{H_o}','line':35,'decision':'retain author notation','reason':'With p_o:H to H_o and i:H_o to H, the needed retract identity is p_o i=id_{H_o}. The source instead places the o under i; this visible formula is preserved and flagged in the guide.'}
 ],'evidence':'Both original halves and sixteen enlarged panels inspected. The old clause ends in a doubtful we-like two-cell word. The cancelled phrase beneath contractibility resolves as the homotopy, and elementary and contractible contractor are recoverable. That has a penned h over typed H. The terminal monoid cell and the old v-cell in give remain unreadable. The displayed inner point covers older strokes, while the composition symbol later is a clear closed ring. The handwritten insertion says singular relation. The arrow in d is an ordinary arrow, End has two X arguments, and the source writes pi_o=id_{H_o}; that misplaced subscript is preserved. The repeated small upper/lower pen graphics are reconstructed, and two whole-phrase insertion boundaries receive actual spaces.'})

key='ps_134-4_035';edits=[
 [r'\mspage{123}',r'\mspage{\hand{123}}','The head number 123 is handwritten, with irregular pen-shaped digits.'],
 [r'o\over{b}{b}ject',r'o\over{\unsure{b}}{b}\over{j}{j}ect','The new b covers an uncertain older b-like cell, and j is separately retraced in pen.'],
 [r'E\over{v}{v}ery',r'E\over[typed]{v}{v}ery','The v consists of displaced typewriter impressions with serifs, not a pen letter.'],
 [r'\inserted{sub}',r'\inserted[typed]{sub}','Sub is typed above the line; as a prefix it remains joined to objects.'],
 [r'object\inserted{X}',r'object \inserted[typed]{X}','X is typed interlinearly. Restore the actual separating space after object.'],
 [r'\over{O}{\unsure{0}}',r'\over{O}{\unsure{\O}}','The circle has an added diagonal pen slash. Retain the slashed glyph with doubt about its intended O/zero interpretation.'],
 [r'\unsure{\deleted{set of}|set of}','set of','The line is continuous with the placing hook for corresponding and runs above the body of set of; there is no independent cancellation.'],
 [r'X\inserted{is unique}',r'X \inserted{is unique}','Restore the visible word space before the whole-phrase insertion.'],
 ['The  subobjects',hmarks()+'  subobjects','The h has paired upper and lower pen marks, not an ordinary typed overprint.'],
 [r'\xout{xx(X)}',r'\xout{\illegible{1}(X)}','The old initial symbol is covered by x strikes; the parenthesized X is readable and retained.'],
 [r'\xout{xxxxx}\inserted[typed]{This}',r'\xout{Which}\inserted[typed]{This}','The old Which is recoverable beneath the machine cancellation.'],
 [r'\inserted{in \hand{M}}',r'\inserted[typed]{in \over{M}{M}}','In is typed above the line, while M is pen-retraced over a typed M.'],
 [r'\inserted{all}',r'\inserted[typed]{all}','All is typed interlinearly.'],
 ['d)  The final',r'd)  T\over[typed]{H}{h}e final','The lowercase h is typed over a capital H with upper bars still visible.'],
 ['e\')  The functor',"e')  "+hmarks()+' functor','The final The has the same upper/lower pen marks around h.'],
 ['however is satisfied',r'ho\over{wever}{wever} is satisfied','Wever is retraced in pen over the same typed sequence.'],
 ['product of two O-connected',r'product of tw\over[typed]{p}{o} O-connected','The o is typed over p, whose descender remains visible.'],
 ['jects of M is again',r'ject\over{s}{s} of M is again','The final s of objects is pen-retraced.'],
 ['clearly equivalent',r'clearly equiv\over{\unsure{alen}}{alen}t','The alen letters are pen-retraced; the exact lower typed sequence remains partly obscured.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3779:['slashed O-connected subobjects','The noun is subobjects, not components. The initial round sign is diagonally slashed and retains interpretive doubt.'],
 3781:['corresponding set of subobjects','Set of is live beneath the continuous insertion hook; the premise that it was cancelled is unsupported by the scan.']
 },'unsure':[
 [r'\unsure{\O}','The graphic is a slashed round O-shaped sign; whether it represents a corrected zero remains uncertain.'],
 ['set of','The apparent strike is the continuous placing curve under corresponding, with no separate cancellation through the words.']
 ],'notes':[
 'The penned b covers an uncertain older b-like cell. The adjacent j is also pen-retraced.',
 'Every has a repeated typed v, not handwriting. The final s and period in ones are handwritten at the edge.',
 'The round sign is diagonally slashed; the glyph is retained without forcing the interpretation as digit zero.',
 'Set of remains live: the line belongs to the continuous hook for corresponding.',
 'The comma after exists is corrected to a pen period, and the later that is cancelled.',
 'The The after unique and in e-prime carry upper/lower pen marks. The d-item The has H/h type overprinting. The other The forms retain their visible typed reading.',
 'However has pen-retraced wever; two has typed o over p; objects has a pen-retraced s; equivalent has pen-retraced alen with doubtful lower letters.',
 'The lower-left 35 is handwritten, as is the head number 123. Sub, X, in and all are typed interlinear additions.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_035:unique','before':'uniqqe','after':'unique','line':20,'decision':'master slip variant','reason':'The second q is a clear typed q with a descender. Unique is correctly typed later in the cancelled is necessarily unique and elsewhere in the reviewed section.'}
 ],'evidence':'Both original halves and fifteen enlarged panels inspected. The page number 123 is handwritten. Object has a pen b over a doubtful older cell and a pen-retraced j; Every has repeated type impressions at v. The slashed O-shaped sign retains uncertainty about its intended numeric reading. The long line under corresponding is a placing hook and does not cancel set of. The scan plainly types uniqqe with two q descenders. Sub, X, in and all are typed additions; M in the in M insertion is pen-retraced. The cancelled Which resolves, while the old initial symbol before (X) remains unreadable. The repeated h marks are distinguished from H/h type overprinting. However, objects and equivalent have pen retracing; two has typed o over p. Whole-phrase insertions receive visible spaces, while the sub prefix stays joined.'})
v={'key':key,'before':'uniqqe','after':'unique','kind':'slip corrected','reason':'Isolated q for u, with unique correctly typed later on the same page and elsewhere in the checked section.','source_id':'OBS:ps_134-4_035:unique'}
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());p.write_text(json.dumps([x for x in old if x['source_id']!=v['source_id']]+[v],ensure_ascii=False,indent=2)+'\n')
